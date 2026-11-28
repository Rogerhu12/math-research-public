#!/usr/bin/env python3
"""Complete outward R727 posterior spherical-mean cap and directed branch glue.

Only public Actions evaluate intervals. The caller must bind the complete
actual spherical equation, full boundary integral and whole-angle data.
This module proves one local cap, not an unqualified global mean branch.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path

SCHEMA = "complete-R727-outward-posterior-spherical-mean-cap-v1"
GLUE_SCHEMA = "complete-R727-directed-small-cap-to-unique-cap-containment-v1"
PARENT_MATH_SHA256 = "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"
PARENT_MATH_BYTES = 72182
THEOREM_PATH = "results/R727-symmetric-spherical-boundary-posterior-root-without-acute-cap.md"
THEOREM_SHA256 = "cee8be0bc6084ed4091cdc68b368311c58715560ddc87086c514e52d7acf1d0f"
THEOREM_BYTES = 20494
DEFAULT_CAP_SEARCH_STEPS = 64
ANGLE_BRACKET_STEPS = 64


class PosteriorCapUnavailable(ArithmeticError):
    """The sufficient outward cap inequalities are unpaid, not a root failure."""


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Complete accurate R727 arithmetic requires public Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def encode(value):
    if isinstance(value, F):
        return str(value)
    if hasattr(value, "lo") and hasattr(value, "hi"):
        return [str(value.lo), str(value.hi)]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def canonical(value):
    return hashlib.sha256(json.dumps(encode(value), sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def definition():
    return dict(schema=SCHEMA, directed_glue_schema=GLUE_SCHEMA,
        complete_theorem=dict(path=THEOREM_PATH, bytes=THEOREM_BYTES,
            sha256=THEOREM_SHA256),
        original_outward_math_source_sha256=PARENT_MATH_SHA256,
        candidate_direction="exact N(all three original binary64 v words)",
        alpha0="accurate Lc times exact norm of original v",
        residual="alpha0*d0 + complete exact spherical B(d0) - fixed-seed K",
        symmetric_cutoff_pairing_and_full_boundary_measure_required=True,
        m="(b/2)*cos(theta_star/2)",
        L="(b/2)*theta_star/sin(theta_star)",
        perturbation_distance="sphere arc length L*eta, never unproved chord length",
        amin="alpha0*cos(eta)-L*eta-epsilon",
        amax="alpha0+L*eta+epsilon",
        kappa="m+amin",
        sufficient_conditions="0<eta<pi/2; beta+eta<pi; amin>0; amax<Lc; epsilon_t<kappa*eta",
        root_angle_radius="epsilon_t/kappa",
        root_scope="unique root in this complete closed cap only",
        full_raw_v_inverse_bound_at_proved_root="sqrt((1+L/kappa)^2+(amax/kappa)^2)/Lc",
        inverse_bound_not_claimed_for_every_point_of_cartesian_enclosure=True,
        adjacent_and_periodic_roots_need_directed_cap_containment=True,
        no_R709_or_R722_existence_hypothesis_reused=True,
        no_positive_vertical_direction_inferred=True,
        no_profile_projection_or_closed_surface_condition_inferred=True)


def bind_math(parent):
    path = Path(parent.__file__).resolve()
    if (path.stat().st_size != PARENT_MATH_BYTES or sha(path) != PARENT_MATH_SHA256
            or sha(parent.normalized_jets.__code__.co_filename) != PARENT_MATH_SHA256):
        raise ValueError("R727 requires the complete original outward interval math")
    return parent


def _box(parent, value, bits):
    if hasattr(value, "lo") and hasattr(value, "hi"):
        return parent.Interval(F(value.lo), F(value.hi), bits)
    return parent.box(value, bits)


def _vector(parent, value, bits):
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError("Retain all three components")
    return [_box(parent, q, bits) for q in value]


def _candidate(parent, words, bits):
    if not isinstance(words, list) or len(words) != 3 or any(type(v) is not str for v in words):
        raise ValueError("Keep all three actual binary64 candidate words")
    values = parent.point_vector(words)
    radius_lo, radius_hi = parent.point_norm(values, bits)
    if radius_lo <= 0:
        raise PosteriorCapUnavailable("The complete candidate normalization is unresolved")
    radius = parent.Interval(radius_lo, radius_hi, bits)
    direction = [(parent.Interval(v, v, bits)/radius).intersect(-1, 1) for v in values]
    return values, radius, direction


def _angle_bound(parent, cosine_lower, bits, budget_check):
    """Return rational beta with cos(beta)<=the paid cosine lower bound."""
    c = F(cosine_lower)
    if not -1 < c <= 1:
        raise PosteriorCapUnavailable("Complete reference/candidate non-antipodality is unresolved")
    if c == 1:
        return F(0)
    I = parent.Interval
    pi = parent.pi_bounds(bits)
    hi = pi.lo
    if parent.trig_boxes(I(hi, hi, bits))[1].hi > c:
        raise PosteriorCapUnavailable("Outward arithmetic cannot resolve the angle below pi")
    lo = F(0)
    for _ in range(ANGLE_BRACKET_STEPS):
        if budget_check is not None:
            budget_check()
        middle = (lo+hi)/2
        cosine = parent.trig_boxes(I(middle, middle, bits))[1]
        if cosine.hi <= c:
            hi = middle
        else:
            lo = middle
    return hi


def posterior_root_domain(parent_math, *, central_length, boundary_length,
        candidate_words, complete_residual, reference_candidate_cosine_lower,
        bits=160, cap_search_steps=DEFAULT_CAP_SEARCH_STEPS, budget_check=None):
    require_actions()
    k = bind_math(parent_math)
    if type(bits) is not int or not 64 <= bits <= 1024:
        raise ValueError("Keep an explicit complete outward arithmetic precision")
    if type(cap_search_steps) is not int or not 1 <= cap_search_steps <= 256:
        raise ValueError("Keep the complete declared finite cap search")
    if budget_check is not None and not callable(budget_check):
        raise ValueError("Use the outer producer's real budget check")
    I = k.Interval
    U = lambda value: k.upper_dyadic(value, bits)
    D = lambda value: k.lower_dyadic(value, bits)
    lc = _box(k, central_length, bits)
    b = _box(k, boundary_length, bits)
    if not 0 < lc.lo <= lc.hi or not 0 < b.lo <= b.hi:
        raise PosteriorCapUnavailable("The entire accurate central/boundary lengths must be positive")
    values, radius, direction = _candidate(k, candidate_words, bits)
    residual = _vector(k, complete_residual, bits)
    if len(residual) != 3:
        raise ValueError("Keep the full three-component accurate spherical mean residual")
    epsilon = U(k.norm_box(residual).hi)
    tangent_residual = k.vsub(residual, k.vscale(direction, k.dot(direction, residual)))
    epsilon_t = min(epsilon, U(k.norm_box(tangent_residual).hi))
    alpha0 = lc*radius
    beta = _angle_bound(k, reference_candidate_cosine_lower, bits, budget_check)
    pi = k.pi_bounds(bits)
    eta0 = min(F(1), (pi.lo-beta)/2)
    if not 0 < eta0 < pi.lo/2:
        raise PosteriorCapUnavailable("No declared candidate cap fits strictly below the antipodal boundary")
    attempts = []
    for attempt in range(cap_search_steps):
        if budget_check is not None:
            budget_check()
        eta = eta0/(2**attempt)
        theta = beta+eta
        if not 0 < eta < pi.lo/2 or not theta < pi.lo:
            raise ValueError("The explicit cap-search geometry is inconsistent")
        sintheta, _ = k.trig_boxes(I(theta, theta, bits))
        _, coshalf = k.trig_boxes(I(theta/2, theta/2, bits))
        _, coseta = k.trig_boxes(I(eta, eta, bits))
        if sintheta.lo <= 0 or coshalf.lo <= 0 or coseta.lo <= 0:
            attempts.append(dict(index=attempt, eta=eta,
                reason="positive exact trigonometric denominators unresolved"))
            continue
        m = D(b.lo*coshalf.lo/2)
        L = U(b.hi*theta/(2*sintheta.lo))
        amin = D(alpha0.lo*coseta.lo-L*eta-epsilon)
        amax = U(alpha0.hi+L*eta+epsilon)
        kappa = D(m+amin)
        margins = dict(positive_alpha_lower=amin,
            alpha_strictly_below_Lc=lc.lo-amax,
            outward_cap_boundary=kappa*eta-epsilon_t)
        if m <= 0 or amin <= 0 or amax >= lc.lo or kappa <= 0 or epsilon_t >= kappa*eta:
            attempts.append(dict(index=attempt, eta=eta, bounds=dict(m=m, L=L,
                amin=amin, amax=amax, kappa=kappa), margins=margins,
                reason="one or more complete sufficient cap inequalities remain unpaid"))
            continue
        rho = U(epsilon_t/kappa)
        if rho >= eta:
            attempts.append(dict(index=attempt, eta=eta, reason="rounded small-root cap is not strictly inside"))
            continue
        sinrhohalf, _ = k.trig_boxes(I(rho/2, rho/2, bits))
        _, cosrho = k.trig_boxes(I(rho, rho, bits))
        direction_error = min(F(2), U(2*sinrhohalf.hi))
        alpha_error = U(epsilon+L*rho+alpha0.hi*(1-cosrho.lo))
        vector_error = U((alpha_error+alpha0.hi*direction_error)/lc.lo)
        rlo, rhi = D(amin/lc.hi), U(amax/lc.lo)
        if not 0 < rlo <= rhi < 1:
            attempts.append(dict(index=attempt, eta=eta,
                reason="outward root radius has not separated both zero and one"))
            continue
        vbox = [I(v-vector_error, v+vector_error, bits).intersect(-rhi, rhi) for v in values]
        dbox = [I(max(F(-1), d.lo-direction_error),
                  min(F(1), d.hi+direction_error), bits) for d in direction]
        for axis in range(3):
            radial_box = I(rlo, rhi, bits)*dbox[axis]
            vbox[axis] = vbox[axis].intersect(radial_box.lo, radial_box.hi)
        inverse_square = (1+L/kappa)**2+(amax/kappa)**2
        inverse = U(k.sqrt_bounds(inverse_square, bits)[1]/lc.lo)
        qcap = U(1-k.trig_boxes(I(theta, theta, bits))[1].lo)
        if not 0 <= qcap < 2:
            attempts.append(dict(index=attempt, eta=eta,
                reason="outward true-root Slerp q cap remains unresolved below two"))
            continue
        inputs = dict(central_length=encode(lc), boundary_length=encode(b),
            complete_candidate_words=list(candidate_words),
            complete_residual=encode(residual),
            reference_candidate_cosine_lower=str(F(reference_candidate_cosine_lower)),
            precision_bits=bits, cap_search_steps=cap_search_steps)
        bounds = dict(candidate_radius_lower=radius.lo, candidate_radius_upper=radius.hi,
            candidate_alpha_lower=alpha0.lo, candidate_alpha_upper=alpha0.hi,
            candidate_direction_enclosure=direction, complete_residual_norm_upper=epsilon,
            complete_tangent_residual_norm_upper=epsilon_t,
            reference_candidate_angle_upper=beta, unique_cap_radius=eta,
            reference_to_every_cap_direction_angle_upper=theta,
            paired_boundary_tangent_monotonicity_lower=m,
            boundary_differential_operator_upper=L,
            accurate_root_alpha_lower=amin, accurate_root_alpha_upper=amax,
            complete_tangent_Hessian_lower=kappa, proved_root_angle_radius_upper=rho,
            accurate_root_radius_lower=rlo, accurate_root_radius_upper=rhi,
            accurate_root_direction_error_upper=direction_error,
            accurate_root_alpha_error_upper=alpha_error,
            accurate_root_vector_error_upper=vector_error,
            accurate_root_vector_enclosure=vbox, accurate_root_direction_enclosure=dbox,
            full_raw_v_J_inverse_upper_at_proved_root=inverse,
            true_root_reference_Slerp_q_upper=qcap)
        return dict(schema=SCHEMA, definition=definition(),
            definition_identity_sha256=canonical(definition()), complete_inputs=inputs,
            complete_input_identity_sha256=canonical(inputs),
            bounds=encode(bounds), strict_margins=encode(margins),
            successful_cap_search_index=attempt,
            preceding_complete_search_attempts=encode(attempts),
            complete_sufficient_R727_cap_inequalities_proved=True,
            local_positive_root_exists_and_is_unique_in_declared_cap=True,
            local_root_is_C2_when_complete_data_are_C2=True,
            global_reference_mean_branch_certified=False,
            adjacent_or_periodic_branch_glue_certified=False,
            full_raw_v_inverse_bound_only_at_proved_root=True,
            positive_vertical_direction_inferred=False,
            R709_or_R722_existence_domain_applied=False,
            accurate_profile_or_projected_frame_denominator_inferred=False)
    raise PosteriorCapUnavailable(
        "The complete R727 whole-angle cap inequalities remain unpaid after "
        +str(cap_search_steps)+" declared radii; no absent-root conclusion follows")


def validate_root_domain(value, *, parent_math, central_length, boundary_length,
        candidate_words, complete_residual, reference_candidate_cosine_lower,
        bits=160, budget_check=None):
    if not isinstance(value, dict) or value.get("schema") != SCHEMA:
        raise ValueError("Use a complete actual R727 root-domain object")
    steps = value.get("complete_inputs", {}).get("cap_search_steps")
    expected = posterior_root_domain(parent_math, central_length=central_length,
        boundary_length=boundary_length, candidate_words=candidate_words,
        complete_residual=complete_residual,
        reference_candidate_cosine_lower=reference_candidate_cosine_lower,
        bits=bits, cap_search_steps=steps, budget_check=budget_check)
    if canonical(value) != canonical(expected):
        raise ValueError("The entire recorded R727 cap differs from the complete recomputed object")
    return expected


def directed_cap_containment(parent_math, source_domain, target_domain, *, bits=160):
    """Algebraic containment only; caller proves same equation at the common angle."""
    require_actions()
    k = bind_math(parent_math)
    for value in (source_domain, target_domain):
        if (not isinstance(value, dict) or value.get("schema") != SCHEMA
                or value.get("complete_sufficient_R727_cap_inequalities_proved") is not True
                or value.get("definition") != definition()
                or value.get("definition_identity_sha256") != canonical(definition())
                or value.get("complete_input_identity_sha256") != canonical(value.get("complete_inputs"))):
            raise ValueError("Containment uses complete independently validated R727 caps")
    _, _, source_center = _candidate(k, source_domain["complete_inputs"]["complete_candidate_words"], bits)
    _, _, target_center = _candidate(k, target_domain["complete_inputs"]["complete_candidate_words"], bits)
    small = F(source_domain["bounds"]["proved_root_angle_radius_upper"])
    large = F(target_domain["bounds"]["unique_cap_radius"])
    gap = large-small
    if gap <= 0:
        return dict(schema=GLUE_SCHEMA, proved=False,
            reason="the complete source small cap is no smaller than the target uniqueness cap",
            source_domain_sha256=canonical(source_domain),
            target_domain_sha256=canonical(target_domain))
    cosine = k.trig_boxes(k.Interval(gap, gap, bits))[1]
    center_dot = k.dot(source_center, target_center).intersect(-1, 1)
    margin = center_dot.lo-cosine.hi
    return dict(schema=GLUE_SCHEMA, proved=margin>0,
        source_domain_sha256=canonical(source_domain),
        target_domain_sha256=canonical(target_domain),
        source_small_root_cap_radius=str(small),
        target_unique_cap_radius=str(large), exact_angle_difference=str(gap),
        complete_normalized_center_dot=encode(center_dot),
        outward_cosine_of_angle_difference=encode(cosine),
        strict_dot_margin=str(margin),
        same_complete_equation_and_common_angle_must_be_checked_by_caller=True,
        proof="angle(center_source,center_target)+small_root_radius<target_unique_cap_radius",
        global_branch_claimed=False)
