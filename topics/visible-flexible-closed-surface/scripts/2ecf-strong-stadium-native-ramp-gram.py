#!/usr/bin/env python3
"""Exact Fourier-Bernstein Gram and local physical shape on a support-defined native H65 ramp."""
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
    spec=importlib.util.spec_from_file_location(n,p);o=importlib.util.module_from_spec(spec);sys.modules[n]=o;spec.loader.exec_module(o);return o


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def near(q,b):
    S=1<<b
    return (2*q.numerator*S+q.denominator)//(2*q.denominator)


def model_for(gram,src,ramp):
    class Model(gram.ActualRamp):
        def __init__(self):
            with np.load(ramp) as a:
                self.raw=a["coefficients"].copy();self.wave=a["wave"].copy();self.sx=a["sx"].copy()
                self.c,self.ramp,self.v,self.a0=[Q(float(a[k])) for k in ("centralLength","ramp","v","a0")]
            self.degree=384;self.index={int(k):i for i,k in enumerate(self.wave)}
            if self.raw.shape!=(65,768,3,3) or set(self.index)!=set(range(-384,384)):raise ValueError("Actual entire H65 full native Fourier required")
            self.input_bits=max(220,max(float(x).as_integer_ratio()[1].bit_length() for a in (self.raw.real,self.raw.imag) for x in a.flat))
            self.port_cache={}
            ex=src["exact"];self.p=ex["power"];self.r=Q(ex["offset"])
            self.rho=[Q(a) for a in ex["rhoEvenCos"]];h=[Q(a) for a in ex["supportEvenCos"]]
            self.rhomax=Q(ex["rhoMax"])
            H={0:h[0]}
            for j,a in enumerate(h[1:],1):H[2*j]=H[-2*j]=a/2
            # Complex planar P=e^{it}(h+ih'); h and its Fourier coefficients are real/even.
            Z={k+1:(1-k)*a for k,a in H.items()}
            D=self.degree;P=[[[[0]*(2*D+1) for _ in range(2)] for _ in range(3)] for _ in range(3)]
            self.first_error=[Q(0)]*3
            for k in range(-D,D+1):
                xp=(Z.get(k,0)+Z.get(-k,0))/2 if k in Z or -k in Z else Q(0)
                yp=(Z.get(-k,0)-Z.get(k,0))/2 if k in Z or -k in Z else Q(0)
                for comp,imag,value in ((0,0,xp),(1,1,yp)):
                    rounded=near(value,self.input_bits);P[0][comp][imag][D+k]=rounded
                    for d in range(3):self.first_error[d]+=abs(value-Q(rounded,1<<self.input_bits))*abs(k)**d
            P[0][2][0][D]=gram.scaled(self.c,self.input_bits);P[1][2][0][D]=1<<self.input_bits
            self.origin=P
            hhat={0:self.rho[0]}
            for j,a in enumerate(self.rho[1:],1):hhat[2*j]=hhat[-2*j]=a/2
            self.rho2={}
            for i,a in hhat.items():
                for j,b in hhat.items():self.rho2[i+j]=self.rho2.get(i+j,Q(0))+a*b
        def port(self,node):
            if node==0:return self.origin
            return super().port(node)
    return Model()


