#!/usr/bin/env python3
"""Consume the published m=8 D25 action, preserving its full local remainder.

The candidate short coefficient identities are all checked against the
published coefficients.  Genuine Ds, the original first integral, and a
fresh original-DAG replay are retained.  The highest two powers of the tail
endpoint use true coefficient primitives, not independent formal histories.
Research execution is restricted to the public repository GitHub Actions.
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

import literature_pure_tail_next_reduce as previous
import literature_pure_tail_subleading_verify as prior
import literature_pure_tail_period as tail
import literature_range_profile_algebra as formal


MODEL = 'published-m8-D25-action-endpoint-compression-v1'
SCRIPT = Path(__file__).resolve()
canonical, sha256, write_json = tail.canonical, tail.sha256, tail.write_json
A = Q(3136, 13)
X = Q(-2304, 13)
Y = Q(-608, 13)
GJ = Q(589589, 900)
GD = Q(491959, 5760)
TJ = Q(1520519, 225)
TD = Q(2923193, 7200)
PJ = Q(217217, 1350)
PD = Q(-8281, 43200)
SCALE = A*A*Q(169, 480)
COORDINATES = previous.COORDINATES


def source_hashes():
    paths = (SCRIPT, Path(previous.__file__).resolve(), Path(prior.__file__).resolve(),
             Path(tail.__file__).resolve(), Path(formal.__file__).resolve())
    return {p.name: sha256(p.read_bytes()) for p in paths}


def polynomial(rows):
    result = {}
    for row in rows:
        monomial = tuple((name, exponent) for name, exponent in row['monomial'])
        if (tuple(sorted(monomial)) != monomial or len(dict(monomial)) != len(monomial)
                or any(type(n) is not int or not n for _, n in monomial)):
            raise ValueError('noncanonical polynomial monomial')
        value = Q(row['coefficient'])
        if not value or monomial in result:
            raise ValueError('zero or repeated polynomial term')
        result[monomial] = value
    return result


def polynomial_root(c, value, coordinates=None):
    coordinates = {} if coordinates is None else coordinates
    terms = []
    for monomial, coefficient in value.items():
        factors = []
        for name, exponent in monomial:
            if name in coordinates:
                node = coordinates[name]
            elif name.startswith('state_'):
                index = int(name[6:])
                if not 0 <= index < len(c.state_rhs):
                    raise ValueError('unknown history in polynomial')
                node = c.intern(('st', index))
            else:
                base, order = name.rsplit('_', 1)
                node = c.geometry(base, int(order))
            factors.append(c.power(node, exponent))
        terms.append((coefficient, c.multiply(*factors)))
    return c.linear(terms)


class EndpointDerivative:
    """Partial c derivative only for local geometry; history jets are not guessed."""
    def __init__(self, c):
        self.c = c
        self.cache = {}

    def __call__(self, root):
        if root in self.cache:
            return self.cache[root]
        c, node = self.c, self.c.nodes[root]
        tag = node[0]
        if tag == 'c':
            value = c.zero
        elif tag == 'g':
            value = c.one if node == ('g', 'tail_end', 0) else c.zero
        elif tag == 'st':
            raise ValueError('c derivatives of genuine histories require their coefficient ODEs')
        elif tag == 'add':
            value = c.linear((Q(n, d), self(child)) for child, n, d in node[1])
        elif tag == 'mul':
            terms = []
            for j, (child, power) in enumerate(node[3]):
                derivative = self(child)
                if derivative == c.zero:
                    continue
                factors = list(node[3])
                factors[j] = (child, power-1)
                terms.append((Q(node[1], node[2])*power,
                              c.multiply(c.multiply_powers(factors), derivative)))
            value = c.linear(terms)
        else:
            raise ValueError('unsupported coefficient node')
        self.cache[root] = value
        return value


def parameter_coefficients(value):
    result = {}
    for monomial, coefficient in value.items():
        power = dict(monomial).get('tail_end_0', 0)
        if power < 0:
            raise ValueError('tail endpoint is not a polynomial parameter')
        kept = tuple((v, n) for v, n in monomial if v != 'tail_end_0')
        bucket = result.setdefault(power, {})
        bucket[kept] = bucket.get(kept, Q(0))+coefficient
        if not bucket[kept]:
            del bucket[kept]
    return {power: poly for power, poly in result.items() if poly}


def check_record(value):
    return prior.polynomial_record(value)


def local_geometry(c):
    g = previous.geometry(c)
    dc = EndpointDerivative(c)
    g.update({'Cc': dc(g['C']), 'Dc': dc(g['D']), 'fss': c.derivative(g['fs']),
              'h': c.geometry('h'), 'k': c.geometry('k')})
    g['Ccc'] = dc(g['Cc'])
    return g


def coefficient_candidates(c, g):
    C, D, Cc, Ccc, Dc, fs, fss = (g[k] for k in ('C', 'D', 'Cc', 'Ccc', 'Dc', 'fs', 'fss'))
    return {
        (('J', 1),): c.multiply(c.constant(A*GJ), fs, C),
        (('d1', 1),): c.multiply(c.constant(A*GD), fs, C),
        (('J', 1), ('d1', 1)): c.multiply(c.constant(TJ), C),
        (('d1', 2),): c.multiply(c.constant(TD), C),
        (('J', 1), ('b0', 1)): c.linear([(Q(-6485479, 1350), Cc),
                                         (Q(-1334333, 1350), D), (GJ, fss)]),
        (('b0', 1), ('d1', 1)): c.linear([(Q(-5156021, 8640), Cc),
                                          (Q(-5607251, 43200), D), (GD, fss)]),
        (('b0', 2),): c.multiply(c.constant(Q(169, 480)),
            c.linear([(1, Ccc), (-5, Dc), (Q(17, 20), c.multiply(g['K'], g['h']))])),
    }


def extra_potential(c, coordinates, g):
    b, d, j = [coordinates[k] for k in ('b0', 'd1', 'J')]
    smooth = c.multiply(g['fs'], b, c.linear([(GJ, j), (GD, d)]))
    cubic = c.multiply(c.constant(1/A), b,
                       c.linear([(TJ, c.multiply(j, d)), (TD, c.power(d, 2))]))
    return c.add(smooth, cubic), smooth, cubic


def compact_candidates(c, g, old_groups):
    E = c.linear([(X, g['Cc']), (Y, g['D'])])
    linear = c.linear([(1, polynomial_root(c, old_groups.get((('b0', 1),), {}))),
                       (-1, c.multiply(g['fs'], c.linear([(GJ, g['D']), (GD, E)])))])
    common = c.linear([(1, g['Cc']), (2, g['D'])])
    return {
        (): polynomial_root(c, old_groups.get((), {})),
        (('b0', 1),): linear,
        (('b0', 2),): coefficient_candidates(c, g)[(('b0', 2),)],
        (('J', 1), ('b0', 1)): c.multiply(c.constant(PJ), common),
        (('b0', 1), ('d1', 1)): c.multiply(c.constant(PD), common),
    }


def assemble_groups(c, groups, coordinates):
    return c.add(*(c.multiply(root, *(c.power(coordinates[v], n) for v, n in monomial))
                   for monomial, root in groups.items()))


def leading_endpoint_checks(c, N, g):
    """Only the highest two parameter coefficients need three new primitives."""
    cp, dp = parameter_coefficients(N.node(g['C'])), parameter_coefficients(N.node(g['D']))
    if max(cp, default=-1) > 4 or max(dp, default=-1) > 3:
        raise ValueError('unexpected local parameter degree')
    C4, C3, D3, D2 = [polynomial_root(c, row) for row in
                       (cp.get(4, {}), cp.get(3, {}), dp.get(3, {}), dp.get(2, {}))]
    B4 = c.state(C4, ('parameter-coefficient', 'B4_s=C4', 'zero-initial', 'zero-end-if-M=0'))
    B3 = c.state(C3, ('parameter-coefficient', 'B3_s=C3', 'zero-initial', 'zero-end-if-M=0'))
    J2 = c.state(D2, ('parameter-coefficient', 'J2_s=D2', 'zero-initial', 'zero-end-if-M=0'))
    z = c.geometry('tail_end')
    B = c.add(c.multiply(B4, c.power(z, 4)), c.multiply(B3, c.power(z, 3)))
    Bc = c.linear([(4, c.multiply(B4, c.power(z, 3))),
                   (3, c.multiply(B3, c.power(z, 2)))])
    J = c.linear([(2, c.multiply(B4, c.power(z, 3))),
                  (1, c.multiply(J2, c.power(z, 2)))])
    high_quadratic = c.multiply(c.constant(SCALE), c.add(
        c.multiply(c.power(B, 2), c.linear([(1, g['Ccc']), (-5, g['Dc']),
                            (Q(17, 20), c.multiply(g['K'], g['h']))])),
        c.multiply(c.constant(Q(2, 5)), B, c.linear([(1, Bc), (5, J)]),
                   c.linear([(1, g['Cc']), (2, g['D'])]))))
    high = parameter_coefficients(N.node(high_quadratic))
    F10 = c.multiply(c.constant(SCALE*Q(56, 5)), c.power(B4, 3))
    F9 = c.multiply(c.constant(SCALE), c.power(B4, 2),
                     c.linear([(16, B3), (8, J2)]))
    kh = c.multiply(g['k'], g['h']) if 'k' in g else c.multiply(c.constant(8), C4)
    kh_coeff = parameter_coefficients(N.node(c.multiply(g['K'], g['h'])))
    differences = {
        'C4_equals_kh_over_8': N.add((1, N.node(C4)), (-Q(1, 8), N.node(kh))),
        'D3_equals_2_C4': N.add((1, N.node(D3)), (-2, N.node(C4))),
        'Kh_linear_equals_8_D2_minus_C3': N.add((1, kh_coeff.get(1, {})),
                                                    (-8, N.node(D2)), (8, N.node(C3))),
        'c10_is_the_declared_true_endpoint_derivative':
            N.add((1, high.get(10, {})), (-1, N.node(c.derivative(F10)))),
        'c9_is_the_declared_true_endpoint_derivative':
            N.add((1, high.get(9, {})), (-1, N.node(c.derivative(F9)))),
        'c10_endpoint_zero_when_B4_zero': previous.substitute(
            N, N.node(F10), {previous.state_variable(c, B4): {}}),
        'c9_endpoint_zero_when_B4_zero': previous.substitute(
            N, N.node(F9), {previous.state_variable(c, B4): {}}),
    }
    return differences, {'B4': B4, 'B3': B3, 'J2': J2, 'C4': C4, 'C3': C3,
                          'D2': D2, 'c10_potential': F10, 'c9_potential': F9,
                          'highest_two_parameter_terms_quadratic': high_quadratic}


def public_input(args):
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != tail.REPOSITORY):
        raise RuntimeError('research consumption is restricted to the public repository Actions')
    if args.report is None or args.certificate is None:
        raise ValueError('--report and --certificate are required')
    notes = SCRIPT.parent.parent/'notes'
    for path in (args.report, args.certificate):
        if not path.resolve().is_relative_to(notes.resolve()):
            raise ValueError('inputs must be published under the topic notes directory')
    report_raw, packed = args.report.read_bytes(), args.certificate.read_bytes()
    if len(report_raw) > 100000 or len(packed) > 5000000:
        raise ValueError('published input byte budget')
    report = json.loads(report_raw)
    if (report.get('model') != previous.MODEL or report.get('completion') != 'complete'
            or report.get('tail_exponent') != 8 or report.get('density_power') != 25
            or not report.get('verified_exact_action_identity')
            or not report.get('verified_three_primitive_quadratic_normal_form')):
        raise ValueError('a completed, verified m8 D25 action is required')
    artifact, = [v for v in report['artifacts'] if v['file'] == args.certificate.name]
    if len(packed) != artifact['compressed_bytes'] or sha256(packed) != artifact['compressed_sha256']:
        raise ValueError('published compressed certificate bytes differ')
    raw = gzip.decompress(packed)
    if len(raw) > 10000000 or len(raw) != artifact['raw_bytes'] or sha256(raw) != artifact['raw_sha256']:
        raise ValueError('published decoded certificate bytes differ')
    payload = json.loads(raw)
    if payload.get('model') != previous.MODEL or payload['report']['tail_exponent'] != 8:
        raise ValueError('published certificate identity mismatch')
    sources = source_hashes()
    for name, digest in report['source_hashes'].items():
        if sources.get(name) != digest or payload['source_hashes'].get(name) != digest:
            raise ValueError(f'published source changed: {name}')
    action = polynomial(payload['action_polynomial'])
    if prior.polynomial_record(action) != report['action']:
        raise ValueError('published action polynomial does not match its report')
    return payload, {'report': args.report.name, 'report_bytes': len(report_raw),
                      'report_sha256': sha256(report_raw), 'certificate': args.certificate.name,
                      **{k: artifact[k] for k in ('compressed_bytes', 'compressed_sha256',
                                                  'raw_bytes', 'raw_sha256')},
                      'published_model': report['model'], 'original_input': report['input']}


def compress(payload, args):
    budget = formal.Budget(max_nodes=args.max_nodes, max_atoms=1,
                           max_terms=args.max_terms, max_seconds=args.max_seconds)
    c = prior.load_coefficients(payload, budget)
    N = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                               max_cache_terms=args.max_cache_terms, max_rss_mib=args.max_rss_mib)
    roots = payload['roots']
    coordinates = {'b0': roots['b0'], 'd1': roots['d1_orthogonal'], 'J': roots['J']}
    g = local_geometry(c)
    original = polynomial(payload['action_polynomial'])
    old_groups = previous.coefficient_groups(original)
    comparisons = {}
    expected = coefficient_candidates(c, g)
    for key, node in expected.items():
        comparisons['coefficient:'+repr(key)] = N.add((1, old_groups.get(key, {})), (-1, N.node(node)))
    rhs = {'b0': c.multiply(c.constant(A), g['C']),
           'd1': c.linear([(X, g['Cc']), (Y, g['D'])]), 'J': g['D']}
    for name, node in coordinates.items():
        comparisons['true_ODE:'+name] = N.add((1, N.node(c.derivative(node))), (-1, N.node(rhs[name])))
    qnorm = c.add(c.one, c.power(g['e'], 2))
    compact_curvature = c.linear([(1, g['Ccc']), (-2, g['Dc']),
        (-Q(1, 4), c.multiply(g['k'], qnorm, c.power(g['h'], -1))),
        (Q(1, 4), c.multiply(g['K'], g['h']))])
    comparisons['Ccc_minus_2Dc_identity'] = N.node(compact_curvature)
    extra, smooth, cubic = extra_potential(c, coordinates, g)
    extra_ds = c.derivative(extra)
    replacements = {name: polynomial(rows) for name, rows in
                    payload['raw_second_to_completed_replacements'].items()}
    extra_action = previous.substitute(N, N.node(extra_ds), replacements)
    new_action = N.add((1, original), (-1, extra_action))
    new_groups = previous.coefficient_groups(new_action)
    short = compact_candidates(c, g, old_groups)
    for key in sorted(set(new_groups) | set(short)):
        comparisons['compact_group:'+repr(key)] = N.add(
            (1, new_groups.get(key, {})), (-1, N.node(short.get(key, c.zero))))
    comparisons['extra_potential_constant_endpoint_trace'] = prior.constant_initial_trace(N.node(extra))
    comparisons['genuine_first_integral_derivative'] = N.node(c.derivative(roots['first_integral']))
    comparisons['genuine_first_integral_initial'] = prior.constant_initial_trace(N.node(roots['first_integral']))

    # The highest-c argument uses all local terms: none are silently dropped.
    constant_degree = max(parameter_coefficients(new_groups.get((), {})), default=-1)
    linear_degree = max(parameter_coefficients(new_groups.get((('b0', 1),), {})), default=-1)
    degree_bounds = constant_degree <= 8 and linear_degree <= 4
    high_checks, high_roots = leading_endpoint_checks(c, N, g)
    comparisons.update(high_checks)

    # Fresh original-DAG replay after both old and new endpoint potentials.
    combined = c.add(roots['endpoint_potential'], extra)
    combined_ds = c.derivative(combined)
    fresh = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                                   max_cache_terms=args.max_cache_terms, max_rss_mib=args.max_rss_mib)
    inverse = {name: fresh.node(node) for name, node in coordinates.items()}
    replay = previous.substitute(fresh, new_action, inverse)
    quotient = polynomial(payload['first_integral_quotient'])
    fresh_difference = fresh.add((1, fresh.node(roots['density'])), (-1, fresh.node(combined_ds)),
        (-1, fresh.multiply(quotient, fresh.node(roots['first_integral']))), (-1, replay))
    comparisons['fresh_original_DAG_identity'] = fresh_difference
    compact_root = assemble_groups(c, short, coordinates)
    comparisons['fresh_compact_full_identity'] = fresh.add(
        (1, fresh.node(roots['density'])), (-1, fresh.node(combined_ds)),
        (-1, fresh.multiply(quotient, fresh.node(roots['first_integral']))),
        (-1, fresh.node(compact_root)))
    verified = all(not value for value in comparisons.values()) and degree_bounds
    report = {
        'tail_exponent': 8, 'density_power': 25,
        'verified_all_published_coefficient_identities': all(
            not value for key, value in comparisons.items() if key.startswith('coefficient:')),
        'verified_complete_action_compression': verified,
        'verified_original_DAG_identity': not fresh_difference,
        'verified_period_parameter_degree_at_most_8': verified,
        'constant_local_parameter_degree': constant_degree,
        'linear_b0_parameter_degree': linear_degree,
        'unpaid_local_constant_and_linear_terms_retained': True,
        'new_action': prior.polynomial_record(new_action),
        'new_action_groups': [{'history_monomial': [[v, p] for v, p in key],
                              **prior.polynomial_record(poly)} for key, poly in sorted(new_groups.items())],
        'exact_differences': {key: check_record(value) for key, value in comparisons.items()},
        'source_genuine_histories_retained': len(payload['state_rhs']),
        'declared_parameter_coefficient_histories': len(c.state_rhs)-len(payload['state_rhs']),
        'period_scope': 'm8, genuine zero incoming histories, constant scalar endpoint germs, complete M=0; all c-polynomial coefficient histories use their actual ODEs',
        'degree_bound_is_not_zero_period': True,
        'action_sign_proved': False, 'nonzero_period_proved': False,
        'new_zero_cost_loop_proved': False, 'geometric_path_evaluated': False,
        'forcing_recompiled': False,
    }
    output = {'model': MODEL, 'coefficient_DAG': c.nodes, 'state_rhs': c.state_rhs,
        'state_labels': c.state_labels, 'state_initial_values': ['0']*len(c.state_rhs),
        'roots': {**roots, 'extra_potential': extra, 'smooth_extra_potential': smooth,
                  'cubic_extra_potential': cubic, 'combined_potential': combined,
                  'combined_potential_derivative': combined_ds, 'compact_full_action': compact_root,
                  **high_roots},
        'first_integral_quotient': tail.poly_rows(quotient),
        'new_action_polynomial': tail.poly_rows(new_action),
        'new_action_groups': [{'history_monomial': [[v, p] for v, p in key],
                              'coefficient': tail.poly_rows(poly)} for key, poly in sorted(new_groups.items())],
        'exact_difference_polynomials': {key: tail.poly_rows(value) for key, value in comparisons.items()},
        'identity': 'D25=Ds(original_potential+extra_potential)+original_quotient*I0+new_action',
        'report': report}
    return report, output, new_groups


def run(args, progress):
    started = time.monotonic()
    payload, provenance = public_input(args)
    progress['input'] = provenance
    report, output, groups = compress(payload, args)
    output.update({'input': provenance, 'source_hashes': source_hashes()})
    raw = canonical(output)+b'\n'
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > 5000000:
        raise formal.CompilationBudgetExceeded('compressed complete certificate budget')
    path = args.out.with_name(args.out.stem+'-certificate.json.gz')
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name(path.name+'.tmp')
    pending.write_bytes(packed)
    pending.replace(path)
    artifact = {'file': path.name, 'compressed_bytes': len(packed), 'compressed_sha256': sha256(packed),
                'raw_bytes': len(raw), 'raw_sha256': sha256(raw)}
    progress['certificate'] = artifact
    readable = {'model': MODEL, 'input': provenance, 'complete_certificate': artifact,
        'meaning': 'Complete local remainder is retained; endpoint and degree identities are not a sign certificate.',
        'new_action_groups': [{'history_monomial': [[v, p] for v, p in key],
                              **prior.polynomial_record(value, 450)} for key, value in sorted(groups.items())]}
    while len(canonical(readable))+1 > 95000:
        entries = [entry for entry in readable['new_action_groups'] if entry.get('readable_terms')]
        if not entries:
            raise formal.CompilationBudgetExceeded('readable metadata budget')
        longest = max(entries, key=lambda entry: len(entry['readable_terms']))
        longest['readable_terms'] = longest['readable_terms'][:len(longest['readable_terms'])//2]
        longest['readable_terms_truncated'] = True
    brief = write_json(args.out.with_name(args.out.stem+'-expressions.json'), readable)
    report.update({'model': MODEL, 'completion': 'complete', 'input': provenance,
                   'source_hashes': source_hashes(), 'artifacts': [artifact, brief],
                   'elapsed_seconds': time.monotonic()-started,
                   'peak_rss_mib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024})
    return report


def developer_check():
    """Small artificial polynomials only; no published research input is read."""
    c = tail.TailCoefficients(formal.Budget(max_nodes=10000, max_atoms=1, max_terms=5000, max_seconds=20))
    N = tail.LaurentNormalizer(c, max_terms=5000, max_cache_terms=100000, max_rss_mib=1800)
    h, z, w = c.geometry('h'), c.geometry('tail_end'), c.geometry('omega')
    dc = EndpointDerivative(c)
    trial = c.multiply(c.power(c.add(z, w), 3), c.power(h, -1))
    expected = c.multiply(c.constant(3), c.power(c.add(z, w), 2), c.power(h, -1))
    checks = {'endpoint_partial_matches_local_polynomial':
              not N.add((1, N.node(dc(trial))), (-1, N.node(expected)))}
    coefficients = parameter_coefficients(N.node(trial))
    checks['c_and_omega_not_collapsed'] = (set(coefficients) == {0, 1, 2, 3}
        and coefficients[3] == {(('h_0', -1),): Q(1)})
    state = c.state(c.constant(2), ('artificial', 'zero-initial'))
    try:
        dc(state)
    except ValueError:
        checks['unjustified_history_partial_rejected'] = True
    else:
        checks['unjustified_history_partial_rejected'] = False
    rows = tail.poly_rows(N.node(trial))
    checks['exact_polynomial_roundtrip'] = polynomial(rows) == N.node(trial)
    try:
        polynomial(rows+rows[:1])
    except ValueError:
        checks['duplicate_term_rejected'] = True
    else:
        checks['duplicate_term_rejected'] = False

    # Manufacture only the top coefficient relations, using constant ODEs.
    C = c.linear([(2, c.power(z, 4)), (3, c.power(z, 3)), (7, c.power(z, 2))])
    D = c.linear([(4, c.power(z, 3)), (5, c.power(z, 2)), (11, z)])
    K = c.linear([(16, c.power(z, 2)), (16, z), (19, c.one)])
    toy = {'C': C, 'D': D, 'Cc': dc(C), 'Ccc': dc(dc(C)), 'Dc': dc(D), 'K': K, 'h': c.one}
    differences, _ = leading_endpoint_checks(c, N, toy)
    checks['manufactured_parameter_coefficient_histories'] = all(not v for v in differences.values())
    bad = dict(toy)
    bad['K'] = c.add(K, z)
    rejected, _ = leading_endpoint_checks(c, N, bad)
    checks['wrong_K1_not_silently_dropped'] = bool(rejected['c9_is_the_declared_true_endpoint_derivative'])
    nonzero = N.add((1, N.node(trial)), (-2, N.node(trial)))
    checks['nonzero_difference_retained'] = bool(nonzero)
    result = {'mode': 'artificial-development-only', 'passed': all(checks.values()), 'checks': checks,
              'research_input_loaded': False, 'forcing_compiled': False, 'source_hashes': source_hashes()}
    json.loads(canonical(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--certificate', type=Path)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--max-seconds', type=float, default=240)
    parser.add_argument('--max-nodes', type=int, default=250000)
    parser.add_argument('--max-terms', type=int, default=120000)
    parser.add_argument('--max-cache-terms', type=int, default=2500000)
    parser.add_argument('--max-rss-mib', type=float, default=1800)
    args = parser.parse_args()
    if args.check_only:
        report = developer_check()
        write_json(args.out, report)
        print(json.dumps({'mode': report['mode'], 'passed': report['passed']}), flush=True)
        return 0 if report['passed'] else 2
    started, progress = time.monotonic(), {}
    try:
        report = run(args, progress)
        code = 0 if report['verified_complete_action_compression'] else 2
    except Exception as exc:
        report = {'model': MODEL, 'completion': 'budget-exhausted' if isinstance(exc, formal.CompilationBudgetExceeded) else 'error',
            'exception_type': type(exc).__name__, 'error': str(exc), 'input': progress.get('input'),
            'preserved_certificate': progress.get('certificate'), 'source_hashes': source_hashes(),
            'elapsed_seconds': time.monotonic()-started, 'verified_complete_action_compression': False,
            'no_omitted_coefficient_is_interpreted_as_zero': True, 'action_sign_proved': False,
            'nonzero_period_proved': False, 'new_zero_cost_loop_proved': False}
        code = 2
    write_json(args.out, report)
    print(json.dumps({'completion': report['completion'],
                      'verified_compression': report['verified_complete_action_compression'],
                      'elapsed_seconds': report['elapsed_seconds']}), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
