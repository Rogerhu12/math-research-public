#!/usr/bin/env python3
"""Local/frozen-frame budgets for actual initial fast-right directions.

Neither matrix below is the full varying-reference propagator.  No BVP is
solved, and the old normal-only 317-column response is not reused.
"""
import argparse,gzip,importlib.util,json
from pathlib import Path
import numpy as np
from scipy.linalg import eigvals,expm,solve,svdvals

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--topic',type=Path,required=True);p.add_argument('--field',type=Path,required=True)
p.add_argument('--out',type=Path,required=True);p.add_argument('--arrays',type=Path,required=True)
args=p.parse_args()
helper=args.topic/'notes/2026-11-17-parallel-geometry-frenet-schur.py'
spec=importlib.util.spec_from_file_location('fast_local_helper',helper)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
d=json.loads(gzip.decompress(args.field.read_bytes()))
if not d.get('ivp_reached_end'):raise ValueError('A successful reference segment is required')
q=h.Frenet(d['M'],d['N']);reader=h.Frenet(q.M,8192);profile=h.profile_from(d)
x=np.array(d['mesh']);ys=np.array(d['states']);dy=np.array(d['rhs']);ddy=np.array(d['d2'])
free=q.M-3;fixed=q.n-free
def frame(i):
 _,t,_=q.jet(ys[i]);v,dv,_=q.jet(dy[i]);acc,_,_=q.jet(ddy[i]);cross=np.cross(v,t)
 area=np.linalg.norm(cross,axis=1)
 T,Ts=h.moving_frame_map(q,dict(d=t,V=v,dV=dv,Acc=acc,normal=cross/area[:,None],area=area))
 a,ap,_=profile(x[i]);A=q.jacobian(ys[i],ap/a)
 return T,Ts,A,solve(T.T,(T@A+Ts).T).T
T0,Ts0,A0,B0=frame(0);T1,Ts1,A1,B1=frame(-1)
def selected(B,right):
 ev=np.sort(eigvals(B).real);lo,hi=float(ev[-free-1]),float(ev[-free])
 if hi-lo<1e-8:raise ValueError('No separated required-dimensional real-part block')
 info,rows=h.selected_left(B.T if right else B,lambda re:re>(lo+hi)/2,q.M,None)
 if info['dimension']!=free:raise ValueError('Cannot split a real Schur block')
 return {k:v for k,v in info.items() if k!='modal_energy'},rows,dict(lower=lo,upper=hi,gap=hi-lo)
info0,R0,gap0=selected(B0,True);info1,LB1,gap1=selected(B1,False);Q0=R0.T
U=solve(T0,Q0);L=LB1@T1;S0=Q0.T@B0@Q0
tail=np.zeros(q.n);m=np.arange(225,q.M+1)
tail[m]=ys[-1,m];tail[q.M+m]=ys[-1,q.M+m];tail[2*q.M+1+m]=ys[-1,2*q.M+1+m]
target=-L@tail;Et=expm((x[-1]-x[0])*S0)
a,ap,app=profile(x[0]);k=ap/a;kp=app/a-k*k
core=np.asarray(d['original_core_coefficients'])
rho=1+np.cos(reader.angle[:,None]*reader.freq[None,1:])@((1-reader.freq[1:]**2)*core)
def norms(v):return [float(np.linalg.norm(z,axis=1).max()) for z in reader.jet(v)]
def domain(y):
 _,t,e=reader.jet(y);Q=np.sum(t*t,axis=1);W=np.sum(np.cross(t,e)**2,axis=1);H=W-k*k*Q**3
 return dict(Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H.min()))
out=dict(scope=__doc__,source_sha256=h.sha(__file__),helper_sha256=h.sha(helper),
         reference_sha256=h.sha(args.field),start=float(x[0]),end=float(x[-1]),M=q.M,N=q.N,
         fixed_left_count=fixed,free_left_count=free,
         initial_fast_gap=gap0,terminal_fast_gap=gap1,initial_right_Schur=info0,terminal_left_Schur=info1,
         initial_right_invariance_relative=float(np.linalg.norm(B0@Q0-Q0@S0)/(np.linalg.norm(B0)*np.linalg.norm(Q0))),
         right_target_max=float(np.max(abs(target))),right_target_norm=float(np.linalg.norm(target)),cases=[])
matrices=[('local_original_coefficients_L1_Ufast',L@U),
          ('frozen_moving_B0_not_actual_Phi',LB1@Q0@Et)]
for label,K in matrices:
 sigma=svdvals(K);eta=solve(K,target);delta=U@eta
 yc=ys[0]+1j*1e-24*delta
 second=q.jvp(yc,k,q.rhs(yc,k),dk=kp).imag/1e-24
 row=dict(model=label,condition_2=float(sigma[0]/sigma[-1]),sigma_max=float(sigma[0]),sigma_min=float(sigma[-1]),
          residual_norm=float(np.linalg.norm(K@eta-target)),initial_F_Fphi_Fphiphi_max=norms(delta),
          initial_linear_radial_first_max=norms(A0@delta)[0],initial_linear_radial_second_max=norms(second)[0],
          initial_coeff_max=float(np.max(abs(delta))),initial_delta_coefficients=delta.tolist(),
          initial_complement_residual_norm=float(np.linalg.norm(T0@delta-Q0@(Q0.T@T0@delta))),
          actual_trial_initial_domain=domain(ys[0]+delta))
 if row['actual_trial_initial_domain']['H_min']>0:
  velocity=q.rhs(ys[0]+delta,k);acc=q.jvp(ys[0]+delta,k,velocity,dk=kp)
  _,t,_=reader.jet(ys[0]+delta);V,_,_=reader.jet(velocity)
  er=np.sum(V*V,axis=1)-1;gr=np.sum(t*t,axis=1)/(a*rho)**2-1;cr=np.sum(V*t,axis=1)/(a*rho)
  gram=(abs(er+gr)+np.sqrt((er-gr)**2+4*cr*cr))/2
  row['actual_trial_initial_Gram']=float(gram.max())
  row['actual_old_prefix_radial_jumps']=[norms(velocity-np.array(d['old_cut_jets']['first']))[0],
                                          norms(acc-np.array(d['old_cut_jets']['second']))[0]]
  row['actual_change_from_reference_radial_jets']=[norms(velocity-dy[0])[0],norms(acc-ddy[0])[0]]
 out['cases'].append(row);print(json.dumps({k:v for k,v in row.items() if k!='initial_delta_coefficients'}),flush=True)
np.savez_compressed(args.arrays,U=U,L=L,target=target,T0=T0,Qfast=Q0)
out['arrays_sha256']=h.sha(args.arrays);out['arrays_path']=str(args.arrays)
args.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(output=str(args.out),sha256=h.sha(args.out),initial_fast_gap=gap0)),flush=True)
