"""JF.5--16: full TC column errors and joint signed finite-matrix gates.

Pure arithmetic only.  No IO, numerical import, old producer, or execution.
The public owner MUST first admit the whole actual original low/58/P224
inverse chain, all224 records, same selected operator, complete TC targets,
complete RW96, and the original SP/PW/WTA/WX receiver identities.  A complete
mapping of scalar bounds is necessary data, not proof of those prerequisites.

NumericalAPI is the directed API used by signed_finite_column_residual_math:
zero, one, lower, rational, sqrt, magnitude; balls have finite/upper/lower.
Every return is unpersisted arithmetic.  The owner saves and reads complete
new bounds, then repeats the strict gate from the saved upper endpoint.
"""

DIMENSION = 96
OUTPUT_CODES = (
    'right97', 'outer96', 'low_body', 'low_root97', 'low_outer96',
    'low_atoms193', 'low_complete', 'high_cut_stableY', 'high_cut_unstableY',
    'high_root_unstableY', 'high_bodyY', 'high_collarY', 'high_globalY',
    'high_raw_Hminus1', 'high_primitive_L2', 'high_root_mixed',
)
RESIDUAL_NAMES = (
    'positive_high_collar', 'positive_high_body', 'positive_low',
    'negative_root', 'negative_strict',
)
RECEIVERS = ('physical_primitive96', 'declared_incoming_cosine96')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite() and api.lower(value) >= 0,
            'finite nonnegative directed bound')
    return value.upper()


def sqrt_upper(api, value):
    return upper(api, api.sqrt(upper(api, value)))


def sum_squares_upper(api, values):
    values = [upper(api, value) for value in values]
    require(values, 'nonempty complete norm list')
    return upper(api, sum((value*value for value in values), api.zero))


def complete_TC_column_errors(api, complete_positive224, residual_columns,
                              CR, CO, C2):
    """JF.5--6, ONLY the TC continuous homogeneous physical root96 columns.

    complete_positive224 maps EVERY (input_index, output_code) to its saved
    upper.  All224 entries are checked; only six multiply nonzero TC ports.
    The owner verifies entire actual files, full original table and all exact
    TC zero identities before this call.  No six-ball-only input is accepted.
    residual_columns contains all96 same-trial saved five-source records in
    their original windows and ordinary dr measure, including both sources.
    """
    keys = {(j, code) for j in range(14) for code in OUTPUT_CODES}
    require(isinstance(complete_positive224, dict)
            and set(complete_positive224) == keys,
            'all224 admitted original positive records, not only six values')
    table = {key: upper(api, complete_positive224[key]) for key in keys}
    require(len(residual_columns) == DIMENSION,
            'all96 original physical root-even trial columns')
    cr, co, c2 = (upper(api, value) for value in (CR, CO, C2))
    columns = []
    for j, saved in enumerate(residual_columns, 1):
        require(isinstance(saved, dict) and set(saved) == set(RESIDUAL_NAMES),
                'all five complete original residual norms per column')
        fc, fb, fl, fn, fs = (upper(api, saved[name]) for name in RESIDUAL_NAMES)
        sources = ((1, fc), (2, fb), (7, fl))
        d = upper(api, sum((table[k, 'low_root97']*value
                            for k, value in sources), api.zero))
        z = upper(api, sum((table[k, 'high_root_mixed']*value
                            for k, value in sources), api.zero))
        root = sqrt_upper(api, upper(api, d*d+z*z))
        error = upper(api, cr*root+co*fn+c2*fs)
        columns.append({
            'column': j,
            'low_odd96_and_moving_mean_root_error_upper': d,
            'high_root_mixed_error_upper': z,
            'complete_physical_root_error_upper': root,
            'complete_waist_column_error_upper': error,
        })
    return columns


def _positive_weights(api, values):
    require(len(values) == DIMENSION
            and all(x.is_finite() and api.lower(x) > 0 for x in values),
            'all96 original strictly positive diagonal weights')


