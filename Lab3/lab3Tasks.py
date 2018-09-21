import numpy as np
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt

# Task 1:
# Run kmeans on http://data.cs1656.org/protein.csv using only the
# 'White Meat' and 'Red Meat' columns. Choose the initial value
# of k. Label all countries on the scatter plot
df = pd.read_csv('http://data.cs1656.org/protein.csv')

# Group data by the Country cluster label
df_group = df.groupby(['Country'])

# Fix random number generator see to allow replicated results
# and run with 4 clusters
k_means = cluster.KMeans(n_clusters=4, init = 'k-means++', random_state=5000)

# Run kmeans
k_means.fit(df[['RedMeat', 'WhiteMeat']])

# Visualize using scatter plot
fig = plt.figure(figsize = (16, 6))
plt.scatter(df['RedMeat'], df['WhiteMeat'], 60, c=k_means.labels_, alpha = 0.6)
plt.xlabel('Red Meat')
plt.ylabel('White Meat')
[plt.text(row.RedMeat, row.WhiteMeat, row.Country) for row in df.itertuples()]
plt.show()

# Task 2:
# Plot and observe the output with atleast three different values of k

# 5 Clusters:
k_means = cluster.KMeans(n_clusters=5, init = 'k-means++', random_state=5000)
k_means.fit(df[['RedMeat', 'WhiteMeat']])
fig = plt.figure(figsize = (16, 6))
plt.scatter(df['RedMeat'], df['WhiteMeat'], 60, c=k_means.labels_, alpha = 0.6)
plt.xlabel('Red Meat')
plt.ylabel('White Meat')
[plt.text(row.RedMeat, row.WhiteMeat, row.Country) for row in df.itertuples()]
plt.show()

# 2 Clusters:
k_means = cluster.KMeans(n_clusters=2, init = 'k-means++', random_state=5000)
k_means.fit(df[['RedMeat', 'WhiteMeat']])
fig = plt.figure(figsize = (16, 6))
plt.scatter(df['RedMeat'], df['WhiteMeat'], 60, c=k_means.labels_, alpha = 0.6)
plt.xlabel('Red Meat')
plt.ylabel('White Meat')
[plt.text(row.RedMeat, row.WhiteMeat, row.Country) for row in df.itertuples()]
plt.show()

# 3 Clusters:
k_means = cluster.KMeans(n_clusters=3, init = 'k-means++', random_state=5000)
k_means.fit(df[['RedMeat', 'WhiteMeat']])
fig = plt.figure(figsize = (16, 6))
plt.scatter(df['RedMeat'], df['WhiteMeat'], 60, c=k_means.labels_, alpha = 0.6)
plt.xlabel('Red Meat')
plt.ylabel('White Meat')
[plt.text(row.RedMeat, row.WhiteMeat, row.Country) for row in df.itertuples()]
plt.show()
# 3 Clusters seems to be the best - the clusters seem to match the most
# evenly with the actual grouping

# Task 3:
# Use the best k found, run kmeans using all columns for input features.
# Observe the differences in output labels and cluster centriods using all
# columns versus the output using two columns. Look at the output clusters
# and determine if it is better or worse to use more input features
k_meansAll = cluster.KMeans(n_clusters=3, init = 'k-means++', random_state=5000)
k_meansAll.fit(df[['RedMeat', 'WhiteMeat', 'Eggs', 'Milk', 'Fish', 'Cereals',
                'Starch', 'Nuts', 'Fr&Veg']])

# Look at cluster centroids
print(k_means.cluster_centers_, '\n', df_group[['RedMeat', 'WhiteMeat']].mean())
print(k_meansAll.cluster_centers_, '\n', df_group[['RedMeat', 'WhiteMeat',
                                                   'Eggs', 'Milk', 'Fish',
                                                   'Cereals','Starch', 'Nuts',
                                                   'Fr&Veg']].mean())

# Look at labels
print(k_means.labels_)
print(k_meansAll.labels_)
