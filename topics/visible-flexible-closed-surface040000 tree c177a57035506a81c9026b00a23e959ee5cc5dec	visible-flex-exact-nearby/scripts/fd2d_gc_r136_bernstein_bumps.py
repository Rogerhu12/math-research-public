"""A tighter interval evaluation of the unchanged R171 physical bumps.

This class reads the existing accurate target packet through the normal
R136ArbProfile constructor/reader. Only polynomial range evaluation is
different. The target, saved coefficients, supports and base Taylor packet
remain identical; the additional enclosure source is explicit in metadata.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb

from flint import arb

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import aq,rational,interval
from fd2d_gc_r136_arb_profile import R136ArbProfile,bernstein_range,derivative

SCHEMA='fd2d-R171-exact-bump-Bernstein-range-consumer-v1'


@lru_cache(maxsize=4)
def bump_derivative_coefficients(order):
    order=int(order)
    if not 0<=order<=3:raise ValueError('Only the four requested physical jets are provided')
    coefficients=[F(0)]*5+[F(1024*comb(5,j)*(-1)**j) for j in range(6)]
    for unused in range(order):
        coefficients=[j*coefficients[j] for j in range(1,len(coefficients))]
    return tuple(coefficients)


def exact_bump_range(lo,hi,left,right,order):
    lo,hi,left,right=map(rational,(lo,hi,left,right))
    if lo>hi or left>=right:raise ValueError('Invalid physical box or bump support')
    if hi<=left or lo>=right:return arb(0)
    width=right-left
    tl=max(F(0),(lo-left)/width);tr=min(F(1),(hi-left)/width)
    result=bernstein_range([aq(v) for v in bump_derivative_coefficients(order)],tl,tr)/aq(width**order)
    if order==0:
        # The independent exact identity 1024[t(1-t)]^5 in [0,1]
        # sharpens the polynomial control hull on very wide intervals.
        lower=max(arb(0),result.lower());upper=min(arb(1),result.upper())
        if lower>upper:raise ArithmeticError('Polynomial hull conflicts with the exact bump range')
        result=lower.union(upper)
    if lo<left or hi>right:result=result.union(arb(0))
    return result


class BernsteinBumpProfile(R136ArbProfile):
    def _bump_jets(self,lo,hi):
        lo,hi=map(rational,(lo,hi))
        answer=[arb(0) for unused in range(4)]
        for coefficient,(left,right) in zip(self.delta,self.supports):
            if coefficient==0 or hi<=left or lo>=right:continue
            for order in range(4):
                answer[order]+=aq(coefficient)*exact_bump_range(lo,hi,left,right,order)
        return answer

    def definition(self):
        result=super().definition()
        result.update(enclosure_backend_schema=SCHEMA,enclosure_backend_source=identity(__file__),
            bump_range_method='Exact degree10 polynomial and its first three derivatives, restricted to the physical box, then enclosed by its Bernstein controls',
            inherited_base_Taylor_packet_and_target_source_unchanged=True,
            target_function_or_derivatives_changed=False)
        return result
