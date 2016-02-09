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


def copyHltMenu(t):
    ncores = t.ncores
    njobs = t.njobs
    nthreads = t.nthreads
    name = (t.baseMenu).split('.py')[0]

    cfgString = '_%sj%sc_%st_j' % (njobs,ncores,nthreads) 

    for i in range(1,t.trials+1):
        trialstring = '_trial%i' % i
        for j in range(1,njobs+1):
            hltname = name+'_'+t.name+cfgString+str(j)+trialstring+'.py'
            os.system('cp %s %s' % (t.baseMenu,hltname)
        
