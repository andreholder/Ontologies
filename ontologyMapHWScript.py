# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:32:11 2018

@author: Andre Holder

Description: BMI 500 Lab 10: GEMs interpretation for ICD 9 & 10

"""

### Pull in argument as a global variable 
import sys
directory_path=sys.argv[1]

import os

### Bring the I9 file & I10 files into Python environment 
#First, build the path based on program argument (The path provided by user to find files)
file_name_icd9 = "2018_I9gem"
file_name_icd10 = "2018_I10gem"
suffix = '.txt'

txt_file_I9=open(os.path.join(directory_path, file_name_icd9 + suffix),'r')
txt_file_I10=open(os.path.join(directory_path, file_name_icd10 + suffix),'r')

#Next, import them from the above paths
txt_file_I9=txt_file_I9.read()
txt_file_I10=txt_file_I10.read()

### This function finds, and adds up the flag designations to answer the HW questions
def tallyICDFlags(txt_file,icd_source,icd_target): #ICD type is either 9 or 10; the ontology source
    element=16
    tally_1_to_1=0
    tally_1_to_many=0
    tally_no_map=0
    while element<=len(txt_file):
        #Tally the number of rows with 1-to-1 flag (combo flag=0)
        if int(txt_file[element])==0: 
            tally_1_to_1 += 1
        #Tally the number of rows with 1-to-Many flag (combo flag=1 & scenario flag>1)
        if int(txt_file[element])==1 and int(txt_file[element+1])>1: 
            tally_1_to_many += 1
        #Tally the number of rows with "No Map" flag (No Map flag=1)
        if int(txt_file[element-1])==1: 
            tally_no_map += 1
        element += 20
    
    # Answer to Q1 (tally_1-to-1 total)
    print("The number of 1-to-1 mappings for the I", icd_source, "->I", icd_target,"GEM is", tally_1_to_1)
    # Answer to Q2 (tally_1_to_Many total)
    print("The number of 1-to-many mappings for the I", icd_source, "->I", icd_target,"GEM is", tally_1_to_many)
    # Answer to Q3 (tally_no_map total)
    print("The number of 'no mapping' flags for the I", icd_source, "->I", icd_target,"GEM is", tally_no_map)

tallyICDFlags(txt_file_I9,9,10)
tallyICDFlags(txt_file_I10,10,9)

"""
#Getting an error. Not sure why
txt_file_I9.close()
txt_file_I10.close()
"""