# Brian Knotten
# CS1656
# Lab 11

import pandas as pd
import numpy as np
from sklearn import linear_model, tree, metrics
import matplotlib.pyplot as plt

# Example of linear regression on the bike sharing dataset
df = pd.read_csv('http://data.cs1656.org/bike_share.csv')
print(df.head())

# Randomly subsample dataset to select 1000 rows
df_subsample = df.sample(1000)
print(df_subsample.head())

# Split subsample into the training (90%) and test (10%) sets
# Using values to convert the Dataframe column into a numpy array and make it 2D
train = df_subsample.iloc[1:900]
train_x = train[['temp']].values
train_y = train[['cnt']].values

test = df_subsample.iloc[901:]
test_x = test[['temp']].values
test_y = test[['cnt']].values
print(type(train_x), type(train_y), type(test_x), type(test_y))

# Fit the linear regression model
# Create the linear regression object:
regr = linear_model.LinearRegression()
# Train the model on the training set
regr.fit(train_x, train_y)

# The coefficients of the estimated model are stored in the coeff attribute
print('Coefficients: \n', regr.coef_)

# Prediction: the model will take the temp attribute of the test data and make
# predictions on the cnt of people who are bike sharing
predict_y = regr.predict(test_x)
# Compare the predicted and actual values side by side
print(np.column_stack((predict_y, test_y)))

# Measure the diff between predicted and actual values via mean squared error
meansq_error = np.mean((predict_y - test_y) ** 2)
print("Mean squared error: %.2f" % meansq_error) # High = not good

# Visualize the differenve between the predictions and actual values
plt.scatter(test_x, test_y, color='black', linewidth=1)
plt.plot(test_x, predict_y, color='blue', linewidth=3)
plt.show()

# Example of binary classification using decision trees on the titanic survival
# dataset
dt = pd.read_csv('http://data.cs1656.org/titanic.csv')
print(dt.head())

# To fit the decision tree model, convert the categorical values into numerical
# values i.e. convert Sex into numerical values, as it is the only categorical
# attribute
dt['Sex'] = dt['Sex'].replace(['female', 'male'], [1, 2])
print(dt.head())

# Split data into test and train sets
dt_train_x = dt.iloc[:800][['Pclass', 'Sex', 'SibSp']].values
dt_train_y = dt.iloc[:800][['Survived']].values

dt_test_x = dt.iloc[801:][['Pclass', 'Sex', 'SibSp']].values
dt_test_y = dt.iloc[801:][['Survived']].values

# Fit the decision tree model onto the training set
clf = tree.DecisionTreeClassifier()
clf = clf.fit(dt_train_x, dt_train_y)

# Predict the test set
dt_predict_y = clf.predict(dt_test_x)
# Compare the predicted and actual values
print(np.column_stack((dt_predict_y, dt_test_y)))

# Measure the accuracy of the prediction
accuracy = metrics.accuracy_score(dt_test_y, dt_predict_y)
print(accuracy)
