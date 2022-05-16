use sakila;
select
    first_name,
    last_name
from
    actor,
    film_actor,
    film
where
    actor.actor_id=film_actor.actor_id and
    film_actor.film_id=film.film_id and
    actor.actor_id not in
                (select
                        actor.actor_id
                 from
                        actor,
                        film_actor,
                        film
                 where
                       actor.actor_id=film_actor.actor_id and
                       film_actor.film_id=film.film_id and
                       film.rating='R'
                group by actor.actor_id)
group by actor.actor_id;