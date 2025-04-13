# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:26:27 2024

@author: vijaykumar02
"""

# Plotting basics
# Import pyplot from metplotlib
import matplotlib.pyplot as plt


x_days = [1, 2, 3, 4, 5]
y_price1 = [9, 9.5, 10.1, 10, 12]

y_price2 = [11, 12, 10.5, 11.5, 12.5]


# define the chart elements

plt.title('Stock Movement')
plt.xlabel('Week Days')
plt.ylabel('Price in USD')

plt.plot(x_days, y_price1, label="Stock 1")
plt.plot(x_days, y_price2, label="Stock 2")

plt.legend(loc=2,fontsize=12)
plt.show()