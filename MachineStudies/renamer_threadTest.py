#!/usr/bin/python


import sys, os
sys.path.append('../Classes/')
from test import *

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--testSaveFile", type = str, help='The save file for the test. Used to configure the script.',required=True,nargs=1)

args=parser.parse_args()

tfile = args.testSaveFile[0]

mt = readMultiTest(tfile)


for t in mt.tests:
    for i in range(1,t.trials+1):
        print t.name
 #       os.system('python renamer.py --basedir %s --njobs %i --ncores %i --trial %i --options %s --nthreads %i' % (basedir,t.njobs,t.ncores,i,t.name,t.nthreads))
