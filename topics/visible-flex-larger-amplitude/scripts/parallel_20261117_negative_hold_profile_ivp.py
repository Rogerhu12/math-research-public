#!/usr/bin/env python3
"""One new scalar: .002 fall to -2.5, .02 hold, .02 rise to +1.5.

The later positive plateau is chosen to finish at angle -pi/2, followed
by a .02 zero-curvature ramp. Exact meridian integrals define the scalar;
Gauss32 evaluates them. The sole IVP retains all 962 equations and starts
from the actual .995 M112 endpoint zero-lifted to M320/N4096.
"""
import argparse,gzip,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853
from parallel_20261117_profile import Profile
from parallel_20261117_inward_profile import smoothstep,primitive
from parallel_20261117_frenet_symbol import Frenet


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


class HoldProfile:
 def __init__(self,geometry,origin,cut=.995,quadrature=32):
  self.base=Profile(geometry,origin);self.cut=float(cut);self.quadrature=quadrature
  self.ac,self.apc,self.appc=self.base(cut);self.alpha0=float(np.arcsin(self.apc));self.kappa0=float(-self.appc/np.cos(self.alpha0))
  self.nodes,self.weights=np.polynomial.legendre.leggauss(quadrature)
  # Each triple is (duration, starting curvature, final curvature).
  first=[(.002,self.kappa0,-2.5),(.02,-2.5,-2.5),(.02,-2.5,1.5)]
  turn=sum(h*(a+b)/2 for h,a,b in first)+.02*1.5/2
  self.plateau=(self.alpha0+np.pi/2-turn)/1.5
  if self.plateau<=0:raise ValueError('Nonpositive closing plateau')
  self.segments=[];start=0.;alpha=self.alpha0;shift=np.zeros(2)
  for h,left,right in first+[(self.plateau,1.5,1.5),(.02,1.5,0.)]:
   segment=dict(start=start,duration=h,left=left,right=right,alpha0=alpha,shift0=shift.copy())
   self.segments.append(segment);shift=shift+self.integral(segment,h);alpha-=h*(left+right)/2;start+=h
  self.end=self.cut+start;self.shift3=shift;self.radius=self.ac+shift[0]
  self.angle_upper=self.alpha0+2.5*(.002+.02+.02)
  if self.angle_upper>=np.pi/2 or self.radius<=0:raise ValueError('Reference leaves the intended chart or crosses the axis')
 def angle(self,seg,t):
  return seg['alpha0']-seg['left']*t-(seg['right']-seg['left'])*seg['duration']*primitive(np.asarray(t)/seg['duration'])
 def integral(self,seg,t):
  if seg['left']==seg['right']:
   k=seg['left'];alpha=self.angle(seg,t)
   if k:return np.array([(np.cos(alpha)-np.cos(seg['alpha0']))/k,(np.sin(seg['alpha0'])-np.sin(alpha))/k])
   return t*np.array([np.sin(alpha),np.cos(alpha)])
  at=self.angle(seg,t*(self.nodes+1)/2);return t/2*np.array([self.weights@np.sin(at),self.weights@np.cos(at)])
 def meridian(self,s):
  u=float(s)-self.cut
  if u<0 or s>self.end+1e-12:raise ValueError('Outside reference extension')
  seg=next((v for v in self.segments if u<=v['start']+v['duration']),self.segments[-1]);t=np.clip(u-seg['start'],0.,seg['duration'])
  alpha=self.angle(seg,t);k=seg['left']+(seg['right']-seg['left'])*smoothstep(t/seg['duration']);shift=seg['shift0']+self.integral(seg,t)
  ap,hs=np.sin(alpha),np.cos(alpha)
  if s==self.end:ap,hs,k=-1.,0.,0.;shift=self.shift3
  return dict(a=float(self.ac+shift[0]),ap=float(ap),app=float(-k*hs),height_increment=float(shift[1]),height_s=float(hs),height_ss=float(k*ap),curvature=float(k),angle=float(alpha))
 def __call__(self,s):
  if s<=self.cut:return self.base(s)
  if s>self.end:
   if s-self.end>=self.radius:raise ValueError('Use Cartesian disk chart at the center')
   return self.radius-(s-self.end),-1.,0.
  p=self.meridian(s);return p['a'],p['ap'],p['app']
 def spec(self):
  return dict(kind='negative-curvature-hold-v1',cut=self.cut,quadrature=self.quadrature,negative_curvature=-2.5,fall=.002,hold=.02,rise=.02,positive_curvature=1.5,ramp_out=.02,
   alpha0=self.alpha0,kappa0=self.kappa0,plateau=self.plateau,end=self.end,planar_radius=float(self.radius),reference_height_increment=float(self.shift3[1]),angle_upper_bound=self.angle_upper,
   definition='On each ramp k=left+(right-left)S(t/h), S=10u^3-15u^4+6u^5; alpha=alpha0-integral k. Positions are exact integrals of sin(alpha),cos(alpha).')


