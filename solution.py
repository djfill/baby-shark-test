#!/usr/bin/python
import os
import csv
dir = os.path.expanduser('~/baby-shark-test/assets/')
with open('baby-sharks.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        jpg = row[2]
        no  = row[0]
        src = dir + no + '/' + os.listdir(dir + no + '/')[0]
        dest = dir + no + '/' + jpg
        os.rename(src, dest)
