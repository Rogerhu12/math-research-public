#!/usr/bin/env python3
"""Finite bridge h controls with exact fixed frame/scalar end conditions.

Only an algebraic development toy is exposed as a CLI.  Real controls and
geometry evaluations belong in public-repository Actions callers.  Controlled
items have a new schema so legacy movement/range helpers cannot silently ignore
the h perturbation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial import polynomial as poly

import literature_range_numeric_engine as engine

LD = engine.LD
KIND = 'endpoint_preserving_h_ramp_v1'


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return out


def scale(a, scalar):
    return [scalar * v for v in a]


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return out


def differentiate(a, order=1):
    for _ in range(order):
        a = [F(i) * a[i] for i in range(1, len(a))] or [F(0)]
    return a


def evaluate_exact(a, x):
    value = F(0)
    for v in reversed(a):
        value = value * x + v
    return value


def shifted_legendre(n):
    if n < 0:
        raise ValueError('negative polynomial degree')
    previous, current = [F(1)], [F(-1), F(2)]
    if n == 0:
        return previous
    for j in range(1, n):
        following = scale(add(
            scale(multiply([F(-1), F(2)], current), F(2 * j + 1)),
            scale(previous, F(-j)),
        ), F(1, j + 1))
        previous, current = current, following
    return current


def basis_polynomial(j):
    return multiply([F(0), F(0), F(1), F(-2), F(1)], shifted_legendre(j))


def bernstein_absolute_bound(coefficients):
    n = len(coefficients) - 1
    bernstein = [sum((coefficients[i] * F(math.comb(j, i), math.comb(n, i))
                      for i in range(j + 1)), F(0)) for j in range(n + 1)]
    return max(abs(v) for v in bernstein)


def rational(value):
    if isinstance(value, F):
        return value
    if isinstance(value, int):
        return F(value)
    if isinstance(value, str):
        return F(value)
    return F.from_float(float(value))


def numeric(value):
    value = rational(value)
    return LD(value.numerator) / LD(value.denominator)


def normalize_base(item):
    if item['kind'] == 'bulk':
        raise ValueError('h bridge controls may not be attached to an N-scaled bulk')
    if item['kind'] == 'constant':
        # Preserve the exact frozen h value, without rounding a new reciprocal.
        b = str(F(1) / (2 * rational(item['h'])))
        return dict(kind='ramp', duration=item['duration'], k0=item['k'], k1=item['k'],
                    b0=b, b_end=b, eta=0., omega0=item['omega'])
    if item['kind'] != 'ramp':
        raise ValueError('expected a fixed-length primitive ramp or constant segment')
    keys = ('kind', 'duration', 'k0', 'k1', 'b0', 'b_end', 'eta', 'omega0')
    return {k: item[k] for k in keys}


def positivity_data(base, coefficients):
    b0, b1, eta = (rational(base[k]) for k in ('b0', 'b_end', 'eta'))
    power = [b0, b1 - b0 + eta, -eta]
    candidates = [b0, b1]
    if power[2] > 0:
        critical = -power[1] / (2 * power[2])
        if 0 < critical < 1:
            candidates.append(evaluate_exact(power, critical))
    lower = min(candidates)
    bounds = [bernstein_absolute_bound(differentiate(basis_polynomial(j)))
              for j in range(len(coefficients))]
    consumption = sum((abs(rational(v)) * bound for v, bound in zip(coefficients, bounds)), F(0))
    return dict(base_lower=lower, perturbation_bound=consumption,
                certified_lower=lower - consumption, derivative_bounds=bounds)


def control_identity(item):
    payload = {key: value for key, value in item.items()
               if key != 'control_identity_sha256'}
    encoded = json.dumps(payload, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


def validate_control_identity(item):
    """Bind the actual control fields and stated bounds to their frozen hash."""
    if item.get('kind') != KIND:
        raise ValueError('expected a controlled bridge primitive')
    if item.get('control_identity_sha256') != control_identity(item):
        raise ValueError('controlled primitive identity does not match its actual fields')
    base = item['base']
    if rational(item['duration']) != rational(base['duration']) or rational(base['duration']) <= 0:
        raise ValueError('controlled primitive has inconsistent or nonpositive duration')
    coefficients = item['coefficients']
    if not coefficients or len(coefficients) > 8 or not all(math.isfinite(v) for v in coefficients):
        raise ValueError('one to eight finite h-control coefficients are required')
    bounds = positivity_data(base, coefficients)
    stated = {key: str(value) for key, value in bounds.items() if key != 'derivative_bounds'}
    if (bounds['certified_lower'] <= 0 or item.get('positivity_bound') != stated or
            item.get('derivative_bounds') != [str(value) for value in bounds['derivative_bounds']]):
        raise ValueError('controlled primitive positivity metadata is not its actual bound')
    return bounds


def make_controlled_item(item, coefficients):
    base = normalize_base(item)
    if base['duration'] <= 0:
        raise ValueError('bridge duration must be positive')
    coefficients = [float(v) for v in coefficients]
    if not coefficients or len(coefficients) > 8 or not all(math.isfinite(v) for v in coefficients):
        raise ValueError('one to eight finite h-control coefficients are required')
    bounds = positivity_data(base, coefficients)
    if bounds['certified_lower'] <= 0:
        raise ValueError('the exact polynomial bound does not preserve positive reciprocal h')
    result = dict(kind=KIND, name=item.get('name', 'bridge_h_control'),
                  duration=base['duration'], base=base, coefficients=coefficients,
                  basis='F_j=S^2(1-S)^2 P_j(2S-1); delta_b=sum beta_j F_j_prime',
                  original_frame_curve_unchanged=True,
                  exact_omega_endpoints_and_range_unchanged=True,
                  positivity_bound={k: str(v) for k, v in bounds.items() if k != 'derivative_bounds'},
                  derivative_bounds=[str(v) for v in bounds['derivative_bounds']])
    result['control_identity_sha256'] = control_identity(result)
    return result


def exact_base_end(base):
    k0, k1, omega0 = (rational(base[k]) for k in ('k0', 'k1', 'omega0'))
    b0, b1, eta = (rational(base[k]) for k in ('b0', 'b_end', 'eta'))
    return k1, F(1) / (2 * b1), omega0 + (k1 - k0) * ((b0 + b1) / 2 + eta / 6)


def reverse_controlled_item(item):
    validate_control_identity(item)
    base = item['base']
    reversed_base = dict(base, k0=base['k1'], k1=base['k0'],
                         b0=base['b_end'], b_end=base['b0'],
                         omega0=str(exact_base_end(base)[2]))
    reversed_base['name'] = item.get('name', 'bridge_h_control') + '_reverse'
    coefficients = [(-1 if j % 2 == 0 else 1) * value
                    for j, value in enumerate(item['coefficients'])]
    return make_controlled_item(reversed_base, coefficients)


def polynomial_values(coefficients, x):
    return poly.polyval(x, [LD(v.numerator) / LD(v.denominator) for v in coefficients])


def F_derivatives(j, S, maximum=4):
    # Factored endpoint values avoid cancellation in F and F' near S=0,1.
    base = [S * S * (1 - S) ** 2,
            2 * S * (1 - S) * (1 - 2 * S),
            2 - 12 * S + 12 * S * S, -12 + 24 * S,
            np.full_like(S, 24)]
    legendre = shifted_legendre(j)
    derivatives = [polynomial_values(differentiate(legendre, r), S) for r in range(maximum + 1)]
    return [sum((math.comb(r, i) * base[i] * derivatives[r - i]
                 for i in range(min(r, 4) + 1)), np.zeros_like(S))
            for r in range(maximum + 1)]


def geometry_jets(item, t, omega_offset=0):
    if item.get('kind') != KIND:
        return engine.geometry_jets(item, t, omega_offset)
    validate_control_identity(item)
    base = item['base']
    t = np.asarray(t, dtype=LD)
    if np.any((t < 0) | (t > 1)):
        raise ValueError('local bridge parameter must lie in [0,1]')
    result = np.zeros((9, len(t)), dtype=LD)
    interior = (t > 0) & (t < 1)
    tau = t[interior]
    duration = LD(base['duration'])
    b0, b1, eta = (numeric(base[k]) for k in ('b0', 'b_end', 'eta'))
    k0, k1 = LD(base['k0']), LD(base['k1'])
    dk = k1 - k0
    rr = 1 / (1 - tau) - 1 / tau
    S = np.empty_like(tau)
    nonnegative = rr >= 0
    with np.errstate(under='ignore'):
        S[nonnegative] = 1 / (1 + np.exp(-rr[nonnegative]))
        ex = np.exp(rr[~nonnegative])
        S[~nonnegative] = ex / (1 + ex)
    r1 = (1 / (1 - tau) ** 2 + 1 / tau ** 2) / duration
    r2 = (2 / (1 - tau) ** 3 - 2 / tau ** 3) / duration ** 2
    r3 = (6 / (1 - tau) ** 4 + 6 / tau ** 4) / duration ** 3
    S1 = S * (1 - S) * r1
    S2 = S * (1 - S) * (r2 + (1 - 2 * S) * r1 * r1)
    S3 = S * (1 - S) * (r3 + 3 * (1 - 2 * S) * r1 * r2
                                      + (1 - 6 * S + 6 * S * S) * r1 ** 3)
    bs = [b0 * (1 - S) + b1 * S + eta * S * (1 - S),
          np.full_like(S, b1 - b0 + eta) - 2 * eta * S,
          np.full_like(S, -2 * eta), np.zeros_like(S)]
    omega_change = np.zeros_like(S)
    for j, beta in enumerate(item['coefficients']):
        derivatives = F_derivatives(j, S)
        for r in range(4):
            bs[r] += LD(beta) * derivatives[r + 1]
        omega_change += LD(beta) * derivatives[0]
    b, bS, bSS, bSSS = bs
    if np.any(b <= 0):
        raise ValueError('nonpositive h reciprocal after floating evaluation')
    b_first = bS * S1
    b_second = bSS * S1 * S1 + bS * S2
    b_third = bSSS * S1 ** 3 + 3 * bSS * S1 * S2 + bS * S3
    result[0, interior] = 1 / (2 * b)
    result[1, interior] = -b_first / (2 * b * b)
    result[2, interior] = b_first * b_first / b ** 3 - b_second / (2 * b * b)
    result[3, interior] = (-3 * b_first ** 3 / b ** 4 + 3 * b_first * b_second / b ** 3
                           - b_third / (2 * b * b))
    result[4, interior] = k0 + dk * S
    result[5, interior] = dk * S1
    result[6, interior] = dk * S2
    result[7, interior] = dk * S3
    result[8, interior] = numeric(base['omega0']) + LD(omega_offset) + dk * (
        b0 * S + (b1 - b0) * S * S / 2 + eta * (S * S / 2 - S ** 3 / 3)
        + omega_change)
    for endpoint, bend, kend, om in (
        (0, b0, k0, numeric(base['omega0']) + LD(omega_offset)),
        (1, b1, k1, numeric(exact_base_end(base)[2]) + LD(omega_offset)),
    ):
        mask = t == endpoint
        result[0, mask] = 1 / (2 * bend)
        result[4, mask] = kend
        result[8, mask] = om
    return result


def toy_check():
    import copy
    import sympy as sp
    for j in range(8):
        polynomial = basis_polynomial(j)
        derivative = differentiate(polynomial)
        assert evaluate_exact(polynomial, F(0)) == evaluate_exact(polynomial, F(1)) == 0
        assert evaluate_exact(derivative, F(0)) == evaluate_exact(derivative, F(1)) == 0
        assert sum((v / F(i + 1) for i, v in enumerate(derivative)), F(0)) == 0
        def reverse_polynomial(values):
            return [sum((values[i] * math.comb(i, r) * (-1) ** r
                         for i in range(r, len(values))), F(0)) for r in range(len(values))]
        assert reverse_polynomial(polynomial) == scale(polynomial, F((-1) ** j))
        assert reverse_polynomial(derivative) == scale(derivative, F((-1) ** (j + 1)))
    b, bS, bSS, bSSS, S1, S2, S3 = sp.symbols('b bS bSS bSSS S1 S2 S3')
    b1 = bS * S1
    b2 = bSS * S1 ** 2 + bS * S2
    b3 = bSSS * S1 ** 3 + 3 * bSS * S1 * S2 + bS * S3
    deriv = lambda z: (sp.diff(z, b) * b1 + sp.diff(z, bS) * bSS * S1
                       + sp.diff(z, bSS) * bSSS * S1 + sp.diff(z, S1) * S2
                       + sp.diff(z, S2) * S3)
    assert sp.cancel(deriv(1 / (2 * b)) + b1 / (2 * b ** 2)) == 0
    assert sp.cancel(deriv(-b1 / (2 * b ** 2)) - (b1 ** 2 / b ** 3 - b2 / (2 * b ** 2))) == 0
    assert sp.cancel(deriv(b1 ** 2 / b ** 3 - b2 / (2 * b ** 2))
                     - (-3 * b1 ** 3 / b ** 4 + 3 * b1 * b2 / b ** 3 - b3 / (2 * b ** 2))) == 0
    # Exact artificial rational bounds; no actual connector is read or evaluated.
    base = dict(b0=F(1, 2), b_end=F(3, 4), eta=F(1, 3))
    bounds = positivity_data(base, [F(1, 100), F(-1, 200), F(1, 300)])
    assert bounds['certified_lower'] > 0
    artificial = make_controlled_item(dict(kind='ramp', duration=2., k0=0., k1=1.,
        b0=.5, b_end=.75, eta=.25, omega0=0.), [.01, -.005])
    validate_control_identity(artificial)
    validate_control_identity(reverse_controlled_item(artificial))
    tampered = copy.deepcopy(artificial)
    tampered['coefficients'][0] += .001
    try:
        validate_control_identity(tampered)
    except ValueError:
        pass
    else:
        raise AssertionError('changed controls retained a stale identity')
    tampered['control_identity_sha256'] = control_identity(tampered)
    try:
        validate_control_identity(tampered)
    except ValueError:
        pass
    else:
        raise AssertionError('changed controls retained stale positivity metadata')
    return dict(schema='endpoint-preserving-h-control-exact-toy-v1',
        exact_polynomial_endpoint_and_zero_omega_increment_checks=8,
        exact_h_three_jet_chain_rule=True,
        exact_reverse_control_parity=True,
        artificial_control_identity_and_tamper_rejection=True,
        artificial_rational_positive_lower=str(bounds['certified_lower']),
        original_frame_curve_unchanged_by_definition=True,
        actual_connector_or_profile_evaluated=False,
        whole_fourth_condition_paid=False,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--toy-only', action='store_true', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(toy_check(), indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
