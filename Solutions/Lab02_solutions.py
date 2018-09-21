
# coding: utf-8

# # CS 1656 – Introduction to Data Science (Fall 2018) 
# 
# ## Instructor: Alexandros Labrinidis / Teaching Assistant: Tahereh Arabghalizi
# 
# ### Additional Credits: Evangelos Karageorgos , Zuha Agha, Anatoli Shein, Phuong Pham
# ---
# In this lab you will be learning pandas dataframe basics and plotting in Python. Packages you will need are,
# * pandas
# * matplotlib
# 
# First step is to import the packages above. If import fails, it means that the package is not installed. 

# In[ ]:

import matplotlib.pyplot as plt
import pandas as pd
import datetime


# ## Tasks
# For your tasks, the input file is available at http://data.cs1656.org/top12cities.csv. The file consists of population density estimates and land area of several cities in USA. 
# 
# You need to read the file into a dataframe and perform the following three tasks during the lab. 
# 
# **Task 1************************************************************************************* 
# 
# Plot a scatter plot of with 'land area' on the x-axis and '2014 estimate' on the y-axis. After observing the plot, do you think the two variables are strongly or weakly correlated? Is the correlation positive or negative?

# In[ ]:

df1 = pd.read_csv('http://data.cs1656.org/top12cities.csv', sep=',',engine='python')

# Initializing a figure
fig = plt.figure(figsize=(10, 6))

# Adding labels using a subplot
ax = plt.subplot(111)
i = 0
for xy in zip(df1['2014 land area'],df1['2014 estimate']):
    ax.annotate(df1['City'][i], xy, textcoords='data')
    i+=1

# Plotting
plt.scatter(df1['2014 land area'],df1['2014 estimate'])

# Formatting graph
plt.xticks(rotation = 45, fontsize = 8)
plt.xlabel('City land area')
plt.ylabel('City population')
plt.title('Correlation between the land area of the city and its estimated population in 2014')

plt.show()


# **Task 2***************************************************************************************
# 
# Plot a bar plot showing each city's 2014 population estimate given by '2014 estimate' column. 

# In[ ]:

fig = plt.figure(figsize=(10, 6))
plt.bar(range(len(df1['City'])),df1['2014 estimate'], align = 'center')

# Formatting graph
plt.xticks(range(len(df1['City'])),df1['City'], rotation = 45, fontsize = 8)
plt.xlabel('City')
plt.ylabel('Population')
plt.title('City population estimate in 2014')

plt.show()


# **Task 3***************************************************************************************
# 
# Now that you plotted a simple bar plot, try plotting a grouped bar plot that shows both 2010 and 2014 estimate for each city on the same plot. This means that there will be two grouped bars per city on your graph. 

# In[ ]:

import numpy as np

fig = plt.figure(figsize=(10, 6))

x = np.arange(len(df1['City'].values))
y1 = df1['2014 estimate']
y2 = [int(i.replace(',','')) for i in df1['2010 Census']]

ax = plt.subplot(111)
ax1 = ax.bar(x-0.15, y1,width=0.3,color='b',align='center')
ax2 = ax.bar(x+0.15, y2,width=0.3,color='g',align='center')

# Formatting graph
plt.xticks(range(len(df1['City'])),df1['City'], rotation = 45, fontsize = 8)
plt.xlabel('City')
plt.ylabel('Population')
plt.title('2014 vs 2010 City Population')
plt.legend([ax1[0],ax2[0]], ['2014', '2010'])

plt.show()


# **Task 4***************************************************************************************

from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def minimumDistance(data, v):
    #note: since you might not be familiar with lambda functions, you can implement minimumDistance using a for loop.
    return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))

	
coordinateList = [{'lat': 40.444618, 'lon': -79.954707},
                {'lat': 40.440939,  'lon': -79.957623 },
                {'lat': 40.442062, 'lon': -79.956097},
    				{'lat': 40.40932, 'lon': -79.898685}]


v = {'lat': 40.442932, 'lon': -79.957651}
print(minimumDistance(coordinateList, v))



