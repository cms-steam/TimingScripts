#!/usr/env/python

import os
from ROOT import *

runs = [278175] 
#runs = [275125,275124,275074,275073,275068,275067,275066,275059,275001,275000,274999,274998,274956,274958,274959,274968,274969,274971,274443,274442,274441,274440,274422,274421,274420,274388,274387,274345,274344,274338,274335,274319,274316,274315,274314,274286,274284,274282,275282,275283,275284,275286,275290,275291,275292,275293,275309,275310,275311,275319,275326,275337,275338,275344,275345,275370,275371,275375,275376,275657,275658,275659,275757,275768,275772,275774,275776,275777,275778,275782,275783,275828,275832,275833,275834,275836,275837,275847,275886,275887,275890,275911,275912,275913,275918,275920,275923,275931,275963,276092,276097,276242,276243,276244,276282,276283,276282,276283,276315,276317,276318,276327,276352,276355,276357,276361,276363,276384,276437,276453,276454,276455,276456,276458,276495,276501,276502,276525,276527,276528,276542,276544,276544,276545,276581,276582,276585,276586,276587,276653,276655,276659,276775,276776,276794,276807,276808,276810,276811,276831,276834,276870,276935,277069,277070,277071,277072,277076,277087,277094,277127,277148,277166,277168,277194,277202,277220,277305,277420,277935,277981,277982,277992,278017,278018,278167,278175,278193,278239,278240,278308,278310,278315,278345,278349,278366,278406,278509,278769,278770,278803,278805,278808,278820,278822,278873,278874,278875,278923,278962,278963,278969,278975,278986]


#for run in runs:
#    f = open("json_%i.txt" %run,"w")
#    f.write("{\"%i\":[[]]}\n")
#    f.close

#make needed directory structure

if not os.path.isdir("./event_rootFiles"):
    os.system("mkdir event_rootFiles")
if not os.path.isdir("./timeByLs_rootFiles"):
    os.system("mkdir timeByLs_rootFiles")
if not os.path.isdir("./throughput_rootFiles"):
    os.system("mkdir throughput_rootFiles")
if not os.path.isdir("./lumi_rootFiles"):
    os.system("mkdir lumi_rootFiles")


for run in runs:
    os.chdir('event_rootFiles')
    command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/HLT/TimerService/*/event\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    os.system(command)
    #cd to timing by ls
    os.chdir('../timeByLs_rootFiles')
    command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/HLT/TimerService/*/event_byls\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    os.system(command)
    #cd to lumi directory
    os.chdir('../lumi_rootFiles')
    if run < 281663:
        command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/Scal/LumiScalers/Instant_Lumi\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    else:
        command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/HLT/LumiMonitoring/lumiVsLS\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    os.system(command)
    #throughput
    os.chdir('../throughput_rootFiles')
    command ="python ../dqm-acces.py -s https://cmsweb.cern.ch/dqm/online/data/json -f \"/HLT/Throughput/throughput_retired\" -e \"run == %i and match(\'/Global/Online/ALL\', dataset)\" -r -w" % run
    os.system(command)
    os.chdir('..')
