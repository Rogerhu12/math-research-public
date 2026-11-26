"""DT: the ORIGINAL same-sign Toeplitz action on all96 finite dual rows.

Pure formulas, no imports, IO, producer, proposal, coefficient solve or
numerical runtime. An owner supplies whole formally saved carriers and
its directed arithmetic API. The original source coefficient is alpha
=v_i-w with its full independent approximation error.
"""


def require(ok, message):
    if not ok:
        raise ValueError(message)


def conjugate(api, value):
    return api.acb(value.real, -value.imag)


def complete_finite_original_source_rows(api, positive_z_columns, positive_alpha):
    """DT.5 for all96 real rows with a declared zero-mean alpha trial.

    positive_z_columns[j][n-1] is the coefficient of exp(4 i n x).
    positive_alpha[ell-1] supplies its same fixed real coefficient trial;
    negative coefficients are exact conjugates and alpha_0 is exact zero.
    No negative INPUT frequency is used in a positive OUTPUT block.
    The returned real rows have degree M+L, including all output modes.
    """
    require(len(positive_z_columns) == 96, "all96 whole original dual trials")
    M = len(positive_z_columns[0])
    L = len(positive_alpha)
    require(M > 0 and all(len(column) == M for column in positive_z_columns),
            "the entire common finite trial degree")
    require(all(value.is_finite() for column in positive_z_columns for value in column)
            and all(value.is_finite() for value in positive_alpha),
            "whole exact or certified finite carrier coefficients")
    alpha = {0: api.acb(0)}
    for ell, value in enumerate(positive_alpha, 1):
        alpha[ell], alpha[-ell] = value, conjugate(api, value)
    rows = []
    for column in positive_z_columns:
        primitive = [value / (4*n) for n, value in enumerate(column, 1)]
        conv = [api.acb(0) for _ in range(M+L)]
        for n, value in enumerate(primitive, 1):
            for ell in range(-L, L+1):
                k = n+ell
                if k > 0:
                    conv[k-1] = conv[k-1] + alpha[ell]*value
        positive = []
        for k, value in enumerate(conv, 1):
            direct = primitive[k-1] if k <= M else api.acb(0)
            coefficient = direct + value/api.acb(0, 4*k)
            require(coefficient.is_finite(), "one whole original same-sign row coefficient")
            positive.append(coefficient)
        full = {0: api.acb(0)}
        for k, value in enumerate(positive, 1):
            full[k], full[-k] = value, conjugate(api, value)
        rows.append(full)
    return rows


def complete_G_trial_Hilbert_Schmidt_upper(api, positive_z_columns):
    """DT.6; a new finite norm, evaluated only if not already completed."""
    require(len(positive_z_columns) == 96, "all96 complete finite trials")
    M = len(positive_z_columns[0])
    require(M > 0 and all(len(column) == M for column in positive_z_columns),
            "one whole common degree")
    square = api.zero
    for column in positive_z_columns:
        for n, value in enumerate(column, 1):
            require(value.is_finite(), "one complete finite signed coefficient")
            magnitude = abs(value).upper()
            square += 2*magnitude*magnitude/api.rational((4*n)**2)
    return square.upper().sqrt().upper()


def complete_original_joint_row_errors(api, *, alpha_A0_upper,
                                      alpha_trial_error_upper,
                                      whole_IR_energy_error,
                                      whole_IR_L2_error,
                                      whole_G_trial_norm,
                                      original_model_one_loss_norm):
    """DT.7--8 from whole completed qualifications, without new admission.

    An actual owner must first validate original same-sign alpha, the
    entire IL/SDI/IR actual identities, and the model's true phases/means.
    These formulas alone are not claims that those inputs have arrived.
    """
    values = (alpha_A0_upper, alpha_trial_error_upper, whole_IR_energy_error,
              whole_IR_L2_error, whole_G_trial_norm, original_model_one_loss_norm)
    require(all(value.is_finite() and value.lower() >= 0 for value in values),
            "whole nonnegative qualified same-object upper bounds")
    A0, error, epsH, eps0, ZG, KG = [value.upper() for value in values]
    KA = api.one+A0/4
    VQ = KA*epsH/2+error*ZG/4
    Theta = KG*(api.rational(1071, 1000)*KA*(eps0+api.rational(10, 9)*epsH)
                +api.rational(21, 20)*error*ZG)
    return {"complete_VQ_joint_L2_row_error_upper": VQ.upper(),
            "complete_Theta_joint_one_loss_error_upper": Theta.upper(),
            "same_sign_source_Toeplitz_used": True,
            "extra_sqrt96_applied": False,
            "physical_mean_or_parameter_equations_eliminated": False,
            "actual_signed_matrix_or_full_Schur_claimed": False}
