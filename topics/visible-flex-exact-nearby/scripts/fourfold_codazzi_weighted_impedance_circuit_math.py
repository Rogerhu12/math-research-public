"""WIC: weighted modal impedance trial, with an exact reverse circuit.

No entry point, numerical package import, file access, or old-producer call.
This is a finite operator recipe, not a certificate for the actual Schur matrix.
All scientific evaluation belongs to a separately frozen Actions consumer.

The scalar backend must enclose the exact expressions below. It must admit
positive h, sqrt_h, coordinate_q, reference_q, rho and p_outer, eta >= 0,
theta > 0, and sqrt_h**2 == h as an exact input identity. Reference rational
expressions may be evaluated as an expression DAG; expanding large Fraction
numerators is unnecessary. Cell and outer Hilbert weights remain separate.
"""

def _lengths(n, *vectors):
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("positive integer cell count required")
    if any(len(v) != n for v in vectors):
        raise ValueError("complete common cell partition required")


def prepare_mode(j, h, eta, reference_q, coordinate_q, sqrt_h, rho,
                 theta, p_outer, zero, one):
    """Prepare the unique exact modal circuit, to be evaluated outward.

    The nonzero mode is (sqrt(2) sin(4j phi), sqrt(2) cos(4j phi)).
    coordinate_q is the actual S_i even scaling. reference_q belongs only
    to D_i=4j eta_i [[0, reference_q_i**2], [1, 0]]. No transformed endpoint
    continuity is imposed. rho_i is the separately declared positive
    finite diagonal; rho=1 and rho=1+h*4j*eta*q/2 are distinct whole trials.
    """
    if isinstance(j, bool) or not isinstance(j, int) or not 1 <= j <= 96:
        raise ValueError("one genuine nonzero head mode 1..96 required")
    n = len(h)
    _lengths(n, h, eta, reference_q, coordinate_q, sqrt_h, rho)
    two = one + one
    half = one / two
    p = [zero for _ in range(n + 1)]
    p[n] = p_outer
    tau = [zero for _ in range(n)]
    lam = [zero for _ in range(n)]
    mu = [zero for _ in range(n)]
    sigma = [zero for _ in range(n)]
    varrho = [zero for _ in range(n)]
    denominators = [zero for _ in range(n)]
    for i in range(n - 1, -1, -1):
        b = h[i] * (4 * j) * eta[i] / (two * rho[i])
        a = b * reference_q[i] * reference_q[i]
        pn = p[i + 1]
        den = one + two * b * pn + a * b
        denominators[i] = den
        p[i] = ((one + a * b) * pn + two * a) / den
        tau[i] = (one - a * b) / den
        lam[i] = two * b * (pn + a) / den
        mu[i] = two * a * (one + b * pn) / den
        sigma[i] = two * b / den
        varrho[i] = two * a * b / den
    return {
        "kind": "weighted_modal_impedance_circuit_v1",
        "j": j, "n": n, "zero": zero, "one": one, "half": half,
        "p": p, "tau": tau, "lambda": lam, "mu": mu,
        "sigma": sigma, "varrho": varrho, "denominators": denominators,
        "input_odd": [one / sqrt_h[i] for i in range(n)],
        "input_even": [one / (sqrt_h[i] * coordinate_q[i]) for i in range(n)],
        "output_odd": [sqrt_h[i] / rho[i] for i in range(n)],
        "output_even": [sqrt_h[i] * coordinate_q[i] / rho[i] for i in range(n)],
        "theta": theta, "p_outer": p_outer,
        "is_positive_majorant": False,
    }


