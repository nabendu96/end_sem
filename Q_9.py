# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:37:52 2020

@author: nabendu
"""

import numpy as np

A=np.array([[2,1],[1,0],[0,1]])

#using numpy.linalg.svd
U_1,S_1,V_1=np.linalg.svd(A)

print('singular values of the 1st matrix are ',S_1)

B=np.array([[1,1,0],[1,0,1],[0,1,1]])

U_2,S_2,V_2=np.linalg.svd(B)

print('singular values of the 2nd matrix are ',S_2)
