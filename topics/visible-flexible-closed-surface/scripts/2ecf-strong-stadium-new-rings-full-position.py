#!/usr/bin/env python3
"""Sequential finite linear minimax proposals and complete nonlinear physical evaluation on both G10 groups."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import argparse
import gc
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy import sparse
from scipy.optimize import linprog


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m


here=Path(__file__).parent
normal=load(here/"2ecf-strong-stadium-full-normal-correction.py","stadium_minimax_true_source")
joint,c=normal.joint,normal.c


def run(args):
    started=time.monotonic()
    gnew=load(here/"2ecf-strong-stadium-fresh-suffix-grid.py","stadium_augmented_real_grid")
    args.extra_state=[]
    sourcefield=gnew.src.Field(args)
    stream=sourcefield.stream;point=stream.point;definition=sourcefield.definition
    cfg=point.PointConfig(**definition["pointConfig"]);old=sourcefield.bd;clock=sourcefield.dclock;w={};phys={}
    meta=dict(actualMetric=sourcefield.ident)
    from types import SimpleNamespace
    for name,d in list(sourcefield.saved["caches"].items())+[("independent",gnew.src.rd(args.observer))]:
        x=np.asarray(d["physicalNodes"] if name=="independent" else d["nodes"]);u=np.asarray(d["angles"])
        if u.ndim==0:u=2*np.pi*np.arange(int(u))/int(u)
        Y=np.zeros((len(x),6,len(u),3));rad=np.zeros((len(x),3));sx,h,_=clock.jets(x)
        iz=np.flatnonzero(x<=sourcefield.end);outside=np.flatnonzero(x>sourcefield.end)
        for start in range(0,len(iz),10):
            sl=iz[start:start+10];Y[sl],rad[sl]=sourcefield.jets(x[sl],u)
        if c.sha(d["files"]["jets"])!=d["SHA256"]["jets"]:raise ValueError("Literal fixed outer R205 data required")
        cache=np.load(d["files"]["jets"],mmap_mode="r");Y[outside]=cache[outside];del cache
        rad[outside,0]=.8-(sx[outside]-clock.jets([sourcefield.end])[0][0]);rad[outside,1]=-1.
        obj=SimpleNamespace(jets=Y,radius=rad,nodes=x,u=u)
        if name=="independent":g11=obj
        else:
            phys[name]=obj;w[name]={kk:.5*np.asarray(v)*h for kk,v in d["weights"].items()}
        print(json.dumps(dict(event="complete literal new source",group=name,radials=len(x),angles=len(u))),flush=True)
    del Y,rad,sourcefield;gc.collect()
    oldstage=json.loads(args.previous.read_text())
    if oldstage["source"]!=c.sha(args.background) or oldstage["sourceMetric"]!=meta["actualMetric"]:
        raise ValueError("Same complete physical V24 background required")
    priorSpec=oldstage["physicalCorrectionBasis"]["sourceChartBasis"]
    priorRaw=stream.HalfTurnBasis(old.c,old.end,radial_count=priorSpec["radialBasisCount"],max_frequency=priorSpec["maxAngularFrequency"],
        normalized_breaks=priorSpec["normalizedBreaks"])
    prior=c.physical_basis(priorRaw,clock,meta["actualMetric"])
    if prior.definition!=oldstage["physicalCorrectionBasis"]:raise ValueError("Exact previous minimized physical basis required")
    priorZ=np.asarray(oldstage["coefficients"]).reshape(prior.nb,prior.na)
    shifted=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","true_stadium_previous_G11").direct_packet
    for n,o in list(phys.items())+[("independent",g11)]:
        for offset in range(0,len(o.nodes),16):
            sl=slice(offset,offset+16);x=o.nodes[sl]
            o.jets[sl]+=shifted(prior,x,priorZ,o.u) if n=="independent" else prior.packet(prior.matrices(x),priorZ,len(o.u))
    baseline=(sum(v["original"] for v in oldstage["states"][-1]["G10"].values()),oldstage["states"][-1]["independent"]["metric"])
    args.extra_state=[args.previous]
    sourcefield=gnew.src.Field(args)
    _,fresh=gnew.evaluate(sourcefield,args,return_arrays=True)
    if args.angular_offset!=0:raise ValueError("This augmented tensor stream uses actual unshifted supplemental angles")
    phys["fresh"]=fresh
    w["fresh"]={k:np.zeros(len(fresh.nodes)) for k in ("metric","curvature","geometry")}
    ts=np.linspace(0.,1.,args.controls+2)
    normalized=.11*ts+.89*ts*ts
    raw=stream.HalfTurnBasis(old.c,old.end,radial_count=args.controls,max_frequency=args.modes,normalized_breaks=normalized)
    raw.channels=sourcefield.full_channels(args.modes);raw.na=len(raw.channels);raw.modes=np.array([q[1] for q in raw.channels])
    raw.dimension=raw.nb*raw.na
    raw.definition=dict(schema="actual-unrestricted-all-XYZ-new-ring-minimax-space-v1",physicalKnots=raw.knots.tolist(),
        degree=5,radialBasisCount=raw.nb,maxAngularFrequency=raw.M,angularChannels=raw.na,dimension=raw.dimension,
        channelOrder=[dict(component=i,frequency=k,kind=kind) for i,k,kind in raw.channels],reflectionOrHalfTurnRestrictions=False,
        allSixEndpointJetsExactlyZero=True)
    basis=c.physical_basis(raw,clock,meta["actualMetric"]);del sourcefield;gc.collect()
    from scipy.optimize._highspy import _core
    _core._Highs.resetGlobalScheduler(True)
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","stadium_minimax_area")
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","stadium_minimax_G11").direct_packet
    idx=np.array([q[0] for q in basis.channels]);k=np.array([q[1] for q in basis.channels]);cos=np.array([q[2]=="cos" for q in basis.channels])
    scales=np.broadcast_to(1/(1+k*k/18),(basis.nb,basis.na))
    def guide_grad(X):
        r=np.linalg.norm(X,axis=-1);rad=np.hypot(X[...,0],X[...,1])
        Yp=X-np.array([0.,cfg.central_a,0.]);Ym=X+np.array([0.,cfg.central_a,0.])
        t=np.clip((rad-cfg.height_radial_start)/(cfg.height_radial_end-cfg.height_radial_start),0,1)
        slope=cfg.height_maximum*30*t*t*(1-t)**2/(cfg.height_radial_end-cfg.height_radial_start)
        side=np.zeros_like(X);side[...,:2]=X[...,:2]*np.divide(slope,rad,out=np.zeros_like(slope),where=rad>0)[...,None]
        G=np.zeros((*X.shape[:-1],7,3));G[...,0,:]=X/r[...,None];G[...,1,1]=1;G[...,2,1]=-1
        G[...,3,:]=np.array([0.,0.,1.])-side;G[...,4,:]=np.array([0.,0.,-1.])-side
        G[...,5,:]=-Yp/np.linalg.norm(Yp,axis=-1)[...,None];G[...,6,:]=-Ym/np.linalg.norm(Ym,axis=-1)[...,None]
        return G
    def observe(groups,z,derivative,shift=None,cutoff=None):
        rows=[];rhs=[];types=[];grad=np.zeros_like(z);summary={}
        for name,o in groups.items():
            N=len(o.u);angles=o.u[:,None]*k[None,:]
            trig=np.where(cos,np.cos(angles),np.sin(angles));trig1=np.where(cos,-np.sin(angles),np.cos(angles))*k
            trigs=(trig,trig1,-trig*k*k)
            st=None;cost=0.;nkeep=0
            for start in range(0,len(o.nodes),args.block):
                sl=slice(start,start+args.block);x=o.nodes[sl];B=basis.matrices(x);a=o.radius[sl,0,None]
                packet=o.jets[sl]+(direct(basis,x,z,o.u) if name=="independent" else basis.packet(B,z,N))
                weights={k:np.ones_like(a)/N for k in ("metric","geometry","curvature")} if name=="independent" else {k:v[sl,None]/N for k,v in w[name].items()}
                pt=point.PointLinearized(packet.swapaxes(1,2),a,cfg,weights);ar=area.AreaPacket(packet,a,weights["metric"],.5)
                spec=stream._block_statistics(pt,x,N)
                for key in ("worstMetric","worstCurvature"):spec[key]["u"]+=o.u[0]
                st=stream._merge_statistics(st,spec)
                cost+=ar.stats["squaredNorm"]
                if not derivative:continue
                if shift is None:
                    cbar=pt.vjp(2*pt.residual);sb,ub=ar.vjp(2*ar.residual)
                    cbar[...,1,:]+=sb;cbar[...,2,:]+=ub
                    grad+=basis.packet_adjoint(B,cbar.swapaxes(1,2))
                g0=pt.metric;h0=pt.curvature["S"];gg=guide_grad(pt.jets[...,0,:])
                guide0=pt.geometry["signed"];g,h,guide=g0,h0,guide0
                if shift is not None:
                    vjet=basis.packet(B,shift,N).swapaxes(1,2);S0=pt.jets[...,1,:];U0=pt.jets[...,2,:]
                    S1=vjet[...,1,:];U1=vjet[...,2,:]
                    dg0=np.stack((2*point.dot(S0,S1),np.sqrt(2)*(point.dot(S0,U1)+point.dot(S1,U0))/a,
                        2*point.dot(U0,U1)/a**2),axis=-1)
                    g=g0+dg0;h=h0+point.curvature_jvp(pt.jets,pt.curvature,vjet)
                    guide=guide0+np.einsum("...ij,...j->...i",gg,vjet[...,0,:])
                gm=joint.signed_eigensystem(g[...,0],g[...,1]/np.sqrt(2),g[...,2],args.metric_scale)
                hs=joint.signed_eigensystem(h[...,0],h[...,1],h[...,2],args.curvature_scale)
                vals=np.stack((gm[0],-gm[1],hs[0],-hs[1],*[v/args.guide_scale for v in np.moveaxis(guide,-1,0)]))
                # Select extremal linear supports sector by sector; acceptance below sees all actual points.
                size=N//args.sectors
                if N%args.sectors:raise ValueError("Complete physical angular partition")
                resh=vals.reshape(11,len(x),args.sectors,size).transpose(0,2,1,3).reshape(11,args.sectors,-1)
                hits=np.argmax(resh,axis=-1);value=resh[np.arange(11)[:,None],np.arange(args.sectors)[None,:],hits]
                threshold=np.full(11,args.floor) if cutoff is None else np.asarray(cutoff)
                kinds,secs=np.where(value>threshold[:,None])
                if not len(kinds):continue
                pick=hits[kinds,secs];ri=pick//size;ui=secs*size+pick%size
                rr=np.arange(len(ri));arr=pt.jets[ri,ui];bar=np.zeros_like(arr);base_value=np.zeros(len(ri))
                for group,eig,scale in ((0,gm,args.metric_scale),(1,hs,args.curvature_scale)):
                    pos=kinds==2*group;neg=kinds==2*group+1
                    dg=joint.eigen_pullback(pos.astype(float),-neg.astype(float),eig[2][ri,ui],eig[3][ri,ui],scale)
                    if group:
                        base_value+=np.sum(dg*h0[ri,ui],axis=-1)
                        bar+=point.curvature_vjp(arr,point.curvature_cache(arr),dg)
                    else:
                        gg0=g0[ri,ui].copy();gg0[:,1]/=np.sqrt(2)
                        base_value+=np.sum(dg*gg0,axis=-1)
                        aa=a[ri,0];xs,xu=arr[:,1],arr[:,2];cross=dg[:,1]/aa
                        bar[:,1]+=2*dg[:,0,None]*xs+cross[:,None]*xu
                        bar[:,2]+=cross[:,None]*xs+2*(dg[:,2]/aa**2)[:,None]*xu
                gmask=kinds>=4
                bar[gmask,0]=gg[ri[gmask],ui[gmask],kinds[gmask]-4]/args.guide_scale
                base_value[gmask]=guide0[ri[gmask],ui[gmask],kinds[gmask]-4]/args.guide_scale
                deriv=np.zeros((len(kinds),basis.nb,basis.na))
                for j,(rs,us) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
                    spatial=bar[:,j,idx]*trigs[us][ui]
                    deriv+=B[rs][ri].toarray()[:,:,None]*spatial[:,None,:]
                rows.append(sparse.csr_matrix((deriv*scales).reshape(len(kinds),-1)))
                rhs.append(base_value);types.append(kinds);nkeep+=len(ri)
            st=joint.full.lm.labels(st,clock)
            summary[name]=dict(rows=len(o.nodes)*N*14,metric=st["maxRelativeMetric"],curvature=st["maxCurvature"],
                held=st["minHeldDistance"],guide=st["geometryMaximumViolations"],original=st["squaredNorm"]+cost,
                area=cost,worstMetric=st["worstMetric"],worstCurvature=st["worstCurvature"],linearWitnessRows=nkeep)
        return summary,rows,rhs,grad,types
    def merit(obs):
        peak=max(max(v["metric"]/args.metric_scale,v["curvature"]/args.curvature_scale,max(v["guide"].values())/args.guide_scale) for v in obs.values())
        cost=sum(x["original"] for x in obs.values())
        return peak+args.original_weight*cost,peak
    z=np.zeros((basis.nb,basis.na));trust=args.trust;state=[]
    if args.restart_state:
        prev=c.sha(args.previous);st=json.loads(args.restart_state.read_text())
        if (st["previousPhysicalCorrection"]!=prev or st["source"]!=c.sha(args.background) or st["physicalCorrectionBasis"]!=basis.definition
                or st["hardCurvature"]!=args.hard_curvature or st["metricScale"]!=args.metric_scale or st["guideScale"]!=args.guide_scale):
            raise ValueError("Same full all-angle augmented physical problem required for restart")
        z=np.asarray(st["coefficients"]).reshape(basis.nb,basis.na);state=st["states"];trust=state[-1]["nextTrust"]
    for it in range(len(state),args.steps):
        base,J,val,grad,types=observe(phys,z,True)
        f0,peak0=merit(base);cost0=sum(x["original"] for x in base.values());n=z.size
        if it==0 and any(v["curvature"]>args.hard_curvature or max(v["guide"].values())>args.hard_guide for v in base.values()):
            raise ValueError("Proposed complete G10 comparison bounds must include the saved starting shape")
        if it==0 and abs(cost0-baseline[0])>2e-10:raise ArithmeticError(("All 4291840 row source failed",cost0,baseline[0]))
        eye=sparse.eye(n,format="csr");zero=sparse.csr_matrix((n,1))
        objective=np.r_[args.original_weight*(grad*scales).ravel(),1.,np.full(n,args.l1)]
        trials=[];acceptance_receipts=[];accepted=False
        for rep in range(3):
            for exchange in range(args.exchange):
                H=sparse.vstack(J,format="csr");v=np.concatenate(val);kind=np.concatenate(types)
                soft=sparse.vstack((sparse.hstack((H,-np.ones((H.shape[0],1)),sparse.csr_matrix(H.shape))),
                    sparse.hstack((eye,zero,-eye)),sparse.hstack((-eye,zero,-eye))),format="csr")
                protect=(kind>=2)
                caps=np.where(kind<4,(args.hard_curvature-.015)/args.curvature_scale,(args.hard_guide-.00002)/args.guide_scale)
                hard=sparse.hstack((H[protect],sparse.csr_matrix((int(protect.sum()),n+1))),format="csr")
                A=sparse.vstack((soft,hard),format="csr");right=np.r_[-v,np.zeros(2*n),(caps-v)[protect]]
                opt=linprog(objective,A_ub=A,b_ub=right,bounds=[(-trust,trust)]*n+[(0,None)]+[(0,trust)]*n,method="highs",options={"threads":1,"parallel":False})
                if not opt.success:raise ArithmeticError(opt.message)
                del A,soft,hard;gc.collect()
                direction=opt.x[:n].reshape(z.shape)*scales
                pred=opt.x[n]
                threshold=np.minimum(np.full(11,pred),np.r_[np.inf,np.inf,np.full(2,(args.hard_curvature-.015)/args.curvature_scale),
                    np.full(7,(args.hard_guide-.00002)/args.guide_scale)])+args.linear_tolerance
                _,newJ,newv,_,newkind=observe(phys,z,True,shift=direction,cutoff=threshold)
                added=sum(x.shape[0] for x in newJ)
                acceptance_receipts.append(dict(outer=rep,exchange=exchange,trust=trust,cutCountBefore=H.shape[0],added=added,epigraph=pred))
                if not added:break
                J.extend(newJ);val.extend(newv);types.extend(newkind)
            for factor in (1.,.5,.25,.125,.0625):
                test=observe(phys,z+factor*direction,False)[0];ft,peakt=merit(test)
                trials.append(dict(trust=trust,factor=factor,merit=ft,peak=peakt,original=sum(x["original"] for x in test.values())))
                feasible=all(a["curvature"]<=args.hard_curvature and max(a["guide"].values())<=args.hard_guide for a in test.values())
                trials[-1]["fullG10HardFeasible"]=feasible
                if ft<f0-1e-9 and feasible:
                    z+=factor*direction;accepted=True;trust=min(args.limit,trust*(1.25 if factor>=.5 else .75));break
            if accepted:break
            trust*=.35
        accepted_report=test if accepted else base
        af,ap=merit(accepted_report)
        independent=observe({"independent":g11},z,False)[0]["independent"]
        if it==0 and not accepted and abs(independent["metric"]-baseline[1])>2e-10:raise ArithmeticError("Independent source mismatch")
        event=dict(iteration=it+1,accepted=accepted,true14Rows=4291840,freshPhysicalPoints=len(fresh.nodes)*len(fresh.u),variables=n,witnessRows=H.shape[0],oldMerit=f0,newMerit=af,oldPeak=peak0,newPeak=ap,trials=trials,linearExchange=acceptance_receipts,
            G10=accepted_report,independent=independent,nextTrust=trust)
        state.append(event)
        data=dict(schema="actual V24 broad stadium constrained minimax source",entry=c.sha(__file__),source=c.sha(args.background),sourceMetric=meta["actualMetric"],
            physicalCorrectionBasis=basis.definition,metricScale=args.metric_scale,curvatureScale=args.curvature_scale,guideScale=args.guide_scale,
            previousPhysicalCorrection=c.sha(args.previous),hardCurvature=args.hard_curvature,hardAllSevenGuide=args.hard_guide,originalCostFactor=args.original_weight,l1=args.l1,retainedAllCartesianCrosses=True,fullG10LinearSpectralSeparation=True,trainingOnlyWitnessExchange=True,extraPhysicalRadii=len(fresh.nodes),extraAngles=len(fresh.u),extraOriginalCostWeight=0,
            independentG11UsedForChoice=False,states=state,coefficients=z.ravel().tolist(),wholeClosedReachCertified=False,
            continuousMetricCertified=False,seconds=time.monotonic()-started)
        dg=c.save(Path(str(args.prefix)+f"-ex{it+1:02}.json"),data)
        print(json.dumps(dict(iteration=it+1,accepted=accepted,G10merit=af,oldMerit=f0,independent=[independent[k] for k in ("metric","curvature","held")],witnessRows=H.shape[0],SHA=dg)),flush=True)
        if not accepted:break


if __name__=="__main__":
    ap=joint.slope.args_base()
    for name in ("fixed-stadium","prior-guide","projected","redesigned-state","background","previous","radius-spec","design-spec","longer-spec"):ap.add_argument("--"+name,type=Path,required=True)
    for name,v in (("guide-scale",.002),("box",.25),("first",3.),("second",65.),("extension",.04),("add-length",.014),("radius-blend",.18),
        ("linear-tolerance",.003),("hard-curvature",11.66),("hard-guide",.0025),("curvature-tau",2.),("metric-sextic",.2),("trust",.0014),("limit",.004),("l1",.03),("floor",.68)):ap.add_argument("--"+name,type=float,default=v)
    for name,v in (("directions",20),("divisions",9),("exchange",6),("correction-frequency",12),("controls",20),("modes",8),("sectors",8),("steps",10)):ap.add_argument("--"+name,type=int,default=v)
    ap.add_argument("--blends",type=float,nargs="+",default=[.06,.095,.14,.19,.25,.33,.42])
    ap.add_argument("--new-angles",type=int,default=320);ap.add_argument("--subdivisions",type=int,default=4)
    ap.add_argument("--offset",type=float,default=.271);ap.add_argument("--angular-offset",type=float,default=0.)
    ap.add_argument("--restart-state",type=Path)
    args=ap.parse_args();args.resume=None
    run(args)
