import psycopg2
import csv
from psycopg2 import sql
from scripts.small_funcs import extract_header, extract_query, query_to_csv, minutes_to_seconds
from scripts.csv_to_batches import csv_to_batches
import sys
import time
import os
import re

total_time1 = time.time()
dbname, user, password, host, port = sys.argv[1:]

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

float_indexes = [18, 29, 39, 49, 59, 69, 79, 88, 98, 108, 118]

encoding = "cp1251"
batches_path = "batches"
datasets_path = "data"
sql_queries_path = "sql_queries"
logs_path = "logs"
query_results_path = "query_results"
batch_rows = 1000

file_to_extcact_head = os.listdir(datasets_path)[0]
head = extract_header(os.path.join(datasets_path, file_to_extcact_head), ";")
inserted_batches = []


def batches_to_sqltable(table, head, batches, db_data):
    try:
        conn, cur = db_data
        fields = sql.SQL(", ").join([sql.Identifier(i.lower()) for i in head])
        for batch in batches:
            with open(batch, "r", encoding=encoding) as f:
                print("Inserting {}...".format(batch))
                reader = csv.reader(f, delimiter=";")

                for row in reader:
                    for n, i in enumerate(row):
                        if n in float_indexes:
                            row[n] = row[n].replace(",", ".")
                        if i == "null":
                            row[n] = None
                    insert = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values});").format(
                        table=sql.SQL(table),
                        fields=fields,
                        values=sql.SQL(", ").join(map(sql.Literal, row)))

                    cur.execute(insert)
                conn.commit()
                inserted_batches.append(batch)

    except Exception as e:
        print("Error caught.")
        print(e)
        print("last batch: {}".format(inserted_batches[-1]))
        time.sleep(5)


create_query = extract_query(os.path.join(sql_queries_path, "CREATE.sql"))
cursor.execute(create_query)
conn.commit()

print("Division into batches...")
os.mkdir(batches_path)
batch_division_time1 = time.time()
datasets = os.listdir(datasets_path)
ctr = 1
for dataset in datasets:
    ctr = csv_to_batches(os.path.join(datasets_path, dataset), batches_path, batch_rows, encoding, ctr)

batches = os.listdir(batches_path)
batches = sorted(batches, key=lambda x: int(re.findall(r"\d+", x)[0]))
batches = [os.path.join(batches_path, batch) for batch in batches]
batch_division_time2 = time.time()
print("Completed.\n")

print("Inseting into database...")
sql_insetrion_time1 = time.time()
ctr = 1
idx = 0
while ctr < 100 and len(batches[idx:]) > 0:
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        batches_to_sqltable("zno_stats", head, batches[idx:], [conn, cursor])
        idx = len(inserted_batches)
    except Exception as e:
        print("Trying to reconnect...")
        time.sleep(5)
        ctr += 1

print("Completed.\n")
sql_insetrion_time2 = time.time()

query_execution_time1 = time.time()
print("Executing a query...")
avg_marks_query = extract_query(os.path.join("sql_queries", "query.sql"))
cursor.execute(avg_marks_query)
query_result = cursor.fetchall()
os.mkdir(query_results_path)
result_file = os.path.join(query_results_path, "query_data.csv")
query_to_csv(result_file, query_result, ["Регіон", "Середній бал з англійскої мови"])
print("Completed. CSV stored in {}.".format(result_file))
query_execution_time2 = time.time()

cursor.close()
conn.close()

total_time2 = time.time()

total_time = minutes_to_seconds(total_time2 - total_time1)
batch_division_time = minutes_to_seconds(batch_division_time2 - batch_division_time1)
sql_insetrion_time = minutes_to_seconds(sql_insetrion_time2 - sql_insetrion_time1)
query_execution_time = minutes_to_seconds(query_execution_time2 - query_execution_time1)

os.mkdir(logs_path)
logfile = os.path.join(logs_path, "time_log.log")

with open(logfile, "w", encoding="UTF-8") as f:
    f.write("{}/{} files was inserted.\n".format(len(inserted_batches), len(batches)))
    f.write("Batch division: {}\n".format(batch_division_time))
    f.write("SQL insertion: {}\n".format(sql_insetrion_time))
    f.write("Query execution and writing to csv: {}\n".format(query_execution_time))
    f.write("Total time: {}\n".format(total_time))

print("Log file stored in {}.".format(logfile))
