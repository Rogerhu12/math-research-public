#!/usr/bin/env python3
"""R449: explicit actual202 parameter candidate for a NEW accurate C ten-family.

This source does not execute C, the scalar factory, a native call or a BVP.
Its prepare phase explicitly projects the published Decimal50 words to ten
binary64 words and declares their exact dyadics as a new accurate family point.
Its bind phase consumes this job's real72c factory and current joint-provider
configuration before producing a separately typed two-problem BVP recipe.
The former finite-Gauss solution, J, RHS, domain and acceptance are not inputs.
All rational/projection/interval work, including the optional necessary coast
center diagnostic, belongs only to public Actions. No diagnostic adds a gate.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R449-actual202-new-accurate-ten-candidate-adapter-v1"
INPUT_SCHEMA = "R449-actual202-original-ten-word-candidate-input-v1"
INPUT_NAME = "actual202-accurate-ten-candidate-input.json"
INPUT_SHA = "c980e9d4c6e15455459dc91a890b4fd9d8b02bced26eecd5d632ff9d250dbd4d"
POLICY = "explicit-binary64-projection-then-exact-dyadic-new-accurate-family-point"
ORIGINAL_WORD_BYTES = 553
ORIGINAL_WORD_SHA = "ba7d7fe3c7fd2599bb7f06863c117b11c6c9f4feb255a160de13023e22129369"
ORIGINAL_RUN = 43784544723
ORIGINAL_COMMIT = "1a757004b7ebff1f43563bd57b5d13961648d681"
PARAMETERS = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3", "xi"]
TERMS = [dict(parameter_index=3*k+i, support_index=i, power=k)
         for k in range(3) for i in range(3)] + [dict(parameter_index=9, support_index=1, power=4)]
FACTORY_NAME = "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA = "72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
FACTORY_SCHEMA = "R300-continuous-ten-fixed-support1-power4-v3-cut-exact-expression-construction-v1"
MODEL_SCHEMA = "R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1"
MODEL_RECIPE_SCHEMA = "R300-new-continuous-ten-fixed-support1-power4-model-recipe-v1"
ACCURATE_TEMPLATE_SHA = "cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb"
ACCURATE_TEMPLATE_BYTES = 2136
ACCURATE_TEMPLATE_SCHEMA = "R300-new-continuous-nine-scalar-model-recipe-v1"
MODEL_KEYS = ("core_end", "cut_radius", "kappa", "collar_width", "first_transition_width",
              "last_transition_width", "first_support", "root_choice", "collar_mode")
BVP_TEMPLATE_SHA = "d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811"
BVP_TEMPLATE_BYTES = 10294
BVP_TEMPLATE_SCHEMA = "explicit-current-C-riccati-R300-v3-three-active-complete453-recipe-v1"
BVP_RECIPE_SCHEMA = "R449-explicit-actual202-projected-accurate-ten-joint-full453-to-frozen450-recipe-v1"
BVP_DRIVER_NAME = "geometry_20261116_actual202_accurate_ten_full453_frozen450.py"
JOINT_DRIVER_BASELINE_NAME = "geometry_20261116_continuous_ten_joint_full453_frozen450_physical_dn.py"
JOINT_DRIVER_BASELINE_SHA = "5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592"
C_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
C_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
C_RESULT_SCHEMA = "R286-original-stored-convention-C-continuous-E-cover-v3"
CUT_SHA = "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed"
ACCEPTED_SHA = "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff"
SEED_SHA = "0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714"
JOINT_ROLES = {
    "geometry_20261115_current_C_pruefer_joint_radial_sampling.py": "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4",
    "geometry_20261115_current_C_pruefer_joint_native_worker.mjs": "d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a",
    "geometry_20261115_current_C_pruefer_joint_tail_client.py": "02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1",
    "geometry_20261115_pruefer_joint_row_representative.py": "24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97"}
LIMIT = 90000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Candidate preparation and all arithmetic are restricted to public Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")


def unique(items):
    value = {}
    for key, item in items:
        require(key not in value, "Duplicate JSON key: " + key)
        value[key] = item
    return value


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Nonfinite JSON token")))


def receipt(path):
    path = Path(path)
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            size += len(block)
            digest.update(block)
    return dict(file=path.name, bytes=size, sha256=digest.hexdigest())


def read(path, expected_sha=None, expected_bytes=None):
    path = Path(path)
    raw = path.read_bytes()
    if expected_sha is not None:
        require(sha(raw) == expected_sha, "Actual file SHA differs: " + str(path))
    if expected_bytes is not None:
        require(len(raw) == expected_bytes, "Actual file byte count differs: " + str(path))
    return decode(raw), dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def member(directory, identity):
    name = PurePosixPath(identity["file"])
    require(not name.is_absolute() and ".." not in name.parts,
        "Keep actual members inside their own temporary directory")
    root = Path(directory).resolve()
    path = Path(directory)/str(name)
    require(not path.is_symlink() and path.resolve().is_relative_to(root),
        "A source member escaped its bound directory")
    return read(path, identity["sha256"], identity["bytes"])


def same_payload(left, right):
    return (isinstance(left, dict) and isinstance(right, dict)
        and type(left.get("bytes")) is int and left["bytes"] >= 0
        and re.fullmatch(r"[0-9a-f]{64}", str(left.get("sha256", ""))) is not None
        and all(left.get(key) == right.get(key) for key in ("bytes", "sha256")))


def same_job(value, label):
    require(value.get("repository") == REPOSITORY
        and str(value.get("run_id")) == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "Consume this job's actual " + label)


def write(path, value):
    path = Path(path)
    raw = canonical(value)
    path.write_bytes(raw)
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def own_source():
    return receipt(__file__)


def raw_words(values):
    return [struct.pack("<d", float(value)).hex() for value in values]


def original_input(path):
    value, identity = read(path, INPUT_SHA)
    require(value.get("schema") == INPUT_SCHEMA
        and value.get("repository") == REPOSITORY
        and value.get("parameter_order") == PARAMETERS
        and value.get("candidate_policy") == POLICY,
        "Use the separately published actual202 parameter candidate")
    words = value["original_decimal50_words"]
    require(isinstance(words, list) and len(words) == 10
        and all(isinstance(word, str) for word in words), "Retain all ten original decimal strings")
    raw = json.dumps(words, ensure_ascii=True, separators=(",", ":"), allow_nan=False).encode("ascii")
    require(len(raw) == ORIGINAL_WORD_BYTES and sha(raw) == ORIGINAL_WORD_SHA,
        "The exact original553-byte parameter array differs")
    origin = value["origin"]
    require(origin["request_number"] == 202 and origin["run_id"] == ORIGINAL_RUN
        and origin["source_commit"] == ORIGINAL_COMMIT,
        "The actual202 point may not be relabelled a current field")
    return value, identity


def project_candidate(value):
    # This is scientific candidate arithmetic, performed only in Actions.
    require_actions()
    exact = [Q(word) for word in value["original_decimal50_words"]]
    projected = [float(word) for word in exact]
    require(all(math.isfinite(word) for word in projected), "Candidate binary64 projection is nonfinite")
    dyadic = [Q.from_float(word) for word in projected]
    rows = [dict(index=i, parameter=PARAMETERS[i], original_decimal50_word=word,
        original_exact_rational=str(a), projected_binary64_value=v,
        projected_binary64le=struct.pack("<d", v).hex(),
        projected_binary64_hex=v.hex(), new_accurate_parameter_exact_dyadic=str(b),
        exact_projection_difference_binary64_minus_original=str(b-a),
        original_rational_exactly_represented=(a == b))
        for i, (word, a, v, b) in enumerate(zip(value["original_decimal50_words"], exact, projected, dyadic))]
    return dict(schema=SCHEMA+"-parameter-point", parameter_order=list(PARAMETERS),
        policy=POLICY, original_decimal50_words=value["original_decimal50_words"],
        original_parameter_array=copy.deepcopy(value["original_parameter_array"]),
        projected_binary64_parameters=projected, projected_binary64le=raw_words(projected),
        new_accurate_ten_parameters=[str(v) for v in dyadic], projection_rows=rows,
        all_original_rationals_exactly_represented=all(row["original_rational_exactly_represented"] for row in rows),
        new_factory_and_initial_BVP_use_the_same_declared_dyadic_point=True,
        original_decimal_point_silently_relabelled=False,
        finite_Gauss_g_residual_J_domain_or_acceptance_transferred=False)


def prepare(args, report):
    original, input_id = original_input(args.parameter_input)
    template, template_id = read(args.model_recipe_template,
        ACCURATE_TEMPLATE_SHA, ACCURATE_TEMPLATE_BYTES)
    require(template.get("schema") == ACCURATE_TEMPLATE_SCHEMA
        and template.get("parameter_order") == PARAMETERS[:9],
        "Use actual180's accurate recipe as a structural template only")
    point = project_candidate(original)
    point_id = write(args.out/"candidate-ten-parameters.json", point)
    model = {key: copy.deepcopy(template[key]) for key in MODEL_KEYS}
    model.update(schema=MODEL_RECIPE_SCHEMA, parameter_order=list(PARAMETERS),
        control_terms=copy.deepcopy(TERMS), ten_parameters=point["new_accurate_ten_parameters"],
        parameter_origin=dict(schema=SCHEMA+"-new-model-origin", adapter_source=own_source(),
            actual202_input=input_id, actual202_origin=original["origin"], actual_candidate_point=point_id,
            structural_template=template_id, copied_structural_fields=list(MODEL_KEYS),
            all_previous_template_coefficients_replaced=True,
            previous_selected_point_or_domain_certificate_not_transferred=True,
            original_finite_Gauss_family_is_not_this_continuous_family=True))
    model_id = write(args.out/"actual202-projected-accurate-ten-model-recipe.json", model)
    report.update(phase="candidate-prepared", candidate_input=input_id,
        original_parameter_origin=original["origin"], structural_template=template_id,
        copied_structural_fields=list(MODEL_KEYS), candidate_parameters=point_id,
        actual_ten_model_recipe=model_id, candidate_policy=POLICY,
        original_decimal50_words=point["original_decimal50_words"],
        projected_binary64le=point["projected_binary64le"],
        new_accurate_ten_parameters=point["new_accurate_ten_parameters"],
        projection_rows=point["projection_rows"],
        accurate_C_factory_domain_or_BVP_called=False,
        full_current_accurate_domain_paid=False, actual_native_calls=0,
        actual_design453_accepted=False, actual_frozen450_accepted=False)


def domain_scope(value):
    if not isinstance(value, dict):
        return value
    keys = ("complete", "processed_nodes", "passed_leaves", "unresolved_terminal_leaves",
        "unvisited_stack_entries", "closed_coverage_kept", "minimum_enclosed_radius",
        "maximum_enclosed_absolute_speed", "ledger", "elapsed_seconds",
        "all_parameter_values_retained", "only_a_sufficient_interval_certificate_no_new_BVP_gate")
    return {key: copy.deepcopy(value[key]) for key in keys if key in value}


def coast_center_diagnostic(factory, model_recipe, point):
    """A necessary center condition derived from the original complete C hull.

    It never selects another parameter, alters a solver flag or controls the
    dispatch of the original full problems. Wide bounds remain inconclusive.
    """
    require_actions()
    box = factory["construction_conditions"]["derived_endpoint_intervals"]["coast_length"]
    lo, hi = Q(box["lower"]), Q(box["upper"])
    require(lo <= hi, "The factory returned a reversed exact coast interval")
    kappa = Q(model_recipe["kappa"])
    theta = Q(point["new_accurate_ten_parameters"][5])
    endpoints = [-kappa+2*theta*length for length in (lo, hi)]
    lower, upper = min(endpoints), max(endpoints)
    return dict(formula="a_s(t=1/2)=-kappa+2*LC*theta3", coordinate="t=(s-S1)/LC",
        complete_source_C_coast_length_enclosure=copy.deepcopy(box),
        kappa_exact=str(kappa), theta3_exact=str(theta),
        center_speed_enclosure=dict(lower=str(lower), upper=str(upper)),
        center_strict_speed_domain_enclosed=(lower > -1 and upper < 1),
        every_retained_C_choice_center_refuted=(lower >= 1 or upper <= -1),
        inconclusive_interval_is_not_a_domain_failure=True,
        full_coast_domain_proved_by_center_check=False,
        p1_p2_p3_eta3_and_support1_xi_cannot_change_this_center_with_theta3_fixed=True,
        actual_solver_or_factory_acceptance_flag_changed=False, new_acceptance_gate=False)


def bind(args, report):
    prepared, prepared_id = read(args.preparation_result, args.preparation_result_sha256)
    same_job(prepared, "candidate preparation")
    require(prepared.get("schema") == SCHEMA and prepared.get("source_sha256") == own_source()["sha256"]
        and prepared.get("phase") == "candidate-prepared" and prepared.get("process_exit_code") == 0,
        "A complete actual preparation by this adapter is required")
    folder = Path(args.preparation_result).parent
    point, point_id = member(folder, prepared["candidate_parameters"])
    model, model_id = member(folder, prepared["actual_ten_model_recipe"])
    require(point.get("schema") == SCHEMA+"-parameter-point" and point.get("policy") == POLICY
        and point.get("parameter_order") == PARAMETERS
        and model.get("schema") == MODEL_RECIPE_SCHEMA and model.get("control_terms") == TERMS,
        "Retain the separately declared complete new point and model")
    require(model["ten_parameters"] == point["new_accurate_ten_parameters"]
        and raw_words(point["projected_binary64_parameters"]) == point["projected_binary64le"]
        and [str(Q.from_float(float(v))) for v in point["projected_binary64_parameters"]]
            == point["new_accurate_ten_parameters"], "The declared accurate and numerical candidate points differ")
    factory, factory_id = read(args.factory_directory/"result.json", args.factory_result_sha256)
    same_job(factory, "accurate ten factory")
    require(factory.get("schema") == FACTORY_SCHEMA and factory.get("source_sha256") == FACTORY_SHA
        and factory.get("exact_model_definition_created") is True and factory.get("error") is None
        and same_payload(factory["actual_model_recipe"], model_id),
        "Require a real72c definition for this new recipe; never manufacture a factory result")
    definition, definition_id = member(args.factory_directory, factory["model_definition"])
    require(definition.get("schema") == MODEL_SCHEMA and definition.get("source_sha256") == FACTORY_SHA
        and definition.get("parameter_order") == PARAMETERS and definition.get("control_terms") == TERMS
        and definition.get("construction_conditions", {}).get("all_strict_conditions_proved") is True
        and same_payload(definition["model_recipe_input"], model_id)
        and [Q(x) for x in definition["ten_parameters"]] == [Q(x) for x in model["ten_parameters"]]
        and [Q(x) for x in factory["starting_parameters"]] == [Q(x) for x in model["ten_parameters"]],
        "The factory's complete definition, point or structural conditions differ")
    current_C, current_C_id = read(args.current_C_directory/"result.json", args.current_C_result_sha256)
    same_job(current_C, "full original C result")
    require(current_C.get("schema") == C_RESULT_SCHEMA and current_C.get("source_sha256") == C_SHA,
        "Use the actual original accurate C producer")
    cut, cut_id = read(args.cut_twojet_readout, args.cut_twojet_readout_sha256)
    require(cut.get("source_sha256") == CUT_SHA,
        "Use the actual original complete cut-twojet readout")
    tail = definition["continuous_tail"]
    require(same_payload(tail["actual_result"], current_C_id)
        and same_payload(tail["actual_complete_cut_twojet_readout"], cut_id)
        and factory["actual_tail_result_sha256"] == current_C_id["sha256"]
        and factory["actual_cut_twojet_readout_sha256"] == cut_id["sha256"]
        and tail.get("source_sha256") == C_SHA,
        "The new accurate definition must use this same job's complete C/cut objects")
    require(definition["core_input"]["sha256"] == ACCEPTED_SHA
        and definition["core_input"]["geometry_pointer"] == "/fixed_scalar_profile/geometry",
        "Retain the genuine original accepted96 only as core geometry/source data")
    template, template_id = read(args.BVP_recipe_template, BVP_TEMPLATE_SHA, BVP_TEMPLATE_BYTES)
    require(template.get("schema") == BVP_TEMPLATE_SCHEMA
        and template.get("accepted_source_sha256") == ACCEPTED_SHA
        and template["complete_initial_guess"]["source_sha256"] == SEED_SHA,
        "Use the original complete policy and independent699 by453 source seed")
    cfg, cfg_id = read(args.tail_config, args.tail_config_sha256)
    require(cfg.get("schema") == "current-C-complete112-client-config-v1"
        and cfg.get("model_schema") == C_SCHEMA and cfg.get("repository") == REPOSITORY,
        "The original joint complete112 config must be actually supplied")
    for name, expected in JOINT_ROLES.items():
        require(cfg.get("source_sha256", {}).get(name) == expected,
            "Keep the explicit197 joint source role: " + name)
    geometry, geometry_id = read(Path(cfg["geometry_directory"])/"result.json", cfg["geometry_result_sha256"])
    same_job(geometry, "complete joint native geometry")
    require(geometry.get("source_sha256") == JOINT_ROLES["geometry_20261115_current_C_pruefer_joint_radial_sampling.py"]
        and same_payload(geometry["actual_original_input_binding"]["actual_cover_result"], current_C_id),
        "The scalar and actual112 provider must consume the same original C bytes")
    # Readiness, every native policy value, all30 native source pins and the
    # full C semantic input equality are still enforced by unchanged c71d.
    # No new radius/speed/FD/row-rank or representation-smallness gate is added.
    driver_id = receipt(args.code_directory/BVP_DRIVER_NAME)
    require(driver_id["sha256"] == args.candidate_driver_sha256,
        "Bind the explicitly published independent nonzero-xi driver")
    require(receipt(args.code_directory/JOINT_DRIVER_BASELINE_NAME)["sha256"] == JOINT_DRIVER_BASELINE_SHA,
        "The original source baseline remains explicit")
    current = copy.deepcopy(template)
    current.update(schema=BVP_RECIPE_SCHEMA, request_number=args.request_number,
        parameter_order=list(PARAMETERS), active_parameter_indices=[0, 1, 2],
        frozen_parameter_indices=list(range(3, 10)),
        initial_ten_parameters=point["projected_binary64_parameters"],
        second_problem="same-ten-words-complete450-K0-k0", second_state_dimension=450,
        two_phases_share_one_original_process_clock=True)
    current.pop("initial_nine_parameters")
    current["initial_parameter_origin"] = dict(schema=SCHEMA+"-BVP-origin", adapter_source=own_source(),
        actual202_origin=copy.deepcopy(prepared["original_parameter_origin"]),
        original_parameter_array=dict(bytes=ORIGINAL_WORD_BYTES, sha256=ORIGINAL_WORD_SHA),
        candidate_policy=POLICY, actual_preparation=prepared_id, actual_candidate_point=point_id,
        actual_model_recipe=model_id, actual_same_job_factory=factory_id,
        actual_same_job_definition=definition_id, actual_same_job_C=current_C_id,
        actual_same_job_cut_readout=cut_id, actual_current_native_config=cfg_id,
        original_decimal50_words=point["original_decimal50_words"],
        projected_binary64le=point["projected_binary64le"],
        new_accurate_ten_parameters=point["new_accurate_ten_parameters"],
        exact_projection_rows=point["projection_rows"],
        old_finite_Gauss_metric_or_accepted_state_or_J_or_domain_not_inherited=True,
        previous_actual180_selected_point_and_domain_not_transferred=True)
    native = current["native_configuration"]
    native["source_sha256"] = copy.deepcopy(cfg["source_sha256"])
    native["original_runtime_sha256"] = copy.deepcopy(cfg["original_runtime_sha256"])
    current["actual_current_native_configuration"] = cfg_id
    execution = current["execution"]
    for key in ("sampling_declared_linear_seconds", "sampling_declared_point_seconds",
                "sampling_startup_reserves_original_BVP_seconds"):
        execution["pruefer_"+key] = execution.pop("riccati_"+key)
    execution["algorithmic_protocol_solve_entry_upper_bound"] = 36
    execution["two_phases_use_one_original_BVP_process_budget"] = True
    reserve_key = "pruefer_sampling_startup_reserves_original_BVP_seconds"
    original_reserve = execution[reserve_key]
    execution[reserve_key] = args.sampling_startup_reserve_seconds
    current["explicit_resource_binding"] = dict(
        original_BVP_template=template_id,
        original_sampling_startup_reserve_seconds=original_reserve,
        actual_sampling_startup_reserve_seconds=args.sampling_startup_reserve_seconds,
        explicit_argument="--sampling-startup-reserve-seconds",
        original_complete_BVP_process_budget_seconds=execution["complete_BVP_process_budget_seconds"],
        original_absolute_job_clock_not_started_or_reset=True,
        sampling_startup_reserve_is_not_a_new_scientific_acceptance_gate=True)
    scope = current["acceptance_scope"]
    for key in ("all_nine_fixed450_same_g_refinement_and_closed_geometry_not_supplied",
                "R375_original_deep_family_recomputed_not_previous_pivot_box_shrunk",
                "two_closed_comparison_barriers_and_full_inherited_ratio_retained"):
        scope.pop(key)
    scope.update(R380_original_deep_family_recomputed_not_previous_endpoint_box_shrunk=True,
        positive_endpoint_projective_continuation_with_uniform_R357_unit_row_rule=True,
        joint_nominal_parameter_box_point_not_claimed_to_be_a_global_C_member=True,
        complete_original_unit_row_family_to_actual_binary64_error_enclosures_retained=True,
        nominal_row_formation_does_not_add_a_native_acceptance_gate=True,
        independent_real_complete450_after_real453=True,
        original_current_H_FD_native_fullJ_final_audit_required_for_each_phase=True,
        current_factory_domain_false_not_a_new_BVP_gate=True,
        closed_geometry_and_continuous_metric_not_supplied=True,
        actual202_only_provides_explicit_new_candidate_coordinates=True,
        original_finite_Gauss_acceptance_not_relabelled=True)
    recipe_id = write(args.out/"actual202-accurate-ten-full453-frozen450-recipe.json", current)
    report.update(phase="BVP-input-bound", actual_preparation=prepared_id,
        actual_candidate_point=point_id, actual_ten_model_recipe=model_id,
        actual_factory_result=factory_id, actual_factory_definition=definition_id,
        actual_same_job_C=current_C_id, actual_cut_twojet_readout=cut_id,
        actual_current_native_configuration=cfg_id, actual_joint_geometry_result=geometry_id,
        actual_joint_geometry_completed=geometry.get("completed"),
        actual_joint_geometry_native_ready=geometry.get("native_geometry_ready"),
        actual_BVP_template=template_id, actual_candidate_driver=driver_id,
        generated_BVP_recipe=recipe_id, actual_request_number=args.request_number,
        explicit_resource_binding=copy.deepcopy(current["explicit_resource_binding"]),
        original_decimal50_words=point["original_decimal50_words"],
        projected_binary64_parameters=point["projected_binary64_parameters"],
        projected_binary64le=point["projected_binary64le"],
        new_accurate_ten_parameters=point["new_accurate_ten_parameters"],
        projection_rows=point["projection_rows"],
        original_factory_base_domain=domain_scope(factory.get("base_domain")),
        original_factory_current_parameter_domain=domain_scope(factory.get("requested_parameter_domain")),
        original_factory_full_current_ten_domain_complete=factory.get("full_current_ten_domain_certificate_complete"),
        coast_center_necessary_diagnostic=coast_center_diagnostic(factory, model, point),
        factory_interval_domain_complete_not_used_as_an_extra_BVP_gate=True,
        actual_native_calls=0, actual_BVP_calls=0,
        actual_design453_accepted=False, actual_frozen450_accepted=False,
        external_original_absolute_clock_and_owned_launcher_still_required=True,
        original_clock_recipe_binding_must_name_generated_recipe_without_restart=True,
        current_cb057_launcher_and_203_pipeline_not_silently_reused=True)


def read_bound_candidate(path, expected_sha, *, recipe, recipe_identity,
                         factory_result_sha, tail_config_sha, driver_source):
    """Source/point binding used by the independent two-phase driver.

    This does not re-evaluate a model or add a scientific pass/fail condition.
    The original full phase bodies retain all their own current input guards.
    """
    require_actions()
    value, identity = read(path, expected_sha)
    same_job(value, "R449 bound candidate")
    require(value.get("schema") == SCHEMA and value.get("phase") == "BVP-input-bound"
        and value.get("process_exit_code") == 0 and value.get("source_sha256") == own_source()["sha256"]
        and same_payload(value["generated_BVP_recipe"], recipe_identity)
        and value["actual_factory_result"]["sha256"] == factory_result_sha
        and value["actual_current_native_configuration"]["sha256"] == tail_config_sha
        and same_payload(value["actual_candidate_driver"], receipt(driver_source)),
        "The actual candidate/factory/config/driver recipe binding differs")
    origin = recipe.get("initial_parameter_origin", {})
    require(recipe.get("schema") == BVP_RECIPE_SCHEMA
        and origin.get("schema") == SCHEMA+"-BVP-origin"
        and origin.get("adapter_source", {}).get("sha256") == own_source()["sha256"]
        and origin.get("original_parameter_array") == dict(bytes=ORIGINAL_WORD_BYTES, sha256=ORIGINAL_WORD_SHA)
        and origin.get("candidate_policy") == POLICY
        and origin.get("projected_binary64le") == value["projected_binary64le"]
        and raw_words(recipe["initial_ten_parameters"]) == value["projected_binary64le"],
        "Retain all ten explicitly declared candidate words, including nonzero xi")
    return identity


def fresh_output(path):
    root = Path(os.environ["RUNNER_TEMP"]).resolve()
    path = Path(path)
    require(not path.exists() and not path.is_symlink()
        and path.resolve().is_relative_to(root) and path.resolve() != root,
        "Use a fresh request-owned directory strictly inside RUNNER_TEMP")
    path.mkdir(parents=True, exist_ok=False)
    return path


def main(argv=None):
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="phase", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--parameter-input", type=Path, required=True)
    p.add_argument("--model-recipe-template", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p = sub.add_parser("bind")
    for name in ("preparation-result", "factory-directory", "current-C-directory",
                 "cut-twojet-readout", "BVP-recipe-template", "tail-config", "code-directory", "out"):
        p.add_argument("--"+name, type=Path, required=True)
    for name in ("preparation-result-sha256", "factory-result-sha256", "current-C-result-sha256",
                 "cut-twojet-readout-sha256", "tail-config-sha256", "candidate-driver-sha256"):
        p.add_argument("--"+name, required=True)
    p.add_argument("--request-number", type=int, required=True)
    p.add_argument("--sampling-startup-reserve-seconds", type=int, required=True)
    args = parser.parse_args(argv)
    if args.phase == "bind":
        require(args.request_number > 0, "The future public request number is explicit; none is selected here")
        require(args.sampling_startup_reserve_seconds > 0,
            "Declare the actual sampling startup reserve explicitly; no inherited default")
    args.out = fresh_output(args.out)
    report = dict(schema=SCHEMA, repository=REPOSITORY, source_sha256=own_source()["sha256"],
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        requested_phase=args.phase, phase="started", process_exit_code=None,
        original202_word_identity=dict(bytes=ORIGINAL_WORD_BYTES, sha256=ORIGINAL_WORD_SHA),
        source_baselines=dict(accurate_factory=FACTORY_SHA, original_joint_two_problem_driver=JOINT_DRIVER_BASELINE_SHA),
        this_adapter_does_not_execute_C_factory_native_or_BVP=True,
        external_owner_clock_not_started_or_reset=True,
        raw_output_not_published_or_uploaded=True, exception=None)
    code = 0
    try:
        (prepare if args.phase == "prepare" else bind)(args, report)
    except Exception as error:
        code = 2
        report.update(phase="exception", exception=repr(error), traceback=traceback.format_exc(),
            actual_design453_accepted=False, actual_frozen450_accepted=False)
    report["process_exit_code"] = code
    raw = canonical(report)
    if len(raw) > LIMIT:
        # This is an honest transport failure; no scientific flag is changed.
        write(args.out/"adapter-result.json", report)
        print(json.dumps(dict(event="R449_candidate_necessary_over_limit", bytes=len(raw), sha256=sha(raw),
            limit=LIMIT, adapter_phase=report["phase"], complete_necessary_readback=False)), flush=True)
        return 70
    identity = write(args.out/"adapter-result.json", report)
    print("BEGIN_R449_CANDIDATE_NECESSARY", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_R449_CANDIDATE_NECESSARY", flush=True)
    print(json.dumps(dict(event="R449_candidate_adapter_returned", result=identity,
        phase=report["phase"], process_exit_code=code, complete_necessary_readback=True)), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
