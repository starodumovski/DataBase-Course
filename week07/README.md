### Exercise 1
- Te table is in 1NF, so I will make another ones Normal Forms

```sql
CREATE TABLE Customer
(
  customerId INT PRIMARY KEY,
  customerName VARCHAR(30),
  city VARCHAR(30)
);

CREATE TABLE Item
(
  itemId INT PRIMARY KEY,
  itemName VARCHAR(30),
  price DECIMAL(7,2)
);

CREATE TABLE "Order"
(
  orderId INT PRIMARY KEY,
  "date" VARCHAR(30)
);
CREATE TABLE common
(
  ord INT NOT NULL PRIMARY KEY,
  oid INT,
  quant INT,
  iId INT,
  cId INT,
  FOREIGN KEY (oId) REFERENCES "Order"(orderid),
  FOREIGN KEY (iId) REFERENCES item(itemid),
  FOREIGN KEY (cId) REFERENCES customer(customerid)
);

INSERT INTO customer (customerid, customername, city)
VALUES (101, 'Martin', 'Prague'),
(107, 'Herman', 'Madrid'),
(110, 'Pedro', 'Moscow');

INSERT INTO item (itemid, itemname, price)
VALUES (3786, 'Net', 35.00),
(4011, 'Racket', 65.00),
(9132, 'Pack-3', 4.75),
(5794, 'Pack-6', 5.00),
(3141, 'Cover', 10.00);

INSERT INTO "Order" (orderid, "date")
VALUES (2301, '23/02/2011'),
(2302, '25/02/2011'),
(2303, '27/02/2011');

INSERT INTO common (ord, oid, cid, iid, quant)
VALUES (1, 2301, 101, 3786, 3),
(2, 2301, 101, 4011, 6),
(3, 2301, 101, 9132, 8),
(4, 2302, 107, 5794, 4),
(5, 2303, 110, 4011, 2),
(6, 2303, 110, 3141, 2);
```
Table customer:
![[Pasted image 20220404154150.png]]
Table item:
![[Pasted image 20220404154220.png]]
Table Order:
![[Pasted image 20220404154242.png]]
Table common:
![[Pasted image 20220404154335.png]]

```sql
SELECT O.oid, SUM(total) as total
FROM (
  SELECT oid, quant, price, SUM(quant*price) as Total
  FROM (common INNER JOIN item ON common.iid = item.itemid) L
  Group BY oid, quant, price
  ) O 
GROUP BY O.oid
```
![[Pasted image 20220404161040.png]]