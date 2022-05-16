use sakila;
select
    customer_id as Customer_id
from
    rental
group by customer_id having count(*)>=40;
