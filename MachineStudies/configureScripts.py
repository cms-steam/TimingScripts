#!/usr/bin/python

import sys, os
sys.path.append('../Classes/')
from test import *
from helperFunctions import * 

def configureCustomScan(arch,name,hlt,trials):
 
    cpus = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell'}

    maxjobs = {'1':32,'2':32,'3':48}

    print 'Configuring Custom Scan for %s machine, which has max number of threads %i.' % (cpus[arch],maxjobs[arch])

    print 'Enter parameters for new test in following format: njobs,ncores,nthreads,baseHLT. When you are finished adding tests type \'Done\''
    mt = multiTest(name)

    while(1):
        params = raw_input('Test parameters, \'Done\' for finished: ')
        if params=='Done':
            return mt
        else:
            njobs = int(params.split(',')[0])
            ncores = int(params.split(',')[1])
            nthreads = int(params.split(',')[2])
            hlt = params.split(',')[3]
            current = test(njobs,ncores,nthreads,name,hlt,trials)
        #add the timing parameters now
            customizeMenuForTiming(hlt)
            mt.tests.append(current)
    

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
