#!/usr/bin/env python3
"""Represent one unprinted original binary64 margin without fabricating it.

Executed only by the declared Actions science child, under its existing clock.
The source reported e=RN64(best_geo+float(.01)), and its paid fine margin is
a lower bound on best_geo.  Exact rational midpoints recover the possible
binary64 inputs of that addition.  Decisions use the original rounded
subtraction and strict comparison at both endpoints of this ordered set.
No model value, derivative, oracle, or prior scan is evaluated here.
"""
from fractions import Fraction
import math
import struct


def ratio(value):
    return Fraction.from_float(float(value))


def finite(value):
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("The recorded original margin must be finite.")
    return result


def lower_binary64(bound, inclusive):
    value = finite(float(bound))
    exact = ratio(value)
    if exact < bound or (exact == bound and not inclusive):
        value = math.nextafter(value, math.inf)
    return value


def upper_binary64(bound, inclusive):
    value = finite(float(bound))
    exact = ratio(value)
    if exact > bound or (exact == bound and not inclusive):
        value = math.nextafter(value, -math.inf)
    return value


def rational_receipt(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


class OriginalMarginState:
    """Exact interval of possible original binary64 best_geo values.

    The set consists of *all* binary64 values between lower and upper, not
    an interval estimate of a continuous geometric function.  An accepted
    new trial or a dominating paid new coarse value makes this state exact.
    """

    def __init__(self, lower, upper, origin):
        self.lower, self.upper = finite(lower), finite(upper)
        if self.lower > self.upper or self.lower < 0:
            raise ValueError("The possible original margin state is empty.")
        self.origin = dict(origin)

    @classmethod
    def exact(cls, value, reason="new_actual_complete_qualification"):
        value = finite(value)
        return cls(value, value, {"kind": "actual_exact_binary64", "reason": reason})

    @classmethod
    def from_recorded_addition(cls, recorded_extra, original_addend, paid_fine_lower):
        e, c, paid = map(finite, (recorded_extra, original_addend, paid_fine_lower))
        previous, following = math.nextafter(e, -math.inf), math.nextafter(e, math.inf)
        if not (0 < e and c > 0 and paid >= 0 and math.isfinite(following)):
            raise ValueError("Outside the positive finite original addition scope.")
        # Binary64 round-to-nearest/ties-to-even chooses e at a midpoint
        # exactly when e's stored significand least significant bit is even.
        even = struct.unpack("<Q", struct.pack("<d", e))[0] % 2 == 0
        left = (ratio(previous)+ratio(e))/2-ratio(c)
        right = (ratio(e)+ratio(following))/2-ratio(c)
        lo = max(paid, 0., lower_binary64(left, even))
        hi = upper_binary64(right, even)
        result = cls(lo, hi, {
            "kind": "inverse_of_one_recorded_original_RN64_addition",
            "recorded_extra": e, "original_binary64_addend": c,
            "paid_fine_lower_bound": paid,
            "exact_real_left": rational_receipt(left),
            "exact_real_right": rational_receipt(right),
            "both_real_midpoint_endpoints_included": even,
            "unprinted_original_scalar_not_replaced_by_e_minus_addend": True,
        })
        # These are arithmetic identity checks of this reconstruction,
        # not new scientific qualification or model evaluations.
        if lo+c != e or hi+c != e:
            raise ArithmeticError("Inverse-rounding endpoints do not recover recorded e.")
        return result

    def phase(self, tolerance):
        tolerance = finite(tolerance)
        if self.lower > tolerance:
            return "geometry_restoration"
        if self.upper <= tolerance:
            return "metric"
        return None

    def original_strict_improvement(self, geometry_peak, original_threshold=1e-10):
        peak, threshold = finite(geometry_peak), finite(original_threshold)
        # Subtraction is deliberately binary64, exactly as the paid driver:
        # geometry_peak < best_geo - 1e-10.  This is monotone in best_geo.
        at_lower = peak < self.lower-threshold
        at_upper = peak < self.upper-threshold
        if at_lower == at_upper:
            return bool(at_lower)
        return None

    def maximize_with_original_coarse(self, coarse_margin):
        value = finite(coarse_margin)
        self.lower, self.upper = max(self.lower, value), max(self.upper, value)
        self.origin = {"kind": "image_under_original_max_with_new_paid_coarse",
                       "new_coarse_margin": value, "previous_origin": self.origin}

    def original_added_extra(self, original_addend=.01):
        addend = finite(original_addend)
        lower_result, upper_result = self.lower+addend, self.upper+addend
        return lower_result if lower_result == upper_result else None

    def receipt(self):
        lowbits = struct.unpack("<Q", struct.pack("<d", self.lower))[0]
        highbits = struct.unpack("<Q", struct.pack("<d", self.upper))[0]
        return {"schema": "original_binary64_best_geo_possible_state_v1",
                "lower_binary64": self.lower, "upper_binary64": self.upper,
                "exact_single_original_value": self.lower == self.upper,
                "possible_nonnegative_binary64_values": highbits-lowbits+1,
                "origin": self.origin,
                "continuous_geometry_enclosure_claim": False,
                "old_coarse_or_fine_scientific_probe_replayed": False}
