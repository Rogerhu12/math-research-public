#!/usr/bin/env python3
"""One true full-ODE shooting trial from the actual linear fast-space step.

The finite BC acceptance gate is max absolute right/left residual <=1e-13.
This file does not turn an IVP or a finite BVP into a completed C2 prefix.
"""
import argparse,gzip,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853

p=argparse.ArgumentParser(description=__doc__)
for key in ('topic','field','local-report','arrays','response','out'):p.add_argument('--'+key,type=Path,required=True)
p.add_argument('--max-step',type=float,default=.000015625)
p.add_argument('--bc-tolerance',type=float,default=1e-13)
args=p.parse_args();helper=args.topic/'notes/2026-11-17-parallel-geometry-frenet-schur.py'
spec=importlib.util.spec_from_file_location('fast_shooting_helper',helper)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
base=json.loads(gzip.decompress(args.field.read_bytes()));definition=json.loads(args.local_report.read_text())
linear=json.loads(args.response.read_text());cache=np.load(args.arrays)
if h.sha(args.arrays)!=definition['arrays_sha256'] or h.sha(args.field)!=definition['reference_sha256']:
 raise ValueError('The fixed boundary definition does not match its reference')
q=h.Frenet(base['M'],base['N']);profile=h.profile_from(base)
U,L,target,T0,Qfast=[cache[k] for k in ('U','L','target','T0','Qfast')]
delta=np.array(linear['initial_delta_coefficients']);eta=Qfast.T@(T0@delta)
y0=np.array(base['states'][0])+U@eta;y1=np.array(base['states'][-1])
begin=float(base['start']);end=float(base['end']);started=time.perf_counter()
stats=dict(rhs_calls=0,stage_min_Q=float('inf'),stage_min_W=float('inf'),stage_min_H=float('inf'))
bad=None
def rhs(s,y):
 global bad
 a,ap,_=profile(s);k=ap/a;stats['rhs_calls']+=1
 try:z=q.local(y,k)
 except FloatingPointError:
  _,d,e=q.jet(y);Q=np.sum(d*d,axis=1);W=np.sum(np.cross(d,e)**2,axis=1);H=W-k*k*Q**3
  bad=dict(s=float(s),Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H.min()))
  raise
 for key in ('Q','W','H'):stats['stage_min_'+key]=min(stats['stage_min_'+key],float(z[key].min()))
 return q.project(z['V'])
mesh=[begin];states=[y0.copy()];failure=None
try:
 sol=DOP853(rhs,begin,y0,end,rtol=1e-13,atol=1e-16,first_step=args.max_step,max_step=args.max_step)
 while sol.status=='running':
  sol.step()
  if sol.t>mesh[-1]:mesh.append(float(sol.t));states.append(sol.y.copy())
 reached=sol.status=='finished'
except FloatingPointError as exc:reached=False;failure=str(exc)
raw_count=len(mesh);removed=[]
if reached:
 while len(mesh)>2 and mesh[-1]-mesh[-2]<64*abs(np.spacing(mesh[-1])):
  removed.append(mesh[-2]);del mesh[-2];del states[-2]
states=np.array(states);mesh=np.array(mesh);velocities=[];accelerations=[]
node_min=dict(Q=float('inf'),W=float('inf'),H=float('inf'))
for s,y in zip(mesh,states):
 a,ap,app=profile(s);k=ap/a;v=q.rhs(y,k)
 velocities.append(v);accelerations.append(q.jvp(y,k,v,dk=app/a-k*k))
 z=q.local(y,k)
 for key in node_min:node_min[key]=min(node_min[key],float(z[key].min()))
right=L@(states[-1]-y1)-target
left=T0@(states[0]-np.array(base['states'][0]));left-=Qfast@(Qfast.T@left)
right_max=float(abs(right).max());left_max=float(abs(left).max())
accepted=reached and max(right_max,left_max)<=args.bc_tolerance
report=dict(scope=__doc__,source_sha256=h.sha(__file__),helper_sha256=h.sha(helper),
 reference_sha256=h.sha(args.field),local_report_sha256=h.sha(args.local_report),response_sha256=h.sha(args.response),
 arrays_sha256=h.sha(args.arrays),M=q.M,N=q.N,start=begin,end=end,last_accepted=float(mesh[-1]),
 ivp_reached_end=reached,bvp_accepted=accepted,bc_tolerance=args.bc_tolerance,
 right_residual_max=right_max,right_residual_norm=float(np.linalg.norm(right)),left_residual_max=left_max,
 baseline_target_max=float(abs(target).max()),right_to_baseline_ratio=right_max/float(abs(target).max()),
 rtol=1e-13,atol=1e-16,max_step=args.max_step,raw_nodes=raw_count,clean_nodes=len(mesh),
 removed_terminal_nodes=removed,accepted_node_domain_min=node_min,failed_stage=bad,failure=failure,
 seconds=time.perf_counter()-started,**stats)
result=dict(base);result.update(mesh=mesh.tolist(),states=states.tolist(),rhs=np.asarray(velocities).tolist(),
 d2=np.asarray(accelerations).tolist(),initial_free_coordinates=eta.tolist(),ivp_reached_end=reached,
 bvp_accepted=accepted,complete_prefix=False,actual_C2_join_completed=False,finite_shooting_definition=report)
args.out.write_bytes(gzip.compress(json.dumps(result,separators=(',',':')).encode(),mtime=0))
report['field_sha256']=h.sha(args.out);report_path=Path(str(args.out)+'.report.json')
report_path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report),flush=True);print(json.dumps(dict(report_sha256=h.sha(report_path))),flush=True)
