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
