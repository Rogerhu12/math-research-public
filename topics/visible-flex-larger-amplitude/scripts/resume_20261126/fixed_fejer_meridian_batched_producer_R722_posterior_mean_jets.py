#!/usr/bin/env python3
"""Complete R722 posterior mean-root domain and unchanged R710/R711 jet arithmetic.

This independent library is consumed by the source-pinned whole-angle radial
producer for the actual meridian-batched field. It has no literal-batch CLI and
does not change the original R709 source or any R709 hypothesis flag.
All accurate arithmetic and immutable numerical-array reads run in public
repository Actions only. No working F, Jacobian, mean root or normal root is
evaluated here. The complete original 0471 mathematical module is shared.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path

SCHEMA = "actual-fixed-fejer-meridian-batched-R722-posterior-mean-jets-v1"
DOMAIN_SCHEMA = "complete-R722-posterior-convex-mean-root-domain-v1"
ATTRIBUTION_SCHEMA = "actual-whole-angle-R722-mean-root-domain-attribution-v1"
PARENT_MATH_SHA256 = "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"
PARENT_MEAN_INTEGRAL_SHA256 = "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0"
ACTUAL_INPUT_SHA256 = "d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7"
ACTUAL_INPUT_SCHEMA = "actual-fixed-fejer-meridian-batched-complete-normal-packet-accurate-field-input-v1"
ACTUAL_DRIVER_SHA256 = "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"
ACTUAL_READER_SHA256 = "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49"
ACTUAL_NORMAL_SHA256 = "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d"
ACTUAL_PACKET_SHA256 = "c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4"
ACTUAL_RUNTIME_ROLE_COUNT = 137
PROVIDER_SHA256 = "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a"
THEOREM_PATH = "results/R722-posterior-convex-mean-root-existence.md"
THEOREM_SHA256 = "b74d5caf7a0e8185e4f82b76e9db6bfc9f736262c16ed62c1d688ef8e7f78721"
THEOREM_BYTES = 25682
PARENT_MEAN_FUNCTION_SHA256 = "e0e233134abb87feb740652810e89d8472588ef162206021a3f04461ea05791f"
RETAINED_COMPLETE_JET_SUFFIX_SHA256 = "4fc958af144bbd27f5c1745fe7d9bd2db86b2ff9aad4ef245b462847aac38db2"
MEAN_VECTOR_KEYS = ("v", "v_phi", "v_phiphi", "d", "d_phi", "d_phiphi",
                    "w", "w_phi", "w_phiphi")
MEAN_SCALAR_KEYS = ("lambda", "lambda_phi", "lambda_phiphi",
    "profile_moment", "profile_moment_first_derivative",
    "profile_moment_second_derivative")


class PosteriorDomainUnavailable(ArithmeticError):
    """The exact posterior sufficient inequalities remain unpaid."""


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("R722 actual posterior fees require public repository Actions")


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


def definition():
    return dict(schema=SCHEMA, root_domain_schema=DOMAIN_SCHEMA,
        attribution_schema=ATTRIBUTION_SCHEMA,
        complete_original_math_source_sha256=PARENT_MATH_SHA256,
        complete_original_integral_source_sha256=PARENT_MEAN_INTEGRAL_SHA256,
        original_mean_function_sha256=PARENT_MEAN_FUNCTION_SHA256,
        retained_complete_jet_suffix_sha256=RETAINED_COMPLETE_JET_SUFFIX_SHA256,
        posterior_theorem=dict(path=THEOREM_PATH, bytes=THEOREM_BYTES,
            sha256=THEOREM_SHA256),
        current_accurate_input_source_sha256=ACTUAL_INPUT_SHA256,
        current_driver_sha256=ACTUAL_DRIVER_SHA256,
        current_reader_sha256=ACTUAL_READER_SHA256,
        current_normal_sha256=ACTUAL_NORMAL_SHA256,
        current_packet_sha256=ACTUAL_PACKET_SHA256,
        complete_runtime_source_role_count=ACTUAL_RUNTIME_ROLE_COUNT,
        exact_candidate_radius_is_recomputed_from_all_three_v_words=True,
        saved_working_d_is_not_an_accurate_unit_direction=True,
        all_three_complete_total_equation_residuals_retained=True,
        complete_R710_two_angle_jet_and_R711_twelve_piece_arithmetic_retained=True,
        original_R709_coarse_hypothesis_flags_not_modified=True,
        literal_batch_CLI_not_added_or_rebound=True,
        whole_angle_scope_must_be_bound_by_the_actual_radial_producer=True,
        complete_active_integral_leaf_cover_and_all_three_residual_sums_rechecked=True,
        no_new_working_F_J_mean_or_normal_root_evaluations=True,
        numerical_or_geometric_success_prepopulated=False)


def bind_parent_math(parent):
    source_path = Path(parent.__file__).resolve()
    if (sha(source_path) != PARENT_MATH_SHA256
            or parent.PROVIDER_SHA != PROVIDER_SHA256
            or tuple(parent.MEAN_VECTOR_KEYS) != MEAN_VECTOR_KEYS
            or tuple(parent.MEAN_SCALAR_KEYS) != MEAN_SCALAR_KEYS):
        raise ValueError("Use the complete unchanged original mathematical module")
    names = (
        "upper_dyadic", "box", "exact_relative_lengths", "fraction",
        "point_vector", "point_norm", "cap_floor", "nonnegative",
        "centered_vector", "normalized_jets", "dot", "vector_box", "vsub",
        "vscale", "pi_bounds", "word", "trig_boxes", "sqrt_bounds",
        "lower_dyadic", "complete_profile_moment_enclosures", "vector_error",
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


def posterior_root_domain(parent, seed, working, fees, *, bits=160):
    """Evaluate only R722(38)-(42), with directed finite-size rational outputs."""
    require_actions()
    k = bind_parent_math(parent)
    if type(bits) is not int or not 64 <= bits <= 1024:
        raise ValueError("Use the actual declared complete outward precision")
    if fees.get("accurate_reference_unit_and_nonnegative_vertical_on_complete_boundary") is not True:
        raise ValueError("The complete structural reference assumptions are missing")
    U = lambda x: k.upper_dyadic(x, bits)
    D = lambda x: k.lower_dyadic(x, bits)
    S = k.box(fees["accurate_S_enclosure"], bits)
    length = k.exact_relative_lengths(seed, S, bits)
    lc, lcu = length["central_lower"], length["central_upper"]
    b = length["boundary_upper"]
    if not 0 < lc <= lcu or b < 0:
        raise ValueError("Keep positive accurate central lengths and every boundary layer")
    v = k.point_vector(working["v"])
    if len(v) != 3:
        raise ValueError("Use the complete three-dimensional actual mean candidate")
    rlo, rhi = k.point_norm(v, bits)
    if rlo <= 0 or v[2] <= 0:
        raise PosteriorDomainUnavailable("The actual exact candidate has no resolved positive normalization chart")
    residuals = [k.nonnegative(x, "complete accurate total-equation residual")
                 for x in fees["accurate_centered_total_equation_residual_norms"]]
    if len(residuals) != 3:
        raise ValueError("Keep all zero, first and second complete total-equation residual bounds")
    E0 = residuals[0]
    zhat = D(v[2]/rhi)
    amin, amax = D(lc*rlo), U(lcu*rhi)
    if amin <= 0:
        raise PosteriorDomainUnavailable("The candidate multiplier lower bound is unresolved")
    eta0 = U(2*E0/amin)
    zeta = D(zhat-eta0)
    if zeta <= 0:
        raise PosteriorDomainUnavailable("R722 cannot yet place every convex minimum in a positive cap")
    LB = U(b/zeta)
    delta = U(E0+LB*eta0)
    alpha_lo, alpha_hi = D(amin-delta), U(amax+delta)
    if alpha_lo <= 0 or alpha_hi >= lc:
        raise PosteriorDomainUnavailable("R722 positive multiplier or strictly subunit mean length remains unpaid")
    rminus, rplus = D(alpha_lo/lcu), U(alpha_hi/lc)
    if not 0 < rminus <= rplus < 1:
        raise PosteriorDomainUnavailable("Finite outward precision does not resolve the strict posterior root interval")
    eta1 = U(2*E0/(amin+alpha_lo))
    vector_error = U((E0+LB*eta1)/lc)
    inverse = U((1+LB/(lc*rminus))/lc)
    return encode(dict(schema=DOMAIN_SCHEMA, theorem_sha256=THEOREM_SHA256,
        precision_bits=bits, seed_model_identity_sha256=k.canonical(seed),
        candidate_literal_phi_hex=working["literal_phi_hex"],
        accurate_candidate_v=[str(q) for q in v],
        accurate_S_enclosure=S, complete_exact_length_bounds=length,
        complete_total_equation_residual_norms=residuals,
        bounds=dict(accurate_central_length_lower=lc,
            accurate_central_length_upper=lcu, complete_boundary_measure_upper=b,
            candidate_radius_lower=rlo, candidate_radius_upper=rhi,
            candidate_direction_vertical_lower=zhat,
            candidate_multiplier_lower=amin, candidate_multiplier_upper=amax,
            all_convex_minima_distance_upper=eta0,
            common_cap_vertical_lower=zeta, complete_boundary_D_B_norm_upper=LB,
            multiplier_error_upper=delta,
            accurate_root_multiplier_lower=alpha_lo,
            accurate_root_multiplier_upper=alpha_hi,
            accurate_root_radius_lower=rminus, accurate_root_radius_upper=rplus,
            accurate_root_direction_vertical_lower=zeta,
            posterior_direction_error_upper=eta1,
            posterior_vector_error_upper=vector_error,
            complete_nonsymmetric_J_inverse_upper=inverse),
        sufficient_inequalities=dict(positive_cap=True, strictly_positive_multiplier=True,
            strictly_subunit_accurate_root=True),
        every_closed_unit_ball_minimum_localized_before_using_its_gradient=True,
        positive_multiplier_supplies_uniqueness_without_global_strict_convexity=True,
        original_R709_coarse_K_bounds_used_for_existence=False,
        full_angle_or_surface_completion_inferred=False,
        accurate_residual_and_structural_inputs_certified_by_this_arithmetic_module=False))


def _bind_actual(actual):
    if (not isinstance(actual, dict) or actual.get("schema") != ACTUAL_INPUT_SCHEMA
            or actual.get("source_sha256") != ACTUAL_INPUT_SHA256
            or actual.get("actual_driver_sha256") != ACTUAL_DRIVER_SHA256
            or actual.get("complete_pure_reader_sha256") != ACTUAL_READER_SHA256):
        raise ValueError("R722 actual attribution requires the complete meridian-batched input")
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
    return model["base_complete_model"]["fixed_supported_unit_seed_model"]


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
            or type(row.get("all_pointwise_R709_sufficient_inequalities_proved")) is not bool):
        raise ValueError("Retain the actual anchor and the original true-or-false coarse R709 result")
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
    return dict(schema="actual-R722-whole-angle-mean-source-scope-v1",
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
        original_R709_coarse_inequalities_proved=row[
            "all_pointwise_R709_sufficient_inequalities_proved"],
        saved_working_d_and_w_retained_only_as_error_comparison_words=True,
        prepared_inputs_or_mutable_progress_used_as_candidate=False)


def _verify_complete_integral_arithmetic(parent, seed, working, result, plan, leaves, bits):
    """Recheck full binary leaf coverage and all already-computed integral sums."""
    k = parent
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
                    or item.get("centrally_integrated_by_exact_Lc_v") is not (kind == "central")
                    or pair(item["left"]) != start):
                raise ValueError("The entire original exact mean partition changed")
            positive_width(item["left"], item["right"])
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
    for order, name in enumerate(("v", "v_phi", "v_phiphi")):
        v = [k.Interval(q, q, bits) for q in k.point_vector(working[name])]
        total = k.vsub(k.vadd(k.vscale(v, Lc), exact_boundary[0][order]),
                      k.vector_box(K[order], bits))
        if encode(total) != residuals[order]:
            raise ValueError("The accurate total residual omits an exact Lc*v, boundary or K term")
    return dict(complete_noncentral_binary_cover_rechecked=True,
        complete_radial_plan_count=len(plan), complete_active_integral_leaf_count=len(leaves),
        exact_boundary_and_complement_endpoint_sums_rechecked=True,
        all_three_full_total_equation_vector_sums_rechecked=True,
        integral_enclosure_values_not_recomputed_or_relabelled=True)


def _attribution(parent, actual, geometry_identity, phi_interval, working, total_equation,
                 exact_partition, active_leaves, structural_reference, *, bits):
    seed = _bind_actual(actual)
    scope = _scope(parent, actual, geometry_identity, phi_interval, working,
        total_equation, exact_partition, active_leaves, structural_reference, bits=bits)
    row = total_equation["angles"][0]
    integral_arithmetic = _verify_complete_integral_arithmetic(parent, seed, working,
        total_equation, exact_partition, active_leaves, bits)
    fees = row["fees"]
    residuals = row["accurate_total_equation_vector_enclosures"]
    if len(residuals) != 3:
        raise ValueError("Keep all three complete accurate vector residuals")
    supplied = fees["accurate_centered_total_equation_residual_norms"]
    if len(supplied) != 3:
        raise ValueError("Keep all three complete accurate residual norm bounds")
    for vector, upper in zip(residuals, supplied):
        actual_upper = parent.norm_box(parent.vector_box(vector, bits)).hi
        if parent.nonnegative(upper, "complete residual") < actual_upper:
            raise ValueError("The supplied residual norm omits its full accurate vector enclosure")
    domain = posterior_root_domain(parent, seed, working, fees, bits=bits)
    body = dict(schema=ATTRIBUTION_SCHEMA, source_sha256=sha(__file__),
        definition=definition(), source_scope=scope, posterior_root_domain=domain,
        complete_integral_arithmetic=integral_arithmetic,
        original_R709_conditions_are_not_relabelled=True,
        all_original_mean_integral_pieces_and_total_residuals_retained=True,
        accurate_whole_angle_root_existence_follows_from_complete_source_bound_inputs=True,
        normal_roots_and_physical_surface_completion_certified=False)
    return dict(definition=body, identity_sha256=canonical(body))


def validate_root_domain_attribution(value, *, parent_math, actual_binding,
        geometry_identity, phi_interval, total_equation, exact_partition,
        active_leaves, structural_reference, files, bits):
    """Re-read actual candidate words and recompute every R722 rational condition."""
    require_actions()
    k = bind_parent_math(parent_math)
    if not isinstance(value, dict) or set(value) != {"definition", "identity_sha256"}:
        raise ValueError("Use the entire posterior root-domain attribution")
    body = value["definition"]
    if canonical(body) != value["identity_sha256"]:
        raise ValueError("The complete posterior root-domain identity changed")
    working = body["source_scope"]["complete_actual_working_candidate"]
    verify_saved_candidate(k, actual_binding, working, files)
    expected = _attribution(k, actual_binding, geometry_identity, phi_interval,
        working, total_equation, exact_partition, active_leaves,
        structural_reference, bits=bits)
    if value != expected:
        raise ValueError("The entire actual R722 domain, source attribution or outward arithmetic differs")
    return dict(schema=ATTRIBUTION_SCHEMA, identity_sha256=value["identity_sha256"],
        source_sha256=sha(__file__), root_domain_recomputed=True,
        entire_original_candidate_batch_reread=True,
        original_R709_coarse_inequalities_proved=body["source_scope"][
            "original_R709_coarse_inequalities_proved"],
        accurate_root_radius_range=[
            body["posterior_root_domain"]["bounds"]["accurate_root_radius_lower"],
            body["posterior_root_domain"]["bounds"]["accurate_root_radius_upper"]],
        accurate_root_vertical_lower=body["posterior_root_domain"]["bounds"][
            "accurate_root_direction_vertical_lower"],
        complete_whole_circle_or_normal_chain_inferred=False)


def _mean_jet_bounds(parent, seed, working, fees, root_domain, *, bits=160,
                     taylor_order=48, profile_series_order=48):
    """New R722 existence prelude, then the complete original R710/R711 body."""
    require_actions()
    upper_dyadic = parent.upper_dyadic
    box = parent.box
    exact_relative_lengths = parent.exact_relative_lengths
    fraction = parent.fraction
    point_vector = parent.point_vector
    point_norm = parent.point_norm
    cap_floor = parent.cap_floor
    nonnegative = parent.nonnegative
    centered_vector = parent.centered_vector
    normalized_jets = parent.normalized_jets
    Interval = parent.Interval
    dot = parent.dot
    vector_box = parent.vector_box
    vsub = parent.vsub
    vscale = parent.vscale
    pi_bounds = parent.pi_bounds
    word = parent.word
    trig_boxes = parent.trig_boxes
    sqrt_bounds = parent.sqrt_bounds
    lower_dyadic = parent.lower_dyadic
    complete_profile_moment_enclosures = parent.complete_profile_moment_enclosures
    vector_error = parent.vector_error
    canonical = parent.canonical
    PROVIDER_SHA = parent.PROVIDER_SHA
    MEAN_VECTOR_KEYS = parent.MEAN_VECTOR_KEYS
    U = lambda q: upper_dyadic(q, bits)
    S = box(fees["accurate_S_enclosure"], bits)
    length = exact_relative_lengths(seed, S, bits)
    lc, lcu, b = length["central_lower"], length["central_upper"], length["boundary_upper"]
    domain = root_domain["bounds"]
    rminus = fraction(domain["accurate_root_radius_lower"])
    rplus = fraction(domain["accurate_root_radius_upper"])
    zeta = fraction(domain["accurate_root_direction_vertical_lower"])
    if not 0 < rminus <= rplus < 1 or not 0 < zeta <= 1:
        raise ValueError("The recomputed complete posterior root domain is inconsistent")
    profile_delta = length["profile_delta"]
    if not 0 < profile_delta < Fraction(1, 8):
        raise ValueError("The complete independent R711 profile delta is invalid")
    candidate = [point_vector(working[name]) for name in ("v", "v_phi", "v_phiphi")]
    v0, v1, v2 = candidate
    amin, amax = point_norm(v0, bits)
    if amin <= 0 or v0[2] <= 0:
        raise ValueError("The actual candidate direction must have a paid positive vertical component")
    zhat = v0[2]/amax
    zstar = min(zhat, zeta)
    nu = cap_floor(zstar, bits)
    residual = [nonnegative(q, "accurate centered equation residual")
                for q in fees["accurate_centered_total_equation_residual_norms"]]
    if len(residual) != 3:
        raise ValueError("Keep zero, first and second centered accurate total-equation residuals")
    E0, R1, R2 = residual
    Ed = min(Fraction(2), U(2*E0/(lc*(amin+rminus))))
    LB = U(b/zstar)
    Er = U((E0+LB*Ed)/lc)
    Ev = U(E0/lc+(LB/lc+rplus)*Ed)
    U1 = nonnegative(fees["boundary_reference_phi_norm_upper"], "T0 phi")
    U2 = nonnegative(fees["boundary_reference_phiphi_norm_upper"], "T0 phiphi")
    M0, C0, C1 = U(b/nu), U(6*b/nu**2), U(36*b/nu**3)
    N0, Nd = U(6*b*U1/nu**2), U(36*b*U1/nu**3)
    Qd = U(6*b*U2/nu**2+36*b*U1**2/nu**3)
    delta1 = U(Er/(rminus*amin)+Ed/amin)
    delta2 = U(6*Er*(rplus+amax)/(rminus**2*amin**2)+12*Ed/amin**2)
    eta = U((1+M0/(lc*rminus))/lc)
    DJ = U(C0*Ed/rminus+M0*delta1)
    h1, h2 = point_norm(v1, bits)[1], point_norm(v2, bits)[1]
    Ev1 = U(eta*(R1+DJ*h1+N0*Ed))
    c1, c2 = U(h1/amin), U(6*h1*h1/(amin*amin))
    e1, e2 = U(delta1*h1), U(delta2*h1*h1)
    move0 = U(DJ*h2+Qd*Ed+2*(Nd*Ed*c1+N0*e1)
        +C1*Ed*c1*c1+C0*(2*c1*e1+e1*e1)+C0*Ed*c2+M0*e2)
    move1 = U(2*N0*Ev1/rminus
        +(C0+6*M0)*(2*h1*Ev1+Ev1*Ev1)/(rminus*rminus))
    Ev2 = U(eta*(R2+move0+move1))
    vboxes = [centered_vector(values, error, bits)
        for values, error in zip(candidate, (Ev, Ev1, Ev2))]
    vboxes[0] = [v.intersect(-rplus, rplus) for v in vboxes[0]]
    vboxes[0][2] = vboxes[0][2].intersect(rminus*zeta, rplus)
    dboxes, rboxes = normalized_jets(*vboxes, norm_lower=rminus, norm_upper=rplus)
    candidate_radius = Interval(amin, amax, bits)
    dcenter = [Interval(q, q, bits)/candidate_radius for q in v0]
    dboxes[0] = [v.intersect(max(Fraction(-1), c.lo-Ed), min(Fraction(1), c.hi+Ed))
        for v, c in zip(dboxes[0], dcenter)]
    dboxes[0][2] = dboxes[0][2].intersect(zeta, 1)
    # Recompute radius jets with the stronger zero-direction enclosure.
    rboxes[1] = dot(dboxes[0], vboxes[1])
    rboxes[2] = (dot(dboxes[0], vboxes[2])+dot(vboxes[1], vboxes[1])/rboxes[0]
        -dot(vboxes[0], vboxes[1])**2/(rboxes[0]**3))
    ejets = [vector_box(fees["accurate_fixed_chart_radial_jets"][name], bits)
             for name in ("e", "ep", "epp")]
    if fees.get("fixed_chart_e_is_the_accurate_horizontal_unit_radial_vector") is not True:
        raise ValueError("The projected frame needs the actual fixed horizontal unit radial vector")
    e0, ep, epp = ejets
    d0, dp, dpp = dboxes
    ed = dot(e0, d0)
    edp = dot(ep, d0)+dot(e0, dp)
    edpp = dot(epp, d0)+2*dot(ep, dp)+dot(e0, dpp)
    y0 = vsub(e0, vscale(d0, ed))
    yp = vsub(vsub(ep, vscale(d0, edp)), vscale(dp, ed))
    ypp = vsub(vsub(vsub(epp, vscale(d0, edpp)), vscale(dp, 2*edp)), vscale(dpp, ed))
    wboxes, _ = normalized_jets(y0, yp, ypp, norm_lower=zeta, norm_upper=1)
    lam = [word(working[name]) for name in ("lambda", "lambda_phi", "lambda_phiphi")]
    pi = pi_bounds(bits)
    if not 0 < lam[0] < pi.lo:
        raise ValueError("Actual R711 amplitude candidate is not proved inside (0,pi)")
    sinhat = trig_boxes(Interval(lam[0], lam[0], bits), taylor_order)[0]
    full_branch_floor = min(sinhat.lo, sqrt_bounds(1-rplus*rplus, bits)[0],
        2*rminus*sqrt_bounds(1-rminus*rminus, bits)[0])
    m = lower_dyadic(full_branch_floor/3, bits)
    if m <= 0:
        raise ValueError("Current outward data cannot resolve the positive full-profile derivative")
    moment_names = ("profile_moment", "profile_moment_first_derivative",
                    "profile_moment_second_derivative")
    moment_proof = complete_profile_moment_enclosures(seed, working["lambda"],
        bits=bits, series_order=profile_series_order)
    moments = moment_proof["intervals"]
    moment_fees = [max(abs(v.lo-word(working[name])), abs(v.hi-word(working[name])))
        for v, name in zip(moments, moment_names)]
    moment_proof["actual_working_moment_binary64_hex"] = [working[name] for name in moment_names]
    moment_proof["complete_working_moment_error_upper"] = moment_fees
    moment_proof["external_profile_moment_error_inputs_used"] = False
    El0 = U((moments[0]-rboxes[0]).abs_upper()/m)
    El1 = U(((moments[1]*lam[1]-rboxes[1]).abs_upper()+El0*abs(lam[1]))/m)
    El2 = U(((moments[1]*lam[2]+moments[2]*lam[1]*lam[1]-rboxes[2]).abs_upper()
        +El0*(abs(lam[2])+lam[1]*lam[1])
        +2*abs(lam[1])*El1+El1*El1)/m)
    lboxes = [Interval(value-error, value+error, bits)
        for value, error in zip(lam, (El0, El1, El2))]
    lboxes[0] = lboxes[0].intersect(0, pi.hi)
    intervals = dict(v=vboxes[0], v_phi=vboxes[1], v_phiphi=vboxes[2],
        d=dboxes[0], d_phi=dboxes[1], d_phiphi=dboxes[2],
        w=wboxes[0], w_phi=wboxes[1], w_phiphi=wboxes[2],
        **{"lambda": lboxes[0], "lambda_phi": lboxes[1], "lambda_phiphi": lboxes[2]})
    errors = {name: vector_error(intervals[name], working[name], bits)
              for name in MEAN_VECTOR_KEYS}
    for name in ("lambda", "lambda_phi", "lambda_phiphi"):
        actual = word(working[name])
        errors[name] = max(abs(intervals[name].lo-actual), abs(intervals[name].hi-actual))
    return dict(seed_model_identity_sha256=canonical(seed),
        literal_phi_hex=working["literal_phi_hex"], provider_sha256=PROVIDER_SHA,
        intervals=intervals, norm_error_upper=errors,
        radius_intervals=rboxes, accurate_root_radius_range=[rminus, rplus],
        accurate_root_vertical_lower=zeta,
        bounds=dict(direction_error=Ed, radius_error=Er, vector_error=Ev,
            first_angular_vector_error=Ev1, second_angular_vector_error=Ev2,
            common_segment_vertical_lower=zstar, common_segment_normalization_lower=nu,
            normalization_first_derivative_difference=delta1,
            normalization_second_derivative_difference=delta2,
            complete_root_J_inverse_upper=eta, complete_root_J_difference=DJ,
            second_equation_zero_root_motion=move0,
            second_equation_first_jet_motion=move1,
            M0=M0, C0=C0, C1=C1, N0=N0, Nd=Nd, Qd=Qd,
            amplitude_derivative_lower=m,
            amplitude_errors=[El0, El1, El2]),
        length_bounds=length, accurate_S_interval=S,
        complete_central_profile_moment_proof=moment_proof,
        central_profile_moment_errors_certified_by_this_module=True,
        precision_bits=bits, taylor_order=taylor_order, profile_series_order=profile_series_order,
        input_fees_certified_by_this_module=False,
        continuous_uniform_field_certificate=False)



class PosteriorMeanKernel:
    """One actual complete immutable input; no caller-created candidate is accepted."""

    def __init__(self, actual, parent_math, mean_integrals):
        require_actions()
        if (sha(type(actual).__init__.__code__.co_filename) != ACTUAL_INPUT_SHA256
                or sha(mean_integrals.__file__) != PARENT_MEAN_INTEGRAL_SHA256):
            raise ValueError("Use the actual complete input and original mean-integral producer")
        self.k = bind_parent_math(parent_math)
        self.actual = actual
        self.seed = _bind_actual(actual.binding)
        if (canonical(actual.binding) != actual.identity
                or self.seed != actual.seed
                or actual.seed_fees is not parent_math
                or actual.seed_identity != self.k.canonical(self.seed)):
            raise ValueError("The complete actual frozen seed or input binding differs")
        self.source_record = actual.used.add(__file__)
        proof = actual.topic/THEOREM_PATH
        self.theorem_record = actual.used.add(proof)
        if (self.theorem_record["sha256"] != THEOREM_SHA256
                or self.theorem_record["bytes"] != THEOREM_BYTES):
            raise ValueError("The complete published R722 theorem source changed")
        self.definition = definition()
        self.definition_identity = canonical(self.definition)

    def mean_jet_bounds(self, geometry, working, total_equation, exact_partition,
                        active_leaves, phi_interval, *, bits=160,
                        taylor_order=48, profile_series_order=48):
        require_actions()
        if (geometry.actual is not self.actual or geometry.k is not self.k
                or bits != geometry.bits
                or canonical(self.actual.binding) != self.actual.identity):
            raise ValueError("The whole-angle mean belongs to a different actual field")
        angle = working["literal_phi_hex"]
        if angle not in self.actual.seed_rows or working != self.actual.seed_rows[angle]:
            raise ValueError("Use the entire genuinely recorded fixed-reference mean candidate")
        attribution = _attribution(self.k, self.actual.binding, geometry.identity,
            phi_interval, working, total_equation, exact_partition, active_leaves,
            geometry.unit_reference_provenance, bits=bits)
        row = total_equation["angles"][0]
        result = _mean_jet_bounds(self.k, self.seed, working, row["fees"],
            attribution["definition"]["posterior_root_domain"], bits=bits,
            taylor_order=taylor_order, profile_series_order=profile_series_order)
        result["root_domain_attribution"] = attribution
        result["root_domain_source"] = "R722 posterior convex minimum localization"
        result["root_domain_source_sha256"] = sha(__file__)
        result["original_R709_coarse_inequalities_proved"] = row[
            "all_pointwise_R709_sufficient_inequalities_proved"]
        result["original_R709_coarse_inequalities_assumed_for_existence"] = False
        self.actual.used.verify(self.source_record)
        self.actual.used.verify(self.theorem_record)
        return result

    def metadata(self):
        return dict(schema=SCHEMA, source=self.source_record,
            theorem_source=self.theorem_record, definition=self.definition,
            definition_identity_sha256=self.definition_identity,
            actual_input_identity=self.actual.identity,
            original_complete_math_source_sha256=PARENT_MATH_SHA256,
            complete_root_domain_and_original_jet_arithmetic_source_explicit=True,
            whole_circle_normal_or_geometry_completion_inferred=False)
