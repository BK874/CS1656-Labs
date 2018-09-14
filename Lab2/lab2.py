import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Creating a dataframe from Weather Undergraound Data
df = pd.read_csv('http://data.cs1656.org/KPIT_Aug17.csv',\
                 sep=',', engine='python', parse_dates=['EST'])

# Display the top 'n' rows of the datafram - default 5
print(df.head())
# Find all column of the dataframe  names and and their datatypes
print(df.dtypes)
# Acces Dataframe column like a dictionary
print(df['EST'].head())
# Access Dataframe column using dot - only if the column name is a
# valid variable name without any spacing
print(df.EST.head())
# Access multiple columns by passing list of column names
print(df[['EST', 'Mean TemperatureF']].head())

# Basic plotting
# p1 = plt.plot(df['EST'], df['MeanDew PointF'])
# p2 = plt.plot(df['EST'], df['Mean TemperatureF'])
# plt.legend([p1[0], p2[0]], ['Mean Dew Point', 'Mean Temperature'])
# plt.show()

# Formatting the plot nicely:
# Initializing a larger figure
fig = plt.figure(figsize = (10, 6))
# Plotting
p1 = plt.plot(df['EST'], df['MeanDew PointF'])
p2 = plt.plot(df['EST'], df['Mean TemperatureF'])
plt.legend([p1[0], p2[0]], ['Mean Dew Point', 'Mean Temperature'])
# Formatting graph
plt.xticks(rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Temperature')
plt.title('Mean Temperatures for August 2017')
# Save graph figure (always before show command - it claers the axis of the figure after displaying)
# plt.savefig("basic_plot.png")
plt.show()

# Bar Plot
fig = plt.figure(figsize=(10, 6))
plt.bar(range(len(df['EST'])), df['Mean Humidity'], align = 'center')
# Formatting graph
plt.xticks(range(len(df['EST'])), df['EST'].dt.strftime('%Y-%m-%d'),\
           rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Humidity')
plt.title('Mean Humidity for August 2017')
#plt.savefig("bar_plot.png")
plt.show()

# Plot both graphs above on the same figure using subplots
fig = plt.figure(figsize=(10, 16))
# Subplot of basic graph
plt.subplot(211)
p1 = plt.plot(df['EST'],df['MeanDew PointF'])
p2 = plt.plot(df['EST'],df['Mean TemperatureF'])
plt.legend([p1[0],p2[0]], ['Mean Dew Point', 'Mean Temperature'])
plt.xticks(rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Temperature')
plt.title('Mean Tempertaures for August 2017')
# Subplot of bar graph graph
plt.subplot(212)
plt.bar(range(len(df['EST'])),df['Mean Humidity'], align = 'center')
plt.xticks(range(len(df['EST'])), df['EST'].dt.strftime('%Y-%m-%d'),\
               rotation = 90, fontsize = 8)
plt.xlabel('Date')
plt.ylabel('Mean Humidity')
plt.title('Mean Humidity for August 2017')
#plt.savefig("subplot_basic_bar.png")
plt.show()
 
# Scatter plot
fig = plt.figure(figsize=(10, 6))
plt.scatter(df['Max TemperatureF'],df['Min TemperatureF'])
# Formatting graph
plt.xlabel('Max Temperture')
plt.ylabel('Min Temperature')
plt.title('Min and Max Temperature for August 2017')
plt.savefig("scatter_plot.png")
plt.show()


