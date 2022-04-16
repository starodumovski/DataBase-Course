import psycopg2
import pandas as pd
import geopy
from geopy.geocoders import Nominatim

con = psycopg2.connect(database="dvdrental", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")
print("Database opened successfully")
cur = con.cursor()


def retrieve_addresses():
    cur.execute('''SELECT address, city_id
    WHERE (city_id BETWEEN 400 AND 600) AND address LIKE '11%';''')

cur.execute('''
CREATE FUNCTION retrieve_addresses()
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

cur.callproc('retrieve_addresses')

m = cur.execute('''SELECT * FROM retrieve_addresses();
''')

data = pd.read_sql('SELECT * FROM retrieve_addresses();',con)
print(data)

cur.execute('ALTER TABLE address ADD COLUMN latitude TEXT')
cur.execute('ALTER TABLE address ADD COLUMN longitude TEXT')

print(data[0])


