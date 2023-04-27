select 'order'.order_no, manager.full_name, customer.full_name
from customer, manager, 'order'
on 'order'.customer_id = customer.customer_id and 'order'.manager_id = manager.manager_id and manager.city != customer.city
