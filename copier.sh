#!/bin/bash

for i in $(seq 1 1 50)
do
    file="hlt_50nsJuneFrozenMenu_Data_ResTest.py"
    newfile="hlt_50nsJuneFrozenMenu_Data_ResTest_job"$i".py"
#    cp $file $newfile
    sed="jobNumber"$i
#    mv $newfile $newfile.old
    echo Running sed "s:1jobs/j1:$sed" $newfile.old #> $newfile
#    sed "s:jobNumber1:$sed:" $newfile.old > $newfile
#    rm $newfile.old
    echo "Ran sed on $newfile"
done
