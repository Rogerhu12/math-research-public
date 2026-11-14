#!/usr/bin/env python3
"""Horner on exact midpoint polynomials, with input balls paid separately.

Avoids repeated rectangular-ball rotation of the true root uncertainty.
Only numerical rounding remains inside Horner; an outer-time-disk Cauchy
fee encloses all coefficient/phase input uncertainties and discarded modes.
"""
from fractions import Fraction
from flint import arb,acb,acb_series,ctx
from fourfold_phase_field_time_horner import HornerPrimitive
from fourfold_phase_field_time_taylor import polynomial,pad_series


def point(value):return acb(value.real.mid(),value.imag.mid())


class CenteredHornerPrimitive(HornerPrimitive):
    def __init__(self,model,extra_bits=160):
        super().__init__(model)
        if extra_bits<0:raise ValueError('nonnegative guard precision required')
        self.extra_bits=int(extra_bits)
        self.midpoint_coefficient={}
        self.error_norm={};self.midpoint_norm={}
        for k,rows in self.coefficient.items():
            middle=[[point(row[i]) for i in range(self.m)] for row in rows]
            self.midpoint_coefficient[k]=[acb_series(row,prec=self.m) for row in middle]
            self.midpoint_norm[k]=[sum((abs(middle[c][i])*model.outer**i for i in range(self.m)),arb(0)).upper() for c in range(3)]
            self.error_norm[k]=[sum((abs(rows[c][i]-middle[c][i])*model.outer**i for i in range(self.m)),arb(0)).upper() for c in range(3)]

    def evaluate(self,theta_coefficients,degree=None):
        model=self.model;m=self.m
        values,_,_,infinite=model.image_and_X_error(theta_coefficients)
        if len(values)>m:raise ValueError('unsupported theta reference degree')
        degree=self.max_degree if degree is None else int(degree)
        if degree<0 or degree>self.max_degree:raise ValueError('invalid Fourier degree')
        middle=[point(v) for v in values]
        theta_error=sum((abs(v-mid)*model.outer**i for i,(v,mid) in enumerate(zip(values,middle))),arb(0)).upper()
        width=(abs(middle[0].imag)+sum((abs(v)*model.outer**i for i,v in enumerate(middle) if i),arb(0))).upper()
        fees=[arb(0) for _ in range(3)];discarded=[arb(0) for _ in range(3)]
        for k in self.coefficient:
            n=4*abs(k);w=(n*width).exp();growth=(n*theta_error).exp()
            for c in range(3):
                if abs(k)>degree:
                    fee=(self.midpoint_norm[k][c]+self.error_norm[k][c])*w*growth
                    discarded[c]+=fee
                else:
                    fee=(self.error_norm[k][c]*growth+self.midpoint_norm[k][c]*(growth-1))*w
                fees[c]+=fee
        oldcap,oldprec=ctx.cap,ctx.prec;ctx.cap=m;ctx.prec=oldprec+self.extra_bits
        try:
            theta=polynomial(middle,m);zp=(acb(0,4)*theta).exp();zm=(acb(0,-4)*theta).exp()
            zero=acb_series([],prec=m);plus=[zero]*3;minus=[zero]*3
            for k in range(degree,0,-1):
                pc=self.midpoint_coefficient.get(k,[zero]*3);mc=self.midpoint_coefficient.get(-k,[zero]*3)
                plus=[pc[c]+zp*plus[c] for c in range(3)]
                minus=[mc[c]+zm*minus[c] for c in range(3)]
            X=[self.midpoint_coefficient[0][c]+zp*plus[c]+zm*minus[c] for c in range(3)]
        finally:ctx.cap=oldcap;ctx.prec=oldprec
        real=all(v.imag==0 for v in values)
        X=[pad_series(X[c],infinite+fees[c],model.outer,real=real) for c in range(3)]
        return X,dict(degree=degree,guard_bits=self.extra_bits,theta_input_error=str(theta_error),
                      finite_input_and_discarded_fees=[str(v) for v in fees],
                      finite_discarded_mode_fees=[str(v) for v in discarded],infinite_primitive_fee=str(infinite))
