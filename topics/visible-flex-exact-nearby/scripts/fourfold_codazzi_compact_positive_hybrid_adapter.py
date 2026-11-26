"""R144-PA: pure signed compact-minus-WVC-hybrid assembly.

This file performs no I/O and has no scientific runtime.  An Actions owner
supplies whole-cell balls, the unchanged signed collar module, and its
declared arithmetic API.  No model, Green, endpoint row, or weight is changed.
"""


def require(condition, message):
    if not condition:
        raise ValueError(message)


def complete_compact_positive_difference(
        api, collar, *, raw_ui, raw_v, repaired_ui, repaired_v,
        beta, curvature, gamma, mean_error, selected_mean_increment):
    """Build all signed difference terms on a whole positive cell.

    u=i*ui is the existing Laurent convention.  mean_error encloses M-m_raw
    (the proved uniform interval is [-2e-7,2e-7]); selected_mean_increment
    encloses delta*Z_mean relative to the REPAIRED mean at the same delta.
    They are function-value enclosures, not balls around positive budgets.
    The caller must retain the original whole-cell radial domain.
    """
    modes = set(range(-32, 33))
    require(all(set(poly) == modes for poly in
                (raw_ui, raw_v, repaired_ui, repaired_v)),
            "all original signed degree32 coefficients")
    require(api.upper(raw_v[0]) < 0, "nonzero negative raw moving mean")
    factor = api.one + mean_error / raw_v[0]
    compact_v = {j: factor * raw_v[j] for j in modes}
    error_u = {j: api.zero for j in range(-96, 97)}
    error_v = {j: api.zero for j in range(-96, 97)}
    for j in modes:
        error_u[j] = raw_ui[j] - repaired_ui[j]
        # Preserve cancellation before the norm or interval hull.
        error_v[j] = (raw_v[j] - repaired_v[j]
                      + mean_error * raw_v[j] / raw_v[0])
    # The lower difference assembly sets its own eta to exact zero.
    centre = collar._complete_centre_packet(
        repaired_ui, repaired_v, beta, curvature, gamma, api.zero, api.zero)
    lower = collar._complete_family_increment(centre, error_u, error_v, api.zero)
    delta_eta = -gamma * (
        mean_error + raw_v[0] - repaired_v[0] - selected_mean_increment)
    return {
        "lower": lower,
        "delta_eta": delta_eta,
        "K": curvature,
        "compact_ui": dict(raw_ui),
        "compact_v": compact_v,
        "degree": 32,
        "local_and_ordered_primitive_band": 64,
        "low_dimension": 193,
        "cross_shell": (97, 160),
        "moving_mean_retained": True,
        "model_or_fixed_weight_changed": False,
    }


def signed_difference_entry(api, collar, packet, output, input_, sqrt_two):
    """One complete physical entry: ordered lower terms plus true speed."""
    value = collar.family_signed_increment_entry(
        packet["lower"], output, input_, sqrt_two, api.zero)
    oc, k = output
    ic, j = input_
    if oc != ic and j == k and j:
        value += 4 * j * packet["delta_eta"] * (
            packet["K"] if oc == 0 else api.one)
    return value


def signed_difference_matrix(api, collar, packet, outputs, inputs, sqrt_two):
    """Complete requested rows/columns; no finite input is silently removed."""
    return [[signed_difference_entry(api, collar, packet, out, inp, sqrt_two)
             for inp in inputs] for out in outputs]


def positive_pointwise_fees(*, beta_upper, gamma_upper, K_upper,
                            state_error, angular_error, principal_mean_error):
    """PA.10--11 in an owner's exact or outward arithmetic.

    K_upper must be at least max(1,abs(K)).  All inputs are nonnegative
    whole-cell upper quantities.  Applying the fixed S or a source-frame
    norm belongs to its explicit receiver, not to this raw fee function.
    """
    b, g, k = beta_upper, gamma_upper, K_upper
    e0, e1, em = state_error, angular_error, principal_mean_error
    C = 14 * e0 + e0 * e0
    drift = b * k * C / 4
    lower = 3 * b * k * C + b * k * (6 * e0 + (7 + e0) * e1) / 2
    M1 = drift + g * k * em
    M0 = lower + g * k * e1
    return {
        "M0": M0,
        "M1": M1,
        "raw_LL": M0 + 384 * M1,
        "raw_HL": lower + 384 * drift,
        "raw_LH": lower + 640 * drift,
        "high_principal_update_bounded": False,
        "whole_positive_inverse_claimed": False,
    }


def two_body_gate_and_response(*, low_self, high_to_low, low_to_high,
                              high_self, low_source, high_source):
    """PA.19--20, only after all six inputs have their actual same units.

    Scalar comparisons and division must be certified by the caller's
    arithmetic; this function does not manufacture a high-self estimate.
    Endpoint/mean receivers remain independent outputs after this step.
    """
    ell, c, b, h = low_self, high_to_low, low_to_high, high_self
    require(0 <= ell < 1 and 0 <= h < 1 and c >= 0 and b >= 0,
            "complete nonnegative block bounds and both diagonal gates")
    det = (1 - ell) * (1 - h) - c * b
    require(det > 0, "complete coupled low/high body gate")
    require(low_source >= 0 and high_source >= 0,
            "independent source magnitudes")
    return (((1 - h) * low_source + c * high_source) / det,
            (b * low_source + (1 - ell) * high_source) / det)
