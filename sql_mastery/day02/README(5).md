# SQL Mastery Repository

Covered: SQL Execution Order, Joins, Window Functions, and CTEs.

## Joins
INNER, LEFT, RIGHT, FULL OUTER, CROSS, and SELF JOIN; grain; one-to-many row multiplication; NULL join behavior; join row counts; aggregating detail rows before joining to avoid inflated measures.

## Window Functions
GROUP BY collapses rows; windows preserve rows. Covered SUM/AVG OVER, running totals, ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, frames, top-N, and filtering window results through CTEs/subqueries.

## CTEs
A CTE is a temporary named result set for one SQL statement. Multiple CTEs are separated by commas, and later CTEs may reference earlier CTEs.

```sql
WITH customer_totals AS (
    SELECT customer_id, SUM(order_amount) AS total_amount
    FROM orders GROUP BY customer_id
), customer_order_counts AS (
    SELECT customer_id, COUNT(*) AS order_count
    FROM orders GROUP BY customer_id
)
SELECT t.customer_id, t.total_amount, c.order_count
FROM customer_totals t
JOIN customer_order_counts c ON t.customer_id = c.customer_id
WHERE t.total_amount > 5000 AND c.order_count >= 3;
```

Common mistakes: missing commas, GROUP BY, aliases, using `&` instead of `AND`, wrong table names, and ignoring grain changes.

Next topic: Recursive CTEs.
