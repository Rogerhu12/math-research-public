#!/usr/bin/env python3
"""Exact c^7 r^25 probe of one existing genuine fourth control direction.

The original eight-coordinate matrix_operator is reused unchanged.  This
adapter evaluates its actual right primitives in the polynomial variables
c and r=c-xi.  Only the R99 direction B_t1(tau_p1,t1) is tested.  A zero
value is not a statement about all fourth controls.  Actual m8 research
execution is restricted to this public repository GitHub Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_pure_bulk_exact_membership as exact


MODEL = 'one-genuine-fourth-direction-c7-right-tail-probe-v1'
REPOSITORY = 'Rogerhu12/math-research-public'
SCRIPT = Path(__file__).resolve()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    raw = canonical(value)+b'\n'
    if len(raw) > 5000000:
        raise ValueError('single report byte budget')
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_bytes(raw)
    temporary.replace(path)


def source_hashes():
    return {p.name: {'bytes': p.stat().st_size, 'sha256': digest(p.read_bytes())}
            for p in (SCRIPT, Path(exact.__file__).resolve())}


class Polynomial:
    """Exact finite c,r polynomial.  J is positive int_xi^c, not int_c^xi."""
    def __init__(self, ring, terms=None):
        self.ring = ring
        self.terms = {tuple(key): Q(value) for key, value in (terms or {}).items() if value}
        if any(len(key) != 2 or any(type(v) is not int or v < 0 for v in key) for key in self.terms):
            raise ValueError('nonnegative integer c,r powers required')
        ring.check(self)

    def coerce(self, value):
        if isinstance(value, Polynomial):
            if value.ring is not self.ring:
                raise ValueError('polynomial belongs to a different right-anchor ring')
            return value
        return Polynomial(self.ring, {(0, 0): Q(value)})

    def __add__(self, value):
        other = self.coerce(value)
        terms = dict(self.terms)
        for key, coefficient in other.terms.items():
            terms[key] = terms.get(key, Q(0))+coefficient
        return Polynomial(self.ring, terms)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial(self.ring, {key: -coefficient for key, coefficient in self.terms.items()})

    def __sub__(self, value):
        return self+(-self.coerce(value))

    def __rsub__(self, value):
        return self.coerce(value)+(-self)

    def __mul__(self, value):
        other = self.coerce(value)
        terms = {}
        for (a, b), coefficient in self.terms.items():
            for (c, d), other_coefficient in other.terms.items():
                key = (a+c, b+d)
                terms[key] = terms.get(key, Q(0))+coefficient*other_coefficient
        return Polynomial(self.ring, terms)

    __rmul__ = __mul__

    def __truediv__(self, value):
        scalar = Q(value)
        if not scalar:
            raise ZeroDivisionError()
        return Polynomial(self.ring, {key: coefficient/scalar for key, coefficient in self.terms.items()})

    def D(self):
        # c is fixed and dr/dxi=-1.
        return Polynomial(self.ring, {(a, b-1): -b*coefficient
            for (a, b), coefficient in self.terms.items() if b})

    def J(self):
        # int_xi^c f(c-eta) d eta = int_0^r f(t) dt.
        return Polynomial(self.ring, {(a, b+1): coefficient/Q(b+1)
                                     for (a, b), coefficient in self.terms.items()})

    def rows(self):
        return [{'c_power': a, 'r_power': b, 'coefficient': str(value)}
                for (a, b), value in sorted(self.terms.items())]

    def right_anchor_trace(self):
        return {a: value for (a, b), value in self.terms.items() if b == 0}


class Ring:
    def __init__(self, seconds=60, max_terms=5000, max_degree=80, max_bits=8192):
        self.started = time.monotonic()
        self.seconds = seconds
        self.max_terms = max_terms
        self.max_degree = max_degree
        self.max_bits = max_bits
        self.operations = 0
        self.maximum_terms = 0

    def check(self, polynomial):
        self.operations += 1
        self.maximum_terms = max(self.maximum_terms, len(polynomial.terms))
        if time.monotonic()-self.started > self.seconds:
            raise RuntimeError('declared exact polynomial time budget')
        if len(polynomial.terms) > self.max_terms:
            raise RuntimeError('declared exact polynomial term budget')
        for (a, b), value in polynomial.terms.items():
            if a+b > self.max_degree:
                raise RuntimeError('declared exact polynomial degree budget')
            if max(value.numerator.bit_length(), value.denominator.bit_length()) > self.max_bits:
                raise RuntimeError('declared exact rational bit budget')

    def x(self):
        return Polynomial(self, {(1, 0): 1, (0, 1): -1})

    def power_tail(self, exponent):
        return Polynomial(self, {(0, exponent): 1})


def third_bracket(Qop, Pop, a, b, c):
    return Qop(a, Pop(b, c))-Pop(a, Qop(b, c))


def pure_fourth_response(Pop, tau, q):
    """Full R83 response specialized to F=0,D=-q^2, no slot omitted."""
    pq = Pop(q, q)
    return 2*tau(pq, q, q)+4*tau(q, q, pq)-4*Pop(q, tau(q, q, q))


def actual(args):
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
        raise RuntimeError('actual tail probe is restricted to the public repository Actions')
    ring = Ring(seconds=args.max_seconds)
    # Reuse the published complete operator, including all three right tails.
    qop = exact.matrix_operator(ring, [0, 1, 0, 0, 0, 0, 0, 0])
    pop = exact.matrix_operator(ring, [0, 0, 0, 0, 0, 0, 0, 1])
    tau = lambda a, b, c: third_bracket(qop, pop, a, b, c)
    q = ring.power_tail(8)
    full_pure = pure_fourth_response(pop, tau, q)
    minus_four = full_pure/16
    value = minus_four.terms.get((7, 25), Q(0))
    all_degree_32 = all(a+b == 32 for a, b in minus_four.terms)
    report = {'model': MODEL, 'completion': 'complete',
        'direction': 'B_P(tau_Q,P), P=Phi_t1, Q=Phi_p1',
        'known_true_direction_source': 'R71/R83/R99, tau_p1_t1 v2 original column 12',
        'operator_source': 'unchanged literature_pure_bulk_exact_membership.matrix_operator',
        'profile': 'unit right tail q=(c-xi)^8; r=c-xi, one true right anchor c',
        'right_primitive': 'J=int_xi^c; D_xi=-D_r and c is constant',
        'pure_full_phase_specialization': 'F=0,D=-q^2: 2*tau(Pqq;q,q)+4*tau(q;q,Pqq)-4*P(q,tau(q;q,q))',
        'minus_four_mode_normalization': 'one sixteenth of the F=0 full q^4 response',
        'c7_r25_full_pure_coefficient': str(full_pure.terms.get((7, 25), Q(0))),
        'c7_r25_minus_four_coefficient': str(value),
        'this_direction_has_nonzero_c7': bool(value),
        'all_output_terms_have_total_degree_32': all_degree_32,
        'c8_r25_coefficient': str(minus_four.terms.get((8, 25), Q(0))),
        'complete_minus_four_polynomial': minus_four.rows(),
        'complete_polynomial_sha256': digest(canonical(minus_four.rows())),
        'polynomial_terms': len(minus_four.terms),
        'maximum_intermediate_terms': ring.maximum_terms, 'exact_polynomial_operations': ring.operations,
        'source_hashes': source_hashes(),
        'old_R99_queries_or_character_recomputed': False,
        'old_R100_or_R106_identity_recomputed': False,
        'other_fourth_directions_evaluated': 0,
        'zero_does_not_annihilate_all_R8': True,
        'base_cost_or_full_fourth_function_cancelled': False,
        'geometric_path_evaluated': False, 'legal_global_profile_constructed': False,
        'complete_fourth_range_proved': False,
        'elapsed_seconds': time.monotonic()-ring.started,
        'peak_rss_mib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024}
    if not all_degree_32:
        report['completion'] = 'unexpected-output-degree'
    return report


def development():
    ring = Ring(seconds=20, max_degree=20)
    f = Polynomial(ring, {(1, 0): 1, (0, 1): 2, (0, 2): 3})
    g = Polynomial(ring, {(0, 0): 2, (1, 1): -1, (0, 3): 1})
    p = exact.matrix_operator(ring, [0, 0, 0, 0, 0, 0, 0, 1])
    q = exact.matrix_operator(ring, [0, 1, 0, 0, 0, 0, 0, 0])
    scalar_one = {(0, 0): Q(1)}
    fabricated = Polynomial(ring, {(2, 3): Q(5, 7), (1, 4): Q(-2, 9)})
    decoded = {tuple((row['c_power'], row['r_power'])): Q(row['coefficient'])
               for row in json.loads(canonical(fabricated.rows()))}
    checks = {
        'xi_derivative_in_c_r_coordinates': ring.x().D().terms == scalar_one,
        'positive_right_primitive_has_negative_derivative': not (f.J().D()+f).terms,
        'right_primitive_has_zero_true_endpoint_value': not f.J().right_anchor_trace(),
        'incorrect_anchor_constant_is_detected': bool((f.J()+1).right_anchor_trace()),
        'original_t1_operator_symmetric_on_small_manufactured_inputs': not (p(f, g)-p(g, f)).terms,
        'original_p1_operator_symmetric_on_small_manufactured_inputs': not (q(f, g)-q(g, f)).terms,
        'zero_self_bracket_preserved': not third_bracket(p, p, f, g, f).terms,
        'exact_rational_polynomial_json_roundtrip': decoded == fabricated.terms,
    }
    return {'model': MODEL, 'mode': 'artificial-development-only', 'passed': all(checks.values()),
        'checks': checks, 'research_m8_target_evaluated': False, 'research_input_loaded': False,
        'source_hashes': source_hashes()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--max-seconds', type=float, default=60)
    args = parser.parse_args()
    started = time.monotonic()
    try:
        report = development() if args.check_only else actual(args)
        passed = report['passed'] if args.check_only else report['completion'] == 'complete'
    except Exception as exc:
        report = {'model': MODEL, 'completion': 'error-or-budget-exit', 'error': str(exc),
            'exception_type': type(exc).__name__, 'source_hashes': source_hashes(),
            'elapsed_seconds': time.monotonic()-started,
            'no_unknown_coefficient_is_interpreted_as_zero': True}
        passed = False
    write_json(args.out, report)
    print(json.dumps({'passed': passed, 'mode': report.get('mode'),
                      'completion': report.get('completion'),
                      'this_direction_has_nonzero_c7': report.get('this_direction_has_nonzero_c7')}), flush=True)
    return 0 if passed else 2


if __name__ == '__main__':
    raise SystemExit(main())
