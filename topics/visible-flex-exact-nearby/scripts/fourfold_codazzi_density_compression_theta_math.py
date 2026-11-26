"""DC.12--20: original same-sign density compression and finite Theta rows.

Pure directed formulas.  No IO, numerical import, or old scientific producer.
The owner must admit the whole WIT/WGB/WBP maps, same selected old one-leg
native, full W/R31/post48 receipts, and all actually used signed coefficients.
No scalar mapping grants that admission.  A Galerkin residual is NOT a full
residual.  Returned bounds are unpersisted until the owner saves/reads them.

API: zero, one, rational(n,d=1), lower, magnitude, sqrt, exp.  Values expose
is_finite(), lower(), upper().  Exact signs and balls stay in the caller's
directed backend.  Physical Fourier frequency is 4*k, never k.
"""

DIMENSION = 96
PHYSICAL_FREQUENCY = 4
INVERSE_LIFT_STRIP = '1/256'
KIND = 'R149_same_sign_density_compression_finite_Theta_formulas_v1'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def upper(api, value):
    require(value.is_finite() and api.lower(value) >= 0,
            'one complete finite nonnegative directed bound')
    return value.upper()


def positive(api, value):
    require(value.is_finite() and api.lower(value) > 0,
            'a proved strictly positive lower endpoint')
    return api.lower(value)


def sqrt_upper(api, value):
    return upper(api, api.sqrt(upper(api, value)))


def sum_squares_upper(api, values):
    require(values, 'a complete nonempty column list')
    values = [upper(api, value) for value in values]
    return upper(api, sum((x*x for x in values), api.zero))


def full_inverse_lift_error(api, EH, G1, Y, selected_delta,
                            post_transport, post_root):
    """DC.20 on the ORIGINAL physical strip1/256 and selected lift.

    The owner admits the original source identity making Y a positive
    complete one-leg majorant, the strip-image inclusion, and the full
    post48 two positive fees.  No old norm is divided or subtracted.
    """
    eh, g1, y, delta, et, er = [upper(api, x) for x in
                               (EH, G1, Y, selected_delta,
                                post_transport, post_root)]
    parameter = upper(api, g1*y*delta)
    return {
        'same_selected_inverse_lift_error_upper': upper(
            api, eh+parameter+et+er),
        'selected_one_leg_parameter_transfer_upper': parameter,
        'complete_old_transport_and_root_fee_upper': upper(api, et+er),
        'physical_strip': INVERSE_LIFT_STRIP,
        'phase_means_and_fixed_original_lifts_retained': True,
        'new_or_old_ray_ODE_called': False,
    }


def analytic_primitive_derivative_tail(api, strip, cutoff, sup_upper):
    """DC.16: Hdot^-1/2 norm of derivative of the ENTIRE |k|>K tail.

    sup_upper bounds the same complete periodic analytic primitive on the
    whole physical strip.  Both Fourier signs and frequency4 are included.
    cutoff0 also bounds a whole analytic primitive model difference.
    """
    require(type(cutoff) is int and cutoff >= 0,
            'the exact nonnegative Fourier tail cutoff')
    sigma, mass = positive(api, strip), upper(api, sup_upper)
    q = upper(api, api.exp(-api.rational(8)*sigma))
    require(q < api.one, 'the complete exponential ratio is below one')
    denominator = api.one-q
    positive(api, denominator)
    # Evaluate the exact monotone closed sum at an outward upper q.
    weighted_sum = upper(api, q**(cutoff+1)*(
        api.rational(cutoff+1)-api.rational(cutoff)*q)/(denominator*denominator))
    squared = upper(api, api.rational(8)*mass*mass*weighted_sum)
    return {'complete_squared_energy_tail_upper': squared,
            'complete_energy_tail_upper': sqrt_upper(api, squared)}


def complete_dft_alias(api, strip, samples, mode, primitive_sup_upper):
    """DC.17 for one exact sampled DFT coefficient, all alias images.

    A caller enumerating |k|<=K must also verify L>2K.  This function does
    not certify sample evaluation or use a sampled maximum as a sup norm.
    """
    require(type(samples) is int and samples > 0
            and type(mode) is int and 2*abs(mode) < samples,
            'an actual sampled Fourier coefficient below Nyquist')
    sigma = positive(api, strip)
    mass = upper(api, primitive_sup_upper)
    u = upper(api, api.exp(-api.rational(4)*sigma))
    require(u < api.one, 'the complete analytic Fourier decay ratio')
    denominator = api.one-u**samples
    positive(api, denominator)
    return upper(api, mass*(u**(samples-abs(mode))+u**(samples+abs(mode)))/denominator)


