#!/usr/bin/env python3
"""Actual all-XYZ two-sided closed-flat-core tangent-ball rows, curvature, geometry and full original G10."""
import os
for env in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[env]="1"
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import cKDTree


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m


home=Path(__file__).parent;sep=load(home/"2ecf-strong-stadium-real-pair-separation.py","two_normal_real_geometry")
arb=sep.arb;c=arb.c;mat=sep.mat;joint=arb.joint


class Balls:
    def __init__(self,f,basis,args,count):
        self.basis=basis
        count0=args.count;args.count=count
        try:x,u,J=sep.coarse(f,args)
        finally:args.count=count0
        self.N=len(u);self.mats=basis.matrices(x);self.base=J
        R=.32;radii=np.linspace(0.,R,9)[:-1]
        P=np.array([[0.,0.,.51]]+[ [r*np.cos(a),r*np.sin(a),.51] for r in radii[1:] for a in u])
        ss=np.broadcast_to([1.,0,0],P.shape);uu=np.broadcast_to([0,1.,0],P.shape)
        self.disk=np.stack((P,ss,uu),axis=1);self.diskCount=len(P)
        self.x=np.r_[np.repeat(x,len(u)),np.full(len(P),x[-1]+1.)]
        self.u=np.r_[np.tile(u,len(x)),np.r_[0.,np.tile(u,len(radii)-1)]]
        half=len(self.x);self.active=len(x)*len(u)
        self.ids=np.r_[np.arange(half),np.flatnonzero(self.x>0)]
        self.flip=np.ones((len(self.ids),3));self.flip[half:,2]=-1.
        self.fullX=self.x[self.ids]*self.flip[:,2];self.fullU=self.u[self.ids]
        self.pool=args.pool;self.r=args.reach;self.block=args.pair_block
        base,_=self.space(np.zeros((basis.nb,basis.na)))
        self.origin=base[:,0]
        ij=cKDTree(self.origin).query_pairs(self.pool,output_type="ndarray").astype(np.int32)
        # Exact seam material labels are included only once. Numerically coincident distinct images are unsafe.
        dist=np.linalg.norm(self.origin[ij[:,0]]-self.origin[ij[:,1]],axis=1)
        if np.min(dist)<1e-9:raise ArithmeticError(("Indistinguishable sampled flat-core images",float(dist.min())))
        self.ij=ij
    def space(self,z):
        upper=self.base+self.basis.packet(self.mats,z,self.N)[:,:3]
        H=np.concatenate((upper.transpose(0,2,1,3).reshape(-1,3,3),self.disk))
        g=H[self.ids]*self.flip[:,None,:]
        N=np.cross(g[:,1],g[:,2]);w=np.linalg.norm(N,axis=1)
        return g,(N/w[:,None],w)
    def evaluate(self,z,beta,gradient=True):
        Y,(n,w)=self.space(z);P=Y[:,0];shift=float(np.linalg.norm(P-self.origin,axis=1).max())
        # At all sampled material points, the triangle inequality exhausts relevant pair candidates.
        # Outside this ball the conservative smooth finite penalty still checks its fixed edge list.
        complete=(2*shift+2*self.r<self.pool)
        ref=-np.inf;mass=0.;pq=0.;where=None
        barP=np.zeros_like(P);barN=np.zeros_like(n)
        for j in range(0,len(self.ij),self.block):
            I,J=self.ij[j:j+self.block].T;v=P[J]-P[I];d2=np.sum(v*v,axis=1);d2=np.maximum(d2,1e-28)
            Ni,Nj=n[I],n[J];si=np.sum(v*Ni,axis=1);sj=np.sum(v*Nj,axis=1)
            fac=2*self.r/d2;ai=abs(si)*fac;aj=abs(sj)*fac
            pi,pj=int(np.argmax(ai)),int(np.argmax(aj))
            if ai[pi]>pq:pq=float(ai[pi]);where=(int(I[pi]),int(J[pi]))
            if aj[pj]>pq:pq=float(aj[pj]);where=(int(J[pj]),int(I[pj]))
            top=max(float(ai[pi]),float(aj[pj]));base=max(ref,top)
            if base>ref:
                facOld=0 if ref==-np.inf else np.exp(beta*(ref-base))
                mass*=facOld
                if gradient:barP*=facOld;barN*=facOld
                ref=base
            wi=np.exp(beta*(ai-ref));wj=np.exp(beta*(aj-ref));mass+=float(wi.sum()+wj.sum())
            if not gradient:continue
            qi=wi*fac*np.sign(si);qj=wj*fac*np.sign(sj)
            vd=qi[:,None]*Ni+qj[:,None]*Nj-(2*(wi*ai+wj*aj)/d2)[:,None]*v
            # bincount is a full scatter sum, and the cross terms of both spatial normals are retained.
            for k in range(3):
                barP[:,k]+=np.bincount(J,vd[:,k],len(P))-np.bincount(I,vd[:,k],len(P))
                barN[:,k]+=np.bincount(I,qi*v[:,k],len(P))+np.bincount(J,qj*v[:,k],len(P))
        val=ref+math.log(mass/(2*len(self.ij)))/beta
        if where is None:raise ArithmeticError("No measured ordered tangent-ball pair")
        i,j=where
        receipt=dict(finiteRadius=self.r/pq,peak=pq,x1=self.fullX[i],u1=self.fullU[i],x2=self.fullX[j],u2=self.fullU[j],
            actualChord=float(np.linalg.norm(P[i]-P[j])),sampleMaxDisplacement=shift,
            exhaustsAllSampledPairsWithChordBelow2R=bool(complete),sampledClosedFlatCorePoints=len(P),
            undirectedSearchPairs=len(self.ij),fixedHeight=.51,staticCentralDiskRadius=.32)
        if not gradient:return val,None,receipt
        nb=(barN-n*np.sum(n*barN,axis=1)[:,None])/w[:,None];S,U=Y[:,1],Y[:,2]
        cot=np.stack((barP,np.cross(U,nb),np.cross(nb,S)),axis=1)*self.flip[:,None,:]/mass
        H=np.zeros((len(self.x),3,3))
        for k in range(3):
            for t in range(3):H[:,k,t]=np.bincount(self.ids,cot[:,k,t],len(H))
        core=H[:self.active].reshape(len(self.base),self.N,3,3).transpose(0,2,1,3)
        gp=np.zeros((len(self.base),6,self.N,3));gp[:,:3]=core
        return val,self.basis.packet_adjoint(self.mats,gp),receipt


