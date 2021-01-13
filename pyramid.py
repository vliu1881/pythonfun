#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 18:40:30 2021

@author: vliu1881
"""

def pypart(n): 
      
    for i in range (1,n):
        for j in range (0,n):
            print(" ", end = " ")
        n-=1
        for k in range (0,(i*2-1)):
            print (" *",end="")
            
        print("\r")
            
        
pypart(10)
    
        
        