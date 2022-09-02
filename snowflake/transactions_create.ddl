create table if not exists TRANSACTIONS (
  product_id varchar(10),
  price integer,
  customer_id varchar(10),
  date_of_purchase datetime
);