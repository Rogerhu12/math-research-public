#!/usr/bin/env python3
"""New diagonal target and positive total length on an explicitly evaluated angular-clocked HF64M80 field."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse
import json
import time
from pathlib import Path
from types import SimpleNamespace
import importlib.util
import sys
import numpy as np
from scipy import sparse
from scipy.optimize import linprog

def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
d=load(Path(__file__).with_name("2ecf-strong-clock-diagonal-minimax.py"),"common_squared_clock")
c=d.c
def build(args):
    saved,definition,coarse,basis,caches,mods,z,alpha,radius,parent=c.inputs(args)
    src=json.loads(args.observer.read_text())
    if src["sourceIdentity"]!=definition["sourceIdentity"] or any(c.sha(p)!=src["SHA256"][k] for k,p in src["files"].items()):
        raise ValueError("Changed actual outside-HF G11 source")
    caches["independent"]=SimpleNamespace(nodes=np.asarray(src["physicalNodes"]),u=np.asarray(src["angles"]),
        jets=np.load(src["files"]["jets"],mmap_mode="r"),radius=np.load(src["files"]["radius"],mmap_mode="r"))
    h=load(args.hf_helpers/"2ecf-strong-hf-material-radial-clock.py","actual_HF_source")
    hc=json.loads(args.angular_clock.read_text())
    if (hc["sourceSHA256"]!=c.sha(h.__file__) or hc["fieldSHA256"]!=c.sha(args.field) or hc["preparedSHA256"]!=c.sha(args.prepared)
        or hc["independentSHA256"]!=c.sha(args.observer)):
        raise ValueError("True coherent angular-dependent HF clock and all original source groups required")
    with np.load(args.field) as data:
        if not np.array_equal(data["alpha"],alpha) or not np.array_equal(data["alphaKnots"],coarse.knots):
            raise ValueError("Entire 36-coefficient angular target differs")
    groups={}
    check={}
    for n,x in caches.items():
        radial=x.nodes;u=x.u
        radii=radius.LogRadiusCache(coarse,x,alpha)
        obj=h.Field(args,u);hc_basis=h.Clock(*obj.knots[[0,-1]])
        coeff=np.asarray(hc["coefficients"])
        if not np.array_equal(hc_basis.knots,np.asarray(hc["radialKnots"])):raise ValueError("Source radial clock knots differ")
        packet=x.jets.copy()
        live=np.flatnonzero((radial>=basis.c)&(radial<=basis.end))
        for j in range(0,len(live),8):
            ix=live[j:j+8]
            packet[ix]=h.compose(obj,hc_basis,radial[ix],u,coeff)
        U=packet[:,1];V=packet[:,2]/radii.radius[:,0,None,None]
        E=np.sum(U*U,axis=-1);F=np.sum(U*V,axis=-1);G=np.sum(V*V,axis=-1)
        err=np.max(abs((E+G-2)/2)+np.hypot((E-G)/2,F))
        expect=hc["allOwnFullGridObservations"][n]["metric"][0]
        if abs(err-expect)>1e-10:raise ArithmeticError(("Reconstructed true HF physical source mismatch",n,err,expect))
        check[n]=float(err)
        groups[n]=dict(cache=x,radius=radii,jets=packet,N=np.stack((E,F,G),axis=-1))
    return saved,definition,basis,mods,groups,check

def derivative_box(basis,first,second):
    T=basis.knots.copy()
    M=np.pad(np.eye(basis.nb),((3,3),(0,0)))
    constraints=[]
    for k,bound in enumerate((first,second)):
        if bound is None:break
        n=len(M)-1
        M=(5-k)*np.diff(M,axis=0)/(T[5-k+1:5-k+1+n]-T[1:1+n])[:,None]
        constraints.append((M.copy(),bound));T=T[1:-1]
    return constraints

def physical(args,groups,basis,ce,cg):
    clock=d.SquareClock(basis,ce)
    caches={}
    for n,src in groups.items():
        x=src["cache"];r=d.radius_jets(src["radius"],basis,cg)
        _,v,vx=clock.jets(x.nodes)
        a,ax,axx=r.T
        # Complete new target and source derivatives in actual material s.
        p=c.physical_jet(src["jets"],v,vx)
        rz=np.column_stack((a,ax/v,axx/v**2-ax*vx/v**3))
        caches[n]=SimpleNamespace(nodes=x.nodes,u=x.u,jets=p,radius=rz,h=v)
    return clock,caches

def sample(caches,mods,saved,definition,clock,args):
    stream=mods["stream"];cfg=stream.point.PointConfig(**definition["pointConfig"])
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","HF_clock_area")
    out={}
    for n,obj in caches.items():
        x=obj.nodes;u=obj.u;tot=None;ac=0.
        for i in range(0,len(x),12):
            s=slice(i,i+12);a=obj.radius[s,0,None];packet=obj.jets[s];h=obj.h[s,None]
            w={k:np.ones_like(h)/len(u) if n=="independent" else .5*np.asarray(saved["caches"][n]["weights"][k])[s,None]*h/len(u)
                for k in ("metric","curvature","geometry")}
            pt=stream.point.PointLinearized(packet.swapaxes(1,2),a,cfg,w)
            v=stream._block_statistics(pt,x[s],len(u))
            for label in ("worstMetric","worstCurvature"):v[label]["u"]+=u[0]
            tot=stream._merge_statistics(tot,v)
            ac+=area.AreaPacket(packet,a,w["metric"],.5).stats["squaredNorm"]
        r=d.lm.labels(tot,clock)
        out[n]=dict(rows=len(x)*len(u)*14,metric=r["maxRelativeMetric"],curvature=r["maxCurvature"],
            original=r["squaredNorm"]+ac,area=ac,held=r["minHeldDistance"],guide=r["geometryMaximumViolations"],
            maxTargetGauss=float(np.max(abs(obj.radius[:,2]/obj.radius[:,0]))),worstMetric=r["worstMetric"],worstCurvature=r["worstCurvature"])
    return out

def main(args):
    t=time.monotonic()
    saved,definition,basis,mods,groups,check=build(args)
    x=groups["training"]["cache"].nodes
    N=np.concatenate([groups[n]["N"] for n in ("training","observer")],axis=1)
    E,F,G=N.transpose(2,0,1)
    B=basis.matrices(x)[0];nb=basis.nb
    live=np.flatnonzero(np.any(B.toarray()!=0,axis=1))
    u=np.arange(args.directions)*np.pi/args.directions
    # For each tested tangent direction, take extrema over *all* material angles.
    # Only rows with candidate-dependent target are needed in the LP. All original
    # rows, including fixed portions, are evaluated for final metric and full cost.
    weights=[];mn=[];mx=[]
    for phi in u:
        aa=np.cos(phi)**2;bb=1-aa;cross=np.sin(2*phi)
        score=aa*E[live]+cross*F[live]+bb*G[live]
        weights.append(sparse.hstack((aa*B[live],bb*B[live]),format="csr"))
        mn.append(np.min(score,axis=1));mx.append(np.max(score,axis=1))
    L=sparse.vstack(weights,format="csr")
    mn=np.concatenate(mn);mx=np.concatenate(mx)
    parts=[];bounds=[]
    for index,(a,bound) in enumerate(((args.speed_first,None),(args.radius_first,args.radius_second))):
        for mat,k in derivative_box(basis,a,bound):
            zero=np.zeros_like(mat)
            box=np.column_stack((mat,zero) if index==0 else (zero,mat))
            parts.append(sparse.csr_matrix(np.vstack((box,-box))))
            bounds.append(np.full(2*len(mat),k))
    BM=sparse.vstack(parts,format="csr");bb=np.concatenate(bounds)
    integ=(basis.knots[6:]-basis.knots[:-6])[3:-3]/6
    target=2*args.delta+args.delta**2/(basis.end-basis.c)
    Aeq=np.r_[integ,np.zeros(nb)][None]
    def actual(pos):
        e=1+B@pos[:nb];g=1+B@pos[nb:]
        u=E/e[:,None]-1;w=G/g[:,None]-1;f=F/np.sqrt(e*g)[:,None]
        return float(np.max(np.abs((u+w)/2)+np.hypot((u-w)/2,f)))
    def solve(eps):
        A=sparse.vstack((-(1+eps)*L,(1-eps)*L,BM),format="csr")
        rhs=np.r_[1+eps-mx,mn-(1-eps),bb]
        # Secondary absolute-amplitude criterion selects a restrained feasible
        # target, so a wide feasible box does not generate gratuitous oscillations.
        n=2*nb;eye=sparse.eye(n,format="csr")
        full=sparse.vstack((sparse.hstack((A,sparse.csr_matrix((len(rhs),n)))),
            sparse.hstack((eye,-eye)),sparse.hstack((-eye,-eye))),format="csr")
        return linprog(np.r_[np.zeros(n),np.ones(n)],A_ub=full,b_ub=np.r_[rhs,np.zeros(2*n)],
            A_eq=np.column_stack((Aeq,np.zeros((1,n)))),b_eq=[target],
            bounds=[(-args.box,args.box)]*n+[(0,args.box)]*n,method="highs",
            options={"primal_feasibility_tolerance":1e-9,"dual_feasibility_tolerance":1e-9})
    lo=0.;hi=.35;best=None;hist=[]
    for it in range(args.bisections+1):
        eps=hi if it==0 else (lo+hi)/2
        res=solve(eps)
        if res.success:
            q=res.x[:2*nb].copy();peak=actual(q)
            hist.append(dict(eps=eps,netFeasible=True,allAngleEvaluation=peak))
            if best is None or peak<best[0]:best=(peak,q)
            hi=eps
        elif res.status==2:
            lo=eps;hist.append(dict(eps=eps,netFeasible=False))
            if it==0:raise ArithmeticError("No target in initial actual-first physical window")
        else:raise ArithmeticError(res.message)
        print(json.dumps(hist[-1]),flush=True)
    peak,q=best
    ce=q[:nb];cg=q[nb:]
    clk,cache=physical(args,groups,basis,ce,cg)
    baseline=sample(cache,mods,saved,definition,clk,args)
    if abs(max(baseline[n]["metric"] for n in ("training","observer"))-peak)>1e-10:raise ArithmeticError("Six-jet direct observation differs")
    definition2=dict(schema="new-S-smooth-squared-diagonal-common-target-for-explicit-HF-source-v1",
        entry=c.sha(__file__),basePositionFile=c.sha(args.field),baseAngleClock=c.sha(args.angular_clock),
        parentPrepared=c.sha(args.prepared),parentDesign=c.sha(args.parent),frozenOldRadius=parent_radius(args),
        CEradialHex=[float(a).hex() for a in ce],CGangularHex=[float(a).hex() for a in cg],basis=basis.definition,
        squaredSpeed="1+B*ce",relativeSquaredAngularRadius="1+B*cg",delta=clk.delta,cut=basis.end+clk.delta,
        allBoundedCoefficientBoxes=args.box,meridianFirstDerivativeLimit=args.speed_first,
        relativeSquaredRadiusFirstDerivativeLimit=args.radius_first,relativeSquaredRadiusSecondDerivativeLimit=args.radius_second,
        actualBaseHF=check,deltaTargetSecondMoment=args.delta,amplitudeDesign="Only common metric changed; physical field is re-clocked, no own position accepts")
    out=dict(definition=definition2,definitionSHA256=c.stable(definition2),parentObserver=c.sha(args.observer),
        trainingGroups=["training","observer"],netDirections=args.directions,history=hist,finiteNetFloatingBracket=[lo,hi],
        trueObservedG10Peak=peak,stats=baseline,ownFixedMetricAccepts=0,finiteOnly=True,seconds=time.monotonic()-t)
    h=c.save(args.output,out)
    print(json.dumps(dict(SHA256=h,delta=clk.delta,summary={k:[v["metric"],v["curvature"],v["held"],v["maxTargetGauss"]] for k,v in baseline.items()})),flush=True)

def parent_radius(args):return json.loads(args.parent.read_text())["provisionalMetricDefinitionSHA256"]
def args_hf(ap):
    c.common_args(ap)
    for n in ("field","angular-clock","hf-helpers","ramp","coast","observer"):ap.add_argument("--"+n,type=Path,required=True)
if __name__=="__main__":
    ap=argparse.ArgumentParser();args_hf(ap);ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--directions",type=int,default=20);ap.add_argument("--bisections",type=int,default=9)
    ap.add_argument("--delta",type=float,default=.006);ap.add_argument("--box",type=float,default=.20)
    ap.add_argument("--speed-first",type=float,default=3.);ap.add_argument("--radius-first",type=float,default=2.)
    ap.add_argument("--radius-second",type=float,default=45.)
    main(ap.parse_args())
