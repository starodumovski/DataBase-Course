import psycopg2

def exercise_2():
    con = psycopg2.connect(database="dvdrental", user="postgres",
                           password="postgres", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    cur = con.cursor()
    cur.execute('DROP FUNCTION IF EXISTS retrievecustomers(start INTEGER, endd INTEGER);')
    cur.execute('''
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
                ''')
    con.commit()
    con.close()

if __name__ == "__main__":
    exercise_2()
