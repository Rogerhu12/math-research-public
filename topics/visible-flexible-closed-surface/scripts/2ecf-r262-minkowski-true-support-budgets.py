#!/usr/bin/env python3
"""Rational original central curvature radius, directed support gains and fitted support convexity."""
import argparse,gzip,hashlib,importlib.util,json,math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
s=importlib.util.spec_from_file_location('native_proof',Path(__file__).with_name('2ecf-g12-actual-central-convexity.py'));base=importlib.util.module_from_spec(s);s.loader.exec_module(base)
def bernstein(c,l,r):
    D=len(c)-1;h=r-l
    p=[sum(c[k]*math.comb(k,i)*l**(k-i)*h**i for k in range(i,D+1)) for i in range(D+1)]
    return [sum(p[i]*Q(math.comb(k,i),math.comb(D,i)) for i in range(k+1)) for k in range(D+1)]
def midpoint_split(b):
    l=[];r=[];t=b
    while len(t):
        l.append(t[0]);r.append(t[-1]);t=[(x+y)/2 for x,y in zip(t,t[1:])]
    return l,r[::-1]
def run(path,states):
    with gzip.open(path,'rb') as f:
        with np.load(f) as z:c=[Q(float(x)) for x in z['jets'][0,0]]
    M=(len(c)-2)//3;a={1:c[0]}
    for j in range(1,M+1):a[1+3*j]=(c[j]+c[M+j])/2;a[1-3*j]=(c[j]-c[M+j])/2
    det=[Q(0)]*(2*M+1);speed=det.copy();av2=sum(k*k*v*v for k,v in a.items())
    for k,x in a.items():
        for l,y in a.items():
            j=abs(l-k)//3;det[j]+=k*l*l*x*y;speed[j]+=k*l*x*y
    A=[bernstein(base.exact_polynomial(p),-Q(1),Q(1)) for p in (speed,det)]
    radius=Q(4,25);cells=[]
    def rec(v,d,level):
        mv,md=min(v),max(d)
        if mv>0 and min(d)>0 and mv**3>radius**2*av2*md*md:
            cells.append(level);return
        if level>=18:raise ArithmeticError('Positive radius test exhausted')
        for vv,dd in zip(midpoint_split(v),midpoint_split(d)):rec(vv,dd,level+1)
    rec(*A,0)
    old60=2*sum(c[1:M+1:2])/a[1];assert 0<old60<Q(1,5)
    # |gamma| upper and directional support lower use the same exact perimeter scale.
    rads=sum(abs(z) for z in c[1:M+1]);tans=sum(abs(z) for z in c[M+1:2*M+1])
    assert (a[1]+rads)**2+tans**2<(a[1]-rads+a[1]/4)**2
    # a-b=21/20, a<pi/2<11/7 from perimeter>=4a; E speed average^2<=mean speed^2 implies b>.3.
    gap=Q(21,20);assert (gap+Q(3,10))**2+Q(3,10)**2<2
    xmax=(Q(11,7)-gap)/(gap+Q(3,10));xmin=Q(3,10)/Q(11,7)
    assert (1+3*xmax*xmax)/4<Q(61,100)**2
    eigengain=3*gap*(1+xmin)/(4*(1+Q(61,100)))-old60
    assert eigengain>Q(38,100)
    # Ellipse curvature radius min=b^2/a>(.3)^2/(11/7).
    ellipse_r=Q(9,100)*Q(7,11);rows=[]
    for p in states:
        t=json.loads(p.read_bytes());eta=Q(t['eta']);q=[Q(v) for v in t.get('support',[])]
        two='widthConstraintSourceSHA256' in t
        co={}
        for j,z in enumerate(q,3):
            co[j]=co.get(j,Q(0))+z
            if two:
                aa=int(j%4==2);bb=(1-[Q(1),Q(1,2),-Q(1,2),-Q(1),-Q(1,2),Q(1,2)][j%6]-Q(3,2)*aa)/2
                co[2]=co.get(2,Q(0))-aa*z;co[3]=co.get(3,Q(0))-bb*z
            else:
                aa=(1-[Q(1),Q(1,2),-Q(1,2),-Q(1),-Q(1,2),Q(1,2)][j%6])/Q(3,2)
                co[2]=co.get(2,Q(0))-aa*z
        cheb=[Q(0)]*(max(co,default=0)+1)
        for j,z in co.items():cheb[j]=(1-j*j)*z
        perturb_lo=base.bound(cheb,64)[0]
        lower=(1-eta)*radius+eta*ellipse_r+perturb_lo
        if lower<=0:raise ValueError((p, float(lower)))
        signed_width=sum(2*z for j,z in co.items() if j%4==2)
        widthGain=(gap-Q(1,4))*eta+signed_width
        rows.append(dict(state=p.name,SHA256=hashlib.sha256(p.read_bytes()).hexdigest(),correctedCentralRadiusStrictLower=str(lower),sixthTurnSupportGainStrictLower=str(eta*eigengain),halfWidthDifferenceGainStrictLower=str(widthGain),widthLocked=(not q or two)))
    return dict(originalNormalizedRadiusStrictLower=str(radius),bernsteinLeaves=len(cells),depth=max(cells),rawPerimeterRadiusSquaredUpper=str(av2),rawPerimeterRadiusLower=str(a[1]),originalSixthTurnSupportGapStrictUpper=str(old60),originalHalfWidthDifferenceStrictUpper='1/4',mixedSixthTurnGainPerEtaStrictLower=str(eigengain),mixedHalfWidthGainPerEtaStrictLower='4/5',states=rows)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('states',nargs='+',type=Path);a=p.parse_args()
    r=run(a.data,a.states);r['entrySHA256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with a.out.open('x') as f:json.dump(r,f,indent=2);f.write('\n')
    for x in r['states']:print(x['state'],*[float(Q(x[k])) for k in ('correctedCentralRadiusStrictLower','sixthTurnSupportGainStrictLower','halfWidthDifferenceGainStrictLower')])
