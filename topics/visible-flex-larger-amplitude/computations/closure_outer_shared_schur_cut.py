#!/usr/bin/env python3
"""Actual two-mode local S0/cut component and a compatible jet recentering.

Only already validated source/flow/head certificates are consumed. The same
true scalar slope occurs in both numerator and denominator. Recentring is
an explicitly defined candidate change: its compensating linear forcing
is NOT discarded and no complete outer Schur inverse is claimed.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx

from closure_real_head_source_enclosure import exact_q, power2
from closure_split_joint_io_v2 import digest, read_field
from closure_shared_slope_cut_interface import ball, endpoint, record


def point(x):
    if not x.is_exact():
        raise ValueError('An explicit dyadic centre must be exact')
    m, e = x.man_exp()
    return dict(mantissa=str(m), binary_exponent=int(e))


def hull(x, y):
    return x.union(y)


def compact(x):
    return arb((int(x[0]), int(x[1])))


def input_guard(path, hashes, expected):
    if hashes.get(str(path)) != expected:
        raise ValueError('The same frozen input is required: '+str(path))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('flow', 'signed-cut', 'cut', 'ready', 'candidate11', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--rss-kib', type=int, default=40960)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh actual local Schur output')
    ctx.prec, ctx.threads = 256, 1
    began = time.monotonic()
    names = ('flow', 'signed_cut', 'cut', 'ready', 'candidate11')
    hashes = {str(getattr(args, name)): digest(getattr(args, name)) for name in names}
    flow = json.loads(args.flow.read_text())
    signed = json.loads(args.signed_cut.read_text())
    cut = json.loads(args.cut.read_text())
    candidate = json.loads(args.candidate11.read_text())
    if (not all(flow['gates'].values()) or not signed['all_gates'] or not cut['all_gates']
            or not all(candidate['gates'].values()) or candidate['cell'] != 11
            or signed['modes'] != [2, 4] or flow['config']['modes'] != [2, 4]
            or flow['config']['cells'] != [11, 10]):
        raise ValueError('Every full actual input certificate must have passed')
    input_guard(args.cut, signed['input_hashes'], hashes[str(args.cut)])
    input_guard(args.ready, flow['input_hashes'], hashes[str(args.ready)])
    input_guard(args.ready, candidate['input_hashes'], hashes[str(args.ready)])
    for name, sha in signed['input_hashes'].items():
        if name.endswith('-port-norms-recovery.json'):
            if candidate['input_hashes'].get(name) != sha:
                raise ValueError('The candidate trace has changed')
    slope_paths = {name: sha for name, sha in signed['input_hashes'].items()
                   if 'taylor-cut-' in name}
    if len(slope_paths) != 1 or any(flow['input_hashes'].get(name) != sha
                                   for name, sha in slope_paths.items()):
        raise ValueError('The common true linear slope was not shared')
    rows = {r['mode']: r for r in signed['rows']}
    B0 = {r['mode']: r for r in cut['B0']}
    derivatives = cut['nonlinear_derivative_columns']
    if sorted(B0) != list(range(2, 93, 2)) or [r['input_mode'] for r in derivatives] != list(range(2, 93, 2)):
        raise ValueError('The true full46 parameter domain must be retained')
    b, wb, mu = (ball(signed[k]) for k in ('true_radius', 'true_w', 'outer_mu11'))
    co = ball(signed['K_per_unit_mu11_slope'])
    if not b > 0 or not wb > 0 or not mu > 0 or not co > 0:
        raise ArithmeticError('A true physical conversion is not positive')
    identity = next(x for x in flow['source_identity'] if x['cell'] == 11)
    if not all(identity[k] for k in ('cap_strictly_inactive', 'valley_control_exact_zero',
                                    'warp_weight_exact_one', 'chi_and_j0_exact_one')):
        raise ValueError('The complete actual raw cell11 source is required')
    ready = dict(rationalDeepModel=read_field(args.ready, 'rationalDeepModel'),
                 shallowSourceParameters=read_field(args.ready, 'shallowSourceParameters'))
    pars = ready['rationalDeepModel']['physicalParameters']
    constants = ready['rationalDeepModel']['exactSourceConstants']
    rc = exact_q(pars['rCuff'])
    d0 = exact_q(Fraction(constants['delta0']))
    c0 = exact_q(Fraction(constants['etaRatioAtN0']))
    delta = d0*power2(-11)
    c11 = c0*(-arb(11)*arb(2).log()/2).exp()
    q32 = (-arb(3)*arb(2).log()/2).exp()
    after = 3*delta+6*c0*d0*q32**12/(1-q32)
    ro_outer = rc*((after+delta*(3+6*c11))/arb(12).sqrt()).exp()
    R, alpha = ball(identity['R']), ball(identity['alpha'])
    rho = (arb(11)*arb(2).log()/4).exp()
    levels = [arb(1), R/delta, delta/alpha, 1/delta, rho]
    wmin = (mu*min(x.lower() for x in levels)/ro_outer**7).lower()
    wmax = ball(identity['whole_cell_raw_w_upper']).upper()
    if not 0 < wmin <= wb or not wb <= wmax < arb(1)/2:
        raise ArithmeticError('The real entire-cell slope envelope failed')
    c = ball(next(x for x in flow['cell_rows'] if x['cell'] == 11)['radius'])
    length = c-b
    if not length > 0:
        raise ArithmeticError('The actual candidate recentering collar has no positive width')
    sigma = arb(1)/64
    Rold = ball(candidate['worst']['R_tau']['value']).upper()
    if not Rold < arb(1)/64:
        raise ValueError('The original whole-cell complete-mean working domain is required')
    recentred = {}
    shift_rows = []
    relative_shift = arb(0)
    for m in (2, 4):
        row = rows[m]
        q, L = ball(row['actual_canonical_Q']), ball(row['stored_orthonormal_L'])
        shat, ds = endpoint(row['shared_exact_dyadic_slope']), ball(row['true_minus_shared_exact_slope'])
        newL = (co*shat*q/arb(2).sqrt()).mid()
        dL = newL-L
        if not dL.is_exact():
            raise ArithmeticError('The old and new saved candidate momenta must be exact dyadics')
        nonlinear = (ball(row['auxiliary_nonlinear_K_upper'])+
                     ball(row['full_head_feedback_same_mode_K_upper'])).upper()
        residual_centre = co*shat*q-arb(2).sqrt()*newL
        beta_linear = residual_centre+co*q*ds
        beta_full = beta_linear+hull(-nonlinear, nonlinear)
        physical_slope_shift = wb*arb(2).sqrt()*dL
        abs_slope_shift = abs(physical_slope_shift).upper()
        height_shift = (length*exact_q(Fraction(16, 81))*abs_slope_shift).upper()
        first_shift = abs_slope_shift
        second_shift = (9*abs_slope_shift/length).upper()
        weight = (1+m)*(sigma*m).exp()
        relative = (weight*abs_slope_shift/wmin*
                    (1+m*length*exact_q(Fraction(16, 81))/b)).upper()
        relative_shift += relative
        recentred[m] = dict(L=newL, nonlinear=nonlinear, beta=beta_full)
        shift_rows.append(dict(mode=m, old_exact_orthonormal_L=record(L),
            new_exact_dyadic_orthonormal_L=point(newL), exact_dyadic_L_shift=point(dL),
            same_canonical_Q=row['actual_canonical_Q'], nonmean_cut_height_shift_exact_zero=True,
            physical_cut_slope_shift=record(physical_slope_shift),
            height_sup_shift=record(height_shift), first_derivative_sup_shift=record(first_shift),
            second_derivative_sup_shift=record(second_shift),
            relative_A1_field_shift_upper=record(relative),
            new_signed_linear_minus_candidate_K=record(beta_linear),
            retained_nonlinear_K_upper=record(nonlinear),
            new_signed_complete_minus_candidate_K=record(beta_full),
            new_complete_Wsigma1_upper=record((weight*abs(beta_full).upper()).upper())))
    relative_shift = relative_shift.upper()
    Rnew = (Rold+relative_shift).upper()
    if not Rnew < arb(1)/64:
        raise ArithmeticError('The explicitly recentred candidate left the full mean domain')
    mean_shift = (16*Rnew*relative_shift).upper()
    mean_height_shift = (length*wmax*mean_shift).upper()
    output_cells = []
    for cell in flow['cell_rows']:
        mode_rows = []
        scaled_columns = {d['input_mode']: arb(0) for d in derivatives}
        for mode in cell['modes']:
            m = mode['mode']
            row = rows[m]
            if (mode['shared_exact_dyadic_slope'] != row['shared_exact_dyadic_slope']
                    or mode['true_minus_shared_exact_slope'] != row['true_minus_shared_exact_slope']):
                raise ValueError('A Schur numerator and denominator use different slope variables')
            A, B = ball(mode['S0_affine_A']), ball(mode['S0_affine_B'])
            shat, ds = endpoint(row['shared_exact_dyadic_slope']), ball(row['true_minus_shared_exact_slope'])
            slope = shat+ds
            S = ball(mode['S0_true_Q'])
            if (A+B*slope).contains(0) or S.contains(0):
                raise ArithmeticError('The common true Mobius denominator is not separated from zero')
            q, L = ball(row['actual_canonical_Q']), ball(row['stored_orthonormal_L'])
            axis = ball(row['canonical_parameter_axis'])
            coefficient = B/(co*S)
            coeff_abs = abs(coefficient).upper()
            def cut_component(s, candidate_L):
                return -B*(co*q*s-arb(2).sqrt()*candidate_L)/(co*(A+B*s))
            linear = hull(cut_component(slope.lower(), L), cut_component(slope.upper(), L))
            nonlinear = recentred[m]['nonlinear']
            correction = (coeff_abs*nonlinear).upper()
            full = linear+hull(-correction, correction)
            newL = recentred[m]['L']
            newlinear = hull(cut_component(slope.lower(), newL), cut_component(slope.upper(), newL))
            newfull = newlinear+hull(-correction, correction)
            columns = []
            for d in derivatives:
                cap = compact(d['low_K_output_coefficient_caps'][m//2-1])
                value = (coeff_abs*cap/axis).upper()
                columns.append(dict(input_mode=d['input_mode'],
                    same_full46_input_axis_log2=d['new_canonical_axis_log2'],
                    normalized_head_nonlinear_Schur_column_upper=record(value)))
                scaled_columns[d['input_mode']] += value
            mode_rows.append(dict(mode=m, S0_true_Q=mode['S0_true_Q'],
                S0_true_height=mode['S0_true_height'],
                shared_exact_dyadic_slope=row['shared_exact_dyadic_slope'],
                true_minus_shared_exact_slope=row['true_minus_shared_exact_slope'],
                K_to_canonical_cut_coefficient=record(coefficient),
                cut_only_signed_linear_canonical_Q=record(linear),
                cut_only_nonlinear_canonical_Q_radius=record(correction),
                cut_only_full_canonical_Q=record(full),
                canonical_parameter_axis=row['canonical_parameter_axis'],
                canonical_parameter_axis_log2=row['canonical_parameter_axis_log2'],
                cut_only_axis_ratio_upper=record((abs(full).upper()/axis).upper()),
                cut_only_axis_ratio_lower=record((abs(full).lower()/axis).lower()),
                recentred_cut_only_full_canonical_Q=record(newfull),
                recentred_cut_only_axis_ratio_upper=record((abs(newfull).upper()/axis).upper()),
                selected_head_DeltaB_columns=columns,
                all46_input_columns_retained=True,
                complete_outer_forcing_included=False))
        output_cells.append(dict(endpoint_physical_node=cell['endpoint_physical_node'],
            radius=cell['radius'], modes=mode_rows,
            selected_two_output_l1_column_norm_upper=record(max(v.upper() for v in scaled_columns.values())),
            selected_two_output_normalized_column_sums=[dict(input_mode=m, upper=record(v.upper()))
                for m, v in scaled_columns.items()], full46_Schur_inverse_paid=False))
    gates = dict(all_actual_dependencies_paid=True, exact_global_mu11_kept=True,
        common_slope_retained_in_each_Mobius_expression=True,
        all_four_true_height_denominators_nonzero=True,
        full46_input_head_derivative_columns_retained=True,
        old_full_mean_and_all_high_trace_still_required=True,
        two_new_candidate_L_values_exact_dyadics=True,
        all_nonmean_cut_heights_unchanged=True,
        outer_cell11_endpoint_twojet_unchanged=True,
        same_real_metric_and_same_actual_reference=True,
        recentred_complete_mean_small_domain=True,
        compensating_linear_forcing_explicitly_required=True)
    result = dict(status='Actual local S0, common-slope cut component and explicit compatible candidate recentering',
        gates=gates, all_gates=all(gates.values()), modes=[2, 4], cells=[11, 10],
        true_radius=record(b), true_w=record(wb), global_mu11=record(mu),
        K_per_unit_mu11_Xi=record(co), cell11_length=record(length),
        cell11_slope_lower=record(wmin), cell11_slope_upper=record(wmax),
        candidate_original_relative_A1_upper=record(Rold),
        candidate_relative_A1_shift_upper=record(relative_shift),
        candidate_recentred_relative_A1_upper=record(Rnew),
        complete_mean_slope_change_upper=record(mean_shift),
        complete_mean_height_change_upper=record(mean_height_shift),
        recentring_rows=shift_rows, cell_rows=output_cells,
        bump_polynomial_coefficients=[0, 1, 0, -6, 8, -3],
        bump_bounds=dict(height='16/81', first='1', second='9'),
        recentring_formula='delta h_m(r)=ell*w_b*sqrt(2)*delta L_m*B((r-b)/ell), with B=x-6x^3+8x^4-3x^5. All other nonmean modes unchanged. Full mean is the unique common root, with its one additive height constant anchored at node11.',
        exact_compensation_identity='Phi beta_new - integral(Phi L(c+delta c)) = Phi beta_old - integral(Phi Lc), since delta c(node11)=0. The true N(c+delta c) term still requires its full source bound.',
        cut_component_is_complete_residual=False,
        two_mode_local_background_inverse_paid=True,
        complete_outer_nonlinear_Schur_problem_paid=False,
        actual_source_integrals_in_Schur_norm_paid=False,
        input_hashes=hashes, entrypoint_sha256=digest(Path(__file__)),
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result['peak_RSS_KiB'] > args.rss_kib:
        raise MemoryError('The owned short ledger exceeded its RSS observation threshold')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='complete', output=str(args.out), all_gates=result['all_gates'],
        rows=[dict(node=c['endpoint_physical_node'], mode=r['mode'],
                   cut_ratio=str(ball(r['cut_only_axis_ratio_upper'])),
                   recentred_cut_ratio=str(ball(r['recentred_cut_only_axis_ratio_upper'])))
              for c in output_cells for r in c['modes']],
        relative_shift=str(relative_shift), seconds=result['elapsed_seconds'],
        peak_RSS_KiB=result['peak_RSS_KiB'])), flush=True)


if __name__ == '__main__':
    main()
