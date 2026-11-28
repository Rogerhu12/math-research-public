"""Matrix-free actions for the CFC row in the *constrained* WGB coordinate.

Operators, vectors, scalar bounds and order tests are supplied by the caller
in the actual directed arithmetic. No finite Fourier cutoff is implicit.
"""
def physical_cross_action(*, low_state, physical96, metric, translation,
                          source, constraint_rhs, selected_columns, metric_column,
                          apply_K, high_projection, low_projection, theta,
                          inverse_high, theta_columns, theta_metric,
                          phase_readout, height_readout, phase_rhs, height_rhs):
    """Return the full reduced residual and the original high state.

    readout(w,c,k) includes the core, exterior, direct, normalizer and affine
    source responses at zero absolute translation. The signed theta_columns
    are evaluations of theta on the same selected_columns, never Θ itself.
    """
    Kq = apply_K(low_state)
    Xc = selected_columns(physical96)
    gk = metric_column * metric
    high_state = inverse_high(high_projection(source) - high_projection(Kq + Xc + gk))
    whole_state = low_state + high_state
    Kw = Kq + apply_K(high_state)
    return {
        "low_waist": low_state + low_projection(Kw + Xc + gk) - low_projection(source),
        "physical96": theta(Kw) + theta_columns(physical96)
                      + theta_metric * metric - theta(source) + constraint_rhs,
        "phase_mean": phase_readout(whole_state, physical96, metric) - phase_rhs,
        "absolute_mean_height": height_readout(whole_state, physical96, metric)
                                + translation - height_rhs,
        "high_state": high_state,
    }


def physical_cross_error(*, whole_theta_norm, high_K_norm, cfc_tail_norm,
                         cfc_theta_matrix_error, one, strictly_positive):
    """Return the joint error radius for the whole 96-square physical block."""
    gap = one - high_K_norm
    if not strictly_positive(gap):
        raise ValueError("strict complete high waist inverse gate required")
    return cfc_theta_matrix_error + (
        whole_theta_norm * high_K_norm * cfc_tail_norm / gap)
