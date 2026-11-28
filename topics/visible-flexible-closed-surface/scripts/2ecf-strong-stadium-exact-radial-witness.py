#!/usr/bin/env python3
"""Pointwise exact rational radial defect at a true interior stadium H65 point."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(args):
    s=args.scripts/"6a65-geometry-ramp-native-gram-certificate.py"
    spec=importlib.util.spec_from_file_location("stadium_radial_lower",s);gram=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=gram;spec.loader.exec_module(gram)
    src=json.loads(args.source.read_text())
    if sha(args.ramp)!=src["ramp"]:raise ValueError("Actual new support ramp required")
    with np.load(args.ramp) as a:
        wave=a["wave"].astype(int)
        if not np.array_equal(wave,a["wave"]):raise ValueError("Native integer Fourier labels required")
        raw=a["coefficients"].copy();sx=a["sx"].copy()
    # Sorting candidates only: integer fourth roots of unity and the raw real Fourier convention.
    candidates=[]
    for corner in range(4):
        roots=np.array([1,1j,-1,-1j])[(wave*corner)%4]
        values=np.einsum("n,jnrt->jrt",roots,raw,optimize=True).real
        for j in range(1,63):
            L=sx[j+1]-sx[j];P=np.concatenate((values[j],values[j+1]))
            power=np.array([1/L,1,L,1/L,1,L])
            for h in range(1,32):
                t=h/32;w=np.array([sum(i*q*t**(i-1)/2 for i,q in enumerate(row) if i) for row in gram.H2])*power
                ds=w@P;candidates.append((abs(ds@ds-1),corner,j,h))
    _,corner,j,h=max(candidates);L=Q(float(sx[j+1]))-Q(float(sx[j]));t=Q(h,32)
    weights=[sum(Q(i*integer,2)*t**(i-1) for i,integer in enumerate(row) if i)*L**(k%3-1) for k,row in enumerate(gram.H2)]
    results=[]
    for alpha in range(4):
        sig=[(1,0),(0,-1),(-1,0),(0,1)]
        DS=[]
        for d in range(3):
            ss=Q(0)
            for p,w in enumerate(weights):
                val=Q(0);u=raw[j+p//3,:,p%3,d]
                for k,z in zip(wave,u):
                    x,y=sig[(int(k)*alpha)%4]
                    val+=x*Q(float(z.real))+y*Q(float(z.imag))
                ss+=w*val
            DS.append(ss)
        e=sum(x*x for x in DS)-1
        results.append(dict(quarter=alpha,derivative=list(map(str,DS)),radialDefect=str(e)))
    witness=abs(Q(results[corner]["radialDefect"]))
    spread=max(Q(q["radialDefect"]) for q in results)-min(Q(q["radialDefect"]) for q in results)
    if witness<=0 or spread<=0:raise ArithmeticError("Actual defect witness required")
    out=dict(schema="literal-stadium-H65-rational-radial-Rayleigh-and-same-ring-variation-v1",entry=sha(__file__),
        gram=sha(s),ramp=sha(args.ramp),source=sha(args.source),cell=j,t=str(t),nativeQuarter=corner,
        radialPoint=str(Q(float(sx[j]))+L*t),metricLower=str(witness),sameRingRadialSpread=str(spread),quarters=results)
    with args.output.open("x") as f:json.dump(out,f,indent=2);f.write("\n")
    print(json.dumps(dict(cell=j,t=str(t),quarter=corner,lower=float(witness),spread=float(spread))))


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for k in ("scripts","source","ramp","output"):ap.add_argument("--"+k,type=Path,required=True)
    run(ap.parse_args())
