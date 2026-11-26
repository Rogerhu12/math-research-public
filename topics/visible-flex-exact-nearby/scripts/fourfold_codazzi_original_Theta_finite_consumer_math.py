"""TQ: the original Theta restriction and whole Schur auxiliary rows.

Pure formulas only. The public consumer must admit the WHOLE completed OT
and restore its entire exact96x2240 carrier before using these functions.
All columns use the true normalized target basis v_n^a. This module never
turns SC physical/incoming matrices into target-coordinate columns.
"""

ROWS = 96
TRIAL_MODES = 2240


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(value):
    require(value.is_finite() and value.lower() >= 0,
            "one complete nonnegative whole bound")
    return value.upper()


def _matrix(values, rows, columns, *, exact=False):
    require(type(values) is list and len(values) == rows and rows > 0 and columns > 0
            and all(type(row) is list and len(row) == columns for row in values),
            "the entire declared real matrix, all rows and columns")
    require(all(value.is_finite() for row in values for value in row),
            "all real signed entries are finite")
    if exact:
        require(all(value.lower() == value.upper() for row in values for value in row),
                "the complete original exact dyadic carrier, not new midpoint choices")


def _theta(values):
    _matrix(values, ROWS, TRIAL_MODES, exact=True)


def complete_constraint_square(theta):
    """TQ.4: first96 target columns, AFTER the whole2240-mode admission."""
    _theta(theta)
    return [list(row[:ROWS]) for row in theta]


def complete_rectangle_norm_candidates(api, values):
    """All entries, with Schur and Frobenius candidates returned separately.

    Save/read BOTH complete candidates before selecting a whole bound.
    These are new consumer norms; no old OT/IR/AS norm is reevaluated.
    """
    require(type(values) is list and values and type(values[0]) is list and values[0],
            "one nonempty complete matrix")
    rows, columns = len(values), len(values[0])
    _matrix(values, rows, columns)
    magnitudes = [[api.magnitude(value) for value in row] for row in values]
    infinity = max(sum(row, api.zero).upper() for row in magnitudes)
    one = max(sum((magnitudes[i][j] for i in range(rows)), api.zero).upper()
              for j in range(columns))
    square = sum((value*value for row in magnitudes for value in row), api.zero).upper()
    return {"complete_infinity_upper": infinity, "complete_one_upper": one,
            "complete_Schur_two_candidate": (infinity*one).sqrt().upper(),
            "complete_Frobenius_candidate": square.sqrt().upper()}


def complete_constraint_gate_ingredients(api, theta, trial_inverse):
    """Full signed E0=I-B*T_hat BEFORE absolute values; all96x96 entries."""
    square = complete_constraint_square(theta)
    _matrix(trial_inverse, ROWS, ROWS, exact=True)
    residual = [[(api.one if i == j else api.zero)-sum(
        (trial_inverse[i][k]*square[k][j] for k in range(ROWS)), api.zero)
        for j in range(ROWS)] for i in range(ROWS)]
    return {"complete_signed_square": square,
            "complete_exact_trial_inverse": trial_inverse,
            "complete_signed_preconditioned_residual": residual,
            "trial_inverse_norm_candidates": complete_rectangle_norm_candidates(api, trial_inverse),
            "trial_residual_norm_candidates": complete_rectangle_norm_candidates(api, residual)}


def complete_constraint_residual_from_saved_bounds(api, saved_r0, saved_b, saved_OT_error):
    """TQ.6. The caller then saves/reads this WHOLE new residual upper."""
    r0, b, error = map(upper, (saved_r0, saved_b, saved_OT_error))
    return (r0+b*error).upper()


