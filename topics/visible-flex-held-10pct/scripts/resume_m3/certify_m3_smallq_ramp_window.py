#!/usr/bin/env python3
"""R40: exact lower enclosure for the actual flat-ramp characteristic window.

No BVP, quadrature library, floating-point square root, or transcendental
function enters the certificate.  The optional checkpoint only identifies the
existing physical ramp parameters; it is not certified as a circular solution.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def frac(value):
    return f'{value.numerator}/{value.denominator}'


def decimal_lower(value, digits=40):
    scale = 10 ** digits
    k = value.numerator * scale // value.denominator
    return f'{k // scale}.{k % scale:0{digits}d}'


def turn_ramp(t, eta):
    """Exact F, its primitive P, and d=F'; same piecewise polynomial law."""
    if not F(0) <= t <= F(1) or not F(0) < eta < F(1, 2):
        raise ValueError('Outside the stated flat-ramp law')
    z = min(t, 1 - t)
    x = z / eta
    if z < eta:
        small_f = eta / (1 - eta) * (x ** 3 - x ** 4 / 2)
        small_p = eta ** 2 / (1 - eta) * (x ** 4 / 4 - x ** 5 / 10)
        d = (3 * x ** 2 - 2 * x ** 3) / (1 - eta)
    else:
        small_f = (z - eta / 2) / (1 - eta)
        small_p = (z ** 2 / 2 - eta * z / 2 + 3 * eta ** 2 / 20) / (1 - eta)
        d = 1 / (1 - eta)
    if t <= F(1, 2):
        return small_f, small_p, d
    return 1 - small_f, F(1, 2) - (1 - t) + small_p, d


def certificate(q_lower, q_upper, delta_lower, vu, eps, eta, panels, digits):
    if not (0 <= q_lower <= q_upper and delta_lower > 0 and
            0 < vu and 0 < eps < F(1, 2) and 0 < eta < F(1, 2)):
        raise ValueError('Invalid parameter range')
    y_lower = (1 + 8 * q_lower) * vu
    y_upper = (1 + 8 * q_upper) * vu
    if not y_upper < 1:
        raise ValueError('The original R5 square root would not stay positive')
    assert y_upper < F('0.597601')
    B = delta_lower * eps / (1 - eps)
    scale = 10 ** digits
    integer_sum = 0
    previous = turn_ramp(F(0), eta)
    assert previous == (0, 0, 0)
    assert turn_ramp(F(1), eta) == (1, F(1, 2), 0)
    assert turn_ramp(F(1, 2), eta)[0] == F(1, 2)
    for j in range(panels):
        current = turn_ramp(F(j + 1, panels), eta)
        f0, p0, d0 = previous
        f1, p1, d1 = current
        assert 0 <= f0 <= f1 <= 1 and 0 <= p0 <= p1 <= F(1, 2)
        # d is increasing, then constant, then decreasing.  Its minimum on
        # every interval is therefore the minimum of its two endpoint values.
        # P and F are nondecreasing.  The two denominator factors below are
        # separate upper bounds, so their product is an upper bound as well.
        radicand = B * min(d0, d1) / ((1 + B * p1) * (1 - y_lower ** 2 * f0 ** 2))
        integer_sum += isqrt(radicand.numerator * scale ** 2 // radicand.denominator)
        previous = current
    lower = F(integer_sum, panels * scale)
    target = F(21, 100)
    published = F('0.2108827779904414')
    assert lower > published > target
    return dict(
        q_lower=frac(q_lower), q_upper=frac(q_upper), delta_lower=frac(delta_lower),
        delta_upper=None, vu=frac(vu), eps=frac(eps), eta=frac(eta),
        B_at_lower_endpoint=frac(B), Rvu_upper=frac(y_upper),
        one_minus_Rvu_squared_lower=frac(1 - y_upper ** 2),
        panels=panels, sqrt_decimal_places=digits,
        exact_lower=frac(lower), lower_decimal_rounded_down=decimal_lower(lower),
        exact_margin_above_arc_halfwidth=frac(lower - target),
        arc_halfwidth=frac(target), published_strict_lower=frac(published),
        gates=dict(lower_above_published=True, published_above_arc_halfwidth=True,
                   Rvu_below_one=True, Rvu_below_0_597601=True),
        lower_validity='q in the stated closed interval; every delta >= delta_lower; '
                       'the fixed vu/eps/eta values in this record.  Monotonicity is '
                       'pointwise in q and delta, not an empirical parameter scan.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile-checkpoint', type=Path)
    p.add_argument('--reference-source', type=Path)
    p.add_argument('--panels', type=int, default=2000)
    p.add_argument('--sqrt-digits', type=int, default=60)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.panels < 2000 or a.sqrt_digits < 50:
        raise ValueError('Use at least the recorded certificate resolution')
    qlo, qhi, dlo = F(39, 1000), F(41, 1000), F(3, 50)
    vu, eps, eta = F(9, 20), F(2, 5), F(1, 20)
    rows = {'exact_rational_design': certificate(qlo, qhi, dlo, vu, eps, eta,
                                                 a.panels, a.sqrt_digits)}
    checkpoint = None
    if a.profile_checkpoint:
        record = json.loads(gzip.decompress(a.profile_checkpoint.read_bytes()))
        profile = record['frozen_profile']
        if profile['direction'] != 'outward' or profile['ramp_law'] != 'flat':
            raise ValueError('The checkpoint uses a different initial profile')
        expected = {'vu': vu, 'ramp': eps, 'ramp_eta': eta}
        for key, value in expected.items():
            if profile[key] != float(value):
                raise ValueError(f'The checkpoint changed the {key} design')
        actual_q = F.from_float(float(record['actual_primary_amplitude']))
        actual_delta = F.from_float(float(profile['delta']))
        if not qlo <= actual_q <= qhi or not actual_delta >= dlo:
            raise ValueError('The checkpoint parameters leave the theorem window')
        # Also certify the analytic ramp interpreted with the exact binary64
        # parameter values.  This does not claim an error bound for NumPy's
        # pointwise polynomial evaluation; both versions use exact polynomials.
        binary_parameters = [F.from_float(float(profile[key]))
                             for key in ('vu', 'ramp', 'ramp_eta')]
        rows['checkpoint_binary_parameters'] = certificate(
            qlo, qhi, dlo, *binary_parameters, a.panels, a.sqrt_digits)
        checkpoint = dict(path=str(a.profile_checkpoint.resolve()),
                          sha256=sha(a.profile_checkpoint), frozen_profile=profile,
                          exact_binary_q=frac(actual_q), exact_binary_delta=frac(actual_delta),
                          role='Parameter identity only; no circular BVP or metric claim.')
    references = {str(Path(__file__).resolve()): sha(__file__)}
    if a.reference_source:
        references[str(a.reference_source.resolve())] = sha(a.reference_source)
    result = dict(theorem='R40', command=sys.argv, certificate=rows,
                  profile_checkpoint=checkpoint, source_sha256=references,
                  scope='The R5 guaranteed circular-data cone is exhausted by the first '
                        'negative-K acceleration end for a normal-angle halfwidth 21/100. '
                        'This neither constructs a circular coupled solution nor proves '
                        'that a circular patch must disappear afterwards.  It is independent '
                        'of primary/control transition widths whenever the exact protected '
                        'arc still has radius R=1+8q.')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({name: {'strict_lower': row['lower_decimal_rounded_down'],
                             'Rvu_upper': row['Rvu_upper'], 'gates': row['gates']}
                      for name, row in rows.items()}, indent=2))


if __name__ == '__main__':
    main()
