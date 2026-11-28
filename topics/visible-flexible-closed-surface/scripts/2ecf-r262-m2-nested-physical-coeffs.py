#!/usr/bin/env python3
"""Nested physical radial and parity-angle correction on the same two-ended m2 seed and metric."""
import importlib.util
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
p=Path(__file__).with_name('2ecf-r262-m2-complete-physical-continuation.py')
s=importlib.util.spec_from_file_location('whole_physical_m2',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def refine(x,old,new,mo,mn):
    if new%old or mn<mo:raise ValueError('Require nested nondecreasing spaces')
    k=np.r_[np.zeros(6),np.arange(1,old)/old,np.ones(6)]
    y=np.zeros((len(k)-6,3*mn));a=np.array(x);ids=np.concatenate([np.arange(mo)+c*mn for c in range(3)]);y[3:-3,ids]=a
    b=BSpline(k,y,5)
    for q in range(1,new):
        if q%(new//old):b=b.insert_knot(q/new)
    return b.c[3:-3]
if __name__=='__main__':
    import argparse,json
    a=argparse.ArgumentParser();a.add_argument('--parent',required=True,type=Path);a.add_argument('--out',required=True,type=Path);a.add_argument('--spans',required=True,type=int);a.add_argument('--modes',required=True,type=int);v=a.parse_args()
    d=json.loads(v.parent.read_bytes());d['prolongationOf']=m.base.sha(v.parent);d['xyz']=refine(d['xyz'],d['spans'],v.spans,d['modes'],v.modes).tolist();d['spans']=v.spans;d['modes']=v.modes
    with v.out.open('x') as f:json.dump(d,f,separators=(',',':'));f.write('\n')
