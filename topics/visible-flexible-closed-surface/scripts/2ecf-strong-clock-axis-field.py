#!/usr/bin/env python3
"""Actual whole G10 and independent G11 H65 warm fields from constrained planar axis trajectories."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[k]="1"
import argparse
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.interpolate import BSpline,CubicHermiteSpline

def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
cut=load(Path(__file__).with_name("2ecf-strong-clock-r205-port-design.py"),"axial_field_ports")
c=cut.c
lm=cut.lm

def trajectory(record,name,s):
    a=record["axes"][name]
    if not a["success"]:raise ValueError("A real actual axial solution required")
    T=np.array(record["knots"]);L=record["length"]
    co=np.array([float.fromhex(v) for v in a["angleCoefficientsHex"]])
    theta=CubicHermiteSpline([0,1],a["coreAngles"],L*np.array(a["coreSignedCurvatures"]))
    corr=BSpline(T,np.r_[0.,0.,co,0.,0.],3)
    def ang(t):return theta(t)+corr(t)
    def kap(t):return (theta(t,nu=1)+corr(t,nu=1))/L
    t=(s-record["startS"])/L
    if min(t)<-1e-12 or max(t)>1+1e-12:raise ValueError("Axis query outside physical interval")
    t=np.clip(t,0,1)
    g,w=np.polynomial.legendre.leggauss(24)
    def integ(a,b):
        tt=.5*(b-a)[:,None]*g+.5*(a+b)[:,None]
        v=ang(tt)
        return .5*(b-a)[:,None]*np.column_stack((np.cos(v)@w,np.sin(v)@w))
    knots=np.unique(T)
    cum=np.vstack((np.zeros((1,2)),np.cumsum(integ(knots[:-1],knots[1:]),axis=0)))
    i=np.minimum(np.searchsorted(knots,t,side="right")-1,len(knots)-2)
    pos=np.asarray(a["portPositions"][0])+L*(cum[i]+integ(knots[i],t))
    th=ang(t);vel=np.column_stack((np.cos(th),np.sin(th)))
    acc=kap(t)[:,None]*np.column_stack((-np.sin(th),np.cos(th)))
    return np.stack((pos,vel,acc),axis=1)

def powercoef(n,sine):
    d={}
    for j in range(n+1):
        k=n-2*j
        if k<0:continue
        z=math.comb(n,j)*((-1)**j if sine else 1)/((2j if sine else 2)**n)
        if k==0:d[(0,"cos")]=z.real
        else:
            d[(k,"cos")]=2*z.real
            d[(k,"sin")]=-2*z.imag
    return d

def directions(basis,corr,m):
    dz=np.zeros((basis.nb,basis.na))
    for i,(axis,k,kind) in enumerate(basis.channels):
        for j in range(2):
            if axis==j:dz[:,i]+=corr[j][:,0]*powercoef(2*m+1,j==1).get((k,kind),0.)
            elif axis==2:dz[:,i]+=corr[j][:,1]*powercoef(2*m,j==1).get((k,kind),0.)
    return dz

def main(args):
    tic=time.monotonic()
    saved,d,basis,seed,mods,warm,clock,oldA,Z=cut.setup(args)
    stream=mods["stream"];cfg=stream.point.PointConfig(**d["pointConfig"])
    ar=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","axialarea")
    b,S=basis.c,basis.end
    groups={}
    for n,dat in seed.items():
        cache=dat["cache"];x=cache.nodes;u=cache.u
        groups[n]=dict(x=x,u=u,base=c.physical_jet(dat["rawbase"],dat["v"],dat["vx"]),
            radius=dat["radius"],weights=dat["weights"])
    inp=[json.loads(p.read_text()) for p in (args.long_axis,args.short_axis)]
    if any(r["clock"]!=c.sha(args.clock) or r["parent"]!=c.sha(args.parent) or r["prepared"]!=c.sha(args.prepared) for r in inp):
        raise ValueError("Axis curves require exact source, endpoints and new physical length")
    xf=groups["training"]["x"];m=(xf>=b)&(xf<=S);x=xf[m]
    s=clock.jets(x)[0];physbasis=c.physical_basis(basis,clock,c.sha(args.clock))
    M=[a.toarray() for a in physbasis.matrices(x)]
    w=caches_w=np.asarray(saved["caches"]["training"]["weights"]["metric"])[m]*clock.jets(x)[1]
    w=np.sqrt(w)
    # Positional, tangential and second-jet imperfections are all charged in the projection.
    pw=np.array((1.,.05,.001))
    matrix=np.vstack([m*w[:,None]*q for m,q in zip(M,pw)])
    corr=[];quality={}
    for i,n in enumerate(("long","short")):
        target=trajectory(inp[i],n,s)
        orig=groups["training"]["base"][m][:,[0,1,3],i*len(groups["training"]["u"])//4][:,:,[i,2]]
        diff=target-orig
        rhs=np.vstack([diff[:,j]*w[:,None]*pw[j] for j in range(3)])
        co=np.linalg.lstsq(matrix,rhs,rcond=None)[0]
        err=np.stack([p@co for p in M],axis=1)-diff
        quality[n]=dict(maxProjectionTwoVectorErrors=np.max(np.linalg.norm(err,axis=2),axis=0).tolist(),
            actualTargetTerminalPositionError=(target[-1,0]-orig[-1,0]).tolist(),
            trueFractionalLength=inp[i]["length"],splineRank=int(np.linalg.matrix_rank(matrix)),
            coefficientHex=[[float(q).hex() for q in row] for row in co])
        corr.append(co)
    independent_direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","axis_direct").direct_packet
    def packet(n,dz):
        dat=groups[n];x=dat["x"];u=dat["u"]
        return independent_direct(physbasis,x,dz,u) if n=="independent" else physbasis.packet(physbasis.matrices(x),dz,len(u))
    def evaluate(n,delta,scale):
        dat=groups[n];x=dat["x"];u=dat["u"]
        total=None;ac=0
        for j in range(0,len(x),16):
            sl=slice(j,j+16);p=dat["base"][sl]+scale*delta[sl]
            a=dat["radius"][sl,None]
            W={k:v[sl,None]/len(u) for k,v in dat["weights"].items()}
            pt=stream.point.PointLinearized(p.swapaxes(1,2),a,cfg,W)
            one=stream._block_statistics(pt,x[sl],len(u))
            for k in ("worstMetric","worstCurvature"):one[k]["u"]+=float(u[0])
            total=stream._merge_statistics(total,one)
            ac+=ar.AreaPacket(p,a,W["metric"],.5).stats["squaredNorm"]
        res=lm.labels(total,clock)
        return dict(original=res["squaredNorm"]+ac,metric=res["maxRelativeMetric"],curvature=res["maxCurvature"],
            held=res["minHeldDistance"],minImmersion=res["minImmersion"],guide=res["geometryMaximumViolations"],
            worstMetric=res["worstMetric"],worstCurvature=res["worstCurvature"],q2=ac,rows=14*len(x)*len(u))
    rows=[]
    for degree in (1,3,6,10):
        dz=directions(basis,corr,degree)
        unit={n:packet(n,dz) for n in ("training","observer")}
        for scale in ([0.,.2,.5,1.] if degree==1 else [.2,.5,1.]):
            grp={n:evaluate(n,value,scale) for n,value in unit.items()}
            cost=sum(v["original"] for v in grp.values())
            rows.append(dict(degree=degree,scale=scale,cost=cost,groups=grp))
            print(json.dumps(dict(degree=degree,scale=scale,cost=cost,metric=max(v["metric"] for v in grp.values()),
                curvature=max(v["curvature"] for v in grp.values()))),flush=True)
        del unit
    best=min(range(1,len(rows)),key=lambda i:rows[i]["cost"])
    chosen=rows[best];dz=directions(basis,corr,chosen["degree"])
    ind=evaluate("independent",packet("independent",dz),chosen["scale"])
    out=dict(schema="new-S-physical-planar-axis-lift-into-actual-full-XYZ-v1",entry=c.sha(__file__),
        cutSource=c.sha(cut.__file__),longAxis=c.sha(args.long_axis),shortAxis=c.sha(args.short_axis),clock=c.sha(args.clock),
        prepared=c.sha(args.prepared),parent=c.sha(args.parent),observer=c.sha(args.observer),portAmplitude=oldA,portOrientation=0,
        totalPhysicalRows=4291840,projectionWeights=pw.tolist(),projection=quality,
        angularFormula="dr_long*cos(u)^(2m+1) ex + dr_short*sin(u)^(2m+1) ey + [dz_long*cos(u)^(2m)+dz_short*sin(u)^(2m)] ez",
        initialRows=rows,chosenNonzeroTrainingIndex=best,beatingZero=bool(chosen["cost"]<rows[0]["cost"]),actualIndependent=ind,
        selectedAddedCoefficientsSHA256=__import__("hashlib").sha256(np.ascontiguousarray(chosen["scale"]*dz).tobytes()).hexdigest(),
        ownXYZOptimizerAccepts=0,continuousGeometryCertified=False,seconds=time.monotonic()-tic)
    h=c.save(args.output,out)
    print(json.dumps(dict(SHA256=h,best=best,initial=rows[0]["cost"],final=chosen["cost"],ind=ind)),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser();c.common_args(ap)
    for k in ("clock","observer","long-axis","short-axis","output"):ap.add_argument("--"+k,type=Path,required=True)
    main(ap.parse_args())
