#!/usr/bin/env python3
"""Distance from an exact rotated core point to the fixed complete hold image.

p=Rot_{pi/2} G(0,0), with its true lambda(0), is enclosed using the already
proved R642 first-cell scale interval. All cell scale intervals come from
R642/R644, without recomputing any speed mean. Position Bernstein boxes
and a second-derivative angular Taylor cover enclose the entire image.
This is a point-to-open-image distance, not closed held/D or a flex member.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from fractions import Fraction
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
for k in ('topic','input','old-scaling','new-scaling','out'):p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();N=4096;subdivisions=4;first=498
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(path,name,expected):
 if sha(path)!=expected:raise ValueError('Frozen dependency mismatch')
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
input_sha='aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15'
old_report_sha='b9813c624e47c05d6ad8cfb21ee026f9e12c83755e4e88f968748eba9a6784a6'
new_report_sha='80377514272e4d68ba8f8d9e5fefdc273c0b74ee221331bfea9a9a8df2c4e59b'
ish='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
hsh='a685b93e888e55e8b2dc4e0505e977a6ac0f2db88c18f2db2b5889d6a7dd02d8'
ip=a.topic/'scripts/parallel_20261117_arclength_interval_positive.py'
hp=a.topic/'notes/2026-11-17-parallel-geometry-normalization-interval-tools.py'
if sha(a.input)!=input_sha or sha(a.old_scaling)!=old_report_sha or sha(a.new_scaling)!=new_report_sha:raise ValueError('Fixed input/evidence changed')
I=load(ip,'witness_interval_arithmetic',ish);H=load(hp,'witness_interval_tools',hsh)
np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
start=time.perf_counter();source_sha=sha(__file__)
data=json.loads(gzip.decompress(a.input.read_bytes()));M=data['M'];nu=2*np.arange(M+1)
x=np.asarray(data.pop('mesh'));Y=np.asarray(data.pop('states'));D=np.asarray(data.pop('rhs'));DD=np.asarray(data.pop('d2'))
if M!=320 or data['N']!=N or len(x)!=2099 or x[0]!=0 or x[first]!=.995 or x[-1]!=1.02 or not np.isfinite(x).all() or np.any(np.diff(x)<=0):raise ValueError('Wrong complete image')
if any(z.shape!=(len(x),3*M+2)or not np.isfinite(z).all()for z in (Y,D,DD)):raise ValueError('Complete finite common jets required')
old=json.loads(a.old_scaling.read_text());new=json.loads(gzip.decompress(a.new_scaling.read_bytes()))
if old['source_sha256']!='0e9185242c05893197332fb376ff06a277279cdfa00808e50a1553342a9c93e4' or new['source_sha256']!='a2a126353e70d6af8b4f03f7dd9bc612236d7d41a01bae7fd449db3685135145':raise ValueError('Different scaling certificate algorithms')
if new['input_sha256']!=input_sha or new['old_input_sha256']!=old['input_sha256'] or new['reused_old_cells']!=first or new['identical_prefix_nodes']!=first+1 or not new['exact_old_scalar_same']:raise ValueError('Missing exact old-prefix identity')
rows=old['per_cell'][:first]+new['per_new_cell']
if len(rows)!=len(x)-1:raise ValueError('Incomplete scaling range table')
for i,row in enumerate(rows):
 lo,hi=row['lambda_interval']
 if row['cell']!=i or row['left']!=x[i] or row['right']!=x[i+1] or not(0<lo<=hi)or not np.isfinite([lo,hi]).all():raise ValueError('Wrong cell or scale bounds')
if np.any(Y[0,2*M+1:]!=0):raise ValueError('The witness requires the actual planar core')
major=sum((Fraction.from_float(float(v))for v in Y[0,:M+1]),Fraction(0))
if major<=0:raise ValueError('Positive selected core coordinate required')
mf=float(major);mbox=(float(I.down(mf)),float(I.up(mf)))
if not (Fraction.from_float(mbox[0])<=major<=Fraction.from_float(mbox[1])):raise ValueError('Bad rational conversion')
lambda0=tuple(rows[0]['lambda_interval']);py=I.mul(mbox,lambda0)
py_exact_box=[str(major*Fraction.from_float(v))for v in lambda0]
tr=I.Transform(N)
def full_period(z):return np.r_[z[0],-z[1]],np.r_[z[1],-z[0]]
cosphi=full_period(tr.cos);sinphi=full_period(tr.sin)
step=I.div(I.exact(tr.pi_upper),I.exact(N));halfstep2=I.scale(I.square(step),.5)
band=4*M;discount=float(I.sub(I.exact(1.),I.scale(halfstep2,band*band))[0])
if discount<=0:raise ValueError('Angular second-derivative cover unavailable')
def split(b):
 work=b;left=[I.at(work,0)];right=[I.at(work,-1)]
 for _ in range(5):
  work=I.scale(I.add(I.at(work,slice(None,-1)),I.at(work,slice(1,None))),.5)
  left.append(I.at(work,0));right.append(I.at(work,-1))
 return I.stack(left),I.stack(list(reversed(right)))
def parts(b):return [z for half in split(b)for z in split(half)]
def prepend(z):
 zero=np.zeros(z[0].shape[:-1]+(1,))
 return np.concatenate([zero,z[0]],axis=-1),np.concatenate([zero,z[1]],axis=-1)
def channels(b):
 R=I.at(b,(slice(None),slice(0,M+1)));T=prepend(I.at(b,(slice(None),slice(M+1,2*M+1))));Z=I.at(b,(slice(None),slice(2*M+1,None)))
 zm=tuple(v.copy()for v in Z)
 for v in zm:v[:,0]=0.
 dr=I.neg(I.add(I.scale(R,nu),T));dt=I.add(R,I.scale(T,nu));dz=I.neg(I.scale(Z,nu))
 er=I.neg(I.add(I.scale(R,nu*nu+1),I.scale(T,2*nu)))
 et=I.neg(I.add(I.scale(T,nu*nu+1),I.scale(R,2*nu)));ez=I.neg(I.scale(Z,nu*nu))
 return R,T,zm,dr,dt,dz,er,et,ez
def add3(z):return I.add(I.add(z[0],z[1]),z[2])
def dot(v,w):return add3([I.mul(u,z)for u,z in zip(v,w)])
worst=dict(squared_lower=float('inf'));records=[];maxwidth=0.;maxB2=0.
for i in range(len(x)-1):
 width=I.sub(I.exact(x[i+1]),I.exact(x[i]))
 b,_=H.hermite_bezier(I,(Y[i],D[i],DD[i]),(Y[i+1],D[i+1],DD[i+1]),width)
 R,T,zm,dr,dt,dz,er,et,ez=channels(b)
 co=tr.cosine_sine(I.stack([R,zm,dt,er,ez]),N,'cos')
 si=tr.cosine_sine(I.stack([T,dr,dz,et]),N,'sin')
 grid=I.stack([I.at(co,0),I.at(si,0),I.at(co,1),I.at(si,1),I.at(co,2),I.at(si,2),I.at(co,3),I.at(si,3),I.at(co,4)])
 grid=tuple(v.transpose(1,0,2)for v in grid);maxwidth=max(maxwidth,float(I.up(grid[1]-grid[0]).max()))
 centers=parts(I.at(b,(slice(None),2*M+1)));lam=tuple(rows[i]['lambda_interval'])
 row=dict(cell=i,left=float(x[i]),right=float(x[i+1]),squared_lower=float('inf'))
 for j,bg in enumerate(parts(grid)):
  box=H.hull(bg);r,t,z,ar,at,az,er,et,ez=[I.at(box,k)for k in range(9)]
  center=H.hull(centers[j]);delta=[I.sub(I.mul(lam,r),I.mul(py,sinphi)),I.sub(I.mul(lam,t),I.mul(py,cosphi)),I.add(center,I.mul(lam,z))]
  firstjet=[I.mul(lam,v)for v in (ar,at,az)];secondjet=[I.mul(lam,v)for v in (er,et,ez)]
  f0=add3([I.square(v)for v in delta]);f1=I.scale(dot(delta,firstjet),2)
  f2=I.scale(I.add(add3([I.square(v)for v in firstjet]),dot(delta,secondjet)),2)
  # For fixed s, f'' is a real trig polynomial of degree <=4M. At its
  # extremum f'''=0, and Bernstein gives ||f''''||<=band^2||f''||.
  # Thus a nearest grid point gives the stated discount, uniformly in s.
  B2=float(I.div(I.exact(float(I.absolute_upper(f2).max())),I.exact(discount))[1]);maxB2=max(maxB2,B2)
  losses=I.add(I.mul(step,I.exact(I.absolute_upper(f1))),I.mul(halfstep2,I.exact(B2)))[1]
  lower=I.down(f0[0]-losses);k=int(np.argmin(lower));value=float(lower[k]);row['squared_lower']=min(row['squared_lower'],value)
  if value<worst['squared_lower']:
   worst=dict(squared_lower=value,cell=i,subcell=j,angle_grid_index=k,left=float(x[i]),right=float(x[i+1]),radial_box_grid_lower=float(f0[0][k]),
    first_angular_loss=float(I.mul(step,I.exact(I.absolute_upper(f1)[k]))[1]),second_angular_loss=float(I.mul(halfstep2,I.exact(B2))[1]),whole_angle_second_bound=B2,
    lambda_interval=list(lam))
 records.append(row)
 if (i+1)%100==0:print(json.dumps(dict(event='distance_progress',cells=i+1,seconds=time.perf_counter()-start,squared_lower=worst['squared_lower'])),flush=True)
if sha(__file__)!=source_sha or sha(a.input)!=input_sha or sha(a.old_scaling)!=old_report_sha or sha(a.new_scaling)!=new_report_sha or sha(ip)!=ish or sha(hp)!=hsh:raise ValueError('Frozen identities changed')
if not np.isfinite(worst['squared_lower']):raise ValueError('Nonfinite bound')
distance=float(I.sqrt(I.exact(max(0.,worst['squared_lower'])))[0])
out=dict(scope=__doc__,source_sha256=source_sha,input_sha256=input_sha,old_scaling_report_sha256=old_report_sha,new_scaling_report_sha256=new_report_sha,
 interval_dependency_sha256=ish,helper_sha256=hsh,M=M,construction_angles=N,angular_cover_grid=N,radial_subdivisions=subdivisions,cells=len(x)-1,
 witness_definition='p=Rot(pi/2)G(0,0)=(0,lambda(0)*sum_m R_m(0),0); a(0)=1 and b is the literal q4096 mean',
 raw_selected_core_x_exact=str(major),core_lambda_enclosure=list(lambda0),witness_y_exact_product_interval=py_exact_box,witness_y_outward_interval=[float(v)for v in py],
 continuous_squared_distance_lower=worst,continuous_distance_lower=distance,threshold_exact='19/20',strictly_exceeds_threshold=Fraction.from_float(distance)>Fraction(19,20),
 maximum_whole_angle_second_bound=maxB2,max_transform_interval_width=maxwidth,trigonometric_degree_bound=band,angular_discount_lower=discount,
 means_recomputed=False,unchanged_normalized_image=True,mirror_same_distance_because_witness_z_zero=True,closed_held_claim=False,constructed_flex_member_claim=False,
 strict_under_stated_IEEE_arithmetic=True,per_cell=records,seconds=time.perf_counter()-start)
a.out.write_bytes(gzip.compress((json.dumps(out,indent=2)+'\n').encode(),mtime=0))
print(json.dumps({k:v for k,v in out.items()if k!='per_cell'}),flush=True);print(json.dumps(dict(output=str(a.out),sha256=sha(a.out))),flush=True)
