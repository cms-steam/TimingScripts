#!/usr/bin/python


#script to make two csv trigger files compatible by adding the paths from one to the other and filling in dummy values

#import argparse and setup to read command line options
import argparse
#parser = argparse.ArgumentParser(description="A simple script to pad one hlt csv file with rows corresponding to paths not in that menu. Useful when comparing results from different menus. Usage: python padder.py --BigCSVFile csvBig --SmallCSVFile csvToPad")



#parser.add_argument("--BigCSVFile",type=str,help='The csv file with more hlt paths',required=True,nargs=1)
#parser.add_argument("--SmallCSVFile",type=str,help='The csv file with fewer hlt paths',required=True,nargs=1)

#args=parser.parse_args()

#print args.BigCSVFile[0]

filelist=['HLT_Paths_Total_Time_CMSSW732p3_pu40bx25.csv','HLT_Paths_Total_Time_CMSSW740p1_pu40bx25.csv','HLT_Paths_Total_Time_CMSSW742_pu40bx25.csv']

masterlist=[]

#make master list of paths
for file in filelist:
    f = open(file,'r')
    
    for line in f:
        path = line.split(",")[0]
        masterlist.append(path)

    f.close()

#prune the master list
prunedmasterlist=[]
for i in range(0, len(masterlist)):
    if not masterlist[i] in prunedmasterlist:
        prunedmasterlist.append(masterlist[i])

#sort the master list
prunedmasterlist.sort()

#now generate output files for each input file
paths732=[]
times732=[]
rates732=[]

file732 = open(filelist[0],'r')

for line in file732:
    paths732.append(line.split(",")[0])
    times732.append(line.split(",")[1])
    rates732.append(line.split(",")[2])
    print line

file732.close()

newtimes732=[]
newrates732=[]

for i in range(0,len(prunedmasterlist)):
    if prunedmasterlist[i] in paths732:
        iter = paths732.index(prunedmasterlist[i])
        newtimes732.append(float(times732[iter]))
        newrates732.append(float(rates732[iter]))
        print paths732[iter], times732[iter], rates732[iter]
    else:
        newtimes732.append(-999)
        newrates732.append(-999)

filename732 = (filelist[0].split("."))[0]+"_padded.csv"

outfile732 = open(filename732,'w')

for i in range(0,len(prunedmasterlist)):
    outfile732.write("%s,%.2f,%.2f\n" % (prunedmasterlist[i],newtimes732[i],newrates732[i]))

outfile732.close()

#now generate output files for each input file
paths740p1=[]
times740p1=[]
rates740p1=[]

file740p1 = open(filelist[1],'r')

for line in file740p1:
    paths740p1.append(line.split(",")[0])
    times740p1.append(line.split(",")[1])
    rates740p1.append(line.split(",")[2])

file740p1.close()

newtimes740p1=[]
newrates740p1=[]

for i in range(0,len(prunedmasterlist)):
    if prunedmasterlist[i] in paths740p1:
        newtimes740p1.append( float(times740p1[ paths740p1.index(prunedmasterlist[i]) ] ))
        newrates740p1.append( float(rates740p1[ paths740p1.index(prunedmasterlist[i]) ] ))
    else:
        newtimes740p1.append(-999)
        newrates740p1.append(-999)

filename740p1 = (filelist[1].split("."))[0]+"_padded.csv"

outfile740p1 = open(filename740p1,'w')

for i in range(0,len(prunedmasterlist)):
    outfile740p1.write("%s,%.2f,%.2f\n" % (prunedmasterlist[i],newtimes740p1[i],newrates740p1[i]))

outfile740p1.close()

#now generate output files for each input file
paths742=[]
times742=[]
rates742=[]

file742 = open(filelist[2],'r')

for line in file742:
    paths742.append(line.split(",")[0])
    times742.append(line.split(",")[1])
    rates742.append(line.split(",")[2])

file742.close()

newtimes742=[]
newrates742=[]

for i in range(0,len(prunedmasterlist)):
    if prunedmasterlist[i] in paths742:
        newtimes742.append(float(times742[ paths742.index(prunedmasterlist[i]) ]))
        newrates742.append(float(rates742[ paths742.index(prunedmasterlist[i]) ]))
    else:
        newtimes742.append(-999)
        newrates742.append(-999)

filename742 = (filelist[2].split("."))[0]+"_padded.csv"

outfile742 = open(filename742,'w')

for i in range(0,len(prunedmasterlist)):
    outfile742.write("%s,%.2f,%.2f\n" % (prunedmasterlist[i],newtimes742[i],newrates742[i]))

outfile742.close()
