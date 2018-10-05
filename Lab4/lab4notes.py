import pandas as pd

# Load dataset
df = pd.read_csv('http://data.cs1656.org/coffee-chain.csv')
print(df.head())

# Get desired subset of the dataframe
df_small = df[['Area Code','Market', 'Market Size', 'Product', 'Product Line', 'Product Type', 'State', 'Type', 'Profit', 'Total Expenses']]
print(df_small.head())

# This is slicing - uses [] operator to select a set of rows and/or columns
# To slice out a set of rows, use syntax: data[start:stop]
# In pandas, start bound is included in the output
print(df_small[0:3])

# Note that this doesn't not create a copy of df_small, it creates a new variable
# and referes it to the same object that df_small refers to. To copy, use
# y = x.copy()

# Select specific ranges of data in both the row and column directions using label
# or integer based indexing: loc (index via labes, ints, or mixed) and iloc (index
# via integers only
print(df_small.loc[0:3, 'Market': 'Product'])
print(df_small.iloc[0:4, 1:4])
# Note that loc is inclusive but iloc is exclusive of the end index

# Cross tabulation computes a frequency table of two or more factors
# Two-variable cross-tab
df_crosstab = pd.crosstab(df_small['Market'], df_small['Market Size'], margins=True)
print(df_crosstab)

print(type(df_crosstab))

# Check if value count of one dimension's totals matches
print(pd.value_counts(df_small['Market Size']))

# Three-variable cross-tab
print(pd.crosstab(df["Product Type"], [df["Market"], df["Market Size"]], margins=True))

# Bin data into categories by specifying bin widths
# Define equal width bins: 4 bins from -800 to -400, -400 to 0, 0 to 400,
# 400 to 800
bins = [-800,-400, 0, 400, 800]
group_names = ['Low', 'Okay', 'Good', 'Great']
# Bin data into categories and add to dataframe as column
df_small['Categories'] = pd.cut(df_small['Profit'], bins=bins, labels=group_names)
print(df_small.head(20))

# Find value counts for each bin category using value_counts
print(pd.value_counts(df_small['Categories']))

# Specify quantiles we want to calculate
quants = [0.0, 0.05, 0.25, 0.5, 0.75, 0.95, 1.0]
# Compute quantiles of Profit and Total Expenses
q = df_small[['Profit', 'Total Expenses']].quantile(quants)
print(q)

# Groupby allows grouping or clustering the dataframe by a particular attribute.
# Apply can be used to apply a function to a group or the entire dataframe.
# Define function we want to apply:
def get_stats(group):
    return{'min': group.min(), 'max': group.max(), 'count': group.count(),
           'mean': group.mean(), 'sum': group.sum()}
# Apply to Dataframe or grouping of the dataframe
df_group = df_small['Profit'].groupby(df_small['Categories']).apply(get_stats)
print(df_group)
# Width format fixed by unstack()
print(df_group.unstack())

# Pandas allows nested sorted over multiple columns of the dataframe:
data_sorted = df_small.sort_values(['Total Expenses', 'Profit'], ascending=False)
print(data_sorted[['Total Expenses', 'Profit']].head(20))
