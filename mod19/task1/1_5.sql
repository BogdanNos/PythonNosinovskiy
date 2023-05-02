select students_groups.group_id,
       students_count,
       average_grade,
       students_pass_count,
       students_missed_count,
       students_repeated_count
from students_groups
inner join  (
    select assignments.group_id,
           avg(assignments_grades.grade) as average_grade,
           sum(assignments_grades.date > assignments.due_date) as students_missed_count,
           count(assignments_grades.student_id) - count(distinct assignments_grades.student_id) as students_repeated_count
    from assignments
    inner join  assignments_grades on assignments.assisgnment_id = assignments_grades.assisgnment_id
    group by assignments.group_id) as table_assignments
on students_groups.group_id = table_assignments.group_id
inner join (
    select students.group_id,
           count(distinct students.student_id) as students_count,
           count(distinct students.student_id) - count(distinct assignments_grades.student_id) as students_pass_count
    from students
    left join assignments_grades on students.student_id = assignments_grades.student_id
    group by students.group_id) as table_students
on students_groups.group_id = table_students.group_id
group by students_groups.group_id