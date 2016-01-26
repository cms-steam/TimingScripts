#!/bin/bash


#########################################
#                                       #
#   A continuation of the xcores xjobs  #
#   scenarios                           #
#                                       #
#########################################

# 1 job 1 core
taskset -c 0 cmsRun hlt_2013_2p1v5_online_1j1c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/1jobs/j1/full.log;
wait $(jobs -p)

# 2 jobs 2 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_2j2c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/2jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_2j2c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/2jobs/j2/full.log;
wait $(jobs -p)

# 3 jobs 3 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_3j3c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/3jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_3j3c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/3jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_3j3c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/3jobs/j3/full.log;
wait $(jobs -p)

# 4 jobs 4 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_4j4c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/4jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_4j4c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/4jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_4j4c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/4jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_4j4c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/4jobs/j4/full.log;
wait $(jobs -p)

# 5 jobs 5 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_5j5c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/5jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_5j5c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/5jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_5j5c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/5jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_5j5c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/5jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_5j5c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/5jobs/j5/full.log;
wait $(jobs -p)

# 6 jobs 6 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_6j6c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/6jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_6j6c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/6jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_6j6c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/6jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_6j6c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/6jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_6j6c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/6jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_6j6c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/6jobs/j6/full.log;
wait $(jobs -p)

# 7 jobs 7 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_7j7c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/7jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_7j7c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/7jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_7j7c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/7jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_7j7c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/7jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_7j7c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/7jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_7j7c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/7jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_7j7c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/7jobs/j7/full.log;
wait $(jobs -p)

# 8 jobs 8 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_8j8c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_8j8c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_8j8c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_8j8c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_8j8c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_8j8c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_8j8c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_8j8c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/8jobs/j8/full.log;
wait $(jobs -p)

# 9 jobs 9 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_9j9c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_9j9c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_9j9c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_9j9c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_9j9c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_9j9c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_9j9c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_9j9c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_9j9c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/9jobs/j9/full.log;
wait $(jobs -p)

# 10 jobs 10 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_10j10c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_10j10c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_10j10c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_10j10c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_10j10c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_10j10c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_10j10c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_10j10c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_10j10c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_10j10c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/10jobs/j10/full.log;
wait $(jobs -p)

# 11 jobs 11 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_11j11c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_11j11c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_11j11c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_11j11c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_11j11c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_11j11c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_11j11c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_11j11c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_11j11c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_11j11c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_11j11c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/11jobs/j11/full.log;
wait $(jobs -p)

# 12 jobs 12 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_12j12c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_12j12c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_12j12c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_12j12c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_12j12c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_12j12c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_12j12c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_12j12c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_12j12c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_12j12c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_12j12c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_12j12c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/12jobs/j12/full.log;
wait $(jobs -p)

# 13 jobs 13 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_13j13c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_13j13c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_13j13c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_13j13c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_13j13c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_13j13c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_13j13c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_13j13c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_13j13c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_13j13c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_13j13c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_13j13c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_13j13c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/13jobs/j13/full.log;
wait $(jobs -p)

# 14 jobs 14 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_14j14c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_14j14c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_14j14c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_14j14c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_14j14c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_14j14c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_14j14c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_14j14c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_14j14c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_14j14c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_14j14c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_14j14c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_14j14c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_14j14c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/14jobs/j14/full.log;
wait $(jobs -p)

# 15 jobs 15 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_15j15c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_15j15c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_15j15c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_15j15c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_15j15c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_15j15c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_15j15c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_15j15c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_15j15c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_15j15c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_15j15c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_15j15c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_15j15c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_15j15c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_15j15c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/15jobs/j15/full.log;
wait $(jobs -p)

