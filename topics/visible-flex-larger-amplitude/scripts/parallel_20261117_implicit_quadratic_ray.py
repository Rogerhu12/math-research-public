#!/usr/bin/env python3
"""All-row quadratic-ray diagnostic; never solves or changes a Newton run.

analyze(P,Y,U,dY,dU) consumes the frozen Pr Problem API. The CLI either uses
a declared non-Newton smooth fixture or two adjacent saved algebraic iterates.
The latter gives a rounded-update secant, not the original Newton direction.
"""
import argparse,gzip,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np

PROBLEM_SHA='5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac'
GROUPS=('nodes','middle','boundary')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def binary_sha(*a):
 h=hashlib.sha256()
 for z in a:h.update(np.asarray(z,dtype='<f8',order='C').tobytes())
 return h.hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))
def dot(a,b):return np.sum(np.asarray(a,dtype=np.longdouble)*np.asarray(b,dtype=np.longdouble),dtype=np.longdouble)
def maximum(a):return float(np.max(np.abs(a)))

def local_terms(P,y,u,dy,du,k):
 _,d,e=P.q.jet(y);v=P.q.jet(u)[0]
 _,dd,de=P.q.jet(dy);dv=P.q.jet(du)[0]
 linear=np.c_[np.sum(dv*d+v*dd,axis=1),
              np.sum(dv*e+v*de+2*k*d*dd,axis=1),2*np.sum(v*dv,axis=1)]
 quadratic=np.c_[np.sum(dv*dd,axis=1),
                 np.sum(dv*de+k*dd*dd,axis=1),np.sum(dv*dv,axis=1)]
 return P.operator.project(linear),P.operator.project(quadratic)

def terms(P,Y,U,dY,dU):
 ym,um=P.midpoint(Y,U);dym,dum=P.midpoint(dY,dU)
 j={};q={}
 for name,ys,us,dys,dus,ks in (
   ('nodes',Y,U,dY,dU,P.k),('middle',ym,um,dym,dum,P.km)):
  j[name]=np.empty_like(ys);q[name]=np.empty_like(ys)
  for i in range(len(ys)):j[name][i],q[name][i]=local_terms(P,ys[i],us[i],dys[i],dus[i],ks[i])
 j['boundary']=P.BA@dY[0]+P.BB@dY[-1];q['boundary']=np.zeros(P.n)
 return j,q

def complex_direction(P,Y,U,dY,dU,eps=1e-25):
 # A separate evaluation of EVERY residual, without any Jacobian assembly.
 ym,um=P.midpoint(Y.astype(complex)+1j*eps*dY,U.astype(complex)+1j*eps*dU)
 j={}
 for name,ys,us,ks in (
   ('nodes',Y.astype(complex)+1j*eps*dY,U.astype(complex)+1j*eps*dU,P.k),
   ('middle',ym,um,P.km)):
  j[name]=np.array([P.operator.residual(y,u,k).imag/eps for y,u,k in zip(ys,us,ks)])
 j['boundary']=P.boundary(Y.astype(complex)+1j*eps*dY).imag/eps
 return j

