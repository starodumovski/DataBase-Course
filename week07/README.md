___
### Exercise 1
---
- Te table is in **1NF**, so I will make **3NF**

```sql

-- Creation of the tables

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

-- Fillig the tables with data

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

INSERT INTO "Order" (orderid, "date", cid)
VALUES (2301, '23/02/2011', 101),
(2302, '25/02/2011', 107),
(2303, '27/02/2011', 110);

INSERT INTO common (ord, oid, iid, quant)
VALUES (1, 2301, 3786, 3),
(2, 2301, 4011, 6),
(3, 2301, 9132, 8),
(4, 2302, 5794, 4),
(5, 2303, 4011, 2),
(6, 2303, 3141, 2);
```
Table **customer**:
![[Lab7_Screens/Table Customer.png]]
Table **item**:
![[Lab7_Screens/Table item.png]]
Table **Order**:
![[Lab7_Screens/Table Order.png]]
Table **common**:
![[Lab7_Screens/Table common.png]]
---
##### Queries for the result table 1
---
- **Calculate the total number of items per order and the total amount to pay for the order**
```sql
SELECT O.oid, SUM(O.quant) as total_quant, SUM(total) as total_price
FROM (
  SELECT oid, quant, price, SUM(quant*price) as Total
  FROM (common INNER JOIN item ON common.iid = item.itemid) L
  Group BY oid, quant, price
  ) O 
GROUP BY O.oid
```

![[Lab7_Screens/1st query.png]]
___
- **Obtain the customer whose purchase in terms of money has been greater than the others**
```sql
SELECT customerid, customername, city, total_price
FROM (
  SELECT Al3.oid, Al3.cid, SUM(total) as total_price
  FROM ((
    SELECT oid, quant, price, SUM(quant*price) as Total
    FROM (common INNER JOIN item ON common.iid = item.itemid) L
    Group BY oid, quant, price
    ) Al INNER JOIN "Order" ON Al.oid = "Order".orderid) Al3
  GROUP BY Al3.oid, Al3.cid
  HAVING SUM(total) = (
    SELECT MAX(total_price) as maximum
    FROM (
      SELECT O.oid, SUM(O.quant) as total_quant, SUM(total) as total_price
      FROM (
        SELECT oid, quant, price, SUM(quant*price) as Total
        FROM (common INNER JOIN item ON common.iid = item.itemid) L
        Group BY oid, quant, price
        ) O 
      GROUP BY O.oid
    ) Alll
  )
) cus INNER JOIN customer ON cus.cid = customer.customerid
```

![[Lab7_Screens/2nd query 1.png]]

---
### Exercise 2
---
- Te table is in **1NF**, so I will make **3NF**

