#!/usr/bin/env python3
"""R521: exact rational majorants for one declared finite Frenet reference.

This module forms conditional bounds from caller-supplied certified enclosures.
It does not read a checkpoint, evaluate a field/root/FFT, run a solver, certify
the supplied domain, create a workflow, or change an existing acceptance test.
All finite words must first be lifted to their exact rational values.  Pass no
float to this module.  Full arrays returned here are temporary internal data;
a caller's original necessary-readback and resource policies remain in force.
"""
from fractions import Fraction as Q
from math import comb, isqrt

SCHEMA = "R521-complete-finite-frenet-tube-majorants-v1"
PHYSICAL_LAYOUT = "r0..rM,t1..tM,z0..zM"


def rational(value):
    if isinstance(value, bool) or isinstance(value, float):
        raise TypeError("Use an exact rational lift, not bool or float")
    if isinstance(value, (Q, int, str)):
        return Q(value)
    raise TypeError("Expected Fraction, integer, or exact rational string")


def nonnegative(value, name):
    answer = rational(value)
    if answer < 0:
        raise ValueError(name + " must be nonnegative")
    return answer


def positive(value, name):
    answer = rational(value)
    if answer <= 0:
        raise ValueError(name + " must be positive")
    return answer


def power_two(exponent):
    return Q(1 << exponent) if exponent >= 0 else Q(1, 1 << -exponent)


