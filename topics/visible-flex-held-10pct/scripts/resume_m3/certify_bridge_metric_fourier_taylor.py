#!/usr/bin/env python3
"""Continuous Gram bounds for the M24 bridge's declared numerical jet oracle.

Fixed mean nodes, exact binary polynomial coefficients, analytic endpoint
extension, and real trigonometry are explicit. The background radius is the
finite GL real function but its supplied radial slope is -sin(phi). Thus a
separate C2-object/target-metric transfer is REQUIRED. This is not by itself a
closed-surface certificate, nor does it change any original solver gate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,bisect,hashlib,json,math,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

import certify_r59_fixed_mean_ranges as m
I=m.I


class D2:
    def __init__(self,v,d=0,d2=0):
        if isinstance(v,D2):self.v,self.d,self.d2=v.v,v.d,v.d2
        else:self.v,self.d,self.d2=I(v),I(d),I(d2)
    def __add__(self,b):
        b=D2(b);return D2(self.v+b.v,self.d+b.d,self.d2+b.d2)
    __radd__=__add__
    def __neg__(self):return D2(-self.v,-self.d,-self.d2)
    def __sub__(self,b):return self+-D2(b)
    def __rsub__(self,b):return D2(b)+-self
    def __mul__(self,b):
        b=D2(b);return D2(self.v*b.v,self.d*b.v+self.v*b.d,
            self.d2*b.v+2*self.d*b.d+self.v*b.d2)
    __rmul__=__mul__
    def inv(self):
        v=1/self.v
        return D2(v,-self.d*v*v,2*self.d*self.d*v*v*v-self.d2*v*v)
    def __truediv__(self,b):return self*D2(b).inv()
    def __rtruediv__(self,b):return D2(b)*self.inv()
    def sq(self):return D2(self.v.sq(),2*self.v*self.d,2*(self.d.sq()+self.v*self.d2))
    def sqrt(self):
        v=self.v.sqrt()
        return D2(v,self.d/(2*v),self.d2/(2*v)-self.d.sq()/(4*v*v*v))
    def sum(self,axis=0):return D2(self.v.sum(axis),self.d.sum(axis),self.d2.sum(axis))
    def item(self,key):return D2(self.v.item(key),self.d.item(key),self.d2.item(key))
    def expand(self):return D2(self.v.expand(),self.d.expand(),self.d2.expand())
    def __pow__(self,n):
        if n==0:return D2(1)
        v=D2(1)
        for _ in range(n):v=v*self
        return v


def trig(x):
    x=D2(x);s,c=m.sincos_i(x.v)
    return D2(s,c*x.d,c*x.d2-s*x.d.sq()),D2(c,-s*x.d,-s*x.d2-c*x.d.sq())


class JetMean(m.MeanVerifier):
    def field(self,s,left,right,order=0):
        mid=(left+right)/2
        idx=min(len(self.xx)-2,bisect.bisect_right(self.xx,mid)-1)
        x=s-I.rational(self.xx[idx]);c=self.pc[idx]
        for _ in range(order):c=m.pder(c)
        return D2(m.poly(c,x)*self.q,m.poly(m.pder(c),x)*self.q,
                  m.poly(m.pder(m.pder(c)),x)*self.q)
    def coefficients(self,s,left,right):return self.field(s,left,right)
    def chart(self,s,left,right):
        # Populate the original exact-rational polynomial cache first.
        super().chart(s,left,right)
        mid=(left+right)/2
        idx=min(len(self.spx)-2,bisect.bisect_right(self.spx,mid)-1)
        origin,c,c1,c2=self.ec[(idx,mid>self.cutoff)]
        x=s-I.rational(origin);c3=m.pder(c2)
        return D2(m.poly(c,x),m.poly(c1,x),m.poly(c2,x)),D2(m.poly(c1,x),m.poly(c2,x),m.poly(c3,x))


def absolute(v):
    return np.maximum(np.abs(v.x[0]),np.abs(v.x[1]))


def l1(v):
    return I(absolute(v)).sum().x[1]


def conv_i(a,b):
    """Real interval convolution with explicit floating dot-product error.

    For n products, gamma_(2n) <= 8(n+1)u here. Positive convolution upper
    bounds divide by 1-gamma. 2^-970 per output covers every subnormal error
    for these admitted lengths; no FFT or unbounded libm is used here.
    """
    n=min(np.size(a.x[0]),np.size(b.x[0]));u=2.**-53
    if not 1<=n<1000000:raise ValueError('Unsupported convolution size')
    g=8*(n+1)*u;tiny=2.**-970
    def pos(x,y):
        z=np.convolve(x,y)
        return m.K.up(m.K.up(z+tiny)/(1-g))
    am=a.x[0]/2+a.x[1]/2;bm=b.x[0]/2+b.x[1]/2
    ar=m.K.up(np.maximum(am-a.x[0],a.x[1]-am))
    br=m.K.up(np.maximum(bm-b.x[0],b.x[1]-bm))
    center=np.convolve(am,bm)
    error=I(pos(np.abs(am),br))+I(pos(ar,np.abs(bm)))+I(pos(ar,br))
    error=error+I(pos(np.abs(am),np.abs(bm)))*g+tiny
    return I(m.K.dn(center-error.x[1]),m.K.up(center+error.x[1]))


def cv(a,b,crop=None):
    z=D2(conv_i(a.v,b.v),conv_i(a.d,b.v)+conv_i(a.v,b.d),
         conv_i(a.d2,b.v)+2*conv_i(a.d,b.d)+conv_i(a.v,b.d2))
    if crop is not None:
        middle=(len(z.v.x[0])-1)//2;z=z.item(slice(middle-crop,middle+crop+1))
    return z


def reverse(z):return z.item(slice(None,None,-1))


def zero(F):
    # K.exact deliberately aliases its two endpoints; it is immutable.
    # These coefficient accumulators are mutable, hence own distinct arrays.
    def pair():return I(np.zeros(2*F+1),np.zeros(2*F+1))
    return D2(pair(),pair(),pair())


def add_at(vec,index,val):
    for name in ('v','d','d2'):
        dst=getattr(vec,name);src=getattr(val,name)
        if np.shares_memory(dst.x[0],dst.x[1]):
            raise ValueError('Mutable interval endpoints must not alias')
        x=dst.item(index)+src
        dst.x[0][index],dst.x[1][index]=x.x


class GramVerifier:
    def __init__(self,mean,order):
        self.mean=mean;self.order=order
        self.F=max(3*mean.M+1,3*order+4)
        self.freq=np.arange(-self.F,self.F+1)
    def evaluate(self,left,right):
        v=self.mean
        s=I(I.rational(left).x[0],I.rational(right).x[1])
        _,mean,root=v.evaluate(left,right)
        a,ap,_=v.profile(s,left,right);e,ep=v.chart(s,left,right)
        y,ys=v.field(s,left,right),v.field(s,left,right,1)
        F=self.F
        E=zero(F);power=D2(1)
        for k in range(self.order+1):
            for j in range(k+1):
                index=F+1+3*(2*j-k)
                add_at(E,index,power*(math.comb(k,j)*(-1)**j))
            power=power*e/(6*(k+1))
        rho,Ts=zero(F),zero(F)
        add_at(rho,F,D2(1))
        for sign in (-1,1):
            add_at(rho,F+3*sign,-e/2)
            add_at(Ts,F+3*sign,ep*sign/6)
        # Horizontal complex position has REAL Fourier coefficients.
        # R+iT gives coefficients (R_j +/- T_j)/2 at 1 +/- m_j.
        U,Us,Z,Zs=zero(F),zero(F),zero(F),zero(F)
        add_at(U,F+1,y.item(0));add_at(Us,F+1,ys.item(0))
        for j,k in enumerate(v.frequencies):
            R,T,z=y.item(1+j),y.item(1+v.M+j),y.item(1+2*v.M+j)
            Rs,Tsv,zs=ys.item(1+j),ys.item(1+v.M+j),ys.item(1+2*v.M+j)
            for sign in (-1,1):
                add_at(U,F+1+int(k)*sign,(R+T*sign)/2)
                add_at(Us,F+1+int(k)*sign,(Rs+Tsv*sign)/2)
                add_at(Z,F+int(k)*sign,z/2);add_at(Zs,F+int(k)*sign,zs/2)
        add_at(Zs,F,mean)
        B=E*ap-cv(Ts,E,F)*a+Us
        C=cv(rho,E,F)*a+U*self.freq
        V=Z*self.freq
        one=zero(2*F);add_at(one,2*F,D2(1))
        rr=cv(B,reverse(B))+cv(Zs,Zs)-one+cv(Ts,Ts)*a*a
        mixed=cv(B,reverse(C))
        rt=(reverse(mixed)-mixed)/2+cv(Zs,V)-cv(Ts,rho)*a*a
        tt=cv(C,reverse(C))-cv(V,V)-cv(rho,rho)*a*a
        # Banach Fourier l1 remainder for exp((e/6)(z^-3-z^3)).
        eb=e.v.absolute_upper();ab=a.v.absolute_upper();apb=ap.v.absolute_upper()
        epb=ep.v.absolute_upper();rhomin=float((I(1)-I(eb)).x[0]);amin=float(np.min(a.v.x[0]))
        if not 0<amin or not 0<rhomin or eb/3>Q(1,10):
            raise ValueError('Target metric or exponential bound outside scope')
        exp_tail=I.rational(2*(Q.from_float(eb)/3)**(self.order+1)/math.factorial(self.order+1))
        db=exp_tail*(I(apb)+I(ab)*epb/3)
        dc=exp_tail*ab*(1+I(eb))
        nb,nc=I(l1(B.v)),I(l1(C.v))
        tails=[2*nb*db+db*db,nb*dc+nc*db+db*dc,2*nc*dc+dc*dc]
        for tensor in (rr,rt,tt):
            if not all(getattr(tensor,k).finite() for k in ('v','d','d2')):
                raise ArithmeticError('Nonfinite Gram interval')
        vmax=float((I(epb)/(3*I(rhomin))).x[1])
        return [rr,rt,tt],dict(amin=amin,rhomin=rhomin,vmax=vmax,
            tails=[float(x.x[1]) for x in tails],root_min=float(np.min(root.x[0])))
    def enclose(self,left,right):
        middle=(left+right)/2;h=(right-left)/2
        point,pmeta=self.evaluate(middle,middle)
        whole,meta=self.evaluate(left,right)
        bounds=[];hI=I.rational(h)
        for c,w,tail in zip(point,whole,meta['tails']):
            bound=I(l1(c.v))+hI*I(l1(c.d))+hI*hI/2*I(l1(w.d2))+tail
            bounds.append(I(bound.x[1]))
        ss,st,tt=bounds
        # Correct explicit pullback to the target orthonormal material frame.
        vm=I(meta['vmax']);den=I(meta['amin'])*meta['rhomin']
        gss=ss+2*vm*st+vm*vm*tt
        gst=(st+vm*tt)/den;gtt=tt/(den*den)
        upper=float(max((gss+gst).x[1],(gtt+gst).x[1]))
        return upper,meta,bounds


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-run',type=Path,required=True)
    p.add_argument('--physical',type=Path,required=True)
    p.add_argument('--interval-kernel',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--mean-nodes',type=int,default=1168)
    p.add_argument('--exp-order',type=int,default=12)
    p.add_argument('--target',type=float,default=9.e-7)
    p.add_argument('--max-cells',type=int,default=200000)
    p.add_argument('--probe-only',action='store_true')
    a=p.parse_args();started=time.monotonic()
    m.K=m.module('_bridge_gram_intervals',a.interval_kernel);m.D=D2;m.sincos_d=trig
    support=Path(__file__).resolve().parent
    adapter=m.module('_bridge_gram_model',support/'actual_m3_metric_model.py')
    loader=m.module('_bridge_gram_field',support/'audit_full_relative_metric.py')
    o=adapter.load_model({'source_run':str(a.source_run.resolve())});z=loader.load_physical(a.physical)
    mean=JetMean(o,z,a.mean_nodes);gram=GramVerifier(mean,a.exp_order)
    report=dict(scope=__doc__,source_sha256=sha(__file__),run_sha256=sha(a.source_run),
        physical_sha256=sha(a.physical),mean_nodes=a.mean_nodes,exp_order=a.exp_order,
        target=a.target,C2_object_transfer_included=False,whole_surface=False,
        status='running',accepted=0,splits=0,attempts=0,peak=0.,root_min=float('inf'))
    a.out.parent.mkdir(parents=True,exist_ok=True)
    def save():a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    if a.probe_only:
        rows=[]
        for j in np.linspace(0,len(mean.grid)-2,7).astype(int):
            left,right=mean.grid[j:j+2];c=(left+right)/2
            upper,meta,_=gram.enclose(c,c)
            row=dict(s=float(c),operator_bound=upper,**meta);rows.append(row)
            print(json.dumps(dict(event='point_probe',**row)),flush=True)
        report.update(status='point_probes_only',rows=rows,root_min=min(x['root_min'] for x in rows))
        save();return
    stack=[(l,r,0) for l,r in zip(mean.grid[:-1],mean.grid[1:])][::-1]
    while stack:
        left,right,depth=stack.pop();report['attempts']+=1
        try:
            upper,meta,_=gram.enclose(left,right)
        except (ValueError,ArithmeticError,FloatingPointError):
            upper=float('inf');meta=None
        if upper<=a.target:
            report['accepted']+=1
            if upper>report['peak']:
                report.update(peak=upper,peak_interval=[float(left),float(right)])
            report['root_min']=min(report['root_min'],meta['root_min'])
        else:
            if depth>=30 or report['accepted']+len(stack)>=a.max_cells:
                report.update(status='not_certified',remaining=len(stack)+1,
                              unresolved_interval=[float(left),float(right)],last_bound=None if not math.isfinite(upper) else upper)
                if not math.isfinite(report['root_min']):report['root_min']=None
                save();return
            mid=(left+right)/2
            stack.extend([(mid,right,depth+1),(left,mid,depth+1)]);report['splits']+=1
        if report['attempts']%100==0:
            print(json.dumps(dict(event='continuous_gram_progress',accepted=report['accepted'],
                attempts=report['attempts'],splits=report['splits'],remaining=len(stack),
                s=float(right),peak=report['peak'])),flush=True)
    report.update(status='continuous_jet_oracle_metric_certified',seconds=time.monotonic()-started)
    save();print(json.dumps(report),flush=True)


if __name__=='__main__':main()
