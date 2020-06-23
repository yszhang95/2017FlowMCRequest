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
            # user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/D0_Kpi.dec'),
			user_decay_embedded = cms.vstring(
				# https://github.com/cms-data/GeneratorInterface-EvtGenInterface/blob/master/D0_Kpi.dec
				"""
Alias myD0      D0
Alias myanti-D0 anti-D0
ChargeConj myanti-D0 myD0
#
Decay myD0
1.000   pi- pi+  PHSP;
Enddecay
CDecay myanti-D0

End
				"""
			),
            list_forced_decays = cms.vstring('myD0', 'myanti-D0')
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

partonfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5) # 4 for c and 5 for b quark
	)

D0Daufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(421),
    MomMinPt = cms.untracked.double(1.2),
    MomMinEta = cms.untracked.double(-2.5),
    MomMaxEta = cms.untracked.double(2.5),
    DaughterIDs = cms.untracked.vint32(211, -211),
    NumberDaughters = cms.untracked.int32(2),
    NumberDescendants = cms.untracked.int32(0),
    BetaBoost = cms.untracked.double(0.434),
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter*D0Daufilter)
