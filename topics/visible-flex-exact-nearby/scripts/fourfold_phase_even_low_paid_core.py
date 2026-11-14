#!/usr/bin/env python3
"""Assemble the actually paid six-dimensional invariant retained-port block.

The core and cut multipliers cover the stated whole parameter interval.  The
cap input is currently paid at the center only.  The program certifies the
center retained block, and separately quantifies the cap variation that would
extend this conclusion to the whole interval.  It never certifies the omitted
height channels or the infinite high-channel Schur complement.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import numpy as np
from flint import arb, acb, acb_mat, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_low_feedback_paid_inputs import (
    adjoint, hermitian_enclosure, load_report, matrix, midpoint, norm,
    real_positive_coefficients, sha, toeplitz)
from fourfold_phase_low_block_dihedral import inverse_certificate


def upper(record):
    return arb(record['ball']).upper()


def cosine_basis(N, regular=False):
    """Physical normalized Fourier -N..N to (1,sqrt(2)cos(4k theta))."""
    n = 2*N+1
    Q = acb_mat(n+int(regular), N+1+int(regular))
    Q[N, 0] = 1
    s = 1/arb(2).sqrt()
    for k in range(1, N+1):
        Q[N-k, k] = s
        Q[N+k, k] = s
    if regular:
        Q[n, N+1] = 1
    return Q


def embed_height(A):
    out = acb_mat(A.nrows()+1, A.ncols()+1)
    for i in range(A.nrows()):
        for j in range(A.ncols()):
            out[i, j] = A[i, j]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--core', type=Path, required=True)
    ap.add_argument('--interface', type=Path, required=True)
    ap.add_argument('--cap', type=Path, default=Path(
        'notes/2026-11-12-actual-cap-compression-energy.json'))
    ap.add_argument('--old-sector', type=Path)
    ap.add_argument('--bits', type=int, default=256)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    ctx.prec = args.bits
    core, core_data = load_report(args.core)
    interface, interface_data = load_report(args.interface)
    cap, cap_data = load_report(args.cap)
    if not core.get('finite_waist_even_DN_certified'):
        raise ValueError('the actual finite even core has not been certified')
    ident = core['identity']
    if not ident.get('uniform_in_the_entire_real_parameter_interval'):
        raise ValueError('the core is not uniform in its declared parameter interval')
    if not interface.get('uniform_in_the_entire_real_parameter_interval'):
        raise ValueError('the interface is not a complete family input')
    interval = list(map(Fraction, ident['exact_parameter_interval']))
    if list(map(Fraction, interface['exact_parameter_interval'])) != interval:
        raise ValueError('the whole-parameter intervals differ')
    center = Fraction(ident['exact_center_parameter'])
    if not interval[0] <= center <= interval[1]:
        raise ValueError('the stated center is outside its family interval')
    if (interface['object_sha256'] != ident['object_sha256']
            or cap['object_sha256'] != ident['object_sha256']
            or Fraction(interface['exact_center_parameter']) != center
            or Fraction(cap['exact_delta_fraction']) != center):
        raise ValueError('the actual center graph identities differ')
    if (core['exact_physical_cuts'] != ['-1/4', '1/4']
            or interface['exact_physical_radius'] != '1/4'
            or cap['exact_radial_cover'] != ['1/4', '25/8']):
        raise ValueError('incompatible physical core/cap ports')
    N = int(cap['boundary_physical_modes'])
    if (core['angular_cos_modes'] != list(range(N+1))
            or not cap['regular_mean_port_retained']):
        raise ValueError('different retained height modes or missing regular port')
    K = matrix(core_data['core_DN_even_waist'])
    C = matrix(cap_data['actual_cap_compression_center'])
    if (K.nrows(), K.ncols()) != (N+1, N+1):
        raise ValueError('wrong even core shape')
    if (C.nrows(), C.ncols()) != (2*N+2, 2*N+2):
        raise ValueError('wrong complete cap compression shape')

    names = interface['exact_function_names']
    coeff = interface_data['positive_fourier_coefficients']
    yc = real_positive_coefficients(coeff[names.index('height_Y')])
    sc = real_positive_coefficients(coeff[names.index('energy_shear_YpY')])
    Q, Qcap = cosine_basis(N), cosine_basis(N, True)
    Y = hermitian_enclosure(adjoint(Q)*toeplitz(yc, N)*Q)
    S = hermitian_enclosure(adjoint(Q)*toeplitz(sc, N)*Q)
    # Compression by an exact isometry contracts the complete cap radius.
    Ccos = hermitian_enclosure(adjoint(Qcap)*C*Qcap)
    exact = hermitian_enclosure(embed_height(adjoint(Y)*K*Y-S)+Ccos)
    certificate, selected, inverse = inverse_certificate(exact)
    if not certificate['inverse_certified']:
        raise ValueError('the exact retained six-block center inverse failed')

    Kn, Yn = norm(K), norm(Y)
    Ey = upper(interface['functions']['height_Y']['complete_polynomial_error_A012'][0])
    Es = upper(interface['functions']['energy_shear_YpY']['complete_polynomial_error_A012'][0])
    Ek = upper(core['actual_finite_even_core_DN_error'])
    Ec = upper(cap['true_cap_compression_operator_radius'])
    trueY = (Yn+Ey).upper()
    core_fee = (trueY**2*Ek).upper()
    multiplier_fee = (Kn*(2*Yn*Ey+Ey**2)+Es).upper()
    fee = (core_fee+multiplier_fee+Ec).upper()
    inv = upper(certificate['exact_parity_block_inverse_norm_upper'])
    product = (inv*fee).upper()
    if not product < 1:
        raise ValueError('the actually paid finite fees exhaust the inverse margin')
    allowance = (1/inv-fee).lower()
    inverse_true_center = (inv/(1-product)).upper()
    cap_norm = (norm(Ccos)+Ec).upper()
    relative_allowance = (allowance/cap_norm).lower()

    comparison = None
    if args.old_sector:
        old, old_data = load_report(args.old_sector)
        if old['object_sha256'] != ident['object_sha256']:
            raise ValueError('old diagnostic uses a different center')
        oldA = matrix(old_data['angular_even_waist_even_center'])
        comparison = dict(path=str(args.old_sector), sha256=sha(args.old_sector),
            exact_center_difference=ball_record(norm(exact-oldA)))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    out_arrays = args.out.with_suffix('.npz')
    np.savez_compressed(out_arrays, finite_center=selected,
        exact_dyadic_inverse_candidate=inverse,
        selected_core_center=core_data['core_DN_even_waist'],
        selected_cosine_height=midpoint(Y), selected_cosine_shear=midpoint(S),
        selected_cosine_cap=midpoint(Ccos))
    report = dict(kind='actual_even_retained_core_cap_block_with_center_cap_scope',
        complete=True, source_sha256=sha(__file__), bits=args.bits,
        object_sha256=ident['object_sha256'], exact_center_parameter=str(center),
        exact_parameter_interval=list(map(str, interval)),
        input_reports=[dict(path=str(p), sha256=sha(p))
                       for p in (args.core,args.interface,args.cap)],
        input_arrays=[core['arrays'],interface['arrays'],cap['arrays']],
        physical_cut='1/4', modes=N, dimension=N+2,
        exact_retained_operator='embed(Y_cos(p)^* DN_even(p) Y_cos(p)-S_cos(p)) + Ccap_cos(p)',
        saved_center_definition='The exact algebraic expression in the three selected centers, compressed in the exact normalized cosine/paired-waist basis. Saved binary64 center selection is paid separately and is not substituted into the inverse proof.',
        inverse_certificate=certificate,
        whole_interval_core_fee=ball_record(core_fee),
        whole_interval_projected_multiplier_fee=ball_record(multiplier_fee),
        center_cap_fee=ball_record(Ec),
        total_paid_center_matrix_fee=ball_record(fee),
        paid_Banach_product=ball_record(product),
        actual_center_retained_block_inverse_certified=True,
        actual_center_retained_block_inverse_upper=ball_record(inverse_true_center),
        uniform_family_with_cap_frozen_at_center_certified=True,
        true_cap_family_variation_paid=False,
        entire_actual_parameter_family_certified=False,
        remaining_cap_variation_or_other_error_allowance=ball_record(allowance),
        true_center_cap_cosine_norm_upper=ball_record(cap_norm),
        sufficient_relative_cap_form_variation=ball_record(relative_allowance),
        relative_cap_form_contract='If (1-epsilon)b0<=bp<=(1+epsilon)b0 on the common complete cap energy space, with both regular trace/flux ports retained, minimization gives the same Loewner inequalities for the complete DN form. The cosine finite compression differs by at most epsilon*||Ccap_cos(0)||. The displayed strict allowance is sufficient; it is not claimed proved here.',
        exact_height_norm_upper=ball_record(Yn),
        whole_family_height_norm_upper=ball_record(trueY),
        exact_core_center_norm_upper=ball_record(Kn),
        raw_uniform_core_DN_radius=ball_record(Ek),
        paired_angular_mean_retained=True,
        paired_regular_trace_and_flux_retained=True,
        translation_border_in_other_representation=True,
        old_selected_sector_comparison=comparison,
        discarded_height_channels_paid=False,
        infinite_high_feedback_paid=False,
        rigorous_full_Schur_inverse=False,
        scope=[
            'The center retained finite core/cap operator is invertible with all radial core error now paid.',
            'The entire stated parameter interval is paid for the core and interface only; the actual varying cap still needs its own form or matrix comparison.',
            'All finite cap input columns include the complete cap response, but the additional chart-generated high height channels and the coupled infinite high problem remain unpaid.',
            'The finite core ODE crosses the turning roots regularly; no strict-negative PDE energy estimate is extended to the positive collars inside the quarter cuts.'],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_low_feedback_paid_inputs.py',
            'fourfold_phase_low_block_dihedral.py',
            'fourfold_phase_cap_energy_collect.py',
            'fourfold_phase_beta_interval.py')},
        arrays=dict(path=str(out_arrays),sha256=sha(out_arrays),bytes=out_arrays.stat().st_size))
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('complete','dimension',
        'total_paid_center_matrix_fee','paid_Banach_product',
        'actual_center_retained_block_inverse_upper',
        'remaining_cap_variation_or_other_error_allowance',
        'sufficient_relative_cap_form_variation',
        'entire_actual_parameter_family_certified','rigorous_full_Schur_inverse')},indent=2),flush=True)


if __name__=='__main__':
    main()
