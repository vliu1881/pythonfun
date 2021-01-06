#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:02:35 2021

@author: vliu1881
"""

        
    
def prime_number_check (a_number):
    
    if  type(a_number) == int:
        if a_number > 1:
            for x in range(2, a_number): 
                if(a_number % x) == 0: 
                    print(str(a_number) +" is not prime.") 
                    return(False)
                    break
                
                    #print("prime") 
            print(str(a_number)+ " is prime.")
            return(True)
        else: 
            print(str(a_number) +" is not prime.")
            return(False)
    else:
        print(str(a_number) +" is not an integer.")
        return(False)
        
#for x in range(2, a_number):
    
prime_number_check("A")
prime_number_check(-1)
prime_number_check(1)
prime_number_check(9)
prime_number_check(13)