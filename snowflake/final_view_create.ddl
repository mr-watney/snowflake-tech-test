create view if not exists final_view as
select c.customer_id, c.loyalty_score, t.product_id, p.product_category, count(t.product_id) purchase_count
from transactions t
left join customers c on c.customer_id = t.customer_id
left join products p on p.product_id = t.product_id
group by 1,2,3,4
;