#!/usr/bin/env python3
"""Evaluate R71's nonprojected ruled continuation on an actual finite entry.

Input is a saved successful outward-coast finite Fourier IVP with a''=0 at
its endpoint. Use actual projected left velocity and the original material
angle, so the finite map matches its incoming first jet exactly. Its small
entry metric/frame defects are NOT discarded. The actual two-dimensional
metric and curvature are computed from derivatives of the resulting map;
the boundary second-jet defect is reported rather than silently removed.
All bounds here are samples, and this is still only a surface with boundary.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_probe',P/'alternative-outward-probe.py');pr=importlib.util.module_from_spec(sp);sp.loader.exec_module(pr)

def angular_derivative(f,order=1):
 n=len(f);k=np.fft.fftfreq(n,1/n)
 factor=(1j*k)**order
 if f.ndim>1:factor=factor[:,None]
 return np.fft.ifft(np.fft.fft(f,axis=0)*factor,axis=0).real

def world(q,phi):
 c=np.cos(phi);s=np.sin(phi)
 return np.stack([c*q[:,0]-s*q[:,1],s*q[:,0]+c*q[:,1],q[:,2]],axis=1)

def shape(Xs,Xp,Xss,Xsp,Xpp):
 E=np.sum(Xs*Xs,axis=1);F=np.sum(Xs*Xp,axis=1);G=np.sum(Xp*Xp,axis=1)
 n=np.cross(Xs,Xp);nn=np.linalg.norm(n,axis=1);n/=nn[:,None]
 L=np.sum(Xss*n,axis=1);M=np.sum(Xsp*n,axis=1);C=np.sum(Xpp*n,axis=1)
 det=E*G-F*F;tr=(L*G+C*E-2*M*F)/det;kd=(L*C-M*M)/det
 kap=(np.abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*kd)))/2
 return n,kap,kd

def evaluate(path,width=.3,radial=81,angular=4096):
 data=json.loads(path.read_text());cfg=data['config'];assert data['status']=='success'
 if cfg.get('radial_law')=='fast_outward':
  sf=importlib.util.spec_from_file_location('alternative_fast_profile_for_flat',P/'alternative-fast-profile.py');fast=importlib.util.module_from_spec(sf);sf.loader.exec_module(fast)
  probe=fast.probe_class()(cfg['A'],cfg['M'],angular,cfg['v'],cfg['S'],cfg['power'])
 else:probe=pr.Probe(cfg['A'],cfg['M'],angular,cfg['v'],cfg['S'],cfg['amax'],cfg.get('coast_at'),cfg.get('coast_length',.1))
 s0=data['reached_s'];a0,c,acc=probe.profile(s0)
 if abs(acc)>1e-12:raise ValueError('The supplied entry has nonzero a second derivative; first append a genuine acceleration ramp.')
 y=np.asarray(data['final_coefficients']);fr=probe.frame(s0,y);yp=probe.project(fr['V']);V,Vp,Vpp=probe.jet(yp)
 gam=world(fr['F'],probe.phi);gp=world(fr['d'],probe.phi);gpp=world(fr['dd'],probe.phi)
 d0=world(V,probe.phi);dp=world(Vp,probe.phi);rho=probe.rho0;T0=gp/(a0*rho[:,None])
 norm=np.cross(d0,T0);norm/=np.linalg.norm(norm,axis=1)[:,None]
 Cden=np.sum(gpp*norm,axis=1);b0=a0*rho*np.sum(dp*norm,axis=1)/Cden
 SS=1+b0*b0;t0=a0/np.sqrt(SS);k=a0*b0/np.sqrt(SS);e=(d0-b0[:,None]*T0)/np.sqrt(SS)[:,None]
 ep=angular_derivative(e);epp=angular_derivative(e,2);kp=angular_derivative(k);kpp=angular_derivative(k,2)
 rho_p=6*cfg['A']*np.sin(2*probe.phi)-60*cfg['A']/(10*np.sqrt(2))*np.sin(4*probe.phi)
 # Actual left finite-ODE second derivative, not a normal-curvature substitution.
 h=1e-25
 jj=probe.project(probe.frame(s0,y.astype(complex)+1j*h*yp,strict=False)['V']).imag/h
 da=c*c/(a0*a0*fr['kap']);db=-fr['al']*da/fr['be']
 ypp=jj+probe.project(da[:,None]*fr['N']+db[:,None]*fr['B'])
 left_ss=world(probe.jet(ypp)[0],probe.phi)
 rows=[];seam={}
 for s in np.linspace(0,width,radial):
  a=a0+c*s;t=np.sqrt(a*a-k*k);ell=(t-t0)/c
  ellp=k*kp*(1/t0-1/t)/c
  ellpp=((kp*kp+k*kpp)*(1/t0-1/t)+k*k*kp*kp*(1/t0**3-1/t**3))/c
  up=rho+kp/c*(1/t-1/t0)
  upp=rho_p+kpp/c*(1/t-1/t0)+k*kp*kp/c*(1/t**3-1/t0**3)
  us=-k/(a*t);uss=k*c*(1/(a*a*t)+1/t**3);usp=-a*kp/t**3
  X=gam+ell[:,None]*e
  Xs=(a/t)[:,None]*e
  Xp=gp+ellp[:,None]*e+ell[:,None]*ep
  Xss=(-c*k*k/t**3)[:,None]*e
  Xsp=(a*k*kp/t**3)[:,None]*e+(a/t)[:,None]*ep
  Xpp=gpp+ellpp[:,None]*e+2*ellp[:,None]*ep+ell[:,None]*epp
  q=us/up;qs=(uss*up-us*usp)/up**2;qp=(usp*up-us*upp)/up**2
  Fs=Xs-q[:,None]*Xp;Fu=Xp/up[:,None]
  Fss=Xss-2*q[:,None]*Xsp+q[:,None]**2*Xpp-(qs-q*qp)[:,None]*Xp
  E=np.sum(Fs*Fs,axis=1);F=np.sum(Fs*Fu,axis=1);G=np.sum(Fu*Fu,axis=1)
  metric=max(float(abs(E-1).max()),float(abs(F/a).max()),float(abs(G/a**2-1).max()))
  normal,kap,kd=shape(Xs,Xp,Xss,Xsp,Xpp)
  if s==0:
   seam=dict(position_jump=float(np.linalg.norm(X-gam,axis=1).max()),velocity_jump=float(np.linalg.norm(Fs-d0,axis=1).max()),second_radial_jump=float(np.linalg.norm(Fss-left_ss,axis=1).max()))
  rows.append(dict(s=float(s),a=float(a),J_min=float((up/rho).min()),metric_sample=metric,kappa_sample=float(kap.max()),gaussian_curvature_abs_sample=float(abs(kd).max()),radius_max=float(np.linalg.norm(X[:,:2],axis=1).max()),height_min=float(X[:,2].min()),height_max=float(X[:,2].max()),ball_radius_max=float(np.linalg.norm(X,axis=1).max()),outward_support_min=float((-np.sum(X*normal,axis=1)).min())))
 return dict(scope=__doc__,input=str(path),input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),probe_source_sha256=hashlib.sha256((P/'alternative-outward-probe.py').read_bytes()).hexdigest(),config=dict(width=width,radial=radial,angular=angular,a0=a0,c=c),entry_b_max=float(abs(b0).max()),entry_Cden_abs_min=float(abs(Cden).min()),entry_ez_min=float(e[:,2].min()),seam=seam,maxima=dict(metric_sample=max(r['metric_sample']for r in rows),kappa_sample=max(r['kappa_sample']for r in rows),ball_radius_sample=max(r['ball_radius_max']for r in rows),height_sample=max(r['height_max']for r in rows)),minima=dict(J_sample=min(r['J_min']for r in rows),outward_support_sample=min(r['outward_support_min']for r in rows)),rows=rows)

def main():
 pa=argparse.ArgumentParser();pa.add_argument('--input',type=Path,required=True);pa.add_argument('--width',type=float,default=.3);pa.add_argument('--radial',type=int,default=81);pa.add_argument('--angular',type=int,default=4096);pa.add_argument('--out',type=Path,required=True);a=pa.parse_args()
 r=evaluate(a.input,a.width,a.radial,a.angular);a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k]for k in ['config','entry_b_max','entry_ez_min','seam','maxima','minima']}));print(json.dumps(r['rows'][-1]))
if __name__=='__main__':main()
