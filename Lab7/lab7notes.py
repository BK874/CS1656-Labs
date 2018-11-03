# Brian Knotten
# CS1656
# Lab 7

import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean, cityblock, cosine
from scipy.stats import pearsonr

# Will walk through a toy example for user-based recommendation

# Data input
df = pd.read_csv('http://data.cs1656.org/movies_example.csv')
print(df)

# Two ways to access dataframes:
# First way:
print(df[df['Name'] == 'The Matrix'])
# Second way:
print(df.iloc[0])

# Use notnull() to exclude missing values or NaNs in a dataframe
print(df['Frank'].notnull())
print(df['Elaine'].notnull())
# May also perform logical ops on the returned booleans
print(df['Frank'].notnull() & df['Elaine'].notnull())
# Can also select a subset of rows and columns where the boolean value is True
df_notmissing = df[['Frank', 'Elaine']][df['Frank'].notnull() & df['Elaine'].notnull()]
print(df_notmissing)
      
# Different similarity metrics: Euclidean, Manhattan, Pearson Corr., and Cosine
# Euclidean:
sim_weights = {}
for user in df.columns[1:-1]:
    df_subset = df[['Frank', user]][df['Frank'].notnull() & df[user].notnull()]
    dist = euclidean(df_subset['Frank'], df_subset[user])
    sim_weights[user] = 1.0 / (1.0 + dist)
print("Similarity weights: %s" % sim_weights)

# Predict Frank's rating for 'The Matrix'
# First, get all ratings for the movie by accessing a row of the dataframe and
# slicing the columns of the ratings needed indicated by the index [1:-1].
ratings = df.iloc[0][1:-1]
print(ratings)
# Find predicted rating by multiplying each user weight with its corresponding rating for the movie matrix
predicted_rating = 0.0
weights_sum = 0.0
for user in df.columns[1:-1]:
    predicted_rating += ratings[user] * sim_weights[user]
    weights_sum += sim_weights[user]
predicted_rating /= weights_sum
print("Predicted rating: %f" % predicted_rating)

# Manhattan (Cityblock)
# Repeat, but use Manhattan distance.
sim_weights = {}
for user in df.columns[1:-1]:
    df_subset = df[['Frank', user]][df['Frank'].notnull() & df[user].notnull()]
    dist = cityblock(df_subset['Frank'], df_subset[user])
    sim_weights[user] = 1.0 / (1.0 + dist)
print("Similarity weights: %s" % sim_weights)

predicted_rating = 0
weights_sum = 0.0
ratings = df.iloc[0][1:-1]
for user in df.columns[1:-1]:
    predicted_rating += ratings[user] * sim_weights[user]
    weights_sum += sim_weights[user]
predicted_rating /= weights_sum
print("Predicted rating: %f" % predicted_rating)

# Pearson Correlation Coefficient
sim_weights = {}
for user in df.columns[1:-1]:
    df_subset = df[['Frank',user]][df['Frank'].notnull() & df[user].notnull()]
    sim_weights[user] = pearsonr(df_subset['Frank'], df_subset[user])[0]
print ("similarity weights: %s" % sim_weights)


predicted_rating = 0.0
weights_sum = 0.0
ratings = df.iloc[0][1:-1]
for user in df.columns[1:-1]:
# Prevent NaN results from dividing by 0:
    if(not np.isnan(sim_weights[user])):
        predicted_rating += ratings[user] * sim_weights[user]
        weights_sum += sim_weights[user]
predicted_rating /= weights_sum
print("Predicted rating: %s" % predicted_rating)
