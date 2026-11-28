#!/usr/bin/env python3
"""Directed continuous Hermite/Fourier+physical-W projection and fixed-ray Lyapunov derivatives."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import time
from fractions import Fraction as F
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def parts(I,a):
    return I(np.stack([q.lo for q in a]),np.stack([q.hi for q in a]))
def split(I,ctrl,t):
    rows=[ctrl]
    while len(rows[-1].lo)>1:
        a=rows[-1];rows.append((1-t)*a[:-1]+t*a[1:])
    return parts(I,[a[0] for a in rows]),parts(I,[a[-1] for a in rows[::-1]])
def section(I,ctrl,l,r,a,b):
    if l!=a:ctrl=split(I,ctrl,I((a-l)/(r-l)))[1]
    if r!=b:ctrl=split(I,ctrl,I((b-a)/(r-a)))[0]
    return ctrl
def lower(q):return np.min(q.lo)
def det(a,b):return a[0]*b[1]-a[1]*b[0]


class Harmonics:
    def __init__(self,K,N,M):
        self.K=K;self.N=N;self.M=M;I=K.I;self.I=I
        wave=np.arange(M+1);j=np.arange(N)
        # Exact dyadic sector indices, reducing the large harmonic angle first.
        k=((2*j[:,None]+1)*wave[None,:]+N)%(2*N)-N
        sn,cs=K.sincos(I(k)*K.PI/N)
        self.trig=np.concatenate((np.asarray(cs.lo,float),-np.asarray(sn.lo,float)),axis=1).T
        err=max(np.max(cs.hi-np.asarray(self.trig[:M+1].T,np.longdouble)),
                np.max(sn.hi+np.asarray(self.trig[M+1:].T,np.longdouble)))
        if err>np.longdouble('4e-14'):raise ArithmeticError('Trigonometric table error budget exceeded')
        self.half=K.PI/N
        self.wave=I(wave.astype(np.longdouble)[None,:,None])

    def centre(self,ctrl,order):
        K=self.K;I=K.I
        # Re(c e^{iku}); complex entries stored as real/imaginary components.
        re=ctrl[:,:,:,0];im=ctrl[:,:,:,1]
        m=self.wave**order
        r=order%4
        x,y=[(re,im),(-im,re),(-re,-im),(im,-re)][r]
        x=x*m;y=y*m
        lo=np.concatenate((x.lo,y.lo),axis=1);hi=np.concatenate((x.hi,y.hi),axis=1)
        reference=np.asarray(lo,dtype=float)
        err=I(np.maximum(abs(lo-reference),abs(hi-reference))).sum(1)
        mag=I(np.maximum(abs(lo),abs(hi))).sum(1)
        dense=reference.transpose(0,2,1).reshape(-1,lo.shape[1])@self.trig
        val=dense.reshape(lo.shape[0],lo.shape[2],self.N).transpose(0,2,1)
        # n <= 322 normal binary64 terms, absolute trig error <=4e-14;
        # gamma_(2n+2)<1e-12. 1e-10 also covers all subnormal absolute errors.
        eb=err+I(F(1,10**10))*(1+mag)
        return I(val).widen(eb[:,None,:]),mag

    def boxes(self,ctrl,order=0):
        a,_=self.centre(ctrl,order);b,_=self.centre(ctrl,order+1)
        _,mag=self.centre(ctrl,order+2)
        return a.widen(Iabs(self.I,b)*self.half+mag[:,None,:]*self.half.square()/2)


def Iabs(I,z):return I(z.abs_upper())


def makepieces(K,args):
    I=K.I
    with np.load(args.field) as data:
        raw=data['coefficients'].copy();raw[[0,-1]]=data['endpointProxy']
        knots=list(map(F,data['knots']));wk=list(map(F,data['Wknots']))
        W=data['physicalW'];M=raw.shape[2]-1
    h=load(args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py','hf_knots')
    ex=load(args.scripts/'2ecf-polar-c2-correction-bernstein-budget.py','hf_w')
    extracted=ex.extract(wk,[[F(x) for x in r] for r in W],h.insert_knot)
    chan=[]
    for d in range(3):
        chan.append((d,0,0))
        for k in range(1,25):
            chan.extend([(d,k,0),(d,k,1)])
    wctrl={}
    for l,r,controls in extracted:
        lower=np.zeros((6,M+1,3,2));upper=lower.copy()
        for j,row in enumerate(controls):
            for val,(d,k,kind) in zip(row,chan):
                v=float(-val if kind else val)
                lower[j,k,d,kind]=np.nextafter(v,-np.inf);upper[j,k,d,kind]=np.nextafter(v,np.inf)
        wctrl[l,r]=I(lower,upper)
    bctrl={}
    for j,(l,r) in enumerate(zip(knots,knots[1:])):
        h=I(r-l);v=I(np.stack((raw.real,raw.imag),axis=-1)[j:j+2])
        p,ps,pss=v[0];q,qs,qss=v[1]
        bctrl[l,r]=parts(I,[p,p+h*ps/5,p+2*h*ps/5+h.square()*pss/20,
                            q-2*h*qs/5+h.square()*qss/20,q-h*qs/5,q])
    allknots=sorted(set(knots+wk));res=[]
    for a,b in zip(allknots[:-1],allknots[1:]):
        if not args.with_proxy_edges and (a<knots[1] or b>knots[-2]):continue
        k=next(k for k in bctrl if k[0]<=a<b<=k[1])
        w=next(k for k in wctrl if k[0]<=a<b<=k[1])
        P=section(I,bctrl[k],*k,a,b)+section(I,wctrl[w],*w,a,b)
        res.append((a,b,P))
    return res,M


def main():
    ap=argparse.ArgumentParser()
    for n in ('scripts','field','potential','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--angles',type=int,default=1024);ap.add_argument('--radial-depth',type=int,default=2)
    ap.add_argument('--with-proxy-edges',action='store_true');ap.add_argument('--positive-only',action='store_true')
    args=ap.parse_args();tick=time.monotonic()
    kp=args.scripts/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py'
    K=load(kp,'hf_x87');I=K.I
    if not 2<=json.loads(args.potential.read_bytes())['degree']<=3:raise ValueError('Expected quadratic or cubic sector potentials')
    if np.finfo(np.float64).nmant!=52 or np.finfo(K.LD).nmant<63:raise ValueError('IEEE double/x87 required')
    candidate=json.loads(args.potential.read_bytes())
    if candidate['fieldSHA256']!=sha(args.field):raise ValueError('Incorrect mathematical field')
    pieces,M=makepieces(K,args)
    N=args.angles
    basis=Harmonics(K,N,M);mons=candidate['monomials'];params=np.array(candidate['coefficients'])
    sec=len(params);sn,cs=K.sincos(K.PI*I(2*np.arange(sec+1))/sec)
    env={'azimuthJacobian':float('inf'),'radiusSquared':float('inf'),'positiveRayNumerator':float('inf')}
    failed=[];counts=0;min_sector=np.full(sec,np.inf);worst=[];digest=hashlib.sha256()
    def hull(ctrl):return I(np.min(ctrl.lo,axis=0),np.max(ctrl.hi,axis=0))
    pregrad=[]
    for coef in params:
        # H_x and H_y are quadratics since the supplied degree is 3.
        q={tuple(m):I(c) for m,c in zip(mons,coef)}
        pregrad.append(q)
    def evaluate(pack,s0,s1):
        nonlocal counts
        pts=[hull(row) for row in pack]
        (x,y,z),(vx,vy,vz),(ux,uy,uz)=[[v[:,k] for k in range(3)] for v in pts]
        R=x.square()+y.square();J=x*uy-y*ux;Kp=x*vy-y*vx;D=vx*uy-vy*ux
        xx=(R-F(7,8))*F(3,2);yy=4*(z-F(3,8));xd=3*R*D;yd=4*(vz*J-uz*Kp)
        env['azimuthJacobian']=min(env['azimuthJacobian'],float(np.nextafter(float(lower(J)),-np.inf)))
        env['radiusSquared']=min(env['radiusSquared'],float(np.nextafter(float(lower(R)),-np.inf)))
        # IEEE binary64 report rounds out once D_s H has been paid below.
        xp=[I(1),xx,xx.square()];yp=[I(1),yy,yy.square()]
        possible=np.zeros(N,dtype=int)
        # A numerical azimuth only proposes three neighboring sectors.
        # Two rigorous half-plane tests prove these sectors contain every
        # physical point in the current box, including modulo the 2π cut.
        ref=np.floor(np.mod(np.arctan2((y.lo+y.hi)/2,(x.lo+x.hi)/2),2*np.pi)*sec/(2*np.pi)).astype(int)%sec
        loidx=(ref-1)%sec;hiidx=(ref+2)%sec
        if np.any((cs[loidx]*y-sn[loidx]*x).lo<0) or np.any((x*sn[hiidx]-y*cs[hiidx]).lo<0):
            raise ArithmeticError('Refine angular or radial boxes for the three-sector cover')
        for dsector in (-1,0,1):
            sectors=(ref+dsector)%sec;ed=(sectors+1)%sec
            ok=((cs[sectors]*y-sn[sectors]*x).hi>=0)&((x*sn[ed]-y*cs[ed]).hi>=0)
            if not np.any(ok):continue
            possible+=ok
            poly={ (i,j):I(params[sectors[ok],v]) for v,(i,j) in enumerate(mons) }
            def deriv(mx,my,ax,ay):
                s=I(0)
                for (i,j),c in poly.items():
                    if i>=mx and j>=my:
                        fac=math.factorial(i)//math.factorial(i-mx)*math.factorial(j)//math.factorial(j-my)
                        s=s+c*fac*(ax**(i-mx))*(ay**(j-my))
                return s
            # Exact quadratic Taylor expansions of H_x,H_y around the local
            # midpoint sharply retain cancellations between monomials.
            X=xx[ok];Y=yy[ok]
            x0=I((X.lo+X.hi)/2);y0=I((Y.lo+Y.hi)/2);ex=X-x0;ey=Y-y0
            gxx=deriv(2,0,x0,y0);gxy=deriv(1,1,x0,y0);gyy=deriv(0,2,x0,y0)
            g0=deriv(1,0,x0,y0)+gxx*ex+gxy*ey
            g1=deriv(0,1,x0,y0)+gxy*ex+gyy*ey
            if candidate['degree']==3:
                xxx=poly[3,0]*6;xxy=poly[2,1]*2;xyy=poly[1,2]*2;yyy=poly[0,3]*6
                g0+=xxx*ex.square()/2+xxy*ex*ey+xyy*ey.square()/2
                g1+=xxy*ex.square()/2+xyy*ex*ey+yyy*ey.square()/2
            d=g0*xd[ok]+g1*yd[ok]
            low=float(np.nextafter(float(lower(d)),-np.inf))
            env['positiveRayNumerator']=min(env['positiveRayNumerator'],low)
            np.minimum.at(min_sector,sectors[ok],np.nextafter(d.lo.astype(float),-np.inf))
            if low<=0:
                ij=int(np.flatnonzero(ok)[np.argmin(d.lo)])
                worst.append([low,float(s0),float(s1),int(sectors[ij]),ij])
        if np.any(possible==0):raise ArithmeticError('Angular sector cover incomplete')
        counts+=N
    for i,(a,b,ctrl) in enumerate(pieces):
        P=basis.boxes(ctrl,0);U=basis.boxes(ctrl,1)
        V=basis.boxes(5*(ctrl[1:]-ctrl[:-1])/I(b-a),0)
        subs=[(a,b,[P,V,U])]
        for unused in range(args.radial_depth):
            new=[]
            for l,r,P in subs:
                split_rows=[split(I,arr,I(F(1,2))) for arr in P];mid=(l+r)/2
                new.extend([(l,mid,[p[0] for p in split_rows]),(mid,r,[p[1] for p in split_rows])])
            subs=new
        for l,r,p in subs:evaluate(p,l,r)
        digest.update(repr((str(a),str(b),env)).encode()+b'\n')
        if i%12==0:print(i,len(pieces),env,flush=True)
    out=dict(schema='physical-HF+original-W-closed-sector-directed-projection-v1',fieldSHA256=sha(args.field),
             potentialSHA256=sha(args.potential),entrySHA256=sha(__file__),kernelSHA256=sha(kp),angles=N,
             interiorRange=[str(pieces[0][0]),str(pieces[-1][1])],commonElements=len(pieces),closedBoxes=counts,
             minimum=env,worst=sorted(worst)[:50],failedSectorRows=len(worst),sectorLower=min_sector.tolist(),
             proxyEdgesOnly=args.with_proxy_edges,traceSHA256=digest.hexdigest(),seconds=time.monotonic()-tick)
    with args.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('final',env,'seconds',out['seconds'],flush=True)
    if min(env.values())<=0 and args.positive_only:raise ArithmeticError('Positive geometric hull did not close')


if __name__=='__main__':main()
