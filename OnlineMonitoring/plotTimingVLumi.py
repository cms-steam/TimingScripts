import os
import argparse
parser = argparse.ArgumentParser(description='script to plot the timing for luminosity ranges specified by the user based on provided root files - if the needed root files do not exist run getDQM.py first for the relevant runs. Specify the luminosity bins as comma separated list. Usage: python plotTimingVLumi.py --runs run1,run2,run3 --lumibins ')

parser.add_argument("--runs",type=str,help='list of runs comma separated',required=True,nargs=1)
parser.add_argument("--lumibins",type=str,help='comma separated list of lumi bins',required=True,nargs=1)

args = parser.parse_args()

def getAverageTimeForLumiRange(lumilow,lumihigh,lhists,thists):
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
lumibins = args.lumibins[0].split(',')


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


#now get average timing for each lumibin
times=[] #will hold average time for each bin
lumis=[] #note that this will be the central value of each bin
for i in range(0,len(lumibins)-1): # len(lumis)-1 so we don't access outside the list
    time =  getAverageTimeForLumiRange(lumibins[i],lumibins[i+1],thists,lhists)
    times.append(time)
    lumi = (lumibins[i]+lumibins[i+1])/2.0
    lumis.append(lumi)


#now make TGraph and plot
c = TCanvas()
g = TGraph(len(lumis),lumis,times)
g.SetMarkerStyle(22)
g.SetMarkerColor(kBlack)
g.Draw("ap")
g.SetTitle("Processing Time vs. Luminosity - Averaged")
g.GetXaxis().SetTitle("Average Luminosity (1e33)")
g.GetYaxis().SetTitle("Average Processing Time")
g.Draw("ap")

name = "Timing_v_AveragedLumi_Run%s-%s" % (runs[0],runs[-1])
c.Print(name+".root")
c.Print(name+".png")
c.Print(name+".pdf")
c.Print(name+".C")
