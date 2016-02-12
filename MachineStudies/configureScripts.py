#!/usr/bin/python

import sys, os
sys.path.append('../Classes/')
from test import *

def configureCPUScan(arch,name,hlt,trials):
 
    cpus = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell'}

    maxjobs = {'1':32,'2':32,'3':48}

    print 'Configuring CPU scan for %s machine, which has max number of jobs %i. Would you like to run this or up to a smaller number?' % (cpus[arch],maxjobs[arch])
    nJobs = int(raw_input('Enter desired number of jobs: '))

    #make multiTest
    mt = multiTest(name)
    
    #now add tests to multiTest
    for i in range(1,nJobs+1):
        current = test(i,i,1,name,hlt,trials)
        mt.tests.append(current)

    #now return correctly configured multiTest
    return mt

def configureOccScan(arch,name):
    return


def configureThreadScan(arch,name,hlt,trials):

    cpus = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell'}

    maxjobs = {'1':32,'2':32,'3':48}

    print 'Configuring Thread scan for %s machine, which has max number of cores %i. Would you like to run this or up to a different number?' % (cpus[arch],maxjobs[arch])
    maxThreads = int(raw_input('Enter desired maximum number of threads: '))    

    mt = multiTest(name)
    for i in range(1,maxThreads+1):
        if i <= maxjobs[arch]:
            cores = i
        else:
            cores = 999
        current = test(1,cores,i,name,hlt,trials)
        mt.tests.append(current)

    return mt
    


def configureFreeScan(arch,name):
    return
