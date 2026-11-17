#!/usr/bin/env python3
"""One original-budget full HoldProfile BVP, with frozen prepared rows.

All 482 M160/N2048 equations and 325 left/157 right rows are retained.
The prepared warm field is not an accepted parent. Rows, nonzero target,
scalar, first three core coefficients and original domain guards are fixed.
Only the existing fresh-J feasible Newton and complete DiskQR are used.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
import parallel_20261117_frenet_symbol as fs
import parallel_20261117_continue as nonlinear

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main(a):
 start=time.perf_counter();qr_path=a.topic/'computations/geometry_20261114_separated_qr_bvp.py'
 identities={str(a.warm):'7feed9f91f60a28d42a0bce352d742804bf11f9b9e5dd567ea5ad871eacebe74',str(a.arrays):'54ee88a8d6d44307431e3ee35dabbc8c907631cfb62512b9bd8b5f59a94260ba',
  str(a.hold_source):'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1',fs.__file__:'7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831',
  nonlinear.__file__:'8b6960119cd978bb7e6208e87934d68f337b9ba5679314c7c048b6cf0cac80ae',str(qr_path):'c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39'}
 for path,expected in identities.items():
  if sha(path)!=expected:raise ValueError('Frozen problem/source identity changed: '+path)
 d=json.loads(gzip.decompress(a.warm.read_bytes()))
 if not d.get('preparation_only') or not d.get('prepared') or (d['M'],d['N'],d['left_count'],d['right_count'])!=(160,2048,325,157):raise ValueError('Wrong complete prepared problem')
 scalar=load(a.hold_source,'same_hold_BVP_scalar');profile=scalar.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'])
 if profile.spec()!=d['hold_scalar_profile']:raise ValueError('Different scalar g')
 q=fs.Frenet(160,2048);reader=fs.Frenet(160,8192);x=np.array(d['mesh']);y=np.array(d['states']).T
 with np.load(a.arrays)as ar:BA=ar['BA'].copy();BB=ar['BB'].copy();target=ar['target'].copy()
 if BA.shape!=(q.n,q.n) or BB.shape!=BA.shape or target.shape!=(q.n,) or np.any(BA[325:])or np.any(BB[:325]):raise ValueError('Separated full boundary changed')
 if not np.array_equal(BB[325:],np.array(d['terminal_rows'])) or not np.array_equal(target[325:],np.array(d['terminal_target'])):raise ValueError('Target or right rows differ from the warm definition')
 counts=dict(rhs_calls=0,rhs_points=0,jacobian_calls=0,jacobian_points=0,invalid_rhs_points=0)
 def fun(s,Y):
  counts['rhs_calls']+=1;counts['rhs_points']+=len(s);out=np.empty_like(Y)
  for j,t in enumerate(s):
   r,ap,_=profile(float(t))
   try:out[:,j]=q.rhs(Y[:,j],ap/r)
   except FloatingPointError:out[:,j]=np.nan;counts['invalid_rhs_points']+=1
  return out
 def jac(s,Y):
  counts['jacobian_calls']+=1;counts['jacobian_points']+=len(s);begin=time.perf_counter();out=np.empty((q.n,q.n,len(s)))
  for j,t in enumerate(s):
   r,ap,_=profile(float(t));out[:,:,j]=q.jacobian(Y[:,j],ap/r)
  print(json.dumps(dict(event='complete_analytic_jacobian',call=counts['jacobian_calls'],points=len(s),seconds=time.perf_counter()-begin)),flush=True);return out
 def bc(ya,yb):return BA@ya+BB@yb-target
 qr=load(qr_path,'original_complete_disk_QR');work=a.out.with_suffix('.qr-work');qr.enable(work,325,chunk_size=32,checkpoint=str(a.out)+'.checkpoint.gz',M=q.M,N=q.N)
 import scipy.integrate._bvp as backend
 backend.splu=qr.factor;backend.solve_newton=nonlinear.feasible_newton
 print(json.dumps(dict(event='single_budget_BVP_start',M=q.M,N=q.N,dimension=q.n,left=325,right=157,nodes=len(x),start=x[0],end=x[-1],tol=1e-8,bc_tol=1e-11,max_nodes=1800,
  warm_initial_coefficient_defect=.3270395216151608,warm_initial_relative_vector_rms=.027936526188258648,warm_collocation_H_sample_lower=6.545488805882082e-9,
  terminal_Schur_relative_sep_estimate=4.607105234715574e-11,boundary_max=float(max(abs(bc(y[:,0],y[:,-1])))),source_sha256=sha(__file__))),flush=True)
 exception=None
 try:sol=solve_bvp(fun,bc,x,y,fun_jac=jac,bc_jac=lambda ya,yb:(BA,BB),tol=1e-8,bc_tol=1e-11,max_nodes=1800,verbose=2)
 except Exception as e:
  exception=dict(type=type(e).__name__,message=str(e))
  report=dict(scope=__doc__,success=False,exception=exception,source_sha256=sha(__file__),identities=identities,counts=counts,checkpoint=str(a.out)+'.checkpoint.gz',seconds=time.perf_counter()-start)
  a.out.with_suffix('.report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report),flush=True);return
 X=sol.x;Y=sol.y.T;F=fun(X,sol.y).T;A=[];missing=[]
 for j,(s,yy,v)in enumerate(zip(X,Y,F)):
  r,ap,app=profile(float(s));k=ap/r
  try:acc=q.jvp(yy,k,v,dk=app/r-k*k)if np.isfinite(v).all()else np.full(q.n,np.nan)
  except FloatingPointError:acc=np.full(q.n,np.nan)
  if not np.isfinite(acc).all():missing.append(j)
  A.append(acc)
 minima={k:dict(value=np.inf)for k in ('Q','W','H')}
 for s,yy in zip(X,Y):
  r,ap,_=profile(float(s));_,t,e=reader.jet(yy);Q=np.sum(t*t,axis=1);W=np.sum(np.cross(t,e)**2,axis=1);H=W-(ap/r)**2*Q**3
  for key,z in zip(('Q','W','H'),(Q,W,H)):
   j=int(np.argmin(z))
   if z[j]<minima[key]['value']:minima[key]=dict(value=float(z[j]),s=float(s),angle=float(reader.angle[j]))
 core=Y[0,1:q.M+1];rho=1+np.cos(reader.angle[:,None]*reader.freq[None,1:])@((1-reader.freq[1:]**2)*core)
 result=dict(schema='complete-fixed-hold-finite-BVP-v1',scope=__doc__,success=bool(sol.success),status=int(sol.status),message=sol.message,source_sha256=sha(__file__),identities=identities,
  M=q.M,N=q.N,dimension=q.n,left_count=325,right_count=157,tol=1e-8,bc_tol=1e-11,max_nodes=1800,mesh=X.tolist(),states=Y.tolist(),rhs=F.tolist(),d2=np.array(A).tolist(),
  missing_acceleration_node_indices=missing,fixed_scalar_profile=d['fixed_scalar_profile'],analytic_extension_origin=d['analytic_extension_origin'],hold_scalar_profile=profile.spec(),hold_profile_sha256=sha(a.hold_source),
  core=dict(coefficients=core.tolist(),fixed_first_three=d['fixed_core_first_three'],rho_sample_min=float(rho.min()),axis_support_gap=float(2*np.sum(core[::2]))),
  terminal_boundary=dict(M=q.M,fixed_modes=3,rows=BB[325:].tolist(),target=target[325:].tolist(),definition='Frozen moving-frame Schur rows of the exact prepared terminal quadratic reference; nonzero target retained.'),
  boundary_residual_max=float(max(abs(bc(Y[0],Y[-1])))),rms_residuals=sol.rms_residuals.tolist(),max_rms_residual=float(np.max(sol.rms_residuals)),iterations=int(sol.niter),
  node_domain_audit_angles=8192,node_domain_audit=minima,counts=counts,seconds=time.perf_counter()-start,
  limitations='One finite BVP only. A successful solver status does not certify actual whole-quintic geometry, fixed-metric refinement, closedness, reach, or the full time family. A failure is not a new parent.')
 a.out.write_bytes(gzip.compress((json.dumps(result)+'\n').encode(),mtime=0))
 report={k:v for k,v in result.items()if k not in ('mesh','states','rhs','d2','rms_residuals','fixed_scalar_profile','core','terminal_boundary')}
 report.update(nodes=len(X),core={k:v for k,v in result['core'].items()if k not in ('coefficients','fixed_first_three')},field_sha256=sha(a.out));rp=a.out.with_suffix('.report.json');rp.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2),flush=True);print(json.dumps(dict(report_path=str(rp),report_sha256=sha(rp))),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','warm','arrays','hold-source','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
