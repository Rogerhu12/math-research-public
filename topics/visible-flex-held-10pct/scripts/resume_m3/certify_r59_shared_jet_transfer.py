#!/usr/bin/env python3
"""Exact common-two-jet Hermite interpretation of saved bridge polynomials.

A NEW explicit C2 interpretation is defined; the original physical file is not
edited. Right-side knot two-jets are selected, and the final knot retains the
last polynomial's left two-jet. Exact quintic Hermite correction matches them.
The angular cubic spline receives the same shared-two-jet construction before
the unchanged exact cutoff is applied. All transfer bounds are exact rational
Bernstein ranges on the complete bridge.
"""
import argparse,bisect,hashlib,importlib.util,json,math,sys
from pathlib import Path
from fractions import Fraction as Q
import numpy as np

def fq(x):return Q.from_float(float(x))
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def power(a,n):
    c=[Q(1)]
    for _ in range(n):c=mul(c,a)
    return c
def derivative(a,order=1):
    for _ in range(order):a=[(j+1)*a[j+1] for j in range(len(a)-1)]
    return a
def value(a,t):
    x=Q(0)
    for c in a[::-1]:x=x*t+c
    return x
def bernstein(coef,origin,left,right):
    n=len(coef)-1;d=left-origin;h=right-left
    local=[sum(coef[j]*math.comb(j,k)*d**(j-k) for j in range(k,n+1))*h**k for k in range(n+1)]
    return [sum(local[j]*Q(math.comb(k,j),math.comb(n,j)) for j in range(k+1)) for k in range(n+1)]
def abrange(coef,origin,left,right):
    return max(map(abs,bernstein(coef,origin,left,right)))
def right_correction(poly,h,target):
    original=[value(derivative(poly,k),h) for k in range(3)]
    d0,d1,d2=[b-a for a,b in zip(original,target)]
    return [Q(0),Q(0),Q(0),
            (10*d0-4*h*d1+h*h*d2/2)/h**3,
            (-15*d0+7*h*d1-h*h*d2)/h**4,
            (6*d0-3*h*d1+h*h*d2/2)/h**5], [d0,d1,d2]
