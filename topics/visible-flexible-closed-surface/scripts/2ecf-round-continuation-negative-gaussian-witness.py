#!/usr/bin/env python3
"""Dyadic spline and interval witness for each actual noncircular metric at t=1/16."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

def spline(t,knots,coeff,degree,order):
    k=list(knots);c=list(coeff)
    for _ in range(order):
        c=[degree*(v-u)/(k[i+degree+1]-k[i+1]) for i,(u,v) in enumerate(zip(c,c[1:]))]
        k=k[1:-1];degree-=1
    active=[Q(int(x<=t<y)) for x,y in zip(k,k[1:])]
    for d in range(1,degree+1):
        nxt=[]
        for i in range(len(active)-1):
            r=Q(0)
            if k[i+d]!=k[i]:r+=(t-k[i])/(k[i+d]-k[i])*active[i]
            if k[i+d+1]!=k[i+1]:r+=(k[i+d+1]-t)/(k[i+d+1]-k[i+1])*active[i+1]
            nxt.append(r)
        active=nxt
    return sum(x*y for x,y in zip(active,c))

def check(path):
    data=json.loads(path.read_bytes());n=data['spans'];t=Q(1,16);L=Q(str(data.get('turnLength',.4)));cut=Q(4,5)
    gap=Q(data['gap']);bump=Q(7,200);lo=Q(333,106);hi=Q(355,113)
    knot=[Q(0)]*6+[Q(float(j/n)) for j in range(1,n)]+[Q(1)]*6
    ctrl=[Q(0)]*3+[Q(x) for x in data['logRadius']]+[Q(0)]*3
    u=spline(t,knot,ctrl,5,1)/L;v=spline(t,knot,ctrl,5,2)/L**2
    # R0>=cut by phi(1-t)=pi/2-phi(t), sin(phi)+cos(phi)>0 on the full range.
    # For semiaxes R0+-d, the perimeter radius lies between R0 and R0+d^2/(2R0).
    gaprad=(gap/2)**2/(2*cut)
    h=1-10*t**3+15*t**4-6*t**5
    ht=-30*t**2*(1-t)**2
    htt=-60*t*(1-t)*(1-2*t)
    p=hi/2*t**3*(10-15*t+6*t*t)+bump
    rate=hi/2*30*t*t*(1-t)**2-4*bump*Q(27,8)
    assert rate<0
    rlo=cut-L*t
    rhi=cut+L+L*t+gaprad*h
    rsslo=(-rate)*(1-p*p/2)/L+gaprad*htt/L**2
    rsabs=p+gaprad*abs(ht)/L
    assert rlo>0 and rsslo>0
    curvature_upper=-(rsslo/rhi-2*rsabs*abs(u)/rlo+v+u*u)
    assert curvature_upper<0,(path, float(curvature_upper))
    return dict(state=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                targetGaussianAtOneSixteenthUpper=str(curvature_upper),decimalUpper=float(curvature_upper))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);p.add_argument('states',nargs='+',type=Path);a=p.parse_args()
    rows=[check(path) for path in a.states]
    out=dict(schema='physical-small-gap-own-target-gaussian-rational-witness-v1',entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=rows)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    for r in rows:print(r['state'],r['decimalUpper'])