# 16 jobs 16 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j16c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j16c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j16c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j16c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j16c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j16c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j16c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j16c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j16c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j16c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j16c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j16c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j16c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j16c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j16c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j16c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# 17 jobs 17 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_17j17c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_17j17c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_17j17c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_17j17c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_17j17c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_17j17c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_17j17c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_17j17c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_17j17c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_17j17c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_17j17c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_17j17c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_17j17c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_17j17c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_17j17c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_17j17c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_17j17c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/17jobs/j17/full.log;
wait $(jobs -p)

# 18 jobs 18 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_18j18c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_18j18c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_18j18c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_18j18c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_18j18c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_18j18c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_18j18c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_18j18c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_18j18c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_18j18c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_18j18c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_18j18c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_18j18c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_18j18c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_18j18c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_18j18c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_18j18c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_18j18c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/18jobs/j18/full.log;
wait $(jobs -p)

# 19 jobs 19 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_19j19c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_19j19c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_19j19c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_19j19c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_19j19c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_19j19c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_19j19c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_19j19c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_19j19c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_19j19c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_19j19c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_19j19c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_19j19c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_19j19c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_19j19c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_19j19c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_19j19c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_19j19c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_19j19c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/19jobs/j19/full.log;
wait $(jobs -p)

# 20 jobs 20 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_20j20c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_20j20c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_20j20c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_20j20c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_20j20c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_20j20c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_20j20c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_20j20c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_20j20c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_20j20c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_20j20c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_20j20c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_20j20c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_20j20c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_20j20c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_20j20c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_20j20c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_20j20c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_20j20c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_20j20c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/20jobs/j20/full.log;
wait $(jobs -p)

# 21 jobs 21 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_21j21c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_21j21c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_21j21c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_21j21c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_21j21c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_21j21c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_21j21c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_21j21c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_21j21c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_21j21c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_21j21c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_21j21c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_21j21c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_21j21c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_21j21c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_21j21c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_21j21c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_21j21c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_21j21c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_21j21c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_21j21c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/21jobs/j21/full.log;
wait $(jobs -p)

# 22 jobs 22 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_22j22c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_22j22c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_22j22c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_22j22c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_22j22c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_22j22c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_22j22c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_22j22c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_22j22c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_22j22c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_22j22c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_22j22c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_22j22c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_22j22c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_22j22c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_22j22c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_22j22c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_22j22c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_22j22c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_22j22c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_22j22c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_22j22c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/22jobs/j22/full.log;
wait $(jobs -p)

# 23 jobs 23 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_23j23c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_23j23c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_23j23c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_23j23c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_23j23c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_23j23c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_23j23c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_23j23c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_23j23c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_23j23c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_23j23c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_23j23c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_23j23c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_23j23c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_23j23c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_23j23c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_23j23c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_23j23c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_23j23c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_23j23c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_23j23c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_23j23c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_23j23c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/23jobs/j23/full.log;
wait $(jobs -p)

# 24 jobs 24 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_24j24c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_24j24c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_24j24c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_24j24c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_24j24c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_24j24c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_24j24c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_24j24c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_24j24c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_24j24c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_24j24c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_24j24c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_24j24c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_24j24c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_24j24c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_24j24c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_24j24c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_24j24c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_24j24c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_24j24c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_24j24c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_24j24c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_24j24c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_24j24c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/24jobs/j24/full.log;
wait $(jobs -p)

# 25 jobs 25 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_25j25c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_25j25c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_25j25c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_25j25c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_25j25c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_25j25c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_25j25c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_25j25c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_25j25c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_25j25c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_25j25c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_25j25c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_25j25c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_25j25c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_25j25c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_25j25c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_25j25c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_25j25c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_25j25c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_25j25c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_25j25c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_25j25c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_25j25c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_25j25c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_25j25c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/25jobs/j25/full.log;
wait $(jobs -p)

