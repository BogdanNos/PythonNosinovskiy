select students.full_name
from students
inner join students_groups on students.group_id = students_groups.group_id
inner join (
       select teachers.teacher_id,
              avg(assignments_grades.grade) as max_grade
       from teachers
       inner join assignments on teachers.teacher_id = assignments.teacher_id
       inner join assignments_grades on assignments_grades.assisgnment_id = assignments.assisgnment_id
       group by teachers.teacher_id
       order by max_grade DESC
       limit 1
       ) as easy_teacher
on students_groups.teacher_id = easy_teacher.teacher_id;
