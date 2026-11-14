#!/usr/bin/env python3
"""Deterministic three-harmonic core optimization and rational extrema audit.

Only planar core design is covered. No closed surface, no global reach and
no preservation of a witness along a complete physical prefix is asserted.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,hashlib,json,math
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.optimize import linprog


def frac(x):return x if isinstance(x,Q)else Q(str(x))


@dataclass(frozen=True)
class I:
    lo:Q
    hi:Q
    def __init__(self,lo,hi=None):
        lo=frac(lo);hi=lo if hi is None else frac(hi)
        if hi<lo:raise ValueError('Reversed interval')
        object.__setattr__(self,'lo',lo);object.__setattr__(self,'hi',hi)
    def __add__(self,other):
        z=asI(other);return I(self.lo+z.lo,self.hi+z.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,other):return self+-asI(other)
    def __rsub__(self,other):return asI(other)+-self
    def __mul__(self,other):
        z=asI(other);v=[self.lo*z.lo,self.lo*z.hi,self.hi*z.lo,self.hi*z.hi];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,other):
        z=asI(other)
        if z.lo<=0<=z.hi:raise ZeroDivisionError('Interval contains zero')
        return self*I(1/z.hi,1/z.lo)
    def __rtruediv__(self,other):return asI(other)/self
    def __pow__(self,n):
        if n<0:return I(1)/(self**(-n))
        if n==0:return I(1)
        if n%2==0:
            v=[self.lo**n,self.hi**n];return I(0 if self.lo<=0<=self.hi else min(v),max(v))
        return I(self.lo**n,self.hi**n)
    def absolute(self):
        return I(0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi)),max(abs(self.lo),abs(self.hi)))
    def mid(self):return float((self.lo+self.hi)/2)


def asI(x):return x if isinstance(x,I)else I(x)
def sqrtQ(q,bits=160):
    q=frac(q)
    if q<0:raise ValueError('Negative square root')
    scale=1<<bits;n=math.isqrt(q.numerator*q.denominator*scale*scale);den=q.denominator*scale
    lo=Q(n,den)
    return I(lo,lo if lo*lo==q else Q(n+1,den))
def sqrtI(v):
    v=asI(v);return I(sqrtQ(v.lo).lo,sqrtQ(v.hi).hi)
def pack(v):
    v=asI(v);return dict(lower=str(v.lo),upper=str(v.hi),lower_float=float(v.lo),upper_float=float(v.hi))
def poly_eval(coeff,x):
    out=I(0)
    for c in reversed(coeff):out=out*x+c
    return out


def rational_extrema(coeff):
    """All extrema of a rational polynomial of degree at most three on [-1,1]."""
    p=list(map(frac,coeff))+[Q(0)]*(4-len(coeff));A,B,C=3*p[3],2*p[2],p[1]
    roots=[]
    if A:
        D=B*B-4*A*C
        if D>=0:
            s=sqrtQ(D);roots=[(-I(B)+s)/(2*A),(-I(B)-s)/(2*A)]
    elif B:roots=[I(-C/B)]
    entries=[dict(kind='left endpoint',x=I(-1)),dict(kind='right endpoint',x=I(1))]
    for root in roots:
        if root.hi<-1 or root.lo>1:continue
        if root.lo<-1 or root.hi>1:raise ValueError('Critical interval meets domain endpoint; increase precision or handle equality')
        if not any(root.lo==row['x'].lo and root.hi==row['x'].hi for row in entries):entries.append(dict(kind='stationary point',x=root))
    for row in entries:row['value']=poly_eval(p,row['x'])
    lower=min(row['value'].lo for row in entries);upper=max(row['value'].hi for row in entries)
    return I(lower,upper),[dict(kind=row['kind'],x=pack(row['x']),value=pack(row['value']))for row in entries]


def rho_coeff(v):
    a,b,c=v;return [1+15*b,-3*a+105*c,-30*b,-140*c]


def float_extrema(v):
    a,b,c=v
    if abs(c)>1e-15:roots=np.roots([-420*c,-60*b,-3*a+105*c])
    elif abs(b)>1e-15:roots=[-a/(20*b)]
    else:roots=[]
    xs=np.asarray([-1.,1.]+[float(np.real(x))for x in roots if abs(np.imag(x))<1e-9 and -1<np.real(x)<1])
    vals=1+15*b+(-3*a+105*c)*xs-30*b*xs*xs-140*c*xs**3
    return xs,vals


def exchange_lp(r,R,sign='free'):
    """Finite LP with cubic-extrema separation, deterministic mesh and solver."""
    points=list(np.cos(np.arange(65)*np.pi/64));history=[];last=None
    for iteration in range(24):
        x=np.asarray(points);P=np.c_[-3*x,15-30*x*x,105*x-140*x**3]
        A=np.r_[P,-P,[[-1.,0.,-9.]]];B=np.r_[np.full(len(x),R-1),np.full(len(x),1-r),0.]
        bound=(0,None)if sign=='nonnegative'else(None,0)if sign=='nonpositive'else(None,None)
        result=linprog([-1,0,-1],A_ub=A,b_ub=B,bounds=[(0,None),(None,None),bound],method='highs',
            options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-10))
        if not result.success:raise RuntimeError(result.message)
        xx,yy=float_extrema(result.x);violation=max(0.,r-float(yy.min()),float(yy.max())-R)
        history.append(dict(iteration=iteration,linear_constraints=len(B),coefficients=result.x.tolist(),gap=float(2*(result.x[0]+result.x[2])),continuous_polynomial_violation=violation))
        if violation<=2e-10:break
        new=[float(z)for z in xx if all(abs(z-t)>1e-13 for t in points)]
        if not new:break
        points.extend(new);last=result
    return dict(method='deterministic Chebyshev65 LP + exact-form cubic stationary-point separation in floating arithmetic; the algebraic dual theorem is the independent global certificate',sign=sign,coefficients=result.x.tolist(),gap=float(2*(result.x[0]+result.x[2])),continuous_violation=violation,history=history)


def analytic_optimum(r,R,k0=Q(9,20),margin=Q(49,50)):
    r,R=frac(r),frac(R);X=(19+sqrtQ(Q(1481)))/70;q=2*X*X-1;A=3*(q+X)
    B=1-r-q;C=margin*A/(2*k0);gate_radius=2*C/(B+sqrtI(B*B+4*q*C))
    if R<=gate_radius.lo:u=I(R);active=False
    elif R>=gate_radius.hi:u=gate_radius;active=True
    else:raise ValueError('Cap lies in the very narrow algebraic uncertainty interval')
    k=(u-r)/(1+X)**2;U=(1-r-k*X)/(X*X-X+Q(1,2));V=U-k
    c=-V/140;b=(2*V*X-U)/30;a=(2*U*X-V*X*X-Q(3,4)*V)/3
    d=2*(a+c);axisplus=r+(1-X)**2*(U+V)
    factor_min=U-V.absolute();derivative_factor_min=2*U-V*X-3*V.absolute()
    checks=dict(factor_positive=factor_min.lo>0,derivative_factor_positive=derivative_factor_min.lo>0,
        right_endpoint_below_cap=axisplus.hi<=R,a_positive=a.lo>0,negative_c_gap_condition=(a+9*c).lo>0,endpoint_upper_below_R=u.hi<=R)
    if not all(checks.values()):raise AssertionError('Closed-form extremizer needs a different contact pattern')
    v=np.array([z.mid()for z in (a,b,c)]);product=k0*d*u
    return dict(r=str(r),R=str(R),xi=pack(X),q=pack(q),A=pack(A),gate_effective_R=pack(gate_radius),gate_active=active,
        coefficients_exact_definition='rho=r+(x-xi)^2(U+V*x); k=(u-r)/(1+xi)^2; U=(1-r-k*xi)/(xi^2-xi+1/2); V=U-k; c=-V/140; b=(2Vxi-U)/30; a=(2Uxi-Vxi^2-3V/4)/3',
        coefficients={name:pack(value)for name,value in zip(('a','b','c'),(a,b,c))},coefficients_float=v.tolist(),gap=pack(d),minor_rho=pack(u),major_rho=pack(axisplus),
        factor_min=pack(factor_min),derivative_factor_min=pack(derivative_factor_min),checks=checks,
        witness_product=pack(product),witness_equality_by_quadratic_definition=active,
        D_gap=pack(5*d),D_local_budget=str(r/Q(3,100)),D_combined_budget=min(5*d.mid(),float(r/Q(3,100))))


def candidate(name,coef,r,R,k0=Q(9,20),margin=Q(49,50)):
    a,b,c=map(frac,coef);r,R=frac(r),frac(R);interval,extrema=rational_extrema(rho_coeff((a,b,c)));d=2*(a+c);minor=1+3*a-15*b+35*c
    hprime_range,hprime_extrema=rational_extrema([a-3*c,4*b,12*c]);product=k0*d*minor
    if not(interval.lo>=r and interval.hi<=R and a>=0 and (c>=0 or a+9*c>=0) and product<=margin):raise AssertionError('Rational candidate violates a requested constraint')
    if hprime_range.lo<=0:raise AssertionError('This candidate needs a separate core diameter calculation')
    return dict(name=name,coefficients={key:str(value)for key,value in zip(('a','b','c'),(a,b,c))},constraints=dict(r=str(r),R=str(R),k0=str(k0),witness_margin_limit=str(margin)),
        rho_polynomial=[str(z)for z in rho_coeff((a,b,c))],rho_range=pack(interval),rho_extrema=extrema,h_x_range=pack(hprime_range),h_x_extrema=hprime_extrema,
        gap=str(d),gap_float=float(d),minor_rho=str(minor),witness_product=str(product),witness_product_float=float(product),witness_margin_to_1=str(1-product),
        witness_margin_to_requested=str(margin-product),k0_critical=str(1/(d*minor)),k0_critical_float=float(1/(d*minor)),a_plus_9c=str(a+9*c),
        major_radius=str(1+a+b+c),minor_radius=str(1-a+b-c),core_diameter=str(2*(1+a+b+c)),core_diameter_float=float(2*(1+a+b+c)),
        D_gap=str(5*d),D_gap_float=float(5*d),D_local_conservative=str(r/Q(3,100)),D_local_from_verified_min_lower=str(interval.lo/Q(3,100)),
        D_combined_conservative=str(min(5*d,r/Q(3,100))),D_combined_conservative_float=float(min(5*d,r/Q(3,100))),
        homothetic_law=dict(b_over_a=str(b/a),c_over_a=str(c/a)),
        cubic_law=dict(definition='b(a)=-a/(10sqrt(2)) + B3*a^3, c(a)=C3*a^3; endpoint matching is exact, this does not fit the current solved BVP branch.',
            B3=(float(b)+float(a)/(10*math.sqrt(2)))/float(a)**3,C3=float(c/a**3)),
        scope='Verified convex planar core only. D_gap and D_local are necessary/conditional future whole-surface budgets, not a measured closed diameter or a reach certificate.')


def comparisons():
    out=[]
    for r in (Q(13,100),Q(3,20)):
        R=2.5;amax=min((R-1)/(3+3/(2*math.sqrt(2))),(1-float(r))*math.sqrt(2)/3)
        out.append(dict(family='R1 minimum-curvature-optimal b=-a/(10sqrt2), with R=2.5 imposed',r=str(r),a=amax,gap=2*amax,rho_min=1-3*amax/math.sqrt(2),rho_max=1+3*amax+3*amax/(2*math.sqrt(2))))
    for N in (2,3,4):
        r=Q(3,20);den=math.comb(2*N,N)
        coef=[Q(2)*(1-r)*(-1)**j*math.comb(2*N,N-j)/(den*(1-4*j*j))for j in range(1,N+1)]
        d=2*sum(coef[::2]);R=r+(1-r)*Q(4**N,den);w=Q(9,20)*d*R
        out.append(dict(family='R2 power core',N=N,r=str(r),coefficients=list(map(str,coef)),gap=str(d),gap_float=float(d),rho_max=str(R),rho_max_float=float(R),witness_product=str(w),witness_product_float=float(w),k0_045_witness_gate_passes=w<=Q(49,50)))
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--anchor',type=Path,default=Path('notes/alternative-neck-k7-v098-q070-m18.json.gz'));a=p.parse_args()
    cases=[]
    for r,R in [(Q(13,100),Q(5,2)),(Q(3,20),Q(5,2)),(Q(13,100),Q(13,5)),(Q(3,20),Q(13,5)),(Q(3,20),Q(267,100))]:
        row=analytic_optimum(r,R)
        if not row['gate_active']:
            row['lp_checks']={sign:exchange_lp(float(r),float(R),sign)for sign in ('free','nonnegative','nonpositive')}
        cases.append(row)
    defs=[('negative_R250_r015',('391/1000','-9/400','-9/25000'),'3/20','5/2'),
          ('negative_R250_r013',('397/1000','-439/20000','-31/50000'),'13/100','5/2'),
          ('positive_R260_r015',('2/5','-257/10000','7/20000'),'3/20','13/5'),
          ('positive_near_witness_r015',('813/2000','-139/5000','41/50000'),'3/20','267/100')]
    candidates=[candidate(*d)for d in defs];anchor=None
    if a.anchor.exists():
        raw=a.anchor.read_bytes();data=json.loads(gzip.decompress(raw)if a.anchor.suffix=='.gz'else raw);v=np.array(data['core']['coefficients'][:3]);xs,rs=float_extrema(v)
        anchor=dict(file=str(a.anchor.resolve()),sha256=hashlib.sha256(raw).hexdigest(),first_three=v.tolist(),truncated_rho_min=float(rs.min()),truncated_rho_max=float(rs.max()),
          higher_mode_curvature_majorant=float(sum(((2*j)**2-1)*abs(q)for j,q in enumerate(data['core']['coefficients'][3:],4))),
          warning='The affine paths below refer to the three-harmonic truncation; a re-solved BVP retains its higher modes and must budget their full contribution.',paths=[])
        for row in candidates:
            target=np.array([float(Q(row['coefficients'][k]))for k in ('a','b','c')]);slope=(target-v)/(target[0]-v[0]);zero=float(v[0]-v[2]/slope[2])if slope[2]else None
            anchor['paths'].append(dict(target=row['name'],formula='v(a)=v0+(a-a0)/(a_star-a0)*(v_star-v0)',db_da=float(slope[1]),dc_da=float(slope[2]),c_zero_amplitude=zero if zero is not None and v[0]<=zero<=target[0]else None,
                monotone_gap_and_minor_rho=bool(2*(target[0]+target[2])>2*(v[0]+v[2])and 1+3*target[0]-15*target[1]+35*target[2]>1+3*v[0]-15*v[1]+35*v[2])))
    result=dict(status='proved-core-optimization-and-certified-rational-candidate-data',scope=__doc__,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      assumptions=dict(a_nonnegative=True,negative_c_requires='a+9c>=0',k0='9/20',witness_product_upper='49/50'),
      optimum_cases=cases,rational_candidates=candidates,reference_comparisons=comparisons(),anchor=anchor,
      closed_surface_constructed=False,closed_diameter_measured=False,global_reach_certified=False)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),bytes=a.out.stat().st_size,optima=[dict(r=z['r'],R=z['R'],coefficients=z['coefficients_float'],d=z['gap']['lower_float'],gate_active=z['gate_active'])for z in cases],
        candidates=[dict(name=z['name'],d=z['gap_float'],rho_min=z['rho_range']['lower_float'],rho_max=z['rho_range']['upper_float'],gate=z['witness_product_float'],D_budget=z['D_combined_conservative_float'])for z in candidates])))


if __name__=='__main__':main()
