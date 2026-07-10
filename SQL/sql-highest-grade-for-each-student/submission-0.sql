-- Write your query below

-- Goal: Return the student_id, exam_id, and score, ordered by student_id in ascending order.

SELECT e.student_id, MIN(e.exam_id) as exam_id, e.score
FROM exam_results as e
WHERE e.score = (
    SELECT MAX(e2.score)
    FROM exam_results as e2
    WHERE e.student_id = e2.student_id
)
GROUP BY e.student_id, e.score
ORDER BY e.student_id