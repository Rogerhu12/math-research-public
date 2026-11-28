#!/usr/bin/env python3
"""Physical core similarity and exact flat recut at radius .32, with an unscaled R293 cap."""
import importlib.util
from pathlib import Path
import sys
import time
import json
import numpy as np


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp)
    sys.modules[n]=m;sp.loader.exec_module(m);return m


here=Path(__file__).parent;obs=load(here/"2ecf-strong-stadium-elevated-independent-closed-pairs.py","raised_core_homothetic_observer")
elev=obs.elev;arb=obs.arb;c=arb.c;mat=elev.mat


def measure(P):
    return dict(ball=float(np.linalg.norm(P,axis=-1).max()),width=float(abs(P[...,1]).max()),height=float(abs(P[...,2]).max()))


def run(a):
    start=time.monotonic();f=elev.RaisedField(a);P,_,_,_,_=obs.cloud(f,a);scanned=measure(P)
    del P
    print(json.dumps(dict(actualShiftedCloudBudget=scanned)),flush=True)
    sets={k:elev.elevated_rows(f,k) for k in ("training","observer","independent")}
    budget={k:measure(Y[:,0]) for k,(_,_,Y,_,_) in sets.items()}
    # Prospective input is chosen only from the two original training grids.
    by={k:max(q[k] for name,q in budget.items() if name!="independent") for k in ("ball","width","height")}
    limits=dict(ball=1.582/by["ball"],width=.894/by["width"],height=.634/by["height"],cuff=.599/f.true_cuff_z)
    lam=float(a.factor) if a.factor else np.floor(min(limits.values())*1000)/1000
    if not 1<lam<=.60/f.true_cuff_z:raise ValueError((lam,limits))
    cuff=lam*f.true_cuff_z;A0=f.definition["pointConfig"]["central_a"]
    f.definition["pointConfig"].update(true_cuff_height=cuff,central_a=lam*A0)
    # New radial coordinate y=s*=lambda s. Reuse the old computational labels for inherited observations.
    gd0=f.dclock
    class ScaledLabel:
        def jets(self,x):return tuple(lam*p for p in gd0.jets(x))
    f.dclock=ScaledLabel()
    report={}
    for name,(x,u,Y,rad,w) in sets.items():
        Y*=np.array([lam,1,lam,1/lam,1,lam])[None,:,None,None];rad*=np.array([lam,1,1/lam])
        W={key:(val*lam if name!="independent" else val) for key,val in w.items()}
        report[name]=mat.observed(f,None,None,(x,u,Y,rad,W),None,None,False,a)
    del sets
    # The end material angle and its s/u derivatives are checked directly against the planar expressions.
    e=np.vstack((np.cos(u),np.sin(u),np.zeros(len(u)))).T;t=np.vstack((-np.sin(u),np.cos(u),np.zeros(len(u)))).T
    images=Y[-1]
    end=np.zeros_like(images);end[0]=.32*lam*e;end[0,:,2]=cuff;end[1]=-e;end[2]=.32*lam*t;end[4]=-t;end[5]=-.32*lam*e
    signCheck=float(np.max(abs(images-end)))
    # If the native outer sheet uses a constant angular origin/orientation, report a geometry-adapted jet regression too.
    actual=(images[0]-np.array([0.,0.,cuff]))/(.32*lam)
    tangent=images[2]/(.32*lam);chart=np.zeros_like(images);chart[0]=.32*lam*actual;chart[0,:,2]+=cuff
    chart[1]=-actual;chart[2]=.32*lam*tangent;chart[4]=-tangent;chart[5]=-.32*lam*actual
    nativeMatch=float(np.max(abs(images-chart)))
    if max(abs(np.linalg.norm(actual,axis=1)-1).max(),abs(np.sum(actual*tangent,axis=1)).max(),nativeMatch)>5e-8:raise ArithmeticError(("Scaled true cuff six-jet mismatch",signCheck,nativeMatch))
    t=np.linspace(0.,.32*(lam-1),17);rr=.32*lam-t
    ann=np.zeros((len(t),6,len(u),3));ann[:,0]=rr[:,None,None]*actual;ann[:,0,:,2]+=cuff;ann[:,1]=-actual
    ann[:,2]=rr[:,None,None]*tangent;ann[:,4]=-tangent;ann[:,5]=-rr[:,None,None]*actual
    cfg=f.stream.point.PointConfig(**f.definition["pointConfig"]);ones=np.ones((len(t),1))/len(u)
    pt=f.stream.point.PointLinearized(ann.swapaxes(1,2),rr[:,None],cfg,{k:ones for k in ("metric","curvature","geometry")})
    m=pt.metric
    mj=float(np.max(np.abs((m[...,0]+m[...,2])/2)+np.hypot((m[...,0]-m[...,2])/2,m[...,1]/np.sqrt(2))))
    out=dict(schema="actual-stadium-core-similarity-with-flat-cuff-recut-and-unscaled-R293-cap-v1",entry=c.sha(__file__),
        originalPhysical=[c.sha(v) for v in a.extra_state],elevation=c.sha(a.elevation),lambdaHex=float(lam).hex(),lambdaValue=lam,
        oldMetric=f.ident,newCoreMetric=dict(radialCoordinate="sStar=lambda*s",radius="fStar(sStar)=lambda*f(sStar/lambda)",
        extraPerHalf=.32*(lam-1),extraTarget="f(t)=.32*lambda-t",fixedCap="R293 recomputed at true ZStar, own induced metric"),
        newCuff=cuff,newCentralA=lam*A0,flatPortSixJetResidual=signCheck,actualFlatPortSixJetResidual=nativeMatch,
        extraAnnulus=dict(rows=len(t)*len(u)*14,points=len(t)*len(u),metric=mj,curvature=float(np.max(abs(pt.curvature["S"])))),
        budget=budget,separatePhysicalCloud=scanned,lamLimitsTrainingOnly=limits,normalizedMetricAndAllFourteenRows=report,
        scaledPhysicalCloud={k:lam*v for k,v in scanned.items()},sameOrderedPairRadiiMultiplyExactlyBy=lam,
        wholeClosedReachCertified=False,wholeClosedMetricCertified=False,seconds=time.monotonic()-start)
    sha=c.save(Path(str(a.prefix)+"-actual-core-dilation.json"),out)
    print(json.dumps(dict(scale=lam,budget=out["scaledPhysicalCloud"],ind=[report["independent"][k] for k in ("metric","curvature","held")],cuff=cuff,extra=out["extraAnnulus"],port=nativeMatch,SHA=sha)),flush=True)


if __name__=="__main__":
    ap=arb.parser();ap.add_argument("--elevation",type=Path,required=True);ap.add_argument("--count",type=int,default=128);ap.add_argument("--factor",type=float)
    args=ap.parse_args();args.resume=None;run(args)
