#!/usr/bin/env python3
"""Actual R726 spherical means: complete R727 cap, direct two-jet residuals.

The original R711/R713 twelve-piece scalar amplitude mathematics is retained.
The boundary is exact Slerp, never the original normalized chord or its
R709/R722 potential. Every candidate and complete radial integration pass is
bound to the real immutable actual point, 137 scientific sources and all input
bytes. Local mean caps are explicitly not a whole-circle branch certificate.
"""
from __future__ import annotations

from fractions import Fraction
F = Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

SCHEMA = "actual-fixed-fejer-r726-R727-posterior-mean-jets-v1"
ATTRIBUTION_SCHEMA = "actual-whole-angle-R727-spherical-mean-root-and-jets-attribution-v1"
PARENT_MATH_SHA256 = "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"
PARENT_MEAN_INTEGRAL_SHA256 = "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0"
ACTUAL_INPUT_SHA256 = "4082fb95d3e90b90701c893236b7a958d16cd883e3af280f65714245c58c2fd5"
ACTUAL_INPUT_SCHEMA = "actual-fixed-fejer-r726-complete-normal-packet-accurate-field-input-v1"
ACTUAL_DRIVER_SHA256 = "58630a875941be3612947e724aa25d9556b903c5ee1c392ff79f8def974e2813"
ACTUAL_READER_SHA256 = "1aae949feefb2e6bfb457d755aaa6a16412d9b5333344fa351b4ab598287248c"
ACTUAL_NORMAL_SHA256 = "335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9"
ACTUAL_PACKET_SHA256 = "9da481209cd48d82cb297b213650cc94c4f2148c097602f3495d57ba8f4508fc"
ACTUAL_RUNTIME_ROLE_COUNT = 137
SHARED_MATH_PROVIDER_SHA256 = "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a"
THEOREM_PATH = "results/R727-symmetric-spherical-boundary-posterior-root-without-acute-cap.md"
THEOREM_SHA256 = "cee8be0bc6084ed4091cdc68b368311c58715560ddc87086c514e52d7acf1d0f"
THEOREM_BYTES = 20494
SPHERICAL_KERNEL_NAME = "fixed_fejer_R726_exact_spherical_boundary_boxes.py"
SPHERICAL_KERNEL_SHA256 = "c7ba94caa8a527981a6a41caf53af7f3e34e50946b90cf8247dc029710d29409"
SPHERICAL_KERNEL_BYTES = 15754
CAP_KERNEL_NAME = "fixed_fejer_R727_posterior_spherical_mean_cap.py"
CAP_KERNEL_SHA256 = "c110ecba9019818cc5922ba12611868e0f2ebc1ada4b7c57f26b607b19c18e1d"
CAP_KERNEL_BYTES = 16340
R711_PATH = "results/R711-smooth-triangle-central-profile-and-geometric-comparison.md"
R711_SHA256 = "7df73fc19224cde3c315d31dfce053892f86ff9af03f376ecee62fdce47b9fe6"
R711_BYTES = 17893
R713_PATH = "results/R713-exact-smooth-triangle-moments-and-actual-fees.md"
R713_SHA256 = "ed9c96e7fd3ac2010f0cb82dc50ebb66d75a04e6683a0d918ff370f6767d7024"
R713_BYTES = 10284
MEAN_VECTOR_KEYS = ("v", "v_phi", "v_phiphi", "d", "d_phi", "d_phiphi",
                    "w", "w_phi", "w_phiphi")
MEAN_SCALAR_KEYS = ("lambda", "lambda_phi", "lambda_phiphi",
    "profile_moment", "profile_moment_first_derivative",
    "profile_moment_second_derivative")


class PosteriorDomainUnavailable(ArithmeticError):
    """The complete local accurate obligations remain unpaid."""


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("R727 actual spherical fees require public repository Actions")

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()

def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    if hasattr(value, "json") and callable(value.json):
        return value.json()
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    if value is None or type(value) in (bool, int, str):
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise TypeError("Keep exact arithmetic and finite original source-bound metadata")

def _copy(value):
    return json.loads(json.dumps(value, sort_keys=True, allow_nan=False))

def _digest(value):
    if (type(value) is not str or len(value) != 64
            or any(c not in "0123456789abcdef" for c in value)):
        raise ValueError("Use an actual complete SHA256 identity")
    return value

def _record(value):
    if (not isinstance(value, dict) or type(value.get("path")) is not str
            or type(value.get("bytes")) is not int or value["bytes"] < 0):
        raise ValueError("Keep a complete actual file path, byte count and digest")
    _digest(value.get("sha256"))
    return value

def bind_parent_math(parent):
    source_path = Path(parent.__file__).resolve()
    if (sha(source_path) != PARENT_MATH_SHA256
            or parent.PROVIDER_SHA != SHARED_MATH_PROVIDER_SHA256
            or tuple(parent.MEAN_VECTOR_KEYS) != MEAN_VECTOR_KEYS
            or tuple(parent.MEAN_SCALAR_KEYS) != MEAN_SCALAR_KEYS):
        raise ValueError("Use the complete unchanged original mathematical module")
    names = (
        "upper_dyadic", "box", "exact_relative_lengths", "fraction",
        "point_vector", "point_norm", "cap_floor", "nonnegative",
        "centered_vector", "normalized_jets", "dot", "vector_box", "vsub",
        "vscale", "pi_bounds", "word", "trig_boxes", "sqrt_bounds",
        "lower_dyadic", "complete_profile_moment_enclosures", "_complete_absolute_profile_moments", "vector_error",
        "norm_box", "vadd", "canonical")
    for name in names:
        function = getattr(parent, name)
        original = getattr(function, "__wrapped__", function)
        if (function.__name__ != name or original.__name__ != name
                or Path(original.__code__.co_filename).resolve() != source_path):
            raise ValueError("A complete original mathematical function changed: "+name)
    if Path(parent.Interval.__post_init__.__code__.co_filename).resolve() != source_path:
        raise ValueError("Use the original complete rational Interval implementation")
    return parent

copy_json = _copy

PAIRED_SEED_SOURCE_SHA256 = "176484582f7bdd83d0efe300d4ce7efe868df9d50a29310d7fb3aedce9d0f20a"
PAIRED_SEED_SCHEMA = "complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1"
AUXILIARY_MEAN_SOURCE_SHA256 = "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23"
PAIRED_Q_SOURCE_SHA256 = "b0b8d3fdffd587ac23b081f69201d9a7fcc52b0369ab483a0d5571fbadcac8b7"
PAIRED_PROFILE_DEFINITION_COPIED_FROM_COMPLETE_Q_SOURCE_SHA256 = PAIRED_Q_SOURCE_SHA256

BOUNDARY_CUTOFF_EPSILON = "1/8"
BOUNDARY_CUTOFF_SCHEMA = "complete-fixed-width-three-piece-C3-boundary-cutoff-v1"


def _flat_cutoff_polynomial_jets(t, epsilon):
    """Exact arithmetic for F inputs; working arithmetic for float inputs."""
    zero, one = t*0, t*0+1
    if t <= zero:
        return zero, zero, zero, zero
    if t >= one:
        return one, zero, zero, zero
    denominator = one-epsilon
    if epsilon <= t <= one-epsilon:
        return (t-epsilon/2)/denominator, one/denominator, zero, zero
    reflected = t > one-epsilon
    u = (one-t)/epsilon if reflected else t/epsilon
    G = (u*u*u*u)*(5+u*(-6+2*u))/2
    S = u*u*u*(10+u*(-15+6*u))
    S1 = 30*u*u*(one-u)*(one-u)
    S2 = 60*u*(one-u)*(one-2*u)
    value = epsilon*G/denominator
    first = S/denominator
    second = S1/(epsilon*denominator)
    third = S2/(epsilon*epsilon*denominator)
    if reflected:
        return one-value, first, -second, third
    return value, first, second, third


def _boundary_cutoff_exact_jets(t):
    """R725 value and first three normalized-coordinate derivatives, all exact."""
    if not isinstance(t, (str, F)):
        raise ValueError("Use an exact F boundary cutoff coordinate")
    t = F(t)
    return _flat_cutoff_polynomial_jets(t, F(BOUNDARY_CUTOFF_EPSILON))


def _boundary_cutoff_definition(support, central):
    """Complete fixed-rational three-piece law and every exact physical cut."""
    epsilon = F(BOUNDARY_CUTOFF_EPSILON)
    support = tuple(tuple(F(v) for v in pair) for pair in support)
    central = tuple(tuple(F(v) for v in pair) for pair in central)
    if (epsilon != F(1,8) or len(support) != 2 or len(central) != 2
            or any(len(pair) != 2 for pair in support+central)):
        raise ValueError("This source fixes the complete R725 cutoff at epsilon=1/8")
    edges = (F(0), epsilon, F(1)-epsilon, F(1))
    layers = []
    for index, ((left, right), (ca, cb)) in enumerate(zip(support, central)):
        if not left < ca < cb < right:
            raise ValueError("Every complete original boundary and central interval is required")
        for side, a, b, orientation in (("left", left, ca, 1), ("right", cb, right, -1)):
            physical = tuple(a+(b-a)*v for v in edges)
            layers.append(dict(support_index=index, side=side,
                exact_relative_interval=[str(a),str(b)],
                exact_relative_piece_edges=[str(v) for v in physical],
                exact_relative_internal_cuts=[str(v) for v in physical[1:-1]],
                original_interval_normalized_piece_edges=[str(v) for v in edges],
                cutoff_coordinate="t" if orientation == 1 else "1-t",
                odd_material_derivative_orientation=orientation,
                physical_piece_count=3,
                branches_in_increasing_material_order=(
                    ["left-polynomial","affine","right-reflection"] if orientation == 1 else
                    ["right-reflection","affine","left-polynomial"])))
    return dict(schema=BOUNDARY_CUTOFF_SCHEMA, proof_result="R725",
        exact_epsilon=str(epsilon), epsilon_is_a_fixed_source_parameter=True,
        epsilon_depends_on_angle_mean_direction_or_outer_point=False,
        accurate_law="C=epsilon*G(t/epsilon)/(1-epsilon); (t-epsilon/2)/(1-epsilon); 1-epsilon*G((1-t)/epsilon)/(1-epsilon)",
        exact_G_ascending_coefficients=["0","0","0","0","5/2","-3","1"],
        exact_velocity_S5_ascending_coefficients=["0","0","0","10","-15","6"],
        exact_normalized_piece_edges=[str(v) for v in edges],
        constant_extension_outside_unit_interval=True,
        piecewise_polynomial_degree=[6,1,6],
        matching_material_derivative_order=3,
        fourth_material_derivative_continuity_claimed=False,
        exact_cut_values_and_first_three_normalized_jets=[
            [str(v) for v in _boundary_cutoff_exact_jets(t)] for t in edges],
        exact_first_derivative_peak=str(F(1)/(1-epsilon)),
        exact_derivative_integral="1", exact_value_integral="1/2",
        four_boundary_layers=layers, complete_physical_boundary_piece_count=12,
        complete_new_internal_boundary_cut_count=8,
        original_central_halfwave_profile_changed=False,
        original_bubble_gamma_and_raw_defect_lift_changed=False,
        working_arithmetic="binary64 evaluation of this complete exact-rational law",
        working_rounding_or_integration_error_enclosed=False)



