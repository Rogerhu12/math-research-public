"""Rational local primitives and inverse transfer for the actual raw m3 core.

The mathematical primary has a=.21, b=.08, eta=0, center pi/3.  Its
mean correction and periodic Green constant reuse R32.  The raw controls
use the source library's certified exact two-by-two moment projection.
Neither the source Gauss evaluator nor its inverse tolerance is a bound.

This module bounds point values or real input intervals.  It does not
certify the whole prefix metric, embedding, reach, or Fourier tails.
"""
from fractions import Fraction as F
from functools import lru_cache
import math

from certify_protected_arc_curvature_dual import (
    point, outward, add, sub, neg, mul, scale, divide, pi_interval, sincos,
)

CHI = (1, 0, 0, 0, 0, -126, 420, -540, 315, -70)
SERIES_DEGREE = 64
PRIMARY_A, PRIMARY_B = F(21, 100), F(2, 25)
R32_BETA = tuple(map(F, (
    '-0.2301638780908070253001170066934325491224',
    '-0.2301638780908070253001170066934325491223')))
R32_CENTER_PER_Q = tuple(map(F, (
    '9.0518983695329193804686089826045741030176',
    '9.0518983695329193804686089826045741030177')))
R32_SOURCE_SHA256 = '7d92c9455f82c40c742f6f6867d61533dd0fc91bc3fcfc3dddaa903255b2d54b'
RAW_PATH = 'raw-mean-primary-compact-v1'


def magnitude(x):
    return max(abs(x[0]), abs(x[1]))


def hull(*values):
    return min(v[0] for v in values), max(v[1] for v in values)


def power(x, k):
    assert isinstance(k, int) and k >= 0
    if not k:
        return point(1)
    if k % 2:
        return outward(x[0]**k, x[1]**k)
    upper = max(abs(x[0]), abs(x[1]))**k
    lower = 0 if x[0] <= 0 <= x[1] else min(abs(x[0]), abs(x[1]))**k
    return outward(lower, upper)


def polynomial(coefficients, x):
    result = point(0)
    for c in reversed(coefficients):
        result = add(mul(result, x), point(c))
    return result


def signed_sincos(x):
    """The imported Taylor enclosure, with real argument parity respected."""
    if x[0] >= 0:
        return sincos(x)
    if x[1] <= 0:
        s, c = sincos(neg(x))
        return neg(s), c
    s0, c0 = sincos((F(0), -x[0]))
    s1, c1 = sincos((F(0), x[1]))
    return hull(neg(s0), s1), hull(c0, c1)


def trig_derivative(x, frequency, derivative=0):
    if frequency == 0:
        return point(int(derivative == 0))
    sn, cs = signed_sincos(scale(x, frequency))
    value = (cs, neg(sn), neg(cs), sn)[derivative % 4]
    return scale(value, frequency**derivative)


def plain_integrals(k, x):
    """Real integrals of cos(k*s), sin(k*s) from zero to x."""
    if not k:
        return x, point(0)
    sn, cs = signed_sincos(scale(x, k))
    return scale(sn, F(1, k)), scale(sub(point(1), cs), F(1, k))


