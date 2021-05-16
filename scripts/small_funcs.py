import csv
import re
import os
from scripts.constants import *


def extract_header(file, delimiter):
    with open(file, "r", encoding="cp1251") as f:
        reader = csv.reader(f, delimiter=delimiter)
        return next(reader)


def extract_number(string):
    return int(re.findall(r"\d+", string)[0])


def extract_text(file):
    with open(file, "r", encoding="UTF-8") as f:
        query = "".join(f.readlines())
        return query


def query_to_csv(file, data, head):
    with open(os.path.join(output_path, file), "w", encoding="UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(head)
        for obj in data:
            writer.writerow([obj["_id"]["Region"], obj["_id"]["Year"], obj["avgBall"]])


def seconds_to_minutes(seconds):
    minutes = int(seconds // 60)
    seconds = round(seconds % 60)
    return "{} minutes {} seconds".format(minutes, seconds)


def get_state():
    with open(os.path.join(logs_path, "status.csv"), "r") as f:
        reader = csv.DictReader(f)
        state = dict(next(reader))
        for key in state:
            if state[key] == "":
                state[key] = None
        return state


def write_state(state):
    with open(os.path.join(logs_path, "status.csv"), "w") as f:
        writer = csv.DictWriter(f, fieldnames=state.keys())
        writer.writeheader()
        writer.writerow(state)


def print_state(state):
    print(f"Status: {state['status']}\n"
          f"Created batches: {state['batches']}\n"
          f"Inserted batches: {state['insertions']}")


def get_splitted_nums(value):
    if not value:
        return [0, 0]
    else:
        nums = value.split("/")
        nums = [int(i) for i in nums]
        return nums


def is_zero_arr(arr):
    res = True
    for x in arr:
        if x != 0:
            res = False
            break
    return res


def store_query(db, result_file, pipeline, header):
    print("Executing a query...")
    query_result = db.zno_data.aggregate(pipeline)
    query_to_csv(result_file, query_result, header)
    print("Completed. CSV stored in {}.".format(result_file))
