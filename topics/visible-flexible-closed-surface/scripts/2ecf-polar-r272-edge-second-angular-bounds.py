#!/usr/bin/env python3
"""Absolute global second angular jets at both nonpolynomial R272 physical ports."""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod);return mod
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def left_series(J,g,arc,a,v,length):
    # Differentiate the R265 true physical frame twice in the outgoing material angle.
    inlet=J.inlet(g,arc,a,v);d=inlet['V'];iq=J.inv(inlet['q'])
    T=J.vscale(iq,J.vderivative(g));N=J.cross(d,T);rate=J.scale(arc,iq)
    Tu=J.vscale(rate,J.vderivative(T));du=J.vscale(rate,J.vderivative(d))
    n=J.scale(1/a,J.dot(Tu,N));k=J.mul(J.dot(du,N),J.inv(J.dot(Tu,N)))
    con=lambda x:J.constant(x,len(k));k2=J.mul(k,k)
    b=J.add(con(1),k2);r0=a/v;D0=length*(2*r0+length)
    w=J.scale(D0,J.inv(J.add(con(r0),J.sqrt(J.add(con(r0.square()),J.scale(D0,b))))))
    H=J.add(con(a),J.scale(v,J.mul(w,b)))
    D=J.add(con(a),J.mul(w,J.sub(J.scale(v,b),J.mul(rate,J.derivative(k)))))
    outgoing=J.mul(rate,J.mul(H,J.inv(D)))
    Du=lambda vec:J.vscale(outgoing,J.vderivative(vec))
    f=a+v*length;cs=J.scale(v/f,J.add(con(r0),w));sn=J.scale(v/f,J.mul(k,w))
    V=J.vadd(J.vscale(cs,d),J.vneg(J.vscale(sn,T)));E=J.vadd(J.vscale(sn,d),J.vscale(cs,T))
    A=J.vscale(J.scale(a**3/f.square(),J.mul(n,J.mul(k2,J.inv(D)))),N)
    return [Du(J.vscale(con(f),E)),Du(Du(V)),Du(Du(A))]
def main():
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--cells',type=int,default=512);a=p.parse_args()
    c=load(a.scripts/'6a65-m12-r137-continuous-domain.py','r272_coast_fixed');ff=load(a.scripts/'6a65-geometry-final-ramp-port-certificate.py','r272_native_series')
    assert sha(a.ramp)==ff.RAMP_SHA and sha(a.coast)==ff.COAST_SHA
    I=c.I;J=ff.Series(c);arc=I(ff.ARC_LO,ff.ARC_HI);e=F('2.453e-17');rad=arc*I(1-e,1+e)
    with np.load(a.coast) as f:co,si=ff.real_curve(f['curve_modes'],f['curve_coefficients']);v,ell=[I(F(float(f[k]))) for k in ('v','length')]
    curve=ff.Fourier(co,si,c,12);n=a.cells;pi=c.pi_interval();half=pi/n;ph={}
    def phase(i,N):
        i%=2*N
        if (i,N) not in ph:ph[i,N]=c.sincos(pi*F(i if i<=N else i-2*N,N))
        return ph[i,N]
    m=[[F(0)]*3 for j in range(3)]
    for i in range(n):
        q=curve.point(i,n,phase,order=10);g=curve.box(q,half,order=9)
        rows=left_series(J,curve.series(g,9),arc,rad,v,ell)
        for j,row in enumerate(rows):
            for d,vec in enumerate(row):m[j][d]=max(m[j][d],F(vec[0].absupper(),c.SCALE))
    # Right true profile S9 is clipped C4. In differentiating C,H, the material chain uses |y'|,|y''|<=.801.
    # |S9'|<=630/256, |S9''|<=2520/64, |S9'''|<=7560/16+15120/64, by the factored expressions.
    A=F('.875');L=F('.45999');u=F('.801')
    k=A/L*630/256;kp=A/L**2*2520/64;kpp=A/L**3*(F(7560,16)+F(15120,64))
    # For P,V=-F_r,A=F_rr, both horizontal and vertical trig components obey the same absolute envelope.
    rP=u+u*u*k
    rV=1+3*u*k+u*u*(kp+k*k)
    rA=4*k+5*u*(kp+k*k)+u*u*(kpp+3*k*kp+k**3)
    out=dict(schema='two-R272-physical-ports-new-second-angular-absolute-bounds-v1',entrySHA256=sha(__file__),
        rampSHA256=sha(a.ramp),coastSHA256=sha(a.coast),nativeClosedCells=n,
        left=[[str(x) for x in row] for row in m],right=[[str(x)]*3 for x in (rP,rV,rA)])
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print([[float(x) for x in row] for row in m],list(map(float,(rP,rV,rA))))
if __name__=='__main__':main()
