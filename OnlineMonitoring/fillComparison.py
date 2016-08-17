#!/usr/env/python

import os
import argparse
parser = argparse.ArgumentParser(description='script to plot the timing vs. luminosity of different fills. Pass different fills as csv list and corresponding runs as csv list with semicolon separating fills. The script relies on the dqm files existing and having been gotten via getDQM.py. Optionally pass names of hlt menus used for each fill. Usage: python fillComparison.py --fills fill1,fill2,etc --runs fill1run1,fill1run2;fill2run1,fill2run2,etc --hlt fill1hlt,fill2hlt.')

parser.add_argument("--fills",type=str,help='list of fill numbers (e.g 5010,5011,etc)',required=True,nargs=1)
parser.add_argument("--runs",type=str,help='list of runs comma separated intrafill and semi-colon separated interfill (e.g. 275000,275001;275100,275101)',required=True,nargs=1)
parser.add_argument("--hlt",type=str,help='option list of menu names, should be one for each fill',required=False,nargs=1)

args = parser.parse_args()

#import helpful plotting functions
from plotDQM import *

class fill(object):
    def __init__(self,number,runs,menu)
    self.number = number
    self.runs = runs
    self.menu = menu
    self.tHists = []
    self.lHists = []

    def addTimeHist(self,f):
        self.tHists.append( f.Get("/HLT/TimerService/Running 4 processes/event_byls"))

    def addLumiHist(self,f):
        self.lHists.append( f.Get("/Scal/LumiScalers/Instant_Lumi"))
        

#get fills
fillnumbers = args.fills[0].split(',')
runnumbers = args.runs[0].split(';')

#create list of fills
fills = []
it=0
for f in fillnumbers:
    #check for hlt name
    if args.hlt is not None:
        hltname=args.hlt[0].split(',')[it]
    else:
        hltname=''
    fills.append( fill(fillnumbers[it],runnumbers[it],hltname) )

#now add histograms to fills
for f in fills:
    for r in f.runs:
        timefname = "timeByLs_rootFiles/Global__Online__ALL__run%i.root" %r
        f.addTimeHist(TFile(timefname))
        lumifname = "lumi_rootFiles/Global__Online__ALL__run%i.root" %r
        f.addLumiHist(TFile(lumifname))

#make list of graphs corresponding to each fill
