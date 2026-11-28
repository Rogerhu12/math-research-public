#!/usr/bin/env python3
"""Injective two-witness radial displacement with full horizontal budgets and true-port identity."""
import argparse
import importlib.util
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import os
for n in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[n]='1'
import numpy as np
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
guard=module(Path(__file__).parent/'2ecf-polar-material-global-spatial-guard-image.py','complete_spatial_chart')
base=guard.base

def transform(j,A,eps=.035,reverse=False):
    tape=guard.Tape(reverse)
    xyz=np.moveaxis(j,1,-2);x,y,z=[tape.node(xyz[...,i]) for i in range(3)]
    def upper(t,H,e):
        return tape.shift(tape.func(tape.shift(t,-H),guard.softened(e)),H)
    def lower(t,H,e):return tape.times(upper(tape.times(t,-1),-H,e),-1)
    def norm2(a,b):return tape.add(tape.mul(a,a),tape.mul(b,b))
    y=upper(y,.895,.083);y=lower(y,-.895,.083)
    rr=tape.func(tape.shift(norm2(x,y),1e-8),guard.power(.5))
    factor=tape.mul(upper(rr,1.48,.035),tape.func(rr,guard.power(-1)))
    x=tape.mul(x,factor);y=tape.mul(y,factor)
    z=lower(z,.10,.035)
    for center in (A,-A):
        off=tape.shift(y,-center)
        r=tape.func(tape.add(norm2(x,off),tape.mul(z,z)),guard.power(.5))
        expanded=lower(r,.65,eps)
        scale=tape.mul(expanded,tape.func(r,guard.power(-1)))
        x=tape.mul(x,scale);y=tape.shift(tape.mul(off,scale),center);z=tape.mul(z,scale)
    z=upper(z,.60,.05)
    ids=(x,y,z)
    out=np.moveaxis(np.stack([tape.v[i] for i in ids],axis=-1),-2,1)
    if not reverse:return out
    def pullback(cot):
        g=np.moveaxis(cot,1,-2)
        return np.moveaxis(tape.reverse(ids,[g[...,i] for i in range(3)]),-2,1)
    return out,pullback

def observe(a):
    if not .01<=a.eps<=.07:raise ValueError('Actual sphere transition rectangle required')
    dest=a.output;guard.transform=transform
    with TemporaryDirectory(dir=dest.parent) as temp:
        q=Path(temp)/'full.json';a.output=q;guard.observe(a);data=base.read(q)
    data.update(trueSphereGuardSHA256=base.sha(__file__),bothPhysicalHeldSpheres=True)
    base.stores(dest,data)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','design','field','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--eps',type=float,default=.035);p.add_argument('--trace-nodes',type=int,default=2048)
    observe(p.parse_args())
