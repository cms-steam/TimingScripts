#!/usr/env/python

import os
from ROOT import *
#runs = [275125,275124,275074,275073,275068,275067,275066,275059,275001,275000,274999,274998,274971,274969,274968,274959,274958,274956,274443,274442,274441,274440,274422,274421,274420,274388,274387,274345,274344,274338,274335,274319,274316,274315,274314,274286,274284,274282,275282,275283,275284,275286,275290,275291,275292,275293]
runs=[274282, 274284, 274286, 274314, 274315, 274316, 274319, 274335, 274338, 274344, 274345, 274387, 274388, 274420, 274421, 274422, 274440, 274441, 274442, 274443, 274956, 274958, 274959, 274968, 274969, 274971, 274998, 274999, 275000, 275001, 275059, 275066, 275067, 275068, 275073, 275074, 275124, 275125, 275282,275283,275284,275286,275290,275291,275292,275293,275309,275310,275311,275319,275326,275337,275338,275344,275345,275370,275371,275375,275376,275657,275658,275757,275768,275772,275774,275776,275777,275778,275782,275783,275828,275832,275833,275834,275836,275837,275847,275886,275887,275890,275911,275912,275913,275918,275920,275923,275931,275963,276092,276097,276242,276243,276244,276282,276283,276315,276317,276318,276327,276352,276355,276357,276361,276363,276384,276437,276453,276454,276455,276456,276458,276495,276501,276502,276525,276527,276528,276542,276544,276544,276545,276581,276582,276585,276586,276587,276653,276655,276659,276775,276776,276794,276807,276808,276810,276811,276831,276834,276870,276935,277069,277070,277071,277072,277076,277087,277094]
thruRuns=[275319,275326,275337,275338,275344,275345,275370,275371,275375,275376,275657,275658,275757,275768,275772,275774,275776,275777,275778,275782,275783,275828,275832,275833,275834,275836,275837,275847,275886,275887,275890,275911,275912,275913,275918,275920,275923,275931,275963,276092,276097,276242,276243,276244,276282,276283,276315,276317,276318,276327,276352,276355,276357,276361,276363,276384,276437,276453,276454,276455,276456,276458,276495,276501,276502,276525,276527,276528,276542,276544,276544,276545,276581,276582,276585,276586,276587,276653,276655,276659,276775,276776,276794,276807,276808,276810,276811,276831,276834,276870,276935,277069,277070,277071,277072,277076,277087,277094]
print len(runs), len(thruRuns)
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
    hist = (f.Get("/HLT/TimerService/Running 4 processes/event_byls"))
    timingByLsHists.append(hist)

lumiHists = []

for f in lumiFiles:
    hist = f.Get("/Scal/LumiScalers/Instant_Lumi")
    lumiHists.append(hist)

thruHists = []

for f in thruFiles:
    hist = f.Get("/HLT/Throughput/throughput_retired")
    thruHists.append(hist)


#now define for fills
runs5106= runs[146:147]
tbls5106=timingByLsHists[146:147]
lumi5106=lumiHists[146:147]
thru5106=thruHists[97:98]

runs5105= runs[140:146]
tbls5105=timingByLsHists[140:146]
lumi5105=lumiHists[140:146]
thru5105=thruHists[91:97]

runs5101= runs[139:140]
tbls5101=timingByLsHists[139:140]
lumi5101=lumiHists[139:140]
thru5101=thruHists[90:91]

runs5097= runs[138:139]
tbls5097=timingByLsHists[138:139]
lumi5097=lumiHists[138:139]
thru5097=thruHists[89:90]

runs5096= runs[136:138]
tbls5096=timingByLsHists[136:138]
lumi5096=lumiHists[136:138]
thru5096=thruHists[87:89]

runs5095= runs[132:136]
tbls5095=timingByLsHists[132:136]
lumi5095=lumiHists[132:136]
thru5095=thruHists[83:87]

runs5093= runs[129:132]
tbls5093=timingByLsHists[129:132]
lumi5093=lumiHists[129:132]
thru5093=thruHists[80:83]

runs5091= runs[126:129]
tbls5091=timingByLsHists[126:129]
lumi5091=lumiHists[126:129]
thru5091=thruHists[77:80]

runs5085= runs[121:126]
tbls5085=timingByLsHists[121:126]
lumi5085=lumiHists[121:126]
thru5085=thruHists[72:77]

