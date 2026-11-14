#!/usr/bin/env python3
"""Sample a support/height bound for the midpoint witness against the prefix.

At each sampled radial section, A=max F.n and B=min z give the valid bound
sqrt(max(xstar-A,0)^2+B^2), provided B>=0. The sampled collection itself is
not a continuous-domain proof. All source data describe a finite prefix.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--linear-port',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--ells',nargs='+',type=float,default=[0.,.02,.04,.08,.16])
    p.add_argument('--radial',type=int,default=1201)
    p.add_argument('--angular',type=int,default=1536)
    a=p.parse_args();S=Path(__file__).resolve().parent
    spec=importlib.util.spec_from_file_location('adaptive',S/'950f-prefix-adaptive-chart-bvp-v2.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.old.install_source(a.source_root)
    from curve_stable_prefix_bvp import load_checkpoint
    rec=load_checkpoint(a.checkpoint);port=json.loads(a.linear_port.read_text());_,BVP=m.build_classes(rec['chart'])
    M=rec['config']['modes'];q=rec['gauge_amplitude'];o=BVP(rec['frozen_profile'],port,q,M,max(256,32*M),True,rec['warp_reference_q'])
    par=np.asarray(rec['parameters']);par[0]=math.log(rec['actual_primary_amplitude']/q);f=o.flow(par[0]);o.initial(par)
    pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),np.asarray(rec['mesh']),extrapolate=True,axis=1)
    sol=SimpleNamespace(x=np.asarray(rec['mesh']),y=pp(np.asarray(rec['mesh'])),p=par,sol=pp)
    s=np.unique(np.r_[np.linspace(0,f.end,a.radial),sol.x,np.asarray(rec['chart']['knots'])*f.end]);B,_,_=f.basis(a.angular);h=f.height_integral(sol,s,a.angular,8)
    coefficients=np.asarray(o._core.summary()['coefficients']);xstar=1+float(coefficients.sum());normal=np.array([.5,math.sqrt(3)/2,0.]);point=xstar*normal
    core_support=1+float(np.sum((-1.)**np.arange(1,len(coefficients)+1)*coefficients));gap=xstar-core_support
    summaries=[dict(ell=ell,min_projection_bound=1e9,min_direct_distance=1e9,max_norm=0.)for ell in a.ells];rows=[]
    for start in range(0,len(s),32):
        sl=slice(start,start+32);g=f.geo(s[sl],a.angular);xyz=g['pos']+q*f.values(pp(s[sl]),B);xyz[:,:,2]+=h[sl,None]
        proj=xyz@normal;A=proj.max(axis=1);Bmin=xyz[:,:,2].min(axis=1)
        for j,sj in enumerate(s[sl]):rows.append(dict(s=float(sj),support_max_sample=float(A[j]),height_min_sample=float(Bmin[j])))
        for record in summaries:
            ell=record['ell'];z=xyz.copy();z[:,:,2]+=ell
            bounds=np.sqrt(np.maximum(xstar-A,0.)**2+np.maximum(Bmin+ell,0.)**2)
            direct=np.linalg.norm(z-point,axis=2);norm=np.linalg.norm(z,axis=2)
            j=int(bounds.argmin())
            if bounds[j]<record['min_projection_bound']:
                record['min_projection_bound']=float(bounds[j]);record['projection_witness_s']=float(s[sl][j])
            ij=np.unravel_index(direct.argmin(),direct.shape)
            if direct[ij]<record['min_direct_distance']:
                record['min_direct_distance']=float(direct[ij]);record['direct_witness_s']=float(s[sl][ij[0]])
            record['max_norm']=max(record['max_norm'],float(norm.max()))
    for r in summaries:
        r['sampled_two_ball_D']=2*r['max_norm'];r['sampled_comparison_hold_lower']=min(gap,r['min_projection_bound']);r['sampled_comparison_hold_ratio']=r['sampled_comparison_hold_lower']/r['sampled_two_ball_D']
    out=dict(scope=__doc__,checkpoint=str(a.checkpoint),checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),modes=M,radial_samples=len(s),angular_samples=a.angular,normal=normal.tolist(),witness=point.tolist(),core_support=core_support,support_gap=gap,ell_sweep=summaries,radial_envelope=rows)
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='radial_envelope'}),flush=True)


if __name__=='__main__':main()
