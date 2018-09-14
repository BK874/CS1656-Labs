import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Create a dataframe from the top12cities
df = pd.read_csv('http://data.cs1656.org/top12cities.csv',\
                 sep=',', engine='python')

# Task 1: plot a scatter plot with 'land area' on the x-axis and '2014 estimate'
# on the y-axis. Are the variables strongly or weakly correlated?
# Is the correlation positive or negative?

# Init large plot
fig = plt.figure(figsize = (10, 6))
# Plot
plt.scatter(df['2014 land area'], df['2014 estimate'])
# Format
plt.xlabel('2014 land area')
plt.ylabel('2014 estimate')
plt.title('Test')
#plt.show()
# I don't think they are correlated at all

# Task 2: Plot a bar graph showing each city's 2014 population estimate
# given by the '2014 estimate' column

# Init large plot
fig = plt.figure(figsize = (10, 6))
# Plot
plt.bar(range(len(df['City'])), df['2014 estimate'], align = 'center')
# Format
plt.xticks(range(len(df['City'])), df['City'], rotation = 90, fontsize = 8)
plt.xlabel('City')
plt.ylabel('2014 Estimate')
plt.title('2014 Estimate per City')
#plt.show()

# Task 3: Plot a grouped bar plot that shows both 2010
# and 2014 estimate for each city on the same plot
# i.e. there will be two grouped bars per city on your graph

# Plot
fig, ax = plt.subplots(figsize=(10, 5)) # Plotting the bars
pos = list(range(len(df['City']))) # Setting position for the bars
width = 0.25 # Setting the width for the bars
plt.bar(pos, df['2014 estimate'], width,color='b')
plt.bar([p + width for p in pos], df['2010 Census'], width, color='r')
# Format
plt.xticks(range(len(df['City'])), df['City'], rotation = 90, fontsize = 8)
plt.xlabel('City')
plt.ylabel('Population')
plt.title('2014 Estimate vs 2010 Census per City')
plt.show()
