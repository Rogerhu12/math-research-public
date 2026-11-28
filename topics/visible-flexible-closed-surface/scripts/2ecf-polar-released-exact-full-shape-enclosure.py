#!/usr/bin/env python3
"""Uniform integer Fourier/Bernstein position enclosures for actual released-cuff fields, including real end traces."""
import argparse
from functools import lru_cache
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
import numpy as np
K=2**25
W=2**32
V=2**20
H=2**37
def q(x):return Q.from_float(float(x))
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ceil(x):return -((-x.numerator)//x.denominator)
def trig(N,M):
    """Rounded fixed-point phases at rational tan(theta/2) midpoints, all four quadrants."""
    rr=np.empty((M,4*N),np.int64);ii=rr.copy()
    for j in range(N):
        a=2*j+1;b=2*N;den=a*a+b*b;cn=b*b-a*a;sn=2*a*b
        x=H;y=0
        for k in range(M):
            for iq in range(4):
                u,v=((x,y),(-y,x),(-x,-y),(y,-x))[(iq*k)%4]
                rr[k,iq*N+j]=(u*V+H//2)//H;ii[k,iq*N+j]=(v*V+H//2)//H
            x,y=(x*cn-y*sn+den//2)//den,(x*sn+y*cn+den//2)//den
    # In complex Euclidean norm, one rounded unit rotation costs < 1/H.
    err=Q(M,H)+Q(1,2*V)
    return np.concatenate([rr,-ii]).astype(float),err
def mix(C,weights):
    w=np.array([round(x*W) for x in weights],dtype=np.int64)
    assert sum(abs(int(z))*int(np.max(abs(v))) for z,v in zip(w,C))<2**62
    return np.tensordot(w,C,axes=(0,0))//W
def split(poly,depth):
    if depth==0:return [poly]
    stages=[poly]
    for k in range(len(poly)-1):stages.append((stages[-1][:-1]+stages[-1][1:])//2)
    left=np.stack([p[0] for p in stages]);right=np.stack([p[-1] for p in stages[::-1]])
    return split(left,depth-1)+split(right,depth-1)
def radial_basis(t,kn):
    @lru_cache(None)
    def B(i,d):
        if d==0:return Q(kn[i]<=t<kn[i+1])
        z=Q(0)
        if kn[i+d]>kn[i]:z+=(t-kn[i])/(kn[i+d]-kn[i])*B(i,d-1)
        if kn[i+d+1]>kn[i+1]:z+=(kn[i+d+1]-t)/(kn[i+d+1]-kn[i+1])*B(i+1,d-1)
        return z
    return [B(i,5) for i in range(len(kn)-6)]
def S5(s,b,T,t0,t1):
    t=min(Q(1),max(Q(0),((s-b)/(T-b)-t0)/(t1-t0)))
    return t**3*(10-15*t+6*t*t)
def run(a):
    state=json.loads(a.state.read_text());cor=json.loads(a.correction.read_text());F=digest(a.field)
    assert state['fieldSHA256']==F==cor['sourceFieldSHA256'] and cor['sourceStateSHA256']==digest(a.state)
    A=q(float.fromhex('0x1.68493d1d794f0p+0'));Alo=int(A*K)
    z=np.load(a.field);knots=list(map(q,z['knots']));coeff=z['coeff'];M=coeff.shape[2]
    b=knots[0];T=knots[-1];origin=q(state['oldS']);r=Q(4,5)+origin-T
    delta=q(cor.get('raisedCuffDelta',0.));t0,t1=map(q,cor.get('transition',(0.,1.)))
    phase,phase_err=trig(a.quarter_cells,M);mx=a.quarter_cells
    C=np.rint(K*np.concatenate([coeff.real,coeff.imag],axis=2)).astype(np.int64)
    # Exact flat last trace (two angular jets follow from the same Fourier polynomial).
    C[-1]=0;C[-1,0,1,0]=round(K*r);C[-1,0,M+1,1]=-round(K*r);C[-1,0,0,2]=round(K*Q(83,200))
    C[-1,1,1,0]=-K;C[-1,1,M+1,1]=K
    maxL1=int(np.max(abs(C).sum(axis=2)))
    ns=cor['spans'];mm=cor['modes'];sk=[Q(0)]*6+[q(i/ns) for i in range(1,ns)]+[Q(1)]*6
    nr=len(sk)-6;cc=np.zeros((nr,2*M,3),np.int64);co=np.array(cor['coefficients']).reshape(3,nr-6,mm+1)
    for d in range(3):
        for m in range(mm+1):
            k=2*m+int(d<2)
            idx=k if d!=1 else M+k
            cc[3:-3,idx,d]=np.rint((1 if d!=1 else -1)*K*co[d,:,m]).astype(np.int64)
    # Bound each correction derivative by its degree-four B-spline control envelope (exact knots).
    dw=[Q(0)]*3
    for i in range(1,nr):
        for d in range(3):
            add=int(abs(cc[i,:,d]-cc[i-1,:,d]).sum())+2*(mm+1)
            dw[d]=max(dw[d],Q(5*add,K)/((T-b)*(sk[i+5]-sk[i])))
    # Units in K for uniform Fourier l1 coefficient error. Each initial coefficient rounding costs ≤.5/K.
    # Raw radial Bernstein has at most 3 contributing traces and sum of absolute weights <2.
    # Each midpoint de Casteljau stage rounds downward by less than 1/K per coefficient.
    raw_error=2*M+Q(3*maxL1,2*W)+2*M*(1+5*a.depth)
    # At most six B-splines (nonnegative, sum 1); no more than mm+1 populated modes per coordinate.
    wc=int(np.max(abs(cc).sum(axis=1)))
    correction_error=Q(mm+1,2)+Q(6*wc,2*W)+(mm+1)
    fixed_pad=ceil(raw_error+correction_error)+3
    thresholds=[Q(514,1000),Q(52,100),Q(54,100),Q(58,100),Q(65,100),Q(75,100),Q(9,10)]
    bounds=dict(maxAbsY=0,maxNorm2=0,minHeld2=9*K*K,maxZ=-2*K,minZ=2*K)
    narrow=[-2*K]*len(thresholds);ranges=0
    def gather(lo,hi):
        nonlocal ranges
        aa=np.maximum(abs(lo),abs(hi));near=np.maximum(0,np.maximum(lo,-hi))
        assert aa.max()<2*K and np.max(aa[1])<Alo
        norm2=aa[0]**2+aa[1]**2+aa[2]**2
        dist2=near[0]**2+(Alo-aa[1])**2+near[2]**2
        bounds['maxAbsY']=max(bounds['maxAbsY'],int(max(aa[1])));bounds['maxNorm2']=max(bounds['maxNorm2'],int(max(norm2)))
        bounds['minHeld2']=min(bounds['minHeld2'],int(min(dist2)));bounds['maxZ']=max(bounds['maxZ'],int(max(hi[2])));bounds['minZ']=min(bounds['minZ'],int(min(lo[2])))
        r2=near[0]**2+near[1]**2
        for i,threshold in enumerate(thresholds):
            use=r2<=ceil((K*threshold)**2)
            if np.any(use):narrow[i]=max(narrow[i],int(max(hi[2,use])))
        ranges+=lo.shape[1]
    # First-cell left three controls from exact R267/Gamma95 position, unit V and |A|<5.897.
    # Both near-flat neighboring endpoint and complete spline are handled by the same first-cell box.
    h=knots[1]-b;assert h<Q(1,100)
    left=[Q(142,100),Q(5,10),Q(182,1000)]
    first=np.array([ceil(K*(x+2*h/5+h*h*6/20)) for x in left])
    other=[]
    for d in range(3):
        m0,m1,m2=[Q(int(np.sum(abs(C[1,j,:,d])))+M,K) for j in range(3)]
        other.append(ceil(K*(m0+2*h*m1/5+h*h*m2/20)))
    a0=np.maximum(first,np.array(other))+np.array([ceil(h*vv*K) for vv in dw])+2
    # For first cell, bound z below by using the known positive constant Fourier mode.
    ztrace=Q(int(C[1,0,0,2])-int(abs(C[1,0,1:,2]).sum())-M,K)
    dv=Q(int(abs(C[1,1,:,2]).sum()+M),K);da=Q(int(abs(C[1,2,:,2]).sum()+M),K)
    lower=min(Q(18078,100000)-2*h/5-h*h*6/20,ztrace-2*h*dv/5-h*h*da/20)-h*dw[2]
    lo=-a0.copy();lo[2]=int(lower*K)-1;hi=a0.copy();hi[2]+=ceil(delta*S5(knots[1],b,T,t0,t1)*K)
    gather(lo[:,None],hi[:,None])
    modes=np.r_[np.arange(M),np.arange(M)]
    for i in range(1,len(knots)-1):
        h=knots[i+1]-knots[i];assert h<Q(1,100)
        a0,a1=C[i],C[i+1]
        poly=np.stack([a0[0],mix(a0,[Q(1),h/5,Q(0)]),mix(a0,[Q(1),2*h/5,h*h/20]),mix(a1,[Q(1),-2*h/5,h*h/20]),mix(a1,[Q(1),-h/5,Q(0)]),a1[0]])
        for j,sub in enumerate(split(poly,a.depth)):
            left=knots[i]+h*Q(j,2**a.depth);right=left+h/2**a.depth;mid=(left+right)/2
            corr=mix(cc,radial_basis((mid-b)/(T-b),sk));P=(sub+corr[None,:,:]).transpose(0,2,1)
            norm=np.sum(abs(P),axis=2)
            assert int(np.max(norm))*V<2**52
            # Integer products and all partial sums are exactly representable by binary64.
            vals=np.rint((P.reshape(18,2*M).astype(float)@phase)/V).astype(np.int64).reshape(6,3,-1)
            L1=np.einsum('acm,m->ac',abs(P),modes)
            for d in range(3):
                kpad=ceil(dw[d]*(right-left)*K/2)
                pad=(L1[:,d]+mx-1)//mx+np.array([ceil(int(v)*phase_err) for v in norm[:,d]])+fixed_pad+kpad
                if d==0:
                    lower3=np.empty((3,vals.shape[2]),np.int64);upper3=lower3.copy()
                lower3[d]=np.min(vals[:,d]-pad[:,None],axis=0);upper3[d]=np.max(vals[:,d]+pad[:,None],axis=0)
            lower3[2]+=int(K*delta*S5(left,b,T,t0,t1));upper3[2]+=ceil(K*delta*S5(right,b,T,t0,t1))
            gather(lower3,upper3)
    out=dict(entrySHA256=digest(__file__),sourceStateSHA256=digest(a.state),sourceFieldSHA256=F,cartesianCorrectionSHA256=digest(a.correction),deltaExact=str(delta),coefficientQuantization=K,weightScale=W,phaseScale=V,phaseRecurrenceScale=H,fullFourierModes=M,quarterAngleCells=mx,radialHalfSubdivisions=2**a.depth,nonemptyBoxCount=ranges,uniformCoefficientFloorPadUnits=fixed_pad,correctionGlobalCartesianDerivativeUpper=list(map(str,dw)),upperAbsY=str(Q(bounds['maxAbsY'],K)),upperNormSquared=str(Q(bounds['maxNorm2'],K*K)),lowerWitnessDistanceSquared=str(Q(bounds['minHeld2'],K*K)),trueConnectorZInterval=[str(Q(bounds['minZ'],K)),str(Q(bounds['maxZ'],K))],radialConditionalUpperZ={str(x):str(Q(v,K)) for x,v in zip(thresholds,narrow)},usesWholeTrueGamma95FirstTrace=True)
    out['strongClosedShapePass']=(Q(out['upperAbsY'])<Q(895,1000) and Q(out['upperNormSquared'])<Q(8,5)**2 and Q(out['lowerWitnessDistanceSquared'])>Q(65,100)**2)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(out['strongClosedShapePass'],float(Q(out['upperAbsY'])),float(Q(out['upperNormSquared']))**.5,float(Q(out['lowerWitnessDistanceSquared']))**.5,out['trueConnectorZInterval'],flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('state','field','correction','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--quarter-cells',type=int,default=1024);p.add_argument('--depth',type=int,default=2);run(p.parse_args())
