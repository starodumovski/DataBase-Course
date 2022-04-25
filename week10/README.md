# LAB10
___
### Exercise 1
___
###### (Banking transactions)
```
transactions=# SELECT * FROM accounts;  
```
account_id |    name     | credit  | currency    
------------|-------------|---------|----------  
         1 | James McCow | 1000.00 | RUB  
         2 | Maria Stalk | 1000.00 | RUB  
         3 | Ludvic Van  | 1000.00 | RUB  
(3 rows)
```
transactions=# BEGIN;  
BEGIN  
transactions=*# UPDATE accounts  
SET credit = credit - 500  
WHERE account_id = 1;  
UPDATE 1  
transactions=*# UPDATE accounts  
SET credit = credit + 500  
WHERE account_id = 3;  
UPDATE 1  
transactions=*# UPDATE accounts  
SET credit = credit - 700  
WHERE account_id = 2;  
UPDATE 1  
transactions=*# UPDATE accounts  
SET credit = credit + 700  
WHERE account_id = 1;  
UPDATE 1  
transactions=*# UPDATE accounts  
SET credit = credit - 100  
WHERE account_id = 2;  
UPDATE 1  
transactions=*# UPDATE accounts  
SET credit = credit + 100  
WHERE account_id = 3;  
UPDATE 1  
transactions=*# SELECT * FROM accounts;  
```
account_id |    name     | credit  | currency    
------------|-------------|---------|----------  
         1 | James McCow | 1200.00 | RUB  
         2 | Maria Stalk |  200.00 | RUB  
         3 | Ludvic Van  | 1600.00 | RUB  
(3 rows)  
```
transactions=*# ROLLBACK;  
ROLLBACK  
transactions=# SELECT * FROM accounts;
```
account_id |    name     | credit  | currency    
------------|-------------|---------|----------  
         1 | James McCow | 1000.00 | RUB  
         2 | Maria Stalk | 1000.00 | RUB  
         3 | Ludvic Van  | 1000.00 | RUB  
(3 rows)

```
transactions=# ALTER TABLE accounts  
transactions-# ADD COLUMN BankName VARCHAR(50);  
ALTER TABLE  
transactions=# SELECT * FROM accounts; 
```

account_id |    name     | credit  | currency | bankname    
-----------|-------------|---------|----------|----------  
         1 | James McCow | 1000.00 | RUB      |    
         2 | Maria Stalk | 1000.00 | RUB      |    
         3 | Ludvic Van  | 1000.00 | RUB      |    
(3 rows)  

```
transactions=# UPDATE accounts  
transactions-# SET bankname = 'SberBank';  
UPDATE 3  
transactions=# UPDATE accounts  
transactions-# SET bankname = 'Tinkoff'  
transactions-# WHERE account_id = 2;  
UPDATE 1
transactions=# SELECT * FROM accounts ORDER BY account_id;
```
account_id |    name     | credit  | currency | bankname    
------------|-------------|---------|----------|----------  
         1 | James McCow | 1000.00 | RUB      | SberBank  
         2 | Maria Stalk | 1000.00 | RUB      | Tinkoff  
         3 | Ludvic Van  | 1000.00 | RUB      | SberBank  
(3 rows)

- **I used the procedure to operate with one banking transaction**
```sql
CREATE PROCEDURE send_money(a_from INTEGER, a_to INTEGER, amount DECIMAL(13,2))
AS
$$
DECLARE
	v_fee DECIMAL(13,2);
BEGIN
	IF $1 = $2
	THEN
		v_fee = (SELECT fee.amount FROM fee WHERE fee_id = 1);
	ELSE
		v_fee = (SELECT fee.amount FROM fee WHERE fee_id = 2);
	END IF;
	IF (SELECT count(*) FROM accounts WHERE accounts.account_id = $1) = 0  
	THEN  
		ROLLBACK;  
	ELSEIF (SELECT count(*) FROM accounts WHERE accounts.account_id = $2) = 0  
	THEN  
		ROLLBACK;  
	ELSEIF (SELECT DISTINCT credit FROM accounts WHERE accounts.account_id = $1) < $3 + v_fee  
	THEN  
		ROLLBACK;  
	ELSE  
		IF $1 = $2
		THEN
			UPDATE accounts SET credit = credit + $3 - v_fee WHERE account_id = $2;
			COMMIT;
			INSERT INTO ledger (account_from, account_to, fee, amount, transaction_date_time) VALUES
			($1, $2, v_fee, $3, now());
			COMMIT;
		ELSE
			IF $3 > 0
			THEN
				UPDATE accounts SET credit = credit - $3 - v_fee WHERE account_id = $1;
				UPDATE accounts SET credit = credit + $3 WHERE account_id = $2;
				COMMIT;
				INSERT INTO ledger (account_from, account_to, fee, amount, transaction_date_time) VALUES
				($1, $2, v_fee, $3, now());
				COMMIT;
			ELSE
				ROLLBACK;
			END IF;
		END IF;
	END IF;
END;
$$
LANGUAGE plpgsql;
```
- calling next procedures:
```sql
CALL send_money (1, 3, 500);
CALL send_money (2, 1, 700);  
CALL send_money (2, 3, 100);
```
I got:
```
transactions=# SELECT * FROM accounts ORDER BY account_id ; 
```
account_id |    name     | credit  | currency | bankname    
------------|-------------|---------|----------|----------  
         1 | James McCow | 1170.00 | RUB      | SberBank  
         2 | Maria Stalk |  140.00 | RUB      | Tinkoff  
         3 | Ludvic Van  | 1600.00 | RUB      | SberBank  
(3 rows)
```
transactions=# SELECT* FROM ledger;  
```
id | account_from | account_to |  fee  | amount |   transaction_date_time       
----|--------------|------------|-------|--------|----------------------------  
 2 |            1 |          3 | 30.00 | 500.00 | 2022-04-25 03:48:19.19953  
 3 |            2 |          1 | 30.00 | 700.00 | 2022-04-25 03:48:53.291323  
 4 |            2 |          3 | 30.00 | 100.00 | 2022-04-25 03:49:04.523163  
(3 rows)

___
### Exercise 2
___
##### $1^{st}$ PART
- **COMMITED READ**:
	- $4^{th}$ step: **Different results** (The changes were not commited)
	- $5^{th}$ step: **The same result** (The changes were commited)
	-  $8^{th}$ step: **2$^{nd}$ terminal is blocked** (Scince there is the queue of potential changes that can be committed)
	- $9^{th}$ step: **2$^{nd}$ terminal is updated**
- **REPEATABLE READ**:
	- $4^{th}$ step: **Different results** (The changes were not commited)
	- $5^{th}$ step: **Different result** (First read data is unchangable)
	- $8^{th}$ step: **** **2$^{nd}$ terminal is blocked** (Scince there is the queue of potential changes that can be committed)
	-  $9^{th}$ step: **Could not serialize access due to concurrent update** (The transaction contains outdated information)