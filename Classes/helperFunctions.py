#!/usr/bin/python

import os.path

def writeTestFile(test,outfile):

    outfile.write("ncores:%i\n"%test.ncores)
    outfile.write("njobs:%i\n"%test.njobs)
    outfile.write("nthreads:%i\n"%test.nthreads)
    outfile.write("name:%s\n"%test.name)
    outfile.write("menu:%s\n"%test.baseMenu)
    outfile.write("trials:%i\n"%test.trials)



def writeMultiTestFile(mt,f):

    #write test paramaters
    for t in mt.tests:
        writeTestFile(t,f)
        #write blank line to separate test info
        f.write("\n")

def writeRunLine(core,filename,logname):
    return "nohup taskset -c %i cmsRun %s >& %s" % (core,filename,logname)


def configureCPUScan(arch,name):
 
    cpus = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell'}

    maxjobs = {'1':32,'2':32,'3':48}

    print 'Configuring CPU scan for %s machine, which has max number of jobs %i. Would you like to run this or up to a smaller number?' % (cpus[arch],maxjobs[arch])
    nJobs = int(raw_input('Enter desired number of jobs'))



def configureOccScan(arch,name):


def configureThreadScan(arch,name):


def configureFreeScan(arch,name):
