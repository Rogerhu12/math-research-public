#!/usr/bin/env python3
"""Publication-only recovery of actual completed run43664532571; no mathematical executable."""
import hashlib,json,os
from pathlib import Path
RULES={'README.md':'8fec34716cd4464b55ef546022bd4eb06ea8f50b2040f4025b7383d043db99f2','topics/invariant-subspace-problem/README.md':'40a65616e7a2cdcdc9916585c048b3f66547e71f0627b4abf58e5d3487ce1929'}
base=Path(os.environ['RUNNER_TEMP'])/'isp-r150-third-publication-recovery'
results=base/'results'
source=json.loads((results/'actions-source.json').read_text())
outcome=json.loads((results/'actions-outcome.json').read_text())
receipt=json.loads((results/'saturated-third-page-pipeline-receipt.json').read_text())
assert source['source_commit']=='39c27f127fa63240629ecb60fe8e13628fee631f'
assert str(source['run_id'])=='43664532571' and str(source['run_attempt'])=='1'
assert source['rules_sha256']==RULES
assert {p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in RULES}==RULES
assert outcome['complete'] is True and receipt['status']=='completed'
assert receipt['outcome']=='third-page-all-local-compatible-global-continuation-required'
assert receipt['thirdImageRank']==2 and receipt['individualTargetCompatible']==[True]*9
assert receipt['thirdSourceCount']==208 and receipt['recoveryFiles']==197 and receipt['recoveryBytes']==440770011
assert receipt['globalAllOriginalSourceMod31SixObstructionVerified'] is False
assert receipt['fullOriginalAllNineMod887503681IdentityVerified'] is False
manifest=json.loads((results/'recovery-manifest.json').read_text())
assert len(manifest['files'])==197 and sum(x['bytes'] for x in manifest['files'])==440770011
print(json.dumps({'status':'ready-to-publish-actual-completed-data','originalRun':43664532571,'thirdImageRank':2,'allNineLocalCompatible':True,'originalMod31SixIdentityAsserted':False,'mathematicsRerun':False,'recoveryFiles':197,'recoveryBytes':440770011}),flush=True)
