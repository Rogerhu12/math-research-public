#!/usr/bin/env python3
"""One actual R582 mean profile, numerical jets and continuous z_s enclosures.

No tail seed is generated. The numerical height evaluates the same infinite
integral as the bound R566 source. A separate outward interval Riemann table
bounds that mathematical height for the continuous positive-chart check.
Scientific execution belongs to the declared public Actions shooting run.
"""
from decimal import Decimal, localcontext, ROUND_HALF_EVEN
import hashlib
import heapq
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import BSpline
from scipy.special import expit

ORIGINAL_SHA256 = "fd4bd864c3e9e96d741b7bc896a1bf6f9d50ba54eda0c02bd898f21bd42427a4"
if hashlib.sha256(Path(__file__).with_name("r582_actual_circle_seed_and_return_20261126.py").read_bytes()).hexdigest() != ORIGINAL_SHA256:
    raise RuntimeError("actual mean-profile source binding changed")
from r582_actual_circle_seed_and_return_20261126 import (
    SOURCE_Q, LENGTH, CORE_END, RC, ELL, AMP, CONTROL_LEFT, CONTROL_RIGHT,
    compact_bump, ClockCheckpoint,
)

BACKGROUND_END = LENGTH - .08
FREE_WIDTH = LENGTH - CORE_END
KNOTS = np.r_[np.zeros(6), [1 / 3, 2 / 3], np.ones(6)]
CIRCLE_RADIUS = .18 + .2
CORE_HALF = .02
CUT = .03
NEG_INF, POS_INF = -math.inf, math.inf


def down(value):
    return math.nextafter(float(value), NEG_INF)


def up(value):
    return math.nextafter(float(value), POS_INF)


