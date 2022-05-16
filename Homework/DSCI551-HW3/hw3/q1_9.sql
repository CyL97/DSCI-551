use sakila;
select
    sum(Total) as Total
from
    (select
        count(*) as Total
    from
        actor
    where (first_name, last_name) in
        (select distinct
            first_name,
            last_name
        from
            actor)
    group by first_name having count(first_name)>1) as T;
