#!/usr/bin/env python3
"""Implicit three-component closure of real unit material tangents; differentiate the actual multiplier."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import os
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[name]='1'
import numpy as np
from scipy.interpolate import BSpline
def module(path):
    spec=importlib.util.spec_from_file_location('mat_spherical_base',path)
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m
old=module(Path(__file__).parent/'2ecf-polar-material-curve-coupled-spherical-design.py')

def dot(a,b):
    return np.einsum('...c,...c->...',a,b)
def Japply(t,q,v):
    return (v-t*dot(t,v)[...,None])/q[...,None]

class Implicit(old.Model):
    def starting(self):
        if self.args.start is None:return super().starting()
        o=old.read(self.args.start)
        assert o['seedFieldSHA256']==old.sha(self.args.seed_field) and o['preparedSHA256']==old.sha(self.args.prepared)
        cfg=o['spans'];M=o['modes'];x=np.asarray(o['coefficients'])
        kn=np.r_[np.zeros(4),np.arange(1,cfg)/cfg,np.ones(4)]
        B=BSpline(kn,np.eye(len(kn)-4),3)(self.t)[:,2:-2]
        count=B.shape[1]*(M+1)
        out=[]
        for j,(a,F) in enumerate(zip((x[:count].reshape(B.shape[1],-1),x[count:].reshape(B.shape[1],-1)),self.F)):
            f=np.cos(self.u[:,None]*2*np.arange(M+1)) if j==0 else np.sin(self.u[:,None]*2*np.arange(1,M+1))
            amp=np.linalg.lstsq(self.B,B@a@f.T,rcond=1e-12)[0]
            out.append(np.linalg.lstsq(F,amp.T,rcond=1e-12)[0].T.ravel())
        return np.concatenate(out)

    def directions(self,x):
        single=[];der=[]
        for mat,(h,hp),F in zip(self.unpack(x),self.base,self.F):
            c=mat@F.T;single.append(h+self.B@c);der.append(hp+self.D@c)
        tang=old.sphere(*single)
        Ts=tang[1]*der[0][...,None]+tang[2]*der[1][...,None]
        return tang,der,Ts

    def close(self,T):
        t=self.t
        h=(16*t*t*(1-t)**2)[:,None,None]
        hp=(32*t*(1-t)*(1-2*t)/self.L)[:,None,None]
        v=self.v
        w=self.I[-1,:,None]*v
        target=old.local(self.P1-self.P0,self.u)
        xi=np.zeros_like(target)
        eye=np.eye(3)
        for it in range(45):
            Q=T+h*xi
            q=np.linalg.norm(Q,axis=-1)
            if np.min(q)<1e-7:raise ArithmeticError('Singular spherical tangent chart')
            U=Q/q[...,None]
            r=np.einsum('su,sui->ui',w,U)-target
            norms=np.linalg.norm(r,axis=-1)
            D=w*h[...,0]/q
            H=np.einsum('u,ij->uij',np.sum(D,axis=0),eye)-np.einsum('su,sui,suj->uij',D,U,U,optimize=True)
            if np.max(norms)<7e-13:break
            d=np.linalg.solve(H,r[...,None])[...,0]
            step=np.ones(len(self.u))
            active=norms>=7e-13
            for _ in range(35):
                trial=xi-step[:,None]*d
                W=T+h*trial
                l=np.linalg.norm(W,axis=-1)
                Utrial=W/np.maximum(l,1e-100)[...,None]
                rr=np.linalg.norm(np.einsum('su,sui->ui',w,Utrial)-target,axis=-1)
                bad=active&((rr>(1-1e-4*step)*norms)|(np.min(l,axis=0)<1e-7))
                if not np.any(bad):break
                step[bad]*=.5
            else:raise ArithmeticError('No regular angular multiplier backtrack')
            xi[active]-=step[active,None]*d[active]
        else:raise ArithmeticError('Incomplete actual three-component closure')
        Hmin=float(np.min(np.linalg.eigvalsh(H)))
        self.last=dict(maxPhysicalClosure=float(max(norms)),minNormBeforeNormalization=float(np.min(q)),minMultiplierHessianEigenvalue=Hmin,maximumMultiplier=float(np.max(np.linalg.norm(xi,axis=-1))),newtonIterations=it)
        return U,q,H,xi,h,hp,r

    def field(self,x):
        tang,der,Ts=self.directions(x)
        U,q,H,xi,h,hp,r=self.close(tang[0])
        Qs=Ts+hp*xi
        Us=Japply(U,q,Qs)
        V=old.world(self.v[...,None]*U,self.u)
        A=old.world(self.vd[...,None]*U+self.v[...,None]*Us,self.u)
        P=self.P0+np.einsum('ij,juc->iuc',self.I,V,optimize=True)
        return P,V,A,-old.world(r,self.u),(tang,der,U,q,Qs,Us,H,h,hp)

    def value(self,x,with_gradient=True):
        P,V,A,delta,stuff=self.field(x)
        jets=np.stack([P,V,old.angular(P,1),A,old.angular(V,1),old.angular(P,2)],axis=1)
        pt=self.point.PointLinearized(jets.swapaxes(1,2),self.rad,self.cfg,self.weights)
        ar=self.area.AreaPacket(jets,self.rad,self.weights['metric'],.5)
        loss=float(np.vdot(pt.residual,pt.residual)+np.vdot(ar.residual,ar.residual))
        if not with_gradient:
            return dict(collocationGeometricObjective=loss,closurePenalty=0.,maxThreeComponentRepair=0.,designTotal=loss,**self.last)
        g=2*pt.vjp(pt.residual).swapaxes(1,2)
        gs,gu=ar.vjp(2*ar.residual);g[:,1]+=gs;g[:,2]+=gu
        bp=g[:,0]-old.angular(g[:,2],1)+old.angular(g[:,5],2)
        bv=g[:,1]-old.angular(g[:,4],1)
        bV=old.local(np.einsum('ij,iuc->juc',self.I,bp,optimize=True)+bv,self.u)
        bA=old.local(g[:,3],self.u)
        tang,der,U,q,Qs,Us,H,h,hp=stuff
        bUs=self.v[...,None]*bA
        bU=self.v[...,None]*bV+self.vd[...,None]*bA-(bUs*dot(U,Qs)[...,None]+Qs*dot(bUs,U)[...,None])/q[...,None]
        bQ=Japply(U,q,bU)-U*(dot(bUs,Us)/q)[...,None]
        bQs=Japply(U,q,bUs)
        multiplier=np.linalg.solve(H,np.sum(h*bQ+hp*bQs,axis=0)[...,None])[...,0]
        bT=bQ-(self.I[-1,:,None]*self.v)[...,None]*Japply(U,q,multiplier[None])
        T,Tp,Tb,Tpp,Tpb,Tbb=tang
        ps,bs=der;parts=[]
        for F,dT,dTp,dTb in ((self.F[0],Tp,Tpp,Tpb),(self.F[1],Tb,Tpb,Tbb)):
            ga=dot(bT,dT)+dot(bQs,dTp*ps[...,None]+dTb*bs[...,None])
            gd=dot(bQs,dT)
            parts.append(((self.B.T@ga+self.D.T@gd)@F).ravel())
        return loss,np.concatenate(parts)

def run(args):
    dest=args.output
    if dest.exists():raise FileExistsError(dest)
    old.Model=Implicit
    with TemporaryDirectory(dir=dest.parent) as temp:
        args.output=Path(temp)/'run.json'
        if args.mode=='design':old.design(args)
        else:old.observe(args)
        result=old.read(args.output)
    if args.mode=='design':
        result['baseSphericalDesignSHA256']=result['entrySHA256']
        result['entrySHA256']=old.sha(__file__)
        result['startSHA256']=None if args.start is None else old.sha(args.start)
        result['schema']='actual-unit-material-spherical-direction-implicit-physical-closure-v1'
        result['threeComponentEndpointPositionRepairApplied']=False
        result['denseEndpointClosureMax']=result.pop('denseMaximumRepair')
    else:
        result['implicitSupplierSHA256']=old.sha(__file__)
    old.stores(dest,result)

if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','field','output','seed-field','seed-design','design','independent','start'):
        a.add_argument('--'+k,type=Path)
    for k,v in [('angles',96),('radials',65),('spans',12),('modes',8),('iterations',180),('fine-radials',513),('fine-angles',256),('cells',64),('stored-modes',80),('trace-nodes',2048)]:
        a.add_argument('--'+k,type=int,default=v)
    for k,v in [('closure',0.),('curvature',.75),('geometry',45.)]:
        a.add_argument('--'+k,type=float,default=v)
    run(a.parse_args())
