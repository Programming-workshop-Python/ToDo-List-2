import os
import psycopg2

DB_NAME = "kbiwhvob"
DB_USER = "kbiwhvob"
DB_PASS = "OjXk60yHtFB9XDqpdIKlzkS2a1vH4_Ry"
DB_PORT = "5432"
DB_HOST = "ruby.db.elephantsql.com"


try:
    conn = psycopg2.connect(database = DB_NAME, password = DB_PASS, user = DB_USER,
                        host = DB_HOST, port = DB_PORT)
    print('ok')
except:
    print('bad')


cur = conn.cursor()
cur.execute("""
CREATE TABLE TASK
(
id SERIAL PRIMARY KEY,
TASK TEXT NOT NULL,
EXPIRATION_DATE TEXT NOT NULL
) 


""")

conn.commit()
print('Created')