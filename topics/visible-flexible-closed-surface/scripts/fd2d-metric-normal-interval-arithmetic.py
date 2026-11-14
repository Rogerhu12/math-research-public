"""Conservative normal-range acceleration for the existing interval backend.

No floating-point mode is changed. Every nonzero interval contained in
[-2^-400,2^-400] is enlarged to that interval before a bulk product. True
zero midpoint radii remain zero. The existing gamma_(2n+2) error proof is
retained, with the underflow allowance INCREASED to at least 2^-400.
This changes enclosures, never the actual finite map or a Fourier mode.
"""
from fractions import Fraction as Q
import numpy as np

FLOOR=float(np.ldexp(1.,-400))


def install(poly, narrow_owner=None):
    I,up,down,qb=poly.I,poly.up,poly.down,poly.qbounds

    def centered(a):
        lo,hi=a.lo,a.hi
        mask=(np.maximum(abs(lo),abs(hi))<FLOOR)&((lo!=0)|(hi!=0))
        if np.any(mask):
            lo=lo.copy();hi=hi.copy();lo[mask]=-FLOOR;hi[mask]=FLOOR
        center=lo/2+hi/2
        raw=np.maximum(center-lo,hi-center)
        radius=np.zeros_like(raw);nonzero=raw>0
        radius[nonzero]=up(raw[nonzero])
        return center,radius

    def budget(n):
        unit=Q(1,2**52)
        if n*unit>=1:raise ArithmeticError('Invalid dot-product gamma budget')
        gamma=float(qb(n*unit/(1-n*unit)).hi)
        tiny=max(FLOOR,float(up(n*np.nextafter(0.,1.))))
        return gamma,tiny

    def matmul(a,b):
        ac,ar=centered(a);bc,br=centered(b)
        gamma,tiny=budget(2*a.lo.shape[1]+2)
        def pos(x,y):return up(up(x@y+tiny)/down(1-gamma))
        nominal=ac@bc;mag=pos(abs(ac),abs(bc))
        rad=up(pos(abs(ac),br)+pos(ar,abs(bc)))
        rad=up(rad+pos(ar,br));rad=up(rad+up(up(gamma*mag)+tiny))
        result=I(down(nominal-rad),up(nominal+rad))
        if not (np.isfinite(result.lo).all() and np.isfinite(result.hi).all()):
            raise ArithmeticError('Nonfinite normal-range matrix enclosure')
        return result

    def convolution(a,b):
        na,ma=a.lo.shape;nb,mb=b.lo.shape;stride=ma+mb-1
        ac,ar=centered(a);bc,br=centered(b)
        def flat(x):
            z=np.zeros((x.shape[0],stride));z[:,:x.shape[1]]=x;return z.ravel()
        ac,bc,ar,br=(flat(x) for x in (ac,bc,ar,br))
        gamma,tiny=budget(2*min(len(ac),len(bc))+2)
        def pos(x,y):return up(up(np.convolve(x,y)+tiny)/down(1-gamma))
        nominal=np.convolve(ac,bc);mag=pos(abs(ac),abs(bc))
        rad=up(pos(abs(ac),br)+pos(ar,abs(bc)))
        rad=up(rad+pos(ar,br));rad=up(rad+up(up(gamma*mag)+tiny))
        shape=(na+nb-1,stride);size=shape[0]*shape[1]
        result=I(down(nominal[:size]-rad[:size]).reshape(shape),
                 up(nominal[:size]+rad[:size]).reshape(shape))
        if not (np.isfinite(result.lo).all() and np.isfinite(result.hi).all()):
            raise ArithmeticError('Nonfinite normal-range convolution enclosure')
        return result

    poly.interval_matmul=matmul
    if narrow_owner is None:poly.interval_convolution=convolution
    else:
        if narrow_owner.poly is not poly:raise ValueError('Narrow convolution owner has another backend')
        narrow_owner._original_convolution=convolution
        poly.interval_convolution=narrow_owner.small_factor_convolution
    return dict(input_normal_range_floor=FLOOR,input_normal_range_floor_exact='1/'+str(2**400),
        exact_zero_midpoint_radii_preserved=True,underflow_budget_only_increased=True,
        floating_point_modes_changed=False,actual_fourier_modes_discarded=False)
