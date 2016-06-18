import FWCore.ParameterSet.Config as cms

process = cms.Process("CMA")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring( 
        'root://eoscms.cern.ch//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/239/785/00000/08A1DDD5-5CDD-E411-8707-02163E0124F6.root',
        ),
                            lumisToProcess = cms.untracked.VLuminosityBlockRange('239785:1800-239785:2000'),
                            skipEvents = cms.untracked.uint32(0),
                            dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
                            inputCommands=cms.untracked.vstring(
        "drop *",
        "keep *_TriggerResults_*_HLT",
        "keep *_hltGtStage2ObjectMap_*_*",
        "keep *_hltTriggerSummaryAOD_*_HLT",
        "keep *_rawDataCollector_*_*"
        )
                            );

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('Commissioning2015_Run239785_CirculatingBeam.root'),
                               outputCommands = cms.untracked.vstring(
        "drop *",
        "keep *_TriggerResults_*_HLT",
        "keep *_hltGtStage2ObjectMap_*_*",
        "keep *_hltTriggerSummaryAOD_*_HLT",
        "keep *_rawDataCollector_*_*",
));

process.myEndPath = cms.EndPath(process.out)
        
