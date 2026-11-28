#!/usr/bin/env python3
"""Replace the actual high-curvature front by a longer proven p32 ruling and rejoin full data."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse
import copy
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import BSpline


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);o=importlib.util.module_from_spec(sp);sys.modules[n]=o;sp.loader.exec_module(o);return o


sdir=Path(__file__).parent
red=load(sdir/"2ecf-strong-stadium-positive-diagonal-redesign.py","shorter_source_stadium")
joint=red.joint;c=red.c
physical=joint.slope.base
pairs=physical.pairs


def product_blend(old,development,t,L):
    a,b,c2=physical.step(t)
    a=a[:,None,None];b=b[:,None,None]/L;c2=c2[:,None,None]/L**2
    diff=old-development
    out=development+a[:,None]*diff
    out[:,1]+=b*diff[:,0]
    out[:,3]+=2*b*diff[:,1]+c2*diff[:,0]
    out[:,4]+=b*diff[:,2]
    return out


def scalar_blend(old,left,t,L):
    a,b,d=physical.step(t);b/=L;d/=L**2
    diff=old-left
    out=left+a[:,None]*diff
    out[:,1]+=b*diff[:,0];out[:,2]+=2*b*diff[:,1]+d*diff[:,0]
    return out


def develop(port,d):
    out=np.empty((len(d),6,len(port["P"]),3));u=d[:,None,None]
    for n,(i,j) in enumerate(pairs):
        ep=[port[q+"u"*j] for q in ("P","V","A")]
        if i==0:out[:,n]=ep[0]+u*ep[1]+.5*u*u*ep[2]
        elif i==1:out[:,n]=ep[1]+u*ep[2]
        else:out[:,n]=ep[2]
    return out


def prepare(args):
    # First reconstruct the actual held-feasible field on its independently frozen two-factor clock.
    oldsc=args.metric_scale,args.curvature_scale
    args.metric_scale,args.curvature_scale=.08,11.3
    try:
        definition,prior,clock0,train,g11,w,mods,radius,meta,_=red.prepare(args)
    finally:
        args.metric_scale,args.curvature_scale=oldsc
    warm=json.loads(args.redesigned_state.read_text())
    if (warm["model"]["actualMetric"]!=meta["actualMetric"] or warm["model"]["physicalBasis"]!=prior.definition
            or warm["model"]["heldFeasiblePhysicalSource"]!=c.sha(args.projected)):
        raise ValueError("Actual frozen p32 source and real outer XYZ required")
    z=np.asarray(warm["coefficients"]).reshape(prior.nb,prior.na)
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","long_coast_G11").direct_packet
    groups=dict(**train,independent=g11)
    raw=copy.copy(prior);del raw.matrices;raw.definition=prior.definition["sourceChartBasis"]
    grid=train["observer"].nodes
    ids=np.flatnonzero((grid>raw.c)&(clock0.jets(grid)[0]<=raw.c+args.extension))
    if not len(ids):raise ValueError("An actual training radius is required for a new physical port")
    idx=int(ids[-1]);cutoff=float(grid[idx])
    b=raw.c;newb=clock0.jets([cutoff])[0][0]
    if newb<=b or newb-b>.04+1e-14:raise ValueError("Actual strict extension within proven .06 physical ruling required")
    clock=physical.Clock(clock0,newb,raw.end,args.add_length)
    S=clock.jets([raw.end])[0][0]
    ob=train["observer"];axis=np.arange(len(ob.u))*2*np.pi/len(ob.u)
    if max(abs(axis-ob.u))>3e-14:raise ValueError("Real full unshifted port ring required")
    oldRing=ob.jets[idx]+prior.packet(prior.matrices([cutoff]),z,len(axis))[0]
    yfft=np.fft.rfft(oldRing[[0,1,3]],axis=1)/len(axis)
    # Reconstruct a precisely defined smooth finite trace. Real FFT Nyquist has a single cosine.
    mult=np.full(len(yfft[0]),2.);mult[0]=mult[-1]=1.
    yfft*=mult[None,:,None]
    wave=np.arange(len(mult))
    def trig_port(u):
        F=np.exp(1j*u[:,None]*wave)
        return {name+"u"*j:np.einsum("uk,kc->uc",F*(1j*wave)**j,yfft[i],optimize=True).real
            for i,name in enumerate(("P","V","A")) for j in range(3)}
    src=physical.Prefix(args,b)
    p0=src.master
    ell=p0.coast+newb-b
    f0=p0.curve.a+p0.v*ell
    raw.knots=np.r_[np.full(6,cutoff),raw.knots[raw.knots>cutoff]]
    raw.breaks=np.unique(raw.knots);raw.c=cutoff;raw.full_count=len(raw.knots)-6;raw.nb=raw.full_count-6
    raw.dimension=raw.nb*raw.na;raw._spline=BSpline(raw.knots,np.eye(raw.full_count),5,extrapolate=False)
    raw.definition=dict(schema="genuine-longer-physical-ruling-clamped-position-suffix-v1",
        physicalKnots=raw.knots.tolist(),degree=5,physicalDomain=[raw.c,raw.end],angularChannels=raw.na,
        radialBasisCount=raw.nb,maxAngularFrequency=raw.M,dimension=raw.dimension,
        sixTrueZeroEndpointJets=True,literalMother=meta["physicalBasis"]["sourceChartBasis"])
    saved=json.loads(args.prepared.read_text());cap={}
    # Keep one unblended suffix copy, trimmed exactly to the G10/G11 variable radial segment.
    # Each candidate is formed by the literal development and old physical jet, never incremental differences.
    for name,obj in groups.items():
        x=obj.nodes;orig_s=clock0.jets(x)[0]
        s,q,qp=clock.relative(orig_s)
        _,h,hx=clock.jets(x);obj.s,obj.h,obj.hx=s,h,hx
        for j in range(0,len(x),12):
            sl=slice(j,j+12);xx=x[sl]
            obj.jets[sl]+=direct(prior,xx,z,obj.u) if name=="independent" else prior.packet(prior.matrices(xx),z,len(obj.u))
            obj.jets[sl]=c.physical_jet(obj.jets[sl],q[sl],qp[sl])
        if name!="independent":w[name]={k:.5*np.asarray(v)*h for k,v in saved["caches"][name]["weights"].items()}
        ir=np.flatnonzero((x>b)&(x<=cutoff))
        for j in ir:
            sigma=p0.coast+(s[j]-b)
            port=p0.coast_port(sigma,obj.u)
            obj.jets[j]=np.stack([port[k] for k in ("P","V","Pu","A","Vu","Puu")])
        right=np.flatnonzero((s>newb)&(s<newb+max(args.blends)))
        ep=p0.coast_port(ell,obj.u)
        approx=trig_port(obj.u)
        diff=physical.difference(ep,approx)
        cap[name]=(right,obj.jets[right].copy(),develop(approx,s[right]-newb),diff)
        a,aa,aaa=obj.radius.T
        obj.radius=np.column_stack((a,aa/q,aaa/q**2-aa*qp/q**3))
        obj.radius[ir,0]=p0.curve.a+p0.v*(p0.coast+s[ir]-b)
        obj.radius[ir,1]=p0.v;obj.radius[ir,2]=0.
        jr=np.flatnonzero((s>newb)&(s<newb+args.radius_blend))
        tv=s[jr]-newb;left=np.column_stack((f0+p0.v*tv,np.full(len(tv),p0.v),np.zeros(len(tv))))
        obj.radius[jr]=scalar_blend(obj.radius[jr],left,tv/args.radius_blend,args.radius_blend)
    def apply(name,L):
        obj=groups[name];ii,old,dev,diff=cap[name];d=obj.s[ii]-newb
        hit=d<args.seam_width
        obj.jets[ii]=old
        if np.any(hit):obj.jets[ii[hit]]=product_blend(old[hit],dev[hit],d[hit]/args.seam_width,args.seam_width)
        physical.add_lift(obj.jets,obj.s-newb,diff,L,1.)
    spec=dict(schema="p32-actual-longer-ruling-extended-material-new-positive-profile-v1",entry=c.sha(__file__),
        oldClock=meta["actualMetric"],priorPhysical=c.sha(args.redesigned_state),newEndOfLockedCoast=float(newb),
        syntheticPortFromActualG10=True,portFFTInputCount=len(axis),seamCancellationWidth=args.seam_width,
        frozenFourierPortSHA=c.stable([yfft.real.tolist(),yfft.imag.tolist()]),oldComputationalCut=float(cutoff),wholeCoastRealLength=float(ell),newCut=float(S),extraMaterial=args.add_length,
        referenceRuling=c.sha(args.stadium_coast),radiusBlendWidth=args.radius_blend,
        addedGeometry="genuine normalized R137 ruling from old .02 to new physical front",
        angularTarget="affine new coast then convex H5 blend from affine extension to positive old target pulled only in f")
    target=c.stable(spec);basis=c.physical_basis(raw,clock,target)
    log=[]
    for L in args.blends:
        if L<=0 or newb+L>=S:raise ValueError("Compact physical blend required")
        for name in train:apply(name,L)
        rr=joint.hf.sample(train,mods,saved,definition,clock,args)
        cost=max(max(v["metric"]/args.metric_scale,v["curvature"]/args.curvature_scale,
            max(v["guide"].values())/args.guide_scale) for v in rr.values())
        log.append(dict(length=L,score=cost,allG10=rr))
        print(json.dumps(dict(event="actual_longer_coast",L=L,objective=cost,metric=max(v["metric"] for v in rr.values()),
            curvature=max(v["curvature"] for v in rr.values()),held=min(v["held"] for v in rr.values()))),flush=True)
    chosen=min(log,key=lambda r:r["score"])
    for name in groups:apply(name,chosen["length"])
    cap.clear()
    ind=joint.hf.sample({"independent":g11},mods,saved,definition,clock,args)["independent"]
    model=dict(newG=spec,SHA=target,fullSamples=log,chosen=chosen["length"],independent=ind,spatialColumns=raw.dimension,
        newMaterialRulingSource=c.sha(args.stadium_coast),frozenObservablePrefixIncludesExtendedActualRuling=True,usesG11ForChoice=False)
    c.save(Path(str(args.prefix)+"-longer.json"),model)
    meta.update(actualMetric=target,physicalBasis=basis.definition,longerRuling=spec,freeXYZ=raw.dimension,
        trueBlendLength=chosen["length"],newDefinitionEventCount=0)
    print(json.dumps(dict(event="longer_ruling_full_baseline",newB=newb,ell=ell,S=S,L=chosen["length"],
        metric=ind["metric"],curvature=ind["curvature"],held=ind["held"],dimension=raw.dimension)),flush=True)
    return definition,basis,clock,train,g11,w,mods,radius,meta,(sum(v["original"] for v in chosen["allG10"].values()),ind["metric"])


if __name__=="__main__":
    ap=joint.slope.args_base()
    for n in ("fixed-stadium","prior-guide","projected","redesigned-state"):ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--guide-scale",type=float,default=.0025);ap.add_argument("--directions",type=int,default=20)
    ap.add_argument("--divisions",type=int,default=9);ap.add_argument("--box",type=float,default=.25)
    ap.add_argument("--first",type=float,default=3.);ap.add_argument("--second",type=float,default=65.)
    ap.add_argument("--seam-width",type=float,default=.012);ap.add_argument("--extension",type=float,default=.036);ap.add_argument("--add-length",type=float,default=.014)
    ap.add_argument("--radius-blend",type=float,default=.18);ap.add_argument("--blends",type=float,nargs="+",default=[.06,.095,.14,.19,.25,.33,.42])
    args=ap.parse_args();args.resume=None
    if not 0<args.seam_width<=min(args.blends):raise ValueError("Short physical cancellation collar required")
    if args.source_only:prepare(args)
    else:
        joint.full.prepare=prepare;joint.main(args)
