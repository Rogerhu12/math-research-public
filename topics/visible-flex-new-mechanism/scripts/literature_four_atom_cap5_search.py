#!/usr/bin/env python3
"""New four-curvature-atom five-gate search; no old science is loaded.

The entire oracle is the twelve-term finite-power formula in R498.  All
derivatives are analytic.  A floating candidate is not a zero certificate.
Only the first qualifying candidate receives a rational interval contraction
test, within the same clock and call account.  This file is authored but is
not executed during review.
"""
import time as _time
ENTRY_START = _time.perf_counter()

import argparse
import decimal
import hashlib
import itertools
import json
import math
import os
import pathlib
import sys
import traceback
from fractions import Fraction

PREFIX = "CAP4_RECORD"
FINAL_PREFIX = "CAP4_FINAL_REPORT"
CLOCK_PREFIX = "CAP4_FINAL_CLOCK"
NU = (1, 2, 3, 4, 6)
PHYSICAL_NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "C")
CHART_NAMES = ("mass_logit1", "mass_logit2", "mass_logit3",
               "gap_logit1", "gap_logit2", "gap_logit3", "zeta")
EXPECTED_RUNTIME = {"python": "3.12.14", "numpy": "2.3.5", "scipy": "1.17.0"}
EXPECTED_BUDGET = {
    "entry_seconds": 180, "search_seconds": 150,
    "complete_oracle_calls": 6000, "stdout_soft_bytes": 33554432,
    "rational_integer_bits": 1000000,
}
EXPECTED_SEARCH = {
    "starts": 64, "per_start_max_nfev": 80,
    "per_start_complete_value_and_J_calls": 80,
    "candidate_unscaled_G_infinity": 1e-8,
    "first_six_z_bounds": [-4.0, 4.0],
    "zeta_bounds": [0.0, 1.0-2.0**-10],
    "mass_simplex_floor": "1/12", "mass_softmax_scale": "2/3",
    "gap_simplex_floor": "1/5", "gap_softmax_scale": "1/5",
    "offset": "C=(7/5-Jshape)*zeta",
    "seed_order": "mass_dominant_0_to_3,gap_dominant_0_to_3,zeta",
    "mass_seed_weights": [9, 1, 1, 1],
    "gap_seed_weights": [4, 1, 1, 1],
    "seed_zetas": [0.0, 1.0/64, 1.0/4, 3.0/4],
    "residual_scaling": "(1+H)**(nu/2-4) * (Delta_nu/R5)",
    "ftol": 1e-12, "xtol": 1e-12, "gtol": 1e-10,
}
EXPECTED_CERTIFICATE = {
    "decimal_precision": 80, "decimal_newton_calls": 8,
    "decimal_stop_G": "1e-55", "center_dyadic_bits": 160,
    "inverse_dyadic_bits": 128,
    "box_radius_negative_binary_exponents": [16, 24, 32, 40, 48, 56, 64, 72],
    "minor_selection": "largest_finite_float_logabsdet_then_exact_slice_certificate",
    "positive_C_columns": [0, 1, 2, 3, 4, 5, 6],
    "zero_C_columns": [0, 1, 2, 3, 4, 5],
    "fixed_parameters": "exact_binary64_rationals_from_first_candidate",
    "whole_box_domain": "mass>1/12,gap>1/5,H<2,and_original_C_branch",
    "no_rounding_positive_C_to_zero": True,
}
TABLE = (
    (0, 1, 1, 2, 3, 0),
    (1, -1, 1, 1, 4, 0),
    (2, 3, 2, 2, 1, 2),
    (2, 3, 10, 0, 5, 0),
    (3, -1, 2, 2, 0, 3),
    (3, -3, 1, 1, 2, 2),
    (4, 3, 2, 1, 1, 3),
    (4, 3, 2, 0, 3, 2),
    (5, -1, 4, 1, 0, 4),
    (5, -1, 1, 0, 2, 3),
    (6, 5, 16, 0, 1, 4),
    (7, -3, 80, 0, 0, 5),
)
np = None
scipy = None
least_squares = None
ACTIVE = None
TERMS = None


class StopAccount(RuntimeError):
    pass


class PerStartLimit(RuntimeError):
    pass


class CandidateFound(RuntimeError):
    def __init__(self, data):
        super().__init__("first complete unscaled five-gate floating candidate")
        self.data = data


def elapsed():
    return _time.perf_counter() - ENTRY_START


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False)


class Account:
    def __init__(self, request):
        self.request = request
        b = request["budget"]
        if b != EXPECTED_BUDGET:
            raise ValueError("the one new 180-second account is immutable")
        self.hard = float(b["entry_seconds"])
        self.search = float(b["search_seconds"])
        self.cap = int(b["complete_oracle_calls"])
        self.output_cap = int(b["stdout_soft_bytes"])
        self.max_bits_cap = int(b["rational_integer_bits"])
        self.started = 0
        self.completed = 0
        self.failed = 0
        self.by_mode = {}
        self.cache_hits = 0
        self.sequence = 0
        self.chain = "0" * 64
        self.stdout_bytes = 0
        self.output_limit_reached = False
        self.algebra_ops = 0
        self.max_integer_bits = 0
        self.linear_solves = 0
        self.scipy_optimizer_calls_started = 0
        self.scipy_optimizer_calls_returned = 0
        self.scipy_optimizer_calls_interrupted = 0
        self.scipy_optimizer_calls_failed = 0
        self.minor_determinants_started = 0
        self.minor_determinants_completed = 0
        self.minor_determinants_failed = 0
        self.per_start_started = {}
        self.science_started = False
        self.best = None
        self.best_score = math.inf
        self.best_scaled = math.inf
        self.starts = []
        self.stop_reason = None
        self.active_call = None
        self.phase = "input"
        self.certificate = None

    def check(self, searching=False):
        if self.output_limit_reached:
            raise StopAccount("stdout_soft_limit_after_complete_record")
        if elapsed() >= self.hard:
            raise StopAccount("entry_clock_exhausted")
        if searching and elapsed() >= self.search:
            raise StopAccount("search_clock_exhausted_reserved_certificate_time")

    def record(self, kind, payload):
        body = {"seq": self.sequence + 1, "kind": kind, "payload": payload}
        raw = canonical(body)
        digest = hashlib.sha256((raw + "\n").encode("utf-8")).hexdigest()
        chain = hashlib.sha256(
            bytes.fromhex(self.chain) + bytes.fromhex(digest)
        ).hexdigest()
        line = PREFIX + " " + canonical({
            **body, "payload_sha256": digest, "chain_sha256": chain
        }) + "\n"
        sys.stdout.write(line)
        sys.stdout.flush()
        self.sequence += 1
        self.chain = chain
        self.stdout_bytes += len(line.encode("utf-8"))
        if self.stdout_bytes >= self.output_cap:
            self.output_limit_reached = True
        return {"seq": self.sequence, "sha256": digest, "chain_sha256": chain}

    def begin(self, mode, label, searching=False):
        self.check(searching=searching)
        if self.started >= self.cap:
            raise StopAccount("complete_oracle_call_cap")
        if searching:
            start_index = label.get("start_index")
            if type(start_index) is not int or not 0 <= start_index < 64:
                raise ValueError("a fixed new start index is required")
            used = self.per_start_started.get(start_index, 0)
            if used >= self.request["search"]["per_start_complete_value_and_J_calls"]:
                raise PerStartLimit("this new start reached its 80 complete-call cap")
            self.per_start_started[start_index] = used + 1
        self.started += 1
        bucket = self.by_mode.setdefault(
            mode, {"started": 0, "completed": 0, "failed": 0, "seconds": 0.0}
        )
        bucket["started"] += 1
        token = {"id": self.started, "mode": mode, "label": label,
                 "start": _time.perf_counter()}
        self.active_call = token
        self.record("oracle_started", {
            "call_id": token["id"], "mode": mode, "label": label,
            "entry_elapsed_seconds": elapsed()
        })
        return token

    def finish(self, token, payload, compact=False):
        seconds = _time.perf_counter() - token["start"]
        self.completed += 1
        bucket = self.by_mode[token["mode"]]
        bucket["completed"] += 1
        bucket["seconds"] += seconds
        self.active_call = None
        receipt = self.record("oracle_completed", {
            "call_id": token["id"], "mode": token["mode"],
            "label": token["label"], "seconds": seconds,
            "entry_elapsed_seconds": elapsed(), **payload
        })
        return receipt

    def fail(self, token, exc):
        seconds = _time.perf_counter() - token["start"]
        self.failed += 1
        bucket = self.by_mode[token["mode"]]
        bucket["failed"] += 1
        bucket["seconds"] += seconds
        self.active_call = None
        self.record("oracle_failed", {
            "call_id": token["id"], "mode": token["mode"],
            "label": token["label"], "seconds": seconds,
            "entry_elapsed_seconds": elapsed(),
            "exception_type": type(exc).__name__, "message": str(exc)
        })

    def costs(self):
        return {
            "entry_elapsed_before_final_output_seconds": elapsed(),
            "oracle_started": self.started,
            "oracle_completed": self.completed,
            "oracle_failed": self.failed,
            "by_mode": self.by_mode,
            "cache_hits": self.cache_hits,
            "algebra_operations_guarded": self.algebra_ops,
            "maximum_observed_integer_bits": self.max_integer_bits,
            "new_small_linear_solves": self.linear_solves,
            "new_small_linear_solve_scope": "explicit Decimal slice solves only",
            "scipy_internal_linear_algebra_is_in_the_same_wall_clock": True,
            "scipy_optimizer_calls_started": self.scipy_optimizer_calls_started,
            "scipy_optimizer_calls_returned": self.scipy_optimizer_calls_returned,
            "scipy_optimizer_calls_interrupted": self.scipy_optimizer_calls_interrupted,
            "scipy_optimizer_calls_failed": self.scipy_optimizer_calls_failed,
            "new_candidate_minor_determinants_started": self.minor_determinants_started,
            "new_candidate_minor_determinants_completed": self.minor_determinants_completed,
            "new_candidate_minor_determinants_failed": self.minor_determinants_failed,
            "per_start_complete_oracle_started": dict(self.per_start_started),
            "records": self.sequence,
            "record_chain_sha256": self.chain,
            "stdout_record_bytes": self.stdout_bytes,
            "stdout_soft_limit_reached": self.output_limit_reached,
            "science_started": self.science_started,
            "active_call_if_any": None if self.active_call is None else {
                k: v for k, v in self.active_call.items() if k != "start"
            },
        }


