-- Write your query below
SELECT p.first_name, p.last_name, city, state
FROM person AS p
LEFT JOIN address AS a
    ON p.person_id = a.person_id
