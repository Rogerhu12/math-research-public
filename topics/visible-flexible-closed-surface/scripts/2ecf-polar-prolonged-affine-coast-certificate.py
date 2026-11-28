#!/usr/bin/env python3
"""All-angle, full radial interval proof for prolonged affine R137 coasts at fixed Gamma95."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(sp);sys.modules[name]=mod;sp.loader.exec_module(mod)
    return mod
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args):
    tick=time.monotonic()
    root=args.scripts
    cp=root/'6a65-m12-r137-continuous-domain.py'
    fp=root/'6a65-geometry-final-ramp-port-certificate.py'
    cert=load(cp,'exit_graph_int');port=load(fp,'exit_graph_fourier')
    if sha(args.ramp)!='0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7' or sha(args.coast)!='f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d':
        raise ValueError('Actual R233 and R232 masters required')
    I=cert.I
    arc=I(port.ARC_LO,port.ARC_HI)
    scale_bound=Q('0.00000000000000002453')
    scale=I(1-scale_bound,1+scale_bound);f0=arc*scale
    with np.load(args.ramp) as r:
        A,B,c=[I(Q.from_float(float(r[k]))) for k in ('centralA','centralB','centralLength')]
    with np.load(args.coast) as z:
        co,si=port.real_curve(z['curve_modes'],z['curve_coefficients'])
        original_length,v=[I(Q.from_float(float(z[k]))) for k in ('length','v')]
    curve=port.Fourier(co,si,cert,max_order=6)
    pi=cert.pi_interval();trig={}
    def phase(index,count):
        m=index%(2*count)
        if m not in trig:trig[m]=cert.sincos(pi*Q(m if m<=count else m-2*count,count))
        return trig[m]
    center=[I(x) for x in co[0]]
    extends=[Q(a) for a in args.lengths]
    if len(set(extends))!=len(extends) or min(extends)<=original_length.upper():raise ValueError("Distinct proper extensions required")
    minimum={};maximum={};rows=hashlib.sha256()
    for j in range(args.cells):
        val=curve.box(curve.point(j,args.cells,phase,order=5),pi/args.cells,order=4)
        gamma,p,q=val[:3]
        base=cert.geometry(val,arc,f0,v,original_length,center);K=base['Tu']
        energy=cert.norm2(p);vel=energy.sqrt()
        cross=cert.cross(p,q);crossnorm=cert.norm2(cross).sqrt()
        curvature=crossnorm/(energy*vel)
        T=cert.scale(1/vel,p)
        NF=cert.scale(1/(energy*curvature),cert.sub(q,cert.scale(cert.dot(p,q)/energy,p)))
        BF=cert.scale(1/crossnorm,cross)
        d=cert.add(cert.scale(-v/K,NF),cert.scale((1-(v/K).square()).sqrt(),BF))
        r0=f0/v
        start=cert.add(center,cert.scale(scale,cert.sub(gamma,center)))
        for length in extends:
            L=I(length);geo=cert.geometry(val,arc,f0,v,L,center);k=geo["ratio"]
            delta=L*(2*r0+L)
            w=delta/(r0+(r0.square()+(1+k.square())*delta).sqrt())
            x=cert.add(start,cert.scale(w,cert.sub(d,cert.scale(k,T))))
            current=dict(exitHeightAboveCentral=x[2]-c,allCoastMaterialAngleDerivative=geo["material_derivative"],
                         allCoastD=geo["D"],allCoastPrincipalCurvature=geo["nonzero_principal_curvature"])
            for name,y in current.items():
                key=(str(length),name)
                minimum[key]=min(minimum.get(key,y.lo),y.lo)
                maximum[key]=max(maximum.get(key,y.hi),y.hi)
            rows.update(repr((str(length),[(a,b.lo,b.hi) for a,b in current.items()])).encode()+b"\n")
    bounds={}
    for length in extends:
        lo={k:str(Q(y,cert.SCALE)) for (s,k),y in minimum.items() if s==str(length)}
        hi={k:str(Q(y,cert.SCALE)) for (s,k),y in maximum.items() if s==str(length)}
        bounds[str(length)]=dict(exactLower=lo,exactUpper=hi)
        print(length,json.dumps({k:[float(Q(lo[k])),float(Q(hi[k]))] for k in lo}),flush=True)
    out=dict(schema="actual-Gamma95-prolonged-accurate-affine-coasts-v1",bounds=bounds,
        radialRangeForEachLength="0<=sigma<=L, height is on sigma=L",cells=args.cells,integerBits=cert.BITS,
        originalCoastLengths=[str(original_length.lower()),str(original_length.upper())],arc=[str(port.ARC_LO),str(port.ARC_HI)],
        allRowsSHA256=rows.hexdigest(),entrySHA256=sha(__file__),integerSHA256=sha(cp),fourierSHA256=sha(fp),
        rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),seconds=time.monotonic()-tick)
    with args.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    if min(minimum.values())<=0:raise ArithmeticError("A prolonged regularity or positive height claim failed")


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for name in ('scripts','ramp','coast','output'):ap.add_argument('--'+name,required=True,type=Path)
    ap.add_argument('--cells',type=int,default=1024)
    ap.add_argument('--lengths',nargs='+',required=True)
    args=ap.parse_args()
    if args.cells<256:raise ValueError('At least 256 complete angle cells required')
    run(args)
