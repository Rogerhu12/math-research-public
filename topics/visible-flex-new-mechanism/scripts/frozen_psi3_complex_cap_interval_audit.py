#!/usr/bin/env python3
"""One new, rigorously enclosed frozen-psi3 complex cap observation.

This module is an Actions entry point, not a reusable old-science runner.
No old response, rank, profile construction, or development check is run.
Every mathematical bound uses exact integers with a common dyadic scale.
"""
import time as _time
_PROCESS_STARTED = _time.monotonic()

import argparse
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
import hashlib
import heapq
import json
import math
import os
from pathlib import Path
import sys

POLICY = "visible-flex-frozen-psi3-complex-cap-interval-v1"
PREFIX = "FROZEN_PSI3_COMPLEX_CAP_RECORD"
BITS = 256
SCALE = 1 << BITS
ORDER = 6
ROOT_STEPS = 160
EXP_TERMS = 48
EXP_SQUARINGS = 9
MAX_LEAVES = 1024
MAX_DEPTH = 20
MAX_JET_EVALUATIONS = 4096
MAX_SECONDS = 240
OUTPUT_RESERVE_SECONDS = 10
MAX_STDOUT_BYTES = 900000
MAX_REQUEST_BYTES = 100000
PAID_FOUR_SELF_SECONDS = "15.69076311099991"
R471_BLOB = "3632fcd81244cbc2efa03fd984770e63cd726b8e"
R455_BLOB = "ee1e04f8f93a2930c6de78191c3c4d91be2b2249"
CUT = Fraction(-19, 20)
ROOT_LO = Fraction(11, 20)
ROOT_HI = Fraction(3, 5)

_LEDGER = None


class ObservationFailure(RuntimeError):
    pass


