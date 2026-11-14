#!/usr/bin/env python3
"""Transfer the true physical cap to the exact continuous repair.

The complete inverse-angle Fourier bounds are consumed coefficientwise.
If a complete actual residual cover is supplied, additionally consume the
exact residual-sensitive Hessian bridge.  Partial covers are rejected;
no original ac1 native is relabelled as a repaired-centre computation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time

from flint import arb, ctx
from fourfold_codazzi_current_positive_complete_coefficients import CURRENT_SHA, OBJECT_SHA
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

CAP_SHA = 'ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b'
POS_SHA = 'ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d'
REPAIR_SHA = '6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc'
DEFINITION = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def up(x):
    return abs(x).upper()


def maximum(values):
    return max((up(x) for x in values), default=arb(0)).upper()


def b(rec):
    return box_from_record(rec)


def native_norm(values, first, width=arb(0), order=0):
    return sum((up(b(z)) * abs(4*j)**order * (abs(4*j)*width).exp()
                for j, z in zip(range(first, first+len(values)), values)), arb(0)).upper()


def continuous_residual(paths, left, right):
    """Require a complete true cover, even when input files contain more rows.

    The merged report and the original checkpointed reports keep the same
    complete per-cell residual fields.  Repeated intervals must be identical.
    Only the overlap of their parameter permissions is advertised.
    """
    selected = {}; inputs = []; halfwidths = []
    for path in paths:
        doc = load(path)
        ident = doc.get('identity', {})
        candidate = ident.get('candidate_sha256', doc.get('candidate_sha256'))
        obj = ident.get('object_sha256', doc.get('object_sha256'))
        if candidate != CURRENT_SHA or obj != OBJECT_SHA:
            raise ValueError('residual inputs must identify the complete same ac1 object')
        if not doc.get('complete_original_primitive_tail', doc.get('full_original_primitive_tail', False)):
            raise ValueError('residual input has not retained the full primitive tail')
        merged = doc.get('kind') == 'complete_actual_moving_residual_all_closed_rows_and_interfaces'
        if merged and not (doc.get('complete') and doc.get('all_7296_closed_rows_reused_without_recomputation')
                           and doc.get('all_6143_actual_interfaces_paid') and doc.get('all_original_dependencies_verified')):
            raise ValueError('the whole residual merge has not verified its actual inputs and interfaces')
        modes = 32 if merged else doc.get('modes')
        support = doc.get('complete_residual_support') if merged else doc.get('complete_interior_support')
        if modes != 32 or support != 96:
            raise ValueError('the exact full moving residual support is required')
        half = ident.get('half_width', doc.get('common_parameter_half_width', doc.get('parameter_half_width')))
        if half is None:
            raise ValueError('the complete residual parameter domain is not explicit')
        halfwidths.append(Fraction(half))
        inputs.append(dict(path=str(path), sha256=sha(path), kind=doc.get('kind'),
                           original_complete=doc.get('complete'), half_width=str(half)))
        for row in doc['rows']:
            a, c = map(Fraction, row['interval'])
            if c <= left or a >= right:
                continue
            if row['exact_angular_support_index'] != 96:
                raise ValueError('a full angular residual row was truncated')
            key = (a, c)
            if key in selected and selected[key] != row:
                raise ValueError('duplicate residual cells disagree')
            selected[key] = row
    cursor = left; rows = []
    for (a, c), row in sorted(selected.items()):
        if a > cursor:
            raise ValueError(f'the actual cap residual has a gap at {cursor}')
        if c <= cursor:
            continue
        if a < cursor and rows:
            raise ValueError('overlapping nonidentical true residual cells are not a partition')
        rows.append(row); cursor = min(c, right)
        if cursor == right:
            break
    if cursor != right:
        raise ValueError(f'the actual cap residual stops at {cursor}, before {right}')
    A0 = [maximum(b(row['complete_residual_A0'][name]) for row in rows) for name in ('U','V')]
    A1 = [maximum(b(row['complete_residual_A1'][name]) for row in rows) for name in ('U','V')]
    return dict(inputs=inputs, rows=rows, half_width=min(halfwidths), A0=A0, A1=A1)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cap', type=Path, default=Path('notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz'))
    ap.add_argument('--positive-cache', type=Path, required=True)
    ap.add_argument('--repair', type=Path, default=Path('notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz'))
    ap.add_argument('--residual', type=Path, action='append', default=[])
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args(); started = time.monotonic(); ctx.prec = 320; ctx.cap = 6
    if args.out.exists():
        raise FileExistsError('preserve every actual conjugation attempt')
    for path, expected in ((args.cap,CAP_SHA),(args.positive_cache,POS_SHA),(args.repair,REPAIR_SHA)):
        if sha(path) != expected:
            raise ValueError(f'a complete proved input changed: {path}')
    cap, pos, repair = load(args.cap), load(args.positive_cache), load(args.repair)
    if not cap['complete'] or not pos['complete'] or not repair['complete']:
        raise ValueError('all three complete certificates are necessary')
    if cap['candidate_sha256'] != CURRENT_SHA or repair['derived_definition_sha256'] != DEFINITION:
        raise ValueError('the original/derived centre identities were interchanged')
    if cap['exact_interval'] != ['9/10','25/8'] or not cap['whole_original_eta'] or not pos['whole_original_eta']:
        raise ValueError('the complete same cap and whole original eta interval are required')
    left, right = Fraction(9,10), Fraction(25,8)
    rows = [r for r in pos['rows'] if Fraction(r['interval'][1]) > left]
    if not rows or Fraction(rows[-1]['interval'][1]) != right:
        raise ValueError('the actual positive coefficient cache does not reach R')
    cb = {k:b(v) for k,v in cap['bounds'].items()}
    cs = cap['complete_coefficient_suprema']; width = exact_arb(Fraction(1,32))
    frequencies = [4*j for j in range(1,33)] + [0] + [4*j for j in range(1,33)]
    offsets = list(map(Fraction, repair['exact_cumulative_coefficient_suprema']))
    eps = [sum((exact_arb(z)*k**j*(k*width).exp() for z,k in zip(offsets,frequencies)),arb(0)).upper() for j in range(2)]
    eps_piece = [exact_arb(Fraction(repair['exact_maximum_piece_pair_Ak'][str(j)])).upper() for j in range(3)]
    eps_mean = exact_arb(Fraction(repair['exact_maximum_mean_correction'])).upper()
    mg_old = cb['minimum_mean_abs'].lower(); mg = (mg_old-eps_mean).lower()
    ratio = (1+eps_mean/mg).upper()
    w_old = native_norm(cs['psi_phi'],-32,width)
    w1_old = native_norm(cs['psi_phi'],-32,width,1)
    psi_old = native_norm(cs['psi'],-32,width)
    w = (ratio*w_old+eps[0]/mg).upper()
    w1 = (ratio*w1_old+eps[1]/mg).upper()
    psi = (ratio*psi_old+eps[0]/(4*mg)).upper()
    U = (native_norm(cs['Q_B_imaginary'],-32,width)/2+eps[0]).upper()
    U1 = (native_norm(cs['Q_B_imaginary'],-32,width,1)/2+eps[1]).upper()
    mmax = (maximum(b(r['bounds']['V_A0']) for r in rows)+eps_mean).upper()
    V = (mmax*(1+w)).upper(); C = (1/(mg*(1-w))).upper()
    C1 = (w1/(mg*(1-w)**3)).upper(); B = (U*C).upper()
    B1 = (U1*C/(1-w)+U*C1).upper(); W1 = (B1+C1).upper()
    Jinv = (1/(1-w)).upper(); jmax = (1+w).upper()
    Icol = ((1+Jinv)/4).upper()
    Sinv = max(V,(V*(U+V)).upper()).upper()
    H = (Sinv*(1+V*W1*Icol)).upper()
    H2 = (V*V*(1+V*C1*Icol)).upper()
    P = max(C,(B*C+C*C).upper()).upper()
    P1 = max(C1,(B1*C+B*C1+2*C*C1).upper()).upper()
    source_map = ((P+W1*C/4)*jmax.sqrt()).upper()
    reconstruction = (H*Jinv.sqrt()).upper()

    beta = maximum(b(r['intrinsic']['beta']) for r in rows)
    gamma = maximum(b(r['intrinsic']['gamma']) for r in rows)
    K = maximum(b(r['intrinsic']['K']) for r in rows)
    Kop = max(arb(1),K).upper()
    oldU = maximum(b(r['bounds']['U_A0']) for r in rows)
    oldV = maximum(b(r['bounds']['V_A0']) for r in rows)
    oldU1 = maximum(b(r['bounds']['U_phi_A0']) for r in rows)
    oldV1 = maximum(b(r['bounds']['V_phi_A0']) for r in rows)
    Q0 = (oldU+oldV).upper(); Q1 = (Q0+oldU1+oldV1).upper()
    Qnorm = [Q0,Q1,(129*Q1).upper()]
    Fdiff = []
    for j in range(2):
        q,e,ep = Qnorm[j],eps_piece[j],eps_piece[j+1]
        ds = (Kop*(2*q*e+e*e)).upper(); s = (Kop*q*q).upper()
        drift = beta*(ds*Qnorm[j+1]+(s+ds)*ep)/4
        principal = gamma*Kop*(eps_mean*Qnorm[j+1]+(oldV+eps_mean)*ep)
        reaction = beta*(e+ds*q+(s+ds)*e)
        Fdiff.append((drift+principal+reaction).upper())

    DB = (cb['complete_physical_Q_B_Awidth']+2*eps[0]).upper()
    oldVstrip = (oldV*(1+w_old)).upper()
    dDC = (2*U*eps[0]+eps[0]**2+K*(2*oldVstrip*eps[0]+eps[0]**2)).upper()
    DC = (cb['complete_physical_Q_C_Awidth']+dDC).upper()
    chi = (cb['complete_module_Q_kernel']*max(DB,DC)+cb['true_outer_feedback']).upper()
    inverse = (1/(1-chi)).upper()
    port_keys = ('inner_C_port','outer_nonzero_d_port','outer_Bmean_port','outer_Cmean_port',
        'ordinary_L2rL2_B_source','ordinary_L2rL2_C_source',
        'divergence_module_B_source','divergence_module_C_source',
        'physical_B_jump_l1_source','physical_C_jump_l1_source')
    gains = {k:(cb[k]*inverse).upper() for k in port_keys}
    delta_C = ((C*C+C1*C/4)*eps[0]).upper()
    outer_Z = (exact_arb(Fraction(2533,10**16))+delta_C).upper()
    right_mean = abs(Fraction(repair['exact_right_mean_offset']))
    delta_Cmean = (exact_arb(right_mean)/(mg_old*mg)).upper()
    bounds = dict(repair_joint_A_1over32=eps[0],repair_joint_phi_A_1over32=eps[1],
        corrected_mean_gap=mg,corrected_mean_abs_upper=mmax,complete_w_A_1over32=w,
        complete_w_phi_A_1over32=w1,actual_inverse_displacement_A_1over64=psi,
        physical_U_A_1over64=U,moving_U_phi_A_1over32=U1,physical_v_A_1over64=V,
        physical_C_A_1over64=C,physical_C_theta_A_1over64=C1,
        physical_B_A_1over64=B,physical_B_theta_A_1over64=B1,
        physical_pair_theta_A_1over64=W1,physical_to_moving_measure=Jinv,
        moving_to_physical_measure=jmax,reciprocal_point_matrix=P,reciprocal_point_matrix_theta=P1,
        physical_to_moving_pair_at_same_physical_angle=H,physical_to_moving_even_at_same_physical_angle=H2,
        ordinary_L2_source_to_physical=source_map,physical_module_to_moving_LinftyL2=reconstruction,
        actual_beta_abs=beta,actual_gamma_abs=gamma,actual_K_abs=K,
        actual_old_Q_A0=Q0,actual_old_Q_A1=Q1,
        exact_repair_residual_difference_A0=Fdiff[0],exact_repair_residual_difference_A1=Fdiff[1],
        corrected_physical_Q_B_A_1over64=DB,corrected_physical_Q_C_A_1over64=DC,
        corrected_complete_physical_cap_feedback=chi,corrected_physical_cap_resolvent=inverse,
        outer_full_C_change_A_1over64=delta_C,outer_even_mean_change=delta_Cmean,
        corrected_outer_Z_A0=outer_Z)
    gates = [dict(name=n,passed=bool(ok)) for n,ok in (
        ('the exact corrected mean is negative on the whole cap',mg>0),
        ('the complete corrected inverse angle exists in the same Banach strip',psi<arb(1)/64 and w<1),
        ('all physical reciprocal products retain a positive denominator',1-w>0),
        ('the corrected all-mode physical Green contracts',chi<1),
        ('the changed outer input remains in the actually proved full L2 DN ball',outer_Z<arb(10)**-12),
        ('the full corrected state preserves the actual reflection mean convention',repair['corrected_value_and_all_angular_derivatives_continuous']),
    )]
    bridge = None
    if args.residual:
        rr = continuous_residual(args.residual,left,right)
        alpha = exact_arb(Fraction(cap['exact_alpha']))
        R0 = [(alpha*z+Fdiff[0]).upper() for z in rr['A0']]
        R1 = [(alpha*z+Fdiff[1]).upper() for z in rr['A1']]
        # Each cosine pair has total amplitude at most its complete A0 bound.
        # The true moving R_v has exact degree 96, including its even mean.
        rv_joint = (R0[1]+sum((min(R0[1],(R1[1]/(1+4*j)).upper())
                      *(4*j*psi).exp() for j in range(1,97)),arb(0))).upper()
        e_joint = (C*rv_joint/4).upper()
        e_sup = (arb.pi()*C*R0[1]/8).upper()
        e_theta_sup = (2*C*R0[1]).upper()
        tB = (C*R0[0]+B*C*R0[1]).upper(); tC = (C*C*R0[1]).upper()
        DP = (C*tB+(1+B+2*C)*tC).upper()
        t1 = (P1*sum(R0,arb(0))+P*Jinv*sum(R1,arb(0))).upper()
        Z = (DP*H+t1*C*H2/4+W1*(C*C*R0[1]/4+2*C*e_sup)*H2).upper()
        ordinary = max(gains['ordinary_L2rL2_B_source'],gains['ordinary_L2rL2_C_source']).upper()
        divergence = max(gains['divergence_module_B_source'],gains['divergence_module_C_source']).upper()
        eps_bridge = (divergence*e_joint+ordinary*exact_arb(right-left).sqrt()*(e_theta_sup+Z)).upper()
        ok = bool(eps_bridge<1)
        gates.append(dict(name='the actual complete residual-sensitive cap bridge contracts',passed=ok))
        bb = dict(physical_moving_residual_U_A0=R0[0],physical_moving_residual_V_A0=R0[1],
            physical_moving_residual_U_A1=R1[0],physical_moving_residual_V_A1=R1[1],
            complete_joint_Rv_after_actual_angle=rv_joint,complete_transport_coefficient_module=e_joint,
            transport_coefficient_pointwise=e_sup,transport_derivative_pointwise=e_theta_sup,
            complete_zero_order_Hessian=Z,complete_bridge_feedback=eps_bridge)
        if ok:
            bridge_inverse = (1/(1-eps_bridge)).upper();bb['complete_bridge_resolvent']=bridge_inverse
            bb['ordinary_moving_source_to_physical_module']=(ordinary*source_map*bridge_inverse).upper()
            bb['ordinary_moving_source_to_moving_LinftyL2']=(ordinary*source_map*bridge_inverse*reconstruction).upper()
            for k,v in gains.items():bb['fully_conjugated_'+k]=(v*bridge_inverse).upper()
        bridge = dict(complete=ok,parameter_half_width=str(rr['half_width']),
            complete_cap_residual_cells=len(rr['rows']),inputs=rr['inputs'],
            normalized_residual_A0=[record(z) for z in rr['A0']],
            normalized_residual_A1=[record(z) for z in rr['A1']],
            bounds={k:record(v) for k,v in bb.items()},full_reflection_even_mean_retained=True,
            full_Codazzi_means_in_physical_Green_retained=True,
            candidate_interfaces_exactly_continuous=True,
            physical_inner_C_port_and_all_true_outer_ports_retained=True)
    report = dict(kind='actual_continuous_repair_physical_cap_and_residual_conjugation_v1',
        complete=all(g['passed'] for g in gates),source_sha256=sha(__file__),
        original_candidate_sha256=CURRENT_SHA,derived_definition_sha256=DEFINITION,
        object_sha256=OBJECT_SHA,exact_interval=['9/10','25/8'],
        cap_input_sha256=sha(args.cap),positive_input_sha256=sha(args.positive_cache),repair_input_sha256=sha(args.repair),
        whole_original_eta_for_background_transfer=True,background_parameter_half_width='1/1000000000',
        bounds={k:record(v) for k,v in bounds.items()},
        corrected_all_mode_physical_Green_gains={k:record(v) for k,v in gains.items()},
        bridge=bridge,full_residual_sensitive_bridge_proved=bool(bridge and bridge['complete']),
        residual_unknown_zero_assumed=False,unknown_Fourier_tail_truncated=False,
        original_ac1_native_silently_relabelled=False,bare_composition_minus_identity_used=False,
        real_continuous_repaired_centre=True,original_radial_derivative_continuity_claimed=False,
        whole_body_inverse_proved=False,negative_return_inverse_proved=False,
        gates=gates,dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_current_positive_complete_coefficients.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')},
        theorem_inputs={name:sha(Path('results')/name) for name in (
            'R133-supplement-exact-continuous-repair-of-final-centre.md',
            'R133-supplement-actual-final-all-mode-physical-cap-Green.md',
            'R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md')},
        seconds=time.monotonic()-started)
    save(args.out,report)
    print(dict(complete=report['complete'],physical_feedback=chi.str(16),
        full_residual_bridge=report['full_residual_sensitive_bridge_proved'],
        bridge_feedback=None if bridge is None else bridge['bounds']['complete_bridge_feedback']['upper'],
        seconds=report['seconds']),flush=True)
    if not report['complete']:raise RuntimeError('an actual full cap gate failed; original result preserved')


if __name__ == '__main__':
    main()
