"""DB: complete same-sign density inverse regularity and full Theta rows.

Pure directed formulas, no IO or numerical imports.  The caller admits the
same selected actual inverse lift, the complete saved model error on its
physical strip, whole derivative bounds, original alpha, and the original
Gbar low/high inverse.  A dictionary of upper bounds alone is no admission.

API: zero, one, rational(n,d=1), lower, magnitude, sqrt, exp, power.
Values expose is_finite(), lower(), upper().  Every returned scalar is new
and unpersisted until its actual owner saves and reads the complete result.
"""

DIMENSION = 96
KIND = "R149_complete_density_inverse_regularization_and_Theta_rows_v1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite() and api.lower(value) >= 0,
            "one whole finite nonnegative directed upper bound")
    return value.upper()


def positive(api, value):
    require(value.is_finite() and api.lower(value) > 0,
            "a complete strictly positive lower endpoint")
    return api.lower(value)


def power_upper(api, value, numerator, denominator=1):
    require(numerator >= 0 and denominator > 0,
            "a monotone nonnegative real exponent")
    return upper(api, api.power(upper(api, value),
                                api.rational(numerator, denominator)))


def actual_third_derivative(api, whole_trial_third, full_lift_error, strip):
    """DB.5 with the complete analytic difference and the true fixed lifts."""
    h3 = upper(api, whole_trial_third)
    error = upper(api, full_lift_error)
    sigma = positive(api, strip)
    return upper(api, h3 + api.rational(6)*error/(sigma*sigma*sigma))


def complete_regularization(api, derivative_lower, second_upper, third_upper):
    """DB.8--18: both signs, all frequencies, same compatible inverses.

    No smallness gate and no finite-mode approximation enter these bounds.
    The H^-4/3 Bessel conversion includes its one true comparison factor.
    """
    m = positive(api, derivative_lower)
    m0 = m if m < api.one else api.one
    b2, b3 = upper(api, second_upper), upper(api, third_upper)
    off = upper(api, (b3/m0**3+api.rational(3)*b2*b2/m0**4)/api.rational(16))
    l0 = upper(api, api.rational(2,3)*off)
    l13 = upper(api, api.rational(9,4)*off)
    invm = upper(api, api.one/m)
    s0 = power_upper(api, invm, 1, 2)
    s1 = upper(api, power_upper(api, invm, 3, 2)
               +b2*power_upper(api, invm, 5, 2)/api.rational(4))
    s13 = upper(api, power_upper(api, s0, 2, 3)*power_upper(api, s1, 1, 3))
    embedding = power_upper(api, api.rational(1,4), 5, 6)
    kt0 = upper(api, s0*(api.one+l0/api.rational(2)))
    kt13 = upper(api, s13*(api.one+embedding*l13))
    bessel = power_upper(api, api.rational(17,16), 2, 3)
    return {
        "complete_opposite_density_coefficient_upper": off,
        "Ddag_energy_to_L2_upper": l0,
        "Ddag_energy_to_Hdot_one_third_upper": l13,
        "actual_forward_density_L2_upper": s0,
        "actual_forward_density_Hdot1_upper": s1,
        "actual_forward_density_Hdot_one_third_upper": s13,
        "adjoint_compression_inverse_L2_upper": kt0,
        "adjoint_compression_inverse_Hdot_one_third_upper": kt13,
        "compression_inverse_Hdot_minus1_upper": kt0,
        "compression_inverse_Hdot_minus_four_thirds_upper": kt13,
        "compression_inverse_Hminus_four_thirds_upper": upper(api, bessel*kt13),
        "same_selected_maps_and_true_distributional_inverses": True,
        "both_signs_and_complete_infinite_input_output_frequencies": True,
        "extra_smallness_or_finite_invertibility_gate_used": False,
        "physical_means_or_coupled_Schur_solved": False,
    }


