#!/usr/bin/env python3
"""Complete actual positive high inverse in the negative height window.

The full band-64 absolute Fourier kernel is conjugated by (4N/M)^(5/3).
The additional shared skew-transport commutator is paid separately.
All finite head, true means, exterior sources and affine joins remain.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
from flint import arb, ctx
from fourfold_codazzi_current_positive_high_Volterra import (
    read_doc, lower_flow, directed_sweep, CURRENT_SHA, KIND)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--coefficients', type=Path, required=True)
    parser.add_argument('--cutoff', type=int, default=97)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('preserve every negative-window high attempt')
    started = time.monotonic()
    ctx.prec = 320
    ctx.cap = 6
    doc = read_doc(args.coefficients)
    if (doc.get('kind') != KIND or not doc.get('complete') or not doc.get('coefficient_cover_complete')
            or doc.get('failure') is not None or not doc.get('whole_original_eta')
            or doc['identity']['candidate_sha256'] != CURRENT_SHA):
        raise ValueError('the complete same-current-centre positive coefficient cover is required')
    producer = Path(__file__).with_name('fourfold_codazzi_current_positive_complete_coefficients.py')
    if doc['identity']['source_sha256'] != sha(producer):
        raise ValueError('the complete coefficient producer changed')
    for name, digest in doc['identity']['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name)) != digest:
            raise ValueError('a complete positive coefficient dependency changed: ' + name)
    N = args.cutoff
    mc = doc['identity']['modes']
    if N < 97 or N <= 2 * mc:
        raise ValueError('the actual complete band must lie below the high cutoff')
    M = 4 * N
    t = arb(5) / 3
    ratio = exact_arb(Fraction(N + 2 * mc, N))
    weight_ratio = (ratio.log() * t).exp().upper()
    # Convexity of x^t, t>=1: this secant also dominates the reversed case.
    drift_commutator = ((ratio + 1) * (weight_ratio - 1) / (2 * (ratio - 1))).upper()
    head_shell_ratio = (exact_arb(Fraction(N - 1 + 2 * mc, N)).log() * t).exp().upper()
    rows = []
    endpoint = Fraction(doc['identity']['left'])
    for saved in doc['rows']:
        left, right = map(Fraction, saved['interval'])
        if left != endpoint or not left < right:
            raise ValueError('the actual complete positive cover has a gap')
        c = {k: box_from_record(v) for k, v in saved['intrinsic'].items()}
        b = {k: box_from_record(v) for k, v in saved['bounds'].items()}
        if not c['K'] > 0 or not b['radial_speed'] > 0:
            raise ValueError('actual positive type and mean speed are unresolved')
        klo = max(c['K'].lower(), exact_arb(Fraction(1, 2000)).lower()).lower()
        khi = min(c['K'].upper(), arb(4)).upper()
        if not klo <= khi:
            raise ValueError('independent true K enclosures are disjoint')
        rows.append(dict(left=left, right=right, length=exact_arb(right-left),
                         K_lower=klo, K_upper=khi, speed=b['radial_speed'],
                         beta=abs(c['beta']).upper(), bounds=b, right_interface=saved['right_interface']))
        endpoint = right
    if endpoint != Fraction(25, 8):
        raise ValueError('the complete current positive body must reach the true exterior')
    p = arb(1)/8
    for row in reversed(rows):
        row['p_lower'], p = lower_flow(p, row['K_lower'], row['speed'].lower(), M, row['length'])
    for row in rows:
        row['p_lower'] = max(row['p_lower'], (arb(1)/45).lower()).lower()
    g = arb(0)
    for row in rows:
        row['g_lower'], g = lower_flow(g, row['K_lower'], row['speed'].lower(), M, row['length'])

    E_integral = arb(0)
    absE_integral = arb(0)
    drift_integral = arb(0)
    reconstruction_sq = arb(0)
    actual_jumps = arb(0)
    digest = hashlib.sha256()
    for index, row in enumerate(rows):
        b = row['bounds']
        W = (row['p_lower'] + row['g_lower']).lower()
        if not W > 0:
            raise ValueError('the actual full Riccati denominator is unresolved')
        qratio = (row['K_upper']/W).upper()
        BA = (b['local_a_A0'] + b['local_e_A0'] + (qratio+4)*b['local_b_A0']).upper()
        U, V, U1, V1 = (b[k] for k in ('U_A0','V_A0','U_phi_A0','V_phi_A0'))
        FN = (U1*U + row['K_upper']*V1*V + qratio*U1*V + 4*V1*U).upper()
        # BA also replaces the same-frequency sup envelope, so this is
        # a bound for the full absolute coefficient kernel before weighting.
        Eabs = ((arb(13)/2)*b['drift_phi_A0'] + 2*BA
                + exact_arb(Fraction(24*mc,N))*BA
                + exact_arb(Fraction(4,N-mc))*row['beta']*FN).upper()
        drift_extra = (drift_commutator*b['drift_phi_A0']).upper()
        E = (weight_ratio*Eabs + drift_extra).upper()
        gap = (M*row['speed'].lower()*W/2).lower()
        frame = min(arb(5), (2*(-arb(M).log()/6).exp()*max(arb(2),1/W.sqrt())).upper()).upper()
        row.update(W=W, E=E, gap=gap, frame=frame, frame_sq=(frame*frame).upper())
        E_integral += row['length']*E
        absE_integral += row['length']*Eabs
        drift_integral += row['length']*drift_extra
        reconstruction_sq += row['length']*frame*frame
        jump = row['right_interface']
        if jump is not None:
            # The high negative weight is <=1, so the full actual A1 fee
            # is a safe bound for its weighted H^(1/3) impulse norm.
            actual_jumps += frame*exact_arb(Fraction(jump['u_v_pair_A1_upper_exact']))
        Lraw = (b['local_a_A0']+b['local_e_A0']+(1+row['K_upper'])*b['local_b_A0']).upper()
        AHL = (4*(N-1)*b['drift_A0']+Lraw+b['primitive_raw_L2']).upper()
        ALH = ((AHL+b['drift_phi_A0'])*head_shell_ratio).upper()
        payload = dict(row=index, interval=[str(row['left']),str(row['right'])],
            W=record(W), Eabs=record(Eabs), weighted_E=record(E), gap=record(gap),
            low_to_high_ordinary_source=record(AHL), weighted_high_to_low_raw=record(ALH))
        digest.update((json.dumps(payload, sort_keys=True, separators=(',',':'))+'\n').encode())

    forward = directed_sweep(rows, 'E', arb(1), False)
    backward = directed_sweep(rows, 'E', arb(1), True)
    source_forward = directed_sweep(rows, 'frame_sq', arb(2), False)
    source_backward = directed_sweep(rows, 'frame_sq', arb(2), True)
    tau_sq = arb(0)
    source_sq = arb(0)
    worst = 0
    for i in range(len(rows)):
        current = (forward[i]**2 + backward[i]**2).upper()
        if current > tau_sq:
            tau_sq, worst = current, i
        source_sq = max(source_sq, (source_forward[i]+source_backward[i]).upper()).upper()
    tau = tau_sq.sqrt().upper()
    exterior = exact_arb(Fraction(1001,250000))  # .004004, paid full H^(-3/2) exterior.
    total = (tau+exterior).upper()
    passed = bool(total < 1)
    native = dict(kind='actual_current_complete_positive_negative_height_window_v1',
        complete=passed, actual_full_high_inverse_certified=passed,
        source_sha256=sha(__file__), coefficient_native_sha256=sha(args.coefficients),
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_current_positive_high_Volterra.py',
            'fourfold_codazzi_current_positive_complete_coefficients.py',
            'fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        candidate_sha256=CURRENT_SHA, whole_original_eta=True,
        parameter_half_width=doc['identity']['parameter_half_width'],
        exact_radial_interval=[doc['identity']['left'],str(endpoint)], rows=len(rows),
        cutoff_index=N, physical_minimum=M, retained_reflection_head_dimension=2*N-1,
        full_unbounded_high=True, actual_weight='(4N/|k|)^(5/3)',
        state='Y_k=(4N/|k|)^(5/3) Z_k; Z_k=|k|^(1/6) T_k^-1 S_sign h_k',
        height_state='tilde Z(r)=n(r)/(4N)^(5/3) Y(r); the radial n is not treated as constant',
        bounds={k:record(v) for k,v in dict(
            finite_band_frequency_ratio=ratio, complete_weight_ratio=weight_ratio,
            exact_shared_skew_drift_secant=drift_commutator,
            complete_head_return_shell_weight=head_shell_ratio,
            complete_absolute_unweighted_E_integral=absE_integral.upper(),
            complete_new_drift_commutator_integral=drift_integral.upper(),
            complete_weighted_E_integral=E_integral.upper(),
            full_interior_Volterra_norm=tau, full_exterior_reflection=exterior,
            full_feedback=total, ordinary_weighted_source_to_unperturbed_Y_sup=source_sq.sqrt().upper(),
            weighted_raw_reconstruction_L2=reconstruction_sq.sqrt().upper(),
            actual_complete_weighted_high_jump_majorant=actual_jumps.upper()).items()},
        worst_closed_box=dict(index=worst, interval=[str(rows[worst]['left']),str(rows[worst]['right'])],
            E=record(rows[worst]['E']), gap=record(rows[worst]['gap']),
            forward_kernel=record(forward[worst]),backward_kernel=record(backward[worst])),
        complete_derived_rows_sha256=digest.hexdigest(),
        source_contract=dict(
            ordinary='L2_r of ||(4N/|D|)^(5/3) f_H||_H^(1/3)',
            left='the complete weighted stable reference port',
            right='(4N)^(5/3) times every independent negative-window exterior raw head/mean/fB/rB/rC column',
            arbitrary_jumps='sum_i C_i ||(4N/|D|)^(5/3) [h_H]_i||_H^(1/3)',
            no_physical_height_L2_source_relabeling=True),
        complete_head=dict(all_original_mean_rows_retained=True,
            high_to_low_interior_input_supported_through_index=N-1+2*mc,
            actual_exterior_mean_high_to_low_full_rank_one_path_retained=True,
            finite_head_inverse_proved=False),
        radial_density_conjugation_performed=False,
        no_global_BVP_or_negative_return_inverse=True,
        no_unknown_correction_given_finite_background_band=True,
        wall_seconds=time.monotonic()-started)
    if passed:
        inverse = (1/(1-total)).upper()
        sf = (inverse*source_sq.sqrt()).upper()
        raw = reconstruction_sq.sqrt().upper()
        trace = max(rows[0]['frame'],rows[-1]['frame']).upper()
        native['inverse_bounds']={k:record(v) for k,v in dict(
            full_Y_sup_resolvent=inverse,ordinary_weighted_source_to_Y_sup=sf,
            incoming_ports_and_weighted_jumps_to_Y_sup=inverse,
            ordinary_source_to_weighted_raw_L2=(raw*sf).upper(),
            incoming_ports_to_weighted_raw_L2=(raw*inverse).upper(),
            ordinary_source_to_both_weighted_raw_traces=(2*trace*sf).upper(),
            incoming_ports_to_both_weighted_raw_traces=(2*trace*inverse).upper()).items()}
    else:
        native['failure']=dict(gate='complete weighted interior plus paid exterior feedback <1',
                               no_negative_window_inverse_granted=True)
    save(args.out,native)
    print(dict(complete=passed,cutoff=N,full_feedback=str(total),out=str(args.out)),flush=True)
    if not passed:
        raise RuntimeError('the actual complete negative-window high gate failed; report preserved')


if __name__=='__main__':
    main()
