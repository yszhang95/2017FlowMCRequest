# 2017FlowMCRequest
This is a repo for configs for MC sample requests.
# Usage
`cmsdriver` cannot find pythons if one put `2017FlowMCRequest` under `${CMSSW_BASE}/src`. 
That is because `CMSSW` will not try to search pythons under `${CMSSW_BASE}/src/path/to/target/python`.
It will cease searching on the level `${CMSSW_BASE}/src/path/to/python`.
It is better to clone the repo outside `${CMSSW_BASE}`.

```
git clone https://github.com/davidlw/2017FlowMCRequest.git
mv 2017FlowMCRequest/Configuration 2017FlowMCRequest/GeneratorInterface ${CMSSW_BASE}/src
scram b
```

Examples of `cmsdriver` usage can be found in `Configuration/GenProduction/scripts`. Parameters for `cmsdriver` can be found on [McM](https://cms-pdmv.cern.ch/mcm/).
