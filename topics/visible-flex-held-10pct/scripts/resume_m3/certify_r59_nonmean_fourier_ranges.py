#!/usr/bin/env python3
"""Exact rational all-angle nonmean bridge-jet ranges for saved physical PPoly.

This certifies the finite Fourier contribution on every radial piece using
exact binary64 input rationals and exact Bernstein transforms. The target
radius/reference mean/core interpolation contracts remain explicit. No BVP is
run, and no complete R59 certificate is asserted by this component alone.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse, bisect, hashlib, importlib.util, json, math, sys
from pathlib import Path
from fractions import Fraction as Q
import numpy as np

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
    return m
def fq(x):return Q.from_float(float(x))
def upper_sqrt(x,scale=10**15):
    if x<0:raise ArithmeticError("negative square")
    t=x.numerator*scale*scale; d=x.denominator
    k=math.isqrt(t//d)
    if k*k*d<t:k+=1
    return Q(k,scale)
def norm(*x):return upper_sqrt(sum(z*z for z in x))
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def power(a,n):
    c=[Q(1)]
    for _ in range(n):c=mul(c,a)
    return c
def derivative(a,order):
    for _ in range(order):a=[(j+1)*a[j+1] for j in range(len(a)-1)]
    return a
def bernstein_range(coef,origin,left,right):
    n=len(coef)-1; offset=left-origin; width=right-left
    local=[sum(coef[j]*math.comb(j,k)*offset**(j-k) for j in range(k,n+1))*width**k
           for k in range(n+1)]
    bb=[sum(local[j]*Q(math.comb(k,j),math.comb(n,j)) for j in range(k+1))
        for k in range(n+1)]
    return min(bb),max(bb)
def absolute_range(coef,origin,left,right):
    lo,hi=bernstein_range(coef,origin,left,right);return max(abs(lo),abs(hi))
def pack(x):return dict(exact=str(x),display=float(x))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-run",type=Path,required=True)
    p.add_argument("--physical",type=Path,required=True)
    p.add_argument("--support-dir",type=Path,default=Path(__file__).resolve().parent)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    ad=module("_bernstein_actual_model",a.support_dir/"actual_m3_metric_model.py")
    loader=module("_bernstein_actual_field",a.support_dir/"audit_full_relative_metric.py")
    o=ad.load_model({"source_run":str(a.source_run.resolve())});z=loader.load_physical(a.physical)
    o.initial(z.p);f=o.flow(z.p[0])
    if f.cfg["prefix_bridge"]!={"kind":"turn_plateau_v1","curvature":4,"peak_fraction":.2}:
        raise ValueError("Wrong bridge for the cited R59 reference")
    entry,end=fq(f.prefix_end),fq(f.end)
    bridge_length=end-entry
    # Strict true-reference length interval inherited from R59's executed
    # full rational interval output. This does not rerun those integrals.
    ref_length_lo,ref_length_hi=Q(93014,100000),Q(93125,100000)
    cmin,cmax=Q(999,1000),Q(1001,1000)
    assert bridge_length/ref_length_hi>cmin
    assert bridge_length/ref_length_lo<cmax
    xx=[fq(v) for v in z.x]
    pp=z.sol.c
    spline_x=[fq(v) for v in f.spline.x]
    spline_origin=[v*end for v in spline_x]
    cutoff=Q(3,4)*end
    grid=sorted(set([entry,end]+[v for v in xx if entry<v<end]+
                    [v for v in spline_origin if entry<v<end]+
                    ([cutoff] if entry<cutoff<end else [])))
    frequencies=[int(v) for v in f.even]
    M=int(o.M);q=fq(o.q);warp=fq(f.warp_e)
    P_cache,E_cache={},{}
    def polys(index):
        if index not in P_cache:
            P_cache[index]=[[q*fq(pp[5-k,index,j]) for k in range(6)] for j in range(o.n)]
        return P_cache[index]
    def e_poly(index,late):
        key=(index,late)
        if key in E_cache:return E_cache[key]
        origin=spline_origin[index]
        e=[fq(f.spline.c[3-k,index])/end**k for k in range(4)]
        if late:
            u=[(origin-cutoff)/(end/4),4/end]
            c=[Q(1)]+[Q(0)]*5
            for factor,degree in [(-10,3),(15,4),(-6,5)]:
                v=power(u,degree)
                for j,x in enumerate(v):c[j]+=factor*x
            e=mul(e,c)
        e=[warp*v for v in e]
        E_cache[key]=(origin,e)
        return origin,e
    def polar_bounds(yy):
        R0=yy[0];R=yy[1:M+1];T=yy[M+1:2*M+1];Z=yy[2*M+1:]
        r,t,z0=R0+sum(R),sum(T),sum(Z)
        r1=sum(m*v for m,v in zip(frequencies,R))+sum(T)
        t1=R0+sum(R)+sum(m*v for m,v in zip(frequencies,T))
        z1=sum(m*v for m,v in zip(frequencies,Z))
        r2=R0+sum((m*m+1)*v for m,v in zip(frequencies,R))+2*sum(m*v for m,v in zip(frequencies,T))
        t2=sum((m*m+1)*v for m,v in zip(frequencies,T))+2*sum(m*v for m,v in zip(frequencies,R))
        z2=sum(m*m*v for m,v in zip(frequencies,Z))
        return norm(r,t,z0),norm(r1,t1,z1),norm(r2,t2,z2)
    maxima={};rho_min=Q(1);rows=0
    def record(name,value,left,right):
        if name not in maxima or value>maxima[name]["value"]:
            maxima[name]=dict(value=value,left=left,right=right)
    for left,right in zip(grid[:-1],grid[1:]):
        mid=(left+right)/2
        index=min(len(xx)-2,bisect.bisect_right(xx,mid)-1)
        sj=min(len(spline_x)-2,bisect.bisect_right(spline_origin,mid)-1)
        eorigin,epoly=e_poly(sj,mid>cutoff)
        eb=[absolute_range(derivative(epoly,k),eorigin,left,right) for k in range(3)]
        rho=1-eb[0]
        if rho<=0:raise ArithmeticError("Angular chart positivity lost")
        rho_min=min(rho_min,rho)
        v=eb[1]/(3*rho)
        vp=eb[1]*(1+eb[0])/rho**2
        vs=eb[2]/(3*rho)+eb[1]**2/(3*rho**2)
        rhop=3*eb[0]
        coef=polys(index)
        yy=[[absolute_range(derivative(cc,k),xx[index],left,right) for cc in coef] for k in range(3)]
        q0,q1,q2=polar_bounds(yy[0]);p0,p1,_=polar_bounds(yy[1]);pp0,_,_=polar_bounds(yy[2])
        A=p0+v*q1;B=q1/rho
        C=pp0+2*v*p1+v*v*q2+(v*vp+vs)*q1
        D=(p1+vp*q1+v*q2)/rho
        EE=q2/rho**2+q1*rhop/rho**3
        # R59 reference radius: a_ref>=R>.299 and a_ref>=1-xi,
        # xi=(s-entry)/c, c>=cmin. Also |a_ref'|<=1.
        aa=max(Q(299,1000),1-(right-entry)/cmin)
        w1=norm(cmax*A,B/aa)
        H00=cmax*cmax*C
        H01=(cmax*D+B/aa)/aa
        H11=(EE+aa*cmax*A)/aa**2
        w2=upper_sqrt(H00*H00+2*H01*H01+H11*H11)
        for name,value in [("G0",q0),("G1",w1),("G2",w2),("G_s",A),("G_theta",B),
                           ("H00",H00),("H01",H01),("H11",H11)]:
            record(name,value,left,right)
        rows+=1
    result={}
    for name,row in maxima.items():
        result[name]={**pack(row["value"]),"s_interval":[float(row["left"]),float(row["right"])]}
    report=dict(
        status="exact_piecewise_radial_and_all_angle_nonmean_ranges_completed",
        whole_R59_certificate=False,solver_called=False,
        scope=__doc__,input_run_sha256=hashlib.sha256(a.source_run.read_bytes()).hexdigest(),
        physical_sha256=hashlib.sha256(a.physical.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        intervals=rows,physical_segments=len(xx)-1,modes=M,q_exact=str(q),
        reference_affine_scale_interval=[str(cmin),str(cmax)],
        reference_length_interval=[str(ref_length_lo),str(ref_length_hi)],
        chart_rho_lower=pack(rho_min),maxima=result,
        exact_scope=[
            "Finite saved quintic coefficients and cubic angular spline read as exact binary64 rationals",
            "Bernstein range on every physical and angular-chart polynomial piece; all angles by Fourier coefficient absolute sums",
            "Both one-sided endpoint polynomial limits are included; this does not assert exact C2 equality of separately rounded coefficients",
            "Material derivatives use the full s-dependent chart and affine pullback into the R59 reference arc variable",
            "Only the finite nonmean Fourier contribution G is certified; background-reference difference and the fixed mean primitive are not silently zero"],
        remaining_contracts=[
            "Same actual mean provider and a rigorous bridge range for its derivative and difference from reference height speed",
            "Actual/reference background jet difference including source quadrature and common C2 interpretation",
            "Actual absolute inlet mean z0 in [.35,.51]"])
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","intervals","chart_rho_lower","maxima","whole_R59_certificate")}))

if __name__=="__main__":main()

