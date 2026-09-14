-- Recursive CTE Examples
-- PostgreSQL syntax

-- ============================================================
-- 1. Basic number generation: 1 to 10
-- ============================================================

WITH RECURSIVE numbers AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT *
FROM numbers;


-- ============================================================
-- 2. Number generation: 5 to 20
-- ============================================================

WITH RECURSIVE numbers AS (
    SELECT 5 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 20
)
SELECT *
FROM numbers;


-- ============================================================
-- 3. Even numbers: 2 to 20
-- ============================================================

WITH RECURSIVE numbers AS (
    SELECT 2 AS n

    UNION ALL

    SELECT n + 2
    FROM numbers
    WHERE n < 20
)
SELECT *
FROM numbers;


-- ============================================================
-- 4. Multiplication sequence
-- ============================================================

WITH RECURSIVE numbers AS (
    SELECT 2 AS n

    UNION ALL

    SELECT n * 2
    FROM numbers
    WHERE n < 20
)
SELECT *
FROM numbers;


-- ============================================================
-- 5. Date generation
-- ============================================================

WITH RECURSIVE dates AS (
    SELECT DATE '2026-09-01' AS dt

    UNION ALL

    SELECT dt + INTERVAL '1 day'
    FROM dates
    WHERE dt < DATE '2026-09-07'
)
SELECT *
FROM dates;


-- ============================================================
-- 6. Basic employee hierarchy
-- Assumes:
-- employees(employee_id, employee_name, manager_id)
-- ============================================================

WITH RECURSIVE employee_hierarchy AS (

    -- Anchor member
    SELECT
        employee_id,
        employee_name,
        manager_id
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive member
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
)
SELECT *
FROM employee_hierarchy;


-- ============================================================
-- 7. Employee hierarchy with level
-- ============================================================

WITH RECURSIVE employee_hierarchy AS (

    -- Anchor member
    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive member
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        h.level + 1 AS level
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
)
SELECT *
FROM employee_hierarchy;


-- ============================================================
-- 8. Employee hierarchy with path
-- PostgreSQL string concatenation uses ||
-- ============================================================

WITH RECURSIVE employee_hierarchy AS (

    -- Anchor member
    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level,
        employee_name AS path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive member
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        h.level + 1 AS level,
        h.path || ' -> ' || e.employee_name AS path
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
)
SELECT
    employee_name,
    level,
    path
FROM employee_hierarchy;


-- ============================================================
-- 9. Start from a specific manager
-- ============================================================

WITH RECURSIVE employee_hierarchy AS (

    -- Anchor member
    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level,
        employee_name AS path
    FROM employees
    WHERE employee_name = 'Manager A'

    UNION ALL

    -- Recursive member
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        h.level + 1 AS level,
        h.path || ' -> ' || e.employee_name AS path
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
)
SELECT
    employee_name,
    level,
    path
FROM employee_hierarchy;


-- ============================================================
-- 10. Multiple starting rows
-- ============================================================

WITH RECURSIVE employee_hierarchy AS (

    -- Two anchor rows
    SELECT
        employee_id,
        employee_name,
        manager_id,
        0 AS level
    FROM employees
    WHERE employee_name IN ('Manager A', 'Manager B')

    UNION ALL

    -- Explore both branches
    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        h.level + 1 AS level
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
)
SELECT *
FROM employee_hierarchy;


-- ============================================================
-- 11. Limit hierarchy depth
-- Includes Levels 0, 1, and 2
-- ============================================================

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
        h.level + 1 AS level
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
    WHERE h.level < 2
)
SELECT *
FROM employee_hierarchy;


-- ============================================================
-- 12. Cycle detection using PostgreSQL arrays
-- ============================================================

WITH RECURSIVE employee_hierarchy AS (

    SELECT
        employee_id,
        employee_name,
        manager_id,
        ARRAY[employee_id] AS visited_ids
    FROM employees
    WHERE employee_id = 1

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.manager_id,
        h.visited_ids || e.employee_id AS visited_ids
    FROM employees e
    JOIN employee_hierarchy h
        ON e.manager_id = h.employee_id
    WHERE NOT e.employee_id = ANY(h.visited_ids)
)
SELECT *
FROM employee_hierarchy;


-- ============================================================
-- 13. Complete recursive hierarchy query
-- ============================================================

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


-- ============================================================
-- 14. Complete query with depth limit and cycle protection
-- ============================================================

WITH RECURSIVE employee_hierarchy AS (

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
    WHERE h.level < 3
      AND NOT e.employee_id = ANY(h.visited_ids)
)
SELECT
    employee_id,
    employee_name,
    manager_id,
    level,
    path
FROM employee_hierarchy;
