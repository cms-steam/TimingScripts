#!/ur/bin/python

#definition of test class

class test(object):

    def __init__(self,njobs,ncores,nthreads,name,baseMenu,trials):
        self.njobs = njobs
        self.ncores = ncores
        self.nthreads = nthreads
        self.name = name
        self.baseMenu = baseMenu
        self.trials = trials



class multiTest(object):

    def __init__(self,name):
        self.name = name
        self.tests = []

    def addTest(self,t):
        self.tests.append(t)


def readTest(tfile):
    return

def readMultiTest(tfile):

    f = open(tfile,'r')

    name = (tfile.split('.txt')[0]).split('cfg_')[1]

    mt = multiTest(name)

    for line in f:
        #read in configuration from first text
        if line.find('ncores')!=-1:
            ncores = int(line.split(':')[1])
        if line.find('njobs')!=-1:
            njobs = int(line.split(':')[1])
        if line.find('nthreads')!=-1:
            nthreads = int(line.split(':')[1])
        if line.find('menu')!=-1:
            menu = line.split(':')[1]
        if line.find('trials')!=-1:
            ntrials = int(line.split(':')[1])

        #if line is newline means we have reach end of test so add it to mtest
        if line == '\n':
            t = test(njobs,ncores,nthreads,name,menu,ntrials)
            mt.addTest(t)
            
    f.close()
    

    return mt
