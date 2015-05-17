#-------------------------------------------------------------------------------
# Name:        Special Characters Remover
# Purpose:     A stright forward way to remove special characters or any other character defined by the user for CSV 
#              files. 
#
# Author:      Haytham Amin
#
# Created:     16/05/2015
# Copyright:   CC
# Licence:     <000000000>
#-------------------------------------------------------------------------------
import csv
fname = raw_input("Enter file name, please include the file extension '.csv' : ")
with open( fname , "rU") as infile, open("repaired_file.csv", "wb") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    conversion = '"/(){}_[]'
    for row in reader:
        newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)
print 'done'
print 'The output file is located in the same folder that contained the input file'
print 'File name = reparied_file.csv'
