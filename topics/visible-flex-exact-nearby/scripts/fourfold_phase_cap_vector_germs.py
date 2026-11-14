#!/usr/bin/env python3
"""Same directed scalar polynomial algebra, with vectorized coefficient updates.

The additions for each polynomial coefficient retain their original order.
No floating convolution, FFT, or unchecked polynomial approximation is used.
Only the current common-cell polynomial cache is kept.
"""
from fractions import Fraction
import numpy as np
from fourfold_phase_beta_bulk_box import zeros
from fourfold_phase_cap_energy_interval import BodyForm
from fourfold_phase_cap_scaled_body import ScaledBodyForm
from fourfold_phase_cap_wiener_box import WienerBodyForm


def derivative(poly):
    return poly[1:]*np.arange(1,len(poly.real.lo))


def multiply(left,right):
    nl,nr=len(left.real.lo),len(right.real.lo)
    result=zeros((nl+nr-1,))
    for i in range(nl):
        result[i:i+nr]=result[i:i+nr]+left[i]*right
    return result


def subtract(left,right):
    nl,nr=len(left.real.lo),len(right.real.lo)
    result=zeros((max(nl,nr),))
    result[:nl]=result[:nl]+left
    result[:nr]=result[:nr]-right
    return result


class VectorScalarRatios:
    def set_cell(self,left,right):
        cell=Fraction(left),Fraction(right)
        if self.cell!=cell:
            self.fast_cell_cache.clear();self.span_cache.clear()
        previous=self.cell
        # Call the unchanged native scalar-germ layer, then replace only the
        # small polynomial arithmetic used to organize exact scalar ratios.
        BodyForm.set_cell(self,*cell)
        if previous==cell and hasattr(self,'ratio_polynomials'):
            return
        a,z=self.scalar_poly[:,-2],self.scalar_poly[:,-1]
        ar,zr=derivative(a),derivative(z)
        arr,zrr=derivative(ar),derivative(zr)
        aa=multiply(a,a)
        l0=float((ar[0]/a[0]).to_acb().real.mid())
        c0=float((zr[0]/(a[0]*a[0])).to_acb().real.mid())
        self.ratio_polynomials=dict(L0=l0,C0=c0,
            L_remainder=subtract(ar,l0*a),C_remainder=subtract(zr,c0*aa),
            Lprime_numerator=subtract(multiply(a,arr),multiply(ar,ar)),
            Cprime_numerator=subtract(multiply(a,zrr),2*multiply(ar,zr)))


class VectorScaledBodyForm(VectorScalarRatios,ScaledBodyForm):
    pass


class VectorWienerBodyForm(VectorScalarRatios,WienerBodyForm):
    pass
