#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:43:43 2021

@author: vliu1881
"""

def bio (total_ml, desired_pct, original_pct):
   if desired_pct < original_pct and original_pct < 100 and total_ml > 0:
       amount = round( (total_ml * desired_pct)/(original_pct),2)
       water = total_ml - amount
       print("You should put " +str(amount) +"ml of ethanol into your mixture to make " + str(desired_pct) +" ethanol solution, then put " +str(water) + " ml of water to complete the mixture.")
       return(amount)
   elif original_pct>100:
        print("You cannot have a solution containing more than 100% of something. Please conside checking the percentage of ethanol you initally have.")
   elif desired_pct>100:
       print("You cannot obtain a solution contaning more than 100 of something. Please consider checking the percentage of ethanol you are trying to get.")
   elif total_ml<0:
       print("Please check the amount of solution you need.")

   else:
       print("Please consider checking your numbers")
       
bio(-100, 0.7,0.8)
       
     
       
       
       
       
             
             
             


             

             

             

             

             

       
       
       
       
       
       





       
              