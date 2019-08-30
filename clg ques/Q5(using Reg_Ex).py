# -*- coding: utf-8 -*-
"""
Q5. Username and Password

Created on Sat Aug 10 19:45:37 2019

@author: SUNNY THAKUR
"""
import re
username = input("Enter username : ")
password = input("Enter password : ")
def func(username,password):
    x = True
    if (len(password)<6 or len(password)>12) :
           x = False
    else:
        for i in username:
            if not re.search("[A-Z]",password):
                x = False
                break
            elif not re.search("[a-z]",password):
                x = False
                break
            elif not re.search("[0-9]",password):
                x = False
                break
            elif not re.search("[$@#]",password):
                x = False
                break
            elif re.search("[^A-Za-z0-9@$#]",password) :
                x = False
                break
    if x :
        print("Valid Password")
    if not x : 
        print("Invalid password")
    
func(username,password)