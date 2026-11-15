#!/usr/bin/env python3
"""Positive rational endpoint operations for the unchanged R380 real family.

A proved intersection is stored as two exact rational endpoints. Its Arb
display may widen across zero and is never reused as a denominator or a
positive argument. Logarithms and square roots are evaluated at the separate
positive endpoints. A reciprocal enclosure is used only as a multiplier.
This is a representation repair, not a new positivity assumption, root
selection, precision change, or BVP acceptance condition.
Scientific arithmetic is restricted to the named public Actions repository.
Author: exact_refinement agent (AI), 2026-11-15.
"""
from __future__ import annotations
from fractions import Fraction as Q
import os

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R380-exact-positive-endpoints-monotone-operations-v1"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Positive endpoint arithmetic only in the named public Actions repository")


def dyadic_q(record):
    m, e = int(record["mantissa"]), record["binary_exponent"]
    if type(e) is not int:
        raise ValueError("Use the producer's exact dyadic endpoint")
    return Q(m)*(Q(1 << e) if e >= 0 else Q(1, 1 << (-e)))


def lower(B, value):
    if not value.is_finite():
        raise ArithmeticError("Nonfinite positive-endpoint operand")
    return dyadic_q(B.dyadic(value.lower()))


def upper(B, value):
    if not value.is_finite():
        raise ArithmeticError("Nonfinite positive-endpoint operand")
    return dyadic_q(B.dyadic(value.upper()))


def bounds(lo, hi, label):
    require_actions()
    lo, hi = Q(lo), Q(hi)
    if not Q(0) < lo <= hi:
        raise ArithmeticError("The exact proved positive intersection is absent: "+label)
    return dict(lower=lo, upper=hi, label=label)


def record(value):
    return dict(schema=SCHEMA, quantity=value["label"],
        lower_exact_rational=str(value["lower"]),
        upper_exact_rational=str(value["upper"]),
        exact_lower_strictly_positive=True,
        midpoint_radius_display_is_not_the_positivity_proof=True)


def intersect(B, value, proved_lower, proved_upper, label):
    """Intersect computed endpoints with already proved bounds, before union."""
    require_actions()
    proved_lower, proved_upper = Q(proved_lower), Q(proved_upper)
    if proved_lower > proved_upper:
        raise ArithmeticError("A proved exact range is reversed: "+label)
    return bounds(max(lower(B,value),proved_lower),
        min(upper(B,value),proved_upper),label)


def enclosure(B, value):
    result = B.interval(value["lower"],value["upper"])
    if not result.is_finite():
        raise ArithmeticError("Nonfinite display of exact positive endpoints")
    return result


def singleton(B, value, label):
    """The outward ball of one positive rational, not of a wide interval."""
    value = Q(value)
    if value <= 0:
        raise ArithmeticError("Nonpositive exact endpoint: "+label)
    result = B.exact(value)
    if not result.is_finite() or not result > 0:
        raise ArithmeticError("A single positive endpoint was not represented positively: "+label)
    return result


def logarithm(B, value):
    require_actions()
    lo = singleton(B,value["lower"],value["label"]+" lower").log()
    hi = singleton(B,value["upper"],value["label"]+" upper").log()
    left, right = lower(B,lo), upper(B,hi)
    if left > right:
        raise ArithmeticError("Endpoint logarithm enclosures lost order")
    result = B.interval(left,right)
    if not result.is_finite():
        raise ArithmeticError("Nonfinite endpoint logarithm enclosure")
    return result,dict(operation="monotone-log-of-separate-positive-endpoints",
        input=record(value),lower_endpoint_evaluation=B.record(lo),
        upper_endpoint_evaluation=B.record(hi),output=B.record(result),
        wide_positive_input_ball_not_formed_for_log=True)


def square_root(B, value):
    require_actions()
    lo = singleton(B,value["lower"],value["label"]+" lower").sqrt()
    hi = singleton(B,value["upper"],value["label"]+" upper").sqrt()
    # For x>0, min(1,x)<=sqrt(x)<=max(1,x). These exact
    # monotone bounds retain positivity even if an outward endpoint is broad.
    left = max(lower(B,lo),min(Q(1),value["lower"]))
    right = min(upper(B,hi),max(Q(1),value["upper"]))
    output = bounds(left,right,"sqrt("+value["label"]+")")
    display = enclosure(B,output)
    return output,display,dict(operation="monotone-sqrt-of-separate-positive-endpoints",
        input=record(value),lower_endpoint_evaluation=B.record(lo),
        upper_endpoint_evaluation=B.record(hi),positive_output=record(output),
        output_display=B.record(display),
        display_not_reused_as_positive_argument_or_denominator=True)


def reciprocal(B, value):
    require_actions()
    output = bounds(Q(1)/value["upper"],Q(1)/value["lower"],
        "reciprocal("+value["label"]+")")
    result = enclosure(B,output)
    return result,dict(operation="exact-positive-endpoint-reciprocal",
        input=record(value),positive_output=record(output),
        output_multiplier=B.record(result),
        output_is_only_a_multiplier_never_a_denominator=True,
        possible_display_zero_does_not_negate_exact_endpoint_positivity=True)


def quotient(B, numerator, denominator):
    multiplier, receipt = reciprocal(B,denominator)
    result = numerator*multiplier
    if not result.is_finite():
        raise ArithmeticError("Nonfinite multiplication by positive endpoint reciprocal")
    return result,dict(operation="numerator-times-positive-endpoint-reciprocal",
        numerator=B.record(numerator),reciprocal=receipt,output=B.record(result))


def inverse_square_root(B, value):
    root, display, root_receipt = square_root(B,value)
    multiplier, inverse_receipt = reciprocal(B,root)
    return multiplier,dict(operation="inverse-sqrt-via-positive-endpoints",
        square_root=root_receipt,reciprocal=inverse_receipt,
        root_display_not_reused_as_denominator=True,
        output_multiplier=B.record(multiplier))
