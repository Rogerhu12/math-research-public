#!/usr/bin/env python3
"""R426 same-job live-query complete metric for the unchanged R416 field.

This independent entry retains the complete R418 field, target, cap identity,
closed root plan, all four R251 Loewner tests and original resource semantics.
Only an unresolved native/collar radial cell may request the original f12f
QueryCover on that exact closed radial interval. All possible source inverse
fragments and the complete original exact deep-root family remain included.
An available complete coarse bound survives a refinement work-budget stop.

The provider reads the actual retained complete source-panel/index payloads
in the same Actions job; it does not reconstruct deleted data from a digest,
select a root, modify a calibration, change the target, or add a native gate.
Only one necessary JSON summary of at most 90000 bytes is emitted. Full
recomputable field, primitive and query evidence stays in the owned directory.
Author: OpenAI / ChatGPT exact_refinement agent, 2026-11-16.
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path, PurePosixPath
import signal
import sys
import time
from types import SimpleNamespace

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R426-current-C-accurate-ten-complete-closed-relative-metric-live-queries-v1"
CUT_NAME = "geometry_20261115_current_C_accurate_cut_patch.py"
PREFIX_NAME = "geometry_20261115_continuous_ten_frozen450_prefix_metric.py"
KERNEL_NAME = "geometry_20261115_shared_field_relative_metric.py"
C_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
CUFF_NAME = "geometry_20261115_current_C_original_cuff_target_atlas.py"
CAP_NAME = "geometry_20261115_current_C_ten450_fixed_cap_balls.py"
LIVE_NAME = "geometry_20261115_same_job_C_live_query_provider.py"
BASE_METRIC_NAME = "geometry_20261115_current_C_ten_complete_relative_metric.py"
SOURCE_PINS = {
    CUT_NAME: "28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b",
    PREFIX_NAME: "011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84",
    KERNEL_NAME: "a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17",
    C_NAME: "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df",
    CUFF_NAME: "02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2",
    CAP_NAME: "0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae",
    LIVE_NAME: "07fc4e41a6318c43a6e03313356df4df7538ccd5ea110406434b2e420c09bcd9",
    BASE_METRIC_NAME: "28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590",
}
SUMMARY_LIMIT = 90000
MODEL_CHOICE = "R286-convention-C-all-original-exact-root-sequences"
TARGET_DEFINITION = "g_C=E_C(r)*dr^2+r^2*dTheta^2 on the original continuous radial domain"
QUERY_KEYS = ("complete_closed_domain_bound", "domain_containment_proved",
              "continuous_model_family_conditions_proved", "work_resolution_complete",
              "budget_or_refinement_stop", "leaf_ledger_rows", "reason")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Execute mathematical consumers only in the named public Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False) + "\n").encode()


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=sha(raw))


def receipt(path, root=None):
    path = Path(path)
    size, digest = 0, hashlib.sha256()
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            size += len(raw)
            digest.update(raw)
    return dict(file=str(path.relative_to(root)) if root is not None else path.name,
                bytes=size, sha256=digest.hexdigest())


def write(path, value, root):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return receipt(path, root)


def same_literal(left, right):
    return canonical(left) == canonical(right)


def same_payload(left, right):
    return (isinstance(left, dict) and isinstance(right, dict)
            and type(left.get("bytes")) is int and type(right.get("bytes")) is int
            and left["bytes"] == right["bytes"] and left.get("sha256") == right.get("sha256"))


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Q)):
        raise ValueError("Use exact rational text or integers for declared coordinates")
    return Q(value)


def load(directory, name):
    require_actions()
    path = (Path(directory) / name).resolve()
    row = receipt(path)
    if row["sha256"] != SOURCE_PINS[name]:
        raise ValueError("An actual complete defining source differs: " + name)
    for module in tuple(sys.modules.values()):
        other = getattr(module, "__file__", None)
        if other is not None and Path(other).resolve() == path:
            return module, row
    module_name = "_r426_" + name[:-3]
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError("The pinned source has no loader: " + name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module, row


def safe_member(directory, name):
    directory = Path(directory).resolve()
    relative = PurePosixPath(name)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise ValueError("Use an original relative output member")
    path = directory / str(relative)
    if path.resolve() == directory or not path.resolve().is_relative_to(directory):
        raise ValueError("An actual member escaped its source directory")
    cursor = path
    while cursor != directory:
        if cursor.is_symlink():
            raise ValueError("An actual bound member may not traverse a symlink")
        cursor = cursor.parent
    return path


def bound_member(C, directory, descriptor):
    if not isinstance(descriptor, dict):
        raise ValueError("An actual original output descriptor is absent")
    path = safe_member(directory, descriptor["file"])
    value, row = C.read_bound(path, descriptor["sha256"])
    if not same_payload(row, descriptor):
        raise ValueError("An actual original member size/SHA differs")
    return value, row


def dyadic_endpoint(row):
    if (not isinstance(row, dict) or not isinstance(row.get("mantissa"), str)
            or type(row.get("binary_exponent")) is not int):
        raise ValueError("Use the producer's exact dyadic endpoint record")
    value, exponent = int(row["mantissa"]), row["binary_exponent"]
    return Q(value * (1 << exponent)) if exponent >= 0 else Q(value, 1 << -exponent)


def producer_interval(row):
    if not isinstance(row, dict):
        raise ValueError("A purported complete producer bound has no interval")
    lo, hi = dyadic_endpoint(row["lower"]), dyadic_endpoint(row["upper"])
    if lo > hi:
        raise ValueError("The actual producer interval is reversed")
    return lo, hi


class ActualCompleteCTarget:
    """Only actual f12f closed queries of the field's already-bound C result.

    Reading the four metadata objects consumes the pinned producer's proved
    enclosure contract.  It does not rerun, replace, or claim a byte audit of
    the original primitive/inverse ledgers.  Work-resolution failure does not
    invalidate a returned complete coarse bound.  No cut-point box is extended
    to a nontrivial radial interval.
    """
    def __init__(self, C, current, result_path, result_sha256):
        require_actions()
        self.domain = (current.field.cuff, current.field.cut)
        self.rows, self.cuts, self.query_status = [], [], []
        self.receipts = {}
        self.producer_report = self.binding = self.query_plan = None
        self.natural_radius = None
        self.conditions_proved = False
        self.supplied = result_path is not None
        self.expected = copy.deepcopy(current.target.definition["continuous_tail"])
        self.expected_binding = current.target.binding["complete_original_C_input_binding"]
        self.expected_result = copy.deepcopy(self.expected["actual_result"])
        self.explicit_target = copy.deepcopy(current.target.binding["complete_target_identity"])
        if not self.supplied:
            return
        report, result_row = C.read_bound(result_path, result_sha256)
        if not same_payload(result_row, self.expected_result):
            raise ValueError("Use the very same actual C result bound into this accurate field")
        if (report.get("schema") != C.SCHEMA
                or report.get("source_sha256") != SOURCE_PINS[C_NAME]
                or report.get("repository") != REPOSITORY
                or report.get("target_model_schema") != C.MODEL_SCHEMA
                or report.get("deep_definition") != "original-exact-root-family"
                or report.get("model_choice_is_explicit_and_not_original_finite_output_relabel") is not True
                or report.get("original_finite_output_certified_as_continuous_solution") is not False
                or report.get("R26_numerical_certificate_or_rational_deep_target_used") is not False
                or report.get("global_warp_alpha_or_original_cut_renormalised") is not False
                or report.get("original_real_profile_and_model_C_unchanged") is not True
                or report.get("preserved_original_producer_source", {}).get("sha256") != C.BASE_SOURCE_SHA256
                or report.get("preserved_unit_panel_producer_source", {}).get("sha256") != C.UNIT_PANEL_SOURCE_SHA256):
            raise ValueError("The actual original continuous-C source/model contract differs")
        if (self.expected.get("source_sha256") != SOURCE_PINS[C_NAME]
                or self.expected.get("preserved_original_source_sha256") != C.BASE_SOURCE_SHA256
                or self.expected.get("preserved_unit_panel_source_sha256") != C.UNIT_PANEL_SOURCE_SHA256):
            raise ValueError("The accurate factory's actual C provenance differs")
        directory = Path(result_path).resolve().parent
        binding, binding_row = bound_member(C, directory, report["input_binding"])
        plan, plan_row = bound_member(C, directory, report["query_plan"])
        queries, queries_row = bound_member(C, directory, report["query_results"])
        for actual, expected in ((binding_row, self.expected["input_binding"]),
                                 (plan_row, self.expected["original_query_plan"]),
                                 (queries_row, self.expected["original_query_results"])):
            if not same_payload(actual, expected):
                raise ValueError("An actual C member differs from the same-field factory identity")
        if (not same_literal(binding, self.expected["actual_input_binding"])
                or not same_literal(binding, self.expected_binding)
                or binding.get("schema") != C.SCHEMA + "-input-binding"
                or binding.get("source_sha256") != SOURCE_PINS[C_NAME]
                or binding.get("original_source_revision") != C.REVISION
                or binding.get("proof", {}).get("sha256") != C.PROOF_SHA
                or not same_literal(binding["preserved_original_producer_source"],
                                    report["preserved_original_producer_source"])
                or not same_literal(binding["preserved_unit_panel_producer_source"],
                                    report["preserved_unit_panel_producer_source"])
                or plan.get("schema") != C.QUERY_SCHEMA
                or plan.get("input_binding_sha256") != report["input_binding"]["sha256"]
                or queries.get("schema") != C.SCHEMA + "-queries"):
            raise ValueError("The full actual C input/query/proof identity differs")
        if (set(binding["original_sources"]) != set(C.PINS)
                or any(binding["original_sources"][name]["sha256"] != expected
                       for name, expected in C.PINS.items())):
            raise ValueError("Retain every original C source, not only a fingerprint")
        convention = binding["convention"]
        if (convention.get("schema") != C.MODEL_SCHEMA
                or convention.get("explicit_model_layer_choice") is not True
                or convention.get("deep_definition") != report["deep_definition"]
                or convention.get("deep_bounds_valid_for_every_original_root_in_half_to_two") is not True
                or convention.get("deep_roots_numerically_selected_or_computed") is not False
                or convention.get("natural_outer_radius_reidentified_as_nominal_cut") is not False
                or convention.get("global_lambda_reselected") is not False
                or self.domain[0] != C.rat(binding["physical_parameters"]["rCuff"])
                or self.domain[1] != rational(self.explicit_target["original_binary_cut_exact_rational"])
                or self.domain[1] != rational(self.expected["cut_radius"])
                or self.domain[0] != rational(self.expected["cuff_radius"])
                or not same_literal(report["natural_outer_radius"], self.expected["natural_outer_radius"])):
            raise ValueError("The original root family, cut, cuff, or natural outer domain differs")
        self.conditions_proved = bool(
            report.get("declared_continuous_model_family_conditions_proved") is True
            and report.get("original_exact_deep_root_existence_proved") is True
            and report.get("all_admissible_original_root_choices_uniformly_enclosed") is True
            and report.get("full_finite_head_complete") is True
            and report.get("complete_original_pieces") == 1440
            and report.get("original_piece_count") == 1440
            and report.get("original_finite_cell_count") == 160
            and report.get("protected_join", {}).get("proved") is True
            and report.get("finite_joins", {}).get("proved") is True
            and convention.get("root_existence_proved") is True)
        if report.get("natural_outer_radius") is not None:
            self.natural_radius = producer_interval(report["natural_outer_radius"])
        requested, returned = plan["queries"], queries["results"]
        if (not isinstance(requested, list) or not isinstance(returned, list)
                or type(report.get("requested_query_count")) is not int
                or type(report.get("returned_query_count")) is not int
                or len(requested) != report["requested_query_count"]
                or len(returned) != report["returned_query_count"]
                or len(returned) > len(requested)
                or not same_literal(queries.get("unvisited_query_suffix"),
                                    report.get("unvisited_query_suffix"))):
            raise ValueError("The full query plan or its actual returned prefix differs")
        self.receipts = dict(result=result_row, input_binding=binding_row,
                             query_plan=plan_row, query_results=queries_row)
        self.producer_report, self.binding, self.query_plan = report, binding, plan
        for index, row in enumerate(returned):
            q = row["query"]
            if (not same_literal(q, requested[index]) or type(q.get("index")) is not int
                    or q["index"] != index or q.get("left_closed") is not True
                    or q.get("right_closed") is not True):
                raise ValueError("Retain original query order, indices and both closed endpoints")
            status = dict(index=index, query=copy.deepcopy(q), usable=False,
                          original={key:copy.deepcopy(row[key]) for key in QUERY_KEYS if key in row})
            self.query_status.append(status)
            if not (self.conditions_proved and self.natural_radius is not None
                    and row.get("complete_closed_domain_bound") is True
                    and row.get("domain_containment_proved") is True
                    and row.get("continuous_model_family_conditions_proved") is True):
                continue
            if q["kind"] == "whole-natural-domain":
                if (q["left"] != "original-exact-dyadic-rCuff"
                        or q["right"] != "natural-real-integral-R_out"):
                    raise ValueError("The actual whole-natural query was relabelled")
                left, right = self.domain[0], self.natural_radius[0]
            elif q["kind"] == "closed-rational-radius-interval":
                left, right = rational(q["left"]), rational(q["right"])
                if left > right or left < self.domain[0] or right > self.natural_radius[0]:
                    raise ValueError("A purported proved query exceeds its common natural domain")
            else:
                raise ValueError("Unsupported actual continuous-C query kind")
            lo, hi = producer_interval(row["E"])
            if hi < 1:
                raise ValueError("The reported E bound contradicts the exact formula E=1+w^2")
            left, right = max(left, self.domain[0]), min(right, self.domain[1])
            if left > right:
                status["unused_reason"] = "This complete original query lies outside this field"
                continue
            # This exact analytic intersection is independent of resolution goals.
            self.rows.append(dict(index=index, left=left, right=right,
                lower=max(Q(1), lo), upper=hi, query_kind=q["kind"],
                original_E=copy.deepcopy(row["E"]),
                work_resolution_complete=row.get("work_resolution_complete")))
            status.update(usable=True, effective_closed_field_interval=[str(left), str(right)],
                E_lower_used=str(max(Q(1), lo)), E_upper_used=str(hi),
                analytic_E_ge_one_intersection=True)
        self.rows.sort(key=lambda row: (row["left"], row["right"], row["index"]))
        self.cuts = sorted({x for row in self.rows for x in (row["left"], row["right"])})

    def bounds(self, a, b):
        if not self.domain[0] <= a <= b <= self.domain[1]:
            raise ValueError("Do not extend the current accurate target beyond its actual radial pieces")
        selected = [row for row in self.rows if row["left"] <= b and a <= row["right"]]
        cursor, started = a, False
        for row in selected:
            if row["left"] > cursor:
                break
            if row["right"] >= cursor:
                cursor, started = max(cursor, row["right"]), True
            if cursor >= b:
                break
        if not started or cursor < b:
            return None
        return (min(row["lower"] for row in selected),
                max(row["upper"] for row in selected),
                [row["index"] for row in selected])

    def describe(self):
        source = self.producer_report or {}
        if self.natural_radius is None:
            domain_status = "actual_natural_outer_radius_not_available"
        elif self.domain[1] <= self.natural_radius[0]:
            domain_status = "actual_cut_at_or_below_common_natural_Rout_lower"
        elif self.domain[1] > self.natural_radius[1]:
            domain_status = "actual_cut_above_reported_natural_Rout_upper"
        else:
            domain_status = "actual_cut_containment_unresolved_in_natural_Rout_interval"
        requested = [] if self.query_plan is None else self.query_plan["queries"]
        returned = len(self.query_status)
        return dict(schema=SCHEMA + "-same-C-closed-target",
            supplied=self.supplied, explicit_model_choice=MODEL_CHOICE,
            definition=TARGET_DEFINITION, actual_result_and_members=self.receipts,
            expected_original_actual_result=self.expected_result,
            complete_input_binding_identity=identity(self.expected_binding),
            complete_current_target_identity=identity(self.explicit_target),
            complete_field_radial_domain=list(map(str, self.domain)),
            natural_outer_radius=None if self.natural_radius is None else list(map(str, self.natural_radius)),
            natural_cut_containment_status=domain_status,
            original_model_family_conditions_proved=self.conditions_proved,
            complete_field_radial_domain_covered=self.bounds(*self.domain) is not None,
            every_original_returned_query=self.query_status,
            actual_not_returned_query_index_suffix=[returned, len(requested)] if self.supplied else None,
            actual_producer_unvisited_query_suffix=source.get("unvisited_query_suffix"),
            actual_producer_unvisited_source_piece_suffix=source.get("unvisited_source_piece_suffix"),
            actual_producer_error=source.get("error"),
            actual_original_ledger_descriptors=source.get("ledgers"),
            actual_original_resolution_unpaid_count=source.get("resource_or_unpaid_scope_rows"),
            original_resolution_flags={key:source[key] for key in (
                "all_requested_closed_query_bounds_complete", "numerical_work_resolution_complete",
                "continuous_convention_C_query_enclosures_complete") if key in source},
            complete_coarse_bounds_used_without_a_work_resolution_gate=True,
            point_cut_boxes_never_extrapolated=True,
            missing_or_unproved_closed_domains_remain_unpaid=True,
            all_original_deep_root_choices_retained=True,
            primitive_and_inverse_ledgers_reexecuted_or_independently_audited=False,
            payload_scope="Complete original result, input binding, query plan and query-results read; ledger payloads only identified",
            original_fingerprint_or_source_schema_used_as_a_bound=False,
            target_replaced_by_Bprime_or_another_finite_profile=False,
            fresh_cross_run_semantic_transfer_not_implemented_here=True,
            actual_C_real_member_selected_or_recalibrated=False)

    def necessary(self):
        description = self.describe()
        return {key:description[key] for key in (
            "supplied", "actual_result_and_members", "expected_original_actual_result",
            "complete_input_binding_identity", "complete_current_target_identity",
            "complete_field_radial_domain", "natural_outer_radius",
            "natural_cut_containment_status", "original_model_family_conditions_proved",
            "complete_field_radial_domain_covered", "every_original_returned_query",
            "actual_not_returned_query_index_suffix",
            "actual_producer_unvisited_query_suffix", "actual_producer_unvisited_source_piece_suffix",
            "actual_producer_error", "actual_original_resolution_unpaid_count", "original_resolution_flags")}


def cap_metric_identity(current, atlas, attachment, cap):
    """Bind the actual complete two graphs once; do not add a cap grid gate."""
    bundle = current.source_bundle
    plan, target = bundle[1], bundle[3]
    binding = cap.describe()
    markers, atlas_markers = binding["markers"], atlas["fixed_caps"]["markers"]
    if (cap.cuff != current.field.cuff
            or not same_literal(binding["original_marker_rows"], plan["fixed_cap"]["markers"])
            or not same_literal(binding["original_complete_ten_target"],
                                target["complete_current_ten_target"])
            or not same_literal(binding["original_complete_ten_target"],
                                current.target.binding["complete_target_identity"])
            or not same_literal(binding["R413_attachment"], attachment)
            or binding["R413_atlas_sha256"] != sha(canonical(atlas))
            or binding["fixed_cap_definition_sha256"] != sha(canonical(plan["fixed_cap"]))
            or len(markers) != len(atlas_markers)
            or len(markers) != atlas["fixed_caps"]["marker_count"]
            or rational(binding["exact_height"]) != rational(atlas["fixed_caps"]["cap_height_exact"])
            or attachment.get("exact_original_cuff_target_twojet_compatibility") is not True):
        raise ValueError("The cap target, actual graph and common original cuff have different owners")
    for index, (row, other) in enumerate(zip(markers, atlas_markers)):
        if (row["current_marker_list_index"] != index or other["index"] != index
                or type(row["upper"]) is not bool or row["upper"] is not other["upper"]
                or row["center_exact"] != other["center_exact"]
                or row["radius_exact"] != other["radius_exact"]
                or row["amplitude_exact"] != other["height_exact"]
                or row["original_float64le"] != other["original_float64le"]):
            raise ValueError("Keep the complete actual side, centre, radius and signed amplitude")
    return dict(schema=SCHEMA + "-complete-cap-target-identity",
        complete_R417_binding=copy.deepcopy(binding),
        actual_R417_binding_sha256=cap.binding_sha256,
        R413_atlas_identity=identity(atlas), complete_R413_attachment=copy.deepcopy(attachment),
        complete_two_closed_disks=True,
        parameter_domain=dict(coordinates="Cartesian x,y, including both poles and the whole cuff",
            exact_radius=str(cap.cuff), sides=["upper", "lower"]),
        exact_graph="F_side(x,y)=(x,y,side*(H+b_side(x,y)))",
        b_definition="sum of every own-side signed A_i*max(0,1-|X-center_i|^2/radius_i^2)^4",
        complete_original_marker_count=len(markers),
        target_metric="I+Db_side tensor Db_side",
        same_actual_graph_and_target_expression=True,
        complete_cap_relative_operator_error_exact="0",
        all_overlaps_and_signed_amplitudes_preserved=True,
        full_closed_disks_paid_by_identity_without_a_new_interval_sweep=True,
        cap_sixjet_balls_curvature_or_spatial_cover_executed=False,
        accurate_cap_not_rounded_renderer=True,
        original_cap_metric_replaced_by_flat_or_zero_tensor=False)


def inspect_cell_once(Prefix, Kernel, M, current, tail, spec, eta):
    field = current.field
    piece = field.pieces[spec["piece_index"]]
    if piece["kind"] == "prefix":
        result = Prefix.inspect(M, Kernel, field, current.target, spec, eta)
        result["piece_target_kind"] = "same_accurate_ten_public_u_prefix"
        return result
    if piece["kind"] not in ("native", "collar"):
        raise ValueError("An actual active piece has an unsupported target coordinate")
    radial, angular = tuple(map(Q, spec["radial"])), tuple(map(Q, spec["angular"]))
    bound = tail.bounds(*radial)
    if bound is None:
        return dict(certified=False, missing_target_premise=True,
            reason="same_actual_C_closed_query_or_common_natural_domain_unpaid",
            actual_closed_radial_cell=list(map(str, radial)),
            piece_target_kind=piece["kind"],
            patch=piece["cut_patch"], cut_three_boxes_not_extrapolated=True,
            geometric_Bprime_not_substituted=True)
    values = current.evaluate(piece, radial, angular, spec["lower"])
    X, Y = tuple(value.d[1] for value in values), tuple(value.d[2] for value in values)
    E, B, C = M.dot(X, X), M.dot(X, Y), M.dot(Y, Y)
    theta, angular_record = Kernel.angle_density(field, M, angular)
    elo, ehi, rows = bound
    r = M.interval(*radial)
    result = Kernel.loewner_certificate(M, E, B, C,
        M.interval(elo, ehi), r*r*theta*theta, eta)
    result.update(
        piece_target_kind="same_actual_C_radial_target",
        actual_complete_closed_query_sources=rows,
        actual_closed_target_E=[str(elo), str(ehi)],
        angular=angular_record, cut_patch=piece["cut_patch"],
        complete_position_and_six_jets={
            name:[M.encode_interval(value.d[j]) for value in values]
            for j, name in enumerate(M.JET_NAMES)},
        independent_R416_patch_used_on_every_affected_cell=True,
        original_four_R251_Loewner_tests_unchanged=True,
        original_C_target_not_one_plus_geometric_Bprime_squared=True,
        full_material_Phi_and_zero_mode_means_retained=True,
        reflected_Gram_uses_the_whole_reflected_field=True,
        common_C_function_not_replaced_by_a_cellwise_midpoint=True)
    return result


def inspect_cell(Prefix, Kernel, M, current, tail, spec, eta):
    report = inspect_cell_once(Prefix, Kernel, M, current, tail, spec, eta)
    piece = current.field.pieces[spec["piece_index"]]
    if report["certified"] or piece["kind"] == "prefix":
        return report
    radial = tuple(map(Q, spec["radial"]))
    before_missing = report.get("missing_target_premise", False)
    attempt = tail.refine(*radial, cell=spec)
    # A cached result is already used by the first call. No identical
    # field evaluation is repeated merely to count a new proof attempt.
    if attempt.get("attempted") and attempt.get("complete_closed_query_bound"):
        report = inspect_cell_once(Prefix, Kernel, M, current, tail, spec, eta)
    report.update(actual_same_job_C_query=attempt,
        target_was_missing_before_this_query=before_missing,
        same_complete_R416_field_and_original_four_Loewner_tests=True,
        query_resolution_target_is_not_an_additional_metric_or_native_gate=True)
    return report


class ExternalStop(RuntimeError):
    def __init__(self, number):
        self.signal_number = number
        super().__init__("Actual external signal " + str(number))


def validate_arguments(args):
    require_actions()
    if (args.continuous_e_result is None) != (args.continuous_e_result_sha256 is None):
        raise ValueError("Supply an actual C result and its SHA together")
    eta = rational(args.eta)
    if (not 0 < eta < 1 or not 64 <= args.interval_bits <= 8192
            or not 64 <= args.sqrt_bits <= 8192
            or not 0 <= args.initial_angular_depth <= 20
            or not 0 <= args.max_depth <= 30 or args.max_visited_cells <= 0
            or not math.isfinite(args.budget_seconds) or args.budget_seconds <= 0):
        raise ValueError("Specify a finite work plan and the requested eta; no target is preset")
    output = args.out.resolve()
    runner = Path(os.environ["RUNNER_TEMP"]).resolve()
    if output == runner or not output.is_relative_to(runner) or args.out.exists():
        raise ValueError("Use a fresh request-owned output below RUNNER_TEMP")
    for path in (args.directory, args.checkpoint_directory, args.cuff_atlas,
                 args.continuous_e_result, args.computations, args.proof_directory):
        if path is not None and Path(path).resolve().is_relative_to(output):
            raise ValueError("A new output must not own an existing input or source")
    return eta


def coverage_state(plan, root_results, active_root, stack, current, ledger):
    if plan is None:
        return dict(schema=SCHEMA + "-coverage-and-pending",
            complete_active_partition=False, complete_root_plan_not_created=True,
            whole_active_closed_domain_unpaid=True,
            full_closed_metric_unpaid=True,
            complete_existing_cell_ledger=ledger)
    total, done = plan["planned_roots"], len(root_results)
    complete = done == total
    active = (not complete and active_root is not None and active_root["rank"] == done)
    pending = ([] if current is None else [copy.deepcopy(current)]) + list(reversed(stack))
    if active and not pending:
        # An exception between last cell retirement and root retirement cannot
        # silently pay the root. Existing cell records remain identified.
        pending = [copy.deepcopy(active_root)]
    if not active:
        pending = []
    suffix_start = total if complete else done + int(active)
    return dict(schema=SCHEMA + "-coverage-and-pending",
        complete_active_partition=complete,
        completed_root_results=copy.deepcopy(root_results),
        current_root_rank=done if active else None,
        current_original_root=copy.deepcopy(active_root) if active else None,
        remaining_closed_DFS_cells=pending,
        untouched_root_rank_suffix=[suffix_start, total],
        exact_root_rank_formula=plan["exact_rank_formula"],
        all_unresolved_terminal_cells_retained_in_ledger=True,
        current_cell_not_retired_until_its_complete_record_and_stack_update=True,
        no_failed_or_unvisited_cell_claimed_certified=True,
        complete_existing_cell_ledger=ledger)


def run(args):
    eta = validate_arguments(args)
    args.out.mkdir(parents=True)
    large = args.out / "large-arrays"
    large.mkdir()
    started = time.monotonic()
    source_rows = {}
    members = {}
    M = None
    old_precision = None
    current_bundle = tail = cap_record = plan = journal = None
    active_root = current_cell = None
    stack, root_results = [], []
    visited = terminal = passed = 0
    kind_counts = {}
    resource_stop = execution_error = None
    phase = "actual_sources_same_field_and_target_binding"
    previous_handlers = {}

    def stop(number, frame):
        raise ExternalStop(number)

    for number in (signal.SIGTERM, signal.SIGINT):
        previous_handlers[number] = signal.getsignal(number)
        signal.signal(number, stop)
    try:
        loaded = {}
        for name in SOURCE_PINS:
            if name == BASE_METRIC_NAME:
                source_rows[name] = receipt(Path(args.computations)/name)
                if source_rows[name]["sha256"] != SOURCE_PINS[name]:
                    raise ValueError("The published R418 algorithm baseline differs")
                continue
            loaded[name], source_rows[name] = load(args.computations, name)
        Live = loaded[LIVE_NAME]
        Live.parameter_record(args)
        Cut, Prefix, Kernel, C, Cuff, Caps = (
            loaded[name] for name in (CUT_NAME, PREFIX_NAME, KERNEL_NAME, C_NAME, CUFF_NAME, CAP_NAME))
        actual_args = SimpleNamespace(**vars(args))
        actual_args.interval_bits = args.interval_bits + args.max_depth
        # R416 sets the public flint context. Save its original value before
        # entering the real loader; do not initialise any legacy geometry.
        from flint import ctx
        old_precision = ctx.prec
        current_bundle = Cut.load_accurate_cut_field(actual_args)
        M = current_bundle.Active
        M.ctx.prec = actual_args.interval_bits
        atlas, atlas_receipt = Cuff.bound_json(args.cuff_atlas, args.cuff_atlas_sha256)
        attachment = Cuff.bind_loaded_shared_bundle(current_bundle.source_bundle, atlas)
        caps = Caps.bind_loaded_shared_bundle(current_bundle.source_bundle,
                                              atlas, attachment, args.computations)
        cap_record = cap_metric_identity(current_bundle, atlas, attachment, caps)
        fixed_tail = ActualCompleteCTarget(C, current_bundle, args.continuous_e_result,
                                           args.continuous_e_result_sha256)
        tail = Live.LiveQueryTarget(C, fixed_tail, args, args.out, started)
        source_rows[Path(__file__).name] = receipt(__file__)
        members["exact_field"] = write(large / "same-R416-accurate-field.json",
            current_bundle.expression_identity(), args.out)
        members["accurate_cut_DAG"] = write(large / "same-R416-cut-expression.json",
            current_bundle.model.definition, args.out)
        members["accurate_prefix_target"] = write(large / "same-complete-ten-target.json",
            current_bundle.target.binding, args.out)
        members["actual_C_target"] = write(large / "actual-complete-C-query-target.json",
            tail.describe(), args.out)
        members["complete_caps_identity"] = write(large / "complete-fixed-cap-metric-identity.json",
            cap_record, args.out)
        binding = dict(schema=SCHEMA + "-input-binding",
            source=receipt(__file__), direct_source_closure=source_rows,
            current_R416_binding=copy.deepcopy(current_bundle.binding),
            complete_original_R409_binding=copy.deepcopy(current_bundle.source_bundle[-1]),
            actual_R413_atlas=atlas_receipt, actual_R413_attachment=copy.deepcopy(attachment),
            actual_R417_binding_identity=identity(caps.describe()),
            actual_complete_C_result=tail.receipts,
            actual_same_job_live_query_binding=tail.binding_receipt,
            original_R418_source_used_only_as_algorithm_provenance=source_rows[BASE_METRIC_NAME],
            complete_original_C_binding_identity=identity(tail.expected_binding),
            actual_genuine_frozen450_checkpoint=copy.deepcopy(current_bundle.binding["actual_450_checkpoint"]),
            actual_same_ten_words=copy.deepcopy(current_bundle.target.binding["all10_frozen_exact_dyadics"]),
            expressions_and_target_members=copy.deepcopy(members),
            whole_native_and_BVP_acceptance_owned_by_original_loader=True,
            old_R409_A_renderer_not_used_for_new_metric=True,
            original_C_root_member_not_changed=True,
            old_finite_target_or_old9_schema_not_relabelled=True)
        members["input_binding"] = write(large / "input-binding.json", binding, args.out)
        plan = Kernel.root_plan(current_bundle.field, current_bundle.target, tail,
                                args.initial_angular_depth)
        plan["original_algorithm_schema"] = plan["schema"]
        plan["schema"] = SCHEMA + "-complete-active-closed-root-plan"
        plan["scope"] = "both exact active sheets; every prefix/collar/native/patch piece; all closed q"
        if plan["planned_roots"] <= 0:
            raise ValueError("The genuine complete field has no active cells")
        for block in plan["radial_blocks"]:
            piece = current_bundle.field.pieces[block["piece_index"]]
            block["actual_cut_patch"] = bool(piece.get("cut_patch", False))
        members["root_plan"] = write(large / "planned-closed-roots.json", plan, args.out)
        kinds = sorted({piece["kind"] for piece in current_bundle.field.pieces})
        kind_counts = {kind:dict(completed_roots=0, certified_roots=0,
                                terminal_cells=0, certified_cells=0, unresolved_cells=0)
                       for kind in kinds}
        journal = Kernel.Journal(large / "relative-metric-cells.jsonl.gz")
        journal.append(dict(type="identity", schema=SCHEMA, eta_exact=str(eta),
            input_binding=members["input_binding"], immutable_root_plan=members["root_plan"]))
        phase = "complete_active_closed_DFS"
        for root in Kernel.roots(plan):
            active_root, stack, root_ok = root, [root], True
            while stack:
                if (visited >= args.max_visited_cells
                        or time.monotonic() - started >= args.budget_seconds):
                    resource_stop = "explicit_cell_or_wall_budget_before_next_cell_pop"
                    break
                current_cell = stack.pop()
                visited += 1
                try:
                    report = inspect_cell(Prefix, Kernel, M, current_bundle, tail, current_cell, eta)
                except (ArithmeticError, ValueError) as error:
                    report = dict(certified=False,
                        reason="interval_or_declared_expression_unresolved",
                        exception=dict(type=type(error).__name__, message=str(error)),
                        pointwise_counterexample_inferred=False)
                if (not report["certified"] and not report.get("missing_target_premise", False)
                        and current_cell["depth"] < args.max_depth):
                    children = Kernel.split_cell(current_cell)
                    journal.append(dict(type="subdivided", cell=current_cell, diagnostic=report))
                    stack.extend(reversed(children))
                    current_cell = None
                    continue
                journal.append(dict(type="terminal_closed_cell", cell=current_cell, operator=report))
                terminal += 1
                passed += int(report["certified"])
                stats = kind_counts[current_cell["piece_kind"]]
                stats["terminal_cells"] += 1
                stats["certified_cells"] += int(report["certified"])
                stats["unresolved_cells"] += int(not report["certified"])
                root_ok = root_ok and report["certified"]
                current_cell = None
            if resource_stop is not None:
                break
            root_results.append(dict(rank=root["rank"], piece_kind=root["piece_kind"],
                lower=root["lower"], actual_cut_patch=root["actual_cut_patch"],
                complete_closed_subdivision=True, certified=root_ok))
            stats = kind_counts[root["piece_kind"]]
            stats["completed_roots"] += 1
            stats["certified_roots"] += int(root_ok)
            active_root = None
            if len(root_results) % 20 == 0:
                print(json.dumps(dict(event="R426_complete_closed_metric_progress",
                    completed_roots=len(root_results), planned_roots=plan["planned_roots"],
                    visited_cells=visited, terminal_cells=terminal, certified_cells=passed,
                    elapsed_seconds=time.monotonic()-started), separators=(",", ":")), flush=True)
        phase = "complete_coverage_readout"
    except BaseException as error:
        execution_error = dict(type=type(error).__name__, message=str(error), phase=phase)
        if isinstance(error, ExternalStop):
            execution_error["external_signal"] = error.signal_number
            execution_error["mathematical_failure_inferred"] = False
    finally:
        if tail is not None:
            closed_queries = tail.close()
            close_errors = {name:row["error"] for name,row in closed_queries.items()
                            if "error" in row}
            if close_errors:
                extra = dict(type="LiveQueryLedgerCloseError",
                    message="Actual live C journal receipts are incomplete",
                    errors=close_errors, phase="closing_actual_live_C_query_ledger_and_status")
                if execution_error is None:
                    execution_error = extra
                else:
                    execution_error["live_query_close_error"] = extra
            try:
                members["actual_live_C_query_status"] = write(
                    large/"same-job-live-C-query-status.json", tail.live_status(), args.out)
            except BaseException as error:
                extra = dict(type=type(error).__name__, message=str(error),
                    phase="closing_actual_live_C_query_ledger_and_status")
                if execution_error is None:
                    execution_error = extra
                else:
                    execution_error["live_query_close_error"] = extra
        if journal is not None:
            try:
                journal.close()
                members["complete_cell_ledger"] = receipt(large / "relative-metric-cells.jsonl.gz", args.out)
            except BaseException as error:
                extra = dict(type=type(error).__name__, message=str(error), phase="closing_original_cell_ledger")
                if execution_error is None:
                    execution_error = extra
                else:
                    execution_error["ledger_close_error"] = extra
        if old_precision is not None:
            from flint import ctx
            ctx.prec = old_precision
        for number, handler in previous_handlers.items():
            signal.signal(number, handler)
    coverage = coverage_state(plan, root_results, active_root, stack, current_cell,
                              members.get("complete_cell_ledger"))
    coverage["immutable_root_plan"] = members.get("root_plan")
    coverage["active_target_and_caps_identity"] = {
        key:members.get(key) for key in ("accurate_prefix_target", "actual_C_target", "complete_caps_identity")}
    coverage["actual_resource_stop"] = resource_stop
    coverage["actual_execution_error"] = execution_error
    coverage["complete_cap_identity_available"] = cap_record is not None
    coverage["all_unpaid_terminal_addresses_are_in_complete_cell_ledger"] = True
    members["coverage_and_pending"] = write(large / "coverage-and-pending.json", coverage, args.out)
    active_complete = coverage["complete_active_partition"]
    active_ok = (active_complete and execution_error is None
                 and all(row["certified"] for row in root_results))
    cap_ok = cap_record is not None
    full_ok = bool(active_ok and cap_ok and tail is not None
                   and tail.bounds(*tail.domain) is not None and tail.conditions_proved)
    field_identity = None if current_bundle is None else identity(current_bundle.binding)
    result = dict(schema=SCHEMA, repository=REPOSITORY, run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"), source=receipt(__file__),
        completed=bool(active_complete and execution_error is None),
        complete_active_partition=active_complete,
        complete_active_relative_operator_bound=active_ok,
        complete_two_cap_relative_operator_identity=cap_ok,
        complete_closed_relative_operator_bound_for_bound_accurate_target=full_ok,
        requested_eta_exact=str(eta), actual_field_binding_identity=field_identity,
        parameters=dict(interval_bits=args.interval_bits,
            effective_interval_bits=args.interval_bits+args.max_depth, sqrt_bits=args.sqrt_bits,
            initial_angular_depth=args.initial_angular_depth, max_depth=args.max_depth,
            max_visited_cells=args.max_visited_cells, budget_seconds=args.budget_seconds,
            same_job_C_queries=({} if tail is None else copy.deepcopy(tail.parameters))),
        members=members,
        counts=dict(planned_roots=None if plan is None else plan["planned_roots"],
            complete_active_piece_count=None if current_bundle is None else len(current_bundle.field.pieces),
            complete_radial_block_count=None if plan is None else len(plan["radial_blocks"]),
            planned_cut_patch_roots=None if plan is None else plan["angular_count"] *
                sum(int(block["actual_cut_patch"]) for block in plan["radial_blocks"]),
            completed_roots=len(root_results), visited_cells=visited, terminal_cells=terminal,
            certified_cells=passed, unresolved_terminal_cells=terminal-passed, by_piece_kind=kind_counts,
            complete_fixed_caps=2 if cap_ok else 0),
        same_actual_C_target=None if tail is None else tail.necessary(),
        scope=dict(
            field="Independent R416 accurate cut field with all original full338 nodal data/B/112 material modes",
            target="Original bound continuous-ten DAG and all-root-family C, plus the same fixed graph caps",
            active_coordinates="prefix t=s_numeric and q; radial collar/native/patch r and q; Theta=Phi(2*pi*q)",
            prefix_radial_target="(L_true/L_numeric)^2",
            prefix_angular_target="a_true(L_true*t/L_numeric;p10)^2*Phi_q^2",
            radial_target="E_C(r), r^2*Phi_q^2",
            cap_target="I+Db_side tensor Db_side on the complete Cartesian disk",
            all_ten_current_words_full_means_material_cut_and_mixed_jets_retained=True,
            both_reflected_sheets_all_closed_angle_endpoints_and_piece_boundaries_retained=True,
            whole_query_bound_not_cut_box_extrapolation=True,
            exact_radial_cells_may_request_original_same_C_QueryCover=True,
            all_possible_inverse_fragments_and_every_original_deep_root_retained=True,
            original_head_source_panels_read_only_from_actual_retained_payload=True,
            all_original_head_six_integral_sums_not_reexecuted=True,
            original_cumulative_radius_and_deep_family_width_may_limit_refinement=True,
            same_closed_radial_interval_shared_by_angles_and_reflections=True,
            a_new_complete_query_is_intersected_with_original_complete_coarse_bounds=True,
            original_root_plan_not_changed_by_queries_made_during_DFS=True,
            four_original_R251_Loewner_tests_and_closed_DFS_unchanged=True,
            complete_phase_bound_follows_from_material_shift_rigid_rotation_and_fixed_caps=full_ok,
            finite_bandwidth_in_physical_or_material_angle_not_inferred=True,
            same_C_coefficients_kept_as_real_functions_not_independent_midpoint_choices=True,
            cut_target_atlas_uses_bound_R416_gamma_third_jet=True,
            cuff_target_atlas_uses_actual_R413_original_cuff=True,
            cap_interval_sixjet_balls_or_curvature_cover_executed=False,
            source_only_caps_identity_does_not_claim_unrun_cell_reports=True,
            accurate_scalar_speed_domain_proved_by_this_metric_consumer=False,
            rounded_evaluator_or_raw_RK_error_certified=False,
            original_accepted_R409_field_metric_reused=False,
            old_field_acceptance_automatically_transferred_to_R416=False,
            reach_embedding_held_and_full_task_completed=False,
            new_native_FD_RMS_BC_or_acceptance_gate_added=False,
            missing_margin_or_budget_stop_is_not_a_pointwise_counterexample=True,
            arbitrary_refinement_of_fixed_C_boxes_promised=False,
            actual_field_or_threshold_result_not_fabricated=True),
        resource_stop=resource_stop, execution_error=execution_error,
        elapsed_seconds=time.monotonic()-started,
        timer_scope="Includes loader/setup and live queries; original cell checks and nested original query checks use the same absolute metric deadline; cooperative, not a hard asynchronous deadline",
        raw_outputs_are_owned_temporary_recomputable_data=True)
    members_result = write(args.out / "result.json", result, args.out)
    pending_cells = coverage.get("remaining_closed_DFS_cells", [])
    necessary_coverage = dict(
        current_root_rank=coverage.get("current_root_rank"),
        current_original_root=coverage.get("current_original_root"),
        remaining_closed_DFS_addresses=[
            dict(rank=row["rank"], dyadic_path=row["dyadic_path"], depth=row["depth"])
            for row in pending_cells],
        untouched_root_rank_suffix=coverage.get("untouched_root_rank_suffix"),
        exact_split_algorithm_source_sha256=SOURCE_PINS[KERNEL_NAME],
        complete_coverage_record=members["coverage_and_pending"],
        full_terminal_unresolved_cells=members.get("complete_cell_ledger"),
        each_pending_cell_reconstructed_by_original_root_and_original_four_closed_splits=True,
        all_other_unfinished_roots_preserved_as_original_rank_suffix=True,
        whole_domain_unpaid_before_root_plan=plan is None)
    summary = dict(schema=SCHEMA + "-necessary-summary", result=members_result,
        **{key:result[key] for key in ("repository", "run_id", "source_commit", "source",
            "completed", "complete_active_partition", "complete_active_relative_operator_bound",
            "complete_two_cap_relative_operator_identity",
            "complete_closed_relative_operator_bound_for_bound_accurate_target",
            "requested_eta_exact", "actual_field_binding_identity", "parameters", "members",
            "counts", "same_actual_C_target", "scope", "resource_stop", "execution_error",
            "elapsed_seconds", "timer_scope")}, complete_pending_addresses=necessary_coverage)
    summary_receipt = write(args.out / "summary.json", summary, args.out)
    if summary_receipt["bytes"] > SUMMARY_LIMIT:
        print(json.dumps(dict(schema=SCHEMA + "-necessary-summary-over-budget",
            original_summary=summary_receipt, limit=SUMMARY_LIMIT,
            necessary_summary_emitted=False, no_chunk_transport_or_raw_deletion=True),
            separators=(",", ":")), flush=True)
        return 70
    print("BEGIN_R426_CURRENT_C_LIVE_QUERY_CLOSED_METRIC_SUMMARY", flush=True)
    print(canonical(summary).decode(), end="", flush=True)
    print("END_R426_CURRENT_C_LIVE_QUERY_CLOSED_METRIC_SUMMARY", flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
            output.write("closed_metric_summary=" + str(args.out / "summary.json") + "\n")
            output.write("closed_metric_summary_bytes=" + str(summary_receipt["bytes"]) + "\n")
            output.write("closed_metric_summary_sha256=" + summary_receipt["sha256"] + "\n")
    return 1 if execution_error is not None else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", type=Path, default=HERE)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--result-sha256", required=True)
    parser.add_argument("--checkpoint-directory", type=Path)
    parser.add_argument("--proof-directory", type=Path)
    parser.add_argument("--cuff-atlas", type=Path, required=True)
    parser.add_argument("--cuff-atlas-sha256", required=True)
    parser.add_argument("--continuous-e-result", type=Path)
    parser.add_argument("--continuous-e-result-sha256")
    parser.add_argument("--eta", required=True)
    parser.add_argument("--interval-bits", type=int, required=True)
    parser.add_argument("--sqrt-bits", type=int, required=True)
    parser.add_argument("--initial-angular-depth", type=int, required=True)
    parser.add_argument("--max-depth", type=int, required=True)
    parser.add_argument("--max-visited-cells", type=int, required=True)
    parser.add_argument("--budget-seconds", type=float, required=True)
    parser.add_argument("--c-query-precision-bits", type=int, required=True)
    parser.add_argument("--c-query-integral-absolute-bits", type=int, required=True)
    parser.add_argument("--c-query-integral-relative-bits", type=int, required=True)
    parser.add_argument("--c-query-analytic-guard-bits", type=int, required=True)
    parser.add_argument("--c-query-integral-evaluation-limit", type=int, required=True)
    parser.add_argument("--c-query-value-width-bits", type=int, required=True)
    parser.add_argument("--c-query-integral-max-depth", type=int, required=True)
    parser.add_argument("--c-query-inverse-max-depth", type=int, required=True)
    parser.add_argument("--c-query-max-panels", type=int, required=True)
    parser.add_argument("--c-query-max-nodes", type=int, required=True)
    parser.add_argument("--c-query-budget-seconds", type=float, required=True)
    parser.add_argument("--out", type=Path, required=True)
    return run(parser.parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
