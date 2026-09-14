-- SQL Window Functions Assignment
-- Do not look at examples.sql until you have attempted each problem.

-- Assumed tables:
-- orders(order_id, customer_id, order_amount)
-- employees(employee_id, department, salary)

------------------------------------------------------------
-- 1. Customer total
------------------------------------------------------------
-- Return every order and the total amount spent by its customer.

------------------------------------------------------------
-- 2. Customer average
------------------------------------------------------------
-- Return every order and the average order amount for its customer.

------------------------------------------------------------
-- 3. Running total
------------------------------------------------------------
-- Return every order and a running total per customer ordered by order_id.

------------------------------------------------------------
-- 4. Row numbering
------------------------------------------------------------
-- Assign a unique row number to each order within its customer.

------------------------------------------------------------
-- 5. First order
------------------------------------------------------------
-- Return only the first order of each customer using ROW_NUMBER().

------------------------------------------------------------
-- 6. Highest-paid employees
------------------------------------------------------------
-- Return all employees tied for the highest salary in each department.

------------------------------------------------------------
-- 7. Exactly one highest-paid employee
------------------------------------------------------------
-- Return exactly one highest-paid employee per department.
-- Make the tie-breaking deterministic.

------------------------------------------------------------
-- 8. Second-highest salary
------------------------------------------------------------
-- Return all employees receiving the second-highest distinct salary
-- in each department.

------------------------------------------------------------
-- 9. Previous order
------------------------------------------------------------
-- Return each order with the previous order amount for that customer.

------------------------------------------------------------
-- 10. Order difference
------------------------------------------------------------
-- Return each order and the difference between its amount and the
-- previous order amount. Return 0 for the first order of each customer.

------------------------------------------------------------
-- 11. Next order
------------------------------------------------------------
-- Return each order with the next order amount for that customer.

------------------------------------------------------------
-- 12. Two-row lookback
------------------------------------------------------------
-- Return the order amount from two orders earlier for each customer.
-- Use NULL when the row does not exist.

------------------------------------------------------------
-- 13. Three-order moving total
------------------------------------------------------------
-- Calculate the sum of the current order and the previous two orders
-- for each customer.

------------------------------------------------------------
-- 14. Explain
------------------------------------------------------------
-- In comments, explain the difference between:
-- ROW_NUMBER(), RANK(), and DENSE_RANK().

------------------------------------------------------------
-- 15. Production reasoning
------------------------------------------------------------
-- In comments, explain:
-- a) Why can’t a window-function alias normally be used in WHERE?
-- b) When would you prefer a CTE over a subquery?
-- c) Why is a CTE not automatically faster?
