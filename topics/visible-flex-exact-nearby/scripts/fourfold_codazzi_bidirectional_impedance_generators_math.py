"""WQS: two independent scalar-state generators of the WIC inverse.

No entry point, scientific imports, file access or old-producer calls.
Input is the complete prepared WIC mode in its actual weighted coordinates.
The algebra below is exactly the same Q_j, not a new approximate operator.
"""

def generators_from_mode(c):
    n = c["n"]
    zero, one, half = c["zero"], c["one"], c["half"]
    if c["is_positive_majorant"] is not False:
        raise ValueError("complete signed WIC mode required")
    H = [zero for _ in range(n + 1)]
    alpha = [zero for _ in range(n)]
    beta = [zero for _ in range(n)]
    forward_output = []
    backward_output = []
    local_output = []
    for i in range(n):
        tau = c["tau"][i]
        H[i + 1] = tau * tau * H[i] + c["sigma"][i]
        alpha[i] = c["sigma"][i] - tau * H[i] * c["lambda"][i]
        beta[i] = -c["varrho"][i] - tau * H[i] * c["mu"][i]
        K = one - c["p"][i] * H[i]
        Kn = one - c["p"][i + 1] * H[i + 1]
        backward_output.append([
            half * (K * tau + Kn),
            half * (H[i] * tau + H[i + 1])])
        forward_output.append([
            -half * (c["p"][i] + c["p"][i + 1] * tau),
            half * (one + tau)])
        local_output.append([
            [one - half * (K * c["lambda"][i] + c["p"][i + 1] * alpha[i]),
             -half * (K * c["mu"][i] + c["p"][i + 1] * beta[i])],
            [half * (alpha[i] - H[i] * c["lambda"][i]),
             one + half * (beta[i] - H[i] * c["mu"][i])]])
    return {
        "kind": "same_WIC_bidirectional_generators_v1",
        "n": n, "j": c["j"], "zero": zero, "one": one,
        "transition": list(c["tau"]),
        "forward_input": [[alpha[i], beta[i]] for i in range(n)],
        "backward_input": [[-c["lambda"][i], -c["mu"][i]] for i in range(n)],
        "forward_output": forward_output,
        "backward_output": backward_output,
        "local_output": local_output,
        "input_odd": list(c["input_odd"]),
        "input_even": list(c["input_even"]),
        "output_odd": list(c["output_odd"]),
        "output_even": list(c["output_even"]),
        "end_from_odd": one, "end_from_even": c["p_outer"],
        "outer_from_forward": c["theta"],
        "outer_from_backward_end": c["theta"] * H[n],
        "outer_direct_even": -c["theta"],
        "root_from_backward": one,
        "is_positive_majorant": False,
        "H": H,
    }


def _vectors(g, odd, even):
    n = g["n"]
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("positive complete cell count required")
    if len(odd) != n or len(even) != n:
        raise ValueError("both complete modal radial vectors required")
    return n


def apply_generators(g, f_odd, f_even, endpoint_odd, endpoint_even):
    n = _vectors(g, f_odd, f_even)
    zero = g["zero"]
    ro = [g["input_odd"][i] * f_odd[i] for i in range(n)]
    re = [g["input_even"][i] * f_even[i] for i in range(n)]
    backward = [zero for _ in range(n + 1)]
    backward[n] = g["end_from_odd"] * endpoint_odd + g["end_from_even"] * endpoint_even
    for i in range(n - 1, -1, -1):
        b = g["backward_input"][i]
        backward[i] = g["transition"][i] * backward[i + 1] + b[0] * ro[i] + b[1] * re[i]
    forward = [zero for _ in range(n + 1)]
    for i in range(n):
        a = g["forward_input"][i]
        forward[i + 1] = g["transition"][i] * forward[i] + a[0] * ro[i] + a[1] * re[i]
    out_odd = []
    out_even = []
    for i in range(n):
        F, G, D = g["forward_output"][i], g["backward_output"][i], g["local_output"][i]
        odd = F[0] * forward[i] + G[0] * backward[i + 1] + D[0][0] * ro[i] + D[0][1] * re[i]
        even = F[1] * forward[i] + G[1] * backward[i + 1] + D[1][0] * ro[i] + D[1][1] * re[i]
        out_odd.append(g["output_odd"][i] * odd)
        out_even.append(g["output_even"][i] * even)
    outer = (g["outer_from_forward"] * forward[n]
             + g["outer_from_backward_end"] * backward[n]
             + g["outer_direct_even"] * endpoint_even)
    return {"odd": out_odd, "even": out_even,
            "root_odd": g["root_from_backward"] * backward[0],
            "outer_weighted": outer}


