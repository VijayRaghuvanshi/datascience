# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:56:51 2024

@author: vijaykumar02
"""

# tuples
# immutible and same data type of elements
t1 = (1,2,3)
print(t1[2])

len(t1)


# Dictionary in Python

# Collection of key-value pair
# values can be accessed using the key

address = {"Street": '180 Adams Street', \
           'City': 'Chicago',\
           'State': 'IL',\
           'Country': 'USA'}

print(address['Street'])

address['Street'] = '181 Adams street'

# add a new key value pair
address['ZIP'] = 60611

# delete a key value pair
del address['ZIP']

# Get the length of dictionary

len(address)

# convert dictionary into string
str(address)

#get all keys
print(address.keys())

#get all values
print(address.values())





