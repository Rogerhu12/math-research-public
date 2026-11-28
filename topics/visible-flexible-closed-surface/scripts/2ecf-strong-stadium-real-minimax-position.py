#!/usr/bin/env python3
"""Sequential finite linear minimax proposals and complete nonlinear physical evaluation on both G10 groups."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import argparse
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
    definition,old,clock,phys,g11,w,mods,_,meta,baseline=normal.prepare(args)
    stream=mods["stream"];point=stream.point;cfg=point.PointConfig(**definition["pointConfig"])
    raw=stream.HalfTurnBasis(old.c,old.end,radial_count=args.controls,max_frequency=args.modes,
        normalized_breaks=np.linspace(0,1,args.controls+2)**1.25)
    basis=c.physical_basis(raw,clock,meta["actualMetric"])
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","stadium_minimax_area")
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","stadium_minimax_G11").direct_packet
    idx=np.array([q[0] for q in basis.channels]);k=np.array([q[1] for q in basis.channels]);cos=np.array([q[2]=="cos" for q in basis.channels])
    scales=np.broadcast_to(1/(1+k*k/18),(basis.nb,basis.na))
    def observe(groups,z,derivative):
        rows=[];rhs=[];grad=np.zeros_like(z);summary={}
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
                cbar=pt.vjp(2*pt.residual);sb,ub=ar.vjp(2*ar.residual)
                cbar[...,1,:]+=sb;cbar[...,2,:]+=ub
                grad+=basis.packet_adjoint(B,cbar.swapaxes(1,2))
                g=pt.metric;h=pt.curvature["S"]
                gm=joint.signed_eigensystem(g[...,0],g[...,1]/np.sqrt(2),g[...,2],args.metric_scale)
                hs=joint.signed_eigensystem(h[...,0],h[...,1],h[...,2],args.curvature_scale)
                vals=np.stack((gm[0],-gm[1],hs[0],-hs[1],*[v/args.guide_scale for v in np.moveaxis(pt.geometry["residual"],-1,0)]))
                # Select extremal linear supports sector by sector; acceptance below sees all actual points.
                size=N//args.sectors
                if N%args.sectors:raise ValueError("Complete physical angular partition")
                resh=vals.reshape(11,len(x),args.sectors,size).transpose(0,2,1,3).reshape(11,args.sectors,-1)
                hits=np.argmax(resh,axis=-1);value=resh[np.arange(11)[:,None],np.arange(args.sectors)[None,:],hits]
                kinds,secs=np.where(value>args.floor)
                if not len(kinds):continue
                pick=hits[kinds,secs];ri=pick//size;ui=secs*size+pick%size
                rr=np.arange(len(ri));arr=pt.jets[ri,ui];bar=np.zeros_like(arr)
                for group,eig,scale in ((0,gm,args.metric_scale),(1,hs,args.curvature_scale)):
                    pos=kinds==2*group;neg=kinds==2*group+1
                    dg=joint.eigen_pullback(pos.astype(float),-neg.astype(float),eig[2][ri,ui],eig[3][ri,ui],scale)
                    if group:
                        bar+=point.curvature_vjp(arr,point.curvature_cache(arr),dg)
                    else:
                        aa=a[ri,0];xs,xu=arr[:,1],arr[:,2];cross=dg[:,1]/aa
                        bar[:,1]+=2*dg[:,0,None]*xs+cross[:,None]*xu
                        bar[:,2]+=cross[:,None]*xs+2*(dg[:,2]/aa**2)[:,None]*xu
                gmask=kinds>=4
                bar[gmask,0]=pt.geometry["jacobian"][ri[gmask],ui[gmask],kinds[gmask]-4]/args.guide_scale
                deriv=np.zeros((len(kinds),basis.nb,basis.na))
                for j,(rs,us) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
                    spatial=bar[:,j,idx]*trigs[us][ui]
                    deriv+=B[rs][ri].toarray()[:,:,None]*spatial[:,None,:]
                rows.append(sparse.csr_matrix((deriv*scales).reshape(len(kinds),-1)))
                rhs.append(value[kinds,secs]);nkeep+=len(ri)
            st=joint.full.lm.labels(st,clock)
            summary[name]=dict(rows=len(o.nodes)*N*14,metric=st["maxRelativeMetric"],curvature=st["maxCurvature"],
                held=st["minHeldDistance"],guide=st["geometryMaximumViolations"],original=st["squaredNorm"]+cost,
                area=cost,worstMetric=st["worstMetric"],worstCurvature=st["worstCurvature"],linearWitnessRows=nkeep)
        return summary,rows,rhs,grad
    def merit(obs):
        peak=max(max(v["metric"]/args.metric_scale,v["curvature"]/args.curvature_scale,max(v["guide"].values())/args.guide_scale) for v in obs.values())
        cost=sum(x["original"] for x in obs.values())
        return peak+args.original_weight*cost,peak
    z=np.zeros((basis.nb,basis.na));trust=args.trust;state=[]
    for it in range(args.steps):
        base,J,val,grad=observe(phys,z,True)
        f0,peak0=merit(base);cost0=sum(x["original"] for x in base.values());n=z.size
        if it==0 and abs(cost0-baseline[0])>2e-10:raise ArithmeticError(("All 4291840 row source failed",cost0,baseline[0]))
        H=sparse.vstack(J,format="csr");v=np.concatenate(val)
        # Max-affine linearization, independently scaled coefficient trust box and small l1 step cost.
        # The full original 14-row objective contributes its complete gradient in every step.
        eye=sparse.eye(n,format="csr");zero=sparse.csr_matrix((n,1))
        A=sparse.vstack((sparse.hstack((H,-np.ones((H.shape[0],1)),sparse.csr_matrix(H.shape))),
            sparse.hstack((eye,zero,-eye)),sparse.hstack((-eye,zero,-eye))),format="csr")
        objective=np.r_[args.original_weight*(grad*scales).ravel(),1.,np.full(n,args.l1)]
        trials=[];accepted=False
        for rep in range(3):
            opt=linprog(objective,A_ub=A,b_ub=np.r_[-v,np.zeros(2*n)],bounds=[(-trust,trust)]*n+[(0,None)]+[(0,trust)]*n,method="highs")
            if not opt.success:raise ArithmeticError(opt.message)
            direction=opt.x[:n].reshape(z.shape)*scales
            for factor in (1.,.5,.25,.125,.0625):
                test=observe(phys,z+factor*direction,False)[0];ft,peakt=merit(test)
                trials.append(dict(trust=trust,factor=factor,merit=ft,peak=peakt,original=sum(x["original"] for x in test.values())))
                if ft<f0-1e-9:
                    z+=factor*direction;accepted=True;trust=min(args.limit,trust*(1.25 if factor>=.5 else .75));break
            if accepted:break
            trust*=.35
        accepted_report=test if accepted else base
        af,ap=merit(accepted_report)
        independent=observe({"independent":g11},z,False)[0]["independent"]
        if it==0 and not accepted and abs(independent["metric"]-baseline[1])>2e-10:raise ArithmeticError("Independent source mismatch")
        event=dict(iteration=it+1,accepted=accepted,true14Rows=4291840,variables=n,witnessRows=H.shape[0],oldMerit=f0,newMerit=af,oldPeak=peak0,newPeak=ap,trials=trials,
            G10=accepted_report,independent=independent,nextTrust=trust)
        state.append(event)
        data=dict(schema="actual V24 broad stadium constrained minimax source",entry=c.sha(__file__),source=c.sha(args.background),sourceMetric=meta["actualMetric"],
            physicalCorrectionBasis=basis.definition,metricScale=args.metric_scale,curvatureScale=args.curvature_scale,guideScale=args.guide_scale,
            originalCostFactor=args.original_weight,l1=args.l1,retainedAllCartesianCrosses=True,trainingOnlyWitnessExchange=True,
            independentG11UsedForChoice=False,states=state,coefficients=z.ravel().tolist(),wholeClosedReachCertified=False,
            continuousMetricCertified=False,seconds=time.monotonic()-started)
        dg=c.save(Path(str(args.prefix)+f"-ex{it+1:02}.json"),data)
        print(json.dumps(dict(iteration=it+1,accepted=accepted,G10merit=af,oldMerit=f0,independent=[independent[k] for k in ("metric","curvature","held")],witnessRows=H.shape[0],SHA=dg)),flush=True)
        if not accepted:break


if __name__=="__main__":
    ap=joint.slope.args_base()
    for name in ("fixed-stadium","prior-guide","projected","redesigned-state","background"):ap.add_argument("--"+name,type=Path,required=True)
    for name,v in (("guide-scale",.002),("box",.25),("first",3.),("second",65.),("extension",.04),("add-length",.014),("radius-blend",.18),
        ("curvature-tau",2.),("metric-sextic",.2),("trust",.0014),("limit",.004),("l1",.03),("floor",.68)):ap.add_argument("--"+name,type=float,default=v)
    for name,v in (("directions",20),("divisions",9),("correction-frequency",12),("controls",20),("modes",8),("sectors",8),("steps",10)):ap.add_argument("--"+name,type=int,default=v)
    ap.add_argument("--blends",type=float,nargs="+",default=[.06,.095,.14,.19,.25,.33,.42])
    args=ap.parse_args();args.resume=None
    run(args)
