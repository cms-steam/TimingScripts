import os
import argparse
parser = argparse.ArgumentParser(description='script to plot the timing for luminosity ranges specified by the user based on provided root files - if the needed root files do not exist run getDQM.py first for the relevant runs. Specify the luminosity bins as comma separated list. Usage: python plotTimingVLumi.py --runs run1,run2,run3 --lumibins ')

parser.add_argument("--runs",type=str,help='list of runs comma separated',required=True,nargs=1)
parser.add_argument("--lumibins",type=str,help='comma separated list of lumi bins',required=True,nargs=1)

args = parser.parse_args()

def selectTimesFromLumi(lumilow,lumihigh,lhists,thists):
    ntimes=0
    time=0.0
    for lhist,thist in zip(lhists,thists):
        for i in range(1,lhist.GetNbinsX()+1):
            lumi = lhist.GetBinContent(i):
            if lumi>=lumilow and lumi<lumihigh:
                time+=thist.GetBinContent(i)
                ntimes+=1

    time = time/float(ntimes)
    return time

#get runs
runs = args.runs[0].split(',')

#get lumi bins
lumis = args.lumibins[0].split(',')


#get timing and lumi hists
thists = []
lhists = []
for run in runs:
    timef = TFile("timeByLs_rootFiles/Global__Online__ALL__run%s.root" %r)
    timehist = timef.Get("/HLT/TimerService/Running 4 processes/event_byls")
    thists.append(timehist)
    lumif = TFile("lumi_rootFiles/Global__Online__ALL__run%s.root" %r)
    lumihist = lumif.Get("/Scal/LumiScalers/Instant_Lumi")
    lhists.append(lumihist)



