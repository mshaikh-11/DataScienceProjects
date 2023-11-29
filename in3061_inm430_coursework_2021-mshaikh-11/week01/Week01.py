#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 07:07:41 2021

@author: sufyaanshaikh
"""
print('Hello, World!') 

import csv     # imports the csv module
import sys      # imports the sys module

#f = open('TB_burden_countries_2014-09-29.csv') # opens the csv file
#for row in csv.reader(f):
  #  print(row) 

# Part 1 Step 1 - 4904 rows (By counting the row)


#Part 1 Step 2 

#Pick one of the columns with numeric data and calculate the average
#value using a loop (not a library function such as avg(),
# "e_prev_num_lo" = "Estimated prevalence of TB (all forms),low bound"

#"e_prev_num_lo" = "Estimated prevalence of TB (all forms),low bound" is the column chosen to calculate the average value using  a loop.
# e_prev_num_lo" is the 11th variable of the column buts since python reads the 1st element at 0, it will be at the 10th index for the columns.

#installed pandas to access the dataframe
import pandas as pd
import numpy as np

#data is named data and has size (4903) which is consisten with step 1 count of  4904 as we innclude the heading in the count.
data = pd.read_csv("TB_burden_countries_2014-09-29.csv")

#variable of interest put in a  seperate columnn to calculate the average
variable_interest = data.e_prev_num_lo

#updated_variable_interest is to update the variable by removing 0 and errors (nan), remove 0 by converting to nan
r=data.e_prev_num_lo.replace(0,np.nan)
updated_variable_interest = data.e_prev_num_lo.dropna()
rowcount=0
for row_count in updated_variable_interest:
    rowcount = rowcount  + 1
#for loop to calculate the average
sum_data=0    
for x in data :
    sum_data=sum(updated_variable_interest)

average = sum_data/rowcount
print("average value for e_prev_num_lo is : ", average )


#Part 1 step 3

#Now, repeat step-2 above but this time find the averages for years 1990 and 2011. Have you observed any difference?

#simillar to step 2 except i created array tables which to year 1990 and 2011

Year_1990=data.loc[(data["year"]==1990)]
r_1990=Year_1990.e_prev_num_lo.replace(0,np.nan)
updated_var_1990 = Year_1990.e_prev_num_lo.dropna()

rowcount_1990=0
for row_count_1990 in updated_var_1990:
    rowcount_1990 = rowcount_1990  + 1

sum_1990=0
for x_1990 in Year_1990 :
   sum_1990=sum(updated_var_1990)

average_1990 = sum_1990/rowcount_1990
print("average value for e_prev_num_lo in the year 1990 is : ", average_1990 )


#44379.73417061612 1990

Year_2011=data.loc[(data["year"]==2011)]
r_2011=Year_2011.e_prev_num_lo.replace(0,np.nan)
updated_var_2011 = Year_2011.e_prev_num_lo.dropna()

rowcount_2011=0
for row_count_2011 in updated_var_2011:
    rowcount_2011 = rowcount_2011  + 1

sum_2011=0
for x_2011 in Year_2011 :
   sum_2011=sum(updated_var_2011)

average_2011 = sum_2011/rowcount_2011
print("average value for e_prev_num_lo in the year 2011 is : ", average_2011 )

 #33320.0524537037
 
 #Part 2
 #Create an array of int ranging from 5-15

import  numpy as np 
print("1starray=",np.array(range(5,16,1)))

#Create an array containing 7 evenly spaced numbers between 0 and 23
import  numpy as np 
print("2ndarray=",np.array(range(1,22,3)))

#Numpy has several routines for generating artificial data following a particular structure. Check this page for different types. And generate an artificial numpy array with values between -1 and 1 that follow a uniform data distribution.
import  numpy as np 
np.random.seed(1)
arr_rand=np.random.uniform(-1,1,(1,10))
print("artifical_array:",arr_rand)

#Visualise the array in an histogram in matplotlib.
import matplotlib.pyplot as plt
np.random.seed(1)
arr_rand = np.random.uniform(-1,1,(1,10)) 
plt.hist(arr_rand)
plt.show()

#Create two random numpy arrays with 10 elements. Find the Euclidean distance between the arrays using arithmetic operators, hint: numpy has a sqrt function
import  numpy as np 
import math 
rand_1 = np.random.randn(1,10)
print("random1:",rand_1)
rand_2 = np.random.randn(1,10)
print("random2:",rand_2)

e_dist=np.sqrt(np.sum(np.square(rand_2 - rand_1)))
print("Euclidean distance",e_dist)
