#!/usr/bin/env python3
"""R462: retain complete old112 far families and truly propagate only new modes.

The original same-job complete112 binding is read by the frozen R456 helper.
The independent R442 full-M deep binding is also read in full. Only their
common original C/cover/cut and one actual physical-far/mu word are joined;
neither old source identity is relabelled. New modes use the frozen complete
Pruefer point_column and original joint numeric-row formation. Every other
radial sample and the whole finite native owner remain fresh.

This sampler has its own result/geometry/config/client/worker source tuple.
It does not mutate published module globals or register itself in an old
refinement driver. All arithmetic is restricted to public Actions. No raw
payload is removed and no native response or BVP acceptance is inferred.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R462-current-C-old112-and-new-M-far-union-fresh-sampling-v1"
GEOMETRY_SCHEMA = "R462-current-C-incremental-M-native-radial-geometry-bundle-v1"
CONFIG_SCHEMA = "R462-current-C-incremental-M-client-config-v1"
READBACK_SCHEMA = "R462-complete-old-new-mode-union-one-necessary-readback-v1"
MODEL = "R286-original-stored-continuous-model-convention-C-v1"
OLD_M, DEPTH = 112, 576
OLD_MODES = list(range(2, 225, 2))
REUSE_NAME = "geometry_20261116_current_C_same_far_registered_resampling.py"
REUSE_SHA = "5f14be90b0e5ae36ee624ece930d46fa1205eee0efcc6e2a97decca15e7011d5"
SAMPLER_NAME = "geometry_20261116_current_C_M_pruefer_joint_radial_sampling.py"
SAMPLER_SHA = "9a85d7d17796ea567cdcfdac567ee531fcf5c225bfe9f57699bbb403aead41c1"
WORKER_NAME = "geometry_20261116_current_C_incremental_M_native_worker.mjs"
CLIENT_NAME = "geometry_20261116_current_C_incremental_M_tail_client.py"
NATIVE_PINS = {
    WORKER_NAME: "b536850a32fb8c26f7bc7a06483a4d3823662ea2fd2a9235e77dbdca069b6b08",
    CLIENT_NAME: "d9db5098b8dbf8ebabb83fb25c060faaa0acf28dd9075654b550bdf07ac5a710",
    "geometry_20261116_current_C_M_general_robin_native.mjs": "fb951f3688673a01b698bb7c606d6a854c061816e139bae55e51a176b4439f8c",
    "geometry_20261116_current_C_M_synchronous_linear_bridge.mjs": "8f189c095ec5bfbc3c323e2421cd98f931931334603ec902a94a75a60a3854de",
    "exact_20261116_current_C_M_general_robin_chain.py": "d4f6d4ffa7f54c38fb251ed72ef7d5bcdd8c5371c99506b0b8d98095506c3737",
    "exact_20261114_tail_capacity_loader.mjs": "07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395",
    "geometry_20261115_pruefer_joint_row_representative.py": "24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "All scientific and comparison arithmetic belongs to this public Actions repository")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode()


def receipt(path):
    path = Path(path)
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1 << 20), b""):
            digest.update(raw); size += len(raw)
    return dict(file=path.name, bytes=size, sha256=digest.hexdigest())


def value_identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=hashlib.sha256(raw).hexdigest())


def load_source(directory, name, expected):
    path = Path(directory)/name
    require(receipt(path)["sha256"] == expected, "A complete original source differs: "+name)
    tag = "_R462_"+name.replace(".", "_")
    spec = importlib.util.spec_from_file_location(tag, path)
    require(spec is not None and spec.loader is not None, "The pinned source has no loader")
    module = importlib.util.module_from_spec(spec); sys.modules[tag] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(tag, None)
        raise
    return module


def requested_modes(value):
    require(type(value) is int and value > OLD_M, "This explicit union requires finite M greater than112")
    return list(range(2, 2*value+1, 2))


class PhaseBudget:
    """Declared phase work stays inside the already running whole-call clock."""
    def __init__(self, base, seconds, limit, label, sampling=False):
        self.base, self.seconds, self.limit, self.label = base, seconds, limit, label
        self.started = time.monotonic(); self.attempts = 0
        self.finished = self.stop = None; self.sampling = sampling

    def check(self):
        self.base.check()
        if time.monotonic()-self.started >= self.seconds:
            self.stop = dict(kind="explicit_phase_wall_budget_reached", label=self.label,
                declared_seconds=self.seconds, actual_attempts=self.attempts)
            self.base.halt("explicit_phase_wall_budget_reached", phase=self.stop)

    def attempt(self):
        self.check()
        if self.attempts >= self.limit:
            self.stop = dict(kind="explicit_phase_work_count_reached", label=self.label,
                declared_count=self.limit, actual_attempts=self.attempts)
            self.base.halt("explicit_phase_work_count_reached", phase=self.stop)
        if self.sampling:
            self.base.attempt()
        self.attempts += 1

    def finish(self):
        if self.finished is None:
            self.finished = time.monotonic()

    def record(self):
        return dict(label=self.label, declared_seconds=self.seconds,
            declared_work_units=self.limit, actual_work_units=self.attempts,
            elapsed_seconds=(self.finished or time.monotonic())-self.started,
            stop=self.stop, contained_in_original_whole_call_and_absolute_deadline=True)


def validate(args, R):
    requested_modes(args.field_modes)
    for key in ("steps", "sample_max_nodes", "max_panels", "max_geometry_cache_records"):
        require(type(getattr(args, key)) is int and getattr(args, key) > 0,
                "An explicit positive finite work count is required: "+key)
    require(64 <= args.precision_bits <= 4096
            and args.precision_bits <= args.representative_max_precision_bits <= 8192
            and 0 <= args.max_depth <= 60 and 0 <= args.sample_inverse_depth <= 60
            and 0 <= args.sample_value_bits <= 1024 and 0 <= args.local_defect_bits <= 1024
            and 1 <= args.taylor_terms <= 256 and Q(0) < args.panel_norm_limit <= Q(1, 4)
            and args.free_bytes_reserve >= 0, "Use the explicit original finite work ranges")
    for key in ("budget_seconds", "linear_budget_seconds", "sampling_budget_seconds"):
        value = getattr(args, key)
        require(type(value) in (int, float) and math.isfinite(value) and value > 0,
                "An explicit positive finite allowance is required: "+key)
    args.code_directory = args.code_directory.resolve(strict=True)
    for key in ("cover_directory", "far_directory", "original_far_directory", "original_sampling_directory"):
        setattr(args, key, R.temporary(getattr(args, key)))
    args.out = R.temporary(args.out, False)
    require(not args.out.exists(), "Use a fresh exclusively owned union output")
    for key in ("cover_directory", "far_directory", "original_far_directory", "original_sampling_directory"):
        old = getattr(args, key)
        require(args.out != old and args.out not in old.parents and old not in args.out.parents,
                "A new output must not contain or be contained in an original input")


def bind_old(args, R, whole, report):
    """Complete old identity is paid with old data, never a new-M replacement."""
    old_args = copy.copy(args)
    old_args.far_directory = args.original_far_directory
    old_args.far_result_sha256 = args.original_far_result_sha256
    old_args.field_modes = OLD_M
    S, runtime, sources, proof = R.load_sampler(args.code_directory, args.original_family, old_args)
    whole.check(); data = S.F.bind_inputs(old_args); whole.check()
    record = dict(runtime=runtime, frozen_sources=sources,
        actual_R380_proof=proof["Pruefer_propagation"], actual_R357_proof=proof["oriented_unit_Robin_rows"],
        actual_original_input_binding=data["binding"], actual_original_scope_conditions=data["facts"])
    report["original112_binding"] = record
    require(data["ready"], "The actual old full C/deep/cut input is not complete")
    old = R.bind_original_far(old_args, record, whole, S, data)
    report["reused_complete_far_modes"] = OLD_MODES
    report["same_original_far_family_reuse"] = copy.deepcopy(old["reuse"])
    # Re-read the one original physical stream, retaining just the full anchor
    # span. Its exact original indices stay in the new-mode tube references.
    desc = old["previous"]["detailed_ledgers"]["sample-inverse-leaves"]
    span = old["far_sample"]["all_closed_inverse_leaves"]
    progress = dict(name="original-complete-far-inverse-anchor", bytes_read=0, physical_lines_read=0)
    report["anchor_read_progress"] = progress
    raw, identity = R.bound_stream(old["original_directory"], desc, whole,
        selected=lambda i:span["first"] <= i < span["stop"], progress=progress)
    require(len(raw) == span["stop"]-span["first"], "Every original far inverse leaf is required")
    leaves = []
    for number, row in enumerate(raw, span["first"]):
        lo, hi = map(Q, row["closed_parameter_interval"])
        require(row["point_index"] == 0 and R.from_word(row["radius_word"]) == old["far"]
                and row["every_original_exact_root_choice_included"] is True
                and row["entire_possible_inverse_fragment_retained"] is True,
                "The old physical far leaf lost its complete original family")
        leaves.append(dict(leaf_row=number, source_piece=row["source_piece"],
            original_source_panel_row=row["original_source_panel_row"], left=lo, right=hi,
            original=row))
    report["original_far_inverse_leaf_namespace"] = dict(directory=str(old["original_directory"]),
        original_ledger=identity, span=copy.deepcopy(span),
        new_mode_far_leaf_indices_refer_to_this_original_ledger=True)
    return old, data, leaves


def bind_union(args, R, S, data, old_data, old, leaves, report, whole):
    """Join common C receipts, not the different old/new deep input bindings."""
    require(data["field_modes"] == args.field_modes and list(data["modes"]) == requested_modes(args.field_modes),
            "The new deep source did not return the actual full requested mode set")
    require(data["core"] == old_data["core"]
            and data["cut"] == old_data["cut"] == Q(old["cut"]),
            "The complete original C binding or actual binary cut changed")
    common = ("actual_cover_result", "actual_cover_input_binding", "actual_complete_source_stream",
              "actual_complete_inverse_stream", "actual_query_plan", "actual_query_results",
              "actual_point_query", "original_binary_cut_exact_rational")
    for key in common:
        require(data["binding"][key] == old_data["binding"][key],
                "A same-job original C/cover/query responsibility changed: "+key)
    whole.check()
    inner = S.F.record_bounds(data["far"]["original_R286_deep_geometry"]["radius"])[1]
    outer = S.F.record_bounds(data["cover"]["natural_outer_radius"])[0]
    require(inner < Q(old["far"]) < data["cut"] <= outer and old["mu"] > 0,
            "The retained actual physical far/cut must remain in every new-M C source domain")
    by_panel, required, after = S.finite_point_required(data, leaves)
    report["finite_far_required_prefix"] = R.write_json(args.out/"required-source-panels.json", dict(
        schema=SCHEMA+"-same-physical-far-required-prefix", actual_physical_radius=R.word(old["far"]),
        actual_mu_word=R.word(old["mu"]), all_possible_inverse_leaves_included=True,
        inverse_leaf_namespace=report["original_far_inverse_leaf_namespace"],
        original_complete_source_stream=data["cover"]["ledgers"]["source_radial_panels"],
        required=[dict(original_source_panel_row=item["panel"]["row"], source_piece=item["panel"]["source_piece"],
            closed_parameter_interval=[str(item["left"]), str(item["right"])]) for item in required],
        complete_not_needed_outer_suffix=after))
    union = dict(schema=SCHEMA+"-union-input-binding", source_sha256=receipt(__file__)["sha256"],
        old112_complete_binding=copy.deepcopy(old_data["binding"]),
        new_complete_M_binding=copy.deepcopy(data["binding"]),
        original_C_input_binding=copy.deepcopy(data["core"]),
        full_same_original_C_cover_and_cut_fields=list(common),
        original112_modes=OLD_MODES, complete_requested_modes=requested_modes(args.field_modes),
        actual_new_modes=requested_modes(args.field_modes)[OLD_M:],
        old112_deep_and_factorized_family_sources_not_relabelled=True,
        all_new_M_deep_conditions_rechecked=True,
        new_deep_old_mode_rows_not_used_as_claimed_fresh_propagations=True,
        physical_far_word=R.word(old["far"]), actual_far_mu_word=R.word(old["mu"]),
        original_far_sample_identity=value_identity(old["far_sample"]),
        original_all112_row_document=copy.deepcopy(old["reuse"]["original_row_document"]),
        original_far_inverse_leaf_namespace=copy.deepcopy(report["original_far_inverse_leaf_namespace"]),
        old_numeric_coefficients_retained_without_reselection=True,
        all_candidate_uncertainty_retained=True, M_changed=True,
        simultaneous_global_C_realization_of_numeric_rows_certified=False,
        nonlinear_response_J_state_factors_or_acceptance_reused=False)
    report["actual_union_input_binding"] = union
    report["union_binding_record"] = R.write_json(args.out/"union-input-binding.json", union)
    return by_panel, required


def new_numeric_rows(args, R, S, rows, old, budget, journal, report):
    """Original N.form, but actual global mode indices instead of suffix index0."""
    result = []; M = args.field_modes
    required_modes = requested_modes(M)[OLD_M:]
    require([row["physical_frequency"] for row in rows] == required_modes
            and all(row["complete"] for row in rows),
            "All new mode families must be complete before numeric formation")
    for position, row in enumerate(rows):
        m = row["physical_frequency"]; index = m//2-1
        selection = dict(mode_index=index, physical_frequency=m,
            complete_old112_and_new_mode_families_required_before_selection=True,
            old_numeric_rows_not_reselected=True, original_joint_formation_source_sha256=S.N_SHA)
        report["numeric_selection_cursor"] = dict(physical_frequency=m,
            remaining_new_modes=required_modes[position:], old112_words_already_bound=True)
        try:
            budget.check()
            require(row["mode_index"] == index and OLD_M <= index < M
                    and row["complete_unit_row_family_enclosed"]
                    and row["physical_far_word"]["f64le"] == R.word(old["far"])["f64le"]
                    and row["mu_word"]["f64le"] == R.word(old["mu"])["f64le"],
                    "The actual new frequency, radius or old momentum-coordinate word differs")
            an, bn = row["full_interval_objects"]["unit_row"]; S.F.finite([an, bn])
            seed = row["first_committed_complete_candidate_nominal_seed"]
            require(seed is not None and seed["physical_frequency"] == m,
                    "The actual committed new-mode seed is absent")
            values, errors = S.N.form(S.F, seed, old["far"], old["mu"], m,
                [an, bn], budget, args.representative_max_precision_bits, selection)
            av, bv = values
            coefficients = []
            for value, box, error in zip((av, bv), (an, bn), errors):
                coefficients.append(dict(actual_word=R.word(value), exact_real_enclosure=S.B.record(box),
                    difference_exact_quantity_minus_numeric_word=S.B.record(error),
                    representative_need_not_lie_in_the_interval=True,
                    representative_is_not_a_selected_exact_root_family_member=True))
            result.append(dict(physical_frequency=m, mode_index=index,
                physical_radius_word=R.word(old["far"]), mu_word=R.word(old["mu"]),
                origin="actual_new_R442_mode_propagated_at_the_original_physical_far_and_mu",
                original_common_orientation="unit family of original Q_F=1 with positive amplitude",
                complete_original_QF_one_unit_row=[S.B.record(an), S.B.record(bn)],
                complete_Q_coefficient=coefficients[0], complete_Pi_coefficient=coefficients[1],
                joint_nominal_selection=selection, candidate_count=row["candidate_count"],
                complete_far_tube_rows=copy.deepcopy(row["complete_far_tube_rows"]),
                complete_far_leaf_coverage_rows=copy.deepcopy(row["complete_far_leaf_coverage_rows"]),
                every_candidate_amplitude_nonzero_and_sign_proved=True,
                every_candidate_Robin_row_norm_strictly_positive_proved=True,
                division_by_far_physical_height=False,
                complete_other_candidates_not_discarded_by_numeric_seed=True,
                simultaneous_global_C_realization_of_numeric_rows_certified=False))
            journal.add(dict(selection, complete_numeric_row=True,
                actual_remaining_new_mode_suffix=required_modes[position+1:]))
        except Exception as failure:
            journal.add(dict(selection, complete_numeric_row=False,
                actual_error=dict(type=type(failure).__name__, message=str(failure)),
                actual_failed_physical_frequency=m,
                actual_remaining_new_mode_suffix=required_modes[position+1:],
                numeric_formation_failure_not_a_family_propagation_failure=True))
            raise
    report["numeric_selection_cursor"] = dict(remaining_new_modes=[], complete=True)
    return result


def materialize_rows(args, R, old, fresh, budget, report):
    M = args.field_modes; K = 2*M
    require(len(fresh) == M-OLD_M, "The complete added-mode row count differs")
    old_rows = old["rows"]["complete_rows"]
    require(len(old_rows) == OLD_M, "All original112 rows must remain present")
    rows, words = [], []
    for index in range(M):
        budget.check(); m = 2*(index+1)
        original = old_rows[index] if index < OLD_M else fresh[index-OLD_M]
        require(original["physical_frequency"] == m, "The explicit union mode order differs")
        qraw = bytes.fromhex(original["complete_Q_coefficient"]["actual_word"]["f64le"])
        praw = bytes.fromhex(original["complete_Pi_coefficient"]["actual_word"]["f64le"])
        q = R.from_word(original["complete_Q_coefficient"]["actual_word"])
        p = R.from_word(original["complete_Pi_coefficient"]["actual_word"])
        require(len(qraw) == len(praw) == 8 and (q != 0 or p != 0), "A complete actual nonzero row is required")
        row = [0.0]*K; row[index] = q; row[M+index] = p
        require(struct.pack("<d", row[index]) == qraw and struct.pack("<d", row[M+index]) == praw,
                "Reindexing must preserve both actual original coefficient words, including negative zero")
        words.extend(row)
        rows.append(dict(mode_index=index, physical_frequency=m,
            origin="retained_original112" if index < OLD_M else "fresh_new_mode",
            original_row_body=copy.deepcopy(original),
            original_row_body_identity=value_identity(original),
            original_row_document=(copy.deepcopy(old["reuse"]["original_row_document"]) if index < OLD_M else None),
            embedded_nonzero_columns=[index, M+index],
            actual_two_word_bytes_unchanged=True, extra_zero_columns_have_exact_zero_error=True,
            complete_old_error_boxes_not_relabelled_as_new_propagation=True))
    report["complete_union_row_summary"] = [dict(mode_index=row["mode_index"],
        physical_frequency=row["physical_frequency"], origin=row["origin"],
        embedded_nonzero_columns=row["embedded_nonzero_columns"],
        Q_word=row["original_row_body"]["complete_Q_coefficient"]["actual_word"]["f64le"],
        Pi_word=row["original_row_body"]["complete_Pi_coefficient"]["actual_word"]["f64le"],
        original_row_body_identity=row["original_row_body_identity"]) for row in rows]
    document = dict(schema=SCHEMA+"-complete-M-general-far-union", field_modes=M,
        physical_radius_word=R.word(old["far"]), mu_word=R.word(old["mu"]), complete_rows=rows,
        original112_full_source=copy.deepcopy(old["reuse"]),
        union_input_binding=report["union_binding_record"],
        every_original_candidate_and_error_retained=True,
        old_Q_Pi_columns_reindexed_at_new_M_without_arithmetic=True,
        original112_matrix_not_copied_into_wrong_Pi_columns=True,
        simultaneous_global_C_realization_of_numeric_rows_certified=False)
    report["complete_union_rows"] = R.write_json(args.out/"complete-M-far-union-rows.json", document)
    return words


def fresh_grid(args, R, S, data, old, matrix, journals, budget, report):
    F, B = S.F, S.B; cb = data["core"]
    head = B.ContinuousHead(cb["physical_parameters"], cb["original_shallow_rows"], cb["original_frozen_warp_alpha"], cb)
    geometry = F.GeometryCache(head, data["panels"], args, journals["coefficient-boxes"], budget)
    sampler = S.InverseSampler(head, data, args, geometry, journals["sample-inverse-leaves"],
        journals["complete-unpaid-scope"], budget)
    anchor = copy.deepcopy(old["far_sample"])
    anchor["point_enclosure_origin"] = dict(kind="retained-original112-same-job-far-anchor",
        original_directory=str(old["original_directory"]), original_result=old["reuse"]["original_result"],
        original_inverse_ledger=report["original_far_inverse_leaf_namespace"],
        all_closed_inverse_leaves=copy.deepcopy(anchor["all_closed_inverse_leaves"]),
        all_interval_errors_and_original_numeric_words_unchanged=True)
    sampler.cache[R.word(old["far"])["f64le"]] = anchor; sampler.point_count = 1
    report["far_point_sample"] = anchor; report["actual_far_coordinate_mu_word"] = R.word(old["mu"])
    nodes, grid, grid_identity = S.radial_grid(old["far"], old["cut"], args.steps, args.field_modes)
    plan = R.write_json(args.out/"actual-radial-field-plan.json", dict(schema=SCHEMA+"-complete-field-plan",
        original_grid_helper=dict(file=SAMPLER_NAME, sha256=SAMPLER_SHA), grid_identity=grid_identity,
        nodes=[R.word(value) for value in nodes], stages=grid))
    report.update(grid_identity=grid_identity, actual_field_plan=plan,
        native_plan_address=dict(phase="nodes", next_node=0, node_stop=577,
            next_stage=0, stage_stop=576, next_field=0, all_fields_required=True, field_plan=plan))
    progress = report["native_plan_address"]; mu, field_words, stage_packets = [], [], []
    field_width = None; fields_done = 0
    try:
        for n, radius in enumerate(nodes):
            progress.update(phase="nodes", next_node=n)
            sample = sampler.sample(radius, "R462-actual-node-"+str(n))
            value = (old["mu"] if R.word(radius)["f64le"] == R.word(old["far"])["f64le"]
                else math.exp(7*math.log(radius)+sample["numerical"]["logw"]))
            require(math.isfinite(value) and value > 0, "The actual new positive node coordinate is unavailable")
            mu.append(value); progress["next_node"] = n+1
        require(struct.pack("<d", mu[-1]) == struct.pack("<d", old["mu"]), "The far coordinate word changed")
        for n, stage in enumerate(grid):
            progress.update(phase="fields", next_stage=n, next_field=0, field_stop=len(stage["fields"]))
            budget.check(); ratio = mu[n]/mu[n+1]
            require(math.isfinite(ratio) and ratio > 0, "The actual new momentum port is unavailable")
            packet = dict(stage=n, rawCell=stage["rawCell"], rawSegment=stage["rawSegment"],
                shootingSubsegment=stage["shootingSubsegment"], fields=[], mu_word=R.word(mu[n+1]),
                output_node_mu_word=R.word(mu[n]), port_ratio_word=R.word(ratio))
            for j, entry in enumerate(stage["fields"]):
                progress["next_field"] = j
                sample = sampler.sample(entry["r_word"]["value"], "R462-stage-"+str(n)+"-field")
                logw = sample["numerical"]["logw"]
                dlog = entry["drdx_word"]["value"]*sample["numerical"]["dlogwdr"]
                require(math.isfinite(dlog), "The actual finite dlogwdx word overflowed")
                actual_dlog = B.exact(Q(entry["drdx_word"]["value"]))*F.as_ball(
                    sample["numerical_word_receipts"]["dlogwdr"]["exact_real_enclosure"])
                journals["numeric-point-values-and-errors"].add(dict(stage=n, field_index=j,
                    x_word=entry["x_word"], r_word=entry["r_word"], drdx_word=entry["drdx_word"],
                    logw_word=R.word(logw), dlogwdx_word=R.word(dlog), same_C_sample=sample,
                    complete_target_dlogwdx=B.record(actual_dlog),
                    target_dlogwdx_minus_actual_numeric_word=B.record(actual_dlog-B.exact(Q(dlog))),
                    finite_derived_numeric_word_not_an_exact_derivative_identity=True))
                packet["fields"].append(dict(x_word=entry["x_word"], point_index=sample["point_index"]))
                field_words.extend([entry["x_word"]["value"], entry["r_word"]["value"],
                    entry["drdx_word"]["value"], logw, dlog])
                fields_done += 1; progress["next_field"] = j+1
                report["complete_native_field_occurrences"] = fields_done
            if field_width is None:
                field_width = len(stage["fields"])
            require(field_width == len(stage["fields"]), "The complete actual stage width differs")
            stage_packets.append(packet); progress.update(next_stage=n+1, next_field=0)
        progress["phase"] = "array_materialization"; budget.check()
        large = args.out/"large-arrays"; M = args.field_modes
        arrays = dict(node_radii=S.raw_array(large/"node-radii.f64le", nodes, [577]),
            node_mu=S.raw_array(large/"node-mu.f64le", mu, [577]),
            field_geometry=S.raw_array(large/"full-stage-field-geometry.f64le", field_words, [576, field_width, 5]),
            far_matrix=S.raw_array(large/"complete-general-far-matrix.f64le", matrix, [M, 2*M]))
        identity = dict(schema=SCHEMA+"-numeric-geometry-identity", sampler_source_sha256=report["source_sha256"],
            actual_union_source_binding=report["union_binding_record"], original_C_model=MODEL,
            actual_radial_field_plan=plan, actual_full_far_union=report["complete_union_rows"],
            complete_native_arrays=arrays, original112_modes_reused=OLD_MODES,
            actual_new_modes_propagated=requested_modes(M)[OLD_M:],
            all_other_grid_points_freshly_enclosed=True,
            exact_global_C_realization_of_numeric_representatives_certified=False,
            finite_evaluator_error_not_paid_by_native_residual=True,
            original_engine_exp_and_exp_twice_logw_rounding_error_certified=False,
            original_engine_must_record_actual_w_w2_E_words=True)
        result = dict(schema=GEOMETRY_SCHEMA, model_schema=MODEL, modes=M, spacing=2, orientation=1,
            stage_count=576, rawNode=[72*i for i in range(9)], cut_radius=old["cut"], finite_far_radius=old["far"],
            native_old_graphs_or_gains_used=False, original_C_input_binding=data["binding"],
            actual_union_input_binding=report["union_binding_record"], numeric_geometry_identity=identity,
            arrays=arrays, stage_packets=stage_packets, field_columns=["x", "r", "drdx", "logw", "dlogwdx"],
            steps_per_stage=args.steps, field_count_per_stage=field_width,
            coordinate_mu_rule="original112 physical-far mu word retained; every other node from fresh original same-C sample",
            finite_far_rows_are_nondividing_approximations_with_bound_error=True,
            exact_global_same_C_and_infinite_nonlinear_DN_not_certified=True,
            far_identity=dict(physical_radius_word=R.word(old["far"]), actual_mu_word=R.word(old["mu"]),
                general_rows=report["complete_union_rows"], complete_all_M_general_matrix=arrays["far_matrix"],
                old112_original_identity=copy.deepcopy(old["geometry"]["far_identity"]),
                actual_new_complete_M_deep_rows=data["far"]["complete_rows"],
                actual_new_R442_proof=data["binding"]["actual_R442_proof"],
                source_scope="old112 complete families plus genuinely propagated new-frequency suffix",
                all_candidate_errors_and_per_mode_source_namespaces_retained=True,
                no_height_division=True))
        report.update(geometry=R.write_json(args.out/"geometry.json", result), completed=True,
            native_geometry_ready=True, complete_unique_sample_points=sampler.point_count,
            freshly_computed_unique_points=sampler.point_count-1,
            numerical_sample_work_resolution_complete=all(row["work_resolution_complete"] for row in sampler.cache.values()))
        progress.update(phase="complete", next_stage=576, next_field=0)
    finally:
        report.update(actual_point_count=sampler.point_count, actual_fresh_point_count=sampler.point_count-1,
            actual_inverse_range_count=sampler.range_count, actual_fresh_coarse_valid_point_leaves=sampler.coarse_count)


def sample(args):
    actions(); started = time.monotonic()
    R = load_source(args.code_directory, REUSE_NAME, REUSE_SHA)
    validate(args, R)
    args.out.mkdir(parents=True); (args.out/"large-arrays").mkdir()
    modes = requested_modes(args.field_modes); suffix = modes[OLD_M:]
    report = dict(schema=SCHEMA, source_sha256=receipt(__file__)["sha256"], target_model_schema=MODEL,
        repository=REPOSITORY, run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        field_modes=args.field_modes, complete_requested_modes=modes, completed=False, native_geometry_ready=False,
        error=None, old_graphs_or_gains_used=False, no_height_division_in_far_rows=True,
        exact_global_C_realization_of_numeric_representatives_certified=False,
        nonlinear_solve_or_DN_computed=False, closed_field_or_BVP_accepted=False,
        old_native_response_J_or_factor_reused=False, M_changed=True,
        reused_complete_far_modes=[], actual_far_modes_attempted=[], actual_far_modes_completed=[],
        actual_not_started_far_modes=suffix, same_original_far_family_reuse=None,
        complete_native_field_occurrences=0, raw_cleanup_performed=False,
        new_caller_registration_required=True,
        native_plan_address=dict(phase="source_binding", all577_nodes_and_all576_stages_unstarted=True,
            requested_steps=args.steps, complete_new_field_plan_not_yet_formed=True),
        requested_work={key:str(getattr(args, key)) if key == "panel_norm_limit" else getattr(args, key)
            for key in ("steps", "precision_bits", "representative_max_precision_bits", "max_panels", "max_depth",
                "local_defect_bits", "panel_norm_limit", "taylor_terms", "max_geometry_cache_records",
                "sample_max_nodes", "sample_inverse_depth", "sample_value_bits", "budget_seconds",
                "linear_budget_seconds", "sampling_budget_seconds", "free_bytes_reserve")})
    whole = linear = sampling = S = None
    journals = {}; rows = []; code = 2
    try:
        absolute, clock = R.bind_clock(args); report.update(clock)
        whole = R.Budget(args, absolute, started); whole.install(); whole.check()
        old, old_data, leaves = bind_old(args, R, whole, report)
        # Finish old live-class binding before the original M loader installs
        # its own runtime tags. Subsequent old evidence is JSON/bytes only.
        S = load_source(args.code_directory, SAMPLER_NAME, SAMPLER_SHA)
        runtime, sources, proof = S.load_runtime(args); whole.check()
        data = S.F.bind_inputs(args); whole.check()
        report.update(runtime=runtime, frozen_sources=sources,
            original_M_sampler=dict(file=SAMPLER_NAME, sha256=SAMPLER_SHA),
            original_reuse_helper=dict(file=REUSE_NAME, sha256=REUSE_SHA),
            actual_R380_proof=proof["Pruefer_propagation"], actual_R357_proof=proof["oriented_unit_Robin_rows"],
            actual_original_input_binding=data["binding"], actual_original_scope_conditions=data["facts"])
        for name in ("coefficient-boxes", "sample-inverse-leaves", "complete-unpaid-scope",
                     "new-mode-accepted-panels", "new-mode-complete-tubes", "new-mode-all-rows",
                     "new-mode-panel-commits", "new-mode-inverse-leaf-coverage",
                     "numeric-point-values-and-errors", "new-mode-numeric-row-selection"):
            journals[name] = S.B.Journal(args.out/"large-arrays"/(name+".jsonl"), args.out)
        unpaid = journals["complete-unpaid-scope"]
        if not data["ready"]:
            unpaid.add(dict(kind="complete-new-M-deep-C-or-cut-scope-unpaid", all_required_modes=modes,
                original112_modes_already_bound=OLD_MODES, actual_new_mode_suffix=suffix,
                original_new_M_scope_conditions=data["facts"], all_native_stages_unstarted=[0, 576],
                missing_C_root_or_mode_conditions_not_assumed=True))
        else:
            by_panel, required = bind_union(args, R, S, data, old_data, old, leaves, report, whole)
            cb = data["core"]
            head = S.B.ContinuousHead(cb["physical_parameters"], cb["original_shallow_rows"],
                cb["original_frozen_warp_alpha"], cb)
            linear = PhaseBudget(whole, args.linear_budget_seconds, args.max_panels, "new-mode-only-finite-far")
            geometry = S.F.GeometryCache(head, data["panels"], args, journals["coefficient-boxes"], linear)
            for index, far in enumerate(data["far_rows"][OLD_M:]):
                m = suffix[index]
                require(far["physical_frequency"] == m and far["mode_index"] == OLD_M+index,
                        "A new deep frequency was substituted or indexed from zero")
                linear.check()
                report["current_new_mode"] = dict(mode_index=OLD_M+index, physical_frequency=m,
                    remaining_new_modes=suffix[index:], original112_complete_family_still_retained=True)
                row = S.point_column(far, data, required, by_panel, geometry, args, linear,
                    journals["new-mode-accepted-panels"], journals["new-mode-complete-tubes"],
                    journals["new-mode-panel-commits"], journals["new-mode-inverse-leaf-coverage"],
                    unpaid, old["far"], old["mu"])
                rows.append(row)
                journals["new-mode-all-rows"].add({key:value for key, value in row.items() if key != "full_interval_objects"})
                report["actual_far_modes_attempted"] = [item["physical_frequency"] for item in rows]
                report["actual_far_modes_completed"] = [item["physical_frequency"] for item in rows if item["complete"]]
                report["actual_not_started_far_modes"] = suffix[len(rows):]
                print(json.dumps(dict(event="R462-new-frequency-far-return", physical_frequency=m,
                    complete=row["complete"], error=row["error"], accepted_panels=row["accepted_panels"])), flush=True)
                if not row["complete_required_far_propagation"]:
                    break
            linear.finish()
            if len(rows) != len(suffix) or not all(row["complete"] for row in rows):
                unpaid.add(dict(kind="R462-complete-M-union-new-mode-suffix-unpaid", all_required_modes=modes,
                    original112_complete_family=OLD_MODES, actual_attempted_new_modes=report["actual_far_modes_attempted"],
                    actual_completed_new_modes=report["actual_far_modes_completed"],
                    actual_not_started_new_modes=suffix[len(rows):],
                    attempted_modes_with_unpaid_units=[row["physical_frequency"] for row in rows if not row["complete"]],
                    original_Mode_rows_hold_complete_pending_and_uncommitted_scope=True,
                    new_native_geometry_not_returned=True))
                code = 75 if whole.stop is not None else 2
            else:
                sampling = PhaseBudget(whole, args.sampling_budget_seconds, args.sample_max_nodes,
                    "new-numeric-rows-and-complete-fresh-grid", sampling=True)
                fresh = new_numeric_rows(args, R, S, rows, old, sampling,
                    journals["new-mode-numeric-row-selection"], report)
                matrix = materialize_rows(args, R, old, fresh, sampling, report)
                fresh_grid(args, R, S, data, old, matrix, journals, sampling, report)
                code = 0
    except Exception as failure:
        code = 75 if isinstance(failure, R.ResourceStop) else 2
        report["error"] = dict(type=type(failure).__name__, message=str(failure),
            resource_partial=isinstance(failure, R.ResourceStop), mathematical_refutation_not_inferred=True)
        if "complete-unpaid-scope" in journals:
            journals["complete-unpaid-scope"].add(dict(kind="R462-union-or-fresh-grid-unfinished",
                error=report["error"], current_new_mode=report.get("current_new_mode"),
                numeric_selection_cursor=report.get("numeric_selection_cursor"),
                complete_native_plan_address=report["native_plan_address"],
                actual_not_started_new_modes=report["actual_not_started_far_modes"],
                original112_reuse_progress=report.get("original112_binding", {}).get("reuse_binding_progress"),
                current_inverse_stack_retained_by_original_sampler_in_same_unpaid_ledger=True))
    finally:
        for budget in (linear, sampling, whole):
            if budget is not None:
                budget.finish()
        if whole is not None:
            whole.restore()
        report.update(detailed_ledgers={key:journal.finish() for key, journal in journals.items()},
            resource_receipt=None if whole is None else whole.record(),
            new_mode_linear_resource=None if linear is None else linear.record(),
            fresh_sampling_resource=None if sampling is None else sampling.record(),
            complete_factorized_new_modes=[row["physical_frequency"] for row in rows if row["complete_required_far_propagation"]],
            complete_unit_new_modes=[row["physical_frequency"] for row in rows if row["complete"]],
            elapsed_seconds=time.monotonic()-started, internal_exit_code=code,
            old112_propagation_work_not_added_to_new_attempt_counts=True,
            raw_owned_temporary_only=True, new_nonlinear_acceptance_gate=False)
        rid = R.write_json(args.out/"result.json", report)
        print(json.dumps(dict(event="R462-complete-M-union-returned", result=rid,
            completed=report["completed"], native_geometry_ready=report["native_geometry_ready"],
            original112_reused=report["reused_complete_far_modes"],
            actual_new_modes_attempted=report["actual_far_modes_attempted"],
            internal_exit_code=code, error=report["error"])), flush=True)
    return code


def configure(args):
    actions(); R = load_source(args.computations, REUSE_NAME, REUSE_SHA)
    directory = R.temporary(args.directory); out = R.temporary(args.out, False)
    require(not out.exists(), "Use a fresh explicit union native configuration")
    report, rid = R.read_json(directory/"result.json", args.result_sha256); R.actual_identity(report)
    require(report.get("schema") == SCHEMA and report.get("source_sha256") == receipt(__file__)["sha256"]
            and report.get("completed") is True and report.get("native_geometry_ready") is True,
            "Only this actual complete union sampling result can configure a new native owner")
    cfg, cid = R.read_json(R.temporary(args.original_config), args.original_config_sha256)
    require(cfg.get("schema") == "current-C-complete112-client-config-v1"
            and cfg.get("model_schema") == MODEL and cfg.get("repository") == REPOSITORY,
            "Use the actual original112 native configuration associated with retained far rows")
    original, pid = R.read_json(R.temporary(cfg["geometry_directory"])/"result.json", cfg["geometry_result_sha256"])
    R.actual_identity(original)
    require(R.same_payload(pid, report["same_original_far_family_reuse"]["original_result"]),
            "The original configuration and retained complete far source differ")
    comp = args.computations.resolve(strict=True)
    require(comp == Path(cfg["computations"]).resolve(strict=True), "The source directory changed")
    for name, expected in cfg["source_sha256"].items():
        require(Path(name).name == name and receipt(comp/name)["sha256"] == expected,
                "An original source differs: "+name)
    M = report["field_modes"]
    require(type(args.quadrature) is int and args.quadrature % 2 == 0 and args.quadrature > 8*M,
            "Use the original full-angle quadrature condition for the actual new M")
    new = copy.deepcopy(cfg)
    for name, expected in NATIVE_PINS.items():
        require(receipt(comp/name)["sha256"] == expected, "An actual complete-M source differs: "+name)
        new["source_sha256"][name] = expected
    require(receipt(comp/Path(__file__).name)["sha256"] == report["source_sha256"], "The union sampler source differs")
    new["source_sha256"][Path(__file__).name] = report["source_sha256"]
    geometry, gid = R.member(directory, report["geometry"])
    new.update(schema=CONFIG_SCHEMA, field_modes=M, geometry_directory=str(directory),
        geometry_result_sha256=rid["sha256"], quadrature=args.quadrature, steps=geometry["steps_per_stage"],
        R462_actual_union_origin=dict(original112_config=cid, original112_sampling=pid,
            actual_union_sampling=rid, actual_union_geometry=gid,
            original112_complete_families_and_mu_preserved=True, new_M_deep_and_added_families_fresh=True,
            every_new_native_response_J_mean_and_factor_must_be_fresh=True,
            original_M_native_bridge_QR_math_unchanged=True,
            current_R442_R457_refinement_driver_source_registration_still_required=True))
    out.parent.mkdir(parents=True, exist_ok=True)
    row = R.write_json(out, new)
    print(json.dumps(dict(event="R462-complete-M-native-configuration-created", configuration=row,
        client=CLIENT_NAME, field_modes=M, no_native_call_performed=True)), flush=True)
    return 0


def readback(args):
    actions(); R = load_source(args.computations, REUSE_NAME, REUSE_SHA)
    directory = R.temporary(args.directory); out = R.temporary(args.out, False)
    require(not out.exists(), "Use a fresh necessary-readback directory"); out.mkdir(parents=True)
    report, rid = R.read_json(directory/"result.json", args.result_sha256); R.actual_identity(report)
    require(report.get("schema") == SCHEMA and report.get("source_sha256") == receipt(__file__)["sha256"],
            "Read the actual independently sourced union producer")
    keys = ("target_model_schema", "repository", "run_id", "source_commit", "source_sha256", "field_modes",
        "complete_requested_modes", "completed", "native_geometry_ready", "error", "internal_exit_code", "elapsed_seconds",
        "M_changed", "actual_origin_launch", "actual_job_deadline", "original_clock", "requested_work",
        "actual_original_scope_conditions", "reused_complete_far_modes", "actual_far_modes_attempted",
        "actual_far_modes_completed", "actual_not_started_far_modes", "complete_factorized_new_modes", "complete_unit_new_modes",
        "resource_receipt", "new_mode_linear_resource", "fresh_sampling_resource", "native_plan_address",
        "current_new_mode", "numeric_selection_cursor", "complete_native_field_occurrences", "complete_unique_sample_points",
        "freshly_computed_unique_points", "actual_point_count", "actual_fresh_point_count", "actual_inverse_range_count",
        "actual_fresh_coarse_valid_point_leaves", "numerical_sample_work_resolution_complete", "union_binding_record",
        "finite_far_required_prefix", "complete_union_rows", "complete_union_row_summary", "original_far_inverse_leaf_namespace",
        "anchor_read_progress", "actual_far_coordinate_mu_word", "actual_field_plan", "old_native_response_J_or_factor_reused",
        "old112_propagation_work_not_added_to_new_attempt_counts", "raw_cleanup_performed", "new_caller_registration_required")
    necessary = {key:copy.deepcopy(report[key]) for key in keys if key in report}
    old_binding = report.get("original112_binding")
    if old_binding is not None:
        necessary["original112_binding_scope"] = {
            key:copy.deepcopy(old_binding[key]) for key in (
                "actual_R380_proof", "actual_R357_proof", "actual_original_scope_conditions")
            if key in old_binding}
        if "actual_original_input_binding" in old_binding:
            necessary["original112_binding_scope"]["complete_input_binding_identity"] = value_identity(
                old_binding["actual_original_input_binding"])
    old = report.get("same_original_far_family_reuse")
    if old is not None:
        selected = ("complete", "original_family", "original_result", "original_geometry", "original_row_document",
            "original_far_matrix", "original_node_mu", "original_required_prefix", "original_far_inverse_span",
            "physical_far_word", "mu_word", "frozen_far_sample_and_mu_words", "original_modes", "full_root_family_not_narrowed")
        necessary["actual_original112_family"] = {key:copy.deepcopy(old[key]) for key in selected if key in old}
        necessary["original112_complete_ledger_identities"] = {name:value["descriptor"]
            for name, value in old["original_ledger_identities"].items()}
    elif report.get("original112_binding") is not None:
        necessary["original112_binding_progress"] = report["original112_binding"].get("reuse_binding_progress")
    identities, unpaid, new_modes = {}, [], []
    for name, desc in report["detailed_ledgers"].items():
        chosen, actual = R.bound_stream(directory, desc, ReadbackBudget(),
            selected=None if name in ("complete-unpaid-scope", "new-mode-all-rows") else lambda _:False)
        identities[name] = actual
        if name == "complete-unpaid-scope":
            unpaid = chosen
        if name == "new-mode-all-rows":
            for row in chosen:
                fields = ("physical_frequency", "mode_index", "complete", "complete_required_far_propagation",
                    "complete_unit_row_family_enclosed", "error", "candidate_count", "complete_unit_row_count",
                    "row_norm_unproved_count", "complete_step_rows", "complete_far_tube_rows",
                    "complete_panel_commit_rows", "complete_far_leaf_coverage_rows", "uncommitted_written_step_span",
                    "uncommitted_written_far_span", "required_leaf_count", "completed_leaf_count",
                    "complete_pending_scope", "uncommitted_transaction", "accepted_panels", "valid_coarse_panels")
                new_modes.append({key:row[key] for key in fields if key in row})
    necessary["complete_new_mode_status"] = new_modes
    necessary["complete_unpaid_records"] = unpaid
    necessary["complete_generated_ledger_identities"] = identities
    if "complete_union_rows" in report:
        union, uid = R.member(directory, report["complete_union_rows"])
        require(union["schema"] == SCHEMA+"-complete-M-general-far-union"
                and union["field_modes"] == report["field_modes"]
                and len(union["complete_rows"]) == report["field_modes"],
                "The full actual old/new row document differs")
        necessary["actual_complete_union_row_document"] = dict(identity=uid,
            all_original_row_and_error_bodies_read=True,
            all_row_body_text_transported=False,
            no_scientific_row_formation_recomputed=True)
    if "geometry" in report:
        geometry, gid = R.member(directory, report["geometry"])
        for desc in geometry["arrays"].values():
            require(R.same_payload(R.receipt(R.contained(directory, desc["file"])), desc),
                    "A complete generated array byte identity differs")
        necessary["actual_complete_geometry"] = dict(identity=gid, arrays=geometry["arrays"],
            modes=geometry["modes"], steps_per_stage=geometry["steps_per_stage"],
            field_count_per_stage=geometry["field_count_per_stage"])
    summary = dict(schema=READBACK_SCHEMA, producer_result=rid, original=necessary,
        missing_original_keys_not_filled=True, complete_successful_candidate_and_error_bodies_retained_at_original_paths=True,
        large_propagation_and_point_arrays_hashed_not_independently_recomputed=True,
        no_raw_cleanup_performed=True, no_new_scientific_gate=True)
    raw = canonical(summary); ident = R.write_json(out/"summary.json", summary)
    if len(raw) > 90000:
        print(json.dumps(dict(event="R462-necessary-readback-over-budget", summary=ident,
            complete_necessary_transported=False, original_raw_retained=True, no_encoded_or_split_transport=True)), flush=True)
        return 70
    print("BEGIN_R462_INCREMENTAL_M_FAR_UNION_NECESSARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R462_INCREMENTAL_M_FAR_UNION_NECESSARY", flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
            stream.write("incremental_M_far_summary="+str((out/"summary.json").resolve())+"\n")
            stream.write("incremental_M_far_summary_bytes="+str(ident["bytes"])+"\n")
            stream.write("incremental_M_far_summary_sha256="+ident["sha256"]+"\n")
    return 0


class ReadbackBudget:
    # Metadata readback is owned and externally timed by the caller. It never
    # consumes an expired scientific clock or starts new arithmetic work.
    def check(self):
        return None


def parser():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    p = sub.add_parser("sample")
    for key in ("cover-directory", "far-directory", "original-far-directory", "original-sampling-directory",
                "code-directory", "proof", "mode-extension-proof", "unit-row-proof",
                "origin-launch-directory", "job-deadline", "out"):
        p.add_argument("--"+key, type=Path, required=True)
    for key in ("cover-result-sha256", "far-result-sha256", "original-far-result-sha256",
                "original-sampling-result-sha256", "origin-launch-result-sha256", "job-deadline-sha256"):
        p.add_argument("--"+key, required=True)
    p.add_argument("--original-family", choices=("positive", "joint"), required=True)
    for key in ("field-modes", "steps", "precision-bits", "representative-max-precision-bits", "max-panels", "max-depth",
                "local-defect-bits", "taylor-terms", "max-geometry-cache-records", "sample-max-nodes",
                "sample-inverse-depth", "sample-value-bits", "free-bytes-reserve"):
        p.add_argument("--"+key, type=int, required=True)
    p.add_argument("--panel-norm-limit", type=Q, required=True)
    for key in ("budget-seconds", "linear-budget-seconds", "sampling-budget-seconds"):
        p.add_argument("--"+key, type=float, required=True)
    p = sub.add_parser("configure")
    for key in ("directory", "original-config", "computations", "out"):
        p.add_argument("--"+key, type=Path, required=True)
    for key in ("result-sha256", "original-config-sha256"):
        p.add_argument("--"+key, required=True)
    p.add_argument("--quadrature", type=int, required=True)
    p = sub.add_parser("readback")
    for key in ("directory", "computations", "out"):
        p.add_argument("--"+key, type=Path, required=True)
    p.add_argument("--result-sha256", required=True)
    return parser


def main(argv=None):
    args = parser().parse_args(argv)
    return {"sample":sample, "configure":configure, "readback":readback}[args.operation](args)


if __name__ == "__main__":
    raise SystemExit(main())
