#/usr/bin/python

#setup argument parser
import argparse

parser = argparse.ArgumentParser(description='A script to plot several timing histograms on top of one another. Pass it arguments for files, runs, and, if needed process names (assumes HLTX by default). For more than one file the arguments should be comma separated lists ordered respectively. Makes an output file called validation_plot.pdf Usage: python validation_plot.py --inputfiles INPUTFILES --runs RUNNUMBERS --processes PROCESSNAMES --log')


parser.add_argument("--inputfiles", type=str, help='The list of input files, comma separated if files should be added together, semicolon separated if files should not be added together',required=True,nargs=1)
parser.add_argument("--runs",type=str,help='the corresponding run numbers, set to 1 by default, separate by commas for input files that should be added, by semicolons for inputfiles that should be plotted separately',nargs=1)
parser.add_argument("--processes",type=str,help='the corresponding process names, set to HLTX by default',nargs=1)
parser.add_argument("--names",type=str,help='comma separated names for each summed plot',nargs=1)
parser.add_argument("--log",dest='log',action='store_true',help='specify to set log scale on the plot')
parser.add_argument("--ext",dest='ext',action='store_true',help='specify to set extended x-axis')
parser.add_argument("--outfile",type=str,help='optional outfile name',nargs=1)
args=parser.parse_args()


#import root libraries
from ROOT import gROOT, TCanvas, TH1F, TFile, TLegend, gStyle

#remove stat box
gStyle.SetOptStat(False)

dirs = []
iter=0
files = args.inputfiles[0].split(":")
runs = []

it=0
nRunsTot=0

runs = args.runs[0].split(":")

                    
def makeHist(runs,files,process):
    splitruns = runs.split(',')
    splitfiles = files.split(',')
    tfiles = []
    for f in splitfiles:
        tfiles.append(TFile(f))

    mainhist = TH1F()
    it=0
    for run in splitruns: 
        directory = '/DQMData/Run %s/HLT/Run summary/TimerService/Running 1 processes/process %s/all_paths' % (run,process)
        temphist =  tfiles[it].Get(directory)
        print temphist
        mainhist.Add(temphist)
        it+=1

    return mainhist

hists = []
for i in range(0,len(files)):
    process = 'HLTX'
    hists.append(makeHist(runs[i],files[i],process))


    names = args.names[0].split(',')
    
c1 = TCanvas()
leg = TLegend(0.5,0.5,0.9,0.9)
leg.SetFillStyle(0)
leg.SetBorderSize(0)

for i in range(0,len(hists)):
    hist = hists[i]
    hist.SetLineColor(i+1)
    hist.SetTitle("HLT Processing Time")
    hist.GetXaxis().SetTitle("Processing Time (ms)")
    hist.GetYaxis().SetTitle("N_{Events}")
    label = names[i]+" Mean: %.2f" % hist.GetMean()
    leg.AddEntry(hist,label,"l")
    if args.ext:
        hist.GetXaxis().SetRangeUser(0,2000)
    else:
        hist.GetXaxis().SetRangeUser(0,400)
    if i==0:
        hist.Draw()
    else:
        hist.Draw("same")

leg.Draw("same")
if args.log:
    c1.SetLogy()

if args.outfile:
    filename=args.outfile[0]
else:
    filename='HLT_Validation_Plot.pdf'
c1.Print(filename)
 
