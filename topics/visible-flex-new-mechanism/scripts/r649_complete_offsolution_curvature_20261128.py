#!/usr/bin/env python3
"""Actual continuous-position curvature, retaining off-solution S and S_s.

R649 supplies the formulas. This is interval algebra for one actual field,
not a model builder, optimizer, source-error certificate, FFT or point query.
The enclosing source owns the real radial/angular cells and every original
source/primitive error. No finite sample is silently turned into a continuous
enclosure. The fixed field's target radial arc coordinate is used only as a
regular coordinate; its metric is not redefined from the approximate field.
"""
from collections import defaultdict
import hashlib
import math
import os
from pathlib import Path


BACKEND_SOURCE = 'r611_circular_reference_global_geometry_20261127.py'
BACKEND_SHA = 'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f'
_path = Path(__file__).with_name(BACKEND_SOURCE)
if hashlib.sha256(_path.read_bytes()).hexdigest() != BACKEND_SHA:
    raise ValueError('the declared outward interval backend changed')
from r611_circular_reference_global_geometry_20261127 import I, sqrt_i, sin_i, cos_i


SCHEMA = 'r649-complete-offsolution-actual-position-interval-curvature-v1'
COUNTS = defaultdict(int)
RAW_KEYS = ('r', 'E', 'Er', 'Err', 'p', 'pr', 'prr', 'q', 't', 'pt', 'prt', 'tr')
GLOBAL_KEYS = ('A', 'G', 'Gr', 'Pi_a', 'Pi_R', 'Pi_Rr')
ARC_FIRST_KEYS = ('r', 'r_s', 'P', 'P_s', 'q', 'q_s', 't', 'U0', 'k', 'h', 'sT', 'sn')
ARC_DEFECT_DERIVATIVE_KEYS = ('U0_s', 'ssT', 'ssn')


def public_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('actual scientific interval arithmetic belongs to the public Actions scope')


def intervals(values, keys):
    if not isinstance(values, dict) or any(key not in values for key in keys):
        raise ValueError('the complete actual interval input is required')
    for key in keys:
        value = values[key]
        if not isinstance(value, I) or not math.isfinite(value.lo) or not math.isfinite(value.hi):
            raise TypeError('finite outward continuous intervals required: ' + key)
    return {key: values[key] for key in keys}


def positive(*values):
    if any(not isinstance(value, I) or value.lo <= 0 for value in values):
        raise ArithmeticError('the actual cell has no proved positive geometric denominator')


def upper_nonnegative(value):
    """Use only where the represented expression is mathematically nonnegative."""
    return I(0, max(0., value.hi))


def abs_i(value):
    if value.lo <= 0 <= value.hi:
        return I(0, max(-value.lo, value.hi))
    return I(min(abs(value.lo), abs(value.hi)), max(abs(value.lo), abs(value.hi)))


def square_sum(*values):
    result = I(0)
    for value in values:
        result += value ** 2
    # The exact sum is nonnegative; eliminate only outward addition noise
    # below zero, not a missing domain assumption.
    return I(max(0., result.lo), result.hi)


def evidence(row):
    if (not isinstance(row, dict) or not isinstance(row.get('same_field_identity'), dict)
            or not row['same_field_identity']
            or row.get('continuous_enclosure_status') not in (
                'all_declared_input_errors_enclosed', 'conditional_on_declared_input_errors')
            or not isinstance(row.get('unresolved_errors'), list)):
        raise ValueError('the actual continuous field and input error status must be explicit')
    if (row['continuous_enclosure_status'] == 'all_declared_input_errors_enclosed'
            and row['unresolved_errors']):
        raise ValueError('unresolved input errors cannot receive enclosed status')
    return dict(row)


