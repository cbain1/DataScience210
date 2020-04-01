SELECT * FROM customer;

SELECT * FROM customer_order;

-- multiple table queries
SELECT * 
FROM customer, customer_order;

SELECT * 
FROM customer CROSS JOIN customer_order;

-- think of each table as a set and then join performs operations on sets

-- natural join pretends that all columns that are the same as eachother, have the same value
-- natural join does not let you pick the columns to do an "inner join", which is explained below
-- it automatically inner joins columns with the same names from both tables
-- find columns that are named exactly the same
-- if the values in the row in the column match, they will match that row, otherwise it does nothing
-- Gupta doesn't recommend these because they are language dependent 
SELECT *
FROM customer NATURAL JOIN customer_order;

-- "." command lets you choose which table you want to pull the variable from
SELECT Customer.customer_id, name, region, street_address, city, state, zip, order_id, order_date, ship_date, product_id, order_qty, shipped
FROM customer NATURAL JOIN customer_order;

-- an inner join is essentially a generalization of natural join (with one slight exception, as youll see below)
-- to do this, we use the "on" command to select what we combine
-- inner join is the intersection of the two sets
SELECT order_id, Customer.customer_Id, order_date, ship_date, name, street_address, city, state, zip, product_id, order_qty
FROM customer INNER JOIN customer_order ON  customer.customer_id = customer_order.customer_id;

-- an outer left join gives you 'table a' augmented with the columns of table b
SELECT order_id, Customer.customer_Id, order_date, ship_date, name, street_address, city, state, zip, product_id, order_qty
FROM customer LEFT OUTER JOIN customer_order ON  customer.customer_id = customer_order.customer_id;

-- right outer join, full outer join
-- right join can just be a left join but you flip the way the tables are arranged
-- sqlite doesn't have a full outer join, you must do a left join, right join, and then join those joins


-- i want to know the list of customers that don't have any orders in the database 
SELECT customer.customer_id, name
FROM customer LEFT OUTER JOIN customer_order ON customer.customer_id = customer_order.customer_id
WHERE order_id IS null;

-- want to get what they ordered and what they paid 
SELECT customer.customer_id, order_date, ship_date, name street_address, city, state, zip, product_id, description, price, order_qty, price*order_qty AS total_price
FROM customer INNER JOIN customer_order ON customer.customer_id = customer_order.customer_id
INNER JOIN product ON customer_order.product_id = product.product_id;

-- want to know how much revenue generated from each customer
SELECT customer.customer_id, name, SUM(order_qty*price) AS revenue
FROM customer INNER JOIN customer_order ON customer.customer_id = customer_order.customer_id
INNER JOIN product ON customer_order.product_id = product.product_id
GROUP BY name;

-- now i want to know the total revenue from each customer, including those who had no revenue 
SELECT customer.customer_id, name, SUM(order_qty*price) AS revenue
FROM customer LEFT JOIN customer_order ON customer.customer_id = customer_order.customer_id
LEFT JOIN product ON customer_order.product_id = product.product_id
GROUP BY name;

-- how i get rid of nulls though 
-- coalesce - if the first thing is null, change it to the second thing
SELECT customer.customer_id, name, COALESCE(SUM(order_qty*price), 0) AS revenue
FROM customer LEFT JOIN customer_order ON customer.customer_id = customer_order.customer_id
LEFT JOIN product ON customer_order.product_id = product.product_id
GROUP BY name;