#!/usr/bin/env python3
"""Directed all-cell/all-angle Q,A,C bounds for the existing R9 criterion.

Exact binary nodal jets define the map. Bernstein convex hulls cover every
radial position; the frozen directed transform plus angular derivative
l1 losses cover every angle. The normalized scaled image is not certified.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
for key in ('topic','input','out'):p.add_argument('--'+key,type=Path,required=True)
p.add_argument('--angles',type=int,default=2048);p.add_argument('--radial-subdivisions',type=int,default=4)
args=p.parse_args();dependency=args.topic/'scripts/parallel_20261117_arclength_interval_positive.py'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
expected='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
if sha(dependency)!=expected:raise ValueError('Frozen directed arithmetic/transform changed')
spec=importlib.util.spec_from_file_location('graph_intervals',dependency)
I=importlib.util.module_from_spec(spec);spec.loader.exec_module(I)
np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
started=time.perf_counter();source_sha=sha(__file__);input_sha=sha(args.input)
data=json.loads(gzip.decompress(args.input.read_bytes()));M=data['M'];Qgrid=args.angles;n=args.radial_subdivisions
if Qgrid&(Qgrid-1) or n<1 or n&(n-1) or 4*M>=Qgrid:raise ValueError('Dyadic grids and Q>4M required')
x=np.array(data['mesh']);Y=np.array(data['states']);D=np.array(data['rhs']);DD=np.array(data['d2'])
if len(x)<2 or np.any(np.diff(x)<=0):raise ValueError('Strict common node ordering required')
if any(z.shape!=(len(x),3*M+2) or not np.isfinite(z).all() for z in (Y,D,DD)):raise ValueError('Full finite 0/1/2 jets required')
jet_sha=hashlib.sha256(b''.join(np.ascontiguousarray(z,dtype='<f8').tobytes()for z in (x,Y,D,DD))).hexdigest()
tr=I.Transform(Qgrid);nu=2*np.arange(M+1)
def prepend(z):return (np.concatenate([np.zeros(z[0].shape[:-1]+(1,)),z[0]],axis=-1),np.concatenate([np.zeros(z[1].shape[:-1]+(1,)),z[1]],axis=-1))
def channels(b):
 R=I.at(b,(slice(None),slice(0,M+1)));T=prepend(I.at(b,(slice(None),slice(M+1,2*M+1))));Z=I.at(b,(slice(None),slice(2*M+1,None)))
 dr=I.neg(I.add(I.scale(R,nu),T));dt=I.add(R,I.scale(T,nu));dz=I.neg(I.scale(Z,nu))
 er=I.neg(I.add(I.scale(R,nu*nu+1),I.scale(T,2*nu)))
 et=I.neg(I.add(I.scale(T,nu*nu+1),I.scale(R,2*nu)));ez=I.neg(I.scale(Z,nu*nu))
 return dict(R=R,T=T,Z=Z,dr=dr,dt=dt,dz=dz,er=er,et=et,ez=ez)
def bounds(co):return float(I.sum_upper(I.absolute_upper(co),axis=-1).max())
def product(*values):
 z=I.exact(1.)
 for v in values:z=I.mul(z,I.exact(v))
 return float(z[1])
def total(*values):return float(I.sum_upper(np.array(values)))
def split(b):
 work=b;left=[I.at(work,0)];right=[I.at(work,-1)]
 for degree in range(5,0,-1):
  work=I.scale(I.add(I.at(work,slice(None,-1)),I.at(work,slice(1,None))),.5)
  left.append(I.at(work,0));right.append(I.at(work,-1))
 return I.stack(left),I.stack(list(reversed(right)))
worst={key:dict(value=float('inf')) for key in ('radius_squared','A','C')};max_derivative={key:0. for key in worst}
max_transform_width=0.;records=[]
for i in range(len(x)-1):
 width=I.sub(I.exact(x[i+1]),I.exact(x[i]));h2=I.mul(width,width)
 y0=I.exact(Y[i]);y1=I.exact(Y[i+1]);v0=I.mul(width,I.exact(D[i]));v1=I.mul(width,I.exact(D[i+1]))
 a0=I.mul(h2,I.exact(DD[i]));a1=I.mul(h2,I.exact(DD[i+1]))
 b=I.stack([y0,I.add(y0,I.div(v0,I.exact(5))),I.add(I.add(y0,I.div(I.scale(v0,2),I.exact(5))),I.div(a0,I.exact(20))),
            I.add(I.sub(y1,I.div(I.scale(v1,2),I.exact(5))),I.div(a1,I.exact(20))),I.sub(y1,I.div(v1,I.exact(5))),y1])
 dv=I.div(I.scale(I.sub(I.at(b,slice(1,None)),I.at(b,slice(None,-1))),5),width)
 ve=[I.at(dv,0)]
 for j in range(1,5):ve.append(I.div(I.add(I.scale(I.at(dv,j-1),j),I.scale(I.at(dv,j),5-j)),I.exact(5)))
 ve.append(I.at(dv,4));vb=I.stack(ve)
 f=channels(b);v=channels(vb);bf={key:bounds(val) for key,val in f.items()};bv={key:bounds(val)for key,val in v.items()}
 Ab=total(product(bf['R'],bf['dt']),product(bf['T'],bf['dr']))
 Bb=total(product(bf['R'],bv['T']),product(bf['T'],bv['R']))
 Ap=total(product(bf['R'],bf['et']),product(bf['T'],bf['er']))
 Bp=total(product(bf['dr'],bv['T']),product(bf['dt'],bv['R']),product(bf['R'],bv['dt']),product(bf['T'],bv['dr']))
 Cp=total(product(bv['dz'],Ab),product(bv['Z'],Ap),product(bf['ez'],Bb),product(bf['dz'],Bp))
 Qp=total(product(2,bf['R'],bf['dr']),product(2,bf['T'],bf['dt']))
 derivative=dict(radius_squared=Qp,A=Ap,C=Cp)
 for key in derivative:max_derivative[key]=max(max_derivative[key],derivative[key])
 cos=tr.cosine_sine(I.stack([f['R'],f['dt'],v['R'],v['Z']]),Qgrid,'cos')
 sin=tr.cosine_sine(I.stack([f['T'],f['dr'],f['dz'],v['T']]),Qgrid,'sin')
 grid=I.stack([I.at(cos,0),I.at(sin,0),I.at(sin,1),I.at(cos,1),I.at(sin,2),I.at(cos,2),I.at(sin,3),I.at(cos,3)])
 grid=tuple(z.transpose(1,0,2) for z in grid)
 max_transform_width=max(max_transform_width,float(I.up(grid[1]-grid[0]).max()))
 parts=[grid]
 for level in range(n.bit_length()-1):parts=[part for item in parts for part in split(item)]
 row=dict(cell=i,left=float(x[i]),right=float(x[i+1]),derivative_bounds=derivative,lower={key:float('inf')for key in worst})
 for sub,bg in enumerate(parts):
  box=(bg[0].min(axis=0),bg[1].max(axis=0));R,T,dr,dt,dz,vr,vt,vz=[I.at(box,k)for k in range(8)]
  AA=I.sub(I.mul(R,dt),I.mul(T,dr));BB=I.sub(I.mul(R,vt),I.mul(T,vr))
  CC=I.sub(I.mul(vz,AA),I.mul(dz,BB));QQ=I.add(I.square(R),I.square(T))
  for key,val in zip(('radius_squared','A','C'),(QQ,AA,CC)):
   angular_loss=I.mul(I.div(I.exact(tr.pi_upper),I.exact(Qgrid)),I.exact(derivative[key]))[1]
   grid_lower=float(val[0].min());lower=float(I.down(grid_lower-angular_loss));row['lower'][key]=min(row['lower'][key],lower)
   if lower<worst[key]['value']:worst[key]=dict(value=lower,cell=i,subcell=sub,left=float(x[i]),right=float(x[i+1]),
     radial_box_grid_lower=grid_lower,angular_loss=float(angular_loss),angular_derivative_bound=derivative[key])
 records.append(row)
 if (i+1)%100==0:print(json.dumps(dict(event='interval_progress',cells=i+1,seconds=time.perf_counter()-started,
  lower={k:v['value']for k,v in worst.items()})),flush=True)
core_lower=Fraction.from_float(float(Y[0,0]))-sum((abs(Fraction.from_float(float(v)))for v in Y[0,1:M+1]),Fraction(0))
if sha(__file__)!=source_sha or sha(args.input)!=input_sha or sha(dependency)!=expected:raise ValueError('Frozen source/input identity changed during run')
out=dict(scope=__doc__,source_sha256=source_sha,interval_dependency_sha256=expected,input_sha256=input_sha,
 nodal_jets_little_endian_float64_sha256=jet_sha,M=M,angle_grid=Qgrid,radial_subdivisions=n,cells=len(x)-1,
 continuous_lower_bounds=worst,maximum_angular_derivative_bounds=max_derivative,max_transform_interval_width=max_transform_width,
 core_R_exact_lower=str(core_lower),core_degree_one=core_lower>0,
 strict_under_stated_IEEE_arithmetic=True,raw_open_prefix_embedded=core_lower>0 and all(v['value']>0 for v in worst.values()),
 normalized_scaled_image_certified=False,closed_surface=False,reach_certified=False,per_cell=records,
 seconds=time.perf_counter()-started)
args.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='per_cell'}),flush=True)
print(json.dumps(dict(output=str(args.out),sha256=sha(args.out))),flush=True)
