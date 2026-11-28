#!/usr/bin/env python3
"""Whole-angle interval budgets for the actual Γ95/R205 physical polar connector."""
import argparse
import hashlib
import importlib.util
import json
import os
import time
from fractions import Fraction as Q
from pathlib import Path

for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"
import numpy as np


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def det(p, q):
    return p[0]*q[1]-p[1]*q[0]


def dot(p, q):
    return p[0]*q[0]+p[1]*q[1]


def left_port(cert, J, g, arc, a, scale, v, length, center):
    """All vector series differentiate the same native Fourier variable."""
    sn = J.inlet(g, arc, a, v)
    d, q = sn["V"], sn["q"]
    iq = J.inv(q)
    T = J.vscale(iq, J.vderivative(g))
    N = J.cross(d, T)
    rate = J.scale(arc, iq)
    dt = lambda y: J.mul(rate, J.derivative(y))
    Tu = J.vscale(rate, J.vderivative(T))
    du = J.vscale(rate, J.vderivative(d))
    n = J.scale(1/a, J.dot(Tu, N))
    k = J.mul(J.dot(du,N),J.inv(J.dot(Tu,N)))
    con = lambda x: J.constant(x,len(k))
    k2 = J.mul(k,k)
    base = J.add(con(1),k2)
    r0 = a/v
    delta = length*(2*r0+length)
    w = J.scale(delta,J.inv(J.add(con(r0),J.sqrt(J.add(con(r0.square()),J.scale(delta,base))))))
    H = J.add(con(a),J.scale(v,J.mul(w,base)))
    D = J.add(con(a),J.mul(w,J.sub(J.scale(v,base),dt(k))))
    outer_rate = J.mul(rate,J.mul(H,J.inv(D)))
    Du = lambda y: J.mul(outer_rate,J.derivative(y))
    f = a+v*length
    cosb = J.scale(v/f,J.add(con(r0),w))
    sinb = J.scale(v/f,J.mul(k,w))
    e1 = J.vadd(J.vscale(cosb,d),J.vneg(J.vscale(sinb,T)))
    start = [J.add(con(c),J.scale(scale,J.sub(b,con(c)))) for c,b in zip(center,g)]
    P = J.vadd(start,J.vscale(w,J.vadd(d,J.vneg(J.vscale(k,T)))))
    lam = J.scale(a**3/f.square(),J.mul(n,J.mul(k2,J.inv(D))))
    A = J.vscale(lam,N)
    e2=J.vadd(J.vscale(sinb,d),J.vscale(cosb,T))
    nn=J.scale(a/f.square(),J.mul(n,J.mul(J.mul(H,H),J.inv(D))))
    mm=J.scale(a.square()/f.square(),J.mul(n,J.mul(k,J.mul(H,J.inv(D)))))
    U=J.vscale(con(f),e2)
    SU=J.vadd(J.vscale(con(v),e2),J.vscale(J.scale(f,mm),N))
    UU=J.vadd(J.vscale(con(-v*f),e1),J.vscale(J.scale(f.square(),nn),N))
    Nu=J.vadd(J.vscale(J.scale(-f,mm),e1),J.vscale(J.scale(-f,nn),e2))
    AU=J.vadd(J.vscale(Du(lam),N),J.vscale(lam,Nu))
    val = lambda y: [x[0] for x in y]
    return {key:val(y) for key,y in dict(P=P,V=e1,A=A,U=U,SU=SU,AU=AU,UU=UU).items()}