def usqrt(x):
    scale=10**18;k=math.isqrt(x.numerator*scale*scale//x.denominator)
    if k*k*x.denominator<x.numerator*scale*scale:k+=1
    return Q(k,scale)
def norm(*x):return usqrt(sum(t*t for t in x))
def pack(x):return dict(exact=str(x),display=float(x))

class SharedBridgeData:
    def __init__(self,o,z):
        self.o,self.z=o,z;o.initial(z.p);self.f=o.flow(z.p[0])
        f=self.f;self.entry,self.end=fq(f.prefix_end),fq(f.end)
        self.x=[fq(x) for x in z.x];self.n=o.n;self.M=o.M;self.q=fq(o.q)
        self.y_corrections={};self.y_error=[[Q(0)]*self.n for _ in range(3)]
        self.y_jump=[[Q(0)]*self.n for _ in range(3)]
        for i in range(len(self.x)-1):
            left,right=self.x[i],self.x[i+1]
            if right<self.entry:continue
            h=right-left;rows=[]
            for j in range(self.n):
                pp=[fq(z.sol.c[5-k,i,j]) for k in range(6)]
                if i+1<len(self.x)-1:
                    target=[fq(z.sol.c[5,i+1,j]),fq(z.sol.c[4,i+1,j]),2*fq(z.sol.c[3,i+1,j])]
                else:target=[value(derivative(pp,k),h) for k in range(3)]
                cc,jj=right_correction(pp,h,target);rows.append(cc)
                for k in range(3):
                    self.y_error[k][j]=max(self.y_error[k][j],abrange(derivative(cc,k),left,max(left,self.entry),right))
                    self.y_jump[k][j]=max(self.y_jump[k][j],abs(jj[k]))
            self.y_corrections[i]=rows
        self.spx=[fq(x)*self.end for x in f.spline.x];self.h_corrections={}
        self.h_original={}
        for i in range(len(self.spx)-1):
            pp=[fq(f.spline.c[3-k,i])/self.end**k for k in range(4)]
            h=self.spx[i+1]-self.spx[i]
            if i+1<len(self.spx)-1:
                target=[fq(f.spline.c[3,i+1]),
                        fq(f.spline.c[2,i+1])/self.end,
                        2*fq(f.spline.c[1,i+1])/self.end**2]
            else:target=[value(derivative(pp,k),h) for k in range(3)]
            cc,_=right_correction(pp,h,target)
            self.h_original[i]=pp;self.h_corrections[i]=cc
        self.cutoff=Q(3,4)*self.end
        grid=sorted(set([self.entry,self.end]+[x for x in self.spx if self.entry<x<self.end]+
                        ([self.cutoff] if self.entry<self.cutoff<self.end else [])))
        self.e_error=[Q(0)]*3
        for left,right in zip(grid[:-1],grid[1:]):
            mid=(left+right)/2;i=min(len(self.spx)-2,bisect.bisect_right(self.spx,mid)-1)
            pp=self.h_corrections[i];origin=self.spx[i]
            if mid>self.cutoff:
                u=[(origin-self.cutoff)/(self.end/4),4/self.end]
                chi=[Q(1)]+[Q(0)]*5
                for factor,degree in [(-10,3),(15,4),(-6,5)]:
                    for j,v in enumerate(power(u,degree)):chi[j]+=factor*v
                pp=mul(pp,chi)
            pp=[fq(f.warp_e)*v for v in pp]
            for k in range(3):
                self.e_error[k]=max(self.e_error[k],abrange(derivative(pp,k),origin,left,right))
    def field_errors(self):
        freq=[int(v) for v in self.f.even];M=self.M
        def pb(y):
            R0=y[0];R=y[1:M+1];T=y[M+1:2*M+1];Z=y[2*M+1:]
            return [
                norm(R0+sum(R),sum(T),sum(Z)),
                norm(sum(m*x for m,x in zip(freq,R))+sum(T),
                     R0+sum(R)+sum(m*x for m,x in zip(freq,T)),
                     sum(m*x for m,x in zip(freq,Z))),
                norm(R0+sum((m*m+1)*x for m,x in zip(freq,R))+2*sum(m*x for m,x in zip(freq,T)),
                     sum((m*m+1)*x for m,x in zip(freq,T))+2*sum(m*x for m,x in zip(freq,R)),
                     sum(m*m*x for m,x in zip(freq,Z)))]
        a,b,c=[pb([self.q*v for v in row]) for row in self.y_error]
        return dict(G=a[0],G_psi=a[1],G_psipsi=a[2],G_s_comp=b[0],G_spsi_comp=b[1],G_ss_comp=c[0])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-run",type=Path,required=True);p.add_argument("--physical",type=Path,required=True)
    p.add_argument("--support-dir",type=Path,default=Path(__file__).resolve().parent);p.add_argument("--out",type=Path,required=True)
    a=p.parse_args();ad=module("_shared_jet_model",a.support_dir/"actual_m3_metric_model.py")
    ld=module("_shared_jet_field",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=ld.load_physical(a.physical)
    data=SharedBridgeData(o,z)
    report=dict(status="exact_shared_two_jet_transfer_bounds_completed",new_C2_interpretation_explicit=True,
        original_physical_file_modified=False,whole_geometry_certificate=False,
        physical_sha256=hashlib.sha256(a.physical.read_bytes()).hexdigest(),
        run_sha256=hashlib.sha256(a.source_run.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        modes=o.M,physical_pieces_with_bridge=len(data.y_corrections),
        coefficient_error_maxima=[pack(max(row)) for row in data.y_error],
        original_knot_jump_maxima=[pack(max(row)) for row in data.y_jump],
        all_angle_computational_field_error={k:pack(v) for k,v in data.field_errors().items()},
        angular_chart_e_error=[pack(v) for v in data.e_error],
        scope=[
            "New shared knot two-jets are selected from each knot's right polynomial, and final knot from last left polynomial",
            "Exact quintic Hermite interpolation defines a new C2 coefficient and angular-spline object",
            "Existing raw fields are not overwritten, and the transfer is not silently identified with them",
            "Bounds cover complete bridge pieces and all computational angles; mean/reference primitive and material inverse-chart transfer are separate",
            "The shared-jet definition may be evaluated as exact rationals or with rigorous rounding; independently rounding its expanded coefficients does not itself preserve literal C2"])
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","modes","coefficient_error_maxima","all_angle_computational_field_error","angular_chart_e_error")}))
if __name__=="__main__":main()

