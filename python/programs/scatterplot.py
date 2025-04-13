# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:27:50 2024

@author: vijaykumar02
"""
#Create the Scatter plot of Sales vs Cost from the file data
#import pyplot
import matplotlib.pyplot as plt

f = open('C:/Users/vijaykumar02/OneDrive - Nagarro/private/study/datascience-course/python/programs/salesdata2.csv','r')

salefile = f.readlines()

#create the sales list
s_list = []
c_list = []

for records in salefile:
    sale, cost = records.split(sep=',')
    s_list.append(sale)
    c_list.append(cost)

plt.title('Sales vs Cost')
plt.xlabel('Sale')
plt.ylabel('Cost')

#create the scatter plot
plt.scatter(s_list,c_list)
plt.show()