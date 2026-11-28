#!/usr/bin/env python3
"""Directed, complete normal-angle and radius bounds for a new normalized stadium Gamma95 coast."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def correlated_ratio(series,port,vals,arc,f0,v):
    """Taylor coefficients in one common native angle, keeping mixed/normal cancellation to fourth order."""
    S=series
    gamma=port.series(vals,order=8)
    gp=S.vderivative(gamma);speed=S.sqrt(S.dot(gp,gp));inv=S.inv(speed)
    T=S.vscale(inv,gp);Tp=S.vderivative(T)
    Tu=S.vscale(S.scale(arc,inv),Tp);K=S.sqrt(S.dot(Tu,Tu));nf=S.vscale(S.inv(K),Tu)
    vK=S.scale(v,S.inv(K))
    rad=S.sub(S.constant(1,len(vK)),S.mul(vK,vK))
    direction=S.vadd(S.vneg(S.vscale(vK,nf)),S.vscale(S.sqrt(rad),S.cross(T,nf)))
    N=S.cross(direction,T)
    numerator=S.dot(Tp,N)
    if numerator[0].lo<=0:raise ArithmeticError("Unresolved positive normal curvature")
    k=S.mul(S.dot(S.vderivative(direction),N),S.inv(numerator))
    ku=S.mul(S.scale(arc,inv),S.derivative(k))
    n=S.scale(arc/f0,S.mul(numerator,inv))
    return k,ku,n,K


def solve(args):
    start=time.monotonic()
    proof=load(args.scripts/"6a65-m12-r137-continuous-domain.py","stadium_coast_integer")
    fourier=load(args.scripts/"6a65-geometry-final-ramp-port-certificate.py","stadium_coast_series")
    source=json.loads(args.input.read_text())
    if source["coast"]!=sha(args.coast) or source["schema"]!="actual-fixed-perimeter-smooth-stadium-support-H65-ramp-and-renormalized-Gamma95-v1":
        raise ValueError("New correctly generated support-normal Gamma95 required")
    with np.load(args.coast) as z:
        co,si=fourier.real_curve(z["curve_modes"],z["curve_coefficients"])
        v=proof.I(Q.from_float(float(z["v"])))
        f0=proof.I(Q.from_float(float(z["exact_target_radius"])))
        L=proof.I(Q.from_float(float(z["length"])))
    I=proof.I;pi=proof.pi_interval()
    curve=fourier.Fourier(co,si,proof,max_order=10)
    base=[I(x) for x in co[0]]
    cells=args.cells
    if cells<256:raise ValueError("Full circle needs at least 256 base cells")
    cached={}
    def phase(index,count):
        k=index%(2*count);key=(k,count)
        if key not in cached:
            cached[key]=proof.sincos(pi*Q(k if k<=count else k-2*count,count))
        return cached[key]
    buf=[];total=I(0);diam=pi/cells
    for j in range(cells):
        point=curve.point(j,cells,phase,order=5)
        val=curve.box(point,diam,order=4)
        p,q,r=val[1:4]
        speed=proof.norm2(p).sqrt()
        if speed.lo<=0:raise ArithmeticError("Unresolved regular raw curve")
        speedpp=(proof.norm2(q)+proof.dot(p,r))/speed-proof.dot(p,q).square()/speed**3
        midpoint=proof.norm2(point[1]).sqrt()
        total+=midpoint+I(-1,1)*diam.square()*I.raw(0,speedpp.absupper())/6
        buf.append(val)
    arc=total/cells
    scale=f0/arc
    angles=[L]+[I(Q(x)) for x in args.extend]
    stats=[{} for _ in angles]
    rows=hashlib.sha256()
    series=fourier.Series(proof)
    def bounded(center,domain,delta):
        if len(center)<5 or len(domain)<5:raise ArithmeticError("Missing fourth-order remainder")
        err=I(0)
        for d in (1,2,3):
            err+=I.raw(0,center[d].absupper())*delta**d
        err+=I.raw(0,domain[4].absupper())*delta**4
        return center[0]+I.raw(-err.hi,err.hi)
    def add(idx,N):
        h=pi/N
        point=curve.point(idx,N,phase,order=9)
        val=curve.box(point,h,order=8)
        try:
            exact=correlated_ratio(series,curve,point,arc,f0,v)
            remainder=correlated_ratio(series,curve,val,arc,f0,v)
            R,Ru,n,K=[bounded(a,b,h) for a,b in zip(exact,remainder)]
            gamma,p,q=val[:3];E=proof.norm2(p);T=proof.scale(1/E.sqrt(),p)
            cross=proof.cross(p,q);H=proof.norm2(cross).sqrt()
            NF=proof.scale(E.sqrt()/H,proof.sub(q,proof.scale(proof.dot(p,q)/E,p)))
            BF=proof.scale(1/H,cross)
            director=proof.add(proof.scale(-v/K,NF),proof.scale((1-(v/K).square()).sqrt(),BF))
            startpoint=proof.add(base,proof.scale(scale,proof.sub(gamma,base)))
            r0=f0/v
            direction=proof.sub(director,proof.scale(R,T))
            each=[]
            for ell in angles:
                z=ell*(2*r0+ell);w=z/(r0+(r0.square()+(1+R.square())*z).sqrt())
                whole=I.raw(0,w.hi);D=f0+whole*(v*(1+R.square())-Ru)
                if D.lo<=0:raise ArithmeticError("Possible singular ruling")
                Ut=D/(f0+v*whole*(1+R.square()));curvature=f0*n*(1+R.square())/D
                if curvature.hi>int(args.curvature_target*proof.SCALE) and N<cells*16:
                    raise ArithmeticError("Requested enclosure refinement")
                end=proof.add(startpoint,proof.scale(w,direction))
                X=proof.add(startpoint,proof.scale(whole,direction))
                each.append(dict(D=D,materialDerivative=Ut,curvature=curvature,angleBending=K,
                    entryNormalCurvature=n,rulingRatio=R,rulingRatioU=Ru,terminalZ=end[2],
                    z=X[2],y=X[1],normSquared=proof.norm2(X)))
        except ArithmeticError:
            if N>=cells*64:raise
            add(2*idx,2*N);add(2*idx+1,2*N)
            return
        for k,obs in enumerate(each):
            for name,a in obs.items():
                old=stats[k].get(name)
                stats[k][name]=(a.lo,a.hi) if old is None else (min(old[0],a.lo),max(old[1],a.hi))
            rows.update(repr((idx,N,k,[(name,a.lo,a.hi) for name,a in obs.items()])).encode()+b"\n")
    for j in range(cells):add(j,cells)
    def pair(lo,hi):
        return [str(Q(lo,proof.SCALE)),str(Q(hi,proof.SCALE))]
    out=dict(schema="actual-stadium-Gamma95-common-angle-quartic-directed-coast-v1",input=sha(args.input),
        entry=sha(__file__),integer=sha(proof.__file__),fourier=sha(fourier.__file__),actualGamma=sha(args.coast),
        fullCircleCells=cells,f0=pair(f0.lo,f0.hi),normalizedMeanSpeed=pair(arc.lo,arc.hi),
        normalizationScale=pair(scale.lo,scale.hi),intervals=[dict(length=pair(l.lo,l.hi),
            bounds={name:pair(*a) for name,a in rec.items()}) for l,rec in zip(angles,stats)],
        rowsSHA=rows.hexdigest(),seconds=time.monotonic()-start)
    with args.output.open("x") as f:json.dump(out,f,indent=2);f.write("\n")
    for l,rec in zip(angles,stats):
        print(json.dumps(dict(length=float(l.upper()),bounds={n:[float(Q(x,proof.SCALE)) for x in a] for n,a in rec.items()})),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for n in ("input","coast","scripts","output"):ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--cells",type=int,default=2048);ap.add_argument("--extend",nargs="*",default=[]);ap.add_argument("--curvature-target",type=float,default=20.)
    solve(ap.parse_args())
