# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:34:37 2024

@author: vijaykumar02
"""

# list in python


list1 = ["Jitesh", "John", "Alia"]

print(list1[2])


# Add operation on list

list1.append("Lise")

# update list
list1[1] = "Frans"

# delete from list

del list1[2]



# Get length of list

len(list1)

# concat list

list2 = ["a", "b", "c"]

contlist = list1+list2


# sort list

list1.sort()


# multi dimensional list

twodlist = [["Jitesh","Frans","Lise"],[123, 456, 345]]
print(twodlist[0])
print(twodlist[0][1])


#slicing of list

sublist = []
for list1 in twodlist:
    sublist.append(list1[1:3])
    




























