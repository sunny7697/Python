# -*- coding: utf-8 -*-
"""
Q2. Take n as input and print dictionary that contains (i,i*i)

Created on Wed Aug 14 09:30:44 2019

@author: SUNNY THAKUR
"""

n = int(input("Enter a number : "))
def func(n):
    dict = {i:i*i for i in range(n+1)}
    print(dict)
    
func(n)