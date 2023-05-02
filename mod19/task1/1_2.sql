select students.full_name,
       avg(assignments_grades.grade) as max_grade
from students
inner join assignments_grades on assignments_grades.student_id = students.student_id
group by students.student_id
order by max_grade DESC
limit 10