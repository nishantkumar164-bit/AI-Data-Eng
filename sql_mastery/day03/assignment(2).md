# Recursive CTE Assignments

Use PostgreSQL syntax unless a question says otherwise.

## Sample Tables

### employees

| employee_id | employee_name | manager_id |
|---:|---|---:|
| 1 | CEO | NULL |
| 2 | Manager A | 1 |
| 3 | Manager B | 1 |
| 4 | Employee 1 | 2 |
| 5 | Employee 2 | 2 |
| 6 | Employee 3 | 3 |
| 7 | Intern 1 | 4 |

---

## Assignment 1: Basic Number Sequence

Generate numbers from 1 to 15 using a recursive CTE.

Requirements:

- Start at 1.
- Add 1 in every recursive step.
- Include 15.

---

## Assignment 2: Descending Sequence

Generate numbers from 10 down to 1.

Requirements:

- Anchor starts at 10.
- Recursive member subtracts 1.
- Stop after generating 1.

---

## Assignment 3: Odd Numbers

Generate odd numbers from 1 to 19.

Expected output:

```text
1, 3, 5, 7, 9, 11, 13, 15, 17, 19
```

---

## Assignment 4: Date Sequence

Generate every date from:

```text
2026-09-01
```

through:

```text
2026-09-10
```

Include both boundary dates.

---

## Assignment 5: Basic Employee Hierarchy

Starting from the CEO, return:

- employee_id
- employee_name
- manager_id
- level

The CEO must be Level 0.

---

## Assignment 6: Hierarchy Path

Starting from the CEO, return:

- employee_name
- level
- path

Expected path format:

```text
CEO -> Manager A -> Employee 1
```

---

## Assignment 7: Specific Subtree

Start recursion from Manager A.

Return all employees under Manager A, including indirect reports.

Expected employees:

```text
Manager A
Employee 1
Employee 2
Intern 1
```

---

## Assignment 8: Multiple Anchors

Start recursion from both Manager A and Manager B.

Return:

- employee_name
- level
- path

Both managers should have Level 0.

---

## Assignment 9: Limit Depth

Starting from the CEO, return only Levels 0, 1, and 2.

Do not generate Level 3.

---

## Assignment 10: Cycle Detection

Create a test table with this relationship:

```text
A -> B
B -> C
C -> A
```

Write a PostgreSQL recursive CTE that:

- Starts from A.
- Tracks visited IDs.
- Prevents revisiting a node.
- Returns the visited path.

---

## Assignment 11: Combined Challenge

Write one recursive CTE that:

- Starts from employee_id = 1.
- Returns employee_id.
- Returns employee_name.
- Returns manager_id.
- Tracks level.
- Builds a path.
- Tracks visited IDs.
- Prevents cycles.
- Limits recursion to Level 3.

---

## Assignment 12: Reasoning Questions

For each query, predict the output before running it.

### A

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

### B

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n <= 4
)
SELECT *
FROM numbers;
```

### C

```sql
WITH RECURSIVE numbers AS (
    SELECT 5 AS n

    UNION ALL

    SELECT n + 2
    FROM numbers
    WHERE n < 15
)
SELECT *
FROM numbers;
```

For each query, explain:

1. The anchor output.
2. Each recursive step.
3. The final output.
4. Why recursion stops.
