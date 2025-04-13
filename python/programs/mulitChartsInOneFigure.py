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
plt.subplot(2, 2, 1)
plt.title('Sales vs Cost')
plt.xlabel('Sale')
plt.ylabel('Cost')

#create the scatter plot
plt.scatter(s_list,c_list)



#plot the boxplotplt.figure("My boxplot")
plt.subplot(2, 2, 2)
plt.title("box plot of sales")
plt.ylabel("usd")
plt.boxplot(sale_list)


#plot the histogram
plt.subplot(2, 2, 3)
plt.title('Histogram of sales') 
plt.ylabel('USD')
plt.hist(s_list, bins=5,  histtype='bar', rwidth=0.9)

#line plot of stock
plt.subplot(2, 2, 4)
x_days = [1,2,3,4,5]
y_price1 = [9,9.5,10.1,10,12]
plt.title("Stockprice History")
plt.xlabel('Day')
plt.ylabel('Price')
plt.plot(x_days,y_price1)


plt.tight_layout()
plt.savefig('01subplot.png')
#show the plots
plt.show()