def joint_TC_matrix_error(api, column_errors, waist_trial_norms,
                          RW_scalar_row_errors, source_weights,
                          BH, KW, receiver):
    """JF.7--12.  True target rows g_i are orthonormal; p_i are NOT.

    Every trial column has full finite support96<J_s and BOTH density means,
    as proved by TC.  Thus RW.26 removes KW only from the incoming row-trial
    term.  KW remains on the true-column error in the complete receiver.
    Source weights are distinct from target weights used by the inverse gate.
    """
    require(receiver in RECEIVERS, 'one declared complete96 receiver')
    require(len(column_errors) == len(waist_trial_norms)
            == len(RW_scalar_row_errors) == DIMENSION,
            'complete96 column errors, trial norms, and original row errors')
    _positive_weights(api, source_weights)
    delta = sqrt_upper(api, sum_squares_upper(api, [
        upper(api, value/weight)
        for value, weight in zip(column_errors, source_weights)]))
    trial = sqrt_upper(api, sum_squares_upper(api, [
        upper(api, value/weight)
        for value, weight in zip(waist_trial_norms, source_weights)]))
    rows = sqrt_upper(api, sum_squares_upper(api, RW_scalar_row_errors))
    bh, kw = (upper(api, value) for value in (BH, KW))
    require(kw >= api.one, 'the original mean-identity fixed normalizer bound')
    if receiver == 'physical_primitive96':
        # Multiply by an upper of sqrt(1/2), never divide by a sqrt(2) upper.
        kappa = sqrt_upper(api, api.rational(1, 2))
        gamma = upper(api, bh*kappa)
    else:
        kappa = api.one
        gamma = upper(api, bh*kw)
    column_term = upper(api, gamma*delta)
    row_term = upper(api, kappa*rows*trial)
    return {
        'receiver': receiver,
        'source_weighted_column_error_upper': delta,
        'source_weighted_trial_column_operator_upper': trial,
        'complete_RW_scalar_row_error_l2_upper': rows,
        'complete_true_receiver_upper': gamma,
        'joint_column_error_contribution_upper': column_term,
        'joint_trial_row_error_contribution_upper': row_term,
        'complete_source_weighted_matrix_error_upper': upper(
            api, column_term+row_term),
    }


def _matrix(matrix):
    require(isinstance(matrix, (list, tuple)) and len(matrix) == DIMENSION
            and all(isinstance(row, (list, tuple)) and len(row) == DIMENSION
                    for row in matrix)
            and all(x.is_finite() for row in matrix for x in row),
            'all9216 entries of the same complete signed96 matrix')


def _maximum(api, values):
    result = api.zero
    for value in values:
        value = upper(api, value)
        if value > result:
            result = value
    return result


def _matrix_norms(api, matrix):
    _matrix(matrix)
    row = _maximum(api, [upper(api, sum((api.magnitude(x) for x in values),
                                       api.zero)) for values in matrix])
    col = _maximum(api, [upper(api, sum((api.magnitude(matrix[i][j])
                                       for i in range(DIMENSION)), api.zero))
                         for j in range(DIMENSION)])
    return row, col, sqrt_upper(api, upper(api, row*col))


def complete_joint_weighted_inverse_gate(
        api, signed_trial_entry_balls, exact_dyadic_trial_inverse,
        source_weights, target_weights, complete_matrix_error_upper):
    """JF.13--16 for the WHOLE declared96 matrix, with both weights distinct.

    The same original TC carrier is necessarily rematerialized/hash checked
    by the owner; its balls enclose all finite pairing evaluation error.
    complete_matrix_error_upper is Xi_A from joint_TC_matrix_error, already
    weighted on the source side, with no duplicated evaluation radius.
    The complete signed multiplication is performed before absolute sums.
    This square is not the full physical-mean/phase/nu/high-eliminated Schur.
    """
    _matrix(signed_trial_entry_balls)
    _matrix(exact_dyadic_trial_inverse)
    _positive_weights(api, source_weights)
    _positive_weights(api, target_weights)
    require(all(x.lower() == x.upper()
                for row in exact_dyadic_trial_inverse for x in row),
            'one complete exact dyadic trial inverse')
    xi = upper(api, complete_matrix_error_upper)
    left = [[exact_dyadic_trial_inverse[i][j]*target_weights[j]
             for j in range(DIMENSION)] for i in range(DIMENSION)]
    residual = [[
        (api.one if i == j else api.zero)-sum((
            left[i][k]*signed_trial_entry_balls[k][j]
            for k in range(DIMENSION)), api.zero)/source_weights[j]
        for j in range(DIMENSION)] for i in range(DIMENSION)]
    ri, r1, r0 = _matrix_norms(api, residual)
    li, l1, lt = _matrix_norms(api, left)
    bi, b1, bn = _matrix_norms(api, exact_dyadic_trial_inverse)
    perturbation = upper(api, lt*xi)
    rho = upper(api, r0+perturbation)
    passed = bool(rho < api.one)
    result = {
        'complete_dimension': DIMENSION,
        'complete_signed_trial_residual_matrix': residual,
        'trial_residual_infinity_upper': ri,
        'trial_residual_one_upper': r1,
        'trial_residual_two_upper': r0,
        'preconditioned_target_infinity_upper': li,
        'preconditioned_target_one_upper': l1,
        'preconditioned_target_two_upper': lt,
        'trial_inverse_infinity_upper': bi,
        'trial_inverse_one_upper': b1,
        'trial_inverse_two_upper': bn,
        'preconditioned_joint_error_upper': perturbation,
        'complete_actual_residual_two_upper': rho,
        'strict_unpersisted_finite_inverse_gate_passed': passed,
        'all_full_incoming_Schur_rows_present': False,
        'topic_completion_proved': False,
    }
    if passed:
        gap = (api.one-rho).lower()
        require(api.lower(gap) > 0, 'strict directed complete inverse gap')
        result['inverse_gap_lower'] = gap
        result['weighted_actual_inverse_two_upper'] = upper(api, bn/gap)
    return result
