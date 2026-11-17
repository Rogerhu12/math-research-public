#!/usr/bin/env python3
"""Actual 317-column finite response for the cached initial fast subspace.

Uses the same successful common-quintic reference, full varying Jacobian,
and independently frozen U/L/target.  This is not a nonlinear BVP.
"""
import argparse,gzip,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853,solve_ivp
from scipy.linalg import solve,svdvals

p=argparse.ArgumentParser(description=__doc__)
for name in ('topic','field','local-report','arrays','out'):p.add_argument('--'+name,type=Path,required=True)
args=p.parse_args();helper=args.topic/'notes/2026-11-17-parallel-geometry-frenet-schur.py'
spec=importlib.util.spec_from_file_location('fast_response_helper',helper)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
local=json.loads(args.local_report.read_text())
if h.sha(args.field)!=local['reference_sha256'] or h.sha(args.arrays)!=local['arrays_sha256']:
 raise ValueError('Reference or boundary arrays differ from the local definition')
data=json.loads(gzip.decompress(args.field.read_bytes()));cache=np.load(args.arrays)
U,L,target,T0,Qfast=[cache[k] for k in ('U','L','target','T0','Qfast')]
q=h.Frenet(data['M'],data['N']);reader=h.Frenet(q.M,8192);profile=h.profile_from(data)
x=np.array(data['mesh']);ys=np.array(data['states']);dy=np.array(data['rhs']);ddy=np.array(data['d2'])
free=U.shape[1];coeff=[]
for i,w in enumerate(np.diff(x)):
 c0=ys[i];c1=w*dy[i];c2=w*w*ddy[i]/2
 a=ys[i+1]-c0-c1-c2;b=w*dy[i+1]-c1-2*c2;c=w*w*ddy[i+1]-2*c2
 coeff.append(np.array([c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2]))
def reference(s):
 i=min(len(x)-2,max(0,int(np.searchsorted(x,s,side='right')-1)));w=x[i+1]-x[i];u=(s-x[i])/w
 return np.polynomial.polynomial.polyval(u,coeff[i]),np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*coeff[i][1:])/w
stats=dict(rhs_calls=0,reference_ODE_defect_max=0.);started=time.perf_counter()
def rhs(s,flat):
 y,v=reference(s);a,ap,_=profile(s);k=ap/a;A=q.jacobian(y,k)
 stats['rhs_calls']+=1
 stats['reference_ODE_defect_max']=max(stats['reference_ODE_defect_max'],float(np.max(abs(v-q.rhs(y,k)))))
 if stats['rhs_calls']%100==0:print(json.dumps(dict(event='progress',s=float(s),seconds=time.perf_counter()-started,**stats)),flush=True)
 return (A@flat.reshape(q.n,free)).ravel()
tau=x[-1]-x[0]
sol=DOP853(rhs,x[0],U.ravel(),x[-1],rtol=1e-9,atol=1e-12,first_step=tau/256,max_step=tau/128)
nodes=1
while sol.status=='running':sol.step();nodes+=1
if sol.status!='finished':raise RuntimeError('Variational propagation did not reach the endpoint')
response=sol.y.reshape(q.n,free);K=L@response;sigma=svdvals(K);eta=solve(K,target)
delta=U@eta;predicted=response@eta
def norms(c):return [float(np.linalg.norm(v,axis=1).max()) for v in reader.jet(c)]
out=dict(scope=__doc__,source_sha256=h.sha(__file__),helper_sha256=h.sha(helper),
         reference_sha256=h.sha(args.field),local_report_sha256=h.sha(args.local_report),arrays_sha256=h.sha(args.arrays),
         M=q.M,N=q.N,start=float(x[0]),end=float(x[-1]),free_count=free,fixed_count=q.n-free,
         integration=dict(rtol=1e-9,atol=1e-12,max_step=float(tau/128),nodes=nodes,nfev=sol.nfev,
                          seconds=time.perf_counter()-started,**stats),
         condition_2=float(sigma[0]/sigma[-1]),sigma_max=float(sigma[0]),sigma_min=float(sigma[-1]),
         right_row_residual_norm=float(np.linalg.norm(K@eta-target)),
         fixed_left_residual_norm=float(np.linalg.norm(T0@delta-Qfast@(Qfast.T@T0@delta))),
         initial_F_Fphi_Fphiphi_max=norms(delta),predicted_right_F_Fphi_Fphiphi_max=norms(predicted),
         initial_delta_coefficients=delta.tolist(),predicted_right_delta_coefficients=predicted.tolist())
a,ap,app=profile(x[0]);k=ap/a;kp=app/a-k*k;trial=ys[0]+delta
_,d,e=reader.jet(trial);Q=np.sum(d*d,axis=1);W=np.sum(np.cross(d,e)**2,axis=1);H=W-k*k*Q**3
out['actual_initial_domain']=dict(Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H.min()))
if H.min()>0:
 v=q.rhs(trial,k);acc=q.jvp(trial,k,v,dk=kp);V=reader.jet(v)[0]
 core=np.array(data['original_core_coefficients'])
 rho=1+np.cos(reader.angle[:,None]*reader.freq[None,1:])@((1-reader.freq[1:]**2)*core)
 er=np.sum(V*V,axis=1)-1;gr=Q/(a*rho)**2-1;cr=np.sum(V*d,axis=1)/(a*rho)
 error=(abs(er+gr)+np.sqrt((er-gr)**2+4*cr*cr))/2
 out['actual_initial_Gram']=float(error.max())
 out['old_prefix_first_second_jump']=[norms(v-np.array(data['old_cut_jets']['first']))[0],norms(acc-np.array(data['old_cut_jets']['second']))[0]]
 out['reference_first_second_change']=[norms(v-dy[0])[0],norms(acc-ddy[0])[0]]
def single(s,direction):
 y,_=reference(s);a,ap,_=profile(s)
 return q.jvp(y,ap/a,direction)
check=solve_ivp(single,(x[0],x[-1]),delta,method='DOP853',rtol=1e-12,atol=1e-20,
                first_step=tau/512,max_step=tau/512,t_eval=[x[-1]])
if not check.success:raise RuntimeError(check.message)
actual=check.y[:,-1];out['independent_single_JVP_check']=dict(nfev=check.nfev,rtol=1e-12,atol=1e-20,
 max_step=float(tau/512),right_row_residual_norm=float(np.linalg.norm(L@actual-target)),
 coefficient_difference_max=float(np.max(abs(actual-predicted))),difference_F_Fphi_Fphiphi_max=norms(actual-predicted))
out['added_value_only_Hermite_bounds']={str(w):dict(first=15*out['initial_F_Fphi_Fphiphi_max'][0]/(8*w),
 second=10*out['initial_F_Fphi_Fphiphi_max'][0]/(np.sqrt(3)*w*w)) for w in [.0005,.001]}
args.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if 'coefficients' not in k}),flush=True)
print(json.dumps(dict(output=str(args.out),sha256=h.sha(args.out))),flush=True)