class RightPort:
    """Profile primitives with monotone endpoint rectangle bounds on [0,1]."""
    def __init__(self,cert,m=512):
        self.c=cert
        I=cert.I
        def either(x):
            return I(min(Q(x),Q(float(x))),max(Q(x),Q(float(x))))
        self.r,self.y0,self.span=[either(x) for x in ("0.8","0.34","0.46")]
        self.amp=I(Q(.8746432018013935))
        self.Z=I(Q(.51))
        self.m=m
        self.primitives=[(I(0),I(0))]
        self.ends=[]
        for j in range(m+1):
            t=I(Q(j,m))
            alpha=self.amp*self.smooth(t)
            self.ends.append(cert.sincos(alpha))
            if j:
                s0,c0=self.ends[-2]; s1,c1=self.ends[-1]
                C,H=self.primitives[-1]
                self.primitives.append((C+I.raw(c1.lo,c0.hi)/m,H+I.raw(s0.lo,s1.hi)/m))

    @staticmethod
    def smooth(t):
        return t**5*(126+t*(-420+t*(540+t*(-315+70*t))))

    def get_primitive(self,t):
        c,I=self.c,self.c.I
        vals=[]
        for x in (t.lower(),t.upper()):
            j=min(self.m,int(x*self.m))
            C,H=self.primitives[j]
            delta=I(x-Q(j,self.m))
            sn0,cs0=self.ends[j]
            sn1,cs1=self.ends[min(j+1,self.m)]
            vals.append((C+delta*I.raw(cs1.lo,cs0.hi),H+delta*I.raw(sn0.lo,sn1.hi)))
        return tuple(c.hull(a,b) for a,b in zip(*vals))

    def port(self,su,cu):
        c,I=self.c,self.c.I
        # Use reflection across y=0; all derivatives below are for the first quadrant.
        y=self.r*su
        t_raw=(y-self.y0)/self.span
        t=I.raw(max(0,min(c.SCALE,t_raw.lo)),max(0,min(c.SCALE,t_raw.hi)))
        slope=self.amp*630/self.span*t**4*(1-t)**4
        second=self.amp*2520/self.span.square()*t**3*(1-t)**3*(1-2*t)
        # S9 monotonicity; avoid dependency growth near t=1.
        alpha0=self.amp*self.smooth(c.lower_i(t))
        alpha1=self.amp*self.smooth(c.upper_i(t))
        sn_lo,cs_hi=c.sincos(alpha0);sn_hi,cs_lo=c.sincos(alpha1)
        sn=I.raw(sn_lo.lo,sn_hi.hi);cs=I.raw(cs_lo.lo,cs_hi.hi)
        Cp,Hp=cs,sn
        Cpp,Hpp=-sn*slope,cs*slope
        Cppp,Hppp=-cs*slope.square()-sn*second,-sn*slope.square()+cs*second
        C,H=self.get_primitive(t)
        C=I.raw(min(y.lo,self.y0.lo),min(y.hi,self.y0.hi))+self.span*C
        H=self.span*H
        x=self.r*cu
        return dict(P=[x,C,self.Z-H],V=[-cu,-Cp*su,Hp*su],A=[I(0),Cpp*su.square(),-Hpp*su.square()],
                    U=[-y,Cp*x,-Hp*x],SU=[su,-Cpp*x*su-Cp*cu,Hpp*x*su+Hp*cu],
                    AU=[I(0),Cppp*x*su.square()+2*Cpp*su*cu,-Hppp*x*su.square()-2*Hpp*su*cu],
                    UU=[-x,Cpp*x.square()-Cp*y,-Hpp*x.square()+Hp*y])


def budgets(port, L, side):
    P,V,A,U,SU,AU,UU=[port[k] for k in ("P","V","A","U","SU","AU","UU")]
    r2=P[0].square()+P[1].square()
    res=2*dot(P,U)/r2
    phiu=det(P,U)/r2
    phis=det(P,V)/r2
    phisu=(det(U,V)+det(P,SU))/r2-res*phis
    phiuu=det(P,UU)/r2-res*phiu
    h=dot(P,V)/r2
    hu=(dot(U,V)+dot(P,SU))/r2-res*h
    g=det(P,A)/r2
    phiss=g-2*h*phis
    phissu=(det(U,A)+det(P,AU))/r2-res*g-2*(hu*phis+h*phisu)
    us=-phis/phiu
    uss=-(phiss+2*phisu*us+phiuu*us.square())/phiu
    zs=V[2]+U[2]*us
    zss=A[2]+2*SU[2]*us+UU[2]*us.square()+U[2]*uss
    rho=r2.sqrt()
    ru=dot(P,U)/rho; rs=dot(P,V)/rho
    rss=(dot(V,V)+dot(P,A)-rs.square())/rho
    rsu=(dot(U,V)+dot(P,SU)-rs*ru)/rho
    ruu=(dot(U,U)+dot(P,UU)-ru.square())/rho
    R_s=rs+ru*us
    R_ss=rss+2*rsu*us+ruu*us.square()+ru*uss
    sign=1 if side=="left" else -1
    return dict(radius=rho,fixedRadiusSpeed=R_s,fixedRadiusAcceleration=R_ss,
                clock0=phiu,clock1=phiu+sign*L*phisu/5,
                clock2=phiu+sign*2*L*phisu/5+L.square()*phissu/20,
                z=P[2],height0=zs,height1=zs+sign*L*zss/31)


