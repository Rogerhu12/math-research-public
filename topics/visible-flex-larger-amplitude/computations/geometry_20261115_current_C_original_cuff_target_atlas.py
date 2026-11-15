#!/usr/bin/env python3
"""R413 bind the original model-C cuff to the independent R409 closing plan.

This is an input/atlas adapter, not a new BVP, E evaluator, field acceptance
or whole-surface certificate.  It reads the actual R400 checkpoint metadata
and its original factory objects, preserves every current ten-parameter word,
and derives the only generated cuff from the original physicalParameters
rCuff word.  It does not replace the original C target by geometric B-prime.

The local target two-jet statement invokes the existing R286/R294 theorem for
every admissible original deep root.  The original R400/R409 loaders still
own complete field/array/response verification.  No field arrays, RHS, native
solver, interval integration, FFT or previous acceptance are recomputed here.
All execution, including exact rational construction, is public-Actions-only.
Author: geometry agent (AI), 2026-11-15.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import signal
import struct
import sys

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R413-current-C-original-cuff-target-atlas-binding-v1"
CONSTRUCTION_SCHEMA = SCHEMA + "-construction-v1"
CHECKPOINT_SCHEMA = "R400-current-continuous-ten-complete-physical-DN-checkpoint-v1"
PROFILE_SCHEMA = "R400-current-continuous-C-ten-complete112-profile-and-freeze-binding-v1"
FACTORY_SCHEMA = "R300-continuous-ten-fixed-support1-power4-v3-cut-exact-expression-construction-v1"
DEFINITION_SCHEMA = "R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1"
C_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
C_BINDING_SCHEMA = "R286-original-stored-convention-C-continuous-E-cover-v3-input-binding"
SHARED_SCHEMA = "R409-current-C-ten450-shared-background-complete-field-v1"
SHARED_PLAN_SCHEMA = "R409-current-C-ten450-shared-field-plan-input-v1"
SHARED_LOADER = "geometry_20261115_current_C_ten450_shared_field.load_shared_bundle"
REVISION = "869436630c99aa5a68afb55bd8877c826034d117"
PARAMETERS = ["p1", "p2", "p3", "theta1", "theta2", "theta3",
              "eta1", "eta2", "eta3", "xi"]
CHECKPOINT_NAME = "geometry_20261115_continuous_ten_frozen450_checkpoint.py"
CHECKPOINT_SHA = "43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae"
PROFILE_NAME = "geometry_20261115_continuous_ten_same_metric_profile.py"
PROFILE_SHA = "3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6"
FACTORY_NAME = "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA = "72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
C_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
C_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
SHARED_NAME = "geometry_20261115_current_C_ten450_shared_field.py"
SHARED_SHA = "6a5f949a0422d0a4794c270140a777af1b2e2f7c73f99ef99e0601fdc634d6f3"
SOURCE_PINS = {CHECKPOINT_NAME: CHECKPOINT_SHA, PROFILE_NAME: PROFILE_SHA,
               FACTORY_NAME: FACTORY_SHA, C_NAME: C_SHA, SHARED_NAME: SHARED_SHA}
PROOF_PINS = {
    "R286-original-stored-continuous-integral-and-metric-bridge.md":
        "81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb",
    "R294-nine450-exact-C2-seams-and-target-atlas.md":
        "6e04015255df15998333d2b1274e0423808b10c63a5209a02de6d7588a7f034e"}
SUMMARY_LIMIT = 90000


def actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Execute this construction only in the named public repository Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode()


def unique(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def finite_float(token):
    value = float(token)
    if not math.isfinite(value):
        raise ValueError("Nonfinite original JSON number")
    return value


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique, parse_float=finite_float,
        parse_int=lambda token: -0.0 if token == "-0" else int(token),
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError("Nonfinite JSON token")))


def receipt(path, root=None):
    path = Path(path)
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            digest.update(block)
            size += len(block)
    return dict(file=str(path.relative_to(root)) if root is not None else path.name,
                bytes=size, sha256=digest.hexdigest())


def bound_json(path, expected):
    path = Path(path)
    raw = path.read_bytes()
    if sha(raw) != expected:
        raise ValueError("Actual original metadata SHA differs: " + str(path))
    return decode(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw), receipt(path)


def within(root, name):
    root = Path(root).resolve()
    relative = PurePosixPath(name)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise ValueError("An original relative member path is required")
    path = root / str(relative)
    if not path.resolve().is_relative_to(root) or path.resolve() == root:
        raise ValueError("An original member escaped its actual directory")
    cursor = path
    while cursor != root:
        if cursor.is_symlink():
            raise ValueError("An original member may not traverse a symlink")
        cursor = cursor.parent
    return path


def member_json(root, descriptor):
    path = within(root, descriptor["file"])
    actual = receipt(path, root)
    if any(actual[k] != descriptor[k] for k in ("bytes", "sha256")):
        raise ValueError("Original metadata member identity differs: " + descriptor["file"])
    value, _ = bound_json(path, descriptor["sha256"])
    return value, actual, path


def same_payload(a, b):
    return all(a.get(k) == b.get(k) for k in ("bytes", "sha256"))


def equal_literal(a, b):
    # Keep negative zero and the actual serialized source distinctions.
    return canonical(a) == canonical(b)


def numeric_word(value):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError("Use the original finite binary64-compatible JSON word")
    return struct.pack("<d", float(value)).hex()


def exact(value):
    if type(value) is bool:
        raise ValueError("A Boolean is not a coordinate")
    if type(value) is float:
        if not math.isfinite(value):
            raise ValueError("Nonfinite coordinate")
        return Q.from_float(value)
    if type(value) in (str, int):
        return Q(value)
    raise ValueError("Use an exact rational or original finite word")


def write_json(path, value):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return receipt(path)


def source_records(computations, proof_directory):
    records = {}
    for directory, pins in ((Path(computations), SOURCE_PINS),
                             (Path(proof_directory), PROOF_PINS)):
        for name, expected in pins.items():
            row = receipt(directory / name)
            if row["sha256"] != expected:
                raise ValueError("The frozen source or existing theorem differs: " + name)
            records[name] = row
    return records


def checkpoint_metadata(directory, expected):
    """Read only metadata/factory definitions, not the scientific field arrays."""
    actions()
    root = Path(directory).resolve()
    manifest, manifest_receipt = bound_json(root / "checkpoint.json", expected)
    if (manifest.get("schema") != CHECKPOINT_SCHEMA
            or manifest.get("repository") != REPOSITORY
            or manifest.get("writer_source", {}).get("sha256") != CHECKPOINT_SHA
            or manifest.get("finite_fullDN_accepted_by_original_gates") is not True
            or manifest.get("actual_frozen450_accepted") is not True
            or manifest.get("actual_active_parameter_count") != 0
            or manifest.get("actual_dimension") != 450
            or manifest.get("actual_physical_dimension") != 338
            or manifest.get("actual_core_dimension") != 112
            or manifest.get("source453_rows_dropped_relabelled_as_accepted450") is not False
            or manifest.get("parent") is None):
        raise ValueError("Use the own-schema metadata of a genuine R400 frozen450 checkpoint")
    target = manifest["current_target_identity"]
    if (target.get("schema") != PROFILE_SCHEMA + "-same-point-identity"
            or target.get("accurate_target_model_schema") != DEFINITION_SCHEMA
            or target.get("continuous_C_model_schema") != C_SCHEMA
            or target.get("parameter_order") != PARAMETERS
            or len(target.get("complete_ten_float64le", [])) != 10
            or len(target.get("complete_ten_exact_dyadics", [])) != 10
            or target["complete_ten_float64le"] != manifest["complete_ten_float64le"]
            or target["complete_ten_exact_dyadics"] != manifest["complete_ten_exact_dyadics"]):
        raise ValueError("Retain the same complete current ten-parameter target identity")
    for word, rational in zip(target["complete_ten_float64le"], target["complete_ten_exact_dyadics"]):
        raw = bytes.fromhex(word)
        if len(raw) != 8:
            raise ValueError("A current parameter is not a complete IEEE word")
        value = struct.unpack("<d", raw)[0]
        if not math.isfinite(value) or exact(value) != exact(rational):
            raise ValueError("The exact current parameter and its original word differ")
    factory, factory_receipt, factory_path = member_json(root, manifest["members"]["factory_result"])
    definition, definition_receipt, definition_path = member_json(root, manifest["members"]["factory_definition"])
    factory_root = within(root, manifest["factory_directory"])
    if (factory_path.resolve() != (factory_root / "result.json").resolve()
            or within(factory_root, factory["model_definition"]["file"]).resolve() != definition_path.resolve()
            or not same_payload(factory["model_definition"], definition_receipt)
            or not same_payload(target["accurate_factory_result"], factory_receipt)
            or not same_payload(target["accurate_definition"], definition_receipt)
            or factory.get("schema") != FACTORY_SCHEMA
            or factory.get("source_sha256") != FACTORY_SHA
            or factory.get("repository") != REPOSITORY
            or factory.get("exact_model_definition_created") is not True
            or definition.get("schema") != DEFINITION_SCHEMA
            or definition.get("source_sha256") != FACTORY_SHA
            or definition.get("parameter_order") != PARAMETERS
            or definition.get("construction_conditions", {}).get("all_strict_conditions_proved") is not True):
        raise ValueError("The complete original ten factory result/definition source differs")
    tail = definition["continuous_tail"]
    binding = target["original_complete_C_input_binding"]
    if (tail.get("source_sha256") != C_SHA
            or not equal_literal(tail["actual_input_binding"], binding)
            or binding.get("schema") != C_BINDING_SCHEMA
            or binding.get("source_sha256") != C_SHA
            or binding.get("original_source_revision") != REVISION
            or factory["actual_tail_result_sha256"] != tail["actual_result"]["sha256"]
            or not equal_literal(factory["actual_core_input"], definition["core_input"])
            or not equal_literal(factory["actual_model_recipe"], definition["model_recipe_input"])
            or exact(target["original_binary_cut_exact_rational"]) != exact(definition["cut_radius"])
            or exact(definition["cut_radius"]) != exact(tail["cut_radius"])):
        raise ValueError("The current point, factory and original convention-C binding differ")
    convention = binding["convention"]
    p = binding["physical_parameters"]
    root_conditions = convention["root_conditions"]
    if (convention.get("schema") != C_SCHEMA
            or convention.get("deep_definition") != "original-exact-root-family"
            or convention.get("binary_inputs_are_exact_dyadics") is not True
            or convention.get("deep_bounds_valid_for_every_original_root_in_half_to_two") is not True
            or convention.get("root_existence_proved") is not True
            or root_conditions.get("deep_start") != 160 or root_conditions.get("R") != 64
            or not 0 < exact(p["delta0"]) <= Q(1, 10)
            or not 0 < exact(p["etaRatioAtN0"]) <= Q(1, 16)
            or exact(p["epsilonScale"]) <= 0):
        raise ValueError("The existing R286 original deep-family cuff theorem premises are unpaid")
    numeric_word(p["rCuff"])
    c = exact(p["rCuff"])
    cut = exact(target["original_binary_cut_exact_rational"])
    if not 0 < c < cut:
        raise ValueError("The original positive cuff/cut layout is not available")
    return dict(manifest=manifest, manifest_receipt=manifest_receipt,
        target=target, definition=definition, binding=binding, cuff=p["rCuff"],
        cut=cut, original_factory=factory_receipt, original_definition=definition_receipt,
        metadata_only_original_field_arrays_and_acceptance_not_rechecked=True)


def construction_plan(construction, checkpoint):
    """Derive cuff from its original word; never choose a new cutoff radius."""
    actions()
    allowed = {"schema", "checkpoint_sha256", "cuff", "cut_correction_width",
               "cap_height", "fixed_cap"}
    if (not isinstance(construction, dict) or set(construction) - allowed
            or construction.get("schema") != CONSTRUCTION_SCHEMA
            or construction.get("checkpoint_sha256") != checkpoint["manifest_receipt"]["sha256"]):
        raise ValueError("Use the explicit R413 construction for this actual checkpoint")
    cuff = checkpoint["cuff"]
    if "cuff" in construction and numeric_word(construction["cuff"]) != numeric_word(cuff):
        raise ValueError("An optional cuff must be the same original C word, not a replacement")
    for key in ("cut_correction_width", "cap_height"):
        numeric_word(construction[key])
    c = exact(cuff)
    width = exact(construction["cut_correction_width"])
    if not 0 < width < checkpoint["cut"] - c:
        raise ValueError("Retain the original positive cut-patch layout; rFar is checked by R409")
    fixed = construction["fixed_cap"]
    if not isinstance(fixed, dict) or set(fixed) != {"markers"} or not isinstance(fixed["markers"], list):
        raise ValueError("Retain the entire explicit fixed-cap marker list")
    marker_records = []
    clearance = c / 4
    for index, row in enumerate(fixed["markers"]):
        if not isinstance(row, dict) or set(row) != {"upper", "center", "radius", "height"}:
            raise ValueError("Every marker needs its side, center, radius and height")
        if type(row["upper"]) is not bool or not isinstance(row["center"], list) or len(row["center"]) != 2:
            raise ValueError("Every fixed marker needs a full side and Cartesian center")
        for value in row["center"] + [row["radius"], row["height"]]:
            numeric_word(value)
        center = list(map(exact, row["center"]))
        radius, height = exact(row["radius"]), exact(row["height"])
        gap = (c - radius) ** 2 - sum(x * x for x in center)
        if not 0 < radius < c or gap <= 0:
            raise ValueError("An original R409 cap marker is not strictly inside the same cuff disk")
        # |center|+radius < c-2*delta_i. No square-root rounding is used.
        delta = gap / (4 * (c - radius))
        clearance = min(clearance, delta)
        marker_records.append(dict(index=index, upper=row["upper"],
            center_exact=list(map(str, center)), radius_exact=str(radius), height_exact=str(height),
            original_float64le=[numeric_word(x) for x in row["center"] + [row["radius"], row["height"]]],
            squared_strict_support_margin=str(gap), proved_inner_clearance=str(delta)))
    plan = dict(schema=SHARED_PLAN_SCHEMA,
        checkpoint_sha256=checkpoint["manifest_receipt"]["sha256"], cuff=copy.deepcopy(cuff),
        cut_correction_width=copy.deepcopy(construction["cut_correction_width"]),
        cap_height=copy.deepcopy(construction["cap_height"]), fixed_cap=copy.deepcopy(fixed))
    return plan, marker_records, clearance


def atlas_definition(checkpoint, plan, markers, clearance, sources):
    actions()
    target, binding = checkpoint["target"], checkpoint["binding"]
    c = exact(checkpoint["cuff"])
    return dict(schema=SCHEMA + "-exact-atlas", repository=REPOSITORY,
        source=receipt(__file__), source_and_existing_theorem_identities=sources,
        original_checkpoint=checkpoint["manifest_receipt"],
        complete_current_target_identity=copy.deepcopy(target),
        original_complete_C_binding_sha256=sha(canonical(binding)),
        original_factory_result=checkpoint["original_factory"],
        original_factory_definition=checkpoint["original_definition"],
        generated_R409_plan=copy.deepcopy(plan),
        original_cuff=dict(
            exact_rational=str(c), float64le=numeric_word(checkpoint["cuff"]),
            checkpoint_pointer="/current_target_identity/original_complete_C_input_binding/physical_parameters/rCuff",
            original_ledger_pointer="/ready/rationalDeepModel/physicalParameters/rCuff",
            original_stored_pointer="/ready/storedMetricAdapter/physicalParameters/rCuff",
            ready_wrapper_optional_in_original_producer=True,
            ledger_and_stored_word_equality_is_original_f12f_binding=True,
            cuff_is_not_a_new_search_parameter=True,
            inner_flat_annulus_added=False, original_natural_Rout_reidentified=False),
        coordinates=dict(material_angle="theta", cartesian="X=(r*cos(theta),r*sin(theta))",
            original_physical_phi_is_not_identified_with_material_theta=True,
            R409_full_material_Phi_pullback_remains_required=True,
            both_caps_use_the_same_original_radius=True,
            no_new_registration_or_phase_rotation_applied_to_fixed_caps=True),
        radial_target=dict(model_schema=C_SCHEMA,
            original_binding_sha256=sha(canonical(binding)),
            exact_definition="g_tail=E_C(r)*dr^2+r^2*dtheta^2",
            cartesian_definition="I+(E_C(r)-1)*X*X^T/(X^T*X)",
            domain_left=str(c), domain_right="the original natural real R_out",
            geometric_Bprime_substituted=False, E_values_evaluated_by_this_adapter=False,
            all_original_deep_roots_in_half_to_two_retained=True),
        fixed_caps=dict(markers=markers, marker_count=len(markers),
            graph="F_plus(X)=(X,H+b_plus(X)); F_minus(X)=(X,-H-b_minus(X))",
            bump="b_side(X)=sum_i A_i*max(0,1-|X-center_i|^2/radius_i^2)^4",
            exact_target="I+Db_side*Db_side^T",
            upper_and_lower_markers_may_differ=True,
            cap_height_exact=str(exact(plan["cap_height"])),
            cap_height_does_not_enter_the_metric=True,
            all_overlapping_markers_summed_before_forming_metric=True,
            complete_flat_inner_annulus=[str(c-clearance), str(c)],
            exact_radial_clearance=str(clearance),
            interval_cap_six_jets_or_spatial_cover_computed=False),
        local_seam_theorem=dict(references=["R286 sections286.9-286.10", "R294 sections294.8.2-294.9.1"],
            original_deep_root_premises=copy.deepcopy(binding["convention"]["root_conditions"]),
            original_cuff_twojet=dict(E="1", E_r="0", E_rr="0"),
            Cartesian_metric_trace="I", Cartesian_first_derivative_trace="0",
            Cartesian_second_derivative_trace="0",
            exact_cuff_C2_target_compatibility_under_bound_original_model=True,
            sign_of_cap_graph_and_normal_orientation_irrelevant_to_metric=True,
            assertion_uses_infinite_tail_theorem_not_finite_samples=True),
        unchanged_open_responsibilities=dict(
            actual_frozen450_arrays_and_all_original_acceptance_remain_R400_loader=True,
            R409_original_radial_rFar_and_full_layout_check_remains=True,
            complete_C_finite_head_protected_join_natural_domain_and_cut_inclusion_remain=True,
            same_exact_C_root_field_and_target_association_not_created=True,
            accurate_prefix_cut_target_atlas_unpaid=True,
            declared_numeric_ap_app_not_exact_C_target_derivatives=True,
            full_closed_relative_metric_or_curvature_or_reach_or_embedding_or_held_unpaid=True,
            complete_cap_interval_six_jet_or_phase_spatial_cover_unpaid=True),
        actual_closed_surface_or_new_scientific_acceptance_created=False)


def bind_loaded_shared_bundle(bundle, atlas):
    """Attach a separate target record to a live, already-loaded R409 tuple.

    Never overwrite the original seven members, their guard, or their unpaid
    whole-atlas flags.  This API does not invoke the shared loader a second time.
    """
    actions()
    if not isinstance(bundle, (tuple, list)) or len(bundle) != 7:
        raise ValueError("Use the complete unchanged R409 seven-member tuple")
    paths, plan, assembly, target, saved, geometry, bindings = bundle
    if (atlas.get("schema") != SCHEMA + "-exact-atlas"
            or atlas.get("source", {}).get("sha256") != receipt(__file__)["sha256"]
            or bindings.get("source", {}).get("sha256") != SHARED_SHA
            or plan.get("schema") != SHARED_SCHEMA + "-plan"
            or not equal_literal(target["complete_current_ten_target"], atlas["complete_current_target_identity"])
            or not equal_literal(saved.checkpoint.target_identity, atlas["complete_current_target_identity"])
            or not same_payload(saved.checkpoint.receipt, atlas["original_checkpoint"])):
        raise ValueError("The local target atlas and complete actual field have different owners")
    original_plan = atlas["generated_R409_plan"]
    for key in ("checkpoint_sha256", "cuff", "cut_correction_width", "cap_height", "fixed_cap"):
        if not equal_literal(plan[key], original_plan[key]):
            raise ValueError("The actual shared field changed the original cuff/cap construction: " + key)
    current_C = target["complete_current_ten_target"]["original_complete_C_input_binding"]
    p = current_C["physical_parameters"]
    convention = current_C["convention"]
    if (current_C.get("schema") != C_BINDING_SCHEMA or current_C.get("source_sha256") != C_SHA
            or convention.get("schema") != C_SCHEMA
            or convention.get("deep_definition") != "original-exact-root-family"
            or convention.get("root_existence_proved") is not True
            or convention.get("deep_bounds_valid_for_every_original_root_in_half_to_two") is not True
            or not 0 < exact(p["delta0"]) <= Q(1, 10)
            or not 0 < exact(p["etaRatioAtN0"]) <= Q(1, 16)
            or exact(p["epsilonScale"]) <= 0
            or numeric_word(plan["cuff"]) != numeric_word(p["rCuff"])
            or numeric_word(plan["cuff"]) != atlas["original_cuff"]["float64le"]
            or exact(atlas["original_cuff"]["exact_rational"]) != exact(p["rCuff"])
            or atlas["original_complete_C_binding_sha256"] != sha(canonical(current_C))):
        raise ValueError("A scalar tolerance is not original cuff identity")
    required = plan["large_core_prefix"]["closed_geometry_wrapper"]["required_geometry_loader"]
    if required != SHARED_LOADER:
        raise ValueError("The existing complete-field loader guard must remain in force")
    return dict(schema=SCHEMA + "-same-field-attachment", atlas_sha256=sha(canonical(atlas)),
        original_shared_binding=copy.deepcopy(bindings),
        exact_original_cuff_target_twojet_compatibility=True,
        original_seven_tuple_and_all_other_unpaid_responsibilities_unchanged=True,
        whole_target_metric_certificate_or_new_field_acceptance=False)


class ExternalStop(RuntimeError):
    def __init__(self, number):
        self.signal_number = number
        super().__init__("Actual external signal " + str(number))


def prepare(args):
    actions()
    out = Path(args.out).resolve()
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    if out.exists() or out == temporary or not out.is_relative_to(temporary):
        raise ValueError("Use a fresh owned Actions-temporary output directory")
    out.mkdir(parents=True)
    report = dict(schema=SCHEMA, repository=REPOSITORY, source=receipt(__file__),
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        completed=False, generated_plan=None, target_atlas=None, error=None,
        complete_original_field_arrays_or_acceptance_reverified=False,
        existing_R400_R409_guards_replaced=False, scientific_solver_or_E_query_run=False,
        new_actual_surface_or_BVP_acceptance=False, full_target_atlas_paid=False)
    try:
        sources = source_records(args.computations, args.proof_directory)
        checkpoint = checkpoint_metadata(args.checkpoint_directory, args.checkpoint_sha256)
        construction, construction_receipt = bound_json(args.construction, args.construction_sha256)
        plan, markers, clearance = construction_plan(construction, checkpoint)
        atlas = atlas_definition(checkpoint, plan, markers, clearance, sources)
        plan_receipt = write_json(out / "r409-original-cuff-plan.json", plan)
        atlas_receipt = write_json(out / "original-cuff-target-atlas.json", atlas)
        report.update(completed=True, sources=sources,
            original_checkpoint=checkpoint["manifest_receipt"],
            construction=construction_receipt, generated_plan=plan_receipt,
            target_atlas=atlas_receipt, original_cuff=atlas["original_cuff"],
            complete_current_target_identity_sha256=sha(canonical(checkpoint["target"])),
            original_complete_C_input_binding_sha256=sha(canonical(checkpoint["binding"])),
            original_ten_parameter_words_retained=True,
            marker_count=len(markers), exact_flat_cap_annulus=atlas["fixed_caps"]["complete_flat_inner_annulus"],
            local_cuff_target_twojet_compatibility=atlas["local_seam_theorem"],
            unpaid=atlas["unchanged_open_responsibilities"],
            original_field_acceptance_is_metadata_source_not_recomputed_certificate=True)
    except BaseException as error:
        report["error"] = dict(type=type(error).__name__, message=str(error))
        report["external_interruption"] = isinstance(error, ExternalStop)
        report["unpaid"] = dict(entire_requested_cuff_binding=True,
            no_new_target_plan_or_whole_metric_certificate_asserted=True)
    write_json(out / "result.json", report)
    summary = dict(report, actual_result=receipt(out / "result.json"))
    raw = canonical(summary)
    if len(raw) > SUMMARY_LIMIT:
        raw = canonical(dict(schema=SCHEMA + "-necessary-summary-too-large",
            summary_bytes=len(raw), summary_sha256=sha(raw),
            original_result=summary["actual_result"], completed=report["completed"],
            necessary_scalar_readback_complete=False, output_not_split_or_encoded=True))
        code = 70
    else:
        code = 0 if report["completed"] else 2
    print("BEGIN_R413_ORIGINAL_C_CUFF_TARGET_ATLAS", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R413_ORIGINAL_C_CUFF_TARGET_ATLAS", flush=True)
    print(json.dumps(dict(event="R413-necessary-summary-identity", bytes=len(raw), sha256=sha(raw),
        original_result=receipt(out / "result.json"), exit_code=code)), flush=True)
    return code


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--computations", required=True, type=Path)
    parser.add_argument("--proof-directory", required=True, type=Path)
    parser.add_argument("--checkpoint-directory", required=True, type=Path)
    parser.add_argument("--checkpoint-sha256", required=True)
    parser.add_argument("--construction", required=True, type=Path)
    parser.add_argument("--construction-sha256", required=True)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    handlers = {}
    def stopped(number, frame):
        raise ExternalStop(number)
    try:
        for sig in (signal.SIGTERM, signal.SIGINT):
            handlers[sig] = signal.signal(sig, stopped)
        return prepare(args)
    finally:
        for sig, handler in handlers.items():
            signal.signal(sig, handler)


if __name__ == "__main__":
    sys.exit(main())
