#!/usr/bin/env python3
"""Strict R726 spherical-boundary input for accurate normal-chain/physical-sixjet work.

This module reads complete existing reports, immutable root packets, every
selected-point angle and every original stage. It never fabricates missing
roots or upgrades a recorded angular order. It unpacks the entire actual
current free point on the unchanged M160/J923 layout; it does not run the
working normal solver or replay a physical field.

Scientific scalar/context and array reads are Actions-only. This complete
input is not itself an accurate root, quadrature or geometry certificate.
"""
from __future__ import annotations

import ast
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

SCHEMA = "actual-fixed-fejer-r726-complete-normal-packet-accurate-field-input-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
SCRIPT_DIRECTORY = "scripts/resume_20261126"
PINS = {
    "reader": ("read_fixed_fejer_r726_dk_cache_report.py", "1aae949feefb2e6bfb457d755aaa6a16412d9b5333344fa351b4ab598287248c"),
    "driver": ("fullclosed_fixed_fejer_r726_dk_cache_qp.py", "58630a875941be3612947e724aa25d9556b903c5ee1c392ff79f8def974e2813"),
    "packets": ("fixed_fejer_r726_root_packets.py", "9da481209cd48d82cb297b213650cc94c4f2148c097602f3495d57ba8f4508fc"),
    "normal": ("fixed_fejer_r726_normal_lift.py", "335ec86217a058b4c1ba982f8ca6f774a139addb8b9f0115ceb4915a1d6842f9"),
    "base": ("fixed_fejer_r726_meridian_operator.py", "bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37"),
    "reference": ("fixed_fejer_axisymmetric_reference.py", "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"),
    "continuous": ("so3_axisymmetric_continuous_integrand.py", "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6"),
    "reference_fees": ("fixed_fejer_reference_seed_angular_profile_error_bounds.py", "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"),
    "mean_integrals": ("fixed_fejer_reference_accurate_mean_residuals.py", "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0"),
    "fixed_input_binding": ("fixed_fejer_reference_input_binding.py", "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"),
    "field_binding": ("fixed_fejer_r726_source_binding.py", "77c4a98d8736f10edcb33e640749033499366e41acbe8b962a0877d304235cfa"),
}
NORMAL_SCHEMA = "complete-fixed-fejer-r726-detached-meridian-normal-layer-v1"
BASE_SCHEMA = "complete-fixed-fejer-r726-so3-meridian-with-core-lift-v1"

REFERENCE_SCHEMA = "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1"
ACTUAL_SOURCE_ROLE_COUNT = 137


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Actual accurate-field input reads require the public Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def copy_json(value):
    return json.loads(json.dumps(value, allow_nan=False))


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def valid_digest(value):
    return (isinstance(value, str) and len(value) == 64
        and all(c in "0123456789abcdef" for c in value))


def array_sha(value):
    import numpy as np
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def load(name, path, digest):
    if sha(path) != digest:
        raise ValueError("The complete bound source differs: "+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(module.__file__) != digest or sha(path) != digest:
        raise ValueError("A complete module changed during source loading")
    return module


def load_source_pins(path):
    tree = ast.parse(Path(path).read_text())
    matches = [node.value for node in tree.body if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "SOURCE_PINS"
                for target in node.targets)]
    if len(matches) != 1:
        raise ValueError("The actual driver must retain its single complete source registry")
    return ast.literal_eval(matches[0])

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


class ActualDataUnavailable(Exception):
    """An actual completed input is absent; no scientific value was supplied."""


