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

def getFastTimerService():
    return """

process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 400.0 ),
    useRealTimeClock = cms.untracked.bool( True ),
    enableTimingModules = cms.untracked.bool( True ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( False ),
    enableTimingExclusive = cms.untracked.bool( True ),
    skipFirstPath = cms.untracked.bool( True ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    dqmPathTimeRange = cms.untracked.double( 1000.0 ),
    dqmTimeRange = cms.untracked.double( 10000.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    enableDQMSummary = cms.untracked.bool( True ),
    enableTimingSummary = cms.untracked.bool( True ),
    enableDQMbyPathTotal = cms.untracked.bool( True ),
    enableTimingPaths = cms.untracked.bool( True ),
    enableDQMbyPathExclusive = cms.untracked.bool( False ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    enableDQMbyPathActive = cms.untracked.bool( False ),
    enableDQMbyPathDetails = cms.untracked.bool( False ),
    enableDQMbyPathOverhead = cms.untracked.bool( False ),
    enableDQMbyPathCounters = cms.untracked.bool( True ),
    enableDQMbyModuleType = cms.untracked.bool( False )
)
"""


def getThroughputService():
    return """

process.ThroughputService = cms.Service('ThroughputService',
  timeRange = cms.untracked.double(60000),
  timeResolution = cms.untracked.double(10),
  dqmPath = cms.untracked.string('HLT/Throughput')
)"""


def getDQMModule():
    return """

# FastTimerServiceClient                                                                                                                                                                                          
process.fastTimerServiceClient = cms.EDAnalyzer( "FastTimerServiceClient",
    dqmPath = cms.untracked.string( "HLT/TimerService" )
)

# DQM file saver                                                                                                                                                                                                  
process.dqmFileSaver = cms.EDAnalyzer( "DQMFileSaver",
    convention        = cms.untracked.string( "Offline" ),
    workflow          = cms.untracked.string( "/HLT/FastTimerService/All" ),
    dirName           = cms.untracked.string( "DQMOUTPUTPATH" ),
    saveByRun         = cms.untracked.int32(1),
    saveByLumiSection = cms.untracked.int32(-1),
    saveByEvent       = cms.untracked.int32(-1),
    saveByTime        = cms.untracked.int32(-1),
    saveByMinute      = cms.untracked.int32(-1),
    saveAtJobEnd      = cms.untracked.bool(False),
    forceRunNumber    = cms.untracked.int32(-1),
)

process.TimingOutput = cms.EndPath( process.fastTimerServiceClient + process.dqmFileSaver )"""

def getThreadConfiguration():
    return """
process.options.numberOfThreads = cms.untracked.uint32( NTHREADS )
process.options.numberOfStreams = cms.untracked.uint32( NTHREADS ) #same number as above
process.options.sizeOfStackForThreadsInKB = cms.untracked.uint32( 10*1024 )
"""

def customizeMenuForTiming(menu):

    #open file to append it
    hlt = open(menu,'a')
    
    #add the timer service:
    hlt.write(getFastTimerService)
    #add the throughput service:
    hlt.write(getThroughputService)
    ##add the DQM output module
    hlt.write(getDQMModule)
    #add multithreading customization
    hlt.write(getThreadConfiguration)
    

def getTestPath(t):
    return './%s' %t.name

def copyHltMenu(t):
    ncores = t.ncores
    njobs = t.njobs
    nthreads = t.nthreads
    name = (t.baseMenu).split('.py')[0]

    cfgString = '_%sj%sc_%st_j' % (njobs,ncores,nthreads) 

    #open base menu
    base = open(t.baseMenu)

    for i in range(1,t.trials+1):
        trialstring = '_trial%i' % i
        for j in range(1,njobs+1):
            hltname = name+'_'+t.name+cfgString+str(j)+trialstring+'.py'
            new = open(hltname)
            dqmPath = "/trial%i/%ijobs/j%i/" % (i,njobs,j)
            for line in base:
                line = line.replace('NTHREADS',t.nThreads)
                line = line.replace('DQMOUTPUTPATH',dqmPath)
                new.write(line)
            new.close()
            #move new file to test directory
            testPath = getTestPath(t)
            os.system('mv %s %s' % (new,testpath))

def copyMenusForMultiTest(mt):
    for test in mt:
        copyHltMenu(test)
