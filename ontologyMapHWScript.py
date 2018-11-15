# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:32:11 2018

@author: Andre Holder

Description: BMI 500 Lab 11: GEMs interpretation for ICD 9 & 10, and 1:many reduction to 1:1 for ICD10->9 conversions

"""

import sys

"""
### Pull in argument as a global variable 
directory_path=sys.argv[1]
"""

import os
import pandas as pd # Python Data Analysis Library
import re
import numpy as np

### Bring the I9 file & I10 files into Python environment 
##Reading data
#Setting the column names

"""
### Create the path names to retrieve the GEM files, given the path in argument
file_name_icd9 = "2018_I9gem"
file_name_icd10 = "2018_I10gem"
suffix = '.txt'

path_name_I9=open(os.path.join(directory_path, file_name_icd9 + suffix),'r')
path_name_I10=open(os.path.join(directory_path, file_name_icd10 + suffix),'r')
"""

### Read the data from the GEM txt files using pandas and create a dataframe (a table).
path_name_I9="2018_I9gem.txt"
columns_9 = ["icd_9", "icd_10", "flags 1-5"]

path_name_I10="2018_I10gem.txt"
columns_10 = ["icd_10", "icd_9", "flags 1-5"]

"""
df_I9 = pd.read_fwf(path_name_I9, sep=' ', header=None, names=columns_9, converters= {'flags 1-5': str})
df_I10 = pd.read_fwf(path_name_I10, sep=' ', header=None, names=columns_10, converters= {'flags 1-5': str})
"""
df_I9 = pd.read_table(path_name_I9, delim_whitespace=True, names=columns_9, converters= {'flags 1-5': str})

df_I10 = pd.read_table(path_name_I10, delim_whitespace=True, names=columns_10, converters= {'flags 1-5': str})

### Create the pertinent designations for HW questions for part I 
#Create a column corresponding to whether rows have a no map flag (T/F)
df_I9['no_map9'] = df_I9['flags 1-5'].str.match('.1...')

df_I10['no_map10'] = df_I10['flags 1-5'].str.match('.1...')

### Filter out those with no mappings out
df_I9_filter = df_I9[df_I9['no_map9']==False]

df_I10_filter = df_I10[df_I10['no_map10']==False]

### Create a "counts" table (2 columns: just source icd codes, and counts=# of mappings)
df_I9_counts=df_I9_filter.groupby( ['icd_9'] ).size().reset_index(name = 'counts')

df_I10_counts = df_I10_filter.groupby( ['icd_10'] ).size().reset_index(name = 'counts')

### Find those with only unique values (count==1) and create a table with unique (1-to-1) mappings
df_I9_one= df_I9_counts[df_I9_counts['counts']==1]

df_I10_one = df_I10_counts[df_I10_counts['counts']==1]

### Create a table with 1:many (counts>1)
df_I9_many = df_I9_counts[df_I9_counts['counts']!=1]

df_I10_many = df_I10_counts[df_I10_counts['counts']!=1]

### Sum the occurences of 1:1 & 1:many mappings to answer the HW questions
### The tally_no_map" variables below give series (vectors) listing frequencies of True & False values; the total # of "True's" answers the HW question
tally_one_to_one9=df_I9_one['counts'].sum()
tally_one_to_many9=df_I9_many['counts'].sum()
tally_no_map9=df_I9['no_map9'].value_counts()

tally_one_to_one10=df_I10_one['counts'].sum()
tally_one_to_many10=df_I10_many['counts'].sum()
tally_no_map10=df_I10['no_map10'].value_counts()

### Print the answers
def printMyTotals(icd_source, icd_target, sum_one_to_one, sum_one_to_many, sum_no_map): #ICD type is either 9 or 10; the ontology source
    # Answer to Q1 (tally_1-to-1 total) 
    print("The number of 1-to-1 mappings for the I", icd_source, "->I", icd_target,"GEM is", sum_one_to_one)
    # Answer to Q2 (tally_1_to_Many total)
    print("The number of 1-to-many mappings for the I", icd_source, "->I", icd_target,"GEM is", sum_one_to_many)
    # Answer to Q3 (tally_no_map total)
    print("The number of 'no mapping' flags for the I", icd_source, "->I", icd_target,"GEM is", sum_no_map)
    print("\n")

printMyTotals(9,10,tally_one_to_one9,tally_one_to_many9,tally_no_map9[1]) #tally_no_map9[1] is a count of the True values
printMyTotals(10,9,tally_one_to_one10,tally_one_to_many10,tally_no_map10[1]) #tally_no_map10[1] is a count of the True values

#####THIS IS THE BEGINNING OF HW11, TO ACQUIRE KNOWLEDGE FROM THE MAPPINGS
### I need the 1:many entries from the ICD 10 GEM txt file
df_I10_only_many = pd.merge(df_I10,df_I10_many,on="icd_10")

### Bring the I9 file & I10 diagnosis frequency files into Python environment 
# Setting the column names
columns_freq_9 = ["icd_9", "total_dx", "dx1", "dx2", "dx3", "dx4", "dx5", "dx6", "dx7", "dx8", "dx9", "dx10", "dx11", "dx12", "dx13", "dx14", "dx15", "dx16", "dx17", "dx18", "dx19", "dx20", "dx21", "dx22", "dx23", "dx24"]
columns_freq_10 = ["icd_10", "total_dx", "dx1", "dx2", "dx3", "dx4", "dx5", "dx6", "dx7", "dx8", "dx9", "dx10", "dx11", "dx12", "dx13", "dx14", "dx15", "dx16", "dx17", "dx18", "dx19", "dx20", "dx21", "dx22", "dx23", "dx24"]

# Create the path names to retrieve the ICD frequency files
file_name_freq_icd9 = "2015-pdd-diagnosis-code-frequencies20160715_ICD9"
file_name_freq_icd10 = "2015-pdd-diagnosis-code-frequencies20160715_ICD10"
suffix = '.txt'

path_name_freq_I9="2015-pdd-diagnosis-code-frequencies20160715_ICD9.txt"
path_name_freq_I10="2015-pdd-diagnosis-code-frequencies20160715_ICD10.txt"

"""
path_name_freq_I9=open(os.path.join(directory_path, file_name_freq_icd9 + suffix),'r')
path_name_freq_I9=open(os.path.join(directory_path, file_name_freq_icd10 + suffix),'r')
"""

# Read the ICD 9 frequency table in to Python environment
freq_I9 = pd.read_table(path_name_freq_I9, delim_whitespace=True, names=columns_freq_9)

# Merge the ICD 9 frequency table with the I10 1:many GEM mappings table
freq_I9['icd_9'] = freq_I9['icd_9'].str.replace('.','') #ICD9 codes in df_I10 have no decimal; need to match
df_I10_best_map_search = pd.merge(df_I10_only_many,freq_I9[["icd_9","total_dx"]],on="icd_9")

"""
#df_I10_best_map_search['total_dx'] = df_I10_best_map_search['total_dx'].apply(int)
"""

df_I10_best_map_search=df_I10_best_map_search.sort_values(['icd_10','icd_9'], ascending=True)

### Among the ICD 10 codes mapped to >1 ICD 9 code, find out the frequency with which their target ICD 9 codes were used 
df_I10_max=df_I10_best_map_search.groupby(['icd_10'])['total_dx'].max().reset_index(name = 'max_total_dx')

### Select the target ICD 9 code that was most frequently used to be the only target ICD9 code for mapping (i.e., convert 1:many mappings to 1:1).
df_I10_best_map_final = pd.merge(df_I10_best_map_search,df_I10_max,left_on=['icd_10','total_dx'],right_on=['icd_10','max_total_dx'])

print('After running this program, the number of 1:many mappings was reduced from', tally_one_to_many10, 'down to', len(df_I10_best_map_final), '1:1 mappings based on the most frequently selected ICD9 codes in 2015.')