class CutoffPrimitive:
    def __init__(self, a, b, degree=SERIES_DEGREE):
        self.a, self.b, self.degree = F(a), F(b), int(degree)
        assert self.a > 0 and self.b > 0 and self.degree >= 8

    def transition(self, k, tau):
        """Integral a..a+b*tau of chi(s)*exp(i*k*s), as real/imag."""
        assert 0 <= tau[0] <= tau[1] <= 1
        z = k*self.b
        re, im = point(0), point(0)
        powers = [power(tau, j) for j in range(self.degree+11)]
        for r in range(self.degree+1):
            moment = point(0)
            for j, coefficient in enumerate(CHI):
                if coefficient:
                    moment = add(moment, scale(powers[r+j+1], F(coefficient, r+j+1)))
            term = scale(moment, z**r/F(math.factorial(r)))
            if r % 4 == 0:
                re = add(re, term)
            elif r % 4 == 1:
                im = add(im, term)
            elif r % 4 == 2:
                re = sub(re, term)
            else:
                im = sub(im, term)
        sn, cs = signed_sincos(point(k*self.a))
        real = scale(sub(mul(cs, re), mul(sn, im)), self.b)
        imag = scale(add(mul(sn, re), mul(cs, im)), self.b)
        # chi lies in [0,1]; integrate the unit-modulus exponential's
        # degree-R integral remainder, then rotate by exp(i*k*a).
        error = self.b*abs(z)**(self.degree+1)*tau[1]**(self.degree+2)/math.factorial(self.degree+2)
        return add(real, (-error, error)), add(imag, (-error, error))

    @lru_cache(None)
    def complete(self, k):
        base = plain_integrals(k, point(self.a))
        rest = self.transition(k, point(1))
        return tuple(add(x, y) for x, y in zip(base, rest))

    def _positive_integrals(self, k, x):
        assert x[0] >= 0
        pieces = []
        if x[0] <= self.a:
            pieces.append(plain_integrals(k, (x[0], min(x[1], self.a))))
        if x[1] >= self.a and x[0] <= self.a+self.b:
            y = max(x[0], self.a), min(x[1], self.a+self.b)
            base = plain_integrals(k, point(self.a))
            rest = self.transition(k, scale(sub(y, point(self.a)), 1/self.b))
            pieces.append(tuple(add(v, w) for v, w in zip(base, rest)))
        if x[1] >= self.a+self.b:
            pieces.append(self.complete(k))
        return tuple(hull(*(piece[j] for piece in pieces)) for j in range(2))

    def integrals(self, k, x):
        assert isinstance(k, int) and k >= 0 and x[0] <= x[1]
        if x[0] >= 0:
            return self._positive_integrals(k, x)
        if x[1] <= 0:
            c, s = self._positive_integrals(k, neg(x))
            return neg(c), s
        c0, s0 = self._positive_integrals(k, (F(0), -x[0]))
        c1, s1 = self._positive_integrals(k, (F(0), x[1]))
        return hull(neg(c0), c1), hull(s0, s1)

    def _positive_jets(self, x, order):
        pieces = []
        if x[0] <= self.a:
            pieces.append(tuple(point(int(j == 0)) for j in range(order+1)))
        if x[1] >= self.a and x[0] <= self.a+self.b:
            y = max(x[0], self.a), min(x[1], self.a+self.b)
            tau = scale(sub(y, point(self.a)), 1/self.b)
            values = []
            for r in range(order+1):
                coefficients = [F(CHI[j]*math.factorial(j), math.factorial(j-r))
                                for j in range(r, len(CHI))]
                values.append(scale(polynomial(coefficients, tau), 1/self.b**r))
            pieces.append(tuple(values))
        if x[1] >= self.a+self.b:
            pieces.append(tuple(point(0) for _ in range(order+1)))
        return tuple(hull(*(piece[j] for piece in pieces)) for j in range(order+1))

    def jets(self, x, order=4):
        assert 0 <= order <= 5
        if x[0] >= 0:
            return self._positive_jets(x, order)
        if x[1] <= 0:
            return tuple(scale(v, (-1)**j) for j, v in enumerate(self._positive_jets(neg(x), order)))
        left = self._positive_jets((F(0), -x[0]), order)
        right = self._positive_jets((F(0), x[1]), order)
        return tuple(hull(scale(u, (-1)**j), v) for j, (u, v) in enumerate(zip(left, right)))


@lru_cache(None)
def cutoff_derivative_bound(order):
    """Exact Bernstein bound on the unit transition, including endpoint limits."""
    if order == 0:
        return F(1)
    coefficients = [F(CHI[k]*math.factorial(k), math.factorial(k-order))
                    for k in range(order, 10)]
    degree, bound = len(coefficients)-1, F(0)
    for cell in range(64):
        a, h = F(cell, 64), F(1, 64)
        power_coefficients = [sum((coefficients[j]*math.comb(j, k)*a**(j-k)*h**k
                                   for j in range(k, degree+1)), F(0))
                              for k in range(degree+1)]
        bernstein = [sum((power_coefficients[j]*F(math.comb(k, j), math.comb(degree, j))
                          for j in range(k+1)), F(0)) for k in range(degree+1)]
        bound = max(bound, *(abs(v) for v in bernstein))
    return bound


