"""WPS: complete ordinary-source pairs in the weighted WIC coordinates.

No entry point, package import, file access, or scientific evaluation.
c is one signed WIC prepared mode; g is its signed WQS generator.
The caller admits both exact definitions, including their common mesh.
Moment0 and moment1 are orthonormal ordinary-dr source coefficients.
The input projection onto these two moments is a coisometry, not sampling.
"""

_SOURCE_KEYS = ("moment1_odd", "moment1_even", "moment0_odd", "moment0_even")


def prepare_source_generators(c, g, sqrt_h, sqrt_h_over_sqrt12):
    n = c["n"]
    if (type(n) is not int or n <= 0 or g["n"] != n or c["j"] != g["j"]
            or c["is_positive_majorant"] is not False
            or g["is_positive_majorant"] is not False
            or len(sqrt_h) != n or len(sqrt_h_over_sqrt12) != n):
        raise ValueError("same complete signed mode and two source moment weights required")
    one, half = c["one"], c["half"]
    backward_input, forward_input, local_output = [], [], []
    for i in range(n):
        den, pn, tau = c["denominators"][i], c["p"][i + 1], c["tau"][i]
        invden = one / den
        b = half * c["sigma"][i] * den
        co = invden + half * pn * c["sigma"][i]
        ce = pn * invden + half * c["mu"][i] / (one + b * pn)
        H = g["H"][i]
        K = one - c["p"][i] * H
        ao = -half * c["sigma"][i] - tau * H * co
        ae = invden - tau * H * ce
        backward_input.append([
            -c["lambda"][i], -c["mu"][i], -co, -ce])
        forward_input.append([
            g["forward_input"][i][0], g["forward_input"][i][1], ao, ae])
        old = g["local_output"][i]
        local_output.append([
            [old[0][0], old[0][1],
             -half * (K * co + pn * ao),
             -half * (K * ce + pn * ae)],
            [old[1][0], old[1][1],
             half * (ao - H * co),
             half * (ae - H * ce)]])
    return {
        "kind": "complete_WIC_ordinary_source_pair_generators_v1",
        "n": n, "j": c["j"], "zero": c["zero"], "one": one,
        "transition": list(g["transition"]),
        "forward_input": forward_input,
        "backward_input": backward_input,
        "forward_output": [list(v) for v in g["forward_output"]],
        "backward_output": [list(v) for v in g["backward_output"]],
        "local_output": local_output,
        "input_weights": [
            [sqrt_h_over_sqrt12[i], sqrt_h_over_sqrt12[i],
             sqrt_h[i], sqrt_h[i]] for i in range(n)],
        "output_odd": list(g["output_odd"]),
        "output_even": list(g["output_even"]),
        "end_from_odd": g["end_from_odd"],
        "end_from_even": g["end_from_even"],
        "outer_from_forward": g["outer_from_forward"],
        "outer_from_backward_end": g["outer_from_backward_end"],
        "outer_direct_even": g["outer_direct_even"],
        "root_from_backward": g["root_from_backward"],
        "is_positive_majorant": False,
        "source_coordinate_order": list(_SOURCE_KEYS),
        "source_moments_are_orthonormal_ordinary_dr": True,
        "endpoint_integral_already_absorbed": True,
    }


def _source_vectors(g, values):
    n = g["n"]
    if (type(n) is not int or n <= 0 or set(values) != set(_SOURCE_KEYS)
            or any(len(values[key]) != n for key in _SOURCE_KEYS)):
        raise ValueError("four complete source moment vectors required")
    return n


