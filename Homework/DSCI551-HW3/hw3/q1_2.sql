use sakila;
select
    first_name,last_name
from
    actor
where last_name like "%i_";
