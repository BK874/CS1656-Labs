# Brian Knotten
# CS1656
# Lab 9

import json
from datetime import datetime, timedelta, date
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Use Allegheny County Restaurant/Food Facility Inspection Violation Dataset
wprdc_api_endpoint = "https://data.wprdc.org/api/3/action/datastore_search_sql"

# ID for database table
resource_id = "1a1329e2-418c-4bd3-af2c-cc334e7559af"

# Retreive the data from 90 days ago
start_date = datetime.now() - timedelta(days = 180)

# Convert the date into a string format accepted by the data center
start_str = start_date.strftime("%Y-%m-%d")

# Task 1: Find the top 30 restaurants in Pittsburgh with the
# maximum number of violations

query = """
SELECT "FACILITY_NAME", COUNT("FACILITY_NAME") AS CT
FROM "{}"
WHERE "INSPECT_DT" >= '{}' AND "CITY" = '{}' AND "RATING" = '{}'
GROUP BY "FACILITY_NAME"
ORDER BY CT DESC LIMIT 30
;""".format(resource_id, start_str, "Pittsburgh", "V")
response = requests.get(wprdc_api_endpoint, {'sql': query})
df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])
print(df)

# Task 2: Find the category descriptions and their high, medium, low risk ratings
# for all violations at facilities that start with "Pitt" over the past six months

# query = """
# SELECT "FACILITY_NAME", "DESCRIPTION_NEW", "RATING", "HIGH", "MEDIUM", "LOW"
# FROM "{}"
# WHERE "FACILITY_NAME" LIKE 'PITT%' AND "INSPECT_DT" >= '{}' AND "CITY" = '{}'
# ;.""".format(resource_id, start_str, "Pittsburgh")
# response = requests.get(wprdc_api_endpoint, {'sql': query})
# print(json.loads(response.text))
# df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])
# print(df)



query = """
SELECT "Facility Name", COUNT("Facility Name") AS count
FROM "{}"
WHERE
    "Facility Name" LIKE '% Pitt %'
    OR "Facility Name" LIKE 'Pitt %'
    OR "Facility Name" LIKE '% Pitt'
    OR "Facility Name" = 'Pitt'
    AND "Inspect Dt" >= '{}' AND "City" = '{}' AND "Rating" = '{}'
GROUP BY "Facility Name"
ORDER BY count DESC LIMIT 20
;""".format(resource_id, start_str, "Pittsburgh", "V")

response = requests.get(wprdc_api_endpoint, {'sql': query})
print(json.loads(response.text))
df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])


