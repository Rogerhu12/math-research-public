#!/usr/bin/env python3
"""R599: exact factory parameter words and actual coast-recipe path.

This is a source library, not a new solver, domain gate, sampler or launcher.
The first function interprets the exact scalars already returned by the
original72c factory at the existing ten-word equality boundary. It does not
replace the binary64 H, state, RHS, Jacobian, native or checkpoint word paths.
The second function selects the actual launch receipt's already-produced
coast-base recipe. The caller must then execute its original complete read()
and bytes/SHA check. No file is created, copied, guessed or relabelled.

All input interpretation used by a scientific caller runs only in the named
public Actions. This authored source has not been executed or tested locally.
"""
from fractions import Fraction
import os
from pathlib import Path
import re
import struct

SCHEMA = "R599-actual-accurate-ten-word-and-coast-recipe-boundaries-v1"
REPOSITORY = "Rogerhu12/math-research-public"
FACTORY_SOURCE = (
    "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py",
    "72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682",
)
PROFILE_SOURCE = (
    "geometry_20261115_continuous_ten_same_metric_profile.py",
    "3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6",
)
PARAMETER_ORDER = (
    "p1", "p2", "p3", "theta1", "theta2", "theta3",
    "eta1", "eta2", "eta3", "xi",
)
COAST_RECIPE_RELATIVE_PATH = (
    "actual202-ten-BVP-input/actual202-coast-base-ten-full453-frozen450-recipe.json"
)


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY
            or not os.environ.get("GITHUB_RUN_ID")
            or not os.environ.get("GITHUB_SHA")):
        raise RuntimeError("Use the actual named public Actions run and source")


def _round_nonnegative_ratio_even(numerator, denominator):
    """Nearest integer; an exact halfway case chooses the even integer."""
    quotient, remainder = divmod(numerator, denominator)
    twice = remainder << 1
    return quotient + int(
        twice > denominator or (twice == denominator and (quotient & 1))
    )


def _finite_rational_word(value, negative_zero=False):
    """One exact rational to finite binary64 RN-even, as eight little-endian bytes.

    No float numerator, denominator, quotient, logarithm or second rounding
    occurs. An overflowing result is an explicit error, never an infinity.
    A negative nonzero input that underflows to zero retains its sign.
    """
    numerator, denominator = value.numerator, value.denominator
    sign = int(numerator < 0 or (numerator == 0 and negative_zero))
    numerator = abs(numerator)
    _require(denominator > 0, "The exact rational denominator must be positive")
    if numerator == 0:
        return (sign << 63).to_bytes(8, "little")

    # The bit-length difference is either floor(log2(n/d)) or one above it.
    exponent = numerator.bit_length() - denominator.bit_length()
    if exponent >= 0:
        if numerator < (denominator << exponent):
            exponent -= 1
    elif (numerator << (-exponent)) < denominator:
        exponent -= 1

    if exponent < -1022:
        # All subnormals and the subnormal/normal tie use the same 2^-1074 unit.
        significand = _round_nonnegative_ratio_even(numerator << 1074, denominator)
        _require(0 <= significand <= (1 << 52),
            "The exact subnormal rounding invariant failed")
        if significand == (1 << 52):
            word = (sign << 63) | (1 << 52)  # The least positive normal magnitude.
        else:
            word = (sign << 63) | significand
        return word.to_bytes(8, "little")

    if exponent > 1023:
        raise OverflowError("The exact factory scalar rounds outside finite binary64")
    shift = 52 - exponent
    if shift >= 0:
        significand = _round_nonnegative_ratio_even(numerator << shift, denominator)
    else:
        significand = _round_nonnegative_ratio_even(numerator, denominator << (-shift))
    if significand == (1 << 53):
        significand = 1 << 52
        exponent += 1
    if exponent > 1023:
        raise OverflowError("The exact factory scalar rounds outside finite binary64")
    _require((1 << 52) <= significand < (1 << 53),
        "The exact normal rounding invariant failed")
    word = ((sign << 63) | ((exponent + 1023) << 52)
        | (significand - (1 << 52)))
    return word.to_bytes(8, "little")


