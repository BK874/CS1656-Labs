#Brian Knotten
#CS166
#Lab 4
import pandas as pd

# Load dataset
df = pd.read_csv('http://data.cs1656.org/bank-data.csv')

# Task 1: Compute the mean income of males versus females

# Get the needed subset of the dataframe:
df_small = df[['sex', 'income']]

def get_mean(group):
    return group.mean()

# Groupby sex and apply the mean function
df_group = df_small['income'].groupby(df_small['sex']).apply(get_mean)
print(df_group)


# Task 2: Create a cross-tab of save_acct and mortgage
df_crosstab = pd.crosstab(df['save_act'], df['mortgage'], margins=True)
print(df_crosstab)

# Task 3: Convert the frequencies in cross-tab to percentages (Hint: use apply
# and indexing):
df_crosstabPercentages = pd.crosstab(df['save_act'], df['mortgage'],
                                     normalize='index', margins=True)
print("Using normalize parameter:\n")
print(df_crosstabPercentages)

# Using apply:
df_crosstabPercentages2 = pd.crosstab(df['save_act'], df['mortgage'],
                                      margins=True).apply(lambda x: x/len(df),
                                                          axis=1)
print("Using apply:\n")
print(df_crosstabPercentages)

