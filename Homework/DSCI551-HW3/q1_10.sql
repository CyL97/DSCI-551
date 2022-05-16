use sakila;
select
    customer.first_name,
    customer.last_name,
    city.city
from
    city,
    address,
    customer
where (customer.first_name="Jamie" or customer.first_name="Jessie" or customer.first_name="Leslie")
  and address.address_id=customer.address_id
  and city.city_id=address.city_id
order by customer.first_name;
