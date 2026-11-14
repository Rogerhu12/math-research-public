"""Cache the immutable right operand of interval Fourier range products.

The same midpoint/radius/gamma formula as the normal-range backend is
used. Only the constant certified trigonometric matrices are prepared
once. Their endpoint arrays are made read-only, retained by the cache,
and sliced without changing their enclosure for shorter Fourier rows.
"""
from fractions import Fraction as Q
import numpy as np


def install(consumer):
    poly=consumer.poly;I,up,down,qb=poly.I,poly.up,poly.down,poly.qbounds
    floor=float(np.ldexp(1.,-400));cache={}

    def center(a):
        lo,hi=a.lo,a.hi
        small=(np.maximum(abs(lo),abs(hi))<floor)&((lo!=0)|(hi!=0))
        if np.any(small):
            lo=lo.copy();hi=hi.copy();lo[small]=-floor;hi[small]=floor
        mid=lo/2+hi/2;raw=np.maximum(mid-lo,hi-mid)
        radius=np.zeros_like(raw);nonzero=raw>0;radius[nonzero]=up(raw[nonzero])
        return mid,radius

    def range_poly(p,trig=None):
        coefficients=consumer.coefficient_ranges(p)
        if trig is None:
            if coefficients.lo.shape[1]!=1:raise ValueError('Expected radial scalar polynomial')
            return coefficients[0,0]
        key=(id(trig),p.phase)
        if key not in cache:
            matrix=trig[p.phase]
            matrix.lo.flags.writeable=False;matrix.hi.flags.writeable=False
            bc,br=center(matrix)
            cache[key]=(trig,bc,br,abs(bc))
        retained,bc,br,absbc=cache[key]
        if retained is not trig:raise AssertionError('Trigonometry identity unexpectedly changed')
        k=coefficients.lo.shape[1]
        if k>len(bc):raise ValueError('Trigonometry omits a Fourier mode')
        bc,br,absbc=bc[:k],br[:k],absbc[:k]
        ac,ar=center(coefficients);absac=abs(ac)
        n=2*k+2;unit=Q(1,2**52)
        if n*unit>=1:raise ArithmeticError('Invalid gamma budget')
        gamma=float(qb(n*unit/(1-n*unit)).hi);tiny=max(floor,float(up(n*np.nextafter(0.,1.))))
        def pos(x,y):return up(up(x@y+tiny)/down(1-gamma))
        nominal=ac@bc;mag=pos(absac,absbc)
        radius=up(pos(absac,br)+pos(ar,absbc));radius=up(radius+pos(ar,br))
        radius=up(radius+up(up(gamma*mag)+tiny))
        result=I(down(nominal-radius),up(nominal+radius))
        if not (np.isfinite(result.lo).all() and np.isfinite(result.hi).all()):
            raise ArithmeticError('Nonfinite prepared-trigonometry range')
        return result[0]

    consumer.range_poly=range_poly
    return dict(immutable_trigonometric_rhs_cached=True,coefficient_rows_recomputed=True,
        gamma_and_outward_formula='Same normal-range interval dot-product bound',
        actual_angular_modes_discarded=False,input_normal_floor=floor,
        rhs_endpoint_arrays_read_only=True)
