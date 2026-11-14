#!/usr/bin/env python3
"""Finite exact modal enclosure refinement of the existing R74 auxiliary head.

Target cell12 only, all46 low modes, all20 R74 parameter axes, canonical
reference strip2.  The field is the already existing low46 auxiliary
solution, not the full head and not an outer solution.  Each finite pass
substitutes known caps into its unchanged fixed-point identity.  No new
existence or floating convergence assertion is used.

R23's material proof gives integral S*c_bg*L^2 <= B12/16 and
sup L*X <= B12*X/32.  R106's coefficientwise quadratic bound23/18
and complete mean/inverse remainder13R^3 therefore give source bounds
(23/288)*B12*(canonical positive convolution) and
(13/16)*B12*Rmax*X^2.  Both Fourier halves, the quadratic zero-mode
interaction with the inverse, all inverse powers and the true far lift
are retained.  This is L1-r source control, not a source radial supremum.

All decisions and inequalities below use fractions.  Decimal output is
only a display of outward dyadic bounds.  No ODE, Arb, Node, numerical
field or outer-centre spectral enclosure is used.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_CEILING, localcontext
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

sys.set_int_max_str_digits(0)

PINS = {
    'reference': ('2026-11-12-closure-newg-strong-m20-real-reference.json',
        'd87a6862836c31f9cb72ed9b8ad74c0ee618797e45a83785c8206a83455233cb'),
    'box': ('2026-11-12-closure-newg-strong-m20-real-box.json',
        '81f8f89aa5ca4ce18d4ea55c33e5fc0d63a8f1776090725af0ab032bc2e703c7'),
    'family': ('2026-11-12-root-anisotropic-auxiliary-family-r3.json.gz',
        '4306f0641856e85a8390dee4c22271dbefe1c6c3c7934f9c9b9a1ec6195ad866'),
    'columns': ('2026-11-12-closure-real-linear-q003-low46-recovered.json.gz',
        'cabdb3fca1d9176b1f2c46a2f7b2ff5b82ff1af426c4c942c7863c3c15c65f91'),
    'ordered': ('2026-11-12-closure-ordered-green-low46-v2.json.gz',
        '482a56deff89bb0e330690713fb33afc3d6f478dc02e58c8f765d2a12fc25ce0'),
    'green': ('2026-11-12-closure-newg-strong-m20-real-green.json.gz',
        '40d5fe5eef1ed986393ffc74a597b34b4ae64cca96b14b1c32580d13037d0bc1'),
    'outside': ('2026-11-13-inner-aux-cell12-outside-floor-r1.json.gz',
        '28e68f029dc61e22192407ee8b8c49c549ee37ab957b31c76d082b1f1bbbf02d'),
}
PROOF_PINS = {
    'R23-warped-head-complete-nonlinear-source-budget.md':
        'e5c2cbd6f705c6e16ce8c3930c96ce9b744e4fd0966428c970a6ed5d87b1d6cc',
    'R106-physical-correlation-and-complete-mean-remainder.md':
        '73746195d586cb85a4270d1a9084e1296ddddbf730d5591b534cb8c1876b2961',
    'R110-exact-canonical-inner-source-and-cut-functional.md':
        '0644ca7544cc5b0b5a28787f2f1c01d6ed83096de6163ca614c0be354b9c233e',
}
MODES = list(range(2, 93, 2))
CELLS = list(range(12, 225))
BITS = 160


def p2(e):
    return F(2) ** int(e)


def endpoint(obj):
    return F(int(obj['mantissa'])) * p2(obj['binary_exponent'])


def upper(obj):
    return endpoint(obj['upper'])


def lower(obj):
    return endpoint(obj['lower'])


def exact(obj):
    lo, hi = lower(obj), upper(obj)
    if lo != hi:
        raise ArithmeticError('An exact saved dyadic was required')
    return lo


def compact_value(obj):
    m, e = obj['upper_dyadic']
    return F(int(m)) * p2(e)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def up(x, bits=BITS):
    """A positive dyadic upper bound with at most bits significant bits."""
    x = F(x)
    if x < 0:
        raise ArithmeticError('Positive upper bound required')
    if not x:
        return F(0)
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < p2(e):
        e -= 1
    step = p2(e - bits + 1)
    q = x / step
    value = ((q.numerator + q.denominator - 1) // q.denominator) * step
    if value < x:
        raise ArithmeticError('Outward rounding failure')
    return value


def record(x):
    value = up(x)
    den = value.denominator
    if den & (den - 1):
        raise ArithmeticError('Dyadic serialization required')
    with localcontext() as ctx:
        ctx.prec = 28
        ctx.rounding = ROUND_CEILING
        display = str(Decimal(value.numerator) / Decimal(den))
    return dict(upper_dyadic=[str(value.numerator), -(den.bit_length() - 1)],
                decimal_upward=display)


def load_pinned(path, expected, identities):
    raw = path.read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected:
        raise ValueError('Pinned immutable input differs: ' + str(path))
    identities[str(path)] = dict(sha256=actual, bytes=len(raw))
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--notes', type=Path, default=Path('notes'))
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--passes', type=int, default=32)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh result path')
    if not 1 <= args.passes <= 128:
        raise ValueError('A declared finite pass count between1 and128 is required')
    started = time.monotonic()
    identities = {}
    docs = {key: load_pinned(args.notes / name, wanted, identities)
            for key, (name, wanted) in PINS.items()}
    proof_identities = {}
    for name, wanted in PROOF_PINS.items():
        path = args.notes.parent / 'results' / name
        actual = digest(path)
        if actual != wanted:
            raise ValueError('Cited proof changed: ' + str(path))
        proof_identities[str(path)] = actual
    ref, box, family, columns, ordered, green, outside = (
        docs[k] for k in ('reference', 'box', 'family', 'columns',
                         'ordered', 'green', 'outside'))
    gates = {}

    def check(name, truth):
        gates[name] = bool(truth)
        if not truth:
            raise ArithmeticError('Unpaid spectral-bootstrap gate: ' + name)

    check('R74_existing_family_all_gates', family['all_gates'] is True
          and all(family['gates'].values()))
    check('R39_exact_reference_identity', all(ref['checks'].values()))
    check('R39_original_box_all_gates', all(box['gates'].values()))
    check('all46_reference_modes', ref['modes'] == MODES)
    check('all46_original_linear_modes', columns['modes'] == MODES)
    check('all46_original_ordered_modes', ordered['modes'] == MODES
          and [r['mode'] for r in ordered['mode_rows']] == MODES)
    check('all46_original_plateau_green_modes', green['modes'] == MODES)
    check('all20_independent_R74_axes',
          [r['mode'] for r in family['parameter_axes']] == MODES[:20])
    check('all213_original_reference_rows', [r['cell'] for r in ref['cell_rows']] == CELLS)
    check('all213_original_box_rows', [r['cell'] for r in box['rows']] == CELLS)
    check('all213_R74_auxiliary_rows', [r['cell'] for r in family['auxiliary_rows']] == CELLS)
    check('outside212_plus_true_far_gates', outside['all_gates'] is True
          and all(outside['gates'].values()))
    check('outside_budget_same_target_strip_and_modes',
          outside['target_cell'] == 12
          and outside['canonical_reference_strip'] == 2
          and outside['all46_modes_retained'] == MODES)
    check('target12_original_tau_exactly2', exact(ref['cell_rows'][0]['tau']) == 2)
    for key in ('reference', 'box', 'family', 'green'):
        path, wanted = PINS[key]
        entry = outside['input_identities']['notes/' + path]
        check('outside_same_' + key, entry['sha256'] == wanted)
    for key in ('reference', 'box', 'columns'):
        path, wanted = PINS[key]
        check('R74_same_' + key, family['input_hashes']['notes/' + path] == wanted)
    for key in ('reference', 'columns', 'ordered'):
        path, wanted = PINS[key]
        check('R39_green_same_' + key, green['input_hashes']['notes/' + path] == wanted)
    check('ordered_same_linear_columns',
          ordered['input_hashes']['notes/' + PINS['columns'][0]] == PINS['columns'][1])
    check('reference_same_true_linear_columns',
          ref['input_hashes']['notes/' + PINS['columns'][0]] == PINS['columns'][1])

    S = exact(family['envelope_factor'])
    alpha = exact(family['total_linear_factor'])
    kappa_A = exact(family['auxiliary_nonlinear_factor'])
    check('exact_R74_constants', S == F(257, 256)
          and alpha == F(513, 512) and kappa_A == F(259, 256))
    row12 = ref['cell_rows'][0]
    x_lo, x = lower(row12['reference_X']), upper(row12['reference_X'])
    check('same_chosen_R74_reference_upper',
          compact_value(outside['original_R74_reference_x12']) >= x > 0)
    U = exact(box['rows'][0]['total_radius_multiple'])
    v = exact(box['rows'][0]['correction_radius_multiple'])
    rho_original = exact(family['auxiliary_rows'][0]['nonlinear_radius_multiple'])
    check('same_complete_original_auxiliary_radius', U == 1 + v
          and rho_original == kappa_A * v)
    check('whole_R74_field_envelope', alpha + rho_original <= S * U)
    check('original_R23_domain_on_entire_family',
          S * U * upper(row12['relative_to_R23_radius']) < 1)
    # The original stored source bound encloses B12*x_ref^2.  Use the
    # LOWER reference endpoint to extract an upper bound on B12.
    B = upper(row12['complete_R23_source_L1']) / (x_lo * x_lo)
    beta = up(B * x)  # beta >= B12*x; all iteration variables are /x.
    source_unit = beta * x
    outside_hat = up(compact_value(outside['fixed_outside_plus_far']) / x)
    check('positive_unchanged_other_cell_and_far_budget', outside_hat > 0)
    check('retained_true_far_strictly_positive',
          compact_value(outside['direct_true_far_contribution']) > 0)
    check('outside_budget_lt_original_radius_2minus50',
          outside_hat < rho_original * p2(-50))
    # Elementary rigorous exponential bounds, not floating evaluation.
    exp_upper, exp_lower = F(87, 32), F(8, 3)
    check('elementary_e_upper', F(1631, 600) < exp_upper)
    check('elementary_e_lower', sum((F(1, z) for z in (1, 1, 2, 6)), F(0)) == exp_lower)
    check('R106_quadratic_and_complete_cubic_constants',
          F(23, 18) / 16 == F(23, 288)
          and F(36640, 3009) < 13)

    by_ref = {row['mode']: row for row in ref['endpoint_rows']}
    by_axis = {row['mode']: row for row in family['parameter_axes']}
    by_ordered = {row['mode']: next(v for v in row['refined_cells'] if v['cell'] == 12)
                  for row in ordered['mode_rows']}
    group_bindings = {r['path']: r for r in family['original_column_groups']}
    linear_q, linear_xi, kernel_q, kernel_xi, mode_ledger = {}, {}, {}, {}, []
    seen_modes = []
    for group_ref in columns['column_groups']:
        spelling, wanted = group_ref['path'], group_ref['sha256']
        name = Path(spelling).name
        check('R74_group_identity_' + name,
              group_bindings[spelling]['sha256'] == wanted
              and group_bindings[spelling]['all213_cells'] is True)
        check('reference_group_identity_' + name, ref['input_hashes'][spelling] == wanted)
        check('ordered_group_identity_' + name, ordered['input_hashes'][spelling] == wanted)
        check('plateau_group_identity_' + name, green['input_hashes'][spelling] == wanted)
        group = load_pinned(args.notes / name, wanted, identities)
        gm = group['modes']
        check('all_original_group_modes_' + name, gm == group_ref['modes']
              and gm == group_bindings[spelling]['modes'])
        check('all213_group_cells_' + name, [r['cell'] for r in group['cell_rows']] == CELLS)
        check('all213_group_mode_orders_' + name,
              all([v['mode'] for v in r['linear_rows']] == gm for r in group['cell_rows']))
        check('group_endpoint_order_' + name, [r['mode'] for r in group['endpoint_rows']] == gm)
        for ep, lin in zip(group['endpoint_rows'], group['cell_rows'][0]['linear_rows']):
            m = ep['mode']
            seen_modes.append(m)
            gain = ep['Q_gain']
            lo, hi = lower(gain), upper(gain)
            check('nonzero_true_height_chart_' + str(m), lo > 0 or hi < 0)
            check('same_reference_gain_' + str(m),
                  lo == lower(by_ref[m]['Q_gain']) and hi == upper(by_ref[m]['Q_gain']))
            gain_min = lo if lo > 0 else -hi
            whole_q = upper(lin['column_Q_sup']) / gain_min
            whole_xi = upper(lin['column_Xi_sup']) / gain_min
            ordered_row = by_ordered[m]
            phi_q = min(whole_q, upper(ordered_row['refined_phi_Q_sup']))
            phi_xi = min(whole_xi, upper(ordered_row['refined_phi_Xi_sup']))
            check('positive_true_normalized_columns_' + str(m), phi_q > 0 and phi_xi > 0)
            if m in by_axis:
                axis = by_axis[m]
                centre, half_axis = exact(axis['exact_centre']), exact(axis['half_axis'])
                check('actual_R74_centre_' + str(m), centre == exact(by_ref[m]['reference_Q']))
                check('complete_R74_axis_' + str(m),
                      exact(axis['lower']) == centre - half_axis
                      and exact(axis['upper']) == centre + half_axis
                      and half_axis == abs(centre) * exact(axis['relative_radius']))
                amplitude = abs(centre) + half_axis
            else:
                amplitude = F(0)
                check('all26_zero_shallow_linear_heights_' + str(m),
                      exact(by_ref[m]['reference_Q']) == 0)
            e_weight = exp_upper ** (2 * m)
            linear_q[m] = up((1 + m) ** 3 * e_weight * amplitude * phi_q / x)
            linear_xi[m] = up((1 + m) * e_weight * amplitude * phi_xi / x)
            Kq = upper(ordered_row['component_kernel']['Q_kernel'])
            Kxi = upper(ordered_row['component_kernel']['Xi_kernel'])
            check('positive_original_ordered_component_kernels_' + str(m), Kq > 0 and Kxi > 0)
            Ktotal = (1 + m) ** 3 * Kq + (1 + m) * Kxi
            check('component_sum_in_original_ordered_bound_' + str(m),
                  Ktotal <= upper(ordered_row['kernel_bound']))
            check('component_sum_in_original_plateau_bound_' + str(m),
                  Ktotal <= p2(green['gamma_log2_upper'][0][0]))
            kernel_q[m] = up((1 + m) ** 3 * Kq * beta)
            kernel_xi[m] = up((1 + m) * Kxi * beta)
            mode_ledger.append(dict(mode=m,linear_support=m in by_axis,
                shallow_height_modulus=record(amplitude),
                true_normalized_phi_Q_sup=record(phi_q),
                true_normalized_phi_Xi_sup=record(phi_xi),
                original_cell12_Q_kernel=record(Kq),
                original_cell12_Xi_kernel=record(Kxi),
                linear_weighted_Q_over_reference=record(linear_q[m]),
                linear_weighted_Xi_over_reference=record(linear_xi[m]),
                source_response_Q_factor=record(kernel_q[m]),
                source_response_Xi_factor=record(kernel_xi[m]),
                original_group_path=spelling,original_group_sha256=wanted))
        del group
    check('all46_true_columns_and_kernels_consumed', seen_modes == MODES)

    linear = {m: linear_q[m] + linear_xi[m] for m in MODES}
    kernel = {m: kernel_q[m] + kernel_xi[m] for m in MODES}
    max_kernel = max(kernel.values())
    linear_total = min(alpha, sum(linear.values(), F(0)))
    qconstant = F(23, 288)
    rconstant = F(13, 16)
    # For opposite signs, exact strip2 correlation is exp(-4*min(|a|,|b|)).
    # e>8/3 gives this positive rational upper bound.  No angular weight
    # is silently changed and both signed halves are included.
    difference_weights = {m: (1 / exp_lower) ** (4 * m) for m in MODES}
    pairs = {m: ([(a, m - a) for a in MODES if m - a in linear],
                 [(a, a + m) for a in MODES if a + m in linear])
             for m in MODES}
    check('positive_same_tau_correlation_weights',
          all(0 < w <= 1 for w in difference_weights.values()))

    def source_bounds(error_caps, common_error):
        error_total = min(common_error, sum(error_caps.values(), F(0)))
        X = min(S * U, linear_total + error_total)
        cap = {m: min(linear[m] + error_caps[m], X) for m in MODES}
        conv = {}
        for m in MODES:
            addition, difference = pairs[m]
            value = sum((cap[a] * cap[b] / 2 for a, b in addition), F(0))
            value += sum((cap[a] * cap[b] * difference_weights[a]
                          for a, b in difference), F(0))
            conv[m] = min(up(value), up(X * X))
        Rmax = up(beta * X / 32)
        rem = up(rconstant * Rmax * X * X)
        return X, cap, conv, Rmax, rem

    errors = {m: rho_original for m in MODES}
    rho = rho_original
    iterations = []
    for step in range(1, args.passes + 1):
        X, cap, conv, Rmax, rem = source_bounds(errors, rho)
        check('full_complete_mean_and_inverse_domain_pass_' + str(step), Rmax <= p2(-16))
        quadratic_map = qconstant * min(
            sum((kernel[m] * conv[m] for m in MODES), F(0)),
            max_kernel * X * X)
        complete_map = up(quadratic_map + max_kernel * rem + outside_hat)
        rho_new = min(rho, complete_map)
        new_errors = {
            m: min(errors[m], rho_new,
                   up(kernel[m] * (qconstant * conv[m] + rem) + outside_hat))
            for m in MODES}
        rho_new = min(rho_new, up(sum(new_errors.values(), F(0))))
        new_errors = {m: min(value, rho_new) for m, value in new_errors.items()}
        check('finite_induction_monotone_all46_pass_' + str(step),
              0 < rho_new <= rho and all(0 < new_errors[m] <= errors[m] for m in MODES))
        check('fixed_positive_outside_budget_retained_pass_' + str(step),
              complete_map >= outside_hat)
        iterations.append(dict(pass_index=step,
            input_common_error_over_reference=record(rho),
            common_total_field_over_reference=record(X),
            complete_relative_physical_norm=record(Rmax),
            complete_mean_inverse_source_remainder_over_Bx2=record(rem),
            common_quadratic_response_over_reference=record(quadratic_map),
            common_complete_response_over_reference=record(complete_map),
            output_common_error_over_reference=record(rho_new),
            modal_error_over_reference=[dict(mode=m,bound=record(new_errors[m])) for m in MODES],
            all46_input_pair_convolutions=[dict(mode=m,bound=record(conv[m])) for m in MODES]))
        errors, rho = new_errors, rho_new
    X, cap, conv, Rmax, rem = source_bounds(errors, rho)
    check('final_complete_mean_and_inverse_domain', Rmax <= p2(-16))
    check('original_common_mass_kept_in_parallel', rho <= rho_original and X <= S * U)
    check('all46_final_nonzero_error_caps', all(errors[m] > 0 for m in MODES))
    check('full_mean_inverse_remainder_not_deleted', rem > 0)
    final_rows = []
    for m in MODES:
        quad = up(qconstant * conv[m] * source_unit)
        full = up((qconstant * conv[m] + rem) * source_unit)
        final_rows.append(dict(mode=m,
            auxiliary_error_pair_mass_over_reference=record(errors[m]),
            auxiliary_error_pair_mass=record(errors[m] * x),
            complete_field_pair_mass_over_reference=record(cap[m]),
            positive_pair_convolution_over_reference_squared=record(conv[m]),
            quadratic_source_canonical_L1_pair=record(quad),
            complete_source_pair_with_common_remainder=record(full),
            full_pair_source_over_old_whole_cell_source=record(full / (source_unit * (S * U) ** 2)),
            error_over_original_complete_error_radius=record(errors[m] / rho_original)))
    final_source_common = up(source_unit * (
        qconstant * min(sum(conv.values(), F(0)), X * X) + rem))
    result = dict(status='Finite exact modal refinement of the already proved full R74 auxiliary family',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        source_sha256=digest(__file__),input_identities=identities,
        cited_proof_identities=proof_identities,all_gates=all(gates.values()),gates=gates,
        parameter_domain=family['parameter_domain'],parameter_axes=family['parameter_axes'],
        target_cell=12,canonical_reference_strip=2,all46_modes_retained=MODES,
        auxiliary_field_support=MODES,complete_source_support='All even frequencies; only the auxiliary response is projected to low46',
        existing_solution='The exact R39/R74 low46 auxiliary solution, with full mean and true nonlinear far lift',
        normalization='All modal and total state masses are divided by the original chosen R74 x12 upper endpoint; positive rows are cosine pairs (two Fourier halves)',
        reference_x12=record(x),B12_upper=record(B),B12_times_reference_upper=record(beta),
        source_unit_B12_reference_squared=record(source_unit),
        fixed_other212_plus_true_far_over_reference=record(outside_hat),
        original_common_error_over_reference=record(rho_original),
        original_common_error_mass=record(rho_original * x),
        original_R74_common_linear_over_reference=record(alpha),
        independent_new_linear_common_over_reference=record(linear_total),
        original_R74_complete_field_over_reference=record(S * U),
        constants=dict(material_integral_B_factor='1/16',physical_norm_BX_factor='1/32',
            physical_quadratic='23/18',canonical_quadratic='23/288',
            complete_mean_inverse_cubic='13',canonical_complete_remainder='13/16',
            e_upper='87/32',e_lower='8/3',rounding_significant_bits=BITS),
        recurrence=dict(modal='E_m_new=min(E_m,rho_new,ceil(A_m*((23/288)*conv_m+rem)+outside))',
            common='rho_new=min(rho,ceil((23/288)*min(sum(A_m*conv_m),Amax*X^2)+Amax*rem+outside),sum(E_m_new))',
            source='rem=(13/16)*Rmax*X^2, Rmax=(B*x)*X/32; all bounds rounded upward',
            convolution='conv_m=(1/2)*sum_{a+b=m,a,b>0}c_a*c_b + sum_{a>0,a+m<=92}c_a*c_(a+m)*(3/8)^(4*a), clipped by the independent common X^2',
            outside_and_remainder_charged_once_in_common_row=True),
        linear_and_kernel_rows=mode_ledger,finite_passes=args.passes,iterations=iterations,
        final_common_error_over_reference=record(rho),
        final_common_error_mass=record(rho * x),
        final_common_error_over_original_radius=record(rho / rho_original),
        final_complete_field_common_over_reference=record(X),
        final_relative_physical_norm=record(Rmax),
        final_common_complete_mean_inverse_source_remainder=record(source_unit * rem),
        final_common_low46_source_canonical_L1=record(final_source_common),
        final_modal_rows=final_rows,
        common_mass_warning='Individual caps and the independent common l1 radius are simultaneous inequalities. Never sum separately allocated copies of the common outside or complete remainder budget and call that the single common budget.',
        scope='Same R74 full parameter domain and same original g only. This is not the full inner head, not a new outer solution, not a q096/q098 certificate, and not yet a complete cut or closed-surface certificate.',
        no_new_ODE=True,no_new_Green=True,no_new_Arb=True,no_new_source_integral=True,no_Node=True,
        outer_R101_centre_spectrum_used=False,new_existence_claimed=False,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw = (json.dumps(result, ensure_ascii=False, indent=2) + '\n').encode()
    payload = gzip.compress(raw, mtime=0) if args.out.suffix == '.gz' else raw
    if len(payload) >= 5_000_000:
        raise ValueError('Per-file repository cap exceeded')
    if len(raw) > 1_000_000 and args.out.suffix != '.gz':
        raise ValueError('Large output must use gzip')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('xb') as stream:
        stream.write(payload)
    chosen = {r['mode']:r for r in final_rows if r['mode'] in (2,4,6,12,14,16,40,92)}
    print(json.dumps(dict(out=str(args.out),sha256=digest(args.out),all_gates=result['all_gates'],
        gates=len(gates),passes=args.passes,
        final_common_error_over_reference=result['final_common_error_over_reference'],
        final_common_error_over_original_radius=result['final_common_error_over_original_radius'],
        final_relative_physical_norm=result['final_relative_physical_norm'],
        complete_remainder=result['final_common_complete_mean_inverse_source_remainder'],
        selected_final_rows=chosen,seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__ == '__main__':
    main()
