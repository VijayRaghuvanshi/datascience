# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:44:29 2024

@author: vijaykumar02
"""

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
sale_list = []
s_list = []
c_list = []

for records in salefile:
    sale, cost = records.split(sep=',')
    s_list.append(sale)
    c_list.append(cost)
    
 
#create a list of list
sale_list.append(s_list)
sale_list.append(c_list) 
   
#scatter plots
plt.figure("My scatter plot")
plt.title('Sales vs Cost')
plt.xlabel('Sale')
plt.ylabel('Cost')

#create the scatter plot
plt.scatter(s_list,c_list)
plt.savefig('01scattered.png')


#plot the boxplot
plt.figure("My boxplot")
plt.title("box plot of sales")
plt.ylabel("usd")
plt.boxplot(sale_list)
plt.savefig('01boxplot.png')
plt.show()


