# SQL Interview Notes

## 1. What is the difference between GROUP BY and a window function?

`GROUP BY` reduces multiple rows into one row per group. A window function calculates across a set of related rows but preserves the original rows.

```sql
SELECT
    customer_id,
    SUM(order_amount) AS total_amount
FROM orders
GROUP BY customer_id;
```

```sql
SELECT
    order_id,
    customer_id,
    order_amount,
    SUM(order_amount) OVER (
        PARTITION BY customer_id
    ) AS customer_total
FROM orders;
```

## 2. What does PARTITION BY do?

It divides rows into independent groups for the window calculation. The calculation restarts for every partition.

## 3. How do you calculate a running total?

```sql
SUM(order_amount) OVER (
    PARTITION BY customer_id
    ORDER BY order_id
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

## 4. Difference between ROW_NUMBER, RANK, and DENSE_RANK

For values `100, 90, 90, 80`:

- `ROW_NUMBER()`: `1, 2, 3, 4`
- `RANK()`: `1, 2, 2, 4`
- `DENSE_RANK()`: `1, 2, 2, 3`

Use `ROW_NUMBER()` when every row needs a unique position. Use `DENSE_RANK()` when ties should be included and ranks should not have gaps.

## 5. How do you get the highest-paid employee in each department?

```sql
WITH ranked_employees AS (
    SELECT
        employee_id,
        department,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
)
SELECT
    employee_id,
    department,
    salary
FROM ranked_employees
WHERE salary_rank = 1;
```

This returns all employees tied for the highest salary.

## 6. How do you get exactly one employee per department?

Use `ROW_NUMBER()`:

```sql
WITH ranked_employees AS (
    SELECT
        employee_id,
        department,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY department
            ORDER BY salary DESC, employee_id
        ) AS row_num
    FROM employees
)
SELECT
    employee_id,
    department,
    salary
FROM ranked_employees
WHERE row_num = 1;
```

The additional `employee_id` ordering makes the tie-breaking deterministic.

## 7. How do you get the previous order amount?

```sql
LAG(order_amount) OVER (
    PARTITION BY customer_id
    ORDER BY order_id
)
```

## 8. How do you get the next order amount?

```sql
LEAD(order_amount) OVER (
    PARTITION BY customer_id
    ORDER BY order_id
)
```

## 9. What is the difference between LAG(column) and LAG(column, offset, default)?

```sql
LAG(order_amount)
```

means one row backward, with `NULL` if no previous row exists.

```sql
LAG(order_amount, 2, 0)
```

means two rows backward, returning `0` if that row does not exist.

The first argument is a column, not a table.

## 10. Why can’t a window-function alias usually be used in WHERE?

Window functions are evaluated after `WHERE`. Use a CTE or subquery:

```sql
WITH ranked AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_id
        ) AS row_num
    FROM orders
)
SELECT *
FROM ranked
WHERE row_num = 1;
```

Some databases support `QUALIFY`, but it is not universally supported.

## 11. CTE versus subquery

Neither is automatically faster. Modern optimizers may produce the same execution plan.

Use a CTE when:

- The query has multiple logical stages
- Readability matters
- An intermediate result has a meaningful name
- The result is reused

Use a subquery for a small, one-off transformation.

For performance-sensitive SQL, inspect the execution plan.

## 12. What is a window frame?

A window frame defines the exact rows included in a window calculation.

```sql
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

means all rows from the beginning of the partition through the current row.

## 13. What happens when ORDER BY is omitted?

For aggregate window functions, the calculation generally covers the whole partition. For ranking, lag, and lead functions, an ordering is required to define row positions.

## 14. Common production mistakes

- Partitioning by a unique identifier instead of the intended grouping column
- Using ascending order when the highest value should rank first
- Ignoring ties
- Assuming `RANK()` and `DENSE_RANK()` behave identically
- Filtering a window-function alias in the same query block
- Ignoring `NULL` behavior
- Forgetting that joins can multiply rows before window calculations
- Assuming CTEs are always faster
- Using nondeterministic ordering when ties exist