def formula(gram,C,bits,L,s0,m,cut):
    T=gram.radial_t(C);U=gram.angular(C,m.degree)
    low=list(range(m.degree-cut,m.degree+cut+1));high=list(range(m.degree-cut))+list(range(m.degree+cut+1,2*m.degree+1))
    a,b=gram.select(T,low),gram.select(U,low)
    peak=max(abs(x).bit_length() for poly in (a,b) for row in poly for pair in row for part in pair for x in part)
    pbits=2*peak+(12*3*max(len(a),len(b))*(2*cut+1)).bit_length()+3
    E=gram.packed_gram(a,a,pbits,True);F=gram.packed_gram(a,b,pbits);G=gram.packed_gram(b,b,pbits,True)
    center=2*cut;E[0][0][center]-=gram.scaled(L*L,2*bits)
    q,qb,qe,qu=gram.target_ratio(s0,L,m.ramp,m.v,(Q(1),Q(1)))
    sq=[sum(q[j]*q[i-j] for j in range(max(0,i-10),min(10,i)+1)) for i in range(21)]
    rho_bits=220;rb={k:near(x,rho_bits) for k,x in m.rho2.items()}
    rhoerr=sum(abs(x-Q(rb[k],1<<rho_bits)) for k,x in m.rho2.items())
    gb=max(2*bits,2*qb+rho_bits)
    G=[[[x<<(gb-2*bits) for x in part]for part in row] for row in G]
    G.extend([[[0]*len(G[0][0]) for _ in range(2)] for _ in range(21-len(G))])
    for i in range(21):
        for k,z in rb.items():G[i][0][center+k]-=sq[i]*z*(1<<(gb-2*qb-rho_bits))
    ms=gram.vector_bernstein_l1(T,bits,L,indices=low)/L
    ds=gram.vector_bernstein_l1(T,bits,L,indices=high)/L
    mu=gram.vector_bernstein_l1(U,bits,L,indices=low)
    du=gram.vector_bernstein_l1(U,bits,L,indices=high)
    eb=gram.bernstein_l1(E,2*bits)/L**2+2*ms*ds+ds**2
    fb=gram.bernstein_l1(F,2*bits)/L+ms*du+mu*ds+ds*du
    gb0=gram.bernstein_l1(G,gb)+2*mu*du+du**2+(qu[0]+qe[0])**2*rhoerr+qe[0]*(2*qu[0]+qe[0])*m.rhomax**2
    return eb,fb,gb0,ms+ds,mu+du


