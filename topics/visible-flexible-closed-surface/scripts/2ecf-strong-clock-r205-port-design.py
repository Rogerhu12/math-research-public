#!/usr/bin/env python3
"""Fully evaluate changed bend amplitude/orientation of R205 on the new physical-length chart."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from numpy.polynomial import Polynomial

def load(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
c=load(Path(__file__).with_name("2ecf-strong-new-material-clock.py"),"changed_cut_clock")
lm=load(Path(__file__).with_name("2ecf-strong-new-material-solve.py"),"changed_cut_base")
NAMES=("P","V","A","Pu","Vu","Au","Puu","Vuu","Auu")
POLY=[Polynomial(p) for p in ((0,0,0,10,-15,6),(0,0,0,-4,7,-3),(0,0,0,.5,-1,.5))]
def port(warm,A,Z,u,r,beta):
    vals=warm.developed_tail_port(A,Z,u+beta,r)
    cb=np.cos(beta);sb=np.sin(beta)
    if beta==np.pi/2:cb,sb=0.,1.
    rot=np.array([[cb,sb,0.],[-sb,cb,0.],[0.,0.,1.]])
    return {k:vals[k]@rot.T for k in NAMES}

def changed(warm,cache,rawbase,oldA,newA,Z,b,S,frac,beta):
    x=cache.nodes;u=cache.u
    left=b+frac*(S-b);L=S-left
    mask=(x>left)&(x<S)
    xx=x[mask];t=(xx-left)/L
    q0=port(warm,oldA,Z,u,.8,0.)
    q1=port(warm,newA,Z,u,.8,beta)
    diff={k:q1[k]-q0[k] for k in NAMES}
    out=rawbase.copy()
    for row,(radial,angle) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
        nk=(("P","V","A"),("Pu","Vu","Au"),("Puu","Vuu","Auu"))[angle]
        add=sum((L**(j-radial)*POLY[j].deriv(radial)(t)[:,None,None]*diff[k][None] for j,k in enumerate(nk)),np.zeros((len(t),len(u),3)))
        out[mask,row]+=add
    tail=np.where(x>=S)[0]
    diff_old=0.
    for ix in tail:
        r=.8-(x[ix]-S)
        p0=port(warm,oldA,Z,u,r,0.)
        p1=port(warm,newA,Z,u,r,beta)
        ks=("P","V","Pu","A","Vu","Puu")
        orig=np.stack([p0[k] for k in ks])
        diff_old=max(diff_old,float(np.max(abs(rawbase[ix]-orig))))
        out[ix]=np.stack([p1[k] for k in ks])
    if diff_old>1e-8:raise ValueError(("Original actual R205 tail mismatch",diff_old))
    return out,diff_old

def setup(args):
    saved,d,coarse,basis,caches,mods,z,alpha,radius,parent=c.inputs(args)
    rec=json.loads(args.clock.read_text());meta=rec["definition"]
    if meta["parentPreparedSHA256"]!=c.sha(args.prepared) or meta["parentDesignStateSHA256"]!=c.sha(args.parent) or meta["chartBasis"]!=basis.definition:
        raise ValueError("Actual bound H65 new meridian material length required")
    clock=c.Clock(basis,[float.fromhex(q) for q in meta["gammaHex"]])
    legacy=json.loads(Path(saved["parentPrepared"]).read_text())["sourceMetadata"]
    oldA,Z=legacy["amplitude"],legacy["Z"]
    warm=load(args.scripts/"6a65-geometry-cauchy-unit-t-warm.py","changed187port")
    src=json.loads(args.observer.read_text())
    if src["sourceIdentity"]!=d["sourceIdentity"] or any(c.sha(p)!=src["SHA256"][k] for k,p in src["files"].items()):raise ValueError("Actual G11 changed")
    caches["independent"]=SimpleNamespace(nodes=np.array(src["physicalNodes"]),u=np.array(src["angles"]),
        jets=np.load(src["files"]["jets"],mmap_mode="r"),radius=np.load(src["files"]["radius"],mmap_mode="r"))
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","changedportsums").direct_packet
    seed={}
    for n,cache in caches.items():
        R=radius.LogRadiusCache(coarse,cache,alpha)
        x,u=cache.nodes,cache.u
        independent=n=="independent"
        _,v,vx=clock.jets(x)
        weights={k:np.ones(len(x)) if independent else .5*np.asarray(saved["caches"][n]["weights"][k])*v
            for k in ("metric","curvature","geometry")}
        xyz=direct(basis,x,z,u) if independent else basis.packet(basis.matrices(x),z,len(u))
        seed[n]=dict(cache=cache,rawbase=cache.jets+xyz,v=v,vx=vx,radius=R.radius[:,0],weights=weights)
    return saved,d,basis,seed,mods,warm,clock,oldA,Z

def evaluate(name,input_data,warm,clock,b,S,oldA,newA,Z,frac,beta,stream,pointconfig,area):
    cache=input_data["cache"];u=cache.u;x=cache.nodes
    raw,err=changed(warm,cache,input_data["rawbase"],oldA,newA,Z,b,S,frac,beta)
    p=c.physical_jet(raw,input_data["v"],input_data["vx"])
    total=None;barrier=0.
    for lo in range(0,len(x),16):
        sl=slice(lo,lo+16);a=input_data["radius"][sl,None]
        W={k:v[sl,None]/len(u) for k,v in input_data["weights"].items()}
        point=stream.point.PointLinearized(p[sl].swapaxes(1,2),a,pointconfig,W)
        row=stream._block_statistics(point,x[sl],len(u))
        for key in ("worstMetric","worstCurvature"):row[key]["u"]+=float(u[0])
        total=stream._merge_statistics(total,row)
        barrier+=area.AreaPacket(p[sl],a,W["metric"],.5).stats["squaredNorm"]
    s=lm.labels(total,clock)
    return dict(original=s["squaredNorm"]+barrier,area=barrier,rows=len(x)*len(u)*14,
        metric=s["maxRelativeMetric"],curvature=s["maxCurvature"],held=s["minHeldDistance"],
        minImmersion=s["minImmersion"],guide=s["geometryMaximumViolations"],worstMetric=s["worstMetric"],
        worstCurvature=s["worstCurvature"],originalTailMaxSixJetDifference=err)

def main(args):
    tic=time.monotonic()
    saved,d,basis,seed,mods,warm,clock,oldA,Z=setup(args)
    stream=mods["stream"];cfg=stream.point.PointConfig(**d["pointConfig"])
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","changedcutarea")
    rows=[]
    params=[(1.,0.,0.)]+[(amp,angle,frac) for amp,angle in (
        (.8,0.),(.5,0.),(0.,0.),(1.,.0625),(1.,.125),(.7,.125),(.7,.25),(.7,.5),(1.,.5))
        for frac in (0.,.40)]
    for amp,angle,frac in params:
        A=amp*oldA;beta=angle*np.pi
        ev={k:evaluate(k,seed[k],warm,clock,basis.c,basis.end,oldA,A,Z,frac,beta,stream,cfg,area)
            for k in ("training","observer")}
        total=sum(q["original"] for q in ev.values())
        rows.append(dict(Afraction=amp,betaPi=angle,startFraction=frac,cost=total,G10=ev))
        print(json.dumps(dict(amp=amp,betaPi=angle,startFraction=frac,cost=total,
            metric=max(q["metric"] for q in ev.values()),curvature=max(q["curvature"] for q in ev.values()))),flush=True)
    if abs(rows[0]["cost"]-json.loads(args.clock.read_text())["fittedNewMaterialObjective"])>2e-9:
        raise ArithmeticError("Actual old-port baseline for this new g differs")
    ix=min(range(1,len(rows)),key=lambda i:rows[i]["cost"])
    p=rows[ix]
    ind=evaluate("independent",seed["independent"],warm,clock,basis.c,basis.end,oldA,p["Afraction"]*oldA,Z,
        p["startFraction"],p["betaPi"]*np.pi,stream,cfg,area)
    oldind=evaluate("independent",seed["independent"],warm,clock,basis.c,basis.end,oldA,oldA,Z,0.,0.,stream,cfg,area)
    result=dict(schema="new-total-S-complete-R205-conjugated-bend-cut-selection-v1",entrySHA256=c.sha(__file__),
        clock=c.sha(args.clock),prepared=c.sha(args.prepared),parent=c.sha(args.parent),observer=c.sha(args.observer),
        portProvider=c.sha(args.scripts/"6a65-geometry-cauchy-unit-t-warm.py"),frozenPhysicalMetric=json.loads(args.clock.read_text())["definitionSHA256"],
        oldA=oldA,Z=Z,allOriginalRows=4291840,allCompleteTwoJets=True,oldAndNewPlanarCollarIdentical=True,
        definition="rot(-beta)*R205_Anew(r,u+beta); exact complete endpoint-jet Hermite lifting on left..cut; entire new tail to flat cuff",
        rows=rows,selectedNontrivialIndex=ix,independentUsedForSelection=False,selectedG11=ind,originalG11=oldind,
        selectionImprovesBaseline=bool(p["cost"]<rows[0]["cost"]),newPositionSolverAccepts=0,seconds=time.monotonic()-tic)
    print(json.dumps(dict(SHA256=c.save(args.output,result),selected=ix,G11=ind["metric"],curvature=ind["curvature"],held=ind["held"])),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser();c.common_args(ap)
    for k in ("clock","observer","output"):ap.add_argument("--"+k,type=Path,required=True)
    main(ap.parse_args())
