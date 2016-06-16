#!/usr/env/python

import os
from ROOT import *
runs = [275125,275124,275074,275073,275068,275067,275066,275059,275001,275000,274999,274998,274971,274969,274968,274959,274958,274956,274443,274442,274441,274440,274422,274421,274420,274388,274387,274345,274344,274338,274335,274319,274316,274315,274314,274286,274284,274282]
timingFiles = []
timeByLsFiles = []
lumiFiles = []
for run in runs:
    fname = "event_rootFiles/Global__Online__ALL__run%i.root" %run
    timingFiles.append(TFile(fname))

for run in runs:
    fname = "timeByLs_rootFiles/Global__Online__ALL__run%i.root" %run
    timeByLsFiles.append(TFile(fname))

for run in runs:
    fname = "lumi_rootFiles/Global__Online__ALL__run%i.root" %run
    lumiFiles.append(TFile(fname))

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


#now define for fills
runs5021= runs[0:2]
tbls5021=timingByLsHists[0:2]
lumi5021=lumiHists[0:2]

runs5020= runs[2:8]
tbls5020=timingByLsHists[2:8]
lumi5020=lumiHists[2:8]

runs5017= runs[8:12]
tbls5017=timingByLsHists[8:12]
lumi5017=lumiHists[8:12]

runs5013= runs[12:15]
tbls5013=timingByLsHists[12:15]
lumi5013=lumiHists[12:15]

runs5005= runs[15:18]
tbls5005=timingByLsHists[15:18]
lumi5005=lumiHists[15:18]

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
        print "overflow is: %.3f" % overflow
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
        print "overflow is: %.3f" % overflow
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
        g.GetYaxis().SetRangeUser(0,250)
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
plotTimingVLumiAll(tbls5021,lumi5021,runs5021)
plotTimingVLumiAll(tbls5020,lumi5020,runs5020)
plotTimingVLumiAll(tbls5017,lumi5017,runs5017)
plotTimingVLumiAll(tbls5013,lumi5013,runs5013)
plotTimingVLumiAll(tbls5005,lumi5005,runs5005)
