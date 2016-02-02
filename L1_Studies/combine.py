#!/usr/bin/python

import os

def writeheader(file):
    file.write("""import FWCore.ParameterSet.Config as cms

process= cms.Process("TEST")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.load('FWCore/MessageService/MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append('L1GtTrigReport')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(\n""")

def writeinputs(file,index):
    start=index*250
    if index<3:
        end=(index+1)*250-1
    else:
        end=808
    print start,end
    for j in range(start,end+1):
        input="\"file:/eos/uscms/store/user/clint/L1Skim/Neutrino_Pt-2to20_gun_Phys14DR-AVE30BX50_tsg_PHYS14_ST_V1-v2/"+files[j]+"\",\n"
        file.write(input)
        
def writecloser(file,index):
    file.write(""")
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *',
                                           ),
                               """)
    output="          fileName = cms.untracked.string(\"/eos/uscms/store/user/lpctlbsm/clint/L1Skim/Neutrino_Pt2-20_gun_PU30bx50_L1_2015_50nsCollisionsMenu/Neutrino_Pt-2to20_gun_PU30bx50_L1_2015_50nsCollisionsMenu_part%i.root\"" % index
    file.write(output)
    file.write(""")
)
process.o = cms.EndPath( process.out )
""")

def makefile(index):
    filename="combine_pt%i_cfg.py" % i
    file = open(filename,"w+")
    writeheader(file)
    writeinputs(file,index)
    writecloser(file,index)
    file.close()


files = os.listdir("/eos/uscms/store/user/clint/L1Skim/Neutrino_Pt-2to20_gun_Phys14DR-AVE30BX50_tsg_PHYS14_ST_V1-v2/")
count=0

for file in files:
    count+=1
numjobs = count/250 +1
print numjobs

for i in range(0,numjobs):
    makefile(i)
#    print i
