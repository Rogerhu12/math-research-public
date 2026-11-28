import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,numpy as np,sys,importlib.util,time
from pathlib import Path
W=Path(__file__).parent;S=Path('/workspace/scratch/2ecfcd6930d6/math-research-public/topics/visible-flexible-closed-surface/scripts')
def load(p,name):
 q=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(q);sys.modules[name]=m;q.loader.exec_module(m);return m
m=load(S/'6a65-geometry-nonfold-polar-background-v2.py','prim_bg');ref=load(W/'2ecf-polar-tight-source-evaluator.py','prim_ref')
with m.NonfoldPolarBackground(S,S.parent/'notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json',W/'target-zero.json',W/'gap105-prefix-ramp-master.npz',W/'gap105-prefix-coast-master.npz') as src:
 base=sys.modules['nonfold_fixed_weighted_formula'].base
 q,receipt=ref.audit_row(src,.856679790800223,2*np.pi*np.arange(128)/128,base)
 np.save(W/'polar-G10-primitive-audit-jets.npy',q['jets'])
receipt['sourceExit']=src.exit_receipt
(W/'polar-G10-primitive-audit.json').write_text(json.dumps(receipt,separators=(',',':'),allow_nan=False)+'\n')
print(json.dumps(dict(event='actual_primitive_audit_passed',maxResidual=max(x['independentPrimitiveResidual'] for c in receipt['strongerPrimitiveChecks'] for x in c['rootChecks']))),flush=True)
