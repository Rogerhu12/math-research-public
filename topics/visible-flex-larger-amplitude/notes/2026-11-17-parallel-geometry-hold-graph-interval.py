#!/usr/bin/env python3
"""Reuse the identical 498 old cells and certify 1600 new hold graph cells.

R640/R642 apply literally on the common exact binary prefix. Only the new
HoldProfile domain [.995,1.02] is enclosed here, including its true finite
N4096 speed mean and the lambda_s term. Raw/normalized graph criteria are
separate; neither implies a closed surface, full metric bound, or reach.
"""
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
for k in ('topic','input','old-input','out'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--radial-subdivisions',type=int,default=4)
a=p.parse_args();N=4096;n=a.radial_subdivisions;first=498
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path,name,expected):
 if sha(path)!=expected:raise ValueError('Frozen dependency changed')
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
ip=a.topic/'scripts/parallel_20261117_arclength_interval_positive.py'
hp=a.topic/'notes/2026-11-17-parallel-geometry-normalization-interval-tools.py'
ish='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
hsh='a685b93e888e55e8b2dc4e0505e977a6ac0f2db88c18f2db2b5889d6a7dd02d8'
input_sha='aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15'
old_sha='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
if sha(a.input)!=input_sha or sha(a.old_input)!=old_sha:raise ValueError('Fixed raw input changed')
I=load(ip,'hold_interval_arithmetic',ish);H=load(hp,'hold_interval_helpers',hsh)
np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
start=time.perf_counter();source_sha=sha(__file__)
d=json.loads(gzip.decompress(a.input.read_bytes()));old=json.loads(gzip.decompress(a.old_input.read_bytes()))
M=d['M'];nu=2*np.arange(M+1)
if M!=320 or d['N']!=N or old['M']!=M or old['N']!=N or n!=4:raise ValueError('Fixed orders and four subcells required')
blocks=[]
for key in ('mesh','states','rhs','d2'):
 v=np.ascontiguousarray(d[key][:first+1],dtype='<f8');w=np.ascontiguousarray(old[key][:first+1],dtype='<f8')
 if v.shape!=w.shape or v.tobytes()!=w.tobytes():raise ValueError('Old node jets differ: '+key)
 blocks.append(v.tobytes())
prefix_sha=hashlib.sha256(b''.join(blocks)).hexdigest()
if d['fixed_scalar_profile']!=old['fixed_scalar_profile'] or d['analytic_extension_origin']!=old['analytic_extension_origin'] or old['inward_scalar_profile']['cut']!=d['hold_scalar_profile']['cut']:
 raise ValueError('Old exact scalar definitions differ')
del old,blocks,v,w
x=np.asarray(d.pop('mesh'));Y=np.asarray(d.pop('states'));D=np.asarray(d.pop('rhs'));DD=np.asarray(d.pop('d2'))
if len(x)!=2099 or not np.isfinite(x).all() or np.any(np.diff(x)<=0) or x[0]!=0 or x[first]!=.995 or x[-1]!=1.02:raise ValueError('Wrong complete hold domain')
if any(z.shape!=(len(x),3*M+2) or not np.isfinite(z).all() for z in (Y,D,DD)):raise ValueError('Full common jets required')
jet_sha=hashlib.sha256(b''.join(np.ascontiguousarray(z,dtype='<f8').tobytes()for z in (x,Y,D,DD))).hexdigest()
geom=d['fixed_scalar_profile']['geometry'];origin=d['analytic_extension_origin'];last=geom['knots'][-1];s=d['hold_scalar_profile']
if origin!=.99 or last['s']!=origin or (s['cut'],s['negative_curvature'],s['fall'],s['hold'],s['rise'],s['positive_curvature'])!=(.995,-2.5,.002,.02,.02,1.5):
 raise ValueError('Incorrect HoldProfile scalar')
K=I.div(I.neg(I.exact(last['app'])),I.sqrt(I.sub(I.exact(1.),I.square(I.exact(last['ap'])))))
if not (0<K[0] and K[1]<2.5):raise ValueError('The |a_ss|<=2.5 envelope is unavailable')
# All hold ramps stay between their endpoint curvatures in [-2.5,K].
# Thus |a_ss|=|kappa*cos(alpha)|<=2.5 throughout [.99,1.02].
def scalar_box(lo,hi):
 delta=(max(0.,float(I.down(lo-origin))),max(0.,float(I.up(hi-origin))))
 r=float(I.scale(I.square(delta),1.25)[1]);rp=float(I.scale(delta,2.5)[1])
 av=I.add(I.add(I.exact(last['a']),I.scale(delta,last['ap'])),(-r,r))
 ap=I.add(I.exact(last['ap']),(-rp,rp));return av,ap