def full_Theta_joint_error(api, residual_L2, residual_energy,
                          density_S0, Ddag_energy_L2, original_A0,
                          original_Gbar_L2_Hminus1,
                          alpha_trial_error, whole_G_trial_norm):
    """DB.21--25: entire Theta:L2->ell2, including its one-loss reference.

    Both residual norms refer to the SAME whole 96-column residual operator.
    The optional alpha error and full trial norm are explicit inputs even
    when one has proved them exactly zero.  No forward inverse is swapped.
    """
    e0, eh, s0, l0, a0, kg, ea, zg = [upper(api, v) for v in (
        residual_L2, residual_energy, density_S0, Ddag_energy_L2,
        original_A0, original_Gbar_L2_Hminus1,
        alpha_trial_error, whole_G_trial_norm)]
    ka = upper(api, api.one+a0/api.rational(4))
    ci = upper(api, api.sqrt(api.rational(17))/api.rational(4))
    ez = upper(api, s0*(e0+l0*eh))
    row = upper(api, ci*(ka*ez+ea*zg))
    return {
        "complete_joint_adjoint_solution_L2_error_upper": ez,
        "complete_joint_physical_dual_H1_row_error_upper": row,
        "complete_Theta_L2_joint_row_error_upper": upper(api, kg*row),
        "full_one_derivative_loss_paid_by_H1_Hminus1_duality": True,
        "full_true_alpha_action_or_explicit_trial_difference_included": True,
        "additional_sqrt96_after_joint_residual": False,
        "complete_incoming_Schur_inverse_proved": False,
    }


def full_Theta_norm(api, density_S0, Ddag_energy_L2, original_A0,
                    original_Gbar_L2_Hminus1):
    """DB.26 for the complete original 96 rows, no entrywise row sum."""
    s0, l0, a0, kg = [upper(api, v) for v in (
        density_S0, Ddag_energy_L2, original_A0, original_Gbar_L2_Hminus1)]
    ka = upper(api, api.one+a0/api.rational(4))
    ci = upper(api, api.sqrt(api.rational(17))/api.rational(4))
    nmax = api.rational(4*DIMENSION)
    return upper(api, kg*ci*ka*s0*(nmax+l0*api.sqrt(nmax)))


def analytic_primitive_derivative_L2_tail(api, strip, cutoff, primitive_sup):
    """DB.27, including both signs and physical frequency4.

    For cutoff0 this pays an entire analytic model difference.  The sup is
    on the whole physical strip, never a maximum over finitely many nodes.
    """
    require(type(cutoff) is int and cutoff >= 0, "an exact Fourier cutoff")
    sigma, mass = positive(api, strip), upper(api, primitive_sup)
    q = upper(api, api.exp(-api.rational(8)*sigma))
    require(q < api.one, "the entire exponential ratio is strictly below one")
    den = api.one-q
    positive(api, den)
    a = api.rational(cutoff+1)
    complete_sum = upper(api, q**(cutoff+1)*(
        a*a/den+api.rational(2)*a*q/(den*den)
        +q*(api.one+q)/(den*den*den)))
    squared = upper(api, api.rational(32)*mass*mass*complete_sum)
    return {"complete_squared_L2_tail_upper": squared,
            "complete_L2_tail_upper": upper(api, api.sqrt(squared))}


def complete_L2_residual(api, signed_head, cutoff, complete_tail, complete_model):
    """All exact residual head balls, disjoint evaluated tail, full model error."""
    require(type(cutoff) is int and cutoff >= 1
            and set(signed_head) == set(range(-cutoff,0)) | set(range(1,cutoff+1)),
            "every complete nonmean Fourier head coefficient with both signs")
    total = api.zero
    for k in sorted(signed_head):
        pair = signed_head[k]
        require(isinstance(pair,(tuple,list)) and len(pair) == 2
                and all(x.is_finite() for x in pair), "one whole signed complex ball")
        re, im = [api.magnitude(x) for x in pair]
        total += re*re+im*im
    tail, model = upper(api, complete_tail), upper(api, complete_model)
    evaluated = upper(api, api.sqrt(upper(api, total+tail*tail)))
    return {"complete_evaluated_L2_residual_upper": evaluated,
            "complete_true_L2_residual_upper": upper(api, evaluated+model),
            "both_signs_aliases_tail_and_true_map_error_included": True}
