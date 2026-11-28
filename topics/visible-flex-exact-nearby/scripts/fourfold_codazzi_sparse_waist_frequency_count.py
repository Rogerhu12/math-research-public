"""Exact address/count of ASQ9's retained subset without a Fourier vector.

No default calculation, scientific inputs, or floating trigonometry. Indices
are the single real reflected mode n (physical wave number 4*n).
"""

from fractions import Fraction
from math import isqrt


ROTATION_INTEGER = 5831714953207175
ROTATION_DENOMINATOR = 21212218271020390
FIRST_SHELL = 1125
LAST_SHELL = 4608


def rational_floor_sum(count, numerator, intercept, denominator):
    """Sum floor((numerator*i+intercept)/denominator), 0 <= i < count."""
    total = 0
    while True:
        whole_slope, numerator = divmod(numerator, denominator)
        whole_intercept, intercept = divmod(intercept, denominator)
        total += whole_slope * count * (count - 1) // 2
        total += whole_intercept * count
        ceiling_numerator = numerator * count + intercept
        if ceiling_numerator < denominator:
            return total
        count, intercept = divmod(ceiling_numerator, denominator)
        numerator, denominator = denominator, numerator


def shifted_rotation_floor_sum(start, stop, shift):
    """Sum floor(n*rho15+shift) over positive n in [start,stop)."""
    if not 1 <= start <= stop:
        raise ValueError("positive half-open mode interval required")
    if start == stop:
        return 0
    shift = Fraction(shift)
    d = ROTATION_DENOMINATOR
    b = shift.denominator
    scale_bits = (stop * b * b * (d + 5 * stop)).bit_length()
    scale = 1 << scale_bits
    root_lower = isqrt(5 << (2 * scale_bits))
    slope = (ROTATION_INTEGER * scale + root_lower) * b
    modulus = d * scale * b
    offset = start * slope + shift.numerator * d * scale
    return rational_floor_sum(stop - start, slope, offset, modulus)


def shell_radius(shell):
    if not FIRST_SHELL <= shell < LAST_SHELL:
        raise ValueError("outside the sparse interior shells")
    return (Fraction(8, 1 << shell)
            + Fraction(1, 1 << (shell + shell // 3 - 1486)))


def retained_count(start, stop):
    """Count the ASQ9 retained original q modes. Empty intervals count zero."""
    if not 1 <= start <= stop <= 1 << LAST_SHELL:
        raise ValueError("interval must lie within the original finite section")
    first = 1 << FIRST_SHELL
    retained = max(0, min(stop, first) - start)
    cursor = max(start, first)
    while cursor < stop:
        shell = cursor.bit_length() - 1
        end = min(stop, 1 << (shell + 1))
        radius = shell_radius(shell)
        lower = Fraction(1, 4) - radius
        upper = Fraction(1, 4) + radius
        retained += shifted_rotation_floor_sum(cursor, end, 1 - lower)
        retained -= shifted_rotation_floor_sum(cursor, end, 1 - upper)
        cursor = end
    return retained
