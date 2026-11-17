#!/usr/bin/env python3
"""Continuous embedding budget for the fixed pulse arclength normalization.

Exact binary common quintic jets define F. The literal N-point speed mean
defines b, lambda=a/b. Directed radial Bernstein boxes enclose b,b_s and
lambda,lambda_s; a is the exact scalar, never its Gauss evaluator. The
existing R9/R638/R640 results supply degree and coordinate regularity.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
for k in ('topic','input','out'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--radial-subdivisions',type=int,default=4)
a=p.parse_args();N=4096;n=a.radial_subdivisions
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
dep=a.topic/'scripts/parallel_20261117_arclength_interval_positive.py'
dep_sha='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
input_sha='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
if sha(dep)!=dep_sha or sha(a.input)!=input_sha:raise ValueError('Fixed dependency/input identity mismatch')
sp=importlib.util.spec_from_file_location('normalized_graph_interval',dep)
I=importlib.util.module_from_spec(sp);sp.loader.exec_module(I)
np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
started=time.perf_counter();source_sha=sha(__file__)
d=json.loads(gzip.decompress(a.input.read_bytes()));M=d['M'];nu=2*np.arange(M+1)
x=np.array(d['mesh']);Y=np.array(d['states']);D=np.array(d['rhs']);DD=np.array(d['d2'])
if M!=320 or d['N']!=N or n<1 or n&(n-1):raise ValueError('Fixed field and dyadic radial subdivisions required')
if x.ndim!=1 or len(x)!=819 or not np.isfinite(x).all() or np.any(np.diff(x)<=0) or x[0]!=0 or x[-1]!=1:raise ValueError('Full ordered pulse prefix required')
if any(z.shape!=(len(x),3*M+2) or not np.isfinite(z).all() for z in (Y,D,DD)):raise ValueError('Full finite common 0/1/2 jets required')
jet_sha=hashlib.sha256(b''.join(np.ascontiguousarray(z,dtype='<f8').tobytes()for z in (x,Y,D,DD))).hexdigest()
tr=I.Transform(N)

def bezier(y0,y1,v0,v1,a0,a1,h):
 y0=I.exact(y0);y1=I.exact(y1);v0=I.mul(h,I.exact(v0));v1=I.mul(h,I.exact(v1))
 h2=I.square(h);a0=I.mul(h2,I.exact(a0));a1=I.mul(h2,I.exact(a1))
 b=I.stack([y0,I.add(y0,I.div(v0,I.exact(5))),I.add(I.add(y0,I.div(I.scale(v0,2),I.exact(5))),I.div(a0,I.exact(20))),
 I.add(I.sub(y1,I.div(I.scale(v1,2),I.exact(5))),I.div(a1,I.exact(20))),I.sub(y1,I.div(v1,I.exact(5))),y1])
 v=I.div(I.scale(I.sub(I.at(b,slice(1,None)),I.at(b,slice(None,-1))),5),h)
 ve=[I.at(v,0)]
 for j in range(1,5):ve.append(I.div(I.add(I.scale(I.at(v,j-1),j),I.scale(I.at(v,j),5-j)),I.exact(5)))
 ve.append(I.at(v,4));return b,I.stack(ve)

def split(b):
 work=b;left=[I.at(work,0)];right=[I.at(work,-1)]
 for degree in range(5,0,-1):
  work=I.scale(I.add(I.at(work,slice(None,-1)),I.at(work,slice(1,None))),.5)
  left.append(I.at(work,0));right.append(I.at(work,-1))
 return I.stack(left),I.stack(list(reversed(right)))

def parts(b):
 z=[b]
 for level in range(n.bit_length()-1):z=[out for item in z for out in split(item)]
 return z

def hull(b):return b[0].min(axis=0),b[1].max(axis=0)
def prepend(z):
 zero=np.zeros(z[0].shape[:-1]+(1,))
 return np.concatenate([zero,z[0]],axis=-1),np.concatenate([zero,z[1]],axis=-1)
def channels(b):
 R=I.at(b,(slice(None),slice(0,M+1)));T=prepend(I.at(b,(slice(None),slice(M+1,2*M+1))));Z=I.at(b,(slice(None),slice(2*M+1,None)))
 dr=I.neg(I.add(I.scale(R,nu),T));dt=I.add(R,I.scale(T,nu));dz=I.neg(I.scale(Z,nu))
 er=I.neg(I.add(I.scale(R,nu*nu+1),I.scale(T,2*nu)))
 et=I.neg(I.add(I.scale(T,nu*nu+1),I.scale(R,2*nu)));ez=I.neg(I.scale(Z,nu*nu))
 zm=tuple(q.copy()for q in Z)
 for q in zm:q[:,0]=0.
 return dict(R=R,T=T,Z=Z,zm=zm,dr=dr,dt=dt,dz=dz,er=er,et=et,ez=ez)
def bound(co):return float(I.sum_upper(I.absolute_upper(co),axis=-1).max())
def prod(*v):
 z=I.exact(1.)
 for q in v:z=I.mul(z,I.exact(q))
 return float(z[1])
def total(*v):return float(I.sum_upper(np.array(v)))
def tree_sum(z):
 # Explicit directed pairwise additions, with both endpoints preserved.
 while z[0].shape[-1]>1:
  z=I.add(I.at(z,(...,slice(0,None,2))),I.at(z,(...,slice(1,None,2))))
 return I.at(z,(...,0))
def expand_interval(target,z):
 target[0]=min(target[0],float(np.min(z[0])));target[1]=max(target[1],float(np.max(z[1])))

# Exact scalar Hermite on [0,.99]. Whole scalar-cell hulls suffice; the
# field subcell can meet more than one scalar cell, all of which are kept.
geom=d['fixed_scalar_profile']['geometry'];knots=geom['knots']
sx=np.array([z['s']for z in knots]);sj=np.array([[z[k]for k in ('a','ap','app')]for z in knots])
origin=d['analytic_extension_origin'];spec=d['inward_scalar_profile'];pulse=spec['compact_curvature_pulse']
if sx[0]!=0 or sx[-1]!=origin or not np.isfinite(sj).all() or np.any(np.diff(sx)<=0):raise ValueError('Scalar node domain mismatch')
if not np.array_equal(sj[0],np.array([1.,0.,geom['initial_law']['k0']])):raise ValueError('Exact first law jet mismatch')
if origin!=.99 or spec['cut']!=.995 or spec['curvature']!=1.5 or spec['ramp_in']!=.02 or pulse['amplitude']!=-5 or pulse['half_width']!=.005:raise ValueError('Pulse design mismatch')
K=I.div(I.neg(I.exact(sj[-1,2])),I.sqrt(I.sub(I.exact(1.),I.square(I.exact(sj[-1,1])))))
if not (K[0]>1.5 and K[1]<3.5):raise ValueError('The analytic |a_ss|<=3.5 proof does not apply')
# Before cut, kappa=K. During the first ramp, base kappa is in [1.5,K]
# and the negative pulse is in [-5,0]. Hence |kappa|<=3.5 and |a_ss|<=3.5.
scalar_hulls=[]
for i in range(len(sx)-1):
 b,v=bezier(sj[i,0],sj[i+1,0],sj[i,1],sj[i+1,1],sj[i,2],sj[i+1,2],I.sub(I.exact(sx[i+1]),I.exact(sx[i])))
 scalar_hulls.append((hull(b),hull(v)))
def scalar_box(slo,shi):
 ab=[float('inf'),-float('inf')];vb=ab.copy()
 if slo<=origin:
  for j in range(max(0,int(np.searchsorted(sx,slo,side='left'))-1),len(sx)-1):
   if sx[j]>shi:break
   if sx[j+1]>=slo:
    expand_interval(ab,scalar_hulls[j][0]);expand_interval(vb,scalar_hulls[j][1])
 if shi>=origin:
  delta=(max(0.,float(I.down(slo-origin))),max(0.,float(I.up(shi-origin))))
  rem=I.scale(I.square(delta),1.75);r=float(rem[1]);lin=I.add(I.exact(sj[-1,0]),I.scale(delta,sj[-1,1]))
  expand_interval(ab,I.add(lin,(-r,r)));r=float(I.scale(delta,3.5)[1])
  expand_interval(vb,I.add(I.exact(sj[-1,1]),(-r,r)))
 return tuple(np.asarray(z)for z in ab),tuple(np.asarray(z)for z in vb)

worst=dict(value=float('inf'));ranges={k:[float('inf'),-float('inf')]for k in ('a','a_s','b','b_s','lambda','lambda_s')}
minq=float('inf');maxwidth=0.;maxCgprime=0.;records=[]
for i in range(len(x)-1):
 width=I.sub(I.exact(x[i+1]),I.exact(x[i]));b,vb=bezier(Y[i],Y[i+1],D[i],D[i+1],DD[i],DD[i+1],width)
 f=channels(b);v=channels(vb);bf={k:bound(q)for k,q in f.items()};bv={k:bound(q)for k,q in v.items()}
 Ab=total(prod(bf['R'],bf['dt']),prod(bf['T'],bf['dr']))
 Bb=total(prod(bf['R'],bv['T']),prod(bf['T'],bv['R']))
 Ap=total(prod(bf['R'],bf['et']),prod(bf['T'],bf['er']))
 Bp=total(prod(bf['dr'],bv['T']),prod(bf['dt'],bv['R']),prod(bf['R'],bv['dt']),prod(bf['T'],bv['dr']))
 Cp=total(prod(bv['dz'],Ab),prod(bv['Z'],Ap),prod(bf['ez'],Bb),prod(bf['dz'],Bp))
 co=tr.cosine_sine(I.stack([f['R'],f['dt'],v['R'],v['Z'],v['dt'],f['zm']]),N,'cos')
 si=tr.cosine_sine(I.stack([f['T'],f['dr'],f['dz'],v['T'],v['dr'],v['dz']]),N,'sin')
 grid=I.stack([I.at(co,0),I.at(si,0),I.at(si,1),I.at(co,1),I.at(si,2),I.at(co,2),I.at(si,3),I.at(co,3),I.at(si,4),I.at(co,4),I.at(si,5),I.at(co,5)])
 grid=tuple(q.transpose(1,0,2)for q in grid)
 maxwidth=max(maxwidth,float(I.up(grid[1]-grid[0]).max()))
 cvparts=parts(I.at(vb,(slice(None),2*M+1)))
 row=dict(cell=i,left=float(x[i]),right=float(x[i+1]),C_G_lower=float('inf'),lambda_interval=[float('inf'),-float('inf')],lambda_s_interval=[float('inf'),-float('inf')])
 for sub,bg in enumerate(parts(grid)):
  R,T,dr,dt,dz,vr,vt,vz,dvr,dvt,dvz,zm=[I.at(hull(bg),k)for k in range(12)]
  q=I.sqrt(I.add(I.add(I.square(dr),I.square(dt)),I.square(dz)))
  if np.any(q[0]<=0):raise ValueError(f'Speed box meets zero at cell {i}, subcell {sub}')
  qs=I.div(I.add(I.add(I.mul(dr,dvr),I.mul(dt,dvt)),I.mul(dz,dvz)),q)
  bm=I.div(tree_sum(q),I.exact(N));bs=I.div(tree_sum(qs),I.exact(N));minq=min(minq,float(q[0].min()))
  sl=I.add(I.exact(x[i]),I.scale(width,sub/n));sr=I.add(I.exact(x[i]),I.scale(width,(sub+1)/n))
  av,ap=scalar_box(max(0.,float(sl[0])),min(1.,float(sr[1])))
  lam=I.div(av,bm);lamp=I.div(I.sub(I.mul(ap,bm),I.mul(av,bs)),I.square(bm))
  if lam[0]<=0:raise ValueError('Positive scalar scaling not proved')
  cs=hull(cvparts[sub]);correction=I.add(I.mul(I.sub(I.exact(1.),lam),cs),I.mul(lamp,zm))
  AA=I.sub(I.mul(R,dt),I.mul(T,dr));BB=I.sub(I.mul(R,vt),I.mul(T,vr));CC=I.sub(I.mul(vz,AA),I.mul(dz,BB))
  l2=I.square(lam);l3=I.mul(l2,lam);CG=I.add(I.mul(l3,CC),I.mul(I.mul(l2,correction),AA))
  ll=float(I.absolute_upper(lam));lp=float(I.absolute_upper(lamp));ld=float(I.absolute_upper(I.sub(I.exact(1.),lam)))
  gb=total(prod(ld,float(I.absolute_upper(cs))),prod(lp,bf['zm']))
  cgprime=total(prod(ll,ll,ll,Cp),prod(ll,ll,gb,Ap),prod(ll,ll,lp,bf['dz'],Ab))
  loss=float(I.mul(I.div(I.exact(tr.pi_upper),I.exact(N)),I.exact(cgprime))[1])
  grid_lower=float(CG[0].min());lower=float(I.down(grid_lower-loss));maxCgprime=max(maxCgprime,cgprime)
  if lower<worst['value']:worst=dict(value=lower,cell=i,subcell=sub,left=float(x[i]),right=float(x[i+1]),radial_box_grid_lower=grid_lower,angular_loss=loss,angular_derivative_bound=cgprime,lambda_interval=[float(z)for z in lam],lambda_s_interval=[float(z)for z in lamp])
  row['C_G_lower']=min(row['C_G_lower'],lower);expand_interval(row['lambda_interval'],lam);expand_interval(row['lambda_s_interval'],lamp)
  for k,z in zip(ranges,(av,ap,bm,bs,lam,lamp)):expand_interval(ranges[k],z)
 records.append(row)
 if (i+1)%100==0:print(json.dumps(dict(event='progress',cells=i+1,seconds=time.perf_counter()-started,C_G_lower=worst['value'],lambda_interval=ranges['lambda'],lambda_s_interval=ranges['lambda_s'])),flush=True)
if sha(__file__)!=source_sha or sha(a.input)!=input_sha or sha(dep)!=dep_sha:raise ValueError('Frozen identity changed during run')
if not np.isfinite(worst['value']) or not all(np.isfinite(q).all()for q in ranges.values()):raise ValueError('Nonfinite final certificate')
out=dict(scope=__doc__,input_sha256=input_sha,source_sha256=source_sha,interval_dependency_sha256=dep_sha,nodal_jets_little_endian_float64_sha256=jet_sha,
 M=M,construction_angles=N,angular_cover_grid=N,radial_subdivisions=n,cells=len(x)-1,scalar_origin=origin,scalar_K_interval=[float(z)for z in K],analytic_absolute_a_ss_bound=3.5,
 continuous_C_G_lower=worst,continuous_scalar_and_normalization_ranges=ranges,minimum_construction_speed_box=minq,maximum_C_G_angular_derivative_bound=maxCgprime,max_transform_interval_width=maxwidth,
 strict_under_stated_IEEE_arithmetic=True,normalized_open_prefix_embedded=worst['value']>0 and ranges['lambda'][0]>0,
 dependencies='R640 supplies raw Q/A/degree; R638 supplies the C2 angular diffeomorphism; R9 supplies global embedding.',closed_surface=False,reach_certified=False,per_cell=records,seconds=time.perf_counter()-started)
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='per_cell'}),flush=True)
print(json.dumps(dict(output=str(a.out),sha256=sha(a.out))),flush=True)
