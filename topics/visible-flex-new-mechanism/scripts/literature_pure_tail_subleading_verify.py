#!/usr/bin/env python3
"""Verify R88 against a published R56 tail DAG, without recompiling forcing.

Research mode only consumes the byte-bound public Actions structure.  It
keeps every genuine history and uses just the proved, zero-initial first
integral u0 + a_mp b0^2/(2 a_mm) = 0.  No geometric path is evaluated.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import json
import os
from pathlib import Path
import resource
import time

import literature_pure_tail_period as tail
import literature_range_profile_algebra as formal


MODEL = 'R88-published-tail-DAG-subleading-first-integral-v1'
SCRIPT = Path(__file__).resolve()
REPOSITORY = tail.REPOSITORY
canonical = tail.canonical
sha256 = tail.sha256
write_json = tail.write_json


def source_hashes():
    return {p.name: sha256(p.read_bytes()) for p in
            (SCRIPT, Path(tail.__file__).resolve(), Path(formal.__file__).resolve())}


def deep_tuple(value):
    return tuple(deep_tuple(v) for v in value) if isinstance(value, list) else value


def load_coefficients(structure, budget):
    """Rehydrate the actual ordered DAG, retaining all original node ids."""
    nodes = [deep_tuple(node) for node in structure['coefficient_DAG']]
    if len(nodes) < 2 or nodes[:2] != [('c', 0, 1), ('c', 1, 1)]:
        raise ValueError('unexpected coefficient zero/one identity')
    if len(nodes) >= budget.max_nodes or len(set(nodes)) != len(nodes):
        raise ValueError('invalid or oversized interned coefficient DAG')
    rhs = structure['state_rhs']
    labels = structure['state_labels']
    if len(rhs) != len(labels) or structure['state_initial_values'] != ['0'] * len(rhs):
        raise ValueError('genuine histories must retain their zero initial data')
    if any(type(v) is not int or not 0 <= v < len(nodes) for v in rhs):
        raise ValueError('state RHS outside the original DAG')
    for index, node in enumerate(nodes):
        tag = node[0]
        if tag == 'c':
            if len(node) != 3 or node[2] <= 0:
                raise ValueError('invalid rational coefficient')
        elif tag == 'g':
            if len(node) != 3 or type(node[2]) is not int or node[2] < 0:
                raise ValueError('invalid geometry jet')
            if node[1] == 'omega' and node[2] != 0:
                raise ValueError('omega must use the genuine k_s/(2h) relation')
        elif tag == 'st':
            if len(node) != 2 or type(node[1]) is not int or not 0 <= node[1] < len(rhs):
                raise ValueError('unknown genuine history')
        elif tag == 'add':
            if any(type(child) is not int or not 0 <= child < index or d <= 0
                   for child, n, d in node[1]):
                raise ValueError('invalid sum references')
        elif tag == 'mul':
            if node[2] <= 0 or any(type(child) is not int or not 0 <= child < index
                                   or type(power) is not int
                                   for child, power in node[3]):
                raise ValueError('invalid product references')
        else:
            raise ValueError(f'unknown coefficient tag {tag}')
    c = tail.TailCoefficients(budget)
    c.nodes = nodes
    c.ids = {node: index for index, node in enumerate(nodes)}
    c.zero, c.one = 0, 1
    c.state_rhs = list(rhs)
    c.state_labels = [deep_tuple(v) for v in labels]
    c.derivatives = {}
    return c


def select_root(structure, key, power, grade):
    rows = [v for v in structure[key]
            if v['t_power'] == power and v['profile_grade'] == grade]
    if len(rows) != 1:
        raise ValueError(f'exactly one complete coefficient required: {key}, {power}, {grade}')
    root = rows[0]['coefficient_root']
    if type(root) is not int or not 0 <= root < len(structure['coefficient_DAG']):
        raise ValueError('selected root outside the published DAG')
    return root


def polynomial_record(value, readable_terms=0):
    rows = tail.poly_rows(value)
    result = {'terms': len(rows), 'exact_zero': not value,
              'normalized_sha256': sha256(canonical(rows))}
    if readable_terms:
        result['readable_terms'] = rows[:readable_terms]
        result['readable_terms_truncated'] = len(rows) > readable_terms
    return result


def max_power(value, variable):
    return max((dict(m).get(variable, 0) for m in value), default=-1)


def divide_by_monic_history(normalizer, polynomial, invariant, variable):
    """Exact division by a *linear monic* history relation, no inversion.

    The coefficient ring is the Laurent ring of every remaining geometry
    jet/history.  A nonzero remainder stays nonzero; it is not a period claim.
    """
    unit = ((variable, 1),)
    if invariant.get(unit) != 1 or any(dict(m).get(variable, 0)
                                     for m in invariant if m != unit):
        raise ValueError('first integral is not monic linear in the chosen history')
    if any(dict(m).get(variable, 0) < 0 for m in polynomial):
        raise ValueError('negative powers of a genuine history are unsupported')
    quotient = {}
    remainder = dict(polynomial)
    while remainder and max_power(remainder, variable) >= 1:
        degree = max_power(remainder, variable)
        leading = {}
        for monomial, coefficient in remainder.items():
            powers = dict(monomial)
            if powers.get(variable, 0) != degree:
                continue
            powers[variable] -= 1
            key = tuple(sorted((v, p) for v, p in powers.items() if p))
            leading[key] = coefficient
        quotient = normalizer.add((1, quotient), (1, leading))
        remainder = normalizer.add((1, remainder),
                                   (-1, normalizer.multiply(leading, invariant)))
        normalizer.c.budget.time_check()
    return quotient, remainder


def constant_initial_trace(value):
    """The actual zero initial histories at a constant scalar germ only."""
    result = {}
    for monomial, coefficient in value.items():
        vanishes = False
        for variable, power in monomial:
            zero_variable = variable.startswith('state_')
            if not zero_variable and variable.startswith(('h_', 'k_')):
                zero_variable = int(variable.rsplit('_', 1)[1]) >= 1
            if zero_variable:
                if power < 0:
                    raise ValueError('initial trace would divide by a vanishing quantity')
                if power:
                    vanishes = True
                    break
        if not vanishes:
            result[monomial] = coefficient
    return result


def public_inputs(args):
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
        raise RuntimeError('research verification is restricted to this public repository GitHub Actions')
    if args.report is None or args.structure is None:
        raise ValueError('--report and --structure are required for the published input')
    notes = SCRIPT.parent.parent / 'notes'
    for path in (args.report, args.structure):
        if not path.resolve().is_relative_to(notes.resolve()):
            raise ValueError('research inputs must be published files under this topic notes/')
    report_bytes = args.report.read_bytes()
    packed = args.structure.read_bytes()
    if len(report_bytes) > 100000 or len(packed) > 5000000:
        raise ValueError('input byte budget')
    original = json.loads(report_bytes)
    if original.get('model') != tail.MODEL or original.get('completion') != 'complete':
        raise ValueError('input is not a completed original tail compilation')
    if not original.get('R85_leading_identities_verified'):
        raise ValueError('published leading identities were not verified')
    artifact, = [v for v in original['artifacts'] if v['file'] == args.structure.name]
    if len(packed) != artifact['compressed_bytes'] or sha256(packed) != artifact['compressed_sha256']:
        raise ValueError('compressed structure does not match the published receipt')
    raw = gzip.decompress(packed)
    if len(raw) > 10000000 or len(raw) != artifact['raw_bytes'] or sha256(raw) != artifact['raw_sha256']:
        raise ValueError('raw structure does not match the published receipt')
    structure = json.loads(raw)
    current_sources = source_hashes()
    for name, expected in original['source_hashes'].items():
        if current_sources.get(name) != expected or structure['source_hashes'].get(name) != expected:
            raise ValueError(f'original imported source changed: {name}')
    if structure['model'] != tail.MODEL or structure['tail_exponent'] != original['tail_exponent']:
        raise ValueError('published structure model/exponent mismatch')
    if structure['geometry_relation'] != 'omega_s=k_s/(2h); D_s c=0':
        raise ValueError('unexpected physical geometry relation')
    if len(structure['state_rhs']) != original['genuine_history_count']:
        raise ValueError('published genuine history count mismatch')
    return structure, {'report': args.report.name, 'report_bytes': len(report_bytes),
                       'report_sha256': sha256(report_bytes),
                       'structure': args.structure.name, 'compressed_bytes': len(packed),
                       'compressed_sha256': sha256(packed), 'raw_bytes': len(raw),
                       'raw_sha256': sha256(raw), 'original_source_hashes': original['source_hashes']}


def verify(args, progress):
    started = time.monotonic()
    structure, provenance = public_inputs(args)
    progress['input'] = provenance
    budget = formal.Budget(max_nodes=args.max_nodes, max_atoms=1,
                           max_terms=args.max_terms, max_seconds=args.max_seconds)
    c = load_coefficients(structure, budget)
    normalizer = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                                        max_cache_terms=args.max_cache_terms,
                                        max_rss_mib=args.max_rss_mib)
    m = structure['tail_exponent']
    if type(m) is not int or m < 8:
        raise ValueError('R88 requires an integer exponent at least eight')
    p, r, n = 2*m-3, 3*m-6, 4*m-9
    b = select_root(structure, 'second_completed_scalar', p, 2)
    d = select_root(structure, 'second_completed_scalar', p+1, 2)
    u = select_root(structure, 'third_completed_scalar', r, 3)
    v = select_root(structure, 'third_completed_scalar', r+1, 3)
    density = select_root(structure, 'pure_completed_period_density', n+1, 4)
    alpha = Q(p**3, 8*m*m*(m-1))
    beta = Q(3*p*(3*m-5), 16*m*(m-1))
    kappa = tail.aij(m, p) / (2*tail.aij(m, m))
    potential = c.linear([(alpha, c.multiply(c.power(b, 2), d)),
                          (beta, c.multiply(b, v))])
    invariant = c.linear([(1, u), (kappa, c.power(b, 2))])
    invariant_derivative = c.derivative(invariant)
    derivative = c.derivative(potential)
    # This orientation is retained in the certificate: density - Ds(potential).
    residual = c.linear([(1, density), (-1, derivative)])
    progress['stage'] = 'exact-first-integral-and-subleading-identity'
    invariant_polynomial = normalizer.node(invariant)
    derivative_polynomial = normalizer.node(invariant_derivative)
    initial_polynomial = constant_initial_trace(invariant_polynomial)
    if derivative_polynomial or initial_polynomial:
        raise ValueError('the proposed first integral lacks its genuine ODE/initial certificate')
    history_ids = [i for i, label in enumerate(structure['state_labels'])
                   if label[0] == 3 and label[2] == r and label[3] == 3]
    if len(history_ids) != 1:
        raise ValueError('cannot identify the original leading third history')
    variable = f'state_{history_ids[0]}'
    residual_polynomial = normalizer.node(residual)
    quotient, remainder = divide_by_monic_history(normalizer, residual_polynomial,
                                                  invariant_polynomial, variable)
    reconstruction = normalizer.add((1, residual_polynomial),
                                    (-1, normalizer.multiply(quotient, invariant_polynomial)),
                                    (-1, remainder))
    if reconstruction:
        raise AssertionError('exact polynomial division reconstruction failed')
    # Freshly expand the original two sides using a separate memo table.
    fresh = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                                   max_cache_terms=args.max_cache_terms,
                                   max_rss_mib=args.max_rss_mib)
    fresh_residual = fresh.add((1, fresh.node(density)), (-1, fresh.node(derivative)),
                               (-1, fresh.multiply(quotient, fresh.node(invariant))))
    if fresh_residual != remainder:
        raise AssertionError('fresh original-DAG verification differs from the division remainder')
    positive = not remainder
    certificate = {
        'model': MODEL, 'input': provenance, 'source_hashes': source_hashes(),
        'coefficient_DAG': c.nodes, 'state_rhs': c.state_rhs,
        'state_labels': c.state_labels, 'state_initial_values': ['0']*len(c.state_rhs),
        'roots': {'b0': b, 'b1': d, 'u0': u, 'u1': v,
                  'density': density, 'potential': potential,
                  'potential_derivative': derivative, 'first_integral': invariant,
                  'first_integral_derivative': invariant_derivative,
                  'density_minus_potential_derivative': residual},
        'alpha': str(alpha), 'beta': str(beta), 'kappa': str(kappa),
        'first_integral_elimination_variable': variable,
        'quotient': tail.poly_rows(quotient), 'remainder': tail.poly_rows(remainder),
        'identity': 'density - Ds(potential) = quotient * first_integral + remainder',
        'first_integral_is_zero_by_actual_RHS_and_initial_trace': True,
        'all_other_histories_remain_genuine': True,
        'verified_original_DAG_identity_modulo_proved_first_integral': positive,
    }
    raw = canonical(certificate) + b'\n'
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > 5000000:
        raise formal.CompilationBudgetExceeded('complete certificate compressed-byte budget')
    output = args.out.with_name(args.out.stem + '-certificate.json.gz')
    output.parent.mkdir(parents=True, exist_ok=True)
    tmp = output.with_name(output.name + '.tmp')
    tmp.write_bytes(packed)
    tmp.replace(output)
    artifact = {'file': output.name, 'compressed_bytes': len(packed),
                'compressed_sha256': sha256(packed), 'raw_bytes': len(raw),
                'raw_sha256': sha256(raw)}
    progress['certificate'] = artifact
    readable = {
        'model': MODEL, 'input': provenance,
        'alpha': str(alpha), 'beta': str(beta), 'kappa': str(kappa),
        'first_integral': polynomial_record(invariant_polynomial, 350),
        'quotient': polynomial_record(quotient, 350),
        'remainder': polynomial_record(remainder, 350),
        'density_minus_Ds_potential': polynomial_record(residual_polynomial, 350),
        'complete_certificate': artifact,
        'warning': 'A nonzero raw residual can vanish along the proved first integral. A density is not a period.'}
    while len(canonical(readable)) + 1 > 95000:
        reducible = [v for v in readable.values()
                     if isinstance(v, dict) and v.get('readable_terms')]
        if not reducible:
            raise formal.CompilationBudgetExceeded('readable metadata byte budget')
        entry = max(reducible, key=lambda v: len(v['readable_terms']))
        entry['readable_terms'] = entry['readable_terms'][:len(entry['readable_terms'])//2]
        entry['readable_terms_truncated'] = True
    readable_artifact = write_json(args.out.with_name(args.out.stem + '-expressions.json'), readable)
    return {
        'completion': 'complete', 'model': MODEL, 'input': provenance,
        'tail_exponent': m, 'verified_density_power': n+1,
        'candidate_potential': 'alpha*b0^2*b1 + beta*b0*u1 (original completed coefficients)',
        'alpha': str(alpha), 'beta': str(beta), 'kappa': str(kappa),
        'first_integral_derivative': polynomial_record(derivative_polynomial),
        'first_integral_constant_initial_trace': polynomial_record(initial_polynomial),
        'raw_density_minus_potential_derivative': polynomial_record(residual_polynomial),
        'first_integral_quotient': polynomial_record(quotient),
        'remainder_after_proved_first_integral': polynomial_record(remainder),
        'fresh_original_DAG_verification': polynomial_record(fresh_residual),
        'verified_original_DAG_identity_modulo_proved_first_integral': positive,
        'zero_M_and_constant_germs_pay_this_endpoint_coefficient': positive,
        'genuine_history_count': len(c.state_rhs),
        'original_coefficient_DAG_nodes': len(structure['coefficient_DAG']),
        'extended_coefficient_DAG_nodes': len(c.nodes),
        'forcing_recompiled': False, 'geometric_path_evaluated': False,
        'all_histories_set_to_zero_interior': False,
        'universal_fourth_sign_proved': False, 'new_zero_cost_loop_proved': False,
        'higher_tail_orders_paid': False,
        'negative_scope': 'Failure rejects only this specified identity or declared budgets, not other endpoint potentials.',
        'artifacts': [artifact, readable_artifact], 'source_hashes': source_hashes(),
        'elapsed_seconds': time.monotonic()-started,
        'peak_rss_mib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
    }


def developer_check():
    """A small artificial triangular ODE; no real tail structure is read."""
    budget = formal.Budget(max_nodes=5000, max_atoms=1, max_terms=1000, max_seconds=20)
    c = tail.TailCoefficients(budget)
    G, P, Q0, H = [c.geometry(v) for v in ('toy_G', 'toy_P', 'toy_Q', 'toy_H')]
    b = c.state(G, (2, 'toy-b', 1, 2))
    d = c.state(P, (2, 'toy-d', 2, 2))
    u = c.state(c.multiply(c.constant(-2), b, G), (3, 'toy-u', 3, 3))
    v = c.state(Q0, (3, 'toy-v', 4, 3))
    invariant = c.add(u, c.power(b, 2))
    potential = c.linear([(2, c.multiply(c.power(b, 2), d)), (3, c.multiply(b, v))])
    density = c.add(c.derivative(potential), c.multiply(invariant, H))
    serialized = {'coefficient_DAG': json.loads(canonical(c.nodes)),
                  'state_rhs': c.state_rhs, 'state_labels': c.state_labels,
                  'state_initial_values': ['0']*len(c.state_rhs)}
    restored = load_coefficients(serialized, budget)
    N = tail.LaurentNormalizer(restored, max_terms=1000, max_cache_terms=20000)
    inv = N.node(invariant)
    diff = N.add((1, N.node(density)), (-1, N.node(restored.derivative(potential))))
    quotient, remainder = divide_by_monic_history(N, diff, inv, 'state_2')
    wrong_q, wrong_r = divide_by_monic_history(N, N.add((1, diff), (1, {(): Q(1)})),
                                               inv, 'state_2')
    rejected = False
    malformed = json.loads(canonical(serialized))
    malformed['state_initial_values'][0] = '1'
    try:
        load_coefficients(malformed, budget)
    except ValueError:
        rejected = True
    checks = {
        'original_node_ids_and_state_RHS_rehydrated': restored.nodes[:len(c.nodes)] == c.nodes,
        'actual_artificial_first_integral_derivative_zero': not N.node(restored.derivative(invariant)),
        'constant_zero_initial_trace_checked': not constant_initial_trace(inv),
        'nonzero_raw_residual_not_hidden': bool(diff),
        'proved_first_integral_division_exact': not remainder and quotient == N.node(H),
        'wrong_density_keeps_nonzero_remainder': wrong_r == {(): Q(1)},
        'nonzero_initial_history_rejected': rejected,
        'tail_endpoint_is_s_constant': restored.derivative(restored.geometry('tail_end')) == restored.zero,
    }
    result = {'mode': 'artificial-development-only', 'passed': all(checks.values()),
              'checks': checks, 'research_structure_loaded': False,
              'forcing_compiled': False, 'source_hashes': source_hashes()}
    json.loads(canonical(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--structure', type=Path)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--max-seconds', type=float, default=240)
    parser.add_argument('--max-nodes', type=int, default=200000)
    parser.add_argument('--max-terms', type=int, default=100000)
    parser.add_argument('--max-cache-terms', type=int, default=2000000)
    parser.add_argument('--max-rss-mib', type=float, default=1600)
    args = parser.parse_args()
    if args.check_only:
        report = developer_check()
        write_json(args.out, report)
        print(json.dumps({'mode': report['mode'], 'passed': report['passed']}), flush=True)
        return 0 if report['passed'] else 2
    started = time.monotonic()
    progress = {}
    try:
        report = verify(args, progress)
        code = 0 if report['verified_original_DAG_identity_modulo_proved_first_integral'] else 2
    except Exception as exc:
        report = {'completion': 'budget-exhausted' if isinstance(exc, formal.CompilationBudgetExceeded) else 'error',
                  'model': MODEL, 'exception_type': type(exc).__name__, 'error': str(exc),
                  'input': progress.get('input'), 'stage': progress.get('stage'),
                  'preserved_certificate': progress.get('certificate'),
                  'source_hashes': source_hashes(), 'elapsed_seconds': time.monotonic()-started,
                  'verified_original_DAG_identity_modulo_proved_first_integral': False,
                  'no_missing_coefficient_interpreted_as_zero': True}
        code = 2
    write_json(args.out, report)
    print(json.dumps({'completion': report['completion'],
                      'verified': report['verified_original_DAG_identity_modulo_proved_first_integral'],
                      'elapsed_seconds': report['elapsed_seconds']}), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