def apply_mode(c, f_odd, f_even, g_odd, g_even):
    """Apply Q_j in the actual orthonormal input/output coordinates.

    Input endpoint rows are raw L2 odd/even coordinates. Output is
    (cell odd/even coefficients, root odd d_j, H^(-5/6) outer b_hat_j).
    The prescribed root even c_j is NOT an additional input of Q_j.
    """
    n, zero, half = c["n"], c["zero"], c["half"]
    _lengths(n, f_odd, f_even)
    positive = c["is_positive_majorant"]
    r_odd = [c["input_odd"][i] * f_odd[i] for i in range(n)]
    r_even = [c["input_even"][i] * f_even[i] for i in range(n)]
    g = [zero for _ in range(n + 1)]
    g[n] = g_odd + c["p_outer"] * g_even
    for i in range(n - 1, -1, -1):
        forcing = c["lambda"][i] * r_odd[i] + c["mu"][i] * r_even[i]
        g[i] = c["tau"][i] * g[i + 1] + forcing if positive else (
            c["tau"][i] * g[i + 1] - forcing)
    zeta = [zero for _ in range(n + 1)]
    for i in range(n):
        value = c["tau"][i] * zeta[i] + c["sigma"][i] * (g[i + 1] + r_odd[i])
        correction = c["varrho"][i] * r_even[i]
        zeta[i + 1] = value + correction if positive else value - correction
    xi = [
        g[i] + c["p"][i] * zeta[i] if positive else g[i] - c["p"][i] * zeta[i]
        for i in range(n + 1)
    ]
    u_odd = [
        c["output_odd"][i] * (half * (xi[i] + xi[i + 1]) + r_odd[i])
        for i in range(n)
    ]
    u_even = [
        c["output_even"][i] * (half * (zeta[i] + zeta[i + 1]) + r_even[i])
        for i in range(n)
    ]
    outer = c["theta"] * (zeta[n] + g_even if positive else zeta[n] - g_even)
    return {"odd": u_odd, "even": u_even, "root_odd": xi[0], "outer_weighted": outer}


def transpose_mode(c, u_odd, u_even, root_odd, outer_weighted):
    """Exact transpose of apply_mode in the SAME Hilbert coordinates.

    This reverses every edge, including cell sqrt(h), S_i, theta_j and both
    direct boundary paths. It is also the transpose of the positive
    majorant circuit when is_positive_majorant is True.
    """
    n, zero, half = c["n"], c["zero"], c["half"]
    _lengths(n, u_odd, u_even)
    positive = c["is_positive_majorant"]
    r_odd_bar = [zero for _ in range(n)]
    r_even_bar = [zero for _ in range(n)]
    xi_bar = [zero for _ in range(n + 1)]
    zeta_bar = [zero for _ in range(n + 1)]
    g_bar = [zero for _ in range(n + 1)]
    for i in range(n):
        odd = c["output_odd"][i] * u_odd[i]
        even = c["output_even"][i] * u_even[i]
        r_odd_bar[i] += odd
        r_even_bar[i] += even
        xi_bar[i] += half * odd
        xi_bar[i + 1] += half * odd
        zeta_bar[i] += half * even
        zeta_bar[i + 1] += half * even
    xi_bar[0] += root_odd
    outer = c["theta"] * outer_weighted
    zeta_bar[n] += outer
    g_even_bar = outer if positive else -outer
    for i in range(n + 1):
        g_bar[i] += xi_bar[i]
        value = c["p"][i] * xi_bar[i]
        zeta_bar[i] = zeta_bar[i] + value if positive else zeta_bar[i] - value
    for i in range(n - 1, -1, -1):
        value = zeta_bar[i + 1]
        zeta_bar[i] += c["tau"][i] * value
        g_bar[i + 1] += c["sigma"][i] * value
        r_odd_bar[i] += c["sigma"][i] * value
        correction = c["varrho"][i] * value
        r_even_bar[i] = r_even_bar[i] + correction if positive else r_even_bar[i] - correction
    # zeta_0 is a fixed zero; its adjoint is not an input coordinate.
    for i in range(n):
        value = g_bar[i]
        g_bar[i + 1] += c["tau"][i] * value
        odd = c["lambda"][i] * value
        even = c["mu"][i] * value
        r_odd_bar[i] = r_odd_bar[i] + odd if positive else r_odd_bar[i] - odd
        r_even_bar[i] = r_even_bar[i] + even if positive else r_even_bar[i] - even
    g_odd_bar = g_bar[n]
    g_even_bar += c["p_outer"] * g_bar[n]
    return {
        "odd": [c["input_odd"][i] * r_odd_bar[i] for i in range(n)],
        "even": [c["input_even"][i] * r_even_bar[i] for i in range(n)],
        "endpoint_odd": g_odd_bar, "endpoint_even": g_even_bar,
    }


