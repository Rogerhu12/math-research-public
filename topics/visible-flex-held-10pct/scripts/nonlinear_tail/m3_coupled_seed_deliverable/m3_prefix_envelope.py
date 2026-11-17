"""Sample a reconstructed finite prefix's Cartesian radius, support and curvature.

No uniform enclosure is claimed. Material angular shifts and spatial rotations
preserve these scalar geometric quantities in the associated phase family.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
p=argparse.ArgumentParser(description=__doc__)
for k in ('source-topic','short-bridge','checkpoint','port','output'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--angular',type=int,default=256);p.add_argument('--radial',type=int,default=1025)
a=p.parse_args();source=a.source_topic
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
ad=module('m3_envelope_adaptive',source/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=module('m3_envelope_flat',source/'scripts/db6f-prefix-flat-profile.py');patch.install(ad);ad.old.install_source(source/'repro/source-root');short=module('m3_envelope_short',a.short_bridge);short.install()
from curve_stable_prefix_bvp import load_checkpoint
r=load_checkpoint(a.checkpoint);port=json.loads(a.port.read_text());port['cut']['_prefix_bridge']=r['frozen_profile']['prefix_bridge']
if not r['solver_success'] or port['parameters']!=r['physical_tail_parameters'] or port['cut']!=r['physical_tail_cut']:raise ValueError('Successful same-port prefix required')
_,BVP=ad.build_classes(r['chart']);obj=BVP(r['frozen_profile'],port,r['gauge_amplitude'],r['config']['modes'],a.angular,True,r['warp_reference_q'])
par=np.array(r['parameters']);par[0]=math.log(r['actual_primary_amplitude']/obj.q);obj.initial(par);flow=obj.flow(par[0])
pp=PPoly.construct_fast(np.array(r['pp_coefficients']),np.array(r['mesh']),extrapolate=True,axis=1);sol=SimpleNamespace(x=np.array(r['mesh']),y=pp(np.array(r['mesh'])),p=par,sol=pp)
s=np.unique(np.r_[np.linspace(0,flow.end,a.radial),flow.breaks]);height=flow.height_integral(sol,s,a.angular,6);B,B1,B2=flow.basis(a.angular)
result=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),q=r['actual_primary_amplitude'],modes=obj.M,angular=a.angular,radial=len(s),meridian_length=flow.end,maxNorm=0.,maxRadiusXY=0.,minSupport=float('inf'),maxCurvature=0.,minZ=float('inf'),maxZ=-float('inf'),where={})
for start in range(0,len(s),64):
 ss=s[start:start+64];Y,Yp,Ypp=pp(ss),pp(ss,1),pp(ss,2);fr,Xst,dW=flow.velocity_s(ss,Y,Yp,B1,B2);geo=fr['geo']
 X=geo['pos']+obj.q*flow.values(Y,B);X[:,:,2]+=height[start:start+64,None]
 Xs=geo['s1']+obj.q*flow.values(Yp,B);Xs[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
 Xss=geo['s2']+obj.q*flow.values(Ypp,B);Xss[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
 Xt=fr['d'];Xtt=fr['dd'];cross=np.cross(Xt,Xs);normal=cross/np.linalg.norm(cross,axis=2)[:,:,None]
 dot=lambda U,V:np.einsum('sui,sui->su',U,V)
 E,F,G=dot(Xs,Xs),dot(Xs,Xt),dot(Xt,Xt);e,f,g=dot(normal,Xss),dot(normal,Xst),dot(normal,Xtt)
 det=E*G-F*F;tr=e*G+g*E-2*f*F;curv=(np.abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*det*(e*g-f*f))))/(2*det)
 values={'maxNorm':np.linalg.norm(X,axis=2),'maxRadiusXY':np.linalg.norm(X[:,:,:2],axis=2),'maxCurvature':curv,'minSupport':dot(X,normal)}
 for k,v in values.items():
  ix=np.unravel_index(np.argmin(v)if k=='minSupport'else np.argmax(v),v.shape);z=float(v[ix]);better=z<result[k]if k=='minSupport'else z>result[k]
  if better:result[k]=z;result['where'][k]=dict(s=float(ss[ix[0]]),u=float(2*np.pi*ix[1]/a.angular))
 result['minZ']=min(result['minZ'],float(X[:,:,2].min()));result['maxZ']=max(result['maxZ'],float(X[:,:,2].max()))
result['centered_reflection_diameter_bound_sampled']=2*result['maxNorm']
a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
