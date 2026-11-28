#!/usr/bin/env python3
"""Bind true gap-.92 Gamma95 characteristic outlet P,V,A and material derivatives to the stored physical Fourier trace."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
for v in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[v]='1'
import numpy as np
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def outlet(C,J,g,arc,a,v,sig,center,n):
    inlet=J.inlet(g,arc,a,v);d=inlet['V'];speed=inlet['q']
    iq=J.inv(speed);T=J.vscale(iq,J.vderivative(g));N=J.cross(d,T)
    rate=J.scale(arc,iq);dt=lambda h:J.mul(rate,J.derivative(h))
    Tu=J.vscale(rate,J.vderivative(T));du=J.vscale(rate,J.vderivative(d))
    nn=J.scale(1/a,J.dot(Tu,N));k=J.mul(J.dot(du,N),J.inv(J.dot(Tu,N)))
    c=lambda x:J.constant(x,len(k));k2=J.mul(k,k);ba=J.add(c(1),k2)
    r0=a/v;delta=sig*(2*r0+sig)
    w=J.scale(delta,J.inv(J.add(c(r0),J.sqrt(J.add(c(r0.square()),J.scale(delta,ba))))))
    H=J.add(c(a),J.scale(v,J.mul(w,ba)));D=J.add(c(a),J.mul(w,J.sub(J.scale(v,ba),dt(k))))
    outer=J.mul(rate,J.mul(H,J.inv(D)));f=a+v*sig
    cosb=J.scale(v/f,J.add(c(r0),w));sinb=J.scale(v/f,J.mul(k,w))
    V=J.vadd(J.vscale(cosb,d),J.vneg(J.vscale(sinb,T)))
    start=[J.add(c(t),J.scale(a/arc,J.sub(z,c(t)))) for t,z in zip(center,g)]
    P=J.vadd(start,J.vscale(w,J.vadd(d,J.vneg(J.vscale(k,T)))))
    lam=J.scale(a*a*a/f.square(),J.mul(nn,J.mul(k2,J.inv(D))));A=J.vscale(lam,N)
    result=[]
    for source in (P,V,A):
        jets=[]
        for j in range(n+1):
            assert min(map(len,source))>0
            jets.append([z[0] for z in source])
            if j<n:source=J.vscale(outer,J.vderivative(source))
        result.append(jets)
    return result,speed,outer[0],w[0]*k[0]/(r0+w[0])
def run(a):
    start=time.monotonic();cp=a.scripts/'6a65-m12-r137-continuous-domain.py';fp=a.scripts/'6a65-geometry-final-ramp-port-certificate.py';C=module(cp,'gamma95_fixed');F=module(fp,'gamma95_fourier')
    I=C.I;J=F.Series(C);raw=json.load(a.primitive.open());assert raw['source']['coastMasterSHA256']==sha(a.coast)
    def from_report(k):d=raw[k];return I(Q(d['lo']),Q(d['hi']))
    aa=from_report('exactTargetRadius');arc=from_report('accurateRawArc')
    with np.load(a.coast) as z:
        c,s=F.real_curve(z['curve_modes'],z['curve_coefficients']);v=I(Q(float(z['v'])));sig=I(Q(float(z['length'])))
    native=F.Fourier(c,s,C,max_order=13);center=[I(y) for y in c[0]]
    rs=np.load(a.field)['coeff'][0];M=rs.shape[1];QQ=2**58;VV=2**58;proxy=[];mag=[]
    for dr in range(3):
        prow=[];mrow=[]
        for d in range(3):
            cr=[round(Q(x.real)*QQ) for x in rs[dr,:,d]];ci=[round(Q(x.imag)*QQ) for x in rs[dr,:,d]]
            prow.append([cr,ci]);mrow.append([sum((abs(x)+abs(y)+1)*k**j for k,(x,y) in enumerate(zip(cr,ci))) for j in range(6)])
        proxy.append(prow);mag.append(mrow)
    pi=C.pi_interval();N=a.cells;h=pi/N;ph={}
    def phase(k,n):
        i=k%(2*n);key=(i,n)
        if key not in ph:ph[key]=C.sincos(pi*Q(i if i<=n else i-2*n,n))
        return ph[key]
    def scalar_atan(x):
        assert x.absupper()<C.SCALE//12
        y=x.square();p=x;total=p
        for z in range(1,8):
            p=-p*y;total+=p/(2*z+1)
        err=C.upper_i(I.raw(0,x.absupper())*I.raw(0,x.absupper()).square().square().square().square()/17)
        return total+I.raw(-err.hi,err.hi)
    integral=I(0);delta_max=[[0]*3 for _ in range(3)];largest_output_angle=I(0);arc_error=I(0)
    def power(z,n):
        s=I(1)
        for _ in range(n):s=s*z
        return s
    for idx in range(N):
        cp=native.point(idx,N,phase,order=12);cb=native.box(cp,h,order=10)
        point,qs,_,at=outlet(C,J,native.series(cp,order=12),arc,aa,v,sig,center,3)
        box,qb,rate,_=outlet(C,J,native.series(cb,order=10),arc,aa,v,sig,center,4)
        # Exact fourth-order Taylor theorem for the speed primitive about this cell center.
        rem=C.upper_i(power(h,5)*I.raw(0,qb[4].absupper())/5)
        pre=h*qs[0]-power(h,2)*qs[1]/2+power(h,3)*qs[2]/3-power(h,4)*qs[3]/4+I.raw(-rem.hi,rem.hi)
        uc=(integral+pre)/arc-scalar_atan(at)/v
        integral+=2*(h*qs[0]+power(h,3)*qs[2]/3+I.raw(-rem.hi,rem.hi))
        rad=C.upper_i(h/rate);largest_output_angle=I.raw(0,max(largest_output_angle.hi,rad.hi))
        mid=(uc.lower()+uc.upper())/2;urad=(uc.upper()-uc.lower())/2
        arc_error=I.raw(0,max(arc_error.hi,I(urad).hi))
        j0=round(float(mid)/(2*math.pi));red=I(mid)-2*j0*pi;assert red.absupper()<4*C.SCALE
        sn,cs=C.sincos(red);c0=round((cs.lower()+cs.upper())*VV/2);s0=round((sn.lower()+sn.upper())*VV/2)
        assert max(abs(Q(c0,VV)-cs.lower()),abs(Q(c0,VV)-cs.upper()),abs(Q(s0,VV)-sn.lower()),abs(Q(s0,VV)-sn.upper()))<Q(1,VV)
        phases=[];re=VV;im=0
        for k in range(M):
            phases.append((re,im));re,im=(re*c0-im*s0+VV//2)//VV,(re*s0+im*c0+VV//2)//VV
        for dr in range(3):
            for d in range(3):
                cr,ci=proxy[dr][d];errs=[]
                for j in range(4):
                    z0=0
                    for k,(cx,cy) in enumerate(phases):
                        x,y=((cx,cy),(-cy,cx),(-cx,-cy),(cy,-cx))[j%4]
                        z0+=(cr[k]*x-ci[k]*y)*k**j
                    # Each complex point recurrence has norm error <= 4*k/VV; angle-center uncertainty adds k*urad.
                    qe=Q(mag[dr][d][j+1],QQ)*(urad+Q(4,VV))+Q(sum(k**j for k in range(M)),QQ)
                    delta0=point[dr][j][d]-I(Q(z0,QQ*VV)-qe,Q(z0,QQ*VV)+qe)
                    errs.append(I.raw(0,delta0.absupper()))
                m4=I.raw(0,box[dr][4][d].absupper())+I(Q(mag[dr][d][4],QQ))
                for j in range(3):
                    bound=sum((power(rad,i-j)*errs[i]/math.factorial(i-j) for i in range(j,4)),I(0))+power(rad,4-j)*m4/math.factorial(4-j)
                    delta_max[dr][j]=max(delta_max[dr][j],bound.hi)
        if (idx+1)%128==0:print(idx+1,[[round(t/C.SCALE,10) for t in r] for r in delta_max],flush=True)
    assert (integral-2*pi*arc).lo<=0<=(integral-2*pi*arc).hi
    out=dict(entrySHA256=sha(__file__),fieldSHA256=sha(a.field),coastSHA256=sha(a.coast),originalAccuratePrimitiveSHA256=sha(a.primitive),trueEndpoint='Gamma95 normalized curve; U_out=integral(q)/arc-atan(wk/(r0+w))/v; physical P,V,A from actual inlet and characteristic',nativeClosedCells=N,storedFourierModes=M,accurateMinusStoredPhysicalDerivativeMaxUpper=[[str(Q(x,C.SCALE)) for x in y] for y in delta_max],maxMaterialCenterRadius=str(arc_error.upper()),maxWholeUHalfwidth=str(largest_output_angle.upper()),closedPrimitiveTrue=True,seconds=time.monotonic()-start)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','field','coast','primitive','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--cells',type=int,default=2048);run(p.parse_args())
