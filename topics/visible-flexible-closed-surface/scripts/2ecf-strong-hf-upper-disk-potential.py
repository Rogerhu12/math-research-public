#!/usr/bin/env python3
"""Select physical-azimuth cubic potentials for the complete upper reference disk."""
import argparse,hashlib
from pathlib import Path
import sys,importlib.util,json,os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.optimize import linprog
from scipy.signal import resample
from scipy.integrate import cumulative_trapezoid
ap=argparse.ArgumentParser()
for key in ('scripts','ramp','coast','field','prepared','independent','output'):
    ap.add_argument('--'+key,type=Path,required=True)
ap.add_argument('--angles',type=int,default=1024)
args=ap.parse_args()
source=Path(__file__).with_name('2ecf-strong-hf-material-radial-clock.py')
spec=importlib.util.spec_from_file_location('upper_clocked_field',source)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
ns,u,ar,jets,_=m.data_g(args,'observer')
u=np.arange(args.angles)*2*np.pi/args.angles
f=m.Field(args,u);b,Sf=f.knots[[0,-1]]
ns0=np.linspace(b,Sf,385);old=resample(np.asarray(jets)[ns<b,:3],len(u),axis=2);mid=np.concatenate([f.at(np.broadcast_to(q[:,None],(len(q),len(u))))[:,:3] for q in np.array_split(ns0,32)])
r=np.linspace(.8,.0001,257)[:,None];cn,sn=np.cos(u)[None,:],np.sin(u)[None,:]
xx=r*cn;yy=r*sn;yt=np.linspace(0,.8,8193);v=np.clip((yt-.34)/.46,0,1);angle=.8746432018013935*v**5*(126-420*v+540*v*v-315*v**3+70*v**4);c0=np.r_[0,cumulative_trapezoid(np.cos(angle),yt)];h0=np.r_[0,cumulative_trapezoid(np.sin(angle),yt)];dy=np.clip((abs(yy)-.34)/.46,0,1);a=.8746432018013935*dy**5*(126-420*dy+540*dy*dy-315*dy**3+70*dy**4)*np.sign(yy)
y=np.interp(abs(yy),yt,c0)*np.sign(yy);z=.51-np.interp(abs(yy),yt,h0)
arr=lambda *v:np.stack(np.broadcast_arrays(*v),axis=-1)
tail=np.stack((arr(xx,y,z),arr(-cn,-sn*np.cos(a),sn*np.sin(a)),arr(-r*sn,r*cn*np.cos(a),-r*cn*np.sin(a))),axis=1)
def det(a,b):return a[:,:,0]*b[:,:,1]-a[:,:,1]*b[:,:,0]
P,V,U=np.concatenate((old,mid,tail)).swapaxes(0,1)
q=np.sum(P[:,:,:2]**2,axis=-1);J=det(P,U);K=det(P,V);a=np.mod(np.arctan2(P[:,:,1],P[:,:,0]),2*np.pi)
x=1.5*(q-.875);y=4*(P[:,:,2]-.375);dx=3*q*det(V,U)/J;dy=4*(V[:,:,2]-U[:,:,2]*K/J)
# Divide the tail derivative by 2r to avoid the pole degeneracy.
dx[-len(r):]/=(2*r);dy[-len(r):]/=(2*r)
for sep in (128,):
 for deg in (3,):
  mons=[(i,n-i) for n in range(1,deg+1) for i in range(n+1)];mat=np.stack([i*x**max(0,i-1)*y**j*dx+j*x**i*y**max(0,j-1)*dy for i,j in mons],axis=-1)
  mar=[];cs=[];w=2*np.pi/sep
  for j in range(sep):
   g=np.mod(a-(j+.5)*w+np.pi,2*np.pi)-np.pi;v=mat[abs(g)<w*.68];sol=linprog(np.r_[np.zeros(len(mons)),-1.],A_ub=np.c_[-v,np.ones(len(v))],b_ub=np.zeros(len(v)),bounds=[(-1,1)]*len(mons)+[(None,None)],method='highs')
   mar.append(sol.x[-1]);cs.append(sol.x[:-1].tolist())
  print('degree',deg,'minimum',min(mar),'small',np.argsort(mar)[:12],flush=True)
  def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
  out=dict(schema='whole-upper-disk-physical-azimuth-potentials-v1',fieldSHA256=sha(args.field),
      sourceSHA256=sha(Path(__file__)),preparedSHA256=sha(args.prepared),degree=deg,sectors=sep,
      monomials=mons,coefficients=cs,angularCandidates=args.angles,finiteMargins=mar,minimumFinite=min(mar),continuousProof=False)
  with args.output.open('x') as h:json.dump(out,h,separators=(',',':'));h.write('\n')