class FiniteLimit(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise ObservationFailure(message)


def ceil_div(a, b):
    require(b != 0, "exact division by zero")
    return -((-a) // b)


def canonical_bytes(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False
    ).encode("utf-8") + b"\n"


class Ledger:
    def __init__(self):
        self.started = _PROCESS_STARTED
        self.counts = {
            "request_reads": 0,
            "new_complex_cap_observations": 0,
            "old_four_self_records_recomputed": 0,
            "old_response_or_rank_calls": 0,
            "development_checks": 0,
            "root_bisections": 0,
            "sqrt_interval_calls": 0,
            "exp_endpoint_bounds": 0,
            "integrand_jet_evaluations": 0,
            "failed_integrand_jet_evaluations": 0,
            "panel_enclosures_completed": 0,
            "splits_completed": 0,
            "maximum_leaf_count": 0,
            "failures": 0,
            "stdout_records": 0,
            "stdout_bytes": 0,
        }
        self.failure_records = []
        self.sequence = 0

    def elapsed(self):
        return _time.monotonic() - self.started

    def check(self):
        if self.elapsed() >= MAX_SECONDS - OUTPUT_RESERVE_SECONDS:
            raise FiniteLimit("single new entry clock reached its output reserve")

    def charge(self, name, amount=1):
        self.check()
        self.counts[name] = self.counts.get(name, 0) + amount
        if name == "integrand_jet_evaluations":
            require(self.counts[name] <= MAX_JET_EVALUATIONS,
                    "new jet-evaluation hard limit exceeded")

    def failure(self, stage, exc):
        self.counts["failures"] += 1
        self.failure_records.append({
            "stage": stage, "exception": type(exc).__name__,
            "message": str(exc), "elapsed_seconds": self.elapsed(),
        })

    def report(self):
        return {
            "policy": POLICY,
            "new_entry_elapsed_seconds": self.elapsed(),
            "limits": {
                "seconds_including_input_and_output": MAX_SECONDS,
                "computation_output_reserve_seconds": OUTPUT_RESERVE_SECONDS,
                "precision_bits": BITS,
                "quadrature_order": ORDER,
                "root_bisections": ROOT_STEPS,
                "exp_alternating_terms": EXP_TERMS,
                "exp_squarings": EXP_SQUARINGS,
                "leaf_panels": MAX_LEAVES,
                "dyadic_panel_depth": MAX_DEPTH,
                "integrand_jet_evaluations": MAX_JET_EVALUATIONS,
                "stdout_bytes": MAX_STDOUT_BYTES,
            },
            "counts": dict(self.counts),
            "failure_records": list(self.failure_records),
            "paid_four_self_seconds": PAID_FOUR_SELF_SECONDS,
            "paid_four_self_recomputed": False,
            "all_old_scientific_calls": 0,
        }

    def emit(self, kind, payload):
        body = canonical_bytes(payload)
        envelope = {
            "sequence": self.sequence, "kind": kind,
            "payload_bytes_including_lf": len(body),
            "payload_sha256_including_lf": hashlib.sha256(body).hexdigest(),
            "payload": payload,
        }
        line = PREFIX.encode("ascii") + b" " + canonical_bytes(envelope)
        require(self.counts["stdout_bytes"] + len(line) <= MAX_STDOUT_BYTES,
                "complete scientific stdout would exceed the fixed byte limit")
        sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()
        self.sequence += 1
        self.counts["stdout_records"] += 1
        self.counts["stdout_bytes"] += len(line)


def tick():
    if _LEDGER is not None:
        _LEDGER.check()


class I:
    """Closed interval [lo/SCALE, hi/SCALE], exact integer endpoints."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi):
        require(isinstance(lo, int) and isinstance(hi, int), "noninteger interval")
        require(lo <= hi, "reversed interval")
        self.lo, self.hi = lo, hi

    @staticmethod
    def integer(n):
        require(isinstance(n, int), "integer constant required")
        return I(n * SCALE, n * SCALE)

    @staticmethod
    def rational(value):
        v = value if isinstance(value, Fraction) else Fraction(value)
        a = v.numerator * SCALE
        return I(a // v.denominator, ceil_div(a, v.denominator))

    def __add__(self, other):
        return I(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return I(min(products) // SCALE, ceil_div(max(products), SCALE))

    def inv(self):
        require(not (self.lo <= 0 <= self.hi), "interval reciprocal contains zero")
        return I((SCALE * SCALE) // self.hi,
                 ceil_div(SCALE * SCALE, self.lo))

    def __truediv__(self, other):
        return self * other.inv()

    def power(self, n):
        require(isinstance(n, int), "integer power required")
        if n < 0:
            return self.inv().power(-n)
        result = I.integer(1)
        base = self
        while n:
            if n & 1:
                result = result * base
            n >>= 1
            if n:
                base = base * base
        return result

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def compact_record(self):
        return [str(self.lo), str(self.hi)]

    def record(self):
        with localcontext() as ctx:
            ctx.prec = 50
            ctx.rounding = ROUND_FLOOR
            lower = str(Decimal(self.lo) / Decimal(SCALE))
        with localcontext() as ctx:
            ctx.prec = 50
            ctx.rounding = ROUND_CEILING
            upper = str(Decimal(self.hi) / Decimal(SCALE))
        return {
            "lo_numerator": str(self.lo), "hi_numerator": str(self.hi),
            "denominator": "2^" + str(BITS),
            "outward_decimal_lower": lower,
            "outward_decimal_upper": upper,
        }


ZERO = I.integer(0)
ONE = I.integer(1)


def sqrt_interval(a):
    _LEDGER.charge("sqrt_interval_calls")
    require(a.lo >= 0, "sqrt interval has negative lower bound")
    lo = math.isqrt(a.lo * SCALE)
    hsq = a.hi * SCALE
    hi = math.isqrt(hsq)
    if hi * hi != hsq:
        hi += 1
    return I(lo, hi)


def exp_negative_endpoint(numerator):
    """Bound exp(numerator/SCALE), numerator <= 0, without binary64 math."""
    _LEDGER.charge("exp_endpoint_bounds")
    require(numerator <= 0, "positive exponent outside this observation")
    require(-numerator <= 256 * SCALE, "exponent outside fixed reduction range")
    v = I((-numerator) // (1 << EXP_SQUARINGS),
          ceil_div(-numerator, 1 << EXP_SQUARINGS))
    # v encloses the exact nonnegative (-numerator/SCALE)/512.
    require(v.lo >= 0 and v.hi <= SCALE // 2,
            "alternating exponential reduction not in [0,1/2]")
    term, total = ONE, ONE
    odd_lower = None
    even_upper = None
    for k in range(1, EXP_TERMS + 1):
        if not (k % 8):
            tick()
        term = (term * v) / I.integer(k)
        total = total - term if k & 1 else total + term
        if k == EXP_TERMS - 1:
            odd_lower = total.lo
        if k == EXP_TERMS:
            even_upper = total.hi
    require(odd_lower is not None and even_upper is not None,
            "exponential alternating endpoints missing")
    result = I(max(0, odd_lower), min(SCALE, even_upper))
    for _ in range(EXP_SQUARINGS):
        result = result * result
    return result


def exp_negative_interval(a):
    require(a.hi <= 0, "positive interval exponent not allowed")
    lo = exp_negative_endpoint(a.lo)
    hi = exp_negative_endpoint(a.hi)
    return I(lo.lo, hi.hi)


class J:
    """Real interval Taylor jet, coefficient j = derivative(j)/j!."""
    __slots__ = ("c", "n")

    def __init__(self, coefficients):
        self.c = tuple(coefficients)
        self.n = len(self.c) - 1
        require(self.n >= 0, "empty jet")

    @staticmethod
    def constant(value, n=ORDER):
        v = value if isinstance(value, I) else I.rational(value)
        return J([v] + [ZERO] * n)

    @staticmethod
    def variable(value, n=ORDER):
        require(n >= 1, "variable jet requires first derivative")
        return J([value, ONE] + [ZERO] * (n - 1))

    def __add__(self, other):
        require(self.n == other.n, "jet order mismatch")
        return J([a + b for a, b in zip(self.c, other.c)])

    def __neg__(self):
        return J([-a for a in self.c])

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        tick()
        require(self.n == other.n, "jet order mismatch")
        result = []
        for n in range(self.n + 1):
            s = ZERO
            for k in range(n + 1):
                s = s + self.c[k] * other.c[n - k]
            result.append(s)
        return J(result)

    def scale(self, value):
        v = value if isinstance(value, I) else I.rational(value)
        return J([a * v for a in self.c])

    def inv(self):
        tick()
        b = [self.c[0].inv()]
        for n in range(1, self.n + 1):
            s = ZERO
            for k in range(1, n + 1):
                s = s + self.c[k] * b[n - k]
            b.append(-(b[0] * s))
        return J(b)

    def power(self, exponent):
        require(isinstance(exponent, int), "jet integer power required")
        if exponent < 0:
            return self.inv().power(-exponent)
        result = J.constant(1, self.n)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            exponent >>= 1
            if exponent:
                base = base * base
        return result

    def exp_negative(self):
        tick()
        b = [exp_negative_interval(self.c[0])]
        for n in range(1, self.n + 1):
            s = ZERO
            for k in range(1, n + 1):
                s = s + (self.c[k] * b[n - k]) * I.integer(k)
            b.append(s / I.integer(n))
        return J(b)


class CJ:
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        require(re.n == im.n, "complex jet order mismatch")
        self.re, self.im = re, im

    def __add__(self, other):
        return CJ(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return CJ(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    def square(self):
        return CJ(self.re * self.re - self.im * self.im,
                  (self.re * self.im).scale(2))

    def times_real(self, other):
        return CJ(self.re * other, self.im * other)


def af_polynomial(t):
    return ((((27 * t + 102) * t - 46) * t - 10) * t - 1)


def isolate_root():
    lo, hi = ROOT_LO, ROOT_HI
    require(af_polynomial(lo) < 0 < af_polynomial(hi),
            "original unique-positive-root bracket failed")
    for _ in range(ROOT_STEPS):
        _LEDGER.charge("root_bisections")
        mid = (lo + hi) / 2
        value = af_polynomial(mid)
        if value == 0:
            lo = hi = mid
            break
        if value < 0:
            lo = mid
        else:
            hi = mid
    alpha = I(I.rational(lo).lo, I.rational(hi).hi)
    return alpha, {
        "polynomial_descending": [27, 102, -46, -10, -1],
        "original_bracket": ["11/20", "3/5"],
        "lower_fraction": [str(lo.numerator), str(lo.denominator)],
        "upper_fraction": [str(hi.numerator), str(hi.denominator)],
        "alpha_interval": alpha.record(),
        "unique_positive_root_reason": "one Descartes sign change; strict endpoint signs",
    }


def parameters_from_root(alpha):
    a = sqrt_interval(alpha)
    d = ONE - alpha
    pjet = alpha.power(2) * I.integer(3) + alpha * I.integer(4) - ONE
    require(d.lo > 0 and pjet.lo > 0, "endpoint rational denominator not positive")
    s = a * d.power(2) / pjet
    h = d.power(4) / (pjet * I.integer(6))
    delta2 = h * I.integer(2) - s.power(2)
    require(delta2.lo > 0, "endpoint variance not strictly positive")
    delta = sqrt_interval(delta2)
    zr = a + s
    zi = delta
    end = -a
    span = end - I.rational(CUT)
    require(span.lo > 0, "tail cutoff is not strictly left of the Af root")
    require(zr.abs_upper() + zi.abs_upper() <= 2 * SCALE,
            "coarse |z| <= 2 tail bound not certified")
    return {
        "alpha": alpha, "a": a, "d": d, "pjet": pjet,
        "s": s, "h": h, "delta2": delta2,
        "zr": zr, "zi": zi, "end": end, "span": span,
    }


def tail_enclosure(params):
    # For -1 < x <= -19/20, 0 < d <= 39/400.
    # |z|<=2, |x+z|<=3, |P|<=6, |B|<=19, |A|<=181.
    dc = Fraction(39, 400)
    require(dc < Fraction(15, 22), "tail monotonicity range not valid")
    prefactor = 1944 * 9 * 6 * (19 ** 2) * (181 ** 2)
    e = exp_negative_interval(I.rational(-Fraction(15, 1) / dc))
    bound = (I.rational(Fraction(prefactor, 20)) * e
             * I.rational(dc).power(-22))
    require(bound.lo >= 0, "negative absolute tail bound")
    return bound.hi, {
        "cutoff": "-19/20",
        "d_cutoff": "39/400",
        "coarse_abs_z_upper": 2,
        "absolute_integrand_prefactor": str(prefactor),
        "tail_length": "1/20",
        "monotonic_function": "exp(-15/d)*d^(-22), derivative sign 15-22d > 0",
        "absolute_tail_bound": I(0, bound.hi).record(),
        "applied_to_each_real_component": True,
        "left_flat_endpoint_not_discarded": True,
    }


def integrand_jet(y_interval, params):
    _LEDGER.charge("integrand_jet_evaluations")
    try:
        y = J.variable(y_interval)
        x = J.constant(CUT) + y.scale(params["span"])
        x2 = x * x
        x4 = x2 * x2
        d = J.constant(1) - x2
        require(d.c[0].lo > 0, "physical finite-panel denominator not positive")
        d2 = d * d
        d4 = d2 * d2
        pjet = x4.scale(3) + x2.scale(4) - J.constant(1)
        zeta = CJ(x + J.constant(params["zr"]), J.constant(params["zi"]))
        zeta2 = zeta.square()
        b = CJ(x * d2, J.constant(0)) + zeta.times_real(pjet)
        a = (CJ(d4, J.constant(0))
             + zeta.times_real((x * d2).scale(6))
             + zeta2.times_real(pjet.scale(3)))
        inverse_d = d.inv()
        exponential = inverse_d.scale(-15).exp_negative()
        real_factor = (
            exponential * x
            * (J.constant(1) - x2.scale(2))
            * (x4 + x2.scale(4) + J.constant(1))
            * inverse_d.power(22)
        ).scale(I.integer(1944) * params["span"])
        return (zeta2 * b.square() * a.square()).times_real(real_factor)
    except Exception:
        _LEDGER.counts["failed_integrand_jet_evaluations"] += 1
        raise


def panel_enclosure(depth, index, params):
    require(0 <= depth <= MAX_DEPTH, "dyadic depth outside fixed limit")
    require(0 <= index < (1 << depth), "invalid dyadic panel")
    denom = 1 << depth
    left = Fraction(index, denom)
    right = Fraction(index + 1, denom)
    centre = (left + right) / 2
    half = (right - left) / 2
    at_mid = integrand_jet(I.rational(centre), params)
    over_panel = integrand_jet(
        I(I.rational(left).lo, I.rational(right).hi), params
    )
    h = I.rational(half)
    result = []
    for mid, whole in ((at_mid.re, over_panel.re), (at_mid.im, over_panel.im)):
        val = ZERO
        for j in (0, 2, 4):
            factor = h.power(j + 1) * I.rational(Fraction(2, j + 1))
            val = val + mid.c[j] * factor
        rem_factor = h.power(7) * I.rational(Fraction(2, 7))
        val = val + whole.c[6] * rem_factor
        result.append(val)
    _LEDGER.counts["panel_enclosures_completed"] += 1
    re, im = result
    return {
        "depth": depth, "index": index, "re": re, "im": im,
        "score": max(re.hi - re.lo, im.hi - im.lo),
    }


def sum_panels(panels, tail):
    rl = sum(p["re"].lo for p in panels.values()) - tail
    rh = sum(p["re"].hi for p in panels.values()) + tail
    il = sum(p["im"].lo for p in panels.values()) - tail
    ih = sum(p["im"].hi for p in panels.values()) + tail
    return I(rl, rh), I(il, ih)


def separation(re, im):
    witnesses = []
    for name, value in (("real", re), ("imaginary", im)):
        if value.lo > 0:
            witnesses.append({"component": name, "strict_sign": "positive"})
        elif value.hi < 0:
            witnesses.append({"component": name, "strict_sign": "negative"})
    return witnesses


def integrate(params, tail, state):
    panels, heap = {}, []
    state["panels"] = panels
    # Eight initial panels. A partial initialization is not a full integral.
    for index in range(8):
        panel = panel_enclosure(3, index, params)
        key = (3, index)
        panels[key] = panel
        heapq.heappush(heap, (-panel["score"], 3, index))
    state["full_partition_available"] = True
    _LEDGER.counts["maximum_leaf_count"] = len(panels)
    reason = "finite-limit"
    while True:
        tick()
        re, im = sum_panels(panels, tail)
        state["last_re"], state["last_im"] = re, im
        witness = separation(re, im)
        if witness:
            reason = "certified-nonzero"
            break
        if len(panels) >= MAX_LEAVES:
            reason = "maximum-leaf-panels"
            break
        if _LEDGER.counts["integrand_jet_evaluations"] + 4 > MAX_JET_EVALUATIONS:
            reason = "maximum-new-jet-evaluations"
            break
        selected = None
        while heap:
            _, depth, index = heapq.heappop(heap)
            key = (depth, index)
            if key not in panels:
                continue
            if depth >= MAX_DEPTH:
                continue
            selected = (depth, index)
            break
        if selected is None:
            reason = "maximum-dyadic-depth"
            break
        depth, index = selected
        # Keep the old complete partition until both new enclosures exist.
        state["pending_children"] = []
        child0 = panel_enclosure(depth + 1, 2 * index, params)
        state["pending_children"].append(child0)
        child1 = panel_enclosure(depth + 1, 2 * index + 1, params)
        state["pending_children"].append(child1)
        del panels[selected]
        for child in (child0, child1):
            key = (child["depth"], child["index"])
            panels[key] = child
            heapq.heappush(heap, (-child["score"], *key))
        state["pending_children"] = []
        _LEDGER.counts["splits_completed"] += 1
        _LEDGER.counts["maximum_leaf_count"] = max(
            _LEDGER.counts["maximum_leaf_count"], len(panels)
        )
        if _LEDGER.counts["splits_completed"] % 32 == 0:
            re, im = sum_panels(panels, tail)
            _LEDGER.emit("PROGRESS", {
                "leaf_panels": len(panels),
                "splits": _LEDGER.counts["splits_completed"],
                "real_interval": re.record(),
                "imaginary_interval": im.record(),
                "elapsed_seconds": _LEDGER.elapsed(),
            })
    return reason


def validate_request(request, source_sha256):
    require(request.get("policy") == POLICY, "request policy mismatch")
    require(request.get("source_sha256") == source_sha256, "source SHA256 mismatch")
    require(request.get("paid_four_self_seconds") == PAID_FOUR_SELF_SECONDS,
            "closed four-self ancestor clock mismatch")
    require(request.get("r471_blob") == R471_BLOB, "complete E source mismatch")
    require(request.get("r455_blob") == R455_BLOB, "frozen-cap source mismatch")
    expected = {
        "precision_bits": BITS, "quadrature_order": ORDER,
        "root_bisections": ROOT_STEPS, "exp_terms": EXP_TERMS,
        "exp_squarings": EXP_SQUARINGS, "max_leaf_panels": MAX_LEAVES,
        "max_panel_depth": MAX_DEPTH,
        "max_integrand_jet_evaluations": MAX_JET_EVALUATIONS,
        "max_new_seconds": MAX_SECONDS,
        "output_reserve_seconds": OUTPUT_RESERVE_SECONDS,
        "max_stdout_bytes": MAX_STDOUT_BYTES,
        "initial_panel_depth": 3,
    }
    require(request.get("limits") == expected, "fixed observation limits differ")
    require(request.get("tail_cutoff") == "-19/20", "tail cutoff mismatch")
    require(request.get("root_bracket") == ["11/20", "3/5"],
            "algebraic root bracket mismatch")
    require(request.get("old_scientific_calls") == 0, "old calls not permitted")
    require(request.get("new_complex_targets") == 1, "only one new complex E allowed")
    return expected


def result_payload(state, status, reason):
    full = bool(state.get("full_partition_available"))
    panels = state.get("panels", {})
    re, im = state.get("last_re"), state.get("last_im")
    if full:
        re, im = sum_panels(panels, state["tail"])
    witness = separation(re, im) if full else []
    if witness and status != "failed":
        status = "certified-nonzero"
    leaf_rows = []
    for (depth, index), p in sorted(panels.items(),
            key=lambda item: Fraction(item[0][1], 1 << item[0][0])):
        leaf_rows.append({
            "depth": depth, "index": index,
            "real_scaled_integer_interval": p["re"].compact_record(),
            "imaginary_scaled_integer_interval": p["im"].compact_record(),
        })
    pending_rows = [{
        "depth": p["depth"], "index": p["index"],
        "real_scaled_integer_interval": p["re"].compact_record(),
        "imaginary_scaled_integer_interval": p["im"].compact_record(),
        "not_added_to_the_complete_partition": True,
    } for p in state.get("pending_children", [])]
    return {
        "policy": POLICY, "status": status, "stop_reason": reason,
        "target": "complete upper-root E for the frozen positive-affine psi3 cap",
        "source": state.get("source_identity"),
        "request_receipt": state.get("request_receipt"),
        "root": state.get("root_record"),
        "parameters": state.get("parameter_record"),
        "tail": state.get("tail_record"),
        "full_finite_interval_partition_available": full,
        "full_real_interval": re.record() if full else None,
        "full_imaginary_interval": im.record() if full else None,
        "strict_nonzero_witnesses": witness,
        "lower_root_value_is_complex_conjugate": True,
        "interval_scale_denominator": "2^" + str(BITS),
        "leaf_panel_certificate": leaf_rows,
        "uncommitted_completed_child_enclosures": pending_rows,
        "panel_rule": {
            "coordinate": "y in [0,1], x=-19/20+(T+19/20)*y",
            "point_terms": [0, 2, 4],
            "point_integral_factor": "2*half_width^(j+1)/(j+1)",
            "remainder": "whole-panel interval of f^(6)/6! times 2*half_width^7/7",
            "all_root_and_complex_parameter_dependence_enclosed": True,
            "no_point_sample_used_as_an_error_bound": True,
        },
        "scope": {
            "frozen_psi3_only": True,
            "positive_affine_and_positive_amplitude_nonzero_covariance":
                "a^5 H^(-2)",
            "universal_Af_cap_nonzero_claimed": False,
            "all_five_self_membership_conditions_solved": False,
            "old_four_self_records_or_ranks_rerun": False,
            "unresolved_is_not_zero": True,
        },
        "ledger_before_final_serialization": _LEDGER.report(),
    }


def main():
    global _LEDGER
    _LEDGER = Ledger()
    state = {"full_partition_available": False}
    status, reason, stage = "failed", "entry-not-completed", "input"
    output_file = None
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--request", required=True)
        parser.add_argument("--out", required=True,
                            help="directory below RUNNER_TEMP for the small result JSON")
        args = parser.parse_args()
        require(os.environ.get("GITHUB_ACTIONS") == "true",
                "this unique observation is authorized only in its public Actions entry")
        require("MR_TOKEN" not in os.environ, "private pull token must be removed first")
        source_bytes = Path(__file__).read_bytes()
        source_sha = hashlib.sha256(source_bytes).hexdigest()
        _LEDGER.charge("request_reads")
        request_bytes = Path(args.request).read_bytes()
        require(len(request_bytes) <= MAX_REQUEST_BYTES, "request exceeds source-only limit")
        request = json.loads(request_bytes.decode("utf-8"))
        limits = validate_request(request, source_sha)
        temp = Path(os.environ["RUNNER_TEMP"]).resolve()
        out = Path(args.out).resolve()
        require(out == temp or temp in out.parents, "temporary output outside RUNNER_TEMP")
        out.mkdir(parents=True, exist_ok=True)
        output_file = out / "frozen-psi3-complex-cap-interval-result.json"
        state["source_identity"] = {
            "source_sha256": source_sha, "source_bytes": len(source_bytes),
            "github_sha": os.environ.get("GITHUB_SHA"),
            "github_run_id": os.environ.get("GITHUB_RUN_ID"),
            "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
            "github_repository": os.environ.get("GITHUB_REPOSITORY"),
            "r471_blob": R471_BLOB, "r455_blob": R455_BLOB,
        }
        state["request_receipt"] = {
            "bytes": len(request_bytes),
            "sha256": hashlib.sha256(request_bytes).hexdigest(),
            "paid_four_self_receipt": request.get("paid_four_self_receipt"),
        }
        _LEDGER.emit("INPUT", {
            "source": state["source_identity"], "request": state["request_receipt"],
            "fixed_limits": limits, "old_scientific_calls": 0,
            "paid_four_self_seconds": PAID_FOUR_SELF_SECONDS,
        })
        _LEDGER.charge("new_complex_cap_observations")
        stage = "algebraic-root"
        alpha, root_record = isolate_root()
        state["root_record"] = root_record
        stage = "dependent-endpoint-parameters"
        params = parameters_from_root(alpha)
        state["parameter_record"] = {
            name: params[name].record()
            for name in ("a", "end", "s", "h", "delta2", "zr", "zi", "span")
        }
        _LEDGER.emit("ROOT", {
            "root": root_record, "parameters": state["parameter_record"],
        })
        stage = "true-flat-end-tail"
        tail, tail_record = tail_enclosure(params)
        state["tail"], state["tail_record"] = tail, tail_record
        stage = "single-adaptive-interval-integral"
        reason = integrate(params, tail, state)
        status = ("certified-nonzero" if reason == "certified-nonzero"
                  else "unresolved-at-finite-limits")
    except FiniteLimit as exc:
        _LEDGER.failure(stage, exc)
        status, reason = "unresolved-at-finite-limits", str(exc)
    except BaseException as exc:
        _LEDGER.failure(stage, exc)
        status, reason = "failed", str(exc)

    result = result_payload(state, status, reason)
    saved = None
    body = canonical_bytes(result)
    if output_file is not None:
        try:
            output_file.write_bytes(body)
            saved = {
                "temporary_path": str(output_file),
                "bytes_including_lf": len(body),
                "sha256_including_lf": hashlib.sha256(body).hexdigest(),
                "artifact_uploaded": False,
            }
        except Exception as exc:
            _LEDGER.failure("temporary-result-write", exc)
            result["status"] = "failed"
            result["stop_reason"] = "temporary result write failed"
            result["temporary_write_failure"] = {
                "exception": type(exc).__name__, "message": str(exc)
            }
    _LEDGER.emit("COMPLETE", {"result": result, "temporary_result": saved})
    # This clock is sampled after the complete mathematical output and its file.
    new_seconds = _LEDGER.elapsed()
    total = Decimal(PAID_FOUR_SELF_SECONDS) + Decimal(str(new_seconds))
    _LEDGER.emit("FINAL_CLOCK", {
        "policy": POLICY,
        "clock_sampled_after_COMPLETE_output": True,
        "paid_four_self_seconds": PAID_FOUR_SELF_SECONDS,
        "this_new_scientific_seconds": new_seconds,
        "total_paid_four_self_plus_new_seconds": str(total),
        "new_entry_budget_seconds": MAX_SECONDS,
        "within_new_total_budget_at_final_sample": new_seconds <= MAX_SECONDS,
        "counts": dict(_LEDGER.counts),
        "all_failures": list(_LEDGER.failure_records),
        "new_complex_targets": _LEDGER.counts["new_complex_cap_observations"],
        "old_scientific_calls": 0,
    })
    return 0 if result["status"] in (
        "certified-nonzero", "unresolved-at-finite-limits"
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
