# -*- coding: utf-8 -*-

#Q1. Number divisible by 7 not by 5 between two given inputs
"""
Created on Sat Aug 10 10:00:36 2019

@author: SUNNY THAKUR
"""

a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number " ))

def func1(a,b):
    print([i for i in range(a,b) if i%5!=0 and i%7==0])

#It will take lesser time than func1
def func2(a,b):
        temp =0
        for num in range(a,b):
                if(num%7==0): 
                    temp = num
                    break
                
        
        for j in range(temp,b,7):
                if(j%5!=0):
                    print(j)

func1(a,b)
func2(a,b)
