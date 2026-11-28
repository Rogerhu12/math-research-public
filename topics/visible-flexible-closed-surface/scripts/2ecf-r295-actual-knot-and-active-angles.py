#!/usr/bin/env python3
"""Observe all literal spline knot lines in physical coordinates and independently selected active meridian rows."""
import argparse,importlib.util,json
from pathlib import Path
import numpy as np
p=Path(__file__).with_name('2ecf-r295-direct-physical-observe.py');s=importlib.util.spec_from_file_location('r295_knot_obs',p);D=importlib.util.module_from_spec(s);s.loader.exec_module(D);O=D.obs
a=O.src.template(argparse.ArgumentParser())
for k in ('source','knot-rows','out'):a.add_argument('--'+k,type=Path,required=True)
a=a.parse_args();g=O.src.load(a);f=D.Direct(g,a.source)
with np.load(a.knot_rows) as q:rows=q['rows']
th=np.linspace(0,np.pi/2,2*f.M+1);rec=[];kx=[];mx=[]
for i in range(0,len(rows),24):
    rr=rows[i:i+24];J,U=f.grid(rr,th);K,_=O.G.F.v.curve(J);V,W=J[:,1],J[:,2]/rr[:,1,None,None];E=(V*V).sum(axis=-1)-1;H=(W*W).sum(axis=-1)-1;F=(W*V).sum(axis=-1);M=abs(E+H)/2+np.hypot((E-H)/2,F)
    mx.extend(M.max(axis=1));kx.extend(abs(K).max(axis=1))
    for X in (M,abs(K)):
        j,l=np.unravel_index(np.argmax(X),X.shape);rec.append((float(X[j,l]),int(i+j),float(rr[j,0]),float(th[l]),float(U[j,l])))
q=dict(metric=max(rec[::2]),curvature=max(rec[1::2]),radial=len(rows),quarterAngular=len(th),topMetric=[[int(i),float(mx[i])] for i in np.argsort(mx)[-35:][::-1]],topCurvature=[[int(i),float(kx[i])] for i in np.argsort(kx)[-35:][::-1]])
text=json.dumps(q,indent=2)+'\n'
with a.out.open('x') as o:o.write(text)
print(q['metric'],q['curvature'],flush=True)
