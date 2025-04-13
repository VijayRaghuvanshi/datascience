#Simple Liner Regression
#Import Pandas library
import pandas as pd

#Read csv file using Pandas
dataset = pd.read_csv('01Students.csv')
df = dataset.copy()

# Split data vertically in X and Y

X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

# Split the dataset by rows into training and test datasets

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = \
    train_test_split(X,Y, test_size=0.3, random_state=1234)
    
# Create and train the simple linear regression model
from sklearn.linear_model import LinearRegression

# Create Regressor
std_reg = LinearRegression()

# Train or fit the traing data
std_reg.fit(x_train, y_train)

# Lets now predict the values of Y from test data
y_predict = std_reg.predict(x_test)


# R-squared and equation of the line
slr_score = std_reg.score(x_test, y_test)

# coefficient of the line

slr_coefficient = std_reg.coef_
slf_intercept = std_reg.intercept_
 
# Equation of the line
# y = 34.27 + 5.02 * x

# How much error our model had made

#RMSE -Root Mean Squared Error

from sklearn.metrics import mean_squared_error
import math

slr_rmse = math.sqrt(mean_squared_error(y_test, y_predict))


# Plotting the result using matplotlib
import matplotlib.pyplot as plt

plt.scatter(x_test, y_test)

# trendline of the prediction
plt.plot(x_test, y_predict)
plt.ylim(ymin=0)
plt.show()

