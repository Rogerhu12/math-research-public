#!/usr/bin/env python3
"""Complete R63's source-only cut bound by the already paid R39 far lift.

The original numerical packages and their source hashes remain unchanged.
All new quantities are exact Fraction operations on saved outward bounds.
R70/R71 centre intervals are enlarged explicitly; source integrals, the
R71 exact candidate, and its complete mean-height change are unchanged.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import read_field


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def p2(e):
    return Fraction(1 << e) if e >= 0 else Fraction(1, 1 << -e)


def ep(d):
    return int(d['mantissa']) * p2(int(d['binary_exponent']))


def bound(d):
    lo, hi = ep(d['lower']), ep(d['upper'])
    if lo > hi:
        raise ValueError('An outward ordered interval is required')
    return lo, hi


def cap(d):
    lo, hi = bound(d)
    return max(abs(lo), abs(hi))


def lower_abs(d):
    lo, hi = bound(d)
    if lo > 0:
        return lo
    if hi < 0:
        return -hi
    raise ArithmeticError('A proved nonzero height chart is required')


def ceil_binary(q, bits=192):
    if q < 0:
        raise ValueError('A nonnegative upper bound is required')
    if q == 0:
        return q
    k = q.numerator.bit_length() - q.denominator.bit_length()
    if q < p2(k):
        k -= 1
    unit = p2(k - bits + 1)
    r = q / unit
    return ((r.numerator + r.denominator - 1) // r.denominator) * unit


def dyadic(q):
    if q.denominator & (q.denominator - 1):
        raise ValueError('Only exact dyadic endpoints are serialized here')
    e = -(q.denominator.bit_length() - 1)
    return dict(mantissa=str(q.numerator), binary_exponent=e)


def record(lo, hi=None):
    if hi is None:
        hi = lo
    with localcontext() as ctx:
        ctx.prec = 32
        display = [str(Decimal(x.numerator) / Decimal(x.denominator)) for x in (lo, hi)]
    return dict(lower=dyadic(lo), upper=dyadic(hi), display=display)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for arg in ('far', 'source-cut', 'cut', 'ready', 'flow', 'r70', 'r71', 'out'):
        p.add_argument('--' + arg, type=Path, required=True)
    a = p.parse_args()
    began = time.monotonic()
    if a.out.exists():
        raise FileExistsError('Preserve all old primary outputs and use a fresh supplement')
    paths = [getattr(a, key) for key in ('far','source_cut','cut','ready','flow','r70','r71')]
    hashes = {str(path): digest(path) for path in paths}
    far = json.loads(a.far.read_text())
    cut = json.loads(a.cut.read_text())
    flow = json.loads(a.flow.read_text())
    r70 = json.loads(a.r70.read_text())
    r71 = json.loads(a.r71.read_text())
    if not (all(far['gates'].values()) and cut['all_gates']
            and all(flow['gates'].values()) and r70['all_gates'] and r71['all_gates']
            and read_field(a.source_cut,'all_gates')):
        raise ValueError('All original real objects must already be certified')
    if far['far_z_dyadic_bound'] != '2^-2224' or far['raw_D_constant'] != '2^1967':
        raise ValueError('Use the original full R39 auxiliary far ball')
    if far['input_hashes'].get(str(a.ready)) != hashes[str(a.ready)]:
        raise ValueError('The R39 far operator and true source differ')
    ci = bound(read_field(a.source_cut,'point_cut_K_conversion'))[1]
    first = next(row for row in far['rows'] if row['cell'] == 12)
    operator = bound(first['boundary_operator'])[1]
    Dmax = p2(1967 - 2 * 2224)
    raw_far = ci * operator * Dmax
    far_K = ceil_binary(raw_far)
    # Reference-width2 controls the whole low46 boundary lift. Dropping
    # exp[-m(2-sigma)] only increases its W_(sigma,1) bound for sigma=1/64.
    assert far_K < p2(-7800)
    source_rows = read_field(a.source_cut,'rows')
    corrected_cut = []
    displayed = {2: Fraction('1.000518e-50'), 4: Fraction('6.183529e-49')}
    for row in source_rows:
        m = row['mode']
        value = bound(row['auxiliary_Kbar_Wsigma1_upper'])[1] + far_K
        complete = bound(row['complete_actual_minus_candidate_same_mode_Wsigma1_upper'])[1] + far_K
        corrected_cut.append(dict(mode=m,original_source_only_Wsigma1=row['auxiliary_Kbar_Wsigma1_upper'],
            full_auxiliary_source_plus_far_Wsigma1_upper=record(value),
            original_R63_displayed_full_bound_still_strict=value < displayed[m],
            complete_actual_minus_candidate_Wsigma1_upper=record(complete)))
    b = bound(cut['true_radius'])[1]
    w = bound(cut['true_w'])[1]
    mu = bound(cut['outer_mu11'])[0]
    rc_value = read_field(a.ready,'physicalParameters')['rCuff']
    rc = Fraction.from_float(rc_value) if isinstance(rc_value,float) else Fraction(str(rc_value))
    if min(b,w,mu,rc) <= 0:
        raise ValueError('The physical cut factors must be positive')
    inverse_K_to_Xi = b**4 * w**2 / (3 * mu)  # sqrt(12)>3 exactly.
    propagation = []
    for cell in flow['cell_rows']:
        node = cell['cell']
        R = bound(cell['radius'])[1]
        for row in cell['modes']:
            m, u = row['mode'], row['mode']**2 - 4
            coefficient = ((R/rc)**u * cap(row['global_gauge_fundamental_matrix'][0][1])
                * (b/rc)**u / lower_abs(row['S0_true_Q']) * inverse_K_to_Xi / (1+m))
            delta = ceil_binary(coefficient * far_K)
            if not delta < p2(-7800):
                raise ArithmeticError('The common explicit propagated cap failed')
            propagation.append(dict(endpoint_physical_node=node,mode=m,
                cut_Q_centre_addition_upper=record(delta),
                whole_low_K_far_upper=record(far_K),
                exp_minus_m_sigma_conservatively_dropped=True))
    deltas = {(row['endpoint_physical_node'],row['mode']):bound(row['cut_Q_centre_addition_upper'])[1]
              for row in propagation}
    r70_rows, r71_rows = [], []
    for row in r70['rows']:
        m = row['mode'];lo,hi = bound(row['complete_candidate_centre_residual_canonical_Q'])
        delta = deltas[11,m]
        r70_rows.append(dict(mode=m,original_raw_interval=row['complete_candidate_centre_residual_canonical_Q'],
            complete_corrected_centre_interval=record(lo-delta,hi+delta),
            added_far_upper=record(delta),
            m2_strict_nonzero_still_paid=(lo-delta > 0) if m==2 else None))
    for row in r71['functional_rows']:
        m = row['mode'];lo,hi = bound(row['new_complete_candidate_centre_residual_canonical_Q'])
        delta = deltas[11,m]
        r71_rows.append(dict(mode=m,original_raw_interval=row['new_complete_candidate_centre_residual_canonical_Q'],
            complete_corrected_centre_interval=record(lo-delta,hi+delta),
            added_far_upper=record(delta),
            original_displayed_complete_bound_still_strict=max(abs(lo-delta),abs(hi+delta)) <
                (Fraction('1.088656e-56') if m==2 else Fraction('1.409564e-52'))))
    gates = dict(original_R39_full_far_operator_reused=True,
        no_linear_far_condition_imposed_on_the_actual_auxiliary_solution=True,
        full_low46_far_boundary_term_paid=True,
        source_and_boundary_parts_added_separately=True,
        original_R63_displayed_auxiliary_bounds_retained=all(row['original_R63_displayed_full_bound_still_strict'] for row in corrected_cut),
        all_four_node11_node10_Q_propagations_paid=len(propagation)==4,
        R70_m2_strict_nonzero_retained=next(row for row in r70_rows if row['mode']==2)['m2_strict_nonzero_still_paid'],
        R71_displayed_bounds_retained=all(row['original_displayed_complete_bound_still_strict'] for row in r71_rows),
        old_primary_source_flow_and_candidate_unchanged=True,
        R71_full_mean_height_change_unchanged=True)
    output = dict(status='Explicit completion of the omitted R39 auxiliary nonlinear far lift in R63 and its propagated centre intervals',
        gates=gates,all_gates=all(gates.values()),
        decomposition='C_aux=L_lin+G N(C_aux)+B D_low(z_aux). The old R63 primary bounds only the G N term. R58-C_aux is a separate correction and does not include B D_low(z_aux) again.',
        whole_low46_far_K_Wsigma1_upper=record(far_K),
        sufficient_common_far_K_and_propagated_Q_upper='2^-7800',
        raw_D_bound=record(Dmax),boundary_operator_at_cell12=first['boundary_operator'],
        point_cut_inner_mu12_K_conversion=read_field(a.source_cut,'point_cut_K_conversion'),
        corrected_R63_cut_rows=corrected_cut,propagation_rows=propagation,
        corrected_R70_rows=r70_rows,corrected_R71_rows=r71_rows,
        R71_mean_height_change=recenter_mean if (recenter_mean:=r71['complete_mean_height_total_change_upper']) else None,
        R72_uniform_value_note='The same far value bound applies on R72 because its full auxiliary far stays in the unchanged2^-2224 ball. This statement alone does not bound the parameter derivative.',
        old_raw_complete_labels_require_this_addendum=True,
        original_ODE_or_source_integrals_recomputed=False,
        input_hashes=hashes,source_sha256=digest(Path(__file__)),
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if output['peak_RSS_KiB'] > 40960:
        raise MemoryError('The owned exact completion exceeded40MiB')
    a.out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),all_gates=output['all_gates'],far_K=record(far_K)['display'],
        propagation=[dict(node=row['endpoint_physical_node'],mode=row['mode'],cap=row['cut_Q_centre_addition_upper']['display']) for row in propagation],
        peak_RSS_KiB=output['peak_RSS_KiB'])),flush=True)
    if not output['all_gates']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
