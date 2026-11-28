#!/usr/bin/env python3
"""Prove all nine terminal trace differences from small exact Fourier compatibility residuals."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);o=importlib.util.module_from_spec(sp);sys.modules[n]=o;sp.loader.exec_module(o);return o
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(args):
    start=time.monotonic();hpath=Path(__file__).parent;s=args.scripts
    a=load(hpath/"2ecf-strong-stadium-terminal-algebra.py","stadium_terminal_exact_products")
    native=load(hpath/"2ecf-strong-stadium-native-ramp-gram.py","stadium_terminal_model")
    gram=load(s/"6a65-geometry-ramp-native-gram-certificate.py","stadium_terminal_gram")
    pp=load(s/"6a65-geometry-final-ramp-port-certificate.py","stadium_terminal_Fourier")
    cert=load(s/"6a65-m12-r137-continuous-domain.py","stadium_terminal_int")
    inv=json.loads(args.inverse.read_text());src=json.loads(args.source.read_text())
    if (inv["actualRamp"]!=sha(args.ramp) or inv["actualCoast"]!=sha(args.coast) or src["ramp"]!=sha(args.ramp)
            or src["coast"]!=sha(args.coast) or inv["entry"]!=sha(hpath/"2ecf-strong-stadium-terminal-speed-inverse.py")):
        raise ValueError("Immutable native support and its actual certified arc inverse required")
    m=native.model_for(gram,src,args.ramp);I=cert.I;S=pp.Series(cert)
    with np.load(args.coast) as d:
        co,si=pp.real_curve(d["curve_modes"],d["curve_coefficients"]);f0=Q(float(d["exact_target_radius"]))
    arc=I(*map(Q,inv["arc"]));v=I(m.v);lam=I(f0)/arc
    P,V,A,R=a.setup(gram,pp,m,co,si,f0)
    pbox=a.spectral_box(P,pp,cert,95,6);vbox=a.spectral_box(V,pp,cert,args.old_cut,5);abox=a.spectral_box(A,pp,cert,args.old_cut,4)
    Rkeys=("Rt","Rn","Rl","At","Ad","Ra")
    rbox=[a.spectral_box([R[q] for q in Rkeys[j:j+3]],pp,cert,args.res_cut,4) for j in (0,3)]
    def vector(d):return [[row[i]/math.factorial(j) for j,row in enumerate(d)] for i in range(len(d[0]))]
    def scalar_vec_norm(data,j):return pp.upq(sum((Q(d[j].absupper(),cert.SCALE)*math.factorial(j) for d in data),Q(0)))
    mult=S.mul;add=S.add;sub=S.sub;sca=S.scale
    div=lambda f,g:mult(f,S.inv(g));dot=S.dot
    def vsub(a,b):return [sub(x,y) for x,y in zip(a,b)]
    pi=cert.pi_interval();cache={}
    def phase(k,N):
        key=(int(k%(2*N)),N)
        if key not in cache:cache[key]=cert.sincos(pi*Q(key[0] if key[0]<=N else key[0]-2*N,N))
        return cache[key]
    bounds={k:[Q(0)]*4 for k in ("P","V","A")}
    dev={k:[Q(0)]*4 for k in ("P","V","A")}
    # The same-angle position difference is an exact Fourier expression plus a small normalization factor.
    oldP=[a.Poly(q[0],q[1],m.input_bits) for q in m.port(64)[0]]
    for j in range(4):
        bounds["P"][j]=pp.upq(sum((x-y).norm(j) for x,y in zip(P,oldP))+max(abs(lam.lower()-1),abs(lam.upper()-1))*sum(x.norm(j) for x in P))
        dev["P"][j]=pp.upq(lam.upper()*sum(x.norm(j) for x in P))
    cells=0;hashes=hashlib.sha256()
    def visit(k,n,depth):
        nonlocal cells
        g=vector(pbox(k,n,phase,pi));oldV=vector(vbox(k,n,phase,pi));oldA=vector(abox(k,n,phase,pi))
        residual=[i for f in rbox for i in vector(f(k,n,phase,pi))]
        RT,RN,RL,AT,AD,RA=residual
        try:
            p=S.vderivative(g);q=S.vderivative(p);E=dot(p,p);J=S.sqrt(E);cross=S.cross(p,q);H=S.sqrt(dot(cross,cross))
            T=S.vscale(S.inv(J),p);B=dot(p,q)
            nf=S.vscale(div(J,H),vsub(q,S.vscale(div(B,E),p)));bf=S.vscale(S.inv(H),cross)
            b=sca(-v/arc,div(mult(E,J),H));cz=S.sqrt(sub(S.constant(1,len(b)),mult(b,b)))
            d=S.vadd(S.vscale(b,nf),S.vscale(cz,bf));N=S.cross(d,T)
            z0=dot(oldV,bf)
            if z0[0].lo<=0:raise ArithmeticError("Wrong director component")
            av=div(RT,J)
            bv=div(add(sca(1/I(f0),RN),sca(v*(1/arc-1/I(f0)),mult(E,E))),mult(J,H))
            cv=div(sub(sub(sub(RL,mult(av,av)),sca(2,mult(b,bv))),mult(bv,bv)),add(cz,z0))
            ev=S.vadd(S.vadd(S.vscale(av,T),S.vscale(bv,nf)),S.vscale(cv,bf))
            w0=S.cross(oldV,p);ww=S.cross(d,p);ew=S.cross(ev,p)
            aw=dot(oldA,w0);qw=dot(q,w0);Vp=S.vderivative(oldV);ww0=dot(Vp,w0)
            ae=dot(oldA,ew);qe=dot(q,ew);eh=add(dot(S.vderivative(ev),ww),dot(Vp,ew))
            residualA=add(RA,sca(lam-1,mult(aw,qw)))
            residualA=add(residualA,sca(lam,sub(sub(mult(ae,qe),mult(ae,qw)),mult(aw,qe))))
            residualA=add(residualA,sub(sca(2,mult(ww0,eh)),mult(eh,eh)))
            normalDen=dot(q,ww)
            if normalDen[0].lo<=0:raise ArithmeticError("No oriented denominator")
            aa=div(AT,J);ba=sub(AD,dot(oldA,ev));ca=div(residualA,sca(lam,mult(normalDen,J)))
            ea=S.vadd(S.vadd(S.vscale(aa,T),S.vscale(ba,d)),S.vscale(ca,N))
        except ArithmeticError:
            if depth>=7:raise
            visit(2*k,2*n,depth+1);visit(2*k+1,2*n,depth+1);return
        vv=[scalar_vec_norm(ev,j) for j in range(4)];aaa=[scalar_vec_norm(ea,j) for j in range(4)]
        if (vv[0]>Q("3e-8") or aaa[0]>Q(".00003")) and depth<2:
            visit(2*k,2*n,depth+1);visit(2*k+1,2*n,depth+1);return
        for key,err,old in (("V",vv,oldV),("A",aaa,oldA)):
            for j in range(4):
                bounds[key][j]=max(bounds[key][j],err[j]);dev[key][j]=max(dev[key][j],scalar_vec_norm(old,j)+err[j])
        cells+=1;hashes.update(repr((k,n,vv,aaa)).encode())
    for k in range(args.cells):
        visit(k,args.cells,0)
        if k%128==127:
            print(json.dumps(dict(base=k+1,leaves=cells,V=[float(x) for x in bounds["V"]],A=[float(x) for x in bounds["A"]])),flush=True)
    e,ep,epp=[Q(inv[k]) for k in ("thetaUpper","firstMinusOne","secondUpper")]
    trace=[]
    for k in ("P","V","A"):
        o=bounds[k];d=dev[k]
        trace.append([pp.upq(o[0]+d[1]*e),pp.upq(o[1]+d[2]*e+d[1]*ep),pp.upq(o[2]+d[3]*e+d[2]*(2*ep+ep**2)+d[1]*epp)])
    out=dict(schema="true-normal-angle-terminal-directed-polynomial-compatibility-trace-v1",entry=sha(__file__),
        exactProducts=sha(a.__file__),native=sha(native.__file__),ramp=sha(args.ramp),coast=sha(args.coast),
        inverse=sha(args.inverse),materialOrdersInNativeCentralAngle=[[str(v) for v in row] for row in trace],
        sameAngle={key:list(map(str,v)) for key,v in bounds.items()},trueDerivatives={key:list(map(str,v)) for key,v in dev.items()},
        original384AllModes=True,residualLowCut=args.res_cut,oldLowCut=args.old_cut,base=args.cells,leaves=cells,
        exactPolynomialResidualDegrees={key:z.d for key,z in R.items()},leafSHA256=hashes.hexdigest(),seconds=time.monotonic()-start)
    with args.output.open("x") as f:json.dump(out,f,indent=2);f.write("\n")
    print(json.dumps(dict(trace=[[float(v) for v in row] for row in trace],seconds=out["seconds"])),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for n in ("scripts","source","ramp","coast","inverse","output"):ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--cells",type=int,default=1024);ap.add_argument("--old-cut",type=int,default=128);ap.add_argument("--res-cut",type=int,default=192)
    run(ap.parse_args())
