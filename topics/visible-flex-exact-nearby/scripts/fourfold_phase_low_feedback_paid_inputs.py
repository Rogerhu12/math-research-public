#!/usr/bin/env python3
"""Replay the paid finite cap/interface part of the actual M4 feedback block.

The exact finite matrix is defined by the saved dyadic input arrays and the
formulas below. A directed inverse bound applies to that matrix. The separate
floating core transfer, its discarded angular channels, and the full infinite
Schur complement are NOT certified by this program.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from flint import arb, acb, acb_mat, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_collect import adjoint, hermitian_norm_bound


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_report(path, arrays=True):
    report = json.loads(Path(path).read_text())
    if not report.get('complete'):
        raise ValueError('an input report is incomplete: '+str(path))
    values = None
    if arrays:
        record = report['arrays']
        p = Path(record['path'])
        if sha(p) != record['sha256']:
            raise ValueError('saved exact finite arrays changed: '+str(p))
        with np.load(p, allow_pickle=False) as data:
            values = {name: np.array(data[name], copy=True) for name in data.files}
    return report, values


def matrix(values):
    a = np.asarray(values)
    return acb_mat([[acb(float(z.real), float(z.imag)) for z in row] for row in a])


def hermitian_enclosure(value):
    """Preserve the known exact Hermitian object inside the supplied balls."""
    n = value.nrows()
    if n != value.ncols():
        raise ValueError('a Hermitian matrix must be square')
    result = acb_mat(n, n)
    for i in range(n):
        result[i, i] = acb(value[i, i].real)
        for j in range(i+1, n):
            z = (value[i, j]+value[j, i].conjugate())/2
            result[i, j], result[j, i] = z, z.conjugate()
    return result


def norm(value):
    # The underlying Gram matrix is Hermitian even when enclosure arithmetic
    # has generated slightly different conjugate endpoint representations.
    gram = hermitian_enclosure(adjoint(value)*value)
    upper, _ = hermitian_norm_bound(gram)
    return upper.sqrt().upper()


def eye(n):
    answer = acb_mat(n, n)
    for i in range(n):
        answer[i, i] = 1
    return answer


def midpoint(value):
    return np.array([[complex(float(value[i, j].real.mid()),
                              float(value[i, j].imag.mid()))
                      for j in range(value.ncols())] for i in range(value.nrows())])


def real_positive_coefficients(values):
    a = np.asarray(values)
    if np.any(a.imag != 0):
        raise ValueError('the saved even multiplier is not exactly real')
    return np.asarray(a.real, dtype=float)


def toeplitz(positive, cutoff):
    indices = range(-cutoff, cutoff+1)
    if len(positive) <= 2*cutoff:
        raise ValueError('insufficient exact multiplier coefficients')
    return acb_mat([[acb(float(positive[abs(i-j)]))
                     for j in indices] for i in indices])


def add_block(target, indices, source):
    if source.nrows() != len(indices) or source.ncols() != len(indices):
        raise ValueError('finite block shape does not match its explicit port')
    for i, target_i in enumerate(indices):
        for j, target_j in enumerate(indices):
            target[target_i, target_j] += source[i, j]


def high_multiplier_norm(positive, cutoff, kind):
    """All output frequencies of the finite polynomial, not a row truncation."""
    degree = len(positive)-1
    indices = list(range(-cutoff, cutoff+1))
    n = len(indices)
    gram = acb_mat(n, n)
    for k in range(-degree-cutoff, degree+cutoff+1):
        if abs(k) <= cutoff:
            continue
        weight = arb(4*abs(k))
        if kind == 'Hminus':
            weight = 1/weight
        elif kind != 'Hhalf':
            raise ValueError('unknown high-output norm')
        row = [arb(float(positive[abs(k-j)])) if abs(k-j) <= degree
               else arb(0) for j in indices]
        for i in range(n):
            for j in range(i, n):
                gram[i, j] += weight*row[i]*row[j]
    for i in range(n):
        for j in range(i+1, n):
            gram[j, i] = gram[i, j].conjugate()
    upper, _ = hermitian_norm_bound(gram)
    return upper.sqrt().upper()


def record_upper(report, key):
    return arb(report[key]['ball']).upper()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--core', type=Path,
        default=Path('notes/2026-11-12-actual-core-low-block-M4.json'))
    parser.add_argument('--cap', type=Path,
        default=Path('notes/2026-11-12-actual-cap-compression-energy.json'))
    parser.add_argument('--hybrid', type=Path,
        default=Path('notes/2026-11-12-actual-cap-full-hybrid-output.json'))
    parser.add_argument('--interface', type=Path,
        default=Path('notes/2026-11-12-actual-quarter-cut-interface-Fourier.json'))
    parser.add_argument('--bits', type=int, default=256)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits

    core, core_data = load_report(args.core)
    cap, cap_data = load_report(args.cap)
    hybrid, _ = load_report(args.hybrid, arrays=False)
    interface, interface_data = load_report(args.interface)
    reports = (core, cap, hybrid, interface)
    if len({r['object_sha256'] for r in reports}) != 1:
        raise ValueError('different exact graphs occur in the feedback inputs')
    if len({r['exact_delta_fraction'] for r in reports}) != 1:
        raise ValueError('different exact affine parameters occur in the inputs')
    if core['exact_physical_cuts'] != ['-1/4', '1/4']:
        raise ValueError('the core is not at the actual physical quarter cuts')
    if interface['exact_physical_radius'] != '1/4':
        raise ValueError('the multiplier data use a different physical port')
    N = core['modes']
    if cap['boundary_physical_modes'] != N or N < 0:
        raise ValueError('the cap and core finite input spaces differ')
    if not cap['regular_mean_port_retained']:
        raise ValueError('the actual regular mean port is missing')
    n, d = 2*N+1, 2*(2*N+1)+2
    Kraw = matrix(core_data['core_DN'])
    Ccap = matrix(cap_data['actual_cap_compression_center'])
    if Kraw.nrows() != 2*n or Ccap.nrows() != n+1:
        raise ValueError('unexpected core or cap matrix dimensions')
    K = (Kraw+adjoint(Kraw))/2
    core_symmetrization = norm(K-Kraw)
    names = interface['exact_function_names']
    coefficients = interface_data['positive_fourier_coefficients']
    ycoeff = real_positive_coefficients(coefficients[names.index('height_Y')])
    scoeff = real_positive_coefficients(coefficients[names.index('energy_shear_YpY')])
    Y, S = toeplitz(ycoeff, N), toeplitz(scoeff, N)
    chart = acb_mat(2*n, 2*n)
    add_block(chart, list(range(n)), Y)
    add_block(chart, list(range(n, 2*n)), Y)
    transformed_core = adjoint(chart)*K*chart
    A = acb_mat(d+1, d+1)
    add_block(A, list(range(2*n)), transformed_core)
    add_block(A, list(range(n))+[2*n], Ccap)
    add_block(A, list(range(n, 2*n))+[2*n+1], Ccap)
    add_block(A, list(range(n)), -S)
    add_block(A, list(range(n, 2*n)), -S)

    translation = np.zeros(d, complex)
    translation[[N, n+N, 2*n, 2*n+1]] = [-.5, .5, -.5, .5]
    for i, value in enumerate(translation):
        A[i, d] = acb(float(value.real), float(value.imag))
        A[d, i] = A[i, d].conjugate()

    chosen = midpoint(A)
    inverse_candidate = np.linalg.inv(chosen)
    R = matrix(inverse_candidate)
    inverse_residual = norm(eye(d+1)-R*A)
    if not inverse_residual < 1:
        raise ValueError('the exact finite matrix inverse residual is not below one')
    candidate_norm = norm(R)
    inverse_bound = (candidate_norm/(1-inverse_residual)).upper()
    chosen_center_error = norm(A-matrix(chosen))

    y_norm, k_norm = norm(Y), norm(K)
    yinfo = interface['functions']['height_Y']
    sinfo = interface['functions']['energy_shear_YpY']
    yerror = arb(yinfo['complete_polynomial_error_A012'][0]['ball']).upper()
    serror = arb(sinfo['complete_polynomial_error_A012'][0]['ball']).upper()
    full_projected_y_norm = (y_norm+yerror).upper()
    interface_fee = (k_norm*(2*y_norm*yerror+yerror*yerror)+serror).upper()
    cap_fee = record_upper(cap, 'true_cap_compression_operator_radius')
    # The two cap copies act on disjoint port summands: max, not their sum.
    symmetrization_fee = (full_projected_y_norm**2*core_symmetrization).upper()
    paid_fee = (interface_fee+cap_fee+symmetrization_fee).upper()
    product = (inverse_bound*paid_fee).upper()
    if not product < 1:
        raise ValueError('the already paid finite fees exhaust the inverse margin')
    remaining = (1/inverse_bound-paid_fee).lower()
    isolated_core_allowance = (remaining/full_projected_y_norm**2).lower()
    conditional_inverse = (inverse_bound/(1-product)).upper()

    yhigh_finite = high_multiplier_norm(ycoeff, N, 'Hhalf')
    yhigh_error = (arb(max(1, 4*N)).sqrt()
        *arb(yinfo['Hhalf_multiplier_error']['ball']).upper()).upper()
    shigh_finite = high_multiplier_norm(scoeff, N, 'Hminus')
    shigh_error = serror
    highcap_rows = [row for row in hybrid['physical_high_output_bounds']
                    if row['physical_cutoff'] == N]
    if len(highcap_rows) != 1:
        raise ValueError('the actual cap high-output bound for this cutoff is missing')
    caphigh = record_upper(highcap_rows[0], 'true_high_output_norm_upper')
    yhigh = (yhigh_finite+yhigh_error).upper()
    shigh = (shigh_finite+shigh_error).upper()

    gauge_vector = np.concatenate((translation, [0]))
    gauge_target = np.zeros(d+1, complex)
    gauge_target[-1] = 1
    gauge_defect = norm(A*matrix(gauge_vector[:, None])
                       -matrix(gauge_target[:, None]))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    arrays = args.out.with_suffix('.npz')
    np.savez_compressed(arrays, finite_bordered_center=chosen,
        exact_dyadic_inverse_candidate=inverse_candidate, translation=translation,
        core_raw_center=core_data['core_DN'],
        projected_height_center=midpoint(Y),
        projected_shear_center=midpoint(S),
        cap_compression_center=cap_data['actual_cap_compression_center'])
    report = dict(
        kind='paid_cap_and_interface_fees_for_exact_finite_low_feedback_candidate',
        complete=True, source_sha256=sha(__file__), bits=args.bits,
        recovery_status='Rebuilt UTF-8 implementation after executor loss; this report is newly executed, not reconstructed from earlier numbers.',
        object_sha256=core['object_sha256'],
        exact_delta_fraction=core['exact_delta_fraction'], modes=N,
        physical_cut='1/4', finite_bordered_dimension=d+1,
        input_reports=[dict(path=str(p), sha256=sha(p))
                       for p in (args.core, args.cap, args.hybrid, args.interface)],
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ('fourfold_phase_beta_interval.py','fourfold_phase_cap_energy_collect.py')},
        arrays=dict(path=str(arrays), sha256=sha(arrays), bytes=arrays.stat().st_size),
        exact_matrix_definition='A is the exact dyadic algebraic expression in the input arrays, two projected Y factors, two complete cap centers, two projected -YpY shears and the exact unit translation border. The saved binary64 finite_bordered_center is an approximation whose selection fee is separately reported.',
        exact_finite_center_inverse_certified=True,
        inverse_candidate_norm=ball_record(candidate_norm),
        inverse_candidate_residual=ball_record(inverse_residual),
        exact_finite_inverse_norm_upper=ball_record(inverse_bound),
        saved_binary_center_selection_error=ball_record(chosen_center_error),
        cap_compression_fee=ball_record(cap_fee),
        true_projected_interface_multiplier_fee=ball_record(interface_fee),
        raw_core_symmetrization_norm=ball_record(core_symmetrization),
        core_symmetrization_after_height_fee=ball_record(symmetrization_fee),
        total_paid_finite_matrix_fee=ball_record(paid_fee),
        paid_Banach_product=ball_record(product),
        remaining_unpaid_low_matrix_error_allowance=ball_record(remaining),
        conditional_core_DN_error_allowance_if_all_other_unpaid_terms_zero=ball_record(isolated_core_allowance),
        conditional_finite_inverse_after_paid_fees=ball_record(conditional_inverse),
        true_projected_height_norm_upper=ball_record(full_projected_y_norm),
        selected_core_norm_upper=ball_record(k_norm),
        selected_gauge_equation_defect=ball_record(gauge_defect),
        full_high_output_diagnostics=dict(
            input_norm='Euclidean physical Fourier coefficients k=-N..N; cap includes its regular mean input',
            output_weights='Hhalf: w0=1,wk=sqrt(4|k|); Hminus: reciprocal; all |k|>N',
            finite_height_low_to_high_Hhalf=ball_record(yhigh_finite),
            full_height_low_to_high_Hhalf=ball_record(yhigh),
            finite_shear_low_to_high_Hminus=ball_record(shigh_finite),
            full_shear_low_to_high_Hminus=ball_record(shigh),
            true_cap_low_to_high_Hminus=ball_record(caphigh),
            cap_plus_shear_triangle_bound=ball_record((caphigh+shigh).upper())),
        angular_mean_and_regular_xi_lambda_ports_retained=True,
        actual_core_radial_error_paid=False,
        infinite_high_frequency_elimination_paid=False,
        rigorous_full_Schur_inverse=False,
        scope=[
            'The cap and quarter-cut multipliers are actual directed inputs.',
            'The core_DN array remains the previously saved floating radial candidate.',
            'No actual full Schur inverse follows until core propagation, all projected-height omitted channels, and the actual high-channel feedback are paid in this same port and norm.',
            'The conditional scalar allowance cannot be combined with any unrecorded or cross-port operator estimate.'])
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in (
        'complete','exact_finite_inverse_norm_upper','total_paid_finite_matrix_fee',
        'paid_Banach_product','remaining_unpaid_low_matrix_error_allowance',
        'rigorous_full_Schur_inverse')}, indent=2), flush=True)


if __name__ == '__main__':
    main()
