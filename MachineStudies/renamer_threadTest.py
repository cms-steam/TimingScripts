#!/usr/bin/python


import sys, os
sys.path.append('../Classes/')
from test import *

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--testSaveFile", type = str, help='The save file for the test. Used to configure the script.',required=True,nargs=1)
parser.add_argument("--run", type = int, help='the run used for the test, needed to get dqm file. should be 1 for MC',required=True,nargs=1)
args=parser.parse_args()

tfile = args.testSaveFile[0]
run = args.run[0]

mt = readMultiTest(tfile)

cwd = os.getcwd()
for t in mt.tests:
    for i in range(1,t.trials+1):
        basedir=cwd+'/'+mt.name+'/trial%i/%ijobs' % (i,t.nthreads)
 #       print 'python renamer.py --basedir %s --njobs %i --ncores %i --trial %i --options %s --nthreads %i --run %i' % (basedir,t.njobs,t.ncores,i,t.name,t.nthreads,run)
        os.system('python renamer.py --basedir %s --njobs %i --ncores %i --trial %i --options %s --nthreads %i --run %i' % (basedir,t.njobs,t.ncores,i,t.name,t.nthreads,run))
