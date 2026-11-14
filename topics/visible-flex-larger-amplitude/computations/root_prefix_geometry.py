#!/usr/bin/env python3
"""Sample the image geometry of a saved m2 prefix in either supported chart.

The upper prefix is mirrored across z=0. This remains a surface with two
boundary circles, not a closed candidate. Point-cloud Hausdorff values and
diameters have no continuous sampling-error certificate and are design screens.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source-topic','checkpoint','port','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--radial',type=int,default=241)
    p.add_argument('--angular',type=int,default=512)
    p.add_argument('--phases',type=int,default=8)
    a=p.parse_args();started=time.time()
    path=Path(__file__).with_name('geometric-checkpoint-core-pullback.py')
    spec=importlib.util.spec_from_file_location('root_geometry_pullback',path)
    pullback=importlib.util.module_from_spec(spec);spec.loader.exec_module(pullback)
    saved,_=pullback.load_saved(a.checkpoint,a.source_topic,a.port,angular=max(256,a.angular))
    if not saved.rec['solver_success']:raise ValueError('Only solved prefixes are screened')
    if saved.mode!=2:raise ValueError('Exact central symmetry diameter identity requires mode 2')
    f=saved.flow;s=np.unique(np.r_[np.linspace(0,f.end,a.radial),f.breakpoints,f.end])
    h=f.height_integral(saved.sol,s,256,6);B,_,_=f.basis(a.angular)
    groups=[]
    for start in range(0,len(s),32):
        sl=slice(start,start+32);ss=s[sl]
        points=f.geo(ss,a.angular)['pos']+saved.q*f.values(saved.sol.sol(ss),B)
        points[:,:,2]+=h[sl,None];groups.append(points.reshape(-1,3))
    upper=np.concatenate(groups);lower=upper*np.array([1.,1.,-1.]);cloud=np.concatenate([upper,lower])
    diam=2*float(np.linalg.norm(cloud,axis=1).max());tree=cKDTree(cloud)
    rows=[]
    for phase in np.linspace(0,math.pi/2,a.phases+1)[1:]:
        c,sn=math.cos(phase),math.sin(phase)
        R=np.array([[c,-sn,0.],[sn,c,0.],[0.,0.,1.]])
        turned=cloud@R.T
        forward,nearest=tree.query(turned,workers=1)
        backward,nearest_back=cKDTree(turned).query(cloud,workers=1)
        i=int(forward.argmax());j=int(backward.argmax());d=float(max(forward[i],backward[j]))
        rows.append(dict(phase=float(phase),hausdorff_sample=d,held_over_D_sample=d/diam,
            forward=float(forward[i]),backward=float(backward[j]),
            forward_witness=turned[i].tolist(),forward_nearest=cloud[nearest[i]].tolist(),
            backward_witness=cloud[j].tolist(),backward_nearest=turned[nearest_back[j]].tolist()))
    coeff=np.array(saved.rec.get('core',saved.rec.get('summary',{}).get('core',{}))['coefficients'])
    witness=np.array([0.,1+coeff.sum(),0.]);dist,index=tree.query(witness)
    result=dict(scope=__doc__,checkpoint=str(a.checkpoint),checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
        source_revision=json.loads((a.source_topic/'source-origin.json').read_text())['source_revision']if(a.source_topic/'source-origin.json').exists()else None,
        modes=saved.M,q=saved.q,radial_samples=len(s),angular_samples=a.angular,
        upper_points=len(upper),diameter_sample=diam,phases=rows,best=max(rows,key=lambda r:r['hausdorff_sample']),
        core_axis_witness=dict(point=witness.tolist(),distance_sample=float(dist),nearest=cloud[index].tolist()),
        seconds=time.time()-started)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ('q','modes','diameter_sample','best','core_axis_witness','seconds')}),flush=True)

if __name__=='__main__':main()
