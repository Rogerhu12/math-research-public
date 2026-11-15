#!/usr/bin/env python3
"""Bind one actual request180 selected accurate coast point to original179 BVP inputs.

This is an Actions-only source/parameter adapter.  It does not create an
accepted field, regenerate scientific data, import a numerical library, run
a solver, or turn a parameter projection into an accurate-domain certificate.
The original factory must have actually run with the selected recipe in this
same job.  Its result is consumed verbatim; no old factory result is forged.
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
# Every mathematical part of factory.definition and its actual semantic leaves.
# Operational domain timings and result paths are retained by separate original
# whole-file identities; they are not substituted for mathematical equality.
MATHEMATICAL_KEYS = (
    "schema", "source_sha256", "exact_definition", "parameter_order",
    "nine_parameters", "expression_nodes", "pieces", "three_true_supports",
    "derived_expression_roots", "core_end", "cut_radius", "chosen_root_scope",
    "continuous_tail", "core_input", "actual_enclosure_leaves",
    "construction_conditions",
    "polynomial_coefficients_are_expressions_not_cut_interval_midpoints",
    "accurate_cumulative_radius_not_reset_to_old_a0",
    "no_early_segment_mask_or_primal_clip",
    "true_derivatives_from_the_same_radius_expression",
    "natural_outer_radius_not_flat_extended",
    "original_finite_Gauss_target_identified_with_this_new_family",
    "published_structural_and_effective_scope_proof",
)

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

def same_accurate_definition(selected_definition, factory_definition):
    for value in (selected_definition, factory_definition):
        if value.get("schema") != MODEL_SCHEMA or value.get("source_sha256") != FACTORY_SHA:
            raise ValueError("Use the original accurate v3 expression definition")
        if value.get("parameter_order") != PARAMETERS:
            raise ValueError("Keep the complete original nine-control order")
    checked = {}
    for key in MATHEMATICAL_KEYS:
        if key not in selected_definition or key not in factory_definition:
            raise ValueError("Missing complete accurate-definition field: " + key)
        left, right = selected_definition[key], factory_definition[key]
        if key == "nine_parameters":
            equal = nine_rationals(left, key) == nine_rationals(right, key)
        else:
            equal = left == right
        if not equal:
            raise ValueError("Fresh original factory changes the selected accurate target: " + key)
        checked[key] = dict(equal=True, canonical_sha256=digest(canonical(left)))
    return checked

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
    report["original_selected_full419_domain_assertion"] = dict(
        producer_flag=True, original_producer_source_bound=True,
        interpreted_only_under_original_selection_source=True,
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
    equivalence = same_accurate_definition(definition, fresh)
    report.update(actual_same_job_original_factory_result=factory_receipt,
        actual_same_job_original_factory_definition=fresh_receipt,
        complete_mathematical_definition_equal=equivalence,
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
        selected_domain_scope_only_initial_parameters=True)
    result["actual_selected_coast_input_binding"] = dict(
        schema=SCHEMA,adapter_source_sha256=digest(Path(__file__).read_bytes()),
        original_BVP_template=template_receipt,
        original_BVP_template_source_commit=BVP_SOURCE_COMMIT,
        accurate_definition_mathematical_field_sha256={
            key:value["canonical_sha256"] for key,value in equivalence.items()},
        initial_accurate_nine_and_numeric_parameter_words_identical=True,
        exact_cut_leaves_and_continuous_C_family_unchanged=True,
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
