#!/usr/bin/env python3
"""Locate actual Cartesian principal-curvature peaks of a saved neck prefix.

Reads the saved C2 finite map and all coefficient chunks. It does not solve
a new BVP, alter the metric, or replace the map by its background surface.
Sampling plus local optimization is diagnostic, not a continuous bound.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_curvature_pullback',P/'geometric-checkpoint-core-pullback.py');pb=importlib.util.module_from_spec(sp);sp.loader.exec_module(pb)

def principal(A,B,AA,AB,BB):
 E=np.sum(A*A,axis=-1);F=np.sum(A*B,axis=-1);G=np.sum(B*B,axis=-1);n=np.cross(A,B);n/=np.linalg.norm(n,axis=-1)[...,None]
 L=np.sum(AA*n,axis=-1);M=np.sum(AB*n,axis=-1);N=np.sum(BB*n,axis=-1);D=E*G-F*F;tr=(L*G-2*M*F+N*E)/D;det=(L*N-M*M)/D
 disc=np.sqrt(np.maximum(0,tr*tr-4*det));p=(tr+disc)/2;q=(tr-disc)/2;kap=np.maximum(abs(p),abs(q))
 # Orthonormal basis: latitude tangent second, its orthogonal meridian first.
 norm=E-F*F/G;LL=(L-2*F/G*M+(F/G)**2*N)/norm;MM=(M-F/G*N)/np.sqrt(norm*G);NN=N/G
 sign=np.where(NN>=0,1.,-1.)
 return kap,p,q,LL*sign,MM*sign,NN*sign

def label(seg,loop_begin,bridge=False):
 if bridge:return 'terminal bridge '+seg['kind']
 if seg['kind']in('hermite','boost'):return seg['kind']
 if seg['s0']>=loop_begin-1e-11:
  if seg['kind']=='turn':return 'loop outward turn'if seg['p1']>seg['p0']else'loop inward turn'
  return 'loop outward coast'if seg['p0']>0 else'loop inward coast'
 if seg['kind']=='turn':return 'first descending turn'if seg['p0']>0 else'descending speed sync'
 return 'outward coast'if seg['p0']>0 else'descending coast'

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=Path,required=True);p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--angular',type=int,default=512);p.add_argument('--radial',type=int,default=1201);p.add_argument('--out',type=Path,required=True);a=p.parse_args();start=time.time();saved,_=pb.load_saved(a.input,a.source_topic,a.port,a.angular);f=saved.flow;N=a.angular;B,B1,B2=f.basis(N);pre=f._alternative_neck
 segments=[]
 for i,seg in enumerate(pre.segments):segments.append(dict(index=i,label=label(seg,pre.loop_begin),lo=seg['s0'],hi=seg['s1'],kind=seg['kind']))
 for i,seg in enumerate(f.bridge.segments):segments.append(dict(index=len(pre.segments)+i,label=label(seg,pre.loop_begin,True),lo=pre.end+seg['s0'],hi=pre.end+seg['s1'],kind=seg['kind']))
 ss=np.unique(np.r_[np.linspace(0,f.end,a.radial),saved.sol.x,(saved.sol.x[:-1]+saved.sol.x[1:])/2,f.breaks]);best={}
 for first in range(0,len(ss),24):
  s=ss[first:first+24];Y=saved.sol.sol(s);Yp=saved.sol.sol(s,1);Ypp=saved.sol.sol(s,2);fr,Fsp,dW=f.velocity_s(s,Y,Yp,B1,B2);g=fr['geo']
  Fs=g['s1']+saved.q*f.values(Yp,B);Fs[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
  Fss=g['s2']+saved.q*f.values(Ypp,B);Fss[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
  vals=principal(Fs,fr['d'],Fss,Fsp,fr['dd']);kap=vals[0]
  for row,si in enumerate(s):
   seg=next((q for q in segments if q['lo']-1e-12<=si<=q['hi']+1e-12),segments[-1]);j=int(np.argmax(kap[row]));data=dict(segment=seg['index'],label=seg['label'],s=float(si),psi=float(2*np.pi*j/N),kappa=float(kap[row,j]))
   if seg['index']not in best or data['kappa']>best[seg['index']]['kappa']:best[seg['index']]=data
 def one(x):
  s=np.array([float(x[0])]);psi=np.array([[float(x[1])]]);Y=saved.sol.sol(s);Yp=saved.sol.sol(s,1);fr,_,dW=f.velocity_s(s,Y,Yp,B1,B2);Hp=np.mean(fr['V'][:,:,2],axis=1);Hpp=np.mean(dW[:,:,2],axis=1);jets=saved.jets(s,psi,(np.zeros(1),Hp,Hpp));vals=principal(jets['s1'],jets['p1'],jets['s2'],jets['sp'],jets['p2']);return [float(v[0,0])for v in vals]
 rows=[]
 for seg in segments:
  if seg['index']not in best:continue
  row=best[seg['index']];x=np.array([row['s'],row['psi']]);half=max((seg['hi']-seg['lo'])/10,2e-5);lo=max(seg['lo'],x[0]-half);hi=min(seg['hi'],x[0]+half)
  z=minimize(lambda y:-one(y)[0],x,method='Nelder-Mead',bounds=[(lo,hi),(x[1]-.08,x[1]+.08)],options=dict(xatol=2e-10,fatol=2e-10,maxiter=180))
  if -z.fun>row['kappa']:row.update(s=float(z.x[0]),psi=float(z.x[1]),kappa=float(-z.fun))
  value=one([row['s'],row['psi']]);aa,v,acc=f.profile([row['s']]);g=saved.angle(np.array([row['s']]),np.array([[row['psi']]]));row.update(principal_signed=value[1:3],meridian_normal_curvature=value[3],mixed_normal_curvature=value[4],latitude_normal_curvature=value[5],material_theta=float(g['theta'][0,0]),a=float(aa[0]),ap=float(v[0]),app=float(acc[0]),background_meridian_curvature=float(abs(acc[0])/np.sqrt(1-v[0]**2)),segment_bounds=[seg['lo'],seg['hi']]);rows.append(row)
 rows.sort(key=lambda z:-z['kappa']);top=rows[0];sj=np.array([top['s']]);H,Hp,Hpp=saved.height_jets(sj,angular=N);jet=saved.jets(sj,np.array([[top['psi']]]),(H,Hp,Hpp));top['XYZ']=jet['pos'][0,0].tolist()
 report=dict(scope=__doc__,input=str(a.input),input_sha256=hashlib.sha256(a.input.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),config=dict(angular=N,radial=a.radial),sampled_radial_count=len(ss),frozen_profile=saved.rec['frozen_profile'],meridian_length=f.end,rows=rows,seconds=time.time()-start)
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(seconds=report['seconds'],top=rows[:5])))
if __name__=='__main__':main()
