#!/usr/bin/env python3
"""Continuous complete-image bounds for the uncorrected C2 physical geometry.

Reference: R299 exact curve, R302 rounded ports, R303 true H65 geometric
bounds. The inputs of this certificate are the explicit unmodified C2
positions, not any subsequent numerically corrected XYZ closing field.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np

U=2**25
PAD=2**-35


def atan_inverse(n):
    s=sum(F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(25))
    return s-F(1,51*n**51),s


a,b=atan_inverse(5)
c,d=atan_inverse(239)
Q=2**50
PL=F(math.floor((16*a-4*d)*Q),Q)
PH=F(math.ceil((16*b-4*c)*Q),Q)
K0=F(1,5)
def high(p):
    return (p-F(3,10))/(p-F(3,2))
KL,KH=high(PH),high(PL)
PI=float((PL+PH)/2)
K1=float((KL+KH)/2)
R=.115
FOOT=.233
ROOT=R*(1+.004*PI/2)
TUBE=FOOT-ROOT
CASES={'C2':[(-.3,.24,.85,.78),(0.,.24,.35,.43)],'C3':[(-1.35,.24,.92,.78),(-.95,.24,.74,.43)]}


def iv(a,b=None):
    return float(a)-PAD,float(a if b is None else b)+PAD


def add(x,y):
    return iv(x[0]+y[0],x[1]+y[1])


def mul(x,y):
    q=[a*b for a in x for b in y]
    return iv(min(q),max(q))


def neg(x):
    return -x[1],-x[0]


def trig(t,cosine):
    unit=2**42
    t=F(round(F(t)*unit),unit)
    j0=0 if cosine else 1
    poly=sum((-1)**j*t**(2*j+j0)/math.factorial(2*j+j0) for j in range(17))
    error=F(1,unit)+abs(t)**(34+j0)/math.factorial(34+j0)
    return iv(poly-error,poly+error)


def trigspan(lo,hi):
    t=(lo+hi)/2
    radius=(hi-lo)/2+PAD
    out=[]
    for c in (True,False):
        l,h=trig(t,c)
        out.append(iv(l-radius,h+radius))
    return out


def rotate(x,y,phi):
    c,s=trigspan(phi-PAD,phi+PAD)
    return add(mul(c,x),neg(mul(s,y))),add(mul(s,x),mul(c,y))


def beta(u,k):
    x=max(F(0),min(F(1),2*u-1))
    p=51480*sum(F((-1)**j*math.comb(7,j),(8+j)*(9+j))*x**(9+j) for j in range(8))
    return K0*u+(k-K0)*(p/2+max(F(0),u-1))


def quadrant(n):
    dt=(PL/(2*n),PH/(2*n))
    tr=[]
    for j in range(n+1):
        if j==0:
            tr.append((0.,0.,1.,1.))
        elif j==n:
            tr.append((1.,1.,0.,0.))
        else:
            lo,hi=beta(dt[0]*j,KL),beta(dt[1]*j,KH)
            tr.append((trig(lo,False)[0],trig(hi,False)[1],trig(hi,True)[0],trig(lo,True)[1]))
    prim=[]
    for k in range(4):
        s=[F(0)]
        for j in range(n):
            s.append(s[-1]+dt[k%2]*(F(tr[j][k])+F(tr[j+1][k]))/2)
        prim.append(s)
    sl,sh,cl,ch=prim
    er=PH/2*13*dt[1]**2/12
    X=[iv(sl[-1]-sh[j]-2*er,sh[-1]-sl[j]+2*er) for j in range(n+1)]
    Y=[iv(cl[j]-er,ch[j]+er) for j in range(n+1)]
    return X,Y


def root_interval(x):
    x=max(F(0),F(x))
    k=math.isqrt(x.numerator*2**74//x.denominator)
    return F(k,2**37),F(k+1,2**37)


def smooth(t):
    return t**3*(10-15*t+6*t*t)


def ports(A,B,ph):
    f=[]
    for j,k in enumerate((.2,K1)):
        be=j*PI/2+k*(.25-ph)
        # Suppress the outer global rotation until evaluating the entire material phase.
        c,s=trigspan(be-5*PAD,be+5*PAD)
        cx,cy=(add(A,iv(-5)),iv(0)) if j==0 else (iv(0),add(B,iv(-1/k)))
        nx,ny=rotate(c,s,ph)
        ox,oy=rotate(add(cx,mul(iv(1/k),c)),add(cy,mul(iv(1/k),s)),ph)
        f.append((ox,oy,nx,ny))
    return f


def port_plane(idx):
    # The R302 true planar face displacement, with a separate lower and upper monotone sum.
    k=(.2,K1)[idx]
    w=(.249,.30)[idx]
    flat=.234
    L=w-flat
    e=L/20
    q=k*(w/L-.025)/.95
    def lam(x):
        if x<=flat:
            return 0.
        if x<=flat+e:
            t=(x-flat)/e
            return q*e*t**3*(1-t/2)
        if x<=w-e:
            return q*(x-flat-e/2)
        if x<w:
            t=(x-(w-e))/e
            return q*(L-1.5*e)+e*(q*t+(k-q)*t**3*(1-t/2))
        return k*x
    n=512
    vals=[]
    for j in range(n+1):
        v=lam(flat+L*j/n)
        # Positive slope integrand. The float division and sqrt use a
        # margin >10^-8 to cover the exact dyadic/rational endpoint error.
        vals.append(v/math.sqrt(1-v*v))
    old=-k*w*w/(1+math.sqrt(1-(k*w)**2))
    return iv(old+L/n*sum(vals[:-1])-1e-8,old+L/n*sum(vals[1:])+1e-8)


def law(t,length):
    if length==.78:
        return smooth(t)
    e=.05
    if t<e:
        v=t/e
        return e*v**3*(1-v/2)/(1-e)
    if t>1-e:
        v=(1-t)/e
        return (1-e-e*v**3*(1-v/2))/(1-e)
    return (t-e/2)/(1-e)


def bend_table(omega,length,n):
    C=[iv(0)]
    S=[iv(0)]
    for j in range(n):
        p=omega*law(j/n,length)
        q=omega*law((j+1)/n,length)
        c,s=trigspan(min(p,q)-PAD,max(p,q)+PAD)
        C.append(add(C[-1],mul(iv(length/n),c)))
        S.append(add(S[-1],mul(iv(length/n),s)))
    return C,S


def tube_segments(idx,n,pair):
    omega,first,last,arc=CASES[pair][idx]
    base=port_plane(idx)
    tubes=[]
    cw,sw=trigspan(omega-PAD,omega+PAD)
    root=iv(ROOT)
    b=iv(TUBE)
    C,S=bend_table(omega,arc,n*4)
    def union(x,y):
        return iv(min(x[0],y[0]),max(x[1],y[1]))
    # Each item is true center (along normal, along tangent), radius and bend direction.
    for j in range(n):
        p,q=j/n,(j+1)/n
        co,si=trigspan(p*PI/2-PAD,q*PI/2+PAD)
        z=add(mul(iv(R),add(iv(1),neg(co))),iv(0,R*.004*PI/2))
        radius=add(iv(FOOT),neg(add(mul(iv(R),si),iv(0,R*.004*PI/2))))
        tubes.append((z,iv(0),radius,iv(1),iv(0)))
        tubes.append((add(root,iv(first*p,first*q)),iv(0),b,iv(1),iv(0)))
        lo,hi=4*j,4*(j+1)
        turn=sorted((omega*law(p,arc),omega*law(q,arc)))
        co,si=trigspan(turn[0]-PAD,turn[1]+PAD)
        tubes.append((add(add(root,iv(first)),union(C[lo],C[hi])),union(S[lo],S[hi]),b,co,si))
    d=add(add(root,iv(first)),C[-1])
    v=S[-1]
    for j in range(n):
        l=iv(last*j/n,last*(j+1)/n)
        tubes.append((add(d,mul(cw,l)),add(v,mul(sw,l)),b,cw,sw))
    d=add(d,mul(iv(last),cw))
    v=add(v,mul(iv(last),sw))
    # J=int_0^(pi/2) sqrt(sin(a)) da lies in [1,pi/2].
    g=iv((TUBE-R)*2/PI,TUBE-R)
    def caprow(p,q):
        co,si=trigspan(p*PI/2-PAD,q*PI/2+PAD)
        sl,sh=root_interval(si[0])[0],root_interval(si[1])[1]
        h=add(mul(iv(R),si),mul(mul(iv(2),g),iv(sl,sh)))
        radius=add(mul(iv(R),co),iv(0,TUBE-R))
        return add(d,mul(h,cw)),add(v,mul(h,sw)),radius,cw,sw
    for j in range(n):
        tubes.append(caprow(j/n,(j+1)/n))
    # Actual witnesses at alpha=11*pi/28 and 23*pi/70, with chi=pi or 0.
    p=((11/14,23/35) if pair=='C2' else (123/140,53/140))[idx]
    mark=caprow(p,p)
    return [(add(dd,base),v,r,c,s) for dd,v,r,c,s in tubes],(add(mark[0],base),*mark[1:])


def tube_box(row,frame,chi):
    d,v,r,c,s=row
    ox,oy,nx,ny=frame
    ch,sh=chi
    x=add(d,neg(mul(mul(r,ch),s)))
    y=add(v,mul(mul(r,ch),c))
    return add(ox,add(mul(x,nx),neg(mul(y,ny)))),add(oy,add(mul(x,ny),mul(y,nx))),mul(r,sh)


def lower_distance_squared(A,B):
    ds=[max(0,x[0]-y[1],y[0]-x[1]) for x,y in zip(A,B)]
    return sum(math.floor(d*U)**2 for d in ds)


def ints(box):
    return [math.floor(v[0]*U) for v in box]+[math.ceil(v[1]*U) for v in box]


def cover(a):
    XX,YY=quadrant(a.quarter)
    A,B=XX[0],YY[-1]
    ph=.5
    rows=[]
    ends={}
    def box(x,y,z):
        rows.append(ints((x,y,z)))
    def mir(x,y,z):
        box(x,y,z)
        box(x,y,neg(z))
    sectors=[]
    for j in range(a.quarter):
        x=XX[j+1][0],XX[j][1]
        y=YY[j][0],YY[j+1][1]
        co,si=trigspan(PI*j/(2*a.quarter)-PAD,PI*(j+1)/(2*a.quarter)+PAD)
        for sx,sy in ((1,1),(-1,1),(-1,-1),(1,-1)):
            gx,gy=rotate(x if sx==1 else neg(x),y if sy==1 else neg(y),ph)
            ex,ey=rotate(mul(iv(a.cap_radius),co if sx==1 else neg(co)),mul(iv(a.cap_radius),si if sy==1 else neg(si)),ph)
            sectors.append((gx,gy,ex,ey))
            box(gx,gy,iv(-.78,.78))
    ff=ports(A,B,ph)
    for j in range(2):
        w=(.249,.30)[j]
        k=(.2,K1)[j]
        ox,oy,nx,ny=ff[j]
        for v in range(80):
            x=iv(-w+2*w*v/80,-w+2*w*(v+1)/80)
            # Original circle or an inward displacement, all z tapers included.
            l=max(0,x[0],-x[1]);h=max(abs(x[0]),abs(x[1]))
            bend=lambda t:-k*t*t/(1+math.sqrt(1-k*k*t*t))
            y=iv(bend(h)-(.005863,.065943)[j],bend(l)+1e-8)
            box(add(ox,add(mul(y,nx),neg(mul(x,ny)))),add(oy,add(mul(y,ny),mul(x,nx))),iv(-.78,.78))
    ends['wholeMotherCylinderSuperset']=len(rows)
    for x,y,ex,ey in sectors:
        mir(add(x,iv(-.0032,.0032)),add(y,iv(-.0032,.0032)),iv(.78-.00005,.84+.00005))
    ends['ramp']=len(rows)
    for j in range(a.radial):
        lo,hi=j/a.radial,(j+1)/a.radial
        q=[1-smooth(t) for t in (lo,hi)]
        for gx,gy,ex,ey in sectors:
            coords=[]
            for g,e in ((gx,ex),(gy,ey)):
                v=[add(mul(iv(h),g),mul(iv(1-h),e)) for h in q]
                coords.append(iv(min(t[0] for t in v)-.0036,max(t[1] for t in v)+.0036))
            mir(*coords,iv(.84+a.length*lo-.00006,.84+a.length*hi+.00006))
    ends['closing']=len(rows)
    for j in range(a.radial):
        v=F(j,a.radial)
        w=F(j+1,a.radial)
        radius=iv(root_interval(1-w**4)[0],root_interval(1-v**4)[1])
        z=iv(.84+a.length+a.cap_height*float(v),.84+a.length+a.cap_height*float(w))
        for gx,gy,ex,ey in sectors:
            mir(mul(radius,ex),mul(radius,ey),z)
    ends['caps']=len(rows)
    ch=[trigspan(2*PI*j/a.chi-PAD,2*PI*(j+1)/a.chi+PAD) for j in range(a.chi)]
    largeframes=ports(A,B,0.)
    markers=[]
    for j in range(2):
        pieces,w=tube_segments(j,a.arm,a.pair)
        for rr in pieces:
            for chi in ch:
                box(*tube_box(rr,ff[j],chi))
        ends['arm'+str(j)]=len(rows)
        markers.append(tube_box(w,largeframes[j],(iv((-1,1)[j] if a.pair=='C2' else 1),iv(0))))
    large_low,large_high=markers
    large_d2=lower_distance_squared(large_low,large_high)
    # High-arm normalization L_1(.5) sends the expanded low-arm witness to the held frame.
    cy=add(B,iv(-1/K1))
    sx,sy=rotate(iv(0),cy,.5)
    dx,dy=rotate(large_low[0],add(large_low[1],neg(cy)),(1-K1)/2)
    witness=(add(sx,dx),add(sy,dy),large_low[2])
    # Complementary directed Hausdorff bound: bring the compact witness through the inverse high frame
    # and compare to the expanded body if required. The first direction usually suffices.
    return np.array(rows,dtype=np.int64),ends,large_d2,ints(witness),markers


def main():
    p=argparse.ArgumentParser()
    for key,v in (('quarter',128),('radial',40),('arm',40),('chi',96),('net',16)):
        p.add_argument('--'+key,type=int,default=v)
    for key,v in (('length',.38),('cap-radius',.62),('cap-height',.30)):
        p.add_argument('--'+key,type=float,default=v)
    p.add_argument('--pair',choices=('C2','C3'),default='C2')
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    B,ends,dlarge,point,marks=cover(a)
    m=a.net
    ks=np.unique([tuple(np.roll([m,i,j],r)) for i in range(-m,m+1) for j in range(-m,m+1) for r in range(3)],axis=0)
    D2=F(0)
    for lo in range(0,len(ks),16):
        k=ks[lo:lo+16]
        kp=np.maximum(k,0);kn=np.minimum(k,0)
        high=(B[:,3:]@kp.T+B[:,:3]@kn.T).max(0)
        low=(B[:,:3]@kp.T+B[:,3:]@kn.T).min(0)
        for i,w in enumerate(high-low):
            D2=max(D2,F(int(w)**2*2*m*m,U**2*int(k[i]@k[i])*(2*m*m-1)))
    diff=np.maximum(0,np.maximum(B[:,:3]-point[3:],np.asarray(point[:3])-B[:,3:]))
    held2=F(int((diff*diff).sum(1).min()),U**2)
    dl=F(dlarge,U**2)
    bounds=dict(DcompactUpper=math.sqrt(D2),DlargeLower=math.sqrt(dl),heldLower=math.sqrt(held2),heldRatioLower=math.sqrt(held2/D2),diameterQuotientRatioLower=(math.sqrt(dl/D2)-1)/2)
    out=dict(schema='C2-or-C3-unmodified-closed-H65-continuous-held-frame-and-diameter-bounds-v2',parameters={k:v for k,v in vars(a).items() if k!='out'},entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),totalContinuousBoxes=len(B),cumulativeCounts=ends,compactSquaredUpper=str(D2),largeSquaredLower=str(dl),heldSquaredLower=str(held2),witness=point,largeMarkers=marks,readable=bounds)
    with a.out.open('x') as f:
        json.dump(out,f,indent=2)
        f.write('\n')
    print(json.dumps(bounds),flush=True)


if __name__=='__main__':
    main()
