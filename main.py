import psycopg2
import sys
import time
import psycopg2.sql as sql
from scripts.csv_to_batches import csv_to_batches
from scripts.batches_to_table import batch_to_table
from scripts.small_funcs import *


def try_connect():
    for i in range(10):
        try:
            conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
            return conn
        except Exception as e:
            print(e)
            print("Trying to reconnect...")
            time.sleep(5)
    exit()


def batches_to_table(idx):
    errors = 0
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()
    while len(batches[idx:]) > 0:
        try:
            fields = sql.SQL(", ").join([sql.Identifier(i.lower()) for i in head])
            for batch in batches[idx:]:
                batch_to_table(batch, "zno_stats", fields, cursor)

                conn.commit()
                inserted_batches.append(batch)
                idx += 1
                state["insertions"] = f"{idx}/{len(batches)}"
                write_state(state)

        except (psycopg2.ProgrammingError, psycopg2.DataError) as e:
            conn.rollback()
            print(e)
            time.sleep(5)
            errors += 1

        except psycopg2.OperationalError as e:
            print(e)
            print("Trying to reconnect...")
            errors += 1
            time.sleep(5)
            if errors > 10:
                exit()
            conn = try_connect()
            cursor = conn.cursor()

    print("Completed.\n")


# state = {
#     "status": "EMPTY_DATABASE",
#     "batches": "",
#     "insertions": ""
# }
# write_state(state)

state = get_state()
print_state(state)

dbname, user, password, host, port = sys.argv[1:]

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

file_to_extcact_head = os.listdir(datasets_path)[0]
head = extract_header(os.path.join(datasets_path, file_to_extcact_head), ";")
head.insert(0, "year")
inserted_batches = []

if state["status"] == "EMPTY_DATABASE" or state["status"] == "BATCH_DIVISION_IS_NOT_FINISHED":
    state["status"] = "BATCH_DIVISION_IS_NOT_FINISHED"
    write_state(state)

    if os.path.exists(batches_path):
        files = os.listdir(batches_path)
        for file in files:
            os.remove(os.path.join(batches_path, file))
        os.rmdir(batches_path)

    print("Division into batches...")
    os.mkdir(batches_path)
    batch_division_time1 = time.time()
    datasets = os.listdir(datasets_path)

    ctr = 1
    for dataset in datasets:
        ctr = csv_to_batches(os.path.join(datasets_path, dataset), batches_path, batch_rows, encoding, ctr)
    batches = os.listdir(batches_path)

    state["batches"] = f"{len(batches)}"
    write_state(state)

    batches = sorted(batches, key=lambda x: extract_number(x))
    batches = [os.path.join(batches_path, batch) for batch in batches]
    batch_division_time2 = time.time()

    print("Completed.\n")

    state["status"] = "INSERTION_IS_NOT_FINISHED"
    write_state(state)

    print("Inseting into database...")

    sql_insetrion_time1 = time.time()
    create_query = extract_text(os.path.join(sql_queries_path, "CREATE.sql"))
    cursor.execute(create_query)
    conn.commit()

    inserted_batches = []
    batches_to_table(0)

    print("Completed.\n")
    sql_insetrion_time2 = time.time()
    state["status"] = "TABLE_POPULATED"
    write_state(state)

    query_execution_time1 = time.time()

    store_query(cursor, "query.sql", "query_data.csv", ["Регіон", "Рік", "Середній бал з англійскої мови"])

    query_execution_time2 = time.time()

    batch_division_time = seconds_to_minutes(batch_division_time2 - batch_division_time1)
    sql_insetrion_time = seconds_to_minutes(sql_insetrion_time2 - sql_insetrion_time1)
    query_execution_time = seconds_to_minutes(query_execution_time2 - query_execution_time1)

    logfile = os.path.join(logs_path, "time_log.log")

    with open(logfile, "w", encoding="UTF-8") as f:
        f.write("{}/{} files was inserted.\n".format(len(inserted_batches), len(batches)))
        f.write("Batch division: {}\n".format(batch_division_time))
        f.write("SQL insertion: {}\n".format(sql_insetrion_time))
        f.write("Query execution and writing to csv: {}\n".format(query_execution_time))

    print("Log file stored in {}.".format(logfile))


elif state["status"] == "INSERTION_IS_NOT_FINISHED":
    batches = os.listdir(batches_path)
    batches = sorted(batches, key=lambda x: extract_number(x))
    batches = [os.path.join(batches_path, batch) for batch in batches]

    (insetred, total) = get_splitted_nums(state["insertions"])
    batches_to_table(insetred)
    state["status"] = "TABLE_POPULATED"
    write_state(state)


elif state["status"] == "TABLE_POPULATED":
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()
    op = ""
    while op != "3":
        print_state(state)

        print("1. Execute sql query.\n"
              "2. Drop table.\n"
              "3. Exit.")

        op = input("Choose the option: ")
        if op == "1":
            store_query(cursor, "query.sql", "query_data.csv", ["Регіон", "Рік", "Середній бал з англійскої мови"])
        elif op == "2":
            cursor.execute("DROP TABLE zno_stats;")
            conn.commit()
            state["status"] = "EMPTY_DATABASE"
            state["batches"] = ""
            state["insertions"] = ""
            write_state(state)
            print("Table has dropped.")
            break
    cursor.close()
    conn.close()
