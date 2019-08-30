# -*- coding: utf-8 -*-
"""
Q4. Compute net amt. of bank acc.

Created on Sat Aug 10 18:56:39 2019

@author: SUNNY THAKUR
"""
net_amount = 0
def func():
    print(" 1 : Check Balance\n 2 : Deposit\n 3 : Withdraw")
    ch = int(input("Enter your choice\n"))
    global net_amount
    if(ch==1):
        print("Net amount in your account is ₹ " + str(net_amount))
        
    elif(ch==2):
        Deposit = int(input("Enter amount to deposit"))
        net_amount += Deposit
        print("Net amount in your account is ₹ " + str(net_amount))

    else :
        Withdraw = int(input("Enter amount to withdraw"))
        net_amount -= Withdraw
        print("Net amount in your account is ₹ " + str(net_amount))
    
    ch1=input("\nDo you want to continue 'y/n'")   
    while(ch1=="y"):
        func()
        break
        
func()