def apply_source_generators(g, source, endpoint_odd, endpoint_even):
    n = _source_vectors(g, source)
    zero = g["zero"]
    inputs = [[g["input_weights"][i][k] * source[key][i]
               for k, key in enumerate(_SOURCE_KEYS)] for i in range(n)]
    backward = [zero for _ in range(n + 1)]
    backward[n] = (g["end_from_odd"] * endpoint_odd
                   + g["end_from_even"] * endpoint_even)
    for i in range(n - 1, -1, -1):
        value = g["transition"][i] * backward[i + 1]
        for k in range(4):
            value += g["backward_input"][i][k] * inputs[i][k]
        backward[i] = value
    forward = [zero for _ in range(n + 1)]
    for i in range(n):
        value = g["transition"][i] * forward[i]
        for k in range(4):
            value += g["forward_input"][i][k] * inputs[i][k]
        forward[i + 1] = value
    out_odd, out_even = [], []
    for i in range(n):
        F, G, D = g["forward_output"][i], g["backward_output"][i], g["local_output"][i]
        odd = F[0] * forward[i] + G[0] * backward[i + 1]
        even = F[1] * forward[i] + G[1] * backward[i + 1]
        for k in range(4):
            odd += D[0][k] * inputs[i][k]
            even += D[1][k] * inputs[i][k]
        out_odd.append(g["output_odd"][i] * odd)
        out_even.append(g["output_even"][i] * even)
    outer = (g["outer_from_forward"] * forward[n]
             + g["outer_from_backward_end"] * backward[n]
             + g["outer_direct_even"] * endpoint_even)
    return {"odd": out_odd, "even": out_even,
            "root_odd": g["root_from_backward"] * backward[0],
            "outer_weighted": outer}


def transpose_source_generators(g, u_odd, u_even, root_odd, outer_weighted):
    n, zero = g["n"], g["zero"]
    if type(n) is not int or n <= 0 or len(u_odd) != n or len(u_even) != n:
        raise ValueError("complete modal output vectors required")
    inputs = [[zero for _ in range(4)] for _ in range(n)]
    forward = [zero for _ in range(n + 1)]
    backward = [zero for _ in range(n + 1)]
    forward[n] += g["outer_from_forward"] * outer_weighted
    backward[n] += g["outer_from_backward_end"] * outer_weighted
    endpoint_even = g["outer_direct_even"] * outer_weighted
    backward[0] += g["root_from_backward"] * root_odd
    for i in range(n):
        odd = g["output_odd"][i] * u_odd[i]
        even = g["output_even"][i] * u_even[i]
        F, G, D = g["forward_output"][i], g["backward_output"][i], g["local_output"][i]
        forward[i] += F[0] * odd + F[1] * even
        backward[i + 1] += G[0] * odd + G[1] * even
        for k in range(4):
            inputs[i][k] += D[0][k] * odd + D[1][k] * even
    for i in range(n - 1, -1, -1):
        value = forward[i + 1]
        forward[i] += g["transition"][i] * value
        for k in range(4):
            inputs[i][k] += g["forward_input"][i][k] * value
    # forward[0] is the adjoint of a fixed zero, not an input.
    for i in range(n):
        value = backward[i]
        backward[i + 1] += g["transition"][i] * value
        for k in range(4):
            inputs[i][k] += g["backward_input"][i][k] * value
    result = {
        key: [g["input_weights"][i][k] * inputs[i][k] for i in range(n)]
        for k, key in enumerate(_SOURCE_KEYS)}
    result["endpoint_odd"] = g["end_from_odd"] * backward[n]
    result["endpoint_even"] = endpoint_even + g["end_from_even"] * backward[n]
    return result


def whole_positive_source_generators(g, absolute_upper):
    """Form a majorant only after each complete signed local contraction."""
    if g["is_positive_majorant"] is not False:
        raise ValueError("complete signed source pair required")
    result = {key: g[key] for key in (
        "n", "j", "zero", "one", "source_coordinate_order",
        "source_moments_are_orthonormal_ordinary_dr",
        "endpoint_integral_already_absorbed")}
    result.update({"kind": "complete_ordinary_source_pair_majorant_v1",
                   "is_positive_majorant": True})

    def absolute(value):
        if isinstance(value, list):
            return [absolute(v) for v in value]
        return absolute_upper(value)

    for key in ("transition", "forward_input", "backward_input",
                "forward_output", "backward_output", "local_output",
                "input_weights", "output_odd", "output_even",
                "end_from_odd", "end_from_even", "outer_from_forward",
                "outer_from_backward_end", "outer_direct_even",
                "root_from_backward"):
        result[key] = absolute(g[key])
    return result


