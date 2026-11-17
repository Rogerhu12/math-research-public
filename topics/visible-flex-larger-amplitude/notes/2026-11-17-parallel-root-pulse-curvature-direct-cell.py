#!/usr/bin/env python3
"""Continuous raw-field curvature bound on selected unchanged pulse cells.

Bernstein products retain radial correlations. Scalar invariant angular Taylor
boxes use directly differentiated invariant polynomials and a trigonometric
Bernstein cover for their second derivatives. This concerns the raw field, not its normalized image G.
"""
import argparse,gzip,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(a):
 start=time.perf_counter();source_sha=sha(__file__)
 expected='26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72'
 dep='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
 if sha(a.input)!=expected or sha(a.interval_source)!=dep:raise ValueError('Frozen input/source changed')
 sp=importlib.util.spec_from_file_location('curv_interval',a.interval_source);I=importlib.util.module_from_spec(sp);sp.loader.exec_module(I)
 np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
 d=json.loads(gzip.decompress(a.input.read_bytes()));M=d['M'];Q=a.angles
 x=np.asarray(d['mesh']);Y=np.asarray(d['states']);D=np.asarray(d['rhs']);DD=np.asarray(d['d2'])
 if M!=320 or Q<=12*M or Q&(Q-1) or a.radial_subdivisions<1 or a.radial_subdivisions&(a.radial_subdivisions-1):raise ValueError('Bad dyadic grids')
 if not np.isfinite(x).all() or not(np.diff(x)>0).all()or any(z.shape!=(len(x),3*M+2)or not np.isfinite(z).all()for z in(Y,D,DD)):raise ValueError('Bad finite jets')
 tr=I.Transform(Q);nu=2*np.arange(M+1)
 step=I.div(I.exact(tr.pi_upper),I.exact(Q));halfstep2=I.scale(I.square(step),.5)
 def add(v,w):return I.add(v,w)
 def product(v,w):
  m=len(v[0])-1;n=len(w[0])-1;out=[]
  for k in range(m+n+1):
   z=I.exact(np.zeros(Q))
   for j in range(max(0,k-n),min(m,k)+1):
    term=I.div(I.scale(I.mul(I.at(v,j),I.at(w,k-j)),math.comb(m,j)*math.comb(n,k-j)),I.exact(math.comb(m+n,k)))
    z=I.add(z,term)
   out.append(z)
  return I.stack(out)
 def dot(v,w):return I.add(I.add(product(v[0],w[0]),product(v[1],w[1])),product(v[2],w[2]))
 def cross(v,w):return [I.sub(product(v[(j+1)%3],w[(j+2)%3]),product(v[(j+2)%3],w[(j+1)%3]))for j in range(3)]
 def split(b):
  degree=len(b[0])-1;work=b;left=[I.at(work,0)];right=[I.at(work,-1)]
  for _ in range(degree):
   work=I.scale(I.add(I.at(work,slice(None,-1)),I.at(work,slice(1,None))),.5)
   left.append(I.at(work,0));right.append(I.at(work,-1))
  return I.stack(left),I.stack(list(reversed(right)))
 def prepend(v):return np.pad(v[0],((0,0),(1,0))),np.pad(v[1],((0,0),(1,0)))
 def channels(b):
  R=I.at(b,(slice(None),slice(0,M+1)));T=prepend(I.at(b,(slice(None),slice(M+1,2*M+1))));Z=I.at(b,(slice(None),slice(2*M+1,None)))
  dr=I.neg(I.add(I.scale(R,nu),T));dt=I.add(R,I.scale(T,nu));dz=I.neg(I.scale(Z,nu))
  er=I.neg(I.add(I.scale(R,nu*nu+1),I.scale(T,2*nu)))
  et=I.neg(I.add(I.scale(T,nu*nu+1),I.scale(R,2*nu)));ez=I.neg(I.scale(Z,nu*nu))
  return [list(zip([R,T,Z],['cos','sin','cos'])),list(zip([dr,dt,dz],['sin','cos','sin'])),list(zip([er,et,ez],['cos','sin','cos']))]
 def grid_jets(components):
  out=[[],[],[]]
  for c,parity in components:
   out[0].append(tr.cosine_sine(c,Q,parity))
   first=I.scale(c,-nu if parity=='cos'else nu)
   out[1].append(tr.cosine_sine(first,Q,'sin'if parity=='cos'else 'cos'))
   out[2].append(tr.cosine_sine(I.scale(c,-nu*nu),Q,parity))
  return out
 def dot_derivative(v,w,order):
  z=None
  for j in range(order+1):
   term=I.scale(dot(v[j],w[order-j]),math.comb(order,j));z=term if z is None else I.add(z,term)
  return z
 def cross_derivative(v,w,order):
  z=None
  for j in range(order+1):
   term=[I.scale(t,math.comb(order,j))for t in cross(v[j],w[order-j])]
   z=term if z is None else[I.add(u,t)for u,t in zip(z,term)]
  return z
 def angular_data(p,K):
  # The exact second derivative of every radial Bernstein coefficient is a
  # real trigonometric polynomial of degree K. R641 (6)-(7) bounds its
  # whole-circle maximum from this grid, independently of any FFT noise.
  discount=I.sub(I.exact(1.),I.scale(halfstep2,K*K))[0]
  if discount<=0:raise ValueError('Insufficient angular Bernstein cover')
  B2=float(I.div(I.exact(float(I.absolute_upper(p[2]).max())),I.exact(discount))[1])
  return p[0],p[1],B2
 def pieces(z):
  out=[z]
  for _ in range(a.radial_subdivisions.bit_length()-1):out=[y for p in out for y in split(p)]
  return out
 records=[]
 for i in a.cells:
  if not 0<=i<len(x)-1:raise ValueError('Bad cell')
  h=I.sub(I.exact(x[i+1]),I.exact(x[i]));h2=I.square(h)
  y0=I.exact(Y[i]);y1=I.exact(Y[i+1]);v0=I.mul(h,I.exact(D[i]));v1=I.mul(h,I.exact(D[i+1]));a0=I.mul(h2,I.exact(DD[i]));a1=I.mul(h2,I.exact(DD[i+1]))
  b=I.stack([y0,I.add(y0,I.div(v0,I.exact(5))),I.add(I.add(y0,I.div(I.scale(v0,2),I.exact(5))),I.div(a0,I.exact(20))),I.add(I.sub(y1,I.div(I.scale(v1,2),I.exact(5))),I.div(a1,I.exact(20))),I.sub(y1,I.div(v1,I.exact(5))),y1])
  db=I.div(I.scale(I.sub(I.at(b,slice(1,None)),I.at(b,slice(None,-1))),5),h)
  ddb=I.div(I.scale(I.sub(I.at(db,slice(1,None)),I.at(db,slice(None,-1))),4),h)
  cb,cdb,cddb=channels(b),channels(db),channels(ddb)
  V=grid_jets(cdb[0]);T=grid_jets(cb[1]);AA=grid_jets(cddb[0]);VT=grid_jets(cdb[1]);EE=grid_jets(cb[2])
  normal=[cross_derivative(V,T,j)for j in range(3)]
  definitions=dict(E=(V,V,4*M),F=(V,T,4*M),G=(T,T,4*M),e=(normal,AA,6*M),f=(normal,VT,6*M),g=(normal,EE,6*M))
  polynomials={key:([dot_derivative(v,w,j)for j in range(3)],K)for key,(v,w,K)in definitions.items()}
  angular={key:angular_data(*value)for key,value in polynomials.items()}
  parts={key:(pieces(v[0]),pieces(v[1]),v[2])for key,v in angular.items()}
  worst=0.;minE=float('inf');minW2=float('inf');address=None
  for j in range(a.radial_subdivisions):
   boxes={}
   for key,(ps,ds,B2)in parts.items():
    p=ps[j];dp=ds[j]
    center=(p[0].min(axis=0),p[1].max(axis=0));Dp=I.absolute_upper(dp).max(axis=0)
    loss=I.add(I.mul(step,I.exact(Dp)),I.mul(halfstep2,I.exact(B2)))[1]
    boxes[key]=(I.down(center[0]-loss),I.up(center[1]+loss))
   E,F,G,e,f,g=[boxes[k]for k in ('E','F','G','e','f','g')]
   W2=I.sub(I.mul(E,G),I.square(F));minE=min(minE,float(E[0].min()));minW2=min(minW2,float(W2[0].min()))
   if minE<=0 or minW2<=0:raise ValueError('Unpaid positive metric '+str((i,j,minE,minW2)))
   W=I.sqrt(W2);FE=I.div(F,E)
   B11=I.div(e,I.mul(W,E));B12=I.div(I.sub(f,I.mul(FE,e)),W2)
   B22=I.div(I.add(I.sub(g,I.scale(I.mul(FE,f),2)),I.mul(I.square(FE),e)),I.mul(W,I.sub(G,I.div(I.square(F),E))))
   u=I.exact(I.absolute_upper(B11));v=I.exact(I.absolute_upper(B22));w=I.exact(I.absolute_upper(B12))
   op=I.scale(I.add(I.add(u,v),I.sqrt(I.add(I.square(I.sub(u,v)),I.scale(I.square(w),4)))),.5)[1]
   idx=int(np.argmax(op));val=float(op[idx])
   if val>worst:worst=val;address=dict(radial_subcell=j,angle_grid_index=idx)
  row=dict(cell=i,left=float(x[i]),right=float(x[i+1]),raw_principal_curvature_upper=worst,metric_E_lower=minE,metric_determinant_lower=minW2,worst_address=address,angular_second_bounds={k:v[2]for k,v in angular.items()},seconds=time.perf_counter()-start)
  records.append(row);print(json.dumps(row),flush=True)
 if sha(__file__)!=source_sha or sha(a.input)!=expected or sha(a.interval_source)!=dep:raise ValueError('Input/source changed')
 out=dict(scope=__doc__,source_sha256=source_sha,input_sha256=expected,interval_source_sha256=dep,angles=Q,radial_subdivisions=a.radial_subdivisions,records=records,seconds=time.perf_counter()-start,full_prefix=False)
 a.out.write_text(json.dumps(out,indent=2)+'\n');print('report_sha256',sha(a.out),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('input','interval-source','out'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--cells',type=int,nargs='+',default=[817]);p.add_argument('--angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4)
 main(p.parse_args())