def analyze(P,Y,U,dY,dU,alphas=(1.,.5,.25),original_linear=None):
 started=time.perf_counter()
 if any(z.shape!=(P.m,P.n)or not np.isfinite(z).all()for z in (Y,U,dY,dU)):raise ValueError('Every finite Y/U direction slot is required')
 r=P.residual(Y,U)
 if not r['finite']:raise ValueError('Nonfinite base residual')
 j,q=terms(P,Y,U,dY,dU);jc=complex_direction(P,Y,U,dY,dU)
 if not all(np.isfinite(z[g]).all()for z in (j,q,jc)for g in GROUPS):raise ValueError('Nonfinite full directional residual')
 rr=sum(dot(r[g],r[g])for g in GROUPS);rj=sum(dot(r[g],j[g])for g in GROUPS)
 jj=sum(dot(j[g],j[g])for g in GROUPS);rq=sum(dot(r[g],q[g])for g in GROUPS)
 jq=sum(dot(j[g],q[g])for g in GROUPS);qq=sum(dot(q[g],q[g])for g in GROUPS)
 c=np.array([rr,2*rj,jj+2*rq,2*jq,qq],dtype=np.longdouble)
 e={g:r[g]+j[g]for g in GROUPS};escale=max(maximum(r[g])for g in GROUPS)
 jnorm=sum(dot(j[g],j[g])for g in GROUPS)
 jerror=sum(dot(j[g]-jc[g],j[g]-jc[g])for g in GROUPS)
 check=[]
 for a in alphas:
  direct=P.residual(Y+a*dY,U+a*dU)
  if not direct['finite']:check.append(dict(alpha=float(a),finite=False));continue
  predicted={g:r[g]+a*j[g]+a*a*q[g]for g in GROUPS}
  pnorm=sum(dot(predicted[g],predicted[g])for g in GROUPS)
  check.append(dict(alpha=float(a),finite=True,direct_raw_SSE=direct['cost'],
    predicted_vector_SSE=float(pnorm),quartic_SSE=float(np.polynomial.polynomial.polyval(np.longdouble(a),c)),
    full_residual_identity_max_by_group={g:maximum(direct[g]-predicted[g])for g in GROUPS},
    direct_Armijo_accepted=bool(direct['cost']<(1-.4*a)*r['cost'])))
 blocks=[];slices=(slice(0,P.M),slice(P.M,2*P.M+1),slice(2*P.M+1,P.n))
 for name in ('nodes','middle'):
  for b,s in enumerate(slices):
   z,t,v=r[name][:,s],j[name][:,s],q[name][:,s]
   blocks.append(dict(group=name,row=b,count=z.size,r_square=float(dot(z,z)),r_dot_q=float(dot(z,v)),
                     j_dot_q=float(dot(t,v)),q_square=float(dot(v,v)),q_max=maximum(v)))
 blocks.append(dict(group='boundary',count=P.n,r_square=float(dot(r['boundary'],r['boundary'])),
                    r_dot_q=0.,j_dot_q=0.,q_square=0.,q_max=0.))
 gates=[]
 for index in range(17):
  a=np.longdouble(2.**(-index));value=np.polynomial.polynomial.polyval(a,c)
  # alpha*gate is S(alpha)-(1-.4alpha)S(0), computed without that subtraction.
  gate=.4*rr+c[1]+a*(c[2]+a*(c[3]+a*c[4]))
  gates.append(dict(index=index,alpha=float(a),predicted_SSE=float(value),Armijo_cubic_gate=float(gate),
                    predicted_original_gate=bool(gate<0)))
 factor_match=None if original_linear is None else original_linear.get('factor_state_sha256')==binary_sha(Y,U)
 return dict(schema='complete-Pr-quadratic-ray-diagnostic-v1',source_sha256=sha(__file__),
  M=P.M,N=P.N,nodes=P.m,node_rows=P.m*P.n,midpoint_rows=(P.m-1)*P.n,boundary_rows=P.n,
  total_residual_rows=2*P.m*P.n,mesh_scalar_boundary_sha256=binary_sha(P.x,P.k,P.km,P.BA,P.BB,P.target),
  base_YU_sha256=binary_sha(Y,U),direction_sha256=binary_sha(dY,dU),
  residual_linear_quadratic_sha256=binary_sha(*(z[g]for z in (r,j,q)for g in GROUPS)),
  base_summary=P.summary(r),raw_SSE_quartic_coefficients=[float(z)for z in c],
  moments=dict(r_square=float(rr),r_dot_j=float(rj),j_square=float(jj),r_dot_q=float(rq),j_dot_q=float(jq),q_square=float(qq)),
  current_linear_defect_max_by_group={g:maximum(e[g])for g in GROUPS},
  current_linear_defect_relative_max=max(maximum(e[g])for g in GROUPS)/max(escale,np.finfo(float).tiny),
  current_linear_defect_L2=float(np.sqrt(sum(dot(e[g],e[g])for g in GROUPS))),
  all_row_complex_step_max_by_group={g:maximum(j[g]-jc[g])for g in GROUPS},
  all_row_complex_step_relative_L2=float(np.sqrt(jerror/max(jnorm,np.longdouble(np.finfo(float).tiny)))),
  direct_vector_checks=check,disjoint_block_moments=blocks,original_17_dyadic_predictions=gates,
  original_linear_report=original_linear,reported_factor_matches_base=factor_match,
  newton_or_linear_solve_executed=False,policy_changed=False,physical_acceptance_claimed=False,
  arithmetic='Ordinary binary64 jets/FFTs, long-double dot accumulation, float JSON; no interval certificate.',
  interpretation='R336 quartic expansion applied to the EXACT fixed Pr quadratic map; direct floating evaluations still have rounding discrepancy.',
  seconds=time.perf_counter()-started)

