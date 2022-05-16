use sakila;
select
    category.name as Category,
    count(film_category.film_id) as Total
from
    category,
    film_category
where category.category_id=film_category.category_id
group by category.name;
