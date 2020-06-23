# Descriptions

Commands for MC D0toKK and D0toPiPi productions in PbPb collisions at 5.02 TeV with 2018 run conditions.

```
# I removed "--nThreads 2".
# GEN-SIM
cmsDriver.py Configuration/GenProduction/python/Pythia8_TuneCP5_5TeV_D0_PiPi_prompt_pt1p2_y2p4_cfi.py \
--fileout file:Pythia8_TuneCP5_5TeV_D0_PiPi_prompt_pt1p2_y2p4.root \
--pileup_input "dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM" \
--mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 103X_upgrade2018_realistic_HI_v11 \
--beamspot MatchHI --step GEN,SIM \ 
--scenario HeavyIons --geometry DB:Extended --era Run2_2018_pp_on_AA \
--python_filename Pythia8_TuneCP5_5TeV_D0_PiPi_prompt_pt1p2_y2p4_cfg.py --no_exec -n 1000

cmsDriver.py Configuration/GenProduction/python/Pythia8_TuneCP5_5TeV_D0_KK_prompt_pt1p2_y2p4_cfi.py \
--fileout file:Pythia8_TuneCP5_5TeV_D0_KK_prompt_pt1p2_y2p4.root \
--pileup_input "dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM" \
--mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 103X_upgrade2018_realistic_HI_v11 \
--beamspot MatchHI --step GEN,SIM \
--scenario HeavyIons --geometry DB:Extended --era Run2_2018_pp_on_AA \
--python_filename Pythia8_TuneCP5_5TeV_D0_KK_prompt_pt1p2_y2p4_cfg.py --no_exec -n 1000

cmsDriver.py Configuration/GenProduction/python/Pythia8_TuneCP5_5TeV_D0_PiPi_nonprompt_pt1p2_y2p4_cfi.py \
--fileout file:Pythia8_TuneCP5_5TeV_D0_PiPi_nonprompt_pt1p2_y2p4.root \
--pileup_input "dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM" \
--mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 103X_upgrade2018_realistic_HI_v11 \
--beamspot MatchHI --step GEN,SIM \
--scenario HeavyIons --geometry DB:Extended --era Run2_2018_pp_on_AA \
--python_filename Pythia8_TuneCP5_5TeV_D0_PiPi_nonprompt_pt1p2_y2p4_cfg.py --no_exec -n 1000

cmsDriver.py Configuration/GenProduction/python/Pythia8_TuneCP5_5TeV_D0_KK_nonprompt_pt1p2_y2p4_cfi.py \
--fileout file:Pythia8_TuneCP5_5TeV_D0_KK_nonprompt_pt1p2_y2p4.root \
--pileup_input "dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM" \
--mc --eventcontent RAWSIM --pileup HiMixGEN --datatier GEN-SIM --conditions 103X_upgrade2018_realistic_HI_v11 \
--beamspot MatchHI --step GEN,SIM \
--scenario HeavyIons --geometry DB:Extended --era Run2_2018_pp_on_AA \
--python_filename Pythia8_TuneCP5_5TeV_D0_KK_nonprompt_pt1p2_y2p4_cfg.py --no_exec -n 1000
```