def complete_weighted_source_schur_sums(
        g, source_weights, output_weights, positive_lower, upper):
    """The ordinary-source column only: independent endpoint data are zero.

    The source moment map is a coisometry onto all 4*n coordinates.
    Endpoint adjoints remain in transpose_source_generators, but are not
    coordinates of this specifically declared source-only norm.
    """
    if g["is_positive_majorant"] is not True:
        raise ValueError("one complete positive source generator required")
    n = _source_vectors(g, source_weights)
    if (set(output_weights) != {"odd", "even", "root_odd", "outer_weighted"}
            or len(output_weights["odd"]) != n or len(output_weights["even"]) != n):
        raise ValueError("complete positive output comparison weights required")
    vl = {key: [positive_lower(v) for v in source_weights[key]] for key in _SOURCE_KEYS}
    vu = {key: [upper(v) for v in source_weights[key]] for key in _SOURCE_KEYS}
    wl, wu = {}, {}
    for key, values in output_weights.items():
        if key in ("odd", "even"):
            wl[key] = [positive_lower(v) for v in values]
            wu[key] = [upper(v) for v in values]
        else:
            wl[key] = positive_lower(values)
            wu[key] = upper(values)
    rows = apply_source_generators(g, vu, g["zero"], g["zero"])
    cols = transpose_source_generators(
        g, wu["odd"], wu["even"], wu["root_odd"], wu["outer_weighted"])
    row_values = rows["odd"] + rows["even"] + [rows["root_odd"], rows["outer_weighted"]]
    row_lowers = wl["odd"] + wl["even"] + [wl["root_odd"], wl["outer_weighted"]]
    row_bounds = [upper(upper(v) / lo) for v, lo in zip(row_values, row_lowers)]
    col_bounds = [
        upper(upper(cols[key][i]) / vl[key][i])
        for key in _SOURCE_KEYS for i in range(n)]
    return {
        "complete_source_row_ratio_upper": max(row_bounds),
        "complete_source_column_ratio_upper": max(col_bounds),
        "complete_source_moment_coordinates": 4 * n,
        "complete_output_coordinates": 2 * n + 2,
        "independent_endpoint_data_zero_only_in_this_source_column": True,
        "matrix_allocations": 0,
    }


def source_mean_action(sqrt_h, sqrt_h_over_sqrt12, sqrt_h_s,
                       moment0, moment1, endpoint_mean, zero, half):
    n = len(sqrt_h)
    if (n <= 0 or any(len(v) != n for v in (
            sqrt_h_over_sqrt12, sqrt_h_s, moment0, moment1))):
        raise ValueError("complete mean source and cell weights required")
    G = [sqrt_h[i] * moment0[i] for i in range(n)]
    r = [sqrt_h_over_sqrt12[i] * moment1[i] for i in range(n)]
    suffix = zero
    result = [zero for _ in range(n)]
    for i in range(n - 1, -1, -1):
        result[i] = sqrt_h_s[i] * (endpoint_mean - suffix - half * G[i] + r[i])
        suffix += G[i]
    return {"body_mean": result, "root_mean": endpoint_mean - suffix}


def source_mean_transpose(sqrt_h, sqrt_h_over_sqrt12, sqrt_h_s,
                         body_mean, root_mean, zero, half):
    n = len(sqrt_h)
    if (n <= 0 or any(len(v) != n for v in (
            sqrt_h_over_sqrt12, sqrt_h_s, body_mean))):
        raise ValueError("complete mean output and cell weights required")
    t = [sqrt_h_s[i] * body_mean[i] for i in range(n)]
    prefix, endpoint = zero, root_mean
    moment0, moment1 = [], []
    for i in range(n):
        moment0.append(sqrt_h[i] * (-root_mean - prefix - half * t[i]))
        moment1.append(sqrt_h_over_sqrt12[i] * t[i])
        prefix += t[i]
        endpoint += t[i]
    return {"moment0": moment0, "moment1": moment1, "endpoint_mean": endpoint}