runs5083= runs[117:121]
tbls5083=timingByLsHists[117:121]
lumi5083=lumiHists[117:121]
thru5083=thruHists[68:72]

runs5080= runs[114:117]
tbls5080=timingByLsHists[114:117]
lumi5080=lumiHists[114:117]
thru5080=thruHists[65:68]

runs5078= runs[111:114]
tbls5078=timingByLsHists[111:114]
lumi5078=lumiHists[111:114]
thru5078=thruHists[62:65]

runs5076= runs[105:111]
tbls5076=timingByLsHists[105:111]
lumi5076=lumiHists[105:111]
thru5076=thruHists[56:62]

runs5073= runs[99:105]
tbls5073=timingByLsHists[99:105]
lumi5073=lumiHists[99:105]
thru5073=thruHists[50:56]

runs5072= runs[95:99]
tbls5072=timingByLsHists[95:99]
lumi5072=lumiHists[95:99]
thru5072=thruHists[46:50]

runs5071= runs[93:95]
tbls5071=timingByLsHists[93:95]
lumi5071=lumiHists[93:95]
thru5071=thruHists[44:46]

runs5069= runs[90:93]
tbls5069=timingByLsHists[90:93]
lumi5069=lumiHists[90:93]
thru5069=thruHists[41:44]

runs5060= runs[88:90]
tbls5060=timingByLsHists[88:90]
lumi5060=lumiHists[88:90]
thru5060=thruHists[39:41]

runs5056= runs[87:88]
tbls5056=timingByLsHists[87:88]
lumi5056=lumiHists[87:88]
thru5056=thruHists[38:39]

runs5052= runs[80:87]
tbls5052=timingByLsHists[80:87]
lumi5052=lumiHists[80:87]
thru5052=thruHists[31:38]

runs5048= runs[77:80]
tbls5048=timingByLsHists[77:80]
lumi5048=lumiHists[77:80]
thru5048=thruHists[28:31]

runs5045= runs[70:77]
tbls5045=timingByLsHists[70:77]
lumi5045=lumiHists[70:77]
thru5045=thruHists[21:28]

runs5043= runs[61:70]
tbls5043=timingByLsHists[61:70]
lumi5043=lumiHists[61:70]
thru5043=thruHists[12:21]

runs5038= runs[59:61]
tbls5038=timingByLsHists[59:61]
lumi5038=lumiHists[59:61]
thru5038=thruHists[10:12]

runs5030= runs[57:59]
tbls5030=timingByLsHists[57:59]
lumi5030=lumiHists[57:59]
thru5030=thruHists[8:10]

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
    #fiitng
    lin = TF1("lin","pol1",3000,12000)
    line = TLine(3000,205,12000,205)
    line.SetLineColor(kRed)
    quad = TF1("quad","pol2",3000,12000)
    g.Fit(quad)
    quad.SetLineColor(kGreen)
    g.Fit(lin)
    lin.SetLineColor(kBlue)
    #dummy point pst fit for drawing
    g.SetPoint(npoints,50000,500)
    g.SetTitle("Processing Time vs. Luminosity")
    g.GetXaxis().SetTitle("Instantaneous Luminosity (e30 cm^{-2})")
    g.GetXaxis().SetRangeUser(3000,12000)
    g.GetYaxis().SetTitle("Processing time (ms)")
    g.GetYaxis().SetRangeUser(0,300)
    g.Draw("ap")
    quad.Draw("same")
    lin.Draw("same")
    line.Draw("same")
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
        g.GetXaxis().SetRangeUser(0,16000)
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

def plotTimingVPileupAll(tHists,lHists,runs):
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
        
        g = getPileupGraph(tHists[it],lHists[it])
        #add a dummy point to make plotting axis range possible
        g.SetPoint(g.GetN(),10000,2000)
        g.GetXaxis().SetRange(0,60)
        g.GetYaxis().SetRangeUser(0,300)
        g.SetMarkerColor(it+1)
        g.SetFillColor(it+1)
        graphs.append(g)
        it+=1

    it=0
    for graph in graphs:
        graph.SetTitle("Processing Time vs. Pileup")
        graph.GetXaxis().SetTitle("Pileup")
        graph.GetYaxis().SetTitle("Processing time (ms)")
        graph.GetXaxis().SetRangeUser(0,60)
        leg.AddEntry(graph,"Run: %s" % runs[it],"f")
        if it ==0:
            graph.Draw("ap")
            graph.GetXaxis().SetRangeUser(0,60)
            graph.Draw("ap")
            c1.Update()
        else:
            graph.Draw("psame")
        it+=1
    
    leg.Draw("same")
    c1.Print("Timing_vPileup_Runs%s-%s.pdf" % (runs[0],runs[len(runs)-1]))


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