BOUNDARY_CUTOFF_THEOREM_PATH = "results/R725-fixed-width-boundary-cutoff-and-curvature-decomposition.md"
BOUNDARY_CUTOFF_THEOREM_SHA256 = "f40eb810c7c5c15583155335756a2ef3aa2c60155f319b6943725906e6171bc3"
BOUNDARY_CUTOFF_THEOREM_BYTES = 30079
BOUNDARY_CUTOFF_DEFINITION_COPIED_FROM_COMPLETE_Q_SOURCE_SHA256 = PAIRED_Q_SOURCE_SHA256


def boundary_cutoff_seed_scope(seed):
    """Bind the entire R725 endpoint law, not a renamed S5 boundary."""
    support = tuple(tuple(F(q) for q in pair)
        for pair in seed["exact_relative_support_intervals"])
    central = tuple(tuple(F(q) for q in pair)
        for pair in seed["exact_relative_central_intervals"])
    boundary = _boundary_cutoff_definition(support, central)
    working = seed.get("working_definition")
    if (seed.get("exact_boundary_cutoff_epsilon") != BOUNDARY_CUTOFF_EPSILON
            or seed.get("boundary_cutoff_definition") != boundary
            or not isinstance(working, dict)
            or working.get("exact_boundary_cutoff_epsilon") != BOUNDARY_CUTOFF_EPSILON
            or working.get("physical_boundary_cutoff_definition") != boundary
            or working.get("old_boundary_quadrature_mean_root_or_cache_inherited") is not False
            or working.get("original_outer_whole_cell_Gauss_and_partial_rule_is_separate") is not True):
        raise ValueError("Bind all twelve R725 boundary pieces and eight exact internal cuts")
    return json.loads(json.dumps(boundary, allow_nan=False))

def paired_halfwave_definition(central, profile_delta):
    """Exact complete radial profile; no numerical mean or field evaluation."""
    central = tuple(tuple(F(v) for v in pair) for pair in central)
    delta = F(profile_delta)
    if (len(central) != 2 or any(len(pair) != 2 for pair in central)
            or not F(0) < delta < F(1, 8)
            or not F(0) < central[0][1]-central[0][0]
            or central[0][1]-central[0][0] != central[1][1]-central[1][0]):
        raise ValueError("The paired halfwaves require two complete equal positive central intervals")
    edges = (F(0), 2*delta, F(1,2)-2*delta, F(1,2),
             F(1,2)+2*delta, F(1)-2*delta, F(1))
    if any(a >= b for a, b in zip(edges, edges[1:])):
        raise ValueError("Every one of the six exact halfwave pieces is required")
    return dict(schema="complete-equal-central-intervals-paired-halfwave-profile-v1",
        auxiliary_profile="the original complete R711 h_delta on [0,1]",
        auxiliary_mean_kernel_source_sha256=AUXILIARY_MEAN_SOURCE_SHA256,
        auxiliary_mean_rule_piece_count=12,
        physical_central_interval_count=2, physical_piece_count_per_interval=6,
        complete_physical_pair_piece_count=12,
        exact_profile_delta=str(delta),
        exact_normalized_piece_edges=[str(v) for v in edges],
        exact_relative_central_intervals=[[str(v) for v in pair] for pair in central],
        exact_relative_central_each_length=str(central[0][1]-central[0][0]),
        exact_relative_physical_piece_edges=[
            [str(a+(b-a)*v) for v in edges] for a,b in central],
        signs_in_radial_discovery_order=[1,-1],
        physical_profile="sign[index]*h_delta(t/2); t=(s-a)/(b-a)",
        radial_derivative_chain_factor="1/2",
        combined_cosine_mean="Lc*A_delta(lambda)*d",
        combined_transverse_mean="zero by equal complete central lengths and opposite signs",
        transverse_mean_zero_in_each_individual_interval=False,
        old_per_interval_odd_physical_profile_inherited=False)



def paired_halfwave_seed_scope(seed, base_model, normal_model):
    """Bind the exact two physical halfwaves separately from the twelve-piece A rule."""
    if (not isinstance(seed, dict)
            or seed.get("schema") != PAIRED_SEED_SCHEMA
            or seed.get("source_sha256") != PAIRED_SEED_SOURCE_SHA256
            or seed.get("mean_kernel_source_sha256") != AUXILIARY_MEAN_SOURCE_SHA256
            or base_model.get("fixed_supported_unit_seed_model") != seed
            or normal_model.get("fixed_supported_unit_seed_model") != seed
            or base_model.get("fixed_supported_unit_seed_identity_sha256") != canonical(seed)
            or normal_model.get("fixed_supported_unit_seed_identity_sha256") != canonical(seed)):
        raise ValueError("The entire paired physical seed must be the current base and normal seed")
    support = tuple(tuple(F(v) for v in pair)
        for pair in seed["exact_relative_support_intervals"])
    boundary = F(seed["exact_relative_boundary_total_length"])
    if (len(support) != 2 or any(len(pair) != 2 for pair in support)
            or not 0 < support[0][0] < support[0][1] < support[1][0] < support[1][1] < 1
            or boundary <= 0 or boundary >= 2*min(b-a for a,b in support)):
        raise ValueError("Keep both full separated supports and all four positive boundary layers")
    central = tuple((a+boundary/4,b-boundary/4) for a,b in support)
    profile_delta = F(seed["exact_profile_delta"])
    physical = paired_halfwave_definition(central,profile_delta)
    if (seed.get("exact_relative_boundary_each_end_length") != str(boundary/4)
            or seed.get("exact_relative_central_intervals") != physical["exact_relative_central_intervals"]
            or seed.get("paired_halfwave_definition") != physical
            or seed.get("mathematical_profile_piece_count") != 6
            or seed.get("mathematical_profile_piece_count_scope") != "one physical central interval"
            or seed.get("auxiliary_mean_profile_piece_count") != 12
            or seed.get("complete_physical_pair_piece_count") != 12
            or seed.get("mathematical_amplitude_interval") != "(0,pi)"):
        raise ValueError("The complete physical six-plus-six halfwave definition differs")
    working = seed.get("working_definition")
    if (not isinstance(working,dict)
            or working.get("schema") != "R726-spherical-boundary-paired-halfwave-reference-working-definition-v1"
            or working.get("physical_central_profile_definition") != physical
            or working.get("auxiliary_mean_metadata_describes_original_full_R711_rule") is not True
            or working.get("physical_profile_is_not_the_auxiliary_full_period_on_each_interval") is not True
            or working.get("actual_field_quadrature_or_closure_words_inherited_from_original_seed") is not False):
        raise ValueError("Keep the actual new working profile distinct from its original auxiliary A rule")
    boundary_cutoff_seed_scope(seed)
    return copy_json(physical)


SPHERICAL_BOUNDARY_SCHEMA = "complete-R726-spherical-boundary-working-value-and-angular-jets-v1"
SPHERICAL_SMALL_Q_MAX = 0.25
SPHERICAL_SERIES_DEGREE = 32
R726_PROOF_PATH = "results/R726-spherical-boundary-strong-monotonicity-and-positive-mean-root.md"
R726_PROOF_SHA256 = "faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b"
R726_PROOF_BYTES = 27362

def _spherical_boundary_definition():
    """Complete declared formulas; this function evaluates no field or root."""
    return dict(
        schema=SPHERICAL_BOUNDARY_SCHEMA,
        source_sha256=AUXILIARY_MEAN_SOURCE_SHA256,
        theorem_source_sha256=R726_PROOF_SHA256,
        accurate_boundary="S_chi(N(x),N(y)); S=sin((1-chi)*theta)/sin(theta)*u+sin(chi*theta)/sin(theta)*d",
        accurate_zero_angle="the analytic extension at u=d, with value u",
        accurate_domain="nonzero x,y and N(x) != -N(y); acute-root theorems have additional hypotheses",
        accurate_normal_extension="normalize both arguments; output normalization is the identity in exact Slerp arithmetic",
        working_coordinate="q=sum((N(x)-N(y))**2)/2; no clipping of q or dot products",
        working_output="N(f_(1-chi)(q)*N(x)+f_chi(q)*N(y))",
        working_small_q_interval=[0.0, SPHERICAL_SMALL_Q_MAX],
        working_small_q_degree=SPHERICAL_SERIES_DEGREE,
        working_coefficient_recurrence="c0=a; c[n+1]=(((n+1)**2-a*a)/((n+1)*(2*n+3)))*c[n]",
        working_q_derivatives="first and second simultaneous Horner derivatives of the same actual coefficient array",
        working_a_derivative="differentiate the same coefficient recurrence; never substitute a separately rounded derivative table",
        working_large_q="theta=acos(1-q); f=sin(a*theta)/sin(theta); explicit first/second chain derivatives",
        working_coefficient_endpoints="a=0 or1 uses the exact constant coefficient value and zero q derivatives; a derivative is retained",
        input_normalizations_and_output_normalization_differentiated=True,
        small_series_truncation_is_not_an_exact_Slerp_identity=True,
        branch_switch_is_not_claimed_exact_C2_in_working_arithmetic=True,
        coefficient_rounding_trigonometric_quadrature_root_and_jet_errors_enclosed=False,
        degree32_exact_coefficient_tail_bounds_at_q_quarter=dict(
            value_strictly_below="2^-98", q_first_strictly_below="2^-91",
            q_second_strictly_below="2^-84", a_first_strictly_below="2^-96",
            scope="only infinite-series truncation in exact arithmetic; not floating-point or full-field error"),
        R709_Euclidean_potential_or_R722_posterior_formula_inherited=False,
        R726_acute_existence_or_global_branch_verified=False,
        working_antipodal_or_nonfinite_pairs_unavailable=True,
        all_original_boundary_nodes_weights_and_two_angular_orders_retained=True)


