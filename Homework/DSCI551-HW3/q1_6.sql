use sakila;
select
    first_name,
    last_name
from
    payment,
    customer
where customer.customer_id=payment.customer_id
group by payment.customer_id having sum(amount)>200;
