#!/usr/local/bin/python
#
# FaR.py

import sys
import re
print 'Number of files:', len(sys.argv) - 1, 'files'
for x in range(1,len(sys.argv)):
    target = sys.argv[x]
    current = open(target, 'r+')
    final = open(target, 'r+')
    find = raw_input("Find All Containing: ")
    replace = raw_input("Replace All With: ")
    data = current.read()
    data1 = re.sub(find, replace, data)
    print data1
    final.write(data1)
print "Done"
