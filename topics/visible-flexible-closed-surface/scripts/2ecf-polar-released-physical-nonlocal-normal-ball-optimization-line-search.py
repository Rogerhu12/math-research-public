#!/usr/bin/env python3
"""Optimize actual paired physical normal-ball inequalities over separated radial sheets and the full inner flat annulus."""
import argparse
import importlib.util
import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.optimize import minimize,OptimizeResult
from scipy.spatial import cKDTree
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
cart=module(here/'2ecf-polar-released-actual-cartesian-guarded-design.py','physical_nonlocal_cart')
ext=cart.ext;base=cart.base
class Pairs:
    def __init__(self,a,ns,u):
        self.a=a;ends,ref,self.b,self.S,self.T,rf,g=ext.setup(a)
        self.ns=np.r_[ns,self.T+np.linspace(.002,float(rf)-.32,11)]
        self.u=u;field=base.MaterialField(a.field,ends)
        self.ref=np.empty((len(self.ns),6,len(u),3))
        for i in range(0,len(ns),12):self.ref[i:min(i+12,len(ns))]=field.position(ns[i:i+12],u)
        for i in range(len(ns),len(self.ns)):
            p=ext.flat_port(u,.8+self.S-self.ns[i]);self.ref[i]=np.stack([p[k] for k in ('P','V','Pu','A','Vu','Puu')])
        self.basis=cart.Basis(self.ns,u,self.b,self.T,a.spans,a.modes);self.num=len(self.ns)*len(u)
        self.ipair=np.array([],dtype=np.int64);self.jpair=self.ipair.copy()
    def geometry(self,x):
        js=self.ref+self.basis.apply(x)
        p=js[:,0].reshape(-1,3);s=js[:,1].reshape(-1,3);u=js[:,2].reshape(-1,3)
        n=np.cross(s,u);v=np.linalg.norm(n,axis=1)
        if min(v)<=1e-14:raise ArithmeticError("Actual zero material normal")
        return js,p,s,u,n/v[:,None],v
    def update(self,x):
        js,p,*_=self.geometry(x);nr=np.repeat(self.ns,len(self.u));tree=cKDTree(p)
        # Directly query separated radial blocks. Avoid storing local-neighbor pairs.
        chunks=np.array_split(np.arange(len(self.ns)),15);allpairs=[]
        for i,first in enumerate(chunks):
            ix=np.arange(first[0]*len(self.u),(first[-1]+1)*len(self.u))
            for second in chunks[i+1:]:
                if self.ns[second[-1]]-self.ns[first[0]]<self.a.separation:continue
                jx=np.arange(second[0]*len(self.u),(second[-1]+1)*len(self.u))
                pairs=cKDTree(p[ix]).sparse_distance_matrix(cKDTree(p[jx]),self.a.neighbors,output_type='coo_matrix')
                pi=ix[pairs.row];pj=jx[pairs.col];pick=nr[pj]-nr[pi]>=self.a.separation
                if np.any(pick):allpairs.append(pi[pick]*len(p)+pj[pick])
        if self.ipair.size:allpairs.append(self.ipair*len(p)+self.jpair)
        enc=np.unique(np.concatenate(allpairs));self.ipair=enc//len(p);self.jpair=enc%len(p)
        print('actual pairs',len(enc),flush=True)
    def __call__(self,x,weight,gradient=True):
        js,p,s,u,n,v=self.geometry(x);i=self.ipair;j=self.jpair;d=p[j]-p[i]
        d2=np.sum(d*d,axis=1);L=np.sqrt(d2);ni=n[i];nj=n[j];di=np.sum(d*ni,axis=1);dj=np.sum(d*nj,axis=1)
        R=self.a.ball_radius
        vi=abs(di)-d2/(2*R);vj=abs(dj)-d2/(2*R)
        if self.a.pair_kind=='chord':
            ei=np.maximum(2*R-L,0);ej=np.zeros_like(ei)
        else:ei=np.maximum(vi,0.);ej=np.maximum(vj,0.)
        scale=weight/len(p)
        val=scale*(ei@ei+ej@ej)
        if not gradient:
            rat=d2/(2*np.maximum(1e-15,np.maximum(abs(di),abs(dj))));k=np.argmin(rat)
            return dict(loss=float(val),pairCount=len(i),maxBallViolation=float(max(0,np.max(vi),np.max(vj))),minNormalRatio=float(rat[k]),minDistance=float(np.min(L)),worst=[float(self.ns[idx//len(self.u)]) for idx in (i[k],j[k])]+[float(self.u[idx%len(self.u)]) for idx in (i[k],j[k])],positivePairCount=int(np.sum((ei>0)|(ej>0))))
        bi=2*scale*ei;bj=2*scale*ej
        if self.a.pair_kind=='chord':
            bd=-bi[:,None]*d/L[:,None];bi*=0
        else:
            bd=(bi*np.sign(di))[:,None]*ni+(bj*np.sign(dj))[:,None]*nj-((bi+bj)/R)[:,None]*d
        adj=np.zeros_like(js)
        def collect(index,vec):return np.stack([np.bincount(index,vec[:,k],minlength=len(p)) for k in range(3)],axis=1)
        gp=collect(j,bd)-collect(i,bd)
        gn=collect(i,(bi*np.sign(di))[:,None]*d)+collect(j,(bj*np.sign(dj))[:,None]*d)
        cross=(gn-n*np.sum(gn*n,axis=1)[:,None])/v[:,None]
        for k,z in enumerate((gp,np.cross(u,cross),np.cross(cross,s))):adj[:,k]=z.reshape(len(self.ns),len(self.u),3)
        return float(val),self.basis.transpose(adj)
def run(a):
    if a.mode=='observe':
        cart.run(a);return
    ends,ref,b,S,T,rf,g=ext.setup(a);ns=np.linspace(b,T,a.radials);u=2*np.pi*np.arange(a.angles)/a.angles
    pairs=Pairs(a,ns,u);outside=a.output;records=[]
    def solve(fun,x0,**opts):
        x=x0.copy();total=0
        cb0=opts['callback']
        for step,weight in enumerate(a.pair_weights):
            pairs.update(x)
            def merit(x):
                loss,grad=fun(x);vv,dv=pairs(x,weight);return loss+vv,grad+dv
            rng=np.random.default_rng(8963+step);d=rng.normal(size=x.size);d/=np.linalg.norm(d)
            v,dv=pairs(x,weight);h=1e-7;fd=(pairs(x+h*d,weight,False)['loss']-pairs(x-h*d,weight,False)['loss'])/(2*h)
            err=abs(dv@d-fd)/max(1.,abs(fd),abs(dv@d));assert err<3e-5,(err,dv@d,fd)
            before=pairs(x,weight,False);opts['options']['maxiter']=a.iterations
            def cb(z):
                cb0(z)
            opts['callback']=cb;res=minimize(merit,x,**opts)
            x=res.x.copy();total+=int(res.nit);selected=pairs(x,weight,False);pairs.update(x);after=pairs(x,weight,False)
            records.append(dict(weight=weight,own=int(res.nit),gradientCheck=err,before=before,selectedAfter=selected,newNeighborsAfter=after));print(records[-1],flush=True)
        return OptimizeResult(nit=total,x=x)
    cart.minimize=solve
    with TemporaryDirectory(dir=outside.parent) as tmp:
        a.output=Path(tmp)/'state.json';cart.run(a);q=base.read(a.output)
    q.update(pairEntrySHA256=base.sha(__file__),kind=a.pair_kind,ballRadius=a.ball_radius,materialSeparation=a.separation,neighborhoodRadius=a.neighbors,nonlocalStages=records)
    base.stores(outside,q)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','solution','start','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('radials',101),('angles',72),('spans',13),('modes',5),('iterations',260)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',3.),('geometry',40.),('guard',500000.),('held',.6547),('separation',.32),('neighbors',.265),('ball-radius',.100)]:p.add_argument('--'+k,type=float,default=v)
    p.add_argument('--pair-kind',choices=('ball','chord'),default='ball');p.add_argument('--pair-weights',type=float,nargs='+',default=[2.,80.,2200.]);run(p.parse_args())
