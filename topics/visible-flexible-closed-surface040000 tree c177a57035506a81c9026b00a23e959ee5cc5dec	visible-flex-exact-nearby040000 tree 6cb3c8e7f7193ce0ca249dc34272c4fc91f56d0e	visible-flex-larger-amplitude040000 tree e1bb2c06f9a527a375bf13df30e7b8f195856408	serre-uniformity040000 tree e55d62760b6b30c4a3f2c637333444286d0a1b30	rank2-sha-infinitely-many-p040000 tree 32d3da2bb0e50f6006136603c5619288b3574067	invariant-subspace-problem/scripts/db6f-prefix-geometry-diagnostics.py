#!/usr/bin/env python3
"""Sample physical XYZ, support, curvature and a short-meridian held witness.
Uses the correct saved flat/cosine metric. These are sampled diagnostics, not
continuous certificates, a full tail/cap audit, or an exact-isometry proof.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math
from pathlib import Path
import numpy as np
S=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--linear-port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--radial',type=int,default=1201);p.add_argument('--angular',type=int,default=1024);p.add_argument('--local-end',type=float,default=.25);a=p.parse_args()
spec=importlib.util.spec_from_file_location('flat_geometry',S/'db6f-prefix-flat-geometry-source.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rec,o,f,sol=m.source(a.checkpoint,a.linear_port,a.source_root)
s=np.unique(np.r_[sol.x,np.linspace(0,f.end,a.radial),a.local_end]);B,B1,B2=f.basis(a.angular);h=f.height_integral(sol,s,a.angular,8);normal=np.array([.5,math.sqrt(3)/2,0.]);core=o._core.summary();Delta=core['phase_pi_over_base_mode_support_gap_at_phi0'];point=core['radius_max_sample']*normal
out=dict(scope=__doc__,source=str(a.checkpoint),source_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),physical_profile=rec['frozen_profile'],chart=rec['chart'],modes=o.M,angular=a.angular,radial_nodes=len(s),source_nodes=len(sol.x),max_norm=0.,min_outward_support=1e9,max_actual_curvature=0.,local_end=a.local_end,local_min_Fsz=1e9,local_max_abs_Fssu=0.,far_min_height=1e9,min_support_distance_bound=1e9,min_direct_distance=1e9,core_gap=Delta,core=core)
for start in range(0,len(s),32):
 sl=slice(start,start+32);ss=s[sl];Y=sol.sol(ss);Yp=sol.sol(ss,1);Ypp=sol.sol(ss,2);fr,Fsp,dW=f.velocity_s(ss,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']
 pos=g['pos']+o.q*f.values(Y,B);pos[:,:,2]+=h[sl,None]
 Fsc=g['s1']+o.q*f.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
 Fssc=g['s2']+o.q*f.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
 Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
 Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
 Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
 Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
 nn=np.cross(Ft,Fs);nn/=np.linalg.norm(nn,axis=2)[:,:,None]
 E=np.sum(Fs*Fs,axis=2);Fm=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2);L=np.sum(Fss*nn,axis=2);M=np.sum(Fst*nn,axis=2);N=np.sum(Ftt*nn,axis=2);detI=E*G-Fm*Fm;tr=(L*G-2*M*Fm+N*E)/detI;detII=(L*N-M*M)/detI;kap=(abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*detII)))/2
 out['max_norm']=max(out['max_norm'],float(np.linalg.norm(pos,axis=2).max()));out['min_outward_support']=min(out['min_outward_support'],float(np.sum(pos*nn,axis=2).min()));out['max_actual_curvature']=max(out['max_actual_curvature'],float(kap.max()))
 A=(pos@normal).max(axis=1);Bm=pos[:,:,2].min(axis=1);dist=np.sqrt(np.maximum(core['radius_max_sample']-A,0.)**2+np.maximum(Bm,0.)**2)
 out['min_support_distance_bound']=min(out['min_support_distance_bound'],float(dist.min()));out['min_direct_distance']=min(out['min_direct_distance'],float(np.linalg.norm(pos-point,axis=2).min()))
 local=ss<=a.local_end
 if np.any(local):out['local_min_Fsz']=min(out['local_min_Fsz'],float(Fs[local,:,2].min()));out['local_max_abs_Fssu']=max(out['local_max_abs_Fssu'],float(abs(Fss[local]@normal).max()))
 far=ss>=a.local_end
 if np.any(far):out['far_min_height']=min(out['far_min_height'],float(pos[far,:,2].min()))
 if start==0:
  out['inlet_physical_first_error']=float(np.linalg.norm(Fs[0]-[0,0,1],axis=1).max());out['inlet_horizontal_second_max']=float(abs(Fss[0,:,:2]).max());out['inlet_height_second_max']=float(abs(Fss[0,:,2]).max())
end=np.array([f.end]);Y=sol.sol(end);Yp=sol.sol(end,1);Ypp=sol.sol(end,2);fr,_,dW=f.velocity_s(end,Y,Yp,B1,B2)
out['cut']=dict(height=(f.bridge.sigma*o.q*Y[o.iz:,0]).tolist(),mean_height=float(h[-1]),height_s=(o.q*Yp[o.iz:,0]).tolist(),height_ss=(o.q*Ypp[o.iz:,0]).tolist(),mean_height_s=float(np.mean(fr['V'][:,:,2])),mean_height_ss=float(np.mean(dW[:,:,2])),r=f.port_data['cut']['radius'])
out['sampled_two_ball_D']=2*out['max_norm'];out['sampled_hold_ratio']=min(Delta,out['min_support_distance_bound'])/out['sampled_two_ball_D'];out['local_margin_b2_minus_DeltaL']=out['local_min_Fsz']**2-Delta*out['local_max_abs_Fssu'];out['local_b_s0_minus_Delta']=out['local_min_Fsz']*a.local_end-Delta
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['sampled_two_ball_D','sampled_hold_ratio','min_outward_support','max_actual_curvature','core_gap','local_min_Fsz','local_max_abs_Fssu','local_margin_b2_minus_DeltaL','local_b_s0_minus_Delta','far_min_height']}),flush=True)
