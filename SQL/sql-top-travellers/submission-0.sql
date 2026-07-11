-- Write your query below
select u.name, SUM(coalesce(r.distance, 0)) as travelled_distance
FROM users as u
left join rides as r 
    on u.id = r.user_id
group by u.name
order by travelled_distance desc, u.name asc;