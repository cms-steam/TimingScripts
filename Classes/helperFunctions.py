#!/usr/bin/python

def writeTestFile(test,f):

    outfile = open(f,'w')
    outfile.write("ncores:%i\n"%test.ncores)
    outfile.write("njobs:%i\n"%test.njobs)
    outfile.write("nthreads:%i\n"%test.nthreads)
    outfile.write("name:%s\n"%test.name)
    outfile.write("menu:%s\n"%test.baseMenu)
    outfile.write("trials:%i\n"%test.trials)

    outfile.close()
