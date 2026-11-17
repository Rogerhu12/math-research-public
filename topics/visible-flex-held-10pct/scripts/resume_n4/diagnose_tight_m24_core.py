from pathlib import Path
import time,json
import numpy as np
from tight_moment_interval_bounds import install,PROVENANCE
install()
from plateau_core import PlateauSupportCore
from large_radius_local_core import make_core_class
start=time.monotonic();root=Path(__file__).parent;old=json.loads((root/'diagnose_m24_core_bound.json').read_text())
Core=make_core_class(PlateauSupportCore)
z=Core(.0175,old['c'],4,halfwidth=.147,transition=.08,control_transition=.16,center=np.pi/4,homotopy=0.,bimodal_eta=.1)
row=dict(scope='Same q .0175/M24 complete seed core; only exact moment interval remainder degree increases',certificate=PROVENANCE,rho_min_sample=z.rho_min_sample,rho_triangle_lower=z.rho_triangle_lower,rho_lower=z.rho_lower,derivative_bound=z.rho_derivative_bound,value_allowance=z.rho_value_roundoff_allowance,grid=z.positivity_grid_per_sector,neumann_residual=float(z.basis.certificate['neumann_residual']),inverse_error=float(z.basis.certificate['inverse_error']),seconds=time.monotonic()-start)
(root/'diagnose_tight_m24_core.json').write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row),flush=True)
