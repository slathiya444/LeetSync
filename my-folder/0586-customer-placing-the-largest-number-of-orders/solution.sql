-- Write your PostgreSQL query statement below
SELECT customer_number 
FROM orders 
GROUP BY customer_number 
ORDER BY COUNT(customer_number) DESC 
limit 1
