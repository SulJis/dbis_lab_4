import csv
from scripts.constants import *


def batch_to_table(batch, fields, db):
    with open(batch, "r", encoding=encoding) as f:
        print("Inserting {}...".format(batch))
        reader = csv.reader(f, delimiter=";")
        docs_list = []
        for row in reader:
            doc = {}
            for key, value in zip(fields, row):
                if value.isdigit():
                    value = int(value)
                if value == "null":
                    value = None
                if "Ball100" in key and value is not None:
                    value = value.replace(",", ".")
                    value = float(value)
                doc.update({key: value})
            docs_list.append(doc)
        db.zno_data.insert_many(docs_list)
