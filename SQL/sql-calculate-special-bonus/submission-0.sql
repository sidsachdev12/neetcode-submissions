-- Write your query below

-- Goal: Return the employee_id and bonus for each employee, ordered by employee_id.


SELECT employee_id,  
        CASE 
            WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
            ELSE 0
        END AS bonus
FROM employees
ORDER BY employee_id;