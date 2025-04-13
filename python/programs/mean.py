# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:47:49 2024

@author: vijaykumar02
"""

# Basic descriptive Statistics
#--------------------------------

import statistics as st

data = [1,2,3,3]
#mean calculation
mean = st.mean(data);

median = st.median(data)

mode = st.mode(data)
std_dev = st.stdev(data)
variance = st.variance(data)