def _factory_scalar_word(value):
    """The original factory's rational types, with explicit zero-word semantics."""
    if isinstance(value, bool):
        raise ValueError("A boolean is not an accurate parameter scalar")
    if type(value) is float:
        # This is already an original binary64 value: preserve every bit,
        # including -0. Do not pass this path through Fraction or a decimal.
        raw = struct.pack("<d", value)
        word = int.from_bytes(raw, "little")
        if ((word >> 52) & 0x7ff) == 0x7ff:
            raise ValueError("A nonfinite original float is not a parameter")
        return raw
    if type(value) is int:
        return _finite_rational_word(Fraction(value))
    if isinstance(value, Fraction):
        # A Fraction has no signed zero. Its zero therefore has the +0 word.
        return _finite_rational_word(value)
    if type(value) is str:
        # Match the72c producer's Fraction grammar. The complete original
        # string remains in its bound report; it is not rewritten in place.
        # Fraction rejects malformed text, zero denominator, NaN and infinity.
        exact = Fraction(value)
        negative_zero = exact == 0 and value.strip().startswith("-")
        return _finite_rational_word(exact, negative_zero=negative_zero)
    raise TypeError("Use a factory exact-rational string, int, Fraction or finite float")


def factory_parameter_words(values):
    """Return all ten exact-report parameter words for the existing equality guard.

    The caller must first bind its actual72c result, definition and source
    through the original CurrentTenProfile. This function does not certify
    that provenance, choose parameters, overwrite the recipe or accept a BVP.
    """
    _actions()
    _require(isinstance(values, (list, tuple)) and len(values) == len(PARAMETER_ORDER),
        "Retain the complete ordered ten factory starting parameters")
    output = []
    for index, (name, value) in enumerate(zip(PARAMETER_ORDER, values)):
        try:
            output.append(_factory_scalar_word(value))
        except (ArithmeticError, TypeError, ValueError) as exc:
            raise ValueError(
                "Factory starting parameter " + str(index) + " (" + name
                + ") has no declared finite binary64 word: " + str(exc)
            ) from exc
    return b"".join(output)


def actual_coast_recipe_path(base, descriptor):
    """Resolve the genuine launcher recipe receipt; the original read must follow.

    The original launcher emits an absolute file path. Only its exact current
    coast-base recipe beneath this namespace is permitted. The caller still
    checks every actual byte against descriptor.bytes/sha256 with its original
    read(). This function has no fallback to the obsolete accurate-ten name.
    """
    _actions()
    _require(isinstance(descriptor, dict)
        and isinstance(descriptor.get("file"), str)
        and type(descriptor.get("bytes")) is int and descriptor["bytes"] >= 0
        and isinstance(descriptor.get("sha256"), str)
        and re.fullmatch(r"[0-9a-f]{64}", descriptor["sha256"]) is not None,
        "Use the complete actual launch recipe file/bytes/SHA receipt")
    root = Path(base).resolve(strict=True)
    _require(root.is_dir(), "The original namespace must be an actual directory")
    recorded = Path(descriptor["file"])
    _require(recorded.is_absolute() and ".." not in recorded.parts,
        "The actual launcher recipe receipt must be an absolute confined path")
    expected = root / COAST_RECIPE_RELATIVE_PATH
    _require(not recorded.is_symlink() and not expected.is_symlink(),
        "The actual coast recipe must be an ordinary file")
    path = recorded.resolve(strict=True)
    expected_resolved = expected.resolve(strict=True)
    _require(path == expected_resolved and expected_resolved == expected
        and path != root and path.is_relative_to(root)
        and path.is_file(),
        "The actual launch receipt does not name this namespace's coast-base recipe")
    return path
