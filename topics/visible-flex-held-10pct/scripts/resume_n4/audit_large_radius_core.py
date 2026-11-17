#!/usr/bin/env python3
"""Exact rational bounds for the eta=1, pi/4-centered local circular core.

This certifies only the planar core and an R19 conditional window.  It does
not certify a nonlinear prefix, tail, closed embedding, diameter or reach.
All decimal input constants below are exact rationals.  No floating point
trigonometric evaluation is used by the bounds.
"""
import argparse
import json
import math
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F

A=F(147,1000); B=F(2,25); ETA=F(1); C=F(45)
CHI={0:1,5:-126,6:420,7:-540,8:315,9:-70}
ORDER=60

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def point(x):return (F(x),F(x))
def mul(x,y):
    z=[a*b for a in x for b in y];return (min(z),max(z))
def scale(x,s):return mul(x,point(s))
def div(x,y):
    if y[0]<=0<=y[1]:raise ValueError('Interval division by zero')
    return mul(x,(1/y[1],1/y[0]))
def pi_bounds(terms=100):
    def atan(d):
        s=sum((F((-1)**j,(2*j+1)*d**(2*j+1)) for j in range(terms)),F(0))
        r=F((-1)**terms,(2*terms+1)*d**(2*terms+1))
        return (min(s,s+r),max(s,s+r))
    return sub(scale(atan(5),16),scale(atan(239),4))
def moment(m):
    # Integral chi(x)*x^m from 0 to a+b; transition x=a+b*t.
    out=A**(m+1)/(m+1)
    for j in range(m+1):
        inner=sum((F(c,j+k+1) for k,c in CHI.items()),F(0))
        out+=B*math.comb(m,j)*A**(m-j)*B**j*inner
    return out
MOMENTS=[moment(m)for m in range(ORDER+1)]
def trig_moment(k,sine=False):
    parity=1 if sine else 0
    s=sum((F((-1)**((m-parity)//2)*k**m,math.factorial(m))*MOMENTS[m]
           for m in range(parity,ORDER+1,2)),F(0))
    # Taylor theorem on [0,a+b], using 0<=chi<=1 and integral chi=a+b/2.
    remainder=(A+B/2)*(k*(A+B))**(ORDER+1)/math.factorial(ORDER+1)
    return s-remainder,s+remainder
def sin_bounds(x):
    s=sum((F((-1)**j,math.factorial(2*j+1))*x**(2*j+1)for j in range(24)),F(0))
    r=abs(x)**49/math.factorial(49)
    return s-r,s+r
def sqrt_bounds(x,digits=65):
    s=10**digits;k=math.isqrt(x.numerator*s*s//x.denominator)
    return F(k,s),F(k+1,s)
def decimal_bound(x,upper=False):
    with localcontext()as c:
        c.prec=42;c.rounding=ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def show(x):return [decimal_bound(x[0]),decimal_bound(x[1],True)]

def calculate():
    pi=pi_bounds();cm={k:trig_moment(k)for k in [1,3,4,5,7,8,9]}
    sm={k:trig_moment(k,True)for k in [1,3,5,7,9]}
    mass=A+B/2
    integral=sub(point(C*mass),scale(add(scale(cm[4],2),cm[8]),15))
    beta=neg(div(integral,sub(scale(pi,F(1,4)),point(mass))))
    i0=add(cm[1],sm[1])
    p4=add(add(cm[3],cm[5]),sub(sm[5],sm[3]))
    p8=add(add(cm[7],cm[9]),sub(sm[9],sm[7]))
    i1=sub(scale(i0,C),scale(add(scale(p4,2),p8),F(15,2)))
    support_correction=add(beta,sub(i1,mul(beta,i0)))
    center_per_q=sub(point(C+F(47,21)),support_correction)
    rows=[]
    for q in [F(1,50),F(11,500)]:
        radius=1+C*q;center=scale(center_per_q,q)
        alpha=2*radius*A-F(1,1000);phase=alpha/(2*radius)
        shift=scale(mul(center,sin_bounds(phase)),2)
        lower=add(point(1-F(45,2)*q),scale(beta,q))
        rows.append(dict(q=str(q),radius=str(radius),circle_center_norm=show(center),
            support_at_circle_axis=show(sub(point(radius),center)),
            rho_global_lower=show(lower),rho_global_upper=str(radius),
            core_curvature_upper=show(div(point(1),lower)),
            alpha=str(alpha),phase_angle=str(phase),held_shift_lower=show(shift),
            held_ratio_if_D_2p65=show(scale(shift,F(20,53))),
            common_I=[str(alpha-radius*A+F(1,4000)),str(radius*A-F(1,4000))],
            common_I_width=str(F(1,2000)),R_times_vu=str(radius*F(7,20)),
            round_patch_root_lower=str(1-(radius*F(7,20))**2)))
    # Conservative lower bound for the complete initial negative-K ramp.
    # The exact-rational profile is the declared decimal of the actual
    # numerical physical design, not an interval enclosure of an unknown root.
    delta=F('0.030016271561983967');vu=F(7,20);eps=F(9,20);eta=F(1,20)
    tu=delta/(vu*(1-eps));amax=1+delta*eps/(2*(1-eps))
    accelmax=vu/(eps*tu*(1-eta))
    window_lower=div(point(vu),sqrt_bounds(amax*accelmax))
    assert beta[1]<0 and center_per_q[0]>0
    assert window_lower[0]>A
    assert all(F(r['rho_global_lower'][0])>0 for r in rows)
    assert all(F(r['held_ratio_if_D_2p65'][0])>F(1,10) for r in rows)
    return dict(scope=__doc__,halfwidth=str(A),transition=str(B),eta=str(ETA),
        cutoff='1 - 126t^5 + 420t^6 - 540t^7 + 315t^8 - 70t^9',
        trigonometric_taylor_order=ORDER,machin_terms=100,
        beta=show(beta),support_correction_at_axis=show(support_correction),
        center_norm_per_q=show(center_per_q),rows=rows,
        profile_initial_window=dict(delta=str(delta),vu=str(vu),ramp=str(eps),ramp_eta=str(eta),
            total_material_loss_div_R_lower=show(window_lower),required_normal_halfwidth=str(A),
            first_positive_K=str((1-eps)*tu)),
        conditional_common_cylinder_length=str(F(27,50)),
        conditional_held_set_diameter_ratio=str(F(54,265)),
        conditional_reach_ratio_if_support_ge_0p08_K_le_12p5=str(F(8,265)),
        boundary='No complementary controls included in the global rho bound. Compact support controls at lambda=1 preserve c and R but need their own rho bound. All full-surface hypotheses of R19 remain unpaid.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out');a=p.parse_args()
    result=calculate();s=json.dumps(result,indent=2)+'\n'
    if a.out:
        with open(a.out,'w')as f:f.write(s)
    print(s,end='')
