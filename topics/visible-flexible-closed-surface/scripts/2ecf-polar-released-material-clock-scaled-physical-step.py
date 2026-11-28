#!/usr/bin/env python3
"""Physical-coordinate step scaling for the two-clock optimizer; source, metric rows and derivatives are unchanged."""
import argparse
import importlib.util
import sys
from pathlib import Path
import os
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.optimize import minimize
from tempfile import TemporaryDirectory
p=Path(__file__).parent/'2ecf-polar-released-material-physical-two-clock-design.py'
sp=importlib.util.spec_from_file_location('physical_step_two_clock',p);c=importlib.util.module_from_spec(sp);sys.modules[sp.name]=c;sp.loader.exec_module(c)
def run(a):
    def scaled(fun,x0,**opts):
        scales=np.full_like(x0,a.step_scale);cb=opts.pop('callback')
        def merit(y):
            ell,grad=fun(x0+scales*y);return ell,scales*grad
        rr=minimize(merit,np.zeros_like(x0),callback=lambda y:cb(x0+scales*y),**opts);rr.x=x0+scales*rr.x;return rr
    c.minimize=scaled;out=a.output
    with TemporaryDirectory(dir=out.parent) as tmp:
        inner=Path(tmp)/'inner.json';a.output=inner;c.run(a);q=c.base.read(inner)
    q.update(physicalStepScaleEntrySHA256=c.base.sha(__file__),physicalParameterScale=a.step_scale);c.base.stores(out,q)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','spatial','closed','warm','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('spans',16),('modes',7),('metric-spans',16),('samples-s',385),('samples-u',256),('radials',143),('angles',88),('iterations',470)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',12.),('geometry',30.),('peak-weight',.08),('peak-tau',.13),('step-scale',.0125)]:p.add_argument('--'+k,type=float,default=v)
    p.add_argument('--new-target',action='store_true');run(p.parse_args())
