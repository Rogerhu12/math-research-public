#!/usr/bin/env python3
"""Complete intrinsic scalar jets by Arb Laurent exponential convolution.

The original finite phase is exponentiated in the complete Wiener algebra.
The one-sided formal exponential polynomials have explicit whole infinite
Fourier remainders. No angular grid, FFT alias assumption, or discarded
primitive tail is used. All declared radial derivatives are formed before
interval collapse on one actual scalar germ.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import json,math,time
from pathlib import Path
from flint import arb,acb,arb_poly,arb_series,ctx
from fourfold_phase_metric_defect import MetricDefectTarget,record,save,sha
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_beta_bulk_interval import BulkTarget,exact_arb,real_interval


class Laurent:
    def __init__(self,values=(),lo=0):
        self.p=values if isinstance(values,arb_poly) else arb_poly(list(values))
        self.lo=int(lo)
    @classmethod
    def constant(cls,x):return cls([x])
    def __getitem__(self,k):
        j=int(k)-self.lo
        return self.p[j] if 0<=j<len(self.p) else arb(0)
    @property
    def hi(self):return self.lo+len(self.p)-1
    def coefficients(self,lo,hi):return [self[j] for j in range(lo,hi+1)]
    def __add__(self,other):
        if not isinstance(other,Laurent):other=Laurent.constant(other)
        lo=min(self.lo,other.lo)
        return Laurent(self.p.left_shift(self.lo-lo)+other.p.left_shift(other.lo-lo),lo)
    __radd__=__add__
    def __neg__(self):return Laurent(-self.p,self.lo)
    def __sub__(self,other):return self+(-other if isinstance(other,Laurent) else -arb(other))
    def __mul__(self,other):
        if isinstance(other,Laurent):return Laurent(self.p*other.p,self.lo+other.lo)
        return Laurent(self.p*other,self.lo)
    __rmul__=__mul__
    def __truediv__(self,other):return Laurent(self.p*(arb(1)/other),self.lo)
    def reverse(self):return Laurent(self.p.coeffs()[::-1],-self.hi)
    def norm(self):return sum((abs(v) for v in self.p.coeffs()),arb(0)).upper()
    def zero_product(self,other):
        j=-self.lo-other.lo;p=self.p*other.p
        return p[j] if 0<=j<len(p) else arb(0)


def real(value,name):
    z=acb(value)
    if not z.imag.contains(0):raise ValueError('true real scalar lost reality: '+name)
    return z.real


def imaginary_phase(coefficients):
    n=len(coefficients);v=[arb(0) for _ in range(2*n+1)]
    for j,a in enumerate(coefficients,1):v[n+j]=a/2;v[n-j]=-a/2
    return Laurent(v,-n)


def exponential_jets(A,goal):
    """Full Laurent exponential by two exact one-sided formal series.

    Their omitted Fourier tails are bounded in the complete weighted
    Wiener algebra, independently of the formal-series implementation.
    """
    n0=max(-A[0].lo,A[0].hi)
    positive=[arb(0)]+[A[0][j] for j in range(1,n0+1)]
    negative=[arb(0)]+[A[0][-j] for j in range(1,n0+1)]
    Mpos=sum((abs(z) for z in positive),arb(0)).upper()
    Mneg=sum((abs(z) for z in negative),arb(0)).upper()
    choices=[]
    for width in (Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
        w=exact_arb(width)
        Mp=sum((abs(z)*(j*w).exp() for j,z in enumerate(positive)),arb(0)).upper()
        Mn=sum((abs(z)*(j*w).exp() for j,z in enumerate(negative)),arb(0)).upper()
        logfee=(Mp+Mneg).union(Mn+Mpos).upper()+arb(2).log()
        estimate=max(n0,int(math.ceil(float(((logfee-goal.log())/w).upper()))))
        fee=((Mp+Mneg).exp()+(Mn+Mpos).exp()).upper()
        while not fee*(-w*(estimate+1)).exp()<goal:estimate+=1
        choices.append((estimate,width,fee))
    n,width,fee=min(choices,key=lambda x:x[0]);w=exact_arb(width)
    if n>4096:raise ValueError('the explicit positive-frequency exponential limit is exceeded')
    tail=(fee*(-w*(n+1)).exp()).upper()
    previous=ctx.cap;ctx.cap=n+1
    try:
        ep=arb_series(positive,prec=n+1).exp()
        en=arb_series(negative,prec=n+1).exp()
        E=Laurent([ep[j] for j in range(n+1)],0)*Laurent([en[j] for j in range(n,-1,-1)],-n)
    finally:ctx.cap=previous
    # exp(A(t)-A0) has finite normalized radial Bell coefficients.
    bell=[Laurent.constant(1)]
    for j in range(1,len(A)):
        z=Laurent.constant(0)
        for k in range(1,j+1):z=z+k*(A[k]*bell[j-k])
        bell.append(z/j)
    return [E*z for z in bell],[(tail*z.norm()).upper() for z in bell],n,tail


class FullArbScalarTarget:
    def __init__(self,object_path,half_width=Fraction(0),exponential_bits=160,jet_order=7):
        self.object_path=Path(object_path);self.half_width=Fraction(half_width)
        self.jet_order=int(jet_order)
        if not 3<=self.jet_order<=12:raise ValueError('an explicit supported high scalar jet order is required')
        self.radial_count=self.jet_order+3
        self.original=MetricDefectTarget(object_path,self.half_width,512)
        self.cuts=sorted(set(common_cells(self.original))|{Fraction(1,20),Fraction(9,50)})
        self.goal=arb(2)**(-int(exponential_bits));self.exponential_bits=int(exponential_bits)
        self.evaluations=0;self.last_details=None;self.scalar_germs={}
        t=self.original
        self.maximum_scalar_degree=max(t.raw.degree+3*t.base.degree,
            t.raw_direction.degree+3*t.base.degree,t.shift.degree,
            *(sp.degree for sp in t.means),*(sp.degree for sp in t.height_integrals))
        if self.maximum_scalar_degree!=20:
            raise ValueError('the exact finite scalar-polynomial degree identity changed')

    def complete_scalar_jets(self,left,right,gl,gr):
        key=gl,gr,ctx.prec
        if key not in self.scalar_germs:
            # Only the exact spline germ is needed. Bypass the double-box
            # field cache, which is neither read nor used by this provider.
            BulkTarget.set_cell(self.original,gl,gr)
            anchor=(gl+gr)/2;previous=ctx.cap;ctx.cap=self.maximum_scalar_degree+1
            try:
                groups=self.original.scalars(acb(exact_arb(anchor)),1)
                flattened=[*groups[0],*groups[1],groups[2],groups[3]]
                polynomials=[[real(p[j],f'exact scalar {i},{j}')
                    for j in range(self.maximum_scalar_degree+1)] for i,p in enumerate(flattened)]
            finally:ctx.cap=previous
            self.scalar_germs[key]=(anchor,polynomials)
        anchor,polynomials=self.scalar_germs[key]
        count=self.radial_count
        delta=arb_series([real_interval(left,right)-exact_arb(anchor),1],prec=count)
        output=[]
        for polynomial in polynomials:
            value=arb_series([polynomial[-1]],prec=count)
            for coefficient in polynomial[-2::-1]:value=coefficient+delta*value
            output.append([value[j] for j in range(count)])
        n=self.original.modes
        beta=[[output[k][d] for k in range(n)] for d in range(count)]
        vertical=[[output[n+k][d] for k in range(n)] for d in range(count)]
        return beta,vertical,output[-2],output[-1]
    def coefficients(self,left,right,nu):
        left,right,nu=Fraction(left),Fraction(right),Fraction(nu)
        if not 0<=left<=right<Fraction(1,2):raise ValueError('this phase provider only serves the actual near-body interval')
        j=bisect_right(self.cuts,left)-1;gl,gr=self.cuts[j:j+2]
        if not gl<=left<=right<=gr:raise ValueError('a scalar model crosses a genuine target/bump germ')
        oldcap=ctx.cap;ctx.cap=self.radial_count
        try:
            radial=acb(real_interval(left,right))
            count=self.radial_count;n=self.original.modes
            b,g,aa,zz=self.complete_scalar_jets(left,right,gl,gr)
            phases=[];errors=[];degrees=[];tails=[]
            for sign in (1,-1,0):
                coefficients=[[g[d][k] if sign==0 else b[d][k]+sign*g[d][k]
                    for k in range(n)] for d in range(count)]
                E,e,degree,tail=exponential_jets([imaginary_phase(z) for z in coefficients],self.goal)
                phases.append(E);errors.append(e);degrees.append(degree);tails.append(tail)
            P=[];epsP=[]
            for d in range(count):
                cos=[];sinI=[]
                for p in phases:
                    rev=p[d].reverse();cos.append((p[d]+rev)/2);sinI.append((rev-p[d])/2)
                tx=-(sinI[0]+sinI[1])/2
                ty=(cos[0]+cos[1])/2-(1 if d==0 else 0)
                tz=sinI[2]
                lo=min(tx.lo,ty.lo,tz.lo);hi=max(tx.hi,ty.hi,tz.hi)
                px=[];py=[];pz=[]
                for k in range(lo,hi+1):
                    frequency=4*k;denominator=1-frequency*frequency
                    px.append((-frequency*tx[k]+ty[k])/denominator)
                    py.append((-tx[k]+frequency*ty[k])/denominator if k else arb(0))
                    pz.append(tz[k]/frequency if k else arb(0))
                P.append([Laurent(px,lo),Laurent(py,lo),Laurent(pz,lo)])
                ex=(errors[0][d]+errors[1][d])/2;ey=ex;ez=errors[2][d]
                epsP.append([(arb(4)*ex/15+ey).upper(),(ex/15+arb(4)*ey/15).upper(),(ez/4).upper()])
            F=[];epsF=[]
            for d in range(count):
                row=[];fee=[]
                for component in range(3):
                    value=Laurent.constant(aa[d] if component==0 else zz[d] if component==2 else 0)
                    err=arb(0)
                    for h in range(d+1):
                        value=value+aa[d-h]*P[h][component]
                        err+=abs(aa[d-h])*epsP[h][component]
                    row.append(value);fee.append(err.upper())
                F.append(row);epsF.append(fee)
            norms=[[p.norm() for p in row] for row in F]
            energy=[];energy_error=[]
            for d in range(count-1):
                value=arb(0);fee=arb(0)
                for i in range(d+1):
                    p,q=i+1,d-i+1;weight=p*q
                    for component in range(3):
                        sign=-1 if component==1 else 1
                        value+=sign*weight*F[p][component].zero_product(F[q][component])
                        fee+=weight*(norms[p][component]*epsF[q][component]
                            +norms[q][component]*epsF[p][component]+epsF[p][component]*epsF[q][component])
                energy.append(value+arb(0,fee.upper()));energy_error.append(fee.upper())
            a=arb_series(aa,prec=count);E=arb_series(energy,prec=count-1);r=arb_series([radial.real,1],prec=count-1)
            beta_series=a.derivative()/a
            Kold=-a.derivative().derivative()/(a*E)+a.derivative()*E.derivative()/(2*a*E*E)
            cl,cr=Fraction(1,20),Fraction(9,50)
            if right<=cl or left>=cr:w=arb_series([0])
            else:
                if left<cl or right>cr:raise ValueError('a complete interval crosses the compact control seam')
                t=(r-exact_arb(cl))/exact_arb(cr-cl);w=4096*t**6*(1-t)**6
            factor=(exact_arb(nu)*w).exp();En=E*factor
            K=(Kold+exact_arb(nu)*beta_series*w.derivative()/(2*E))/factor
            gap=En-a.derivative()**2
            if not a[0]>0 or not En[0]>0 or not gap[0]>0:
                raise ValueError('the entire true scalar interval lacks positive denominators')
            gamma=En.sqrt()/a
            s=-a*(En/gap).sqrt()
            values=dict(a=a[0],E=E[0],controlled_E=En[0],rotational_gap=gap[0])
            for name,series in (('beta',beta_series),('gamma',gamma),('K',K),('s',s)):
                if series.prec<self.jet_order+1:raise ValueError('the declared complete high scalar jet is incomplete')
                for d in range(self.jet_order+1):values[name+(str(d) if d else '')]=math.factorial(d)*series[d]
            self.evaluations+=1
            self.last_details=dict(one_sided_exponential_frequency_cutoffs=degrees,exponential_tail_A0=[record(z) for z in tails],
                complete_energy_series_remainders=[record(z) for z in energy_error],
                full_angular_exponential_error_not_grid_alias=True,
                actual_phase_modes=n,maximum_exact_scalar_degree=self.maximum_scalar_degree,
                complete_scalar_jet_order=self.jet_order,
                complete_scalar_polynomials_reorganized_before_interval_evaluation=True,
                highest_finite_primitive_mode=max(p.hi for row in P for p in row))
            return values,(gl,gr)
        finally:ctx.cap=oldcap


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,required=True)
    ap.add_argument('--left',type=Fraction,required=True);ap.add_argument('--right',type=Fraction)
    ap.add_argument('--nu',type=Fraction,default=Fraction(-2572625729470897,72057594037927936))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(0))
    ap.add_argument('--bits',type=int,default=192);ap.add_argument('--exponential-bits',type=int,default=160)
    ap.add_argument('--jet-order',type=int,default=7)
    ap.add_argument('--compare-existing',action='store_true')
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=args.bits;ctx.cap=6;started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every genuine scalar-provider attempt')
    right=args.left if args.right is None else args.right
    target=FullArbScalarTarget(args.object,args.half_width,args.exponential_bits,args.jet_order)
    values,germ=target.coefficients(args.left,right,args.nu)
    native=dict(kind='actual_complete_Arb_Laurent_exponential_scalar_jets',complete=True,
        source_sha256=sha(__file__),object_sha256=sha(args.object),interval=list(map(str,(args.left,right))),
        actual_scalar_germ=list(map(str,germ)),half_width=str(args.half_width),nu=str(args.nu),
        coefficients={k:record(v) for k,v in values.items()},details=target.last_details,
        no_Fourier_frequency_tail_discarded=True,no_angular_grid_used=True,
        whole_negative_cover=False,flow_or_conjugacy_proved=False)
    if args.compare_existing:
        from fourfold_codazzi_reciprocal_compact_target_jets import ReciprocalCompactTargetJets
        existing=ReciprocalCompactTargetJets(args.object,args.half_width,512)
        old,oldg=existing.coefficients(args.left,right,args.nu)
        overlap={k:bool(v.overlaps(old[k])) for k,v in values.items() if k in old}
        native['existing_complete_provider_comparison']=dict(germ=list(map(str,oldg)),overlap=overlap,
            all_overlap=all(overlap.values()))
        if not all(overlap.values()):native['complete']=False
    native['seconds']=time.monotonic()-started;save(args.out,native)
    print(dict(complete=native['complete'],seconds=native['seconds'],details=target.last_details,
        coefficients={k:v.str(20) for k,v in values.items() if k in ('K','K1','gamma','beta','s')}),flush=True)
    if not native['complete']:raise RuntimeError('the exact complete provider comparison failed')


if __name__=='__main__':main()
