#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:33:05 2020

@author: emmanuelidehen
"""

import numpy as np 
from scipy import sparse
import pandas as pd 

""" 
converting a numpy array to csr matrix format 
"""
x = np.eye(4)
print(format(x))
print("======== CSR_Matrix format =============")
y = sparse.csr_matrix(x)
print(y)
print("This next space addreses the pandans library ")
#create a dictionary
data = {'Name':["emmanuel","idehen","Osagumwenro"],
        'Age':[20,30,40],
        'Major':['Machine','Learning','101']
        }
#pass the dictionary to a dataframe 
data_frame = pd.DataFrame(data)
#display the dictionary in an excel format or database format 
display(data_frame)
#query the table
print("===========  My Query  =============")

display(data_frame[data_frame.Age < 40])
