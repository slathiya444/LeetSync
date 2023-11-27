-- Write your PostgreSQL query statement below
-- select
--     *,
--     row_number() over (partition by s.product_id order by s.year asc) as row_num
-- from sales s

-- select product_id, year as first_year, quantity, price
-- from (
--     select
--         *,
--         row_number() over (partition by s.product_id order by s.year asc) as row_num
--     from sales s
-- )
-- where row_num = 1

select product_id, year as first_year, quantity, price
from sales
where (product_id, year) in (
    select product_id, min(year) from sales group by product_id
)
