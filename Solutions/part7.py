import os
import csv

reader = open('hours.csv', 'rt')
csv_reader = csv.reader(reader)
for row in csv_reader:
	for field in row:
		print (field)
reader.close()