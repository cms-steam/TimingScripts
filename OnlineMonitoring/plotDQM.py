#!/usr/env/python

import os
from ROOT import *
#runs = [275125,275124,275074,275073,275068,275067,275066,275059,275001,275000,274999,274998,274971,274969,274968,274959,274958,274956,274443,274442,274441,274440,274422,274421,274420,274388,274387,274345,274344,274338,274335,274319,274316,274315,274314,274286,274284,274282,275282,275283,275284,275286,275290,275291,275292,275293]
runs=[274282, 274284, 274286, 274314, 274315, 274316, 274319, 274335, 274338, 274344, 274345, 274387, 274388, 274420, 274421, 274422, 274440, 274441, 274442, 274443, 274956, 274958, 274959, 274968, 274969, 274971, 274998, 274999, 275000, 275001, 275059, 275066, 275067, 275068, 275073, 275074, 275124, 275125, 275282,275283,275284,275286,275290,275291,275292,275293,275309,275310,275311,275319,275326,275337,275338,275344,275345,275370,275371,275375]
thruRuns=[275319,275326,275337,275338,275344,275345,275370,275371,275375]

timingFiles = []
timeByLsFiles = []
lumiFiles = []
thruFiles = []
for run in runs:
    fname = "event_rootFiles/Global__Online__ALL__run%i.root" %run
    timingFiles.append(TFile(fname))

for run in runs:
    fname = "timeByLs_rootFiles/Global__Online__ALL__run%i.root" %run
    timeByLsFiles.append(TFile(fname))

for run in runs:
    fname = "lumi_rootFiles/Global__Online__ALL__run%i.root" %run
    lumiFiles.append(TFile(fname))

for run in thruRuns:
    fname = "throughput_rootFiles/Global__Online__ALL__run%i.root" %run
    thruFiles.append(TFile(fname))

timingHists = []

for f in timingFiles:
    hist = f.Get("/HLT/TimerService/Running 4 processes/event")
    timingHists.append(hist)

timingByLsHists = []

for f in timeByLsFiles:
    hist = f.Get("/HLT/TimerService/Running 4 processes/event_byls")
    timingByLsHists.append(hist)

lumiHists = []

for f in lumiFiles:
    hist = f.Get("/Scal/LumiScalers/Instant_Lumi")
    lumiHists.append(hist)

thruHists = []

for f in thruFiles:
    hist = f.Get("/HLT/Throughput/throughput_retired")
    thruHists.append(hist)

print len(runs)
#now define for fills
runs5030= runs[57:58]
tbls5030=timingByLsHists[57:58]
lumi5030=lumiHists[57:58]
thru5030=thruHists[8:9]

runs5029= runs[55:57]
tbls5029=timingByLsHists[55:57]
lumi5029=lumiHists[55:57]
thru5029=thruHists[6:8]

runs5028= runs[53:55]
tbls5028=timingByLsHists[53:55]
lumi5028=lumiHists[53:55]
thru5028=thruHists[4:6]

runs5027= runs[49:53]
tbls5027=timingByLsHists[49:53]
lumi5027=lumiHists[49:53]
thru5027=thruHists[0:4]

runs5026= runs[45:49]
tbls5026=timingByLsHists[45:49]
lumi5026=lumiHists[45:49]

runs5024= runs[38:45]
tbls5024=timingByLsHists[38:45]
lumi5024=lumiHists[38:45]

runs5021= runs[36:38]
tbls5021=timingByLsHists[36:38]
lumi5021=lumiHists[36:38]

runs5020= runs[30:36]
tbls5020=timingByLsHists[30:36]
lumi5020=lumiHists[30:36]

runs5017= runs[26:30]
tbls5017=timingByLsHists[26:30]
lumi5017=lumiHists[26:30]

runs5013= runs[23:26]
tbls5013=timingByLsHists[23:26]
lumi5013=lumiHists[23:26]

runs5005= runs[20:23]
tbls5005=timingByLsHists[20:23]
lumi5005=lumiHists[20:23]

