import os
import json
import csv
from requests import get

# retrieving json file
response = get('http://data.cs1656.org/hours.json') 
hours = json.loads(response.content)

print('Converting to CSV and writing:')
with open('hours.csv', 'w') as outfile:
	writer = csv.writer(outfile)
	writer.writerow(["name","day","time"])
	for line in hours:
		writer.writerow([line["name"],
				line["day"],
				line["time"]])