class VerifiedFiles:
    def __init__(self):
        self.used = {}

    def verify(self, record):
        if (not isinstance(record, dict) or not isinstance(record.get("path"), str)
                or not valid_digest(record.get("sha256")) or type(record.get("bytes")) is not int
                or record["bytes"] < 0):
            raise ValueError("Keep a complete path, byte count and whole-file identity")
        path = Path(record["path"]).resolve()
        normalized = dict(path=str(path), bytes=record["bytes"], sha256=record["sha256"])
        old = self.used.get(str(path))
        if old is not None and old != normalized:
            raise ValueError("One physical input path was declared with incompatible whole identities")
        actual = file_record(path)
        if actual != normalized:
            raise ValueError("Changed complete actual input: "+str(path))
        self.used[str(path)] = normalized
        return path

    def add(self, path):
        record = file_record(path)
        self.verify(record)
        return record

    def json(self, record):
        path = self.verify(record)
        content = path.read_bytes()
        if len(content) != record["bytes"] or hashlib.sha256(content).hexdigest() != record["sha256"]:
            raise ValueError("The actual JSON snapshot changed during its read")
        result = json.loads(content)
        self.verify(record)
        return result

    def recheck(self):
        for record in tuple(self.used.values()):
            self.verify(record)

    def protect_output(self, directory):
        out = Path(directory).resolve()
        for record in self.used.values():
            source = Path(record["path"])
            if out == source or out in source.parents:
                raise ValueError("Output may not contain or replace any complete consumed source or input")
        return out


def bind_fixed_reference_inputs(raw, entry, module, used):
    """Re-read the complete declared recipe and actual six-file input closure.

    Mathematical recipe, actual generated reference/model, and actual full
    target file have separate identities. None is a future numerical point.
    """
    if (not isinstance(entry, dict)
            or entry.get("schema") != "actual-fixed-fejer-complete-input-entry-binding-v1"
            or raw.get("actual_fixed_reference_input_binding") != entry
            or entry.get("source_sha256") != PINS["field_binding"][1]
            or entry.get("actual_pure_input_binding_source_sha256") != PINS["fixed_input_binding"][1]
            or entry.get("actual_input_producer_source_sha256") != PINS["reference"][1]
            or entry.get("all_six_current_whole_files_reread") is not True):
        raise ValueError("Use the complete source-bound fixed Fejer input entry")
    record = entry.get("actual_binding_file")
    path = used.verify(record)
    payload = used.json(record)
    rebound, checked = module.read_binding(path,
        current_files=entry.get("complete_current_input_files"))
    if (payload != rebound or checked != entry.get("complete_input_validation")
            or checked.get("actual_binding_file") != record
            or checked.get("complete_generated_fixed_chart_verified") is not True
            or checked.get("complete_current_six_files_verified") is not True
            or checked.get("predeclared_deterministic_mathematical_target") is not True):
        raise ValueError("The actual complete fixed-input validation changed")
    target = payload["fixed_target_definition"]
    reference = raw["representation"]["base_complete_model"]["complete_axisymmetric_reference_model"]
    target_identity = canonical(target)
    reference_identity = canonical(reference)
    chart_identity = reference.get("fixed_chart_core_sha256")
    mathematical_identity = canonical(target["mathematical_target_recipe"])
    if (target != raw.get("independent_fixed_target_definition")
            or target_identity != raw.get("independent_fixed_target_definition_identity_sha256")
            or target_identity != entry.get("actual_fixed_target_definition_identity_sha256")
            or target_identity != checked.get("fixed_target_definition_identity_sha256")
            or target.get("complete_current_reference_model") != reference
            or reference.get("schema") != REFERENCE_SCHEMA
            or reference.get("source_sha256") != PINS["reference"][1]
            or reference_identity != entry.get("actual_reference_model_identity_sha256")
            or reference_identity != checked.get("actual_current_model_identity_sha256")
            or chart_identity != entry.get("actual_fixed_chart_core_sha256")
            or chart_identity != checked.get("current_fixed_chart_core_sha256")
            or mathematical_identity != entry.get("mathematical_target_identity_sha256")
            or mathematical_identity != checked.get("mathematical_target_identity_sha256")
            or mathematical_identity != reference.get("mathematical_target_identity_sha256")
            or not all(valid_digest(value) for value in
                (target_identity, reference_identity, chart_identity, mathematical_identity))):
        raise ValueError("Keep the complete recipe, actual reference and target identities distinct and equal to their own definitions")
    files = entry["complete_current_input_files"]
    required = {"current_fixed_input_bundle", "current_node_report",
        "current_scalar_input", "current_reference_bundle", "current_carrier",
        "current_preparation_report"}
    if (not isinstance(files, dict) or set(files) != required
            or files != checked.get("current_input_records")):
        raise ValueError("Retain every complete actual fixed-reference input")
    for value in files.values():
        used.verify(value)
    # These complete records were actually consumed by the fixed-input binder.
    # Do not silently substitute a current checkout path for an original path.
    bound_records = [payload[key] for key in ("fixed_input_preparation_report",
        "fixed_target_definition_file", "new_locations",
        "complete_supplied_location_provenance")]
    for value in bound_records:
        used.verify(value)
    maker_report = used.json(payload["fixed_input_preparation_report"])
    def retain_declared_records(value):
        if isinstance(value, dict):
            if {"path", "bytes", "sha256"} <= set(value):
                used.verify(value)
            for item in value.values():
                retain_declared_records(item)
        elif isinstance(value, list):
            for item in value:
                retain_declared_records(item)
    retain_declared_records(maker_report)
    used.verify(record)
    return dict(entry=copy_json(entry), binding_payload=copy_json(payload),
        exact_fixed_target_identity_sha256=target_identity,
        actual_reference_model_identity_sha256=reference_identity,
        fixed_chart_core_sha256=chart_identity,
        mathematical_target_identity_sha256=mathematical_identity,
        complete_current_input_files=copy_json(files))


