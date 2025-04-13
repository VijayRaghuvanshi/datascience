# Bike Sharing Demand prediction Project for the hourly dataset
#
#
# Pre-requisites
# - Knowledge of basic Python
# - Statistics
# - Data Processing
# - Multiple Linear Regression


#--------------------------------
# Step 0 -Import Libraries
#--------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


#--------------------------------
# Step 1 - Read the data
#--------------------------------
bikes = pd.read_csv('hour.csv')


#-----------------------------------------------
# Step 2 - Prelim Analysis and Feature Selection
#-----------------------------------------------
#
bikes_prep = bikes.copy()
bikes_prep = bikes_prep.drop(['index', 'date','casual','registered'],axis=1)


# Basics checks of missing values
bikes_prep.isnull().sum()


# Visualise the data using pandas histogram
#bikes_prep.hist(rwidth=0.9)
#plt.tight_layout()


#-----------------------------------------------
# Step 3 - Data Visualization
#-----------------------------------------------
#
#Visualize the continous features vs demand
plt.subplot(2,2,1 )
plt.title('Temperature vs Demand')
plt.scatter(bikes_prep['temp'], bikes_prep['demand'], s=2, c='g')

plt.subplot(2,2,2 )
plt.title('aTemp vs Demand')
plt.scatter(bikes_prep['atemp'], bikes_prep['demand'], s=2, c='b')


plt.subplot(2,2,3 )
plt.title('Humidity vs Demand')
plt.scatter(bikes_prep['humidity'], bikes_prep['demand'], s=2, c='m')


plt.subplot(2,2,4 )
plt.title('Windspeed vs Demand')
plt.scatter(bikes_prep['windspeed'], bikes_prep['demand'], s=2, c='c')

plt.tight_layout()

# Plot the categorical features vs demand
# Create a 3 * 3 subplot

plt.subplot(3,3,1)
plt.title('Average Demand per Season')
# Create unique season values
cat_list = bikes_prep['season'].unique()
# Create average demand per season
cat_average = bikes_prep.groupby('season').mean()['demand']
colors = ['g','r','m','b']
plt.bar(cat_list, cat_average,color=colors)


plt.subplot(3,3,2)
plt.title('Average Demand per Month')
cat_list = bikes_prep['month'].unique()
cat_average = bikes_prep.groupby('month').mean()['demand']
plt.bar(cat_list, cat_average,color=colors)

plt.subplot(3,3,3)
plt.title('Average Demand per Holiday')
cat_list = bikes_prep['holiday'].unique()
cat_average = bikes_prep.groupby('holiday').mean()['demand']
plt.bar(cat_list, cat_average,color=colors)

plt.subplot(3,3,4)
plt.title('Average Demand per Weekday')
cat_list = bikes_prep['weekday'].unique()
cat_average = bikes_prep.groupby('weekday').mean()['demand']
plt.bar(cat_list, cat_average,color=colors)

plt.subplot(3,3,5)
plt.title('Average Demand per Year')
cat_list = bikes_prep['year'].unique()
cat_average = bikes_prep.groupby('year').mean()['demand']
plt.bar(cat_list, cat_average,color=colors)


plt.subplot(3,3,6)
plt.title('Average Demand per Hour')
cat_list = bikes_prep['hour'].unique()
cat_average = bikes_prep.groupby('hour').mean()['demand']
plt.bar(cat_list, cat_average,color=colors)

plt.subplot(3,3,7)
plt.title('Average Demand per Workingday')
cat_list = bikes_prep['workingday'].unique()
cat_average = bikes_prep.groupby('workingday').mean()['demand']
plt.bar(cat_list, cat_average,color=colors)

plt.subplot(3,3,8)
plt.title('Average Demand per Weather')
cat_list = bikes_prep['weather'].unique()
cat_average = bikes_prep.groupby('weather').mean()['demand']
plt.bar(cat_list, cat_average,color=colors)

plt.tight_layout()



