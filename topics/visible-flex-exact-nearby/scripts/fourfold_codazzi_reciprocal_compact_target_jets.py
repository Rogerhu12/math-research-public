#!/usr/bin/env python3
"""Complete stable compact-metric target jets for the reciprocal body chart.

The original infinite unit primitive is retained. Radius powers are
cancelled before the rotational square root, on either side of K=0.
All scalar Taylor jets are formed before interval collapse. A cell must
stay inside one original scalar germ and one compact-bump polynomial piece.
This provider proves coefficient enclosures, not a nonlinear BVP solution.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction
import math
import numpy as np
from flint import arb,acb
from fourfold_phase_metric_defect import MetricDefectTarget
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_codazzi_cubic_target_jets import CubicCodazziTarget,series_sqrt
from fourfold_codazzi_high_target_jets import series_mul,series_inv,series_dr
from fourfold_phase_beta_bulk_box import CBox,Box,cdot,reduce_box,arb_box
from fourfold_phase_beta_bulk_interval import exact_arb,real_interval


def real(value,name):
    z=value.to_acb() if hasattr(value,'to_acb') else acb(value)
    if not z.imag.contains(0):raise ValueError('a true target jet lost reality: '+name)
    if not z.real.is_finite():raise ValueError('a true target jet is nonfinite: '+name)
    return z.real


def add(a,b):
    return [a[i]+b[i] for i in range(min(len(a),len(b)))]


def scale(a,c):return [x*c for x in a]


def power(a,n):
    if n<0:raise ValueError('nonnegative integer series power required')
    out=[arb(1)]+[arb(0)]*(len(a)-1)
    for _ in range(n):out=series_mul(out,a)
    return out


def exponential(a):
    out=[a[0].exp()]
    for n in range(1,len(a)):
        out.append(sum((k*a[k]*out[n-k] for k in range(1,n+1)),arb(0))/n)
    return out


def bump_series(left,right,radial,count=5):
    a,b=Fraction(1,20),Fraction(9,50)
    if right<=a or left>=b:return [arb(0)]*count
    if left<a or right>b:raise ValueError('target box crosses a true compact-bump piece')
    inv=arb(100)/13
    tt=[(radial-exact_arb(a))*inv,inv]+[arb(0)]*(count-2)
    om=[1-tt[0],-tt[1]]+[arb(0)]*(count-2)
    return scale(series_mul(power(tt,6),power(om,6)),arb(4096))


class ReciprocalCompactTargetJets(MetricDefectTarget):
    # This already-paid unit-primitive routine supplies six actual radial
    # derivatives using the same complete scalar germs and directed FFT.
    unit_finite_data=CubicCodazziTarget.unit_finite_data

    def __init__(self,object_path,half_width=Fraction(0),nodes=512):
        super().__init__(object_path,half_width,nodes)
        self.cuts=common_cells(self)

    def coefficients(self,left,right,nu):
        left,right,nu=Fraction(left),Fraction(right),Fraction(nu)
        if not 0<=left<=right<=Fraction(3,2):
            raise ValueError('the new reciprocal body provider covers only [0,3/2]')
        j=bisect_right(self.cuts,left)-1;gl,gr=self.cuts[j:j+2]
        if not gl<=left<=right<=gr:raise ValueError('target box crosses an actual scalar germ')
        self.set_cell(gl,gr);rad=real_interval(left,right)
        primitive,radius=self.unit_finite_data(acb(rad))
        _,_,radius,height=self.last_scalar
        aa=[real(radius[i],'a'+str(i))/math.factorial(i) for i in range(6)]
        zz=[real(height[i],'z'+str(i))/math.factorial(i) for i in range(6)]
        if not aa[0]>0:raise ValueError('actual body radius positivity unresolved')
        ia=series_inv(aa);ia2=series_mul(ia,ia)
        L=series_mul(series_dr(aa),ia)
        H=series_mul(series_dr(zz),ia2)
        Ld=[math.factorial(i)*v for i,v in enumerate(L)]
        Lbox=[CBox(arb_box(x)) for x in Ld]
        # u=L*P+P_r is the exact scaled radial primitive correction.
        unit_tail=self.unit_tail_errors(acb(rad),arb(0))[0]
        epsilon=[(math.factorial(i)*unit_tail/self.tail_radius**i).upper() for i in range(6)]
        uu=[];eu=[];Mu=[]
        for order in range(5):
            value=primitive[order+1]
            fee=epsilon[order+1]
            for i in range(order+1):
                value=value+math.comb(order,i)*Lbox[i]*primitive[order-i]
                fee+=math.comb(order,i)*abs(Ld[i])*epsilon[order-i]
            uu.append(value);eu.append(fee.upper())
            # Separate three component A0 norms; the factor three in the
            # product estimate below pays all components, without assuming
            # the omitted primitive is a scalar function.
            Mu.append(arb(float(np.max(reduce_box(Box(value.magnitude_upper())).hi))).upper())
        rev=(-np.arange(self.nodes))%self.nodes
        energy=[];energy_fees=[]
        for order in range(5):
            finite=CBox(0.);fee=arb(0)
            for i in range(order+1):
                choose=math.comb(order,i);q=order-i
                finite+=2*choose*Lbox[i]*uu[q][0,0]
                finite+=choose*cdot(uu[i],uu[q][rev]).sum()
                fee+=2*choose*abs(Ld[i])*eu[q]
                fee+=3*choose*(Mu[i]*eu[q]+Mu[q]*eu[i]+eu[i]*eu[q])
            value=real(finite,'scaled_energy_derivative_'+str(order))+arb(0,fee.upper())
            energy.append(value/math.factorial(order));energy_fees.append(fee.upper())
        aa2=series_mul(aa,aa);L2=series_mul(L,L);H2=series_mul(H,H)
        Ebar=add(add(L2,series_mul(aa2,H2)),energy)
        Lp,Hp,ep=series_dr(L),series_dr(H),series_dr(energy)
        numerator=add(series_mul(H2,add(L2,scale(Lp,-1))),series_mul(series_mul(L,H),Hp))
        numerator=add(numerator,scale(series_mul(add(series_mul(L,ep),
            scale(series_mul(Lp,energy),-2)),ia2),arb(1)/2))
        oldK=series_mul(numerator,power(series_inv(Ebar),2))
        hh=bump_series(left,right,rad);nuarb=exact_arb(nu)
        expnu=exponential(scale(hh,nuarb))
        # expm1 at order zero is essential outside/near the compact support.
        expminusone=[(nuarb*hh[0]).expm1()]+expnu[1:]
        G=series_mul(Ebar,expnu)
        R=add(add(H2,series_mul(energy,ia2)),
              series_mul(series_mul(Ebar,ia2),expminusone))
        if not Ebar[0]>0 or not G[0]>0 or not R[0]>0:
            raise ValueError('actual complete rotational chart positivity unresolved')
        K=series_mul(add(oldK,scale(series_mul(series_mul(series_mul(L,series_dr(hh)),ia2),
            series_inv(Ebar)),nuarb/2)),series_inv(expnu))
        gamma=series_sqrt(G)
        reciprocal=scale(series_sqrt(series_mul(G,series_inv(R))),-1)
        result=dict(a=aa[0],Ebar=Ebar[0],controlled_Ebar=G[0],controlled_scaled_gap=R[0],
            Cref=1/reciprocal[0],nu=nuarb,compact_bump=hh[0],
            complete_primitive_tail_A0=unit_tail)
        for name,series in (('gamma',gamma),('beta',L),('K',K),('s',reciprocal)):
            if len(series)<4:raise ValueError('incomplete actual third target jet')
            for order in range(4):
                result[name+(str(order) if order else '')]=math.factorial(order)*series[order]
        for i,fee in enumerate(energy_fees):result['complete_scaled_energy_error_'+str(i)]=fee
        if not all(v.is_finite() for v in result.values()):raise ValueError('nonfinite complete scalar jet')
        return result,(gl,gr)
