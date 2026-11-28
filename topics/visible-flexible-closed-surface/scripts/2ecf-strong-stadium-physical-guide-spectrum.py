#!/usr/bin/env python3
"""Original 14 physical rows plus all signed Gram and shape eigenvalues at both training grids."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"

import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.optimize import minimize


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


full=load(Path(__file__).with_name("2ecf-strong-hf-new-clock-full-position.py"),"spectral_full_HF")
hf,c=full.hf,full.c


def signed_eigensystem(a,b,g,scale):
    mid=.5*(a+g);d=.5*(a-g);rad=np.hypot(d,b)
    safe=np.where(rad>0,rad,1.)
    return (mid+rad)/scale,(mid-rad)/scale,d/safe,b/safe


def eigen_pullback(plus,minus,df,b,scale):
    tr=(plus+minus)/scale
    diff=(plus-minus)/scale
    return np.stack((.5*(tr+df*diff),b*diff,.5*(tr-df*diff)),axis=-1)


def main(args):
    tic=time.monotonic()
    args.metric_sextic=.2;args.curvature_tau=2.
    definition,basis,clock,physical,g11,weights,mods,radius,metadata,expect=full.prepare(args)
    stream=mods["stream"];point=stream.point
    cfg=point.PointConfig(**definition["pointConfig"])
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","joint_spectral_area")
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","joint_spectral_shift").direct_packet
    dimension=basis.dimension
    allrad=physical["training"].nodes
    pre=stream.BandedSobolev(basis,allrad,weights["training"]["metric"]+weights["observer"]["metric"],
        dict(beta0=.1,beta1=1.,beta2=.001))
    metric_scale,shape_scale=args.metric_scale,args.curvature_scale
    blank=lambda:np.zeros((basis.nb,basis.na))
    # One fixed chart includes all source rows. Blocks outside all variable
    # supports contribute exactly their initial objective at every trial.
    fixed=[];active=[]
    for name,cache in physical.items():
        x=cache.nodes;u=cache.u;N=len(u)
        if max(abs(u-2*np.pi*np.arange(N)/N))>1e-13:
            raise ValueError("Both G10 angular grids must be actual unshifted complete sets")
        for live in (False,True):
            ix=np.flatnonzero(((x>=basis.c)&(x<=basis.end))==live)
            dest=active if live else fixed
            for start in range(0,len(ix),args.block):
                j=ix[start:start+args.block]
                w={k:r[j,None]/N for k,r in weights[name].items()}
                dest.append((cache.jets[j],cache.radius[j,0,None],w,basis.matrices(x[j]),N))
    def block_eval(record,z,beta,variable):
        base,a,w,mats,N=record
        packet=base+basis.packet(mats,z,N) if variable else base
        pt=point.PointLinearized(packet.swapaxes(1,2),a,cfg,w)
        ar=area.AreaPacket(packet,a,w["metric"],.5)
        metric=pt.metric;form=pt.curvature["S"]
        gm=signed_eigensystem(metric[...,0],metric[...,1]/np.sqrt(2),metric[...,2],metric_scale)
        gs=signed_eigensystem(form[...,0],form[...,1],form[...,2],shape_scale)
        e=np.stack([v for group in (gm,gs) for v in (group[0],group[1],-group[0],-group[1])])
        violation=pt.geometry["residual"]
        radial=np.sqrt(1+(violation/args.guide_scale)**2)
        extra=(radial-1).transpose(2,0,1)
        e=np.concatenate((e,extra),axis=0)
        shift=float(e.max())
        powers=w["metric"]*np.exp(beta*(e-shift))
        soft_sum=float(np.sum(powers))
        measure=15*N*float(w["metric"].sum())
        c14=float(np.sum(pt.residual**2)+ar.stats["squaredNorm"])
        peaks=(float(np.max(abs(e[:4]))*metric_scale),float(np.max(abs(e[4:8]))*shape_scale))
        if not variable:return shift,soft_sum,None,c14,None,measure,peaks
        ds=eigen_pullback(powers[4]-powers[6],powers[5]-powers[7],gs[2],gs[3],shape_scale)
        jetbar=point.curvature_vjp(pt.jets,pt.curvature,ds)
        dm=eigen_pullback(powers[0]-powers[2],powers[1]-powers[3],gm[2],gm[3],metric_scale)
        xs,xu=pt.jets[...,1,:],pt.jets[...,2,:]
        cross=(dm[...,1]/a)[...,None]
        jetbar[...,1,:]+=2*dm[...,0,None]*xs+cross*xu
        jetbar[...,2,:]+=cross*xs+(2*dm[...,2]/a**2)[...,None]*xu
        gbar=powers[8:].transpose(1,2,0)*violation/(args.guide_scale**2*radial)
        jetbar[...,0,:]+=np.einsum("...k,...kj->...j",gbar,pt.geometry["jacobian"])
        soft_grad=basis.packet_adjoint(mats,jetbar.swapaxes(1,2))
        cbar=pt.vjp(2*pt.residual)
        ss,uu=ar.vjp(2*ar.residual)
        cbar[...,1,:]+=ss;cbar[...,2,:]+=uu
        cost_grad=basis.packet_adjoint(mats,cbar.swapaxes(1,2))
        return shift,soft_sum,soft_grad,c14,cost_grad,measure,peaks
    class Reduction:
        def __init__(self):
            self.ref=-np.inf;self.mass=0.;self.grad=blank();self.c14=0.;self.cgrad=blank()
            self.weight=0.;self.mpeak=0.;self.kpeak=0.
        def add(self,r,beta):
            shift,s,v,cost,cv,w,peaks=r
            if shift>self.ref:
                old=np.exp(beta*(self.ref-shift));self.mass*=old;self.grad*=old;self.ref=shift
            scale=np.exp(beta*(shift-self.ref))
            self.mass+=s*scale
            if v is not None:self.grad+=v*scale
            self.c14+=cost
            if cv is not None:self.cgrad+=cv
            self.weight+=w
            self.mpeak=max(self.mpeak,peaks[0]);self.kpeak=max(self.kpeak,peaks[1])
        def fixed_record(self):return self.ref,self.mass,None,self.c14,None,self.weight,(self.mpeak,self.kpeak)
    def independent(z):
        x=g11.nodes;u=g11.u;res=None;arCost=0.
        for start in range(0,len(x),24):
            s=slice(start,start+24);a=g11.radius[s,0,None]
            jets=g11.jets[s]+direct(basis,x[s],z,u)
            w={k:np.ones_like(a)/len(u) for k in ("metric","curvature","geometry")}
            pt=point.PointLinearized(jets.swapaxes(1,2),a,cfg,w)
            st=stream._block_statistics(pt,x[s],len(u))
            for k in ("worstMetric","worstCurvature"):st[k]["u"]+=u[0]
            res=stream._merge_statistics(res,st)
            arCost+=area.AreaPacket(jets,a,w["metric"],.5).stats["squaredNorm"]
        res=full.lm.labels(res,clock)
        return dict(metric=res["maxRelativeMetric"],curvature=res["maxCurvature"],held=res["minHeldDistance"],
            original=res["squaredNorm"]+arCost,area=arCost,guide=res["geometryMaximumViolations"],
            worstMetric=res["worstMetric"],worstCurvature=res["worstCurvature"])
    y=np.zeros(dimension)
    metadata.update(schema="actual-new-g-dual-clocked-HF-finite-full-Cartesian-joint-spectrum-and-14-rows-v1",
        entry=c.sha(__file__),sourceEvaluator=c.sha(full.__file__),metricScale=metric_scale,curvatureScale=shape_scale,
        fullCostFactor=args.original_weight,coordinateScale=args.coordinate_scale,
        betas=args.betas,iterationsPerBeta=args.iterations,preconditioner=pre.definition,rows=4291840,
        regularization=args.ridge,positiveSoftWeights="physical metric quadrature on both G10 groups",
        signedEigenvaluesPerPoint=8,additionalPhysicalPointSets=False,allSevenPhysicalGuidesInSmoothMaximum=True,
        sevenGuidePseudoHuberScale=args.guide_scale)
    msha=c.stable(metadata)
    cached=None;trace=[];gradcheck=None;stage_rows=[]
    def evaluate(y,beta,frozen):
        z=pre.unpack(args.coordinate_scale*y)
        agg=Reduction()
        agg.add(frozen,beta)
        for rec in active:agg.add(block_eval(rec,z,beta,True),beta)
        smooth=agg.ref+np.log(agg.mass/agg.weight)/beta
        f=smooth+args.original_weight*agg.c14+args.ridge*np.mean(y*y)
        raw=agg.grad/agg.mass+args.original_weight*agg.cgrad
        grad=args.coordinate_scale*pre.transpose(raw)+2*args.ridge*y/dimension
        return f,grad,dict(metric=agg.mpeak,curvature=agg.kpeak,original=agg.c14,regularized=f,smooth=smooth)
    for stage,beta in enumerate(args.betas):
        const=Reduction()
        for rec in fixed:const.add(block_eval(rec,blank(),beta,False),beta)
        frozen=const.fixed_record()
        f0,g0,stats=evaluate(y,beta,frozen)
        if stage==0:
            init_ind=independent(blank())
            if abs(stats["original"]-expect[0])>2e-10 or abs(init_ind["metric"]-expect[1])>2e-10:
                raise ArithmeticError("All original 14 rows in zero extension and G11 must match")
            v=np.random.default_rng(27186).standard_normal(dimension);v/=np.linalg.norm(v)
            eps=1e-4
            d1=evaluate(y+eps*v,beta,frozen)[0];d2=evaluate(y-eps*v,beta,frozen)[0]
            numerical=(d1-d2)/(2*eps);analytic=float(g0@v)
            gradcheck=dict(eps=eps,numerical=numerical,analytic=analytic,absolute=abs(numerical-analytic))
            if abs(numerical-analytic)>2e-8*max(1.,abs(numerical),abs(analytic)):
                raise ArithmeticError(("Full physical eight spectral and 14-row gradient mismatch",gradcheck))
            print(json.dumps(dict(initial=stats,gradient=gradcheck)),flush=True)
        neval=0
        def objective(vec):
            nonlocal cached,neval
            if cached is not None and np.array_equal(cached[0],vec):return cached[1],cached[2]
            f,g,stats=evaluate(vec,beta,frozen)
            cached=(vec.copy(),f,g,stats);neval+=1
            return f,g
        cached=(y.copy(),f0,g0,stats)
        def callback(vec):
            st=cached[3]
            if not np.array_equal(vec,cached[0]):raise ArithmeticError("Callback lost actual physical trial")
            trace.append(dict(stage=stage,beta=beta,iteration=len(trace)+1,eval=neval,**st))
            if len(trace)%5==1:print(json.dumps(trace[-1]),flush=True)
        result=minimize(objective,y,jac=True,method="L-BFGS-B",callback=callback,
            options=dict(maxiter=args.iterations,maxcor=14,ftol=1e-13,gtol=1e-9,maxls=24))
        y=result.x.copy()
        if not np.array_equal(y,cached[0]):objective(y)
        row=dict(stage=stage,beta=beta,iterations=result.nit,evals=neval,converged=bool(result.success),
            message=result.message,allG10=cached[3],independent=independent(pre.unpack(args.coordinate_scale*y)))
        stage_rows.append(row)
        data=dict(model=metadata,modelSHA256=msha,stages=stage_rows,trace=trace,gradientCheck=gradcheck,
            coefficients=pre.unpack(args.coordinate_scale*y).ravel().tolist(),timeSeconds=time.monotonic()-tic,
            wholeClosedReachCertified=False,continuousMetricCertified=False)
        sha=c.save(Path(str(args.prefix)+f"-{stage+1:02}.json"),data)
        print(json.dumps(dict(SHA=sha,**row,time=data["timeSeconds"])),flush=True)
        cached=None


slope=load(Path(__file__).with_name("2ecf-strong-stadium-lower-slope-complete.py"),"matched_stadium_base")


def actual_stadium(args):
    old_scales=args.metric_scale,args.curvature_scale
    args.metric_scale,args.curvature_scale=.105,13.
    try:
        definition,basis,clock,physical,g11,w,mods,radius,meta,_=slope.prepare(args)
    finally:
        args.metric_scale,args.curvature_scale=old_scales
    st=json.loads(args.fixed_stadium.read_text())
    if (st["model"]["stadiumEvaluatorV2"]!=c.sha(slope.__file__) or st["model"]["actualMetric"]!=meta["actualMetric"]
            or st["model"]["physicalBasis"]!=basis.definition or st["model"]["liftLength"]!=meta["liftLength"]
            or st["model"]["originalHFCarrier"]["priorStadiumPositionOnly"]!=c.sha(args.stadium_carrier)):
        raise ValueError("Same lower-slope material, physical coordinate family, and complete saved positions required")
    z=np.asarray(st["coefficients"]).reshape(basis.nb,basis.na)
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","stadium_guide_observer").direct_packet
    for name,obj in list(physical.items())+[("independent",g11)]:
        for j in range(0,len(obj.nodes),12):
            sl=slice(j,j+12);x=obj.nodes[sl]
            obj.jets[sl]+=direct(basis,x,z,obj.u) if name=="independent" else basis.packet(basis.matrices(x),z,len(obj.u))
    meta.update(fixedStadiumCompleteSource=c.sha(args.fixed_stadium),allGuideBudget=args.guide_scale,
        actualSameStadiumG=st["model"]["actualMetric"])
    return definition,basis,clock,physical,g11,w,mods,radius,meta,(st["stages"][-1]["allG10"]["original"],st["stages"][-1]["independent"]["metric"])


if __name__=="__main__":
    ap=slope.args_base()
    ap.add_argument("--fixed-stadium",type=Path,required=True)
    ap.add_argument("--guide-scale",type=float,default=.0025)
    args=ap.parse_args();args.resume=None
    full.prepare=actual_stadium
    main(args)