def run(args):
    from copy import copy
    start=time.monotonic();s=args.scripts
    gram=load(s/"6a65-geometry-ramp-native-gram-certificate.py","stadium_native_algebra")
    curv=load(s/"6a65-geometry-ramp-native-curvature-certificate.py","stadium_native_curvature")
    cert=load(s/"6a65-m12-r137-continuous-domain.py","stadium_native_integer")
    terminal=load(s/"6a65-geometry-final-ramp-cell-certificate.py","stadium_native_end")
    src=json.loads(args.source.read_text())
    if src["ramp"]!=sha(args.ramp) or src["coast"]!=sha(args.coast):raise ValueError("Actual matching source required")
    m=model_for(gram,src,args.ramp)
    with np.load(args.coast) as z: f0=Q(float(z["exact_target_radius"]))
    correction=abs(f0-(1+m.v*m.ramp/2))
    I=cert.I
    class NativeCell(curv.Cell):
        def geometry(self,index,count,lo,hi):
            q=self.jets(index,count,lo,hi)
            for i,j,k in ((1,0,"S"),(0,1,"U"),(2,0,"SS"),(1,1,"SU"),(0,2,"UU")):
                err=self.jet_error.get((i,j),0)
                if err:q[k]=[v+I(-err,err) for v in q[k]]
            es=I(1-self.epsE,1+self.epsE);fs=I(-self.epsF,self.epsF)
            sn,_=self.w.phase(2*index+1,count);delta=self.w.pi/count;sn+=I.raw(-delta.hi,delta.hi)
            rho=I(m.r)+(m.rhomax-m.r)*sn.square()**m.p
            rho=I.raw(max(I(m.r).lo,rho.lo),min(I(m.rhomax).hi,rho.hi))
            gs=self.ratio(lo,hi).square()*rho.square()+I(-self.epsG,self.epsG)
            det=es*gs-fs.square()
            if det.lo<=0:raise ArithmeticError("No determinant lower bound")
            root=det.sqrt();N=cert.scale(1/root,cert.cross(q["S"],q["U"]))
            l,v,n=[cert.dot(N,q[k]) for k in ("SS","SU","UU")]
            aa=l/es;bb=(v-fs*aa)/root;dd=(es*n-2*fs*v+fs.square()*aa)/det
            return (I.raw((aa+dd).absupper(),(aa+dd).absupper())+((aa-dd).square()+4*bb.square()).sqrt())/2,root
    rr=[]
    if args.end_trace:
        tr=json.loads(args.end_trace.read_text())
        if tr["ramp"]!=sha(args.ramp) or tr["coast"]!=sha(args.coast):raise ValueError("Changed exact terminal bound")
    for j in range(args.left,args.right):
        small=copy(m);small.sx=m.sx[j:j+2];small.port=lambda i,j=j:m.port(j+i)
        C,bits,L,s0=small.cell(0)
        eb,fb,gb,ms,mu=formula(gram,C,bits,L,s0,m,args.cutoff)
        errors={}
        if j==0:
            for i in range(3):
                for k in range(3):
                    errors[i,k]=terminal.hermite_norm(gram.H2[0],i)*m.first_error[k]/L**i
        if j==63 and args.end_trace:
            trace=tr["materialOrdersInNativeCentralAngle"]
            for i in range(3):
                for k in range(3):
                    errors[i,k]=sum(L**(d-i)*terminal.hermite_norm(gram.H2[3+d],i)*Q(trace[d][k]) for d in range(3))
        se,ue=errors.get((1,0),0),errors.get((0,1),0)
        eb+=2*ms*se+se**2;fb+=ms*ue+mu*se+se*ue;gb+=2*mu*ue+ue**2
        # Geometry uses original 1+vrJ as its close proxy; the separate target
        # bound below also covers the smooth ramp-to-literal-F0 correction.
        proxy=gb
        gb+=m.rhomax**2*correction*(2*(1+m.v*m.ramp/2)+correction)
        fmin=1-correction
        metric=max(eb+fb/(fmin*m.r),gb/(fmin*m.r)**2+fb/(fmin*m.r))
        report=dict(exactEllipticArcRadiusInterval=["1","1"],rows=[dict(index=0,completeRawNativeGramBounds=dict(
            Eminus1=gram.upper(eb),F=gram.upper(fb),GminusTarget=[gram.upper(proxy)]))])
        whole=curv.WholeDomain(gram,cert,small,report,args.cutoff)
        cell=NativeCell(whole,0);cell.jet_error=errors
        maxk=Q(0);minarea=None;leaves=0
        def do(k,N,a,b,level):
            nonlocal maxk,minarea,leaves
            kv,area=cell.geometry(k,N,a,b);bound=kv.upper()
            if bound>args.kcap and level<args.depth:
                if level%3!=2:do(2*k,2*N,a,b,level+1);do(2*k+1,2*N,a,b,level+1)
                else:
                    mid=(a+b)/2;do(k,N,a,mid,level+1);do(k,N,mid,b,level+1)
                return
            leaves+=1;maxk=max(bound,maxk);minarea=area.lower() if minarea is None else min(minarea,area.lower())
        for k in range(args.angular):do(k,args.angular,Q(0),Q(1),0)
        row=dict(index=j,left=str(s0),right=str(s0+L),metric=str(metric),curvature=str(maxk),area=str(minarea),leaves=leaves,
            endpoint="new exact physical Gamma95" if j==63 and args.end_trace else "raw polynomial")
        rr.append(row)
        print(json.dumps(dict(cell=j,metric=float(metric),curvature=float(maxk),leaves=leaves)),flush=True)
    out=dict(schema="true-support-native-full-H65-Fourier-Bernstein-Gram-and-curvature-v1",entry=sha(__file__),
        ramp=sha(args.ramp),coast=sha(args.coast),support=src["exact"],integer=sha(cert.__file__),gram=sha(gram.__file__),
        curvature=sha(curv.__file__),firstNodeError=[str(q) for q in m.first_error],matchedAngularTarget=True,
        terminalTrace=sha(args.end_trace) if args.end_trace else None,rows=rr,seconds=time.monotonic()-start)
    with args.output.open("x") as f:json.dump(out,f,indent=2);f.write("\n")


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for name in ("scripts","source","ramp","coast","output"):ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--cutoff",type=int,default=112);ap.add_argument("--angular",type=int,default=32)
    ap.add_argument("--kcap",type=Q,default=Q(8));ap.add_argument("--depth",type=int,default=7)
    ap.add_argument("--left",type=int,default=0);ap.add_argument("--right",type=int,default=64);ap.add_argument("--end-trace",type=Path)
    args=ap.parse_args()
    if not 0<=args.left<args.right<=64:raise ValueError("Physical node range required")
    run(args)
