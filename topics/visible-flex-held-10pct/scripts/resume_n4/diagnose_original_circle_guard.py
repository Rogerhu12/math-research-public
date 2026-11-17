from pathlib import Path
import gzip,json
import numpy as np
from tight_moment_interval_bounds import install
install()
from plateau_core import PlateauSupportCore
from large_radius_local_core import make_core_class
p=Path('/workspace/scratch/7322d0dee069/transfer_work/n4-thicker-cut/q0125-m16-lam0.json.gz');r=json.loads(gzip.decompress(p.read_bytes()));c=np.zeros(19);c[:15]=np.asarray(r['parameters'][1:])*r['central_correction_scales'];c[0]=0.;Core=make_core_class(PlateauSupportCore);rows=[]
for lam in [1e-4,.001,.005]:
 try:
  z=Core(r['gauge_amplitude'],c,4,arc_nodes=1024,**(r['plateau_settings']|dict(homotopy=lam)))
  row=dict(homotopy=lam,passed=True,rho_lower=z.rho_lower,grid=z.positivity_grid_per_sector,derivative_bound=z.rho_derivative_bound,value_allowance=z.rho_value_roundoff_allowance)
 except Exception as exc:row=dict(homotopy=lam,passed=False,error=repr(exc))
 rows.append(row);print(json.dumps(row),flush=True)
Path('w016-q0125-m20-circle-core-guard.json').write_text(json.dumps(rows,indent=2)+'\n')