tr=I.Transform(N)
def split(b):
 work=b;left=[I.at(work,0)];right=[I.at(work,-1)]
 for _ in range(5):
  work=I.scale(I.add(I.at(work,slice(None,-1)),I.at(work,slice(1,None))),.5)
  left.append(I.at(work,0));right.append(I.at(work,-1))
 return I.stack(left),I.stack(list(reversed(right)))
def parts(b):return [out for half in split(b)for out in split(half)]
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
def bounds(z,keys):
 vals=I.sum_upper(I.absolute_upper(I.stack([z[k]for k in keys])),axis=-1).max(axis=-1)
 return {k:float(v)for k,v in zip(keys,vals)}
def prod(*v):
 z=I.exact(1.)
 for q in v:z=I.mul(z,I.exact(q))
 return float(z[1])
def total(*v):return float(I.sum_upper(np.array(v)))
def expand(target,z):
 target[0]=min(target[0],float(np.min(z[0])));target[1]=max(target[1],float(np.max(z[1])))
keys=('radius_squared','A','C','C_G');worst={k:dict(value=float('inf'))for k in keys}
ranges={k:[float('inf'),-float('inf')]for k in ('a','a_s','b','b_s','lambda','lambda_s')}
minq=float('inf');maxwidth=0.;records=[]
for i in range(first,len(x)-1):
 h=I.sub(I.exact(x[i+1]),I.exact(x[i]))
 b,vb=H.hermite_bezier(I,(Y[i],D[i],DD[i]),(Y[i+1],D[i+1],DD[i+1]),h)
 f=channels(b);v=channels(vb)
 bf=bounds(f,('R','T','dr','dt','dz','er','et','ez','zm'));bv=bounds(v,('R','T','Z','dr','dt','dz'))
 Ab=total(prod(bf['R'],bf['dt']),prod(bf['T'],bf['dr']));Bb=total(prod(bf['R'],bv['T']),prod(bf['T'],bv['R']))
 Ap=total(prod(bf['R'],bf['et']),prod(bf['T'],bf['er']))
 Bp=total(prod(bf['dr'],bv['T']),prod(bf['dt'],bv['R']),prod(bf['R'],bv['dt']),prod(bf['T'],bv['dr']))
 Cp=total(prod(bv['dz'],Ab),prod(bv['Z'],Ap),prod(bf['ez'],Bb),prod(bf['dz'],Bp))
 Qp=total(prod(2,bf['R'],bf['dr']),prod(2,bf['T'],bf['dt']))
 co=tr.cosine_sine(I.stack([f['R'],f['dt'],v['R'],v['Z'],v['dt'],f['zm']]),N,'cos')
 si=tr.cosine_sine(I.stack([f['T'],f['dr'],f['dz'],v['T'],v['dr'],v['dz']]),N,'sin')
 grid=I.stack([I.at(co,0),I.at(si,0),I.at(si,1),I.at(co,1),I.at(si,2),I.at(co,2),I.at(si,3),I.at(co,3),I.at(si,4),I.at(co,4),I.at(si,5),I.at(co,5)])
 grid=tuple(q.transpose(1,0,2)for q in grid);maxwidth=max(maxwidth,float(I.up(grid[1]-grid[0]).max()))
 cvs=parts(I.at(vb,(slice(None),2*M+1)))
 row=dict(cell=i,left=float(x[i]),right=float(x[i+1]),lower={k:float('inf')for k in keys},lambda_interval=[float('inf'),-float('inf')],lambda_s_interval=[float('inf'),-float('inf')])
 for sub,bg in enumerate(parts(grid)):
  box=H.hull(bg);R,T,dr,dt,dz,vr,vt,vz,dvr,dvt,dvz,zm=[I.at(box,k)for k in range(12)]
  bm,bs=H.speed_mean_jets(I,(dr,dt,dz),(dvr,dvt,dvz))
  q=I.sqrt(I.add(I.add(I.square(dr),I.square(dt)),I.square(dz)));minq=min(minq,float(q[0].min()))
  sl=I.add(I.exact(x[i]),I.scale(h,sub/n));sr=I.add(I.exact(x[i]),I.scale(h,(sub+1)/n))
  av,ap=scalar_box(float(sl[0]),float(sr[1]));lam,lamp=H.scaling_jets(I,av,ap,bm,bs)
  if lam[0]<=0:raise ValueError('Positive normalization scale not paid')
  cs=H.hull(cvs[sub]);corr=I.add(I.mul(I.sub(I.exact(1.),lam),cs),I.mul(lamp,zm))
  AA=I.sub(I.mul(R,dt),I.mul(T,dr));BB=I.sub(I.mul(R,vt),I.mul(T,vr));CC=I.sub(I.mul(vz,AA),I.mul(dz,BB));QQ=I.add(I.square(R),I.square(T))
  l2=I.square(lam);CG=I.add(I.mul(I.mul(l2,lam),CC),I.mul(I.mul(l2,corr),AA))
  ll=float(I.absolute_upper(lam));lp=float(I.absolute_upper(lamp));ld=float(I.absolute_upper(I.sub(I.exact(1.),lam)))
  gb=total(prod(ld,float(I.absolute_upper(cs))),prod(lp,bf['zm']))
  Gp=total(prod(ll,ll,ll,Cp),prod(ll,ll,gb,Ap),prod(ll,ll,lp,bf['dz'],Ab))
  for key,val,deriv in zip(keys,(QQ,AA,CC,CG),(Qp,Ap,Cp,Gp)):
   loss=float(I.mul(I.div(I.exact(tr.pi_upper),I.exact(N)),I.exact(deriv))[1]);gl=float(val[0].min());lower=float(I.down(gl-loss))
   row['lower'][key]=min(row['lower'][key],lower)
   if lower<worst[key]['value']:worst[key]=dict(value=lower,cell=i,subcell=sub,left=float(x[i]),right=float(x[i+1]),radial_box_grid_lower=gl,angular_loss=loss,angular_derivative_bound=deriv)
  expand(row['lambda_interval'],lam);expand(row['lambda_s_interval'],lamp)
  for k,z in zip(ranges,(av,ap,bm,bs,lam,lamp)):expand(ranges[k],z)
 records.append(row)
 if len(records)%100==0:print(json.dumps(dict(event='new_cell_progress',new_cells=len(records),seconds=time.perf_counter()-start,lower={k:v['value']for k,v in worst.items()},lambda_s=ranges['lambda_s'])),flush=True)
