"""Compare full Cartesian two-jets in the same material angle and s direction.

Only one global rotation about z and one translation are fitted. No material
reparametrization or per-point alignment is permitted. Arrays stay in scratch.
"""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('prefix',type=Path);p.add_argument('tail',type=Path);p.add_argument('output',type=Path)
a=p.parse_args();pre=np.load(a.prefix);tail=json.loads(a.tail.read_text())
keys=('X','Xs','Xss','Xtheta','Xstheta','Xthetatheta')
t={k:np.array([r[k]for r in tail['rows']])for k in keys}
angles=np.array([r['theta']for r in tail['rows']])
if not np.allclose(pre['theta'],angles,rtol=0,atol=1e-14):raise ValueError('Material angular grids differ')
u=t['X'][:,:2]-t['X'][:,:2].mean(0);v=pre['X'][:,:2]-pre['X'][:,:2].mean(0)
dot=(u*v).sum();cross=(u[:,0]*v[:,1]-u[:,1]*v[:,0]).sum();theta=float(np.arctan2(cross,dot))
R=np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
translation=pre['X'].mean(0)-t['X'].mean(0)@R.T
result={}
for k in keys:
 z=t[k]@R.T+(translation if k=='X' else 0);d=z-pre[k]
 result[k]={'sup_euclidean':float(np.linalg.norm(d,axis=1).max()),'max_component':float(np.abs(d).max())}
report=dict(scope=__doc__,prefix_sha256=hashlib.sha256(a.prefix.read_bytes()).hexdigest(),tail_sha256=hashlib.sha256(a.tail.read_bytes()).hexdigest(),angular=len(angles),rotation_about_z=theta,translation=translation.tolist(),differences=result,radial_difference_step=tail['radialDifferenceStep'],tail_actual_metric=tail['actualMetric'],tail_root_residual=tail['rootResidual'])
a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
