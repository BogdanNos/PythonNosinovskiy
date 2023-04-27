select customer.full_name, 'order'.order_no
from customer, 'order'
on 'order'.customer_id = customer.customer_id
where 'order'.manager_id IS NULL;