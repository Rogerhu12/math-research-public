#!/usr/bin/env python3
"""Reduce the genuine c^8 coefficient of the published compressed D25 action.

No forcing or geometric path is evaluated.  The coefficient histories have
their actual ODEs and zero initial values; the original history system and
fresh original-DAG identity are retained.  A short integrated action does
not imply a sign, a nonzero period, or a zero-cost loop.
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

import literature_pure_tail_action_compress as compressed
import literature_pure_tail_next_reduce as previous
import literature_pure_tail_subleading_verify as prior
import literature_pure_tail_period as tail
import literature_range_profile_algebra as formal


MODEL = 'published-m8-D25-c8-true-coefficient-history-action-v1'
SCRIPT = Path(__file__).resolve()
canonical, sha256, write_json = tail.canonical, tail.sha256, tail.write_json
A, X, Y, SCALE = compressed.A, compressed.X, compressed.Y, compressed.SCALE


def source_hashes():
    paths = (SCRIPT, Path(compressed.__file__).resolve(), Path(previous.__file__).resolve(),
             Path(prior.__file__).resolve(), Path(tail.__file__).resolve(), Path(formal.__file__).resolve())
    return {p.name: sha256(p.read_bytes()) for p in paths}


def public_input(args):
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != tail.REPOSITORY):
        raise RuntimeError('research consumption is restricted to the public repository Actions')
    if args.report is None or args.certificate is None:
        raise ValueError('--report and --certificate are required')
    notes = SCRIPT.parent.parent/'notes'
    for path in (args.report, args.certificate):
        if not path.resolve().is_relative_to(notes.resolve()):
            raise ValueError('input must be published under the topic notes directory')
    report_raw, packed = args.report.read_bytes(), args.certificate.read_bytes()
    if len(report_raw) > 100000 or len(packed) > 5000000:
        raise ValueError('published input byte budget')
    report = json.loads(report_raw)
    if (report.get('model') != compressed.MODEL or report.get('completion') != 'complete'
            or report.get('tail_exponent') != 8 or report.get('density_power') != 25
            or not report.get('verified_complete_action_compression')
            or not report.get('verified_period_parameter_degree_at_most_8')):
        raise ValueError('the completed verified m8 compressed action is required')
    artifact, = [v for v in report['artifacts'] if v['file'] == args.certificate.name]
    if len(packed) != artifact['compressed_bytes'] or sha256(packed) != artifact['compressed_sha256']:
        raise ValueError('compressed certificate bytes differ')
    raw = gzip.decompress(packed)
    if len(raw) > 10000000 or len(raw) != artifact['raw_bytes'] or sha256(raw) != artifact['raw_sha256']:
        raise ValueError('decoded certificate bytes differ')
    payload = json.loads(raw)
    if payload.get('model') != compressed.MODEL or payload['report']['tail_exponent'] != 8:
        raise ValueError('certificate model/exponent differs')
    current = source_hashes()
    for name, digest in report['source_hashes'].items():
        if current.get(name) != digest or payload['source_hashes'].get(name) != digest:
            raise ValueError(f'published imported source changed: {name}')
    action = compressed.polynomial(payload['new_action_polynomial'])
    if prior.polynomial_record(action) != report['new_action']:
        raise ValueError('published compressed action polynomial differs from its report')
    return payload, {'report': args.report.name, 'report_bytes': len(report_raw),
        'report_sha256': sha256(report_raw), 'certificate': args.certificate.name,
        **{k: artifact[k] for k in ('compressed_bytes', 'compressed_sha256', 'raw_bytes', 'raw_sha256')},
        'published_model': report['model'], 'original_input': report['input']}


def short_roots(c, B, J, eta, k_over_h, G):
    """The proposed c8 endpoint potential and short density, with genuine Ds."""
    p, B3, B2, J2, J1 = B[4], B[3], B[2], J[2], J[1]
    etas = c.derivative(eta)
    ell = c.linear([(1, B3), (-Q(1, 2), J2), (-1, c.multiply(eta, p))])
    zeta = c.linear([(1, B3), (-4, c.multiply(eta, p))])
    potential = c.linear([
        (Q(72, 5), c.multiply(c.power(p, 2), B2)),
        (8, c.multiply(c.power(p, 2), J1)),
        (-Q(8, 5), c.multiply(p, c.power(B3, 2))),
        (16, c.multiply(p, B3, J2)),
        (-Q(56, 5), c.multiply(c.power(eta, 2), c.power(p, 3))),
        (Q(8, 5), c.multiply(eta, c.power(p, 2), c.linear([(11, B3), (-5, J2)]))),
        (Q(1, 4), c.multiply(c.power(p, 2), etas)),
        (-Q(1, 20), p),
    ])
    short = c.linear([
        (Q(2, 5), c.multiply(p, c.linear([(1, zeta), (10, ell)]), c.derivative(zeta))),
        (-Q(2, 5), c.multiply(k_over_h, c.power(p, 2))),
        (-Q(1, 20), c.multiply(c.derivative(p), c.derivative(zeta))),
        (-Q(1, 5), c.multiply(c.derivative(p), c.derivative(ell))),
    ])
    return {'Phi8': potential, 'short_density': short, 'p': p, 'ell': ell, 'zeta': zeta,
            'eta': eta, 'eta_s': etas, 'G': G,
            'ell_rhs': c.multiply(c.constant(-1), etas, p),
            'zeta_rhs': c.linear([(Q(1, 8), G), (-4, c.multiply(etas, p))])}


def coefficient_history_family(c, N, g, roots):
    """Complete finite parameter family, justified by ODE/initial uniqueness."""
    cp = compressed.parameter_coefficients(N.node(g['C']))
    dp = compressed.parameter_coefficients(N.node(g['D']))
    if max(cp, default=-1) > 4 or max(dp, default=-1) > 3:
        raise ValueError('unexpected geometry parameter degrees')
    C = {j: compressed.polynomial_root(c, cp.get(j, {})) for j in range(5)}
    D = {j: compressed.polynomial_root(c, dp.get(j, {})) for j in range(4)}
    B = {4: roots['B4'], 3: roots['B3']}
    J = {2: roots['J2']}
    for j in range(3):
        B[j] = c.state(C[j], ('parameter-coefficient', f'B{j}_s=C{j}',
                              'zero-initial', 'zero-end-if-complete-M=0'))
    for j in range(2):
        J[j] = c.state(D[j], ('parameter-coefficient', f'J{j}_s=D{j}',
                              'zero-initial', 'zero-end-if-complete-M=0'))
    J[3] = c.multiply(c.constant(2), B[4])
    parameter = c.geometry('tail_end')
    Bpoly = c.add(*(c.multiply(B[j], c.power(parameter, j)) for j in range(5)))
    Bcpoly = c.add(*(c.multiply(c.constant(j), B[j], c.power(parameter, j-1)) for j in range(1, 5)))
    Jpoly = c.add(*(c.multiply(J[j], c.power(parameter, j)) for j in range(4)))
    family = {'b0': c.multiply(c.constant(A), Bpoly),
              'd1': c.linear([(X, Bcpoly), (Y, Jpoly)]), 'J': Jpoly}
    differences = {}
    for j in range(5):
        differences[f'coefficient_B{j}_actual_ODE'] = N.add((1, N.node(c.derivative(B[j]))), (-1, N.node(C[j])))
    for j in range(4):
        differences[f'coefficient_J{j}_actual_ODE'] = N.add((1, N.node(c.derivative(J[j]))), (-1, N.node(D[j])))
    rhs = {'b0': c.multiply(c.constant(A), g['C']),
           'd1': c.linear([(X, g['Cc']), (Y, g['D'])]), 'J': g['D']}
    original = {'b0': roots['b0'], 'd1': roots['d1_orthogonal'], 'J': roots['J']}
    for name, node in family.items():
        differences[f'parameter_family_{name}_same_ODE'] = N.add(
            (1, N.node(c.derivative(node))), (-1, N.node(rhs[name])))
        differences[f'original_{name}_same_ODE'] = N.add(
            (1, N.node(c.derivative(original[name]))), (-1, N.node(rhs[name])))
        differences[f'parameter_family_{name}_zero_initial'] = prior.constant_initial_trace(N.node(node))
        differences[f'original_{name}_zero_initial'] = prior.constant_initial_trace(N.node(original[name]))
    return B, J, C, D, family, differences


def history_coordinate_groups(value, names=('p', 'ell', 'zeta')):
    result = {}
    for monomial, coefficient in value.items():
        history = tuple((v, n) for v, n in monomial if v in names)
        local = tuple((v, n) for v, n in monomial if v not in names)
        bucket = result.setdefault(history, {})
        bucket[local] = bucket.get(local, Q(0))+coefficient
        if not bucket[local]:
            del bucket[local]
    return {key: poly for key, poly in result.items() if poly}


def reduce_action(payload, args):
    budget = formal.Budget(max_nodes=args.max_nodes, max_atoms=1,
                           max_terms=args.max_terms, max_seconds=args.max_seconds)
    c = prior.load_coefficients(payload, budget)
    N = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                               max_cache_terms=args.max_cache_terms, max_rss_mib=args.max_rss_mib)
    roots = payload['roots']
    g = compressed.local_geometry(c)
    action = compressed.polynomial(payload['new_action_polynomial'])
    groups = previous.coefficient_groups(action)
    B, J, Cj, Dj, family, differences = coefficient_history_family(c, N, g, roots)
    family_poly = {key: N.node(node) for key, node in family.items()}
    parameter_action = previous.substitute(N, action, family_poly)
    parameter_coefficients = compressed.parameter_coefficients(parameter_action)
    a8 = N.add((1/SCALE, parameter_coefficients.get(8, {})))
    a8root = compressed.polynomial_root(c, a8)
    h, k = g['h'], g['k']
    rho = c.multiply(c.geometry('h', 1), c.power(h, -1))
    ell_h = c.derivative(c.multiply(c.geometry('h', 1), c.power(h, -2)))
    eta = c.linear([(1, c.geometry('omega')), (-1, c.multiply(k, c.power(h, -1)))])
    G = c.linear([(1, c.power(k, 2)), (-1, c.one), (1, c.multiply(h, ell_h))])
    k_over_h = c.multiply(k, c.power(h, -1))
    short = short_roots(c, B, J, eta, k_over_h, G)

    # Two small, directly visible coefficient groups are independently tied.
    const8 = compressed.parameter_coefficients(groups.get((), {})).get(8, {})
    linear4 = compressed.parameter_coefficients(groups.get((('b0', 1),), {})).get(4, {})
    const_expected = c.multiply(c.constant(-Q(2401, 150)), h, k, c.add(G, c.constant(8)))
    linear_expected = c.multiply(c.constant(-Q(1911, 400)), k,
        c.linear([(1, c.geometry('k', 1)), (-2, c.multiply(k, c.geometry('h', 1), c.power(h, -1)))]))
    differences['published_local_constant_c8'] = N.add((1, const8), (-1, N.node(const_expected)))
    differences['published_linear_b0_c4'] = N.add((1, linear4), (-1, N.node(linear_expected)))
    parameter = c.geometry('tail_end')
    moving_parameter = c.add(parameter, eta)
    Kh_short = c.linear([(1, c.multiply(h, k, c.power(moving_parameter, 2))),
                         (1, c.multiply(G, moving_parameter)),
                         (1, c.derivative(c.derivative(eta))), (-1, k_over_h)])
    differences['Kh_in_moving_parameter'] = N.add(
        (1, N.node(c.multiply(h, g['K']))), (-1, N.node(Kh_short)))
    for name in ('ell', 'zeta'):
        differences[f'short_{name}_actual_ODE'] = N.add(
            (1, N.node(c.derivative(short[name]))), (-1, N.node(short[name+'_rhs'])))
    potential_ds = c.derivative(short['Phi8'])
    differences['c8_exact_endpoint_potential_and_short_action'] = N.add(
        (1, a8), (-1, N.node(potential_ds)), (-1, N.node(short['short_density'])))
    pvar = previous.state_variable(c, B[4])
    differences['c8_potential_zero_when_B4_zero'] = previous.substitute(
        N, N.node(short['Phi8']), {pvar: {}})

    # R97 is used as an endpoint identity, not as a pointwise constraint.
    u = c.multiply(c.constant(8), B[4], c.power(h, -1))
    square_primitive = c.linear([(8, short['zeta']), (-1, rho), (-2, c.multiply(u, k))])
    square_rhs = c.linear([(1, c.multiply(c.linear([(1, c.power(u, 2)), (-1, c.one)]), c.power(rho, 2))),
                           (-1, c.power(c.add(k, c.multiply(u, rho)), 2)), (-1, c.one)])
    correlation_primitive = c.linear([(8, short['ell']), (-Q(1, 2), c.multiply(u, k))])
    correlation_rhs = c.multiply(c.constant(-Q(1, 2)), k, c.add(k, c.multiply(u, rho)))
    differences['R97_square_is_true_primitive_derivative'] = N.add(
        (1, N.node(c.derivative(square_primitive))), (-1, N.node(square_rhs)))
    differences['R97_correlation_is_true_primitive_derivative'] = N.add(
        (1, N.node(c.derivative(correlation_primitive))), (-1, N.node(correlation_rhs)))

    # Tie the input to the original unchanged D25 DAG once more.
    original_coordinates = {'b0': roots['b0'], 'd1': roots['d1_orthogonal'], 'J': roots['J']}
    fresh = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                                   max_cache_terms=args.max_cache_terms, max_rss_mib=args.max_rss_mib)
    original_action_root = compressed.polynomial_root(c, action, original_coordinates)
    quotient = compressed.polynomial(payload['first_integral_quotient'])
    differences['fresh_original_DAG_input_identity'] = fresh.add(
        (1, fresh.node(roots['density'])), (-1, fresh.node(roots['combined_potential_derivative'])),
        (-1, fresh.multiply(quotient, fresh.node(roots['first_integral']))),
        (-1, fresh.node(original_action_root)))
    fresh_family_root = compressed.polynomial_root(c, action, family)
    fresh_c8 = compressed.parameter_coefficients(fresh.node(fresh_family_root)).get(8, {})
    differences['fresh_parameter_family_c8_identity'] = fresh.add(
        (1/SCALE, fresh_c8), (-1, fresh.node(potential_ds)), (-1, fresh.node(short['short_density'])))
    differences['fresh_parameter_family_replay'] = fresh.add((1, fresh.node(fresh_family_root)), (-1, parameter_action))

    # A readable three-history expression; all geometry-dependent change
    # of variables is also exactly reversed, without resetting histories.
    ppoly, lpoly, zpoly = ({((name, 1),): Q(1)} for name in ('p', 'ell', 'zeta'))
    etapoly = N.node(eta)
    B3poly = N.add((1, zpoly), (4, N.multiply(etapoly, ppoly)))
    J2poly = N.add((2, zpoly), (6, N.multiply(etapoly, ppoly)), (-2, lpoly))
    substitution = {pvar: ppoly,
                    previous.state_variable(c, B[3]): B3poly,
                    previous.state_variable(c, J[2]): J2poly}
    short_coordinates = previous.substitute(N, N.node(short['short_density']), substitution)
    remaining_states = previous.state_names(short_coordinates)
    inverse = {'p': N.node(B[4]), 'ell': N.node(short['ell']), 'zeta': N.node(short['zeta'])}
    differences['short_history_coordinate_replay'] = N.add(
        (1, previous.substitute(N, short_coordinates, inverse)), (-1, N.node(short['short_density'])))
    short_groups = history_coordinate_groups(short_coordinates)
    verified = not remaining_states and all(not value for value in differences.values())
    report = {'tail_exponent': 8, 'density_power': 25, 'tail_endpoint_parameter_power': 8,
        'verified_exact_c8_action_reduction': verified,
        'genuine_source_histories_retained': len(payload['state_rhs']),
        'new_coefficient_histories_added': len(c.state_rhs)-len(payload['state_rhs']),
        'parameter_family_degree': max(parameter_coefficients, default=-1),
        'unscaled_c8_terms': len(parameter_coefficients.get(8, {})),
        'normalized_c8': prior.polynomial_record(a8),
        'short_action': prior.polynomial_record(short_coordinates),
        'short_action_groups': [{'history_monomial': [[v, p] for v, p in key],
                                **prior.polynomial_record(value)} for key, value in sorted(short_groups.items())],
        'unexpected_retained_histories': remaining_states,
        'exact_differences': {name: prior.polynomial_record(value) for name, value in differences.items()},
        'normalization': str(SCALE),
        'actual_history_definitions': {'p': 'B4; p_s=kh/8',
            'ell': 'B3-J2/2-eta*p; ell_s=-eta_s*p',
            'zeta': 'B3-4*eta*p; zeta_s=(k^2-1+h*(h_s/h^2)_s)/8-4*eta_s*p',
            'eta': 'omega-k/h, with the genuine omega_s=k_s/(2h)'},
        'period_scope': 'm8 D25 c8 coefficient; complete M=0, genuine zero incoming histories, constant scalar endpoint germs; no T=0 assumed',
        'R97_used_only_as_true_endpoint_identities': True,
        'action_sign_proved': False, 'nonzero_period_proved': False,
        'new_zero_cost_loop_proved': False, 'forcing_recompiled': False, 'geometric_path_evaluated': False}
    output = {'model': MODEL, 'coefficient_DAG': c.nodes, 'state_rhs': c.state_rhs,
        'state_labels': c.state_labels, 'state_initial_values': ['0']*len(c.state_rhs),
        'roots': {**roots, **{f'coefficient_B{j}': node for j, node in B.items()},
                  **{f'coefficient_J{j}': node for j, node in J.items()},
                  **{f'parameter_family_{key}': node for key, node in family.items()},
                  **{f'c8_{key}': node for key, node in short.items()},
                  'c8_normalized_original': a8root, 'c8_potential_derivative': potential_ds,
                  'R97_square_primitive': square_primitive, 'R97_square_rhs': square_rhs,
                  'R97_correlation_primitive': correlation_primitive,
                  'R97_correlation_rhs': correlation_rhs},
        'parameter_action_polynomial': tail.poly_rows(parameter_action),
        'normalized_c8_polynomial': tail.poly_rows(a8),
        'short_action_polynomial': tail.poly_rows(short_coordinates),
        'short_action_groups': [{'history_monomial': [[v, p] for v, p in key],
                                'coefficient': tail.poly_rows(value)} for key, value in sorted(short_groups.items())],
        'exact_difference_polynomials': {key: tail.poly_rows(value) for key, value in differences.items()},
        'identity': '[c^8](compressed D25 action)=SCALE*(Ds(Phi8)+short_action(p,ell,zeta))',
        'report': report}
    return report, output, short_groups


def run(args, progress):
    started = time.monotonic()
    payload, provenance = public_input(args)
    progress['input'] = provenance
    report, output, groups = reduce_action(payload, args)
    output.update({'input': provenance, 'source_hashes': source_hashes()})
    raw = canonical(output)+b'\n'
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > 5000000:
        raise formal.CompilationBudgetExceeded('complete certificate byte budget')
    path = args.out.with_name(args.out.stem+'-certificate.json.gz')
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name(path.name+'.tmp')
    pending.write_bytes(packed)
    pending.replace(path)
    artifact = {'file': path.name, 'compressed_bytes': len(packed), 'compressed_sha256': sha256(packed),
                'raw_bytes': len(raw), 'raw_sha256': sha256(raw)}
    progress['certificate'] = artifact
    readable = {'model': MODEL, 'input': provenance, 'complete_certificate': artifact,
        'meaning': 'True zero-end history action; no sign or period-nonvanishing assertion.',
        'history_definitions': report['actual_history_definitions'],
        'short_action_groups': [{'history_monomial': [[v, p] for v, p in key],
                                **prior.polynomial_record(value, 450)} for key, value in sorted(groups.items())]}
    while len(canonical(readable))+1 > 95000:
        entries = [entry for entry in readable['short_action_groups'] if entry.get('readable_terms')]
        if not entries:
            raise formal.CompilationBudgetExceeded('readable coefficient byte budget')
        entry = max(entries, key=lambda value: len(value['readable_terms']))
        entry['readable_terms'] = entry['readable_terms'][:len(entry['readable_terms'])//2]
        entry['readable_terms_truncated'] = True
    brief = write_json(args.out.with_name(args.out.stem+'-expressions.json'), readable)
    report.update({'model': MODEL, 'completion': 'complete', 'input': provenance,
        'source_hashes': source_hashes(), 'artifacts': [artifact, brief],
        'elapsed_seconds': time.monotonic()-started,
        'peak_rss_mib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024})
    return report


def developer_check():
    """Small manufactured coefficient path; no actual research input is read."""
    c = tail.TailCoefficients(formal.Budget(max_nodes=15000, max_atoms=1, max_terms=10000, max_seconds=20))
    N = tail.LaurentNormalizer(c, max_terms=10000, max_cache_terms=150000, max_rss_mib=1800)
    s = c.state(c.one, ('artificial-clock', 's_s=1', 'zero-initial'))
    C4 = c.constant(2)
    C3 = c.linear([(8, s), (3, c.one)])
    C2 = c.linear([(12, c.power(s, 2)), (9, s)])
    D2 = c.linear([(12, s), (6, c.one)])
    D1 = c.linear([(12, c.power(s, 2)), (12, s), (-Q(5, 4), c.one)])
    B = {4: c.state(C4, ('artificial-B4',)), 3: c.state(C3, ('artificial-B3',)),
         2: c.state(C2, ('artificial-B2',))}
    J = {2: c.state(D2, ('artificial-J2',)), 1: c.state(D1, ('artificial-J1',))}
    eta, G, kh = s, c.constant(24), c.constant(5)
    short = short_roots(c, B, J, eta, kh, G)
    p, b3, b2, j2, j1 = B[4], B[3], B[2], J[2], J[1]
    K0 = c.linear([(16, c.power(s, 2)), (24, s), (-5, c.one)])
    P0 = c.linear([(2, C2), (-5, D1), (Q(17, 20), K0)])
    P1 = c.linear([(-Q(4, 5), C3), (-Q(16, 5), D2)])
    P2 = c.multiply(c.constant(-Q(56, 5)), C4)
    S1 = c.linear([(2, C2), (2, D1)])
    S2 = c.linear([(3, C3), (2, D2)])
    S3 = c.multiply(c.constant(8), C4)
    expanded = c.add(
        c.multiply(c.power(p, 2), P0), c.multiply(c.constant(2), p, b3, P1),
        c.multiply(c.linear([(2, c.multiply(p, b2)), (1, c.power(b3, 2))]), P2),
        c.multiply(c.constant(Q(2, 5)), c.add(
            c.multiply(c.constant(14), c.power(p, 2), S1),
            c.multiply(p, c.linear([(17, b3), (5, j2)]), S2),
            c.multiply(c.add(c.multiply(p, c.linear([(16, b2), (5, j1)])),
                             c.multiply(c.constant(3), c.power(b3, 2)),
                             c.multiply(c.constant(5), b3, j2)), S3))),
        c.multiply(c.constant(Q(9, 10)), p, C4),
        c.multiply(c.constant(-Q(1, 160)), C4, c.add(G, c.constant(8))))
    difference = N.add((1, N.node(expanded)), (-1, N.node(c.derivative(short['Phi8']))),
                       (-1, N.node(short['short_density'])))
    bad = N.add((1, difference), (1, N.node(p)))
    checks = {
        'manufactured_expanded_coefficient_vs_short_endpoint_form': not difference,
        'manufactured_ell_ODE': not N.add((1, N.node(c.derivative(short['ell']))),
                                          (-1, N.node(short['ell_rhs']))),
        'manufactured_zeta_ODE': not N.add((1, N.node(c.derivative(short['zeta']))),
                                           (-1, N.node(short['zeta_rhs']))),
        'wrong_coefficient_preserved_as_nonzero': bool(bad),
        'endpoint_potential_only_needs_B4_zero': not previous.substitute(
            N, N.node(short['Phi8']), {previous.state_variable(c, p): {}}),
        'small_manufactured_polynomial_JSON_roundtrip':
            compressed.polynomial(json.loads(canonical(tail.poly_rows(N.node(expanded))))) == N.node(expanded),
    }
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
        code = 0 if report['verified_exact_c8_action_reduction'] else 2
    except Exception as exc:
        report = {'model': MODEL, 'completion': 'budget-exhausted' if isinstance(exc, formal.CompilationBudgetExceeded) else 'error',
            'exception_type': type(exc).__name__, 'error': str(exc), 'input': progress.get('input'),
            'preserved_certificate': progress.get('certificate'), 'source_hashes': source_hashes(),
            'elapsed_seconds': time.monotonic()-started, 'verified_exact_c8_action_reduction': False,
            'no_omitted_coefficient_is_interpreted_as_zero': True, 'action_sign_proved': False,
            'nonzero_period_proved': False, 'new_zero_cost_loop_proved': False}
        code = 2
    write_json(args.out, report)
    print(json.dumps({'completion': report['completion'],
                      'verified_c8_reduction': report['verified_exact_c8_action_reduction'],
                      'elapsed_seconds': report['elapsed_seconds']}), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
