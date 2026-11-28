import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,argparse,numpy as np,time,importlib.util,hashlib
from pathlib import Path
W=Path(__file__).parent;S=Path('/workspace/scratch/2ecfcd6930d6/math-research-public/topics/visible-flexible-closed-surface/scripts')
def load(p,name):
 q=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(q);sys.modules[name]=m;q.loader.exec_module(m);return m
prep=load(W/'2ecf-polar-c2-g10-prepare.py','consistent_prep');ref=load(W/'2ecf-polar-refined-arc-source-evaluator.py','consistent_ref')
a=argparse.Namespace(scripts=S,parent_entry=W/'2ecf-polar-c2-prefix-prepare.py',parent_prepared=W/'polar-c2-extended-prepared.json',third_observer=W/'polar-independent-G3-shifted256-independent.json')
saved,definition,basis,caches,mods,obs=prep.load_parent(a);_,added,_,_=prep.dense_grid(caches['observer'].nodes,basis,obs);s=float(added[502]);start=time.monotonic()
with mods['background'].NonfoldPolarBackground(S,S.parent/'notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json',W/'target-zero.json',W/'gap105-prefix-ramp-master.npz',W/'gap105-prefix-coast-master.npz') as src:
 base=sys.modules['nonfold_fixed_weighted_formula'].base
 packet,audit=ref.audit_row(src,s,caches['observer'].u,base)
 before=src.metric.radius(s);assert np.array_equal(np.asarray(before),packet['radius'][0])
 np.save(W/'polar-G10-consistent-arc-audit-jets.npy',packet['jets'])
 audit.update(independentTargetRadiusBytesUnchanged=True,actualTargetRadius=packet['radius'][0].tolist())
audit.update(sourceExit=src.exit_receipt,seconds=time.monotonic()-start,entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),helperSHA256=hashlib.sha256((W/'2ecf-polar-refined-arc-source-evaluator.py').read_bytes()).hexdigest())
(W/'polar-G10-consistent-arc-audit.json').write_text(json.dumps(audit,separators=(',',':'),allow_nan=False)+'\n')
print(json.dumps(dict(event='actual_consistent_global_arc_audit_passed',s=s,maxResidual=max(x['independentPrimitiveResidual'] for p in audit['strongerPrimitiveChecks'] for x in p['rootChecks']),seconds=audit['seconds'])),flush=True)
