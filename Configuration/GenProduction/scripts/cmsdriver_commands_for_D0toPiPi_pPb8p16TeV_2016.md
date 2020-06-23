# An example
This file shows how to generate MC samples for D0->PiPi in pPb collisions at 8.16 TeV with `cmsDriver`. Parameters can be found on McM.

```
# For GEN-SIM:
cmsDriver.py Configuration/GenProduction/python/Pythia8_TuneCUETP8M1_8160GeV_D0_PiPi_prompt_pt1p2_y2p4_pPb_embed_cfi.py \
--python_filename Pythia8_TuneCUETP8M1_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_embed_cfg.py --mc --pileup HiMixGEN \
--pileup_input "dbs:/ReggeGribovPartonMC_EposLHC_pPb_4080_4080_DataBS/pPb816Spring16GS-MB_80X_mcRun2_pA_v4-v2/GEN-SIM" \
--pileup_dasoption "--limit 0" --eventcontent RAWSIM --customise Configuration/StandardSequences/SimWithCastor_cff.py \
--datatier GEN-SIM --conditions 80X_mcRun2_pA_v4 --beamspot MatchPbPBoost --step GEN,SIM \
--scenario HeavyIons --era Run2_2016_pA --number=100 --fileout=Pythia8_TuneCUETP8M1_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_embed.root --no_exec

# For DIGI:
cmsDriver.py --python_filename Pythia8_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_embed_digi_cfg.py\
--filein=file:Pythia8_TuneCUETP8M1_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_embed.root \
--fileout=Pythia8_EmbedEPOS_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_DIGI.root \
--mc --pileup HiMix  \
--pileup_input "dbs:/ReggeGribovPartonMC_EposLHC_pPb_4080_4080_DataBS/pPb816Spring16GS-MB_80X_mcRun2_pA_v4-v2/GEN-SIM" \
--pileup_dasoption "--limit 0" --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 80X_mcRun2_pA_v4 \
--step DIGI,L1,DIGI2RAW,HLT:PIon --era Run2_2016_pA  --customise Configuration/DataProcessing/Utils.addMonitoring \
--number=100  --no_exec

# For RECONSTRUCTION:
cmsDriver.py --python_filename Pythia8_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_embed_reco_cfg.py \
--filein=file:Pythia8_EmbedEPOS_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_DIGI.root  \
--fileout=Pythia8_EmbedEPOS_8p16TeV_PromptD0_PiPi_pt1p2_y2p4_pPb_RECO.root \
--mc --eventcontent AODSIM --datatier GEN-SIM-RECO --conditions 80X_mcRun2_pA_v4 --step RAW2DIGI,L1Reco,RECO \
--era Run2_2016_pA  \
--customise_commands \
"process.bunchSpacingProducer.bunchSpacingOverride=cms.uint32(25)\nprocess.bunchSpacingProducer.overrideBunchSpacing=cms.bool(True)" \
--number=100 --no_exec
```
