use sakila;
select
    title as Title,
    length as Length
from
    film
where length=(select max(length) from film);
