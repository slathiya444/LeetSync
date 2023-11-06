-- Write your PostgreSQL query statement below
-- select com_id from company
-- where name not like '%RED%'

-- select s.name, o.com_id
-- from salesperson s left join orders o
-- on s.sales_id = o.sales_id
-- where o.com_id in (
--   select com_id from company
--   where name not like '%RED%' or name = null
-- )

select name
from salesperson
where name not in (
  SELECT sp.name
  FROM Orders AS od
  INNER JOIN Company cmp
      ON od.com_id=cmp.com_id
  INNER JOIN SalesPerson AS sp
      ON od.sales_id=sp.sales_id
  WHERE cmp.name ='RED'
)
