#!/usr/bin/env python3
"""Complete moving cut rows from the real physical cap and its padded columns.

The odd input block is the exact identity, not a truncated composition.
The independent even mean and the complete moving high output are retained.
Each matrix Schur row/column maximum is taken after directed upper extraction.
This computes the actual finite inlet and a subspace proposal.  The complete
physical cap residual is a separate scalar input: unfinished cap rows are
never promoted to a full cap or body inverse here.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import time
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import numpy as np
from scipy.linalg import qr
from flint import arb, arb_mat, arb_poly, ctx
from fourfold_codazzi_final_moving96_physical128_C_matrix import (
    exponential, coefficient, integer_box)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save

CURRENT = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
REPAIR = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
C_SHA = '119dedb2e62f23553b81dea9eb787d8298c1224eebc2cc38790ec50274df0ca7'
B_SHA = '3e6f4a745a6e49331df784644daea88272132c6f4792c01968de82e42f60092f'
K_SOURCE = 'e6e291718c45480be5994d2a8ca8b0fc93e2922963c99fd2b52134d03ddda5bf'
KIND = 'actual_complete_moving193_cap_cut_rows_and_high_defect_v2'
CUT = Fraction(9, 10)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(2**20), b''):
            h.update(block)
    return h.hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def dyadic(value):
    return Fraction.from_float(float(value))


def interval(pair, denominator):
    left, right = (Fraction(int(x), denominator) for x in pair)
    if left > right:
        raise ValueError('a directed interval was reversed')
    return exact_arb((left+right)/2) + arb(0, exact_arb((right-left)/2).upper())


def matrix_rows(document, columns=None):
    den = int(document['exact_interval_denominator'])
    values = []
    for row in document['rows']:
        entries = row['exact_interval_numerators']
        if columns is not None:
            entries = [entries[j] for j in columns]
        values.append([interval(x, den) for x in entries])
    return arb_mat(values)


def matrix_norms(matrix):
    nr, nc = matrix.nrows(), matrix.ncols()
    rows = [arb(0) for _ in range(nr)]
    cols = [arb(0) for _ in range(nc)]
    squared = arb(0)
    for i in range(nr):
        for j in range(nc):
            value = abs(matrix[i, j]).upper()
            rows[i] += value
            cols[j] += value
            squared += value*value
    hilbert = squared.sqrt().upper()
    schur = (max(x.upper() for x in rows)*max(x.upper() for x in cols)).sqrt().upper() if nr and nc else arb(0)
    return min(hilbert, schur).upper(), hilbert, schur


def midpoint_proposal(matrix):
    values = np.empty((matrix.nrows(), matrix.ncols()))
    error = arb(0)
    for i in range(matrix.nrows()):
        for j in range(matrix.ncols()):
            values[i, j] = float(matrix[i, j].mid())
            e = abs(matrix[i, j]-exact_arb(dyadic(values[i, j]))).upper()
            error += e*e
    return values, error.sqrt().upper()


def exact_left_endpoint(proposal):
    """Evaluate the declared shared-node Hermite trial at the rational cut.

    Original large inputs are streamed once for identity.  Only the first
    two shared values and the first pair of one-sided slopes are mapped.
    This is an evaluation of the exactly defined trial polynomial; it does
    not extrapolate the background geometry.
    """
    expected = proposal['full_matrix_inputs']
    paths = {Path(path).name: Path(path) for path in expected}
    if set(paths) != {'state.npy', 'derivative-left.npy', 'derivative-right.npy'}:
        raise ValueError('all shared values and both one-sided derivatives are required')
    for path, digest in expected.items():
        if sha(path) != digest:
            raise ValueError('an actual complete cap Hermite array changed')
    endpoint = proposal['physical_endpoint_graph']
    if sha(endpoint['path']) != endpoint['sha256']:
        raise ValueError('the actual complete endpoint array changed')
    with np.load(endpoint['path'], allow_pickle=False) as z:
        nodes = z['nodes'].copy()
    states = np.load(paths['state.npy'], mmap_mode='r', allow_pickle=False)
    dl = np.load(paths['derivative-left.npy'], mmap_mode='r', allow_pickle=False)
    dr = np.load(paths['derivative-right.npy'], mmap_mode='r', allow_pickle=False)
    if states.shape != (len(nodes), 257, 97) or dl.shape != (len(nodes)-1, 257, 97) or dr.shape != dl.shape:
        raise ValueError('the complete 257-state / 97-column trial changed')
    left, right = map(dyadic, nodes[:2])
    h = right-left
    x = (CUT-left)/h
    if not abs(CUT-left) < Fraction(1, 2**50) or not h > 0:
        raise ValueError('the original actual first Hermite interval changed')
    weights = (2*x**3-3*x*x+1, -2*x**3+3*x*x,
               h*(x**3-2*x*x+x), h*(x**3-x*x))
    # Only B_1..128 and C_0 are needed by the complete inlet rows.
    output = []
    for i in range(129):
        output.append([sum((exact_arb(w)*exact_arb(dyadic(v)) for w, v in zip(
            weights, (states[0, i, j], states[1, i, j], dl[0, i, j], dr[0, i, j]))), arb(0))
            for j in range(97)])
    return arb_mat(output), dict(exact_evaluation_radius=str(CUT),
        original_first_nodes=[str(left), str(right)], exact_Hermite_weights=list(map(str, weights)),
        complete_input_arrays=expected, endpoint_input=endpoint,
        common_shared_values_and_true_one_sided_derivatives_retained=True)


def full_high_transform(C, difference):
    """Retain every Fourier coefficient of v times the finite exponential.

    The infinite exponential remainder is bounded before projection in
    complete L2.  No differentiated A0 error is used.  Each physical sine
    input is normalized by sqrt(2), giving the explicit factor2 in the
    Hilbert--Schmidt remainder below.
    """
    m = box_from_record(C['complete_actual_mean'])
    psi = [box_from_record(x) for x in C['complete_phase_sine_coefficients']]
    alpha = Fraction(C['exact_alpha'])
    values = list(map(Fraction, C['exact_cut_finite_candidate']))
    offsets = list(map(Fraction, C['exact_cut_physical_offset']))
    vcos = [exact_arb(alpha*values[32+j]+offsets[32+j]) for j in range(1, 33)]
    A = [arb(0) for _ in range(65)]
    V = [arb(0) for _ in range(65)]
    V[32] = m
    for j, (p, v) in enumerate(zip(psi, vcos), 1):
        A[32+j], A[32-j] = p/2, -p/2
        V[32+j] = V[32-j] = v/2
    vnorm = sum(map(abs, V), arb(0)).upper()
    transformed = []
    details = []
    remainder_squared = arb(0)
    last_mode = 96
    for ell in range(1, 129):
        E, lo, fee, detail = exponential([-4*ell*x for x in A], arb(2)**-180)
        VE = arb_poly(V)*E
        vlo = lo-32
        end = ell+max(abs(vlo), abs(vlo+len(VE)-1))
        last_mode = max(last_mode, end)
        transformed.append((ell, VE, vlo))
        details.append(dict(physical_index=ell, full_finite_last_moving_mode=end, **detail))
        remainder_squared += 2*(vnorm*fee)**2
    rows = [[coefficient(VE, lo, ell-j)-coefficient(VE, lo, ell+j)
             for ell, VE, lo in transformed] for j in range(97, last_mode+1)]
    high = arb_mat(rows)*difference
    high_norm, hs, schur = matrix_norms(high)
    difference_norm = matrix_norms(difference)[0]
    fee = (remainder_squared.sqrt()*difference_norm).upper()
    return (high_norm+fee).upper(), dict(
        first_moving_high_index=97, complete_finite_last_moving_index=last_mode,
        finite_high_operator_upper=record(high_norm), finite_high_HS_upper=record(hs),
        finite_high_Schur_upper=record(schur),
        complete_exponential_L2_operator_remainder=record(remainder_squared.sqrt().upper()),
        complete_applied_exponential_remainder=record(fee),
        infinite_moving_output_not_truncated=True, exponential_details=details)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--proposal', type=Path, required=True)
    ap.add_argument('--C-matrix', type=Path, default=Path('notes/2026-11-14-R133-repaired-moving96-physical128-C-matrix-native.json.gz'))
    ap.add_argument('--B-matrix', type=Path, default=Path('notes/2026-11-14-R133-repaired-moving193-physical128-B-matrix-native.json.gz'))
    ap.add_argument('--K-matrix', type=Path, default=Path('notes/2026-11-14-R133-repaired-physical128-moving96-residual-matrix-native.json.gz'))
    ap.add_argument('--bridge', type=Path, default=Path('notes/2026-11-14-R133-continuous-repair-complete-moving-cap-bridge-native.json.gz'))
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('preserve each actual cut-row computation')
    started = time.monotonic()
    ctx.prec, ctx.cap = 320, 6
    C, B, K, proposal, bridge = (read(p) for p in (
        args.C_matrix, args.B_matrix, args.K_matrix, args.proposal, args.bridge))
    if sha(args.C_matrix) != C_SHA or sha(args.B_matrix) != B_SHA:
        raise ValueError('the full actual same-cut B/C matrices are required')
    for document in (C, B, K):
        if (not document['complete'] or document['candidate_sha256'] != CURRENT
            or document['derived_definition_sha256'] != REPAIR
            or document['exact_cut'] != str(CUT) or not document['whole_original_eta']
            or document['parameter_half_width'] != '1/1000000000'
            or any(not x['passed'] for x in document['gates'])):
            raise ValueError('a complete same-object whole-eta inlet is missing')
    if (K['kind'] != 'actual_complete_physical128_B_residual_to_moving96_matrix'
        or K['source_sha256'] != K_SOURCE or K['C_matrix_sha256'] != C_SHA):
        raise ValueError('the exact complete residual change of equations changed')
    if (proposal['kind'] != 'actual_repaired_physical128_cap_precomposed_moving96_L2_proposal_v1'
        or not proposal['complete'] or proposal.get('failure')
        or proposal['complete_moving_even_input_columns'] != 97
        or proposal['complete_physical_state_dimension'] != 257
        or proposal['identity']['derived_centre_definition_sha256'] != REPAIR
        or proposal['actual_physical_inlet_matrix']['sha256'] != C_SHA):
        raise ValueError('the complete actual padded 97-column trial is required')
    if (not bridge['complete'] or not bridge['full_residual_sensitive_bridge_proved']
        or bridge['original_candidate_sha256'] != CURRENT
        or bridge['derived_definition_sha256'] != REPAIR
        or bridge['bridge']['parameter_half_width'] != '0'):
        raise ValueError('the actual eta0 residual-sensitive cap bridge is required')
    T, endpoint_details = exact_left_endpoint(proposal)
    S = matrix_rows(K)
    BE = matrix_rows(B, range(96, 193))
    H = matrix_rows(C)
    sqrt2 = arb(2).sqrt()
    normalization = [arb(1)]+[sqrt2]*96
    difference = arb_mat([[ (BE[i, j]*normalization[j]-T[i, j])/sqrt2
                           for j in range(97)] for i in range(128)])
    even = S*difference
    mean_den = int(C['exact_interval_denominator'])
    mean = interval(C['physical_mean_row']['exact_interval_numerator'], mean_den)
    mean_row = arb_mat([[mean-T[128, 0]]+[-T[128, j] for j in range(1, 97)]])
    even_proposal, even_fee = midpoint_proposal(even)
    mean_proposal, mean_fee = midpoint_proposal(mean_row)
    full_S = box_from_record(K['complete_full_L2_operator_norm'])
    B_tail = box_from_record(B['best_complete_B_tail']['complete_pair_L2_to_physical_B_tail'])
    finite_low_error = (even_fee+full_S*B_tail).upper()
    complete_high, high_details = full_high_transform(C, difference)
    complete_high = (complete_high+full_S*B_tail).upper()
    H_orth = arb_mat([[H[i, j]*normalization[j]/sqrt2 for j in range(97)] for i in range(128)])
    HC = (matrix_norms(H_orth)[0]+box_from_record(C['complete_physical_tail_L2_gain'])).upper()
    chi = box_from_record(bridge['bridge']['bounds']['complete_bridge_feedback'])
    GL = box_from_record(bridge['corrected_all_mode_physical_Green_gains']['inner_C_port'])
    bridge_error = (chi/(1-chi)*GL*HC).upper()
    remaining_mean_margin = (abs(mean_row[0, 0]).lower()-bridge_error).lower()
    # A floating kernel is only a proposal for the conditional complete cut
    # rows.  Mean is eliminated by its actual nonzero coefficient, not set0.
    mean0 = mean_proposal[0, 0]
    E = np.vstack((-mean_proposal[0, 1:]/mean0, np.eye(96)))
    X = np.vstack((-even_proposal@E, E))
    Q, R = qr(X, mode='economic', check_finite=True)
    signs = np.where(np.diag(R) < 0, -1., 1.)
    Q *= signs[None, :]
    rows = np.zeros((97, 193))
    rows[:96, :96] = np.eye(96)
    rows[:96, 96:] = even_proposal
    rows[96, 96:] = mean_proposal[0]
    model_kernel_error = float(np.linalg.norm(rows@Q, 2))
    gram_error = float(np.linalg.norm(Q.T@Q-np.eye(96), 2))
    if not model_kernel_error < 1e-10 or not gram_error < 1e-11:
        raise ValueError('the complete finite cut kernel or physical Gram proposal failed')
    scale = 2**256
    encoded = []
    for i in range(96):
        intervals = [integer_box(even[i, j], scale) for j in range(97)]
        encoded.append(dict(moving_sine_index=i+1,
            complete_even_interval_numerators=[[str(a), str(b)] for a, b in intervals],
            complete_even_binary64_proposal_hex=[x.hex() for x in even_proposal[i]]))
    mean_intervals = [integer_box(mean_row[0, j], scale) for j in range(97)]
    gates = [dict(name=name, passed=bool(ok)) for name, ok in (
        ('same actual repaired whole-eta physical cut in every directed input', True),
        ('all128 physical rows and all97 even moving inputs retained', even.nrows() == 96 and even.ncols() == 97),
        ('complete exact shared-value Hermite trial evaluated at rational9/10', endpoint_details['exact_evaluation_radius'] == '9/10'),
        ('odd moving h1 block is an exact mathematical identity', K['full_moving_h1_boundary_coefficient_is_exact_identity']),
        ('independent mean is retained with all97 input columns', mean_row.ncols() == 97),
        ('complete moving high output and exponential tails are included', high_details['infinite_moving_output_not_truncated']),
        ('whole-eta physical cap and eta0 moving bridge scopes are distinct', bridge['bridge']['parameter_half_width'] == '0'),
        ('actual bridge correction leaves a positive conditional mean-rank margin', remaining_mean_margin > 0),
        ('full finite kernel has96 columns and97 original cut rows', Q.shape == (193, 96) and rows.shape == (97, 193)),
        ('finite complete-kernel proposal check passed', model_kernel_error < 1e-10),
        ('finite physical orthonormal Gram proposal check passed', gram_error < 1e-11),
    )]
    out = dict(kind=KIND, complete=all(x['passed'] for x in gates),
        source_sha256=sha(__file__), candidate_sha256=CURRENT,
        derived_definition_sha256=REPAIR, exact_cut=str(CUT),
        exact_nu=C['exact_nu'], whole_original_eta_for_physical_cut=True,
        physical_parameter_half_width=C['parameter_half_width'],
        actual_moving_residual_bridge_parameter_half_width='0',
        input_sha256={str(p):sha(p) for p in (args.C_matrix, args.B_matrix,
            args.K_matrix, args.proposal, args.bridge)},
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_final_moving96_physical128_C_matrix.py',
            'fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_phase_beta_bulk_interval.py', 'fourfold_phase_metric_defect.py')},
        exact_input_basis='h1:sqrt(2)sin(4j phi); h2:1,sqrt(2)cos(4j phi), j=1..96',
        exact_output_basis='moving odd sqrt(2)sin(4j phi), j=1..96; physical C mean independent',
        exact_odd_block='I_96', exact_interval_denominator=str(scale), rows=encoded,
        independent_mean_row=dict(exact_interval_numerators=[[str(a),str(b)] for a,b in mean_intervals],
            binary64_proposal_hex=[x.hex() for x in mean_proposal[0]]),
        endpoint_evaluation=endpoint_details,
        complete_finite_even_matrix_midpoint_error=record(even_fee),
        complete_low_row_error_before_unknown_cap_error=record(finite_low_error),
        complete_mean_midpoint_error_before_unknown_cap_error=record(mean_fee),
        complete_physical_cap_to_moving_row_gain=record(full_S),
        complete_moving_high_before_unknown_cap_error=record(complete_high),
        complete_high_details=high_details,
        complete_physical_inlet_HC_L2_gain=record(HC),
        eta0_conservative_physical_to_actual_moving_cap_difference=record(bridge_error),
        allowable_complete_physical_cap_error_for_mean_rank=record(remaining_mean_margin),
        true_error_contract=dict(
            physical_even_rows='low_error_before_cap + S_norm * epsilon_cap',
            actual_eta0_moving_even_rows='low_error_before_cap + S_norm * (epsilon_cap + bridge_error)',
            physical_mean='mean_midpoint_error + epsilon_cap',
            actual_eta0_moving_mean='mean_midpoint_error + epsilon_cap + bridge_error',
            actual_eta0_moving_high='complete_high_before_cap + S_norm * (epsilon_cap + bridge_error)',
            epsilon_cap='the complete1977-cell physical cap matrix error, not its completed prefix'),
        kernel_proposal=dict(coordinates='the complete orthonormal moving193 basis',
            complete_basis_binary64_hex=[[float(x).hex() for x in row] for row in Q],
            boundary_residual_2=model_kernel_error, Gram_error_2=gram_error,
            all_96_columns=True, mean_not_zeroed=True, diagnostic_only=True),
        complete_physical_cap_error_has_been_supplied=False,
        continuous_head_inverse_proved=False, complete_body_inverse_proved=False,
        no_head_or_high_boundary_row_deleted=True, gates=gates,
        seconds=time.monotonic()-started)
    save(args.out, out)
    print(dict(complete=out['complete'], high=complete_high.str(14),
        low_error=finite_low_error.str(14), HC=HC.str(14), bridge=bridge_error.str(14),
        mean_margin=remaining_mean_margin.str(14), seconds=out['seconds']), flush=True)
    if not out['complete']:
        raise RuntimeError('an actual complete cut-row gate failed')


if __name__ == '__main__':
    main()