def main(a):
 start_clock=time.perf_counter();parent=json.loads(gzip.decompress(a.parent.read_bytes()))
 if not parent['success'] or parent['M']!=112 or parent['mesh'][-1]!=.995:raise ValueError('Require the actual .995 M112 parent')
 profile=HoldProfile(parent['fixed_scalar_profile']['geometry'],parent['analytic_extension_origin']);q=Frenet(320,4096);old=Frenet(parent['M'],parent['N']);read=Frenet(320,8192)
 def lift(v):
  out=np.zeros(q.n);m=old.M;M=q.M;out[:m+1]=v[:m+1];out[M+1:M+m+1]=v[m+1:2*m+1];out[2*M+1:2*M+m+2]=v[2*m+1:];return out
 initial=lift(np.array(parent['states'][-1]));core=np.pad(np.array(parent['core']['coefficients']),(0,q.M-old.M));_,dcut,_=read.jet(initial);Fcut=read.jet(initial)[0]
 theta=read.angle+np.sin(read.angle[:,None]*read.freq[None,1:])@((1-read.freq[1:]**2)*core/read.freq[1:])
 cp,sp=np.cos(read.angle),np.sin(read.angle);xyz=np.c_[cp*Fcut[:,0]-sp*Fcut[:,1],sp*Fcut[:,0]+cp*Fcut[:,1],Fcut[:,2]]
 H=float(initial[2*q.M+1]+profile.shift3[1]);target=np.c_[profile.radius*np.cos(theta),profile.radius*np.sin(theta),np.full(read.N,H)]
 chord=np.linalg.norm(target-xyz,axis=1);times=np.unique(np.r_[np.linspace(profile.cut,profile.end,2049),[profile.cut+v['start'] for v in profile.segments],profile.end]);reference=[profile.meridian(t)for t in times]
 budget=dict(scope='Reference scalar and sampled fixed-material necessary chord only; not actual future nonaxisymmetric geometry.',parent_sha256=sha(a.parent),source_sha256=sha(__file__),profile=profile.spec(),
  initial_scalar_jet_difference=(np.array(profile(.995))-np.array(profile.base(.995))).tolist(),reference_length=profile.end-profile.cut,reference_max_sample_radius=max(v['a']for v in reference),
  reference_height_from_actual_cut_phi_mean=H,fixed_material_chord_sample_max=float(chord.max()),fixed_material_chord_sample_margin=float(profile.end-profile.cut-chord.max()),
  reference_axis_box_diameter_upper=2*float(np.hypot(max(v['a']for v in reference),H)),actual_core_gap=float(2*np.sum(core[::2])))
 # Radius grows until the unique alpha=0 crossing in the positive plateau.
 seg=profile.segments[3];at_zero=seg['alpha0']/1.5;radius_max=profile.ac+seg['shift0'][0]+profile.integral(seg,at_zero)[0]
 budget['reference_radius_max_from_turn']=float(radius_max);budget['reference_axis_box_diameter_upper']=2*float(np.hypot(radius_max,H))
 a.out.with_suffix('.budget.json').write_text(json.dumps(budget,indent=2)+'\n');print(json.dumps(dict(event='reference_budget',**budget)),flush=True)
 def domain(y,k,qq=q):
  _,d,e=qq.jet(y);Q=np.sum(d*d,axis=1);W=np.sum(np.cross(d,e)**2,axis=1);H=W-k*k*Q**3;j=int(np.argmin(H));allowed=np.sqrt(W/Q**3);ja=int(np.argmin(allowed))
  return dict(N=qq.N,Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H[j]),H_min_angle=float(qq.angle[j]),k=float(k),k_admissible=float(allowed[ja]),k_margin=float(allowed[ja]-abs(k)))
 failure_info={}
 def rhs(s,y):
  r,ap,_=profile(s)
  try:return q.rhs(y,ap/r)
  except FloatingPointError:
   failure_info.update(attempted_time=float(s),attempted_domain=domain(y,ap/r));raise
 solver=DOP853(rhs,.995,initial,1.02,rtol=1e-13,atol=1e-16,first_step=.000015625,max_step=.000015625)
 mesh=[.995];states=[initial.copy()];failure=None
 while solver.status=='running':
  try:message=solver.step()
  except FloatingPointError as error:
   failure=dict(kind='domain_evaluation_error',message=str(error),last_accepted_time=mesh[-1],**failure_info);break
  if solver.t>mesh[-1]:mesh.append(float(solver.t));states.append(solver.y.copy())
  if solver.status=='failed':failure=dict(kind='integrator_failed',message=message,last_accepted_time=mesh[-1]);break
  if len(mesh)%200==0:print(json.dumps(dict(event='progress',s=mesh[-1],nodes=len(mesh),nfev=solver.nfev)),flush=True)
 success=failure is None and solver.status=='finished';integrator_nodes=len(mesh);dropped=[]
 if success:
  while len(mesh)>2 and mesh[-1]-mesh[-2]<64*abs(np.spacing(1.02)):
   dropped.append(mesh[-2]);del mesh[-2];del states[-2]
 velocities=[];accelerations=[]
 for s,y in zip(mesh,states):
  r,ap,app=profile(s);k=ap/r;v=q.rhs(y,k);velocities.append(v);accelerations.append(q.jvp(y,k,v,dk=app/r-k*k))
 ac,apc,appc=profile(.995);oldv=np.array(parent['rhs'][-1]);olda=old.jvp(np.array(parent['states'][-1]),apc/ac,oldv,dk=appc/ac-(apc/ac)**2)
 data=dict(schema='negative-hold-local-common-jets-v1',scope=__doc__,ivp_reached_end=success,bvp_accepted=False,complete_prefix=False,old_prefix_C2_join_completed=False,
  reference_sha256=sha(a.parent),source_sha256=sha(__file__),hold_profile_sha256=sha(__file__),hold_scalar_profile=profile.spec(),fixed_scalar_profile=parent['fixed_scalar_profile'],analytic_extension_origin=parent['analytic_extension_origin'],
  M=q.M,N=q.N,start=.995,requested_end=1.02,end=mesh[-1],rtol=1e-13,atol=1e-16,max_step=.000015625,nfev=solver.nfev,integrator_accepted_nodes=integrator_nodes,dropped_terminal_node_times=dropped,
  failure=failure,mesh=mesh,states=np.array(states).tolist(),rhs=np.array(velocities).tolist(),d2=np.array(accelerations).tolist(),original_core_coefficients=core.tolist(),
  old_cut_jets=dict(value=initial.tolist(),first=lift(oldv).tolist(),second=lift(olda).tolist()),metric_reader_requirement='Use this frozen HoldProfile with hold_scalar_profile; old h.profile_from does not describe this g.')
 field=a.out.with_suffix('.json.gz');field.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0));r,ap,_=profile(mesh[-1]);last=states[-1];lastv=velocities[-1]
 F,t,e=read.jet(last);V=read.jet(lastv)[0];rho=1+np.cos(read.angle[:,None]*read.freq[None,1:])@((1-read.freq[1:]**2)*core)
 er=np.sum(V*V,axis=1)-1;gr=np.sum(t*t,axis=1)/(r*rho)**2-1;fr=np.sum(V*t,axis=1)/(r*rho);metric=(abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2
 report=dict(scope=__doc__,source_sha256=sha(__file__),parent_sha256=sha(a.parent),field_sha256=sha(field),budget_sha256=sha(a.out.with_suffix('.budget.json')),ivp_reached_end=success,bvp_accepted=False,
  M=q.M,N=q.N,dimension=q.n,requested_end=1.02,last_accepted_time=mesh[-1],nodes=len(mesh),nfev=solver.nfev,failure=failure,last_accepted_domain=domain(last,ap/r),last_accepted_audit_domain=domain(last,ap/r,read),last_accepted_RHS_gram=float(metric.max()),seconds=time.perf_counter()-start_clock)
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True);print(json.dumps(dict(output_sha256=sha(a.out))),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--parent',type=Path,required=True);p.add_argument('--out',type=Path,required=True);main(p.parse_args())
