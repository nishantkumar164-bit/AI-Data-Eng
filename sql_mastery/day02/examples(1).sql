-- SQL Window Functions and CTE Examples

-- Sample tables assumed:
-- orders(order_id, customer_id, order_amount)
-- employees(employee_id, department, salary)

------------------------------------------------------------
-- 1. Customer total while preserving every order row
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    SUM(order_amount) OVER (
        PARTITION BY customer_id
    ) AS customer_total
FROM orders;

------------------------------------------------------------
-- 2. Customer average while preserving every order row
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    AVG(order_amount) OVER (
        PARTITION BY customer_id
    ) AS customer_avg
FROM orders;

------------------------------------------------------------
-- 3. Running total per customer
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    SUM(order_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders;

------------------------------------------------------------
-- 4. ROW_NUMBER: unique row number per customer
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY order_id
    ) AS row_num
FROM orders;

------------------------------------------------------------
-- 5. First order per customer
------------------------------------------------------------
WITH ranked_orders AS (
    SELECT
        order_id,
        customer_id,
        order_amount,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_id
        ) AS row_num
    FROM orders
)
SELECT
    order_id,
    customer_id,
    order_amount
FROM ranked_orders
WHERE row_num = 1;

------------------------------------------------------------
-- 6. Rank employees within each department
------------------------------------------------------------
SELECT
    employee_id,
    department,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

------------------------------------------------------------
-- 7. Dense rank employees within each department
------------------------------------------------------------
SELECT
    employee_id,
    department,
    salary,
    DENSE_RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS dense_salary_rank
FROM employees;

------------------------------------------------------------
-- 8. Highest-paid employee(s) per department
-- Includes ties
------------------------------------------------------------
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

------------------------------------------------------------
-- 9. Exactly one highest-paid employee per department
-- Tie-breaks by employee_id
------------------------------------------------------------
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

------------------------------------------------------------
-- 10. Previous order amount
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    LAG(order_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_id
    ) AS previous_order_amount
FROM orders;

------------------------------------------------------------
-- 11. Previous order amount with a default value
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    LAG(order_amount, 1, 0) OVER (
        PARTITION BY customer_id
        ORDER BY order_id
    ) AS previous_order_amount
FROM orders;

------------------------------------------------------------
-- 12. Difference from previous order using a CTE
------------------------------------------------------------
WITH order_history AS (
    SELECT
        order_id,
        customer_id,
        order_amount,
        LAG(order_amount) OVER (
            PARTITION BY customer_id
            ORDER BY order_id
        ) AS previous_order_amount
    FROM orders
)
SELECT
    order_id,
    customer_id,
    order_amount,
    previous_order_amount,
    CASE
        WHEN previous_order_amount IS NULL THEN 0
        ELSE order_amount - previous_order_amount
    END AS amount_difference
FROM order_history;

------------------------------------------------------------
-- 13. Next order amount
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    LEAD(order_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_id
    ) AS next_order_amount
FROM orders;

------------------------------------------------------------
-- 14. Two rows earlier
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    LAG(order_amount, 2) OVER (
        PARTITION BY customer_id
        ORDER BY order_id
    ) AS amount_two_orders_ago
FROM orders;

------------------------------------------------------------
-- 15. Three-order moving total
------------------------------------------------------------
SELECT
    order_id,
    customer_id,
    order_amount,
    SUM(order_amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_id
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS three_order_total
FROM orders;
