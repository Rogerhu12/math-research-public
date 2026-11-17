#!/usr/bin/env python3
"""Repair only the initial mesh coverage of the frozen HoldProfile BVP.

Start from the original prepared reference, never the failed 1396-node
iterate. Preserve all old jets. New tail nodes evaluate the same original
quadratic true-interface reference. Bisect the union of cells failing any
actual midpoint/Lobatto RMS point, within the unchanged 1800-node budget.
No Newton, QR, ODE continuation, new target or equation change is allowed.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
import scipy.integrate._bvp as backend
from parallel_20261117_frenet_symbol import Frenet
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def project(v,old,M):
 v=np.asarray(v);return np.r_[v[:M+1],v[old+1:old+M+1],v[2*old+1:2*old+M+2]]
def main(a):
 start=time.perf_counter();expected={a.warm:'7feed9f91f60a28d42a0bce352d742804bf11f9b9e5dd567ea5ad871eacebe74',a.interface:'a425e38ed4caeebf4d1f96629721c2ba1f54d72eef863ac278e7fb64f0327ba8',
  a.arrays:'54ee88a8d6d44307431e3ee35dabbc8c907631cfb62512b9bd8b5f59a94260ba',a.hold_source:'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'}
 for p,s in expected.items():
  if sha(p)!=s:raise ValueError('Original reference/targets/source changed: '+str(p))
 d=json.loads(gzip.decompress(a.warm.read_bytes()));ivp=json.loads(gzip.decompress(a.interface.read_bytes()))
 if not d.get('preparation_only') or not ivp.get('ivp_reached_end'):raise ValueError('Need the original prepared reference and true interface')
 spec=importlib.util.spec_from_file_location('frozen_hold_cover',a.hold_source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 profile=m.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin']);q=Frenet(160,2048);audit=Frenet(160,8192)
 if profile.spec()!=d['hold_scalar_profile']:raise ValueError('Different scalar g')
 x=np.array(d['mesh']);Y=np.array(d['states']);V=np.array(d['warm_quintic_first']);A=np.array(d['warm_quintic_second']);oldx=x.copy();oldY=Y.copy();oldV=V.copy();oldA=A.copy()
 cut=float(ivp['mesh'][-1]);y0,v0,a0=[project(ivp[k][-1],ivp['M'],q.M)for k in ('states','rhs','d2')];j=int(np.searchsorted(x,cut))
 if x[j]!=cut or any(not np.array_equal(z[j],v)for z,v in zip((Y,V,A),(y0,v0,a0))):raise ValueError('Original true-interface jets differ')
 def domain(y,s):
  r,ap,_=profile(float(s));_,t,e=audit.jet(y);Q=np.sum(t*t,axis=1);W=np.sum(np.cross(t,e)**2,axis=1);H=W-(ap/r)**2*Q**3
  return np.array([Q.min(),W.min(),H.min()])
 layers=[];reason=None;passed=False
 while True:
  F=[];node_low=np.full(3,np.inf);node_bad=[]
  for j,(s,y)in enumerate(zip(x,Y)):
   val=domain(y,s);node_low=np.minimum(node_low,val);r,ap,_=profile(float(s))
   if min(val)<=0:node_bad.append(j)
   try:F.append(q.rhs(y,ap/r))
   except FloatingPointError:F.append(np.full(q.n,np.nan));node_bad.append(j)
  F=np.array(F);delta=V-F;rel=delta/(1+abs(F));h=np.diff(x);mid=x[:-1]+.5*h;off=.5*h*np.sqrt(3/7);groups=[];union=set()
  if not node_bad:
   spline=backend.create_spline(Y.T,F.T,x,h)
   for name,times in (('midpoint',mid),('RMS_left',mid-off),('RMS_right',mid+off)):
    ys=spline(times).T;bad=[];lo=np.full(3,np.inf);where=None
    for j,(s,y)in enumerate(zip(times,ys)):
     val=domain(y,s)
     if val[2]<lo[2]:where=dict(cell=j,s=float(s))
     lo=np.minimum(lo,val)
     if min(val)<=0:bad.append(j);union.add(j)
    groups.append(dict(kind=name,QWH_lower=lo.tolist(),H_location=where,invalid_cells=bad,invalid_count=len(bad)))
  row=dict(layer=len(layers),nodes=len(x),node_QWH_lower=node_low.tolist(),invalid_node_indices=sorted(set(node_bad)),groups=groups,invalid_union_count=len(union),
   node_complete_ODE_defect=float(np.max(abs(delta))),node_relative_component_defect=float(np.max(abs(rel))),node_relative_vector_rms=float(np.sqrt(np.mean(rel*rel,axis=1)).max()))
  layers.append(row);print(json.dumps(dict(event='all_solver_point_mesh_preparation',**row)),flush=True)
  if node_bad:reason='The unchanged reference has an invalid actual node';break
  if not union:reason='All original midpoint and both RMS evaluation points pass on the angular audit grid';passed=True;break
  if any(x[j]<cut for j in union):reason='A failing cell lies outside the authorized quadratic tail';break
  if len(x)+len(union)>1800:reason='Bisecting every remaining bad cell requires more than the original 1800-node budget';break
  newx=np.array([(x[j]+x[j+1])/2 for j in sorted(union)]);dt=newx-cut
  ny=y0+dt[:,None]*v0+.5*dt[:,None]**2*a0;nv=v0+dt[:,None]*a0;na=np.broadcast_to(a0,ny.shape)
  order=np.argsort(np.r_[x,newx]);x=np.r_[x,newx][order];Y=np.r_[Y,ny][order];V=np.r_[V,nv][order];A=np.r_[A,na][order]
 indices=np.searchsorted(x,oldx);shared=[bool(np.array_equal(z[indices],v))for z,v in zip((Y,V,A),(oldY,oldV,oldA))]
 if not all(shared):raise ValueError('An original reference jet changed')
 d.update(schema='hold-original-solver-point-coverage-preparation-v1',scope=__doc__,source_sha256=sha(__file__),original_prepared_warm_sha256=sha(a.warm),frozen_boundary_arrays_sha256=sha(a.arrays),
  success=False,preparation_only=True,prepared=passed,bvp_solved=False,mesh=x.tolist(),states=Y.tolist(),warm_quintic_first=V.tolist(),warm_quintic_second=A.tolist(),full_ode_rhs_at_nodes=F.tolist(),
  original_solver_point_coverage=dict(layers=layers,stop_reason=reason,original_jet_arrays_unchanged=shared,budget=1800,passed=passed))
 a.output_warm.write_bytes(gzip.compress((json.dumps(d)+'\n').encode(),mtime=0))
 report=dict(scope=__doc__,source_sha256=sha(__file__),original_warm_sha256=sha(a.warm),true_interface_sha256=sha(a.interface),fixed_arrays_sha256=sha(a.arrays),hold_profile_sha256=sha(a.hold_source),backend_sha256=sha(backend.__file__),
  output_warm_sha256=sha(a.output_warm),layers=layers,stop_reason=reason,original_jet_arrays_unchanged=shared,nodes=len(x),budget=1800,passed=passed,new_BVP_solved=False,seconds=time.perf_counter()-start)
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('warm','interface','arrays','hold-source','output-warm','out'):p.add_argument('--'+k,type=Path,required=True)
 main(p.parse_args())