def sqrt_bounds(value, bits):
    """Relative dyadic enclosure, including a positive lower endpoint for x>0."""
    x = nonnegative(value, "square-root argument")
    if isinstance(bits, bool) or not isinstance(bits, int) or bits < 1:
        raise ValueError("sqrt bits must be a positive integer")
    if x == 0:
        return Q(0), Q(0)
    exponent = x.numerator.bit_length() - x.denominator.bit_length()
    if x < power_two(exponent):
        exponent -= 1
    half_exponent = exponent // 2
    scaled = x / power_two(2 * half_exponent)
    numerator = isqrt((scaled.numerator << (2 * bits)) // scaled.denominator)
    scale = power_two(half_exponent - bits)
    lower = numerator * scale
    upper = lower if lower * lower == x else (numerator + 1) * scale
    # Since 1 <= scaled < 4, numerator >= 2**bits.  No absolute-grid
    # underflow can turn the proved positive endpoint into zero.
    if lower <= 0:
        raise ArithmeticError("Internal positive-square-root endpoint failure")
    return lower, upper


def norm_upper(components, bits):
    squared = sum((rational(x) ** 2 for x in components), Q(0))
    return sqrt_bounds(squared, bits)[1]


def jet_product(left, right):
    """Bounds for value, first derivative, and second derivative, not t^j jets."""
    a0, a1, a2 = left
    b0, b1, b2 = right
    return (a0 * b0,
            a1 * b0 + a0 * b1,
            a2 * b0 + 2 * a1 * b1 + a0 * b2)


def jet_power(value, exponent):
    result = (Q(1), Q(0), Q(0))
    for _ in range(exponent):
        result = jet_product(result, value)
    return result


def validate_modes(field_modes, angular_count):
    if isinstance(field_modes, bool) or not isinstance(field_modes, int) or field_modes < 1:
        raise ValueError("field_modes must be a positive integer")
    if isinstance(angular_count, bool) or not isinstance(angular_count, int):
        raise ValueError("angular_count must be an integer")
    if angular_count <= 4 * field_modes:
        raise ValueError("This exact uniform-DFT convention requires N > 4*M")
    return tuple(2 * j for j in range(1, field_modes + 1))


def fourier_synthesis_majorants(coefficient_abs_upper, field_modes, angular_count,
                                sqrt_bits):
    """Complete physical Fourier layout, with all means and frequencies 2..2M.

    The input bounds all coefficient vectors in the actual required tube.
    These are exact-trigonometric reference weights, not a claim about rounded
    FFT execution.  Literal-table references need their own actual row norms.
    """
    frequencies = validate_modes(field_modes, angular_count)
    size = 3 * field_modes + 2
    if len(coefficient_abs_upper) != size:
        raise ValueError("The complete physical 3*M+2 coefficient vector is required")
    bound = [nonnegative(x, "coefficient bound") for x in coefficient_abs_upper]
    m = field_modes
    r = bound[:m + 1]
    t = bound[m + 1:2 * m + 1]
    z = bound[2 * m + 1:]
    d_components = (
        sum((w * r[j] + t[j - 1] for j, w in enumerate(frequencies, 1)), Q(0)),
        r[0] + sum((w * t[j - 1] + r[j] for j, w in enumerate(frequencies, 1)), Q(0)),
        sum((w * z[j] for j, w in enumerate(frequencies, 1)), Q(0)),
    )
    e_components = (
        r[0] + sum(((w * w + 1) * r[j] + 2 * w * t[j - 1]
                    for j, w in enumerate(frequencies, 1)), Q(0)),
        sum(((w * w + 1) * t[j - 1] + 2 * w * r[j]
             for j, w in enumerate(frequencies, 1)), Q(0)),
        sum((w * w * z[j] for j, w in enumerate(frequencies, 1)), Q(0)),
    )
    first_sum = sum(frequencies)
    second_sum = sum(w * w for w in frequencies)
    d_unit = (Q(first_sum + m), Q(1 + first_sum + m), Q(first_sum))
    e_unit = (Q(1 + second_sum + m + 2 * first_sum),
              Q(second_sum + m + 2 * first_sum), Q(second_sum))
    return {
        "schema": SCHEMA + "-synthesis",
        "field_modes": m,
        "angular_count": angular_count,
        "physical_size": size,
        "physical_layout": PHYSICAL_LAYOUT,
        "frequencies": frequencies,
        "d_component_upper": d_components,
        "e_component_upper": e_components,
        "d_upper": norm_upper(d_components, sqrt_bits),
        "e_upper": norm_upper(e_components, sqrt_bits),
        "state_to_d_upper": norm_upper(d_unit, sqrt_bits),
        "state_to_e_upper": norm_upper(e_unit, sqrt_bits),
        "projection_nonmean_row_absolute_sum_upper": Q(2),
        "projection_mean_row_absolute_sum_upper": Q(1),
        "reference": "exact uniform-grid trigonometric synthesis and finite DFT",
        "runtime_only_coefficient_bounds": tuple(bound),
    }


def frenet_directional_majorants(domain, direction, sqrt_bits):
    """Uniform bounds for V and its first two affine-input derivatives.

    Domain must bound every required actual path, including all relevant angles.
    P_lower is a caller-certified lower bound for
        A*A*mu*mu*|d cross e|**2 - nu*nu*|d|**6.
    A smaller point-sample minimum is not such a lower bound.
    direction gives Euclidean d/e and absolute A/nu/mu affine-direction bounds.
    The selected sign of sqrt(P) is fixed along each path; either sign obeys
    the same nonnegative bounds.
    """
    al = positive(domain["A_lower"], "A_lower")
    au = positive(domain["A_upper"], "A_upper")
    ml = positive(domain["mu_lower"], "mu_lower")
    mu = positive(domain["mu_upper"], "mu_upper")
    if al > au or ml > mu:
        raise ValueError("Reversed scalar enclosure")
    nu = nonnegative(domain["nu_abs_upper"], "nu_abs_upper")
    d = nonnegative(domain["d_upper"], "d_upper")
    e = nonnegative(domain["e_upper"], "e_upper")
    p_lower = positive(domain["P_lower"], "P_lower")
    w_lower = nonnegative(domain.get("W_lower", 0), "W_lower")
    du = nonnegative(direction["d"], "direction.d")
    eu = nonnegative(direction["e"], "direction.e")
    av = nonnegative(direction["A"], "direction.A")
    nv = nonnegative(direction["nu"], "direction.nu")
    mv = nonnegative(direction["mu"], "direction.mu")
    q = (d * d, 2 * d * du, 2 * du * du)
    cross = (d * e, du * e + d * eu, 2 * du * eu)
    w = jet_product(cross, cross)
    # B = |d|^2 e - (d.e)d.  The value bound uses |B|^2=|d|^2 W.
    b = (d * d * e,
         4 * d * du * e + 2 * d * d * eu,
         4 * du * du * e + 8 * d * du * eu)
    a = (au, av, Q(0))
    speed = (mu, mv, Q(0))
    derivative = (nu, nv, Q(0))
    positive_term = jet_product(jet_product(jet_power(a, 2),
                                            jet_power(speed, 2)), w)
    subtracted_term = jet_product(jet_power(derivative, 2), jet_power(q, 3))
    p1 = positive_term[1] + subtracted_term[1]
    p2 = positive_term[2] + subtracted_term[2]
    root_lower = sqrt_bounds(p_lower, sqrt_bits)[0]
    # P <= A^2 mu^2 W, so this is a direct upper bound for sqrt(P).
    k0 = au * mu * cross[0]
    k1 = p1 / (2 * root_lower)
    k2 = p2 / (2 * root_lower) + p1 * p1 / (4 * root_lower ** 3)
    t = jet_product(derivative, jet_product(q, b))
    den = jet_product(a, w)
    # P <= A*mu^2*(A W), and also A W >= A_lower*W_lower.
    den_lower = max(al * w_lower, p_lower / (au * mu * mu))
    u1 = k1 * cross[0] + k0 * cross[1] + t[1]
    u2 = k2 * cross[0] + 2 * k1 * cross[1] + k0 * cross[2] + t[2]
    # Differentiate (A W)V=U; use the exact identity |V|=mu.
    v1 = (u1 + mu * den[1]) / den_lower
    v2 = (u2 + mu * den[2] + 2 * v1 * den[1]) / den_lower
    return {
        "schema": SCHEMA + "-affine-direction",
        "value_upper": mu,
        "first_upper": v1,
        "second_upper": v2,
        "P_first_upper": p1,
        "P_second_upper": p2,
        "sqrt_P_lower_used": root_lower,
        "AW_lower_used": den_lower,
        "AW_first_upper": den[1],
        "AW_second_upper": den[2],
        "direction": {"d": du, "e": eu, "A": av, "nu": nv, "mu": mv},
        "scope": "conditional on the complete supplied legal tube; no field evaluated",
    }


def finite_rhs_majorants(domain, synthesis, sqrt_bits):
    """Four blocks of complete coefficient-infinity Lipschitz constants.

    The output is for physical size 3*M+2; optional constant augmented RHS rows
    are zero, while their boundary/input influence is not discarded.
    """
    if synthesis.get("schema") != SCHEMA + "-synthesis":
        raise ValueError("Use the matching complete synthesis record")
    validate_modes(synthesis["field_modes"], synthesis["angular_count"])
    local = dict(domain)
    local["d_upper"] = synthesis["d_upper"]
    local["e_upper"] = synthesis["e_upper"]
    directions = {
        "y": {"d": synthesis["state_to_d_upper"], "e": synthesis["state_to_e_upper"],
              "A": Q(0), "nu": Q(0), "mu": Q(0)},
        "A": {"d": Q(0), "e": Q(0), "A": Q(1), "nu": Q(0), "mu": Q(0)},
        "nu": {"d": Q(0), "e": Q(0), "A": Q(0), "nu": Q(1), "mu": Q(0)},
        "mu": {"d": Q(0), "e": Q(0), "A": Q(0), "nu": Q(0), "mu": Q(1)},
    }
    rows = {name: frenet_directional_majorants(local, v, sqrt_bits)
            for name, v in directions.items()}
    projection = synthesis["projection_nonmean_row_absolute_sum_upper"]
    return {
        "schema": SCHEMA + "-finite-RHS",
        "field_modes": synthesis["field_modes"],
        "angular_count": synthesis["angular_count"],
        "physical_size": synthesis["physical_size"],
        "block_lipschitz": {name: projection * row["first_upper"]
                            for name, row in rows.items()},
        "state_second_direction_upper": projection * rows["y"]["second_upper"],
        "coefficient_value_upper": projection * rational(local["mu_upper"]),
        "mean_value_upper": rational(local["mu_upper"]),
        "local_direction_records": rows,
        "scope": "all reference DFT rows, including two means; no FFT-rounding claim",
    }


def cubic_power_bounds(local_power_rows, x0, x1, field_modes):
    """Exact Bernstein bounds for the actual four local power coefficient rows.

    C(x)=sum_j local_power_rows[j]*(x-x0)^j, j=0..3.
    Supply the exact lift of the actual saved coefficients, in this order.
    This does not substitute exact Hermite coefficients for rounded PPoly data.
    """
    left, right = rational(x0), rational(x1)
    h = positive(right - left, "cell length")
    if isinstance(field_modes, bool) or not isinstance(field_modes, int) or field_modes < 1:
        raise ValueError("field_modes must be a positive integer")
    size = 3 * field_modes + 2
    if len(local_power_rows) != 4 or any(len(row) != size for row in local_power_rows):
        raise ValueError("Require all four rows and all 3*M+2 physical components")
    power = [[rational(x) * h ** j for x in row]
             for j, row in enumerate(local_power_rows)]
    bernstein = [
        [sum((Q(comb(k, j), comb(3, j)) * power[j][column]
              for j in range(k + 1)), Q(0)) for column in range(size)]
        for k in range(4)
    ]
    d1 = [[3 * (bernstein[k + 1][j] - bernstein[k][j]) / h
           for j in range(size)] for k in range(3)]
    d2 = [[2 * (d1[k + 1][j] - d1[k][j]) / h
           for j in range(size)] for k in range(2)]
    value_abs = tuple(max(abs(row[j]) for row in bernstein) for j in range(size))
    first = max(abs(x) for row in d1 for x in row)
    second = max(abs(x) for row in d2 for x in row)
    return {
        "schema": SCHEMA + "-literal-cubic",
        "x0": left, "x1": right, "field_modes": field_modes, "physical_size": size,
        "coefficient_abs_upper": value_abs,
        "C_prime_upper": first,
        "C_second_upper": second,
        "runtime_only_bernstein_rows": tuple(tuple(row) for row in bernstein),
        "scope": "this literal local-power cubic, not an asserted exact ODE solution",
    }


def closed_cell_residual(majorants, cell, scalar_derivatives, samples):
    """Extend actual certified sample residuals to one complete closed cell.

    Each sample carries an original address and:
      x, literal_residual_norm_upper, formation_error_upper,
      state_gap_upper, A_gap_upper, nu_gap_upper, mu_gap_upper.
    Formation error includes both C' formation and RHS/norm formation for the
    declared nominal exact finite expression.  It cannot be defaulted to zero.
    Scalar gaps include numerical-shadow versus accurate-target differences.
    This function does not infer these inputs from an RMS tolerance or hashes.
    """
    if majorants.get("schema") != SCHEMA + "-finite-RHS":
        raise ValueError("Use the matching finite RHS record")
    if cell.get("schema") != SCHEMA + "-literal-cubic":
        raise ValueError("Use the matching literal cubic record")
    if majorants["field_modes"] != cell["field_modes"]:
        raise ValueError("The residual and all coefficient bounds must have the same M")
    x0, x1 = rational(cell["x0"]), rational(cell["x1"])
    if x1 <= x0:
        raise ValueError("A nonempty closed cell is required")
    block = {k: nonnegative(majorants["block_lipschitz"][k], "Lipschitz."+k)
             for k in ("y", "A", "nu", "mu")}
    c1 = nonnegative(cell["C_prime_upper"], "C_prime_upper")
    c2 = nonnegative(cell["C_second_upper"], "C_second_upper")
    radial = {k: nonnegative(scalar_derivatives[k], "scalar derivative."+k)
              for k in ("A", "nu", "mu")}
    residual_lipschitz = c2 + block["y"] * c1 + sum(
        (block[k] * radial[k] for k in ("A", "nu", "mu")), Q(0))
    recorded = []
    for index, sample in enumerate(samples):
        x = rational(sample["x"])
        if not x0 <= x <= x1:
            raise ValueError("Every sample must belong to this exact closed cell")
        residual = nonnegative(sample["literal_residual_norm_upper"], "literal residual")
        formation = nonnegative(sample["formation_error_upper"], "formation error")
        gaps = {
            "y": nonnegative(sample["state_gap_upper"], "state gap"),
            "A": nonnegative(sample["A_gap_upper"], "A gap"),
            "nu": nonnegative(sample["nu_gap_upper"], "nu gap"),
            "mu": nonnegative(sample["mu_gap_upper"], "mu gap"),
        }
        correction = formation + sum((block[k] * gaps[k] for k in block), Q(0))
        recorded.append({
            "original_index": index,
            "original_address": sample["original_address"],
            "x": x,
            "literal_residual_norm_upper": residual,
            "formation_error_upper": formation,
            "argument_gaps": gaps,
            "accurate_sample_residual_upper": residual + correction,
        })
    answer = {
        "schema": SCHEMA + "-closed-cell-residual",
        "x0": x0, "x1": x1,
        "residual_lipschitz_upper": residual_lipschitz,
        "sample_count": len(recorded),
        "runtime_only_sample_records": recorded,
        "available": bool(recorded),
        "scope": "conditional complete-cell bound, not a new solver acceptance gate",
    }
    if not recorded:
        answer.update(fill_distance=None, sample_max_upper=None, eta_C_upper=None,
                      unpaid_reason="no actual certified residual sample supplied")
        return answer
    ordered = sorted({row["x"] for row in recorded})
    fill = max([ordered[0] - x0, x1 - ordered[-1]]
               + [(b - a) / 2 for a, b in zip(ordered, ordered[1:])])
    sample_max = max(row["accurate_sample_residual_upper"] for row in recorded)
    answer.update(fill_distance=fill, sample_max_upper=sample_max,
                  eta_C_upper=sample_max + fill * residual_lipschitz,
                  unpaid_reason=None)
    return answer


def quintic_residual_transfer(eta_C_upper, E0_upper, E1_upper, state_lipschitz):
    """R514.16, only when the same actual scalar/state tube binds both curves."""
    eta = nonnegative(eta_C_upper, "eta_C")
    e0 = nonnegative(E0_upper, "E0")
    e1 = nonnegative(E1_upper, "E1")
    ky = nonnegative(state_lipschitz, "state Lipschitz")
    return eta + e1 + ky * e0


def scalar_necessary_summary(majorants, residual):
    """One selected scalar summary; original arrays/samples stay temporary."""
    if majorants.get("schema") != SCHEMA + "-finite-RHS":
        raise ValueError("Use the matching majorant schema")
    if residual.get("schema") != SCHEMA + "-closed-cell-residual":
        raise ValueError("Use the matching residual schema")
    def word(value):
        return None if value is None else str(rational(value))
    return {
        "schema": SCHEMA + "-necessary-scalars",
        "field_modes": majorants["field_modes"],
        "angular_count": majorants["angular_count"],
        "physical_size": majorants["physical_size"],
        "block_lipschitz": {key: word(value)
                            for key, value in majorants["block_lipschitz"].items()},
        "state_second_direction_upper": word(majorants["state_second_direction_upper"]),
        "cell": {"x0": word(residual["x0"]), "x1": word(residual["x1"])},
        "sample_count": residual["sample_count"],
        "fill_distance": word(residual["fill_distance"]),
        "sample_max_upper": word(residual["sample_max_upper"]),
        "residual_lipschitz_upper": word(residual["residual_lipschitz_upper"]),
        "eta_C_upper": word(residual["eta_C_upper"]),
        "available": residual["available"],
        "unpaid_reason": residual["unpaid_reason"],
        "scope": "exact rational conditional bounds; no actual domain/sample certification here",
    }
