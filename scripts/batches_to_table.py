import csv
import time

import psycopg2.sql as sql
from scripts.small_funcs import write_state
from scripts.constants import *


def batch_to_table(batch, table, fields, cur):
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
