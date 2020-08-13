import csv
import numpy as np

rows = []

with open('data_freq3.csv') as csvFile:
    csv_reader = csv.reader(csvFile)
    pre_row = [0 for x in range(0, 2050)]
    for row in csv_reader:
        rows.append((np.array(pre_row, dtype=float) + np.array(row, dtype=float)) / 2)
        # csv_writer.writerow(str(temp_row))
        pre_row = row

np.savetxt("post_precess.csv", rows, delimiter=",", fmt="%.2f")
