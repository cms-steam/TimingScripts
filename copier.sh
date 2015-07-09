#!/bin/bash

for i in $(seq 1 1 32)
do
    file="hlt_.py"
 
#    cp $file $newfile
    sed="jobNumber"$i
#    mv $newfile $newfile.old
    echo Running sed "s:1jobs/j1:$sed" $newfile.old #> $newfile
#    sed "s:jobNumber1:$sed:" $newfile.old > $newfile
#    rm $newfile.old
    echo "Ran sed on $newfile"
done
