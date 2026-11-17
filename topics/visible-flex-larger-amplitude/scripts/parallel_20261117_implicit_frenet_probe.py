#!/usr/bin/env python3
"""Polynomial implicit Frenet residual and one complete-cell condensation.

Only frozen original warm references are read. This is a finite algebraic
experiment, not a BVP solve, accepted parent, continuous certificate, or a
claim that projected constraints equal the original projected explicit RHS.
"""
import argparse,gzip,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np
from scipy.linalg import lu_factor,lu_solve
import scipy.integrate._bvp as backend

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

class PolynomialFrenet:
 def __init__(self,field):
  self.q=field;self.M=field.M;self.N=field.N;self.n=field.n
  if self.N<=8*self.M:raise ValueError('The complete quadratic spectra must fit below Nyquist')
 def project_real(self,value):
  s=np.fft.rfft(value,axis=0)/self.N;f=self.q.freq
  c1=2*s[f,1].real;c2=2*s[f,2].real;c1[0]*=.5;c2[0]*=.5
  return np.r_[-2*s[f[1:],0].imag,c1,c2]
 def project(self,value):
  if np.iscomplexobj(value):return self.project_real(value.real)+1j*self.project_real(value.imag)
  return self.project_real(value)
 def point_residual(self,y,v,k):
  _,d,e=self.q.jet(y);V=self.q.jet(v)[0];Q=np.sum(d*d,axis=1)
  return np.c_[np.sum(V*d,axis=1),np.sum(V*e,axis=1)+k*Q,np.sum(V*V,axis=1)-1]
 def residual(self,y,v,k):return self.project(self.point_residual(y,v,k))
 def coefficient_operator(self,Kp,Km):
  C=(Kp+Km)/2;S=(-1j*Kp+1j*Km)/2;f=np.full(self.M+1,2.);f[0]=1.
  blocks=[]
  for component,kernel,start in ((0,C,0),(1,S,1),(2,C,0)):
   blocks.append(np.vstack((-2*kernel[1:,start:,0,component].imag,
                 f[:,None]*kernel[:,start:,1,component].real,
                 f[:,None]*kernel[:,start:,2,component].real)))
  return np.hstack(blocks)
 def jacobians(self,y,v,k):
  _,d,e=self.q.jet(y);V=self.q.jet(v)[0]
  A=np.zeros((self.N,3,3));B=np.zeros_like(A);C=np.zeros_like(A)
  A[:,0,:]=V;A[:,1,:]=2*k*d;B[:,1,:]=V
  C[:,0,:]=d;C[:,1,:]=e;C[:,2,:]=2*V
  Ah=np.fft.fft(A,axis=0)/self.N;Bh=np.fft.fft(B,axis=0)/self.N;Ch=np.fft.fft(C,axis=0)/self.N
  plus,minus=self.q.plus_indices,self.q.minus_indices
  Kp=Ah[plus]@self.q.Dp[None,:,:,:]+Bh[plus]@self.q.D2p[None,:,:,:]
  Km=Ah[minus]@self.q.Dm[None,:,:,:]+Bh[minus]@self.q.D2m[None,:,:,:]
  return self.coefficient_operator(Kp,Km),self.coefficient_operator(Ch[plus],Ch[minus])