def tick(value=None):
    if ACTIVE is None:
        return
    ACTIVE.algebra_ops += 1
    if ACTIVE.algebra_ops % 128 == 0:
        ACTIVE.check()
        components = ((value.v,) + value.g) if isinstance(value, Jet) else (value,)
        vals = []
        for component in components:
            if isinstance(component, Fraction):
                vals.append(component)
            elif isinstance(component, Interval):
                vals.extend((component.lo, component.hi))
        for q in vals:
            bits = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
            ACTIVE.max_integer_bits = max(ACTIVE.max_integer_bits, bits)
            if bits > ACTIVE.max_bits_cap:
                raise StopAccount("new_rational_integer_bit_cap")


class Interval:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, Fraction) else Fraction(lo)
        self.hi = self.lo if hi is None else (
            hi if isinstance(hi, Fraction) else Fraction(hi)
        )
        if self.lo > self.hi:
            raise ValueError("reversed rational interval")

    @staticmethod
    def get(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, other):
        if isinstance(other, Jet):
            return NotImplemented
        other = self.get(other)
        out = Interval(self.lo + other.lo, self.hi + other.hi)
        tick(out)
        return out

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        if isinstance(other, Jet):
            return NotImplemented
        return self + (-self.get(other))

    def __rsub__(self, other):
        return self.get(other) - self

    def __mul__(self, other):
        if isinstance(other, Jet):
            return NotImplemented
        other = self.get(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        out = Interval(min(products), max(products))
        tick(out)
        return out

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ValueError("interval denominator contains zero")
        out = Interval(1 / self.hi, 1 / self.lo)
        tick(out)
        return out

    def __truediv__(self, other):
        if isinstance(other, Jet):
            return NotImplemented
        return self * self.get(other).reciprocal()

    def __rtruediv__(self, other):
        return self.get(other) / self

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("only integer interval powers are used")
        if exponent < 0:
            return (self ** (-exponent)).reciprocal()
        if exponent == 0:
            return Interval(1)
        if exponent % 2:
            out = Interval(self.lo ** exponent, self.hi ** exponent)
        else:
            upper = max(self.lo ** exponent, self.hi ** exponent)
            lower = (Fraction(0) if self.lo <= 0 <= self.hi
                     else min(self.lo ** exponent, self.hi ** exponent))
            out = Interval(lower, upper)
        tick(out)
        return out

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))


class Jet:
    __slots__ = ("v", "g")

    def __init__(self, value, gradient=None):
        self.v = value
        zero = value * 0
        self.g = tuple(zero for _ in range(7)) if gradient is None else tuple(gradient)

    def get(self, other):
        if isinstance(other, Jet):
            if len(other.g) != len(self.g):
                raise ValueError("incompatible analytic gradient dimensions")
            return other
        return Jet(other + self.v * 0,
                   tuple(self.v * 0 for _ in self.g))

    def __add__(self, other):
        other = self.get(other)
        out = Jet(self.v + other.v, (a + b for a, b in zip(self.g, other.g)))
        tick(out)
        return out

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.v, (-x for x in self.g))

    def __sub__(self, other):
        return self + (-self.get(other))

    def __rsub__(self, other):
        return self.get(other) - self

    def __mul__(self, other):
        other = self.get(other)
        out = Jet(self.v * other.v,
                  (a * other.v + self.v * b for a, b in zip(self.g, other.g)))
        tick(out)
        return out

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.get(other)
        value = self.v / other.v
        out = Jet(value, ((a - value * b) / other.v
                          for a, b in zip(self.g, other.g)))
        tick(out)
        return out

    def __rtruediv__(self, other):
        return self.get(other) / self

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError("Jet is used only with integer powers")
        if exponent == 0:
            return Jet(self.v * 0 + 1, tuple(self.v * 0 for _ in self.g))
        value = self.v ** exponent
        coefficient = exponent * (self.v ** (exponent - 1))
        out = Jet(value, (coefficient * a for a in self.g))
        tick(out)
        return out


def compile_terms():
    terms = []
    for j in range(8):
        for k, numerator, denominator, aa, bb, dd in TABLE:
            if k < j:
                continue
            for ell in range(aa + 1):
                for n in range(k - j + 1):
                    degree = 5 * ell + 3 * bb + dd + 2 * n + 2
                    coefficient = (
                        Fraction(3 * numerator, denominator * degree)
                        * math.comb(k, j) * math.comb(aa, ell)
                        * math.comb(k - j, n)
                        * Fraction(3, 5) ** ell * Fraction(3, 2) ** n
                    )
                    terms.append((j, coefficient, dd - ell - n - 1,
                                  aa - ell, k - j - n, degree))
    return tuple(terms)


