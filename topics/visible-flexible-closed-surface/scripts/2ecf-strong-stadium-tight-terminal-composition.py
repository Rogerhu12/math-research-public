#!/usr/bin/env python3
"""Combine an independently sharpened signed arc inverse with full physical H65 terminal traces."""
import argparse
from copy import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args):
    work=Path(__file__).parent
    native=load(work/"2ecf-strong-stadium-native-ramp-gram.py","stadium_tight_native")
    gram=load(args.scripts/"6a65-geometry-ramp-native-gram-certificate.py","stadium_tight_gram")
    term=load(args.scripts/"6a65-geometry-final-ramp-cell-certificate.py","stadium_tight_term")
    cert=load(args.scripts/"6a65-m12-r137-continuous-domain.py","stadium_tight_cert")
    inv=json.loads(args.inverse.read_text());res=json.loads(args.residual.read_text());src=json.loads(args.source.read_text())
    rsha,csha=sha(args.ramp),sha(args.coast)
    if not (rsha==inv["actualRamp"]==res["ramp"]==src["ramp"] and csha==inv["actualCoast"]==res["coast"]==src["coast"]):
        raise ValueError("Matched physical native model required")
    if inv["entry"]!=sha(work/"2ecf-strong-stadium-terminal-speed-inverse.py") or res["entry"]!=sha(work/"2ecf-strong-stadium-terminal-residual-trace.py"):
        raise ValueError("Changed source of input angular estimates")
    d0,d1,d2=[Q(inv[k]) for k in ("thetaUpper","firstMinusOne","secondUpper")]
    I=cert.I;trace=[]
    for key in ("P","V","A"):
        a=list(map(Q,res["sameAngle"][key]));b=list(map(Q,res["trueDerivatives"][key]))
        trace.append([I(x).upper() for x in (a[0]+b[1]*d0,a[1]+b[2]*d0+b[1]*d1,
            a[2]+b[3]*d0+b[2]*(2*d1+d1*d1)+b[1]*d2)])
    m=native.model_for(gram,src,args.ramp)
    last=copy(m);last.sx=m.sx[-2:];last.port=lambda i:m.port(63+i)
    C,bits,L,s0=last.cell(0)
    eb,fb,gb,_,_=native.formula(gram,C,bits,L,s0,m,args.cutoff)
    errors={(i,j):sum(L**(k-i)*term.hermite_norm(gram.H2[3+k],i)*trace[k][j] for k in range(3))
            for i in range(3) for j in range(3)}
    with np.load(args.coast) as z:f0=Q(float(z["exact_target_radius"]))
    corr=abs(f0-(1+m.v*m.ramp/2))
    fmax=1+m.v*m.ramp/2;fmin=1-corr
    # Compare derivatives in the material arc u, so d/du=(1/rho)d/dtheta.
    oldS=I(1+eb).sqrt().upper();oldU=I(fmax**2+gb/m.r**2).sqrt().upper()
    se,ue=errors[1,0],errors[0,1]/m.r
    E=eb+2*oldS*se+se**2
    F=(fb/m.r+oldS*ue+oldU*se+se*ue)/fmin
    G=(gb/m.r**2+2*oldU*ue+ue**2+corr*(2*fmax+corr))/fmin**2
    eig=(E+G+I((E-G)**2+4*F**2).sqrt().upper())/2
    out=dict(schema="actual-final-H65-terminal-composition-and-normalized-Gram-v1",entry=sha(__file__),ramp=rsha,coast=csha,
        inverse=sha(args.inverse),residual=sha(args.residual),native=sha(native.__file__),gram=sha(gram.__file__),
        radialHermite=sha(term.__file__),integer=sha(cert.__file__),cutoff=args.cutoff,
        materialOrdersInNativeCentralAngle=[[str(v) for v in row] for row in trace],
        finalCellNativeErrors={str(k):str(v) for k,v in errors.items()},rawMaterialSpeedUpper=[str(oldS),str(oldU)],
        normalizedGram=[str(E),str(F),str(G)],metric=str(eig))
    with args.output.open("x") as f:json.dump(out,f,indent=2);f.write("\n")
    print(json.dumps(dict(trace=[[float(v) for v in row] for row in trace],gram=[float(q) for q in (E,F,G)],metric=float(eig))),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for key in ("scripts","source","ramp","coast","inverse","residual","output"):
        parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--cutoff",type=int,default=112)
    run(parser.parse_args())