def transpose_generators(g, u_odd, u_even, root_odd, outer_weighted):
    n = _vectors(g, u_odd, u_even)
    zero = g["zero"]
    ro = [zero for _ in range(n)]
    re = [zero for _ in range(n)]
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
        ro[i] += D[0][0] * odd + D[1][0] * even
        re[i] += D[0][1] * odd + D[1][1] * even
    for i in range(n - 1, -1, -1):
        value = forward[i + 1]
        forward[i] += g["transition"][i] * value
        a = g["forward_input"][i]
        ro[i] += a[0] * value
        re[i] += a[1] * value
    # forward[0] is the adjoint of a fixed zero, so is not a data coordinate.
    for i in range(n):
        value = backward[i]
        backward[i + 1] += g["transition"][i] * value
        b = g["backward_input"][i]
        ro[i] += b[0] * value
        re[i] += b[1] * value
    endpoint_odd = g["end_from_odd"] * backward[n]
    endpoint_even += g["end_from_even"] * backward[n]
    return {
        "odd": [g["input_odd"][i] * ro[i] for i in range(n)],
        "even": [g["input_even"][i] * re[i] for i in range(n)],
        "endpoint_odd": endpoint_odd, "endpoint_even": endpoint_even,
    }


def whole_positive_generator(g, absolute_upper):
    """Absolute values are taken after the complete signed local contractions."""
    result = {key: g[key] for key in ("n", "j", "zero", "one")}
    result.update({"kind": "same_WIC_whole_generator_majorant_v1",
                   "is_positive_majorant": True})

    def full(value):
        if isinstance(value, list):
            return [full(v) for v in value]
        return absolute_upper(value)

    for key in ("transition", "forward_input", "backward_input",
                "forward_output", "backward_output", "local_output",
                "input_odd", "input_even", "output_odd", "output_even",
                "end_from_odd", "end_from_even", "outer_from_forward",
                "outer_from_backward_end", "outer_direct_even",
                "root_from_backward"):
        result[key] = full(g[key])
    return result


def complete_generator_schur_sums(g, upper):
    if g["is_positive_majorant"] is not True:
        raise ValueError("one entire positive generator required")
    n, one = g["n"], g["one"]
    ones = [one for _ in range(n)]
    r = apply_generators(g, ones, ones, one, one)
    c = transpose_generators(g, ones, ones, one, one)
    rows = r["odd"] + r["even"] + [r["root_odd"], r["outer_weighted"]]
    cols = c["odd"] + c["even"] + [c["endpoint_odd"], c["endpoint_even"]]
    return {
        "complete_row_sum_upper": max(upper(v) for v in rows),
        "complete_column_sum_upper": max(upper(v) for v in cols),
        "complete_input_coordinates": 2 * n + 2,
        "complete_output_coordinates": 2 * n + 2,
        "matrix_allocations": 0,
    }


def complete_weighted_generator_schur_sums(
        g, input_weights, output_weights, positive_lower, upper):
    """Whole weighted Schur sums for the unchanged Hilbert-space operator.

    positive_lower returns a finite, strictly positive directed point lower.
    upper returns a finite directed point upper. All weights enclose one
    declared positive vector; they are comparison weights, not new coordinates.
    """
    if g["is_positive_majorant"] is not True:
        raise ValueError("one entire positive generator required")
    if set(input_weights) != {"odd", "even", "endpoint_odd", "endpoint_even"}:
        raise ValueError("all complete input comparison weights required")
    if set(output_weights) != {"odd", "even", "root_odd", "outer_weighted"}:
        raise ValueError("all complete output comparison weights required")
    n = _vectors(g, input_weights["odd"], input_weights["even"])
    _vectors(g, output_weights["odd"], output_weights["even"])

    def endpoints(weights):
        highs, lows = {}, {}
        for key, value in weights.items():
            if key in ("odd", "even"):
                lows[key] = [positive_lower(v) for v in value]
                highs[key] = [upper(v) for v in value]
            else:
                lows[key] = positive_lower(value)
                highs[key] = upper(value)
        return highs, lows

    vu, vl = endpoints(input_weights)
    wu, wl = endpoints(output_weights)
    r = apply_generators(g, vu["odd"], vu["even"],
                         vu["endpoint_odd"], vu["endpoint_even"])
    c = transpose_generators(g, wu["odd"], wu["even"],
                             wu["root_odd"], wu["outer_weighted"])
    row_values = r["odd"] + r["even"] + [r["root_odd"], r["outer_weighted"]]
    row_lowers = wl["odd"] + wl["even"] + [wl["root_odd"], wl["outer_weighted"]]
    col_values = c["odd"] + c["even"] + [c["endpoint_odd"], c["endpoint_even"]]
    col_lowers = vl["odd"] + vl["even"] + [vl["endpoint_odd"], vl["endpoint_even"]]
    rows = [upper(upper(value) / lower) for value, lower in zip(row_values, row_lowers)]
    cols = [upper(upper(value) / lower) for value, lower in zip(col_values, col_lowers)]
    return {
        "complete_weighted_row_ratio_upper": max(rows),
        "complete_weighted_column_ratio_upper": max(cols),
        "complete_input_coordinates": 2 * n + 2,
        "complete_output_coordinates": 2 * n + 2,
        "comparison_weights_do_not_change_actual_Hilbert_coordinates": True,
        "matrix_allocations": 0,
    }
