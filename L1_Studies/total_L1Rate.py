#!/usr/bin/python

import os,math

f = open("L1_TotalRate_PHYS14_50ns_5e33.txt",'w')
os.system('cat Neutrino_Pt-2to20_gun_Phys14DR-AVE30BX50_tsg_PHYS14_ST_V1-v2/res/CMSSW_*.stdout | grep \"Total number of events processed:\" >> L1_TotalRate_PHYS14_50ns_5e33.txt')
f.close()


total=0
f = open("L1_TotalRate_PHYS14_50ns_5e33.txt",'r')
for line in f:
    total+=int(line[44:48])


##normalize output to rate assume 1254 bx for 50ns and 11246 zero bias events per bx gives 14102484 events per second, then 9997019/14102484 is 0.7088 so each event counts as 1/0.7088 Hz
rate = total/(0.7088)
rate=rate/1000.0
err = math.sqrt(total)/(1000.0*0.7088)
#outstring = '%s,%f,%f\n'%(path,rate,err)
#outfile.write(outstring)
f.close()

print "Rate for Entire L1 Menu: %f +/- %f" %(rate,err)

#outfile.close()
