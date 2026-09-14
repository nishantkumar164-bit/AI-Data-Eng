# SQL Learning — Aggregation, Grain & Safe Joins

This repository contains the SQL concepts covered so far in the learning roadmap.

## Topics Covered

- `GROUP BY`
- Aggregate functions: `SUM()`, `COUNT()`
- Common Table Expressions (CTEs)
- Table grain
- Aggregating before joining
- One-to-many relationships
- Join multiplication / double counting
- `LEFT JOIN`
- `COALESCE()`
- Separating metrics into multiple CTEs
- Joining CTEs at a common grain

---

## 1. The Most Important Concept: Grain

**Grain means what one row represents in a table or result set.**

Example:

```text
customers   → 1 row = 1 customer
orders      → 1 row = 1 order
order_items → 1 row = 1 item within an order
```

Before writing an aggregation or join, always ask:

> What does one row represent here?

This prevents many SQL errors, especially incorrect totals after joins.

---

## 2. Basic Aggregation

Suppose `orders` contains:

```text
order_id | customer_id | amount
---------+-------------+-------
101      | 1           | 500
102      | 1           | 300
103      | 2           | 700
104      | 1           | 200
105      | 3           | 400
```

To calculate total spending per customer:

```sql
SELECT
    customer_id,
    SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;
```

The result has:

```text
1 row = 1 customer
```

So the query has changed the grain from **order grain** to **customer grain**.

---

## 3. CTEs

A CTE lets us create an intermediate result that can be referenced by the following query.

```sql
WITH customer_summary AS (
    SELECT
        customer_id,
        SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_summary;
```

A useful mental model:

```text
Source table
    ↓
CTE transformation
    ↓
Intermediate result
    ↓
Final query
```

CTEs are especially useful when we want to isolate an aggregation before joining it to other data.

---

## 4. LEFT JOIN + COALESCE

Suppose there is a customer who has never placed an order.

The customer will not exist in the aggregated `orders` CTE.

But if we start from `customers` and use a `LEFT JOIN`, the customer remains in the final result:

```sql
WITH customer_summary AS (
    SELECT
        customer_id,
        SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.name,
    COALESCE(cs.total_amount, 0) AS total_amount
FROM customers c
LEFT JOIN customer_summary cs
    ON c.customer_id = cs.customer_id;
```

`COALESCE()` replaces `NULL` with the specified fallback value.

```sql
COALESCE(cs.total_amount, 0)
```

means:

```text
if total_amount is NULL → return 0
otherwise                → return total_amount
```

Important:

> Do not memorize that `COALESCE()` must always be outside a CTE. It can be used anywhere it is useful. In this example, the `NULL` is created by the `LEFT JOIN`, so using it in the final `SELECT` is natural.

---

## 5. Multiple Metrics at the Same Grain

If we need:

- total amount
- number of orders

both metrics come from `orders` and both are required at **customer grain**.

Therefore they can be calculated together:

```sql
WITH customer_summary AS (
    SELECT
        customer_id,
        SUM(amount) AS total_amount,
        COUNT(order_id) AS order_count
    FROM orders
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.name,
    COALESCE(cs.total_amount, 0) AS total_amount,
    COALESCE(cs.order_count, 0) AS order_count
FROM customers c
LEFT JOIN customer_summary cs
    ON c.customer_id = cs.customer_id;
```

The CTE produces:

```text
1 row = 1 customer
```

---

## 6. Why Joining Different Grains Can Cause Wrong Results

Relationship:

```text
customers
    |
    | 1-to-many
    ↓
orders
    |
    | 1-to-many
    ↓
order_items
```

Example:

### orders

```text
order_id | customer_id | amount
---------+-------------+-------
101      | 1           | 500
```

### order_items

```text
order_id | item       | quantity
---------+------------+---------
101      | Shampoo    | 2
101      | Oil        | 3
101      | Face Wash  | 1
```

After joining:

```text
order_id | amount | item       | quantity
---------+--------+------------+---------
101      | 500    | Shampoo    | 2
101      | 500    | Oil        | 3
101      | 500    | Face Wash  | 1
```

