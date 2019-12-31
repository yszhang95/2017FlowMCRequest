import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(10),
        MinPt = cms.double(0),
        PartID = cms.vint32(1000010020),
        MaxEta = cms.double(3.2),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(0),
        MinPhi = cms.double(-3.14159265359) ## in radians

    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

    psethack = cms.string('single deuteron'),
    AddAntiParticle = cms.bool(True),
    firstRun = cms.untracked.uint32(1)
)
