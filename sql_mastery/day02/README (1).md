# SQL Mastery Repository

## Learning Progress

1. SQL Execution Order — completed
2. Joins — completed
3. Window Functions — completed
4. CTE — next formal topic
5. Recursive CTE
6. Views
7. Indexing
8. Transactions
9. ACID
10. Query Optimization
11. Partitioning
12. Slowly Changing Dimensions
13. Change Data Capture
14. Warehouse Design
15. Analytics Data Warehouse Project

## Joins

### Join Types
- INNER JOIN: returns matching rows from both tables.
- LEFT JOIN: keeps every row from the left table.
- RIGHT JOIN: keeps every row from the right table.
- FULL OUTER JOIN: keeps matched and unmatched rows from both tables.
- CROSS JOIN: Cartesian product.
- SELF JOIN: a table joined to itself.

### Grain
Always identify the grain of each table before joining.

Examples:
- `orders`: one row per order
- `order_items`: one row per order item
- `products`: one row per product

Joining `orders` to `order_items` changes the result grain to one row per order item.

### One-to-Many and Row Multiplication
If a key appears twice in the left table and twice in the right table, the join can produce four rows for that key.

For example:

```text
A = [1, 1, 3, 4]
B = [1, 1, 2, 3]
```

- INNER JOIN = 5 rows
- LEFT JOIN = 6 rows
- RIGHT JOIN = 6 rows
- FULL OUTER JOIN = 7 rows

### NULL Behavior
`NULL = NULL` is not true in SQL. Therefore, two NULL join keys do not match with:

```sql
ON a.id = b.id
```

### Aggregating Before Joining
Do not join detail-level rows to order-level rows and then blindly sum order-level measures. Aggregate the detail table first when necessary.

## Window Functions

Window functions preserve row-level detail while calculating across related rows.

Covered:
- `SUM() OVER`
- `AVG() OVER`
- running totals
- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- `LAG()`
- `LEAD()`
- window frames
- top-N per group
- first row per group
- filtering window results with CTEs/subqueries

## Core Mental Models

- GROUP BY collapses rows; window functions preserve rows.
- JOINs can change grain.
- Always validate row counts after joins.
- Aggregate before joining when the required metric is at a higher grain.
- Window functions are evaluated after WHERE, so filter their results in a CTE or subquery.