def spherical_seed_scope(seed):
    """Read the actual complete spherical working graph without evaluating it.

    The expected object is the whole declared 2513 definition. Its finite
    approximation is a working-source identity, never the accurate Slerp fee.
    """
    expected = _spherical_boundary_definition()
    working = seed.get("working_definition")
    if (seed.get("spherical_boundary_definition") != expected
            or not isinstance(working,dict)
            or working.get("spherical_boundary_definition") != expected
            or working.get("mean_and_field_use_same_raw_v_and_full_two_angular_jet_graph") is not True
            or working.get("old_R709_potential_or_R722_posterior_formula_inherited") is not False
            or working.get("R726_acute_domain_and_existence_hypotheses_certified") is not False
            or seed.get("accurate_mean_definition") !=
                "Lc*v+integral_E S_chi(T0,N(v))=P_original-Gamma_original-integral_complement_U T0; a_delta(lambda)=norm(v)"
            or seed.get("accurate_definition") !=
                "fixed original unit T0 outside U; R726 S_chi(T0,d) on all boundary layers; cos(lambda*h_delta(t/2))*d+sign[index]*sin(lambda*h_delta(t/2))*w on the two equal central intervals"):
        raise ValueError("Bind the complete actual R726 spherical mean/field graph and its unpaid accurate obligations")
    return copy_json(expected)


def boundary_cutoff_interval_bounds(lower, upper):
    """Exact outward range of C and C' using the proved R725 monotonic pieces."""
    require_actions()
    if any(not isinstance(q, (str, Fraction)) for q in (lower, upper)):
        raise ValueError("Use exact interval endpoints for the fixed R725 cutoff")
    lower, upper = Fraction(lower), Fraction(upper)
    if lower > upper:
        raise ValueError("The cutoff interval endpoints are reversed")
    lo, hi = max(Fraction(0), lower), min(Fraction(1), upper)
    if lo > hi:
        raise ValueError("The declared boundary interval misses its exact cutoff domain")
    epsilon = Fraction(BOUNDARY_CUTOFF_EPSILON)
    left = _boundary_cutoff_exact_jets(lo)
    right = _boundary_cutoff_exact_jets(hi)
    derivative_lower = min(left[1], right[1])
    derivative_upper = (Fraction(1)/(1-epsilon)
        if lo <= 1-epsilon and hi >= epsilon else max(left[1], right[1]))
    return left[0], right[0], derivative_lower, derivative_upper

def boundary_leaf_attribution(boundary, kind, support_index, left, right, S):
    """One exact physical boundary polynomial piece, including its orientation."""
    fields = dict(boundary_cutoff_piece_index=None, boundary_cutoff_branch=None,
        odd_material_derivative_orientation=None)
    if kind not in ("boundary_left", "boundary_right"):
        return fields
    if type(support_index) is not int or support_index not in (0, 1):
        raise ValueError("Keep the exact support index of each complete boundary leaf")
    if (not isinstance(boundary, dict)
            or boundary.get("schema") != BOUNDARY_CUTOFF_SCHEMA
            or boundary.get("exact_epsilon") != BOUNDARY_CUTOFF_EPSILON
            or len(boundary.get("four_boundary_layers", [])) != 4
            or S.lo <= 0):
        raise ValueError("Bind the entire R725 boundary definition and positive exact S")
    def pair(value):
        if (not isinstance(value, (tuple, list)) or len(value) != 2
                or any(type(q) is not int and not isinstance(q, (str, Fraction)) for q in value)):
            raise ValueError("Retain both exact affine material-coordinate coefficients")
        return tuple(Fraction(q) for q in value)
    def lower_difference(b, a):
        da, db = b[0]-a[0], b[1]-a[1]
        return da*(S.lo if da >= 0 else S.hi)+db
    a, b = pair(left), pair(right)
    if lower_difference(b, a) <= 0:
        raise PosteriorDomainUnavailable("The complete boundary leaf width remains unresolved")
    side = "left" if kind == "boundary_left" else "right"
    layer = boundary["four_boundary_layers"][2*support_index+(side == "right")]
    if layer.get("support_index") != support_index or layer.get("side") != side:
        raise ValueError("The exact ordered four-boundary-layer definition changed")
    edges = [(Fraction(q), Fraction(0)) for q in layer["exact_relative_piece_edges"]]
    if len(edges) != 4 or any(x >= y for x, y in zip(edges, edges[1:])):
        raise ValueError("Retain both internal cuts of this entire boundary layer")
    hits = [j for j in range(3) if lower_difference(a,edges[j]) >= 0
        and lower_difference(edges[j+1],b) >= 0]
    if len(hits) != 1:
        raise PosteriorDomainUnavailable("The full exact boundary leaf is not resolved inside one R725 polynomial piece")
    j = hits[0]
    return dict(boundary_cutoff_piece_index=j,
        boundary_cutoff_branch=layer["branches_in_increasing_material_order"][j],
        odd_material_derivative_orientation=layer["odd_material_derivative_orientation"])

