# Recursive CTEs in SQL

## Overview

A recursive Common Table Expression (CTE) is a CTE that refers to itself. It is useful for problems where data must be explored or generated repeatedly, such as:

- Employee hierarchies
- Parent-child relationships
- Number sequences
- Date sequences
- Hierarchical paths
- Graph traversal
- Cycle detection

A recursive CTE normally contains two parts:

1. **Anchor member**: defines the starting rows.
2. **Recursive member**: uses the previous result to generate the next rows.

General structure:

```sql
WITH RECURSIVE cte_name AS (
    -- Anchor member
    SELECT ...

    UNION ALL

    -- Recursive member
    SELECT ...
    FROM cte_name
    ...
)
SELECT *
FROM cte_name;
```

---

## 1. Anchor Member

The anchor member defines where recursion starts.

Example:

```sql
SELECT
    employee_id,
    employee_name,
    manager_id
FROM employees
WHERE manager_id IS NULL;
```

For an employee hierarchy, this usually selects the top-level employee, such as the CEO.

The anchor does not always need to select the top-most record. It can start from any selected row or set of rows.

Example:

```sql
WHERE employee_name = 'Manager A'
```

This starts recursion from Manager A and explores only the subtree below Manager A.

---

## 2. Recursive Member

The recursive member refers to the CTE being built.

Example:

```sql
SELECT
    e.employee_id,
    e.employee_name,
    e.manager_id
FROM employees e
JOIN employee_hierarchy h
    ON e.manager_id = h.employee_id;
```

This finds employees whose manager is present in the previous recursive result.

The mental model is:

```text
Anchor
  -> next level
  -> next level
  -> next level
  -> stop
```

---

## 3. Recursive Execution

Consider:

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 5
)
SELECT *
FROM numbers;
```

Execution:

| Current value | Condition | Generated value |
|---|---:|---:|
| 1 | 1 < 5 | 2 |
| 2 | 2 < 5 | 3 |
| 3 | 3 < 5 | 4 |
| 4 | 4 < 5 | 5 |
| 5 | 5 < 5 is false | Nothing |

Result:

```text
1
2
3
4
5
```

### Important boundary rule

The `WHERE` condition is checked on the current input row. It determines whether that row can generate another row.

Therefore:

```sql
WHERE n < 4
```

produces:

```text
1, 2, 3, 4
```

But:

```sql
WHERE n <= 4
```

produces:

```text
1, 2, 3, 4, 5
```

The value `5` is generated from the current value `4`, because `4 <= 4` is true.

---

## 4. Recursion Stopping

Recursion stops when the recursive member returns no new rows.

For a number generator:

```sql
WHERE n < 10
```

For an employee hierarchy, recursion stops when no employees match the manager relationship.

A recursive CTE may also stop because of an explicit depth condition:

```sql
WHERE h.level < 2
```

If the anchor starts at Level 0, the result can contain Levels 0, 1, and 2.

It does not generate Level 3 because a Level 2 row fails the condition.

---

## 5. Level Tracking

A level column records the distance from the starting row.

Example:

```text
CEO          Level 0
Manager A    Level 1
Employee 1   Level 2
Intern 1     Level 3
```

Anchor:

```sql
0 AS level
```

Recursive member:

```sql
h.level + 1 AS level
```

Do not use:

```sql
1 AS level
```

in the recursive member, because every generated row would receive Level 1.

The level is based on the number of relationship steps from the anchor, not on whether the employee is themselves a manager.

---

## 6. Hierarchical Paths

A path preserves the complete chain from the starting row to the current row.

Anchor:

```sql
employee_name AS path
```

Recursive member in PostgreSQL:

```sql
h.path || ' -> ' || e.employee_name AS path
```

Example:

```text
CEO
CEO -> Manager A
CEO -> Manager A -> Employee 1
CEO -> Manager A -> Employee 1 -> Intern 1
```

`h.path` contains the previous path, while `e.employee_name` is the current employee.

If only `e.employee_name` were selected as the path, the earlier hierarchy would be lost.

---

## 7. Starting From a Specific Employee

To explore the subtree below a particular manager, change the anchor.

Example:

```sql
WHERE employee_name = 'Manager A'
```

The result starts with:

```text
Manager A -> Level 0
```

Then recursion finds:

```text
Employee 1 -> Level 1
Employee 2 -> Level 1
Intern 1   -> Level 2
```

The same recursive member can explore different parts of the hierarchy depending on the anchor.

---

## 8. Multiple Starting Rows

The anchor can return multiple rows.

Example:

```sql
SELECT
    employee_id,
    employee_name,
    manager_id,
    0 AS level
