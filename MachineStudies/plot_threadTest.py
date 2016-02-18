#/usr/bin/python

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

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--outputDir",type=str,help='The directory where output files are. Default is renamer_output',required=False,nargs=1,default='./renamer_output/')
parser.add_argument("--testSaveFile",type=str,help='The name of the config file for the test whose results you want to plot',required=True,nargs=1)
parser.add_argument("--process",type=str,help='The process name used for hlt test',required=True,nargs=1)
parser.add_argument("--run",type=str,help='The run used for input files',required=True,nargs=1)

args=parser.parse_args()

#define variables from input arguments
tfile =  args.testSaveFile[0]
run = args.run[0]
process = args.process[0]
outputDir=args.outputDir[0]
#read in multitest
import sys, os
sys.path.append('../Classes/')
from test import *
mt = readMultiTest(tfile)

#import needed root libraries
from ROOT import gROOT, TCanvas, TH1F, TFile, TLegend, gStyle, TGraph

#make of threads array and file array
threads = []
tfiles = []
dirs=[]
for t in mt.tests:
    threads.append(t.nthreads)
    fname = outputDir+"DQM_Timing_%ij%ic_%ithreads_j1_trial1_%s.root" % (t.njobs,t.ncores,t.nthreads,t.name)
    tfiles.append(TFile(fname))
    dirs.append("DQMData/Run %s/HLT/Run summary/TimerService/Running %i processes/process %s/" % (run,t.nthreads,process))

### Make Timing Plot ####################

#get timing histograms
eventHistos = []
pathHistos = []
iter=0

for f in tfiles:
    ap=dirs[iter]+"all_paths"
    ev=dirs[iter]+"event"
    evhist=tfiles[iter].Get(ev)
    aphist=tfiles[iter].Get(ap)
    eventHistos.append(evhist)
    pathHistos.append(aphist)
    iter+=1

#loop over histograms to make plot
evGraph = TGraph(len(threads))
iter=0
for h in eventHistos:
    evGraph.SetPoint(iter,threads[iter],h.GetMean())
    iter+=1
apGraph = TGraph(len(threads))
iter=0

for h in pathHistos:
    apGraph.SetPoint(iter,threads[iter],h.GetMean())
    print "x: %i, y: %f" % (threads[iter],h.GetMean())
    iter+=1

evGraph.SetMarkerColor(1)
evGraph.SetMarkerStyle(22)
evGraph.GetYaxis().SetRangeUser(0,120)
evGraph.SetTitle("Timing vs. N_{threads} (1 job)")
evGraph.GetYaxis().SetTitle("Processing Time (ms)")
evGraph.GetXaxis().SetTitle("N_{threads}")
apGraph.SetMarkerColor(2)
apGraph.SetMarkerStyle(24)

leg = TLegend(0.4,0.1,0.9,0.5,"")
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.AddEntry(evGraph,"Event Time","p")
leg.AddEntry(apGraph,"All Paths Time","p")

c1 = TCanvas()

evGraph.Draw("ap")
apGraph.Draw("psame")
leg.Draw("same")
pdfTiming = "Timing_AllPaths_vs_Event_%s.pdf" % mt.name
c1.Print(pdfTiming)


### Make Throughput Plot #############
thruGraph = TGraph(len(threads))
for i in range(0,len(threads)):
    hist = tfiles[i].Get("DQMData/Run 256843/HLT/Run summary/Throughput/throughput_retired")
    throughput = getAvgThru(hist)/float(threads[i])
    thruGraph.SetPoint(i,threads[i],throughput)

thruGraph.SetMarkerColor(1)
thruGraph.SetMarkerStyle(22)
thruGraph.GetYaxis().SetRangeUser(0,200)
thruGraph.GetYaxis().SetTitle(" < N_events> / 10s / thread")
thruGraph.GetXaxis().SetTitle(" N_{threads}")
thruGraph.SetTitle("Average Job Throughput per Thread")
thruGraph.Draw("ap")
thruName="Throughput_vs_Threads_%s.pdf" % mt.name
c1.Print(thruName)