def complete_paired_profile_moment_enclosures(parent,seed,lambda_word,*,bits=160,series_order=48):
    """The entire original auxiliary A/A'/A'' arithmetic under the true paired seed."""
    require_actions()
    physical = paired_halfwave_definition(seed["exact_relative_central_intervals"],
        seed["exact_profile_delta"])
    if (seed.get("schema") != PAIRED_SEED_SCHEMA
            or seed.get("source_sha256") != PAIRED_SEED_SOURCE_SHA256
            or seed.get("mean_kernel_source_sha256") != AUXILIARY_MEAN_SOURCE_SHA256
            or seed.get("mathematical_profile_piece_count") != 6
            or seed.get("auxiliary_mean_profile_piece_count") != 12
            or seed.get("complete_physical_pair_piece_count") != 12
            or seed.get("paired_halfwave_definition") != physical
            or seed.get("mathematical_amplitude_interval") != "(0,pi)"):
        raise ValueError("Use the full paired physical seed and its unchanged auxiliary twelve-piece A rule")
    Interval,word = parent.Interval,parent.word
    _complete_absolute_profile_moments = parent._complete_absolute_profile_moments
    delta = Fraction(seed['exact_profile_delta'])
    if (isinstance(series_order, bool) or not isinstance(series_order, int)
            or series_order < 2 or series_order % 2):
        raise ValueError('The complete simultaneous derivative series uses one even L>=2')
    if not isinstance(lambda_word, str):
        raise TypeError('Bind the actual canonical binary64 amplitude word')
    x = word(lambda_word)
    moments = _complete_absolute_profile_moments(delta, series_order+1)
    x_box = Interval(x, x, bits)
    x2 = x_box*x_box
    values = []
    remainders = []
    for derivative in range(3):
        first_even = 0 if derivative == 0 else 2
        total = Interval(0, 0, bits)
        for degree in range(series_order, first_even-1, -2):
            coefficient = (Fraction((-1)**(degree//2))*moments[degree]
                           /math.factorial(degree-derivative))
            total = total*x2+coefficient
        if derivative == 1:
            total = x_box*total
        power = series_order+1-derivative
        remainder = moments[series_order+1]*abs(x)**power/math.factorial(power)
        values.append(total+Interval(-remainder, remainder, bits))
        remainders.append(remainder)
    proof_identity = dict(exact_profile_delta=str(delta), maximum_absolute_moment_degree=series_order+1,
        absolute_moments=[str(value) for value in moments])
    return dict(intervals=values, derivative_orders=[0, 1, 2],
        exact_profile_delta=str(delta), actual_lambda_binary64_hex=lambda_word,
        even_series_order=series_order, precision_bits=bits,
        exact_absolute_moment_identity_sha256=canonical(proof_identity),
        exact_mass=moments[0], exact_remainder_moment=moments[series_order+1],
        exact_Taylor_remainder_upper=remainders,
        all_twelve_profile_pieces_in_exact_moments=True,
        exact_Fraction_polynomial_integrals=True,
        polynomial_evaluation_outward_dyadic=True,
        working_quadrature_or_trigonometric_accuracy_assumed=False,
        accurate_moment_enclosures_computed_here=True)

def _bind_actual(actual):
    if (not isinstance(actual, dict) or actual.get("schema") != ACTUAL_INPUT_SCHEMA
            or actual.get("source_sha256") != ACTUAL_INPUT_SHA256
            or actual.get("actual_driver_sha256") != ACTUAL_DRIVER_SHA256
            or actual.get("complete_pure_reader_sha256") != ACTUAL_READER_SHA256):
        raise ValueError("R727 attribution requires the complete actual spherical input")
    model = actual["complete_model"]
    if (model.get("source_sha256") != ACTUAL_NORMAL_SHA256
            or canonical(model) != actual.get("model_identity_sha256")
            or model.get("normal_stage_count") != 32
            or actual.get("full_stage_count") != 32):
        raise ValueError("The complete actual normal model or all thirty-two stages differ")
    roles = actual["full_scientific_runtime_source_records"]
    if not isinstance(roles, dict) or len(roles) != ACTUAL_RUNTIME_ROLE_COUNT:
        raise ValueError("Retain every actual complete scientific source role")
    for record in roles.values():
        _record(record)
    pins = actual["source_sha256_by_role"]
    expected = dict(driver=ACTUAL_DRIVER_SHA256, reader=ACTUAL_READER_SHA256,
        normal=ACTUAL_NORMAL_SHA256, packets=ACTUAL_PACKET_SHA256,
        reference_fees=PARENT_MATH_SHA256, mean_integrals=PARENT_MEAN_INTEGRAL_SHA256)
    if any(pins.get(role) != digest for role, digest in expected.items()):
        raise ValueError("The complete actual input's scientific or exact-math source differs")
    for key in ("current_full_point_sha256", "actual_snapshot_identity_sha256",
            "model_identity_sha256", "exact_fixed_target_identity_sha256",
            "actual_reference_model_identity_sha256", "fixed_chart_core_sha256",
            "mathematical_target_identity_sha256", "fixed_scalar_metric_identity_sha256"):
        _digest(actual.get(key))
    for key in ("scientific_report", "actual_snapshot_file", "current_point_arrays_file"):
        _record(actual[key])
    base = model["base_complete_model"]
    seed = base["fixed_supported_unit_seed_model"]
    physical = paired_halfwave_seed_scope(seed,base,model)
    if (roles["seed_reference"]["sha256"] != PAIRED_SEED_SOURCE_SHA256
            or roles["new_moment_input"]["sha256"] != PAIRED_Q_SOURCE_SHA256
            or roles["seed_mean"]["sha256"] != AUXILIARY_MEAN_SOURCE_SHA256
            or actual.get("complete_paired_halfwave_physical_definition") != physical
            or actual.get("paired_halfwave_physical_definition_identity_sha256") != canonical(physical)
            or actual.get("physical_profile_piece_count_per_central_interval") != 6
            or actual.get("complete_physical_pair_piece_count") != 12
            or actual.get("auxiliary_mean_profile_piece_count") != 12
            or actual.get("combined_central_mean_uses_R724_pair_identity") is not True
            or actual.get("per_interval_transverse_mean_assumed_zero") is not False):
        raise ValueError("The actual complete physical halfwave pair or its auxiliary mean attribution changed")
    boundary = boundary_cutoff_seed_scope(seed)
    proof = _record(actual["boundary_cutoff_theorem_source"])
    if (actual.get("complete_boundary_cutoff_definition") != boundary
            or actual.get("boundary_cutoff_definition_identity_sha256") != canonical(boundary)
            or actual.get("complete_physical_boundary_piece_count") != 12
            or actual.get("complete_internal_boundary_cut_count") != 8
            or actual.get("original_boundary_mean_or_quadrature_words_inherited") is not False
            or proof["sha256"] != BOUNDARY_CUTOFF_THEOREM_SHA256
            or proof["bytes"] != BOUNDARY_CUTOFF_THEOREM_BYTES):
        raise ValueError("The actual whole-input R725 boundary law or full theorem record changed")
    spherical = spherical_seed_scope(seed)
    spherical_proof = _record(actual["spherical_boundary_theorem_source"])
    if (actual.get("complete_spherical_boundary_definition") != spherical
            or actual.get("spherical_boundary_definition_identity_sha256") != canonical(spherical)
            or actual.get("accurate_spherical_mean_root_or_R727_domain_paid_here") is not False
            or actual.get("old_R709_or_R722_chord_existence_inherited") is not False
            or spherical_proof["sha256"] != R726_PROOF_SHA256
            or spherical_proof["bytes"] != R726_PROOF_BYTES):
        raise ValueError("The entire actual R726 spherical graph or accurate/working separation changed")
    return seed

def _candidate_source(parent, actual, working):
    expected = set(MEAN_VECTOR_KEYS+MEAN_SCALAR_KEYS+(
        "literal_phi_hex", "actual_completed_batch_index", "actual_raw_batch_sha256"))
    if not isinstance(working, dict) or set(working) != expected:
        raise ValueError("Retain the entire original actual candidate row")
    angle = working["literal_phi_hex"]
    parent.word(angle)
    if type(angle) is not str:
        raise ValueError("Use the original canonical literal-angle word")
    for name in MEAN_VECTOR_KEYS:
        values = working[name]
        if not isinstance(values, list) or len(values) != 3:
            raise ValueError("Keep every component of every saved candidate vector")
        for value in values:
            if type(value) is not str:
                raise ValueError("Keep original canonical binary64 words")
            parent.word(value)
    for name in MEAN_SCALAR_KEYS:
        if type(working[name]) is not str:
            raise ValueError("Keep original canonical binary64 scalar words")
        parent.word(working[name])
    index = working["actual_completed_batch_index"]
    sources = actual["complete_actual_seed_candidate_sources"]
    if type(index) is not int or not 0 <= index < len(sources):
        raise ValueError("Use a genuinely completed complete mean batch")
    source = sources[index]
    record = _record(source["runner_raw_arrays"])
    angles = source["literal_angle_hex"]
    if (source.get("actual_completed_batch_index") != index
            or type(angles) is not list or len(angles) != len(set(angles))
            or angles.count(angle) != 1
            or record["sha256"] != working["actual_raw_batch_sha256"]
            or source["complete_original_batch_metadata"].get("literal_angle_hex") != angles
            or source["complete_original_batch_metadata"].get("runner_raw_arrays") != record):
        raise ValueError("The actual complete candidate batch/source/order differs")
    return source

def verify_saved_candidate(parent, actual, working, files):
    """Re-read the original complete mean batch; no working field is evaluated."""
    require_actions()
    k = bind_parent_math(parent)
    seed = _bind_actual(actual)
    source = _candidate_source(k, actual, working)
    record = source["runner_raw_arrays"]
    path = Path(files.verify(record)).resolve()
    if path.stat().st_size != record["bytes"] or sha(path) != record["sha256"]:
        raise ValueError("The entire original mean batch changed before rereading")
    import numpy as np
    angles = source["literal_angle_hex"]
    index = angles.index(working["literal_phi_hex"])
    with np.load(path, allow_pickle=False) as data:
        if (str(data["seed_model_identity"].item()) != k.canonical(seed)
                or [float(v).hex() for v in data["phi"]] != angles):
            raise ValueError("The complete original candidate batch changed seed or angle order")
        for name in MEAN_VECTOR_KEYS+MEAN_SCALAR_KEYS:
            array = np.array(data[name], copy=True)
            shape = (len(angles), 3) if name in MEAN_VECTOR_KEYS else (len(angles),)
            if (array.shape != shape or array.dtype.kind != "f" or array.dtype.itemsize != 8
                    or not np.isfinite(array).all()):
                raise ValueError("A complete original mean candidate array is invalid")
            value = ([float(v).hex() for v in array[index]] if name in MEAN_VECTOR_KEYS
                     else float(array[index]).hex())
            if value != working[name]:
                raise ValueError("The root-domain candidate differs from the entire recorded mean row: "+name)
    if path.stat().st_size != record["bytes"] or sha(path) != record["sha256"]:
        raise ValueError("The entire original mean batch changed during rereading")
    files.verify(record)
    return source

def _verify_complete_integral_arithmetic(parent, seed, working, result, plan, leaves, bits, expected_v_jets, pass_kind):
    """Recheck full binary leaf coverage and all already-computed integral sums."""
    k = parent
    if (pass_kind not in ("candidate", "first-root-residual", "second-root-residual")
            or result.get("spherical_mean_pass") != pass_kind
            or result.get("complete_raw_v_jets") != encode(expected_v_jets)
            or result.get("exact_spherical_kernel_sha256") != SPHERICAL_KERNEL_SHA256):
        raise ValueError("Retain the complete actual spherical integration pass and all raw v jets")
    row = result["angles"][0]
    S = k.box(row["fees"]["accurate_S_enclosure"], bits)
    length = k.exact_relative_lengths(seed, S, bits)
    def pair(value):
        if not isinstance(value, (list, tuple)) or len(value) != 2:
            raise ValueError("Retain both exact affine coefficients")
        return tuple(k.fraction(q) for q in value)
    def midpoint(left, right):
        return tuple((a+b)/2 for a, b in zip(pair(left), pair(right)))
    def positive_width(left, right):
        a, b = pair(left), pair(right)
        da, db = b[0]-a[0], b[1]-a[1]
        lower = da*(S.lo if da >= 0 else S.hi)+db
        if lower <= 0:
            raise PosteriorDomainUnavailable("Complete mean-leaf positive widths are not resolved by the declared exact S box")
    support = [[k.fraction(q) for q in p] for p in seed["exact_relative_support_intervals"]]
    central = length["relative_central_intervals"]
    physical = paired_halfwave_definition(central,seed["exact_profile_delta"])
    complete_edges = {pair(item["left"]) for item in plan}
    if plan:
        complete_edges.add(pair(plan[-1]["right"]))
    if any((Fraction(edge),Fraction(0)) not in complete_edges
            for interval in physical["exact_relative_physical_piece_edges"] for edge in interval):
        raise ValueError("The exact mean plan must retain all six physical cuts in both complete central intervals")
    cutoff_definition = boundary_cutoff_seed_scope(seed)
    if any((Fraction(edge),Fraction(0)) not in complete_edges
            for layer in cutoff_definition["four_boundary_layers"]
            for edge in layer["exact_relative_piece_edges"]):
        raise ValueError("The full mean plan lost an endpoint or one of the eight exact R725 internal cuts")
    segments = []
    before = Fraction(0)
    for index, ((a, b), (ca, cb)) in enumerate(zip(support, central)):
        segments.extend((("outside", None, before, a),
            ("boundary_left", index, a, ca), ("central", index, ca, cb),
            ("boundary_right", index, cb, b)))
        before = b
    segments.append(("outside", None, before, Fraction(1)))
    cursor = 0
    for kind, support_index, left, right in segments:
        start = (left, Fraction(0))
        end = (right, Fraction(0))
        if start == end:
            continue
        if cursor >= len(plan) or pair(plan[cursor]["left"]) != start:
            raise ValueError("The complete mean plan lost a support, boundary, central or complement endpoint")
        while True:
            if cursor >= len(plan):
                raise ValueError("The complete mean plan has an unfilled radial interval")
            item = plan[cursor]
            if (item.get("id") != "r"+str(cursor) or item.get("depth") != 0
                    or item.get("kind") != kind or item.get("support_index") != support_index
                    or item.get("central_member_of_exact_pair_Lc_v") is not (kind == "central")
                    or "centrally_integrated_by_exact_Lc_v" in item
                    or pair(item["left"]) != start):
                raise ValueError("The entire original exact mean partition changed")
            positive_width(item["left"], item["right"])
            cutoff_scope = boundary_leaf_attribution(cutoff_definition,kind,
                support_index,item["left"],item["right"],S)
            if any(key not in item or item[key] != value for key,value in cutoff_scope.items()):
                raise ValueError("A mean leaf changed its exact R725 branch or derivative orientation")
            start = pair(item["right"])
            cursor += 1
            if start == end:
                break
    if cursor != len(plan):
        raise ValueError("The mean plan has undeclared trailing radial pieces")
    by_id = {}
    prefixes = set()
    for leaf in leaves:
        description = leaf["description"]
        name = description["id"]
        if type(name) is not str or name in by_id:
            raise ValueError("Every complete active integral leaf has one identity")
        parts = name.split("/")
        if any(p not in ("0", "1") for p in parts[1:]):
            raise ValueError("Only the original exact binary midpoint refinement is allowed")
        by_id[name] = leaf
        for i in range(1, len(parts)+1):
            prefixes.add("/".join(parts[:i]))
    seen = set()
    stack = [dict(item) for item in reversed(plan) if item["kind"] != "central"]
    while stack:
        description = stack.pop()
        name = description["id"]
        if name in by_id:
            if by_id[name]["description"] != description:
                raise ValueError("An active leaf altered its exact endpoints, region or depth")
            seen.add(name)
            continue
        if name+"/0" not in prefixes or name+"/1" not in prefixes:
            raise ValueError("Both complete children are required before replacing an integral parent")
        middle = [str(q) for q in midpoint(description["left"], description["right"])]
        for index, left, right in reversed((
                (0, description["left"], middle),
                (1, middle, description["right"]))):
            stack.append(dict(description, id=name+"/"+str(index),
                depth=description["depth"]+1, left=left, right=right))
    if seen != set(by_id):
        raise ValueError("A mean integral leaf is outside the complete noncentral domain")
    complement = [[Fraction(0), Fraction(0)] for _ in range(2)]
    boundary = [[[[Fraction(0), Fraction(0)] for _ in range(3)] for _ in range(3)]]
    for leaf in leaves:
        kind = leaf["description"]["kind"]
        if kind == "outside":
            if (leaf.get("contribution") != "complement_scalar_b_c"
                    or len(leaf["integral"]) != 2):
                raise ValueError("Keep both complete complement scalar contributions")
            for index, value in enumerate(leaf["integral"]):
                item = k.box(value, bits)
                complement[index][0] += item.lo
                complement[index][1] += item.hi
        else:
            if (kind not in ("boundary_left", "boundary_right")
                    or leaf.get("contribution") != "complete_boundary_three_angular_jets"
                    or len(leaf["integral"]) != 1 or len(leaf["integral"][0]) != 3):
                raise ValueError("Keep all three full boundary angular jets")
            evaluation = leaf.get("spherical_boundary_evaluation")
            if (not isinstance(evaluation, dict)
                    or evaluation.get("source_sha256") != SPHERICAL_KERNEL_SHA256
                    or evaluation.get("pass_kind") != pass_kind
                    or evaluation.get("complete_raw_v_jets") != encode(expected_v_jets)
                    or evaluation.get("accurate_output_is_Slerp_not_working_polynomial") is not True):
                raise ValueError("The full boundary leaf lost its exact spherical source or mean graph")
            for order, vector in enumerate(leaf["integral"][0]):
                for axis, item in enumerate(k.vector_box(vector, bits)):
                    boundary[0][order][axis][0] += item.lo
                    boundary[0][order][axis][1] += item.hi
    exact_complement = [k.Interval(a, b, bits) for a, b in complement]
    exact_boundary = [[[k.Interval(a, b, bits) for a, b in jet] for jet in angle]
                      for angle in boundary]
    if (encode(exact_complement) != result["complement_scalar_integral"]
            or encode(exact_boundary) != result["complete_boundary_angular_integrals"]):
        raise ValueError("The full boundary/complement sum is not the exact sum of all active leaves")
    K = row["accurate_K_angular_jets"]
    residuals = row["accurate_total_equation_vector_enclosures"]
    if len(K) != 3 or len(residuals) != 3:
        raise ValueError("Retain all three accurate K and total-equation jets")
    Lc = k.Interval(length["central_lower"], length["central_upper"], bits)
    for order in range(3):
        v = k.vector_box(encode(expected_v_jets[order]), bits)
        total = k.vsub(k.vadd(k.vscale(v, Lc), exact_boundary[0][order]),
                      k.vector_box(K[order], bits))
        if encode(total) != residuals[order]:
            raise ValueError("The accurate total residual omits an exact Lc*v, boundary or K term")
    return dict(complete_noncentral_binary_cover_rechecked=True,
        complete_radial_plan_count=len(plan), complete_active_integral_leaf_count=len(leaves),
        exact_boundary_and_complement_endpoint_sums_rechecked=True,
        all_three_full_total_equation_vector_sums_rechecked=True,
        complete_equal_opposite_halfwave_mean_identity_rechecked=True,
        complete_physical_pair_definition_identity_sha256=canonical(physical),
        complete_boundary_cutoff_definition_identity_sha256=canonical(cutoff_definition),
        all_eight_R725_internal_cuts_and_boundary_leaf_ownership_rechecked=True,
        no_individual_interval_transverse_mean_was_removed=True,
        complete_raw_v_jets_identity_sha256=canonical(encode(expected_v_jets)),
        spherical_mean_pass=pass_kind,
        complete_exact_spherical_boundary_source_sha256=SPHERICAL_KERNEL_SHA256,
        integral_enclosure_values_not_recomputed_or_relabelled=True)


PAIRED_MEAN_THEOREM_PATH = "results/R724-paired-halfwave-central-seed-and-complete-source-identity.md"
PAIRED_MEAN_THEOREM_SHA256 = "fea22bde71c3780bead8b7448c5fc057e64f8e6429f97c1b3155e1d13e32f878"
PAIRED_MEAN_THEOREM_BYTES = 25314


def definition():
    return dict(schema=SCHEMA, attribution_schema=ATTRIBUTION_SCHEMA,
        current_input_source_sha256=ACTUAL_INPUT_SHA256,
        current_driver_sha256=ACTUAL_DRIVER_SHA256,
        current_reader_sha256=ACTUAL_READER_SHA256,
        current_normal_sha256=ACTUAL_NORMAL_SHA256,
        current_packet_sha256=ACTUAL_PACKET_SHA256,
        current_seed_sha256=PAIRED_SEED_SOURCE_SHA256,
        current_working_mean_sha256=AUXILIARY_MEAN_SOURCE_SHA256,
        current_Q_sha256=PAIRED_Q_SOURCE_SHA256,
        complete_scientific_source_role_count=ACTUAL_RUNTIME_ROLE_COUNT,
        complete_original_profile_math_source_sha256=PARENT_MATH_SHA256,
        complete_original_integral_utility_source_sha256=PARENT_MEAN_INTEGRAL_SHA256,
        exact_spherical_kernel=dict(name=SPHERICAL_KERNEL_NAME,
            sha256=SPHERICAL_KERNEL_SHA256,bytes=SPHERICAL_KERNEL_BYTES),
        posterior_cap_kernel=dict(name=CAP_KERNEL_NAME,
            sha256=CAP_KERNEL_SHA256,bytes=CAP_KERNEL_BYTES),
        theorem=dict(path=THEOREM_PATH,sha256=THEOREM_SHA256,bytes=THEOREM_BYTES),
        complete_boundary_is_analytic_Slerp=True,
        complete_zero_first_second_angular_graph_is_differentiated=True,
        raw_candidate_v_normalization_uses_all_actual_words=True,
        fixed_seed_H_is_used_in_K_not_current_free_H=True,
        R725_all_eight_internal_boundary_cuts_are_required=True,
        R724_all_six_pieces_in_both_physical_central_intervals_are_required=True,
        complete_twelve_piece_auxiliary_profile_moments_retained=True,
        root_existence_is_local_R727_cap_not_global_chord_convexity=True,
        first_error="M*norm(Lc*saved_v_phi+B_total_phi(v*,saved_v_phi)-K_phi)",
        second_error="M*norm(Lc*saved_v_phiphi+B_total_phiphi(v*,true_v_phi,saved_v_phiphi)-K_phiphi)",
        all_mixed_reference_mean_and_second_mean_terms_included=True,
        M_is_required_only_at_the_certified_true_root=True,
        accurate_root_and_jet_constraints_may_intersect_boxes_only_with_proof=True,
        positive_d_z_is_not_assumed=True,
        projected_radial_frame_has_an_independent_positive_denominator=True,
        R711_exact_A_pi_zero_is_not_a_claim_about_working_endpoint_words=True,
        R709_and_R722_existence_formulas_not_applied=True,
        whole_angle_cap_alone_does_not_certify_adjacent_or_periodic_mean_branch=True,
        no_working_F_J_or_mean_normal_root_is_run=True)


def _load_record(name, record, digest, size, files):
    _record(record)
    if record["sha256"] != digest or record["bytes"] != size:
        raise ValueError("The complete dependency source identity differs: "+name)
    path = Path(files.verify(record)).resolve()
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    files.verify(record)
    if sha(module.__file__) != digest or Path(module.__file__).stat().st_size != size:
        raise ValueError("A complete accurate dependency changed while loading")
    return module


def _candidate_jets(k, working, bits):
    return [[k.Interval(q,q,bits) for q in k.point_vector(working[name])]
            for name in ("v","v_phi","v_phiphi")]


def _positive_lengths(k, seed, result, bits):
    S = k.box(result["angles"][0]["fees"]["accurate_S_enclosure"],bits)
    length = k.exact_relative_lengths(seed,S,bits)
    lc = k.Interval(length["central_lower"],length["central_upper"],bits)
    b = S*Fraction(seed["exact_relative_boundary_total_length"])
    return S,length,lc,b


def _candidate_cosine_lower(leaves):
    values = []
    for leaf in leaves:
        if leaf["description"]["kind"].startswith("boundary"):
            value = leaf.get("spherical_boundary_evaluation",{}).get("reference_candidate_cosine_lower")
            if value is None:
                raise ValueError("Every complete spherical boundary leaf needs its paid reference/candidate dot bound")
            values.append(Fraction(value))
    if not values:
        raise ValueError("Keep all four complete positive boundary layers")
    return min(values)


def _domain(k, cap_module, seed, working, result, leaves, bits, budget_check=None):
    _,_,lc,b = _positive_lengths(k,seed,result,bits)
    cosine = _candidate_cosine_lower(leaves)
    if Fraction(result["complete_boundary_candidate_cosine_lower"]) != cosine:
        raise ValueError("The whole-boundary angle bound must include every complete active boundary leaf")
    return cap_module.posterior_root_domain(k,central_length=lc,boundary_length=b,
        candidate_words=working["v"],
        complete_residual=result["angles"][0]["accurate_total_equation_vector_enclosures"][0],
        reference_candidate_cosine_lower=cosine,bits=bits,budget_check=budget_check)


def true_root_first_residual_jets(k, working, domain, bits):
    candidate = _candidate_jets(k,working,bits)
    return [k.vector_box(domain["bounds"]["accurate_root_vector_enclosure"],bits),
            candidate[1],candidate[2]]


def first_residual_bounds(k, working, domain, first_result, bits):
    M = Fraction(domain["bounds"]["full_raw_v_J_inverse_upper_at_proved_root"])
    residual = k.vector_box(first_result["angles"][0][
        "accurate_total_equation_vector_enclosures"][1],bits)
    error = k.upper_dyadic(M*k.norm_box(residual).hi,bits)
    candidate = _candidate_jets(k,working,bits)
    first = k.centered_vector(k.point_vector(working["v_phi"]),error,bits)
    second_pass = [k.vector_box(domain["bounds"]["accurate_root_vector_enclosure"],bits),
        first,candidate[2]]
    return dict(first_angular_vector_error_upper=error,
        complete_first_equation_residual=residual,
        true_root_and_first_jet_for_second_residual=second_pass)


def _mean_jet_bounds(parent,seed,working,fees,root_domain,first_result,second_result,
                     *,bits=160,taylor_order=48,profile_series_order=48):
    """Direct full E1/E2 at the proved root, followed by original profile arithmetic."""
    require_actions()
    k = parent
    I = k.Interval
    U = lambda value:k.upper_dyadic(value,bits)
    root = root_domain["bounds"]
    rminus = Fraction(root["accurate_root_radius_lower"])
    rplus = Fraction(root["accurate_root_radius_upper"])
    if not 0 < rminus <= rplus < 1:
        raise ValueError("The complete R727 radius must lie strictly between zero and one")
    candidate = [k.point_vector(working[name]) for name in ("v","v_phi","v_phiphi")]
    Ev = Fraction(root["accurate_root_vector_error_upper"])
    first = first_residual_bounds(k,working,root_domain,first_result,bits)
    Ev1 = first["first_angular_vector_error_upper"]
    M = Fraction(root["full_raw_v_J_inverse_upper_at_proved_root"])
    second_residual = k.vector_box(second_result["angles"][0][
        "accurate_total_equation_vector_enclosures"][2],bits)
    Ev2 = U(M*k.norm_box(second_residual).hi)
    vboxes = [k.vector_box(root["accurate_root_vector_enclosure"],bits),
        k.centered_vector(candidate[1],Ev1,bits),k.centered_vector(candidate[2],Ev2,bits)]
    dboxes,rboxes = k.normalized_jets(*vboxes,norm_lower=rminus,norm_upper=rplus)
    dpaid = k.vector_box(root["accurate_root_direction_enclosure"],bits)
    dboxes[0] = [q.intersect(max(Fraction(-1),p.lo),min(Fraction(1),p.hi))
        for q,p in zip(dboxes[0],dpaid)]
    rboxes[1] = k.dot(dboxes[0],vboxes[1])
    rboxes[2] = (k.dot(dboxes[0],vboxes[2])+k.dot(vboxes[1],vboxes[1])/rboxes[0]
        -k.dot(vboxes[0],vboxes[1])**2/rboxes[0]**3)
    ejets = [k.vector_box(fees["accurate_fixed_chart_radial_jets"][name],bits)
        for name in ("e","ep","epp")]
    if fees.get("fixed_chart_e_is_the_accurate_horizontal_unit_radial_vector") is not True:
        raise ValueError("Bind the actual complete fixed horizontal unit radial vector")
    e0,ep,epp = ejets
    d0,dp,dpp = dboxes
    ed = k.dot(e0,d0).intersect(-1,1)
    squared_floor = 1-ed.abs_upper()**2
    if squared_floor <= 0:
        raise PosteriorDomainUnavailable("The complete R727 root cap does not yet pay the projected-radial-frame denominator")
    frame_floor = k.lower_dyadic(k.sqrt_bounds(squared_floor,bits)[0],bits)
    if frame_floor <= 0:
        raise PosteriorDomainUnavailable("The outward projected-radial-frame denominator remains unresolved")
    edp = k.dot(ep,d0)+k.dot(e0,dp)
    edpp = k.dot(epp,d0)+2*k.dot(ep,dp)+k.dot(e0,dpp)
    y0 = k.vsub(e0,k.vscale(d0,ed))
    yp = k.vsub(k.vsub(ep,k.vscale(d0,edp)),k.vscale(dp,ed))
    ypp = k.vsub(k.vsub(k.vsub(epp,k.vscale(d0,edpp)),
        k.vscale(dp,2*edp)),k.vscale(dpp,ed))
    wboxes,_ = k.normalized_jets(y0,yp,ypp,norm_lower=frame_floor,norm_upper=1)
    wboxes[0] = [q.intersect(-1,1) for q in wboxes[0]]
    S = k.box(fees["accurate_S_enclosure"],bits)
    length = k.exact_relative_lengths(seed,S,bits)
    if not 0 < length["profile_delta"] < Fraction(1,8):
        raise ValueError("The complete R711 profile delta changed its exact admissible range")
    lam = [k.word(working[name]) for name in ("lambda","lambda_phi","lambda_phiphi")]
    pi = k.pi_bounds(bits)
    if not 0 < lam[0] < pi.lo:
        raise PosteriorDomainUnavailable("The actual amplitude candidate is not proved inside the complete (0,pi) branch")
    sinhat = k.trig_boxes(I(lam[0],lam[0],bits),taylor_order)[0]
    full_branch_floor = min(sinhat.lo,k.sqrt_bounds(1-rplus*rplus,bits)[0],
        2*rminus*k.sqrt_bounds(1-rminus*rminus,bits)[0])
    amplitude_floor = k.lower_dyadic(full_branch_floor/3,bits)
    if amplitude_floor <= 0:
        raise PosteriorDomainUnavailable("The outward complete R711 profile derivative floor remains unresolved")
    moment_names = ("profile_moment","profile_moment_first_derivative",
                    "profile_moment_second_derivative")
    moment_proof = complete_paired_profile_moment_enclosures(k,seed,working["lambda"],
        bits=bits,series_order=profile_series_order)
    moments = moment_proof["intervals"]
    moment_fees = [max(abs(v.lo-k.word(working[name])),abs(v.hi-k.word(working[name])))
        for v,name in zip(moments,moment_names)]
    moment_proof["actual_working_moment_binary64_hex"] = [working[name] for name in moment_names]
    moment_proof["complete_working_moment_error_upper"] = moment_fees
    moment_proof["external_profile_moment_error_inputs_used"] = False
    El0 = U((moments[0]-rboxes[0]).abs_upper()/amplitude_floor)
    El1 = U(((moments[1]*lam[1]-rboxes[1]).abs_upper()+El0*abs(lam[1]))/amplitude_floor)
    El2 = U(((moments[1]*lam[2]+moments[2]*lam[1]*lam[1]-rboxes[2]).abs_upper()
        +El0*(abs(lam[2])+lam[1]*lam[1])+2*abs(lam[1])*El1+El1*El1)/amplitude_floor)
    lboxes = [I(value-error,value+error,bits) for value,error in zip(lam,(El0,El1,El2))]
    lboxes[0] = lboxes[0].intersect(0,pi.hi)
    intervals = dict(v=vboxes[0],v_phi=vboxes[1],v_phiphi=vboxes[2],
        d=dboxes[0],d_phi=dboxes[1],d_phiphi=dboxes[2],
        w=wboxes[0],w_phi=wboxes[1],w_phiphi=wboxes[2],
        **{"lambda":lboxes[0],"lambda_phi":lboxes[1],"lambda_phiphi":lboxes[2]})
    errors = {name:k.vector_error(intervals[name],working[name],bits) for name in MEAN_VECTOR_KEYS}
    for name in ("lambda","lambda_phi","lambda_phiphi"):
        value = k.word(working[name])
        errors[name] = max(abs(intervals[name].lo-value),abs(intervals[name].hi-value))
    return dict(seed_model_identity_sha256=canonical(seed),
        literal_phi_hex=working["literal_phi_hex"],provider_sha256=k.PROVIDER_SHA,
        intervals=intervals,norm_error_upper=errors,radius_intervals=rboxes,
        accurate_root_radius_range=[rminus,rplus],accurate_root_vertical_lower=None,
        accurate_root_reference_q_upper=Fraction(root["true_root_reference_Slerp_q_upper"]),
        accurate_root_unique_cap=root_domain,
        projected_frame_denominator_lower=frame_floor,
        projected_frame_proof=dict(complete_fixed_e_dot_d=ed,
            exact_squared_denominator_lower=squared_floor,
            positive_norm_lower=frame_floor,
            exact_identity="|e-(e dot d)d|^2=1-(e dot d)^2",
            positive_d_z_assumed=False),
        profile_existence_proof=dict(complete_R711_source_sha256=R711_SHA256,
            full_twelve_piece_exact_A_zero=1,full_twelve_piece_exact_A_pi=0,
            true_mean_radius_strictly_between_zero_and_one=True,
            working_endpoint_moment_was_set_to_zero=False,
            unique_profile_root_in_open_zero_pi=True),
        bounds=dict(vector_error=Ev,first_angular_vector_error=Ev1,
            second_angular_vector_error=Ev2,complete_root_J_inverse_upper=M,
            first_complete_equation_residual=first["complete_first_equation_residual"],
            second_complete_equation_residual=second_residual,
            M_required_only_at_proved_true_root=True,
            amplitude_derivative_lower=amplitude_floor,amplitude_errors=[El0,El1,El2]),
        length_bounds=length,accurate_S_interval=S,
        complete_central_profile_moment_proof=moment_proof,
        central_profile_moment_errors_certified_by_this_module=True,
        precision_bits=bits,taylor_order=taylor_order,profile_series_order=profile_series_order,
        input_fees_certified_by_this_module=False,
        global_reference_mean_branch_certified=False,
        continuous_uniform_field_certificate=False)
def _scope(parent, actual, geometry_identity, phi_interval, working, total_equation,
           exact_partition, active_leaves, structural_reference, *, bits):
    k = parent
    seed = _bind_actual(actual)
    source = _candidate_source(k, actual, working)
    _digest(geometry_identity)
    if (not isinstance(total_equation, dict)
            or not isinstance(total_equation.get("angles"), list)
            or len(total_equation["angles"]) != 1):
        raise ValueError("Use the full one-box accurate total-equation output")
    row = total_equation["angles"][0]
    if (row.get("literal_phi_hex") != working["literal_phi_hex"]
            or total_equation.get("old_R709_or_R722_existence_inherited") is not False):
        raise ValueError("Bind the actual anchor and explicitly separate the new spherical existence proof")
    if (not isinstance(exact_partition, list) or not exact_partition
            or not isinstance(active_leaves, list) or not active_leaves
            or len({leaf["description"]["id"] for leaf in active_leaves}) != len(active_leaves)):
        raise ValueError("Keep every complete original radial integral leaf")
    if (not isinstance(structural_reference, dict)
            or structural_reference.get("structural_unit_and_nonnegative_vertical") is not True
            or structural_reference.get("sampled_norm_or_working_clamp_used_as_proof") is not False):
        raise ValueError("Use the complete actual structural unit-reference proof")
    reference = actual["complete_model"]["base_complete_model"]["complete_axisymmetric_reference_model"]
    if (canonical(reference) != actual["actual_reference_model_identity_sha256"]
            or structural_reference.get("complete_reference_source_sha256") != reference.get("source_sha256")
            or structural_reference.get("actual_complete_model_T0") != reference.get("T0")):
        raise ValueError("The structural unit-reference law is not the actual complete fixed reference")
    phi = k.box(phi_interval, bits)
    if phi.lo > phi.hi:
        raise ValueError("The actual accurate angle interval is empty")
    return dict(schema="actual-R727-whole-angle-spherical-mean-source-scope-v1",
        complete_actual_input_identity=canonical(actual),
        actual_driver_sha256=ACTUAL_DRIVER_SHA256,
        complete_pure_reader_sha256=ACTUAL_READER_SHA256,
        scientific_report=_copy(actual["scientific_report"]),
        actual_snapshot_file=_copy(actual["actual_snapshot_file"]),
        actual_snapshot_identity_sha256=actual["actual_snapshot_identity_sha256"],
        current_full_point_sha256=actual["current_full_point_sha256"],
        complete_model_identity_sha256=actual["model_identity_sha256"],
        exact_fixed_target_identity_sha256=actual["exact_fixed_target_identity_sha256"],
        actual_reference_model_identity_sha256=actual["actual_reference_model_identity_sha256"],
        mathematical_target_identity_sha256=actual["mathematical_target_identity_sha256"],
        fixed_chart_core_sha256=actual["fixed_chart_core_sha256"],
        fixed_scalar_metric_identity_sha256=actual["fixed_scalar_metric_identity_sha256"],
        complete_supported_unit_seed_identity_sha256=k.canonical(seed),
        complete_paired_physical_definition=_copy(seed["paired_halfwave_definition"]),
        paired_physical_definition_identity_sha256=canonical(seed["paired_halfwave_definition"]),
        complete_paired_mean_theorem_sha256=PAIRED_MEAN_THEOREM_SHA256,
        complete_boundary_cutoff_definition=_copy(seed["boundary_cutoff_definition"]),
        boundary_cutoff_definition_identity_sha256=canonical(seed["boundary_cutoff_definition"]),
        complete_boundary_cutoff_theorem_sha256=BOUNDARY_CUTOFF_THEOREM_SHA256,
        accurate_geometry_identity_sha256=geometry_identity,
        accurate_phi_interval=encode(phi_interval),
        candidate_literal_phi_hex=working["literal_phi_hex"],
        complete_actual_candidate_source=_copy(source),
        complete_actual_working_candidate=_copy(working),
        complete_actual_working_candidate_identity_sha256=canonical(working),
        complete_exact_mean_partition_identity_sha256=canonical(encode(exact_partition)),
        complete_active_mean_integral_leaves_identity_sha256=canonical(encode(active_leaves)),
        complete_accurate_total_equation_identity_sha256=canonical(encode(total_equation)),
        complete_structural_reference_proof=_copy(structural_reference),
        complete_spherical_boundary_definition=_copy(seed["spherical_boundary_definition"]),
        spherical_boundary_definition_identity_sha256=canonical(seed["spherical_boundary_definition"]),
        complete_spherical_kernel_sha256=SPHERICAL_KERNEL_SHA256,
        complete_R727_cap_kernel_sha256=CAP_KERNEL_SHA256,
        R709_or_R722_existence_domain_applied=False,
        saved_working_d_and_w_retained_only_as_error_comparison_words=True,
        prepared_inputs_or_mutable_progress_used_as_candidate=False)


def _source_records(records, files):
    expected = dict(
        posterior=(sha(__file__),Path(__file__).stat().st_size),
        spherical=(SPHERICAL_KERNEL_SHA256,SPHERICAL_KERNEL_BYTES),
        cap=(CAP_KERNEL_SHA256,CAP_KERNEL_BYTES),
        R711=(R711_SHA256,R711_BYTES),R713=(R713_SHA256,R713_BYTES),
        R724=(PAIRED_MEAN_THEOREM_SHA256,PAIRED_MEAN_THEOREM_BYTES),
        R725=(BOUNDARY_CUTOFF_THEOREM_SHA256,BOUNDARY_CUTOFF_THEOREM_BYTES),
        R726=(R726_PROOF_SHA256,R726_PROOF_BYTES),
        R727=(THEOREM_SHA256,THEOREM_BYTES))
    if not isinstance(records,dict) or set(records) != set(expected):
        raise ValueError("Keep every complete actual analytic source and complete theorem record")
    for role,(digest,size) in expected.items():
        record = _record(records[role])
        if record["sha256"] != digest or record["bytes"] != size:
            raise ValueError("A complete spherical/R727 source or theorem differs: "+role)
        files.verify(record)
    return records


def _attribution(parent, cap_module, actual, geometry_identity, phi_interval,
        working,total_equation,exact_partition,active_leaves,structural_reference,
        jet_residual_evidence,source_records,*,bits,taylor_order,profile_series_order,
        budget_check=None):
    seed = _bind_actual(actual)
    scope = _scope(parent,actual,geometry_identity,phi_interval,working,total_equation,
        exact_partition,active_leaves,structural_reference,bits=bits)
    if (not isinstance(jet_residual_evidence,dict)
            or set(jet_residual_evidence) != {"first","second"}):
        raise ValueError("Both complete true-root angular residual integration passes are required")
    candidate = _candidate_jets(parent,working,bits)
    arithmetic = dict(candidate=_verify_complete_integral_arithmetic(parent,seed,working,
        total_equation,exact_partition,active_leaves,bits,candidate,"candidate"))
    domain = _domain(parent,cap_module,seed,working,total_equation,active_leaves,bits,budget_check)
    first = jet_residual_evidence["first"]
    second = jet_residual_evidence["second"]
    for pass_value in (first,second):
        if (not isinstance(pass_value,dict)
                or set(pass_value) != {"complete_accurate_total_equation","complete_active_leaves"}
                or pass_value["complete_accurate_total_equation"]["complement_scalar_integral"]
                    != total_equation["complement_scalar_integral"]
                or pass_value["complete_accurate_total_equation"]["angles"][0]["accurate_K_angular_jets"]
                    != total_equation["angles"][0]["accurate_K_angular_jets"]):
            raise ValueError("Both residual passes must retain the entire same fixed-seed K and complement")
        if ([v["description"] for v in pass_value["complete_active_leaves"]]
                != [v["description"] for v in active_leaves]):
            raise ValueError("Each angular residual pass must cover the same complete active radial partition")
    first_jets = true_root_first_residual_jets(parent,working,domain,bits)
    first_total = first["complete_accurate_total_equation"]
    arithmetic["first"] = _verify_complete_integral_arithmetic(parent,seed,working,
        first_total,exact_partition,first["complete_active_leaves"],bits,
        first_jets,"first-root-residual")
    first_bounds = first_residual_bounds(parent,working,domain,first_total,bits)
    second_jets = first_bounds["true_root_and_first_jet_for_second_residual"]
    second_total = second["complete_accurate_total_equation"]
    arithmetic["second"] = _verify_complete_integral_arithmetic(parent,seed,working,
        second_total,exact_partition,second["complete_active_leaves"],bits,
        second_jets,"second-root-residual")
    for pass_value in (first,second):
        for leaf in pass_value["complete_active_leaves"]:
            if leaf["description"]["kind"].startswith("boundary"):
                evidence = leaf["spherical_boundary_evaluation"]
                if (Fraction(evidence["nonantipodal_q_upper"]) != Fraction(
                        domain["bounds"]["true_root_reference_Slerp_q_upper"])
                        or evidence.get("root_cap_domain_identity_sha256") != canonical(domain)):
                    raise ValueError("Every root-residual boundary evaluation uses the same proved cap constraint")
    bounds = _mean_jet_bounds(parent,seed,working,total_equation["angles"][0]["fees"],
        domain,first_total,second_total,bits=bits,taylor_order=taylor_order,
        profile_series_order=profile_series_order)
    scope["complete_jet_residual_evidence_identity_sha256"] = canonical(encode(jet_residual_evidence))
    scope["complete_root_domain_identity_sha256"] = canonical(domain)
    body = dict(schema=ATTRIBUTION_SCHEMA,source_sha256=sha(__file__),
        definition=definition(),source_scope=scope,source_records=_copy(source_records),
        posterior_root_domain=domain,complete_integral_arithmetic=arithmetic,
        complete_accurate_jet_bounds=encode(bounds),
        complete_first_and_second_true_root_residual_integrals_retained=True,
        full_R711_R713_profile_and_independent_projected_frame_proofs_retained=True,
        original_R709_and_R722_conditions_are_not_relabelled=True,
        accurate_whole_angle_local_root_existence_follows_from_complete_source_bound_inputs=True,
        adjacent_or_periodic_reference_mean_branch_certified=False,
        normal_roots_and_physical_surface_completion_certified=False)
    return dict(definition=body,identity_sha256=canonical(body)),bounds


def validate_root_domain_attribution(value,*,parent_math,actual_binding,
        geometry_identity,phi_interval,total_equation,exact_partition,
        active_leaves,structural_reference,jet_residual_evidence,files,bits):
    """Read all original records and recompute local cap and full E1/E2 bounds."""
    require_actions()
    k = bind_parent_math(parent_math)
    if not isinstance(value,dict) or set(value) != {"definition","identity_sha256"}:
        raise ValueError("Use the complete independently attributed R727 root and jets")
    body = value["definition"]
    if canonical(body) != value["identity_sha256"]:
        raise ValueError("The entire spherical root/jet attribution changed")
    records = _source_records(body["source_records"],files)
    cap = _load_record("_read_actual_R727_cap",records["cap"],
        CAP_KERNEL_SHA256,CAP_KERNEL_BYTES,files)
    sphere = _load_record("_read_actual_R726_sphere",records["spherical"],
        SPHERICAL_KERNEL_SHA256,SPHERICAL_KERNEL_BYTES,files)
    if cap.definition() != body["posterior_root_domain"]["definition"]:
        raise ValueError("The complete cap implementation and recorded definition differ")
    if sphere.definition() != body["definition"]["complete_analytic_spherical_definition"]:
        raise ValueError("The complete analytic Slerp definition differs")
    working = body["source_scope"]["complete_actual_working_candidate"]
    verify_saved_candidate(k,actual_binding,working,files)
    supplied = body["complete_accurate_jet_bounds"]
    expected,bounds = _attribution(k,cap,actual_binding,geometry_identity,phi_interval,
        working,total_equation,exact_partition,active_leaves,structural_reference,
        jet_residual_evidence,records,bits=bits,
        taylor_order=supplied["taylor_order"],
        profile_series_order=supplied["profile_series_order"])
    # The entire analytic definition is source-checked, not a caller-chosen flag.
    expected["definition"]["definition"]["complete_analytic_spherical_definition"] = sphere.definition()
    expected["identity_sha256"] = canonical(expected["definition"])
    if canonical(value) != canonical(expected):
        raise ValueError("The entire R727 source, cap, exact integrals or jet arithmetic differs")
    _source_records(records,files)
    return dict(schema=ATTRIBUTION_SCHEMA,identity_sha256=value["identity_sha256"],
        source_sha256=sha(__file__),root_domain_recomputed=True,
        all_three_complete_integral_passes_and_both_jet_bounds_recomputed=True,
        entire_original_candidate_batch_reread=True,
        accurate_root_radius_range=bounds["accurate_root_radius_range"],
        accurate_projected_frame_denominator_lower=bounds["projected_frame_denominator_lower"],
        complete_local_R727_cap=body["posterior_root_domain"],
        old_R709_or_R722_existence_inherited=False,
        adjacent_or_periodic_reference_mean_branch_certified=False,
        complete_whole_circle_or_normal_chain_inferred=False)


class PosteriorMeanKernel:
    """Actual immutable point and source-bound local spherical mean machinery."""

    def __init__(self,actual,parent_math,mean_integrals):
        require_actions()
        if (sha(type(actual).__init__.__code__.co_filename) != ACTUAL_INPUT_SHA256
                or sha(mean_integrals.__file__) != PARENT_MEAN_INTEGRAL_SHA256):
            raise ValueError("Use the complete actual spherical input and unchanged mean integral utilities")
        self.k = bind_parent_math(parent_math)
        self.actual = actual
        self.seed = _bind_actual(actual.binding)
        if (canonical(actual.binding) != actual.identity or self.seed != actual.seed
                or actual.seed_fees is not parent_math
                or actual.seed_identity != self.k.canonical(self.seed)):
            raise ValueError("The complete immutable spherical seed or point binding differs")
        directory = actual.topic/"scripts"/"resume_20261126"
        self.source_records = dict(posterior=actual.used.add(__file__),
            spherical=actual.used.add(directory/SPHERICAL_KERNEL_NAME),
            cap=actual.used.add(directory/CAP_KERNEL_NAME))
        for role,path in (("R711",R711_PATH),("R713",R713_PATH),
                ("R724",PAIRED_MEAN_THEOREM_PATH),("R725",BOUNDARY_CUTOFF_THEOREM_PATH),
                ("R726",R726_PROOF_PATH),("R727",THEOREM_PATH)):
            self.source_records[role] = actual.used.add(actual.topic/path)
        _source_records(self.source_records,actual.used)
        self.cap_module = _load_record("_actual_R727_local_cap",self.source_records["cap"],
            CAP_KERNEL_SHA256,CAP_KERNEL_BYTES,actual.used)
        self.spherical_module = _load_record("_actual_R726_exact_sphere",
            self.source_records["spherical"],SPHERICAL_KERNEL_SHA256,
            SPHERICAL_KERNEL_BYTES,actual.used)
        self.definition = definition()
        self.definition["complete_analytic_spherical_definition"] = self.spherical_module.definition()
        self.definition_identity = canonical(self.definition)
        self.source_record = self.source_records["posterior"]
        self.theorem_record = self.source_records["R727"]
        self.physical_pair_theorem_record = self.source_records["R724"]
        self.boundary_cutoff_theorem_record = self.source_records["R725"]

    def _actual_candidate(self,geometry,working,bits):
        if (geometry.actual is not self.actual or geometry.k is not self.k
                or bits != geometry.bits or canonical(self.actual.binding) != self.actual.identity):
            raise ValueError("Keep the entire current geometry and immutable input")
        angle = working["literal_phi_hex"]
        if angle not in self.actual.seed_rows or working != self.actual.seed_rows[angle]:
            raise ValueError("Use the complete genuinely recorded spherical mean candidate")

    def candidate_domain(self,geometry,working,total_equation,exact_partition,
                         active_leaves,phi_interval,*,bits):
        self._actual_candidate(geometry,working,bits)
        _scope(self.k,self.actual.binding,geometry.identity,phi_interval,working,
            total_equation,exact_partition,active_leaves,geometry.unit_reference_provenance,bits=bits)
        _verify_complete_integral_arithmetic(self.k,self.seed,working,total_equation,
            exact_partition,active_leaves,bits,_candidate_jets(self.k,working,bits),"candidate")
        try:
            return _domain(self.k,self.cap_module,self.seed,working,total_equation,
                active_leaves,bits,geometry.budget.check)
        except self.cap_module.PosteriorCapUnavailable as error:
            raise PosteriorDomainUnavailable(str(error)) from error

    def mean_jet_bounds(self,geometry,working,total_equation,exact_partition,
                        active_leaves,phi_interval,*,jet_residual_evidence,bits=160,
                        taylor_order=48,profile_series_order=48):
        self._actual_candidate(geometry,working,bits)
        try:
            attribution,result = _attribution(self.k,self.cap_module,self.actual.binding,
                geometry.identity,phi_interval,working,total_equation,exact_partition,
                active_leaves,geometry.unit_reference_provenance,jet_residual_evidence,
                self.source_records,bits=bits,taylor_order=taylor_order,
                profile_series_order=profile_series_order,budget_check=geometry.budget.check)
        except self.cap_module.PosteriorCapUnavailable as error:
            raise PosteriorDomainUnavailable(str(error)) from error
        attribution["definition"]["definition"]["complete_analytic_spherical_definition"] = (
            self.spherical_module.definition())
        attribution["identity_sha256"] = canonical(attribution["definition"])
        result["root_domain_attribution"] = attribution
        result["root_domain_source"] = "R727 local symmetric-spherical-boundary posterior cap"
        result["root_domain_source_sha256"] = sha(__file__)
        result["original_R709_coarse_inequalities_assumed_for_existence"] = False
        result["old_R709_or_R722_existence_inherited"] = False
        _source_records(self.source_records,self.actual.used)
        return result

    def metadata(self):
        return dict(schema=SCHEMA,source=self.source_record,
            theorem_source=self.theorem_record,source_records=self.source_records,
            physical_pair_theorem_source=self.physical_pair_theorem_record,
            boundary_cutoff_theorem_source=self.boundary_cutoff_theorem_record,
            spherical_boundary_theorem_source=self.source_records["R726"],
            complete_R711_theorem_source=self.source_records["R711"],
            complete_R713_theorem_source=self.source_records["R713"],
            definition=self.definition,definition_identity_sha256=self.definition_identity,
            actual_input_identity=self.actual.identity,
            original_complete_math_source_sha256=PARENT_MATH_SHA256,
            complete_local_root_and_direct_two_jet_arithmetic_source_explicit=True,
            adjacent_or_periodic_mean_branch_inferred=False,
            whole_circle_normal_or_geometry_completion_inferred=False)
