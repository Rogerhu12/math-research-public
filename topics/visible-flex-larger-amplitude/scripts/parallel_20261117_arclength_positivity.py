#!/usr/bin/env python3
"""Float evaluation of all-radial/all-angular analytic positivity bounds.

Real even trigonometric interpolation has cardinal l2 norm <=1, hence
L-infinity norm <=sqrt(N). On each radial quintic cell, vector Bernstein
bounds on F_sphi imply |q_N(s)-q_N(t)|_infinity <=sqrt(N)*B*|s-t|.
These inequalities do not assume q positive before taking norms. Positive
bounds establish the mathematical criterion if their numerical evaluations
are enclosed; this reader itself does not implement directed rounding.
"""
import argparse,gzip,hashlib,json,math,time
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
import parallel_20261117_inward_profile as scalar
p=argparse.ArgumentParser(description=__doc__)
for k in ('input','out'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--construction-angles',type=int,default=2048);p.add_argument('--angles',type=int,default=4096);p.add_argument('--radial-subdivisions',type=int,default=4);a=p.parse_args();start=time.perf_counter()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();d=json.loads(gzip.decompress(a.input.read_bytes()))
if not d['success']or sha(scalar.__file__)!=d['inward_profile_sha256']:raise ValueError('Actual accepted inward source required')
N=a.construction_angles;Q=a.angles;M=d['M'];qc=Frenet(M,N);qa=Frenet(M,Q);old=Frenet(M,d['N']);v=d['inward_scalar_profile'];profile=scalar.InwardProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'],v['cut'],v['curvature'],v['ramp_in'],v['ramp_out'],v['quadrature'])
x=np.array(d['mesh']);Y=np.array(d['states']);D=np.array(d['rhs']);DD=[]
for s,y,dy in zip(x,Y,D):
 r,ap,app=profile(s);k=ap/r;DD.append(old.jvp(y,k,dy,dk=app/r-k*k))
DD=np.array(DD);nu=qc.freq[1:];freq=np.arange(N//2+1);minimum=dict(value=np.inf);maxB=0.;maxloss=0.
for i,h in enumerate(np.diff(x)):
 c0=Y[i];c1=h*D[i];c2=h*h*DD[i]/2;aa=Y[i+1]-c0-c1-c2;bb=h*D[i+1]-c1-2*c2;cc=h*h*DD[i+1]-2*c2
 co=np.array([c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2]);dp=np.arange(1,6)[:,None]*co[1:]/h;B=0.
 for j in range(5):
  b=sum(math.comb(j,k)/math.comb(4,k)*dp[k]for k in range(j+1));R=b[1:M+1];T=b[M+1:2*M+1];Z=b[2*M+2:]
  bound=np.array([sum(abs(nu*R+T)),abs(b[0])+sum(abs(R+nu*T)),sum(abs(nu*Z))]);B=max(B,float(np.linalg.norm(bound)))
 lower=np.inf
 for u in np.linspace(0,1,a.radial_subdivisions+1):
  state=np.polynomial.polynomial.polyval(u,co);_,t,_=qc.jet(state);speed=np.linalg.norm(t,axis=1);spec=np.fft.rfft(speed)/N;spec[-1]*=.5
  hspec=np.zeros(Q//2+1,complex);hspec[:len(spec)]=spec
  if Q==N:hspec[-1]*=2
  values=np.fft.irfft(Q*hspec,n=Q);angular_lower=float(values.min()-np.pi/Q*2*np.sum(freq*abs(spec)));lower=min(lower,angular_lower)
 loss=np.sqrt(N)*B*h/(2*a.radial_subdivisions);global_lower=lower-loss;maxB=max(maxB,B);maxloss=max(maxloss,float(loss))
 if global_lower<minimum['value']:minimum=dict(value=float(global_lower),cell=i,left=float(x[i]),right=float(x[i+1]),angle_lower_at_sampled_s=float(lower),radial_loss=float(loss),derivative_bound=B)
rho=1+np.cos(qa.angle[:,None]*qa.freq[None,1:])@((1-nu*nu)*Y[0,1:M+1]);rho_lower=float(rho.min()-np.pi/Q*np.sum(nu*abs((1-nu*nu)*Y[0,1:M+1])))
report=dict(scope=__doc__,input_sha256=sha(a.input),source_sha256=sha(__file__),construction_angles=N,angle_samples=Q,radial_subdivisions=a.radial_subdivisions,
 cells=len(x)-1,minimum_bound=minimum,max_derivative_bound=maxB,max_radial_loss=maxloss,rho_all_angle_lower=rho_lower,seconds=time.perf_counter()-start)
a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print('sha256',sha(a.out))
