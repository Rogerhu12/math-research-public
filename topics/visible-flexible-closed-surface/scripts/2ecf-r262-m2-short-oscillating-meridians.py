#!/usr/bin/env python3
"""Match a genuinely short physical meridian to the original full-160-cell m=2 line while measuring its physical two-jet amplification."""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.stats import qmc
D=5.7127541919784495;PHIC=-math.atan(2.);DC=4.173993557999608;FC=-.5*(.6*D-4)/3

def design(unit):
    # Forward order: central vertical, first high-speed turn, positive rebound,
    # second high-speed turn, actual R262 cut. Each interposed coast is physical.
    x=np.atleast_2d(unit);e=lambda v:np.exp(np.log(.0005)+v*np.log(.55/.0005))
    p=np.stack([x[:,0]*0,-np.pi/2+e(x[:,0]),-.35+1.61*x[:,1],
                  -np.pi/2+e(x[:,2]),x[:,0]*0+PHIC],axis=1)
    lengths=.018+1.5*abs(np.diff(p,axis=1))/(7.8+1.7*x[:,3:7])*(1+.55*x[:,7:11])
    coasts=x[:,11:14]*np.array([.32,.42,.32])
    return p,lengths,coasts

def run(p,l,c,steps,track=False):
    n=len(p);y=np.column_stack([np.full(n,.6),np.zeros(n),np.full(n,FC),np.ones(n)])
    minr=y[:,0].copy();maxr=y[:,0].copy();maxK=np.zeros(n);maxShape=np.zeros(n);sample=[]
    def calc(v,phi,rate):
        r,z,f,H=v.T;sn=np.sin(phi);cs=np.cos(phi);q=H+(sn/cs)*f
        rhs=(3*sn*f+4*cs*H)/r
        der=np.column_stack([-sn,cs,rhs,-sn/cs*rhs]);dN=3*f/(r*r*cs);dM=-6*q/(r*r);dL=3*rate*f/(r*cs*cs)
        K=np.maximum(abs(rate),abs(cs/r))
        return der,K,np.maximum(abs(dN)+abs(dM),abs(dL)+abs(dM))
    for seg in range(3,-1,-1):
        d=p[:,seg+1]-p[:,seg];ell=l[:,seg];v1=DC if seg==3 else 0.
        def jets(t):
            h=t*t*(3-2*t);ht=6*t*(1-t);g=t*t*(t-1);gt=t*(3*t-2)
            return p[:,seg]+d*h+ell*v1*g,d*ht/ell+v1*gt
        for k in range(steps):
            t=1-k/steps;dt=ell[:,None]/steps
            a,ka,sa=calc(y,*jets(t));b,kb,sb=calc(y+dt*a/2,*jets(t-.5/steps));e,ke,se=calc(y+dt*b/2,*jets(t-.5/steps));d4,kd,sd=calc(y+dt*e,*jets(t-1/steps))
            if track:sample.append((seg,'turn',t,y.copy(),ka,sa))
            y+=dt*(a+2*b+2*e+d4)/6;minr=np.minimum(minr,y[:,0]);maxr=np.maximum(maxr,y[:,0]);maxK=np.maximum.reduce([maxK,ka,kb,ke,kd]);maxShape=np.maximum.reduce([maxShape,sa,sb,se,sd])
        if seg>0:
            ell=c[:,seg-1];phi=p[:,seg];v=np.sin(phi);b=np.cos(phi);r,z,f,h=y.T;q=h+v/b*f
            rnew=r-ell*v
            fnew=rnew/r*f+(4*b*q)*(ell/r)
            hnew=q-v/b*fnew
            if track:
                _,kc,sc=calc(y,phi,0);sample.append((seg,'coast',1.,y.copy(),kc,sc))
            y=np.column_stack([rnew,z+ell*b,fnew,hnew]);ka,ks,ss=calc(y,phi,0);maxShape=np.maximum(maxShape,ss);maxK=np.maximum(maxK,ks)
            minr=np.minimum(minr,rnew);maxr=np.maximum(maxr,rnew)
    return y,minr,maxr,maxK,maxShape,sample

