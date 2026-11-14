"""R48 positive-moment height construction and its R44 defect interface.

This module defines one continuous candidate using the five *true*
background integrals.  Supplied Arb boxes must enclose those same
integrals; they do not define independently selected pointwise data.
No source integration, radial flow or saved-state evaluation is started.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction

from flint import acb, arb
from closure_real_head_source_enclosure import ball_record
from tail_r41_connection_polynomial import real, norm
from tail_outer_compatible_mean_defect import _certify_same_height_fields


MOMENT_KEYS = ("00", "10", "01", "11", "b")


def intersection(a, b):
    a, b = real(a), real(b)
    lo, hi = max(a.lower(), b.lower()), min(a.upper(), b.upper())
    if not lo <= hi:
        raise ArithmeticError("Two enclosures of the same true quantity are disjoint")
    return lo.union(hi)


def positive_basis(u):
    """The fourth basis is -q11; all five are nonnegative on [0,1]."""
    u = real(u)
    return {
        "00": (1-u)**2*(1+2*u),
        "10": u*(1-u)**2,
        "01": u*u*(3-2*u),
        "11": u*u*(1-u),
        "b": u*u*(1-u)**2,
    }


def signed_basis_derivative(u):
    """Derivatives of q00,q10,q01,q11,b in that order."""
    u = real(u)
    return (-6*u*(1-u), (1-u)*(1-3*u),
            6*u*(1-u), -u*(2-3*u), 2*u*(1-u)*(1-2*u))


def cell_source_coordinate(segment_lengths, segment, x):
    """Unwarped source length, normalized once over the entire true cell.

Original segment coordinates are not concatenated as j+x: their unequal
source lengths must be retained in both u and du/dx.
"""
    if len(segment_lengths) != 9 or not 0 <= segment < 9:
        raise ValueError("A complete original nine-segment source cell is required")
    lengths = [real(v) for v in segment_lengths]
    if not all(v > 0 for v in lengths):
        raise ValueError("Every true source length must be positive")
    total = sum(lengths, arb(0))
    x = real(x)
    # These are exact identities of the same true lengths.  Dividing two
    # copies of an interval for total would otherwise manufacture endpoint
    # width, even though the actual coordinate is exactly one.
    u = (arb(0) if segment == 0 and x == 0 else
         arb(1) if segment == 8 and x == 1 else
         (sum(lengths[:segment], arb(0))+lengths[segment]*x)/total)
    return u, lengths[segment]/total


def normalized_endpoint_jet(height, slope, second, *, w, radius_u, log_w_u):
    """Convert physical-r nonmean jets to H,K,K_u using the same background."""
    w, radius_u, log_w_u = map(real, (w, radius_u, log_w_u))
    if not w > 0 or not radius_u > 0:
        raise ValueError("The true endpoint w and r_u must be positive")
    modes = set(height)
    if set(slope) != modes or set(second) != modes:
        raise ValueError("All endpoint physical jets must retain the same spectrum")
    K = {m: real(slope[m])/w for m in modes}
    Ku = {m: radius_u*real(second[m])/w-log_w_u*K[m] for m in modes}
    return dict(H={m: real(height[m]) for m in modes}, K=K, Ku=Ku)


def _check_moments(values, *, strict):
    if set(values) != set(MOMENT_KEYS):
        raise ValueError("All five positive R48 moments are required")
    result = {key: real(values[key]) for key in MOMENT_KEYS}
    for value in result.values():
        if (strict and not value > 0) or (not strict and not value >= 0):
            raise ValueError("A required true positive-moment lower bound failed")
    return result


def make_weighted_candidate(left, right, total_moments):
    """Define the exact R48 candidate; boxes only enclose its fixed constants.

left/right each have H,K,Ku positive-even cosine coefficient dictionaries.
The mathematical total_moments are the same five integrals of r_u*w
throughout every later evaluation, not five independent rounded choices.
"""
    I = _check_moments(total_moments, strict=True)
    modes = set(left["H"])
    fields = [endpoint[key] for endpoint in (left, right) for key in ("H", "K", "Ku")]
    if any(set(field) != modes for field in fields):
        raise ValueError("Both complete endpoint two-jets must use the same modes")
    if any(not isinstance(m, int) or m <= 0 or m % 2 for m in modes):
        raise ValueError("Use the complete positive even cosine spectrum")
    a = {key: {m: real(left[key][m]) for m in sorted(modes)}
         for key in ("H", "K", "Ku")}
    b = {key: {m: real(right[key][m]) for m in sorted(modes)}
         for key in ("H", "K", "Ku")}
    lam = {
        m: (b["H"][m]-a["H"][m]-a["K"][m]*I["00"]
            -a["Ku"][m]*I["10"]-b["K"][m]*I["01"]
            +b["Ku"][m]*I["11"])/I["b"]
        for m in sorted(modes)
    }
    return dict(left=a, right=b, total_moments=I, bubble_coefficient=lam)


def _height_increment(candidate, moments, mode):
    a, b = candidate["left"], candidate["right"]
    return (a["K"][mode]*moments["00"]+a["Ku"][mode]*moments["10"]
            +b["K"][mode]*moments["01"]-b["Ku"][mode]*moments["11"]
            +candidate["bubble_coefficient"][mode]*moments["b"])


def weighted_panel_fields(candidate, *, u, u_x, prefix_moments, suffix_moments):
    """Enclose H,K,K_x of one candidate throughout a source panel.

