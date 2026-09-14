# Recursive CTE Interview Questions

## 1. What is a recursive CTE?

A recursive CTE is a Common Table Expression that refers to itself. It is used to repeatedly generate or traverse data.

Common use cases include:

- Employee hierarchies
- Parent-child data
- Number sequences
- Date sequences
- Graph traversal

---

## 2. What are the two parts of a recursive CTE?

A recursive CTE has:

1. **Anchor member**: defines the starting rows.
2. **Recursive member**: refers to the CTE and generates the next rows.

Example:

```sql
WITH RECURSIVE numbers AS (
    SELECT 1

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT *
FROM numbers;
```

---

## 3. What is the purpose of the anchor member?

The anchor defines where recursion starts.

It may return:

- One row
- Multiple rows
- A top-level employee
- A selected manager
- An initial number
- An initial date

The anchor does not always have to be the top-most record in a hierarchy.

---

## 4. What does the recursive member do?

The recursive member uses rows already produced by the CTE to generate the next level or next iteration.

In an employee hierarchy, it joins employees to the previous level's employee IDs.

---

## 5. When does recursion stop?

Recursion stops when the recursive member returns no new rows.

It can also stop because of:

- A depth condition
- A date boundary
- A number boundary
- Cycle protection
- A database recursion limit

---

## 6. Explain the difference between `<` and `<=` in a recursive CTE.

Example:

```sql
WHERE n < 4
```

Starting from 1 produces:

```text
1, 2, 3, 4
```

Example:

```sql
WHERE n <= 4
```

Starting from 1 produces:

```text
1, 2, 3, 4, 5
```

The condition is evaluated on the current input row. If the current row passes, the recursive expression can generate the next row.

---

## 7. How do you track hierarchy depth?

Initialize the anchor with:

```sql
0 AS level
```

Then increment in the recursive member:

```sql
h.level + 1 AS level
```

Using `1 AS level` in the recursive member would assign Level 1 to every generated row.

---

## 8. How do you build a hierarchy path?

Use the previous path plus the current employee.

PostgreSQL example:

```sql
h.path || ' -> ' || e.employee_name AS path
```

The anchor initializes the path:

```sql
employee_name AS path
```

---

## 9. How do you start recursion from a specific employee?

Change the anchor filter.

Example:

```sql
WHERE employee_name = 'Manager A'
```

This starts at Manager A with Level 0 and explores only the subtree below that employee.

---

## 10. Can the anchor return multiple rows?

Yes.

Example:

```sql
WHERE employee_name IN ('Manager A', 'Manager B')
```

Both rows become starting points, and the recursive member explores both branches.

---

## 11. What is the difference between filtering the anchor and filtering the recursive member?

Filtering the anchor changes where recursion starts.

Filtering the recursive member changes which next-level rows are generated.

If the requirement is "start from Manager A," filter the anchor. Filtering only the recursive member does not change the starting point.

---

## 12. How can a recursive CTE generate numbers?

Use an anchor for the first number and a recursive expression for the increment.

```sql
WITH RECURSIVE numbers AS (
    SELECT 5 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 20
)
SELECT *
FROM numbers;
```

---

## 13. How can a recursive CTE generate dates?

Use an anchor for the first date and add an interval in the recursive member.

PostgreSQL example:

```sql
WITH RECURSIVE dates AS (
    SELECT DATE '2026-09-01' AS dt

    UNION ALL

    SELECT dt + INTERVAL '1 day'
    FROM dates
    WHERE dt < DATE '2026-09-07'
)
SELECT *
FROM dates;
```

---

## 14. What is a cycle?

A cycle occurs when recursion reaches a row that was already visited.

Example:

```text
A -> B -> C -> A
```

Without cycle protection, recursion can continue indefinitely or hit a recursion limit.

---

## 15. How do you prevent cycles in PostgreSQL?

Track visited IDs in an array.

Anchor:

```sql
ARRAY[employee_id] AS visited_ids
```

Recursive member:

```sql
h.visited_ids || e.employee_id AS visited_ids
```

Cycle check:

```sql
WHERE NOT e.employee_id = ANY(h.visited_ids)
```

This prevents an already visited employee from being added again in the current path.

---

## 16. Is cycle detection syntax identical in every database?

No.

The concept is portable, but implementation differs.

Possible techniques include:

- PostgreSQL arrays
- String-based visited paths
- JSON arrays
- Database-specific cycle clauses
- Explicit recursion limits

---

## 17. Why is `UNION ALL` commonly used?

`UNION ALL` preserves all generated rows and avoids the duplicate-elimination work performed by `UNION`.

In recursive CTEs, it is commonly used because each generated row represents a meaningful iteration or path.

Cycle protection should be handled explicitly when needed.

---

## 18. What happens if the anchor returns no rows?

The recursive member has no starting rows to work with, so it produces no rows.

The final result is empty.

---

## 19. What happens if the recursive member generates no rows?

The current recursion terminates, and the final result contains the rows generated up to that point.

---

## 20. What is the difference between hierarchy level and manager status?

Level is the number of steps from the anchor.

An employee can be a manager and still be Level 1, Level 2, or any other level.

Level is not determined by whether the employee appears in another row's `manager_id`.

---

## 21. How do you limit recursion to Level 2?

Use:

```sql
WHERE h.level < 2
```

If the anchor is Level 0, the final result includes Levels 0, 1, and 2.

---

## 22. What are common recursive CTE mistakes?

- Missing `WITH RECURSIVE`
- Forgetting the self-reference to the CTE
- Missing commas between selected columns
- Resetting level to 1 instead of incrementing it
- Losing the previous path
- Filtering the wrong part of the query
- Forgetting a stopping condition
- Ignoring cycles
- Assuming PostgreSQL syntax works unchanged in every database

---

## 23. Explain the execution of this query.

```sql
WITH RECURSIVE numbers AS (
    SELECT 2 AS n

    UNION ALL

    SELECT n * 2
    FROM numbers
    WHERE n < 20
)
SELECT *
FROM numbers;
```

Answer:

```text
2
4
8
16
32
```

The row `32` is included because it is generated from `16`, and `16 < 20` is true. The next iteration checks `32 < 20`, which is false.

---

## 24. Write a recursive CTE for an employee hierarchy.

Expected solution pattern:

```sql
WITH RECURSIVE employee_hierarchy AS (

    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        h.level + 1
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
)
SELECT *
FROM employee_hierarchy;
```

---

## 25. What is the most important mental model?

Always identify:

1. Starting rows.
2. One recursive step.
3. The relationship between current and next rows.
4. The level calculation.
5. The path calculation.
6. The stopping condition.
7. The cycle protection strategy.
