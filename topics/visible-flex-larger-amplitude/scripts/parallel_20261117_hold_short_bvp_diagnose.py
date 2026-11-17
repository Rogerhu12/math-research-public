#!/usr/bin/env python3
"""Read the actual finite Hold BVP output; never solve or change its field.
Domain and ODE extrema below are point samples. The original SciPy RMS rule
is rerun on the saved node values/RHS defining the actual cubic interpolant.
"""
import argparse,gzip,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
import scipy.integrate._bvp as backend
import parallel_20261117_frenet_symbol as fs
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def region(s):
 for b,n in [(0.995,'old_prefix'),(.9955,'original_warm_bridge'),(.997,'remaining_curvature_fall'),(1.017,'negative_curvature_hold'),(1.0283496328972757,'rise_to_true_type_interface')]:
  if s<=b:return n
 return 'explicit_reference_interval'
def coordinate(j,M):
 if j<=M:return ['R',j]
 if j<=2*M:return ['T',j-M]
 return ['Z',j-2*M-1]
def main(a):
 start=time.perf_counter();d=json.loads(gzip.decompress(a.input.read_bytes()))
 if (d['M'],d['N'])!=(160,2048):raise ValueError('Require the actual full M160/N2048 output')
 if sha(a.hold_source)!=d['hold_profile_sha256']:raise ValueError('Different scalar source')
 sp=importlib.util.spec_from_file_location('same_diagnostic_hold',a.hold_source);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
 profile=m.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'])
 if profile.spec()!=d['hold_scalar_profile']:raise ValueError('Different mathematical g')
 x=np.array(d['mesh']);Y=np.array(d['states']).T;F=np.array(d['rhs']).T;h=np.diff(x);mid=x[:-1]+.5*h;off=.5*h*np.sqrt(3/7)
 q=fs.Frenet(d['M'],d['N']);audit=fs.Frenet(d['M'],a.audit_angles);spline=backend.create_spline(Y,F,x,h)
 def fun(s,v,p=None):
  out=np.empty_like(v)
  for j,t in enumerate(s):
   r,ap,_=profile(float(t))
   try:out[:,j]=q.rhs(v[:,j],ap/r)
   except FloatingPointError:out[:,j]=np.nan
  return out
 rows=[]
 for name,ts in [('nodes',x),('midpoint',mid),('RMS_left',mid-off),('RMS_right',mid+off)]:
  vals=spline(ts);der=spline(ts,1);rhs=fun(ts,vals);err=der-rhs;relative=err/(1+abs(rhs));finite=np.all(np.isfinite(err),axis=0)
  stats={}
  for key,array in [('coefficient',abs(err)),('relative_component',abs(relative))]:
   v=np.where(np.isfinite(array),array,-np.inf);j,k=np.unravel_index(v.argmax(),v.shape)
   stats[key]=dict(value=float(v[j,k])if np.isfinite(v[j,k])else None,s=float(ts[k]),point_index=int(k),state=coordinate(int(j),q.M),region=region(float(ts[k])))
  v=np.sqrt(np.sum(relative**2,axis=0));k=int(np.argmax(np.where(np.isfinite(v),v,-np.inf)))
  stats['relative_vector_l2']=dict(value=float(v[k])if np.isfinite(v[k])else None,s=float(ts[k]),point_index=k,region=region(float(ts[k])))
  domains=[]
  for reader in (q,audit):
   low={key:dict(value=np.inf)for key in ('Q','W','H','H_over_W','admissible_k_margin')};bad=[]
   for i,(t,y)in enumerate(zip(ts,vals.T)):
    if not np.isfinite(y).all():bad.append(i);continue
    r,ap,_=profile(float(t));_,v,e=reader.jet(y);Q=(v*v).sum(1);W=(np.cross(v,e)**2).sum(1);H=W-(ap/r)**2*Q**3
    with np.errstate(divide='ignore',invalid='ignore'):arrays=(Q,W,H,H/W,np.sqrt(W/Q**3)-abs(ap/r))
    if not all(np.isfinite(v).all()for v in (Q,W,H))or min(Q.min(),W.min(),H.min())<=0:bad.append(i)
    for key,z in zip(low,arrays):
     if not np.isfinite(z).any():continue
     j=int(np.nanargmin(z))
     if z[j]<low[key]['value']:low[key]=dict(value=float(z[j]),s=float(t),angle=float(reader.angle[j]),point_index=i,region=region(float(t)))
   domains.append(dict(angles=reader.N,minima=low,invalid_count=len(bad),invalid_point_indices=bad))
  rows.append(dict(kind=name,points=len(ts),ODE=stats,nonfinite_rhs_points=int((~finite).sum()),domain=domains))
  print(json.dumps(dict(event='diagnostic_group',kind=name,points=len(ts),ODE=stats,domain_H=[v['minima']['H']for v in domains])),flush=True)
 col,ym,fn,fm=backend.collocation_fun(fun,Y,np.empty(0),x,h)
 rms=backend.estimate_rms_residuals(fun,spline,x,h,np.empty(0),1.5*col/h,fm);saved=np.array(d['rms_residuals']);good=np.isfinite(rms);j=int(np.argmax(np.where(good,rms,-np.inf)))
 pair=np.isfinite(rms)&np.isfinite(saved);rms_data=dict(finite_count=int(good.sum()),nonfinite_count=int((~good).sum()),saved_recomputed_max_difference=float(max(abs(rms[pair]-saved[pair])))if pair.any()else None,
  maximum=dict(value=float(rms[j])if good.any()else None,cell=j,interval=[float(x[j]),float(x[j+1])],midpoint=float(mid[j]),region=region(float(mid[j]))))
 by_region={}
 for label in sorted(set(map(region,mid))):
  ids=np.array([i for i,t in enumerate(mid)if region(float(t))==label]);ii=ids[np.argmax(np.where(good[ids],rms[ids],-np.inf))]
  by_region[label]=dict(cells=len(ids),nonfinite_count=int((~good[ids]).sum()),max_finite=float(rms[ii])if good[ids].any()else None,cell=int(ii),interval=[float(x[ii]),float(x[ii+1])])
 events=[];solves=fresh=0;factor=None
 for line in a.log.read_text().splitlines():
  try:z=json.loads(line)
  except ValueError:continue
  e=z.get('event')
  if e=='single_budget_BVP_start'and z['source_sha256']!=d['source_sha256']:raise ValueError('Log and field sources differ')
  if e=='separated_qr_factor':factor=z;fresh+=1
  elif e=='separated_qr_solve':solves+=1
  elif e in ('accepted_newton','no_descending_trial_old_point_retained','stale_factor_no_descent_refresh'):
   accepted=e=='accepted_newton';trials=int(round(-math.log2(z['alpha'])))+1 if accepted else 17;finite=solves-fresh
   if not 0<=finite<=trials:raise ValueError('Unexpected solver event accounting')
   events.append(dict(event=e,iteration=z['iteration'],nodes=factor['nodes'],alpha=z.get('alpha'),trials=trials,finite_trials=finite,nonfinite_trials=trials-finite,finite_rejected=finite-int(accepted),reduced_condition=factor['reduced_condition'],collocation_max=z.get('collocation_max',z.get('residual_max'))));solves=fresh=0
 report=dict(scope=__doc__,input_sha256=sha(a.input),log_sha256=sha(a.log),source_sha256=sha(__file__),hold_source_sha256=sha(a.hold_source),frenet_sha256=sha(fs.__file__),backend_sha256=sha(backend.__file__),
  solver_success=d['success'],solver_status=d['status'],nodes=len(x),groups=rows,RMS=rms_data,RMS_by_region=by_region,backtracking=events,seconds=time.perf_counter()-start,
  limitation='Finite/nonfinite trial counts follow the frozen callback and solve log; the unlogged angle and Q/W/H values for rejected trials are not reconstructed. No new BVP, parent, whole-quintic geometry or continuum certification is asserted.')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(report=str(a.out),report_sha256=sha(a.out),RMS=rms_data,RMS_by_region=by_region)),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('input','log','hold-source','out'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--audit-angles',type=int,default=8192);main(p.parse_args())