def complete_composition_model_error(api, strip, inverse_lift_error,
                                     full_input_image_sup_upper):
    """DC.18 then DC.16(K=0), including ALL derivative output frequencies.

    full_input_image_sup_upper bounds f, the derivative of the primitive
    If, on every complex segment connecting the two declared lift images.
    The owner proves that domain inclusion; no sampled derivative is used.
    """
    mass = upper(api, upper(api, inverse_lift_error)*
                 upper(api, full_input_image_sup_upper))
    result = analytic_primitive_derivative_tail(api, strip, 0, mass)
    return {'complete_primitive_composition_difference_upper': mass,
            'complete_density_composition_energy_error_upper':
                result['complete_energy_tail_upper']}


def complete_fourier_energy_residual(api, signed_head, cutoff,
                                     complete_outside_energy_upper,
                                     complete_model_energy_upper):
    """Full Hdot^-1/2 residual, never merely a Galerkin residual.

    signed_head maps EVERY -K..-1,1..K to (real_ball,imag_ball) for the same
    full residual's head.  These include all arithmetic/DFT alias errors.
    outside is the complete complementary Fourier tail of that evaluated
    object, while model is a separate FULL true-map error before projection.
    The owner proves the output mean is exactly zero, not approximately so.
    """
    require(type(cutoff) is int and cutoff >= 1
            and set(signed_head) == set(range(-cutoff, 0)) | set(range(1, cutoff+1)),
            'all declared residual head frequencies, including both signs')
    total = api.zero
    for k in sorted(signed_head):
        pair = signed_head[k]
        require(isinstance(pair, (tuple, list)) and len(pair) == 2
                and all(x.is_finite() for x in pair),
                'one complete signed complex Fourier coefficient ball')
        re, im = (api.magnitude(x) for x in pair)
        total += (re*re+im*im)/api.rational(PHYSICAL_FREQUENCY*abs(k))
    tail = upper(api, complete_outside_energy_upper)
    evaluated = sqrt_upper(api, upper(api, total+tail*tail))
    model = upper(api, complete_model_energy_upper)
    return {'complete_evaluated_energy_residual_upper': evaluated,
            'complete_true_energy_residual_upper': upper(api, evaluated+model),
            'full_infinite_frequency_tail_included': True}


def complete_VQ_row_error(api, full_residual_operator_upper, original_A0):
    """DC.12--13: original full96 VQ rows on L2, not full Theta on L2.

    full_residual_operator_upper is an independently certified WHOLE joint
    residual norm ell2_96->Hdot^-1/2.  If only column bounds are available,
    first use joint_residual_from_all_columns.  No extra sqrt96 is inserted.
    A0 belongs to the same complete alpha=v_i-w, not a fitted surrogate.
    """
    residual, a0 = upper(api, full_residual_operator_upper), upper(api, original_A0)
    ka0 = upper(api, api.one+a0/api.rational(4))
    return {'original_source_A_L2_upper': ka0,
            'complete_VQ_L2_operator_upper': upper(
                api, sqrt_upper(api, api.rational(DIMENSION))*ka0),
            'complete_VQ_L2_joint_row_error_upper': upper(
                api, ka0*residual/api.rational(2)),
            'whole_Theta_L2_row_certificate_proved': False,
            'all_physical_mean_phase_nu_Schur_rows_present': False}


def joint_residual_from_all_columns(api, full_residual_columns):
    require(len(full_residual_columns) == DIMENSION,
            'all96 complete true residual columns, never a prefix')
    return sqrt_upper(api, sum_squares_upper(api, full_residual_columns))


def complete_finite_Theta_error(api, VQ_error, VQ_norm,
                                trial_Gbar_F_L2_upper,
                                complete_Gbar_input_error_upper):
    """DC.14 for the specific finite input with a proved GbarF->L2 bound.

    Merely knowing F has finitely many columns is insufficient: every
    column's infinite Fourier tail and the one-loss Gbar must be paid.
    The output never grants a whole Theta:L2 certificate or a Schur gate.
    """
    e, v, f, df = [upper(api, x) for x in
                   (VQ_error, VQ_norm, trial_Gbar_F_L2_upper,
                    complete_Gbar_input_error_upper)]
    return {'complete_finite_Theta_pairing_error_upper': upper(api, e*f+v*df),
            'whole_Theta_L2_row_certificate_proved': False,
            'full_incoming_Schur_inverse_proved': False}
