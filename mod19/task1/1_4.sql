select avg(overdue_tasks_count),
       max(overdue_tasks_count),
       min(overdue_tasks_count)
from(
    select sum(assignments_grades.date > assignments.due_date) as overdue_tasks_count
    from assignments
    inner join assignments_grades on assignments.assisgnment_id = assignments_grades.assisgnment_id
    group by assignments.group_id
    );