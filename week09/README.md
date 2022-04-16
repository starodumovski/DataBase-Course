# LAB09
____
## Exercise 1
___
###### Code
- The python code is stored in the folowing file:
	[Exs](<file:///home/andrew/Desktop/DHAM/address.py>)

Here is the Python-code representation:
```python
import psycopg2
import pandas as pd
import geopy
from geopy.geocoders import Nominatim


def exercise_1():
    con = psycopg2.connect(database="dvdrental", user="postgres",
                           password="postgres", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    cur = con.cursor()

    cur.execute('''DROP FUNCTION IF EXISTS retrieve_addresses''')
    cur.execute('''
    CREATE OR REPLACE FUNCTION retrieve_addresses()
      RETURNS TABLE(address_id INTEGER, address VARCHAR, city_id SMALLINT) AS
    $$
    BEGIN
     RETURN QUERY

     SELECT address.address_id,address.address, address.city_id
     FROM address
     WHERE (address.city_id BETWEEN 400 AND 600) AND address.address LIKE '11%';

    END; $$


    LANGUAGE plpgsql;
    ''')

    data = pd.read_sql('SELECT * FROM retrieve_addresses();', con)
    print(data)

    cur.execute('ALTER TABLE address ADD COLUMN IF NOT EXISTS latitude TEXT')
    cur.execute('ALTER TABLE address ADD COLUMN IF NOT EXISTS longitude TEXT')
    con.commit()

    addresses_id = []
    addresses = []
    locations = []
    for raw in data.itertuples():
        addresses_id.append(raw[1])
        addresses.append(raw[2])
    for i in addresses:
        print(i)
    geolocator = Nominatim(user_agent='http')
    for ad in addresses:
        loc = geolocator.geocode(ad, timeout=30)
        if loc:
            print(type(loc.latitude))
            locations.append([loc.latitude, loc.longitude])
        else:
            locations.append([0.0, 0.0])
    for i, loc in enumerate(locations):
        lat, long = loc[0], loc[1]
        cur.execute('''UPDATE address SET latitude = %s WHERE address_id = %s''', (lat, addresses_id[i]))
        con.commit()
        cur.execute('''UPDATE address SET longitude = %s WHERE address_id = %s''', (long, addresses_id[i]))
        con.commit()


if __name__ == "__main__":
    exercise_1()

```

###### Result
It is the partial result of the our function:
![[Partial answer.png]]

The whole Table **address** after the calling the function:
[Address](file:////home/andrew/Desktop/Database_course/week09/exercise_1_function.csv)

___
## Excercise 2
___
I used the Python code to create the function *retrievecustomers*:
[Excercise 2](file:////home/andrew/Desktop/Database_course/week09/exercise_2_function.py)

The **SQL-query** for function creation is:
```sql
CREATE OR REPLACE FUNCTION retrievecustomers(start INTEGER, endd INTEGER)
    RETURNS SETOF customer AS                 
$$
BEGIN
	IF start <= 0
	THEN
		RAISE EXCEPTION '"start" must be positive';
		RETURN QUERY SELECT * FROM customer LIMIT 0;
	ELSIF endd > 600
	THEN
		RAISE EXCEPTION '"end" must be less or equal to 600';
		RETURN QUERY SELECT * FROM customer LIMIT 0;
	ELSIF start > endd
	THEN
		RAISE EXCEPTION '"start" must be less or equal to "end"';
		RETURN QUERY SELECT * FROM customer LIMIT 0;
	ELSE
		RETURN QUERY

		SELECT *
		FROM customer
		ORDER BY customer.address_id
		OFFSET (start-1) ROWS
		FETCH NEXT (endd-start+1) ROWS ONLY;
	END IF;
END;
$$
LANGUAGE plpgsql;
```

- **1st example**
```sql
SELECT * FROM retrievecustomers(1,7);
```
![[1-7.png]]
- **2nd example**
```sql
SELECT * FROM retrievecustomers(60,73);
```
![[60-73.png]]
- **3rd example - error**
```sql
SELECT * FROM retrievecustomers(90,73);
```
![[start>end.png]]
- **4th example - error**
```sql
SELECT * FROM retrievecustomers(90,730);
```
![[end>600.png]]