def tree_intervals(value):
    if isinstance(value, I):
        return {'lo': value.lo, 'hi': value.hi}
    if isinstance(value, dict):
        return {key: tree_intervals(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [tree_intervals(item) for item in value]
    return value


def full_radial_defect_kernel(raw, global_intervals, *, input_evidence):
    """Exact R_r and the FULL vector H/H_r coefficients at a true r cell.

    pt=Z_{r theta}, prt=Z_{rr theta}, tr=Z_{r theta theta}, prr=Z_{rrr}.
    Gr is the actual continuous mean of R_r. Pi_a/Pi_R/Pi_Rr are the actual
    continuous zero-mean primitives on this same field and radial/angle cell.
    The returned H_T,H_JT are coefficients of a theta-dependent frame;
    taking their scalar primitive first would be incorrect.
    """
    public_only()
    raw = intervals(raw, RAW_KEYS)
    mean = intervals(global_intervals, GLOBAL_KEYS)
    source = evidence(input_evidence)
    r, E, Er, Err, p, pr, prr, q, t, pt, prt, tr = [raw[key] for key in RAW_KEYS]
    A, G, Gr, Pa, PR, PRr = [mean[key] for key in GLOBAL_KEYS]
    positive(r, E, A)
    b2 = r ** 2 - q ** 2
    positive(b2)
    b = sqrt_i(b2)
    u2 = E - r ** 2 * p ** 2 / b2
    positive(u2)
    u = sqrt_i(u2)
    N = r / b + r ** 2 * p * t / b ** 3
    positive(N)
    a = N / u
    v = -p * q / b
    br = (r - q * pt) / b
    bt = -q * t / b
    vr = -(pr * q + p * pt) / b + p * q * br / b2
    ur = (Er / 2 - r * p ** 2 / b2 - r ** 2 * p * pr / b2
          + r ** 2 * p ** 2 * br / b ** 3) / u
    ut = -r ** 2 * p * pt / (u * b2) - r ** 2 * p ** 2 * q * t / (u * b2 ** 2)
    C = E * t + r * p
    B = pt - q / r
    M = r + p * t - q ** 2 / r
    omega = r ** 2 / (u ** 3 * b ** 3)
    D = C * pr - E * B ** 2 - Er * M / 2
    R = omega * D
    Cr = Er * t + E * tr + p + r * pr
    Br = prt - pt / r + q / r ** 2
    Mr = 1 + pr * t + p * tr - 2 * q * pt / r + q ** 2 / r ** 2
    Dr = Cr * pr + C * prr - Er * B ** 2 - 2 * E * B * Br - Err * M / 2 - Er * Mr / 2
    Rr = omega * Dr + (2 / r - 3 * ur / u - 3 * br / b) * R
    K = r ** 2 * p * B / (u * b ** 3)
    Kr = (2 * r * p * B + r ** 2 * (pr * B + p * Br)) / (u * b ** 3) \
         - K * (ur / u + 3 * br / b)
    Kt = r ** 2 * (pt * B + p * (tr - t / r)) / (u * b ** 3) \
         - K * (ut / u + 3 * bt / b)
    ar = Kt + R
    utr = ar * v + a * vr - br * K - b * Kr
    Nr = 1 / b - r * br / b2 + (2 * r * p * t + r ** 2 * (pr * t + p * tr)) / b ** 3 \
         - 3 * r ** 2 * p * t * br / b ** 4
    F = A - 1
    phase_r = (K + PR) / A - Pa * G / A ** 2
    phase_theta = a / A
    Q = PR - Pa * G / A
    Qr = PRr - (K + PR) * G / A - Pa * Gr / A + Pa * G ** 2 / A ** 2
    c, cr = F / A, G / A ** 2
    db, dbr = b / A, br / A - b * G / A ** 2
    HT, HJ = c * N, c * ut + db * Q
    HrT = cr * N + c * Nr - phase_r * HJ
    HrJ = cr * ut + c * utr + dbr * Q + db * Qr + phase_r * HT
    COUNTS['complete_actual_radial_H_Hr_Rr_interval_blocks'] += 1
    return {
        'schema': SCHEMA, 'raw_intervals': raw, 'global_intervals': mean,
        'input_evidence': source,
        'b': b, 'br': br, 'bt': bt, 'u': u, 'ur': ur, 'ut': ut, 'utr': utr,
        'v': v, 'vr': vr, 'N': N, 'Nr': Nr, 'a': a, 'ar': ar,
        'C': C, 'B': B, 'M': M, 'D': D, 'R': R, 'Rr': Rr,
        'K': K, 'Kr': Kr, 'Ktheta': Kt,
        'F': F, 'Q': Q, 'Qr': Qr,
        'normal_angle_delta': Pa / A,
        'normal_angle_r': phase_r, 'normal_angle_theta': phase_theta,
        'H_coefficient_T': HT, 'H_coefficient_JT': HJ,
        'Hr_coefficient_T': HrT, 'Hr_coefficient_JT': HrJ,
        'frame_derivative_terms_retained': True,
        'complete_F_G_Gr_and_nonzero_R_terms_retained': True,
        'scalar_primitives_of_frame_coefficients_are_not_vector_primitives': True,
        'mean_c0_p_or_B_denominators_introduced': False,
        'angle_integrals_primitive_errors_or_original_source_errors_paid_by_this_call': False}


def arc_input_from_complete_vector_primitives(kernel, theta, PiH, PiHr, *, primitive_evidence):
    """Interior r->s conversion after the TRUE full vector primitives.

    PiH/PiHr are pairs of global planar-component intervals, not scalar
    primitives of H_T/H_JT. Use independently supplied regular core s jets
    at an endpoint where raw r derivatives are not finite.
    """
    public_only()
    if kernel.get('schema') != SCHEMA:
        raise ValueError('one complete same-source radial kernel is required')
    source = evidence(primitive_evidence)
    old_source = evidence(kernel['input_evidence'])
    if source['same_field_identity'] != old_source['same_field_identity']:
        raise ValueError('the full vector primitives must belong to the same continuous field')
    if (not isinstance(theta, I) or len(PiH) != 2 or len(PiHr) != 2
            or any(not isinstance(value, I) for value in tuple(PiH) + tuple(PiHr))):
        raise TypeError('one true theta cell and both complete planar vector primitive enclosures are required')
    raw = kernel['raw_intervals']
    r, E, Er, p, pr, q, t, pt = [raw[key] for key in ('r', 'E', 'Er', 'p', 'pr', 'q', 't', 'pt')]
    rootE = sqrt_i(E)
    chi = 1 / rootE
    chi_s = -Er / (2 * E ** 2)
    phi = theta + kernel['normal_angle_delta']
    cosine, sine = cos_i(phi), sin_i(phi)
    tangent, normal = (-sine, cosine), (cosine, sine)
    S = tuple(chi * value for value in PiH)
    Ss = tuple(PiHr[i] / E + chi_s * PiH[i] for i in range(2))

    def dot(values, frame):
        return values[0] * frame[0] + values[1] * frame[1]

    answer = {
        'r': r, 'r_s': chi, 'P': chi * p, 'P_s': pr / E + chi_s * p,
        'q': q, 'q_s': chi * pt, 't': t,
        'U0': chi * kernel['u'], 'U0_s': kernel['ur'] / E + chi_s * kernel['u'],
        'h': chi * kernel['normal_angle_r'], 'k': kernel['normal_angle_theta'],
        'sT': dot(S, tangent), 'sn': dot(S, normal),
        'ssT': dot(Ss, tangent), 'ssn': dot(Ss, normal)}
    # Both error lists remain present even when the primitive producer owns
    # an additional alias/integration error beyond the radial input source.
    combined = {
        'same_field_identity': source['same_field_identity'],
        'continuous_enclosure_status':
            ('all_declared_input_errors_enclosed'
             if source['continuous_enclosure_status'] == old_source['continuous_enclosure_status']
                == 'all_declared_input_errors_enclosed'
             else 'conditional_on_declared_input_errors'),
        'unresolved_errors': old_source['unresolved_errors'] + source['unresolved_errors'],
        'radial_kernel_evidence': old_source, 'vector_primitive_evidence': source}
    COUNTS['same_field_actual_arc_coordinate_interval_conversions'] += 1
    return {
        'arc_intervals': answer, 'input_evidence': combined,
        'global_S_intervals': S, 'global_S_s_intervals': Ss,
        'normal_angle_interval': phi,
        'moving_frame_derivative_is_vector_derivative_then_projection': True,
        'actual_third_jet_or_vector_primitive_calls_added': 0,
        'singular_core_endpoint_claimed_from_raw_r_infinities': False}


def actual_arc_curvature(arc, *, input_evidence, actual_Yss_frame=None,
                         actual_Yss_evidence=None, Z=None, core_height=None, tau=None):
    """Curvature of the ACTUAL current position, including complete defects.

    All arc entries enclose the same regular target s coordinate. The
    ssT/ssn entries are S_s dot T/n, not derivatives of S dot T/n.
    An already-paid actual Y_ss enclosure may instead supply (L_T,L_n);
    then no new S_s or U0_s reconstruction is performed.
    """
    public_only()
    source = evidence(input_evidence)
    values = intervals(arc, ARC_FIRST_KEYS)
    r, rs, P, Ps, q, qs, t, U0, k, h, sT, sn = [values[key] for key in ARC_FIRST_KEYS]
    positive(r)
    b2 = r ** 2 - q ** 2
    positive(b2)
    b = sqrt_i(b2)
    bs = (r * rs - q * qs) / b
    bt = -q * t / b
    V0 = -P * q / b
    V0s = -(Ps * q + P * qs) / b + P * q * bs / b2
    V, U = V0 + sT, U0 + sn
    if actual_Yss_frame is None:
        extra = intervals(arc, ARC_DEFECT_DERIVATIVE_KEYS)
        LT = V0s + U0 * h + extra['ssT']
        Ln = extra['U0_s'] - V0 * h + extra['ssn']
        acceleration_source = {
            'kind': 'complete_actual_S_s_and_regular_base_jets',
            'actual_S_s_vector_derivative_retained': True,
            'same_source_evidence': source}
    else:
        if len(actual_Yss_frame) != 2 or any(not isinstance(value, I) for value in actual_Yss_frame):
            raise TypeError('the already-enclosed actual Y_ss requires both moving-frame projections')
        accel_evidence = evidence(actual_Yss_evidence)
        if accel_evidence['same_field_identity'] != source['same_field_identity']:
            raise ValueError('the actual Y_ss enclosure belongs to another continuous field')
        LT, Ln = actual_Yss_frame
        acceleration_source = {
            'kind': 'already_paid_true_Y_ss_interval_used_directly',
            'same_source_evidence': accel_evidence,
            'new_S_s_base_derivative_or_position_queries': 0}
        source = {
            'same_field_identity': source['same_field_identity'],
            'continuous_enclosure_status':
                ('all_declared_input_errors_enclosed'
                 if source['continuous_enclosure_status'] == accel_evidence['continuous_enclosure_status']
                    == 'all_declared_input_errors_enclosed'
                 else 'conditional_on_declared_input_errors'),
            'unresolved_errors': source['unresolved_errors'] + accel_evidence['unresolved_errors'],
            'first_jet_evidence': source, 'second_jet_evidence': accel_evidence}
    CN = V * q - P * b
    Q2 = square_sum(U * r, CN)
    positive(Q2)
    Q = sqrt_i(Q2)
    e = square_sum(U, V, P)
    f = (b * V + q * P) / r
    determinant = square_sum(U, CN / r)
    positive(determinant)
    B11 = (-U * q * LT + CN * Ln + U * b * Ps) / Q
    B12 = (-U * q * bs - CN * b * h + U * b * qs) / (Q * r)
    B22 = (-U * q * bt - CN * b * k + U * b * t) / (Q * r ** 2)
    A11 = (B11 - 2 * f * B12 + f ** 2 * B22) / determinant
    A12 = (B12 - f * B22) / sqrt_i(determinant)
    A22 = B22
    discriminant_root = sqrt_i(square_sum(A11 - A22, 2 * A12))
    spectral = upper_nonnegative((abs_i(A11 + A22) + discriminant_root) / 2)
    rows0, rows1 = abs_i(A11) + abs_i(A12), abs_i(A22) + abs_i(A12)
    row_bound = I(0, max(rows0.hi, rows1.hi))
    curvature_upper = I(0, min(spectral.hi, row_bound.hi))
    e_error = e - 1
    eta = upper_nonnegative((abs_i(e_error) + sqrt_i(square_sum(e_error, 2 * f))) / 2)
    normal_z = U * b / Q
    planar_jacobian = b * U
    height_margin = curvature_margin = None
    if tau is not None:
        if not isinstance(tau, I):
            raise TypeError('the declared reach scale must retain its outward input interval')
        positive(tau)
        curvature_margin = 1 - tau * curvature_upper
        if Z is not None or core_height is not None:
            if not isinstance(Z, I) or not isinstance(core_height, I):
                raise TypeError('the actual height and matching core height must both be supplied')
            height_margin = Z - core_height - tau * abs_i(normal_z)
    elif Z is not None or core_height is not None:
        raise ValueError('the same declared tau is necessary to consume a height gate')
    COUNTS['complete_actual_regular_arc_curvature_interval_blocks'] += 1
    result = {
        'schema': SCHEMA,
        'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'outward_backend_sha256': BACKEND_SHA,
        'input_evidence': source,
        'actual_radial_second_derivative_source': acceleration_source,
        'real_radial_arc_inputs': values,
        'actual_horizontal_radial_components': {'U': U, 'V': V},
        'actual_horizontal_radial_acceleration_components': {'L_T': LT, 'L_n': Ln},
        'actual_spatial_area_squared_for_s_theta': Q2,
        'actual_spatial_unit_normal_T_n_z': (-U * q / Q, CN / Q, normal_z),
        'actual_relative_metric_e_f_g': (e, f, I(1)),
        'actual_relative_metric_determinant': determinant,
        'actual_relative_metric_operator_upper': eta,
        'actual_second_form_in_target_unit_frame': ((B11, B12), (B12, B22)),
        'actual_second_form_in_true_orthonormal_frame': ((A11, A12), (A12, A22)),
        'actual_principal_curvature_intervals':
            ((A11 + A22 - discriminant_root) / 2, (A11 + A22 + discriminant_root) / 2),
        'actual_absolute_principal_curvature_spectral_upper': spectral,
        'actual_absolute_principal_curvature_row_sum_upper': row_bound,
        'actual_absolute_principal_curvature_upper': curvature_upper,
        'actual_horizontal_Jacobian_s_theta_interval': planar_jacobian,
        'actual_horizontal_Jacobian_strictly_positive_on_supplied_cell': planar_jacobian.lo > 0,
        'actual_scalar_turning_strictly_positive_on_supplied_cell': k.lo > 0,
        'actual_upper_height_gate_interval_or_unrequested': height_margin,
        'actual_one_minus_tau_K_interval_or_unrequested': curvature_margin,
        'target_metric_or_normal_z_substituted_for_actual_geometry': False,
        'divides_by_normal_z': False,
        'full_F_G_phase_and_S_s_chain_required_by_inputs': True,
        'new_ODE_mean_root_J_FFT_quadrature_or_position_queries': 0,
        'continuous_input_qualification_upgraded_by_this_algebra': False,
        'full_R645_global_hypotheses_or_README_completion_claimed': False,
        'consumer_cumulative_interval_block_counts': dict(COUNTS)}
    return result