def positive_majorant(c, positive_upper, absolute_upper):
    """One fixed positive circuit dominating every signed matrix entry.

    The callbacks return exact nonnegative directed upper endpoints.
    An interval object must never be selected by max before taking its upper.
    This does not change the signed trial Q; it only defines its norm majorant.
    """
    result = {
        "kind": "positive_modal_impedance_majorant_v1",
        "j": c["j"], "n": c["n"], "zero": c["zero"],
        "one": c["one"], "half": c["half"],
        "is_positive_majorant": True,
        "theta": positive_upper(c["theta"]),
        "p_outer": positive_upper(c["p_outer"]),
    }
    for name in ("p", "lambda", "mu", "sigma", "varrho",
                 "input_odd", "input_even", "output_odd", "output_even"):
        result[name] = [positive_upper(value) for value in c[name]]
    result["tau"] = [absolute_upper(value) for value in c["tau"]]
    return result


def complete_modal_schur_sums(majorant, upper):
    """Complete row/column sums in O(N), without a finite matrix.

    Return the two whole positive sums. A consumer may save them and then
    save sqrt(row_sum_upper * column_sum_upper); no columns are omitted.
    """
    if majorant["is_positive_majorant"] is not True:
        raise ValueError("one full positive circuit required")
    n, one = majorant["n"], majorant["one"]
    ones = [one for _ in range(n)]
    rows = apply_mode(majorant, ones, ones, one, one)
    cols = transpose_mode(majorant, ones, ones, one, one)
    row_values = rows["odd"] + rows["even"] + [rows["root_odd"], rows["outer_weighted"]]
    col_values = cols["odd"] + cols["even"] + [cols["endpoint_odd"], cols["endpoint_even"]]
    return {
        "complete_row_sum_upper": max(upper(value) for value in row_values),
        "complete_column_sum_upper": max(upper(value) for value in col_values),
        "complete_input_coordinates": 2 * n + 2,
        "complete_output_coordinates": 2 * n + 2,
        "matrix_allocations": 0,
    }


def mean_action(weights, body, endpoint_mean):
    """Physical mean: weights_i=sqrt(h_i)*coordinate_q_i; no sqrt(2)."""
    _lengths(len(weights), body)
    return {
        "body": [body[i] + weights[i] * endpoint_mean for i in range(len(weights))],
        "root_mean": endpoint_mean,
    }


def mean_transpose(weights, body, root_mean):
    _lengths(len(weights), body)
    value = root_mean
    for i in range(len(weights)):
        value += weights[i] * body[i]
    return {"body": list(body), "endpoint_mean": value}


def complete_mean_norm(weights, zero, one, sqrt):
    """Exact norm formula for [[Id,w],[0,1]], evaluated outward by caller."""
    squared = zero
    for value in weights:
        squared += value * value
    two = one + one
    return (sqrt(two * two + squared) + sqrt(squared)) / two


def inherited_rho_linear(j, h, eta, reference_q, one):
    """rho_0(x)=1+x/2; nonzero eigenvalue magnitude is 4j eta q."""
    _lengths(len(h), eta, reference_q)
    two = one + one
    return [one + h[i] * (4 * j) * eta[i] * reference_q[i] / two
            for i in range(len(h))]


def inherited_rho_quadratic(j, h, eta, reference_q, one):
    """Frozen WIC primary: rho_2(x)=1+x*x/12, with error <= x**4/720.

    The exact principal Schur normalizer is rho_*(x)=(x/2)coth(x/2).
    This function evaluates only the rational reference. The inequality
    is a theorem; any numerical error record for it is a separate new target.
    """
    if isinstance(j, bool) or not isinstance(j, int) or not 1 <= j <= 96:
        raise ValueError("one genuine nonzero head mode 1..96 required")
    _lengths(len(h), eta, reference_q)
    twelve = 12 * one
    values = []
    for i in range(len(h)):
        x = h[i] * (4 * j) * eta[i] * reference_q[i]
        values.append(one + x * x / twelve)
    return values
