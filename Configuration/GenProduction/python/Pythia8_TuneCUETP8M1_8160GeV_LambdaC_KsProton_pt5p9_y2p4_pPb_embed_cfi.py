import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8160.0),
    maxEventsToPrint = cms.untracked.int32(0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            operates_on_particles = cms.vint32(),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/LambdaC_KsProton.dec'),
            list_forced_decays = cms.vstring('myLambdaC', 'myanti-LambdaC')
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(     
            'HardQCD:all = on',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

LambdaCDaufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(4122),
    MomMinPt = cms.untracked.double(0.),
    MomMinEta = cms.untracked.double(-10),
    MomMaxEta = cms.untracked.double(10),
    DaughterIDs = cms.untracked.vint32(310, 2212),
    NumberDaughters = cms.untracked.int32(2),
    NumberDescendants = cms.untracked.int32(0),
)

LambdaCrapidityPtfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(4122),
                                MinPt = cms.untracked.double(5.9),
                                MaxPt = cms.untracked.double(99999.),
                                MinRapidity = cms.untracked.double(-2.9),
                                MaxRapidity = cms.untracked.double(2.0),
                                )


ProductionFilterSequence = cms.Sequence(generator*LambdaCDaufilter*LambdaCrapidityPtfilter)
