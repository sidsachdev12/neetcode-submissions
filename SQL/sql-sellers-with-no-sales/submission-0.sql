-- Write your query below

SELECT seller.seller_name
FROM seller
WHERE seller.seller_id NOT IN(
    SELECT s.seller_id
    FROM seller AS s JOIN orders AS o
        ON s.seller_id = o.seller_id
    WHERE EXTRACT(YEAR FROM o.sale_date) = '2020'
    GROUP BY s.seller_id
)
-- HAVING COUNT(*) = 0
ORDER BY seller.seller_name ASC;