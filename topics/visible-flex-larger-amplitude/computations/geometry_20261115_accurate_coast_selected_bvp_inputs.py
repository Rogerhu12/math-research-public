#!/usr/bin/env python3
"""Bind one actual request180 selected accurate coast point to original179 BVP inputs.

This is an Actions-only source/parameter adapter.  It does not create an
accepted field, regenerate scientific data, import a numerical library, run
a solver, or turn a parameter projection into an accurate-domain certificate.
The original factory must have actually run with the selected recipe in this
same job.  Its result is consumed verbatim; no old factory result is forged.
R383 semantic equality transfers the actual selected full-root-family domain
statement across independently bound enclosure runs.  New interval boxes and
numerical shadows are never substituted for the old exact target or proof.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "actual-accurate-coast-selected-words-to-original-current-BVP-inputs-v1"
SELECTION_SCHEMA = "request180-accurate-R323-coast-three-coefficient-repair-v1"
FACTORY_NAME = "geometry_20261115_continuous_nine_scalar_factory_v3.py"
FACTORY_SHA = "0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
FACTORY_SCHEMA = "R300-continuous-nine-scalar-v3-cut-exact-expression-construction-v1"
MODEL_SCHEMA = "R300-new-continuous-nine-target-family-v3-cut-v1"
MODEL_RECIPE_SCHEMA = "R300-new-continuous-nine-scalar-model-recipe-v1"
BVP_RECIPE_SCHEMA = "explicit-current-C-riccati-R300-v3-three-active-complete453-recipe-v1"
BVP_TEMPLATE_NAME = "current-C-riccati-full453-physical-DN179-recipe.json"
BVP_TEMPLATE_SHA = "d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811"
BVP_SOURCE_COMMIT = "ccf1b02341f365e4b6eff5d5eeeba9be2b0487ad"
PARAMETERS = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3"]
DIRECT_SOURCES = {
    FACTORY_NAME: FACTORY_SHA,
    "geometry_20261115_continuous_nine_scalar_numeric_v3.py":
        "7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60",
    "geometry_20261115_continuous_C_full112_binding.py":
        "c0bda3350b30b9659c326112eaf8f411d0bb6f825a7a3f81fcc6c7502ed3f952",
    "geometry_20261115_current_C_riccati_full453_physical_dn.py":
        "76c51a05c8ce40f78225aa3bfbd5db2b1ac39e0d6fb7f8b84f02e0dfaafd122f",
}
# R383 identifies the exact family independently of a particular enclosure run.
# The old and fresh evidence objects remain separately bound in full.  In
# particular, enclosure widths, runtime paths and proof timings are not target
# coefficients, and equality of those objects is not a domain-transfer premise.
MATHEMATICAL_KEYS = (
    "schema", "source_sha256", "exact_definition", "parameter_order",
    "expression_nodes", "pieces", "three_true_supports",
    "derived_expression_roots", "chosen_root_scope",
    "polynomial_coefficients_are_expressions_not_cut_interval_midpoints",
    "accurate_cumulative_radius_not_reset_to_old_a0",
    "no_early_segment_mask_or_primal_clip",
    "true_derivatives_from_the_same_radius_expression",
    "natural_outer_radius_not_flat_extended",
    "original_finite_Gauss_target_identified_with_this_new_family",
)
C_SOURCE_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
C_BASE_SHA = "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed"
C_UNIT_SHA = "004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea"
CUT_READER_SHA = "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed"
CORE_JET_SHA = "a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703"
C_MODEL_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
SEMANTIC_TRANSFER_BASIS = dict(
    result="R383-accurate-R323-target-identity-and-coast-control-necessary-band.md",
    sha256="71b1b3061c0cf613237fa2fb1f6fc622f267f353e9e3486376ca63d6f058b4ed",
    new_theorem_or_new_scientific_acceptance_gate=False)

class NoDirectSelection(Exception):
    """A source-scope result, not an original nonlinear rejection."""

def require_actions():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise RuntimeError("Execute source/word binding only in the public repository Actions job")

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate original JSON key: " + key)
        result[key] = value
    return result

def read_json(path, expected):
    path = Path(path)
    raw = path.read_bytes()
    if digest(raw) != expected:
        raise ValueError("Complete original file SHA differs: " + str(path))
    value = json.loads(raw, object_pairs_hook=unique,
                       parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    return value, dict(file=str(path), bytes=len(raw), sha256=digest(raw))

def check_descriptor(receipt, descriptor, label):
    if not isinstance(descriptor, dict):
        raise ValueError(label + " must have an actual complete descriptor")
    if descriptor.get("bytes") != receipt["bytes"] or descriptor.get("sha256") != receipt["sha256"]:
        raise ValueError(label + " complete original bytes differ")

def safe_member(root, descriptor):
    if not isinstance(descriptor, dict) or not isinstance(descriptor.get("file"), str):
        raise ValueError("A complete original factory descriptor is required")
    root = Path(root).resolve()
    path = (root / descriptor["file"]).resolve()
    if path == root or not path.is_relative_to(root):
        raise ValueError("An original factory member escapes its temporary root")
    data, receipt = read_json(path, descriptor["sha256"])
    check_descriptor(receipt, descriptor, "factory member")
    return data, receipt

def q(value):
    if isinstance(value, bool):
        raise ValueError("A boolean is not a coefficient")
    if isinstance(value, str):
        return Q(value)
    if isinstance(value, int):
        return Q(value)
    if isinstance(value, float) and math.isfinite(value):
        return Q.from_float(value)
    raise ValueError("Use the complete original exact rational or finite word")

def nine_rationals(values, label):
    if not isinstance(values, list) or len(values) != 9:
        raise ValueError(label + " must preserve all nine coefficients")
    return [q(value) for value in values]

def parameter_projection(selected):
    exact = nine_rationals(selected["nine_parameters_exact"], "selected accurate point")
    projection = selected["binary64_projection"]
    rows = projection["parameters"]
    if not isinstance(rows, list) or len(rows) != 9:
        raise ValueError("Read every original coefficient projection row")
    output = []
    checked = []
    any_nonzero = False
    for index, (name, expected, row) in enumerate(zip(PARAMETERS, exact, rows)):
        if row.get("parameter") != name or q(row["accurate_rational"]) != expected:
            raise ValueError("The selected exact coefficient order differs")
        word = row["binary64_word"]
        if not isinstance(word, str) or len(word) != 16:
            raise ValueError("Preserve each original finite binary64 word")
        binary = bytes.fromhex(word)
        value = struct.unpack("<d", binary)[0]
        if not math.isfinite(value):
            raise ValueError("The original projection is nonfinite")
        literal = row["binary64_value"]
        if isinstance(literal, bool) or not isinstance(literal, (float, int)):
            raise ValueError("A finite original projection literal is required")
        if struct.pack("<d", float(literal)) != binary:
            raise ValueError("Original projection literal and word differ")
        represented = Q.from_float(value) == expected
        difference = Q.from_float(value) - expected
        if (type(row.get("represented_exactly")) is not bool
                or row["represented_exactly"] != represented
                or q(row["exact_projection_difference"]) != difference):
            raise ValueError("Original projection identity fields differ")
        any_nonzero |= not represented
        checked.append(dict(parameter=name, accurate_rational=str(expected),
                            binary64_word=word, represented_exactly=represented,
                            exact_projection_difference=str(difference)))
        output.append(value)
    if type(projection.get("all_nine_exactly_representable")) is not bool:
        raise ValueError("Keep the producer's complete projection classification")
    if projection["all_nine_exactly_representable"] != (not any_nonzero):
        raise ValueError("The complete original projection classification differs")
    return output, exact, checked, not any_nonzero

def checked_sources(directory, selection_source, selection_source_sha):
    out = {}
    for name, expected in DIRECT_SOURCES.items():
        path = Path(directory) / name
        raw = path.read_bytes()
        if digest(raw) != expected:
            raise ValueError("Actual unchanged direct source differs: " + name)
        out[name] = dict(bytes=len(raw), sha256=expected)
    raw = Path(selection_source).read_bytes()
    if digest(raw) != selection_source_sha:
        raise ValueError("The actual selection producer source differs")
    out[Path(selection_source).name] = dict(bytes=len(raw), sha256=selection_source_sha)
    return out

def exact_number_tree(value):
    """Compare original JSON numbers as their exact stored rational values."""
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return {"exact_original_number": str(q(value))}
    if isinstance(value, list):
        return [exact_number_tree(x) for x in value]
    if isinstance(value, dict):
        return {key: exact_number_tree(item) for key, item in value.items()}
    raise ValueError("An original mathematical JSON field has an unsupported type")

def byte_identity(value, label):
    """Retain full original byte identity without treating a path as a scalar."""
    if not isinstance(value, dict):
        raise ValueError("Missing complete original byte descriptor: " + label)
    size, sha = value.get("bytes"), value.get("sha256")
    if (type(size) is not int or size < 0 or not isinstance(sha, str)
            or len(sha) != 64 or any(c not in "0123456789abcdef" for c in sha)):
        raise ValueError("Invalid complete original byte descriptor: " + label)
    result = dict(bytes=size, sha256=sha)
    for key in ("decoded_bytes", "decoded_sha256", "encoding"):
        if key in value:
            result[key] = value[key]
    return result

def required_fields(value, keys, label):
    if not isinstance(value, dict):
        raise ValueError("Missing original object: " + label)
    result = {}
    for key in keys:
        if key not in value:
            raise ValueError("Missing original field: " + label + "/" + key)
        result[key] = value[key]
    return result

def complete_object_identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=digest(raw))

def accurate_C_signature(definition):
    tail = definition["continuous_tail"]
    binding = tail["actual_input_binding"]
    convention = binding["convention"]
    if (tail.get("source_sha256") != C_SOURCE_SHA
            or tail.get("preserved_original_source_sha256") != C_BASE_SHA
            or tail.get("preserved_unit_panel_source_sha256") != C_UNIT_SHA
            or tail.get("actual_cut_twojet_readout_source_sha256") != CUT_READER_SHA
            or tail.get("actual_cut_twojet_readout_schema") !=
                "R286-v3-original-binary-cut-complete-twojet-hull-v1"
            or binding.get("schema") != "R286-original-stored-convention-C-continuous-E-cover-v3-input-binding"
            or binding.get("source_sha256") != C_SOURCE_SHA
            or convention.get("schema") != C_MODEL_SCHEMA
            or convention.get("deep_definition") != "original-exact-root-family"
            or tail.get("semantic_leaves") != ["E(R)", "dE/dr(R)", "d2E/dr2(R)"]
            or tail.get("coefficient_midpoints_substituted") is not False
            or tail.get("original_producer_encloses_every_admissible_root_sequence") is not True
            or binding.get("original_real_profile_and_model_C_unchanged") is not True):
        raise ValueError("Retain the original same-C semantic leaves and complete root family")
    true_flags = (
        "explicit_model_layer_choice", "binary_inputs_are_exact_dyadics",
        "dependent_delta_c_mu_and_radius_are_real_relations_not_independent_rounded_words",
        "shallow_alpha_and_R_are_original_saved_dyadics",
        "deep_bounds_valid_for_every_original_root_in_half_to_two", "root_existence_proved")
    false_flags = (
        "global_lambda_reselected", "natural_outer_radius_reidentified_as_nominal_cut",
        "deep_roots_numerically_selected_or_computed",
        "old_finite_selector_certified_as_this_continuous_model",
        "R26_rational_deep_or_numerical_certificate_used")
    if (any(convention.get(key) is not True for key in true_flags)
            or any(convention.get(key) is not False for key in false_flags)):
        raise ValueError("The all-root real convention was changed or narrowed")
    cut = q(definition["cut_radius"])
    physical = binding["physical_parameters"]
    original_cut = tail["original_binary_cut"]
    query = tail["selected_complete_query"]
    if (q(tail["cut_radius"]) != cut or q(physical["rCut"]) != cut
            or q(original_cut["exact_rational"]) != cut
            or original_cut.get("query_value_not_renormalised") is not True
            or query.get("id") != "original-binary-config-cut-point"
            or query.get("index") != 0
            or query.get("kind") != "closed-rational-radius-interval"
            or query.get("left_closed") is not True
            or query.get("right_closed") is not True
            or q(query["left"]) != cut or q(query["right"]) != cut
            or q(tail["cuff_radius"]) != q(physical["rCuff"])):
        raise ValueError("The semantic query-cut or original physical coordinate changed")
    original_inputs = {
        key: byte_identity(binding[key], "C original " + key)
        for key in ("config", "calibration_ledger", "stored_reference")}
    source_fields = {
        key: byte_identity(binding[key], key)
        for key in ("preserved_original_producer_source",
                    "preserved_unit_panel_producer_source", "proof")}
    if (source_fields["preserved_original_producer_source"]["sha256"] != C_BASE_SHA
            or source_fields["preserved_unit_panel_producer_source"]["sha256"] != C_UNIT_SHA):
        raise ValueError("The original C implementation ancestry changed")
    formula_sources = {
        key: byte_identity(value, "C source " + key)
        for key, value in binding["original_sources"].items()}
    mathematical = required_fields(binding, (
        "original_source_revision", "physical_parameters",
        "original_frozen_warp_alpha", "original_shallow_rows",
        "original_profile_fingerprint", "original_finite_head_fingerprint",
        "original_calibration_table_interpretation", "convention"), "C binding")
    if len(mathematical["original_shallow_rows"]) != 160 or not formula_sources:
        raise ValueError("Keep the complete original finite head and formula sources")
    return dict(
        source_sha256=C_SOURCE_SHA, ancestry_and_proof=source_fields,
        original_three_inputs=original_inputs, original_formula_sources=formula_sources,
        original_mathematical_fields=exact_number_tree(mathematical),
        cut_query=dict(id=query["id"], index=0, kind=query["kind"],
            left=str(cut), right=str(cut), left_closed=True, right_closed=True),
        semantic_leaves=tail["semantic_leaves"],
        source_declares_all_original_root_choices=True,
        coefficient_midpoints_substituted=False)

def accurate_core_signature(definition):
    core = definition["core_input"]
    selected = core.get("selected_geometry_canonical_sha256")
    if (not isinstance(selected, str) or len(selected) != 64
            or any(c not in "0123456789abcdef" for c in selected)
            or not isinstance(core.get("geometry_pointer"), str)):
        raise ValueError("Bind the actual exact selected core geometry and pointer")
    source = byte_identity(core["original_exact_shared_jet_source"], "exact core jet source")
    if source["sha256"] != CORE_JET_SHA:
        raise ValueError("Do not change the original exact shared core construction")
    return dict(selected_geometry_canonical_sha256=selected,
        geometry_pointer=core["geometry_pointer"], original_exact_shared_jet_source=source)

def accurate_recipe_signature(recipe):
    if (recipe.get("schema") != MODEL_RECIPE_SCHEMA
            or recipe.get("parameter_order") != PARAMETERS
            or recipe.get("collar_mode") != "cut-cubic-jet-collar"
            or recipe.get("root_choice") not in (
                "R286-dovetailed-rational-middle-third",
                "uniform-original-admissible-root-family")):
        raise ValueError("Keep the explicit original exact R323 recipe")
    return dict(schema=recipe["schema"], parameter_order=PARAMETERS,
        collar_mode=recipe["collar_mode"], root_choice=recipe["root_choice"],
        nine_parameters=[str(x) for x in nine_rationals(recipe["nine_parameters"], "recipe")],
        exact_constants={key: str(q(recipe[key])) for key in (
            "core_end", "cut_radius", "kappa", "collar_width",
            "first_transition_width", "last_transition_width")},
        first_support={key: str(q(recipe["first_support"][key]))
                       for key in ("left", "stored_width")})

def same_accurate_definition(selected_definition, factory_definition, recipe):
    signatures = []
    for value in (selected_definition, factory_definition):
        if value.get("schema") != MODEL_SCHEMA or value.get("source_sha256") != FACTORY_SHA:
            raise ValueError("Use the original accurate v3 expression definition")
        if value.get("parameter_order") != PARAMETERS:
            raise ValueError("Keep the complete original nine-control order")
        signature = required_fields(value, MATHEMATICAL_KEYS, "accurate definition")
        signature["nine_parameters"] = [
            str(x) for x in nine_rationals(value["nine_parameters"], "definition")]
        signature["core_end"] = str(q(value["core_end"]))
        signature["cut_radius"] = str(q(value["cut_radius"]))
        signature["continuous_C_semantics"] = accurate_C_signature(value)
        signature["selected_exact_core"] = accurate_core_signature(value)
        signature["published_structural_and_effective_scope_proof"] = byte_identity(
            value["published_structural_and_effective_scope_proof"], "R300 proof")
        signatures.append(signature)
    checked = {}
    for key, left in signatures[0].items():
        if canonical(left) != canonical(signatures[1][key]):
            raise ValueError("Fresh original factory changes the selected accurate target: " + key)
        checked[key] = dict(equal=True, canonical_sha256=digest(canonical(left)))
    recipe_signature = accurate_recipe_signature(recipe)
    if (recipe_signature["nine_parameters"] != signatures[0]["nine_parameters"]
            or recipe_signature["exact_constants"]["core_end"] != signatures[0]["core_end"]
            or recipe_signature["exact_constants"]["cut_radius"] != signatures[0]["cut_radius"]
            or recipe_signature["root_choice"] != signatures[0]["chosen_root_scope"]):
        raise ValueError("The common actual recipe differs from the accurate definition")
    checked["same_bound_exact_recipe"] = dict(
        equal=True, canonical_sha256=digest(canonical(recipe_signature)))
    return checked

def actual_definition_evidence(value):
    """No comparison of these run-specific evidence objects is made."""
    tail = value["continuous_tail"]
    return dict(
        complete_continuous_tail=complete_object_identity(tail),
        complete_actual_C_input_binding=complete_object_identity(tail["actual_input_binding"]),
        original_core_input=deepcopy(value["core_input"]),
        original_model_recipe_input=deepcopy(value["model_recipe_input"]),
        continuous_tail_original_receipts=required_fields(tail, (
            "actual_result", "input_binding", "original_query_plan", "original_query_results",
            "original_complete_leaf_ledger", "actual_complete_cut_twojet_readout",
            "original_readout_run_id", "original_readout_source_commit"), "tail evidence"),
        actual_enclosure_leaves=complete_object_identity(value["actual_enclosure_leaves"]),
        construction_conditions=complete_object_identity(value["construction_conditions"]),
        original_all_strict_construction_conditions_flag=
            value["construction_conditions"].get("all_strict_conditions_proved"),
        old_or_fresh_boxes_used_as_new_target_coefficients=False)

def bind(args, report):
    report["actual_sources"] = checked_sources(
        args.code_directory, args.selection_source, args.selection_source_sha256)
    selection, selection_receipt = read_json(args.selection_summary, args.selection_summary_sha256)
    report["actual_selection_summary"] = selection_receipt
    if selection.get("schema") != SELECTION_SCHEMA:
        raise ValueError("Use the actual coast-selection summary and its own schema")
    selected = selection.get("selected_profile")
    if selected is None:
        raise NoDirectSelection("The actual producer selected no complete-domain coast point")
    if not isinstance(selected, dict):
        raise ValueError("The original selected profile is not a complete record")
    if (selection.get("request_number") != 180
            or selection.get("full_accurate_nine_domain_proved") is not True
            or selected.get("semantic_C_remains_original_all_root_family") is not True
            or selected.get("full_length_expression_unchanged") is not True):
        raise ValueError("Retain the original successful complete419-domain selection scope")
    outside = selection["all418_unchanged_piece_domain"]
    geometry = selection["unchanged_target_geometry"]
    if (outside.get("complete") is not True
            or geometry.get("complete_accurate_piece_count") != 419
            or geometry.get("coast_piece") != 416
            or geometry.get("unchanged_piece_count") != 418):
        raise ValueError("The actual selected proof does not retain the original complete419 scope")
    report["original_selected_full419_domain_assertion"] = dict(
        producer_flag=True, original_producer_source_bound=True,
        interpreted_only_under_original_selection_source=True,
        original_all418_unchanged_piece_domain_complete=True,
        original_complete_coast_and_whole419_assertion_from_selected_producer=True,
        complete_accurate_piece_count=419, coast_piece=416, unchanged_piece_count=418,
        all_original_C_root_choices_in_scope=True,
        complete_leaf_ledger_independently_recomputed_here=False,
        selected_point_is_not_a_BVP_solution=True)
    if (selected.get("factory_source_sha256") != FACTORY_SHA
            or selected.get("new_selection_source_sha256") != args.selection_source_sha256
            or selected.get("continuous_model_schema") != MODEL_SCHEMA
            or selected.get("parameter_order") != PARAMETERS):
        raise ValueError("The original selection source, target, or parameter order differs")
    if q(selection["selected_beta_exact"]) != q(selected["beta_exact"]):
        raise ValueError("The actual selected beta identities differ")
    projected, exact, projections, exact_words = parameter_projection(selected)
    report.update(selected_beta_exact=str(q(selected["beta_exact"])),
        selected_nine_parameters_exact=[str(x) for x in exact],
        all_nine_original_projection_rows=projections,
        direct_words_exactly_preserve_selected_accurate_coefficients=exact_words)
    if not exact_words:
        raise NoDirectSelection("At least one actual projection is nonzero; no direct same-point recipe is emitted")
    recipe, recipe_receipt = read_json(args.selected_recipe, selected["recipe"]["sha256"])
    definition, definition_receipt = read_json(
        args.selected_definition, selected["accurate_definition"]["sha256"])
    check_descriptor(recipe_receipt, selected["recipe"], "selected accurate recipe")
    check_descriptor(definition_receipt, selected["accurate_definition"], "selected accurate definition")
    if (recipe.get("schema") != MODEL_RECIPE_SCHEMA or recipe.get("parameter_order") != PARAMETERS
            or nine_rationals(recipe["nine_parameters"], "actual selected recipe") != exact
            or nine_rationals(definition["nine_parameters"], "actual selected definition") != exact):
        raise ValueError("The complete selected recipe and definition must retain the same nine rationals")
    if definition.get("model_recipe_input", {}).get("sha256") != recipe_receipt["sha256"]:
        raise ValueError("The selected definition does not bind the actual new recipe")
    report["actual_selected_recipe"] = recipe_receipt
    report["actual_selected_definition"] = definition_receipt
    factory, factory_receipt = read_json(
        args.factory_directory / "result.json", args.factory_result_sha256)
    if (factory.get("schema") != FACTORY_SCHEMA or factory.get("source_sha256") != FACTORY_SHA
            or factory.get("repository") != REPOSITORY
            or str(factory.get("run_id")) != os.environ.get("GITHUB_RUN_ID")
            or factory.get("source_commit") != os.environ.get("GITHUB_SHA")
            or factory.get("exact_model_definition_created") is not True):
        raise ValueError("Require the actual original factory result from this job, never a rewritten producer")
    fresh, fresh_receipt = safe_member(args.factory_directory, factory["model_definition"])
    if (nine_rationals(factory["starting_parameters"], "actual original factory point") != exact
            or factory.get("actual_model_recipe", {}).get("sha256") != recipe_receipt["sha256"]
            or fresh.get("model_recipe_input", {}).get("sha256") != recipe_receipt["sha256"]
            or factory.get("actual_core_input") != fresh.get("core_input")
            or factory.get("actual_tail_result_sha256") != fresh["continuous_tail"]["actual_result"]["sha256"]):
        raise ValueError("The actual same-job factory result has a different complete target or source")
    check_descriptor(recipe_receipt, definition["model_recipe_input"], "selected definition recipe")
    check_descriptor(recipe_receipt, fresh["model_recipe_input"], "fresh definition recipe")
    equivalence = same_accurate_definition(definition, fresh, recipe)
    evidence = dict(selected=actual_definition_evidence(definition),
                    fresh=actual_definition_evidence(fresh))
    transfer = dict(
        schema="R383-same-accurate-family-initial-point-domain-transfer-v1",
        published_basis=SEMANTIC_TRANSFER_BASIS,
        original_selected_full419_domain_assertion_retained=True,
        same_original_complete_C_root_family_and_exact_initial_nine_point=True,
        same_exact_core_cut_windows_DAG_and_all_nine_support_terms=True,
        selected_and_fresh_run_evidence_bound_separately=True,
        equality_or_subset_of_new_and_old_enclosure_boxes_required=False,
        all_points_of_the_new_independent_enclosure_box_certified=False,
        old_certificate_transferred_to_the_same_semantic_root_family=True,
        numerical_shadow_domain_J_FD_or_metric_proof_inherited=False,
        subsequent_active_p_covered_by_initial_certificate=False,
        actual_BVP_or_native_acceptance_created=False)
    report.update(actual_same_job_original_factory_result=factory_receipt,
        actual_same_job_original_factory_definition=fresh_receipt,
        complete_mathematical_definition_equal=equivalence,
        separately_bound_original_and_fresh_evidence=evidence,
        accurate_initial_domain_certificate_transfer=transfer,
        original_factory_parameter_domain_complete=factory.get("full_current_nine_domain_certificate_complete"),
        original_factory_domain_status_used_as_new_BVP_gate=False)
    template, template_receipt = read_json(args.template_bvp_recipe, BVP_TEMPLATE_SHA)
    if (template.get("schema") != BVP_RECIPE_SCHEMA or template.get("parameter_order") != PARAMETERS
            or template.get("active_parameter_indices") != [0,1,2]
            or template.get("frozen_parameter_indices") != [3,4,5,6,7,8]):
        raise ValueError("Use the complete unchanged original179 three-active input contract")
    result = deepcopy(template)
    result["request_number"] = args.bvp_request_number
    result["initial_nine_parameters"] = projected
    result["initial_parameter_origin"] = dict(
        kind="actual-complete-domain-coast-selection-with-exact-original-binary64-words",
        selection_summary=selection_receipt,
        selection_source_sha256=args.selection_source_sha256,
        selected_recipe=recipe_receipt, selected_accurate_definition=definition_receipt,
        same_job_original_factory_result=factory_receipt,
        same_job_original_factory_definition=fresh_receipt,
        selected_beta_exact=str(q(selected["beta_exact"])),
        all_nine_original_projection_rows=projections,
        original_template_parameter_origin=template["initial_parameter_origin"],
        accurate_target_coefficient_roundtrip_paid=True,
        actual_numeric_profile_error_or_new_BVP_acceptance_inherited=False,
        accurate_initial_domain_certificate_transfer=transfer,
        selected_domain_scope_only_initial_parameters=True)
    result["actual_selected_coast_input_binding"] = dict(
        schema=SCHEMA,adapter_source_sha256=digest(Path(__file__).read_bytes()),
        original_BVP_template=template_receipt,
        original_BVP_template_source_commit=BVP_SOURCE_COMMIT,
        accurate_definition_mathematical_field_sha256={
            key:value["canonical_sha256"] for key,value in equivalence.items()},
        initial_accurate_nine_and_numeric_parameter_words_identical=True,
        exact_cut_leaves_and_continuous_C_family_unchanged=True,
        separate_original_and_fresh_actual_evidence=evidence,
        old_and_fresh_enclosure_equality_not_required=True,
        numerical_shadow_not_identified_with_accurate_target=True,
        full338_112_3_state_layout_unchanged=True,
        original_complete453_seed_only_initial_guess=True,
        original_BVP_FD_native_line_search_tolerances_and_fresh_audit_unchanged=True,
        any_later_active_p_requires_its_own_accurate_domain_responsibility=True)
    changed = {"request_number","initial_nine_parameters","initial_parameter_origin",
               "actual_selected_coast_input_binding"}
    for key,value in template.items():
        if key not in changed and result.get(key) != value:
            raise AssertionError("Original complete BVP contract changed: " + key)
    report["original_BVP_template"] = template_receipt
    report["changed_BVP_recipe_fields"] = sorted(changed)
    return result

def main(argv=None):
    require_actions()
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("selection-summary","selection-source","selected-recipe",
                 "selected-definition","factory-directory","template-bvp-recipe",
                 "code-directory","out"):
        p.add_argument("--"+name,type=Path,required=True)
    for name in ("selection-summary-sha256","selection-source-sha256","factory-result-sha256"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--bvp-request-number",type=int,required=True)
    args = p.parse_args(argv)
    if args.bvp_request_number <= 0:
        raise ValueError("Declare the actual future request number; no number is guessed")
    if args.out.exists():
        raise FileExistsError("Use fresh owned temporary output")
    destination = args.out.resolve()
    for name in ("selection_summary","selection_source","selected_recipe",
                 "selected_definition","factory_directory","template_bvp_recipe","code_directory"):
        source = getattr(args,name).resolve()
        if source == destination or source.is_relative_to(destination):
            raise ValueError("The adapter output must not own any original input")
    args.out.mkdir(parents=True)
    report = dict(schema=SCHEMA,source_sha256=digest(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],complete_source_parameter_readback=False,
        direct_BVP_input_created=False,actual_BVP_solve_performed=False,
        actual_native_calls=0,actual_fresh_J_calls=0,actual_accepted_field_created=False,
        exact_target_or_same_field_metric_certified=False,
        no_implicit_binary64_projection_adopted_as_selected_accurate_target=True,
        original179_scientific_sources_and_algorithm_gates_unchanged=True,
        source_scope_partial_is_not_a_new_nonlinear_rejection=True,error=None)
    code = 0
    try:
        recipe = bind(args,report)
        raw = canonical(recipe)
        path = args.out / "current-coast-selected-BVP-recipe.json"
        path.write_bytes(raw)
        report.update(complete_source_parameter_readback=True,direct_BVP_input_created=True,
            generated_BVP_recipe=dict(file=path.name,bytes=len(raw),sha256=digest(raw)))
    except NoDirectSelection as exc:
        report["error"] = dict(type=type(exc).__name__,message=str(exc))
        code = 3
    except Exception as exc:
        report["error"] = dict(type=type(exc).__name__,message=str(exc))
        code = 2
    raw = canonical(report)
    (args.out / "result.json").write_bytes(raw)
    if len(raw) > 90000:
        print(json.dumps(dict(event="coast-BVP-binding-summary-over-budget",
            bytes=len(raw),sha256=digest(raw),summary_not_split=True,
            complete_summary_returned=False)),flush=True)
        return 70
    print("BEGIN_ACTUAL_COAST_SELECTED_BVP_INPUT_BINDING",flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_ACTUAL_COAST_SELECTED_BVP_INPUT_BINDING",flush=True)
    print(json.dumps(dict(event="coast-BVP-binding-summary-identity",
        bytes=len(raw),sha256=digest(raw))),flush=True)
    return code

if __name__ == "__main__":
    raise SystemExit(main())
