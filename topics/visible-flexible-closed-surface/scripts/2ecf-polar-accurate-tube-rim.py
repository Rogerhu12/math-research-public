#!/usr/bin/env python3
"""Directed whole-angle interval tests on the actual accurate exit normal ribbon."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import time
from fractions import Fraction as Q
from pathlib import Path

for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"
import numpy as np


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def run(args):
    started = time.monotonic()
    cp = args.scripts / "6a65-m12-r137-continuous-domain.py"
    fp = args.scripts / "6a65-geometry-final-ramp-port-certificate.py"
    cert = load(cp, "tube_integer")
    port = load(fp, "tube_fourier")
    if sha(args.ramp) != port.RAMP_SHA or sha(args.coast) != port.COAST_SHA:
        raise ValueError("Incorrect geometric source")
    I = cert.I
    with np.load(args.ramp) as source:
        A, B, c = [I(Q.from_float(float(source[key]))) for key in ("centralA","centralB","centralLength")]
    with np.load(args.coast) as source:
        co, si = port.real_curve(source["curve_modes"], source["curve_coefficients"])
        length, v = [I(Q.from_float(float(source[key]))) for key in ("length","v")]
    scale_bound = Q("2.453e-17")
    arc = I(port.ARC_LO, port.ARC_HI)
    scale = I(1-scale_bound, 1+scale_bound)
    f0 = arc*scale
    r0 = f0/v
    delta = length*(2*r0+length)
    center = [I(x) for x in co[0]]
    curve = port.Fourier(co, si, cert, max_order=6)
    jets = port.Series(cert)
    pi = cert.pi_interval()
    trig = {}
    def phase(index,count):
        m = index % (2*count)
        if m not in trig:
            trig[m] = cert.sincos(pi*Q(m if m<=count else m-2*count,count))
        return trig[m]
    lower = {}
    upper = {}
    trace = hashlib.sha256()
    R = Q(97,1000)
    for index in range(args.cells):
        half = pi/args.cells
        values = curve.box(curve.point(index,args.cells,phase,order=5),half,order=4)
        gamma, gp = values[:2]
        geometry = cert.geometry(values,arc,f0,v,length,center)
        inlet = jets.inlet(curve.series(values,order=4),arc,f0,v)
        d, dt = ([x[j] for x in inlet["V"]] for j in (0,1))
        speed = inlet["q"][0]
        T = cert.scale(1/speed,gp)
        Tt = cert.scale(1/speed,cert.sub(values[2],cert.scale(inlet["q"][1],T)))
        outward = cert.cross(T,d)
        nt = cert.add(cert.cross(Tt,d),cert.cross(T,dt))
        k = geometry["ratio"]
        kt = geometry["ratio_u"]*speed/arc
        w = delta/(r0+(r0.square()+(1+k.square())*delta).sqrt())
        wt = -k*kt*w.square()/(r0+(1+k.square())*w)
        line = cert.sub(d,cert.scale(k,T))
        line_t = cert.sub(cert.sub(dt,cert.scale(kt,T)),cert.scale(k,Tt))
        inlet_point = cert.add(center,cert.scale(scale,cert.sub(gamma,center)))
        x = cert.add(inlet_point,cert.scale(w,line))
        xt = cert.add(cert.scale(scale,gp),cert.add(cert.scale(wt,line),cert.scale(w,line_t)))
        sn, cs = phase(2*index+1,args.cells)
        err = (half+I(Q("1.075e-14"))).hi
        sn, cs = sn+I.raw(-err,err), cs+I.raw(-err,err)
        n0 = [B*cs,A*sn,I(0)]
        n0 = cert.scale(1/cert.norm2(n0).sqrt(),n0)
        chord = cert.norm2(cert.sub(outward,n0)).sqrt()
        vals = {"inletNormalChordUpper":chord, "outwardZ":outward[2],
                "positiveMaterialDerivative":geometry["material_derivative"]}
        def field(y):
            return [y[0],4*y[1]]
        parts = {key:[] for key in ("rimAngular","rimHorizontalJacobian","rimHeightAboveCylinder")}
        # Bernstein ranges on each τ interval of polys of degree at most two.
        # The mixed product is evaluated at the two edge endpoints separately.
        for sub in range(args.offset_splits):
            ta,tb = (R*(Q(2*(sub+j),args.offset_splits)-1) for j in (0,1))
            ya,yb = [cert.add(x,cert.scale(I(t),outward)) for t in (ta,tb)]
            va,vb = [cert.add(xt,cert.scale(I(t),nt)) for t in (ta,tb)]
            parts["rimAngular"].extend([det(field(ya),va), (det(field(ya),vb)+det(field(yb),va))/2,det(field(yb),vb)])
            parts["rimHorizontalJacobian"].extend([det(outward,va),det(outward,vb)])
            parts["rimHeightAboveCylinder"].extend([ya[2]-c,yb[2]-c])
        for key, possibilities in parts.items():
            vals[key] = I.raw(min(a.lo for a in possibilities),max(a.hi for a in possibilities))
        for key,val in vals.items():
            lower[key]=min(lower.get(key,val.lo),val.lo)
            upper[key]=max(upper.get(key,val.hi),val.hi)
        trace.update(repr([(key,val.lo,val.hi) for key,val in vals.items()]).encode()+b"\n")
    output = dict(schema="actual-accurate-R233-R232-two-sided-normal-rim-v1",
                  exactLower={k:str(Q(v,cert.SCALE)) for k,v in lower.items()},
                  exactUpper={k:str(Q(v,cert.SCALE)) for k,v in upper.items()},
                  integerBits=cert.BITS,cells=args.cells,offsetSplits=args.offset_splits,
                  offsetRadius=str(R),vectorField="(x,4y,0)",
                  entrySHA256=sha(__file__),integerSHA256=sha(cp),fourierSHA256=sha(fp),
                  rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),
                  rowSHA256=trace.hexdigest(),seconds=time.monotonic()-started)
    with args.output.open("x") as fp:
        json.dump(output,fp,indent=2)
        fp.write("\n")
    print(json.dumps({k:[float(Q(lower[k],cert.SCALE)),float(Q(upper[k],cert.SCALE))] for k in lower}))
    if any(lower[k]<=0 for k in ("rimAngular","rimHorizontalJacobian","rimHeightAboveCylinder","positiveMaterialDerivative")):
        raise ArithmeticError("Some rim bounds did not close")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for arg in ("scripts","ramp","coast","output"):
        parser.add_argument("--"+arg,required=True,type=Path)
    parser.add_argument("--cells",type=int,default=2048)
    parser.add_argument("--offset-splits",type=int,default=2)
    args = parser.parse_args()
    if args.cells<256 or args.offset_splits<1:
        raise ValueError("Invalid cover")
    run(args)
