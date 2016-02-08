#!/usr/bin/python


'''types of tests are:

1) CPU Scan, starts with 1 job and fills the machine 1 job at a time - can be configured with different ratios of jobs to threads, multithreading, hyperthreading, etc

2) Occupancy Scan, an abbreviated version of above, which does only a few selected points.

3) Thread Scan, starts with one job and 1 one thread, then increases number of threads for that job until full cpu is reached.

'''
#define dictionary for types of scans
types = {'1':'CPU-Scan','2':'Occ-Scan','3':'Thread-Scan'}
#define dicionary for architectures the script will know how to handle
archs = {'1':'SandyBridge','2':'IvyBridge','3':'Haswell','4':'Broadwell'}