def root_candidates(unit,steps):
    p,l,c=design(unit);c0=c.copy();c1=c.copy();c0[:,1]=0.;c1[:,1]=.63
    y0,*_=run(p,l,c0,steps);y1,*_=run(p,l,c1,steps)
    ok=(y0[:,3]*y1[:,3]<0)&(y0[:,0]>.25)&(y1[:,0]>.25)
    p,l,c0,c1,u=p[ok],l[ok],c0[ok],c1[ok],unit[ok]
    if not len(p):return []
    yl=y0[ok,3];lo=c0[:,1].copy();hi=c1[:,1].copy()
    for i in range(24):
        c0[:,1]=(lo+hi)/2;y,*_=run(p,l,c0,steps)
        left=y[:,3]*yl>0;lo=np.where(left,c0[:,1],lo);hi=np.where(left,hi,c0[:,1])
    c0[:,1]=(lo+hi)/2;y,minr,maxr,k,sh,_=run(p,l,c0,steps);R,Z,F,H=y.T
    # q gain is normalized to central horizontal displacement per unit.
    gain=1/abs(F);normshape=sh/abs(F);tail=90689.28*gain
    accept=(R>.66)&(R<1.42)&(Z<1.5)&(maxr<1.53)&(k<10.3)&(minr>.24)&(abs(H/F)<.1)
    rows=[]
    for i in np.flatnonzero(accept):
        rows.append(dict(unit=u[i].tolist(),phases=p[i].tolist(),lengths=l[i].tolist(),coasts=c0[i].tolist(),radius=R[i],height=Z[i],baseCurvature=k[i],cutGain=gain[i],prefixShapeGain=normshape[i],tailShapeGain=tail[i],combined=max(normshape[i],tail[i]),angleMismatch=H[i]/F[i],maxRadius=maxr[i]))
    return rows

def refine(row,steps):
    p=np.array(row['phases'])[None,:];l=np.array(row['lengths'])[None,:];c=np.array(row['coasts'])[None,:]
    def ev(v):c[0,1]=v;return run(p,l,c,steps)[0][0,3]
    a=ev(0.);b=ev(.63)
    if a*b>=0:return None
    v=brentq(ev,0,.63,xtol=7e-15);c[0,1]=v;y,r0,r1,k,sh,_=run(p,l,c,steps);r,z,f,h=y[0];gain=1/abs(f)
    return dict(phases=p[0].tolist(),lengths=l[0].tolist(),coasts=c[0].tolist(),radius=r,height=z,maxRadius=r1[0],minRadius=r0[0],baseCurvature=k[0],cutGain=gain,
                prefixShapeGain=sh[0]*gain,tailShapeGain=90689.28*gain,combined=max(sh[0]*gain,90689.28*gain),angleMismatch=h/f)
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--full',type=Path,required=True);ap.add_argument('--power',type=int,default=13);ap.add_argument('--seed',type=int,default=7213);ap.add_argument('--coarse',type=int,default=28);ap.add_argument('--fine',type=int,default=192);a=ap.parse_args()
    full=json.loads(a.full.read_bytes());D=full['finite'][-1]['cutSlope'];FC=-.5*(.6*D-4)/3
    unit=qmc.Sobol(14,scramble=True,seed=a.seed).random_base2(a.power);rows=[]
    for k in range(0,len(unit),2048):
        rows.extend(root_candidates(unit[k:k+2048],a.coarse));print('group',k,'candidates',len(rows),flush=True)
    selected=sorted(rows,key=lambda x:x['combined'])[:4]+sorted(rows,key=lambda x:x['cutGain'])[:2]
    verified=[]
    for i,row in enumerate(selected):
        actual=refine(row,a.fine)
        if actual is not None:verified.append(actual);print('actual',actual,flush=True)
    out=dict(schema='R262-original-full160-m2-finite-short-resonant-physical-meridians-v1',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),lineSHA256=hashlib.sha256(a.full.read_bytes()).hexdigest(),size=len(unit),accepted=len(rows),coarse=a.coarse,fine=a.fine,seed=a.seed,selected=verified)
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
