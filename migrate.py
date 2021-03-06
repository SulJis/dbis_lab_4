import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="vfrcbv2001", host="localhost", port="5000")
cursor = conn.cursor()

conn.commit()

cursor.close()
conn.close()