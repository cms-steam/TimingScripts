#!/usr/bin/python

#define function to get average throughput
def getAvgThru(h):
    tot=0.0;
    nbins=0.0;
    for i in range(1,h.GetNbinsX()):
        if h.GetBinContent(i)!=0:
            tot+=h.GetBinContent(i)
            nbins+=1

    avg = tot/nbins
    return avg


def getEventHistos(tfiles,dirs):
    iter =0;
    eventHistos = []
    for f in tfiles:
        ev=dirs[iter]+"event"
        evhist=tfiles[iter].Get(ev)
        eventHistos.append(evhist)
        iter+=1

    return eventHistos


def getAllPathsHistos(tfiles,dirs):
    iter=0;
    apHistos = []

    for f in tfiles:
        ap=dirs[iter]+"all_paths"
        aphist=tfiles[iter].Get(ap)
        apHistos.append(aphist)
        iter+=1

    return apHistos


def getThroughputGraph(mt):
    #make dictionary to hold nThreads:TFiles pairs
    from collections import defaultdict
    tFileDict = defaultdict(list)
    
    for t in mt.tests:
        for i in range(1,t.njobs+1):
            fname = outputDir+"DQM_Timing_%ij%ic_%ithreads_j%i_trial1_%s.root" % (t.njobs,t.ncores,t.nthreads,i,t.name)
            tFileDict[t.nthreads].append(TFile(fname))

    g = TGraph(len(tFileDict))
            
    #loop over dictionary
    for k,v in tFileDict.iteritems():
                
        thru=0.0
        for i in range(0,len(v)):
            hist=v[i].Get("DQMData/Run 256843/HLT/Run summary/Throughput/throughput_retired")
            thru += getAvgThru(hist)
            
        #divide by total number of jobs
        thru = thru / float(len(v))

                         
        #set point in TGraph
        g.SetPoint(int(k)-1,int(k),thru)
    
    #return the tgraph
    return g