prefix_moments enclose integrals 0..u and suffix_moments integrals u..1.
For interval u, monotonicity of all five true positive integrands gives
whole-panel enclosures from the two panel endpoints.  The two height
formulas are intersected, retaining the same global bubble coefficient.
"""
    u, u_x = real(u), real(u_x)
    if u.upper() < 0 or u.lower() > 1 or not u_x > 0:
        raise ValueError("The source panel must meet [0,1] with positive du/dx")
    # The actual u belongs to [0,1] by its source-chart definition.  An Arb
    # hull may extend just beyond an endpoint because its radius is rounded.
    # Restrict to the mathematical domain; do not infer a domain assertion
    # merely from the endpoints of the rounded hull.
    u = intersection(u, arb(0).union(arb(1)))
    prefix = _check_moments(prefix_moments, strict=False)
    suffix = _check_moments(suffix_moments, strict=False)
    # Necessary consistency check; the actual common-integral obligation
    # is supplied by the source integrator, not inferred from this check.
    for key in MOMENT_KEYS:
        intersection(prefix[key]+suffix[key], candidate["total_moments"][key])
    basis, deriv = positive_basis(u), signed_basis_derivative(u)
    a, b = candidate["left"], candidate["right"]
    H, K, Kx = {}, {}, {}
    for m in sorted(a["H"]):
        lam = candidate["bubble_coefficient"][m]
        from_left = a["H"][m]+_height_increment(candidate, prefix, m)
        from_right = b["H"][m]-_height_increment(candidate, suffix, m)
        height = intersection(from_left, from_right)
        slope = (a["K"][m]*basis["00"]+a["Ku"][m]*basis["10"]
                 +b["K"][m]*basis["01"]-b["Ku"][m]*basis["11"]+lam*basis["b"])
        slope_u = (a["K"][m]*deriv[0]+a["Ku"][m]*deriv[1]
                   +b["K"][m]*deriv[2]+b["Ku"][m]*deriv[3]+lam*deriv[4])
        for target, value in ((H, height), (K, slope), (Kx, slope_u*u_x)):
            target[m] = target[-m] = acb(value/2)
    return H, K, Kx


def certify_weighted_panel(candidate, *, u, u_x, prefix_moments, suffix_moments,
                           radius, radius_x, w, log_w_x,
                           mean_candidate, mean_radius, tau=Fraction(1, 64),
                           binomial_degree=8, geometric_degree=8):
    """R48 same-height construction followed by complete R44 mean and defect."""
    H, K, Kx = weighted_panel_fields(
        candidate, u=u, u_x=u_x, prefix_moments=prefix_moments,
        suffix_moments=suffix_moments)
    result = _certify_same_height_fields(
        H, K, Kx, radius=radius, radius_x=radius_x, w=w, log_w_x=log_w_x,
        mean_candidate=mean_candidate, mean_radius=mean_radius, tau=tau,
        binomial_degree=binomial_degree, geometric_degree=geometric_degree,
        construction="R48 single quartic normalized slope and its five true positive weighted integrals")
    result.update(
        weighted_moment_enclosure_obligation=(
            "Total/prefix/suffix boxes enclose the same five integrals of "
            "r_u*w times q00,q10,q01,-q11,b on this fixed true background; "
            "u(x) and u_x are its actual single source chart"),
        weighted_moment_enclosures_certified_by_this_module=False,
        total_positive_moments={key: ball_record(value)
                                for key, value in candidate["total_moments"].items()},
        bubble_coefficient_cosine={str(m): ball_record(value)
                                   for m, value in candidate["bubble_coefficient"].items()},
        normalized_slope_W1=ball_record(norm(K, real(tau))),
        normalized_slope_source_derivative_W1=ball_record(norm(Kx, real(tau))),
        endpoint_height_and_nonmean_two_jets_exact_by_candidate_definition=True,
        saved_connection_momentum_matched_by_construction=False,
        actual_13port_radial_certificate=False)
    return result
