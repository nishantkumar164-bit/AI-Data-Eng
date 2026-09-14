# SQL Exercises — Aggregation, Grain & Safe Joins

Do not look at the examples file while solving these.

The objective is to practice **reasoning about grain**, not just SQL syntax.

---

## Setup

Use these tables:

### customers

| customer_id | name |
|---:|---|
| 1 | Amit |
| 2 | Ravi |
| 3 | Neha |
| 4 | Pooja |

### orders

| order_id | customer_id | amount |
|---:|---:|---:|
| 101 | 1 | 500 |
| 102 | 1 | 300 |
| 103 | 2 | 700 |
| 104 | 1 | 200 |
| 105 | 3 | 400 |

### order_items

| order_item_id | order_id | product | quantity |
|---:|---:|---|---:|
| 1 | 101 | Shampoo | 2 |
| 2 | 101 | Oil | 3 |
| 3 | 102 | Face Wash | 1 |
| 4 | 103 | Shampoo | 2 |
| 5 | 104 | Oil | 4 |
| 6 | 104 | Shampoo | 1 |
| 7 | 105 | Face Wash | 2 |

---

# Exercise 1 — Basic Aggregation

Find the total amount spent by each customer.

Requirements:

- Output `customer_id`
- Output `total_amount`
- Use `GROUP BY`

Before writing the query, state:

**What is the grain of the result?**

---

# Exercise 2 — CTE

Rewrite Exercise 1 using a CTE.

The CTE should contain:

```text
customer_id
total_amount
```

The outer query should return the CTE result.

---

# Exercise 3 — Customer Details

Return:

- customer ID
- customer name
- total amount

Every customer must appear, including customers who have never placed an order.

Hint:

Think carefully about which table should be on the left side of the join.

---

# Exercise 4 — COALESCE

Modify Exercise 3 so that a customer with no orders gets:

```text
0
```

instead of:

```text
NULL
```

Explain why `NULL` appears before applying `COALESCE()`.

---

# Exercise 5 — Two Metrics

Return:

- customer ID
- customer name
- total amount
- number of orders

Requirements:

- Use a CTE.
- Calculate `SUM(amount)` inside the CTE.
- Calculate `COUNT(order_id)` inside the CTE.
- Preserve customers with no orders.
- Return `0` for missing totals/counts.

Before writing SQL:

**Why can SUM and COUNT be calculated in the same CTE?**

---

# Exercise 6 — Identify the Grain

For each table/result below, identify the grain.

1. `customers`
2. `orders`
3. `order_items`
4. `GROUP BY customer_id` on `orders`
5. `GROUP BY order_id` on `order_items`
6. A result after joining `orders` to `order_items`

Do not just say "customer" or "order".

Write:

```text
1 row = __________________
```

---

# Exercise 7 — Find the Bug

Consider:

```sql
SELECT
    o.customer_id,
    SUM(o.amount) AS total_amount,
    SUM(oi.quantity) AS total_quantity
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY o.customer_id;
```

Question:

Is this query safe?

If not:

1. Which metric can become incorrect?
2. Why?
3. Which table has the finer grain?
4. What should be done before calculating the affected metric?

---

# Exercise 8 — Separate CTEs

Build a query that returns:

- customer ID
- customer name
- number of orders
- total order amount
- total item quantity

Use:

```text
CTE 1 → order-related metrics
CTE 2 → item-related metrics
```

Important:

Each CTE should finish at:

```text
1 row = 1 customer
```

Then join both CTEs to `customers`.

---

# Exercise 9 — Reason Before Coding

Suppose:

```text
Customer 1
    ↓
2 orders
    ↓
Order 101 → 3 items
Order 102 → 2 items
```

After joining `orders` and `order_items`, how many rows will customer 1 contribute?

Do not calculate from the total number of items alone.

Explain your reasoning using **row multiplication**.

---

# Exercise 10 — Interview Question

Answer this in your own words:

> "Why should you sometimes aggregate data before joining tables?"

Your answer should mention:

- grain
- one-to-many relationships
- row multiplication
- incorrect aggregates

---

# Challenge — Data Engineering Thinking

You are given:

```text
customers
orders
order_items
products
```

The business asks:

> "Give me one row per customer containing total revenue, order count, total quantity purchased, number of unique products purchased, and customer name."

Before writing SQL, design the query on paper.

Answer:

1. What is the grain of each source table?
2. Which metrics come from `orders`?
3. Which metrics come from `order_items`?
4. Would you use one CTE or multiple CTEs?
5. What grain should each CTE produce?
6. What should the final result's grain be?
7. Where might row multiplication occur?
8. Where might `COALESCE()` be required?

Only after answering these questions should you write the SQL.

---

# Revision Rule

For every future SQL problem involving joins and aggregates, pause and ask:

```text
What is my grain?
        ↓
What is the grain of each table?
        ↓
Will this join multiply rows?
        ↓
Where should aggregation happen?
        ↓
Are my CTEs at compatible grains?
        ↓
Do I need COALESCE?
```

Master this thought process and many advanced SQL problems become much easier.
