#!/usr/bin/env python3
"""Consume only the next c^7 coefficient of the published m8 D25 family.

The R100 input has already verified the complete parameter family and all
23 genuine histories.  This consumer does not repeat those identities or
compile forcing.  It checks one new zero-end potential, two new true
history coordinates, and the complete five-history remainder.  Research
execution is restricted to the public repository's own GitHub Actions.
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

import literature_pure_tail_c8_reduce as previous_c8
import literature_pure_tail_action_compress as compressed
import literature_pure_tail_next_reduce as previous
import literature_pure_tail_subleading_verify as prior
import literature_pure_tail_period as tail
import literature_range_profile_algebra as formal


MODEL = 'published-m8-D25-c7-five-true-history-action-v1'
SCRIPT = Path(__file__).resolve()
canonical, sha256, write_json = tail.canonical, tail.sha256, tail.write_json
SCALE = compressed.SCALE
NAMES = ('p', 'ell', 'zeta', 'mu', 'nu')


def source_hashes():
    paths = (SCRIPT, Path(previous_c8.__file__).resolve(), Path(compressed.__file__).resolve(),
             Path(previous.__file__).resolve(), Path(prior.__file__).resolve(),
             Path(tail.__file__).resolve(), Path(formal.__file__).resolve())
    return {p.name: sha256(p.read_bytes()) for p in paths}


def checked_payload(report_raw, packed, certificate_name, current_sources):
    """Byte-bound public interface; also exercised with artificial metadata."""
    if len(report_raw) > 100000 or len(packed) > 5000000:
        raise ValueError('published input byte budget')
    report = json.loads(report_raw)
    if (report.get('model') != previous_c8.MODEL or report.get('completion') != 'complete'
            or report.get('tail_exponent') != 8 or report.get('density_power') != 25
            or not report.get('verified_exact_c8_action_reduction')):
        raise ValueError('the completed R100 parameter-family certificate is required')
    artifact, = [v for v in report['artifacts'] if v['file'] == certificate_name]
    if len(packed) != artifact['compressed_bytes'] or sha256(packed) != artifact['compressed_sha256']:
        raise ValueError('compressed certificate bytes differ')
    raw = gzip.decompress(packed)
    if len(raw) > 10000000 or len(raw) != artifact['raw_bytes'] or sha256(raw) != artifact['raw_sha256']:
        raise ValueError('decoded certificate bytes differ')
    payload = json.loads(raw)
    if (payload.get('model') != previous_c8.MODEL
            or payload['report'].get('tail_exponent') != 8
            or not payload['report'].get('verified_exact_c8_action_reduction')):
        raise ValueError('certificate model or completed family differs')
    for name, digest in report['source_hashes'].items():
        if current_sources.get(name) != digest or payload['source_hashes'].get(name) != digest:
            raise ValueError(f'published imported source changed: {name}')
    return payload, {'report_bytes': len(report_raw), 'report_sha256': sha256(report_raw),
        'certificate': certificate_name,
        **{k: artifact[k] for k in ('compressed_bytes', 'compressed_sha256', 'raw_bytes', 'raw_sha256')},
        'published_model': report['model'], 'original_input': report['input'],
        'R100_complete_family_and_34_identities_consumed_not_recomputed': True}


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
    payload, provenance = checked_payload(args.report.read_bytes(), args.certificate.read_bytes(),
                                          args.certificate.name, source_hashes())
    provenance['report'] = args.report.name
    if len(payload['state_rhs']) != 23 or payload['state_initial_values'] != ['0']*23:
        raise ValueError('the 23 genuine zero-initial R100 histories are required')
    return payload, provenance


def low_endpoint_potential(c, B, J):
    p = B[4]
    return c.multiply(c.power(p, 2), c.linear([(Q(64, 5), B[1]), (8, J[0])]))


def five_coordinates(c, B, J, eta):
    p, etas = B[4], c.derivative(eta)
    zeta = c.linear([(1, B[3]), (-4, c.multiply(eta, p))])
    ell = c.linear([(1, B[3]), (-Q(1, 2), J[2]), (-1, c.multiply(eta, p))])
    beta2 = c.linear([(1, B[2]), (-3, c.multiply(eta, B[3])),
                      (6, c.multiply(c.power(eta, 2), p))])
    j1 = c.linear([(1, J[1]), (-2, c.multiply(eta, J[2])),
                   (6, c.multiply(c.power(eta, 2), p))])
    mu = c.linear([(1, beta2), (-Q(1, 8), etas)])
    nu = c.linear([(1, beta2), (-Q(1, 2), j1)])
    kh = c.multiply(c.geometry('k'), c.power(c.geometry('h'), -1))
    return {'p': p, 'ell': ell, 'zeta': zeta, 'mu': mu, 'nu': nu,
        'eta': eta, 'eta_s': etas, 'beta2': beta2, 'moving_J1': j1,
        'mu_rhs': c.multiply(c.constant(-3), etas, zeta),
        'nu_rhs': c.linear([(Q(1, 8), kh),
                            (-1, c.multiply(etas, c.linear([(1, zeta), (2, ell)])))])}


def five_substitution(c, normalizer, B, J, eta):
    N = normalizer
    v = {name: {((name, 1),): Q(1)} for name in NAMES}
    p, ell, zeta, mu, nu = [v[name] for name in NAMES]
    e, es = N.node(eta), N.node(c.derivative(eta))
    ep, e2p = N.multiply(e, p), N.multiply(N.power(e, 2), p)
    return {
        previous.state_variable(c, B[4]): p,
        previous.state_variable(c, B[3]): N.add((1, zeta), (4, ep)),
        previous.state_variable(c, J[2]): N.add((2, zeta), (-2, ell), (6, ep)),
        previous.state_variable(c, B[2]): N.add((1, mu), (Q(1, 8), es),
                                                (3, N.multiply(e, zeta)), (6, e2p)),
        previous.state_variable(c, J[1]): N.add((2, mu), (Q(1, 4), es), (-2, nu),
                                                (4, N.multiply(e, zeta)),
                                                (-4, N.multiply(e, ell)), (6, e2p)),
    }


def variable_coefficients(poly, variable):
    result = {}
    for monomial, coefficient in poly.items():
        power = dict(monomial).get(variable, 0)
        kept = tuple((v, n) for v, n in monomial if v != variable)
        bucket = result.setdefault(power, {})
        bucket[kept] = bucket.get(kept, Q(0))+coefficient
        if not bucket[kept]:
            del bucket[kept]
    return {power: value for power, value in result.items() if value}


def reflected_five_polynomial(poly):
    """New c7 parity only; no old whole-DAG reflection calculation."""
    result = {}
    for monomial, coefficient in poly.items():
        parity = sum(power for name, power in monomial
                     if name in ('p', 'mu', 'nu', 'omega_0') or name.startswith('k_'))
        result[monomial] = coefficient*((-1)**parity)
    return result


def reduce_action(payload, args):
    budget = formal.Budget(max_nodes=args.max_nodes, max_atoms=1,
                           max_terms=args.max_terms, max_seconds=args.max_seconds)
    c = prior.load_coefficients(payload, budget)
    N = tail.LaurentNormalizer(c, max_terms=args.max_terms,
                               max_cache_terms=args.max_cache_terms, max_rss_mib=args.max_rss_mib)
    roots = payload['roots']
    B = {j: roots[f'coefficient_B{j}'] for j in range(5)}
    J = {j: roots[f'coefficient_J{j}'] for j in range(4)}
    family = compressed.polynomial(payload['parameter_action_polynomial'])
    a7 = N.add((1/SCALE, compressed.parameter_coefficients(family).get(7, {})))
    # This is the only new parameter coefficient consumed.  The full family
    # remains in the emitted certificate and is not recompiled or re-expanded.
    eta = roots['c8_eta']
    coords = five_coordinates(c, B, J, eta)
    phi = low_endpoint_potential(c, B, J)
    phi_ds = c.derivative(phi)
    remainder = N.add((1, a7), (-1, N.node(phi_ds)))
    b1, j0 = previous.state_variable(c, B[1]), previous.state_variable(c, J[0])
    p, ps = N.node(B[4]), N.node(c.derivative(B[4]))
    b1_coeff = variable_coefficients(a7, b1)
    j0_coeff = variable_coefficients(a7, j0)
    differences = {
        'c7_B1_linear_coefficient': N.add((1, b1_coeff.get(1, {})),
                                           (-Q(128, 5), N.multiply(p, ps))),
        'c7_J0_linear_coefficient': N.add((1, j0_coeff.get(1, {})),
                                           (-16, N.multiply(p, ps))),
        'new_potential_zero_when_true_B4_zero': previous.substitute(N, N.node(phi),
                                        {previous.state_variable(c, B[4]): {}}),
    }
    for name in ('mu', 'nu'):
        differences[f'{name}_true_ODE'] = N.add((1, N.node(c.derivative(coords[name]))),
                                                (-1, N.node(coords[name+'_rhs'])))
        differences[f'{name}_zero_history_constant_germ_trace'] = prior.constant_initial_trace(N.node(coords[name]))
    substitution = five_substitution(c, N, B, J, eta)
    short = previous.substitute(N, remainder, substitution)
    inverse = {name: N.node(coords[name]) for name in NAMES}
    inverse_short = previous.substitute(N, short, inverse)
    differences['five_history_coordinates_exact_inverse'] = N.add((1, inverse_short), (-1, remainder))
    differences['c7_full_consumed_coefficient_identity'] = N.add(
        (1, a7), (-1, N.node(phi_ds)), (-1, inverse_short))
    differences['c7_scalar_reflection_even_in_true_coordinates'] = N.add(
        (1, short), (-1, reflected_five_polynomial(short)))
    allowed = {previous.state_variable(c, B[j]) for j in (4, 3, 2)} | {
        previous.state_variable(c, J[j]) for j in (2, 1)}
    unexpected = sorted(set(previous.state_names(remainder))-allowed)
    short_unexpected = previous.state_names(short)
    groups = previous_c8.history_coordinate_groups(short, NAMES)
    low_history_degree_ok = max(b1_coeff, default=0) <= 1 and max(j0_coeff, default=0) <= 1
    unchanged_histories = len(c.state_rhs) == len(payload['state_rhs']) == 23
    verified = (all(not value for value in differences.values()) and not unexpected
                and not short_unexpected and low_history_degree_ok and unchanged_histories)
    report = {'tail_exponent': 8, 'density_power': 25, 'tail_endpoint_parameter_power': 7,
        'verified_exact_c7_five_history_reduction': verified,
        'normalization': str(SCALE), 'genuine_histories_retained': len(c.state_rhs),
        'new_histories_added': len(c.state_rhs)-len(payload['state_rhs']),
        'parameter_family_preserved': prior.polynomial_record(family),
        'normalized_c7': prior.polynomial_record(a7), 'endpoint_potential': prior.polynomial_record(N.node(phi)),
        'five_history_action': prior.polynomial_record(short),
        'five_history_total_degree': max((sum(power for _, power in key) for key in groups), default=0),
        'five_history_groups': [{'history_monomial': [[v, p] for v, p in key],
                                **prior.polynomial_record(value)} for key, value in sorted(groups.items())],
        'B1_J0_at_most_linear': low_history_degree_ok,
        'unexpected_original_histories_after_potential': unexpected,
        'unexpected_original_histories_after_coordinate_change': short_unexpected,
        'exact_differences': {name: prior.polynomial_record(value) for name, value in differences.items()},
        'actual_history_definitions': {
            'p': 'B4', 'ell': 'B3-J2/2-eta*p', 'zeta': 'B3-4*eta*p',
            'mu': 'B2-3*eta*B3+6*eta^2*p-eta_s/8; mu_s=-3*eta_s*zeta',
            'nu': 'B2-3*eta*B3+3*eta^2*p+eta*J2-J1/2; nu_s=k/(8*h)-eta_s*(zeta+2*ell)',
            'eta': 'omega-k/h with actual omega_s=k_s/(2*h)'},
        'endpoint_trace_scope': 'zero incoming histories at a constant scalar germ; same trace at final endpoint only under complete M=0',
        'potential_scope': 'Phi7=(64/5)*p^2*B1+8*p^2*J0; vanishes whenever p=0',
        'R104_R106_scope': 'for the reflected-reversed four-block path its c7 period is four times the original block c7 period',
        'old_34_identities_recomputed': False, 'forcing_recompiled': False,
        'geometric_path_evaluated': False, 'action_sign_proved': False,
        'nonzero_period_proved': False, 'complete_fourth_range_proved': False}
    output = {'model': MODEL, 'coefficient_DAG': c.nodes, 'state_rhs': c.state_rhs,
        'state_labels': c.state_labels, 'state_initial_values': ['0']*len(c.state_rhs),
        'roots': {**roots, **{f'c7_{name}': node for name, node in coords.items()},
                  'c7_endpoint_potential': phi, 'c7_endpoint_potential_derivative': phi_ds},
        'parameter_action_polynomial': payload['parameter_action_polynomial'],
        'normalized_c7_polynomial': tail.poly_rows(a7),
        'remainder_original_histories_polynomial': tail.poly_rows(remainder),
        'five_history_action_polynomial': tail.poly_rows(short),
        'five_history_groups': [{'history_monomial': [[v, p] for v, p in key],
                                 'coefficient': tail.poly_rows(value)} for key, value in sorted(groups.items())],
        'exact_difference_polynomials': {name: tail.poly_rows(value) for name, value in differences.items()},
        'identity': '[c^7](published compressed D25 action)=SCALE*(Ds(Phi7)+five_history_action)',
        'report': report}
    return report, output, groups


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
        'meaning': 'Complete true five-history c7 action; no sign or zero-cost assertion.',
        'history_definitions': report['actual_history_definitions'],
        'five_history_groups': [{'history_monomial': [[v, p] for v, p in key],
                                 **prior.polynomial_record(value, 500)} for key, value in sorted(groups.items())]}
    while len(canonical(readable))+1 > 95000:
        entries = [entry for entry in readable['five_history_groups'] if entry.get('readable_terms')]
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
    """Small manufactured array/metadata adapter; no research input is read."""
    c = tail.TailCoefficients(formal.Budget(max_nodes=12000, max_atoms=1, max_terms=8000, max_seconds=20))
    N = tail.LaurentNormalizer(c, max_terms=8000, max_cache_terms=100000, max_rss_mib=1800)
    B = {j: c.state(c.constant(j+1), ('artificial-B', j)) for j in range(5)}
    J = {j: c.state(c.constant(2*j+3), ('artificial-J', j)) for j in range(3)}
    eta = c.state(c.one, ('artificial-eta-clock',))
    coords = five_coordinates(c, B, J, eta)
    sub = five_substitution(c, N, B, J, eta)
    inverse = {name: N.node(coords[name]) for name in NAMES}
    sample = c.linear([(3, B[2]), (-2, J[1]), (1, c.multiply(B[4], B[3], J[2]))])
    sample_poly = N.node(sample)
    transformed = previous.substitute(N, sample_poly, sub)
    roundtrip = previous.substitute(N, transformed, inverse)
    phi = low_endpoint_potential(c, B, J)
    manufactured = N.add((1, N.node(c.derivative(phi))), (1, sample_poly))
    c7 = N.multiply(manufactured, {(('tail_end_0', 7),): Q(1)})
    distractor = {(('tail_end_0', 8),): Q(17)}
    family = N.add((1, c7), (1, distractor))
    selected = compressed.parameter_coefficients(family)[7]
    bad = N.add((1, selected), (-1, N.node(c.derivative(phi))), (-1, sample_poly), (1, N.node(B[1])))
    fake_payload = {'model': previous_c8.MODEL, 'report': {'tail_exponent': 8,
                    'verified_exact_c8_action_reduction': True}, 'source_hashes': {'artificial.py': 'abc'},
                    'manufactured_only': True}
    raw = canonical(fake_payload)+b'\n'
    packed = gzip.compress(raw, mtime=0)
    fake_report = {'model': previous_c8.MODEL, 'completion': 'complete', 'tail_exponent': 8,
        'density_power': 25, 'verified_exact_c8_action_reduction': True,
        'source_hashes': {'artificial.py': 'abc'}, 'input': {'artificial': True},
        'artifacts': [{'file': 'fake.json.gz', 'compressed_bytes': len(packed),
                      'compressed_sha256': sha256(packed), 'raw_bytes': len(raw), 'raw_sha256': sha256(raw)}]}
    valid, _ = checked_payload(canonical(fake_report), packed, 'fake.json.gz', {'artificial.py': 'abc'})
    rejected = False
    try:
        checked_payload(canonical(fake_report), packed+b'X', 'fake.json.gz', {'artificial.py': 'abc'})
    except ValueError:
        rejected = True
    checks = {
        'manufactured_five_coordinate_forward_inverse': not N.add((1, roundtrip), (-1, sample_poly)),
        'manufactured_c7_selects_no_c8_distractor': selected == manufactured,
        'manufactured_zero_end_potential_recovers_full_remainder':
            not N.add((1, selected), (-1, N.node(c.derivative(phi))), (-1, sample_poly)),
        'manufactured_wrong_low_history_not_erased': bool(bad),
        'manufactured_exact_polynomial_JSON_roundtrip': compressed.polynomial(json.loads(canonical(tail.poly_rows(family)))) == family,
        'manufactured_input_byte_binding_accepts_correct_payload': valid == fake_payload,
        'manufactured_input_byte_binding_rejects_tamper': rejected,
    }
    result = {'mode': 'artificial-development-only', 'passed': all(checks.values()), 'checks': checks,
        'research_input_loaded': False, 'research_target_evaluated': False,
        'forcing_compiled': False, 'source_hashes': source_hashes()}
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
        code = 0 if report['verified_exact_c7_five_history_reduction'] else 2
    except Exception as exc:
        report = {'model': MODEL, 'completion': 'budget-exhausted' if isinstance(exc, formal.CompilationBudgetExceeded) else 'error',
            'exception_type': type(exc).__name__, 'error': str(exc), 'input': progress.get('input'),
            'preserved_certificate': progress.get('certificate'), 'source_hashes': source_hashes(),
            'elapsed_seconds': time.monotonic()-started, 'verified_exact_c7_five_history_reduction': False,
            'no_omitted_coefficient_is_interpreted_as_zero': True, 'action_sign_proved': False,
            'nonzero_period_proved': False, 'complete_fourth_range_proved': False}
        code = 2
    write_json(args.out, report)
    print(json.dumps({'completion': report['completion'],
                      'verified_c7_reduction': report['verified_exact_c7_five_history_reduction'],
                      'elapsed_seconds': report['elapsed_seconds']}), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
