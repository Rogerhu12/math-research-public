#!/usr/bin/env python3
"""Finite resolved normal acceleration with exact pointwise tangent projection and a fixed initial high-mode lift."""
import argparse
import importlib.util
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
old=module(Path(__file__).parent/'2ecf-polar-geodesic-material-physical-shooting.py','geodesic_original')
base=old.base
def smooth(x,m):
    coeff=np.fft.rfft(x,axis=-2);coeff[...,m+1:,:]=0.
    return np.fft.irfft(coeff,n=x.shape[-2],axis=-2)
def projected(P,T,k,lift,m):
    D,n,w=old.geometry(P,T);C=smooth(k[...,None]*n,m)+lift
    E=old.dot(T,T);r=old.dot(T,C)/E
    return C-T*r[...,None],(D,n,w,C,E,r)
def backward(P,T,k,cache,b,m):
    D,n,w,C,E,r=cache
    bt=old.dot(b,T)/E
    bc=b-T*bt[...,None]
    bT=-b*r[...,None]-C*bt[...,None]+2*T*(r*bt)[...,None]
    bk_vec=smooth(bc,m)
    bn=k[...,None]*bk_vec
    bw=(bn-n*old.dot(n,bn)[...,None])/w[...,None]
    return -old.du(np.cross(bw,T)),bT+np.cross(D,bw),old.dot(n,bk_vec)
def lift_from(P,T,k,t,m):
    D,n,w=old.geometry(P,T);A=k[...,None]*n
    return (1-t**3*(10+t*(-15+6*t)))[...,None,None]*(A-smooth(A,m))
class Filtered(old.Shooting):
    def __init__(self,a,N,radials,ends,ref):
        super().__init__(a,N,radials,ends,ref)
        if a.cut>=N//2:raise ValueError('Resolved shape filter must be strictly below grid Nyquist')
        self.cut=a.cut;t=(self.half-self.half[0])/(self.half[-1]-self.half[0])
        self.lift=lift_from(self.y0[0],self.y0[1],self.k0[0],t,a.cut)
    def field(self,x):
        k=self.k0+(self.B@x.reshape(self.B.shape[1],self.C.shape[1]))@self.C.T
        path=[self.y0];mid=[]
        for i in range(len(self.ns)-1):
            y=path[-1];a0,_=projected(y[0],y[1],k[2*i],self.lift[2*i],self.cut)
            half=y+.5*self.step*np.stack([y[1],a0])
            am,_=projected(half[0],half[1],k[2*i+1],self.lift[2*i+1],self.cut)
            path.append(y+self.step*np.stack([half[1],am]));mid.append(half)
        return np.stack(path),np.array(mid),k
    def value(self,x,gradient=True):
        Y,mid,kval=self.field(x);P,T=Y[:,0],Y[:,1]
        A,cache=projected(P,T,kval[::2],self.lift[::2],self.cut)
        j=np.stack([P,T,cache[0],A,old.du(T),old.du(P,2)],axis=1)
        pt=self.point.PointLinearized(j.swapaxes(1,2),self.f,self.cfg,self.weights);ar=self.area.AreaPacket(j,self.f,self.weights['metric'],.5)
        dif=j[-1]-self.target
        phys=float(np.vdot(pt.residual,pt.residual)+np.vdot(ar.residual,ar.residual))
        end=float(np.sum(self.port_weights[:,None]*old.dot(dif,dif))/self.N)
        loss=phys+end+self.a.reg*np.mean(x*x)
        if not gradient:
            return dict(physical=phys,endpoint=end,total=loss,rawEndMax=[float(z) for z in np.max(np.linalg.norm(dif,axis=-1),axis=1)],rawE=float(np.max(abs(pt.metric[...,0]))),rawMixedNormalized=float(np.max(abs(pt.metric[...,1])/np.sqrt(2))),rawG=float(np.max(abs(pt.metric[...,2]))),minJacobian=float(np.min(pt.curvature['w'])))
        g=2*pt.vjp(pt.residual).swapaxes(1,2);gs,gu=ar.vjp(2*ar.residual);g[:,1]+=gs;g[:,2]+=gu
        g[-1]+=2*self.port_weights[:,None,None]*dif/self.N
        p,t,k=backward(P,T,kval[::2],cache,g[:,3],self.cut)
        bp=g[:,0]-old.du(g[:,2])+old.du(g[:,5],2)+p
        bt=g[:,1]-old.du(g[:,4])+t
        bk=np.zeros_like(kval);bk[::2]=k;bar=np.stack([bp[-1],bt[-1]])
        for i in reversed(range(len(mid))):
            bmid=self.step*bar;half=mid[i];left=Y[i]
            cc=projected(half[0],half[1],kval[2*i+1],self.lift[2*i+1],self.cut)[1]
            dp,dt,dk=backward(half[0],half[1],kval[2*i+1],cc,bmid[1],self.cut)
            bk[2*i+1]+=dk;bm=np.stack([dp,dt+bmid[0]])
            cc=tuple(q[i] for q in cache);bleft=.5*self.step*bm
            dp,dt,dk=backward(left[0],left[1],kval[2*i],cc,bleft[1],self.cut)
            bk[2*i]+=dk;bar+=bm+np.stack([dp+bp[i],dt+bleft[0]+bt[i]])
        return loss,(self.B.T@bk@self.C).ravel()+2*self.a.reg*x/len(x)

def run(a):
    dest=a.output;old.Shooting=Filtered
    def jets(P,T,k):
        t=np.linspace(0,1,len(P));lift=lift_from(P[0],T[0],k[0],t,a.cut)
        A,c=projected(P,T,k,lift,a.cut)
        return np.stack([P,T,c[0],A,old.du(T),old.du(P,2)],axis=1)
    old.jet=jets
    with TemporaryDirectory(dir=dest.parent) as tmp:
        p=Path(tmp)/'design.json';a.output=p;old.design(a);q=base.read(p)
    q.update(projectedGeodesicEntrySHA256=base.sha(__file__),cutoff=a.cut,equation='resolved normal acceleration plus inherited initial high modes, project onto sphere tangent; F is not identically zero in this regularized equation')
    base.stores(dest,q)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','seed-design','donor','input-field','frozen','field','output'):p.add_argument('--'+k,type=Path,required=True)
    for k,v in [('angles',64),('radials',96),('spans',9),('modes',5),('iterations',85),('fine-angles',192),('fine-radials',384),('cells',96),('stored-modes',80),('cut',12)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('position',180.),('velocity',26.),('reg',1e-5),('geometry',5.),('curvature',.5)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