def main():
    parser=argparse.ArgumentParser()
    for name in ("scripts","ramp","coast","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--cells",type=int,default=2048)
    args=parser.parse_args()
    if args.cells<256 or args.cells%4:raise ValueError("Use a multiple of four")
    tick=time.monotonic()
    cp=args.scripts/"6a65-m12-r137-continuous-domain.py"
    fp=args.scripts/"6a65-geometry-final-ramp-port-certificate.py"
    cert=load(cp,"polar_cert");p=load(fp,"polar_port")
    if sha(args.ramp)!=p.RAMP_SHA or sha(args.coast)!=p.COAST_SHA:raise ValueError("Wrong masters")
    I=cert.I; pi=cert.pi_interval(); J=p.Series(cert)
    arc=I(p.ARC_LO,p.ARC_HI)
    scale=I(1-Q("2.453e-17"),1+Q("2.453e-17"))
    a=arc*scale
    with np.load(args.coast) as z:
        co,si=p.real_curve(z["curve_modes"],z["curve_coefficients"])
        v,length=[I(Q.from_float(float(z[key]))) for key in ("v","length")]
    center=[I(x) for x in co[0]];curve=p.Fourier(co,si,cert,max_order=8)
    cache={}
    def phase(i,n):
        k=i%(2*n)
        if (k,n) not in cache:cache[(k,n)]=cert.sincos(pi*Q(k if k<=n else k-2*n,n))
        return cache[(k,n)]
    n=args.cells
    half=pi/n
    L0=Q(.7956739498716915)
    b=Q(.1815625);S=Q(float(b)+float(L0))
    L=I(min(L0,S-b),max(L0,S-b))
    right=RightPort(cert)
    hull={};trace=hashlib.sha256()
    leafcounts={}
    def record(j,count,side,row):
        if side not in hull:hull[side]=row.copy()
        else:
            for k,y in row.items():hull[side][k]=cert.hull(hull[side][k],y)
        trace.update(repr((j,count,side,[(k,y.lo,y.hi) for k,y in row.items()])).encode()+b"\n")
        label=f"{side}-{count}"
        leafcounts[label]=leafcounts.get(label,0)+1
    def visit(j,count):
        sample=curve.point(j,count,phase,order=7)
        half=pi/count
        box=curve.box(sample,half,order=6)
        port=left_port(cert,J,curve.series(box,order=6),arc,a,scale,v,length,center)
        row=budgets(port,L,"left")
        sn,cs=phase(2*j+1,count)
        err=I.raw(-half.hi,half.hi)
        row["positiveRadialProjection"]=port["P"][0]*(cs+err)+port["P"][1]*(sn+err)
        if count<16*n and min(row[k].lo for k in ("clock0","clock1","clock2","positiveRadialProjection"))<=cert.SCALE//10:
            visit(2*j,2*count)
            visit(2*j+1,2*count)
        else:
            record(j,count,"left",row)
    for j in range(n):
        visit(j,n)
        # The R205 horizontal coordinate reflections preserve all controls.
        if j<n//4:
            sn0,cs0=phase(2*j,n);sn1,cs1=phase(2*j+2,n)
            su=I.raw(max(0,sn0.lo),min(cert.SCALE,sn1.hi))
            cu=I.raw(max(0,cs1.lo),min(cert.SCALE,cs0.hi))
            record(j,n,"right",budgets(right.port(su,cu),L,"right"))
    left,right=hull["left"],hull["right"]
    mass=32*(right["z"]-left["z"])/L-sum(data[k] for data in (left,right) for k in ("height0","height1"))
    allclock=min(row[k].lower() for row in (left,right) for k in ("clock0","clock1","clock2"))
    out=dict(schema="actual-accurate-Gamma95-and-R205-whole-polar-control-budgets-v1",
             scripts={v.name:sha(v) for v in (Path(__file__),cp,fp)},
             rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),cells=n,leafCounts=leafcounts,integerBits=cert.BITS,
             arc=arc.display(),scale=scale.display(),L=L.display(),nominalL=str(L0),
             literalS=str(S),literalB=str(b),rowSHA256=trace.hexdigest(),
             exactHull={side:{k:v.display() for k,v in row.items()} for side,row in hull.items()},
             freeControlMass=mass.display(),minimumClockControl=str(allclock),seconds=time.monotonic()-tick)
    with args.output.open("x") as f:json.dump(out,f,indent=2);f.write("\n")
    print(json.dumps({s:{k:y.display()["display"] for k,y in q.items()} for s,q in hull.items()}),flush=True)
    print("mass",mass.display(),"min clock",float(allclock),flush=True)
    if min(allclock,mass.lower(),left["positiveRadialProjection"].lower(),left["height0"].lower(),left["height1"].lower())<=0:
        raise ArithmeticError("Complete positivity estimates did not close")


if __name__=="__main__":
    main()
