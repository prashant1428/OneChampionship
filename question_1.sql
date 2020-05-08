select e.id, e.event_name, e.people_count
from
(
    select  events.*,
            lag(people_count,2) over(order by id) second_prev,
            lag(people_count,1) over(order by id) first_prev,
            lead(people_count,1) over(order by id) first_next,
            lead(people_count,2) over(order by id) second_next
    from events 
) e
where (e.people_count>=100 and e.second_prev>=100 and e.first_prev>=100) or (e.people_count>=100 and e.second_next>=100 and e.first_next>=100) or
(e.people_count>=100 and e.first_next>=100 and e.first_prev>=100);
