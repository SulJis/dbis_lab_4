import os
import csv


def extract_header(file, delimiter):
    with open(file, "r", encoding="cp1251") as f:
        reader = csv.reader(f, delimiter=delimiter)
        return next(reader)


def extract_query(file):
    with open(file, "r", encoding="UTF-8") as f:
        query = "".join(f.readlines())
        return query


def query_to_csv(file, result, head):
    with open(file, "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(head)
        for row in result:
            writer.writerow(row)


def minutes_to_seconds(seconds):
    minutes = int(seconds // 60)
    seconds = round(seconds % 60)
    return "{} minutes {} seconds".format(minutes, seconds)

