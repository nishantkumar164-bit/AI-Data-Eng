-- Joins
SELECT o.order_id, oi.product_id FROM orders o JOIN order_items oi ON o.order_id = oi.order_id;

-- Aggregate before joining
WITH order_totals AS (
 SELECT order_id, SUM(quantity * unit_price) AS order_total
 FROM order_items GROUP BY order_id
)
SELECT o.customer_id, SUM(ot.order_total) AS customer_revenue
FROM orders o JOIN order_totals ot ON o.order_id = ot.order_id
GROUP BY o.customer_id;

-- Window function
SELECT customer_id, order_id, order_amount,
 SUM(order_amount) OVER (PARTITION BY customer_id) AS customer_total
FROM orders;

-- Highest-paid employee per department
WITH ranked_employees AS (
 SELECT employee_id, department, salary,
 ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC, employee_id) AS rn
 FROM employees
)
SELECT * FROM ranked_employees WHERE rn = 1;

-- Multiple CTEs
WITH customer_totals AS (
 SELECT customer_id, SUM(order_amount) AS total_amount
 FROM orders GROUP BY customer_id
), customer_order_counts AS (
 SELECT customer_id, COUNT(*) AS order_count
 FROM orders GROUP BY customer_id
)
SELECT t.customer_id, t.total_amount, c.order_count
FROM customer_totals t JOIN customer_order_counts c
 ON t.customer_id = c.customer_id
WHERE t.total_amount > 5000 AND c.order_count >= 3;