def main(args):
    tic=time.monotonic();f=arb.Field(args);b=sep.basis_from(f,args);cfg=f.stream.point.PointConfig(**f.definition["pointConfig"])
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","p32_ball_area")
    train={n:mat.source_rows(f,n) for n in ("training","observer")}
    geob=Balls(f,b,args,args.count);print(json.dumps(dict(stage="true_all_ordered_normal_pairs",points=len(geob.ids),edges=len(geob.ij),dimension=b.dimension)),flush=True)
    xs=train["training"][0];weights=sum(g[4]["metric"].ravel()*len(g[1]) for g in train.values())
    pre=f.stream.BandedSobolev(b,xs,weights,dict(beta0=.1,beta1=1.,beta2=.001))
    zm=np.zeros((b.nb,b.na));fixed=[];active=[]
    for name,(x,u,Y,rad,w) in train.items():
        N=len(u)
        for live in (False,True):
            ids=np.flatnonzero(((x>b.c)&(x<b.end))==live)
            for j in range(0,len(ids),args.block):
                ix=ids[j:j+args.block];rec=(Y[ix],rad[ix,0,None],{k:v[ix] for k,v in w.items()},b.matrices(x[ix]),N)
                (active if live else fixed).append(rec)
    del train
    def block(rec,z,beta,live):
        base,a,w,M,N=rec;Y=base+b.packet(M,z,N) if live else base
        p=f.stream.point;pt=p.PointLinearized(Y.swapaxes(1,2),a,cfg,w);ar=area.AreaPacket(Y,a,w["metric"],.5)
        g=pt.metric;S=pt.curvature["S"]
        gm=joint.signed_eigensystem(g[...,0],g[...,1]/math.sqrt(2),g[...,2],args.metric_scale)
        ks=joint.signed_eigensystem(S[...,0],S[...,1],S[...,2],args.curvature_scale)
        e=np.stack([x for a0 in (gm,ks) for x in (a0[0],a0[1],-a0[0],-a0[1])]+list(np.moveaxis(pt.geometry["residual"]/args.guide_scale,-1,0)))
        top=float(e.max());ew=w["metric"]*np.exp(beta*(e-top));mass=float(ew.sum());weight=15*N*float(w["metric"].sum())
        cost=float(np.sum(pt.residual**2)+ar.stats["squaredNorm"]);mpe=float(e[:4].max()*args.metric_scale);kpe=float(e[4:8].max()*args.curvature_scale)
        if not live:return top,mass,weight,cost,None,None,mpe,kpe
        ds=joint.eigen_pullback(ew[4]-ew[6],ew[5]-ew[7],ks[2],ks[3],args.curvature_scale)
        bar=p.curvature_vjp(pt.jets,pt.curvature,ds);dm=joint.eigen_pullback(ew[0]-ew[2],ew[1]-ew[3],gm[2],gm[3],args.metric_scale)
        ss,uu=pt.jets[...,1,:],pt.jets[...,2,:]
        bar[...,1,:]+=2*dm[...,0,None]*ss+(dm[...,1]/a)[...,None]*uu
        bar[...,2,:]+=(dm[...,1]/a)[...,None]*ss+(2*dm[...,2]/a**2)[...,None]*uu
        bar[...,0,:]+=np.einsum("...k,...kj->...j",np.moveaxis(ew[8:],0,-1)/args.guide_scale,pt.geometry["jacobian"])
        gb=b.packet_adjoint(M,bar.swapaxes(1,2))
        cb=pt.vjp(2*pt.residual);bs,bu=ar.vjp(2*ar.residual);cb[...,1,:]+=bs;cb[...,2,:]+=bu
        return top,mass,weight,cost,gb,b.packet_adjoint(M,cb.swapaxes(1,2)),mpe,kpe
    def total(blocks,base=None):
        ref,mass,wt,cost,g,cg,mp,kp=(-np.inf,0.,0.,0.,zm.copy(),zm.copy(),0.,0.) if base is None else (base[0],base[1],base[2],base[3],base[4].copy(),base[5].copy(),base[6],base[7])
        for top,mm,ww,cc,gg,gc,em,ek in blocks:
            if top>ref:
                scale=np.exp(beta*(ref-top));mass*=scale;g*=scale;ref=top
            scale=np.exp(beta*(top-ref));mass+=scale*mm;wt+=ww;cost+=cc
            if gg is not None:g+=scale*gg;cg+=gc
            mp=max(mp,em);kp=max(kp,ek)
        return ref,mass,wt,cost,g,cg,mp,kp
    state=[];v=np.zeros(b.dimension)
    if args.start_state:
        old=arb.rd(args.start_state)
        if old["previousPhysicalCorrection"]!=c.sha(args.extra_state[-1]) or old["physicalCorrectionBasis"]!=b.definition:raise ValueError("Same explicit geometry required")
        v=np.asarray(old["preconditionedCoordinates"]);state=old["stages"]
    for st,beta in enumerate(args.betas):
        const=total(block(rec,zm,beta,False) for rec in fixed)
        last=None;hist=[];calls=0
        def cost(y):
            nonlocal last,calls
            if last is not None and np.array_equal(y,last[0]):return last[1],last[2]
            z=pre.unpack(args.coordinate_scale*y)
            ref,ss,weight,cc,gg,cg,mp,kp=total((block(rec,z,beta,True) for rec in active),const)
            fv=ref+np.log(ss/weight)/beta;gs=gg/ss
            bv,bg,br=geob.evaluate(z,beta)
            # Equal group weights for the complete sampled closed flat core and the G10 shape/metric spectrum.
            shift=max(fv,bv);sw,wb=np.exp(beta*(fv-shift)),np.exp(beta*(bv-shift));den=sw+wb
            peak=shift+np.log(den/2)/beta
            val=peak+args.original_weight*cc+args.ridge*np.mean(y*y)
            raw=(sw*gs+wb*bg)/den+args.original_weight*cg;grad=args.coordinate_scale*pre.transpose(raw)+2*args.ridge*y/b.dimension
            record=dict(cost=float(val),completeOriginal=cc,G10Metric=mp,G10Curvature=kp,geometric=br,fitPair=bv,fitSpectrum=fv)
            last=(y.copy(),val,grad,record);calls+=1;return val,grad
        val,gr=cost(v)
        if st==0:
            w=np.random.default_rng(287).standard_normal(len(v));w/=np.linalg.norm(w);eps=6e-5
            data=(cost(v+eps*w)[0]-cost(v-eps*w)[0])/(2*eps);exact=float(gr@w)
            if abs(data-exact)>2e-7:raise ArithmeticError(("Full closed-pair and all-row directional derivative mismatch",data,exact))
            print(json.dumps(dict(actualCost=val,analytic=exact,difference=data,error=abs(data-exact))),flush=True)
        def callback(y):
            if not np.array_equal(y,last[0]):cost(y)
            hist.append(last[3])
            if len(hist)%8==0:
                print(json.dumps(dict(stage=st,iteration=len(hist),cost=last[1],regularizedPair=last[3]["geometric"]["finiteRadius"],
                    metric=last[3]["G10Metric"],curvature=last[3]["G10Curvature"])),flush=True)
        res=minimize(cost,v,method="L-BFGS-B",jac=True,callback=callback,options=dict(maxiter=args.iterations,maxcor=12,maxls=25,ftol=1e-14,gtol=1e-9))
        v=res.x.copy();cost(v);z=pre.unpack(args.coordinate_scale*v)
        # Full independent unshifted-source geometry evaluation on the actual shifted G11 angles.
        xx,uu,yy,rad,w=mat.source_rows(f,"independent")
        for j in range(0,len(xx),12):
            sl=slice(j,j+12);yy[sl]+=f.direct(b,xx[sl],z,uu)
        ind=mat.observed(f,None,None,(xx,uu,yy,rad,w),None,None,False,args);del yy
        row=dict(stage=st,beta=beta,iterations=res.nit,evaluations=calls,status=str(res.message),G10=last[3],G11=ind,history=hist)
        state.append(row)
        record=dict(schema="p32-actual-complete-two-sided-flat-core-normal-balls-and-original-G10-spatial-optimization-v1",entry=c.sha(__file__),
            source=c.sha(args.background),previousPhysicalCorrection=c.sha(args.extra_state[-1]),physicalCorrectionBasis=b.definition,
            coefficients=z.ravel().tolist(),preconditionedCoordinates=v.tolist(),stages=state,sourceMetric=f.ident,
            trueOriginalRows=4291840,allG11Independent=True,spatialDimensions=b.dimension,wholeClosedReachCertified=False,
            continuousMetricCertified=False,seconds=time.monotonic()-tic)
        receipt=c.save(Path(str(args.prefix)+f"-stage{st+1:02}.json"),record)
        print(json.dumps(dict(stage=st,accepted=len(hist),G11Metric=ind["metric"],G11Curvature=ind["curvature"],held=ind["held"],
            geometric=last[3]["geometric"],SHA=receipt)),flush=True)


if __name__=="__main__":
    ap=arb.parser()
    for k,v in (("count",48),("controls",18),("modes",6),("pair-block",72000)):ap.add_argument("--"+k,type=int,default=v)
    ap.add_argument("--pool",type=float,default=.295);ap.add_argument("--reach",type=float,default=.097);ap.add_argument("--start-state",type=Path)
    args=ap.parse_args();args.resume=None;main(args)
