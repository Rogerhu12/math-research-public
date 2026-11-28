#!/usr/bin/env python3
"""Certify the entire accurate normalized Gamma95 coast using whole-disk potentials."""
import argparse
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np


def load(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def main():
    ap=argparse.ArgumentParser()
    for n in ('scripts','potential','ramp','coast','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--radials',type=int,default=4)
    a=ap.parse_args();here=Path(__file__).parent;S=a.scripts
    lib=load(here/'2ecf-strong-hf-upper-sector-check.py','cg_sector')
    edge=load(here/'2ecf-strong-hf-true-edge-defects.py','cg_exact_vec')
    raw=load(S/'6a65-m12-r137-continuous-domain.py','cg_iv')
    p=load(S/'6a65-geometry-final-ramp-port-certificate.py','cg_ends')
    port=load(S/'2ecf-strong-accurate-polar-port-budgets.py','cg_port')
    K=load(S/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','cg_K');I=raw.I
    if lib.digest(a.coast)!=p.COAST_SHA or lib.digest(a.ramp)!=p.RAMP_SHA:raise ValueError('Incorrect actual inputs')
    with np.load(a.ramp) as v:A=F(float(v['centralA']))
    with np.load(a.coast) as v:
        co,si=p.real_curve(v['curve_modes'],v['curve_coefficients'])
        velocity=I(F(float(v['v'])));L=F(float(v['length']))
    check=lib.SectorCheck(K,json.loads(a.potential.read_bytes()),K.I(A))
    N=a.angles;pi=raw.pi_interval();half=pi/N;data={};curve=p.Fourier(co,si,raw,8);series=p.Series(raw)
    def phase(index,n):
        index%=2*n;key=(index,n)
        if key not in data:data[key]=raw.sincos(pi*F(index if index<=n else index-2*n,n))
        return data[key]
    arc=I(p.ARC_LO,p.ARC_HI);eps=F('2.453e-17');scale=I(1-eps,1+eps);radius=arc*scale
    center=[I(x) for x in co[0]]
    rows=[[] for _ in range(a.radials)]
    for j in range(N):
        mid=curve.point(j,N,phase,order=7)
        box=curve.box(mid,half,order=6)
        g=curve.series(box,6)
        # These exact frame identities from R265 can be evaluated on a closed
        # sigma interval. Only P,V,U are needed by the potential.
        for i in range(a.radials):
            sig=I(L*i/a.radials,L*(i+1)/a.radials)
            q=port.left_port(raw,series,g,arc,radius,scale,velocity,sig,center)
            rows[i].append([q[k] for k in ('P','V','U')])
    for i,row in enumerate(rows):
        vals=edge.ulp_vec(K,row)
        check.cartesian(*[[vals[:,d,k] for k in range(3)] for d in range(3)],'coast '+str(i))
    out=dict(schema='upper-disk-potential-true-R232-affine-coast-all-sigma-v1',entrySHA256=lib.digest(Path(__file__)),sectorSourceSHA256=lib.digest(lib.__file__),
             potentialSHA256=lib.digest(a.potential),rampSHA256=lib.digest(a.ramp),coastSHA256=lib.digest(a.coast),angles=N,radials=a.radials,
             physicalLengthExact=str(L),**check.json())
    with a.output.open('x') as h:json.dump(out,h,indent=2);h.write('\n')
    print(check.limits,flush=True)


if __name__=='__main__':main()
