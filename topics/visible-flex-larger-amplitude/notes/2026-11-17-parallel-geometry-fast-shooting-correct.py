#!/usr/bin/env python3
"""Bounded full finite shooting corrector with fixed 645/317 boundary rows.

At most three new complete 317-column Jacobians and twelve total IVPs,
including the supplied first trial.  No clipping or small-mode deletion.
"""
import argparse,gzip,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
from scipy.linalg import solve,svdvals

p=argparse.ArgumentParser(description=__doc__)
for key in ('topic','reference','local-report','arrays','initial-trial','out'):p.add_argument('--'+key,type=Path,required=True)
args=p.parse_args();helper=args.topic/'notes/2026-11-17-parallel-geometry-frenet-schur.py'
spec=importlib.util.spec_from_file_location('bounded_shooting_helper',helper)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
base=json.loads(gzip.decompress(args.reference.read_bytes()));definition=json.loads(args.local_report.read_text())
current=json.loads(gzip.decompress(args.initial_trial.read_bytes()));cache=np.load(args.arrays)
if h.sha(args.reference)!=definition['reference_sha256'] or h.sha(args.arrays)!=definition['arrays_sha256']:
 raise ValueError('Fixed boundary provenance mismatch')
if not current.get('ivp_reached_end'):raise ValueError('Need a true completed initial shooting trial')
U,L,target,T0,Qfast=[cache[k] for k in ('U','L','target','T0','Qfast')]
q=h.Frenet(base['M'],base['N']);profile=h.profile_from(base)
ybase=np.array(base['states'][0]);yend=np.array(base['states'][-1]);s0=base['start'];s1=base['end'];tau=s1-s0
eta=np.array(current['initial_free_coordinates']);tolerance=1e-13;step=.000015625
report=dict(scope=__doc__,source_sha256=h.sha(__file__),helper_sha256=h.sha(helper),
 reference_sha256=h.sha(args.reference),local_report_sha256=h.sha(args.local_report),arrays_sha256=h.sha(args.arrays),
 initial_trial_sha256=h.sha(args.initial_trial),bc_tolerance=tolerance,max_new_jacobians=3,max_total_ivps=12,
 total_ivps=1,new_jacobians=0,trials=[current['finite_shooting_definition']],jacobians=[])
def save_report():args.out.with_suffix('.report.json').write_text(json.dumps(report,indent=2)+'\n')
def residual(field):return L@(np.array(field['states'][-1])-yend)-target
def left_residual(free):
 z=T0@(ybase+U@free-ybase)
 return z-Qfast@(Qfast.T@z)
def shoot(free,maxstep,label):
 report['total_ivps']+=1;number=report['total_ivps'];begin=time.perf_counter()
 stats=dict(rhs_calls=0,min_Q=float('inf'),min_W=float('inf'),min_H=float('inf'))
 bad=None;failure=None;mesh=[float(s0)];states=[ybase+U@free]
 def fun(s,y):
  nonlocal bad
  a,ap,_=profile(s);k=ap/a;stats['rhs_calls']+=1
  try:z=q.local(y,k)
  except FloatingPointError:
   _,d,e=q.jet(y);Q=np.sum(d*d,axis=1);W=np.sum(np.cross(d,e)**2,axis=1);H=W-k*k*Q**3
   bad=dict(s=float(s),Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H.min()));raise
  for key in ('Q','W','H'):stats['min_'+key]=min(stats['min_'+key],float(z[key].min()))
  return q.project(z['V'])
 try:
  sol=DOP853(fun,s0,states[0],s1,rtol=1e-13,atol=1e-16,first_step=maxstep,max_step=maxstep)
  while sol.status=='running':
   message=sol.step()
   if sol.t>mesh[-1]:mesh.append(float(sol.t));states.append(sol.y.copy())
   if message is not None:failure=message
  reached=sol.status=='finished'
 except FloatingPointError as exc:reached=False;failure=str(exc)
 raw_count=len(mesh);removed=[]
 if reached:
  while len(mesh)>2 and mesh[-1]-mesh[-2]<64*abs(np.spacing(mesh[-1])):
   removed.append(mesh[-2]);del mesh[-2];del states[-2]
 r=L@(states[-1]-yend)-target;left=left_residual(free)
 row=dict(number=number,label=label,reached_end=reached,last_valid=float(mesh[-1]),right_max=float(abs(r).max()),
          right_norm=float(np.linalg.norm(r)),left_max=float(abs(left).max()),max_step=maxstep,
          raw_nodes=raw_count,clean_nodes=len(mesh),removed_terminal_nodes=removed,failed_stage=bad,
          failure=failure,seconds=time.perf_counter()-begin,**stats)
 field=None
 if reached:
  v=[];acc=[]
  for s,y in zip(mesh,states):
   a,ap,app=profile(s);k=ap/a;yp=q.rhs(y,k);v.append(yp);acc.append(q.jvp(y,k,yp,dk=app/a-k*k))
  field=dict(base);field.update(mesh=mesh,states=np.asarray(states).tolist(),rhs=np.asarray(v).tolist(),
   d2=np.asarray(acc).tolist(),initial_free_coordinates=free.tolist(),ivp_reached_end=True,
   bvp_accepted=False,complete_prefix=False,actual_C2_join_completed=False,finite_shooting_trial=row)
  path=args.out.with_name(args.out.name+f'.trial{number}.json.gz')
  path.write_bytes(gzip.compress(json.dumps(field,separators=(',',':')).encode(),mtime=0))
  row['field_path']=str(path);row['field_sha256']=h.sha(path)
 report['trials'].append(row);save_report();print(json.dumps(dict(event='ivp_trial',**row)),flush=True)
 return field,r,row
