-- Write your PostgreSQL query statement below
select email as Email
from person
group by email
having count(id) > 1
