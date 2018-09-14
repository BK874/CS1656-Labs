import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Create a dataframe from the top12cities
df = pd.read_csv('http://data.cs1656.org/top12cities.csv',\
                 sep=',', engine='python')

# Task 3: Plot a grouped bar plot that shows both 2010
# and 2014 estimate for each city on the same plot
# i.e. there will be two grouped bars per city on your graph

# Plot
fig, ax = plt.subplots(figsize=(10, 5)) # Plotting the bars
pos = list(range(len(df['City']))) # Setting position for the bars
width = 0.25 # Setting the width for the bars
plt.bar(pos, df['2014 estimate'], width,color='b', label='2014')
plt.bar([p + width for p in pos], df['2010 Census'], width*2, color='r',
        label='2010')
# Format
plt.xticks(range(len(df['City'])), df['City'], rotation = 90, fontsize = 8)
plt.xlabel('City')
plt.ylabel('Population')
plt.title('2014 Estimate vs 2010 Census per City')
plt.show()
