from pathlib import Path
import sys,json,gzip,hashlib
from functools import lru_cache
import numpy as np
b=Path('/workspace/scratch/f00f08c94d46');w=b/'even_plateau_work';sys.path[:0]=[str(w/'complementary_snapshot'),str(w)]
from complementary_moment_basis import ComplementaryMomentBasis
import uniform_complement_core as wrapper
from plateau_core import PlateauSupportCore as ReferenceCore
wrapper.ComplementaryMomentBasis=lru_cache(maxsize=32)(ComplementaryMomentBasis)
Core=wrapper.make_core_class(ReferenceCore)
p=b/'smallcut_highq_work/fixed-r30-p20-q20-m24/fixed.json.gz';d=json.load(gzip.open(p,'rt'))
co=np.array(d['summary']['core']['coefficients']);out=[]
for M in [8,12,16,20]:
 basis=wrapper.ComplementaryMomentBasis(base_mode=2,modes=M,halfwidth=.28,transition=.08,center=0.,lock_fundamental=False)
 c=co[1:M];q=co[0]-c@basis.fundamental_leakage
 for lam in [0.,.001,.01,.05,1.]:
  r=dict(M=M,q_parameter=float(q),old_primary=float(co[0]),lambda_value=lam,support_condition=basis.constants['support_condition'],support_coefficients=c.tolist())
  try:
   core=Core(q,c,2,halfwidth=.28,transition=.08,control_transition=.08,homotopy=lam,arc_nodes=1024)
   s=core.summary();r.update(success=True,rho_min_sample=s['rho_min_sample'],rho_lower=s['rho_lower_conservative'],rho_derivative_bound=s['rho_derivative_bound'],radius_max_sample=s['radius_max_sample'])
  except Exception as e:r.update(success=False,error=repr(e))
  out.append(r);print(json.dumps(r),flush=True)
  (b/'m2_circle_work/legacy_core_probe.json').write_text(json.dumps(dict(scope='Core-only initializer audit, no BVP or geometric family.',input_checkpoint_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),source_sha256={str(f.relative_to(b)):hashlib.sha256(f.read_bytes()).hexdigest()for f in [Path(__file__),w/'plateau_core.py',w/'complementary_snapshot/uniform_complement_core.py',w/'complementary_snapshot/complementary_moment_basis.py',w/'complementary_snapshot/moment_interval_bounds.py']},rows=out),indent=2)+'\n')
