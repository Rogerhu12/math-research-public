"""TP: full same-sign alpha-error products for the original96 Theta rows.

Pure new finite-carrier formulas. No imports, IO, old norm, old residual,
proposal, numerical runtime or scientific target invocation.
"""


def require(ok, message):
    if not ok:
        raise ValueError(message)


def up(value):
    require(value.is_finite() and value.lower() >= 0, "one complete nonnegative upper")
    return value.upper()


def complete_new_finite_carrier_norms(api, positive_z_columns, positive_alpha):
    require(len(positive_z_columns) == 96
            and all(len(column) == 192 for column in positive_z_columns)
            and len(positive_alpha) == 2048,
            "the full original192x96 IR and2048-mode AS carriers")
    require(all(value.is_finite() for column in positive_z_columns for value in column)
            and all(value.is_finite() for value in positive_alpha),
            "every exact signed coefficient is present")
    square, BZ = api.zero, api.zero
    for n in range(1, 193):
        one = sum((abs(column[n-1]).upper()**2/(4*n)**2
                   for column in positive_z_columns), api.zero).upper()
        square = square+2*one
        BZ = BZ+one.sqrt().upper()
    Atrial = 2*sum((abs(value).upper() for value in positive_alpha), api.zero)
    return {"complete_G_trial_Hilbert_Schmidt_upper": square.sqrt().upper(),
            "complete_positive_G_trial_vector_Wiener_upper": BZ.upper(),
            "complete_alpha_trial_Wiener_upper": Atrial.upper()}


def complete_product_candidates(api, *, alpha_Linf_error, alpha_L2_error,
                                G_trial_HS, positive_G_vector_Wiener):
    """Save both whole candidates before choosing one in the actual owner."""
    e0, e2, ZG, BZ = map(up, (alpha_Linf_error, alpha_L2_error,
                             G_trial_HS, positive_G_vector_Wiener))
    return {"complete_alpha_Linf_product_upper": (e0*ZG).upper(),
            "complete_alpha_L2_product_upper": (api.rational(2).sqrt()*e2*BZ).upper()}


def complete_true_alpha_upper(api, whole_trial_Wiener, whole_AS_Linf_error):
    return (up(whole_trial_Wiener)+up(whole_AS_Linf_error)).upper()


def complete_original_joint_errors(api, *, true_alpha_upper, whole_alpha_product,
                                   whole_IR_energy_error, whole_IR_L2_error,
                                   original_model_one_loss_norm):
    A0, P, epsH, eps0, KG = map(up, (true_alpha_upper, whole_alpha_product,
        whole_IR_energy_error, whole_IR_L2_error, original_model_one_loss_norm))
    KA = api.one+A0/4
    return {"complete_original_VQ_joint_L2_error_upper": (KA*epsH/2+P/4).upper(),
            "complete_original_Theta_before_rounding_error_upper":
                (KG*(api.rational(1071, 1000)*KA*(eps0+api.rational(10, 9)*epsH)
                     +api.rational(21, 20)*P)).upper()}
