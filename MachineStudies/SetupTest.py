#!/usr/bin/python

from test import test

name = raw_input("enter a name for the test to run, this name will be used for saving test attributes, output directories, etc so choose one that makes sense: ")

nj = raw_input("How many jobs would you like to run for this test?")
nc = raw_input("How many cores would you like those jobs to run on?")
nt = raw_input("How many threads per job would you like?")
trials = raw_input("How many trials of this test would you like to run?")
menu = raw_input("What is the base hlt menu you would like to use for the test (enter filename)?")

currentTest = test(nj,nc,nt,name,menu,trials)