# 26 jobs 26 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_26j26c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_26j26c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_26j26c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_26j26c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_26j26c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_26j26c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_26j26c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_26j26c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_26j26c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_26j26c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_26j26c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_26j26c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_26j26c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_26j26c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_26j26c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_26j26c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_26j26c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_26j26c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_26j26c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_26j26c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_26j26c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_26j26c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_26j26c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_26j26c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_26j26c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j25/full.log&
taskset -c 25 cmsRun hlt_2013_2p1v5_online_26j26c_j26_wallclock_CR_PU30.py >& 2013/xjobs_xcores/26jobs/j26/full.log;
wait $(jobs -p)

# 27 jobs 27 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_27j27c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_27j27c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_27j27c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_27j27c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_27j27c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_27j27c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_27j27c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_27j27c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_27j27c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_27j27c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_27j27c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_27j27c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_27j27c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_27j27c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_27j27c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_27j27c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_27j27c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_27j27c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_27j27c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_27j27c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_27j27c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_27j27c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_27j27c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_27j27c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_27j27c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j25/full.log&
taskset -c 25 cmsRun hlt_2013_2p1v5_online_27j27c_j26_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j26/full.log&
taskset -c 26 cmsRun hlt_2013_2p1v5_online_27j27c_j27_wallclock_CR_PU30.py >& 2013/xjobs_xcores/27jobs/j27/full.log;
wait $(jobs -p)

# 28 jobs 28 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_28j28c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_28j28c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_28j28c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_28j28c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_28j28c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_28j28c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_28j28c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_28j28c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_28j28c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_28j28c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_28j28c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_28j28c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_28j28c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_28j28c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_28j28c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_28j28c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_28j28c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_28j28c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_28j28c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_28j28c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_28j28c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_28j28c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_28j28c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_28j28c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_28j28c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j25/full.log&
taskset -c 25 cmsRun hlt_2013_2p1v5_online_28j28c_j26_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j26/full.log&
taskset -c 26 cmsRun hlt_2013_2p1v5_online_28j28c_j27_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j27/full.log&
taskset -c 27 cmsRun hlt_2013_2p1v5_online_28j28c_j28_wallclock_CR_PU30.py >& 2013/xjobs_xcores/28jobs/j28/full.log;
wait $(jobs -p)

# 29 jobs 29 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_29j29c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_29j29c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_29j29c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_29j29c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_29j29c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_29j29c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_29j29c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_29j29c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_29j29c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_29j29c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_29j29c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_29j29c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_29j29c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_29j29c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_29j29c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_29j29c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_29j29c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_29j29c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_29j29c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_29j29c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_29j29c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_29j29c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_29j29c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_29j29c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_29j29c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j25/full.log&
taskset -c 25 cmsRun hlt_2013_2p1v5_online_29j29c_j26_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j26/full.log&
taskset -c 26 cmsRun hlt_2013_2p1v5_online_29j29c_j27_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j27/full.log&
taskset -c 27 cmsRun hlt_2013_2p1v5_online_29j29c_j28_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j28/full.log&
taskset -c 28 cmsRun hlt_2013_2p1v5_online_29j29c_j29_wallclock_CR_PU30.py >& 2013/xjobs_xcores/29jobs/j29/full.log;
wait $(jobs -p)

# 30 jobs 30 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_30j30c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_30j30c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_30j30c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_30j30c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_30j30c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_30j30c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_30j30c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_30j30c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_30j30c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_30j30c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_30j30c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_30j30c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_30j30c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_30j30c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_30j30c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_30j30c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_30j30c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_30j30c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_30j30c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_30j30c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_30j30c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_30j30c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_30j30c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_30j30c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_30j30c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j25/full.log&
taskset -c 25 cmsRun hlt_2013_2p1v5_online_30j30c_j26_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j26/full.log&
taskset -c 26 cmsRun hlt_2013_2p1v5_online_30j30c_j27_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j27/full.log&
taskset -c 27 cmsRun hlt_2013_2p1v5_online_30j30c_j28_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j28/full.log&
taskset -c 28 cmsRun hlt_2013_2p1v5_online_30j30c_j29_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j29/full.log&
taskset -c 29 cmsRun hlt_2013_2p1v5_online_30j30c_j30_wallclock_CR_PU30.py >& 2013/xjobs_xcores/30jobs/j30/full.log;
wait $(jobs -p)

