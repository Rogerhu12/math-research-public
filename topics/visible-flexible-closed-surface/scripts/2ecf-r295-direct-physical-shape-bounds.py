#!/usr/bin/env python3
"""Integer and rational full direct-image slab, radius and witness-distance bounds for literal cubic cores."""
import argparse,hashlib,importlib.util,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
p=Path(__file__).with_name('2ecf-r289-cubic-meridian-physical-source.py');sp=importlib.util.spec_from_file_location('r295_literal_direct',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
def trig(hi,scale):
    s=sum((-1)**j*hi**(2*j+1)/math.factorial(2*j+1) for j in range(5));c=sum((-1)**j*hi**(2*j)/math.factorial(2*j) for j in range(6));return min(scale,math.ceil(s*scale)), max(0,math.floor(c*scale))
def cuts(t):
    p,q,r,s=(t[:,:,j] for j in range(4));return np.stack([8*p,4*(p+q),2*(p+2*q+r),p+3*q+3*r+s],axis=2),np.stack([p+3*q+3*r+s,2*(q+2*r+s),4*(r+s),8*s],axis=2)
def main():
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--split',type=int,default=3);a=p.parse_args()
    with np.load(a.source) as q:B=m.bernstein(q['cp']);d=int(q['seamDen']);n=int(q['N']);M=int(q['M']);Q=36*int(q['den']);A=F(int(q['Aint']),Q);Z=F(int(q['Zint']),int(q['den']))
    K=n*(d-1)//d;B=B[:K,:M];units=2**23;assert Q%units==0 and a.split<=4
    den=Q*8**a.split;assert np.max(abs(B))<2**49 and int(np.max(abs(B)))*8**a.split<2**62
    upper_normsq=upper_y=0;lower_gap=2**62;A0=math.floor(A*units)
    for j in range(M):
        vec=[B[:,j]]
        for _ in range(a.split):vec=[q for r in vec for q in cuts(r)]
        for k,v in enumerate(vec):
            sl,cl=trig(F(355*(j*len(vec)+k+1),113*2*M*len(vec)),units)
            r=v[...,0];z=v[...,1];denunit=den//units
            rlo=r.min(axis=(1,2))//denunit;rhi=-((-r.max(axis=(1,2)))//denunit);zlo=np.maximum(0,z.min(axis=(1,2))//denunit);zhi=-((-z.max(axis=(1,2)))//denunit)
            xlo=(rlo*cl)//units;yhi=-((-rhi*sl)//units);delta=np.maximum(A0-yhi,0)
            upper_y=max(upper_y,int(yhi.max()));upper_normsq=max(upper_normsq,int(np.max(rhi*rhi+zhi*zhi)));lower_gap=min(lower_gap,int(np.min(xlo*xlo+delta*delta+zlo*zlo)))
    y=F(upper_y,units);n2=F(upper_normsq,units**2);d2=F(lower_gap,units**2)
    out=dict(source=hashlib.sha256(a.source.read_bytes()).hexdigest(),polarCells=K*M,angularSubdivisions=2**a.split,major=str(A),cuffHeight=str(Z),finiteYUpper=str(y),finiteNormSquaredUpper=str(n2),finiteHeldDistanceSquaredLower=str(d2),finiteY=float(y),finiteRadius=math.sqrt(n2),finiteHeld=math.sqrt(d2),passStrong=y<F(895,1000) and n2<F(8,5)**2 and d2>F(64,100)**2)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(out,flush=True)
if __name__=='__main__':main()
