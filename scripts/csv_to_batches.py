import csv
import os
from scripts.small_funcs import extract_number


def csv_to_batches(file, batches_path, batch_rows, encoding, ctr=1):
    year = str(extract_number(file))

    with open(file, "r", encoding=encoding) as dataset:
        reader = csv.reader(dataset, delimiter=";")
        head = next(reader)
        row = next(reader)

        while row is not None:
            batch_file = "batch_{}.csv".format(ctr)
            with open(os.path.join(batches_path, batch_file), "w", newline="", encoding=encoding) as batch:
                writer = csv.writer(batch, delimiter=";")
                rows_writed = 0
                while rows_writed < batch_rows and row is not None:
                    row.insert(0, year)
                    writer.writerow(row)
                    rows_writed += 1
                    row = next(reader, None)
            ctr += 1
    return ctr