FROM employees
WHERE employee_name IN ('Manager A', 'Manager B');
```

Both managers become independent starting points.

The recursive member explores the children of both branches.

Example result:

| employee_name | level |
|---|---:|
| Manager A | 0 |
| Manager B | 0 |
| Employee 1 | 1 |
| Employee 2 | 1 |

The total number of rows is the number of anchor rows plus all rows generated from each branch.

---

## 9. Number Generation

A recursive CTE can generate a sequence of numbers.

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

This produces values from 5 through 20.

### Even numbers

```sql
WITH RECURSIVE numbers AS (
    SELECT 2 AS n

    UNION ALL

    SELECT n + 2
    FROM numbers
    WHERE n < 20
)
SELECT *
FROM numbers;
```

This produces:

```text
2, 4, 6, 8, 10, 12, 14, 16, 18, 20
```

The increment is controlled by the recursive expression.

---

## 10. Date Generation

The same pattern can generate dates.

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

This produces every date from September 1 through September 7, 2026.

Date arithmetic differs between database systems, so syntax may need to be adapted for MySQL, SQL Server, Oracle, or other databases.

---

## 11. Cycle Detection

A cycle occurs when recursion reaches a row that was already visited.

Example:

```text
A -> B -> C -> A -> B -> C -> ...
```

Without protection, recursion may continue indefinitely or hit the database's recursion limit.

In PostgreSQL, one approach is to maintain an array of visited IDs.

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

This prevents a row from being added if its ID already exists in the current path.

Example:

| Employee | Visited IDs |
|---|---|
| A | `{1}` |
| B | `{1,2}` |
| C | `{1,2,3}` |
| A again | Blocked |

Cycle detection is database-specific. PostgreSQL arrays are one solution; other systems may use strings, JSON, path columns, or built-in cycle features.

---

## 12. Complete Hierarchy Query

PostgreSQL example combining:

- Anchor
- Recursive member
- Level tracking
- Path tracking
- Visited IDs
- Cycle protection

```sql
WITH RECURSIVE employee_hierarchy AS (

    -- Anchor member
    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level,
        employee_name AS path,
        ARRAY[employee_id] AS visited_ids
    FROM employees
    WHERE employee_id = 1

    UNION ALL

    -- Recursive member
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        h.level + 1 AS level,
        h.path || ' -> ' || e.employee_name AS path,
        h.visited_ids || e.employee_id AS visited_ids
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
    WHERE NOT e.employee_id = ANY(h.visited_ids)
)

SELECT
    employee_id,
    employee_name,
    level,
    path
FROM employee_hierarchy;
```

---

## 13. Core Mental Model

Always ask:

1. Where does recursion start?
2. What does one recursive step do?
3. What column connects the current row to the next row?
4. How is the level updated?
5. How is the path updated?
6. What condition stops recursion?
7. Can the data contain cycles?
8. If cycles exist, how are visited rows tracked?

---

## 14. Common Mistakes

### Mistake 1: Forgetting the recursive reference

The recursive member must refer to the CTE.

### Mistake 2: Missing a comma

```sql
e.manager_id
h.level + 1
```

should be:

```sql
e.manager_id,
h.level + 1
```

### Mistake 3: Resetting the level

```sql
1 AS level
```

resets every generated row to Level 1.

Use:

```sql
h.level + 1
```

### Mistake 4: Losing the path

```sql
e.employee_name AS path
```

loses all previous hierarchy information.

Use:

```sql
h.path || ' -> ' || e.employee_name
```

### Mistake 5: Filtering the wrong stage

If the requirement is to start from Manager A, change the anchor. Filtering only the recursive member does not change the starting point.

### Mistake 6: Ignoring cycles

Parent-child data may contain bad or cyclic relationships. Add cycle protection when necessary.

---

## 15. Topic Completion Checklist

- [x] Anchor member
- [x] Recursive member
- [x] Recursive execution
- [x] Stopping conditions
- [x] Boundary behavior of `<` and `<=`
- [x] Level tracking
- [x] Hierarchical paths
- [x] Starting from a specific employee
- [x] Multiple starting rows
- [x] Number generation
- [x] Date generation
- [x] Cycle detection
- [x] Complete hierarchy query
