#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:33:05 2020

@author: emmanuelidehen
"""

import numpy as np 
from scipy import sparse

""" 
converting a numpy array to csr matrix format 
"""
x = np.eye(4)
print(format(x))
print("=================")
y = sparse.csr_matrix(x)
print(y)