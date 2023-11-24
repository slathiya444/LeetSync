-- Write your PostgreSQL query statement below

WITH cte1 AS (
    SELECT
        b.user_id,
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed,
        COUNT(action) AS overall
    FROM confirmations AS a
    RIGHT JOIN Signups AS b
    ON a.user_id = b.user_id
    GROUP BY b.user_id
)

select 
    user_id,
    (case when overall != 0 then round(confirmed::numeric / overall, 2) else 0 end)  as confirmation_rate 
from cte1
