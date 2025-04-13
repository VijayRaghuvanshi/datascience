# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:41:47 2024

@author: vijaykumar02
"""
#import pyplot from matplotlib
import matplotlib.pyplot as plt
 
# plot a bar chart

x_cities = ['New York', 'London', 'Dubai', 'New Delhi', 'Tokyo']
y_temp = [75, 65, 105, 98, 90]

# define the chart elements

plt.title('Temprature Variance')
plt.xlabel('Cities')
plt.ylabel('Temprature')

plt.bar(x_cities, y_temp)
plt.show()