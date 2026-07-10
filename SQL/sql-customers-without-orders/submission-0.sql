-- Write your query below

-- Goal: all customers who have never placed an order -> Customer names

SELECT customers.name
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id
WHERE orders.customer_id IS NULL;