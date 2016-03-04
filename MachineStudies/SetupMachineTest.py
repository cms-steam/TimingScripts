#!/usr/bin/python

#import some needed libraries
import sys, os
sys.path.append('../Classes/')
from test import *
from helperFunctions import *
#import configure scripts
from configureScripts import *

'''types of tests are:

1) CPU Scan, starts with 1 job and fills the machine 1 job at a time

2) Custom Scan - Add tests by hand with whatever settings you please (can be used for PU test)

3) Thread Scan, starts with one job and 1 one thread, then increases number of threads for that job until full cpu is reached.

'''
#4) Free Scan, set the number of threads, the ratio of jobs to cores, starting, and stopping number of jobs
#define dictionary for types of scans
types = {'1':'CPU-Scan','2':'Custom-Scan','3':'Thread-Scan'}
#define dicionary for architectures the script will know how to handle
archs = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell','4':'Broadwell'}

print 'Please pick a type of test to run. The currently supported options are: \n 1 - CPU-Scan \n 2 - Custom Scan \n 3 - Multithreading Scan \n 4 - Free Scan \n'
type = raw_input('Choose 1, 2, 3, or 4: ')

print 'What type of cpu architecture is this for? The currently supported options are: \n 1 - SandyBridge \n 2 - IvyBridge \n 3 - Haswell \n'
arch = raw_input('Choose 1, 2, or 3: ')

#get number of trials
tries = int(raw_input('Enter how many trials of the test you would like to run: '))

#get extra naming info for the test
name = raw_input('Enter any extra naming you would like the test to have (default is \'TYPE_ARCH\'): \n')
if name != '':
    name = '_'+name

name = types[type]+'_'+archs[arch]+name

if type!='2':
    hlt = raw_input('Enter path to base menu to be used for study: ')
else:
    hlt=''

if type=='1':
    mTest = configureCPUScan(arch,name,hlt,tries)
elif type=='2':
    mTest = configureCustomScan(arch,name,hlt,tries)
elif type=='3':
    mTest = configureThreadScan(arch,name,hlt,tries)
#elif type=='4':
#    mTest = configureFreeScan(arch,name,hlt,tries)
else:
    print 'You did not pick a valid choice for test type! Exiting...'
    sys.exit(0)

#save the test configuration for later
filename = 'mtest_cfg_%s.txt' % mTest.name
outfile = open(filename,'w')
writeMultiTestFile(mTest,outfile)
outfile.close()

#add needing services and dqm to base menu
if type !='2':
    print "Adding FastTimerService, ThroughputService, and DQM outputmodule to base hlt menu..."
    customizeMenuForTiming(hlt)

#make needed copies of menu
#make needed directory first
os.system('mkdir %s' % mTest.name)
print "Making needed copies of menus"
copyMenusForMultiTest(mTest)

#make directory structure
setupDirectoriesForMultiTest(mTest)

# now run test if desired
runFilename = 'run_'+types[type]+'_'+archs[arch]+name+'.sh'
runFile = open(runFilename,'w')
writeRunFile(runFile,mTest)
runFile.close()

print 'Would you like to start the test now (If not, simply run the following file later: %s)?' % runFilename
run = raw_input('Enter Y/n: ')

if run=='Y':
#    os.system('nohup sh %s' % runFilename)
    print 'Jobs started. Now exiting...'
else:
    print 'Exiting...'
