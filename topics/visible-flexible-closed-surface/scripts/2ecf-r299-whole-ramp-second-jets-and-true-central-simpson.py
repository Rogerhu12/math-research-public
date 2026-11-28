#!/usr/bin/env python3
"""Global continuous second jets of the actual R299 H65 ramp, including its exact non-Fourier inlet."""
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np


def ataninv(n):
    s=sum(F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(28))
    return s,s+F(1,57*n**57)


a,b=ataninv(5)
c,d=ataninv(239)
QPI=2**57
PL=F(math.floor((16*a-4*d)*QPI),QPI)
PH=F(math.ceil((16*b-4*c)*QPI),QPI)
K0=F(1,5)
def high(p):
    return (p-F(3,10))/(p-F(3,2))
KL,KH=high(PH),high(PL)

def compact(lo,hi,n=2**48):
    return F(math.floor(lo*n),n),F(math.ceil(hi*n),n)

def beta(u,k):
    x=max(F(0),min(F(1),2*u-1))
    p=51480*sum(F((-1)**j*math.comb(7,j),(8+j)*(9+j))*x**(9+j) for j in range(8))
    return K0*u+(k-K0)*(p/2+max(F(0),u-1))

def curvature(u,k):
    x=max(F(0),min(F(1),2*u-1))
    s=sum(math.comb(15,j)*x**j*(1-x)**(15-j) for j in range(8,16))
    return K0+(k-K0)*s

def trig(t,cosine):
    n=2**53;t0=F(round(t*n),n);j0=0 if cosine else 1
    val=sum((-1)**j*t0**(2*j+j0)/math.factorial(2*j+j0) for j in range(14))
    e=F(1,n)+abs(t0)**(28+j0)/math.factorial(28+j0)
    return compact(val-e,val+e)

def trig_bounds(lo,hi):
    return trig(lo,False)[0],trig(hi,False)[1],trig(hi,True)[0],trig(lo,True)[1]

def moment(C,d):
    return max(sum((1 if k==0 else 2)*k**d*(abs(F(float(v.real)))+abs(F(float(v.imag)))) for k,v in enumerate(C[:,c])) for c in range(2))

