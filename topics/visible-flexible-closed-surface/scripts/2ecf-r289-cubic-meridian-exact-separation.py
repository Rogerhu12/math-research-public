#!/usr/bin/env python3
"""Integer closed-cell certificates for a cubic polar meridian tensor and its exact material angle."""
import argparse,importlib.util,json,math
from pathlib import Path
import numpy as np
from fractions import Fraction
p=Path(__file__).with_name('2ecf-r289-cubic-meridian-physical-source.py');sp=importlib.util.spec_from_file_location('cubicsrc',p);c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
DIRECTIONS=np.array([(a,b) for a in range(-5,6) for b in range(-5,6) if (a or b) and math.gcd(abs(a),abs(b))==1],dtype=np.int64)
def main():
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    with np.load(a.source) as q:cp=q['cp'];N=int(q['N']);M=int(q['M']);D=int(q['den']);Z=int(q['Zint']);sd=int(q['seamDen']) if 'seamDen' in q.files else 32;bias=Fraction(float(q['clockBias'])) if 'clockBias' in q.files else Fraction(0)
    end=N*(sd-1)//sd;B=c.bernstein(cp)[:end,:M];assert np.max(abs(B))<2**48 and np.max(abs(DIRECTIONS))<=5
    # Each sign comparison is a strict integer Bernstein convex-hull test at the same physical angle.
    bn=36*D;w=B[...,2];lo=int(np.diff(w,axis=3).min());assert lo>0
    assert np.all(w[:,0,:,0]==0) and np.all(w[:,-1,:,-1]==bn)
    rsp=int(B[:end-1,...,0].min());pc=lambda x:Fraction(8,25)+Fraction(3,2)*(1-c.clock(x,bias));dpc=lambda x:-Fraction(3,2)*(1+bias*(1-3*x*x)/2);seam=pc(Fraction(sd-1,sd))
    terminalR=[int(row[0,0]) for row in B[-1,:1,:,:,0].transpose(1,0,2)]
    assert Fraction(rsp,bn)>seam and Fraction(terminalR[-1],bn)==seam and np.all(np.diff(B[-1,...,0],axis=1)<0)
    assert np.all(B[0,: ,0,:,1]==0) and np.all(np.diff(B[0,...,1],axis=1)>0) and np.min(B[1:,...,1])>0
    assert np.all(B[-1,...,1]==36*Z)
    a0=Fraction(end-1,N);a1=Fraction(end,N);p0,p1=pc(a0),pc(a1);tcheck=[j*bn for j in (p0,p0+dpc(a0)/(3*N),p1-dpc(a1)/(3*N),p1)];assert all(q.denominator==1 for q in tcheck);tcheck=np.array(list(map(int,tcheck)),np.int64)
    assert np.all(B[-1,...,0]==tcheck[None,:,None])
    # Fractional angle u=(pi/2)*w equals the polar angle at the unmodified round terminal seam.
    for j in range(M):
        for k in range(4):
            assert int(B[-1,j,0,k,2])*3*M==bn*(3*j+k)
    A=Fraction(int(B[0,0,0,0,0]),bn);maxcent=Fraction(int(B[0,:,0,:,0].max()),bn);majorY=Fraction(0)
    # dyadic eights subdivisions in angle, evaluated by exact integer Bernstein combinations.
    # sin(x)<=x-x^3/6+x^5/120 up to pi/2; pi<355/113 and the polynomial is increasing here.
    import math as mm
    def split(controls):
        p,q,r,s=controls;return [8*p,4*(p+q),2*(p+2*q+r),p+3*q+3*r+s],[p+3*q+3*r+s,2*(q+2*r+s),4*(r+s),8*s]
    for j in range(M):
        segs=[list(map(int,B[0,j,0,:,0]))]
        for _ in range(3):segs=[s for seg in segs for s in split(seg)]
        for k,seg in enumerate(segs):
            x=Fraction(355*(8*j+k+1),113*2*8*M)
            si=min(Fraction(1),x-x**3/6+x**5/120)
            majorY=max(majorY,Fraction(max(seg),512*bn)*si)
    assert A>Fraction(145,100) and majorY<Fraction(399,512) and A-majorY>Fraction(66,100) and maxcent<Fraction(1635,1024)
    failed=[];adj=far=0;localmin=2**61;farmin=2**61
    for l in range(M):
        proj=B[:,l,:,:,:2]@DIRECTIONS.T # cell, radial-Bernstein, angular-Bernstein, integer direction
        deriv=np.diff(proj,axis=1).min(axis=(1,2));ds=np.minimum(deriv[:-1],deriv[1:]).max(axis=1);localmin=min(localmin,int(ds.min()))
        for i in np.nonzero(ds<=0)[0]:failed.append(['adjacent',int(i),int(i+1),l])
        adj+=len(ds);upper=proj.max(axis=1);lower=proj.min(axis=1)
        for i in range(end-2):
            scores=(lower[i+2:]-upper[i]).min(axis=1).max(axis=1)
            farmin=min(farmin,int(scores.min()));far+=len(scores)
            for j in np.nonzero(scores<=0)[0]:failed.append(['separated',i,int(i+2+j),l])
    out=dict(schema='literal-integer-cubic-all-angles-and-all-meridian-pairs-v1',spaceDenominator=str(bn),angularDerivativeDifference=str(lo),radiusBeforeLast=str(Fraction(rsp,bn)),exactSeam=str(seam),centralMajor=str(A),centralNormUpper=str(maxcent),centralYUpper=str(majorY),zUpper=str(Fraction(int(B[...,1].max()),bn)),finiteAngularSectors=M,finiteRadialCells=end,directionCount=len(DIRECTIONS),adjacentSuccess=adj-sum(x[0]=='adjacent' for x in failed),adjacentCount=adj,farSuccess=far-sum(x[0]=='separated' for x in failed),farCount=far,localNumeratorMin=int(localmin),farNumeratorMin=int(farmin),failures=len(failed),failedCells=failed[:200])
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print({k:v for k,v in out.items() if k!='failedCells'},flush=True)
if __name__=='__main__':main()
