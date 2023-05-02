select assignments_grades.assisgnment_id, avg(assignments_grades.grade)
from assignments_grades
where assignments_grades.assisgnment_id in (
    select assignments.assisgnment_id
    from assignments
    where assignments.assignment_text like 'прочитать%' or assignments.assignment_text like 'выучить%'
    )
group by assignments_grades.assisgnment_id