def plotTiming(hists):
    c1=TCanvas()
    it=0
    leg = TLegend(0.4,0.3,0.9,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    
    gStyle.SetOptStat(False)
    
    for h in hists:

        it+=1
        h.Scale(1.0 / h.Integral() )
        h.SetLineColor(it)
        if it==1:
            h.Draw()
        else:
            h.Draw("same")
        overflow = h.GetBinContent(201)
        #print "overflow is: %.3f" % overflow
        name="Run: %i; Mean: %.1f; Overflow: %.3f" % (runs[it-1], h.GetMean(),overflow)
        leg.AddEntry(h,name,"l")

    leg.Draw("same")
        
    c1.Print("TimingComparison_Runs%i-%i.pdf" % (runs[0],runs[len(runs)-1]) )

def plotLogTiming(hists):
    c1=TCanvas()
    c1.SetLogy()
    it=0
    leg = TLegend(0.4,0.3,0.9,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    
    gStyle.SetOptStat(False)
    
    for h in hists:

        it+=1
        h.Scale(1.0 / h.Integral() )
        h.SetLineColor(it)
        if it==1:
            h.GetYaxis().SetRangeUser(.00009,10)
            h.Draw()
        else:
            h.Draw("same")
        overflow = h.GetBinContent(201)
        #print "overflow is: %.3f" % overflow
        name="Run: %i; Mean: %.1f; Overflow: %.3f" % (runs[it-1], h.GetMean(),overflow)
        leg.AddEntry(h,name,"l")

    leg.Draw("same")
        
    c1.Print("TimingComparison_Runs%i-%i_log.pdf" % (runs[0],runs[len(runs)-1]) )


def plotOverFlow(hists):
    c1=TCanvas()
    it=0
    leg = TLegend(0.5,0.3,0.9,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    
    gStyle.SetOptStat(False)
    hist = TH1F("hist","OverFlow Percentage v Run Number",len(hists),0,len(hists))
    for h in hists:

        it+=1
        h.Scale(1.0 / h.Integral() )
        h.SetLineColor(it)
        overflow = h.GetBinContent(201)
        hist.SetBinContent(it,overflow)
        hist.GetXaxis().SetBinLabel(it,"Run: %i" %runs[it-1])

    hist.GetYaxis().SetTitle("PercentageOverFlow")
    hist.SetMarkerStyle(22)
    hist.Draw("p")
    c1.Print("OverFlowComparison_Runs%i-%i.pdf" % (runs[0],runs[len(runs)-1]) )


def plotTimingVRun(hists):
    c1=TCanvas()

    it=0
    leg = TLegend(0.5,0.3,0.9,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    
    gStyle.SetOptStat(False)
    hist = TH1F("hist","ProcessingTime v Run Number",len(hists),0,len(hists))
    for h in hists:

        it+=1
        h.Scale(1.0 / h.Integral() )
        h.SetLineColor(it)
        hist.SetBinContent(it,h.GetMean())
        hist.GetXaxis().SetBinLabel(it,"Run: %i" %runs[it-1])

    hist.GetYaxis().SetTitle("AverageProcessingTime (ms)")
    hist.SetMarkerStyle(22)
    hist.Draw("p")
    c1.Print("Timing_V_Run_Runs%i-%i.pdf" % (runs[0],runs[len(runs)-1]) )


def plotTimingVOverFlow(hists):
    c1=TCanvas()

    it=0
    leg = TLegend(0.5,0.3,0.9,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    
    gStyle.SetOptStat(False)
    hist = TGraph(len(hists))
    for h in hists:

        it+=1
        h.Scale(1.0 / h.Integral() )
        h.SetLineColor(it)
        overflow=h.GetBinContent(h.GetNbinsX()+1)
        hist.SetPoint(it-1,overflow,h.GetMean())

    hist.GetYaxis().SetTitle("AverageProcessingTime (ms)")
    hist.GetXaxis().SetTitle("OverFlowPercentage")
    hist.SetMarkerStyle(22)
    hist.Draw("ap")
    c1.Print("Timing_V_OverFlow_Runs%i-%i.pdf" % (runs[0],runs[len(runs)-1]) )


def plotTimingVLumi(tHist,lHist,run):

    c1 = TCanvas()
    times = []
    lumis = []
    npoints=0
    for i in range(0,tHist.GetNbinsX()):
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
    g.Draw("ap")
    pdfname = "Timing_v_Lumi_Run%s.pdf" %run
    c1.Print(pdfname)

def plotTimingVLumiAll(tHists,lHists,runs):

    c1 = TCanvas()
    if len(runs)>5:
        leg = TLegend(0.1,0.3,0.5,0.9)
    else:
        leg = TLegend(0.1,0.6,0.5,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    it=0
    graphs =[]
    for run in runs:
        g = getGraph(tHists[it],lHists[it])
        #add a dummy point to make plotting axis range possible
        g.SetPoint(g.GetN(),10000,2000)
        g.GetXaxis().SetRangeUser(0,10000)
        g.GetYaxis().SetRangeUser(0,300)
        g.SetMarkerColor(it+1)
        g.SetFillColor(it+1)
        graphs.append(g)
        it+=1

    it=0
    for graph in graphs:
        graph.SetTitle("Processing Time vs. Luminosity")
        graph.GetXaxis().SetTitle("Instantaneous Luminosity (e30 cm^{-2})")
        graph.GetYaxis().SetTitle("Processing time (ms)")

        leg.AddEntry(graph,"Run: %s" % runs[it],"f")
        if it ==0:
            graph.Draw("ap")
        else:
            graph.Draw("psame")
        it+=1
    
    leg.Draw("same")
    c1.Print("Timing_vLumi_Runs%s-%s.pdf" % (runs[0],runs[len(runs)-1]))

def getGraph(tHist,lHist):
    times = []
    lumis = []
    npoints=0
    for i in range(0,tHist.GetNbinsX()):
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

def getThruGraph(tHist,lHist):
    times = []
    lumis = []
    npoints=0
    for i in range(0,lHist.GetNbinsX()):
        #skip above 1200 ls - where throughput service won't work
        if(i>1199):
            continue
        if (tHist.GetBinContent(i+1)>0 or i<20):
            j=(i+1)*7
            k=(i+1)*3
            times.append(tHist.GetBinContent(j) + tHist.GetBinContent(j-1)+ tHist.GetBinContent(j-2)+ tHist.GetBinContent(j-3)+ tHist.GetBinContent(j-4)+ tHist.GetBinContent(j-5)+ tHist.GetBinContent(j-6))
            lumis.append( ( lHist.GetBinContent(k) + lHist.GetBinContent(k-1) + lHist.GetBinContent(k-2)) /3)
            npoints+=1
            #print "lumi section: %i throughput: %.2f" % (i, tHist.GetBinContent(j)+tHist.GetBinContent(j-1))
    g = TGraph(npoints)
    for i in range(0,npoints):
        g.SetPoint(i,lumis[i],times[i])

#    g.SetMarkerStyle(22)
#    g.SetTitle("Processing Time vs. Luminosity")
#    g.GetXaxis().SetTitle("Instantaneous Luminosity (e30 cm^{-2})")
#    g.GetYaxis().SetTitle("Processing time (ms)")
    return g


def plotThroughputANDTiming(thruHist,timeHist,run):
    c = TCanvas()
    p1 = TPad()
    p2 = TPad()
    p2.SetFillStyle(40000)
    p1.Draw()
    p1.cd()
    leg = TLegend(0.5,0.6,0.9,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)

    timeHist.SetMarkerStyle(22)
    timeHist.SetMarkerColor(kBlue)
    timeHist.GetXaxis().SetRangeUser(0,700)
    thruHist.SetMarkerStyle(33)
    thruHist.SetMarkerColor(kRed)

    leg.AddEntry(timeHist,"Processing Time","p")
    leg.AddEntry(thruHist,"Throughput","p")

    timeHist.Draw()
    leg.Draw("same")
    p1.Update()
    c.cd()

    #set range for pad 2
    ymin =0
    ymax = 2500000
    dy = (ymax-ymin)/0.8
    xmin = 0
    xmax = 16800
    dx = (xmax-xmin)/0.8
    p2.Range(xmin-0.1*dx,ymin-0.1*dy,xmax+0.1*dx,ymax+0.1*dy)
    p2.Draw()
    p2.cd()
    thruHist.GetXaxis().SetRangeUser(0,16800)
    thruHist.Draw("][psames")
    p2.Update()
    raxis = TGaxis(xmax,ymin,xmax,ymax,ymin,ymax,50510,"+L")
    raxis.SetLabelColor(kRed)
    raxis.Draw()

    pdfname = "ThroughputAndTiming_Run%s.pdf" % run
    c.Print(pdfname)

def plotThroughputVLumi(thruHists,lHists,runs):

    c1 = TCanvas()
    if len(runs)>5:
        leg = TLegend(0.1,0.3,0.5,0.9)
    else:
        leg = TLegend(0.1,0.6,0.5,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    it=0
    graphs =[]
    for run in runs:
        #rebin throughput to be 70 seconds
        #thruHists[it].Rebin(5)
        #rebin lumi to be 70 seconds
        #lHists[it].Rebin(2)
        g = getThruGraph(thruHists[it],lHists[it])
        #add a dummy point to make plotting axis range possible
        g.SetPoint(g.GetN(),10000,2000)
        g.GetXaxis().SetRangeUser(0,10000)
        g.GetYaxis().SetRangeUser(0,8000000)
        g.SetMarkerColor(it+1)
        g.SetFillColor(it+1)
        graphs.append(g)
        it+=1

    it=0
    for graph in graphs:
        graph.SetTitle("Throughput vs. Luminosity")
        graph.GetXaxis().SetTitle("Instantaneous Luminosity (e30 cm^{-2})")
        graph.GetYaxis().SetTitle("Throughput (evts/70s)")

        leg.AddEntry(graph,"Run: %s" % runs[it],"f")
        if it ==0:
            graph.Draw("ap")
        else:
            graph.Draw("psame")
        it+=1
    
    leg.Draw("same")
    c1.Print("Throughput_vLumi_Runs%s-%s.pdf" % (runs[0],runs[len(runs)-1]))
    

plotTiming(timingHists)
plotLogTiming(timingHists)
plotOverFlow(timingHists)
plotTimingVRun(timingHists)
plotTimingVOverFlow(timingHists)
it=0
for run in runs:
    plotTimingVLumi(timingByLsHists[it],lumiHists[it],run)
    it+=1

plotTimingVLumiAll(timingByLsHists,lumiHists,runs)
plotThroughputVLumi(thru5029,lumi5029,runs5029)
plotThroughputVLumi(thru5028,lumi5028,runs5028)
plotThroughputVLumi(thru5027,lumi5027,runs5027)
plotTimingVLumiAll(tbls5029,lumi5029,runs5029)
plotTimingVLumiAll(tbls5028,lumi5028,runs5028)
plotTimingVLumiAll(tbls5027,lumi5027,runs5027)
plotTimingVLumiAll(tbls5026,lumi5026,runs5026)
plotTimingVLumiAll(tbls5024,lumi5024,runs5024)
plotTimingVLumiAll(tbls5021,lumi5021,runs5021)
plotTimingVLumiAll(tbls5020,lumi5020,runs5020)
plotTimingVLumiAll(tbls5017,lumi5017,runs5017)
plotTimingVLumiAll(tbls5013,lumi5013,runs5013)
plotTimingVLumiAll(tbls5005,lumi5005,runs5005)

it=0
for run in runs5029:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5029[it],tbls5029[it],run)
    it+=1

it=0
for run in runs5028:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5028[it],tbls5028[it],run)
    it+=1

it=0
for run in runs5027:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5027[it],tbls5027[it],run)
    it+=1
