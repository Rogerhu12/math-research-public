"""Validated radial primitives of the frozen finite rotational background.

This module supplies source-coordinate primitives, not an inverse theorem.
Every profile endpoint is anchored by independently certified full A/B
integrals. On an analytic leaf, a Taylor polynomial plus an explicit
primitive remainder encloses r(x); on a crossing leaf, an interval range
integral is used. All later inverse approximations must be checked against
these enclosures before they can describe a physical-radius function.
"""
from fractions import Fraction as Q
import math
import numpy as np

from db6f_tail_interval_elementary import I, qbounds
from db6f_tail_interval_source import FrozenSource, Jet


def scalar_pair(x):
    return [float(x.lo), float(x.hi)]


def from_pair(x):
    return I(x[0], x[1])


def interval_sum(values):
    lo = sum((Q(float(x.lo)) for x in values), Q(0))
    hi = sum((Q(float(x.hi)) for x in values), Q(0))
    return I(float(qbounds(lo).lo), float(qbounds(hi).hi))


def intersect(a, b):
    lo, hi = max(float(a.lo), float(b.lo)), min(float(a.hi), float(b.hi))
    if lo > hi:
        raise ArithmeticError('two radial enclosures have empty intersection')
    return I(lo, hi)


def poly_value(coefficients, x):
    ans = I(0)
    for coefficient in coefficients[::-1]:
        ans = ans*x+coefficient
    return ans


def strong_profile_anchors(parameters, alpha, zero_a, inner_a, outer_b, depth):
    """Exact-rational accumulation from the fixed outer cut toward the cuff."""
    if not 1 <= depth <= 16:
        raise ValueError('strong B anchors are available only for cells 0..15')
    A = {(0, row['segment']): tuple(map(Q, row['interval'])) for row in zero_a['rows']}
    for cell in inner_a['rows']:
        for row in cell['segments']:
            A[(cell['n'], row['segment'])] = tuple(map(Q, row['A']))
    B = {(row['cell'], row['segment']): tuple(map(Q, row['interval'])) for row in outer_b['rows']}
    al, ah = map(Q, alpha)
    low = high = Q(parameters['rCut'])
    out = {}
    for n in range(depth):
        for j in range(8, -1, -1):
            right = [float(qbounds(low).lo), float(qbounds(high).hi)]
            aa, bb = A[(n, j)], B[(n, j)]
            # A can carry a negative subnormal interval artifact at an exact
            # zero. Both A and B are analytically nonnegative.
            alo, ahi = max(Q(0), aa[0]), aa[1]
            blo, bhi = max(Q(0), bb[0]), bb[1]
            il, ih = alo+al*blo, ahi+ah*bhi
            low, high = low-ih, high-il
            out[(n, j)] = {'left': [float(qbounds(low).lo), float(qbounds(high).hi)],
                           'right': right,
                           'integral': [float(qbounds(il).lo), float(qbounds(ih).hi)]}
    return out