class ActualNormalPacketPoint:
    """One genuinely recorded complete point and all its actual angular packets."""

    def __init__(self, args):
        require_actions()
        import numpy as np
        self.np = np
        self.repo = Path(args.repo).resolve()
        self.topic = self.repo/TOPIC
        self.used = VerifiedFiles()
        self.used.add(__file__)
        self.paths = {role: self.topic/SCRIPT_DIRECTORY/name
                      for role, (name, _) in PINS.items()}
        for role, (_, digest) in PINS.items():
            record = self.used.add(self.paths[role])
            if record["sha256"] != digest:
                raise ValueError("The complete source-specific accurate-input role changed: "+role)
        self.reader = load("_normal_fee_fixed_fejer_reader", self.paths["reader"], PINS["reader"][1])
        self.packet_module = load("_normal_fee_actual_packets", self.paths["packets"], PINS["packets"][1])
        self.reference_module = load("_normal_fee_actual_reference", self.paths["reference"], PINS["reference"][1])
        self.continuous_module = load("_normal_fee_exact_scalar", self.paths["continuous"], PINS["continuous"][1])
        self.seed_fees = load("_normal_fee_reference_math", self.paths["reference_fees"], PINS["reference_fees"][1])
        self.fixed_input_module = load("_normal_fee_fixed_fejer_inputs",
            self.paths["fixed_input_binding"], PINS["fixed_input_binding"][1])
        self.report_record = self.used.add(args.report)
        expected_report = getattr(args, "report_sha256", None)
        if expected_report is not None and expected_report != self.report_record["sha256"]:
            raise ValueError("The requested immutable actual report identity differs")
        self.report = raw = self.used.json(self.report_record)
        self.pure = pure = self.reader.read_report(self.repo, self.report_record["path"],
                                                  verify_final_bundle=False)
        if (pure.get("report_sha256") != self.report_record["sha256"]
                or raw.get("source_sha256") != PINS["driver"][1]
                or pure.get("actual_driver_sha256") != PINS["driver"][1]):
            raise ValueError("The actual complete reader and scientific report differ")
        roles = load_source_pins(self.paths["driver"])
        if len(roles) != ACTUAL_SOURCE_ROLE_COUNT or raw.get("source_sha256_by_role") != {k: v[1] for k, v in roles.items()}:
            raise ValueError("Retain every actual complete scientific source role")
        self.runtime_source_records = {}
        for role, (relative, digest) in roles.items():
            record = self.used.add(self.topic/relative)
            if record["sha256"] != digest:
                raise ValueError("Changed full scientific role: "+role)
            self.runtime_source_records[role] = record
        self.fixed_reference_scope = bind_fixed_reference_inputs(raw,
            pure.get("actual_fixed_reference_input_binding"), self.fixed_input_module, self.used)
        self.target_identity = self.fixed_reference_scope["exact_fixed_target_identity_sha256"]
        self.reference_identity = self.fixed_reference_scope["actual_reference_model_identity_sha256"]
        self.fixed_chart_identity = self.fixed_reference_scope["fixed_chart_core_sha256"]
        self.mathematical_target_identity = self.fixed_reference_scope["mathematical_target_identity_sha256"]
        self.model = copy_json(raw["representation"])
        self.model_identity = canonical(self.model)
        self.base_model = self.model["base_complete_model"]
        self.reference_model = self.base_model["complete_axisymmetric_reference_model"]
        self.seed = copy_json(raw["supported_unit_seed_definition"])
        self.seed_identity = canonical(self.seed)
        if (self.model_identity != raw["model_identity_sha256"]
                or self.model.get("schema") != NORMAL_SCHEMA
                or self.model.get("source_sha256") != PINS["normal"][1]
                or self.base_model.get("schema") != BASE_SCHEMA
                or self.base_model.get("source_sha256") != PINS["base"][1]
                or canonical(self.base_model) != self.model.get("base_model_identity_sha256")
                or canonical(self.reference_model) != self.reference_identity
                or self.reference_model.get("fixed_chart_core_sha256") != self.fixed_chart_identity
                or self.seed_identity != raw.get("supported_unit_seed_identity_sha256")
                or self.base_model.get("fixed_supported_unit_seed_model") != self.seed
                or raw.get("independent_fixed_target_definition_identity_sha256") != self.target_identity):
            raise ValueError("Bind the complete same-point normal/base/frozen-reference/target chain")
        if (raw.get("M") != 160 or raw.get("J") != 923 or raw.get("N") != 2048
                or self.model.get("implicit_control_dimension") != 6
                or self.model.get("normal_increment_dimension") != 3
                or self.model.get("normal_stage_count") != 32):
            raise ValueError("This actual producer retains the complete original fixed Fejer layout and 32 stages")
        if (roles["seed_reference"][1] != PAIRED_SEED_SOURCE_SHA256
                or roles["seed_mean"][1] != AUXILIARY_MEAN_SOURCE_SHA256
                or roles["new_moment_input"][1] != PAIRED_Q_SOURCE_SHA256):
            raise ValueError("The current full scientific sources do not define this physical halfwave pair")
        self.physical_profile_definition = paired_halfwave_seed_scope(
            self.seed,self.base_model,self.model)
        self.physical_profile_identity = canonical(self.physical_profile_definition)
        self.spherical_boundary_definition = spherical_seed_scope(self.seed)
        self.spherical_boundary_identity = canonical(self.spherical_boundary_definition)
        self.spherical_theorem_record = self.used.add(self.topic/R726_PROOF_PATH)
        if (self.spherical_theorem_record["sha256"] != R726_PROOF_SHA256
                or self.spherical_theorem_record["bytes"] != R726_PROOF_BYTES):
            raise ValueError("The complete actual R726 spherical-boundary theorem differs")
        self.boundary_cutoff_definition = boundary_cutoff_seed_scope(self.seed)
        self.boundary_cutoff_identity = canonical(self.boundary_cutoff_definition)
        self.boundary_cutoff_theorem_record = self.used.add(self.topic/BOUNDARY_CUTOFF_THEOREM_PATH)
        if (self.boundary_cutoff_theorem_record["sha256"] != BOUNDARY_CUTOFF_THEOREM_SHA256
                or self.boundary_cutoff_theorem_record["bytes"] != BOUNDARY_CUTOFF_THEOREM_BYTES):
            raise ValueError("The complete R725 boundary-cutoff theorem source differs")
        self.partition = [F(v) for v in self.model["exact_normal_step_nodes"]]
        if (len(self.partition) != 33 or self.partition[0] != 0 or self.partition[-1] != 1
                or any(a >= b for a, b in zip(self.partition, self.partition[1:]))):
            raise ValueError("The exact complete common normal partition changed")
        self.packet_module.validate_entry_report(raw, reread_packets=True, reread_arrays=True)
        metadata = raw["normal_root_packets"]
        snapshots = metadata["snapshots"]
        selected_identity = getattr(args, "snapshot_identity_sha256", None)
        if selected_identity is not None:
            matches = [item for item in snapshots if item["snapshot_identity_sha256"] == selected_identity]
            if len(matches) != 1:
                raise ActualDataUnavailable("The explicitly requested actual immutable snapshot is absent")
            selected = matches[0]
        else:
            complete = [item for item in snapshots
                if item["summary"].get("all_required_angle_roots_recorded") is True
                and item["summary"].get("current_full_point_sha256") is not None]
            if not complete:
                raise ActualDataUnavailable("No actual point has all required complete normal angle roots")
            selected = complete[-1]
        self.snapshot_record = copy_json(selected["snapshot_file"])
        self.snapshot = self.used.json(self.snapshot_record)
        summary = self.packet_module.validate_snapshot(self.snapshot, model=self.model,
            operator_source_sha256=PINS["normal"][1], caller_source_sha256=PINS["driver"][1],
            reread_packets=True, reread_arrays=True)
        if summary != selected["summary"]:
            raise ValueError("The complete selected immutable snapshot changed")
        d = self.snapshot["definition"]
        if d.get("all_required_angle_roots_recorded") is not True:
            raise ActualDataUnavailable("The selected actual point lacks original required angle roots")
        self.point_sha256 = d["current_full_point_sha256"]
        self.required_angles = tuple(d["required_literal_angle_hex"])
        self.angles = tuple(d["cache_literal_angle_hex"])
        self.angle_records = {item["literal_angle_hex"]: copy_json(item) for item in d["angle_packets"]}
        if (len(self.angle_records) != len(self.angles)
                or not set(self.required_angles) <= set(self.angles)):
            raise ValueError("No original actual required or cached angle may be dropped")
        self.point_record = copy_json(d["current_point_file"])
        self.x = self._read_npz(self.point_record["arrays_file"],
                               [self.point_record["array"]])["x"]
        if array_sha(self.x) != self.point_sha256:
            raise ValueError("The full selected current free-point words differ")
        self.carrier_record = copy_json(metadata["fixed_working_carrier"])
        self.carrier = self._read_npz(self.carrier_record["arrays_file"],
                                     self.carrier_record["arrays"])
        self.operator_metadata_record = copy_json(d["operator_metadata_snapshot"])
        self.operator_metadata = self.used.json(self.operator_metadata_record)
        self.calibration_records = copy_json(d["actual_reference_calibration_files"])
        for record in self.calibration_records:
            self.used.verify(record["immutable_copy"])
        current = self.fixed_reference_scope["entry"]
        if (current.get("actual_fixed_target_definition_identity_sha256") != self.target_identity
                or current.get("actual_reference_model_identity_sha256") != self.reference_identity
                or current.get("actual_fixed_chart_core_sha256") != self.fixed_chart_identity):
            raise ValueError("The actual six-file fixed Fejer input contract differs")
        self.input_records = copy_json(current["complete_current_input_files"])
        for record in self.input_records.values():
            self.used.verify(record)
        self.used.verify(current["actual_binding_file"])
        keys = dict(reference_bundle="current_reference_bundle", carrier="current_carrier",
            node_report="current_node_report", scalar_input="current_scalar_input",
            preparation_report="current_preparation_report")
        context_args = {k: self.input_records[v]["path"] for k, v in keys.items()}
        if type(args.panels) is not int or args.panels < 1:
            raise ValueError("Use an explicit positive complete scalar enclosure panel count")
        self.context = self.reference_module.AxisymmetricReferenceContext.from_files(
            repo=self.repo, panels=args.panels, **context_args)
        if (self.context.model != self.reference_model or self.context.identity != self.reference_identity
                or self.context.scalar_definition != self.base_model["fixed_scalar_profile_definition"]
                or self.context.scalar_identity != self.base_model["fixed_scalar_metric_identity_sha256"]):
            raise ValueError("The whole accurate scalar/chart context changed the actual frozen target")
        self.M, self.J, self.n, self.K = 160, 923, 482, 3
        free_rows = np.array([i for i in range(3*self.J)
            if i not in (0, 3*(self.J-1), 3*(self.J-1)+1)], dtype=np.int64)
        core_count = self.M-self.K
        expected_size = core_count+len(free_rows)*self.n+1
        if (self.x.shape != (expected_size,) or raw.get("original_variables") != expected_size
                or self.x.dtype != np.dtype("float64") or not np.isfinite(self.x).all()):
            raise ValueError("Use the complete actual full current point on the unchanged source layout")
        # Exact literal unpack of the complete bound base's public layout.
        self.core = np.concatenate((self.context.core[:3], self.x[:core_count]))
        omega = np.zeros((3*self.J, self.n), dtype=np.float64)
        omega[free_rows] = self.x[core_count:-1].reshape(len(free_rows), self.n)
        self.omega = omega.reshape(self.J, 3, self.n)
        self.height = float(self.x[-1])
        self.initial_point = np.concatenate((self.context.core[3:],
            np.zeros(len(free_rows)*self.n, dtype=np.float64),
            np.array([float.fromhex(self.seed["initial_height_hex"])], dtype=np.float64)))
        self.reference_point_sha256 = array_sha(self.initial_point)
        if self.reference_point_sha256 != self.model["reference_centering_definition"]["original_reference_point_sha256"]:
            raise ValueError("The entire frozen original point was not recovered exactly")
        for array in (self.x, self.core, self.omega, self.initial_point):
            array.setflags(write=False)
        self.scalar = self.continuous_module.ScalarWholeInterval(self)
        self.seed_rows, self.seed_row_sources = self._read_complete_seed_candidates(pure)
        if any(angle not in self.seed_rows for angle in self.angles):
            raise ActualDataUnavailable("A recorded normal angle lacks a genuinely returned fixed-reference mean candidate")
        self._packet_cache = {}
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            scientific_report=self.report_record, complete_pure_reader_sha256=PINS["reader"][1],
            actual_driver_sha256=PINS["driver"][1], actual_source_commit=raw["source_commit"],
            actual_run_id=raw.get("github_run_id"), model_identity_sha256=self.model_identity,
            complete_model=self.model, exact_fixed_target_identity_sha256=self.target_identity,
            actual_reference_model_identity_sha256=self.reference_identity,
            fixed_chart_core_sha256=self.fixed_chart_identity,
            mathematical_target_identity_sha256=self.mathematical_target_identity,
            complete_actual_fixed_reference_input_binding=copy_json(current),
            fixed_scalar_metric_identity_sha256=self.context.scalar_identity,
            actual_snapshot_identity_sha256=self.snapshot["snapshot_identity_sha256"],
            actual_snapshot_file=self.snapshot_record, current_full_point_sha256=self.point_sha256,
            current_point_arrays_file=self.point_record["arrays_file"],
            exact_common_normal_partition=[str(v) for v in self.partition],
            full_stage_count=32, complete_required_literal_angles=list(self.required_angles),
            complete_cached_literal_angles=list(self.angles),
            all_cached_angles_retained=True, current_point_is_original_reference=bool(np.array_equal(self.x,self.initial_point)),
            actual_original_reference_point_sha256=self.reference_point_sha256,
            actual_packet_matrix_orders_are_not_upgraded=True,
            existing_calibration_files=self.calibration_records,
            complete_actual_working_carrier=self.carrier_record,
            complete_six_actual_inputs=self.input_records,
            original_current_core_sha256=array_sha(self.core),
            original_current_omega_sha256=array_sha(self.omega),
            original_current_H_hex=self.height.hex(),
            complete_actual_seed_candidate_sources=self.seed_row_sources,
            complete_spherical_boundary_definition=self.spherical_boundary_definition,
            spherical_boundary_definition_identity_sha256=self.spherical_boundary_identity,
            spherical_boundary_theorem_source=self.spherical_theorem_record,
            accurate_spherical_mean_root_or_R727_domain_paid_here=False,
            old_R709_or_R722_chord_existence_inherited=False,
            complete_paired_halfwave_physical_definition=self.physical_profile_definition,
            paired_halfwave_physical_definition_identity_sha256=self.physical_profile_identity,
            complete_boundary_cutoff_definition=self.boundary_cutoff_definition,
            boundary_cutoff_definition_identity_sha256=self.boundary_cutoff_identity,
            boundary_cutoff_theorem_source=self.boundary_cutoff_theorem_record,
            complete_physical_boundary_piece_count=12,
            complete_internal_boundary_cut_count=8,
            original_boundary_mean_or_quadrature_words_inherited=False,
            physical_profile_piece_count_per_central_interval=6,
            complete_physical_pair_piece_count=12,
            auxiliary_mean_profile_piece_count=12,
            combined_central_mean_uses_R724_pair_identity=True,
            per_interval_transverse_mean_assumed_zero=False,
            source_sha256_by_role={role: value[1] for role,value in PINS.items()},
            full_scientific_runtime_source_records=self.runtime_source_records,
            no_new_working_field_J_or_normal_root_evaluation=True,
            accurate_scalar_context_may_be_evaluated=True,
            accepted_outer_point_not_inferred_from_cache=True,
            literal_node_coverage_is_not_whole_angle_coverage=True,
            reference_root_or_normal_root_or_physical_sixjet_fee_paid_here=False)
        self.identity = canonical(self.binding)
        self.used.recheck()

    def _read_npz(self, record, descriptors):
        require_actions()
        np = self.np
        path = self.used.verify(record)
        expected = {d["name"]: d for d in descriptors}
        if len(expected) != len(descriptors):
            raise ValueError("Duplicate immutable array name")
        self.packet_module.validate_arrays_file(record, descriptors)
        with np.load(path, allow_pickle=False) as data:
            if set(data.files) != set(expected):
                raise ValueError("Keep every complete declared immutable array, without extras")
            result = {}
            for name, d in expected.items():
                a = np.array(data[name], copy=True)
                if (list(a.shape) != d["shape"] or str(a.dtype) != d["dtype"]
                        or array_sha(a) != d["array_sha256"]
                        or (a.dtype.kind == "f" and not np.isfinite(a).all())):
                    raise ValueError("An immutable actual array changed: "+name)
                a.setflags(write=False)
                result[name] = a
        self.used.verify(record)
        return result

    def _read_complete_seed_candidates(self, pure):
        require_actions()
        np = self.np
        latest = self.report.get("latest_operator_metadata", {})
        seed_meta = latest.get("base_complete_metadata", {}).get("fixed_supported_unit_seed")
        if not isinstance(seed_meta, dict) or pure.get("seed_diagnostics") is None:
            raise ActualDataUnavailable("No actual completed fixed-reference mean batches exist")
        records = seed_meta.get("mean_batch_records")
        if records != pure["seed_diagnostics"].get("mean_batch_records"):
            raise ValueError("The complete pure and actual fixed-reference batch lists differ")
        rows, provenance = {}, []
        vector_keys = self.seed_fees.MEAN_VECTOR_KEYS
        scalar_keys = self.seed_fees.MEAN_SCALAR_KEYS
        for index, batch in enumerate(records):
            record = batch["runner_raw_arrays"]
            path = self.used.verify(record)
            angles = batch["literal_angle_hex"]
            with np.load(path, allow_pickle=False) as data:
                if (str(data["seed_model_identity"].item()) != self.seed_identity
                        or [float(v).hex() for v in data["phi"]] != angles):
                    raise ValueError("An actual complete mean batch changed seed or angle order")
                arrays = {}
                for name in vector_keys+scalar_keys:
                    a = np.array(data[name], copy=True)
                    expected = (len(angles), 3) if name in vector_keys else (len(angles),)
                    if (a.shape != expected or a.dtype.kind != "f" or a.dtype.itemsize != 8
                            or not np.isfinite(a).all()):
                        raise ValueError("A full actual fixed-reference candidate array is missing")
                    arrays[name] = a
            self.used.verify(record)
            source = dict(actual_completed_batch_index=index, runner_raw_arrays=copy_json(record),
                literal_angle_hex=list(angles), complete_original_batch_metadata=copy_json(batch))
            provenance.append(source)
            for i, angle in enumerate(angles):
                if angle in rows:
                    raise ValueError("The original fixed-reference provider records each missing literal angle once")
                candidate = dict(literal_phi_hex=angle)
                for name in vector_keys:
                    candidate[name] = [float(v).hex() for v in arrays[name][i]]
                for name in scalar_keys:
                    candidate[name] = float(arrays[name][i]).hex()
                candidate["actual_completed_batch_index"] = index
                candidate["actual_raw_batch_sha256"] = record["sha256"]
                rows[angle] = candidate
        return rows, provenance

    def packet(self, angle):
        require_actions()
        if angle not in self.angle_records:
            raise ValueError("Use an actually recorded literal angle; do not synthesize a root")
        if angle in self._packet_cache:
            return self._packet_cache[angle]
        item = self.angle_records[angle]
        packet = self.used.json(item["packet_file"])
        summary = self.packet_module.validate_packet(packet, model=self.model,
            operator_source_sha256=PINS["normal"][1], caller_source_sha256=PINS["driver"][1],
            point_sha256=self.point_sha256, angle_hex=angle, reread_arrays=True)
        if summary["packet_identity_sha256"] != item["packet_identity_sha256"]:
            raise ValueError("The actual angle packet changed after snapshot binding")
        arrays = self._read_npz(packet["arrays_file"], packet["definition"]["arrays"])
        result = dict(packet=packet, arrays=arrays, actual_summary=summary,
            original_packet_file=copy_json(item["packet_file"]))
        self._packet_cache[angle] = result
        return result

    def recheck(self):
        rebound = bind_fixed_reference_inputs(self.report,
            self.fixed_reference_scope["entry"], self.fixed_input_module, self.used)
        if rebound != self.fixed_reference_scope:
            raise ValueError("The full fixed-reference input changed during accurate field work")
        self.used.recheck()
        physical = paired_halfwave_seed_scope(self.seed,self.base_model,self.model)
        if (physical != self.physical_profile_definition
                or canonical(physical) != self.physical_profile_identity):
            raise ValueError("The complete paired physical profile changed during accurate work")
        boundary = boundary_cutoff_seed_scope(self.seed)
        if (boundary != self.boundary_cutoff_definition
                or canonical(boundary) != self.boundary_cutoff_identity):
            raise ValueError("The complete R725 boundary law changed during accurate work")
        self.used.verify(self.boundary_cutoff_theorem_record)
        spherical = spherical_seed_scope(self.seed)
        if (spherical != self.spherical_boundary_definition
                or canonical(spherical) != self.spherical_boundary_identity):
            raise ValueError("The complete R726 spherical boundary changed during accurate work")
        self.used.verify(self.spherical_theorem_record)
        if self.point_sha256 != array_sha(self.x):
            raise ValueError("The selected entire current point was modified")
        return True

    def metadata(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__), binding=self.binding,
            binding_identity_sha256=self.identity, actual_angle_packets_read=len(self._packet_cache),
            all_required_angle_count=len(self.required_angles), all_cached_angle_count=len(self.angles),
            all_original_stages_per_angle=32, physical_F_J_root_reads=0,
            exact_field_or_geometry_certified=False)
