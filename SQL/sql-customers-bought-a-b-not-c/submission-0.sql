-- Write your query below

-- SELECT customers.customer_id, customers.customer_name
-- FROM customers
-- LEFT JOIN orders
--     ON customers.customer_id = orders.customer_id
-- GROUP BY customers.customer_id, customers.customer_name
-- HAVING 
--     COUNT(CASE WHEN orders.product_name = 'A' THEN 1 ELSE 0) > 0 AND
--     COUNT(CASE WHEN orders.product_name = 'B' THEN 1 ELSE 0) > 0 AND
--     COUNT(CASE WHEN orders.product_name = 'C' THEN 1 ELSE 0) = 0
-- ORDER BY customers.customer_name;

SELECT
    c.customer_id,
    c.customer_name
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
HAVING
    SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN o.product_name = 'B' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN o.product_name = 'C' THEN 1 ELSE 0 END) = 0
ORDER BY c.customer_name;