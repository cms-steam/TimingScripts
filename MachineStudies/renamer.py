#/usr/bin/python

#setup argparser and os
import argparse, os

#add arguments
parser = argparse.ArgumentParser()

parser.add_argument("--basedir", type=str, help='The base directory from which to look for individual directories default is current directory',required=False,nargs=1,default='.')
parser.add_argument("--njobs", type=int, help='The number of total jobs',required=True, nargs=1)
parser.add_argument("--ncores",type=int, help='The number of cores for the job',required=True,nargs=1)
parser.add_argument("--trial",type=int,help='The trial for this test, no default value to avoid accidental overwrite',required=True,nargs=1)
parser.add_argument("--options",type=str,help='The extra info for naming the files based on the conditions of the test (eg. cmssw, pu, etc)',required=False)
parser.add_argument("--nthreads", type=int, help='The number of total threads',required=True, nargs=1)
parser.add_argument("--run",type=int,help='Run number of input data. Should be 1 for MC.',required=True,nargs=1)
#parse the arguments
args=parser.parse_args()

#setup and change to base directory
basedir=args.basedir[0]
#save current directory
home = os.getcwd()
#make output directory
output=home+"/renamer_output/"
os.system('mkdir -p %s' % output)
os.chdir(basedir)
print 'now working in',os.getcwd()

#get the naming conventions
nameOpts=args.options

names = nameOpts.split(",")
for i in range(0,len(names)):
    print names[i]

#get other arguments
njobs = args.njobs[0]
ncores = args.ncores[0]
nthreads = args.nthreads[0]
run = args.run[0]

#loop to copy and rename files
for i in range(1,njobs+1):
    newname = output+'DQM_Timing_%ij%ic_%ithreads_j%i_trial%i' % (njobs,ncores,nthreads,i,args.trial[0])
    for j in range(0,len(names)):
        newname += "_%s" % names[j]
    newname+='.root'

    #copy the file
    oldname = './j%i/DQM_V0001_R000%i__HLT__FastTimerService__All.root' % (i,run)
    copy = 'cp %s %s' % (oldname,newname)
    print copy
    os.system(copy)
