import csv


def csv_to_batches(file, batches_path, batch_rows, encoding, ctr=1):
    with open(file, "r", encoding=encoding) as dataset:
        reader = csv.reader(dataset, delimiter=";")
        head = next(reader)
        row = next(reader)
        while row is not None:
            with open("{}/batch_{}.csv".format(batches_path, ctr), "w", newline="", encoding=encoding) as batch:
                writer = csv.writer(batch, delimiter=";")
                rows_writed = 0
                while rows_writed < batch_rows and row is not None:
                    writer.writerow(row)
                    rows_writed += 1
                    row = next(reader, None)
            ctr += 1
    return ctr

