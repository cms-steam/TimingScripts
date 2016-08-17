#!/usr/env/python

import os
import argparse
parser = argparse.ArgumentParser(description='script to plot the timing vs. luminosity of different fills. Pass different fills as csv list and corresponding runs as csv list with a colon separating fills. The script relies on the dqm files existing and having been gotten via getDQM.py. Optionally pass names of hlt menus used for each fill. Usage: python fillComparison.py --fills fill1,fill2,etc --runs fill1run1,fill1run2:fill2run1,fill2run2,etc --hlt fill1hlt,fill2hlt.')

parser.add_argument("--fills",type=str,help='list of fill numbers (e.g 5010,5011,etc)',required=True,nargs=1)
parser.add_argument("--runs",type=str,help='list of runs comma separated intrafill and colon separated interfill (e.g. 275000,275001:275100,275101)',required=True,nargs=1)
parser.add_argument("--hlt",type=str,help='option list of menu names, should be one for each fill',required=False,nargs=1)

args = parser.parse_args()

#import helpful plotting functions
#from plotDQM import getGraph

from ROOT import *
def getGraph(tHist,lHist):
    times = []
    lumis = []
    npoints=0
    for i in range(0,tHist.GetNbinsX()):
        #print "timing: %f ; lumi: %f" % (tHist.GetBinContent(i+1),lHist.GetBinContent(i+1))
        if (tHist.GetBinContent(i+1)>0 or i<20):
            
            times.append(tHist.GetBinContent(i+1))
            lumis.append(lHist.GetBinContent(i+1))
            npoints+=1
            
    g = TGraph(npoints)
    for i in range(0,npoints):
        g.SetPoint(i,lumis[i],times[i])

#    g.SetMarkerStyle(22)
    g.SetTitle("Processing Time vs. Luminosity")
    g.GetXaxis().SetTitle("Instantaneous Luminosity (e30 cm^{-2})")
    g.GetYaxis().SetTitle("Processing time (ms)")
    return g


class fill(object):
    def __init__(self,number,runs,menu):
        self.number = number
        self.runs = runs
        self.menu = menu
        self.tHists = []
        self.lHists = []
        self.graph = TMultiGraph()

    def addTimeHist(self,f):
        self.tHists.append( f.Get("/HLT/TimerService/Running 4 processes/event_byls"))

    def addLumiHist(self,f):
        self.lHists.append( f.Get("/Scal/LumiScalers/Instant_Lumi"))
        
    def SetMultiGraph(self):
        for lh,th in zip(self.lHists,self.tHists):
            self.graph.Add( getGraph(lh,th) )
        self.graph.SetTitle("Processing Time vs. Luminosity; Luminosity (e30 cm^{-2}); Average Processing Time")

#get fills
fillnumbers = args.fills[0].split(',')
runnumbers = args.runs[0].split(':')

print fillnumbers, runnumbers

#create list of fills
fills = []

for f,it in zip(fillnumbers,range(0,1000)):
    #check for hlt name
    if args.hlt is not None:
        hltname=args.hlt[0].split(',')[it]
    else:
        hltname=''
    fills.append( fill(fillnumbers[it],runnumbers[it].split(','),hltname) )


#now add histograms to fills
for f in fills:
    for r in f.runs:
        timefname = "timeByLs_rootFiles/Global__Online__ALL__run%s.root" %r
        f.addTimeHist(TFile(timefname))
        lumifname = "lumi_rootFiles/Global__Online__ALL__run%s.root" %r
        f.addLumiHist(TFile(lumifname))

#set multigraph
for f in fills:
    f.SetMultiGraph()
    
#now draw

c = TCanvas()
leg = TLegend()

for f,it in zip(fills, range(0,10000)):
    f.graph.SetMarkerColor(it+1)
    if it==0:
        f.graph.Draw("APL")
    else:
        f.graph.Draw("p same")
    legtext ="Fill %s" % f.number
    if f.hlt is not '':
        legtext+="; HLT Menu: %s" % f.hlt
    leg.AddEntry(f.graph,legtext,"p")


pdfname = "FillComparison_"

for f in fills:
    pdfname+="%s_" % fill.number

pdfname+=".pdf"

c.Print()
