import csv
import matplotlib.pyplot as pl
import numpy as np

f = open('data.csv')

csv_reader = csv.reader(f)
c = 0
low = []
high = []
for row in csv_reader:
    c += 1
    if c>=5000 and c< 10000:
        low.append(int(row[0]))
        high.append(int(row[1]))


x = np.arange(5000,10000)
pl.subplot(211)
pl.plot(x, low)
pl.subplot(212)
pl.plot(x, high)
pl.xlabel("index")
pl.show()
