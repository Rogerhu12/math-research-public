#!/usr/bin/env python3
"""Stream full closed flat-core geometry, extract frozen true ordered witnesses for each nonlinear stage."""
import importlib.util
from pathlib import Path
import sys
import json
import numpy as np
from scipy.spatial import cKDTree


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m


here=Path(__file__).parent;ball=load(here/"2ecf-strong-stadium-two-normal-ball-solver.py","old_complete_geometric_operator")
elev=load(here/"2ecf-strong-stadium-real-elevated-cuff.py","elevated_actual_core_operator")
arb=ball.arb;c=arb.c


class Dense(ball.Balls):
    def __init__(self,f,basis,args,count):
        self.basis=basis;self.f=f;self.args=args;self.r=args.reach;self.pool=0.;self.block=args.pair_block
        d=f.saved["caches"]["observer"];a=np.asarray(d["angles"]);self.N=count
        if len(a)%count:raise ValueError("Use original unshifted training source angles")
        u=a[::len(a)//count];knots=f.cutraw.breaks;fresh=(knots[:-1,None]+np.diff(knots)[:,None]*[.213,.657]).ravel()
        x=np.unique(np.r_[np.linspace(0.,f.b,28),np.linspace(f.b,f.cut,19),knots,fresh])
        xs=np.asarray(d["nodes"]);oi=np.flatnonzero(xs>f.end);oi=np.unique(np.r_[oi[::max(1,len(oi)//38)],oi[-1]])
        raw=np.load(d["files"]["jets"],mmap_mode="r");outer=raw[oi][:,:3,::len(a)//count].copy()
        self.zc=float(f.definition["pointConfig"]["true_cuff_height"]);outer[:,0,:,2]+=self.zc-.51
        cuts=[f.jets(x[j:j+6],u)[0][:,:3] for j in range(0,len(x),6)]
        self.base=np.concatenate(cuts+[outer]);x=np.r_[x,xs[oi]];self.mats=basis.matrices(x)
        radii=np.arange(1,12)*.32/12;uR=np.concatenate([u+(np.pi/count if k%2==0 else 0.) for k in range(len(radii))])
        rr=np.repeat(radii,count);D=np.r_[[[0,0,self.zc]],np.column_stack((rr*np.cos(uR),rr*np.sin(uR),np.full(len(rr),self.zc)))]
        self.disk=np.stack((D,np.broadcast_to([1.,0,0],D.shape),np.broadcast_to([0,1.,0],D.shape)),axis=1)
        self.active=len(x)*count
        self.x=np.r_[np.repeat(x,count),np.full(len(D),x[-1])+.32-np.r_[0.,rr]];self.u=np.r_[np.tile(u,len(x)),0.,uR]
        both=np.flatnonzero(self.x>0);half=len(self.x);self.ids=np.r_[np.arange(half),both]
        self.flip=np.ones((len(self.ids),3));self.flip[half:,2]=-1.;self.fullX=self.x[self.ids]*self.flip[:,2];self.fullU=self.u[self.ids]
        self.ij=np.empty((0,2),dtype=np.int32);self.recent={};self.origin=self.space(np.zeros((basis.nb,basis.na)))[0][:,0]
    def refresh(self,z):
        Y,(n,_)=self.space(z);P=Y[:,0];tree=cKDTree(P);q=2*self.r+.005
        best=np.inf;rec=None;tot=0;selected=[];minfar=np.inf;minop=np.inf;mind=np.inf
        for j0 in range(0,len(P),self.args.cloud_batch):
            j1=min(j0+self.args.cloud_batch,len(P));near=tree.query_ball_point(P[j0:j1],q)
            I=np.repeat(np.arange(j0,j1),list(map(len,near)));J=np.concatenate(near).astype(int);ok=I!=J;I,J=I[ok],J[ok]
            d=P[J]-P[I];sq=np.einsum("ij,ij->i",d,d);den=2*abs(np.einsum("ij,ij->i",n[I],d));tot+=len(I)
            rr=np.divide(sq,den,out=np.full_like(sq,np.inf),where=den>0);mind=min(mind,float(sq.min()))
            k=int(np.argmin(rr))
            if rr[k]<best:
                i,j=I[k],J[k];best=float(rr[k]);rec=[float(self.fullX[i]),float(self.fullU[i]),float(self.fullX[j]),float(self.fullU[j]),float(sq[k]**.5)]
            far=abs(self.fullX[I]-self.fullX[J])>.19;opp=self.fullX[I]*self.fullX[J]<0
            if np.any(far):minfar=min(minfar,float(rr[far].min()))
            if np.any(opp):minop=min(minop,float(rr[opp].min()))
            # Keep a per-source worst for distinct distance groups. Every captured pair is then tested in both orders.
            for subtype,number in ((np.ones(len(I),dtype=bool),self.args.witnesses),(far,2),(opp,1)):
                h=np.flatnonzero(subtype&(rr<self.args.activation*self.r));sort=h[np.lexsort((rr[h],I[h]))]
                if not len(sort):continue
                a=I[sort];start=np.r_[True,a[1:]!=a[:-1]]
                ranks=np.arange(len(a))-np.maximum.accumulate(np.where(start,np.arange(len(a)),0))
                ii=sort[ranks<number];selected.append(np.column_stack([np.minimum(I[ii],J[ii]),np.maximum(I[ii],J[ii])]).astype(np.int32))
        if mind<1e-20:raise ArithmeticError(("Sampled duplicate material positions",mind))
        Z=np.concatenate(selected,axis=0)
        # Preserve earlier support points when taking a new nonlinear step.
        self.ij=np.unique(np.r_[self.ij,Z],axis=0);self.origin=P.copy()
        self.recent=dict(sampledMinimum=best,far=minfar,opposite=minop,arg=rec,points=len(P),orderedActualNearPairs=tot,
            selectedUndirectedWitnesses=len(self.ij),maximumHeight=float(abs(P[:,2]).max()),largestBallNorm=float(np.linalg.norm(P,axis=1).max()))
        return self.recent
    def evaluate(self,z,beta,gradient=True):
        val,grad,rec=super().evaluate(z,beta,gradient)
        rec["exhaustsAllSampledPairsWithChordBelow2R"]=False;rec["fixedHeight"]=self.zc
        rec["lastFullGeometryScreen"]=self.recent
        return val,grad,rec
