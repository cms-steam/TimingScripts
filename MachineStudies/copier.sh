#!/bin/bash

for i in $(seq 1 1 32)
do
    for j in $(seq 1 1 $i)
    do
	file="hlt_2013_TEMPLATE.py"
	f1="hlt_2013_2p1v5_online_"
	f2="j"
	f3="c_j"
	if [ $i -eq '4' ]
	then
	    n=2
	elif [ $i -eq '6' ]
	then
	    n=3
	elif [ $i -eq '8' ]
	then
	    n=4
	elif [ $i -eq '10' ]
	then
	    n=5
	elif [ $i -eq '12' ]
	then
	    n=6
	elif [ $i -eq '14' ]
	then
	    n=7
	elif [ $i -eq '16' ]
	then
	    n=8
	fi
	f4="_wallclock_CR_PU30.py"
	newfile=$f1$i$f2$i$f3$j$f4
	cp $file $newfile
	sed1="xjobs_xcores/"
	sed2="jobs/j"
	sed=$sed1$i$sed2$j
	mv $newfile $newfile.old
#	echo Running sed "s:1jobs/j1:$sed" $newfile.old #> $newfile
	sed "s:xjobs_xcores/1jobs/j1:$sed:" $newfile.old > $newfile
	rm $newfile.old
#	echo "Ran sed on $newfile"
    done
done