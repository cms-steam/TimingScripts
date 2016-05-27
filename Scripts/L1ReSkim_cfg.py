import FWCore.ParameterSet.Config as cms

process = cms.Process("L1RESKIM")

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring( 
        'root://eoscms.cern.ch//eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/239/785/00000/08A1DDD5-5CDD-E411-8707-02163E0124F6.root',
        ),
                            skipEvents = cms.untracked.uint32(0),
                            inputCommands=cms.untracked.vstring(
        "drop *",
        "keep *_TriggerResults_*_HLT",
        "keep *_hltGtStage2ObjectMap_*_*",
        "keep *_hltTriggerSummaryAOD_*_HLT",
        "keep *_rawDataCollector_*_*"
        )
                            )


process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('Commissioning2015_Run239785_CirculatingBeam.root'),
                               SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'L1Skim' ) )
                               outputCommands = cms.untracked.vstring(
        "drop *",
        "keep *_TriggerResults_*_HLT",
        "keep *_hltGtStage2ObjectMap_*_*",
        "keep *_hltTriggerSummaryAOD_*_HLT",
        "keep *_rawDataCollector_*_*"
))

process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)

process.L1ReSkim = cms.EDFilter("L1TGlobalPrescaler",
                                l1tresults = cms.InputTag("hltGtStage2Digis"),
                                l1tprescales = cms.vdouble(1.,1.,1.),
)

process.L1Skim = cms.Path( process.hltGtStage2Digis + process.L1ReSkim)

#endprocess stuff- don't really know what it does
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWoutput_step = cms.EndPath(process.out)

# Schedule definition
process.schedule = cms.Schedule(process.L1Skim,process.endjob_step,process.RAWoutput_step)