def targets(h, a, q):
    a0, a1, a2, a3, a4, a5, a6, a7 = a
    b1 = (h**3*a1 + 24*h**5*(2*h-1)*a7 + 6*h**2*(1-h)*a0
          - q(5, 2)*h**5 + q(21, 5)*h**6)
    b2 = (h**3*a2 + (48*h**4-84*h**5-8*h**6)*a7
          + (-9*h+9*h**2+h**3)*a0
          + q(9, 2)*h**4-q(147, 20)*h**5-q(7, 10)*h**6)
    b3 = (h**3*a3 + (-24*h**3+60*h**5)*a7
          + (4+3*h-8*h**2)*a0
          - q(21, 10)*h**3+q(3, 5)*h**4+q(103, 20)*h**5)
    b4 = (h**3*a4+(36*h**3-40*h**4)*a7+(-6+q(21, 4)*h)*a0
          + q(51, 20)*h**3-q(79, 20)*h**4)
    b5 = (h**3*a5+(-18*h**3+8*h**4)*a7+(10-6*h)*a0/4
          - q(7, 8)*h**3+q(9, 10)*h**4)
    b6 = (h**3*a6+(5*h**3+2*h**4)*a7-(1+h)*a0/4
          + q(3, 80)*h**3+q(3, 20)*h**4)
    rr = (48*h**2-120*h**3,
          -96*h+240*h**2+20*h**3,
          48-72*h-168*h**2,
          -48+164*h,
          -4-34*h,
          8-5*h)
    bs = (b1, b2, b3, b4, b5, b6)
    gs = tuple((rr[4]*bs[n-1]-rr[n-1]*b5)/(h**3*rr[4]) for n in NU)
    deltas = tuple(g * rr[4] for g in gs)
    return gs, deltas, bs, rr


def segment_generic(a, c, tau, low, high, cast):
    result = [a * 0 for _ in range(8)]
    for j, coefficient, ea, ec, et, degree in TERMS:
        co = cast(coefficient.numerator, coefficient.denominator)
        term = co * a**ea * c**ec * tau**et * (high**degree-low**degree)
        result[j] = result[j] + term
    return result


def generic_oracle(theta, cast, active_indices=None):
    """Complete original physical formula; only derivative columns may be sliced."""
    if len(theta) != 7:
        raise ValueError("four atoms require seven physical coordinates")
    active = tuple(range(7) if active_indices is None else active_indices)
    if (len(set(active)) != len(active) or not active
            or any(type(i) is not int or not 0 <= i < 7 for i in active)):
        raise ValueError("invalid physical derivative columns")
    variables = []
    for i, x in enumerate(theta):
        zero = x * 0
        variables.append(Jet(x, tuple(zero + int(i == j) for j in active)))
    zero = variables[0] * 0
    one = zero + 1
    aa = variables[:3] + [one]
    bb = [zero] + variables[3:6] + [one]
    cc = variables[6]
    delta = [1/aa[i]-1/aa[i+1] for i in range(3)]
    constants = [cc]
    for i in range(3):
        constants.append(constants[-1]+cast(3, 5)*delta[i]*bb[i+1]**5)
    times = []
    for i in range(4):
        tau = zero-cast(3, 2)
        for j in range(i, 3):
            tau = tau-cast(3, 2)*delta[j]*bb[j+1]**2
        times.append(tau)
    accum = [zero for _ in range(8)]
    for i in range(4):
        block = segment_generic(aa[i], constants[i], times[i],
                                bb[i], bb[i+1], cast)
        accum = [x+y for x, y in zip(accum, block)]
    hh = cast(3, 5)+constants[3]
    gs, ds, bs, rs = targets(hh, accum, cast)
    return {"H": hh, "Jshape": constants[3]-cc, "A": accum,
            "G": gs, "Delta": ds, "B": bs, "R": rs,
            "active_physical_columns": active}


def number_cast(x):
    if isinstance(x, decimal.Decimal):
        return lambda n, d=1: decimal.Decimal(n)/decimal.Decimal(d)
    if isinstance(x, Fraction):
        return Fraction
    return lambda n, d=1: n/d


def physical_components(theta, cast):
    aa = list(theta[:3]) + [cast(1)]
    bb = [cast(0)] + list(theta[3:6]) + [cast(1)]
    masses = [aa[0]] + [aa[i]-aa[i-1] for i in range(1, 4)]
    gaps = [bb[i+1]-bb[i] for i in range(4)]
    jshape = cast(0)
    for i in range(3):
        jshape = jshape+cast(3, 5)*(1/aa[i]-1/aa[i+1])*bb[i+1]**5
    hh = cast(3, 5)+jshape+theta[6]
    return masses, gaps, jshape, hh


def physical_valid(theta, zero_C=None):
    if len(theta) != 7 or not all(math.isfinite(float(x)) for x in theta):
        return False
    cast = number_cast(theta[0])
    if not (cast(0) < theta[0] < theta[1] < theta[2] < cast(1)
            and cast(0) < theta[3] < theta[4] < theta[5] < cast(1)):
        return False
    masses, gaps, _, hh = physical_components(theta, cast)
    if not (all(x > cast(1, 12) for x in masses)
            and all(x > cast(1, 5) for x in gaps)
            and cast(3, 5) < hh < cast(2) and theta[6] >= cast(0)):
        return False
    if zero_C is True:
        return theta[6] == cast(0)
    if zero_C is False:
        return theta[6] > cast(0)
    return True


def physical_box_domain(box, zero_C):
    """Conservative exact whole-slice enclosure; no chart or sign clipping."""
    if len(box) != 7:
        return {"passed": False, "reason": "seven physical intervals required"}
    mass_margins = [
        box[0].lo-Fraction(1, 12),
        box[1].lo-box[0].hi-Fraction(1, 12),
        box[2].lo-box[1].hi-Fraction(1, 12),
        1-box[2].hi-Fraction(1, 12),
    ]
    gap_margins = [
        box[3].lo-Fraction(1, 5),
        box[4].lo-box[3].hi-Fraction(1, 5),
        box[5].lo-box[4].hi-Fraction(1, 5),
        1-box[5].hi-Fraction(1, 5),
    ]
    c_ok = (box[6].lo == box[6].hi == 0 if zero_C else box[6].lo > 0)
    if not (min(mass_margins) > 0 and min(gap_margins) > 0 and c_ok):
        return {"passed": False, "reason": "mass, gap, or C branch left original domain",
                "mass_margin_lower": [qtext(x) for x in mass_margins],
                "gap_margin_lower": [qtext(x) for x in gap_margins],
                "C": itext(box[6]), "zero_C_slice": bool(zero_C)}
    _, _, jshape, hh = physical_components(
        box, lambda n, d=1: Interval(Fraction(n, d)))
    passed = hh.lo > Fraction(3, 5) and hh.hi < 2
    return {"passed": bool(passed),
            "mass_margin_lower": [qtext(x) for x in mass_margins],
            "gap_margin_lower": [qtext(x) for x in gap_margins],
            "Jshape": itext(jshape), "H": itext(hh),
            "H_upper_margin": qtext(2-hh.hi),
            "C": itext(box[6]), "zero_C_slice": bool(zero_C)}


