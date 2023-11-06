-- Write your PostgreSQL query statement below
-- select * 
-- from employees e FULL OUTER JOIN salaries s
-- on e.employee_id = s.employee_id

select coalesce(e.employee_id, s.employee_id) as employee_id 
from Employees e full join Salaries s  
on e.employee_id=s.employee_id
where e.name is null or s.salary is null
