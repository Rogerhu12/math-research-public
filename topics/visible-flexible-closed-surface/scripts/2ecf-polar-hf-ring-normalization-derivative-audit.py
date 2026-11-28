#!/usr/bin/env python3
"""Finite-difference all six analytic jets of the actual ring-normalized HF source at true physical nodes."""
import argparse
from pathlib import Path
import json
import importlib.util
import os
import types
for k in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[k]="1"
import numpy as np

def m(path,name):
    s=importlib.util.spec_from_file_location(name,path);v=importlib.util.module_from_spec(s);s.loader.exec_module(v);return v

def run(a):
    here=Path(__file__).resolve().parent;main=m(here/'2ecf-polar-hf-actual-ring-normalization.py','real_ring')
    op=main.load(here/'2ecf-polar-log-radius-operator.py','frozen_radius')
    pr=main.load(here/'2ecf-polar-raw-ramp-source-compose.py','h65_src')
    prep,de,b,caches,*_=pr.validate_prepared(a)
    co=main.load(here/'2ecf-polar-fixed-prefix-position-basis.py','radial36').restrict(b)[0]
    fine=main.load(here/'2ecf-polar-local-suffix-boehm.py','radial45').build(co)[0]
    hf=main.load(a.hf_entry,'hf_ring_src');field=np.load(a.field)
    cr=main.RingSource(hf,field,fine,a.quadrature,a.scripts,a.ramp,a.coast)
    c=caches['training'];radius=op.LogRadiusCache(co,c,field['alpha']).radius
    nodes=c.nodes;u=np.array([.14,.73,1.49,2.30,3.82,4.45,5.77]);table=[]
    for goal in (.185,.271,.494,.975):
        i=np.argmin(abs(nodes-goal));s=nodes[i];f,fs,fss=radius[i];x=1e-6;y=2e-6
        def jets(ds,du):
            rad=(f+fs*ds+.5*fss*ds**2,fs+fss*ds,fss)
            return main.transformed(cr.coefficients(s+ds),rad,u+du,a.quadrature,[(1,1)])[0][(1,1)]
        j=jets(0,0);sp=jets(x,0);sm=jets(-x,0);up=jets(0,y);um=jets(0,-y)
        checks={'Xs':((sp[0]-sm[0])/(2*x),j[1]),'Xu':((up[0]-um[0])/(2*y),j[2]),
            'Xss':((sp[1]-sm[1])/(2*x),j[3]),'XsuFromXs':((up[1]-um[1])/(2*y),j[4]),
            'XsuFromXu':((sp[2]-sm[2])/(2*x),j[4]),'Xuu':((up[2]-um[2])/(2*y),j[5])}
        err={k:float(np.linalg.norm(first-second,axis=-1).max()) for k,(first,second) in checks.items()}
        table.append(dict(s=float(s),maximumEuclideanErrors=err));print(s,err,flush=True)
    out=dict(schema='HF64-ring-reset-FD-six-jet-actual-audit-v1',entrySHA256=main.sha(__file__),
        transformationSHA256=main.sha(here/'2ecf-polar-hf-actual-ring-normalization.py'),fieldSHA256=main.sha(a.field),
        quadrature=a.quadrature,angles=u.tolist(),radialEpsilon=x,angularEpsilon=y,rows=table)
    with a.output.open('x') as ff:json.dump(out,ff,indent=2);ff.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','prepared','hf-entry','field','ramp','coast','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--quadrature',type=int,required=True)
    run(p.parse_args())
