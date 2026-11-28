#!/usr/bin/env python3
"""Directed R302/R299 port-Weingarten certificate and the full arm clearances for two physical inputs."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import numpy as np


def low(v):
    return np.nextafter(v, -np.inf)


def high(v):
    return np.nextafter(v, np.inf)


class I:
    def __init__(self, a, b=None):
        if isinstance(a, I):
            self.l, self.h = a.l, a.h
        elif b is not None:
            self.l, self.h = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
        elif isinstance(a, (Q, str)):
            self.l, self.h = low(float(Q(a))), high(float(Q(a)))
        else:
            self.l, self.h = np.asarray(a, dtype=float), np.asarray(a, dtype=float)

    def __add__(s, o):
        o = I(o)
        return I(low(s.l+o.l), high(s.h+o.h))

    __radd__ = __add__

    def __neg__(s):
        return I(-s.h, -s.l)

    def __sub__(s, o):
        return s+-I(o)

    def __rsub__(s, o):
        return I(o)+-s

    def __mul__(s, o):
        o = I(o)
        a,b,c,d = s.l*o.l,s.l*o.h,s.h*o.l,s.h*o.h
        return I(low(np.minimum(np.minimum(a,b), np.minimum(c,d))),
                 high(np.maximum(np.maximum(a,b), np.maximum(c,d))))

    __rmul__ = __mul__

    def __truediv__(s, o):
        o = I(o)
        assert np.all(o.l > 0)
        return s*I(low(1/o.h), high(1/o.l))

    def sq(s):
        a,b = s.l*s.l,s.h*s.h
        return I(np.where((s.l<=0)&(s.h>=0), 0., low(np.minimum(a,b))), high(np.maximum(a,b)))

    def sqrt(s):
        assert np.all(s.l >= 0)
        return I(low(np.sqrt(s.l)), high(np.sqrt(s.h)))

    def __getitem__(s, ix):
        return I(s.l[ix], s.h[ix])


def uniform(n):
    return I(low(np.arange(n,dtype=float)/n), high(np.arange(1,n+1,dtype=float)/n))


def directed_window(kl, kh, A, n, nt):
    k = I(low(float(kl)), high(float(kh)))
    flat = Q(117,500)
    L = A-flat
    e = L/20
    q = k*(I(A)/I(L)-I(Q(1,40)))/I(Q(19,20))
    t = uniform(n)
    p0, p1, pp0, pp1, width = [], [], [], [], []
    pieces = [(Q(0),flat), (flat, flat+e), (flat+e, A-e), (A-e,A)]
    for j,(lo,hi) in enumerate(pieces):
        x = I(lo)+I(hi-lo)*t
        S3 = t.sq()*(3-2*t)
        integral_S3 = t.sq()*t*(1-t/2)
        if j == 0:
            la, dl = t*0, t*0
        elif j == 1:
            la, dl = q*I(e)*integral_S3, q*S3
        elif j == 2:
            la, dl = q*I(e/2)+q*I(hi-lo)*t, q+t*0
        else:
            la = q*I(L-3*e/2)+I(e)*(q*t+(k-q)*integral_S3)
            dl = q+(k-q)*S3
        a, b = (1-(k*x).sq()).sqrt(), (1-la.sq()).sqrt()
        p0.append(-k*x/a)
        p1.append(-la/b)
        pp0.append(-k/(a*a*a))
        pp1.append(-dl/(b*b*b))
        width.append(I((hi-lo)/n))
    def cat(v):
        return I(np.concatenate([x.l for x in v]), np.concatenate([x.h for x in v]))
    p, v, pp, vv = map(cat, (p0,p1,pp0,pp1))
    deriv = v-p
    integrals, current = [], I(0)
    for a in range(3,-1,-1):
        for b in range(n-1,-1,-1):
            step = -deriv[a*n+b]*width[a]
            integrals.append(current+I(min(0,float(step.l)), max(0,float(step.h))))
            current = current+step
    dh = I(np.array([v.l for v in integrals[::-1]]),np.array([v.h for v in integrals[::-1]]))
    y = uniform(nt)[None,:]
    def S5(z):
        z=I(z)
        return z.sq()*z*(10+z*(-15+6*z))
    w = I(np.maximum(0,S5(y.l).l),np.minimum(1,S5(y.h).h))
    wp = 30*y.sq()*(1-y).sq()/I(Q(3,10))
    wpp = 60*y*(1-y)*(1-2*y)/I(Q(9,100))
    x1 = p[:,None]*(1-w)+v[:,None]*w
    z1 = dh[:,None]*wp
    x2 = pp[:,None]*(1-w)+vv[:,None]*w
    z2 = dh[:,None]*wpp
    mixed = deriv[:,None]*wp
    scale = I(Q(173,20))*(1+x1.sq()+z1.sq()).sqrt()
    tests={}
    for sign in (-1,1):
        u = scale*(1+x1.sq())+sign*x2
        v = scale*(1+z1.sq())+sign*z2
        j = scale*x1*z1+sign*mixed
        det = u*v-j.sq()
        tests[str(sign)] = [str(Q(float(np.min(g.l)))) for g in (u,v,det)]
    assert all(Q(x)>0 for row in tests.values() for x in row)
    upper = lambda a: str(Q(float(max(np.max(abs(a.l)),np.max(abs(a.h))))))
    return dict(tests=tests, cells=4*n*nt, offset=upper(dh), axialSlope=upper(z1),
                maxMiddleCurvature=str(Q(float(q.h))))


def run(args):
    if args.r299:
        baseline=json.loads(args.r299.read_text())
        kl,kh=map(Q,baseline["highCurvature"])
        B=Q(baseline["centerB"][0])
    else:
        kl,kh,B=Q(3211,1855),Q(117578,67925),Q(123497,100000)
    lower=directed_window(Q(1,5),Q(1,5),Q(249,1000),args.cells,args.axial)
    upper=directed_window(kl,kh,Q(3,10),args.cells,args.axial)
    assert Q(lower["offset"])<Q(5862,10**6) and Q(upper["offset"])<Q(65942,10**6)
    r=Q(23,200)
    a=Q(233,1000)
    pl,ph=Q(103993,33102),Q(355,113)
    dblo,dbhi=[r*(1+p/500) for p in (pl,ph)]
    blo,bhi=a-dbhi,a-dblo
    tiphi=r+2*(bhi-r)
    bend_s5=Q(78,100)/(Q(15,8)*Q(1117,1000))
    bend_short=Q(43,100)*Q(19,20)/Q(1117,1000)
    assert r<blo<bhi<Q(118,1000) and min(bend_s5,bend_short)>bhi+r
    ang=(pl-Q(5,2))/2
    assert Q(1,4)*(1-Q(1,20)**2/6)>Q(249,1000)
    assert ang*(1-(kh*ang)**2/6)>Q(3,10)
    assert pl/2-kh/4-Q(1117,1000)>0
    highbase=B-1/kl+(1/kh-Q(upper["offset"]))*(1-(kh/4)**2/2)
    highlower=highbase-max(bhi,a*kh/4)
    original_low=max(Q(1,4)+a+dbhi/20,Q(1,4)+Q(19,10)*Q(177,1000)+bhi)
    new_low_len=dbhi+Q(24,100)+Q(78,100)+Q(85,100)+tiphi
    new_low=max(Q(1,4)+a+dbhi/20,Q(1,4)+new_low_len/20+bhi)
    high_held_diameter=dblo+Q(24,100)+Q(43,100)+Q(35,100)+r
    assert highlower-original_low>Q(300,1000) and highlower-new_low>Q(514,1000)
    assert high_held_diameter>Q(125,100)
    out=dict(schema="reconstructed-directed-R302-and-C2-v2",entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             R299SHA256=hashlib.sha256(args.r299.read_bytes()).hexdigest() if args.r299 else None,
             low=lower,high=upper,K="173/20",r=str(r),tubeBounds=list(map(str,(blo,bhi))),
             bothBendRadiiLower=list(map(str,(bend_s5,bend_short))),
             completeArmClearanceLower=dict(R302=str(highlower-original_low),C2=str(highlower-new_low)),
             C2HighHeldPatchDiameterLower=str(high_held_diameter))
    with args.output.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--r299", type=Path)
    parser.add_argument("--cells",type=int,default=192)
    parser.add_argument("--axial",type=int,default=192)
    parser.add_argument("--output",type=Path,required=True)
    run(parser.parse_args())
