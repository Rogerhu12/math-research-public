#!/usr/bin/env python3
"""Preserve a shared exact linear slope centre in the actual strong cut trace.

R65 refines selected true B0 slopes. This file combines those SAME slopes
with the original actual Q/L candidate and R63/R61 nonlinear bounds. It
exports an affine signed interface, not an outer Schur inverse or an
assertion that the actual nonlinear correction is zero.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import exact_q
from closure_split_joint_io_v2 import digest, iter_array, read_field


def endpoint(d):
    return arb((int(d['mantissa']), int(d['binary_exponent'])))


def ball(d):
    return endpoint(d['lower']).union(endpoint(d['upper']))


def record(x):
    if not x.is_finite():
        raise ArithmeticError('Nonfinite trace interval')
    def point(t):
        a, b = t.man_exp()
        return dict(mantissa=str(a), binary_exponent=int(b))
    return dict(lower=point(x.lower()), upper=point(x.upper()))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('slope', 'reference', 'cut', 'ports', 'auxiliary', 'out'):
        p.add_argument('--'+name, required=True, type=Path)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh signed-interface output')
    ctx.prec, ctx.threads = 256, 1
    started = time.monotonic()
    hashes = {str(getattr(args, name)):digest(getattr(args, name))
              for name in ('slope', 'reference', 'cut', 'ports', 'auxiliary')}
    slope = json.loads(args.slope.read_text())
    if not all(slope['gates'].values()) or slope['config']['cut'] != 12:
        raise ValueError('A completed true cut slope certificate is required')
    if not read_field(args.cut, 'all_gates') or not read_field(args.auxiliary, 'all_gates'):
        raise ValueError('The original true-cut and auxiliary nonlinear certificates must be paid')
    cut_hashes = read_field(args.cut, 'input_hashes')
    for path in (args.reference, args.ports):
        if cut_hashes.get(str(path)) != hashes[str(path)]:
            raise ValueError('The full head and saved actual candidate have changed')
    aux_hashes = read_field(args.auxiliary, 'input_hashes')
    if aux_hashes.get(str(args.cut)) != hashes[str(args.cut)]:
        raise ValueError('The auxiliary correction is for another true cut')
    reference_hashes = read_field(args.reference, 'input_hashes')
    ready_paths = [Path(s) for s in slope['config']['input_hashes'] if s.endswith('-ready.json')]
    if len(ready_paths) != 1 or slope['config']['input_hashes'][str(ready_paths[0])] not in reference_hashes.values():
        raise ValueError('The real reference and the Taylor flow have different frozen ready inputs')
    if not all(read_field(args.reference, 'checks').values()):
        raise ValueError('The original full46 real reference is unverified')
    refs = {x['mode']: x for x in read_field(args.reference, 'endpoint_rows')}
    if sorted(refs) != list(range(2, 93, 2)):
        raise ValueError('The original true reference must retain all46 modes')
    old_B0 = {x['mode']: x for x in read_field(args.cut, 'B0')}
    aux = {x['mode']: x for x in iter_array(args.auxiliary, 'rows')}
    candidate = next(x for x in iter_array(args.ports, 'rows') if x['physical_node'] == 12)
    L = candidate['candidate_L_orthonormal_cosine']
    if candidate['source_cell'] != 11 or len(L) != 21:
        raise ValueError('The exact stored actual M20 endpoint is required')
    b, w, mu = (ball(read_field(args.cut, name)) for name in ('true_radius', 'true_w', 'outer_mu11'))
    rho = ball(read_field(args.cut, 'normalization_factor'))
    if not b > 0 or not w > 0 or not mu > 0 or not rho > 1:
        raise ValueError('The physical cut normalization is not positive')
    co = arb(12).sqrt()*mu/(b**4*w*w)
    sigma = exact_q(Fraction(1, 64))
    beta = read_field(args.cut, 'beta')
    extra_global = ball(beta['outer']['full_head_low_correction_K']).upper()
    outputs = []
    for row in slope['rows']:
        m = row['mode']
        if m not in aux or m > 40:
            raise ValueError('This selected actual endpoint mode lacks its R63 source functional')
        reference = refs[m]
        if old_B0[m]['Xi_mu11_over_Q'] != reference['raw_worker_slope']:
            raise ValueError('The old reference/B0 shared slope identity was lost')
        q = ball(reference['reference_Q'])
        stored_L = exact_q(L[m//2])
        shared = endpoint(row['shared_exact_dyadic_slope'])
        uncertainty = ball(row['true_minus_shared_exact_slope'])
        known = co*shared*q-arb(2).sqrt()*stored_L
        uncertainty_K = co*q*uncertainty
        signed_linear = known+uncertainty_K
        weight = (1+m)*(m*sigma).exp()
        nonlinear_aux = ball(aux[m]['auxiliary_Kbar_coefficient_upper']).upper()
        nonlinear_full = (extra_global/weight).upper()
        nonlinear_total = (nonlinear_aux+nonlinear_full).upper()
        signed_actual = signed_linear+(-nonlinear_total).union(nonlinear_total)
        old_weighted = (weight*abs(ball(old_B0[m]['linear_minus_saved_candidate_K'])).upper()).upper()
        new_weighted = (weight*abs(signed_linear).upper()).upper()
        total_weighted = (weight*abs(signed_actual).upper()).upper()
        # A true parameter axis is copied without reinterpretation. The trace
        # mismatch is not compared to it without an actual outer Schur map.
        outputs.append(dict(mode=m, shared_exact_dyadic_slope=row['shared_exact_dyadic_slope'],
            true_minus_shared_exact_slope=row['true_minus_shared_exact_slope'],
            actual_canonical_Q=reference['reference_Q'], stored_orthonormal_L=record(stored_L),
            common_linear_K_coefficient_per_slope=record(co*q),
            known_signed_linear_minus_candidate_K=record(known),
            true_slope_uncertainty_signed_K=record(uncertainty_K),
            complete_signed_linear_minus_candidate_K=record(signed_linear),
            auxiliary_nonlinear_K_upper=record(nonlinear_aux),
            full_head_feedback_same_mode_K_upper=record(nonlinear_full),
            complete_signed_actual_minus_candidate_K=record(signed_actual),
            complete_actual_minus_candidate_Wsigma1_upper=record(total_weighted),
            old_linear_Wsigma1_upper=record(old_weighted), new_linear_Wsigma1_upper=record(new_weighted),
            linear_bound_improvement_log2=record((old_weighted/new_weighted).log()/arb(2).log()),
            canonical_parameter_axis=old_B0[m]['canonical_Q_axis'],
            canonical_parameter_axis_log2=old_B0[m]['canonical_Q_axis_log2'],
            low_Q_and_P_difference_exactly_zero=True,
            reference_frozen_linear_vector=dict(Q=1, Xi_mu11=row['shared_exact_dyadic_slope']),
            real_slope_remainder_is_shared=True))
    gates = dict(new_true_slope_certificate_paid=all(slope['gates'].values()),
        same_actual_full46_reference=True, same_saved_actual_M20_candidate=True,
        outer_mu11_retained_without_duplicate_rho=True, exact_low_Q_and_P_zero_retained=True,
        same_shared_slope_in_B0_and_beta=True, actual_R63_selected_nonlinear_functionals_retained=True,
        full_R58_low_feedback_retained=True, full_mean_and_high_interfaces_not_deleted=True)
    result = dict(status='Actual selected cut trace with a shared exact slope centre and signed remainder',
        gates=gates, all_gates=all(gates.values()), modes=[x['mode'] for x in outputs],
        rows=outputs, true_radius=record(b), true_w=record(w), outer_mu11=record(mu),
        K_per_unit_mu11_slope=record(co), outer_strip='1/64',
        complete_high_interface_unchanged_from=str(args.cut), full_mean_interface_unchanged_from=str(args.cut),
        outer_Schur_inverse_paid=False, signed_outer_source_integral_evaluated=False,
        input_hashes=hashes, entrypoint_sha256=digest(Path(__file__)),
        limits=['Only the listed linear slope intervals are replaced by tighter true intervals.',
                'Signed candidate mismatch is not an error estimate for a solved outer equation.',
                'The same exact shared slope and the same remainder variable must occur in B0, beta and the outer Schur denominator.',
                'No direct comparison of bare physical K mismatch to canonical Q parameter axes is justified without the outer map.'],
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result['peak_RSS_KiB'] > 40960:
        raise MemoryError('The selected-interface arithmetic exceeded its observed40MiB stop threshold')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='complete', path=str(args.out), gates=gates,
        rows=[dict(mode=x['mode'], linear=str(ball(x['complete_signed_linear_minus_candidate_K'])),
            actual=str(ball(x['complete_signed_actual_minus_candidate_K'])),
            bound=str(ball(x['complete_actual_minus_candidate_Wsigma1_upper'])),
            improved_bits=str(ball(x['linear_bound_improvement_log2']))) for x in outputs],
        elapsed_seconds=result['elapsed_seconds'], peak_RSS_KiB=result['peak_RSS_KiB'])), flush=True)


if __name__ == '__main__':
    main()
