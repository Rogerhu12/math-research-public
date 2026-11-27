"""BR: complete low target-coordinate rows of the ORIGINAL B inverse.

Pure finite same-sign residuals and joint bounds. The true inverse is the
WBP energy inverse of B=Id+T_w I; its two physical means stay independent.
An actual owner must admit the whole BW carrier/error and original phase.
"""

ROWS = 96
TRIAL_MODES = 192
W_MODES = 2048


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.lower() >= 0, "one whole nonnegative directed upper")
    return value.upper()


def conjugate(api, value):
    return api.acb(value.real, -value.imag)


def complete_same_sign_residual(api, positive_trial_columns, positive_w, true_phase_a):
    """Bdagger Y-G^-1 E96a, retaining all2240 positive outputs and both signs.

    api.acb_poly is directed full polynomial multiplication, with no FFT
    cutoff or cyclic convolution. True a is its complete original ball.
    """
    require(len(positive_trial_columns) == ROWS
            and all(len(column) == TRIAL_MODES for column in positive_trial_columns)
            and len(positive_w) == W_MODES and true_phase_a.is_finite(),
            "all96 full192-mode trials, the whole signed w2048 and true phase")
    require(all(value.is_finite() for column in positive_trial_columns for value in column)
            and all(value.is_finite() for value in positive_w), "every complete directed coefficient")
    M, K = TRIAL_MODES, W_MODES
    wpoly = [api.acb(0) for _ in range(2*K+1)]
    for n, value in enumerate(positive_w, 1):
        wpoly[K+n], wpoly[K-n] = value, conjugate(api, value)
    whole_w = api.acb_poly(wpoly)
    root2 = api.rational(2).sqrt()
    residuals = []
    for j, column in enumerate(positive_trial_columns, 1):
        primitive = [api.acb(0)]+[value/api.acb(0, 4*n) for n, value in enumerate(column, 1)]
        full_product = whole_w*api.acb_poly(primitive)
        require(len(full_product) <= 2*K+M+1, "the entire noncyclic finite product support")
        phase = 2*j*true_phase_a
        forcing = (4*j/root2)*api.acb(phase.cos(), -phase.sin())
        one = []
        for n in range(1, M+K+1):
            direct = column[n-1] if n <= M else api.acb(0)
            product = full_product[K+n] if K+n < len(full_product) else api.acb(0)
            residual = direct-product-(forcing if n == j else api.acb(0))
            require(residual.is_finite(), "one whole same-sign residual coefficient")
            one.append(residual)
        residuals.append(one)
    return residuals


def complete_finite_energy_residual(api, all_positive_residual_columns):
    require(len(all_positive_residual_columns) == ROWS
            and all(len(column) == TRIAL_MODES+W_MODES for column in all_positive_residual_columns),
            "every complete residual column, including outputs193..2240")
    square = api.zero
    for column in all_positive_residual_columns:
        for n, value in enumerate(column, 1):
            require(value.is_finite(), "every full signed coefficient ball")
            radius = abs(value).upper()
            square = square+2*radius*radius/(4*n)
    return square.sqrt().upper()


def complete_primitive_trial_norms(api, positive_trial_columns):
    require(len(positive_trial_columns) == ROWS
            and all(len(column) == TRIAL_MODES for column in positive_trial_columns),
            "all complete original finite trial columns")
    square, vector_W = api.zero, api.zero
    for n in range(1, TRIAL_MODES+1):
        one = sum((abs(column[n-1]).upper()**2/(4*n)**2 for column in positive_trial_columns), api.zero)
        square = square+2*one
        vector_W = vector_W+one.sqrt().upper()
    return {"complete_I_trial_Hilbert_Schmidt_upper": square.sqrt().upper(),
            "complete_positive_I_trial_vector_Wiener_upper": vector_W.upper()}


def complete_w_product_candidates(api, saved_w_Linf_error, saved_w_L2_error,
                                  saved_I_HS, saved_positive_I_vector_W):
    e0, e2, H, W = map(up, (saved_w_Linf_error, saved_w_L2_error,
                           saved_I_HS, saved_positive_I_vector_W))
    return {"complete_target_w_Linf_product_upper": (e0*H).upper(),
            "complete_target_w_L2_product_upper": (api.rational(2).sqrt()*e2*W).upper()}


def complete_target_row_error(api, saved_full_finite_energy_residual, saved_whole_w_product):
    finite, product = map(up, (saved_full_finite_energy_residual, saved_whole_w_product))
    energy = (finite+product/2).upper()
    return {"complete_target_B_adjoint_joint_energy_residual_upper": energy,
            "complete_target_B_inverse96_joint_L2_row_error_upper": (energy/2).upper()}


def complete_target_coordinate_column_error(api, saved_joint_row_error,
                                           saved_complete_column_trial_norm, saved_full_column_error):
    """Full physical Y_a columns are required, not their96 raw pairings."""
    row, trial, error = map(up, (saved_joint_row_error, saved_complete_column_trial_norm, saved_full_column_error))
    return (row*trial+api.rational(ROWS).sqrt()*error).upper()
