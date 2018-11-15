README file (ontologyMapHWScript python program)

This program is designed to reduce the number of 1:many ICD10->ICD9 mappings down to 1:1 mappings based on the two data sources: 
(1) the Center for Medicare and Medicaid Services (CMS) GEM files from their website (https://www.cms.gov/Medicare/Coding/ICD10/2018-ICD-10-CM-and-GEMs.html.)
(2) The frequency of ICD9 codes submitted in 2015. https://data.chhs.ca.gov/dataset/hospital-inpatient-diagnosis-procedure-and-external-cause-codes/resource/6e320cac-26ba-42d9-870a-fada82f66600)
(Note, the second set of files were xlsx files converted to txt files in the github folder.)
Download all txt files my Github repo (https://github.com/andreholder)

Once the GEM files and this program have been saved locally, open an Anaconda shell and run the program.
(NOTE 1: All files must be saved in the same folder.)

Your run commmand should be: python ontologyMapHWScript.py