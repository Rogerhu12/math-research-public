"""Retain low radial powers and enclose higher powers as a range remainder.

This is a VALUE enclosure on the current normalized radial interval [0,1].
It is safe for subsequent sums, products, angular differentiation and
range bounds. It MUST NOT be differentiated in the radial variable.
No actual field/geometry polynomial or Fourier mode is changed.
"""
import numpy as np


def install(poly,degree=12):
    if not isinstance(degree,int) or degree<0:raise ValueError('Nonnegative integer range degree required')
    original=poly.interval_convolution;I=poly.I

    def product(a,b):
        c=original(a,b)
        if c.lo.shape[0]<=degree+1:return c
        remainder=I(np.zeros(c.lo.shape[1]))
        for j in range(degree+1,c.lo.shape[0]):
            remainder=remainder+I(np.minimum(0,c.lo[j]),np.maximum(0,c.hi[j]))
        lo=c.lo[:degree+1].copy();hi=c.hi[:degree+1].copy()
        constant=I(lo[0],hi[0])+remainder;lo[0]=constant.lo;hi[0]=constant.hi
        return I(lo,hi)

    poly.interval_convolution=product
    return dict(retained_radial_degree=degree,radial_domain_exact=['0','1'],
        higher_radial_powers='Full signed range enclosure added to the same Fourier coefficient at radial degree zero',
        actual_fourier_modes_discarded=False,actual_finite_map_changed=False,
        later_radial_differentiation_permitted=False,
        later_angular_differentiation_permitted=True)
