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

    def addTest(test):
        tests.append(test)
