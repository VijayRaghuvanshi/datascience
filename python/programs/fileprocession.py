# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:17:35 2024

@author: vijaykumar02
"""

# File functions - Open, Read, Write, Close

# Open operation on File

cityTemp =  open('citytemp.csv', 'r') # r for read mode
citywrite = open('citywrite.csv', 'a') # a for append mode

rec1 = cityTemp.readline() # read line 1 record
rec2 = cityTemp.readlines() # read all records from the pointer

# data processing
city, temprature, unit = rec1.split(',')
temprature = (float(temprature)-32) * 5/9

# write records to file
citywrite.write(rec1)
citywrite.close()

cityTemp.seek(0)
for records in cityTemp:
    records = records.rstrip('\n')
    print(records)
    