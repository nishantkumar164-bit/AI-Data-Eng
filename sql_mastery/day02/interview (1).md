# SQL Interview Revision

## Joins

### 1. What is the difference between INNER JOIN and LEFT JOIN?
`INNER JOIN` returns only matching rows. `LEFT JOIN` returns every left-table row and NULLs for unmatched right-table columns.

### 2. What is join grain?
Join grain is the level represented by one row in the result. Joining an order table to an order-item table usually changes the grain from order to order-item.

### 3. Why can joins inflate totals?
A one-to-many join repeats the one-side values for every matching many-side row. Summing the repeated value can overstate the metric.

### 4. How do you prevent inflated order totals?
Aggregate the detail table to order grain first, then join it to the orders table.

### 5. Do NULL keys match in SQL joins?
Not with normal equality. `NULL = NULL` evaluates to UNKNOWN, not TRUE.

### 6. How do you calculate join row counts?
For each join key, multiply the number of matching rows on each side. Add unmatched rows according to the join type.

### 7. Does MySQL support FULL OUTER JOIN?
MySQL does not provide direct FULL OUTER JOIN syntax. It can be approximated with a UNION of LEFT JOIN and unmatched RIGHT JOIN results.

### 8. What is the difference between ROW_NUMBER, RANK, and DENSE_RANK?
- `ROW_NUMBER`: unique sequence, even for ties.
- `RANK`: ties share rank and create gaps.
- `DENSE_RANK`: ties share rank without gaps.

### 9. Why can’t a window-function alias normally be used in WHERE?
WHERE is evaluated before the window function. Use a CTE or subquery and filter outside it.

### 10. What is the difference between a CTE and a subquery?
Both can structure a query. CTEs improve readability and support multiple named stages; a subquery is useful for a small one-off transformation. Performance depends on the database optimizer.

### 11. What does LAG do?
`LAG` returns a value from a previous row within the window ordering.

### 12. What does LEAD do?
`LEAD` returns a value from a following row within the window ordering.
