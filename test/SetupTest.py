#!/usr/bin/python

import sys
sys.path.append('../Classes/')

from test import test
from helperFunctions import *
#grab all input
name = raw_input("enter a name for the test to run, this name will be used for saving test attributes, output directories, etc so choose one that makes sense: ")

nj = int(raw_input("How many jobs would you like to run for this test? "))
nc = int(raw_input("How many cores would you like those jobs to run on? "))
nt = int(raw_input("How many threads per job would you like? "))
trials = int(raw_input("How many trials of this test would you like to run? "))
menu = raw_input("What is the base hlt menu you would like to use for the test (enter filename)? ")

#make test
currentTest = test(nj,nc,nt,name,menu,trials)

#report back to user so that they know what's going on
print "You have configured the test as follows: "
print test

print "making copy of menu and customizing for timing info"
newhltname = menu.split('.py')[0]+'_'+name+'.py'
os.system('cp %s %s' %(menu,newhltname))
customizeMenuForTiming(newhltname)

base = open(newhltname,'r')
lines = base.readlines()
base.close()
base = open(newhltname,'w')
for line in lines:
    line = line.replace('NTHREADS',str(currentTest.nthreads))
    line = line.replace('DQMOUTPUTPATH','.')
    base.write(line)

base.close()

#save the test configuration
savefile = "test_cfg_%s.txt" % currentTest.name
print "Saving as %s" % savefile

outfile = open(savefile,'w')
writeTestFile(currentTest,outfile)
outfile.close()
