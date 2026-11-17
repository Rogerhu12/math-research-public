#!/usr/bin/env python3
"""Actual common-quintic inputs for the existing R9 embedding criterion.

All spatial extrema below are sampled.  Core degree one has a separate
exact-rational half-plane check.  No continuous A/C positivity is claimed.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
for name in ('topic','input','out'):p.add_argument('--'+name,type=Path,required=True)
p.add_argument('--angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4)
args=p.parse_args()
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
operator=args.topic/'scripts/parallel_20261117_frenet_symbol.py'
spec=importlib.util.spec_from_file_location('cylindrical_graph_operator',operator)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
data=json.loads(gzip.decompress(args.input.read_bytes()));q=h.Frenet(data['M'],args.angles)
x=np.array(data['mesh']);Y=np.array(data['states']);D=np.array(data['rhs']);DD=np.array(data['d2'])
if np.any(np.diff(x)<=0):raise ValueError('Actual common-quintic nodes must be strictly increasing')
def cross(a,b):return a[:,0]*b[:,1]-a[:,1]*b[:,0]
keys=('radius_squared','rotating_R','A','C','angle_phi','height_angle_Jacobian','height_s_at_fixed_angle','height_s')
minimum={key:dict(value=float('inf')) for key in keys}
maximum={key:dict(value=0.) for key in ('angle_s_abs','height_angle_derivative_abs','A_s_abs','A_phi_abs','C_s_abs','C_phi_abs')}
cells=[];samples=0;start=time.perf_counter()
core_lower=Fraction.from_float(float(Y[0,0]))-sum((abs(Fraction.from_float(float(v)))for v in Y[0,1:q.M+1]),Fraction(0))
for i,width in enumerate(np.diff(x)):
 c0=Y[i];c1=width*D[i];c2=width*width*DD[i]/2
 a=Y[i+1]-c0-c1-c2;b=width*D[i+1]-c1-2*c2;c=width*width*DD[i+1]-2*c2
 co=np.array([c0,c1,c2,10*a-4*b+c/2,-15*a+7*b-c,6*a-3*b+c/2])
 cell_min={key:float('inf') for key in keys};cell_max={key:0. for key in maximum}
 for j in range(args.radial_subdivisions+1):
  u=j/args.radial_subdivisions;s=float(x[i]+u*width)
  if j==0:y,dy,ddy=Y[i],D[i],DD[i]
  elif j==args.radial_subdivisions:y,dy,ddy=Y[i+1],D[i+1],DD[i+1]
  else:
   y=np.polynomial.polynomial.polyval(u,co)
   dy=np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*co[1:])/width
   ddy=np.polynomial.polynomial.polyval(u,(np.arange(2,6)*np.arange(1,5))[:,None]*co[2:])/width**2
  F,d,e=q.jet(y);V,dV,_=q.jet(dy);Acc,_,_=q.jet(ddy)
  Q=F[:,0]**2+F[:,1]**2;A=cross(F,d);B=cross(F,V);C=V[:,2]*A-d[:,2]*B
  if Q.min()<=0:raise ValueError('A sampled point reaches the rotation axis')
  angle_phi=A/Q;angle_s=B/Q
  As=cross(V,d)+cross(F,dV);Ap=cross(F,e);Bs=cross(F,Acc);Bp=cross(d,V)+cross(F,dV)
  Cs=Acc[:,2]*A+V[:,2]*As-dV[:,2]*B-d[:,2]*Bs
  Cp=dV[:,2]*A+V[:,2]*Ap-e[:,2]*B-d[:,2]*Bp
  values=dict(radius_squared=Q,rotating_R=F[:,0],A=A,C=C,angle_phi=angle_phi,
   height_angle_Jacobian=C/Q,height_s_at_fixed_angle=C/A,height_s=V[:,2])
  upper=dict(angle_s_abs=abs(angle_s),height_angle_derivative_abs=abs(d[:,2]/angle_phi),
   A_s_abs=abs(As),A_phi_abs=abs(Ap),C_s_abs=abs(Cs),C_phi_abs=abs(Cp))
  for key,v in values.items():
   k=int(np.argmin(v));value=float(v[k]);cell_min[key]=min(cell_min[key],value)
   if value<minimum[key]['value']:minimum[key]=dict(value=value,s=s,angle=float(q.angle[k]),cell=i,u=u)
  for key,v in upper.items():
   k=int(np.argmax(v));value=float(v[k]);cell_max[key]=max(cell_max[key],value)
   if value>maximum[key]['value']:maximum[key]=dict(value=value,s=s,angle=float(q.angle[k]),cell=i,u=u)
  samples+=q.N
 cells.append(dict(cell=i,left=float(x[i]),right=float(x[i+1]),sample_minimum=cell_min,sample_absolute_maximum=cell_max))
 if (i+1)%100==0:print(json.dumps(dict(event='cell_progress',cells=i+1,seconds=time.perf_counter()-start)),flush=True)
out=dict(scope=__doc__,source_sha256=sha(__file__),operator_sha256=sha(operator),input_sha256=sha(args.input),
 input_schema=data.get('schema'),M=q.M,angles=q.N,radial_subdivisions=args.radial_subdivisions,
 start=float(x[0]),end=float(x[-1]),quintic_cells=len(x)-1,sample_points=samples,
 sampled_minimum=minimum,sampled_absolute_maximum=maximum,
 core_degree_one_halfplane=dict(exact_R_lower=str(core_lower),lower_float=float(core_lower),
  positive=core_lower>0,reason='R(0,phi)>0 puts R+iT in the open right half-plane; beta=phi+arg(R+iT) has degree one'),
 all_sampled_graph_signs_positive=all(minimum[key]['value']>0 for key in ('radius_squared','A','C')),
 continuous_graph_certificate=False,continuous_embedding_certified=False,
 polynomial_degrees=dict(radial_radius_squared=10,radial_A=10,radial_C=14,
  max_angular_frequency_radius_squared=4*q.M,max_angular_frequency_A=4*q.M,max_angular_frequency_C=6*q.M),
 per_cell=cells,seconds=time.perf_counter()-start)
args.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='per_cell'}),flush=True)
print(json.dumps(dict(output=str(args.out),sha256=sha(args.out))),flush=True)
