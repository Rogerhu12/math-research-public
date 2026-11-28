#!/usr/bin/env python3
"""Actual whole sampled upper core of each saved material field against both held support planes."""
import argparse
import importlib.util
import json
import sys
from pathlib import Path
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import numpy as np
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
def run(a):
    h=Path(__file__).parent;base=module(h/'2ecf-polar-material-curve-coupled-spherical-design.py','plane_material_source')
    q=base.read(a.prepared);ind=base.read(a.independent)
    seed=base.read(a.seed_design);end=base.end_module(h,seed)
    ends=end.Ends(a.scripts,a.ramp,a.coast,seed['amp'],seed['flat'],2048)
    A=float(ends.master.A);limit=A-.65*np.sqrt(2)
    groups={k:(np.array(v['nodes']),np.array(v['angles']),np.load(v['files']['jets'],mmap_mode='r'),np.load(v['files']['radius'],mmap_mode='r')) for k,v in q['caches'].items()}
    groups['independent']=(np.array(ind['physicalNodes']),np.array(ind['angles']),np.load(ind['files']['jets'],mmap_mode='r'),np.load(ind['files']['radius'],mmap_mode='r'))
    rows=[]
    for state,field in zip(a.states,a.fields,strict=True):
        d=base.read(state);assert d['fieldSHA256']==base.sha(field) and d['seedDesignSHA256']==base.sha(a.seed_design)
        model=base.MaterialField(field,ends);b,S=model.knots[[0,-1]]
        observations={}
        for key,(ns,u,js,rad) in groups.items():
            peak=-np.inf;minheld=np.inf;count=0;where=None
            for i in range(0,len(ns),12):
                sl=slice(i,i+12);nodes=ns[sl];x=js[sl,0].copy()
                use=np.flatnonzero((nodes>=b)&(nodes<=S))
                if use.size:x[use]=model.position(nodes[use],u)[:,0]
                for k in np.flatnonzero(nodes>S):x[k]=ends.raised.raised_port(ends.warm,seed['amp'],seed['flat'],u,rad[i+k,0])['P']
                g=np.abs(x[...,1])-x[...,2];index=np.unravel_index(np.argmax(g),g.shape)
                if g[index]>peak:
                    peak=float(g[index]);where=dict(s=float(nodes[index[0]]),u=float(u[index[1]]),xyz=x[index].tolist())
                minheld=min(minheld,float(np.min(np.sqrt(x[...,0]**2+(A-np.abs(x[...,1]))**2+x[...,2]**2))))
                count+=int(np.sum(g>limit))
            observations[key]=dict(maxAbsYMinusZ=peak,projectedShortfall=peak-limit,signedDistanceHalfspaceMargin=(limit-peak)/np.sqrt(2),actualMinimumHeld=minheld,violatingPoints=count,maxLocation=where)
        print(state,observations['independent'],flush=True)
        rows.append(dict(stateSHA256=base.sha(state),fieldSHA256=base.sha(field),groups=observations))
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),centralA=A,planeThreshold=limit,finiteOnly=True,rows=rows))
if __name__=='__main__':
    a=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','output'):a.add_argument('--'+k,type=Path,required=True)
    for k in ('states','fields'):a.add_argument('--'+k,type=Path,nargs='+',required=True)
    run(a.parse_args())
