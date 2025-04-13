# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:58:01 2024

@author: vijaykumar02
"""
import matplotlib.pyplot as plt

f = open('C:/Users/vijaykumar02/OneDrive - Nagarro/private/study/datascience-course/python/programs/agedata2.csv','r')

agefile = f.readlines()
# Integer list

#list of cities
city_list = []

for records in agefile:
        #split the records
        age,city = records.split(sep=',')
        city_list.append(city)
        
from collections import Counter
city_count = Counter(city_list)        

city_names = list(city_count.keys())
city_values = list(city_count.values())

#plot the pie chart
plt.pie(city_values, labels=city_names, autopct='%.2f%%')
plt.show()