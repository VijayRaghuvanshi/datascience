# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:54:20 2024

@author: vijaykumar02
"""
#import Pandas
import pandas as pd
# Read CSV file using Pandas

dataset = pd.read_csv('loan_small.csv')

#Drop the rows with the missing values
cleandata = dataset.dropna()

# Extract the three numerical columns

data_to_scale = cleandata.iloc[:,2:5]


# import standar scalar z-transformation.

from sklearn.preprocessing import StandardScaler

scaler_ = StandardScaler()

ss_scalar = scaler_.fit_transform(data_to_scale)


# minmax scaler

from sklearn.preprocessing import minmax_scale

mm_scaler = minmax_scale(data_to_scale)
