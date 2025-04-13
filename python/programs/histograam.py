import matplotlib.pyplot as plt

f = open('C:/Users/vijaykumar02/OneDrive - Nagarro/private/study/datascience-course/python/programs/agedata.csv','r')

agefile = f.readlines()
# Integer list

age_list = []

for records in agefile:
        age_list.append(int(records))

bins = [0, 10, 20, 30, 40,50,60,70,80,90,100]       

#plot the histogram

plt.title('Age Histogram') 
plt.xlabel('Group')
plt.ylabel('Age')

plt.hist(age_list,bins, histtype='bar', rwidth=0.9)
plt.show()