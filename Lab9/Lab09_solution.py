
# coding: utf-8

# # CS 1656 – Introduction to Data Science 
# 
# ## Instructor: Alexandros Labrinidis / Teaching Assistant: Tahereh Arabghalizi
# ### Additional credits: Evangelos Karageorgos, Zuha Agha, Anatoli Shein, Phuong Pham
# ## Lab 09: SQL via Data API
# ---
# In this recitation, you will execute SQL queries on real data by connecting to the open data portal of [Western Pennsylavnia Regional Data Center](https://www.wprdc.org/) and requesting data via API calls.  

# In[1]:


import json
from datetime import datetime, timedelta
import requests
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')


# We will be using Allegheny County Restaurant/Food Facility Inspection Violation Dataset found here https://data.wprdc.org/dataset/allegheny-county-restaurant-food-facility-inspection-violations. This dataset contains violation data from actual routine inspections by one of health department staff's members for the last two years. It should be fun to find out inspection results for places where we eat in Pittsburgh! =)

# In[2]:


wprdc_api_endpoint = "https://data.wprdc.org/api/3/action/datastore_search_sql"

# id for database table
resource_id = "1a1329e2-418c-4bd3-af2c-cc334e7559af"

# Get the date from 180 days ago)
start_date = datetime.now() - timedelta(days=180)

# Convert to a string the format the the data center accepts (yyyy-mm-dd)
start_str = start_date.strftime("%Y-%m-%d")

# SQL query we'll use in API call to request data
query = """
SELECT *
FROM "{}"
WHERE "Inspect Dt" >= '{}' AND "City" = '{}'
;""".format(resource_id, start_str, "Pittsburgh")

# Make WPRDC API Call
response = requests.get(wprdc_api_endpoint, {'sql': query})

# Parse response JSON into python dictionary
response_data = json.loads(response.text)

# Convert dictionary to dataframe
df = pd.DataFrame.from_dict(response_data['result']['records'])

# Print the number of rows
print(df.shape[0], "rows total")

df.head()


# Details of dataset attributes are below. (Taken from https://data.wprdc.org/dataset/allegheny-county-restaurant-food-facility-inspection-violations/resource/8744b4f6-5525-49be-9054-401a2c4c2fac)
# 
# ![title](attribs.png)

# ## Queries
# 
# __Q1) Find all unique decription categories of violation in Pittsburgh restaurants over the past six months.__

# In[3]:


query = """
SELECT DISTINCT "Description New"
FROM "{}"
WHERE "Inspect Dt" >= '{}' AND "City" = '{}'
;""".format(resource_id, start_str, "Pittsburgh")

response = requests.get(wprdc_api_endpoint, {'sql': query})

df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])

df


# __Q2) Find restaurants in Pittsburgh with no violations in at least one decription category over the past six months.__

# In[4]:


query = """
SELECT "Facility Name", COUNT("Facility Name")
FROM "{}"
WHERE "Inspect Dt" >= '{}' AND "City" = '{}' AND "Rating" <> '{}'
GROUP BY "Facility Name"
;""".format(resource_id, start_str, "Pittsburgh", "V")

response = requests.get(wprdc_api_endpoint, {'sql': query})

df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])

df


# ### Tasks
# 
# __T1) Find top 30 restaurants in Pittsburgh with maximum number of violations.__

# In[5]:


query = """
SELECT "Facility Name", COUNT("Facility Name") AS CT
FROM "{}"
WHERE "Inspect Dt" >= '{}' AND "City" = '{}' AND "Rating" = '{}'
GROUP BY "Facility Name"
ORDER BY CT DESC LIMIT 30
;""".format(resource_id, start_str, "Pittsburgh", "V")

response = requests.get(wprdc_api_endpoint, {'sql': query})

df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])

df


# Lets look more closely into the inspection results of Pitt facilities.
# 
# __T2) Find the category descriptions and their high, medium, low risk ratings for all violations at facilities that start with 'Pitt' over the past six months.__

# In[6]:


query = """
SELECT "Facility Name", "Description New", "Rating", "High", "Medium", "Low"
FROM "{}"
WHERE "Facility Name" LIKE 'Pitt%' AND "Inspect Dt" >= '{}' AND "City" = '{}'
;""".format(resource_id, start_str, "Pittsburgh")

response = requests.get(wprdc_api_endpoint, {'sql': query})
json.loads(response.text)

df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])

df


# Now lets look at all facilities that contain word 'Pitt'.
# 
# __T3) Find the category descriptions and their high, medium, low risk ratings for all violations at all facilities that have word 'Pitt' in their name over the past six months. Note that results that contain word 'Pitt' as part of another word (e.g. 'Pittsburgh') should not be included__

# In[7]:


query = """
SELECT "Facility Name", "Description New", "Rating", "High", "Medium", "Low"
FROM "{}"
WHERE
    "Facility Name" LIKE '% Pitt %'
    OR "Facility Name" LIKE 'Pitt %'
    OR "Facility Name" LIKE '% Pitt'
    OR "Facility Name" = 'Pitt'
    AND "Inspect Dt" >= '{}' AND "City" = '{}'
;""".format(resource_id, start_str, "Pittsburgh")

response = requests.get(wprdc_api_endpoint, {'sql': query})
json.loads(response.text)

df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])

df


# __T4) Find top 20 facilities that have word 'Pitt' in their name and have the highest counts of violations over the past six months.__

# In[8]:


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
df = pd.DataFrame.from_dict(json.loads(response.text)['result']['records'])

df


# Let's make a bar graph of these counts now
# 
# __T5) Create a bar graph of the counts from T4).__

# In[9]:


df['count'] = df['count'].astype(float)
ax = df[['Facility Name','count']].plot(kind='bar',             title ="Violations Plot", figsize=(10, 5), legend=True, fontsize=12)
ax.set_xticklabels(df['Facility Name'], rotation = 90)
ax.set_xlabel("Pitt facilities", fontsize=12)
ax.set_ylabel("Number of violations", fontsize=12)
#plt.show()
plt.savefig('recitation8.png')

