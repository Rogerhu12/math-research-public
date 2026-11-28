#!/usr/bin/env python3
"""Enforce both half-turn width anisotropy and the original sixth-turn directional support gain exactly."""
from pathlib import Path
import importlib.util,sys,numpy as np
def load():
    p=Path(__file__).resolve().with_name('2ecf-r262-free-support-full-shape.py')
    s=importlib.util.spec_from_file_location('R262_width_locked_full_physical',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def directions(t,js):
    x=t[:,None];m=js[None,:];a=(js%4==2).astype(float);c3=np.array([1,.5,-.5,-1,-.5,.5])[js%6]
    b=(1-c3-1.5*a)/2
    c=np.cos(m*x);s=np.sin(m*x);c2=np.cos(2*x);s2=np.sin(2*x);c3=np.cos(3*x);s3=np.sin(3*x)
    h=c-a*c2-b*c3;hp=-m*s+2*a*s2+3*b*s3;rad=(1-m*m)*c+3*a*c2+8*b*c3
    drad=-(1-m*m)*m*s-6*a*s2-24*b*s3
    integ=s/m-a*s2/2-b*s3/3;radint=(1-m*m)*s/m+1.5*a*s2+(8/3)*b*s3
    return h,hp,rad,drad,integ,radint
if __name__=='__main__':
    import json
    mod=load();mod.directions=directions
    old_dump=mod.json.dump
    def dump(obj,f,**kwargs):
        obj.update(schema='R262-fixed-original-g-two-width-and-sixth-turn-constraints-physical-v1',widthConstraintSourceSHA256=mod.base.sha(__file__))
        old_dump(obj,f,**kwargs)
    mod.json.dump=dump
    mod.main()