def build_profile(model, alpha, n, j, anchor, order=8, density=1e-10, initial=16,
                  minimum_width=2**-34, batch=128):
    if order < 2 or order % 2 or not 0 < initial <= 2**48 or initial&(initial-1):
        raise ValueError('even Taylor order and positive dyadic initial count required')
    if not 2**-48 <= minimum_width <= 1 or batch <= 0 or density <= 0:
        raise ValueError('invalid primitive partition settings')
    pending = [(k/initial, (k+1)/initial) for k in range(initial)]
    saved = []
    evaluated = 0
    for depth in range(49):
        if not pending:
            break
        nxt = []
        for start in range(0, len(pending), batch):
            block = pending[start:start+batch]
            lo = np.array([a for a,b in block]); hi = np.array([b for a,b in block])
            width = hi-lo; mid = (lo+hi)/2
            if not np.all(width == width[0]):
                raise ValueError('primitive wavefront must have one dyadic width')
            h = Q(float(width[0]))/2
            rr = model.evaluate(n, j, Jet.variable(I(lo, hi), order))
            pp = model.evaluate(n, j, Jet.variable(I(mid), order))
            f = rr['A']+rr['B']*alpha
            point = pp['A']+pp['B']*alpha
            valid = rr['validA']&rr['validB']&pp['validA']&pp['validB']
            remainder = f.c[order]*qbounds(2*h**(order+1)/(order+1))
            budget = density*width
            plain = f.c[0]*I(width)
            okay = valid&(remainder.abs().hi <= budget)
            range_okay = (~valid)&((plain.hi-plain.lo <= budget)|(width <= minimum_width))
            for k,(a,b) in enumerate(block):
                if okay[k]:
                    cc = [I(0)]+[point.c[z][k]/(z+1) for z in range(order)]
                    pl = poly_value(cc, I(-float(h)))
                    ph = poly_value(cc, I(float(h)))
                    integral = ph-pl+remainder[k]
                    saved.append({'left':a, 'right':b, 'center':float(mid[k]),
                                  'polynomial':[scalar_pair(z) for z in cc],
                                  'polynomialAtLeft':scalar_pair(pl),
                                  'primitiveRemainder':float(remainder[k].abs().hi),
                                  'integral':scalar_pair(integral), 'analytic':True})
                elif range_okay[k] or width[k] <= minimum_width:
                    # For x in [a,b], integral_a^x f is in [f] (x-a).
                    cc = [I(0), f.c[0][k]]
                    saved.append({'left':a, 'right':b, 'center':a,
                                  'polynomial':[scalar_pair(z) for z in cc],
                                  'polynomialAtLeft':[0.,0.], 'primitiveRemainder':0.,
                                  'integral':scalar_pair(plain[k]), 'analytic':False})
                else:
                    m=(a+b)/2
                    nxt.extend([(a,m),(m,b)])
            evaluated += len(block)
        pending = nxt
    if pending:
        raise RuntimeError('primitive integration failed to terminate')
    saved.sort(key=lambda row:row['left'])
    if saved[0]['left'] != 0 or saved[-1]['right'] != 1 or any(
            a['right'] != b['left'] for a,b in zip(saved[:-1],saved[1:])):
        raise ArithmeticError('primitive source partition is incomplete')
    integrals = [from_pair(row['integral']) for row in saved]
    total = interval_sum(integrals)
    # These are independent valid enclosures of the same full integral.
    intersect(total, from_pair(anchor['integral']))
    prefix_lo = prefix_hi = Q(0)
    total_lo, total_hi = sum((Q(float(x.lo)) for x in integrals),Q(0)), sum((Q(float(x.hi)) for x in integrals),Q(0))
    left_anchor, right_anchor = from_pair(anchor['left']), from_pair(anchor['right'])
    for leaf, inc in zip(saved, integrals):
        forward = left_anchor+I(float(qbounds(prefix_lo).lo),float(qbounds(prefix_hi).hi))
        backward = right_anchor-I(float(qbounds(total_lo-prefix_lo).lo),float(qbounds(total_hi-prefix_hi).hi))
        node = intersect(forward, backward)
        leaf['radiusAtLeft'] = scalar_pair(node)
        prefix_lo += Q(float(inc.lo)); prefix_hi += Q(float(inc.hi))
        if not all(math.isfinite(z) for row in leaf['polynomial'] for z in row):
            raise ArithmeticError('nonfinite radial primitive coefficient')
    return {'n':n, 'segment':j, 'anchor':anchor, 'leaves':saved,
            'integral':scalar_pair(total), 'boxesEvaluated':evaluated,
            'analyticLeaves':sum(row['analytic'] for row in saved),
            'rangeLeaves':sum(not row['analytic'] for row in saved)}


class ProfilePrimitive:
    def __init__(self, record):
        self.record=record
        self.n, self.j=record['n'], record['segment']
        self.leaves=record['leaves']
        self.ends=np.array([x['right'] for x in self.leaves])
        self.anchors=record['anchor']
        self.central=[]
        for leaf in self.leaves:
            coefficients=np.mean(np.array(leaf['polynomial']),axis=1)
            coefficients[0] += (sum(leaf['radiusAtLeft'])-sum(leaf['polynomialAtLeft']))/2
            self.central.append(coefficients)

    def leaf_index(self, x):
        if not 0 <= x <= 1:
            raise ValueError('source query outside one profile')
        return min(len(self.leaves)-1, int(np.searchsorted(self.ends,x,side='right')))

    def point(self, x):
        if x == 0:
            return from_pair(self.anchors['left'])
        if x == 1:
            return from_pair(self.anchors['right'])
        leaf=self.leaves[self.leaf_index(x)]
        y=qbounds(Q(x)-Q(leaf['center']))
        coeff=[from_pair(v) for v in leaf['polynomial']]
        value=(from_pair(leaf['radiusAtLeft'])+poly_value(coeff,y)
               -from_pair(leaf['polynomialAtLeft']))
        rem=leaf['primitiveRemainder']
        return value+I(-rem,rem)

    def approximate(self, x):
        if x == 0:return sum(self.anchors['left'])/2
        if x == 1:return sum(self.anchors['right'])/2
        index=self.leaf_index(x)
        return float(np.polynomial.polynomial.polyval(x-self.leaves[index]['center'],self.central[index]))

    def approximate_inverse(self, r):
        if r <= self.approximate(0):return 0.
        if r >= self.approximate(1):return 1.
        lo,hi=0.,1.
        for _ in range(42):
            mid=(lo+hi)/2
            if self.approximate(mid)<r:lo=mid
            else:hi=mid
        return (lo+hi)/2

    def inverse_cover(self, left_r, right_r):
        """Every inverse point belonging to this profile lies in this box."""
        left_r,right_r=Q(left_r),Q(right_r)
        seed=self.approximate_inverse(float(left_r));step=2**-36
        left=seed
        while left > 0 and Q(float(self.point(left).hi)) > left_r:
            left=max(0.,seed-step);step*=2
        seed=self.approximate_inverse(float(right_r));step=2**-36
        right=seed
        while right < 1 and Q(float(self.point(right).lo)) < right_r:
            right=min(1.,seed+step);step*=2
        if left > right:
            raise ArithmeticError('source inverse enclosure is reversed')
        return I(left,right)
