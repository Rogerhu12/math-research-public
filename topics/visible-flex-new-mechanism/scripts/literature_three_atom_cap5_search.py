#!/usr/bin/env python3
"""New three-curvature-atom five-gate search; no old science is loaded.

The entire oracle is the twelve-term finite-power formula in R493.  All
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

PREFIX = "CAP3_RECORD"
FINAL_PREFIX = "CAP3_FINAL_REPORT"
CLOCK_PREFIX = "CAP3_FINAL_CLOCK"
NU = (1, 2, 3, 4, 6)
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
        self.g = tuple(zero for _ in range(5)) if gradient is None else tuple(gradient)

    def get(self, other):
        if isinstance(other, Jet):
            return other
        return Jet(other + self.v * 0)

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
            return Jet(self.v * 0 + 1)
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
    result = [Jet(a.v * 0) for _ in range(8)]
    for j, coefficient, ea, ec, et, degree in TERMS:
        co = cast(coefficient.numerator, coefficient.denominator)
        term = co * a**ea * c**ec * tau**et * (high**degree-low**degree)
        result[j] = result[j] + term
    return result


def generic_oracle(theta, cast):
    variables = []
    for i, x in enumerate(theta):
        zero = x * 0
        variables.append(Jet(x, tuple(zero + (1 if i == j else 0)
                                      for j in range(5))))
    a1, a2, b1, b2, cc = variables
    c2 = cc + cast(3, 5)*(1/a1-1/a2)*b1**5
    c3 = c2 + cast(3, 5)*(1/a2-1)*b2**5
    t2 = -cast(3, 2)-cast(3, 2)*(1/a2-1)*b2**2
    t1 = t2-cast(3, 2)*(1/a1-1/a2)*b1**2
    zero = Jet(theta[0] * 0)
    one = Jet(theta[0] * 0 + 1)
    accum = segment_generic(a1, cc, t1, zero, b1, cast)
    for second in (
        segment_generic(a2, c2, t2, b1, b2, cast),
        segment_generic(one, c3, Jet(-cast(3, 2)), b2, one, cast),
    ):
        accum = [x + y for x, y in zip(accum, second)]
    hh = cast(3, 5) + c3
    gs, ds, bs, rs = targets(hh, accum, cast)
    return {"H": hh, "A": accum, "G": gs, "Delta": ds, "B": bs, "R": rs}


def physical_valid(x):
    return (len(x) == 5 and 0 < x[0] < x[1] < 1
            and 0 < x[2] < x[3] < 1 and x[4] > 0)


def physical_box_valid(box):
    return (box[0].lo > 0 and box[0].hi < box[1].lo and box[1].hi < 1
            and box[2].lo > 0 and box[2].hi < box[3].lo
            and box[3].hi < 1 and box[4].lo > 0)


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
        common = self.co * np.power(a, self.ea) * np.power(c, self.ec) * np.power(tau, self.et)
        powers = np.power(high, self.nn) - np.power(low, self.nn)
        value = common * powers
        rows = (
            value,
            value * self.ea / a,
            value * self.ec / c,
            value * self.et / tau,
            -common*self.nn*np.power(low, self.nn-1),
            common*self.nn*np.power(high, self.nn-1),
        )
        return np.stack([np.bincount(self.index, weights=row, minlength=8)
                         for row in rows], axis=1)

    def physical(self, theta):
        a1, a2, b1, b2, cc = theta
        if not physical_valid(theta):
            raise ValueError("physical point is outside the genuine positive family")
        basis = np.eye(5)
        da1, da2, db1, db2, dc = basis
        c2 = cc + 3*(1/a1-1/a2)*b1**5/5
        dc2 = (dc + 3*b1**5*(-da1/a1**2+da2/a2**2)/5
               + 3*(1/a1-1/a2)*b1**4*db1)
        c3 = c2 + 3*(1/a2-1)*b2**5/5
        dc3 = dc2 - 3*b2**5*da2/(5*a2**2) + 3*(1/a2-1)*b2**4*db2
        t2 = -1.5 - 1.5*(1/a2-1)*b2**2
        dt2 = 1.5*b2**2*da2/a2**2 - 3*(1/a2-1)*b2*db2
        t1 = t2 - 1.5*(1/a1-1/a2)*b1**2
        dt1 = dt2 + 1.5*b1**2*(da1/a1**2-da2/a2**2) - 3*(1/a1-1/a2)*b1*db1
        zero = np.zeros(5)
        specifications = (
            ((a1, cc, t1, 0.0, b1), np.stack((da1, dc, dt1, zero, db1))),
            ((a2, c2, t2, b1, b2), np.stack((da2, dc2, dt2, db1, db2))),
            ((1.0, c3, -1.5, b2, 1.0), np.stack((zero, dc3, zero, db2, zero))),
        )
        av = np.zeros(8)
        aj = np.zeros((8, 5))
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            for values, chain in specifications:
                block = self.segment(*values)
                av += block[:, 0]
                aj += block[:, 1:] @ chain
            hh = 0.6 + c3
            jets = [Jet(float(av[i]), aj[i]) for i in range(8)]
            gj, dj, _, _ = targets(Jet(float(hh), dc3), jets, lambda n, d: n/d)
            gv = np.array([x.v for x in gj], dtype=float)
            jg = np.array([x.g for x in gj], dtype=float)
            dv = np.array([x.v for x in dj], dtype=float)
        if not all(np.all(np.isfinite(x)) for x in (av, aj, gv, jg, dv, dc3)):
            raise FloatingPointError("nonfinite complete finite-power value or Jacobian")
        return {"H": float(hh), "A": av, "DA": aj, "G": gv,
                "DG": jg, "Delta": dv, "DH": dc3}

    @staticmethod
    def chart(z):
        qs = 1.0/(1.0+np.exp(-z[:4]))
        q1, q2, q3, q4 = qs
        cc = math.exp(float(z[4]))
        theta = np.array((q1*q2, q2, q3*q4, q4, cc))
        chain = np.zeros((5, 5))
        chain[0, 0] = q2*q1*(1-q1)
        chain[0, 1] = q1*q2*(1-q2)
        chain[1, 1] = q2*(1-q2)
        chain[2, 2] = q4*q3*(1-q3)
        chain[2, 3] = q3*q4*(1-q4)
        chain[3, 3] = q4*(1-q4)
        chain[4, 4] = cc
        return theta, chain

    def evaluate(self, z):
        z = np.asarray(z, dtype=float)
        self.account.check(searching=True)
        if z.shape != (5,) or not np.all(np.isfinite(z)):
            raise ValueError("invalid search coordinate")
        key = tuple(float(value).hex() for value in z)
        if key in self.cache:
            self.account.cache_hits += 1
            return self.cache[key]
        theta, chain = self.chart(z)
        token = self.account.begin("float_value_and_analytic_J",
                                   {"start_index": self.current_start, "z": z.tolist()},
                                   searching=True)
        try:
            data = self.physical(theta)
            powers = np.array([n/2-4 for n in NU])
            scale = np.power(1+data["H"], powers)
            fv = scale*data["G"]
            jf_physical = (scale[:, None]*data["DG"]
                           + (powers*scale*data["G"]/(1+data["H"]))[:, None]
                           * data["DH"][None, :])
            jf = jf_physical @ chain
            if not np.all(np.isfinite(jf)) or not np.all(np.isfinite(fv)):
                raise FloatingPointError("nonfinite scaled complete residual or Jacobian")
            ginf = float(np.max(np.abs(data["G"])))
            fnorm = float(np.linalg.norm(fv))
            payload = {
                "start_index": self.current_start, "z": z.tolist(),
                "theta_a1_a2_b1_b2_C": theta.tolist(),
                "H": data["H"], "A0_through_A7": data["A"].tolist(),
                "Delta_1_2_3_4_6": data["Delta"].tolist(),
                "G_1_2_3_4_6": data["G"].tolist(),
                "DG_physical": data["DG"].tolist(),
                "DH_physical": data["DH"].tolist(),
                "F_scaled": fv.tolist(), "DF_chart": jf.tolist(),
                "unscaled_G_infinity": ginf, "scaled_F_euclidean": fnorm,
                "physical_legal": True,
            }
            receipt = self.account.finish(token, payload)
        except BaseException as exc:
            if self.account.active_call is token:
                self.account.fail(token, exc)
            raise
        data.update({"theta": theta, "z": z.copy(), "F": fv, "DF": jf,
                     "G_infinity": ginf, "F_norm": fnorm, "receipt": receipt})
        self.last_z = z.copy()
        self.last_data = data
        self.cache[key] = data
        if ginf < self.account.best_score:
            self.account.best_score = ginf
            self.account.best_scaled = fnorm
            self.account.best = payload | {"record": receipt}
        if ginf <= float(self.account.request["search"]["candidate_unscaled_G_infinity"]):
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


def generic_call(theta, mode, label, cast, summary):
    token = ACTIVE.begin(mode, label)
    try:
        result = generic_oracle(theta, cast)
        payload = summary(result)
        receipt = ACTIVE.finish(token, payload)
        ACTIVE.check()
        return result, receipt
    except BaseException as exc:
        if ACTIVE.active_call is token:
            ACTIVE.fail(token, exc)
        raise


def certify_first_candidate(candidate, request):
    ACTIVE.phase = "first_new_candidate_refinement_and_rational_certificate"
    settings = request["certificate"]
    with decimal.localcontext() as context:
        context.prec = int(settings["decimal_precision"])
        theta = [decimal.Decimal(repr(float(x))) for x in candidate["theta"]]
        data = None
        for iteration in range(int(settings["decimal_newton_calls"])):
            if not physical_valid(theta):
                raise ValueError("new Decimal Newton point left the genuine parameter domain")
            data, receipt = generic_call(
                theta, "decimal_complete_value_and_analytic_J",
                {"iteration": iteration, "theta": [str(x) for x in theta]},
                cast_decimal,
                lambda out: {
                    "theta": [str(x) for x in theta],
                    "H": str(out["H"].v),
                    "A0_through_A7": [str(x.v) for x in out["A"]],
                    "G_1_2_3_4_6": [str(x.v) for x in out["G"]],
                    "DG_physical": [[str(y) for y in x.g] for x in out["G"]],
                    "Delta_1_2_3_4_6": [str(x.v) for x in out["Delta"]],
                })
            values = [x.v for x in data["G"]]
            jacobian = [list(x.g) for x in data["G"]]
            if max(abs(x) for x in values) <= decimal.Decimal(settings["decimal_stop_G"]):
                break
            if iteration + 1 == int(settings["decimal_newton_calls"]):
                break
            direction = decimal_solve(jacobian, [-x for x in values])
            next_theta = [x+d for x, d in zip(theta, direction)]
            if not physical_valid(next_theta):
                raise ValueError("full new Decimal Newton correction leaves genuine domain")
            theta = next_theta
        if data is None:
            raise RuntimeError("no new Decimal candidate value")
        matrix = [list(x.g) for x in data["G"]]
        identity = [[decimal.Decimal(i == j) for j in range(5)] for i in range(5)]
        inverse = decimal_solve(matrix, identity)
        center = [nearest_dyadic(Fraction(x), int(settings["center_dyadic_bits"]))
                  for x in theta]
        bb = [[nearest_dyadic(Fraction(x), int(settings["inverse_dyadic_bits"]))
               for x in row] for row in inverse]
    if not physical_valid(center):
        raise ValueError("dyadic center is outside genuine parameter domain")
    exact, center_receipt = generic_call(
        center, "exact_rational_center_complete_value_and_J",
        {"center": [qtext(x) for x in center]}, Fraction,
        lambda out: {
            "center": [qtext(x) for x in center],
            "H_outward": itext(outward_dyadic(out["H"].v, 160)),
            "A0_through_A7_outward": [
                itext(outward_dyadic(x.v, 160)) for x in out["A"]],
            "G_outward": [itext(outward_dyadic(x.v, 160)) for x in out["G"]],
            "DG_outward": [
                [itext(outward_dyadic(y, 128)) for y in x.g] for x in out["G"]],
        })
    ff = [outward_dyadic(x.v, 160) for x in exact["G"]]
    best_failure = None
    for exponent in settings["box_radius_negative_binary_exponents"]:
        ACTIVE.check()
        radius = Fraction(1, 1 << int(exponent))
        box = [Interval(x-radius, x+radius) for x in center]
        if not physical_box_valid(box):
            ACTIVE.record("certificate_box_domain_rejected", {
                "negative_binary_exponent": exponent,
                "center_record": center_receipt,
                "reason": "whole rational box must lie in strict genuine domain",
            })
            continue
        interval_data, box_receipt = generic_call(
            box, "rational_interval_complete_value_and_analytic_J",
            {"negative_binary_exponent": exponent, "radius": qtext(radius)},
            lambda n, d=1: Interval(Fraction(n, d)),
            lambda out: {
                "negative_binary_exponent": exponent, "radius": qtext(radius),
                "H_outward": itext(outward_dyadic(out["H"].v, 128)),
                "A0_through_A7_outward": [
                    itext(outward_dyadic(x.v, 128)) for x in out["A"]],
                "G_outward": [itext(outward_dyadic(x.v, 128)) for x in out["G"]],
                "DG_outward": [
                    [itext(outward_dyadic(y, 128)) for y in x.g] for x in out["G"]],
            })
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
        q_upper = ceil_dyadic(q_bound, 160)
        eta_upper = ceil_dyadic(eta, 160)
        image_upper = eta_upper + q_upper*radius
        passed = q_upper < 1 and image_upper < radius
        certificate = {
            "passed": bool(passed),
            "target": "all five original G=Delta/R5, not only complex E",
            "center_record": center_receipt, "box_record": box_receipt,
            "center": [qtext(x) for x in center],
            "radius": qtext(radius),
            "B_rational": [[qtext(x) for x in row] for row in bb],
            "G_at_center_outward": [itext(x) for x in ff],
            "DG_box_outward": [[itext(x) for x in row] for row in jj],
            "contraction_q_upper": qtext(q_upper),
            "center_displacement_upper": qtext(eta_upper),
            "self_map_radius_upper": qtext(image_upper),
            "whole_box_strictly_legal": True,
            "unique_exact_boundary_root": bool(passed),
            "Jacobian_invertible_on_box": bool(passed),
            "smooth_cap_explicitly_constructed": False,
            "full_original_mechanism_resolved": False,
        }
        ACTIVE.record("rational_contraction_test", certificate)
        ACTIVE.certificate = certificate
        if passed:
            return certificate
        best_failure = certificate
    return {"passed": False, "reason": "finite new rational boxes did not certify",
            "last_test": best_failure}


def start_points():
    rows = []
    for qs in itertools.product((0.25, 0.75), repeat=4):
        for cc in (1/32, 1.0):
            rows.append([math.log(q/(1-q)) for q in qs] + [math.log(cc)])
    for cc in (1/128, 1/8, 1.0, 8.0):
        rows.append([0.0, 0.0, 0.0, 0.0, math.log(cc)])
    return rows


def validate_request(request, topic):
    if request["entry_point"] != "scripts/literature_three_atom_cap5_search.py":
        raise ValueError("wrong new entry point")
    if request["scientific_scope"] != "new_three_curvature_atoms_offset_complete_five_gates":
        raise ValueError("wrong new scientific scope")
    expected = {
        "entry_seconds": 120, "search_seconds": 105,
        "complete_oracle_calls": 5000, "stdout_soft_bytes": 33554432,
        "rational_integer_bits": 1000000,
    }
    if request["budget"] != expected:
        raise ValueError("budget must match the frozen one-account contract")
    if request["search"] != {
        "starts": 36, "per_start_max_nfev": 120,
        "candidate_unscaled_G_infinity": 1e-8,
        "first_four_z_bounds": [-4.0, 4.0], "last_z_bounds": [-8.0, 3.0],
        "residual_scaling": "(1+H)**(nu/2-4) * (Delta_nu/R5)",
        "ftol": 1e-12, "xtol": 1e-12, "gtol": 1e-10,
    }:
        raise ValueError("search coordinates or fixed starts contract changed")
    if request["certificate"] != {
        "decimal_precision": 80, "decimal_newton_calls": 8,
        "decimal_stop_G": "1e-55", "center_dyadic_bits": 160,
        "inverse_dyadic_bits": 128,
        "box_radius_negative_binary_exponents": [16, 24, 32, 40, 48, 56, 64, 72],
    }:
        raise ValueError("new candidate-only certificate contract changed")
    identities = {}
    for specification in request["source_manifest"]:
        path = topic / specification["path"]
        data = path.read_bytes()
        actual = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        if actual["bytes"] != specification["bytes"] or actual["sha256"] != specification["sha256"]:
            raise ValueError("bound new source bytes/hash changed: " + specification["path"])
        identities[specification["path"]] = actual
    if "scripts/literature_three_atom_cap5_search.py" not in identities:
        raise ValueError("entry source must itself be bound")
    for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                 "NUMEXPR_NUM_THREADS"):
        if os.environ.get(name) != "1":
            raise ValueError("single-thread environment missing: " + name)
    if sys.version.split()[0] != request["runtime"]["python"]:
        raise ValueError("pinned Python version changed")
    return identities


def science(request, report):
    global np, scipy, least_squares, TERMS
    ACTIVE.science_started = True
    ACTIVE.phase = "new_imports_and_finite_coefficient_preparation"
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
        "finite_terms": len(TERMS), "maximum_power": 21,
        "runtime": {"python": sys.version.split()[0], "numpy": np.__version__,
                    "scipy": scipy.__version__},
        "old_paid_log_reads": 0, "old_ODE_calls": 0, "new_quadrature_calls": 0,
        "old_rank_or_mapper_calls": 0, "development_checks": 0,
        "formula_scope": "complete twelve L terms, eight A_j, all five Delta",
    })
    ACTIVE.check()
    oracle = FloatOracle(ACTIVE)
    lower = np.array([-4., -4., -4., -4., -8.])
    upper = np.array([4., 4., 4., 4., 3.])
    candidate = None
    ACTIVE.phase = "new_fixed_36_start_finite_power_search"
    for index, initial in enumerate(start_points()):
        ACTIVE.check(searching=True)
        oracle.current_start = index
        started = _time.perf_counter()
        item = {"index": index, "initial_z": initial, "status": "started"}
        ACTIVE.starts.append(item)
        ACTIVE.record("optimization_start", item)
        try:
            result = least_squares(
                oracle.fun, np.array(initial), jac=oracle.jac,
                bounds=(lower, upper), method="trf", tr_solver="exact",
                x_scale="jac", max_nfev=request["search"]["per_start_max_nfev"],
                ftol=request["search"]["ftol"], xtol=request["search"]["xtol"],
                gtol=request["search"]["gtol"])
            item.update({
                "status": "returned", "scipy_status": int(result.status),
                "message": str(result.message), "nfev": int(result.nfev),
                "njev": None if result.njev is None else int(result.njev),
                "final_z": result.x.tolist(), "scaled_cost": float(result.cost),
                "floating_optimality": float(result.optimality),
                "seconds": _time.perf_counter()-started,
            })
            ACTIVE.record("optimization_return", item)
        except CandidateFound as found:
            candidate = found.data
            item.update({"status": "first_floating_candidate",
                         "record": candidate["receipt"],
                         "seconds": _time.perf_counter()-started})
            ACTIVE.record("optimization_candidate_stop", item)
            break
        except StopAccount:
            item.update({"status": "account_stop", "seconds": _time.perf_counter()-started})
            ACTIVE.record("optimization_account_stop", item)
            raise
        except Exception as exc:
            item.update({"status": "optimizer_failure", "exception_type": type(exc).__name__,
                         "message": str(exc), "seconds": _time.perf_counter()-started})
            ACTIVE.record("optimization_failure", item)
    if candidate is not None:
        report["floating_candidate_record"] = candidate["receipt"]
        report["candidate_physical_theta"] = candidate["theta"].tolist()
        try:
            certificate = certify_first_candidate(candidate, request)
            report["certificate"] = certificate
            report["outcome"] = (
                "certified_regular_three_atom_five_gate_boundary_root"
                if certificate.get("passed")
                else "floating_candidate_not_certified_by_finite_new_boxes"
            )
        except BaseException as exc:
            report["certificate_failure"] = {
                "exception_type": type(exc).__name__, "message": str(exc),
                "entry_elapsed_seconds": elapsed(),
            }
            report["outcome"] = "floating_candidate_certificate_failed_or_budget_stopped"
            if isinstance(exc, (KeyboardInterrupt, SystemExit)):
                raise
    else:
        report["outcome"] = "finite_new_model_search_no_five_gate_candidate"
    ACTIVE.phase = "science_completed"


def main():
    global ACTIVE
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    report = {
        "schema": "three-curvature-atom-cap5-first-search-v1",
        "paper_reference": "R493",
        "outcome": "entry_not_completed",
        "old_cap15_account_reopened": False,
        "original_full_mechanism_resolved": False,
        "smooth_profile_constructed": False,
        "all_outputs_are_new_finite_formula_observations": True,
    }
    out = pathlib.Path(args.out)
    hard = 120.0
    try:
        request_bytes = pathlib.Path(args.request).read_bytes()
        request = json.loads(request_bytes)
        ACTIVE = Account(request)
        hard = ACTIVE.hard
        topic = pathlib.Path(__file__).resolve().parent.parent
        report["request_identity"] = {
            "bytes": len(request_bytes), "sha256": hashlib.sha256(request_bytes).hexdigest()
        }
        report["actual_bound_sources"] = validate_request(request, topic)
        report["workflow_source_sha"] = os.environ.get("CAP3_SOURCE_SHA")
        ACTIVE.record("entry_inputs_bound", {
            "request": report["request_identity"],
            "sources": report["actual_bound_sources"],
            "budget": request["budget"], "scientific_scope": request["scientific_scope"],
            "previous_cap15_account_is_closed_and_not_read": True,
        })
        ACTIVE.check()
        science(request, report)
    except BaseException as exc:
        report["failure"] = {
            "exception_type": type(exc).__name__, "message": str(exc),
            "phase": None if ACTIVE is None else ACTIVE.phase,
            "entry_elapsed_seconds": elapsed(),
            "traceback": traceback.format_exc(),
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
            "finite_positive_three_atom_plus_offset_model": True,
            "floating_small_residual_is_not_a_zero_proof": True,
            "no_candidate_does_not_prove_cap_nonexistence": True,
            "all_true_smoothing_consequences_require_R493_and_a_certified_regular_root": True,
            "old_research_recomputed": False,
        }
        text = canonical(report)
        try:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text + "\n", encoding="utf-8")
        except BaseException as output_error:
            report["temporary_output_error"] = {
                "type": type(output_error).__name__, "message": str(output_error)
            }
            text = canonical(report)
        sys.stdout.write(FINAL_PREFIX + " " + text + "\n")
        sys.stdout.flush()
        final_elapsed = elapsed()
        clock = {
            "entry_elapsed_seconds": final_elapsed,
            "limit_seconds": hard,
            "overrun_seconds": max(0.0, final_elapsed-hard),
            "sampled_after_final_report_and_file_output": True,
            "supersedes_all_pre_output_elapsed_fields": True,
            "no_further_science_after_this_record": True,
            "science_started": False if ACTIVE is None else ACTIVE.science_started,
            "oracle_started": 0 if ACTIVE is None else ACTIVE.started,
            "oracle_completed": 0 if ACTIVE is None else ACTIVE.completed,
            "oracle_failed": 0 if ACTIVE is None else ACTIVE.failed,
        }
        sys.stdout.write(CLOCK_PREFIX + " " + canonical(clock) + "\n")
        sys.stdout.flush()
    return 2 if report["outcome"] in (
        "new_entry_or_science_failure", "new_entry_failure_before_account"
    ) else 0


if __name__ == "__main__":
    sys.exit(main())
