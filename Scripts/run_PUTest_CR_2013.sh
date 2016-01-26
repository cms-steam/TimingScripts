#!/bin/bash


#########################################
#                                       #
#   A continuation of the xcores xjobs  #
#   scenarios                           #
#                                       #
#########################################

# PU15
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU15.py >& 2013/PU15/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# PU20
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU20.py >& 2013/PU20/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# PU25
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU25.py >& 2013/PU25/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# PU30
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU30.py >& 2013/PU30/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# PU33
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU33.py >& 2013/PU33/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# PU44
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU44.py >& 2013/PU44/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# PU57
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU57.py >& 2013/PU57/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)

# PU63
taskset -c 0 cmsRun hlt_2013_2p1v5_online_16j8c_j1_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j1/full.log&
taskset -c 1 cmsRun hlt_2013_2p1v5_online_16j8c_j2_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j2/full.log&
taskset -c 2 cmsRun hlt_2013_2p1v5_online_16j8c_j3_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j3/full.log&
taskset -c 3 cmsRun hlt_2013_2p1v5_online_16j8c_j4_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j4/full.log&
taskset -c 4 cmsRun hlt_2013_2p1v5_online_16j8c_j5_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j5/full.log&
taskset -c 5 cmsRun hlt_2013_2p1v5_online_16j8c_j6_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j6/full.log&
taskset -c 6 cmsRun hlt_2013_2p1v5_online_16j8c_j7_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j7/full.log&
taskset -c 7 cmsRun hlt_2013_2p1v5_online_16j8c_j8_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j8/full.log&
taskset -c 8 cmsRun hlt_2013_2p1v5_online_16j8c_j9_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j9/full.log&
taskset -c 9 cmsRun hlt_2013_2p1v5_online_16j8c_j10_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j10/full.log&
taskset -c 10 cmsRun hlt_2013_2p1v5_online_16j8c_j11_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j11/full.log&
taskset -c 11 cmsRun hlt_2013_2p1v5_online_16j8c_j12_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j12/full.log&
taskset -c 12 cmsRun hlt_2013_2p1v5_online_16j8c_j13_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j13/full.log&
taskset -c 13 cmsRun hlt_2013_2p1v5_online_16j8c_j14_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j14/full.log&
taskset -c 14 cmsRun hlt_2013_2p1v5_online_16j8c_j15_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j15/full.log&
taskset -c 15 cmsRun hlt_2013_2p1v5_online_16j8c_j16_wallclock_CR_PU63.py >& 2013/PU63/xjobs_xcores/16jobs/j16/full.log;
wait $(jobs -p)