Now:

```sql
SUM(amount)
```

becomes:

```text
500 + 500 + 500 = 1500
```

which is incorrect.

But:

```sql
SUM(quantity)
```

becomes:

```text
2 + 3 + 1 = 6
```

which is correct.

### Key lesson

A join can multiply rows.

Therefore:

> **Never aggregate blindly after joining one-to-many tables.**

First determine the grain required for each metric.

---

## 7. Separate CTEs for Different Metric Sources

Suppose we need:

- customer name
- total order amount
- number of orders
- total quantity of items purchased

A safe design is:

```sql
WITH order_summary AS (
    SELECT
        customer_id,
        COUNT(order_id) AS order_count,
        SUM(amount) AS total_order_amount
    FROM orders
    GROUP BY customer_id
),

item_summary AS (
    SELECT
        o.customer_id,
        SUM(oi.quantity) AS total_quantity
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY o.customer_id
)

SELECT
    c.customer_id,
    c.name,
    COALESCE(os.order_count, 0) AS order_count,
    COALESCE(os.total_order_amount, 0) AS total_order_amount,
    COALESCE(isum.total_quantity, 0) AS total_quantity
FROM customers c
LEFT JOIN order_summary os
    ON c.customer_id = os.customer_id
LEFT JOIN item_summary isum
    ON c.customer_id = isum.customer_id;
```

Notice that both CTEs end at the same grain:

```text
order_summary → 1 row per customer
item_summary  → 1 row per customer

             ↓

final result  → 1 row per customer
```

This makes the final joins much safer.

---

## 8. The Rule to Remember

Before writing SQL, ask these questions:

1. **What is the grain of each table?**
2. **What is the grain of my desired result?**
3. **Which table contains the metric I need?**
4. **Will a join multiply rows?**
5. **Should I aggregate before joining?**
6. **Do multiple metrics belong to the same grain?**
7. **Should missing values become `0` using `COALESCE()`?**

### Core mental model

```text
Understand grain
      ↓
Identify metric source
      ↓
Aggregate at required grain
      ↓
Join compatible grains
      ↓
Handle NULLs
      ↓
Return final result
```

---

## 9. Common Mistakes

### Mistake 1 — Aggregating after a row-multiplying join

```sql
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
```

and then:

```sql
SUM(o.amount)
```

This can double-count or triple-count order amounts.

### Mistake 2 — Ignoring table grain

Knowing column names is not enough. Understand what one row represents.

### Mistake 3 — Putting unrelated metrics into one aggregation

If metrics come from different grains, separate the transformations.

### Mistake 4 — Forgetting `LEFT JOIN`

If the requirement is "show every customer, including customers with no orders", start from `customers` and use `LEFT JOIN`.

### Mistake 5 — Forgetting NULL handling

A missing matching row often produces `NULL`, not `0`.

Use:

```sql
COALESCE(value, 0)
```

when zero is the appropriate business meaning.

---

## 10. Interview-Level Takeaway

A strong SQL developer should be able to explain:

> "I aggregate each metric at its appropriate grain before joining. This prevents row multiplication from causing incorrect aggregates. If metrics originate from different grains, I use separate CTEs and bring them to a common grain before combining them."

This is more important than simply memorizing SQL syntax.

---

## Revision Checklist

- [ ] I can explain table grain.
- [ ] I can use `GROUP BY` with `SUM()` and `COUNT()`.
- [ ] I understand what a CTE represents.
- [ ] I understand why aggregation before joining can be necessary.
- [ ] I can identify one-to-many relationships.
- [ ] I understand join multiplication.
- [ ] I know why `SUM(order_amount)` can become incorrect after joining order items.
- [ ] I can use `LEFT JOIN` to preserve customers without orders.
- [ ] I understand when and why to use `COALESCE()`.
- [ ] I can create separate CTEs for metrics from different grains.
- [ ] I can bring separate CTEs to a common grain before joining.
