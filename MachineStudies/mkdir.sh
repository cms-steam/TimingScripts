#!/bin/bash

BASE="/tmp/clint/CMSSW_7_0_3/src/2013"

for i in $(seq 16 1 16)
do
    topdir=$i"jobs"
    cd $BASE
    mkdir $1
    cd $1
    mkdir xjobs_xcores
    cd xjobs_xcores
    mkdir $topdir
    cd $topdir
    for j in $(seq 1 1 $i)
    do
	botdir="j"$j
	mkdir $botdir
    done
done