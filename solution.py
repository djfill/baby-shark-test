#!/usr/bin/python
import os
import csv
with open('baby-sharks.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        sub = os.path.expanduser('~/baby-shark-test/assets/') + row[0] + '/'
        os.rename((sub + os.listdir(sub)[0]), (sub + row[2]))