def main(a):
 start=time.perf_counter();source_sha=sha(__file__);scripts=a.topic/'scripts';sys.path.insert(0,str(scripts))
 dependencies={scripts/'parallel_20261117_frenet_symbol.py':'7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831',scripts/'parallel_20261117_negative_hold_profile_ivp.py':'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1',scripts/'parallel_20261117_profile.py':'08b1894ca407a0c49b0de80427c669cafe702ab5878b1abf7b346994138d79b3',scripts/'parallel_20261117_inward_profile.py':'1816ba9f5c9d1c207ba5e502ed5fa37a2f28807c54067cde766ae313df40e3e0',Path(backend.__file__):'59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2'}
 inputs={a.warm:'1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057',a.long_warm:'7feed9f91f60a28d42a0bce352d742804bf11f9b9e5dd567ea5ad871eacebe74',a.rms_report:'2a06e383d44835fb2f44c1da8d2c55fe0ea1f57a690c2b5bc773ed3144a62be5'}
 for path,expected in {**dependencies,**inputs}.items():
  if sha(path)!=expected:raise ValueError('Frozen identity changed: '+str(path))
 fs=load(scripts/'parallel_20261117_frenet_symbol.py','implicit_probe_frenet');hp=load(scripts/'parallel_20261117_negative_hold_profile_ivp.py','implicit_probe_hold')
 d=json.loads(gzip.decompress(a.warm.read_bytes()));profile=hp.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'])
 if profile.spec()!=d['hold_scalar_profile']:raise ValueError('Different fixed HoldProfile')
 M,N=d['M'],d['N'];q=fs.Frenet(M,N);operator=PolynomialFrenet(q);n=q.n
 if (M,N,n,d['left_count'],d['right_count'])!=(160,2048,482,325,157):raise ValueError('All original slots are required')
 x=np.array(d['mesh']);Y=np.array(d['states']);V=np.array(d['full_ode_rhs_at_nodes'])
 rng=np.random.default_rng(647);dy=rng.standard_normal(n)/(1+np.arange(n));dv=rng.standard_normal(n)/(1+np.arange(n));eps=1e-25
 def evaluate(label,s,y,v):
  radius,ap,_=profile(float(s));k=ap/radius;point=operator.point_residual(y,v,k);res=operator.project(point);Jy,Jv=operator.jacobians(y,v,k)
  analytic=Jy@dy+Jv@dv;direct=operator.residual(y.astype(complex)+1j*eps*dy,v.astype(complex)+1j*eps*dv,k).imag/eps
  singular=np.linalg.svd(Jv,compute_uv=False);_,t,e=q.jet(y);velocity=q.jet(v)[0];Q=np.sum(t*t,axis=1);normal=np.cross(t,e);W=np.sum(normal*normal,axis=1);H=W-k*k*Q**3
  return dict(label=label,s=float(s),projected_residual_max=float(np.max(abs(res))),point_residual_max_by_row=np.max(abs(point),axis=0).tolist(),Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H.min()),normal_velocity_min=float(np.sum(normal*velocity,axis=1).min()),velocity_jacobian_singular_min=float(singular[-1]),velocity_jacobian_singular_max=float(singular[0]),velocity_jacobian_condition=float(singular[0]/singular[-1]),jacobian_direction_complex_step_abs=float(np.max(abs(analytic-direct))),jacobian_direction_complex_step_relative=float(np.linalg.norm(analytic-direct)/np.linalg.norm(direct)),all_polynomial_entries_finite=bool(np.isfinite(point).all()and np.isfinite(Jy).all()and np.isfinite(Jv).all()))
 rows=[]
 for target in (1.0066,1.0283496328972757,1.03):
  i=int(np.argmin(abs(x-target)));row=evaluate('original_short_warm_node',x[i],Y[i],V[i]);row['node']=i;rows.append(row);print(json.dumps(row),flush=True)
 # One previously recorded negative-H point, from the original long warm.
 # No failed solver output is opened or used as a parent.
 long=json.loads(gzip.decompress(a.long_warm.read_bytes()));rx=np.array(long['mesh']);ry=np.array(long['states']);rv=np.array(long['full_ode_rhs_at_nodes'])
 prior=json.loads(a.rms_report.read_bytes());entry=next(r for r in prior['runs']if r['input_sha256']==inputs[a.long_warm]);known=next(r for r in entry['rows']if r['kind']=='Lobatto_left');cell=known['invalid_cells'][0];u=known['cell_coordinate'];s=float(rx[cell]+u*(rx[cell+1]-rx[cell]))
 spline=backend.create_spline(ry.T,rv.T,rx,np.diff(rx));row=evaluate('original_long_warm_known_bad_RMS_point',s,spline(s),spline(s,1));row.update(cell=int(cell),cell_coordinate=u,recorded_bad_before_this_probe=True);rows.append(row);print(json.dumps(row),flush=True)
 # Exact node elimination and one full midpoint linearization comparison.
 i=max(0,min(len(x)-2,int(np.searchsorted(x,1.0066))-1));h=float(x[i+1]-x[i]);s=float((x[i]+x[i+1])/2);node=[]
 for j in (i,i+1):
  r,ap,_=profile(float(x[j]));k=ap/r;f=operator.residual(Y[j],V[j],k);fy,fv=operator.jacobians(Y[j],V[j],k);lu=lu_factor(fv);A=-lu_solve(lu,fy);b=-lu_solve(lu,f);node.append((f,fy,fv,A,b))
 ym=(Y[i]+Y[i+1])/2+h*(V[i]-V[i+1])/8;vm=1.5*(Y[i+1]-Y[i])/h-.25*(V[i]+V[i+1]);r,ap,_=profile(s);fm=operator.residual(ym,vm,ap/r);fy,fv=operator.jacobians(ym,vm,ap/r)
 A0,b0=node[0][3:];A1,b1=node[1][3:];eye=np.eye(n)
 left=fy@(.5*eye+h*A0/8)+fv@(-1.5*eye/h-.25*A0)
 right=fy@(.5*eye-h*A1/8)+fv@(1.5*eye/h-.25*A1)
 rhs=-fm-fy@(h*(b0-b1)/8)+fv@(.25*(b0+b1))
 dy0=dy;dy1=dv;dv0=b0+A0@dy0;dv1=b1+A1@dy1
 dym=(dy0+dy1)/2+h*(dv0-dv1)/8;dvm=1.5*(dy1-dy0)/h-.25*(dv0+dv1)
 direct=fm+fy@dym+fv@dvm;condensed=left@dy0+right@dy1-rhs
 condensation=dict(cell=i,left=float(x[i]),right=float(x[i+1]),node_velocity_elimination_residual_max=max(float(np.max(abs(node[j][0]+node[j][1]@yy+node[j][2]@vv)))for j,(yy,vv)in enumerate(((dy0,dv0),(dy1,dv1)))),full_vs_condensed_midpoint_abs=float(np.max(abs(direct-condensed))),full_vs_condensed_midpoint_relative=float(np.linalg.norm(direct-condensed)/np.linalg.norm(direct)),left_block_shape=list(left.shape),right_block_shape=list(right.shape),unchanged_boundary_rows=[325,157],global_system_solved=False)
 for path,expected in {**dependencies,**inputs}.items():
  if sha(path)!=expected:raise ValueError('Frozen dependency/input changed during probe')
 if sha(__file__)!=source_sha:raise ValueError('Source changed during probe')
 out=dict(scope=__doc__,source_sha256=source_sha,dependencies={str(p):v for p,v in dependencies.items()},inputs={str(p):v for p,v in inputs.items()},M=M,N=N,dimension=n,scalar_projection_rows=[M,M+1,M+1],finite_polynomial_system_differs_from_projected_explicit_rhs=True,original_full_boundary_rows_preserved=[325,157],rows=rows,complete_cell_condensation=condensation,BVP_solved=False,accepted_parent=False,continuous_metric_certified=False,seconds=time.perf_counter()-start)
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(condensation),flush=True);print(json.dumps(dict(report=str(a.out),sha256=sha(a.out),seconds=out['seconds'])),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','warm','long-warm','rms-report','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
