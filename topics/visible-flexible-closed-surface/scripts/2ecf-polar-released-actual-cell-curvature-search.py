#!/usr/bin/env python3
"""Search every saved radial element and all angles on the completed cap-aware physical geometry."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
p=Path(__file__).parent/'2ecf-polar-released-material-physical-two-clock-design.py'
sp=importlib.util.spec_from_file_location('complete_physical_cell',p);c=importlib.util.module_from_spec(sp);sys.modules[sp.name]=c;sp.loader.exec_module(c)
def run(a):
    ends,sol,b,S,T,rf,g,position=c.source(a);kn=np.load(a.field)['knots'];u=2*np.pi*(np.arange(a.angles)+.317)/a.angles
    point=c.module(a.scripts/'6a65-cartesian-complete-stream.py','cell_full_curvature').point
    rows=[];largest=0
    for k,(l,r) in enumerate(zip(kn[:-1],kn[1:])):
        ns=l+(r-l)*np.r_[0.,(np.arange(a.interior)+.413)/a.interior,1.]
        v=position(ns,u);cur=point.curvature_cache(v.swapaxes(1,2));z=np.max(abs(cur['eigenvalues']),axis=-1);i,j=np.unravel_index(z.argmax(),z.shape)
        w=dict(cell=k,s=float(ns[i]),u=float(u[j]),kappa=float(z[i,j]),minJac=float(np.min(cur['w'])));rows.append(w);largest=max(largest,w['kappa'])
    c.base.stores(a.output,dict(entrySHA256=c.base.sha(__file__),fieldSHA256=c.base.sha(a.field),spatialSHA256=c.base.sha(a.spatial),angularCount=len(u),radialPointsPerCell=a.interior+2,allPhysicalHermiteCells=len(rows),cellExtrema=rows,peak=max(rows,key=lambda z:z['kappa']),minJac=min(z['minJac'] for z in rows)))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','spatial','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--angles',type=int,default=768);p.add_argument('--interior',type=int,default=10)
    run(p.parse_args())
