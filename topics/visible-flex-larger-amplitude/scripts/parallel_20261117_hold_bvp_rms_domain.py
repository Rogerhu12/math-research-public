#!/usr/bin/env python3
"""Read-only domain audit at the actual collocation/RMS evaluation points.
No field, mesh, equation, boundary target, or solver is changed.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
import scipy.integrate._bvp as backend
from parallel_20261117_frenet_symbol import Frenet
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(a):
 spec=importlib.util.spec_from_file_location('actual_hold_domain',a.hold_source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);runs=[]
 for path in a.inputs:
  d=json.loads(gzip.decompress(path.read_bytes()));profile=m.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin']);q=Frenet(d['M'],d['N'])
  x=np.array(d['mesh']);y=np.array(d['states']);f=np.array(d['full_ode_rhs_at_nodes']if d.get('preparation_only')else d['rhs']);h=np.diff(x)
  spline=backend.create_spline(y.T,f.T,x,h);rows=[]
  for name,u in [('midpoint',.5),('Lobatto_left',.5-.5*np.sqrt(3/7)),('Lobatto_right',.5+.5*np.sqrt(3/7))]:
   s=x[:-1]+u*h;v=spline(s).T;bad=[];low=dict(value=np.inf)
   for j,(t,z)in enumerate(zip(s,v)):
    r,ap,_=profile(float(t));_,dt,dd=q.jet(z);Q=np.sum(dt*dt,axis=1);W=np.sum(np.cross(dt,dd)**2,axis=1);H=W-(ap/r)**2*Q**3;k=int(np.argmin(H))
    if H[k]<low['value']:low=dict(value=float(H[k]),s=float(t),cell=j,angle=float(q.angle[k]))
    if min(Q.min(),W.min(),H.min())<=0:bad.append(j)
   rows.append(dict(kind=name,cell_coordinate=float(u),invalid_count=len(bad),invalid_cells=bad,Hmin=low))
  runs.append(dict(input_sha256=sha(path),nodes=len(x),M=q.M,N=q.N,rows=rows))
 report=dict(scope=__doc__,source_sha256=sha(__file__),hold_profile_sha256=sha(a.hold_source),backend_sha256=sha(backend.__file__),runs=runs)
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--inputs',type=Path,nargs='+',required=True)
 for k in ('hold-source','out'):p.add_argument('--'+k,type=Path,required=True)
 main(p.parse_args())
