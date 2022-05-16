use sakila;
select
    count(*) as Total
from
    film
where film.film_id not in
      (select
            film.film_id
      from
            film,
            inventory
      where film.film_id=inventory.film_id);
