select customer.full_name, manager.full_name, 'order'.purchase_amount, 'order'.date
from customer, manager, 'order'
on 'order'.customer_id = customer.customer_id and 'order'.manager_id = manager.manager_id