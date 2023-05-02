select teachers.full_name,
       avg(assignments_grades.grade) as minimal_grade
from teachers
inner join assignments on teachers.teacher_id = assignments.teacher_id
inner join assignments_grades on assignments_grades.assisgnment_id = assignments.assisgnment_id
group by teachers.teacher_id
order by minimal_grade
limit 1