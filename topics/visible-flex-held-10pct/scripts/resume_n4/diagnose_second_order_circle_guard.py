from pathlib import Path
import gzip,json,hashlib
import numpy as np
from tight_moment_interval_bounds import install
install()
from plateau_core import PlateauSupportCore
from second_order_large_radius_core import make_core_class,PROVENANCE
p=Path('/workspace/scratch/7322d0dee069/transfer_work/n4-thicker-cut/q0125-m16-lam0.json.gz');r=json.loads(gzip.decompress(p.read_bytes()));c=np.zeros(19);c[:15]=np.asarray(r['parameters'][1:])*r['central_correction_scales'];c[0]=0.
Core=make_core_class(PlateauSupportCore);rows=[]
for lam in [1e-4,.001,.005,.01]:
 try:
  z=Core(r['gauge_amplitude'],c,4,arc_nodes=1024,**(r['plateau_settings']|dict(homotopy=lam)))
  row=dict(homotopy=lam,passed=True,rho_lower=z.rho_lower,rho_min_sample=z.rho_min_sample,grid=z.positivity_grid_per_sector,derivative_bound=z.rho_derivative_bound,second_derivative_bound=z.rho_second_derivative_bound,value_allowance=z.rho_value_roundoff_allowance)
 except Exception as exc:row=dict(homotopy=lam,passed=False,error=repr(exc))
 rows.append(row);print(json.dumps(row),flush=True)
result=dict(scope='Same exact complete proposed input core. The original two sufficient bounds are retained, and the C2 interpolation bound is added; no BVP acceptance asserted',input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),guard_definition=PROVENANCE,rows=rows)
Path('w016-q0125-m20-second-order-circle-guard.json').write_text(json.dumps(result,indent=2)+'\n')
