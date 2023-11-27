-- Write your PostgreSQL query statement below
with cte1 as (
    select
        customer_id,
        ROW_NUMBER() over(partition by customer_id) as row_num
    from (
        select distinct customer_id, product_key from customer
    )
)

select distinct(customer_id)
from cte1
where row_num >= (
    select count(product_key) from product
)



