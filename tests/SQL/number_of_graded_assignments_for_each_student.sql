-- Write query to get number of graded assignments for each student:
SELECT a.student_id, COUNT(a.state) AS no_graded_assignments
from assignments a
where a.state = 'GRADED'
group by a.student_id