#!/usr/bin/env python3
"""Rigorous Riemann enclosures for the nine finite cell-zero warp integrals.

Finite calibration constants are fixed binary-real geometry coefficients.
Elementary exp/log enclosures use explicit convergent series and remainder
bounds. No Gauss quadrature value is promoted into a certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np

backend=Path(__file__).with_name('db6f-audit-continuous-hermite.py')
spec=importlib.util.spec_from_file_location('db6f_background_interval_backend',backend)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
I,qbounds=mod.I,mod.qbounds


def hull(a,b):
    return I(np.minimum(a.lo,b.lo),np.maximum(a.hi,b.hi))


def positive_intersection(a):
    return I(np.maximum(0,a.lo),np.maximum(0,a.hi))


def iexp(a):
    """Taylor at |y|<=1/8, then exact positive squaring."""
    a=I.get(a)
    m=float(np.max(np.maximum(np.abs(a.lo),np.abs(a.hi))))
    k=max(0,math.ceil(math.log2(m*8))) if m else 0
    while m/(2**k)>.125:k+=1
    y=a/(2**k)
    term=I(np.ones(y.lo.shape));out=term
    for j in range(1,19):
        term=term*y/j;out=out+term
    # exp(1/8) <= 8/7; Taylor remainder after degree 18.
    rem=qbounds(Q(8,7)*Q(1,8)**19/Q(math.factorial(19)))
    out=positive_intersection(out+I(-rem.hi,rem.hi))
    for _ in range(k):out=out.square()
    return out


def log_unit(m):
    z=(m-1)/(m+1);z2=z.square();term=z;total=I(np.zeros(z.lo.shape))
    for j in range(32):
        total=total+term/(2*j+1);term=term*z2
    # |z|<=1/3, including exact endpoint m=2.
    rem=qbounds(2*Q(1,3)**65/(Q(65)*(1-Q(1,9))))
    return 2*total+I(-rem.hi,rem.hi)


LOG2=log_unit(I(2))


def ilog_point(x):
    if not x>0:raise ValueError('positive logarithm input required')
    mant,expo=math.frexp(float(x))
    return log_unit(I(2*mant))+(expo-1)*LOG2


def ilog(a):
    a=I.get(a)
    if a.lo.shape or a.hi.shape:raise ValueError('scalar logarithm interval required')
    return I(ilog_point(float(a.lo)).lo,ilog_point(float(a.hi)).hi)


def smooth(x):
    # Range hull from monotone endpoint evaluations, rather than one wide
    # power-basis interval. Every endpoint operation still rounds out.
    def one(t):return t*t*t*(10+t*(-15+6*t))
    l,h=one(I(x.lo)),one(I(x.hi))
    return I(np.maximum(0,l.lo),np.minimum(1,h.hi))


def dsmooth(x):
    return 30*x.square()*(1-x).square()


def cap(raw,raw_d,c,c_d,L):
    t=(raw-c+L)/(2*L)
    tc=I(np.clip(t.lo,0,1),np.clip(t.hi,0,1))
    # Algebraically identical to t-J(t); two symmetric branches reduce
    # interval widths near 1. All branch intersections are covered.
    def J(u):return u*u*u*u*u*(7+u*(-14+u*(10-qbounds(Q(5,2))*u)))
    left=tc-J(tc);right=qbounds(Q(1,2))-J(1-tc)
    primitive=I(np.where(tc.hi<=.5,left.lo,np.where(tc.lo>=.5,right.lo,np.minimum(left.lo,right.lo))),
                np.where(tc.hi<=.5,left.hi,np.where(tc.lo>=.5,right.hi,np.maximum(left.hi,right.hi))))
    central=c-L+2*L*primitive
    lo=central.lo.copy();hi=central.hi.copy()
    lo=np.where(t.lo<0,np.minimum(lo,raw.lo),lo);hi=np.where(t.lo<0,np.maximum(hi,raw.hi),hi)
    lo=np.where(t.hi>1,np.minimum(lo,c.lo),lo);hi=np.where(t.hi>1,np.maximum(hi,c.hi),hi)
    out=I(lo,hi)
    # Make entirely exterior cells exact formula branches.
    out=I(np.where(t.hi<=0,raw.lo,np.where(t.lo>=1,c.lo,out.lo)),
          np.where(t.hi<=0,raw.hi,np.where(t.lo>=1,c.hi,out.hi)))
    S7=tc.square().square()*(35+tc*(-84+tc*(70-20*tc)))
    d=I(np.clip(1-S7.hi,0,1),np.clip(1-S7.lo,0,1))
    return out,d*raw_d+(1-d)*c_d


def isum(a):
    l,h=a.lo.copy(),a.hi.copy()
    while len(l)>1:
        if len(l)%2:l=np.r_[l,0.];h=np.r_[h,0.]
        b=I(l[::2],h[::2])+I(l[1::2],h[1::2]);l,h=b.lo,b.hi
    return I(l[0],h[0])


def as_pair(a):return [float(a.lo),float(a.hi)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkpoint');ap.add_argument('bookkeeping');ap.add_argument('out')
    ap.add_argument('--cells',type=int,default=8192)
    ap.add_argument('--calibration-lower',type=float)
    ap.add_argument('--calibration-upper',type=float)
    args=ap.parse_args()
    f=Path(args.checkpoint);record=json.load(gzip.open(f,'rt') if f.suffix=='.gz' else f.open())
    r=record.get('response',record);cp=r.get('checkpoint',r);p=cp['parameters']
    bk=json.loads(Path(args.bookkeeping).read_text())
    ca=bk['first']['calibrationAlpha']
    calibration=I(ca if args.calibration_lower is None else args.calibration_lower,
                  ca if args.calibration_upper is None else args.calibration_upper)
    if p.get('flatOuterThroughCell',-1)>=0 or p.get('rejoinR20At') is not None:
        raise ValueError('proof assumes no flat override and no literal rejoin')
    if p['capMode']!='cut-preserving' or p['orientation']!=1 or p['a']!=2.75 or p['etaPower']!=1.5:
        raise ValueError('unsupported background class')
    if not p['capTransition']>0 or p['protectCell']!=160 or not 0<Q(p['rCut'])-Q(p['rCuff'])<Q(1,2):
        raise ValueError('transition, protected index, or exact width outside proof scope')
    if not (Q(1,200)<=Q(p['delta0'])<=Q(1,160) and Q(1,25)<=Q(p['etaRatioAtN0'])<=Q(1,16)
            and Q(p['rCuff'])>Q(7,50) and p['R']==64 and p['curvatureBound']==6 and p['wCut']==.5):
        raise ValueError('parameters outside the reviewed R15 source box')
    if len(p.get('pulseCaps',[]))>1 or len(p.get('valleyCaps',[]))>1:
        raise ValueError('all later cells must use the base cap')
    if not 0<p['slopeCap']<=1/49:
        raise ValueError('base cap not covered by 1/49')
    N=args.cells
    if N<8:raise ValueError('insufficient interval count')
    points=[qbounds(Q(j,N)) for j in range(N+1)]
    x=I(np.array([float(v.lo) for v in points[:-1]]),np.array([float(v.hi) for v in points[1:]]))
    s,sd=smooth(x),dsmooth(x)
    delta=I(p['delta0']);c0=I(p['etaRatioAtN0']);eta=delta*c0
    a=I(p['a']);root12=I(12).sqrt();q=I(1)/(2*I(2).sqrt())
    T=6*delta+6*eta/(1-q);after=3*delta+6*eta*q/(1-q)
    cuff=I(p['rCuff']);cut=I(p['rCut']);wcut=I(p['wCut'])
    oldCut=cuff*iexp(T/root12)
    R=I(p.get('prefixRByCell',[p['prefixR']])[0])
    ld=ilog(delta);beta=I(p['valleyControls'][0])
    vp=[ld,ilog(R),2*ld-ilog(calibration),I(0),ld+a*LOG2]
    desc=[(0,0,eta),(0,1,eta),(1,1,delta),(1,2,eta),(2,2,delta),
          (2,3,eta),(3,3,delta),(3,4,eta),(4,4,eta)]
    caplevels=[p['slopeCap'],p.get('pulseCaps',[[p['slopeCap'],p['slopeCap']]])[0][0],
               p.get('valleyCaps',[p['slopeCap']])[0],
               p.get('pulseCaps',[[p['slopeCap'],p['slopeCap']]])[0][1],p['slopeCap']]
    if not max(caplevels)<=.5 or not min(caplevels)>0 or max(caplevels[3:])>1/49:
        raise ValueError('cap levels violate the height lemma conditions')
    levels=[ilog_point(v) for v in caplevels]
    weights=p.get('warpWeightLevels',[[1]*5])[0]
    if min(weights)<=0:raise ValueError('positive radial weights required')
    wl=[ilog_point(v) for v in weights]
    off=I(0);totalA=I(0);totalB=I(0);totalAH=I(0);totalBH=I(0);rows=[]
    for j,(l,h,length) in enumerate(desc):
        shape=vp[l] if l==h else vp[l]+(vp[h]-vp[l])*s
        shape_d=I(0) if l==h else (vp[h]-vp[l])*sd
        vr=s if j==3 else I(1) if j==4 else 1-s if j==5 else I(0)
        vr_d=sd if j==3 else -sd if j==5 else I(0)
        source_dist=after+off+length*x
        raw=ilog(wcut)+7*(T-source_dist)/root12-a*LOG2+shape-ld+beta*vr
        raw_d=-7*length/root12+shape_d+beta*vr_d
        if j%2==0:
            lc=levels[j//2];lcd=I(0);weight=I(weights[j//2])
        else:
            k=(j-1)//2;lc=levels[k]+(levels[k+1]-levels[k])*s;lcd=(levels[k+1]-levels[k])*sd
            weight=iexp(wl[k]+(wl[k+1]-wl[k])*s)
        logw,logwd=cap(raw,raw_d,lc,lcd,I(p['capTransition']))
        if j==7:
            logwd=sd*(raw-logw)+s*raw_d+(1-s)*logwd
            logw=s*raw+(1-s)*logw
        elif j==8:logw,logwd=raw,raw_d
        w=iexp(logw);E=1+w.square();rs=cuff*iexp(source_dist/root12);rx=length*rs/root12
        chi=1-s if j==8 else I(1)
        j0=1+(cut/oldCut-1)*s if j==8 else I(1)
        A=rx*j0*(1-chi)+chi*(w*logwd).abs()/(I(p['curvatureBound'])*E*E.sqrt())
        B=chi*rx/E*weight
        IA,IB,IAH,IBH=[isum(v*qbounds(Q(1,N))) for v in [A,B,w*A,w*B]]
        totalA=totalA+IA;totalB=totalB+IB;totalAH=totalAH+IAH;totalBH=totalBH+IBH
        rows.append({'segment':j,'A':as_pair(IA),'B':as_pair(IB),'AH':as_pair(IAH),'BH':as_pair(IBH)})
        off=off+length
    if not totalB.lo>0:raise ValueError('no positive denominator bound')
    # All other finite cells have w<=1/49; the protected infinite source is
    # covered by R15's w_n<=1280*2^(-7n/4), hence also w<1/49 for n>=160.
    # Since alpha*B0 <= total physical width <1/2, these overcounting bounds
    # avoid validating alpha or any integral on the rest of the finite tail.
    height=qbounds(Q(1,98))+totalAH+qbounds(Q(1,2))*totalBH/totalB
    result={'status':'rigorous-cell-zero-integral-enclosure-and-conditional-whole-height-bound',
            'scope':__doc__,'checkpoint':str(f.resolve()),'checkpointSHA256':hashlib.sha256(f.read_bytes()).hexdigest(),
            'scriptSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'intervalBackendSHA256':hashlib.sha256(backend.read_bytes()).hexdigest(),
            'bookkeepingSHA256':hashlib.sha256(Path(args.bookkeeping).read_bytes()).hexdigest(),
            'riemannCellsPerSegment':N,'calibrationAlpha0Interval':as_pair(calibration),
            'cell0':{'A':as_pair(totalA),'B':as_pair(totalB),'AH':as_pair(totalAH),'BH':as_pair(totalBH)},
            'wholeHeightUpper':float(height.hi),'strictlyBelowOneTenth':bool(height.hi<.1),
            'formula':'H <= 1/98 + AH_0 + (1/2)*BH_0/B_0; uses positive exact global radial alpha and width<1/2',
            'segments':rows,
            'conditions':['finite source calibration coefficients frozen as binary-real constants (or inside the stated boxes)',
                          'oldCut and epsilonScale analytically derived, not independent rounded values',
                          'positive exact global radial alpha from the original width normalization',
                          'R15 raw infinite source bound beyond protectCell=160',
                          'all finite cells except cell0 use the stated common cap; no flat override or literal rejoin'],
            'notCertified':['global radial-alpha normalization existence','nonlinear surface metric','reach','infinite nonlinear graph','README completion']}
    Path(args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['calibrationAlpha0Interval','cell0','wholeHeightUpper','strictlyBelowOneTenth']}))


if __name__=='__main__':main()
