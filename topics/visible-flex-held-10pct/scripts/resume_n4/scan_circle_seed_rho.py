#!/usr/bin/env python3
"""Sample the exact normal-angle rho of one material-homotopy initializer.

Only the proposed initial core is examined. The positive-lambda BVP is not
solved, and sampled positivity limits are not continuous geometry certificates.
"""
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np
from tight_moment_interval_bounds import install
install()
from plateau_core import PlateauSupportCore
from large_radius_local_core import make_core_class
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--modes',type=int,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
x=json.loads(gzip.decompress(a.checkpoint.read_bytes()));settings=x['plateau_settings'];q=x['gauge_amplitude'];M0=x['config']['modes']
if a.modes<M0 or settings['homotopy']!=0 or x['config'].get('fixed_metric',False):raise ValueError('An unrounded design seed and nondecreasing mode count are required')
c=np.zeros(a.modes-1);c[:M0-1]=np.asarray(x['parameters'][1:])*x['central_correction_scales'];c[0]=0.
Core=make_core_class(PlateauSupportCore);z=Core(q,c,4,arc_nodes=1024,**settings)
phi=z.T*np.arange(16384)/16384;s=z._smooth_jets(phi)[0];chi=z.chi(phi)
lo=z.basis.support_jets(phi,2,0.);hi=z.basis.support_jets(phi,2,1.)
rho0=1+q*s+c@(lo[0]+lo[2]);delta=q*(chi*(z._circle_constant-s)+z.local_flatten_beta*(1-chi))+c@(hi[0]+hi[2]-lo[0]-lo[2])
mask=delta<0.;lam=float(np.min((rho0[mask]-1e-5)/(-delta[mask])))if mask.any()else None
row=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),physical_port_sha256=x['physical_port_sha256'],physical_profile=x['physical_profile'],q=q,modes=a.modes,eta=settings['bimodal_eta'],rho0_sample_min=float(rho0.min()),delta_rho_sample_min=float(delta.min()),delta_rho_sample_max=float(delta.max()),sampled_upper_lambda_for_this_unchanged_control_vector=lam,rows=[dict(homotopy=t,rho_min_sample=float((rho0+t*delta).min()))for t in [1e-6,1e-5,1e-4,.001,.005,.01]],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
a.out.write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row),flush=True)
