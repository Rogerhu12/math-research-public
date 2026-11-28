#!/usr/bin/env python3
"""Observe the complete new C2 arm family with its actual H65 ramp, caps and genuine XYZ correction."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
from types import SimpleNamespace

for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.spatial import ConvexHull,cKDTree
from scipy.spatial.distance import cdist


def mod(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


class Whole:
    def __init__(self,cli):
        self.cli=cli
        self.m=mod(cli.arms,'thickC2')
        self.cl=mod(cli.solver,'shortR303')
        self.fit=json.loads(cli.fit.read_text())
        self.a=SimpleNamespace(**dict(self.fit['parameters'],scripts=cli.scripts,field=cli.field))
        # Translating the upper and lower complete Cauchy packets by +/-.13
        # preserves their physical jets and moves the ports to the proven c=.78.
        self.a.c=.78
        self.src=self.cl.PhysicalSource(self.a,cli.angles)
        self.ports=[self.m.Port(i) for i in range(2)]
        self.arm_parameters={'C2':self.m.NEW_C2,'C3':self.m.WIDE_C3}[cli.pair]
        self.rings=[self.m.surface_rings(i,law,omega,first,last,n=cli.rings) for i,(omega,first,last,law) in enumerate(self.arm_parameters)]
        K=self.a.modes
        n=self.a.spans
        knots=np.r_[np.zeros(5),np.linspace(0,1,n+1),np.ones(5)]
        self.B=BSpline(knots,np.eye(len(knots)-6)[:,3:-3],5)
        with np.load(cli.state) as z:
            self.x=z['coefficients'].reshape(3,n-1,K)
        if cli.unmodified:
            self.x*=0
        self.A=[]
        for c in range(3):
            w=2*np.arange(K)+(c!=2)
            phase=-(c==1)*np.pi/2
            self.A.append([w[None,:]**j*np.cos(self.src.u[:,None]*w[None,:]+phase+j*np.pi/2) for j in range(3)])
        self.sleeves=[self.m.points(p,.5,r,np.linspace(0,2*np.pi,cli.angles//2,endpoint=False)).reshape(-1,3) for p,r in zip(self.ports,self.rings)]

    def closing(self,t):
        J,tar=self.src.closing(t)
        for c in range(3):
            for j,(k,b) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
                B=self.B.derivative(k)(t)/self.a.length**k
                J[j,:,c]+=self.A[c][b]@(B@self.x[c])
        return J,tar

    def active(self):
        upper=[]
        peak=curv=0.
        minimum=1e100
        where=[]
        def add(j,t,part,r):
            nonlocal peak,curv,minimum,where
            upper.append(j[0])
            _,err,geo=self.cl.gram(j[None],*t)
            k,ar=self.cl.curvature(j[None],geo)
            if err.max()>peak:
                peak=float(err.max())
                where=[part,float(r),float(self.src.u[err.argmax()])]
            curv=max(curv,float(k.max()))
            minimum=min(minimum,float(ar.min()))
        ss=self.src.s
        for r in np.unique(np.r_[ss,*[ss[:-1]+t*np.diff(ss) for t in (.112701665379,.5,.887298334621)]]):
            j,t=self.src.ramp(r)
            add(j,t,'ramp',r)
        for t in np.unique(np.r_[np.linspace(0,1,2*self.cli.radial+1),(np.arange(self.cli.radial)+.427)/self.cli.radial]):
            j,target=self.closing(t)
            add(j,target,'closing',t*self.a.length)
        return np.vstack(upper),dict(maximumRelativeOperator=peak,maximumAbsolutePrincipalCurvature=curv,minimumAreaSquared=minimum,point=where)

    def closed(self,ph,active):
        u=self.src.u
        # The open disks are removed from their actual material windows.
        extra=np.unique(np.r_[u,*[np.linspace(p.u-np.arcsin(p.k*p.width)/p.k,p.u+np.arcsin(p.k*p.width)/p.k,85) for p in self.ports]])
        base=self.cl.rotation(self.src.inlet.geometry(extra-ph)[0],ph)
        rows=[]
        for z in np.unique(np.r_[np.linspace(0,self.m.A_ROOT,22),np.linspace(self.m.A_ROOT,.47,10),np.linspace(.47,.77,29),.78]):
            w=base.copy()
            w[:,2]=z
            keep=np.ones(len(w),dtype=bool)
            for p in self.ports:
                off,x=p.local_offset(extra)
                idx=np.where(abs(off)<=np.arcsin(p.k*p.width)/p.k)[0]
                w[idx]=p.mother(ph,z,extra[idx])
                keep[idx[x[idx]**2+z*z<self.m.A_ROOT**2]]=False
            rows.append(w[keep])
        upper=np.vstack([*rows,self.cl.rotation(active,ph),*[self.src.cap(s,u) for s in np.linspace(0,np.pi/2,81)]])
        lower=upper.copy()
        lower[:,2]*=-1
        chi=np.linspace(0,2*np.pi,self.cli.angles//2,endpoint=False)
        arms=[self.m.points(p,ph,r,chi).reshape(-1,3) for p,r in zip(self.ports,self.rings)]
        return np.vstack([upper,lower,*arms])

    def diameter(self,P):
        hull=P[ConvexHull(P).vertices]
        best=(-1.,0,0)
        for i in range(0,len(hull),48):
            d=cdist(hull[i:i+48],hull)
            j,k=np.unravel_index(np.argmax(d),d.shape)
            if d[j,k]>best[0]:
                best=(float(d[j,k]),i+j,k)
        return dict(distance=best[0],pair=hull[[best[1],best[2]]].tolist())

    def run(self):
        active,metric=self.active()
        p0=self.closed(.5,active)
        p1=self.closed(0.,active)
        D0=self.diameter(p0)
        D1=self.diameter(p1)
        tree0=cKDTree(p0)
        result=[]
        for hold in (-1,0,1):
            h=self.ports[hold] if hold>=0 else -1
            q1=self.m.holding_frame(p1,h,0.,initial=.5)
            tree1=cKDTree(q1)
            directed=[]
            for cloud,tree,other in ((q1,tree0,p0),(p0,tree1,q1)):
                dist,idx=tree.query(cloud)
                where=np.argmax(dist)
                directed.append(dict(distance=float(dist[where]),point=cloud[where].tolist(),near=other[idx[where]].tolist()))
            result.append(dict(heldComponent=hold,directed=directed,sampledRatio=max(v['distance'] for v in directed)/D0['distance']))
        return dict(schema='true-two-arm-full-H65-complete-closed-image-observation-with-explicit-pair',pair=self.cli.pair,armParameters=self.arm_parameters,entry=digest(Path(__file__)),source=digest(self.cli.solver),arms=digest(self.cli.arms),field=digest(self.cli.field),fitReport=digest(self.cli.fit),state=digest(self.cli.state),unmodified=self.cli.unmodified,
          sampleCounts=[len(p0),len(p1)],parameters={k:v for k,v in vars(self.a).items() if not isinstance(v,Path)},centralHalfheight=self.a.c,
          activeMetricAndCurvature=metric,initialHalfPhaseDiameter=D0,finalZeroPhaseDiameter=D1,
          diameterVariationQuotientRatio=(D1['distance']-D0['distance'])/(2*D0['distance']),
          allThreeHoldingFrames=result,actualHighArmDiameterAtInitial=self.diameter(self.sleeves[1]),
          scope='Floating complete-image observations; the sampled Hausdorff distance and diameter differences do not themselves certify a continuous lower bound.')


if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','field','solver','arms','fit','state','out'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--angles',type=int,default=192)
    p.add_argument('--rings',type=int,default=48)
    p.add_argument('--radial',type=int,default=64)
    p.add_argument('--unmodified',action='store_true')
    p.add_argument('--pair',choices=('C2','C3'),default='C2')
    cli=p.parse_args()
    out=Whole(cli).run()
    with cli.out.open('x') as f:
        json.dump(out,f,indent=2)
        f.write('\n')
    print(json.dumps(out),flush=True)
