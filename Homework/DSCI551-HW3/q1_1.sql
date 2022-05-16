use sakila;
select
    count(*) as Total
from
    film
where
    rating='PG-13' and length>=100 and length<=200;
