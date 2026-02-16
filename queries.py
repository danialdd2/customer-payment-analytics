query='''
select c.customer_id,c.first_name,c.last_name,p.amount,r.rental_id
from customer c 
join payment p
on c.customer_id=p.customer_id
join rental r
on r.customer_id=p.customer_id
'''