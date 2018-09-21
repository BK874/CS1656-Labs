import numpy as np
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt

# Read input file into dataframe
df = pd.read_csv('http://data.cs1656.org/crime_data.csv')
print(df.head())

# Groud data by cluster label and compute mean of each cluster across all
# columns - will be user to compare the output of our kmeans clustering
df_group = df.groupby(['CrimeCluster'])
print(df_group.mean())

# Fix random number generator see to allow replicated results
# and run with 4 clusters
k_means = cluster.KMeans(n_clusters=4, init = 'k-means++', random_state=5000)

# Run kmeans
print(k_means.fit(df[['Murder', 'Assault']]))

# Look at kmeans output via cluster centroids (mean of all data smaples within
# a cluster.
print(k_means.cluster_centers_, '\n', df_group[['Murder','Assault']].mean())

# The cluster_centers are numpy arrays; n-dimensional arrays in python.
# They are useful for linear algebra, especially at a large scale
print(type(k_means.cluster_centers_))

# View predicted cluster labels
print(k_means.labels_)

# Reorder our predicted cluster labels
labels_reorder = np.choose(k_means.labels_, [1, 4, 3, 2])
print(labels_reorder)

# Add our predicted labels as a column in the data frame in order to
# compoare predicted cluster labels with our ground truth cluster labels
df['PredictedCluster'] = pd.Series(labels_reorder, index=df.index)
print(df.head())

# Check if CrimeCluster and PredictedCluster have any rows where they do not match
print(df[df['PredictedCluster'] != df['CrimeCluster']])

# Visualize clusters using scatter plots
# fig = plt.figure(figsize=(16,6))
# plt.scatter(df['Assault'],df['Murder'],60,c=k_means.labels_, alpha = 0.6)
# plt.xlabel('Assault')
# plt.ylabel('Murder')
# [plt.text(row.Assault, row.Murder, row.State) for row in df.itertuples()]
# plt.show()

# Kmeans with 3 clusters now
# k_means = cluster.KMeans(n_clusters=3, init='k-means++', random_state=5000)
# k_means.fit(df[['Murder', 'Assault']])
# fig = plt.figure(figsize=(16,6))
# plt.scatter(df['Assault'],df['Murder'],60,c=k_means.labels_, alpha = 0.6)
# plt.xlabel('Assault')
# plt.ylabel('Murder')
# [plt.text(row.Assault, row.Murder, row.State) for row in df.itertuples()]
# plt.show()

# Kmeans with 2 clusters
k_means = cluster.KMeans(n_clusters=2, init='k-means++', random_state=5000)
k_means.fit(df[['Murder', 'Assault']])
fig = plt.figure(figsize=(16,6))
plt.scatter(df['Assault'],df['Murder'],60,c=k_means.labels_, alpha = 0.6)
plt.xlabel('Assault')
plt.ylabel('Murder')
[plt.text(row.Assault, row.Murder, row.State) for row in df.itertuples()]
plt.show()

