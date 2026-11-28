#!/usr/bin/env python3
"""Certified full two-sided stadium prefix reach, including every truncation within a coast window."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(sp)
    sys.modules[name]=obj;sp.loader.exec_module(obj);return obj


def sin_lower(t):
    return t-t**3/6+t**5/120-t**7/5040


def run(args):
    here=Path(__file__).parent
    cert=load(args.scripts/"6a65-m12-r137-continuous-domain.py","stadium_whole_directed")
    I=cert.I;pi=cert.pi_interval().lower()
    read=lambda p:json.loads(p.read_text())
    src=read(args.source);g0=read(args.first);g1=read(args.middle);gt=read(args.terminal);tight=read(args.tight);co=read(args.ruling)
    rs,cs=sha(args.ramp),sha(args.coast)
    native=sha(here/"2ecf-strong-stadium-native-ramp-gram.py")
    if not(all(r["entry"]==native and r["ramp"]==rs and r["coast"]==cs for r in (g0,g1,gt))
        and src["ramp"]==rs and src["coast"]==cs and co["actualGamma"]==cs and co["input"]==sha(args.source)
        and gt["terminalTrace"]==sha(args.tight) and tight["ramp"]==rs and tight["coast"]==cs
        and co["entry"]==sha(here/"2ecf-strong-stadium-correlated-ruling-interval.py")
        and tight["entry"]==sha(here/"2ecf-strong-stadium-tight-terminal-composition.py")):
        raise ValueError("All literal source, accurate terminal, and real coast receipts required")
    if g0["terminalTrace"] or g1["terminalTrace"] or len(g0["rows"])!=1 or int(g0["rows"][0]["index"])!=0 or len(gt["rows"])!=1:
        raise ValueError("Incorrect split of actual native ramp receipts")
    rows=g0["rows"]+[r for r in g1["rows"] if int(r["index"])<63]+gt["rows"]
    with np.load(args.ramp) as m:
        c,r,v=map(lambda k:Q(float(m[k])),("centralLength","ramp","v"))
        sx=[Q(float(x)) for x in m["sx"]]
    if len(rows)!=64 or len(sx)!=65 or any(int(x["index"])!=j or Q(x["left"])!=sx[j] or Q(x["right"])!=sx[j+1] for j,x in enumerate(rows)):
        raise ValueError("Entire 64-cell exact physical material cover required")
    if gt["rows"][0]["endpoint"]!="new exact physical Gamma95" or min(Q(x["area"]) for x in rows)<=0:raise ValueError("Physical terminal immersion")
    with np.load(args.coast) as m:
        f0,ell=map(lambda k:Q(float(m[k])),("exact_target_radius","length"))
    b=Q(float(float(c+r)+float(ell)));delta=c+r+ell-b;ell0=ell-delta
    if delta<0 or delta>=ell:raise ValueError("Incorrect literal coast correction")
    slopeDev=Q(15,8)*delta/ell0
    er=max([Q(x["metric"]) for x in rows[:-1]]+[Q(tight["metric"])])
    e=max(er,slopeDev*(2+slopeDev))
    A,B,rr=map(Q,(src["exact"]["A"],src["exact"]["B"],src["exact"]["rhoMin"]))
    if not (0<e<Q(".000001") and r==sx[-1] and sx[0]==0 and rr==Q(1,4)):raise ValueError("Unresolved matched material target")
    Kraw=max([1/rr]+[Q(x["curvature"]) for x in rows])
    sums=[]
    for L,box in zip((ell,Q(3,50)),co["intervals"][:2]):
        L0,L1=map(Q,box["length"])
        if not L0<=L<=L1:raise ValueError("Actual outward-rounded complete coast interval")
        if L<ell:raise ValueError("Uniform family must include true first coast")
        Rbox=box["bounds"];K=max(Kraw,Q(Rbox["curvature"][1]));zend=Q(Rbox["terminalZ"][0])
        # For a shorter terminal sigma T one has z(T)>=z(L)-(L-T), since
        # each true material meridian has speed one. H(T)-z(T)+c stays bounded by the same d.
        H=r*(1+er/2)+L;dz=H-zend+c
        lat=I(2*H*dz).sqrt().upper()
        vertical=dz+er*r+delta;drift=I(lat**2+vertical**2).sqrt().upper()
        wrap=max(1+v*r/2+abs(f0-(1+v*r/2)), f0+v*L, Q(1))
        zmax=c+H
        fullball=I((A+lat)**2+zmax**2).sqrt().upper()
        achieved=[]
        for n in range(50,131):
            R=Q(n,1000)
            if R*K>1:continue
            d=2*R+2*lat;ratio=d/(2*rr)
            if ratio>=sin_lower(Q(1570,1000)):continue
            lo,hi=0,1570
            while hi-lo>1:
                mid=(lo+hi)//2
                if sin_lower(Q(mid,1000))>ratio:hi=mid
                else:lo=mid
            t=Q(hi,1000)
            if not (t<pi/2 and sin_lower(t)>ratio):raise ArithmeticError("Nonrigorous arc-chord inversion")
            C=t/sin_lower(t);length=(1+e/2)*wrap*C*(2*R+2*drift)
            if length*K<pi:
                achieved.append(dict(reach=str(R),arcChord=str(C),intrinsicUpper=str(length)))
        sums.append(dict(Tmin=str(ell),Tmax=str(L),K=str(K),metric=str(e),angularRadiusUpper=str(wrap), 
            upperMeridianLength=str(H),verticalDeficit=str(dz),horizontalDrift=str(lat),spatialDrift=str(drift),
            maximumHeight=str(zmax),maximumBall=str(fullball),maximumAbsY=str(B+lat),heldLower=str(A-B-lat),
            guide097=next((z for z in achieved if Q(z["reach"])==Q(".097")),None),best=achieved[-1] if achieved else None))
    result=dict(schema="real-p32-H65-whole-two-sided-prefix-and-all-truncated-coasts-continuous-v1",entry=sha(__file__),
        ramp=rs,coast=cs,inlet=sha(args.source),trueRuling=sha(args.ruling),
        partialReceipts=[sha(a) for a in (args.first,args.middle,args.terminal,args.tight)],all64NativeRadialCells=True,
        actualCorrectedFinalUsed=True,nativeLeaves=sum(int(x["leaves"]) for x in rows),minimumNativeArea=str(min(Q(x["area"]) for x in rows)),
        rampBound=str(er),coastDerivativeError=str(slopeDev),dyadicSewCorrection=str(delta),families=sums)
    if len(sums)!=2 or any(x["guide097"] is None for x in sums):raise ArithmeticError("Requested whole-prefix reach unresolved")
    with args.output.open("x") as f:json.dump(result,f,indent=2);f.write("\n")
    print(json.dumps(dict(metric=float(er),K=float(Kraw),results=[{k:(float(Q(x[k])) if isinstance(x[k],str) else
    {key:float(Q(value)) for key,value in x[k].items()}) for k in ("Tmax","best","guide097","maximumBall","maximumAbsY","heldLower")} for x in sums])),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for key in ("scripts","source","ramp","coast","first","middle","terminal","tight","ruling","output"):
        ap.add_argument("--"+key,type=Path,required=True)
    run(ap.parse_args())
