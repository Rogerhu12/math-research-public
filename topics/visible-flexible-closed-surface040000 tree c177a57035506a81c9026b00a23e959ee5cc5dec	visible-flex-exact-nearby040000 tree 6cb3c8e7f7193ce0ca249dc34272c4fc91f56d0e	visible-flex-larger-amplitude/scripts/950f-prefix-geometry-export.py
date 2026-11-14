#!/usr/bin/env python3
"""Reproducible sampled XYZ envelope and physical cut two-jet export.

This reads a complete prefix checkpoint without printing arrays. The envelope
is sampled, not a continuous-radius certificate; no complete closed surface.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--linear-port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--ell',type=float,default=.16);p.add_argument('--radial',type=int,default=801);p.add_argument('--angular',type=int,default=1024);a=p.parse_args()
S=Path(__file__).resolve().parent;spec=importlib.util.spec_from_file_location('adaptive',S/'950f-prefix-adaptive-chart-bvp-v2.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.old.install_source(a.source_root)
from curve_stable_prefix_bvp import load_checkpoint
rec=load_checkpoint(a.checkpoint);port=json.loads(a.linear_port.read_text());_,BVP=m.build_classes(rec['chart']);M=rec['config']['modes'];q=rec['gauge_amplitude'];o=BVP(rec['frozen_profile'],port,q,M,max(256,32*M),True,rec['warp_reference_q']);par=np.asarray(rec['parameters']);par[0]=math.log(rec['actual_primary_amplitude']/q);f=o.flow(par[0]);o.initial(par)
pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),np.asarray(rec['mesh']),extrapolate=True,axis=1);sol=SimpleNamespace(x=np.asarray(rec['mesh']),y=pp(np.asarray(rec['mesh'])),p=par,sol=pp)
s=np.unique(np.r_[np.linspace(0,f.end,a.radial),sol.x,np.asarray(rec['chart']['knots'])*f.end]);B,B1,B2=f.basis(a.angular);h=f.height_integral(sol,s,a.angular,8)
rows=[];maxR=0.;point=None
for start in range(0,len(s),32):
 sl=slice(start,start+32);g=f.geo(s[sl],a.angular);xyz=g['pos']+q*f.values(pp(s[sl]),B);xyz[:,:,2]+=h[sl,None]+a.ell
 radius=np.linalg.norm(xyz[:,:,:2],axis=2);norm=np.linalg.norm(xyz,axis=2)
 for j,sj in enumerate(s[sl]):
  rows.append(dict(s=float(sj),radius_max=float(radius[j].max()),z_min=float(xyz[j,:,2].min()),z_max=float(xyz[j,:,2].max()),norm_max=float(norm[j].max())))
 k=np.unravel_index(np.argmax(norm),norm.shape)
 if norm[k]>maxR:maxR=float(norm[k]);point=dict(s=float(s[sl][k[0]]),psi=float(2*np.pi*k[1]/a.angular),xyz=xyz[k].tolist())
end=np.array([f.end]);Y=pp(end);Yp=pp(end,1);Ypp=pp(end,2);fr,_,dW=f.velocity_s(end,Y,Yp,B1,B2)
cut=dict(scope='All height coefficients in physical material theta, since the chart is the identity to order two at the cut. Mean derivatives include the background.',basis='cos(3*j*theta), j=1,...,M',height=(q*Y[f.iz:,0]).tolist(),height_s=(q*Yp[f.iz:,0]).tolist(),height_ss=(q*Ypp[f.iz:,0]).tolist(),mean_height=float(h[-1]+a.ell),mean_height_s=float(np.mean(fr['V'][:,:,2])),mean_height_ss=float(np.mean(dW[:,:,2])),tail_input_height=(f.bridge.sigma*q*Y[f.iz:,0]).tolist(),sigma=f.bridge.sigma,E=port['cut']['E'],cut=port['cut'])
out=dict(scope=__doc__,checkpoint=str(a.checkpoint),checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),ell=a.ell,modes=M,radial_samples=len(s),angular_samples=a.angular,sampled_prefix_max_norm=maxR,sampled_two_ball_diameter=2*maxR,sampled_maximum_witness=point,core=o._core.summary(),cut=cut,radial_envelope=rows)
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k in ('sampled_prefix_max_norm','sampled_two_ball_diameter','sampled_maximum_witness','modes','radial_samples','angular_samples')}))