class FloatOracle:
    def __init__(self, account):
        self.account = account
        self.index = np.array([x[0] for x in TERMS], dtype=np.int64)
        self.co = np.array([float(x[1]) for x in TERMS])
        self.ea = np.array([x[2] for x in TERMS], dtype=np.int64)
        self.ec = np.array([x[3] for x in TERMS], dtype=np.int64)
        self.et = np.array([x[4] for x in TERMS], dtype=np.int64)
        self.nn = np.array([x[5] for x in TERMS], dtype=np.int64)
        self.last_z = None
        self.last_data = None
        self.cache = {}
        self.current_start = None

    def segment(self, a, c, tau, low, high):
        """Analytic power derivatives, including exact C=0 without 0/0."""
        pa = np.power(a, self.ea)
        pc = np.power(c, self.ec)
        pt = np.power(tau, self.et)
        end = np.power(high, self.nn)-np.power(low, self.nn)
        common = self.co*pa*pc*pt
        value = common*end
        da = self.co*self.ea*np.power(a, self.ea-1)*pc*pt*end
        dc = np.zeros_like(value)
        mask = self.ec != 0
        dc[mask] = (self.co[mask]*pa[mask]*self.ec[mask]
                    *np.power(c, self.ec[mask]-1)*pt[mask]*end[mask])
        dtau = np.zeros_like(value)
        mask = self.et != 0
        dtau[mask] = (self.co[mask]*pa[mask]*pc[mask]*self.et[mask]
                      *np.power(tau, self.et[mask]-1)*end[mask])
        rows = (
            value, da, dc, dtau,
            -common*self.nn*np.power(low, self.nn-1),
            common*self.nn*np.power(high, self.nn-1),
        )
        return np.stack([np.bincount(self.index, weights=row, minlength=8)
                         for row in rows], axis=1)

    def physical(self, theta):
        if not physical_valid(theta):
            raise ValueError("physical point is outside the new genuine four-atom family")
        basis = np.eye(7)
        zero = np.zeros(7)
        aa = list(theta[:3])+[1.0]
        daa = [basis[i] for i in range(3)]+[zero]
        bb = [0.0]+list(theta[3:6])+[1.0]
        dbb = [zero]+[basis[i] for i in range(3, 6)]+[zero]
        delta = [1/aa[i]-1/aa[i+1] for i in range(3)]
        ddelta = [-daa[i]/aa[i]**2+daa[i+1]/aa[i+1]**2
                  for i in range(3)]
        constants = [float(theta[6])]
        dconstants = [basis[6]]
        for i in range(3):
            constants.append(constants[-1]+3*delta[i]*bb[i+1]**5/5)
            dconstants.append(dconstants[-1]+3*bb[i+1]**5*ddelta[i]/5
                              +3*delta[i]*bb[i+1]**4*dbb[i+1])
        times, dtimes = [], []
        for i in range(4):
            tau, dtau = -1.5, zero.copy()
            for j in range(i, 3):
                tau -= 1.5*delta[j]*bb[j+1]**2
                dtau -= (1.5*bb[j+1]**2*ddelta[j]
                         +3*delta[j]*bb[j+1]*dbb[j+1])
            times.append(tau)
            dtimes.append(dtau)
        av, aj = np.zeros(8), np.zeros((8, 7))
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            for i in range(4):
                values = (aa[i], constants[i], times[i], bb[i], bb[i+1])
                chain = np.stack((daa[i], dconstants[i], dtimes[i], dbb[i], dbb[i+1]))
                block = self.segment(*values)
                av += block[:, 0]
                aj += block[:, 1:] @ chain
            hh = 0.6+constants[3]
            jets = [Jet(float(av[i]), aj[i]) for i in range(8)]
            gj, dj, bj, rj = targets(
                Jet(float(hh), dconstants[3]), jets, lambda n, d=1: n/d)
            gv = np.array([x.v for x in gj], dtype=float)
            jg = np.array([x.g for x in gj], dtype=float)
            dv = np.array([x.v for x in dj], dtype=float)
        if not all(np.all(np.isfinite(x)) for x in
                   (av, aj, gv, jg, dv, dconstants[3])):
            raise FloatingPointError("nonfinite complete four-segment value or analytic J")
        masses, gaps, jshape, _ = physical_components(theta, lambda n, d=1: n/d)
        atom_time = [times[i]+1.5*bb[i]**2/aa[i] for i in range(4)]
        return {
            "H": float(hh), "Jshape": float(jshape),
            "A": av, "DA": aj, "G": gv, "DG": jg, "Delta": dv,
            "DH": dconstants[3], "mass_proportions": list(masses),
            "xi_gap_proportions": list(gaps), "atom_times": atom_time,
            "atom_curvature_masses": [2*x/3 for x in masses],
            "segment_constants": constants, "segment_taus": times,
            "B": [float(x.v) for x in bj], "R": [float(x.v) for x in rj],
        }

    @staticmethod
    def chart(z):
        mass_logits = np.array([*z[:3], 0.0], dtype=float)
        gap_logits = np.array([*z[3:6], 0.0], dtype=float)
        mass_exp = np.exp(mass_logits-np.max(mass_logits))
        gap_exp = np.exp(gap_logits-np.max(gap_logits))
        mass_softmax = mass_exp/np.sum(mass_exp)
        gap_softmax = gap_exp/np.sum(gap_exp)
        masses = 1/12+(2/3)*mass_softmax
        gaps = 1/5+(1/5)*gap_softmax
        aa = np.cumsum(masses)[:3]
        bb = np.cumsum(gaps)[:3]
        chain = np.zeros((7, 7))
        for k in range(3):
            mass_prefix = float(np.sum(mass_softmax[:k+1]))
            gap_prefix = float(np.sum(gap_softmax[:k+1]))
            for j in range(3):
                chain[k, j] = (2/3)*mass_softmax[j]*(int(j <= k)-mass_prefix)
                chain[k+3, j+3] = (1/5)*gap_softmax[j]*(int(j <= k)-gap_prefix)
        full_a = list(aa)+[1.0]
        delta = np.array([1/full_a[i]-1/full_a[i+1] for i in range(3)])
        jshape = float((3/5)*np.sum(delta*bb**5))
        dj_shape = np.zeros(6)
        for i in range(3):
            dj_shape[i] -= (3/5)*bb[i]**5/full_a[i]**2
            if i+1 < 3:
                dj_shape[i+1] += (3/5)*bb[i]**5/full_a[i+1]**2
            dj_shape[3+i] += 3*delta[i]*bb[i]**4
        zeta = float(z[6])
        factor = 1.4-jshape
        cc = factor*zeta
        chain[6, :6] = -zeta*(dj_shape @ chain[:6, :6])
        chain[6, 6] = factor
        theta = np.array([*aa, *bb, cc])
        return theta, chain

    def evaluate(self, z):
        z = np.asarray(z, dtype=float)
        self.account.check(searching=True)
        if (z.shape != (7,) or not np.all(np.isfinite(z))
                or np.any(z[:6] < -4) or np.any(z[:6] > 4)
                or not 0 <= z[6] <= 1-2**-10):
            raise ValueError("invalid new seven-coordinate search point")
        key = tuple(float(value).hex() for value in z)
        if key in self.cache:
            self.account.cache_hits += 1
            return self.cache[key]
        token = self.account.begin(
            "float_value_and_analytic_J",
            {"start_index": self.current_start, "z": z.tolist()}, searching=True)
        try:
            theta, chain = self.chart(z)
            data = self.physical(theta)
            powers = np.array([n/2-4 for n in NU])
            scale = np.power(1+data["H"], powers)
            fv = scale*data["G"]
            jf_physical = (scale[:, None]*data["DG"]
                           + (powers*scale*data["G"]/(1+data["H"]))[:, None]
                           *data["DH"][None, :])
            jf = jf_physical @ chain
            if not np.all(np.isfinite(jf)) or not np.all(np.isfinite(fv)):
                raise FloatingPointError("nonfinite scaled residual or chart Jacobian")
            ginf = float(np.max(np.abs(data["G"])))
            fnorm = float(np.linalg.norm(fv))
            payload = {
                "start_index": self.current_start, "z_chart7": z.tolist(),
                "theta_physical7": theta.tolist(), "physical_order": list(PHYSICAL_NAMES),
                "H": data["H"], "Jshape": data["Jshape"],
                "mass_proportions": data["mass_proportions"],
                "xi_gap_proportions": data["xi_gap_proportions"],
                "atom_times": data["atom_times"],
                "atom_curvature_masses": data["atom_curvature_masses"],
                "segment_constants": data["segment_constants"],
                "segment_taus": data["segment_taus"],
                "A0_through_A7": data["A"].tolist(),
                "DA_physical_8_by_7": data["DA"].tolist(),
                "Delta_1_2_3_4_6": data["Delta"].tolist(),
                "G_1_2_3_4_6": data["G"].tolist(),
                "DG_physical_5_by_7": data["DG"].tolist(),
                "DH_physical": data["DH"].tolist(),
                "Dtheta_chart_7_by_7": chain.tolist(),
                "F_scaled": fv.tolist(), "DF_chart_5_by_7": jf.tolist(),
                "unscaled_G_infinity": ginf, "scaled_F_euclidean": fnorm,
                "C_is_exactly_zero_in_this_float_input": bool(theta[6] == 0.0),
                "physical_legal": True,
                "no_quadrature_ODE_or_old_science_called": True,
            }
            receipt = self.account.finish(token, payload)
        except BaseException as exc:
            if self.account.active_call is token:
                self.account.fail(token, exc)
            raise
        data.update({"theta": theta, "z": z.copy(), "F": fv, "DF": jf,
                     "G_infinity": ginf, "F_norm": fnorm, "receipt": receipt})
        self.last_z, self.last_data = z.copy(), data
        self.cache[key] = data
        if ginf < self.account.best_score:
            self.account.best_score = ginf
            self.account.best_scaled = fnorm
            self.account.best = payload | {"record": receipt}
        self.account.check()
        if ginf <= self.account.request["search"]["candidate_unscaled_G_infinity"]:
            raise CandidateFound(data)
        self.account.check(searching=True)
        return data

    def fun(self, z):
        return self.evaluate(z)["F"]

    def jac(self, z):
        return self.evaluate(z)["DF"]


