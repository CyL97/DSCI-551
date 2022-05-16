use sakila;
select
    sum(Total) as Total
from
    (select
        count(*) as Total
    from
        (select distinct 
	    first_name,
            last_name 
    from actor) as T 
    group by first_name having count(first_name)>1) as T1;
