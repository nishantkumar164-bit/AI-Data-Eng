-- SQL Learning Examples
-- Topics: GROUP BY, Aggregation, CTE, Grain, LEFT JOIN, COALESCE
-- and safe aggregation across different grains.

-- ============================================================
-- EXAMPLE 1: Total amount per customer
-- ============================================================

SELECT
    customer_id,
    SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;


-- ============================================================
-- EXAMPLE 2: Total amount using a CTE
-- ============================================================

WITH customer_summary AS (
    SELECT
        customer_id,
        SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_summary;


-- ============================================================
-- EXAMPLE 3: Include customers with no orders
-- ============================================================

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


-- ============================================================
-- EXAMPLE 4: Total amount + order count
-- Both metrics are at customer grain.
-- ============================================================

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


-- ============================================================
-- EXAMPLE 5: The double-counting problem
-- DO NOT use this pattern when amount is at order grain
-- and order_items is at item grain.
-- ============================================================

SELECT
    o.customer_id,
    SUM(o.amount) AS total_amount,
    SUM(oi.quantity) AS total_quantity
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY o.customer_id;

-- Why can total_amount be wrong?
-- An order with 3 items appears 3 times after the join.
-- Its amount is therefore repeated 3 times.


-- ============================================================
-- EXAMPLE 6: Safe approach using separate CTEs
-- ============================================================

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


-- ============================================================
-- EXAMPLE 7: Grain map
-- ============================================================

-- customers:
--     1 row = 1 customer
--
-- orders:
--     1 row = 1 order
--
-- order_items:
--     1 row = 1 item within an order
--
-- customer_summary:
--     1 row = 1 customer
--
-- order_summary:
--     1 row = 1 customer
--
-- item_summary:
--     1 row = 1 customer


-- ============================================================
-- EXAMPLE 8: Practical design pattern
-- ============================================================

-- Step 1: Identify grain
-- Step 2: Aggregate each metric at the required grain
-- Step 3: Make sure the CTEs being joined have compatible grain
-- Step 4: Join
-- Step 5: Handle NULLs

-- This pattern is reusable in analytics and data engineering SQL.
