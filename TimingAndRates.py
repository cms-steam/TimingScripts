#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='A script which is just a nice wrapper for running a root macro to generate a csv file full of the timing and rates for paths from a dqm timing file. Usage: python TimingAndRates.py --inpufile INFILE [--mc --time TIME] [--data --lumis nLumis] [--outfile OUTFILE]')

parser.add_argument("--inputfile", type=str,help='The name of the DQM file you want to run the script over',required=True,nargs=1)
parser.add_argument("--outfile", type=str, help="Use to customize the name of the output file if you wish. Otherwise it will be called HLT_Paths_TimingAndRates.csv. NB: File type should be .csv", nargs=1)
parser.add_argument("--mc", dest='mc',action='store_true', help='specify to run on mc, all this means is you need to specify the number of seconds yourself for the rate calculation')
parser.add_argument("--data",dest='data',action='store_true', help='specify to run on data, if you use this you must also specify lumi sections')
parser.add_argument("--time",type=float, help='for MC: the amount of time in the detector the sample represents',nargs=1)
parser.add_argument("--lumis",type=float, help='for Data: the number of lumi sections run', nargs=1)
parser.add_argument("--run",type=int, help="for Data: specify the run number",nargs=1)
parser.add_argument("--process",type=str, help="In case the name of the process used is not HLTX specify it with this",nargs=1)

args = parser.parse_args()

nSeconds=0.0
run=1
if args.mc:
    if not args.time:
        print "Error! Need to specify time when running with mc option"
        quit()
    elif args.data:
        print "Error! Can only specify either mc or data - not both"
        quit()
    else:
        print "running mc with time in event: %f" % args.time[0]
        nSeconds=args.time[0]

if args.data:
    if not args.lumis:
        print "Error! Need to specify lumis when running on data"
        quit()
    elif not args.run:
        print "Error! Need to specify run number"
        quit()
    else:
        nSeconds = args.lumis[0] * 23.3
        run=args.run[0]
        print "running data with %f lumis corresponding to %f seconds for run number %i" % (args.lumis[0],nSeconds,run)


import os
#run root macro
cmdstring=''

if args.outfile:
    print 'Customizing to make output file', args.outfile[0]
    if args.data:
        cmdstring='root -b -q -l \'TimingAndRates.cc(%f,\"%s\",%i,\"%s\",\"HLT\")\'' % (nSeconds,args.inputfile[0],run,args.outfile[0])
    else:
        if args.process:
            cmdstring='root -b -q -l \'TimingAndRates.cc(%f,\"%s\",1,\"%s\",\"%s\")\'' % (nSeconds,args.inputfile[0],args.outfile[0],args.process[0])
        else:
                        cmdstring='root -b -q -l \'TimingAndRates.cc(%f,\"%s\",1,\"%s\")\'' % (nSeconds,args.inputfile[0],args.outfile[0])
else:
    print 'Running with default output file name'
    cmdstring='root -b -q -l \'TimingAndRates.cc(%f,\"%s\")\'' % (nSeconds,args.inputfile[0])

os.system(cmdstring)
