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
