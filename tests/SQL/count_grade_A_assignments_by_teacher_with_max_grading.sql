-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(a.id) as num_grade_a
FROM teachers t
JOIN assignments a ON t.id = a.teacher_id
WHERE a.grade = 'A' AND a.state = 'GRADED'
GROUP BY t.id
ORDER BY num_grade_a DESC
LIMIT 1;