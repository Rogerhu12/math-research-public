#!/usr/bin/env python3
"""Continue a saved successful true HoldProfile IVP, never a corrected map.

All 962 equations, M320/N4096, rtol=1e-13, atol=1e-16 and the 1/64000
first/max step are unchanged. Recomputed starting rhs and JVP d2 must be
bit-identical to the previous saved jets. The previous trajectory is
preserved exactly and the new true nodes are appended without a duplicate.
Failure preserves the last accepted point but is not an accepted parent.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
import parallel_20261117_frenet_symbol as symbol

HOLD_SHA='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
SYMBOL_SHA='7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main(a):
 start_clock=time.perf_counter();data=json.loads(gzip.decompress(a.input.read_bytes()))
 if not data.get('ivp_reached_end') or data.get('old_prefix_C2_join_completed'):raise ValueError('Require an uncorrected successful true IVP')
 if (data['M'],data['N'])!=(320,4096) or data['rtol']!=1e-13 or data['atol']!=1e-16 or data['max_step']!=1/64000:raise ValueError('Discretization or tolerance changed')
 if sha(a.hold_source)!=HOLD_SHA or data['hold_profile_sha256']!=HOLD_SHA or sha(symbol.__file__)!=SYMBOL_SHA:raise ValueError('Frozen source identity changed')
 spec=importlib.util.spec_from_file_location('same_frozen_hold_scalar',a.hold_source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 profile=module.HoldProfile(data['fixed_scalar_profile']['geometry'],data['analytic_extension_origin'],data['hold_scalar_profile']['cut'],data['hold_scalar_profile']['quadrature'])
 if profile.spec()!=data['hold_scalar_profile']:raise ValueError('The same g was not reconstructed')
 q=symbol.Frenet(320,4096);read=symbol.Frenet(320,8192);begin=float(data['mesh'][-1]);initial=np.array(data['states'][-1])
 if not begin<a.end<=profile.end:raise ValueError('The single requested endpoint must lie after the saved true endpoint')
 r,ap,app=profile(begin);k=ap/r;v0=q.rhs(initial,k);d20=q.jvp(initial,k,v0,dk=app/r-k*k)
 shared=[float(np.max(abs(x-np.array(data[key][-1]))))for x,key in zip((initial,v0,d20),('states','rhs','d2'))]
 if any(shared):raise ValueError('The actual initial jets changed: '+str(shared))
 def domain(y,k,qq=q):
  _,d,e=qq.jet(y);Q=np.sum(d*d,axis=1);W=np.sum(np.cross(d,e)**2,axis=1);H=W-k*k*Q**3;allowed=np.sqrt(W/Q**3);j=int(np.argmin(H));ja=int(np.argmin(allowed))
  return dict(N=qq.N,Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H[j]),H_min_angle=float(qq.angle[j]),k=float(k),k_admissible=float(allowed[ja]),k_margin=float(allowed[ja]-abs(k)))
 failure_info={}
 def rhs(s,y):
  r,ap,_=profile(s)
  try:return q.rhs(y,ap/r)
  except FloatingPointError:
   failure_info.update(attempted_time=float(s),attempted_domain=domain(y,ap/r));raise
 solver=DOP853(rhs,begin,initial,a.end,rtol=1e-13,atol=1e-16,first_step=1/64000,max_step=1/64000)
 mesh=[begin];states=[initial.copy()];failure=None
 while solver.status=='running':
  try:message=solver.step()
  except FloatingPointError as error:
   failure=dict(kind='domain_evaluation_error',message=str(error),last_accepted_time=mesh[-1],**failure_info);break
  if solver.t>mesh[-1]:mesh.append(float(solver.t));states.append(solver.y.copy())
  if solver.status=='failed':failure=dict(kind='integrator_failed',message=message,last_accepted_time=mesh[-1]);break
  if len(mesh)%200==0:print(json.dumps(dict(event='progress',s=mesh[-1],nodes=len(mesh),nfev=solver.nfev)),flush=True)
 success=failure is None and solver.status=='finished';integrator_nodes=len(mesh);dropped=[]
 if success:
  while len(mesh)>2 and mesh[-1]-mesh[-2]<64*abs(np.spacing(a.end)):
   dropped.append(mesh[-2]);del mesh[-2];del states[-2]
 velocities=[];accelerations=[]
 for s,y in zip(mesh,states):
  r,ap,app=profile(s);k=ap/r;v=q.rhs(y,k);velocities.append(v);accelerations.append(q.jvp(y,k,v,dk=app/r-k*k))
 if not np.array_equal(velocities[0],v0) or not np.array_equal(accelerations[0],d20):raise ValueError('The saved joining jets drifted')
 history=dict(input_sha256=sha(a.input),source_sha256=sha(__file__),start=begin,requested_end=a.end,actual_end=mesh[-1],starting_jet_differences=shared,
  previous_nodes=len(data['mesh']),new_nodes=len(mesh),nfev=solver.nfev,integrator_accepted_nodes=integrator_nodes,dropped_terminal_node_times=dropped,failure=failure)
 for key,values in (('mesh',mesh),('states',[v.tolist()for v in states]),('rhs',[v.tolist()for v in velocities]),('d2',[v.tolist()for v in accelerations])):data[key].extend(values[1:])
 data.update(schema='continued-negative-hold-true-common-jets-v1',scope=__doc__,ivp_reached_end=success,bvp_accepted=False,old_prefix_C2_join_completed=False,
  source_sha256=sha(__file__),source_ivp_sha256=sha(a.input),requested_end=a.end,end=mesh[-1],nfev=data.get('nfev',0)+solver.nfev,failure=failure)
 data.setdefault('true_ivp_continuations',[]).append(history)
 field=a.out.with_suffix('.json.gz');field.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0))
 r,ap,_=profile(mesh[-1]);last=states[-1];V=read.jet(velocities[-1])[0];_,t,_=read.jet(last)
 core=np.array(data['original_core_coefficients']);rho=1+np.cos(read.angle[:,None]*read.freq[None,1:])@((1-read.freq[1:]**2)*core)
 er=np.sum(V*V,axis=1)-1;gr=np.sum(t*t,axis=1)/(r*rho)**2-1;fr=np.sum(V*t,axis=1)/(r*rho);metric=(abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2
 report=dict(scope=__doc__,source_sha256=sha(__file__),hold_profile_sha256=HOLD_SHA,input_sha256=sha(a.input),field_sha256=sha(field),ivp_reached_end=success,bvp_accepted=False,
  continuation=history,total_nodes=len(data['mesh']),M=320,N=4096,dimension=962,rtol=1e-13,atol=1e-16,max_step=1/64000,
  last_accepted_domain=domain(last,ap/r),last_accepted_audit_domain=domain(last,ap/r,read),last_accepted_RHS_gram=float(metric.max()),seconds=time.perf_counter()-start_clock)
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True);print(json.dumps(dict(output_sha256=sha(a.out))),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('input','hold-source','out'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--end',type=float,required=True);main(p.parse_args())