def getPileupGraph(tHist,lHist):
    times = []
    lumis = []
    npoints=0
    for i in range(0,tHist.GetNbinsX()):
        #print "timing: %f ; lumi: %f" % (tHist.GetBinContent(i+1),lHist.GetBinContent(i+1))
        if (tHist.GetBinContent(i+1)>0 or i<20):
            
            times.append(tHist.GetBinContent(i+1))
            pileup = (lHist.GetBinContent(i+1) * 71.3*.54)/ 11246.0
            print pileup
            lumis.append(pileup)
            npoints+=1
            
    g = TGraph(npoints)
    for i in range(0,npoints):
        g.SetPoint(i,lumis[i],times[i])

#    g.SetMarkerStyle(22)
    g.SetTitle("Processing Time vs. Pileup")
    g.GetXaxis().SetTitle("Instantaneous Pileup")
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

plotThroughputVLumi(thru5106,lumi5106,runs5106)
plotThroughputVLumi(thru5105,lumi5105,runs5105)
plotThroughputVLumi(thru5101,lumi5101,runs5101)
plotThroughputVLumi(thru5097,lumi5097,runs5097)
plotThroughputVLumi(thru5096,lumi5096,runs5096)
plotThroughputVLumi(thru5095,lumi5095,runs5095)
plotThroughputVLumi(thru5093,lumi5093,runs5093)
plotThroughputVLumi(thru5091,lumi5091,runs5091)
plotThroughputVLumi(thru5085,lumi5085,runs5085)
plotThroughputVLumi(thru5083,lumi5083,runs5083)
plotThroughputVLumi(thru5080,lumi5080,runs5080)
plotThroughputVLumi(thru5078,lumi5078,runs5078)
plotThroughputVLumi(thru5076,lumi5076,runs5076)
plotThroughputVLumi(thru5073,lumi5073,runs5073)
plotThroughputVLumi(thru5072,lumi5072,runs5072)
plotThroughputVLumi(thru5071,lumi5071,runs5071)
plotThroughputVLumi(thru5069,lumi5069,runs5069)
plotThroughputVLumi(thru5060,lumi5060,runs5060)
plotThroughputVLumi(thru5056,lumi5056,runs5056)
plotThroughputVLumi(thru5052,lumi5052,runs5052)
plotThroughputVLumi(thru5048,lumi5048,runs5048)
plotThroughputVLumi(thru5045,lumi5045,runs5045)
plotThroughputVLumi(thru5043,lumi5043,runs5043)
plotThroughputVLumi(thru5038,lumi5038,runs5038)
plotThroughputVLumi(thru5030,lumi5030,runs5030)
plotThroughputVLumi(thru5029,lumi5029,runs5029)
plotThroughputVLumi(thru5028,lumi5028,runs5028)
plotThroughputVLumi(thru5027,lumi5027,runs5027)

plotTimingVLumiAll(tbls5106,lumi5106,runs5106)
plotTimingVLumiAll(tbls5105,lumi5105,runs5105)
plotTimingVLumiAll(tbls5101,lumi5101,runs5101)
plotTimingVLumiAll(tbls5097,lumi5097,runs5097)
plotTimingVLumiAll(tbls5096,lumi5096,runs5096)
plotTimingVLumiAll(tbls5095,lumi5095,runs5095)
plotTimingVLumiAll(tbls5093,lumi5093,runs5093)
plotTimingVLumiAll(tbls5091,lumi5091,runs5091)
plotTimingVLumiAll(tbls5085,lumi5085,runs5085)
plotTimingVLumiAll(tbls5083,lumi5083,runs5083)
plotTimingVLumiAll(tbls5080,lumi5080,runs5080)
plotTimingVLumiAll(tbls5078,lumi5078,runs5078)
plotTimingVLumiAll(tbls5076,lumi5076,runs5076)
plotTimingVLumiAll(tbls5073,lumi5073,runs5073)
plotTimingVLumiAll(tbls5072,lumi5072,runs5072)
plotTimingVLumiAll(tbls5071,lumi5071,runs5071)
plotTimingVLumiAll(tbls5069,lumi5069,runs5069)
plotTimingVLumiAll(tbls5060,lumi5060,runs5060)
plotTimingVLumiAll(tbls5056,lumi5056,runs5056)
plotTimingVLumiAll(tbls5052,lumi5052,runs5052)
plotTimingVLumiAll(tbls5048,lumi5048,runs5048)
plotTimingVLumiAll(tbls5045,lumi5045,runs5045)
plotTimingVLumiAll(tbls5043,lumi5043,runs5043)
plotTimingVLumiAll(tbls5038,lumi5038,runs5038)
plotTimingVLumiAll(tbls5030,lumi5030,runs5030)
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

