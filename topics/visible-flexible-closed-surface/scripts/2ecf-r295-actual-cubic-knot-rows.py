#!/usr/bin/env python3
"""Actual original target rows at every new cubic knot and midpoint via physical inversion."""
import argparse,importlib.util,hashlib
from pathlib import Path
import numpy as np
p=Path(__file__).with_name('2ecf-r295-direct-physical-observe.py');s=importlib.util.spec_from_file_location('query_direct',p);D=importlib.util.module_from_spec(s);s.loader.exec_module(D);O=D.obs
a=O.src.template(argparse.ArgumentParser());a.add_argument('--source',type=Path,required=True);a.add_argument('--out',type=Path,required=True);a=a.parse_args();g=O.src.load(a);f=D.Direct(g,a.source);K=f.N*(f.sd-1)//f.sd;y=np.arange(2*K+1)/(2*f.N);ss=O.src.clock(y,f.bias)*g.T;rows=[]
for k,z in enumerate(ss):
    rows.append(g.row(z))
    if k%200==0:print(k,z,flush=True)
np.savez_compressed(a.out,rows=np.array(rows),N=f.N,M=f.M,bias=f.bias,seamDen=f.sd,materialT=g.T)
print('done',len(rows),hashlib.sha256(a.out.read_bytes()).hexdigest())
