#!/usr/bin/env python3
"""Full original G10/G11 of the sewn geodesic shooting field using its true frozen target."""
import argparse
import importlib.util
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
guard=module(Path(__file__).parent/'2ecf-polar-material-global-spatial-guard-image.py','geodesic_target_observer')
def run(a):
    orig=a.output
    guard.transform=lambda jet,A,eps:jet
    a.eps=0.
    with TemporaryDirectory(dir=orig.parent) as temp:
        p=Path(temp)/'observer.json';a.output=p;guard.observe(a);q=guard.base.read(p)
    for key in ('actualSpatialGuardSHA256','epsilon','pointTransform'):q.pop(key)
    q.update(actualGeodesicObservableSHA256=guard.base.sha(__file__),observedPosition='full three-dimensional endpoint P,V,A Hermite repair and actual physical Cartesian reconstruction')
    guard.base.stores(orig,q)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','design','field','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--trace-nodes',type=int,default=2048);run(p.parse_args())
