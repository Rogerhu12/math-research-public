#!/usr/bin/env python3
"""Reduce the next published pure-tail density to a real quadratic action.

No forcing is recompiled.  The original genuine histories remain live;
one declared auxiliary primitive J_s=K e/4 is added, with zero initial
value and a proved zero end value when the complete second matrix is zero.
Research execution is restricted to the public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import json
from pathlib import Path
import resource
import time

import literature_pure_tail_subleading_verify as prior
import literature_pure_tail_period as tail
import literature_range_profile_algebra as formal


MODEL = 'published-pure-tail-next-order-triangular-action-v1'
SCRIPT = Path(__file__).resolve()
canonical, sha256, write_json = tail.canonical, tail.sha256, tail.write_json
COORDINATES = ('b0', 'd1', 'J')


def source_hashes():
    return {p.name: sha256(p.read_bytes()) for p in
            (SCRIPT, Path(prior.__file__).resolve(), Path(tail.__file__).resolve(),
             Path(formal.__file__).resolve())}


def geometry(c):
    h, k = c.geometry('h'), c.geometry('k')
    z = c.add(c.geometry('tail_end'), c.geometry('omega'))
    gamma = c.geometry('h', 1)
    nu = c.multiply(c.constant(Q(1, 2)), c.geometry('k', 1), c.power(h, -1))
    e = c.linear([(1, c.multiply(h, z)), (-1, k)])
    qnorm = c.add(c.one, c.power(e, 2))
    lam = c.multiply(c.linear([(1, c.multiply(gamma, z)),
                               (-1, c.multiply(h, nu))]), c.power(h, -2))
    K0 = c.linear([(1, c.multiply(k, c.power(z, 2))),
                   (-1, c.multiply(c.add(c.power(k, 2), c.one), z, c.power(h, -1)))])
    K = c.add(K0, c.derivative(lam))
    C = c.multiply(c.constant(Q(1, 8)), K, qnorm, c.power(h, -1))
    D = c.multiply(c.constant(Q(1, 4)), K, e)
    f = c.multiply(c.constant(Q(1, 8)), qnorm, c.power(h, -2))
    return {'C': C, 'D': D, 'f': f, 'fs': c.derivative(f), 'K': K, 'e': e}


def constants(m):
    p, r = 2*m-3, 3*m-6
    A = tail.aij(m, m)
    beta = tail.aij(m, r+2)/(4*A)
    alpha = (beta*tail.aij(m, p+2)-tail.aij(p, p+2)/8)/(2*A)
    def xy(i, j):
        a = tail.aij(i, j)
        return Q(i*j)-a, a/Q(i+j-2)-Q(i*j)
    x0, y0 = xy(m, m)
    xt, yt = xy(m, r+1)
    l0 = xt/(4*x0)
    l1 = (yt-xt*y0/x0)/4
    lf = Q(m*(r+1), 8)-l0*Q(m*m, 2)
    return {'alpha2': alpha, 'beta2': beta, 'lambda0': l0,
            'lambda1': l1, 'lambda_f': lf,
            'kappa': tail.aij(m, p)/(2*A)}


def potential(c, m, B, U, J, g):
    values = constants(m)
    top = c.linear([(values['alpha2'], c.multiply(c.power(B[0], 2), B[2])),
                    (values['beta2'], c.multiply(B[0], U[2]))])
    middle_factor = c.linear([(values['lambda0'], B[1]),
                              (values['lambda1'], J),
                              (values['lambda_f'], g['fs'])])
    middle = c.multiply(middle_factor, U[1])
    return c.add(top, middle), top, middle, values


def substitute(normalizer, polynomial, replacements):
    """Exact finite substitution; every substituted power must be nonnegative."""
    result = {}
    for monomial, coefficient in polynomial.items():
        kept = []
        factors = []
        for variable, power in monomial:
            if variable in replacements:
                if power < 0:
                    raise ValueError('no inverse of an auxiliary or completed history is allowed')
                factors.append((replacements[variable], power))
            else:
                kept.append((variable, power))
        term = {tuple(kept): coefficient}
        for value, power in factors:
            term = normalizer.multiply(term, normalizer.power(value, power))
        result = normalizer.add((1, result), (1, term))
    return result


def state_variable(c, node):
    item = c.nodes[node]
    if item[0] != 'st':
        raise ValueError('expected an actual history node')
    return f'state_{item[1]}'


def original_history_id(structure, stage, power, grade):
    ids = [i for i, row in enumerate(structure['state_labels'])
           if row[0] == stage and row[2] == power and row[3] == grade]
    if len(ids) != 1:
        raise ValueError('cannot identify a unique original coefficient history')
    return ids[0]


def state_names(polynomial):
    return sorted({name for monomial in polynomial for name, power in monomial
                   if name.startswith('state_') and power})


def coefficient_groups(polynomial):
    groups = {}
    for monomial, coefficient in polynomial.items():
        history = tuple((v, p) for v, p in monomial if v in COORDINATES)
        geometric = tuple((v, p) for v, p in monomial if v not in COORDINATES)
        if any(p < 0 for v, p in history):
            raise ValueError('negative degree in action coordinates')
        value = groups.setdefault(history, {})
        value[geometric] = value.get(geometric, Q(0))+coefficient
        if not value[geometric]:
            del value[geometric]
    return {key: value for key, value in groups.items() if value}


def reduce_structure(structure, args):
    budget = formal.Budget(max_nodes=args.max_nodes, max_atoms=1,
                           max_terms=args.max_terms, max_seconds=args.max_seconds)
    c = prior.load_coefficients(structure, budget)
    N = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                               max_cache_terms=args.max_cache_terms,
                               max_rss_mib=args.max_rss_mib)
    m = structure['tail_exponent']
    if type(m) is not int or m < 8:
        raise ValueError('integer m>=8 required')
    p, r, n = 2*m-3, 3*m-6, 4*m-9
    B = [prior.select_root(structure, 'second_completed_scalar', p+j, 2) for j in range(3)]
    U = [prior.select_root(structure, 'third_completed_scalar', r+j, 3) for j in range(3)]
    density = prior.select_root(structure, 'pure_completed_period_density', n+2, 4)
    g = geometry(c)
    J = c.state(g['D'], ('auxiliary', 'J_s=K*e/4', 'zero-initial', 'zero-end-if-complete-M=0'))
    F, Ftop, Fmid, values = potential(c, m, B, U, J, g)
    dF = c.derivative(F)
    residual = c.linear([(1, density), (-1, dF)])
    invariant = c.linear([(1, U[0]), (values['kappa'], c.power(B[0], 2))])
    invariant_ds = c.derivative(invariant)
    inv = N.node(invariant)
    inv_derivative = N.node(invariant_ds)
    inv_initial = prior.constant_initial_trace(inv)
    if inv_derivative or inv_initial:
        raise ValueError('the zero-initial leading first integral did not verify')
    u0_index = original_history_id(structure, 3, r, 3)
    raw = N.node(residual)
    quotient, reduced = prior.divide_by_monic_history(N, raw, inv, f'state_{u0_index}')
    raw_b0 = original_history_id(structure, 2, p, 2)
    raw_b1 = original_history_id(structure, 2, p+1, 2)
    Jvar = state_variable(c, J)
    allowed = {f'state_{raw_b0}', f'state_{raw_b1}', Jvar}
    unexpected = sorted(set(state_names(reduced))-allowed)
    # Keep the original coefficient system if a claimed cancellation fails.
    # Never discard an unexpected history or a polynomial term.
    b0poly = N.node(B[0])
    d1root = c.linear([(1, B[1]), (-Q(m*m, 2), g['fs'])])
    d1poly = N.node(d1root)
    local_b0 = N.add((1, b0poly), (-1, {((f'state_{raw_b0}', 1),): Q(1)}))
    local_d1 = N.add((1, d1poly), (-1, {((f'state_{raw_b1}', 1),): Q(1)}))
    if state_names(local_b0) or state_names(local_d1):
        raise ValueError('completed second coordinate is not raw history plus a local geometric term')
    replacements = {
        f'state_{raw_b0}': N.add((1, {(('b0', 1),): Q(1)}), (-1, local_b0)),
        f'state_{raw_b1}': N.add((1, {(('d1', 1),): Q(1)}), (-1, local_d1)),
        Jvar: {(('J', 1),): Q(1)},
    }
    action = substitute(N, reduced, replacements)
    groups = coefficient_groups(action)
    max_degree = max((sum(power for name, power in monomial) for monomial in groups), default=0)
    inverse = {'b0': b0poly, 'd1': d1poly, 'J': N.node(J)}
    replay = substitute(N, action, inverse)
    replay_difference = N.add((1, replay), (-1, reduced))
    if replay_difference:
        raise AssertionError('completed-coordinate replay failed')
    fresh = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                                   max_cache_terms=args.max_cache_terms,
                                   max_rss_mib=args.max_rss_mib)
    fresh_difference = fresh.add((1, fresh.node(density)), (-1, fresh.node(dF)),
                                  (-1, fresh.multiply(quotient, fresh.node(invariant))),
                                  (-1, replay))
    if fresh_difference:
        raise AssertionError('fresh original-DAG action identity failed')
    complete_form = not unexpected and max_degree <= 2
    report = {
        'tail_exponent': m, 'density_power': n+2,
        'rational_constants': {key: str(value) for key, value in values.items()},
        'verified_exact_action_identity': True,
        'all_third_and_highest_second_histories_eliminated': not unexpected,
        'unexpected_retained_histories': unexpected,
        'verified_three_primitive_quadratic_normal_form': complete_form,
        'action_coordinate_total_degree': max_degree,
        'action_coordinates': {'b0': 'original completed second leading coefficient',
                               'd1': 'original completed second next coefficient - m^2*f_s/2',
                               'J': 'genuine auxiliary integral J_s=K*e/4, J(0)=0'},
        'original_history_count': len(structure['state_rhs']),
        'actual_history_count_with_declared_auxiliary': len(c.state_rhs),
        'raw_density_minus_endpoint_potential_derivative': prior.polynomial_record(raw),
        'first_integral_quotient': prior.polynomial_record(quotient),
        'first_integral_derivative': prior.polynomial_record(inv_derivative),
        'first_integral_initial_trace': prior.polynomial_record(inv_initial),
        'action': prior.polynomial_record(action),
        'action_groups': [{'history_monomial': [[v, power] for v, power in monomial],
                           **prior.polynomial_record(value)}
                          for monomial, value in sorted(groups.items())],
        'fresh_original_DAG_identity': prior.polynomial_record(fresh_difference),
        'completed_coordinate_replay': prior.polynomial_record(replay_difference),
        'period_equivalence_scope': 'zero incoming histories, constant scalar endpoint germs, complete M=0; J end value uses the full operator, not one sampled profile',
        'entire_action_zero': not action,
        'action_sign_proved': False, 'nonzero_period_proved': False,
        'new_zero_cost_loop_proved': False, 'forcing_recompiled': False,
        'geometric_path_evaluated': False,
    }
    payload = {'coefficient_DAG': c.nodes, 'state_rhs': c.state_rhs,
               'state_labels': c.state_labels, 'state_initial_values': ['0']*len(c.state_rhs),
               'roots': {'density': density, 'F_top': Ftop, 'F_mid': Fmid,
                         'endpoint_potential': F, 'potential_derivative': dF,
                         'first_integral': invariant, 'first_integral_derivative': invariant_ds,
                         'b0': B[0], 'b1_completed': B[1], 'd1_orthogonal': d1root,
                         'J': J, 'J_rhs': g['D']},
               'first_integral_quotient': tail.poly_rows(quotient),
               'action_polynomial': tail.poly_rows(action),
               'action_groups': [{'history_monomial': [[v, power] for v, power in monomial],
                                  'coefficient': tail.poly_rows(value)}
                                 for monomial, value in sorted(groups.items())],
               'raw_second_to_completed_replacements': {key: tail.poly_rows(value)
                                                         for key, value in replacements.items()},
               'identity': 'density = Ds(F_top+F_mid) + quotient*I0 + action(b0,d1,J)',
               'report': report}
    return report, payload, groups


def run(args, progress):
    started = time.monotonic()
    # This inherited entry point enforces public Actions, byte hashes,
    # original source identity and published topic-notes input paths.
    structure, provenance = prior.public_inputs(args)
    progress['input'] = provenance
    report, payload, groups = reduce_structure(structure, args)
    payload.update({'model': MODEL, 'input': provenance, 'source_hashes': source_hashes()})
    raw = canonical(payload)+b'\n'
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > 5000000:
        raise formal.CompilationBudgetExceeded('complete action certificate compressed-byte budget')
    path = args.out.with_name(args.out.stem+'-certificate.json.gz')
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_name(path.name+'.tmp')
    pending.write_bytes(packed)
    pending.replace(path)
    artifact = {'file': path.name, 'compressed_bytes': len(packed),
                'compressed_sha256': sha256(packed), 'raw_bytes': len(raw),
                'raw_sha256': sha256(raw)}
    progress['certificate'] = artifact
    readable = {'model': MODEL, 'input': provenance, 'complete_certificate': artifact,
                'meaning': 'An exact integrated-action representative, not a sign or nonzero-period certificate.',
                'coordinate_definition': report['action_coordinates'],
                'action_groups': [{'history_monomial': [[v, p] for v, p in monomial],
                                   **prior.polynomial_record(value, 400)}
                                  for monomial, value in sorted(groups.items())]}
    while len(canonical(readable))+1 > 95000:
        candidates = [v for v in readable['action_groups'] if v.get('readable_terms')]
        if not candidates:
            raise formal.CompilationBudgetExceeded('readable coefficient metadata byte budget')
        entry = max(candidates, key=lambda v: len(v['readable_terms']))
        entry['readable_terms'] = entry['readable_terms'][:len(entry['readable_terms'])//2]
        entry['readable_terms_truncated'] = True
    brief = write_json(args.out.with_name(args.out.stem+'-expressions.json'), readable)
    report.update({'completion': 'complete', 'model': MODEL, 'input': provenance,
                   'source_hashes': source_hashes(), 'artifacts': [artifact, brief],
                   'elapsed_seconds': time.monotonic()-started,
                   'peak_rss_mib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024})
    return report


def developer_check(args):
    """Artificial triangular histories plus a manufactured exact action."""
    budget = formal.Budget(max_nodes=5000, max_atoms=1, max_terms=1000, max_seconds=20)
    c = tail.TailCoefficients(budget)
    m = 8
    values = constants(m)
    G, P, R, H = [c.geometry(name) for name in ('toy_G', 'toy_P', 'toy_R', 'toy_H')]
    B = [c.state(node, (2, 'toy-B', 13+i, 2)) for i, node in enumerate((G, P, R))]
    U = [c.state(c.multiply(c.constant(-2*values['kappa']), B[0], G), (3, 'toy-U', 18, 3)),
         c.state(c.add(B[0], B[1]), (3, 'toy-U', 19, 3)),
         c.state(B[2], (3, 'toy-U', 20, 3))]
    g = geometry(c)
    # Manufacture the expected form without introducing J in the input.
    F0, _, _, _ = potential(c, m, B, U, c.zero, g)
    inv = c.linear([(1, U[0]), (values['kappa'], c.power(B[0], 2))])
    density = c.add(c.derivative(F0),
                    c.multiply(c.constant(values['lambda1']), g['D'], U[1]),
                    c.multiply(inv, H), c.power(B[0], 2), B[1])
    structure = {'coefficient_DAG': json.loads(canonical(c.nodes)),
                 'state_rhs': c.state_rhs, 'state_labels': c.state_labels,
                 'state_initial_values': ['0']*len(c.state_rhs), 'tail_exponent': m,
                 'second_completed_scalar': [{'t_power': 13+i, 'profile_grade': 2,
                                               'coefficient_root': root} for i, root in enumerate(B)],
                 'third_completed_scalar': [{'t_power': 18+i, 'profile_grade': 3,
                                              'coefficient_root': root} for i, root in enumerate(U)],
                 'pure_completed_period_density': [{'t_power': 25, 'profile_grade': 4,
                                                     'coefficient_root': density}]}
    report, payload, groups = reduce_structure(structure, args)
    wrong_density = c.add(density, U[2])
    wrong = json.loads(canonical(structure))
    wrong['coefficient_DAG'] = json.loads(canonical(c.nodes))
    wrong['pure_completed_period_density'][0]['coefficient_root'] = wrong_density
    wrong_report, _, _ = reduce_structure(wrong, args)
    checks = {
        'complete_artificial_reduction_path': report['verified_three_primitive_quadratic_normal_form'],
        'one_genuine_auxiliary_history_added': report['actual_history_count_with_declared_auxiliary'] == 7,
        'wrong_independent_state_not_silently_zeroed': report['raw_density_minus_endpoint_potential_derivative']['terms'] > 0,
        'first_integral_and_initial_checked': report['first_integral_derivative']['exact_zero']
                                             and report['first_integral_initial_trace']['exact_zero'],
        'fresh_original_reconstruction': report['fresh_original_DAG_identity']['exact_zero'],
        'completed_coordinates_replay_exact': report['completed_coordinate_replay']['exact_zero'],
        'nonzero_action_preserved': bool(groups),
        'degree_two_not_a_sign_assertion': report['action_coordinate_total_degree'] == 2
                                          and not report['action_sign_proved'],
        'unexpected_history_rejects_normal_form_without_dropping_it':
            not wrong_report['verified_three_primitive_quadratic_normal_form']
            and f'state_{c.nodes[U[2]][1]}' in wrong_report['unexpected_retained_histories'],
    }
    result = {'mode': 'artificial-development-only', 'passed': all(checks.values()),
              'checks': checks, 'research_structure_loaded': False, 'forcing_compiled': False,
              'source_hashes': source_hashes()}
    json.loads(canonical(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--structure', type=Path)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--max-seconds', type=float, default=240)
    parser.add_argument('--max-nodes', type=int, default=250000)
    parser.add_argument('--max-terms', type=int, default=120000)
    parser.add_argument('--max-cache-terms', type=int, default=2500000)
    parser.add_argument('--max-rss-mib', type=float, default=1800)
    args = parser.parse_args()
    if args.check_only:
        report = developer_check(args)
        write_json(args.out, report)
        print(json.dumps({'mode': report['mode'], 'passed': report['passed']}), flush=True)
        return 0 if report['passed'] else 2
    started = time.monotonic()
    progress = {}
    try:
        report = run(args, progress)
        code = 0 if report['verified_three_primitive_quadratic_normal_form'] else 2
    except Exception as exc:
        report = {'completion': 'budget-exhausted' if isinstance(exc, formal.CompilationBudgetExceeded) else 'error',
                  'model': MODEL, 'exception_type': type(exc).__name__, 'error': str(exc),
                  'input': progress.get('input'), 'preserved_certificate': progress.get('certificate'),
                  'source_hashes': source_hashes(), 'elapsed_seconds': time.monotonic()-started,
                  'verified_three_primitive_quadratic_normal_form': False,
                  'no_omitted_coefficient_is_interpreted_as_zero': True,
                  'nonzero_period_proved': False, 'action_sign_proved': False}
        code = 2
    write_json(args.out, report)
    print(json.dumps({'completion': report['completion'],
                      'quadratic_form_verified': report['verified_three_primitive_quadratic_normal_form'],
                      'elapsed_seconds': report['elapsed_seconds']}), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