# 31 jobs 31 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_31j31c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_31j31c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_31j31c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_31j31c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_31j31c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_31j31c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_31j31c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_31j31c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_31j31c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_31j31c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_31j31c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_31j31c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_31j31c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_31j31c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_31j31c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_31j31c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_31j31c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_31j31c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_31j31c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_31j31c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_31j31c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_31j31c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_31j31c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_31j31c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_31j31c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j25/full.log&
taskset -c 25 cmsRun hlt_2013_2p1v5_online_31j31c_j26_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j26/full.log&
taskset -c 26 cmsRun hlt_2013_2p1v5_online_31j31c_j27_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j27/full.log&
taskset -c 27 cmsRun hlt_2013_2p1v5_online_31j31c_j28_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j28/full.log&
taskset -c 28 cmsRun hlt_2013_2p1v5_online_31j31c_j29_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j29/full.log&
taskset -c 29 cmsRun hlt_2013_2p1v5_online_31j31c_j30_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j30/full.log&
taskset -c 30 cmsRun hlt_2013_2p1v5_online_31j31c_j31_wallclock_CR_PU30.py >& 2013/xjobs_xcores/31jobs/j31/full.log;
wait $(jobs -p)

# 32 jobs 32 cores
taskset -c 0 cmsRun hlt_2013_2p1v5_online_32j32c_j1_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_32j32c_j2_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_32j32c_j3_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_32j32c_j4_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_32j32c_j5_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_32j32c_j6_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_32j32c_j7_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_32j32c_j8_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_32j32c_j9_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_32j32c_j10_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_32j32c_j11_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_32j32c_j12_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_32j32c_j13_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_32j32c_j14_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_32j32c_j15_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_32j32c_j16_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j16/full.log&
taskset -c 16 cmsRun hlt_2013_2p1v5_online_32j32c_j17_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j17/full.log&
taskset -c 17 cmsRun hlt_2013_2p1v5_online_32j32c_j18_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j18/full.log&
taskset -c 18 cmsRun hlt_2013_2p1v5_online_32j32c_j19_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j19/full.log&
taskset -c 19 cmsRun hlt_2013_2p1v5_online_32j32c_j20_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j20/full.log&
taskset -c 20 cmsRun hlt_2013_2p1v5_online_32j32c_j21_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j21/full.log&
taskset -c 21 cmsRun hlt_2013_2p1v5_online_32j32c_j22_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j22/full.log&
taskset -c 22 cmsRun hlt_2013_2p1v5_online_32j32c_j23_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j23/full.log&
taskset -c 23 cmsRun hlt_2013_2p1v5_online_32j32c_j24_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j24/full.log&
taskset -c 24 cmsRun hlt_2013_2p1v5_online_32j32c_j25_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j25/full.log&
taskset -c 25 cmsRun hlt_2013_2p1v5_online_32j32c_j26_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j26/full.log&
taskset -c 26 cmsRun hlt_2013_2p1v5_online_32j32c_j27_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j27/full.log&
taskset -c 27 cmsRun hlt_2013_2p1v5_online_32j32c_j28_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j28/full.log&
taskset -c 28 cmsRun hlt_2013_2p1v5_online_32j32c_j29_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j29/full.log&
taskset -c 29 cmsRun hlt_2013_2p1v5_online_32j32c_j30_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j30/full.log&
taskset -c 30 cmsRun hlt_2013_2p1v5_online_32j32c_j31_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j31/full.log&
taskset -c 31 cmsRun hlt_2013_2p1v5_online_32j32c_j32_wallclock_CR_PU30.py >& 2013/xjobs_xcores/32jobs/j32/full.log;
wait $(jobs -p)