def cast_decimal(n, d=1):
    return decimal.Decimal(n)/decimal.Decimal(d)


def decimal_solve(matrix, rhs):
    ACTIVE.linear_solves += 1
    size = len(matrix)
    multiple = isinstance(rhs[0], (list, tuple))
    rr = [list(x) if multiple else [x] for x in rhs]
    width = len(rr[0])
    a = [list(matrix[i]) + rr[i] for i in range(size)]
    for k in range(size):
        ACTIVE.check()
        pivot = max(range(k, size), key=lambda i: abs(a[i][k]))
        if a[pivot][k] == 0:
            raise ValueError("singular new candidate Decimal Jacobian")
        a[k], a[pivot] = a[pivot], a[k]
        div = a[k][k]
        a[k] = [x/div for x in a[k]]
        for i in range(size):
            if i == k:
                continue
            factor = a[i][k]
            a[i] = [x-factor*y for x, y in zip(a[i], a[k])]
    result = [row[size:size+width] for row in a]
    return result if multiple else [row[0] for row in result]


def qtext(q):
    q = q if isinstance(q, Fraction) else Fraction(q)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def itext(x):
    x = Interval.get(x)
    return {"lo": qtext(x.lo), "hi": qtext(x.hi)}


def floor_dyadic(q, bits):
    denominator = 1 << bits
    return Fraction((q.numerator*denominator)//q.denominator, denominator)


def ceil_dyadic(q, bits):
    return -floor_dyadic(-q, bits)


def nearest_dyadic(q, bits):
    denominator = 1 << bits
    scaled = q*denominator
    base = scaled.numerator//scaled.denominator
    if scaled-Fraction(base) >= Fraction(1, 2):
        base += 1
    return Fraction(base, denominator)


def outward_dyadic(x, bits):
    x = Interval.get(x)
    return Interval(floor_dyadic(x.lo, bits), ceil_dyadic(x.hi, bits))


def generic_call(theta, mode, label, cast, summary, *, active_indices=None):
    token = ACTIVE.begin(mode, label)
    try:
        result = generic_oracle(theta, cast, active_indices=active_indices)
        payload = summary(result)
        receipt = ACTIVE.finish(token, payload)
        ACTIVE.check()
        return result, receipt
    except BaseException as exc:
        if ACTIVE.active_call is token:
            ACTIVE.fail(token, exc)
        raise


def select_candidate_slice(candidate):
    theta = candidate["theta"]
    if not physical_valid(theta):
        raise ValueError("first floating candidate is outside the declared physical family")
    zero_C = bool(theta[6] == 0.0)
    allowed = tuple(range(6) if zero_C else range(7))
    matrix = np.asarray(candidate["DG"], dtype=float)
    if matrix.shape != (5, 7) or not np.all(np.isfinite(matrix)):
        raise ValueError("the paid physical five-by-seven Jacobian is required")
    attempts, chosen, best = [], None, -math.inf
    for columns in itertools.combinations(allowed, 5):
        ACTIVE.check()
        item = {"physical_columns": list(columns), "status": "started"}
        started = _time.perf_counter()
        ACTIVE.minor_determinants_started += 1
        try:
            sign, logabsdet = np.linalg.slogdet(matrix[:, columns])
            ACTIVE.minor_determinants_completed += 1
            item.update(status="returned", sign=float(sign),
                        log_abs_det=float(logabsdet) if math.isfinite(float(logabsdet)) else None,
                        finite_nonzero=bool(sign != 0 and math.isfinite(float(logabsdet))))
            if item["finite_nonzero"] and float(logabsdet) > best:
                chosen, best = tuple(columns), float(logabsdet)
        except Exception as exc:
            ACTIVE.minor_determinants_failed += 1
            item.update(status="raised", error={
                "type": type(exc).__name__, "message": str(exc)})
        item["seconds"] = _time.perf_counter()-started
        attempts.append(item)
        ACTIVE.certificate = {
            "passed": False, "status": "floating_minor_selection_in_progress",
            "candidate_record": candidate["receipt"], "zero_C_slice": zero_C,
            "last_minor_attempt": item,
        }
        ACTIVE.record("candidate_physical_minor_attempt", item)
        ACTIVE.check()
    record = {
        "candidate_record": candidate["receipt"],
        "zero_C_slice": zero_C, "allowed_physical_columns": list(allowed),
        "selection_uses_only_already_computed_candidate_DG": True,
        "attempts": attempts,
        "selected_physical_columns": None if chosen is None else list(chosen),
        "float_determinant_is_not_a_rank_or_root_certificate": True,
        "no_positive_C_was_rounded_to_zero": True,
    }
    receipt = ACTIVE.record("candidate_physical_minor_selection", record)
    if chosen is None:
        raise ValueError("no finite nonzero floating minor was found for the permitted slice")
    fixed = tuple(i for i in range(7) if i not in chosen)
    fixed_values = {i: Fraction.from_float(float(theta[i])) for i in fixed}
    if zero_C and (6 not in fixed or fixed_values[6] != 0):
        raise ValueError("C=0 candidate must fix exact C and use five shape columns")
    return chosen, fixed, fixed_values, zero_C, receipt


def certify_first_candidate(candidate, request):
    ACTIVE.phase = "first_new_candidate_slice_and_rational_certificate"
    settings = request["certificate"]
    columns, fixed, fixed_values, zero_C, minor_receipt = select_candidate_slice(candidate)
    slice_spec = {
        "active_physical_columns": list(columns),
        "active_physical_names": [PHYSICAL_NAMES[i] for i in columns],
        "fixed_physical_columns": list(fixed),
        "fixed_physical_rationals": {
            PHYSICAL_NAMES[i]: qtext(fixed_values[i]) for i in fixed},
        "zero_C_slice": zero_C, "minor_selection_record": minor_receipt,
        "target": "all five original G on one fixed two-parameter physical slice",
    }
    ACTIVE.certificate = {"passed": False, "status": "slice_selected", **slice_spec}
    ACTIVE.record("candidate_exact_physical_slice", slice_spec)
    with decimal.localcontext() as context:
        context.prec = int(settings["decimal_precision"])
        binary_input = [Fraction.from_float(float(x)) for x in candidate["theta"]]
        theta = [cast_decimal(x.numerator, x.denominator) for x in binary_input]
        for i in fixed:
            theta[i] = cast_decimal(fixed_values[i].numerator, fixed_values[i].denominator)
        data = None
        for iteration in range(int(settings["decimal_newton_calls"])):
            if not physical_valid(theta, zero_C=zero_C):
                raise ValueError("new Decimal slice point left the strict original domain")
            data, receipt = generic_call(
                theta, "decimal_complete_value_and_slice_analytic_J",
                {"iteration": iteration, "theta_physical7": [str(x) for x in theta],
                 "active_physical_columns": list(columns)},
                cast_decimal,
                lambda out: {
                    "theta_physical7": [str(x) for x in theta],
                    "active_physical_columns": list(columns), "zero_C_slice": zero_C,
                    "H": str(out["H"].v), "Jshape": str(out["Jshape"].v),
                    "A0_through_A7": [str(x.v) for x in out["A"]],
                    "G_1_2_3_4_6": [str(x.v) for x in out["G"]],
                    "DG_slice_5_by_5": [[str(y) for y in x.g] for x in out["G"]],
                    "Delta_1_2_3_4_6": [str(x.v) for x in out["Delta"]],
                }, active_indices=columns)
            values = [x.v for x in data["G"]]
            jacobian = [list(x.g) for x in data["G"]]
            ACTIVE.certificate.update(status="decimal_slice_value_completed",
                                      last_decimal_record=receipt, decimal_iteration=iteration)
            if max(abs(x) for x in values) <= decimal.Decimal(settings["decimal_stop_G"]):
                break
            if iteration+1 == int(settings["decimal_newton_calls"]):
                break
            direction = decimal_solve(jacobian, [-x for x in values])
            next_theta = list(theta)
            for j, physical_index in enumerate(columns):
                next_theta[physical_index] += direction[j]
            if not physical_valid(next_theta, zero_C=zero_C):
                raise ValueError("full new Decimal correction leaves the fixed physical slice domain")
            theta = next_theta
        if data is None:
            raise RuntimeError("no new Decimal candidate value")
        matrix = [list(x.g) for x in data["G"]]
        identity = [[decimal.Decimal(i == j) for j in range(5)] for i in range(5)]
        inverse = decimal_solve(matrix, identity)
        center = [
            fixed_values[i] if i in fixed_values
            else nearest_dyadic(Fraction(theta[i]), int(settings["center_dyadic_bits"]))
            for i in range(7)
        ]
        bb = [[nearest_dyadic(Fraction(x), int(settings["inverse_dyadic_bits"]))
               for x in row] for row in inverse]
    if not physical_valid(center, zero_C=zero_C):
        raise ValueError("dyadic slice center is outside the strict original domain")
    exact, center_receipt = generic_call(
        center, "exact_rational_slice_center_complete_value_and_J",
        {"center_physical7": [qtext(x) for x in center],
         "active_physical_columns": list(columns)}, Fraction,
        lambda out: {
            "center_physical7": [qtext(x) for x in center],
            "active_physical_columns": list(columns), "zero_C_slice": zero_C,
            "H_outward": itext(outward_dyadic(out["H"].v, 160)),
            "A0_through_A7_outward": [
                itext(outward_dyadic(x.v, 160)) for x in out["A"]],
            "G_outward": [itext(outward_dyadic(x.v, 160)) for x in out["G"]],
            "DG_slice_outward": [
                [itext(outward_dyadic(y, 128)) for y in x.g] for x in out["G"]],
        }, active_indices=columns)
    ff = [outward_dyadic(x.v, 160) for x in exact["G"]]
    ACTIVE.certificate.update(status="rational_slice_center_completed",
                              center_record=center_receipt,
                              center_physical7=[qtext(x) for x in center])
    best_failure = None
    for exponent in settings["box_radius_negative_binary_exponents"]:
        ACTIVE.check()
        radius = Fraction(1, 1 << int(exponent))
        box = [
            Interval(x-radius, x+radius) if i in columns else Interval(x)
            for i, x in enumerate(center)
        ]
        domain = physical_box_domain(box, zero_C)
        if not domain["passed"]:
            ACTIVE.record("certificate_box_domain_rejected", {
                "negative_binary_exponent": exponent, "center_record": center_receipt,
                "slice": slice_spec, "domain": domain,
            })
            continue
        interval_data, box_receipt = generic_call(
            box, "rational_interval_complete_slice_value_and_analytic_J",
            {"negative_binary_exponent": exponent, "radius": qtext(radius),
             "active_physical_columns": list(columns)},
            lambda n, d=1: Interval(Fraction(n, d)),
            lambda out: {
                "negative_binary_exponent": exponent, "radius": qtext(radius),
                "active_physical_columns": list(columns), "zero_C_slice": zero_C,
                "H_outward": itext(outward_dyadic(out["H"].v, 128)),
                "A0_through_A7_outward": [
                    itext(outward_dyadic(x.v, 128)) for x in out["A"]],
                "G_outward": [itext(outward_dyadic(x.v, 128)) for x in out["G"]],
                "DG_slice_outward": [
                    [itext(outward_dyadic(y, 128)) for y in x.g] for x in out["G"]],
            }, active_indices=columns)
        jj = [[outward_dyadic(y, 128) for y in x.g] for x in interval_data["G"]]
        error = []
        for i in range(5):
            row = []
            for j in range(5):
                product = sum((bb[i][k]*jj[k][j] for k in range(5)), Interval(0))
                row.append(Interval(i == j)-product)
            error.append(row)
        q_bound = max(sum(x.abs_upper() for x in row) for row in error)
        bf = [sum((bb[i][k]*ff[k] for k in range(5)), Interval(0)) for i in range(5)]
        eta = max(x.abs_upper() for x in bf)
        q_upper, eta_upper = ceil_dyadic(q_bound, 160), ceil_dyadic(eta, 160)
        image_upper = eta_upper+q_upper*radius
        passed = (domain["passed"] and interval_data["H"].v.hi < 2
                  and q_upper < 1 and image_upper < radius)
        certificate = {
            **slice_spec, "passed": bool(passed), "status": "rational_contraction_test",
            "center_record": center_receipt, "box_record": box_receipt,
            "center_physical7": [qtext(x) for x in center],
            "radius_in_the_five_active_physical_coordinates": qtext(radius),
            "B_rational_5_by_5": [[qtext(x) for x in row] for row in bb],
            "G_at_center_outward": [itext(x) for x in ff],
            "DG_slice_box_outward": [[itext(x) for x in row] for row in jj],
            "contraction_q_upper": qtext(q_upper),
            "center_displacement_upper": qtext(eta_upper),
            "self_map_radius_upper": qtext(image_upper),
            "whole_physical_box_domain": domain,
            "unique_exact_root_in_selected_five_dimensional_slice": bool(passed),
            "selected_physical_minor_invertible_on_box": bool(passed),
            "full_seven_parameter_root_isolated": False,
            "C_zero_certificate_does_not_use_C_derivative": bool(zero_C and 6 not in columns),
            "smooth_cap_explicitly_constructed": False,
            "full_original_mechanism_resolved": False,
        }
        ACTIVE.record("rational_contraction_test", certificate)
        ACTIVE.certificate = certificate
        if passed:
            return certificate
        best_failure = certificate
    result = {
        **slice_spec, "passed": False,
        "reason": "finite new fixed-parameter rational boxes did not certify",
        "last_test": best_failure,
    }
    ACTIVE.certificate = result
    return result


def start_points():
    rows = []
    for mass_dominant in range(4):
        mass_weights = [9 if i == mass_dominant else 1 for i in range(4)]
        mass_logits = [math.log(mass_weights[i]/mass_weights[3]) for i in range(3)]
        for gap_dominant in range(4):
            gap_weights = [4 if i == gap_dominant else 1 for i in range(4)]
            gap_logits = [math.log(gap_weights[i]/gap_weights[3]) for i in range(3)]
            for zeta in (0.0, 1.0/64, 1.0/4, 3.0/4):
                rows.append({
                    "mass_dominant": mass_dominant, "gap_dominant": gap_dominant,
                    "zeta": zeta, "mass_weights": mass_weights,
                    "gap_weights": gap_weights,
                    "z": mass_logits+gap_logits+[zeta],
                })
    return rows


def _validate_request(request, topic):
    if request["schema"] != "four-curvature-atom-cap5-first-search-request-v1":
        raise ValueError("wrong new request schema")
    if request["entry_point"] != "scripts/literature_four_atom_cap5_search.py":
        raise ValueError("wrong new entry point")
    if request["scientific_scope"] != "new_four_separated_curvature_atoms_complete_five_gates":
        raise ValueError("wrong new scientific scope")
    if request["paper_reference"] != "R498":
        raise ValueError("the complete four-segment original formula must be referenced")
    if request["budget"] != EXPECTED_BUDGET:
        raise ValueError("budget must match the frozen one-account contract")
    if request["search"] != EXPECTED_SEARCH:
        raise ValueError("seven-coordinate chart or fixed 64-start contract changed")
    if request["certificate"] != EXPECTED_CERTIFICATE:
        raise ValueError("first candidate physical-slice certificate contract changed")
    if request["runtime"] != EXPECTED_RUNTIME:
        raise ValueError("the pinned runtime declaration changed")
    identities = {}
    for specification in request["source_manifest"]:
        name = specification["path"]
        if name in identities:
            raise ValueError("duplicate source manifest path")
        path = topic/name
        data = path.read_bytes()
        actual = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        if actual["bytes"] != specification["bytes"] or actual["sha256"] != specification["sha256"]:
            raise ValueError("bound new source bytes/hash changed: "+name)
        identities[name] = actual
    if "scripts/literature_four_atom_cap5_search.py" not in identities:
        raise ValueError("the new entry source must itself be bound")
    paper = "results/R498-four-separated-curvature-atoms-and-complete-seven-parameter-cap5-design.md"
    if identities.get(paper) != {
            "bytes": 17416,
            "sha256": "7e5261cb66f63837f8e85cc25f04be448f8c23fdbdc70224c4235bf4ee18ce25"}:
        raise ValueError("the published final R498 formula source must be pinned")
    for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                 "NUMEXPR_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise ValueError("single-thread environment missing: "+name)
    if sys.version.split()[0] != request["runtime"]["python"]:
        raise ValueError("pinned Python version changed")
    commit = os.environ.get("CAP4_SOURCE_SHA", "")
    if len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit):
        raise ValueError("the actual CAP4 workflow source commit is required")
    return identities