def main(a):
 if sha(a.problem_source)!=PROBLEM_SHA:raise ValueError('Not frozen 5b965 Problem source')
 p=load(a.problem_source,'ray_problem');scripts=a.topic/'scripts';sys.path.insert(0,str(scripts))
 hp=scripts/'parallel_20261117_negative_hold_profile_ivp.py';fs=scripts/'parallel_20261117_frenet_symbol.py'
 identities={str(a.problem_source):PROBLEM_SHA,str(a.warm):p.WARM_SHA,str(a.polynomial_source):p.POLYNOMIAL_SHA,
  str(hp):p.HOLD_SHA,str(fs):p.FRENET_SHA,str(scripts/'parallel_20261117_profile.py'):p.PROFILE_SHA,
  str(scripts/'parallel_20261117_inward_profile.py'):p.INWARD_SHA}
 p.assert_sources(identities)
 P=p.Problem(read(a.warm),load(fs,'ray_fs'),load(hp,'ray_hp'),load(a.polynomial_source,'ray_poly'))
 original=None;provenance={}
 if a.base is not None:
  if a.next is None:raise ValueError('--base needs --next')
  b,c=read(a.base),read(a.next)
  for z in (b,c):
   if z['source_sha256']!=PROBLEM_SHA or not np.array_equal(z['mesh'],P.x):raise ValueError('Wrong checkpoint source/mesh')
  if len(c['history'])!=len(b['history'])+1 or c['history'][:-1]!=b['history']:raise ValueError('Need consecutive saved history')
  last=c['history'][-1]
  if not last['accepted']:raise ValueError('Next checkpoint must be an accepted algebraic iterate')
  alpha=last['alpha'];Y=np.array(b['states']);U=np.array(b['independent_velocities'])
  yn=np.array(c['states']);un=np.array(c['independent_velocities']);dY=(yn-Y)/alpha;dU=(un-U)/alpha
  original=last['linear'];provenance=dict(kind='rounded-update secant; NOT the original Newton direction',
   base_sha256=sha(a.base),next_sha256=sha(a.next),accepted_alpha=alpha,accepted_iteration=last['iteration'],
   restored_next_max=max(maximum(Y+alpha*dY-yn),maximum(U+alpha*dU-un)))
  alphas=(1.,.5,.25,alpha)
 else:
  if a.next is not None:raise ValueError('--next needs --base')
  Y,U=P.Y.copy(),P.U.copy();nu=np.r_[P.q.freq,P.q.freq[1:],P.q.freq]
  j=np.arange(P.n);phase=P.x[:,None]*(1+j%7)[None,:]+.37*j[None,:]
  dY=1e-4*np.cos(phase)/(1+nu[None,:]**2);dU=1e-4*np.sin(phase+.23)/(1+nu[None,:])
  provenance=dict(kind='declared smooth full-slot NON-NEWTON fixture',formula='dY=1e-4 cos(s*(1+j%7)+.37j)/(1+nu_j^2); dU=1e-4 sin(s*(1+j%7)+.37j+.23)/(1+nu_j)')
  alphas=(1.,.5,.25)
 out=analyze(P,Y,U,dY,dU,alphas,original);out.update(identities=identities,ray_provenance=provenance)
 p.assert_sources(identities);a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
 print(json.dumps(dict(output=str(a.out),sha256=sha(a.out),seconds=out['seconds'],provenance=provenance,
  jvp_relative=out['all_row_complex_step_relative_L2'],checks=out['direct_vector_checks']),allow_nan=False),flush=True)

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for name in ('topic','problem-source','warm','polynomial-source','out'):a.add_argument('--'+name,type=Path,required=True)
 a.add_argument('--base',type=Path);a.add_argument('--next',type=Path);main(a.parse_args())