```sql
-- Creation of the tables
CREATE TABLE school
(
  school_id SERIAL Primary Key,
  school_name VARCHAR(50)
);

CREATE TABLE room
(
  room_id SERIAL PRIMARY KEY,
  room_name Varchar(10)
);

CREATE TABLE teacher
(
  teacher_id SERIAL PRIMARY KEY,
  teacher_name VARCHAR(50)
);

CREATE TABLE course
(
  course_id SERIAL PRIMARY KEY,
  course_name VARCHAR(50)
);

CREATE TABLE publisher
(
  publisher_id SERIAL PRIMARY KEY,
  publisher_name VARCHAR(30)
);

create table grade
(
  grade_id SERIAL PRIMARY KEY,
  grade_name VARCHAR(20)
);

CREATE TABLE book
(
  book_id SERIAL PRIMARY KEY,
  book_name VARCHAR(50),
  p_id INT,
  FOREIGN KEY (p_id) REFERENCES publisher(publisher_id)
);

CREATE TABLE common
(
  common_id SERIAL PRIMARY KEY,
  s_id INT,
  t_id INT,
  c_id INT,
  r_id INT,
  g_id INT,
  b_id INT,
  loan_date VARCHAR(20),
  FOREIGN KEY (s_id) REFERENCES school(school_id),
  FOREIGN KEY (t_id) REFERENCES teacher(teacher_id),
  FOREIGN KEY (c_id) REFERENCES course(course_id),
  FOREIGN KEY (r_id) REFERENCES room(room_id),
  FOREIGN KEY (g_id) REFERENCES grade(grade_id),
  FOREIGN KEY (b_id) REFERENCES book(book_id)
);

-- Filling the tables with data

INSERT INTO school (school_name) VALUES
('Horizon Education Institute'),
('Bright Institution');
INSERT INTO teacher (teacher_name) VALUES
('Chad Russell'),
('E.F.Codd'),
('Jones Smith'),
('Adam Baker');
INSERT INTO publisher (publisher_name) VALUES
('BOA Editions'),
('Taylor & Francis Publishing'),
('Prentice Hall'),
('McGraw Hill');
INSERT INTO room (room_name) VALUES
('1.A01'),
('1.B01'),
('2.B01');
INSERT INTO grade (grade_name) VALUES
('1st grade'),
('2nd grade');
INSERT iNTO book (book_name, p_id) VALUES
('Learning and teaching in early childhood', 1),
('Preschool,N56', 2),
('Early Childhood Education N9', 3),
('Know how to educate: guide for Parents', 4);
INSERT INTO course (course_name) VALUES
('Logical thinking'),
('Wrtting'),
('Numerical Thinking'),
('Spatial, Temporal and Causal Thinking'),
('English');
INSERT INTO common (s_id, t_id, c_id, r_id, g_id, b_id, loan_date) VALUES
(1, 1, 1, 1, 1, 1, '09/09/2010'),
(1, 1, 2, 1, 1, 2, '05/05/2010'),
(1, 1, 3, 1, 1, 1, '05/05/2010'),
(1, 2, 4, 2, 1, 3, '06/05/2010'),
(1, 2, 3, 2, 1, 1, '06/05/2010'),
(1, 3, 2, 1, 2, 1, '09/09/2010'),
(1, 3, 5, 1, 2, 4, '05/05/2010'),
(2, 4, 1, 3, 1, 4, '18/12/2010'),
(2, 4, 3, 3, 1, 1, '06/05/2010');
```
Table **school**:
![[Lab7_Screens/Table school.png]]
Table **teacher**:
![[Lab7_Screens/Table teacher.png]]
Table **grade**:
![[Lab7_Screens/Table grade.png]]
Table **publisher**:
![[Lab7_Screens/Table publisher.png]]
Table **room**:
![[Lab7_Screens/Table room.png]]
Table **book**:
![[Lab7_Screens/Table book.png]]
Table **course**:
![[Lab7_Screens/Table course.png]]
Table **common**:
![[Lab7_Screens/Table common2.png]]
___
##### Queries for the result table 1
___
- **Obtain for each of the schools, the number of books that have been loaned to each publishers**
```sql
SELECT s_id as school, p_id as publisher, COUNT(O.loan_date) as number_of_books
FROM (common INNER JOIN book ON common.b_id = book.book_id) O
GROUP BY O.s_id, O.p_id
```
![[Lab7_Screens/1st query 2.png]]
___
- **For each school, find the book that has been on loan the longest and the teacher in charge of it**
```sql
SELECT V5.s_id, V5.school_name, V5.b_id, V5.book_name, V5.t_id, V5.teacher_name
FROM (((((
  SELECT s_id as sch, MIN(loan_date) as ld
  FROM common
  GROUP BY common.s_id
) V1 INNER JOIN common ON (common.s_id = V1.sch AND common.loan_date = V1.ld)) V2
INNER JOIN teacher ON V2.t_id = teacher.teacher_id) V3
INNER JOIN book ON V3.b_id = book.book_id) V4
INNER JOIN school ON V4.s_id = school.school_id) V5
```
![[Lab7_Screens/2nd query 2.png]]