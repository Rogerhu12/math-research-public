"""Horner and angle-addition implementation of the unchanged R36 oracle.

The defining integrals, exact inputs, degree-64 exponential remainder and
80-digit outward Fraction arithmetic are identical to R36.  This module
only collects the finite Taylor polynomial coefficients before evaluation
and reuses integer-angle sine/cosine recurrences.  No physical datum changes.
"""
from fractions import Fraction as F
from functools import lru_cache
import math

import integral_core_intervals as exact
from integral_core_intervals import point, add, sub, neg, mul, scale, power


class HornerCutoffPrimitive(exact.CutoffPrimitive):
    def __init__(self, a, b, plain):
        super().__init__(a, b)
        self.plain = plain

    @lru_cache(None)
    def coefficients(self, k):
        size = self.degree+11
        re, im = [F(0)]*size, [F(0)]*size
        for r in range(self.degree+1):
            for j, p in enumerate(exact.CHI):
                if not p:
                    continue
                c = F(p, r+j+1)*(k*self.b)**r/math.factorial(r)
                n = r+j+1
                if r % 4 == 0:
                    re[n] += c
                elif r % 4 == 1:
                    im[n] += c
                elif r % 4 == 2:
                    re[n] -= c
                else:
                    im[n] -= c
        sn, cs = exact.signed_sincos(point(k*self.a))
        return tuple(scale(sub(scale(cs, x), scale(sn, y)), self.b) for x, y in zip(re, im)), \
               tuple(scale(add(scale(sn, x), scale(cs, y)), self.b) for x, y in zip(re, im))

    def transition(self, k, tau):
        assert 0 <= tau[0] <= tau[1] <= 1
        result = []
        error = self.b*abs(k*self.b)**(self.degree+1)*tau[1]**(self.degree+2)/math.factorial(self.degree+2)
        for coefficients in self.coefficients(k):
            value = point(0)
            for coefficient in reversed(coefficients):
                value = add(mul(value, tau), coefficient)
            result.append(add(value, (-error, error)))
        return tuple(result)

    @lru_cache(None)
    def complete(self, k):
        return tuple(add(x, y) for x, y in zip(self.plain(k, point(self.a)), self.transition(k, point(1))))

    def _positive_integrals(self, k, x):
        assert x[0] >= 0
        pieces = []
        if x[0] <= self.a:
            pieces.append(self.plain(k, (x[0], min(x[1], self.a))))
        if x[1] >= self.a and x[0] <= self.a+self.b:
            y = max(x[0], self.a), min(x[1], self.a+self.b)
            base = self.plain(k, point(self.a))
            rest = self.transition(k, scale(sub(y, point(self.a)), 1/self.b))
            pieces.append(tuple(add(v, w) for v, w in zip(base, rest)))
        if x[1] >= self.a+self.b:
            pieces.append(self.complete(k))
        return tuple(exact.hull(*(piece[j] for piece in pieces)) for j in range(2))


class FastExactRawM3Core(exact.ExactRawM3Core):
    def __init__(self, core, provenance):
        super().__init__(core, provenance)
        self.primary = HornerCutoffPrimitive(self.primary.a, self.primary.b, self.plain)
        self.controls = HornerCutoffPrimitive(self.controls.a, self.controls.b, self.plain)

    @lru_cache(maxsize=64)
    def multiples(self, x):
        sn, cs = exact.signed_sincos(scale(x, 3))
        values = [(point(0), point(1))]
        for _ in range(self.M):
            a, b = values[-1]
            values.append((add(mul(a, cs), mul(b, sn)), sub(mul(b, cs), mul(a, sn))))
        return tuple(values)

    def trig(self, x, k, derivative=0):
        if k == 0:
            return point(int(derivative == 0))
        sn, cs = self.multiples(x)[k]
        return scale((cs, neg(sn), neg(cs), sn)[derivative % 4], (3*k)**derivative)

    def plain(self, frequency, x):
        if not frequency:
            return x, point(0)
        if frequency % 3 == 0 and frequency//3 <= self.M:
            sn, cs = self.multiples(x)[frequency//3]
            return scale(sn, F(1, frequency)), scale(sub(point(1), cs), F(1, frequency))
        return exact.plain_integrals(frequency, x)

    def control_jets(self, x, order=4):
        chi = self.controls.jets(x, order)
        window = [sub(point(1), chi[0])]+[neg(v) for v in chi[1:]]
        sums = [exact.sum_intervals(scale(mul(v, self.trig(x, k, r)), (-1)**k)
                                   for k, v in enumerate(self.D)) for r in range(order+1)]
        output = []
        for r in range(order+1):
            pure = exact.sum_intervals(scale(self.trig(x, j+2, r), c*(-1)**(j+2))
                                       for j, c in enumerate(self.c))
            compact = exact.sum_intervals(scale(mul(window[ell], sums[r-ell]), math.comb(r, ell))
                                          for ell in range(r+1))
            output.append(add(scale(pure, 1-self.lam), scale(compact, self.lam)))
        return output

    def control_primitive(self, x):
        pure = exact.sum_intervals(scale(self.plain(3*(j+2), x)[0], c*(-1)**(j+2))
                                   for j, c in enumerate(self.c))
        compact = exact.sum_intervals(scale(mul(v, sub(self.plain(3*k, x)[0],
                                                       self.controls.integrals(3*k, x)[0])), (-1)**k)
                                      for k, v in enumerate(self.D))
        return add(scale(pure, 1-self.lam), scale(compact, self.lam))

    def material_derivative_bounds(self):
        b = self.global_bounds
        m, r1, r2, r3 = (b[k] for k in ('rho_lower', 'rho_phi_upper', 'rho_phiphi_upper',
                                        'rho_phiphiphi_piecewise_upper'))
        assert m > 0
        return (None, F(1), 1/m, 1/m**2+r1/m**3,
                1/m**3+(3*r1+r2)/m**4+3*r1*r1/m**5,
                1/m**4+(6*r1+4*r2+r3)/m**5+(10*r1*r2+15*r1*r1)/m**6+15*r1**3/m**7)

    def point_normal_through_four(self, approximate_phi):
        values = self.normal_jets(point(F.from_float(float(approximate_phi))))
        rho, r1, r2 = values['rho'], values['rho_phi'], values['rho_phiphi']
        tangent = values['tangent']
        normal = tangent[1], neg(tangent[0])
        a = add(exact.divide(point(1), power(rho, 3)),
                sub(exact.divide(r2, power(rho, 4)),
                    scale(exact.divide(power(r1, 2), power(rho, 5)), 3)))
        b = scale(exact.divide(r1, power(rho, 4)), 3)
        values['fourth'] = tuple(add(mul(a, n), mul(b, t)) for n, t in zip(normal, tangent))
        return values

    def material_intervals(self, normal_values, target):
        residual = exact.magnitude(sub(normal_values['arc'], target))
        K = self.material_derivative_bounds()
        return tuple(tuple(add(v, (-residual*K[j+1], residual*K[j+1])) for v in normal_values[key])
                     for j, key in enumerate(('position', 'tangent', 'second', 'third', 'fourth')))
