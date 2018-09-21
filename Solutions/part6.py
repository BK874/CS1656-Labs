import os
import csv

reader = open('hours.csv', 'rt')
csv_reader = csv.reader(reader)
for row in csv_reader:
	print (row)
reader.close()