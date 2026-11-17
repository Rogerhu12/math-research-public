#!/usr/bin/env python3
"""Localize the original physical Cartesian Darboux tensor of an m3 prefix.

Uses the same exact angular chain rule and full 3x3 tensor as the original
950f adaptive audit. Also reports scalar Gauss/tangential Hessian defects and
an ODE-jet diagnostic at the same positions. The latter is not substituted for
the saved C2 interpolant, and is not itself claimed to define another surface.
All results are finite sampled diagnostics.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
p=argparse.ArgumentParser(description=__doc__)
for k in ('source-topic','short-bridge','checkpoint','port','output'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--angular',type=int,default=512)
a=p.parse_args()
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
ad=module('m3_tensor_adaptive',a.source_topic/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');patch=module('m3_tensor_flat',a.source_topic/'scripts/db6f-prefix-flat-profile.py');patch.install(ad);ad.old.install_source(a.source_topic/'repro/source-root');module('m3_tensor_short',a.short_bridge).install()
from curve_stable_prefix_bvp import load_checkpoint
r=load_checkpoint(a.checkpoint);port=json.loads(a.port.read_text());port['cut']['_prefix_bridge']=r['frozen_profile']['prefix_bridge']
if not r['solver_success'] or r['config']['base_mode']!=3 or port['parameters']!=r['physical_tail_parameters'] or port['cut']!=r['physical_tail_cut']:raise ValueError('Successful same-port m3 prefix required')
_,BVP=ad.build_classes(r['chart']);obj=BVP(r['frozen_profile'],port,r['gauge_amplitude'],r['config']['modes'],r['config']['angular'],True,r['warp_reference_q'])
par=np.array(r['parameters']);par[0]=math.log(r['actual_primary_amplitude']/obj.q);obj.initial(par);flow=obj.flow(par[0]);N=max(a.angular,16*(obj.M*3+1));B,B1,B2=flow.basis(N)
mesh=np.array(r['mesh']);pp=PPoly.construct_fast(np.array(r['pp_coefficients']),mesh,extrapolate=True,axis=1)
samples=np.unique(np.r_[np.linspace(0,flow.end,151),mesh,(mesh[:-1]+mesh[1:])/2]);dot=lambda U,V:np.einsum('sui,sui->su',U,V)
def audit_jets(s,Y,Yp,Ypp):
 aa,ap,app=flow.profile(s);fr,Fsp,dW=flow.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']
 Fsc=g['s1']+obj.q*flow.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
 Fssc=g['s2']+obj.q*flow.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
 Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
 Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
 Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
 Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
 U=Ft/aa[:,None,None];Hs=Fss;Hm=(Fst-ap[:,None,None]/aa[:,None,None]*Ft)/aa[:,None,None];Ht=(Ftt+(aa*ap)[:,None,None]*Fs)/aa[:,None,None]**2
 gram=np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]-U[:,:,:,None]*U[:,:,None,:]
 tensor=.5*(Hs[:,:,:,None]*Ht[:,:,None,:]+Ht[:,:,:,None]*Hs[:,:,None,:])-Hm[:,:,:,None]*Hm[:,:,None,:]+(app/aa)[:,None,None,None]*gram
 ft=np.fft.fft(tensor,axis=1)/N;l1=np.sum(np.sqrt(np.sum(abs(ft)**2,axis=(2,3))),axis=1)
 n=np.cross(Fs,Ft);n/=np.linalg.norm(n,axis=2)[:,:,None];ls,mm,nt=dot(Hs,n),dot(Hm,n),dot(Ht,n)
 scalar=ls*nt-mm*mm+(app/aa)[:,None];tangent=np.maximum.reduce([np.linalg.norm(H-l[:,:,None]*n,axis=2)for H,l in [(Hs,ls),(Hm,mm),(Ht,nt)]])
 metric=np.stack((dot(Fs,Fs)-1,dot(Fs,U),dot(U,U)-1),axis=2);metricl1=np.max(np.sum(abs(np.fft.fft(metric,axis=1)/N),axis=1),axis=1)
 E,F,G=dot(Fs,Fs),dot(Fs,U),dot(U,U);actualgauss=(ls*nt-mm*mm)/(E*G-F*F);gausserr=actualgauss+(app/aa)[:,None]
 return dict(l1=l1,sup=np.linalg.norm(tensor,axis=(2,3)),scalar=scalar,gauss_error=gausserr,tangent=tangent,metric_l1=metricl1,flow_defect=np.linalg.norm(Fs-fr['Vnormal'],axis=2),root=fr['margin'],profile=[aa,ap,app],Fss=Fss)
res=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),source_sha256=hashlib.sha256((a.source_topic/'scripts/950f-prefix-adaptive-chart-bvp-v2.py').read_bytes()).hexdigest(),q=r['actual_primary_amplitude'],modes=obj.M,angular=N,samples=len(samples),physical_tensor_formula='sym(Hss⊗Htt)-Hst⊗Hst+(a_ss/a)*(I-Xs⊗Xs-(Xu/a)⊗(Xu/a)); Hss=Xss, Hst=(Xsu-a_s*Xu/a)/a, Htt=(Xuu+a*a_s*Xs)/a^2',saved_interpolant={},ode_jet_diagnostic={},max_second_jet_change=0.)
for group in ['saved_interpolant','ode_jet_diagnostic']:
 res[group]={k:0. for k in ['darboux_l1','darboux_sup','scalar_gauss_defect_sup','actual_gauss_error_sup','tangential_hessian_sup','metric_l1','flow_defect','knot_darboux_l1','off_knot_darboux_l1']}
for first in range(0,len(samples),24):
 s=samples[first:first+24];Y,Yp,Ypp=pp(s),pp(s,1),pp(s,2);d=audit_jets(s,Y,Yp,Ypp)
 op=flow.adapt_fun(s,Y,par);ofr,_,odW=flow.velocity_s(s,Y,op);opp=flow.project(odW-ofr['geo']['s2'],flow.B)/obj.q;od=audit_jets(s,Y,op,opp)
 res['max_second_jet_change']=max(res['max_second_jet_change'],float(np.linalg.norm(d['Fss']-od['Fss'],axis=2).max()))
 for name,data in [('saved_interpolant',d),('ode_jet_diagnostic',od)]:
  out=res[name]
  for key,val in [('darboux_l1',data['l1']),('darboux_sup',data['sup']),('scalar_gauss_defect_sup',abs(data['scalar'])),('actual_gauss_error_sup',abs(data['gauss_error'])),('tangential_hessian_sup',data['tangent']),('metric_l1',data['metric_l1']),('flow_defect',data['flow_defect'])]:out[key]=max(out[key],float(np.max(val)))
  knot=np.isin(s,mesh)
  for key,mask in [('knot_darboux_l1',knot),('off_knot_darboux_l1',~knot)]:
   if np.any(mask):out[key]=max(out[key],float(np.max(data['l1'][mask])))
  row=int(np.argmax(data['l1']));value=float(data['l1'][row])
  if value>=out.get('worst_value',-1):
   si=float(s[row]);cell=min(len(mesh)-2,max(0,int(np.searchsorted(mesh,si,side='right')-1)));j=int(np.argmax(data['sup'][row]));out['worst_value']=value;out['worst']=dict(s=si,psi=float(2*np.pi*j/N),cell=cell,cell_width=float(mesh[cell+1]-mesh[cell]),cell_fraction=float((si-mesh[cell])/(mesh[cell+1]-mesh[cell])),is_knot=bool(knot[row]),a=float(data['profile'][0][row]),a_s=float(data['profile'][1][row]),a_ss=float(data['profile'][2][row]),root_min=float(data['root'][row].min()),metric_l1=float(data['metric_l1'][row]),gauss_at_worst=float(data['gauss_error'][row,j]),scalar_at_worst=float(data['scalar'][row,j]),tangent_at_worst=float(data['tangent'][row,j]))
knots=np.asarray(r['chart']['knots'])*flow.end
for name in ['saved_interpolant','ode_jet_diagnostic']:
 w=res[name]['worst'];j=int(np.argmin(abs(knots-w['s'])));w['nearest_angular_spline_knot']=float(knots[j]);w['nearest_angular_spline_knot_index']=j;w['distance_to_angular_spline_knot']=float(w['s']-knots[j])
 cell=w['cell'];w['cell_crosses_angular_spline_knot']=bool(mesh[cell]<knots[j]<mesh[cell+1])
res['saved_config_fixed_metric']=r['config']['fixed_metric']
a.output.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res),flush=True)