def complete_constraint_inverse_from_saved_residual(api, saved_rho, saved_b):
    """TQ.7: false remains an explicit outcome of the sufficient gate."""
    rho, b = map(upper, (saved_rho, saved_b))
    passed = bool(rho < api.one)
    result = {"finite_coordinate_inverse_proved": passed,
              "physical_PDE_column_inverse_proved": False,
              "full_physical_Schur_proved": False,
              "complete_coordinate_inverse_two_upper": None}
    if passed:
        gap = (api.one-rho).lower()
        require(gap > 0, "strict gap from the entire saved residual upper")
        result["complete_coordinate_inverse_two_upper"] = (b/gap).upper()
    return result


def complete_signed_actions(api, theta, finite_target_columns):
    """TQ.14 exact trial product. Rows of X are target Fourier MODE labels.

    Every supplied mode and every column is validated. Terms past2240
    vanish only because the original Theta TRIAL is exactly zero there;
    the true full column and its infinite error are paid separately.
    """
    _theta(theta)
    require(type(finite_target_columns) is list and finite_target_columns
            and type(finite_target_columns[0]) is list and finite_target_columns[0],
            "whole finite target-coordinate columns")
    modes, columns = len(finite_target_columns), len(finite_target_columns[0])
    _matrix(finite_target_columns, modes, columns)
    overlap = min(modes, TRIAL_MODES)
    return [[sum((theta[j][n]*finite_target_columns[n][k] for n in range(overlap)), api.zero)
             for k in range(columns)] for j in range(ROWS)]


def complete_joint_action_candidates(api, saved_OT_error, saved_theta_trial_norm,
                                     saved_column_trial_norm, saved_full_column_error,
                                     saved_true_column_norm=None):
    """Whole operator errors; no per-target-row sqrt96 is introduced."""
    e, t, x, d = map(upper, (saved_OT_error, saved_theta_trial_norm,
                            saved_column_trial_norm, saved_full_column_error))
    result = {"complete_trial_column_decomposition": (e*x+(t+e)*d).upper()}
    if saved_true_column_norm is not None:
        result["complete_true_column_decomposition"] = (
            e*upper(saved_true_column_norm)+t*d).upper()
    return result


def complete_high_solve_error(api, saved_high_inverse_norm, saved_full_high_residual):
    """TQ.17 requires the ENTIRE high residual, including infinite outputs."""
    return (upper(saved_high_inverse_norm)*upper(saved_full_high_residual)).upper()


def complete_constraint_schur_trial(api, theta, complete_high_trial, *,
                                    target_cutoff, extra_physical_coordinates,
                                    auxiliary_coordinates, metric_coordinates=1):
    """TQ.15--16: first96 rows of the ORIGINAL complete WGB.32 matrix.

    The source order is q in Q_J Y, all extra physical q slots, all z
    factors (physical96 FIRST), then the actual metric coordinate.
    complete_high_trial is W_hat for ALL these columns in that order.
    This does not certify H, W_hat's full residual or any remaining row.
    """
    _theta(theta)
    require(type(target_cutoff) is int and target_cutoff >= 97
            and type(extra_physical_coordinates) is int and extra_physical_coordinates >= 0
            and type(auxiliary_coordinates) is int and auxiliary_coordinates >= ROWS
            and metric_coordinates == 1,
            "the complete original target/physical/factor/metric index ledger")
    q_dimension = target_cutoff-1+extra_physical_coordinates
    columns = q_dimension+auxiliary_coordinates+metric_coordinates
    require(type(complete_high_trial) is list and complete_high_trial,
            "the entire high trial in consecutive target mode coordinates")
    _matrix(complete_high_trial, len(complete_high_trial), columns)
    for row in complete_high_trial[:min(target_cutoff-1, len(complete_high_trial))]:
        require(all(value.lower() == value.upper() == api.zero for value in row),
                "the declared high trial is exactly in P_J, including every column")
    result = complete_signed_actions(api, theta, complete_high_trial)
    for j in range(ROWS):
        for n in range(min(target_cutoff-1, TRIAL_MODES)):
            result[j][n] = result[j][n]-theta[j][n]
        # J96 is the first physical-coordinate block of the exact z identity.
        result[j][q_dimension+j] = result[j][q_dimension+j]+api.one
    return result
