#!/bin/bash

#This script will rename the output DQM files to have 
#more organized names

for i in $(seq 16 1 16)
do
  P1="2013/PU15/2xjobs_xcores/"
  P2="jobs"
  P3="/j"

  for j in $(seq 1 1 $i)
  do
    P=$P1$i$P2$P3$j
    LOC1="/tmp/clint/CMSSW_7_0_3/src/"
    LOC=$LOC1$P
    cd $LOC
    F1="DQM_Timing_"
    F2="j"
    F5="8c_j"
    F3="_wallclock_CR_local_2013_CMSSW703_PU15_trial2.root"
    F4="_trial1.root"
    F=$F1$i$F2$F5$j$F3
    FNEW=$F1$i$F2$j$F4
    cp DQM_V0001_R000207518__HLT__FastTimerService__All.root $F
    echo "This is the command I will run: cp DQM... $F and I'm in $P"
  done
done

