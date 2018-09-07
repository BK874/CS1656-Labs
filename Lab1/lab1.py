import os
import json
from requests import get
import csv

file_in = input('Enter name of input file: ')
if os.path.isfile(os.path.join(os.getcwd(),file_in)):
    with open(file_in, "r+") as f:
        for line in f:
            print(line)
        f.writelines("Yay! Written to file on Friday, 9/7/18 :D \n")
        f.close()

zipCodes = [60290, 60601, 60602, 60603, 60604, 60605, 60606]
f = open('example2.json', 'w')
json.dump(zipCodes, f)
f.close()
f = open('example2.json','r')
zipCodes2 = json.load(f)
f.close()
print("Checking zipcodes...")
print(zipCodes == zipCodes2)

print('Downloading JSON file and printing entire file: ')
response = get('http://data.cs1656.org/hours.json')
print(response.content)
print('Loading as JSON and iterating one line at a time:')
hours = json.loads(response.content)
print(hours)
print('\nIterating over JSON: ')
for line in hours:
    print (line)


#Parts 4-7 - on your own
#Part 4: convert downloaded JSON to .csv
with open('hours.csv', 'w') as h:
    fieldnames = ['name', 'day', 'time']
    hour_writer = csv.DictWriter(h, fieldnames=fieldnames)
    hour_writer.writeheader()
    for line in hours:
        hour_writer.writerow(line)
h.close()

#Part 5: read csv and display raw contents
with open('hours.csv') as r:
    raw = r.read()
print(raw)
r.close()

#Part 6: read csv and display contents one row at a time
with open('hours.csv') as r:
    csvreader = csv.reader(r, delimiter = ',', quotechar = ':')
    for row in csvreader:
        print(row)
r.close()

#Part 7: read csv and display contents one row and one field at a tiem
with open('hours.csv') as r:
    csvreader = csv.reader(r, delimiter = ',', quotechar = ':')
    for row in csvreader:
        print("Row: ")
        for field in row:
            print("Field: ")
            print(field)
r.close()
