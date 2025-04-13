# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:58:01 2024

@author: vijaykumar02
"""
import matplotlib.pyplot as plt

f = open('C:/Users/vijaykumar02/OneDrive - Nagarro/private/study/datascience-course/python/programs/salesdata.csv','r')

salefile = f.readlines()
# Integer list

sale_list = []

for records in salefile:
        sale_list.append(int(records))

   

#plot the boxplot

plt.title('Boxplot of Sales') 
plt.boxplot(sale_list)
plt.show()