def science(request, report):
    global np, scipy, least_squares, TERMS
    ACTIVE.science_started = True
    ACTIVE.phase = "new_imports_and_four_segment_finite_coefficient_preparation"
    ACTIVE.check()
    import numpy as _np
    import scipy as _scipy
    from scipy.optimize import least_squares as _least_squares
    np, scipy, least_squares = _np, _scipy, _least_squares
    if np.__version__ != request["runtime"]["numpy"]:
        raise ValueError("pinned numpy version changed")
    if scipy.__version__ != request["runtime"]["scipy"]:
        raise ValueError("pinned scipy version changed")
    TERMS = compile_terms()
    ACTIVE.record("new_finite_formula_ready", {
        "density_rows": [list(x) for x in TABLE],
        "finite_terms_per_segment": len(TERMS), "segments": 4, "maximum_power": 21,
        "physical_order": list(PHYSICAL_NAMES), "chart_order": list(CHART_NAMES),
        "runtime": {"python": sys.version.split()[0], "numpy": np.__version__,
                    "scipy": scipy.__version__},
        "old_paid_log_reads": 0, "old_ODE_calls": 0, "new_quadrature_calls": 0,
        "old_rank_or_mapper_calls": 0, "development_checks": 0,
        "old_three_atom_or_cap15_account_reopened": False,
        "formula_scope": "complete twelve L terms, four segments, eight A_j, all five original G",
        "zero_C_analytic_derivatives_use_power_rules_not_division_by_C": True,
        "physical_DG_shape": [5, 7],
        "first_candidate_certificate_only_on_one_fixed_five_dimensional_slice": True,
    })
    ACTIVE.check()
    oracle = FloatOracle(ACTIVE)
    lower = np.array([-4.0]*6+[0.0])
    upper = np.array([4.0]*6+[1.0-2.0**-10])
    candidate = None
    ACTIVE.phase = "new_fixed_64_start_four_atom_finite_power_search"
    seeds = start_points()
    if len(seeds) != request["search"]["starts"]:
        raise ValueError("the literal new start family changed")
    report["fixed_start_definitions"] = seeds
    for index, seed in enumerate(seeds):
        ACTIVE.check(searching=True)
        oracle.current_start = index
        started = _time.perf_counter()
        initial = seed["z"]
        item = {"index": index, "definition": seed, "initial_z": initial,
                "status": "started"}
        ACTIVE.starts.append(item)
        ACTIVE.record("optimization_start", item)
        backend_started = False
        try:
            # Pay the literal boundary seed once before TRF's feasible-interior
            # adjustment.  Its value and J remain in this same cache/account.
            oracle.evaluate(np.array(initial, dtype=float))
            ACTIVE.check(searching=True)
            ACTIVE.scipy_optimizer_calls_started += 1
            backend_started = True
            result = least_squares(
                oracle.fun, np.array(initial), jac=oracle.jac,
                bounds=(lower, upper), method="trf", tr_solver="exact",
                x_scale="jac", max_nfev=request["search"]["per_start_max_nfev"],
                ftol=request["search"]["ftol"], xtol=request["search"]["xtol"],
                gtol=request["search"]["gtol"])
            ACTIVE.scipy_optimizer_calls_returned += 1
            backend_started = False
            item.update({
                "status": "returned", "scipy_status": int(result.status),
                "message": str(result.message), "nfev": int(result.nfev),
                "njev": None if result.njev is None else int(result.njev),
                "final_z": result.x.tolist(), "scaled_cost": float(result.cost),
                "floating_optimality": float(result.optimality),
                "complete_oracle_calls_started": ACTIVE.per_start_started.get(index, 0),
                "seconds": _time.perf_counter()-started,
                "optimizer_return_is_not_a_root_or_stationarity_certificate": True,
            })
            ACTIVE.record("optimization_return", item)
        except CandidateFound as found:
            if backend_started:
                ACTIVE.scipy_optimizer_calls_interrupted += 1
            candidate = found.data
            item.update({"status": "first_floating_candidate",
                         "record": candidate["receipt"],
                         "complete_oracle_calls_started": ACTIVE.per_start_started.get(index, 0),
                         "seconds": _time.perf_counter()-started})
            ACTIVE.record("optimization_candidate_stop", item)
            break
        except PerStartLimit as exc:
            if backend_started:
                ACTIVE.scipy_optimizer_calls_interrupted += 1
            item.update({
                "status": "per_start_complete_call_limit", "message": str(exc),
                "complete_oracle_calls_started": ACTIVE.per_start_started.get(index, 0),
                "seconds": _time.perf_counter()-started,
            })
            ACTIVE.record("optimization_per_start_limit", item)
        except StopAccount:
            if backend_started:
                ACTIVE.scipy_optimizer_calls_interrupted += 1
            item.update({
                "status": "account_stop",
                "complete_oracle_calls_started": ACTIVE.per_start_started.get(index, 0),
                "seconds": _time.perf_counter()-started,
            })
            ACTIVE.record("optimization_account_stop", item)
            raise
        except Exception as exc:
            if backend_started:
                ACTIVE.scipy_optimizer_calls_failed += 1
            item.update({
                "status": "optimizer_failure", "exception_type": type(exc).__name__,
                "message": str(exc),
                "complete_oracle_calls_started": ACTIVE.per_start_started.get(index, 0),
                "seconds": _time.perf_counter()-started,
            })
            ACTIVE.record("optimization_failure", item)
    if candidate is not None:
        report["floating_candidate_record"] = candidate["receipt"]
        report["candidate_physical_theta7"] = candidate["theta"].tolist()
        report["candidate_chart7"] = candidate["z"].tolist()
        report["candidate_C_exactly_zero_in_float"] = bool(candidate["theta"][6] == 0.0)
        try:
            certificate = certify_first_candidate(candidate, request)
            report["certificate"] = certificate
            report["outcome"] = (
                "certified_regular_four_atom_five_gate_physical_slice_root"
                if certificate.get("passed")
                else "floating_candidate_not_certified_by_finite_new_slice_boxes"
            )
        except BaseException as exc:
            report["certificate_failure"] = {
                "exception_type": type(exc).__name__, "message": str(exc),
                "entry_elapsed_seconds": elapsed(),
            }
            ACTIVE.stop_reason = str(exc)
            report["outcome"] = "floating_candidate_certificate_failed_or_budget_stopped"
            if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                raise
    else:
        report["outcome"] = "finite_new_four_atom_model_search_no_five_gate_candidate"
    ACTIVE.phase = "science_completed"