def inlet_errors(C,n):
    nt=4*n
    step=PL/(2*n),PH/(2*n)
    wz=2**43
    scal=2**49
    ctr=[]
    dirs=[]
    for j in range(2*n+1):
        ulo,uhi=PL*j/(4*n),PH*j/(4*n)
        if j==0:
            z=(F(0),F(0),F(1),F(1))
            t=z
        elif j==2*n:
            z=(F(1),F(1),F(0),F(0))
            t=z
        else:
            z=trig_bounds(beta(ulo,KL),beta(uhi,KH))
            t=trig_bounds(ulo,uhi) if j%2==0 else None
        ctr.append(z)
        if j%2==0:
            sn,co=math.floor(t[0]*wz),math.floor(t[2]*wz)
            assert t[1]-F(sn,wz)<F(2,wz) and t[3]-F(co,wz)<F(2,wz)
            dirs.append((sn,co))
    # S=I_x(8,8) has degree-15 Bernstein controls 0 through 7, then 1.
    kx=(KH-K0)*30
    kxx=(KH-K0)*15*14*4
    kxxx=(KH-K0)*15*14*13*8*2
    d4=kxxx+4*KH*kxx+3*kx**2+6*KH**2*kx+KH**4
    assert d4<100000
    # Composite cell Simpson, on each cell using its actual midpoint.
    er=PH/2*step[1]**4*d4/2880
    ints=[]
    for k in range(4):
        ar=[F(0)]
        for j in range(n):
            ar.append(ar[-1]+step[k%2]*(ctr[2*j][k]+4*ctr[2*j+1][k]+ctr[2*j+2][k])/6)
        ints.append(ar)
    sl,sh,cl,ch=ints
    vals=[[],[],[]]
    for j in range(n+1):
        l,h,ll,hh=ctr[2*j]
        klo=curvature(step[0]*j,KL)
        khi=curvature(step[1]*j,KH)
        vals[0].append(((sl[-1]-sh[j]-2*er,sh[-1]-sl[j]+2*er),(cl[j]-er,ch[j]+er)))
        vals[1].append(((-h,-l),(ll,hh)))
        vals[2].append(((-khi*hh,-klo*ll),(-khi*h,-klo*l)))
    quad=np.arange(nt)//n
    idx=np.arange(nt)%n
    idx=np.where(quad%2,n-idx,idx)
    sx=np.where((quad==0)|(quad==3),1,-1)
    sy=np.where(quad<2,1,-1)
    gr=np.asarray(dirs,np.int64)
    SN=gr[idx,0]*sy;CS=gr[idx,1]*sx
    waves=np.arange(len(C))
    eps=[]
    for der in (0,1,2):
        cc=[];ci=[]
        for k,row in enumerate(C):
            rr=[];ii=[]
            for c in range(2):
                re,im=F(float(row[c].real)),F(float(row[c].imag))
                for j in range(der):
                    re,im=-im*k,re*k
                fac=1 if k==0 else 2
                rr.append(fac*round(re*scal));ii.append(fac*round(im*scal))
            cc.append(rr);ci.append(ii)
        rc=np.asarray(cc,np.int64);ic=np.asarray(ci,np.int64)
        assert rc.shape==ic.shape and max(np.abs(rc).max(),np.abs(ic).max())<2**61
        bits=10
        def digits(arr):
            return [(np.sign(arr)*((np.abs(arr)>>(bits*p))%2**bits)).astype(np.int64) for p in range(7)]
        rr,ii=digits(rc),digits(ic)
        # All limb dot-products and their differences fit signed 64 bit.
        assert 2*len(C)*wz*2**bits<2**63
        upper=F(0)
        for start in range(0,nt,96):
            seq=np.arange(start,min(start+96,nt))
            w=seq[:,None]*waves[None,:]%nt
            sn,co=SN[w],CS[w]
            pol=np.zeros((len(seq),2),dtype=object)
            for p in range(7):
                if np.any(rr[p]) or np.any(ii[p]):
                    pol+=(co@rr[p]-sn@ii[p]).astype(object)*(2**(bits*p))
            for jj,i in enumerate(seq):
                for c in (0,1):
                    lo,hi=vals[der][idx[i]][c]
                    sg=(sy if der==1 and c==0 or der!=1 and c==1 else sx)[i]
                    if sg<0:lo,hi=-hi,-lo
                    v=F(int(pol[jj,c]),wz*scal)
                    upper=max(upper,abs(lo-v),abs(hi-v))
        # The dot with rounded trig differs by <=2/wz times coefficient l1.
        # Rounding exact Fourier real and imaginary inputs adds <=2*nmodes/scal.
        eps.append(upper+F(2,wz)*(moment(C,der)+F(2*len(C),scal))+F(2*len(C),scal))
    h=step[1]
    M4=moment(C,4)+kxx+3*KH*kx+KH**3
    M3=moment(C,3)+kx+KH**2
    # Cubic Hermite value remainder, linear derivative interpolation, and
    # nearest-node second derivative comparison on every real angular cell.
    return [eps[0]+h*eps[1]/4+M4*h**4/384,eps[1]+M3*h*h/8,eps[2]+M3*h/2]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--field',type=Path,required=True)
    ap.add_argument('--quarter',type=int,default=2048)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    with np.load(a.field) as f:C=f['portPVA'];nodes=f['radialNodes']
    initial=inlet_errors(C[0,0],a.quarter)
    print('actual inlet enclosure',list(map(float,initial)),flush=True)
    scale=2**52
    raw=np.stack((np.rint(C.real*scale),np.rint(C.imag*scale)),axis=-1).astype(np.int64).astype(object)
    n=C.shape[2]
    K=np.arange(n,dtype=object)
    weights=[np.r_[1,np.full(n-1,2)].astype(object)*K**j for j in range(3)]
    unit=np.zeros_like(raw[0,0])
    unit[0,2,0]=scale
    # V0 and A0 are exactly prescribed. Native initial z is a constant double.
    assert np.count_nonzero(C[0,1])==1 and C[0,1,0,2]==1 and np.count_nonzero(C[0,2])==0
    assert np.count_nonzero(C[0,0,1:,2])==0
    zerr=abs(F(float(C[0,0,0,2].real))-F(1,5))
    def bound(arr,coef,der,axis):
        w=list(map(F,coef))
        den=math.lcm(*[x.denominator for x in w])
        v=sum((c.numerator*(den//c.denominator))*d[:,axis] for c,d in zip(w,arr))
        return F(int(np.sum(np.abs(v)*weights[der][:,None])),den*scale)+sum(map(abs,w))*F(int(sum(weights[der])),scale)
    XSS=[F(0)]*3
    XSU=[F(0)]*3
    XUU=[F(0)]*3
    dangle=[F(0)]*3
    dzvel=[F(0)]*3
    eP=[[F(0)]*3 for i in range(3)]
    dP=[[F(0)]*3 for i in range(3)]
    ddP=[[F(0)]*3 for i in range(3)]
    for i in range(len(nodes)-1):
        h=F(float(nodes[i+1]))-F(float(nodes[i]))
        data=[*raw[i],*raw[i+1]]
        # Input order P0,V0,A0,P1,V1,A1.
        b=[(1,0,0,0,0,0),(1,h/5,0,0,0,0),(1,2*h/5,h*h/20,0,0,0),(0,0,0,1,-2*h/5,h*h/20),(0,0,0,1,-h/5,0),(0,0,0,1,0,0)]
        v=[[(F(q)-F(p))*5/h for p,q in zip(r,t)] for r,t in zip(b,b[1:])]
        acc=[[(q-p)*4/h for p,q in zip(r,t)] for r,t in zip(v,v[1:])]
        for c in range(3):
            for co in v:
                native=bound(data,co,1,c)
                if i==0:native+=abs(co[0])*(initial[1] if c<2 else 0)
                XSU[c]=max(XSU[c],native)
                dz=bound(data+[unit],co+[-1],0,c)
                if i==0:dz+=abs(co[0])*(initial[0] if c<2 else zerr)
                dzvel[c]=max(dzvel[c],dz)
            for co in acc:
                z=bound(data,co,0,c)
                if i==0:z+=abs(co[0])*(initial[0] if c<2 else zerr)
                XSS[c]=max(XSS[c],z)
            for co in b:
                # Refers to the exact central angular second derivative for all controls.
                diff=bound(data+[raw[0,0]],list(co)+[-1],2,c)+(initial[2] if c<2 else 0)
                if i==0 and co[0]==1:
                    # Native V0,A0 have zero angular derivatives. The true control
                    # at this endpoint is exactly the true central position.
                    diff=F(0)
                XUU[c]=max(XUU[c],diff)
                diff=bound(data+[raw[0,0]],list(co)+[-1],1,c)+(initial[1] if c<2 else 0)
                if i==0 and co[0]==1:diff=F(0)
                dangle[c]=max(dangle[c],diff)
    # Actual terminal endpoint discrepancy from (gamma+d e_z, e_z, 0).
    for j in range(3):
        for c in range(3):
            a0=raw[-1,j]
            for der,out in ((0,eP),(1,dP),(2,ddP)):
                if j==0:
                    value=bound([a0,raw[0,0],unit],[1,-1,-F(float(nodes[-1]))],der,c)
                    value+=initial[der] if c<2 else (zerr if der==0 else 0)
                elif j==1:value=bound([a0,unit],[1,-1],der,c)
                else:value=bound([a0],[1],der,c)
                out[j][c]=value
    sc=2**40
    def sqrtup(x):
        return F(1+math.isqrt(x.numerator*sc**2//x.denominator),sc)
    def norm(x):return sqrtup(sum(v*v for v in x))
    drift=sqrtup(sum(v*v for v in dzvel+dangle))
    gmin=(1-drift)**2
    assert drift<1
    s,st,t=norm(XSS),norm(XSU),KH+norm(XUU)
    upper=(s+t+sqrtup((s-t)**2+4*st**2))/(2*gmin)
    pack=lambda v:[str(x) for x in v]
    out=dict(schema='true-H65-continuous-ramp-second-jets-Bernstein-and-fourth-order-inlet-v1',fieldSHA256=hashlib.sha256(a.field.read_bytes()).hexdigest(),sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),quarter=a.quarter,inletMaxPerCoordinate=pack(initial),velocityFromVertical=pack(dzvel),angularFromCenter=pack(dangle),fullXss=pack(XSS),fullXsu=pack(XSU),fullXuuFromTrueCenter=pack(XUU),terminalValue=[pack(t) for t in eP],terminalAngular=[pack(t) for t in dP],terminalSecondAngular=[pack(t) for t in ddP],metricEigenvalueLower=str(gmin),globalPrincipalAbsoluteUpper=str(upper))
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('curvature',float(upper),'global minimum Gram eigenvalue',float(gmin),'terminal_second',[[float(x) for x in z] for z in ddP],flush=True)

if __name__=='__main__':
    main()
