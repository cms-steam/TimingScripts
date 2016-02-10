#!/usr/bin/python


def configureCPUScan(arch,name,hlt,trials):
 
    cpus = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell'}

    maxjobs = {'1':32,'2':32,'3':48}

    print 'Configuring CPU scan for %s machine, which has max number of jobs %i. Would you like to run this or up to a smaller number?' % (cpus[arch],maxjobs[arch])
    nJobs = int(raw_input('Enter desired number of jobs: '))

    #make multitest
    mt = multitest(name)
    
    #now add tests to multitest
    for i in range(1,nJobs+1):
        current = test(i,i,1,name,hlt,trials)
        mt.addTest(test)

    #now return correctly configured multitest
    return mt

def configureOccScan(arch,name):


def configureThreadScan(arch,name):


def configureFreeScan(arch,name):