def main():
    global ACTIVE
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    report = {
        "schema": "four-curvature-atom-cap5-first-search-v1",
        "paper_reference": "R498", "outcome": "entry_not_completed",
        "old_cap15_account_reopened": False,
        "old_three_atom_36_start_account_reopened": False,
        "original_full_mechanism_resolved": False,
        "smooth_profile_constructed": False,
        "all_scientific_outputs_are_new_four_segment_formula_observations": True,
    }
    out = pathlib.Path(args.out)
    hard = float(EXPECTED_BUDGET["entry_seconds"])
    try:
        request_bytes = pathlib.Path(args.request).read_bytes()
        request = json.loads(request_bytes)
        ACTIVE = Account(request)
        topic = pathlib.Path(__file__).resolve().parent.parent
        report["request_identity"] = {
            "bytes": len(request_bytes), "sha256": hashlib.sha256(request_bytes).hexdigest()
        }
        report["actual_bound_sources"] = _validate_request(request, topic)
        report["workflow_source_sha"] = os.environ.get("CAP4_SOURCE_SHA")
        ACTIVE.record("entry_inputs_bound", {
            "request": report["request_identity"], "sources": report["actual_bound_sources"],
            "budget": request["budget"], "search": request["search"],
            "certificate": request["certificate"],
            "scientific_scope": request["scientific_scope"],
            "previous_three_atom_cap15_and_other_research_are_closed_and_not_read": True,
        })
        ACTIVE.check()
        science(request, report)
    except BaseException as exc:
        report["failure"] = {
            "exception_type": type(exc).__name__, "message": str(exc),
            "phase": None if ACTIVE is None else ACTIVE.phase,
            "entry_elapsed_seconds": elapsed(), "traceback": traceback.format_exc(),
        }
        if ACTIVE is not None:
            ACTIVE.stop_reason = str(exc)
            report["outcome"] = (
                "new_account_finite_stop" if isinstance(exc, StopAccount)
                else "new_entry_or_science_failure"
            )
        else:
            report["outcome"] = "new_entry_failure_before_account"
    finally:
        if ACTIVE is not None:
            report["costs_before_final_output"] = ACTIVE.costs()
            report["best_complete_observation"] = ACTIVE.best
            report["optimization_starts"] = ACTIVE.starts
            report["last_certificate_progress"] = ACTIVE.certificate
            report["stop_reason"] = ACTIVE.stop_reason
        else:
            report["costs_before_final_output"] = {
                "entry_elapsed_before_final_output_seconds": elapsed(),
                "oracle_started": 0, "oracle_completed": 0, "oracle_failed": 0,
                "science_started": False,
            }
        report["scope"] = {
            "complete_original_five_targets": True,
            "new_separated_four_atom_plus_nonnegative_offset_family": True,
            "physical_dimension": 7, "original_G_dimension": 5,
            "floating_small_residual_is_not_a_zero_proof": True,
            "no_candidate_does_not_prove_cap_nonexistence": True,
            "C_zero_smoothing_requires_a_certified_shape_only_minor": True,
            "all_true_smoothing_consequences_require_R498_and_a_certified_regular_slice_root": True,
            "old_research_recomputed": False,
        }
        text = canonical(report)
        try:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text+"\n", encoding="utf-8")
        except BaseException as output_error:
            report["temporary_output_error"] = {
                "type": type(output_error).__name__, "message": str(output_error)}
            text = canonical(report)
        sys.stdout.write(FINAL_PREFIX+" "+text+"\n")
        sys.stdout.flush()
        final_elapsed = elapsed()
        scope_exhausted = final_elapsed >= hard
        clock = {
            "entry_elapsed_seconds": final_elapsed, "limit_seconds": hard,
            "overrun_seconds": max(0.0, final_elapsed-hard),
            "entry_scope_exhausted": scope_exhausted,
            "final_execution_status": (
                "scope_exhausted_including_final_output" if scope_exhausted
                else "entry_completed_within_scientific_clock"),
            "sampled_after_final_report_and_file_output": True,
            "supersedes_all_pre_output_elapsed_fields": True,
            "no_further_science_after_this_record": True,
            "science_started": False if ACTIVE is None else ACTIVE.science_started,
            "oracle_started": 0 if ACTIVE is None else ACTIVE.started,
            "oracle_completed": 0 if ACTIVE is None else ACTIVE.completed,
            "oracle_failed": 0 if ACTIVE is None else ACTIVE.failed,
            "stdout_soft_limit_reached": False if ACTIVE is None else ACTIVE.output_limit_reached,
        }
        sys.stdout.write(CLOCK_PREFIX+" "+canonical(clock)+"\n")
        sys.stdout.flush()
    return 2 if report["outcome"] in (
        "new_entry_or_science_failure", "new_entry_failure_before_account"
    ) else 0


if __name__ == "__main__":
    sys.exit(main())
