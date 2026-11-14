#!/usr/bin/env python3
"""Consume the actual q106 continuous domain in the complete mean repair map.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This is a rigorous difference between the explicitly defined original aligned
exact-real field and its C2 comparison, along their full linear repair
homotopy. The uniform-psi mean and its single anchored physical-s primitive
are complete integrals; no angular or radial quadrature replaces them.
Original floating evaluation, coordinate alignment, numerical quadrature,
target-g error, PDE closure and reach are separate unpaid tasks.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx

PINS = {
    'domain': 'a7342234eb1ce94569f7de40f1fa084701da35b87dbf4bdcec82be1e84cde39d',
    'domain_check': 'e1b31766b465956cc9f337cf9921d2cde4b1641c8362ad6f622e8443837456ac',
    'background': 'a3f57c4efdbd5170183cd97ffe4d2828c57c6a2c13c5f603fd1ed144f99db60f',
    'state_repair': 'd848f7a1996e7cb620275e86d336faa0d22d84c1e44f5a2ee707c1e29a337dda',
    'radial': '2d4993d9d5735e5acafe563cbec6def27718d5b0764ad182c3588f8fedf2a83d',
    'cartesian': '05ea9580832c1b59ec6ec80e88ac484dcc8b2fa3f0ead68867d0bad8212f7775',
    'primary': '83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293',
}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == '.gz' else data)


def dy(z):
    return Q(int(z[0])) * Q(2) ** int(z[1])


def rational(z):
    return Q(int(z['numerator']), int(z['denominator']))


def binary(z):
    return Q.from_float(float(z))


def aq(z):
    z = Q(z)
    return arb(z.numerator) / z.denominator


def upper(z, bits=160):
    """Positive outward dyadic, checked against the Arb upper endpoint."""
    m, e = arb(z).upper().man_exp()
    endpoint = Q(int(m)) * Q(2) ** int(e)
    if endpoint < 0:
        raise ArithmeticError('Positive majorant required')
    if not endpoint:
        return ['0', 0]
    exponent = endpoint.numerator.bit_length() - endpoint.denominator.bit_length() - bits
    scaled = endpoint / Q(2) ** exponent
    mantissa = (scaled.numerator + scaled.denominator - 1) // scaled.denominator
    result = [str(mantissa), exponent]
    if dy(result) < endpoint:
        raise ArithmeticError('Inward majorant rounding')
    return result


def jet_add(a, b):
    return [x + y for x, y in zip(a, b)]


def jet_product(a, b):
    """Norm majorants in order value, lambda, s, lambda-s."""
    return [
        a[0] * b[0],
        a[1] * b[0] + a[0] * b[1],
        a[2] * b[0] + a[0] * b[2],
        a[3] * b[0] + a[1] * b[2] + a[2] * b[1] + a[0] * b[3],
    ]


def vector_formula_majorants(uj, vj, tj, Pu, Wu, Du, Wl, Dl):
    """Complete F=(-t P(Pv-(u.v)u)+sqrt(D)(u x v))/W.

    Products stand for scalar product, cross product or scalar multiplication
    as appropriate; each has operator norm one. Negative signs pay sums.
    Saved actual domain bounds replace only zeroth-order norm majorants.
    """
    P = jet_product(uj, uj)
    P[0] = Pu
    Z = jet_product(uj, vj)
    Z[0] = Wu.sqrt()
    W = jet_product(Z, Z)
    W[0] = Wu
    t2 = jet_product(tj, tj)
    P3 = jet_product(jet_product(P, P), P)
    D = jet_add(W, jet_product(t2, P3))
    D[0] = Du
    root = Dl.sqrt()
    rootD = [Du.sqrt(), D[1] / (2 * root), D[2] / (2 * root),
             D[3] / (2 * root) + D[1] * D[2] / (4 * Dl * root)]
    invW = [1 / Wl, W[1] / Wl**2, W[2] / Wl**2,
            W[3] / Wl**2 + 2 * W[1] * W[2] / Wl**3]
    c = jet_product(uj, vj)
    A = jet_add(jet_product(P, vj), jet_product(c, uj))
    A[0] = (Pu * Wu).sqrt()  # exact identity |Pv-(u.v)u|^2=P W
    numerator = jet_add(jet_product(jet_product(tj, P), A), jet_product(rootD, Z))
    return jet_product(numerator, invW)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in PINS:
        parser.add_argument('--' + key.replace('_', '-'), type=Path, required=True)
    parser.add_argument('--domain-resource', type=Path, required=True)
    parser.add_argument('--domain-check-resource', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    ctx.prec = 256
    ctx.threads = 1
    if args.out.exists():
        raise FileExistsError('Fresh complete mean repair output required')
    counts = {}
    def check(name, condition):
        if not condition:
            raise ArithmeticError(name)
        counts[name] = counts.get(name, 0) + 1
    identities = {}
    for key, expected in PINS.items():
        path = getattr(args, key)
        check('every_frozen_actual_input_SHA_matches', sha(path) == expected)
        identities[str(path)] = expected
    domain, audit, bg, state, manifest, cart, primary = [read(getattr(args, key)) for key in PINS]
    for path in (args.domain_resource, args.domain_check_resource):
        res = read(path)
        check('owned_actual_domain_and_saved_check_exits_zero', res['exitcode'] == 0 and res['wait4_observed'])
        identities[str(path)] = sha(path)
    check('complete_actual_continuous_homotopy_domain', domain['all_domain_gates'] and
          domain['complete_original_interval_cover'] and domain['failed_atoms'] == 0)
    check('complete_independent_saved_domain_consumption', audit['all_gates'] and
          audit['input_sha256'][str(args.domain)] == sha(args.domain) and
          audit['final_complete_atoms'] == len(domain['rows']))
    check('actual_primary_accepted_and_identity_unchanged', primary['solver_success'] and
          not primary.get('audit_pending', True) and domain['primary_sha256'] == sha(args.primary))
    check('all_original_radial_jets_available', manifest['finished'] and
          manifest['all_original_intervals_covered'] and manifest['all_radial_state_jets_exactly_enclosed'] and
          manifest['input_identity']['primary_sha256'] == sha(args.primary))
    check('all_actual_repair_inputs_complete', bg['all_gates'] and state['all_gates'] and cart['all_gates'])
    B = next(p for p in bg['profiles'] if p['accepted_primary_sha256'] == sha(args.primary))
    C = next(p for p in cart['profiles'] if p['accepted_primary_sha256'] == sha(args.primary))
    check('same_explicit_background_and_full_state_comparisons', C['full_state_repair_included'] and
          domain['background_comparison_definition_sha256'] == B['comparison_definition_sha256'] == C['background_comparison_definition_sha256'] and
          domain['state_comparison_definition_sha256'] == state['comparison_field_definition_sha256'] == C['state_comparison_definition_sha256'])
    M = primary['modes']
    n = 3 * M + 1
    check('all_states_same_gauge_and_material_chart', M == 28 and manifest['complete_state_count'] == n and
          [r['state_index'] for r in state['state_bounds']] == list(range(n)) and
          binary(primary['gauge_amplitude']) == rational(C['gauge']) == binary(manifest['input_identity']['gauge']) and
          primary['chart_reference_coefficients'] == manifest['input_identity']['chart_reference_coefficients'] and
          primary['chart_reference_frequencies'] == manifest['input_identity']['chart_reference_frequencies'])
    check('same_actual_full_meridian_chart_blend', binary(primary.get('chart_transition_start', 0)) == 0 and
          binary(primary.get('chart_transition_end', 1)) == 1)
    gauge = rational(C['gauge'])
    L = binary(primary['meridian_length'])
    e0, e1, e2 = map(dy, B['global_explicit_repair_C0_C1_C2_upper'])
    errors = {r['jet']: dy(r['combined_paid_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}
    check('all_seven_actual_nonmean_jets_present', set(errors) == {'X', 'Xs', 'Xpsi', 'Xss', 'Xspsi', 'Xpsipsi', 'Xspsipsi'})
    base = {k: rational(v) for k, v in C['global_dimensionless_base_jet_upper'].items()}
    phaseA = rational(C['full_angle_sums']['arc_offset_A'])
    rhoB = rational(C['full_angle_sums']['rho_variation_B'])
    b1, b2 = map(rational, C['global_chart_weight_first_second'])
    rho_min = 1 - rhoB
    check('whole_fixed_chart_transport_denominator_positive', rho_min > 0)
    nu = b1 * phaseA / rho_min
    nu_s = b2 * phaseA / rho_min + b1*b1*phaseA*rhoB/rho_min**2
    repair0 = [dy(r['global_correction_C0_C1_C2'][0]) for r in state['state_bounds']]
    repair1 = [dy(r['global_correction_C0_C1_C2'][1]) for r in state['state_bounds']]
    w1, w2 = [], []
    for j in range(n):
        m = 2 * ((j-1) % M + 1) if j else 0
        w1.append(m if j else 1)
        w2.append(m*m + (j <= 2*M) if j else 1)
    state_masses = []
    radial_cursor = Q(0)
    for chunk in manifest['radial_chunks']:
        path = Path(chunk['path'])
        check('every_original_radial_chunk_SHA_matches', sha(path) == chunk['sha256'])
        identities[str(path)] = chunk['sha256']
        data = read(path)
        check('same_complete_original_radial_identity', data['input_identity_sha256'] == manifest['input_identity_sha256'])
        for row in data['rows']:
            index = row['original_interval']
            left, right = map(Q, row['s_interval'])
            check('every_original_radial_interval_in_order', index == len(state_masses) and left == radial_cursor and left < right)
            check('complete_value_and_first_radial_jets', len(row['state_jet_intervals'][0]) == len(row['state_jet_intervals'][1]) == n)
            A0 = [max(abs(dy(z[0])), abs(dy(z[1]))) + r for z, r in zip(row['state_jet_intervals'][0], repair0)]
            A1 = [max(abs(dy(z[0])), abs(dy(z[1]))) + r for z, r in zip(row['state_jet_intervals'][1], repair1)]
            state_masses.append([gauge * sum((weight*x for weight, x in zip(weights, values)), Q(0))
                                 for weights, values in ((w1, A0), (w1, A1), (w2, A0), (w2, A1))])
            radial_cursor = right
    check('all_original_radial_intervals_and_endpoints_consumed', len(state_masses) == manifest['original_physical_intervals'] == 2227 and radial_cursor == L)
    results = []
    cursor = Q(0)
    integral = Q(0)
    max_hs = Q(0)
    max_hss = Q(0)
    max_hs_index = max_hss_index = -1
    for index, row in enumerate(domain['rows']):
        left, right = map(Q, row['s_interval'])
        check('complete_domain_cover_consumed_in_original_physical_order', left == cursor and left < right)
        cursor = right
        check('entire_actual_homotopy_domain_strictly_positive', row['positive_domain'] and
              all(binary(row[k]) > 0 for k in ('radius_lower', 'chart_rho_lower', 'normalized_P_lower', 'normalized_W_lower', 'normalized_D_lower')))
        piece = B['piece_rows'][row['background_piece']]
        a = aq(binary(row['radius_lower']))
        t = aq(binary(row['speed_absolute_upper']))
        # Adding the repair again remains conservative if the background row
        # already encloses its full repaired second derivative.
        ts_exact = dy(piece['continuous_second_absolute_upper']) + dy(piece['quintic_repair_uniform_C0_C1_C2_upper'][2])
        ts = aq(ts_exact)
        Pu = aq(binary(row['normalized_P_upper']))
        Wu = aq(binary(row['normalized_W_upper']))
        Du = aq(binary(row['normalized_D_upper']))
        Wl = aq(binary(row['normalized_W_lower']))
        Dl = aq(binary(row['normalized_D_lower']))
        U = Pu.sqrt()
        V = sum((aq(binary(z))**2 for z in row['normalized_v_absolute_upper']), arb(0)).sqrt()
        mass = state_masses[row['original_interval']]
        Cpsi0, Cpsi1, Cpsi20, Cpsi21 = [aq(q) / a for q in mass]
        Us = aq(base['Bspsi']) + Cpsi1 + t*Cpsi0/a
        Vs = aq(base['Bspsipsi']) + Cpsi21 + t*Cpsi20/a
        Ul = (aq(errors['Xpsi']) + aq(e0)*U) / a
        Vl = (aq(errors['Xpsipsi']) + aq(e0)*V) / a
        Uls = (aq(errors['Xspsi']) + aq(e1)*U + t*Ul + aq(e0)*Us) / a
        Vls = (aq(errors['Xspsipsi']) + aq(e1)*V + t*Vl + aq(e0)*Vs) / a
        uj = [U, Ul, Us, Uls]
        vj = [V, Vl, Vs, Vls]
        tj = [t, aq(e1), ts, aq(e2)]
        Fj = vector_formula_majorants(uj, vj, tj, Pu, Wu, Du, Wl, Dl)
        full_lambda = Fj[1] + aq(nu*errors['Xpsi'])
        full_lambda_s = Fj[3] + aq(nu_s*errors['Xpsi'] + nu*errors['Xspsi'])
        paid = [upper(full_lambda), upper(full_lambda_s)]
        hs, hss = map(dy, paid)
        check('finite_positive_complete_uniform_mean_majorants', hs >= 0 and hss >= 0)
        contribution = (right-left)*hs
        integral += contribution
        if hs > max_hs:
            max_hs, max_hs_index = hs, index
        if hss > max_hss:
            max_hss, max_hss_index = hss, index
        results.append(dict(atom=index, original_interval=row['original_interval'], background_piece=row['background_piece'],
            s_interval=row['s_interval'], full_real_psi_and_repair_homotopy=True,
            normalized_input_jets_value_lambda_s_lambdas={k: [upper(z) for z in value] for k, value in [('u',uj),('v',vj),('a_s',tj)]},
            actual_domain_lower_upper={k: row[k] for k in ('radius_lower','normalized_P_upper','normalized_W_lower','normalized_W_upper','normalized_D_lower','normalized_D_upper')},
            normal_velocity_lambda_lambdas_upper=[upper(Fj[1]),upper(Fj[3])],
            complete_uniform_mean_Hs_Hss_difference_upper=paid,
            exact_height_contribution_before_final_rounding=str(contribution)))
        if (index+1) % 512 == 0:
            print(json.dumps(dict(event='complete_mean_repair_atoms', atoms=index+1,
                                 current_Hs=float(max_hs), current_Hss=float(max_hss),
                                 rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    check('all_continuous_domain_atoms_and_single_anchor_consumed', cursor == L and len(results) == domain['continuous_product_atoms'] == 3152)
    full_errors = [upper(aq(z)) for z in (integral, max_hs, max_hss)]
    nonmean_plus_mean = {key: upper(aq(errors[key] + {'X': integral, 'Xs': max_hs, 'Xss': max_hss}.get(key,Q(0)))) for key in errors}
    output = dict(schema='actual-q106-complete-uniform-mean-C2-repair-transfer-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),input_sha256=identities,
        all_gates=True,gate_count=sum(counts.values()),gate_multiplicities=counts,primary_sha256=sha(args.primary),
        background_comparison_definition_sha256=B['comparison_definition_sha256'],state_comparison_definition_sha256=state['comparison_field_definition_sha256'],
        complete_atoms=len(results),original_intervals=2227,rows=results,
        global_complete_mean_H_Hs_Hss_repair_difference_upper=full_errors,
        global_display_H_Hs_Hss=[float(dy(z)) for z in full_errors],
        maximizing_Hs_atom=max_hs_index,maximizing_Hss_atom=max_hss_index,
        complete_Cartesian_repair_jet_upper=nonmean_plus_mean,
        transport_fixed_in_homotopy=True,nu_and_nu_s_wholefield_upper=[upper(aq(nu)),upper(aq(nu_s))],
        mean_measure='dpsi/(2*pi), identical for all homotopy parameters',
        mean_anchor='H(0)=0 for both comparison fields; every positive physical-s atom width paid once',
        derivatives='positive norm jets (value,lambda,s,lambda-s); full nu_s transport term included',
        original_floating_evaluation_alignment_quadrature_or_target_g_certified=False,
        PDE_metric_reach_or_closed_surface_certified=False,original_g_or_accepted_candidate_modified=False,
        new_ODE_Node_Newton_or_spatial_sampling_calls=0,elapsed_seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    payload=(json.dumps(output,separators=(',',':'))+'\n').encode()
    if args.out.suffix=='.gz':
        with args.out.open('wb') as f:
            with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as g:
                g.write(payload)
    else:
        args.out.write_bytes(payload)
    print(json.dumps(dict(event='complete_mean_repair_finished',all_gates=True,gates=output['gate_count'],
                         atoms=len(results),H_Hs_Hss=output['global_display_H_Hs_Hss'],
                         path=str(args.out),sha256=sha(args.out),bytes=args.out.stat().st_size)),flush=True)


if __name__ == '__main__':
    main()