def jacobian(field):
 report['new_jacobians']+=1;begin=time.perf_counter();calls=0;defect=0.
 x=np.array(field['mesh']);ys=np.array(field['states']);dy=np.array(field['rhs']);ddy=np.array(field['d2']);coeff=[]
 for i,w in enumerate(np.diff(x)):
  c0=ys[i];c1=w*dy[i];c2=w*w*ddy[i]/2;a=ys[i+1]-c0-c1-c2;b=w*dy[i+1]-c1-2*c2;c=w*w*ddy[i+1]-2*c2
  coeff.append(np.array([c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2]))
 def fun(s,flat):
  nonlocal calls,defect
  i=min(len(x)-2,max(0,int(np.searchsorted(x,s,side='right')-1)));w=x[i+1]-x[i];u=(s-x[i])/w;c=coeff[i]
  y=np.polynomial.polynomial.polyval(u,c);v=np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*c[1:])/w
  a,ap,_=profile(s);k=ap/a;A=q.jacobian(y,k);defect=max(defect,float(abs(v-q.rhs(y,k)).max()));calls+=1
  if calls%200==0:print(json.dumps(dict(event='Jacobian_progress',jacobian=report['new_jacobians'],s=float(s),calls=calls,seconds=time.perf_counter()-begin)),flush=True)
  return (A@flat.reshape(q.n,U.shape[1])).ravel()
 sol=DOP853(fun,s0,U.ravel(),s1,rtol=1e-9,atol=1e-12,first_step=tau/256,max_step=tau/128);nodes=1
 while sol.status=='running':sol.step();nodes+=1
 if sol.status!='finished':raise RuntimeError('Complete variational Jacobian did not finish')
 K=L@sol.y.reshape(q.n,U.shape[1]);sigma=svdvals(K)
 path=args.out.with_name(args.out.name+f'.Jacobian{report["new_jacobians"]}.npz');np.savez_compressed(path,K=K)
 row=dict(number=report['new_jacobians'],condition_2=float(sigma[0]/sigma[-1]),sigma_max=float(sigma[0]),sigma_min=float(sigma[-1]),
          nodes=nodes,calls=calls,reference_ODE_defect_max=defect,seconds=time.perf_counter()-begin,
          matrix_path=str(path),matrix_sha256=h.sha(path))
 report['jacobians'].append(row);save_report();print(json.dumps(dict(event='Jacobian_complete',**row)),flush=True)
 return K
r=residual(current);accepted=False
try:
 for iteration in range(3):
  if max(float(abs(r).max()),float(abs(left_residual(eta)).max()))<=tolerance:break
  K=jacobian(current);change=solve(K,-r);old_merit=float(abs(r).max());improved=False
  for fraction in (1.,.5,.25,.125):
   if report['total_ivps']>=11:break
   candidate,rr,row=shoot(eta+fraction*change,step,f'Newton{iteration+1}_fraction{fraction}')
   if candidate is not None and row['right_max']<old_merit:
    current=candidate;eta=eta+fraction*change;r=rr;improved=True;break
  if not improved:report['stop']='No actual maximum-row decrease within the fixed IVP budget';break
 if max(float(abs(r).max()),float(abs(left_residual(eta)).max()))<=tolerance and report['total_ivps']<12:
  refined,rr,row=shoot(eta,step/2,'final_step_halving')
  if refined is not None and max(row['right_max'],row['left_max'])<=tolerance:
   report['final_step_coefficient_difference_max']=float(np.max(abs(np.asarray(refined['states'][-1])-np.asarray(current['states'][-1]))))
   current=refined;r=rr;accepted=True
except (FloatingPointError,RuntimeError,np.linalg.LinAlgError) as error:report['stop']=str(error)
report.update(bvp_accepted=accepted,right_residual_max=float(abs(r).max()),right_residual_norm=float(np.linalg.norm(r)),
              left_residual_max=float(abs(left_residual(eta)).max()))
current['bvp_accepted']=accepted;current['finite_shooting_definition']=report
args.out.write_bytes(gzip.compress(json.dumps(current,separators=(',',':')).encode(),mtime=0))
report['field_sha256']=h.sha(args.out);save_report()
print(json.dumps(dict(event='complete',**{k:v for k,v in report.items() if k not in ('trials','jacobians')})),flush=True)
