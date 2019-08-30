# -*- coding: utf-8 -*-


"""
Q3. 2-D array and element at ith row and jth column is i*j

Created on Sat Aug 10 18:35:49 2019

@author: SUNNY THAKUR
"""

x = int(input("Enter 1st number "))
y = int(input("Enter 2nd number " ))

def func():
    arr = [[i*j for j in range(1,y+1)] for i in range(1,x+1) ]
#    for i in range(1,x):
#        for j in range(1,y):
#            arr[i][j] = i*j
    print(arr)

func()