#!/usr/bin/python

#import some needed libraries
import sys, os

'''types of tests are:

1) CPU Scan, starts with 1 job and fills the machine 1 job at a time - can be configured with different ratios of jobs to threads, multithreading, hyperthreading, etc

2) Occupancy Scan, an abbreviated version of above, which does only a few selected points.

3) Thread Scan, starts with one job and 1 one thread, then increases number of threads for that job until full cpu is reached.

'''
#define dictionary for types of scans
types = {'1':'CPU-Scan','2':'Occ-Scan','3':'Thread-Scan'}
#define dicionary for architectures the script will know how to handle
archs = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell','4':'Broadwell'}

print 'Please pick a type of test to run. The currently supported options are: \n 1 - CPU-Scan \n 2 - Occupancy Scan \n 3 - Multithreading Scan \n'
type = raw_input('Choose 1, 2, or 3: ')

print 'What type of cpu architecture is this for? The currently supported options are: \n 1 - SandyBridge \n 2 - IvyBridge \n 3 - Haswell \n'
arch = raw_input('Choose 1, 2, or 3: ')

#get extra naming info for the test
name = raw_input('Enter any extra naming you would like the test to have (default is \'TYPE_ARCH\'): \n')
if name != '':
    name = '_'+name

if type=='1':
    mTest = configureCPUScan(arch,name)
elif type=='2':
    mTest = configureOccScan(arch,name)
elif type=='3':
    mTest = configureThreadScan(arch,name)
else:
    print 'You did not pick a valid choice for test type! Exiting...'
    sys.exit(0)


# now run test if desired
runFile = 'run_'+types[type]+'_'+archs[arch]+name+'.sh'
print 'Would you like to start the test now (If not, simply run the following file later: %s)?' % runFile
run = raw_input('Enter Y/n: ')

if run=='Y':
    os.system('nohup sh %s' % runFile)
    print 'Jobs started. Now exiting...'
else:
    print 'Exiting...'