plotTimingVPileupAll(tbls5106,lumi5106,runs5106)
plotTimingVPileupAll(tbls5105,lumi5105,runs5105)
plotTimingVPileupAll(tbls5101,lumi5101,runs5101)
plotTimingVPileupAll(tbls5097,lumi5097,runs5097)
plotTimingVPileupAll(tbls5096,lumi5096,runs5096)
plotTimingVPileupAll(tbls5095,lumi5095,runs5095)
plotTimingVPileupAll(tbls5093,lumi5093,runs5093)
plotTimingVPileupAll(tbls5091,lumi5091,runs5091)
plotTimingVPileupAll(tbls5085,lumi5085,runs5085)
plotTimingVPileupAll(tbls5083,lumi5083,runs5083)
plotTimingVPileupAll(tbls5080,lumi5080,runs5080)
plotTimingVPileupAll(tbls5078,lumi5078,runs5078)
plotTimingVPileupAll(tbls5076,lumi5076,runs5076)
plotTimingVPileupAll(tbls5073,lumi5073,runs5073)
plotTimingVPileupAll(tbls5072,lumi5072,runs5072)
plotTimingVPileupAll(tbls5071,lumi5071,runs5071)
plotTimingVPileupAll(tbls5069,lumi5069,runs5069)
plotTimingVPileupAll(tbls5060,lumi5060,runs5060)
plotTimingVPileupAll(tbls5056,lumi5056,runs5056)
plotTimingVPileupAll(tbls5052,lumi5052,runs5052)
plotTimingVPileupAll(tbls5048,lumi5048,runs5048)
plotTimingVPileupAll(tbls5045,lumi5045,runs5045)
plotTimingVPileupAll(tbls5043,lumi5043,runs5043)
plotTimingVPileupAll(tbls5038,lumi5038,runs5038)
plotTimingVPileupAll(tbls5030,lumi5030,runs5030)
plotTimingVPileupAll(tbls5029,lumi5029,runs5029)
plotTimingVPileupAll(tbls5028,lumi5028,runs5028)
plotTimingVPileupAll(tbls5027,lumi5027,runs5027)
plotTimingVPileupAll(tbls5026,lumi5026,runs5026)
plotTimingVPileupAll(tbls5024,lumi5024,runs5024)
plotTimingVPileupAll(tbls5021,lumi5021,runs5021)
plotTimingVPileupAll(tbls5020,lumi5020,runs5020)
plotTimingVPileupAll(tbls5017,lumi5017,runs5017)
plotTimingVPileupAll(tbls5013,lumi5013,runs5013)
plotTimingVPileupAll(tbls5005,lumi5005,runs5005)


it=0
for run in runs5071:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5071[it],tbls5071[it],run)
    it+=1

it=0
for run in runs5069:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5069[it],tbls5069[it],run)
    it+=1

it=0
for run in runs5060:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5060[it],tbls5060[it],run)
    it+=1

it=0
for run in runs5056:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5056[it],tbls5056[it],run)
    it+=1

it=0
for run in runs5052:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5052[it],tbls5052[it],run)
    it+=1

it=0
for run in runs5048:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5048[it],tbls5048[it],run)
    it+=1

it=0
for run in runs5045:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5045[it],tbls5045[it],run)
    it+=1

it=0
for run in runs5043:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5043[it],tbls5043[it],run)
    it+=1

it=0
for run in runs5038:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5038[it],tbls5038[it],run)
    it+=1

it=0
for run in runs5030:
    print "it: %i run %s" % (it,run)
    plotThroughputANDTiming(thru5030[it],tbls5030[it],run)
    it+=1

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