class ExactRawM3Core:
    def __init__(self, core, provenance):
        settings = provenance['core_round_settings']
        assert provenance['core_kind'] == 'exact_m3_raw_local_circle_integral_lift'
        assert provenance['core_control_path'] == RAW_PATH
        assert core.basis.summary()['control_path'] == RAW_PATH
        assert core.base_mode == 3 and core.bimodal_eta == 0
        assert F(str(settings['halfwidth'])) == PRIMARY_A
        assert F(str(settings['transition'])) == PRIMARY_B
        assert settings['center'] == math.pi/3 and settings['lock_fundamental']
        self.q = F.from_float(core.support_amplitude)
        self.lam = F.from_float(core.lam)
        self.c = tuple(F.from_float(v) for v in core.corrections)
        assert [float(v) for v in self.c] == provenance['physical_controls']
        self.M = len(self.c)+1
        assert core.basis.M == self.M == provenance['core_projection_order_J']
        self.H = tuple(tuple(outward(*v) for v in row) for row in core.basis.certificate['coefficients'])
        self.D = tuple(sum_intervals(scale(self.H[j][k], self.c[j]) for j in range(self.M-1))
                       for k in range(self.M+1))
        self.L = scale(pi_interval(), F(1, 3))
        self.T = scale(self.L, 2)
        self.beta, self.center_per_q = R32_BETA, R32_CENTER_PER_Q
        self.primary = CutoffPrimitive(PRIMARY_A, PRIMARY_B)
        self.controls = CutoffPrimitive(PRIMARY_A, F(str(settings['control_transition'])))
        assert self.controls.a+self.controls.b < self.L[0]
        self.global_bounds = self._global_bounds()

    def _global_bounds(self):
        trig = [sum(magnitude(v)*(3*k)**r for k, v in enumerate(self.D))
                if r else sum(magnitude(v) for v in self.D) for r in range(6)]
        cut = [cutoff_derivative_bound(r)/self.controls.b**r for r in range(6)]
        control = []
        for r in range(6):
            pure = sum(abs(c)*(3*(j+2))**r for j, c in enumerate(self.c))
            compact = sum(math.comb(r, ell)*cut[ell]*trig[r-ell] for ell in range(r+1))
            control.append((1-self.lam)*pure+self.lam*compact)
        rho_control = control[0]+control[2]
        minimum = 1-8*self.q+self.q*self.lam*self.beta[0]-rho_control
        maximum = 1+8*self.q+rho_control
        primary_cut = [cutoff_derivative_bound(r)/PRIMARY_B**r for r in range(4)]
        derivatives = []
        for r in range(1, 4):
            primary = 8*3**r+self.lam*sum(
                math.comb(r, ell)*primary_cut[ell]*(16-self.beta[0] if ell == r else 8*3**(r-ell))
                for ell in range(1, r+1))
            derivatives.append(self.q*primary+control[r]+control[r+2])
        return dict(rho_lower=minimum, rho_upper=maximum,
                    rho_phi_upper=derivatives[0], rho_phiphi_upper=derivatives[1],
                    rho_phiphiphi_piecewise_upper=derivatives[2], control_support_derivative_bounds=control)

    def local_intervals(self, phi):
        quot = divide(phi, self.T)
        first, last = math.floor(quot[0]), math.floor(quot[1])
        assert last-first <= 1
        return [sub(phi, add(self.L, scale(self.T, sector))) for sector in range(first, last+1)]

    def control_jets(self, x, order=4):
        chi = self.controls.jets(x, order)
        window = [sub(point(1), chi[0])]+[neg(v) for v in chi[1:]]
        compact_trig = [sum_intervals(scale(mul(v, trig_derivative(x, 3*k, r)), (-1)**k)
                                     for k, v in enumerate(self.D)) for r in range(order+1)]
        output = []
        for r in range(order+1):
            pure = sum_intervals(scale(trig_derivative(x, 3*(j+2), r), c*(-1)**(j+2))
                                 for j, c in enumerate(self.c))
            compact = sum_intervals(scale(mul(window[ell], compact_trig[r-ell]), math.comb(r, ell))
                                    for ell in range(r+1))
            output.append(add(scale(pure, 1-self.lam), scale(compact, self.lam)))
        return output

    def control_primitive(self, x):
        pure = sum_intervals(scale(plain_integrals(3*(j+2), x)[0], c*(-1)**(j+2))
                             for j, c in enumerate(self.c))
        compact = sum_intervals(scale(mul(v, sub(plain_integrals(3*k, x)[0],
                                                     self.controls.integrals(3*k, x)[0])), (-1)**k)
                                for k, v in enumerate(self.D))
        return add(scale(pure, 1-self.lam), scale(compact, self.lam))

    def _normal_jets_local(self, phi, x):
        sn, cs = signed_sincos(x)
        sin3, cos3 = signed_sincos(scale(x, 3))
        cutoff = self.primary.jets(x, 2)
        moments = {k: self.primary.integrals(k, x) for k in (0, 1, 2, 3, 4)}
        C = sub(mul(sub(point(8), self.beta), moments[1][0]),
                scale(add(moments[2][0], moments[4][0]), 4))
        S = add(sub(mul(sub(point(8), self.beta), moments[1][1]), scale(moments[4][1], 4)),
                scale(moments[2][1], 4))
        homogeneous = sub(sub(sub(point(9), self.center_per_q), self.beta), S)
        w = add(self.beta, add(mul(homogeneous, cs), mul(C, sn)))
        wp = add(neg(mul(homogeneous, sn)), mul(C, cs))
        v = add(neg(cos3), scale(w, self.lam))
        vp = add(scale(sin3, 3), scale(wp, self.lam))
        control = self.control_jets(x, 4)
        h = add(add(point(1), scale(v, self.q)), control[0])
        hp = add(scale(vp, self.q), control[1])
        snphi, csphi = signed_sincos(phi)
        normal, tangent = (csphi, snphi), (neg(snphi), csphi)
        curve = tuple(add(mul(h, n), mul(hp, t)) for n, t in zip(normal, tangent))
        delta = sub(sub(point(8), self.beta), scale(cos3, 8))
        unit = add(scale(cos3, 8), scale(add(self.beta, mul(cutoff[0], delta)), self.lam))
        unit1 = add(scale(sin3, -24), scale(add(mul(cutoff[1], delta), scale(mul(cutoff[0], sin3), 24)), self.lam))
        unit2 = add(scale(cos3, -72), scale(add(mul(cutoff[2], delta),
                     add(scale(mul(cutoff[1], sin3), 48), scale(mul(cutoff[0], cos3), 72))), self.lam))
        rho = add(add(point(1), scale(unit, self.q)), add(control[0], control[2]))
        rho1 = add(scale(unit1, self.q), add(control[1], control[3]))
        rho2 = add(scale(unit2, self.q), add(control[2], control[4]))
        primary_arc = add(scale(sin3, F(8, 3)), scale(add(mul(self.beta, x),
                          sub(mul(sub(point(8), self.beta), moments[0][0]), scale(moments[3][0], 8))), self.lam))
        arc = add(phi, add(scale(primary_arc, self.q), add(self.control_primitive(x), control[1])))
        second = tuple(neg(divide(n, rho)) for n in normal)
        third = tuple(add(neg(divide(t, power(rho, 2))), divide(mul(n, rho1), power(rho, 3)))
                      for n, t in zip(normal, tangent))
        return dict(arc=arc, position=curve, tangent=tangent, second=second, third=third,
                    rho=rho, rho_phi=rho1, rho_phiphi=rho2)

    def normal_jets(self, phi):
        pieces = [self._normal_jets_local(phi, x) for x in self.local_intervals(phi)]
        if len(pieces) == 1:
            return pieces[0]
        result = {}
        for name in pieces[0]:
            result[name] = (tuple(hull(*(p[name][j] for p in pieces)) for j in range(2))
                            if name in ('position', 'tangent', 'second', 'third')
                            else hull(*(p[name] for p in pieces)))
        return result

    def material_enclosure(self, target, approximate_phi):
        """True material Gamma jets from an arbitrary approximate inverse."""
        values = self.normal_jets(point(F.from_float(float(approximate_phi))))
        target = F.from_float(float(target))
        residual = magnitude(sub(values['arc'], point(target)))
        bounds = self.global_bounds
        m, r1, r2 = bounds['rho_lower'], bounds['rho_phi_upper'], bounds['rho_phiphi_upper']
        assert m > 0, 'A true positive rho lower bound is needed for inverse transfer'
        costs = [residual, residual/m,
                 residual*(1/m**2+r1/m**3),
                 residual*(1/m**3+3*r1/m**4+r2/m**4+3*r1*r1/m**5)]
        result = dict(arc_residual_upper=residual, inverse_normal_error_upper=residual/m)
        for key, cost in zip(('position', 'tangent', 'second', 'third'), costs):
            result[key] = tuple(add(v, (-cost, cost)) for v in values[key])
        result['material_transfer_costs'] = costs
        return result


def sum_intervals(values):
    result = point(0)
    for value in values:
        result = add(result, value)
    return result
