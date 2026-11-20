#!/usr/bin/env python3
"""Continuous radial interval ranges for the actual finite 512-node mean.

No field coefficients, core, metric, or solver are changed. This verifies the
bridge mean of the declared finite angular rule; it is not a continuous-angle
quadrature certificate and not a whole closed-surface certificate. All original
PPoly/angular-spline pieces are covered, including their one-sided limits.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse,bisect,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import mpmath as mp

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
    return m
K=None
class I:
    def __init__(self,a,b=None):
        if isinstance(a,I):self.x=a.x
        elif b is None:self.x=K.exact(a)
        else:self.x=(np.asarray(a,float),np.asarray(b,float))
    @staticmethod
    def raw(z):
        v=I.__new__(I);v.x=z;return v
    @staticmethod
    def rational(z):
        z=Q(z);v=float(z)
        if not math.isfinite(v):raise ArithmeticError("Nonfinite rational conversion")
        return I(K.dn(v),K.up(v))
    def __add__(self,b):return I.raw(K.add(self.x,I(b).x))
    __radd__=__add__
    def __neg__(self):return I.raw(K.neg(self.x))
    def __sub__(self,b):return self+-I(b)
    def __rsub__(self,b):return I(b)+-self
    def __mul__(self,b):return I.raw(K.mul(self.x,I(b).x))
    __rmul__=__mul__
    def __truediv__(self,b):return I.raw(K.div(self.x,I(b).x))
    def __rtruediv__(self,b):return I(b)/self
    def sq(self):return I.raw(K.square(self.x))
    def sqrt(self):return I.raw(K.sqrt(self.x))
    def sum(self,axis=0):return I.raw(K.interval_sum_terms(self.x,axis))
    def item(self,key):return I(self.x[0][key],self.x[1][key])
    def expand(self):return I(np.asarray(self.x[0])[...,None],np.asarray(self.x[1])[...,None])
    def absolute_upper(self):return float(np.max(np.maximum(abs(self.x[0]),abs(self.x[1]))))
    def finite(self):return bool(np.all(np.isfinite(self.x[0])) and np.all(np.isfinite(self.x[1])))
    def __pow__(self,n):
        if n==0:return I(1)
        if n==2:return self.sq()
        v=I(1)
        for _ in range(n):v=v*self
        return v
class D:
    def __init__(self,v,d=0):
        if isinstance(v,D):self.v,self.d=v.v,v.d
        else:self.v,self.d=I(v),I(d)
    def __add__(self,b):
        b=D(b);return D(self.v+b.v,self.d+b.d)
    __radd__=__add__
    def __neg__(self):return D(-self.v,-self.d)
    def __sub__(self,b):return self+-D(b)
    def __rsub__(self,b):return D(b)+-self
    def __mul__(self,b):
        b=D(b);return D(self.v*b.v,self.d*b.v+self.v*b.d)
    __rmul__=__mul__
    def __truediv__(self,b):
        b=D(b);return D(self.v/b.v,(self.d*b.v-self.v*b.d)/b.v.sq())
    def __rtruediv__(self,b):return D(b)/self
    def sq(self):return D(self.v.sq(),2*self.v*self.d)
    def sqrt(self):
        v=self.v.sqrt();return D(v,self.d/(2*v))
    def sum(self,axis=0):return D(self.v.sum(axis),self.d.sum(axis))
    def item(self,key):return D(self.v.item(key),self.d.item(key))
    def expand(self):return D(self.v.expand(),self.d.expand())
    def __pow__(self,n):
        if n==0:return D(1)
        if n==2:return self.sq()
        v=D(1)
        for _ in range(n):v=v*self
        return v

def sincos_i(x):
    # Full Taylor polynomials with uniform remainder, only |x|<=2 is admitted.
    x=I(x);h=x.absolute_upper()
    if h>2:raise ValueError("Taylor trigonometry outside declared radius")
    xx=x.sq()
    # sin through degree 29, cos through degree 30.
    ps=I.rational(Q((-1)**14,math.factorial(29)))
    for k in range(13,-1,-1):ps=ps*xx+I.rational(Q((-1)**k,math.factorial(2*k+1)))
    pc=I.rational(Q((-1)**15,math.factorial(30)))
    for k in range(14,-1,-1):pc=pc*xx+I.rational(Q((-1)**k,math.factorial(2*k)))
    rs=I.rational(Q.from_float(h)**31/math.factorial(31)).x[1]
    rc=I.rational(Q.from_float(h)**32/math.factorial(32)).x[1]
    return x*ps+I(-rs,rs),pc+I(-rc,rc)
def sincos_d(x):
    x=D(x);s,c=sincos_i(x.v)
    return D(s,c*x.d),D(c,-s*x.d)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),D(0))
def norm(a):return sum((x.sq() for x in a),D(0)).sqrt()
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def poly(coef,x):
    v=I(0)
    for c in coef[::-1]:v=v*x+c
    return v
def pder(c):return [(i+1)*c[i+1] for i in range(len(c)-1)]
def fq(x):return Q.from_float(float(x))
def qmul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def qpower(a,n):
    c=[Q(1)]
    for _ in range(n):c=qmul(c,a)
    return c

class MeanVerifier:
    def __init__(self,o,z,N):
        self.o,self.z=o,z;o.initial(z.p);self.f=o.flow(z.p[0]);self.N=N
        f=self.f;self.M=o.M;self.q=I(o.q)
        self.entry,self.end=fq(f.prefix_end),fq(f.end)
        self.xx=[fq(x) for x in z.x]
        self.pc=[[I(z.sol.c[5-k,i,:]) for k in range(6)] for i in range(len(z.x)-1)]
        self.spx=[fq(x)*self.end for x in f.spline.x]
        self.cutoff=Q(3,4)*self.end
        self.ec={}
        self.L1,self.L2,self.L3=map(fq,(f.bridge.L1,f.bridge.L2,f.bridge.L3))
        self.peak,self.eps=I(f.bridge.peak),I(f.bridge.eps)
        self.gl_t=I((1+f.bridge.g)/2)
        # Literal source computes u*(1+g)/2 in that order. The mathematical
        # reference uses the exact binary constants 1+g and w/2 as below.
        self.gl_t=(I(1)+I(f.bridge.g))/2
        self.gl_w=I(f.bridge.gw)/2
        self.frequencies=np.asarray(f.even,int)
        psi=2*np.pi*np.arange(N)/N
        self.psi_literal=psi
        mp.iv.dps=60
        cs=[];sn=[]
        for m in [3]+self.frequencies.tolist():
            cr=[];ci=[];sr=[];si=[]
            for p in psi:
                t=mp.iv.mpf(float(p))*int(m)
                c=mp.iv.cos(t);s=mp.iv.sin(t)
                cr.append(float(K.dn(float(c.a))));ci.append(float(K.up(float(c.b))))
                sr.append(float(K.dn(float(s.a))));si.append(float(K.up(float(s.b))))
            cs.append(I(np.array(cr),np.array(ci)));sn.append(I(np.array(sr),np.array(si)))
        self.co3,self.sn3=cs[0],sn[0]
        self.co=I(np.stack([v.x[0] for v in cs[1:]]),np.stack([v.x[1] for v in cs[1:]]))
        self.sn=I(np.stack([v.x[0] for v in sn[1:]]),np.stack([v.x[1] for v in sn[1:]]))
        self.grid=sorted(set([self.entry,self.end]+[x for x in self.xx if self.entry<x<self.end]+
            [x for x in self.spx if self.entry<x<self.end]+
            [x for x in [self.cutoff,self.entry+self.L1,self.entry+self.L1+self.L2] if self.entry<x<self.end]))
        self.drop1=self.integral(D(1),1)*I.rational(self.L1)
        self.drop3=self.integral(D(1),3)*I.rational(self.L3)
    def integral(self,u,part):
        t=u*D(self.gl_t)
        phi=D(self.peak)*(3*t*t-2*t*t*t) if part==1 else D(self.peak)-D(self.eps)*t*t
        sin,_=sincos_d(phi)
        return u*(sin*D(self.gl_w)).sum()
    def profile(self,s,left,right):
        x=D(s-I.rational(self.entry),1)
        mid=(left+right)/2-self.entry
        L1,L2,L3=(D(I.rational(v)) for v in (self.L1,self.L2,self.L3))
        sp,cp=sincos_d(D(self.peak))
        if mid<self.L1:
            u=x/L1;phi=D(self.peak)*(3*u*u-2*u*u*u)
            aa=1-L1*self.integral(u,1)
        elif mid<self.L1+self.L2:
            phi=D(self.peak)
            aa=1-self.drop1-(x-L1)*sp
        else:
            u=(x-L1-L2)/L3;phi=D(self.peak)-D(self.eps)*u*u
            aa=1-self.drop1-L2*sp-L3*self.integral(u,3)
        ss,cc=sincos_d(phi)
        return aa,-ss,cc
    def chart(self,s,left,right):
        mid=(left+right)/2
        idx=min(len(self.spx)-2,bisect.bisect_right(self.spx,mid)-1)
        late=mid>self.cutoff;key=(idx,late)
        if key not in self.ec:
            origin=self.spx[idx]
            qcoef=[fq(self.f.spline.c[3-k,idx])/self.end**k for k in range(4)]
            if late:
                u=[(origin-self.cutoff)/(self.end/4),4/self.end]
                cc=[Q(1)]+[Q(0)]*5
                for factor,degree in [(-10,3),(15,4),(-6,5)]:
                    v=qpower(u,degree)
                    for j,x in enumerate(v):cc[j]+=factor*x
                qcoef=qmul(qcoef,cc)
            cc=[I.rational(fq(self.f.warp_e)*v) for v in qcoef]
            self.ec[key]=(origin,cc,pder(cc),pder(pder(cc)))
        origin,c,c1,c2=self.ec[key];x=s-I.rational(origin)
        return D(poly(c,x),poly(c1,x)),D(poly(c1,x),poly(c2,x))
    def coefficients(self,s,left,right):
        mid=(left+right)/2;idx=min(len(self.xx)-2,bisect.bisect_right(self.xx,mid)-1)
        x=s-I.rational(self.xx[idx]);c=self.pc[idx]
        return D(poly(c,x)*self.q,poly(pder(c),x)*self.q)
    def evaluate(self,left,right):
        s=I(I.rational(left).x[0],I.rational(right).x[1])
        y=self.coefficients(s,left,right);a,ap,reference=self.profile(s,left,right)
        e,ep=self.chart(s,left,right)
        co,sn=self.co,self.sn
        fr=I(self.frequencies[:,None])
        r=y.item(slice(1,self.M+1)).expand()
        t=y.item(slice(self.M+1,2*self.M+1)).expand()
        z=y.item(slice(2*self.M+1,None)).expand()
        R=y.item(0)+(r*co).sum()
        Rp=-(r*(fr*sn)).sum();Rpp=-(r*(fr.sq()*co)).sum()
        T=(t*sn).sum();Tp=(t*(fr*co)).sum();Tpp=-(t*(fr.sq()*sn)).sum()
        Zp=-(z*(fr*sn)).sum();Zpp=-(z*(fr.sq()*co)).sum()
        rho=1-e*self.co3;rp=3*e*self.sn3
        delta=e*self.sn3/3
        sd,cd=sincos_d(delta)
        D1r,D1t=Rp-T,Tp+R
        D2r,D2t=Rpp-2*Tp-R,Tpp+2*Rp-T
        R1,T1=D1r*cd-D1t*sd,D1r*sd+D1t*cd
        R2,T2=D2r*cd-D2t*sd,D2r*sd+D2t*cd
        U=[R1/(a*rho),1+T1/(a*rho),Zp/(a*rho)]
        V=[-1+R2/(a*rho*rho)-R1*rp/(a*rho*rho*rho),
           T2/(a*rho*rho)-T1*rp/(a*rho*rho*rho),
           Zpp/(a*rho*rho)-Zp*rp/(a*rho*rho*rho)]
        un=norm(U);un2=un*un
        kap_a=norm(cross(U,V))/(un*un*un)
        Tunit=[x/un for x in U]
        projection=dot(Tunit,V)
        nn=[x-projection*t0 for x,t0 in zip(V,Tunit)]
        nv=norm(nn)
        Nunit=[x/nv for x in nn]
        Bin=cross(Tunit,Nunit)
        alpha=-ap/kap_a
        root=1-alpha.sq()
        if np.any(root.v.x[0]<=0):raise ValueError("interval Frenet root not positive")
        beta=root.sqrt()
        v=-ep*self.sn3/(3*rho)
        Wz=alpha*Nunit[2]+beta*Bin[2]+v*Zp
        mean=Wz.sum()/self.N
        difference=mean-reference
        if not difference.v.finite() or not difference.d.finite():raise ArithmeticError("Nonfinite interval")
        return difference,mean,root.v

def main():
    global K
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-run",type=Path,required=True);p.add_argument("--physical",type=Path,required=True)
    p.add_argument("--support-dir",type=Path,default=Path(__file__).resolve().parent)
    p.add_argument("--interval-kernel",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True);p.add_argument("--mean-nodes",type=int,default=512)
    p.add_argument("--difference",type=float,default=.01);p.add_argument("--derivative-difference",type=float,default=1.)
    p.add_argument("--max-cells",type=int,default=30000)
    a=p.parse_args();beg=time.monotonic()
    K=module("_r59_interval_kernel",a.interval_kernel)
    ad=module("_r59_mean_actual_model",a.support_dir/"actual_m3_metric_model.py")
    ld=module("_r59_mean_physical",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    obj=MeanVerifier(o,z,a.mean_nodes)
    stack=[(l,r,0) for l,r in zip(obj.grid[:-1],obj.grid[1:])][::-1]
    accepted=split=domain=attempts=0;max_depth=0
    d0=d1=0.;root_min=float("inf");ml=float("inf");mh=-float("inf")
    peak0=peak1=None
    failed=None
    while stack:
        left,right,depth=stack.pop();attempts+=1
        try:
            diff,mean,root=obj.evaluate(left,right)
            v0,v1=diff.v.absolute_upper(),diff.d.absolute_upper()
            valid=v0<=a.difference and v1<=a.derivative_difference
        except (ValueError,ArithmeticError) as exc:
            valid=False;domain+=1;v0=v1=float("inf");reason=str(exc)
        if not valid:
            if attempts>=a.max_cells or depth>=22:
                failed=dict(s_interval=[float(left),float(right)],depth=depth,
                            reason=reason if not math.isfinite(v0) else "required mean range unresolved",
                            value=v0,derivative=v1);break
            mid=(left+right)/2
            stack.extend([(mid,right,depth+1),(left,mid,depth+1)]);split+=1
            continue
        accepted+=1;max_depth=max(max_depth,depth)
        if v0>d0:d0=v0;peak0=[float(left),float(right)]
        if v1>d1:d1=v1;peak1=[float(left),float(right)]
        root_min=min(root_min,float(np.min(root.x[0])))
        ml=min(ml,float(mean.v.x[0]));mh=max(mh,float(mean.v.x[1]))
        if accepted%250==0:
            print(json.dumps(dict(progress_cells=accepted,attempts=attempts,pending=len(stack),
                                 seconds=time.monotonic()-beg,max_difference=d0,max_derivative_difference=d1)),flush=True)
    status="continuous_finite_mean_ranges_completed" if failed is None else "continuous_finite_mean_ranges_unresolved"
    report=dict(status=status,complete=failed is None,whole_R59_certificate=False,
        mean_nodes=a.mean_nodes,angular_rule="equal positive weights at literal source binary64 psi nodes; no continuous mean substitution",
        physical_sha256=hashlib.sha256(a.physical.read_bytes()).hexdigest(),
        run_sha256=hashlib.sha256(a.source_run.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        interval_kernel_sha256=hashlib.sha256(a.interval_kernel.read_bytes()).hexdigest(),
        accepted_cells=accepted,attempted_cells=attempts,split_cells=split,domain_bisections=domain,
        max_depth=max_depth,mean_difference_upper=d0,mean_derivative_difference_upper=d1,
        mean_difference_peak=peak0,derivative_difference_peak=peak1,mean_value_range=[ml,mh],
        frenet_root_lower=root_min,failed_cell=failed,seconds=time.monotonic()-beg,
        scope=[
            "Continuous in the radial variable on all recorded polynomial and analytic bridge pieces",
            "Interval derivative uses the same full coefficient field, true derivative of literal GL64 source radius, and source manual slope in the Frenet velocity",
            "Comparison baseline is the source-angle cosine, with its true derivative; affine/true-reference transfer is separate",
            "Nonrotating exact lift vanishes identically on this bridge",
            "Both one-sided endpoint limits covered; public common-C2 interpretation remains separate",
            "No inlet height primitive has been certified by this bridge-only calculation"])
    report["diagnostics"]={k:report[k] for k in
        ("status","complete","accepted_cells","mean_difference_upper","mean_derivative_difference_upper","frenet_root_lower","failed_cell")}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report["diagnostics"]))
    if failed is not None:raise SystemExit(1)
if __name__=="__main__":main()