class Interval:
    """Outward binary64 basic arithmetic; transcendental endpoints use Decimal."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo, self.hi = float(lo), float(lo if hi is None else hi)
        if not self.lo <= self.hi or not math.isfinite(self.lo + self.hi):
            raise ArithmeticError("nonfinite or reversed interval")

    @staticmethod
    def as_interval(value):
        return value if isinstance(value, Interval) else Interval(value)

    def __add__(self, other):
        other = self.as_interval(other)
        return Interval(down(self.lo + other.lo), up(self.hi + other.hi))

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.as_interval(other)

    def __rsub__(self, other):
        return self.as_interval(other) + -self

    def __mul__(self, other):
        other = self.as_interval(other)
        products = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(down(min(products)), up(max(products)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.as_interval(other)
        if other.lo <= 0 <= other.hi:
            raise ArithmeticError("interval division contains zero")
        return self * Interval(down(1 / other.hi), up(1 / other.lo))

    def __rtruediv__(self, other):
        return self.as_interval(other) / self

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("interval powers must be integers")
        if power < 0:
            return 1 / (self ** -power)
        if power == 0:
            return Interval(1)
        if power == 2:
            values = (self.lo * self.lo, self.hi * self.hi)
            return Interval(0 if self.lo <= 0 <= self.hi else down(min(values)), up(max(values)))
        result = Interval(1)
        for _ in range(power):
            result = result * self
        return result


def _decimal_exp_bounds(x):
    # Decimal exp is correctly rounded. Ninety significant digits and this
    # relative guard dominate its rounding before outward binary64 conversion.
    if x < -700:
        return 0.0, _decimal_exp_bounds(-700.)[1]
    if x > 700:
        raise ArithmeticError("declared interval exponential range exceeded")
    with localcontext() as ctx:
        ctx.prec = 90
        v = Decimal.from_float(float(x)).exp()
        guard = abs(v) * Decimal("1e-70") + Decimal("1e-320")
        lo, hi = float(max(Decimal(0), v - guard)), float(v + guard)
    return max(0., down(lo)), up(hi)


def exp_interval(value):
    value = Interval.as_interval(value)
    return Interval(_decimal_exp_bounds(value.lo)[0], _decimal_exp_bounds(value.hi)[1])


def _decimal_pi():
    # Machin: pi=16 atan(1/5)-4 atan(1/239). Each alternating remainder
    # after 120 terms is below its first omitted term; it is <1e-168 here.
    with localcontext() as ctx:
        ctx.prec = 90
        def atan_reciprocal(n):
            x = Decimal(1) / Decimal(n)
            term, total = x, x
            for k in range(1, 120):
                term *= -x * x
                total += term / Decimal(2 * k + 1)
            return total
        return +(16 * atan_reciprocal(5) - 4 * atan_reciprocal(239))


DECIMAL_PI = _decimal_pi()


def _decimal_sin_bounds(x):
    # Only |x| <= 1200 is used. Ninety-digit reduction and 80 Taylor terms
    # on |remainder| < 4 have total error much smaller than the 1e-60 guard.
    if abs(x) > 1200:
        raise ArithmeticError("validated sine argument exceeded declared range")
    with localcontext() as ctx:
        ctx.prec = 90
        d = Decimal.from_float(float(x))
        turns = (d / (2 * DECIMAL_PI)).to_integral_value(rounding=ROUND_HALF_EVEN)
        r = d - turns * 2 * DECIMAL_PI
        if abs(r) >= 4:
            raise ArithmeticError("sine argument reduction left proved range")
        term, total = r, r
        for k in range(1, 80):
            term *= -r * r / Decimal((2 * k) * (2 * k + 1))
            total += term
        guard = Decimal("1e-60")
        lo, hi = float(total - guard), float(total + guard)
    return max(-1., down(lo)), min(1., up(hi))


def sin_interval(value):
    value = Interval.as_interval(value)
    middle = value.lo + (value.hi - value.lo) / 2
    radius = up(max(abs(middle - value.lo), abs(value.hi - middle)))
    lo, hi = _decimal_sin_bounds(middle)
    # |sin'(x)|<=1 supplies a whole-interval bound, including extrema.
    return Interval(max(-1., down(lo - radius)), min(1., up(hi + radius)))


def step_intervals(s, left, right):
    """Return chi, chi*(1-chi), chi_s, including exact flat endpoints."""
    # Stored endpoints denote exact real constants. Their mathematical width
    # is the exact difference, enclosed here rather than rounded beforehand.
    width = Interval(right) - left
    if s.hi <= left:
        return Interval(0), Interval(0), Interval(0)
    if s.lo >= right:
        return Interval(1), Interval(0), Interval(0)
    x = (s - left) / width
    x = Interval(max(0., x.lo), min(1., x.hi))
    return _step_x_intervals(x, width)


def _step_x_intervals(x, width):
    if x.lo <= 0:
        if x.hi > .25:
            raise ArithmeticError("endpoint interval needs subdivision")
        h = Interval(x.hi)
        bound = exp_interval(-1 / h + 1 / (1 - h))
        # exp(-1/x)*x^-2 increases for 0<x<1/2. The other
        # positive factors also increase on this endpoint interval.
        derivative = bound * (1 / h ** 2 + 1 / (1 - h) ** 2) / width
        return Interval(0, min(.5, bound.hi)), Interval(0, bound.hi), Interval(0, derivative.hi)
    if x.hi >= 1:
        reflected = 1 - x
        reflected = Interval(max(0., reflected.lo), min(1., reflected.hi))
        chi, product, derivative = _step_x_intervals(reflected, width)
        return 1 - chi, product, derivative
    ell = -1 / x + 1 / (1 - x)
    if x.hi <= .5:
        e = exp_interval(ell)
        chi = e / (1 + e)
        product = e / (1 + e) ** 2
    elif x.lo >= .5:
        e = exp_interval(-ell)
        chi = 1 - e / (1 + e)
        product = e / (1 + e) ** 2
    else:
        e = exp_interval(ell)
        chi = e / (1 + e)
        product = chi * (1 - chi)
    product = Interval(max(0., product.lo), min(.25, product.hi))
    derivative = product * (1 / x ** 2 + 1 / (1 - x) ** 2) / width
    return chi, product, derivative


def bump_derivative_interval(s):
    width = Interval(CONTROL_RIGHT) - CONTROL_LEFT
    if s.hi <= CONTROL_LEFT or s.lo >= CONTROL_RIGHT:
        return Interval(0)
    x = (s - CONTROL_LEFT) / width
    x = Interval(max(0., x.lo), min(1., x.hi))
    return _bump_x_derivative_interval(x, width)


def _bump_x_derivative_interval(x, width):
    if x.lo <= 0:
        if x.hi > .25:
            raise ArithmeticError("bump endpoint interval needs subdivision")
        h = Interval(x.hi)
        bound = exp_interval(4 - 1 / h) * (1 / h ** 2 + 1 / (1 - h) ** 2) / width
        return Interval(0, bound.hi)
    if x.hi >= 1:
        reflected = 1 - x
        reflected = Interval(max(0., reflected.lo), min(1., reflected.hi))
        return -_bump_x_derivative_interval(reflected, width)
    value = exp_interval(4 - 1 / x - 1 / (1 - x))
    return value * (1 / x ** 2 - 1 / (1 - x) ** 2) / width


def spline_interval(x, knots, coefficients, degree):
    """de Boor on every intersected knot span, using interval coefficients."""
    spans = [k for k in range(degree, len(coefficients))
             if knots[k] < knots[k + 1] and x.hi >= knots[k] and x.lo <= knots[k + 1]]
    if not spans:
        raise ArithmeticError("spline interval outside the declared domain")
    answers = []
    for k in spans:
        xx = Interval(max(x.lo, knots[k]), min(x.hi, knots[k + 1]))
        values = [Interval.as_interval(coefficients[k - degree + j]) for j in range(degree + 1)]
        for r in range(1, degree + 1):
            for j in range(degree, r - 1, -1):
                lo = knots[j + k - degree]
                hi = knots[j + k - r + 1]
                alpha = (xx - lo) / (Interval(hi) - lo)
                values[j] = (1 - alpha) * values[j - 1] + alpha * values[j]
        answers.append(values[degree])
    return Interval(min(v.lo for v in answers), max(v.hi for v in answers))


class ValidatedTailHeight:
    """Outward Riemann bounds for the same infinite H integral."""
    def __init__(self, deadline, counts, height_width_target=1e-6, maximum_cells=65536):
        self.deadline, self.counts = deadline, counts
        self.maximum = ((Interval(LENGTH) - CORE_END) / ELL).hi
        self.target = height_width_target
        self.maximum_cells = maximum_cells
        self.cells, self.next_id = {}, 0
        self.cache = {}
        self.ready = False

    def check(self):
        if time.monotonic() >= self.deadline:
            raise ClockCheckpoint("continuous positive-chart interval clock")

    def integrand(self, a, b):
        self.counts["interval_integrand_cells"] += 1
        d = Interval(a, b)
        return exp_interval(-(2 - sin_interval(d ** -2)) / d)

    def add_cell(self, left, right):
        value = self.integrand(left, right)
        integral = value * (Interval(right) - left)
        identifier = self.next_id
        self.next_id += 1
        self.cells[identifier] = (left, right, integral.lo, integral.hi, value.lo, value.hi)
        return (-up(integral.hi - integral.lo), identifier)

    def build(self):
        if self.ready:
            return
        points = sorted(set([CUT, .05, .1, .2, .4, .6, 1., 2., 3., self.maximum]))
        heap = []
        for left, right in zip(points[:-1], points[1:]):
            heapq.heappush(heap, self.add_cell(left, right))
        gap = math.fsum(row[3] - row[2] for row in self.cells.values())
        while AMP * ELL * gap > self.target and len(self.cells) < self.maximum_cells:
            self.check()
            _, identifier = heapq.heappop(heap)
            left, right, low, high, _, _ = self.cells.pop(identifier)
            middle = left + (right - left) / 2
            first, second = self.add_cell(left, middle), self.add_cell(middle, right)
            heapq.heappush(heap, first)
            heapq.heappush(heap, second)
            gap = gap - (high - low) - first[0] - second[0]
            # This only schedules work. The final outward prefix interval,
            # not this scheduling sum, is used by the positivity enclosure.
            if len(self.cells) % 256 == 0:
                gap = math.fsum(row[3] - row[2] for row in self.cells.values())
        rows = sorted(self.cells.values())
        self.lefts = [r[0] for r in rows]
        self.rights = [r[1] for r in rows]
        self.values = [Interval(r[4], r[5]) for r in rows]
        omitted = Interval(0, (Interval(CUT) * exp_interval(-1 / Interval(CUT))).hi)
        self.prefix = [omitted]
        for row in rows:
            self.prefix.append(self.prefix[-1] + Interval(row[2], row[3]))
        self.ready = True
        self.receipt = {
            "outward_interval_Riemann_cells": len(rows),
            "delta_cut": CUT,
            "omitted_dimensionless_integral_upper_bound": omitted.hi,
            "full_height_interval_width": (AMP * ELL * self.prefix[-1]).hi - (AMP * ELL * self.prefix[-1]).lo,
            "requested_height_width_target": self.target,
            "cell_capacity_reached": len(rows) >= self.maximum_cells,
            "no_QUADPACK_error_estimate_used_as_a_proof": True,
            "infinite_tail_is_not_redefined_by_the_cut": True,
        }

    def integral(self, delta):
        self.build()
        if delta in self.cache:
            return self.cache[delta]
        if not CUT <= delta <= self.maximum:
            raise ArithmeticError("validated height query outside covered interval")
        import bisect
        index = min(len(self.lefts) - 1, bisect.bisect_right(self.lefts, delta) - 1)
        result = self.prefix[index] + self.values[index] * (Interval(delta) - self.lefts[index])
        self.cache[delta] = result
        return result

    def height(self, s):
        d = (LENGTH - s) / ELL
        dlo, dhi = max(CUT, d.lo), min(self.maximum, d.hi)
        left, right = self.integral(dlo), self.integral(dhi)
        return -AMP * ELL * Interval(left.lo, right.hi)


class ContinuousMean:
    """Scalar/vector analytic spatial jets of the same actual circular model."""
    def __init__(self, deadline, counts):
        self.deadline, self.counts = deadline, counts
        self.spline_a = BSpline(KNOTS, SOURCE_Q[64:72], 5, extrapolate=False)
        self.spline_z = BSpline(KNOTS, SOURCE_Q[72:80], 5, extrapolate=False)
        self.height_cache = {}
        self.quad_error_sum, self.quad_partial_error_max = 0., 0.
        maximum = LENGTH / ELL
        quarter = np.pi / 2
        ks = np.arange(max(1, int(np.ceil(maximum ** -2 / quarter))),
                       int(np.floor(CUT ** -2 / quarter)) + 1)
        oscillation = 1 / np.sqrt(ks * quarter)
        self.breaks = np.unique(np.r_[CUT, maximum, oscillation[(oscillation > CUT) & (oscillation < maximum)]])
        self.cumulative = [0.]
        for left, right in zip(self.breaks[:-1], self.breaks[1:]):
            self.check()
            result = quad(self.integrand, left, right, epsabs=1e-14 / (AMP * ELL * len(self.breaks)),
                          epsrel=1e-13, limit=100, full_output=1)
            value, error, info = result[:3]
            self.counts["height_QUADPACK_RHS"] += int(info["neval"])
            if len(result) > 3:
                self.counts["height_QUADPACK_nonconvergences"] += 1
                raise ArithmeticError("fixed actual height quadrature: " + str(result[3]))
            self.quad_error_sum += AMP * ELL * error
            self.cumulative.append(self.cumulative[-1] + value)
        self.cumulative = np.asarray(self.cumulative)
        self.omitted_bound = AMP * ELL * CUT * np.exp(-1 / CUT)
        self.validated_height = ValidatedTailHeight(deadline, counts)
        self.interval_base_cache = {}
        derivative = [5 * (Interval(SOURCE_Q[73 + j]) - SOURCE_Q[72 + j])
                      / (Interval(KNOTS[j + 6]) - KNOTS[j + 1]) for j in range(7)]
        self.z_derivative_coefficients = derivative

    def check(self):
        if time.monotonic() >= self.deadline:
            raise ClockCheckpoint("true core-return cooperative scientific clock")

    @staticmethod
    def integrand(delta):
        return np.exp(-(2 - np.sin(delta ** -2)) / delta)

    def height_one(self, s):
        self.counts["height_queries"] += 1
        if s in self.height_cache:
            self.counts["height_cache_hits"] += 1
            return self.height_cache[s]
        delta = (LENGTH - s) / ELL
        if delta <= CUT:
            value = 0.
        else:
            index = min(len(self.breaks) - 2, int(np.searchsorted(self.breaks, delta, side="right") - 1))
            left = self.breaks[index]
            result = quad(self.integrand, left, delta, epsabs=1e-14 / (AMP * ELL),
                          epsrel=1e-13, limit=100, full_output=1)
            part, error, info = result[:3]
            self.counts["height_QUADPACK_RHS"] += int(info["neval"])
            if len(result) > 3:
                self.counts["height_QUADPACK_nonconvergences"] += 1
                raise ArithmeticError("partial actual height quadrature: " + str(result[3]))
            self.quad_partial_error_max = max(self.quad_partial_error_max, AMP * ELL * error)
            value = -AMP * ELL * (self.cumulative[index] + part)
        self.height_cache[s] = value
        return value

    @staticmethod
    def step_jets(s, left, right):
        s = np.asarray(s, dtype=float)
        x, width = (s - left) / (right - left), right - left
        active = (x > 0) & (x < 1)
        chi = np.where(x >= 1, 1., 0.)
        comp, first, second = 1 - chi, np.zeros_like(s), np.zeros_like(s)
        y = x[active]
        ell = -1 / y + 1 / (1 - y)
        chi[active], comp[active] = expit(ell), expit(-ell)
        ell1 = (y ** -2 + (1 - y) ** -2) / width
        ell2 = (-2 * y ** -3 + 2 * (1 - y) ** -3) / width ** 2
        prod = chi[active] * comp[active]
        first[active] = prod * ell1
        second[active] = prod * (ell2 + (comp[active] - chi[active]) * ell1 ** 2)
        return chi, comp, first, second

    def base_jets(self, positions):
        self.check()
        s = np.atleast_1d(np.asarray(positions, dtype=float))
        if np.any(s < 0) or np.any(s > LENGTH):
            raise ValueError("mean profile queried outside the original meridian")
        self.counts["continuous_profile_radial_values"] += len(s)
        chi, comp, first, second = self.step_jets(s, CORE_END, LENGTH)
        beta, beta1, beta2 = 4 * chi * comp, 4 * first * (comp - chi), 4 * second * (comp - chi) - 8 * first * first
        x = np.clip((s - CORE_END) / FREE_WIDTH, 0, 1)
        def field(spline):
            p, p1, p2 = spline(x), spline(x, 1) / FREE_WIDTH, spline(x, 2) / FREE_WIDTH ** 2
            return beta * p, beta1 * p + beta * p1, beta2 * p + 2 * beta1 * p1 + beta * p2
        alpha, alpha1, alpha2 = field(self.spline_a)
        correction, correction1, correction2 = field(self.spline_z)
        bg, bgc, bg1, bg2 = self.step_jets(s, CORE_END, BACKGROUND_END)
        r0 = RC + LENGTH - s
        ab = bgc * CIRCLE_RADIUS + bg * r0
        ab1, ab2 = bg1 * (r0 - CIRCLE_RADIUS) - bg, bg2 * (r0 - CIRCLE_RADIUS) - 2 * bg1
        ea = np.exp(alpha)
        a, a1 = ea * ab, ea * (ab1 + ab * alpha1)
        a2 = ea * (ab2 + 2 * ab1 * alpha1 + ab * (alpha2 + alpha1 * alpha1))
        H = np.array([self.height_one(float(value)) for value in s])
        d = (LENGTH - s) / ELL
        H1, H2 = np.zeros_like(s), np.zeros_like(s)
        active = d > 0
        dd = d[active]
        with np.errstate(under="ignore"):
            H1[active] = AMP * np.exp(-(2 - np.sin(dd ** -2)) / dd)
        H2[active] = -H1[active] * ((2 - np.sin(dd ** -2)) / dd ** 2 - 2 * np.cos(dd ** -2) / dd ** 4) / ELL
        central, tail = CORE_HALF + s, SOURCE_Q[-1] + H
        z = bgc * central + bg * tail + correction
        z1 = bgc + bg1 * (tail - central) + bg * H1 + correction1
        z2 = -2 * bg1 + bg2 * (tail - central) + 2 * bg1 * H1 + bg * H2 + correction2
        return (a, a1, a2, z, z1, z2), compact_bump(s)

    def jets(self, positions, control):
        base, bump = self.base_jets(positions)
        a, a1, a2, z, z1, z2 = base
        psi, psi1, psi2 = bump.T
        mu, nu = control
        e = np.exp(mu * psi)
        return (e * a, e * (a1 + a * mu * psi1),
                e * (a2 + 2 * a1 * mu * psi1 + a * (mu * psi2 + mu * mu * psi1 * psi1)),
                z + nu * psi, z1 + nu * psi1, z2 + nu * psi2), bump

    def interval_base(self, left, right):
        key = (left, right)
        if key in self.interval_base_cache:
            self.counts["interval_profile_cache_hits"] += 1
            return self.interval_base_cache[key]
        self.check()
        self.counts["interval_profile_cells"] += 1
        s = Interval(left, right)
        chi, _, chi1 = step_intervals(s, CORE_END, BACKGROUND_END)
        free, product, free1 = step_intervals(s, CORE_END, LENGTH)
        beta, beta1 = 4 * product, 4 * free1 * (1 - 2 * free)
        free_width = Interval(LENGTH) - CORE_END
        x = (s - CORE_END) / free_width
        x = Interval(max(0., x.lo), min(1., x.hi))
        pz = spline_interval(x, KNOTS, SOURCE_Q[72:80], 5)
        pz1 = spline_interval(x, KNOTS[1:-1], self.z_derivative_coefficients, 4) / free_width
        d = (LENGTH - s) / ELL
        w = AMP * exp_interval(-(2 - sin_interval(d ** -2)) / d)
        height = self.validated_height.height(s)
        base = 1 - chi + chi1 * (SOURCE_Q[-1] + height - CORE_HALF - s) + chi * w + beta1 * pz + beta * pz1
        result = (base, bump_derivative_interval(s))
        self.interval_base_cache[key] = result
        return result

    def positive_chart(self, nu_interval, minimum=1e-6, maximum_cells=32768):
        self.validated_height.build()
        points = np.unique(np.r_[np.linspace(CORE_END, BACKGROUND_END, 65),
            CORE_END + FREE_WIDTH * np.array([1/3, 1/2, 2/3]),
            (CORE_END + BACKGROUND_END) / 2,
            CONTROL_LEFT, CONTROL_RIGHT, (CONTROL_LEFT + CONTROL_RIGHT) / 2])
        stack = [(float(a), float(b), 0) for a, b in zip(points[:-1], points[1:])]
        leaves, unresolved = [], []
        nu = Interval(*nu_interval)
        examined = 0
        while stack:
            self.check()
            left, right, depth = stack.pop()
            examined += 1
            try:
                base, derivative = self.interval_base(left, right)
                bound = base + nu * derivative
            except ArithmeticError as error:
                bound = None
                reason = str(error)
            if bound is not None and bound.lo > minimum:
                leaves.append((left, right, bound.lo, bound.hi))
                continue
            if depth >= 24 or examined >= maximum_cells:
                unresolved.append({"s": [left, right], "depth": depth,
                    "z_s_enclosure": None if bound is None else [bound.lo, bound.hi],
                    "reason": reason if bound is None else "positive lower bound not established"})
                unresolved.extend({"s": [a, b], "depth": d, "reason": "unprocessed after declared capacity"}
                                  for a, b, d in stack)
                break
            middle = left + (right - left) / 2
            stack.extend([(left, middle, depth + 1), (middle, right, depth + 1)])
        success = not unresolved and not stack
        # stack is empty after the normal successful pass. On a break all
        # remaining intervals were explicitly copied into unresolved.
        return {"continuous_positive_z_s_chart_established": bool(success),
            "scope_s": [CORE_END, BACKGROUND_END], "scope_nu": list(nu_interval),
            "mu_independent_chart": True, "strict_lower_threshold": minimum,
            "minimum_proved_z_s_lower_bound": min((x[2] for x in leaves), default=None),
            "completed_positive_cells": len(leaves), "examined_cells": examined,
            "unresolved_intervals": unresolved,
            "height_bound_receipt": self.validated_height.receipt,
            "arithmetic_identity": "outward binary64 basic operations; guarded 90-digit Decimal exp/sin endpoints; interval Riemann height including infinite omitted-tail bound",
            "not_a_curve_or_reach_certificate": True}

    def quadrature_receipt(self):
        return {"same_mathematical_infinite_height_definition": True,
            "delta_cut": CUT, "omitted_height_upper_bound": self.omitted_bound,
            "fixed_phase_intervals": len(self.breaks) - 1,
            "fixed_phase_QUADPACK_error_estimate_sum": self.quad_error_sum,
            "largest_partial_QUADPACK_error_estimate": self.quad_partial_error_max,
            "numerical_height_error_is_not_interval_certified": True,
            "continuous_chart_uses_independent_outward_interval_height_bounds": True}

