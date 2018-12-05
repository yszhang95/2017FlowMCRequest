import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(5020.0),
    maxEventsToPrint = cms.untracked.int32(0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            operates_on_particles = cms.vint32(),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/D0_Kpi.dec'),
            list_forced_decays = cms.vstring('myB+','myB-','myD0', 'myanti-D0'),
      user_decay_embedded= cms.vstring(
"""
Alias        myB+                 B+
Alias        myB-                 B-
ChargeConj   myB-                 myB+
Decay myB+
    1.000           myanti-D0     pi+     PHSP;
Enddecay
CDecay myB-
End
"""
       )
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 0.', #min pthat
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

partonfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5) # 4 for c and 5 for b quark
	)

BDaufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(521),
    MomMinPt = cms.untracked.double(0.0),
    MomMinEta = cms.untracked.double(-10.),
    MomMaxEta = cms.untracked.double(10.),
    DaughterIDs = cms.untracked.vint32(211, -421),
    NumberDaughters = cms.untracked.int32(2),
    NumberDescendants = cms.untracked.int32(2),
    DaughterID = cms.untracked.int32(-421),
    DescendantsIDs = cms.untracked.vint32(-211, 321),
)

Brapidityfilter = cms.EDFilter("PythiaFilter",
      ParticleID = cms.untracked.int32(521),
                                 MinPt = cms.untracked.double(0.0),
                                                                 MaxPt = cms.untracked.double(1000.),
                                                                 MinRapidity = cms.untracked.double(-4.),
                                                                 MaxRapidity = cms.untracked.double(4.),
                                                                 )
ProductionFilterSequence = cms.Sequence(generator*partonfilter*BDaufilter*Brapidityfilter)
