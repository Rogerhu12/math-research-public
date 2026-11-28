#!/usr/bin/env python3
"""Observe angular degree, material slab, centered ball, true cuff and candidate radial-height potentials on the whole selected physical meridian."""
import argparse,importlib.util,json,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,hstack
p=Path(__file__).with_name('2ecf-r262-m2-low-cap-stadium-active.py');sp=importlib.util.spec_from_file_location('lowst',p);s=importlib.util.module_from_spec(sp);sp.loader.exec_module(s);m=s.m
p=argparse.ArgumentParser()
for name in ('meridian','buffer','tail-table','state','out'):p.add_argument('--'+name,type=Path,required=True)
a=p.parse_args();d=json.loads(a.state.read_bytes());a.index=d['index'];z=m.Source(a);u0=d['epsilon'];sp,mo=d['spans'],d['modes'];x=np.array(d['xyz']);m.support=lambda R,e,u:s.stadium_center(R,e,u,d['stadiumPower'],d['stadiumMix']);j0=m.jet
def jet(rows,u,eps,linear=True):
    t=rows.copy();t[:,[7,9,11]]*=d['horizontalLinearScale'];t[:,[8,10,12]]*=d['verticalLinearScale'];return j0(t,u,eps,linear)
m.jet=jet;data=[];narrow=[]
rows,u=z.grid(375,178,True)
for i in range(0,len(rows),80):
    rr=rows[i:i+80];g=m.Fit(z,rr,u,u0,sp,mo);P,Ps,Pu,*_=g.field(x).swapaxes(0,1);xy=P[...,:2];r=np.linalg.norm(xy,axis=-1);det=lambda a,b:a[...,0]*b[...,1]-a[...,1]*b[...,0];A=det(xy,Pu[...,:2]);B=det(xy,Ps[...,:2]);U=Ps-Pu*(B/A)[...,None];dr=m.base.dot(xy,U[...,:2])/r;dz=U[...,2];data.append(np.column_stack([r.ravel(),dr.ravel(),dz.ravel(),(A/r**2).ravel()]));j,k=np.unravel_index(np.argmax(abs(P[...,1])),r.shape);narrow.append([float(abs(P[j,k,1])),float(rr[j,0]),float(u[k]),P[j,k].tolist()]);
r,dr,dz,tu=np.vstack(data).T;res=[]
for n in (8,18,32):
    lb=r.min()-.01;ub=r.max()+.01;knots=np.r_[np.full(4,lb),np.linspace(lb,ub,n+1)[1:-1],np.full(4,ub)];J=BSpline.design_matrix(r,knots,3);G=hstack([-J.multiply(dr[:,None]),csr_matrix(np.ones((len(r),1)))],format='csr');obj=np.r_[np.zeros(J.shape[1]),-1.];lp=linprog(obj,A_ub=G,b_ub=dz,bounds=[(-10,10)]*J.shape[1]+[(None,None)],method='highs');assert lp.success;v=dz+dr*(J@lp.x[:-1]);res.append(dict(spans=n,lower=float(v.min()),maxAbsCoefficient=float(abs(lp.x[:-1]).max()),weights=lp.x[:-1].tolist()))
out=dict(entry=m.base.sha(__file__),state=m.base.sha(a.state),grid=[len(rows),len(u)],minThetaU=float(tu.min()),maxThetaU=float(tu.max()),minHeightDerivativeAtPolarAngle=float(dz.min()),maxHeightDerivativeAtPolarAngle=float(dz.max()),slabMaximum=max(narrow),fits=res)
with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['minThetaU'],out['minHeightDerivativeAtPolarAngle'],out['slabMaximum'],[q['lower'] for q in res])