if sha(__file__)!=source_sha or sha(a.input)!=input_sha or sha(a.old_input)!=old_sha or sha(ip)!=ish or sha(hp)!=hsh:raise ValueError('Frozen identity changed')
if not all(np.isfinite(z['value'])for z in worst.values()) or not all(np.isfinite(v).all()for v in ranges.values()):raise ValueError('Nonfinite certificate')
old_lower={k:float(I.div(I.exact(nu),I.exact(de))[0])for k,nu,de in [('radius_squared',117,625),('A',177,1000),('C',51,1000),('C_G',329,2000)]}
out=dict(scope=__doc__,source_sha256=source_sha,input_sha256=input_sha,old_input_sha256=old_sha,interval_dependency_sha256=ish,helper_sha256=hsh,
 nodal_jets_little_endian_float64_sha256=jet_sha,identical_prefix_nodes=first+1,identical_prefix_jets_sha256=prefix_sha,exact_old_scalar_same=True,reused_old_cells=first,new_cells=len(records),total_cells=len(x)-1,
 M=M,construction_angles=N,radial_subdivisions=n,scalar_origin=origin,scalar_K_interval=[float(z)for z in K],analytic_absolute_a_ss_bound=2.5,
 new_domain_continuous_lower_bounds=worst,new_domain_scalar_normalization_ranges=ranges,old_domain_proven_lower_bounds=old_lower,
 full_domain_continuous_lower_bounds={k:min(old_lower[k],worst[k]['value'])for k in keys},minimum_new_construction_speed_box=minq,max_transform_interval_width=maxwidth,
 raw_open_prefix_embedded=all(worst[k]['value']>0 for k in keys[:3]),normalized_open_prefix_embedded=all(worst[k]['value']>0 for k in ('radius_squared','A','C_G')) and ranges['lambda'][0]>0,
 strict_under_stated_IEEE_arithmetic=True,coordinates_C2_by='R638 section 6',previous_embedding_by='R640/R642 on the proved identical old prefix',closed_surface=False,reach_certified=False,
 per_new_cell=records,seconds=time.perf_counter()-start)
a.out.write_bytes(gzip.compress((json.dumps(out,indent=2)+'\n').encode(),mtime=0))
print(json.dumps({k:v for k,v in out.items()if k!='per_new_cell'}),flush=True);print(json.dumps(dict(output=str(a.out),sha256=sha(a.out))),flush=True)
