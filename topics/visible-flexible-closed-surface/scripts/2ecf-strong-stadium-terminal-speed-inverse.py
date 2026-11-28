#!/usr/bin/env python3
"""A signed integral of the tiny exact Gamma95 squared-speed difference fixes its true arc inverse."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np


def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p);o=importlib.util.module_from_spec(spec);sys.modules[n]=o;spec.loader.exec_module(o);return o


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def absq(x):return max(abs(x.lower()),abs(x.upper()))


def run(args):
    now=time.monotonic();root=args.scripts
    native=load(Path(__file__).with_name("2ecf-strong-stadium-native-ramp-gram.py"),"true_stadium_ramp")
    gram=load(root/"6a65-geometry-ramp-native-gram-certificate.py","true_stadium_gram")
    cert=load(root/"6a65-m12-r137-continuous-domain.py","true_stadium_speed_integer")
    port=load(root/"6a65-geometry-final-ramp-port-certificate.py","true_stadium_speed_Fourier")
    source=json.loads(args.source.read_text())
    if source["coast"]!=sha(args.coast) or source["ramp"]!=sha(args.ramp):raise ValueError("Actual new support masters required")
    model=native.model_for(gram,source,args.ramp);I=cert.I;S=port.Series(cert)
    with np.load(args.coast) as zz:
        co,si=port.real_curve(zz["curve_modes"],zz["curve_coefficients"]);f0=Q(float(zz["exact_target_radius"]))
    D=len(co)-1;bits=max(gram.dyadic_bits(q/2) for row in co+si for q in row)
    C=[[[[0]*(2*D+1) for _ in range(2)] for _ in range(3)]]
    for d in range(3):
        C[0][d][0][D]=gram.scaled(co[0][d],bits)
        for k in range(1,D+1):
            a=gram.scaled(co[k][d]/2,bits);b=gram.scaled(-si[k][d]/2,bits)
            C[0][d][0][D+k]=C[0][d][0][D-k]=a
            C[0][d][1][D+k]=b;C[0][d][1][D-k]=-b
    U=gram.angular(C,D);peak=max(abs(a).bit_length() for row in U for part in row for a2 in part for a in a2)
    R=gram.packed_gram(U,U,2*peak+(12*3*(2*D+1)).bit_length()+5,True)[0]
    rc=[];rs=[];hc=[];hs=[]
    for k in range(2*D+1):
        factor=1 if k==0 else 2
        x=factor*(Q(R[0][2*D+k],1<<(2*bits))-f0*f0*model.rho2.get(k,0))
        y=-factor*Q(R[1][2*D+k],1<<(2*bits))
        rc.append([x,Q(0),Q(0)]);rs.append([y,Q(0),Q(0)])
    for k in range(2*model.p+1):
        hc.append([model.rho[k//2] if k%2==0 else Q(0),Q(0),Q(0)]);hs.append([Q(0)]*3)
    rp=port.Fourier(rc,rs,cert,max_order=4);cp=port.Fourier(hc,hs,cert,max_order=4)
    N=args.cells;pi=cert.pi_interval();h=pi/N;cache={}
    def phase(k,N):
        j=k%(2*N)
        if j not in cache:cache[j]=cert.sincos(pi*Q(j if j<=N else j-2*N,N))
        return cache[j]
    def field(rv,cv):
        rr=[r[0]/math.factorial(i) for i,r in enumerate(rv[:3])]
        h0=[r[0]/math.factorial(i) for i,r in enumerate(cv[:3])]
        h0[0]=I.raw(max(I(model.r).lo,h0[0].lo),min(I(model.rhomax).hi,h0[0].hi))
        a=S.scale(f0,h0)
        J=S.sqrt(S.add(S.mul(a,a),rr))
        e=S.mul(rr,S.inv(S.add(J,a)))
        return h0,J,e
    rows=[];average=I(0);qmin=None
    for j in range(N):
        rp0=rp.point(j,N,phase,order=3);cp0=cp.point(j,N,phase,order=3)
        rc0=rp.box(rp0,h,order=2);cc0=cp.box(cp0,h,order=2)
        _,_,e0=field(rp0,cp0);hv,J,e=field(rc0,cc0)
        # e[2] already includes the Taylor factorial, so averaging t^2 contributes h^2/3.
        err=I.raw(0,e[2].absupper())*h.square()/3
        avg=e0[0]+I.raw(-err.hi,err.hi)
        average+=avg
        rows.append((avg,hv,J,e))
        qmin=J[0].lower() if qmin is None else min(qmin,J[0].lower())
    shift=average/N;arc=I(f0)+shift
    trace=I(0);maxprim=Q(0);emax=Q(0);epmax=Q(0);Jpmax=Q(0);Jppmax=Q(0)
    hits=hashlib.sha256()
    for avg,hv,J,e in rows:
        g=e[0]-shift*hv[0];dg=e[1]-shift*hv[1]
        local=trace+I(0,2*h.upper())*g
        maxprim=max(maxprim,absq(local));emax=max(emax,absq(g));epmax=max(epmax,absq(dg))
        Jpmax=max(Jpmax,absq(J[1]));Jppmax=max(Jppmax,2*absq(J[2]))
        trace+=2*h*(avg-shift*hv[0])
        hits.update(repr((trace.lo,trace.hi,local.lo,local.hi)).encode())
    if not(trace.lo<=0<=trace.hi):raise ArithmeticError("Complete zero mean arc primitive does not contain zero")
    theta=maxprim/qmin
    first=(emax+Jpmax*theta)/qmin
    second=(epmax+Jppmax*theta+(2*first+first*first)*Jpmax)/qmin
    data=dict(schema="new-nonellipse-true-Gamma95-signed-cumulative-arc-inverse-v1",
        actualRamp=sha(args.ramp),actualCoast=sha(args.coast),entry=sha(__file__),native=sha(native.__file__),
        exactSquaredSpeedResidualDegree=2*D,scalarNorms=[str(sum(abs(rc[k][0])+abs(rs[k][0]) for k in range(2*D+1)))],
        f0=str(f0),arc=[str(arc.lower()),str(arc.upper())],meanSpeedShift=[str(shift.lower()),str(shift.upper())],
        qmin=str(qmin),primitiveUpper=str(maxprim),zeroMeanSpeedUpper=str(emax),q1=str(Jpmax),q2=str(Jppmax),
        thetaUpper=str(theta),firstMinusOne=str(first),secondUpper=str(second),cells=N,cellSHA256=hits.hexdigest(),
        seconds=time.monotonic()-now)
    with args.output.open("x") as fp:json.dump(data,fp,indent=2);fp.write("\n")
    print(json.dumps({k:float(Q(data[k])) for k in ("qmin","primitiveUpper","thetaUpper","firstMinusOne","secondUpper")}),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for n in ("scripts","source","ramp","coast","output"):ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--cells",type=int,default=2048)
    run(ap.parse_args())
