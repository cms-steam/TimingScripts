#!/usr/env/python

import os
import argparse
parser = argparse.ArgumentParser(description='script to plot the timing vs. luminosity of different fills. Pass different fills as csv list and corresponding runs as csv list with a colon separating fills. The script relies on the dqm files existing and having been gotten via getDQM.py. Optionally pass names of hlt menus used for each fill. Usage: python fillComparison.py --fills fill1,fill2,etc --runs fill1run1,fill1run2:fill2run1,fill2run2,etc --hlt fill1hlt,fill2hlt')

parser.add_argument("--fills",type=str,help='list of fill numbers (e.g 5010,5011,etc)',required=True,nargs=1)
parser.add_argument("--runs",type=str,help='list of runs comma separated intrafill and colon separated interfill (e.g. 275000,275001:275100,275101)',required=True,nargs=1)
parser.add_argument("--hlt",type=str,help='option list of menu names, should be one for each fill',required=False,nargs=1)
parser.add_argument("--cmssw",type=str,help='option list of cmssw version used, should be one for each fill',required=False,nargs=1)

args = parser.parse_args()

#import helpful plotting functions
#from plotDQM import getGraph
import sys
sys.path.append('../Classes/')
from dqmFunctions import *

from ROOT import *



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
    if args.cmssw is not None:
        cmsswname = args.cmssw[0].split(',')[it]
    else:
        cmsswname = ''
    fills.append( fill(fillnumbers[it],runnumbers[it].split(','),hltname,cmsswname) )


#now add histograms to fills

for f in fills:
    # make file lists
    for r in f.runs:
        timefname = "timeByLs_rootFiles/Global__Online__ALL__run%s.root" %r
        f.tFiles.append(TFile(timefname))
        lumifname = "lumi_rootFiles/Global__Online__ALL__run%s.root" %r
        f.lFiles.append(TFile(lumifname))
#        lhist = flumi.Get("/Scal/LumiScalers/Instant_Lumi")
        #f.lHists.append(lhist)

    #make histograms
    for lf in f.lFiles:
        f.lHists.append( lf.Get("/Scal/LumiScalers/Instant_Lumi"))
    for tf in f.tFiles:
        f.tHists.append( tf.Get("/HLT/TimerService/Running 4 processes/event_byls") )
    #print f.lHists, f.tHists

#set multigraph
for f in fills:
    f.SetGraph()
    
#now draw

c = TCanvas()
leg = TLegend(0.1,0.5,0.5,0.9)

for f,it in zip(fills, range(0,10000)):
    f.graph.SetMarkerColor(it+1)
    f.graph.SetFillColor(it+1)
    if it==0:
        f.graph.GetXaxis().SetLimits(0,13000)
        f.graph.Draw("AP")
        #f.graph.GetYaxis().SetRangeUser(0,250)
        #f.graph.Draw("AP")
    else:
        f.graph.Draw("p same")
    legtext ="Fill %s" % f.number
    if f.menu is not '':
        legtext+="; HLT Menu: %s" % f.menu
    if f.cmssw is not '':
        legtext+="; %s" % f.cmssw
    leg.AddEntry(f.graph,legtext,"f")

leg.SetBorderSize(0)
leg.SetFillStyle(0)
leg.Draw("same")

pdfname = "FillComparison"

for f in fills:
    pdfname+="_%s" % f.number

pdfname+=".pdf"

c.Print(pdfname)
