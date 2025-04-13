# Autocorrelation

# import Pandas 
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file for correlation
f = pd.read_csv("03corr.csv")

# convert the column 't0' to float type
f['t0'] = pd.to_numeric(f['t0'], downcast='float')

# plot autocorrelation

plt.acorr(f['t0'],maxlags=10)

# use pandas shift function to create a timelag dataset
#t_1, t_2

t_1=f['t0'].shift(+1).to_frame()
t_2=f['t0'].shift(+2).to_frame()

