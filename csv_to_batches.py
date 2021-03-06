import csv


def csv_to_batches(file, batches_path, batch_rows, ctr=1):
    with open(file, "r") as dataset:
        reader = csv.reader(dataset, delimiter=";")
        row = next(reader)
        while row is not None:
            print(ctr)
            with open("{}/batch_{}.csv".format(batches_path, ctr), "w") as batch:
                writer = csv.writer(batch, delimiter=";")
                rows_writed = 0
                while rows_writed < batch_rows and row is not None:
                    writer.writerow(row)
                    rows_writed += 1
                    row = next(reader, None)
            ctr += 1
    return ctr



