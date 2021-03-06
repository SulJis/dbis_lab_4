import psycopg2
import csv
from psycopg2 import sql

conn = psycopg2.connect(dbname="postgres", user="postgres", password="vfrcbv2001", host="localhost", port="5000")
cursor = conn.cursor()

float_indexes = [18, 29, 39, 49, 59, 69, 79, 88, 98, 108, 118]

with open("data/Odata2020File.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    head = reader.__next__()
    for row in reader:

        for n, i in enumerate(row):
            if n in float_indexes:
                row[n] = row[n].replace(",", ".")
            if i == "null":
                row[n] = None

        insert = sql.SQL("INSERT INTO zno_stats ({fields}) VALUES ({values})").format(
            fields=sql.SQL(",").join([sql.Identifier(i.lower()) for i in head]),
            values=sql.SQL(", ").join(map(sql.Literal, row)))
        cursor.execute(insert)
        conn.commit()

cursor.close()
conn.close()