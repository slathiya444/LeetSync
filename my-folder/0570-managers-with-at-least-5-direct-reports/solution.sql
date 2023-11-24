-- Write your PostgreSQL query statement below

select name
from employee
where id in (
  select managerid
  from employee
  group by managerid
  having count(employee.managerid) >= 5
)

