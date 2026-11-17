#!/usr/bin/env python3
"""Read the literal common-two-jet quintic from the failed fixed Pr602 attempt.

Every one of the 601 cells is sampled using its actual polynomial derivatives.
The saved independent U and implicit accelerations define a NEW C2 map; this
is not the solver cubic, an accepted parent, or a continuous metric certificate.
The actual core mirror conditions are inspected literally, never rounded to zero.
"""
import argparse,gzip,hashlib,importlib.util,json,math,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

FIELD='3a7f49623d03a1534a620e3c3d69d7a64c122fc01074b197002bf08de67c294c'
PRODUCER='5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac'
REFERENCE='aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15'
FRENET='7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831'
HOLD='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
PROFILE='08b1894ca407a0c49b0de80427c669cafe702ab5878b1abf7b346994138d79b3'
INWARD='1816ba9f5c9d1c207ba5e502ed5fa37a2f28807c54067cde766ae313df40e3e0'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def literal(v):
 v=np.asarray(v);j=np.flatnonzero(v)
 return dict(nonzero_count=len(j),nonzero_slots=j.tolist(),nonzero_values=v[j].tolist(),maximum_absolute=float(abs(v).max(initial=0.)))
def address(value,cell,u,s,j,angles):return dict(value=float(value),cell=cell,u=float(u),s=float(s),angle_index=int(j),angle=float(angles[j]))
def main(a):
 begin=time.perf_counter();source=sha(__file__);scripts=a.topic/'scripts';sys.path.insert(0,str(scripts))
 identities={a.input:FIELD,a.reference:REFERENCE,scripts/'parallel_20261117_frenet_symbol.py':FRENET,scripts/'parallel_20261117_negative_hold_profile_ivp.py':HOLD,scripts/'parallel_20261117_profile.py':PROFILE,scripts/'parallel_20261117_inward_profile.py':INWARD}
 for p,h in identities.items():
  if sha(p)!=h:raise ValueError('Frozen input/source differs: '+str(p))
 d=json.loads(gzip.decompress(a.input.read_bytes()));ref=json.loads(gzip.decompress(a.reference.read_bytes()))
 if d['source_sha256']!=PRODUCER or d['schema']!='independent-YU-polynomial-Frenet-finite-attempt-v1' or not d['full_Newton_executed'] or d['finite_algebraic_converged'] or d['accepted_parent']:raise ValueError('This is only the declared failed finite terminal')
 M,N=d['M'],d['N'];x=np.asarray(d['mesh']);Y=np.asarray(d['states']);U=np.asarray(d['independent_velocities']);A=np.asarray(d['common_accelerations'])
 if (M,N,len(x))!=(160,2048,602)or x[0]!=0 or x[-1]!=1.03 or np.any(np.diff(x)<=0):raise ValueError('Wrong complete mesh')
 if d['common_jet_readout']['missing_acceleration_nodes'] or any(v.shape!=(602,482)or not np.isfinite(v).all()for v in (Y,U,A)):raise ValueError('A complete finite common two-jet is required')
 if not np.array_equal(Y[0,1:M+1],d['core']['coefficients']):raise ValueError('Actual core metadata differs')
 core=dict(position_Z=literal(Y[0,2*M+1:]),velocity_horizontal=literal(U[0,:2*M+1]),acceleration_Z=literal(A[0,2*M+1:]),velocity_Z_minus_ez=literal(U[0,2*M+1:]-np.r_[1.,np.zeros(M)]),R0=float(Y[0,0]))
 mirror=all(core[k]['nonzero_count']==0 for k in ('position_Z','velocity_horizontal','acceleration_Z'))
 if not mirror:raise ValueError('This frozen terminal was declared literally mirror compatible; do not silently repair it')
 eps=[Q.from_float(float(Y[0,M+j]))+2*j*Q.from_float(float(Y[0,j]))for j in range(1,M+1)]
 core['support_relation_nonzero']=[dict(mode=j,value_exact=str(v))for j,v in enumerate(eps,1)if v]
 oldcore=list(map(Q.from_float,ref['original_core_coefficients']));newcore=list(map(Q.from_float,d['core']['coefficients']))
 if ref['M']!=320 or any(oldcore[M:]) or list(map(Q.from_float,ref['states'][0][1:321]))!=oldcore:raise ValueError('Wrong reference core for R638 density reuse')
 density_difference=sum((abs((1-(2*j)**2)*(newcore[j-1]-oldcore[j-1]))for j in range(1,M+1)),Q())
 core['reference_core_coefficient_max_difference']=float(max(abs(v-w)for v,w in zip(newcore,oldcore)))
 core['rho_reference_all_angle_lower_exact']='159/1000'
 core['rho_difference_l1_exact']=str(density_difference)
 core['rho_all_angle_lower_exact']=str(Q(159,1000)-density_difference)
 core['rho_strictly_positive_by_R638_reuse']=density_difference<Q(159,1000)
 fs=load(scripts/'parallel_20261117_frenet_symbol.py','actual_implicit_quintic_fs');hp=load(scripts/'parallel_20261117_negative_hold_profile_ivp.py','actual_implicit_quintic_hold')
 profile=hp.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'])
 if profile.spec()!=d['hold_scalar_profile']or d['hold_profile_sha256']!=HOLD:raise ValueError('Wrong fixed scalar')
 angles=8192;subdivisions=4;q=fs.Frenet(M,angles)
 rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*Y[0,1:M+1])
 saved_scalar=np.array([d['scalar_nodes'][key]for key in ('a','ap','app')]).T;scalar_error=np.zeros(3)
 metric=dict(value=0.);curvature=dict(value=0.);minimum={k:dict(value=float('inf'))for k in ('Q','W','H','normal_velocity','Gram_determinant','cross_area_squared')}
 full_residual=np.zeros(3);omitted=np.zeros(3);retained=np.zeros(3);node_projection_error=0.;position_norm=0.;bad=dict(nonfinite_samples=0,zero_area_samples=0,H_nonpositive_samples=0,normal_velocity_nonpositive_samples=0,Gram_determinant_nonpositive_samples=0)
 records=[];points=0;negative_discriminant=0.;worst_acceleration=dict(value=0.)
 for i,h in enumerate(np.diff(x)):
  c0=Y[i];c1=h*U[i];c2=h*h*A[i]/2
  aa=Y[i+1]-c0-c1-c2;bb=h*U[i+1]-c1-2*c2;cc=h*h*A[i+1]-2*c2
  coefficient=np.array([c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2])
  first=np.arange(1,6)[:,None]*coefficient[1:];second=(np.arange(2,6)*np.arange(1,5))[:,None]*coefficient[2:]
  cm=dict(cell=i,left=float(x[i]),right=float(x[i+1]),metric_max=0.,curvature_max=0.,H_min=float('inf'),normal_velocity_min=float('inf'))
  for u in np.linspace(0,1,subdivisions+1):
   # Endpoint evaluation uses the exact defining common jets, not a new RHS.
   if u==0:s=float(x[i]);y,v,acc=Y[i],U[i],A[i];node=i
   elif u==1:s=float(x[i+1]);y,v,acc=Y[i+1],U[i+1],A[i+1];node=i+1
   else:s=float(x[i]+u*h);y=np.polynomial.polynomial.polyval(u,coefficient);v=np.polynomial.polynomial.polyval(u,first)/h;acc=np.polynomial.polynomial.polyval(u,second)/(h*h);node=None
   F,t,e=q.jet(y);V,Vphi,_=q.jet(v);Acc,_,_=q.jet(acc)
   radius,ap,app=profile(s);k=ap/radius
   if node is not None:scalar_error=np.maximum(scalar_error,abs(np.array([radius,ap,app])-saved_scalar[node]))
   E=np.sum(V*V,axis=1);mix=np.sum(V*t,axis=1);G=np.sum(t*t,axis=1)
   er=E-1;cr=mix/(radius*rho);gr=G/(radius*rho)**2-1
   op=(abs(er+gr)+np.sqrt((er-gr)**2+4*cr*cr))/2
   if not all(np.isfinite(z).all()for z in (F,V,Acc,op)):raise FloatingPointError('Nonfinite actual field at cell '+str(i)+' u '+str(u))
   j=int(np.argmax(op));cm['metric_max']=max(cm['metric_max'],float(op[j]))
   if op[j]>metric['value']:metric=address(op[j],i,u,s,j,q.angle);metric.update(rr=float(er[j]),mixed=float(cr[j]),angular=float(gr[j]))
   normal_curve=np.cross(t,e);W=np.sum(normal_curve*normal_curve,axis=1);H=W-k*k*G**3;branch=np.sum(V*normal_curve,axis=1)
   area_vector=np.cross(V,t);area2=np.sum(area_vector*area_vector,axis=1);det=E*G-mix*mix
   for name,value in (('Q',G),('W',W),('H',H),('normal_velocity',branch),('Gram_determinant',det),('cross_area_squared',area2)):
    j=int(np.argmin(value))
    if value[j]<minimum[name]['value']:minimum[name]=address(value[j],i,u,s,j,q.angle)
   bad['H_nonpositive_samples']+=int(np.count_nonzero(H<=0));bad['normal_velocity_nonpositive_samples']+=int(np.count_nonzero(branch<=0));bad['Gram_determinant_nonpositive_samples']+=int(np.count_nonzero(det<=0));bad['zero_area_samples']+=int(np.count_nonzero(area2<=0))
   cm['H_min']=min(cm['H_min'],float(H.min()));cm['normal_velocity_min']=min(cm['normal_velocity_min'],float(branch.min()))
   valid=area2>0;normal=area_vector[valid]/np.sqrt(area2[valid,None])
   ess=np.sum(Acc[valid]*normal,axis=1);est=np.sum(Vphi[valid]*normal,axis=1);ett=np.sum(e[valid]*normal,axis=1)
   trace=(ess*G[valid]+ett*E[valid]-2*est*mix[valid])/area2[valid];gauss=(ess*ett-est*est)/area2[valid]
   disc=trace*trace-4*gauss;negative_discriminant=min(negative_discriminant,float(disc.min(initial=0.)))
   kval=(abs(trace)+np.sqrt(np.maximum(0,disc)))/2
   if len(kval):
    local=int(np.argmax(kval));j=int(np.flatnonzero(valid)[local]);value=float(kval[local]);cm['curvature_max']=max(cm['curvature_max'],value)
    if value>curvature['value']:curvature=address(value,i,u,s,j,q.angle)
   acceleration_norm=np.linalg.norm(Acc,axis=1);j=int(np.argmax(acceleration_norm))
   if acceleration_norm[j]>worst_acceleration['value']:worst_acceleration=address(acceleration_norm[j],i,u,s,j,q.angle)
   position_norm=max(position_norm,float(np.linalg.norm(F,axis=1).max()))
   raw=np.c_[mix,np.sum(V*e,axis=1)+k*G,E-1];full_residual=np.maximum(full_residual,np.max(abs(raw),axis=0));spectrum=np.fft.rfft(raw,axis=0)/angles
   coeff=[-2*spectrum[2*np.arange(1,2*M+1),0].imag,2*spectrum[2*np.arange(0,2*M+1),1].real,2*spectrum[2*np.arange(0,2*M+1),2].real];coeff[1][0]*=.5;coeff[2][0]*=.5
   parts=[coeff[0][:M],coeff[1][:M+1],coeff[2][:M+1]]
   retained=np.maximum(retained,[max(abs(z))for z in parts]);omitted=np.maximum(omitted,[max(abs(coeff[0][M:])),max(abs(coeff[1][M+1:])),max(abs(coeff[2][M+1:]))])
   if node is not None:node_projection_error=max(node_projection_error,float(np.max(abs(np.concatenate(parts)-d['nodes_raw_constraints'][node]))))
   points+=angles
  records.append(cm)
  if (i+1)%100==0:print(json.dumps(dict(event='actual_quintic_progress',cells=i+1,metric=metric['value'],curvature=curvature['value'],seconds=time.perf_counter()-begin)),flush=True)
 for p,h in identities.items():
  if sha(p)!=h:raise ValueError('Frozen identity changed during readout')
 if sha(__file__)!=source:raise ValueError('Reader changed during its only pass')
 out=dict(scope=__doc__,source_sha256=source,input_sha256=FIELD,producer_sha256=PRODUCER,dependencies={str(p):h for p,h in identities.items()},M=M,construction_angles=N,read_angles=angles,radial_subdivisions=subdivisions,quintic_cells=len(x)-1,sampled_points=points,end=float(x[-1]),all_cells_read=True,source_finite_algebraic_converged=False,accepted_parent=False,
  candidate_definition='Unique common quintic of the literal binary Y/U/common_accelerations in the terminal field; original solver cubic is not read again.',core=core,core_mirror_conditions_literal_zero=mirror,mirror_patch_constructed=False,mirror_extension_C2_as_map=True,immersion_embedding_reach_certified=False,
  scalar_definition='Unchanged HoldProfile; stored scalar_nodes are numerical evaluations, not a new target metric.',scalar_source_sha256=HOLD,scalar_node_recompute_max_abs=scalar_error.tolist(),rho_sample_min=float(rho.min()),
  max_sample_relative_Gram_operator=metric,max_sample_principal_curvature=curvature,minimum_sample_domain=minimum,nonpositive_counts=bad,minimum_roundoff_principal_discriminant=negative_discriminant,max_sample_actual_acceleration_norm=worst_acceleration,max_sample_position_norm=position_norm,
  actual_quintic_full_point_constraint_max_by_row=full_residual.tolist(),actual_quintic_retained_constraint_coefficient_max_by_row=retained.tolist(),actual_quintic_unretained_constraint_coefficient_max_by_row=omitted.tolist(),node_projection_difference_from_saved_original_constraints=node_projection_error,
  unretained_mode_indices=[M+1,2*M],continuous_metric_certified=False,new_BVP_solved=False,core_rho_may_differ_from_reference=True,per_cell=records,seconds=time.perf_counter()-begin)
 a.out.write_bytes(gzip.compress((json.dumps(out,indent=2,allow_nan=False)+'\n').encode(),mtime=0))
 print(json.dumps({k:v for k,v in out.items()if k not in ('per_cell','core')}),flush=True);print(json.dumps(dict(report=str(a.out),sha256=sha(a.out))),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','input','reference','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
