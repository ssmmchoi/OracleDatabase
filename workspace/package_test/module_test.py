# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:15:56 2020

@author: user
"""


import pandas as pd

lst = [2,3,4,5]
ser1d = pd.Series(lst)  # 객체
print('sum =', ser1d.sum())  # sum = 14