# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:37:13 2024

@author: vijaykumar02
"""

#Excercise 1
cityTemp =  open('citytemp.csv', 'r') # r for read mode
citywriteAvgTemp = open('citywriteAvgTemp.csv', 'w') # a for append mode

cityTempDataDict = {};

cityTemp.seek(0)
for records in cityTemp:
    records = records.rstrip('\n')
    city, temprature, unit = records.split(',')
    temprature = float(temprature)
    if(unit == 'C'):
        temprature = (temprature * 9/5) +32
    if(city in cityTempDataDict):
        cityTempList = cityTempDataDict[city]
        cityTempList[0] = cityTempList[0]+1
        cityTempList[1] = cityTempList[1]+temprature
    else:
        cityTempDataDict[city] = [1,temprature]
else:
    for key, value in cityTempDataDict.items():
        citywriteAvgTemp.write(key+","+str((value[1]/value[0]))+"\n")
    else:
        citywriteAvgTemp.close();       
citywriteAvgTemp = open('citywriteAvgTemp.csv', 'r')        
for records in citywriteAvgTemp:
    records = records.rstrip('\n')
    print(records)
 