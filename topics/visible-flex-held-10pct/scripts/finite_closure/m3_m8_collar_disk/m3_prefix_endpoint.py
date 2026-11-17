#!/usr/bin/env python3
"""Recover actual Cartesian position/two-jet at a successful small-cut prefix.
Includes nonlinear mean height and its derivatives. The saved arrays are local,
recomputable intermediate data; neither these nor H alone close a nonlinear tail.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--short-bridge',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--angular',type=int,default=512);a=p.parse_args()
source=a.source_topic
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
ad=module('m3_endpoint_adaptive',source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=module('m3_endpoint_flat',source/'scripts/db6f-prefix-flat-profile.py');patch.install(ad);ad.old.install_source(source/'repro/source-root');short=module('m3_endpoint_short',a.short_bridge);short.install()
from curve_stable_prefix_bvp import load_checkpoint
r=load_checkpoint(a.checkpoint)
if r['config']['base_mode']!=3:raise SystemExit('m3 checkpoint required.')
if not r['solver_success']:raise SystemExit('Successful checkpoint required.')
port=json.loads(a.port.read_text());port['cut']['_prefix_bridge']=r['frozen_profile']['prefix_bridge']
if port['parameters']!=r['physical_tail_parameters'] or port['cut']!=r['physical_tail_cut']:raise SystemExit('Physical port mismatch.')
_,BVP=ad.build_classes(r['chart']);obj=BVP(r['frozen_profile'],port,r['gauge_amplitude'],r['config']['modes'],a.angular,True,r['warp_reference_q'])
par=np.array(r['parameters']);par[0]=math.log(r['actual_primary_amplitude']/obj.q);obj.initial(par);flow=obj.flow(par[0])
pp=PPoly.construct_fast(np.array(r['pp_coefficients']),np.array(r['mesh']),extrapolate=True,axis=1);sol=SimpleNamespace(x=np.array(r['mesh']),y=pp(np.array(r['mesh'])),p=par,sol=pp)
s=np.array([flow.end]);height=flow.height_integral(sol,s,a.angular,6)[0];B,B1,B2=flow.basis(a.angular);Y,Yp,Ypp=pp(s),pp(s,1),pp(s,2);fr,Xsp,dW=flow.velocity_s(s,Y,Yp,B1,B2);geo=fr['geo']
chart_defect=max(float(np.max(np.abs(geo[k])))for k in ['v','vp','vs']);chart_defect=max(chart_defect,float(np.max(np.abs(geo['rho']-1))))
if chart_defect>1e-12:raise SystemExit('Endpoint angular chart is not identity.')
X=(geo['pos']+obj.q*flow.values(Y,B))[0];X[:,2]+=height
Xs=(geo['s1']+obj.q*flow.values(Yp,B))[0];Xs[:,2]+=np.mean(fr['V'][:,:,2])
Xss=(geo['s2']+obj.q*flow.values(Ypp,B))[0];Xss[:,2]+=np.mean(dW[:,:,2])
Xt=fr['d'][0];Xtt=fr['dd'][0];Xst=Xsp[0];rad=flow.profile(s)[0][0];E=np.einsum('ij,ij->i',Xs,Xs);F=np.einsum('ij,ij->i',Xs,Xt);G=np.einsum('ij,ij->i',Xt,Xt)
a.output.parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(a.output.with_suffix('.npz'),theta=2*np.pi*np.arange(a.angular)/a.angular,X=X,Xs=Xs,Xss=Xss,Xtheta=Xt,Xthetatheta=Xtt,Xstheta=Xst)
summary=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),array_sha256=hashlib.sha256(a.output.with_suffix('.npz').read_bytes()).hexdigest(),q=r['actual_primary_amplitude'],modes=r['config']['modes'],angular=a.angular,cut=port['cut'],mean_position=X.mean(axis=0).tolist(),mean_Xs=Xs.mean(axis=0).tolist(),mean_Xss=Xss.mean(axis=0).tolist(),mean_height=float(height),height_deviation_max=float(np.max(np.abs(X[:,2]-height))),metric_components_max=[float(np.max(np.abs(E-1))),float(np.max(np.abs(F/rad))),float(np.max(np.abs(G/rad**2-1)))],chart_defect=chart_defect)
a.output.with_suffix('.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary),flush=True)
