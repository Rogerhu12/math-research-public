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



dense=load(home/"2ecf-strong-stadium-dense-pair-exchange.py","stadium_elevated_dense_ball_exchange")
elev=dense.elev

def main(args):
    tic=time.monotonic();f=elev.RaisedField(args);b=sep.basis_from(f,args);cfg=f.stream.point.PointConfig(**f.definition["pointConfig"])
    legacy_cfg=f.stream.point.PointConfig(**dict(f.definition["pointConfig"],true_cuff_height=.51))
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","p32_ball_area")
    train={n:elev.elevated_rows(f,n) for n in ("training","observer")}
    geob=dense.Dense(f,b,args,args.count);print(json.dumps(dict(stage="true_all_ordered_normal_pairs",points=len(geob.ids),edges=len(geob.ij),dimension=b.dimension)),flush=True)
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
        legacy=p.geometry_cache(Y[:,0],legacy_cfg)
        oldh=legacy["residual"][...,3:5];newh=pt.geometry["residual"][...,3:5]
        replaced=float(np.sum(w["geometry"][...,None]*(oldh**2-newh**2)))
        cost=float(np.sum(pt.residual**2)+ar.stats["squaredNorm"]+replaced);mpe=float(e[:4].max()*args.metric_scale);kpe=float(e[4:8].max()*args.curvature_scale)
        if not live:return top,mass,weight,cost,None,None,mpe,kpe
        ds=joint.eigen_pullback(ew[4]-ew[6],ew[5]-ew[7],ks[2],ks[3],args.curvature_scale)
        bar=p.curvature_vjp(pt.jets,pt.curvature,ds);dm=joint.eigen_pullback(ew[0]-ew[2],ew[1]-ew[3],gm[2],gm[3],args.metric_scale)
        ss,uu=pt.jets[...,1,:],pt.jets[...,2,:]
        bar[...,1,:]+=2*dm[...,0,None]*ss+(dm[...,1]/a)[...,None]*uu
        bar[...,2,:]+=(dm[...,1]/a)[...,None]*ss+(2*dm[...,2]/a**2)[...,None]*uu
        bar[...,0,:]+=np.einsum("...k,...kj->...j",np.moveaxis(ew[8:],0,-1)/args.guide_scale,pt.geometry["jacobian"])
        gb=b.packet_adjoint(M,bar.swapaxes(1,2))
        cb=pt.vjp(2*pt.residual)
        cb[...,0,:]+=2*w["geometry"][...,None]*(np.einsum("...k,...kj->...j",oldh,legacy["jacobian"][...,3:5,:])-np.einsum("...k,...kj->...j",newh,pt.geometry["jacobian"][...,3:5,:]))
        bs,bu=ar.vjp(2*ar.residual);cb[...,1,:]+=bs;cb[...,2,:]+=bu
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
        beforeGeometry=geob.refresh(pre.unpack(args.coordinate_scale*v));print(json.dumps(dict(stage=st,beforeGeometry=beforeGeometry)),flush=True)
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
        xx,uu,yy,rad,w=elev.elevated_rows(f,"independent")
        for j in range(0,len(xx),12):
            sl=slice(j,j+12);yy[sl]+=f.direct(b,xx[sl],z,uu)
        ind=mat.observed(f,None,None,(xx,uu,yy,rad,w),None,None,False,args);del yy
        afterGeometry=geob.refresh(z)
        row=dict(stage=st,beta=beta,beforeGeometry=beforeGeometry,afterGeometry=afterGeometry,iterations=res.nit,evaluations=calls,status=str(res.message),G10=last[3],G11=ind,history=hist)
        state.append(row)
        record=dict(schema="R293-p32-actual-complete-two-sided-moving-cut-graph-updates-and-original-G10-spatial-optimization-v1",entry=c.sha(__file__),
            source=c.sha(args.background),previousPhysicalCorrection=c.sha(args.extra_state[-1]),physicalCorrectionBasis=b.definition,
            coefficients=z.ravel().tolist(),preconditionedCoordinates=v.tolist(),stages=state,sourceMetric=f.ident,
            elevation=c.sha(args.elevation),trueCuff=f.true_cuff_z,originalFourteenRowsIncludeFormerCuffHeight=.51,nativeSevenGuideIncludesActualCuffHeight=f.true_cuff_z,trueOriginalRows=4291840,allG11Independent=True,spatialDimensions=b.dimension,wholeClosedReachCertified=False,
            continuousMetricCertified=False,seconds=time.monotonic()-tic)
        receipt=c.save(Path(str(args.prefix)+f"-stage{st+1:02}.json"),record)
        print(json.dumps(dict(stage=st,accepted=len(hist),G11Metric=ind["metric"],G11Curvature=ind["curvature"],held=ind["held"],
            geometric=afterGeometry,SHA=receipt)),flush=True)


if __name__=="__main__":
    ap=arb.parser()
    for k,v in (("count",48),("controls",18),("modes",6),("pair-block",72000)):ap.add_argument("--"+k,type=int,default=v)
    ap.add_argument("--pool",type=float,default=.295);ap.add_argument("--reach",type=float,default=.097);ap.add_argument("--start-state",type=Path)
    ap.add_argument("--elevation",type=Path,required=True);ap.add_argument("--cloud-batch",type=int,default=36)
    ap.add_argument("--activation",type=float,default=1.24);ap.add_argument("--witnesses",type=int,default=3)
    args=ap.parse_args();args.resume=None;main(args)
