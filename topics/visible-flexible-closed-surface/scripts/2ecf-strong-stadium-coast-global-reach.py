#!/usr/bin/env python3
"""All-pair reach of the actual new affine coasts, including the concave inner boundary."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sin_lower(t):return t-t**3/6+t**5/120-t**7/5040


def run(args):
    tick=time.monotonic();r=json.loads(args.certificate.read_text())
    if r["entry"]!=sha(Path(__file__).with_name("2ecf-strong-stadium-correlated-ruling-interval.py")) or r["actualGamma"]!=sha(args.coast):
        raise ValueError("Actual correlated certificate and complete source required")
    proof=load(args.scripts/"6a65-m12-r137-continuous-domain.py","stadium_global_int")
    port=load(args.scripts/"6a65-geometry-final-ramp-port-certificate.py","stadium_global_fourier")
    if sha(proof.__file__)!=r["integer"] or sha(port.__file__)!=r["fourier"]:raise ValueError("Changed directed arithmetic")
    I=proof.I;pi=proof.pi_interval();arc=I(*map(Q,r["normalizedMeanSpeed"]));f0=I(*map(Q,r["f0"]))
    with np.load(args.coast) as ff:
        co,si=port.real_curve(ff["curve_modes"],ff["curve_coefficients"])
        v=Q.from_float(float(ff["v"]))
    a=f0/arc
    curve=port.Fourier(co,si,proof,max_order=4)
    cache={}
    def phase(i,N):
        k=i%(2*N)
        if k not in cache:cache[k]=proof.sincos(pi*Q(k if k<=N else k-2*N,N))
        return cache[k]
    q={}
    n=args.cells;h=pi/n
    for j in range(n):
        pt=curve.point(j,n,phase,order=3)
        P,p,z=curve.box(pt,h,order=2)
        sn,cs=phase(2*j+1,n);delta=I.raw(-h.hi,h.hi)
        sn+=delta;cs+=delta
        perp=p[1]*cs-p[0]*sn
        norm2=p[0].square()+p[1].square()
        det2=p[0]*z[1]-p[1]*z[0]
        k=det2/(norm2*norm2.sqrt()*a)
        stretch=(proof.norm2(p)/norm2).sqrt()
        rz=I(co[0][2])+a*(P[2]-I(co[0][2]))
        for name,y in dict(orientedAnchor=perp,planarCurvature=k,spaceOverPlane=stretch,initialZ=rz).items():
            old=q.get(name)
            q[name]=(y.lo,y.hi) if old is None else (min(old[0],y.lo),max(old[1],y.hi))
    bounds={name:[Q(x,proof.SCALE) for x in vv] for name,vv in q.items()}
    kp=bounds["planarCurvature"][1]
    if min(bounds["orientedAnchor"][0],bounds["planarCurvature"][0])<=0:raise ArithmeticError("Strictly convex planar projection not resolved")
    rmin=1/kp;ratio=bounds["spaceOverPlane"][1];out=[]
    grid=[Q(i,1000) for i in range(50,251)]
    for interval in r["intervals"]:
        L=Q(interval["length"][1]);a0=interval["bounds"];W=1+v*L/f0.lower()
        K=max(Q(a0["curvature"][1]),Q(a0["angleBending"][1])/f0.lower())
        deficit=L-max(Q(0),Q(a0["terminalZ"][0])-bounds["initialZ"][1])
        lateral=min(L,(I(2*L*deficit)).sqrt().upper())
        achieved=[]
        for R in grid:
            if R*K>1:continue
            d=2*R+2*lateral
            if d>=2*rmin:continue
            target=d/(2*rmin)
            if sin_lower(Q(1570,1000))<=target:continue
            lo,hi=0,1570
            while hi-lo>1:
                m=(lo+hi)//2
                if sin_lower(Q(m,1000))>target:hi=m
                else:lo=m
            t=Q(hi,1000)
            if not(t<pi.lower()/2 and sin_lower(t)>target):raise ArithmeticError("Directed chord inverse failed")
            length2=L**2+(W*ratio*(2*rmin*t))**2
            if K*K*length2>=pi.lower()**2:continue
            achieved.append(dict(R=str(R),chordMax=str(d),arcsinUpper=str(t),
                actualPathLengthUpper=str(I(length2).sqrt().upper()),K=str(K),lateral=str(lateral)))
        out.append(dict(materialLength=str(L),maximumProven=achieved[-1] if achieved else None,
            guide097=next((v for v in achieved if Q(v["R"])==Q(".097")),None),achievedCount=len(achieved)))
    result=dict(schema="actual-nonelliptic-coast-concave-inner-circle-path-all-pairs-reach-v1",
        source=sha(args.coast),certificate=sha(args.certificate),entry=sha(__file__),nativeCells=n,
        projected={k:[str(a) for a in vv] for k,vv in bounds.items()},results=out,seconds=time.monotonic()-tick)
    with args.output.open("x") as f:json.dump(result,f,indent=2);f.write("\n")
    print(json.dumps(dict(projected={k:list(map(float,y)) for k,y in bounds.items()},
        results=[(a["materialLength"],None if not a["maximumProven"] else float(Q(a["maximumProven"]["R"]))) for a in out])),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for x in ("scripts","certificate","coast","output"):ap.add_argument("--"+x,type=Path,required=True)
    ap.add_argument("--cells",type=int,default=2048)
    run(ap.parse_args())
