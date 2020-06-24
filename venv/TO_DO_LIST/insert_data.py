import os
import psycopg2

DB_NAME = "kbiwhvob"
DB_USER = "kbiwhvob"
DB_PASS = "OjXk60yHtFB9XDqpdIKlzkS2a1vH4_Ry"
DB_PORT = "5432"
DB_HOST = "ruby.db.elephantsql.com"

conn = psycopg2.connect(database=DB_NAME, password=DB_PASS, user=DB_USER,
                        host=DB_HOST, port=DB_PORT)

def insert(NEW_TASK, NEW_DATE):
    cur = conn.cursor()
    cur.execute("INSERT INTO TASK (task, expiration_date) VALUES(%s, %s)", (NEW_TASK, NEW_DATE))
    conn.commit()


def read():
    cur = conn.cursor()
    postgreSQL_select_Query = "select * from task"
    cur.execute(postgreSQL_select_Query)
    conn.commit()
    task_records = cur.fetchall()
    col1=list()
    col2=list()
    col3 = list()
    for row in task_records:
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])
    return ({"id": col1, "task": col2, "expiration_date": col3})

def delete(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM TASK WHERE ID=%s", (id,))
    conn.commit()
