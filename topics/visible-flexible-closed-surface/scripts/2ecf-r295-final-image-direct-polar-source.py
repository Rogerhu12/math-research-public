#!/usr/bin/env python3
"""Generate a literal embedded-candidate polar spline directly from physical Cartesian images, without spatial reclamping."""
import argparse,importlib.util
from pathlib import Path
import numpy as np
here=Path(__file__).resolve().parent
def load_module(file,name):
    sp=importlib.util.spec_from_file_location(name,here/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
S=load_module('2ecf-r289-cubic-meridian-physical-source.py','r295_src')
def main():
    p=S.template(argparse.ArgumentParser());p.add_argument('--out',type=Path,required=True);p.add_argument('--spans',type=int,default=512);p.add_argument('--angles',type=int,default=128);p.add_argument('--prefilter',type=float,default=.5);a=p.parse_args();g=S.load(a);old=S.sec.collect;S.sec.collect=lambda g,r,n,bare=False:old(g,r,n,False);S.DEN=int(np.lcm(S.DEN,a.angles));cp,z=S.tensor(g,a.spans,a.angles,128,15/16,a.prefilter);b=S.bernstein(cp);np.savez_compressed(a.out,cp=cp,N=a.spans,M=a.angles,den=S.DEN,Zint=z,Aint=int(b[0,0,0,0,0]),seamDen=128,clockBias=15/16);print(g.m.base.sha(a.out))
if __name__=='__main__':main()
