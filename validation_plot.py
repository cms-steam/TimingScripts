#/usr/bin/python

#setup argument parser
import argparse

parser = argparse.ArgumentParser(description='A script to plot several timing histograms on top of one another. Pass it arguments for files, runs, and, if needed process names (assumes HLTX by default). For more than one file the arguments should be comma separated lists ordered respectively. Makes an output file called validation_plot.pdf Usage: python validation_plot.py --inputfiles INPUTFILES --runs RUNNUMBERS --processes PROCESSNAMES')


parser.add_argument("--inputfiles", type=str, help='The list of input files, comma separated if more than one file',required=True,nargs=1)
parser.add_argument("--runs",type=str,help='the corresponding run numbers, set to 1 by default',nargs=1)
parser.add_argument("--processes",type=str,help='the corresponding process names, set to HLTX by default',nargs=1)

args=parser.parse_args()



from ROOT import gROOT, TCanvas, TH1, TFile 

multi=False
if args.inputfiles[0].find(","):
    files=args.inputfiles[0].split(",")
    if args.runs:
        runs=args.runs[0].split(",")
    else:
        j=0
        runs=[]
        while j<len(files):
            runs.append("1")
            j+=1
    if args.processes:
        processes=args.processes[0].split(",")
    else:
        k=0
        processes=[]
        while k < len(files):
            processes.append("HLTX")
            k+=1
    multi=True
else:
    files=args.inputfiles[0]
    if args.runs:
        runs=args.runs[0]
    else:
        runs=['1']
    if args.processes:
        processes=args.processes[0]
    else:
        processes=['HLTX']

i=0
while i<len(files):
    print "Adding file: %s to list of files to run with Run Number: %s and Process Name: %s" % (files[i],runs[i],processes[i])
    i+=1




#clear memory 
gROOT.Reset()
#make canvas to save plots to
c1 = TCanvas('c1')



 
