#!/usr/bin/env python3
"""New complete physical waist first-row receiver.
Only new scalar combinations of two immutable successful small receipts.
No old scientific source is imported or called; the ST source is read as text.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, importlib.metadata, json, os, platform, re, time, traceback
from pathlib import Path
from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
KIND = "actual_complete_physical_waist_first_row_receiver_v1"
MANIFEST_KIND = "complete_physical_waist_first_row_receiver_inputs_v1"
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0"}
GATE_COUNT = 16
SCI_LIMIT = 75000
PARAMETERS = json.loads("{\"arithmetic_bits\":320,\"exact_complete_radial_interval\":[\"0\",\"76285779072683/320000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"continuous_centre_definition_sha256\":\"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47\",\"continuous_response_definition_sha256\":\"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04\",\"input_cutoff_abs_j\":97,\"exact_moving_normalizer_cutoff_abs_j\":268435456,\"physical_frequency\":\"n=4|j|\",\"selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"reference_column\":\"same terminal Ai free P8 first column\",\"exact_row\":\"B_partial Q_R (Y_A - Y_WJ)\",\"exact_row_input\":\"same reflected natural root H^(-4/3) with |j|>=97\",\"exact_row_output\":\"raw moving-angle even meanzero L2 primitive row\",\"same_trial\":\"single W=A(1+M_C I)Lc and original compressed TJ\",\"same_cut_density_error\":\"original full-T cut difference from SW/UT\",\"ordinary_source\":\"(P[T DW-Q W], -Zy T W), ungauged primitive and complete mean\",\"complete_source_rows\":3071,\"complete_interface_rows\":3070,\"genuine_interface_rows\":2549,\"conservative_interface_rows\":521,\"independent_physical_mean_coordinates\":2,\"old_ST_gate_count\":25,\"old_SW_gate_count\":24,\"saved_original_scalar_record_count\":14,\"copied_complete_scope_object_count\":9,\"new_gain_scalar_count\":4,\"new_contribution_scalar_count\":5,\"expected_actual_gate_count\":16,\"whole_selection\":\"final serialized complete upper endpoints; old candidate wins ties\",\"old_successful_scientific_calls_allowed\":0,\"signed_adjoint_cancellation_numerically_certified\":false,\"full_incoming_or_finite_Schur_or_return_R0_claimed\":false}")
PIN_SPECS = json.loads("{\"contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-complete-adjoint-physical-waist-row-and-saved-first-row-receiver.md\",\"git_blob\":\"1dfa6d56a249157b27d23d6249fb451cb9fdb6d0\",\"bytes\":28366,\"sha256\":\"0a92e2e5e5c1f0e1e93bc509ad5883d20630ad9909be3b33eaff7546f641702a\"},\"st_execution\":{\"path\":\"topics/visible-flex-exact-nearby/notes/strict_tail_true_cut_to_waist_ci/run-43757644616-1/execution.json\",\"git_blob\":\"94eb4c7d643edc33f696d101753e4d23a7936a26\",\"bytes\":47282,\"sha256\":\"b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637\"},\"sw_science\":{\"path\":\"topics/visible-flex-exact-nearby/notes/single_root_first_symbol_trial_ci/run-43781399696-1/actual-scientific-conclusion.json\",\"git_blob\":\"3dbcf931b1b98fb7a7822ef5c1ed7df10135b894\",\"bytes\":27687,\"sha256\":\"f16a1dc6177ef8a76d34e859fa37a51461a6ed142f20714e3dcb9212a3647659\"},\"st_source\":{\"path\":\"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_tail_true_cut_to_waist.py\",\"git_blob\":\"e47bdce4d3716b800f6282be6a45cc3323b8119b\",\"bytes\":50111,\"sha256\":\"743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5\"}}")
PINNED = {role: row["sha256"] for role, row in PIN_SPECS.items()}
SCHEMA = json.loads("[\"kind\",\"complete\",\"proved\",\"stage\",\"failure\",\"source_sha256\",\"input_manifest_sha256\",\"input_sha256\",\"verified_original_inputs\",\"parameters\",\"runtime\",\"arithmetic_bits\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"actual_returncode\",\"gates\",\"actual_progress\",\"accepted_old_receipts\",\"copied_original_scalar_records\",\"copied_complete_original_scopes\",\"complete_new_first_row_gain_conclusion\",\"complete_new_whole_row_candidate_conclusion\",\"complete_whole_row_selection\",\"original_scalar14_canonical_sha256\",\"original_scope9_canonical_sha256\",\"scope\",\"actual_mathematical_wall_seconds\",\"old_successful_targets_recomputed\",\"new_reproducible_arrays_persisted\"]")
EXPECTED_PROGRESS = json.loads("{\"completed_old_receipts_read\":2,\"completed_old_scalar_records_copied\":14,\"completed_old_scope_objects_copied\":9,\"entered_new_scalar_stage\":true,\"complete_first_row_gain_graph_count\":1,\"new_gain_scalar_records_saved\":4,\"complete_whole_candidate_graph_count\":1,\"new_contribution_scalar_records_saved\":5,\"complete_whole_selection_count\":1,\"actual_old_source_calls\":0,\"actual_old_scientific_targets_recomputed\":0,\"final_readonly_input_check_count\":5}")
OLD_SCALAR_SHA = "070b718bed4a386dea25f0570c17a8573e8d1f33befea4edb81db9ebf0d4dc66"
OLD_SCOPE_SHA = "fa01be532e31dc611aaf858b505115afb2596120f54de30de59ddb4b537ddec7"
ST_EXPECTED = json.loads("{\"execution_kind\":\"actual_public_strict_tail_true_cut_to_waist_execution\",\"scientific_kind\":\"actual_complete_strict_tail_true_branch_cut_to_waist_v1\",\"run_id\":\"43757644616\",\"run_attempt\":\"1\",\"source_sha256\":\"743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5\",\"input_manifest_sha256\":\"e43b2c7036088cd8d1401c580c1aa6ef694d283057dcce7c65839f92fc1b0e80\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"gates\":25}")
SW_EXPECTED = json.loads("{\"scientific_kind\":\"actual_single_complete_root_first_symbol_trial_v1\",\"run_id\":\"43781399696\",\"run_attempt\":\"1\",\"source_sha256\":\"d0380618d0e57fe4771ad0fb5b6a92990225abc9c6f2f379959653eab4e93fb9\",\"input_manifest_sha256\":\"5d62a5e758cd11d4325d1797666bb57683ee94f79e4d4fb4351c33b7f94d78e4\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"gates\":24}")
SCOPE = json.loads("{\"same_complete_reflected_primitive_waist_row\":true,\"same_selected_parameter_and_original_terminal_Ai_column\":true,\"same_single_W_and_same_compressed_TJ_trial\":true,\"input_window\":\"same reflected natural root H^(-4/3), original |j|>=97\",\"output_window\":\"raw moving-angle even meanzero L2 primitive row\",\"complete_mean_source_and_both_physical_mean_coordinates_retained\":true,\"raw_h1_mean_redundancy_does_not_delete_even_mean_or_amplitude\":true,\"all_3070_interfaces_without_length_factor_retained\":true,\"PC_ST4_cut_and_saved_waist_FT_each_retained_once\":true,\"old_ST_and_SW_successes_read_only\":true,\"old_scientific_imports_calls_native_restoration_and_new_grids\":0,\"whole_selection_same_object_and_same_output_units_only\":true,\"signed_adjoint_cancellation_numerically_certified\":false,\"raw_L2_derivative_readout_proved\":false,\"physical_leading_row_square_inverse_proved\":false,\"full_incoming_inverse_proved\":false,\"finite_Schur_inverse_proved\":false,\"whole_return_R0_proved\":false,\"actual_nonlinear_background_proved\":false,\"final_surface_proved\":false,\"independent_even_mean_amplitude_nu_head_and_other_ports_retained\":true}")
BEGIN = "PHYSICAL_WAIST_FIRST_ROW_SCIENTIFIC_RESULT_BEGIN"
END = "PHYSICAL_WAIST_FIRST_ROW_SCIENTIFIC_RESULT_END"

def canonical(x):
    return (json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False) + "\n").encode("utf-8")

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def sha(path):
    return digest(Path(path).read_bytes())

def read(path):
    def nonfinite(token):
        raise ValueError("nonfinite JSON token in immutable small input: " + token)
    return json.loads(Path(path).read_bytes(), parse_constant=nonfinite)

def save(path, doc):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = canonical(doc)
    temporary = path.with_name(path.name + ".partial")
    temporary.write_bytes(raw)
    temporary.replace(path)
    return raw

def gate(doc, name, passed):
    value = bool(passed)
    doc["gates"].append({"name": name, "passed": value})
    if not value:
        raise ValueError("required complete gate failed: " + name)

def rb(value):
    if isinstance(value, arb):
        x = value
    elif isinstance(value, dict) and set(value) == {"ball"}:
        x = arb(value["ball"])
    elif isinstance(value, (str, int)):
        x = arb(value)
    else:
        raise TypeError("expected an entire scalar ball record")
    if not x.is_finite():
        raise ValueError("a complete old or new scalar ball is not finite")
    return x

def up(value):
    return rb(value).upper()

def record(value):
    return {"ball": rb(value).str(72)}

def ball_count(value):
    if isinstance(value, dict):
        if set(value) == {"ball"}:
            return 1
        return sum(ball_count(x) for x in value.values())
    if isinstance(value, list):
        return sum(ball_count(x) for x in value)
    return 0

def successful(r, expected):
    return (
        r.get("kind") == expected["scientific_kind"]
        and str(r.get("run_id")) == expected["run_id"]
        and str(r.get("run_attempt")) == expected["run_attempt"]
        and r.get("complete") is True and r.get("proved") is True
        and r.get("actual_returncode") == 0 and r.get("failure") is None
        and r.get("source_sha256") == expected["source_sha256"]
        and r.get("input_manifest_sha256") == expected["input_manifest_sha256"]
        and r.get("runtime") == expected["runtime"]
        and r.get("arithmetic_bits") == 320
        and len(r.get("gates", [])) == expected["gates"]
        and all(x.get("passed") is True for x in r.get("gates", []))
    )

def old_scalar_records(st, sw):
    product = st["complete_new_strict_propagation_conclusion"]
    end = st["complete_endpoint_and_source_conclusion"]
    source = sw["complete_new_source_and_interface_conclusion"]
    trial = sw["complete_new_full_and_compressed_trial_conclusion"]
    old = sw["copied_complete_scalar_inputs_read_verbatim"]
    result = {
        "m11": product["complete_reverse_matrix"][0][0],
        "m12": product["complete_reverse_matrix"][0][1],
        "O0": end["waist_output_factor"],
        "Ic": end["cut_input_factor"],
        "Jstar": end["complete_source_injection_upper"],
        "Flead": source["complete_ordinary_leading_defect_L1_upper"],
        "FQ": source["complete_ordinary_Q_F0_F1_T1F2_L1_upper"],
        "Fmean": source["complete_ordinary_independent_mean_L1_upper"],
        "Jy": source["complete_all_interface_impulses_upper"],
        "Ecut": trial["original_fullT_cut_error_read_verbatim"],
        "Ewaist": trial["complete_physical_waist_FT_W_correction_upper"],
        "C_PC": old["C_PC"],
        "C_ST4": old["C_ST4"],
        "Cold": sw["complete_new_ordered_paid_conclusion"]["complete_Cstar_singleW_upper"],
    }
    return copy.deepcopy(result)

def old_scope_objects(st, sw):
    return copy.deepcopy({
        "ST_complete_parameter_scope": st["mathematical_parameters"],
        "ST_complete_family_identity":
            st["complete_accepted_original_conclusion"]["exact_family_identity_read_verbatim"],
        "ST_complete_positive_propagation": st["complete_new_strict_propagation_conclusion"],
        "ST_complete_endpoint_and_source": st["complete_endpoint_and_source_conclusion"],
        "SW_complete_parameter_scope": sw["parameters"],
        "SW_complete_selected_scope": sw["copied_complete_selected_scope"],
        "SW_complete_source_and_interface": sw["complete_new_source_and_interface_conclusion"],
        "SW_complete_trial_and_endpoints": sw["complete_new_full_and_compressed_trial_conclusion"],
        "SW_complete_original_scope": sw["scope"],
    })

def checked_inputs(a, doc):
    actual = {"Python": platform.python_version(),
              "python_flint": importlib.metadata.version("python-flint")}
    doc["runtime"] = actual
    doc["arithmetic_bits"] = ctx.prec
    gate(doc, "public runtime and exact 320-bit arithmetic with actual workflow and checkout identities",
         actual == RUNTIME and a.bits == ctx.prec == 320
         and os.environ.get("GITHUB_ACTIONS") == "true"
         and os.environ.get("GITHUB_REPOSITORY") == PUBLIC
         and str(a.run_id) == os.environ.get("GITHUB_RUN_ID")
         and str(a.run_attempt) == os.environ.get("GITHUB_RUN_ATTEMPT")
         and bool(re.fullmatch(r"[0-9a-f]{40}", str(doc["workflow_event_commit"])))
         and bool(re.fullmatch(r"[0-9a-f]{40}", str(doc["actual_scientific_checkout_commit"]))))
    m = read(a.manifest)
    paths = {role: Path(getattr(a, role)).resolve() for role in PINNED}
    expected_files = {x["role"]: x for x in m.get("files", [])}
    same_files = all(
        role in expected_files
        and all(expected_files[role].get(k) == row[k]
                for k in ("path", "git_blob", "bytes", "sha256"))
        and paths[role] == (a.repo.resolve() / row["path"]).resolve()
        and paths[role].is_file()
        and paths[role].stat().st_size == row["bytes"]
        and sha(paths[role]) == row["sha256"]
        for role, row in PIN_SPECS.items()
    )
    gate(doc, "four exact current mathematical texts and their complete manifest closure are frozen",
         sha(a.manifest) == a.manifest_sha
         and m.get("kind") == MANIFEST_KIND
         and m.get("public_repository") == PUBLIC
         and m.get("source_sha256") == doc["source_sha256"]
         and m.get("parameters") == PARAMETERS
         and m.get("scientific_runtime") == RUNTIME
         and m.get("mathematical_input_sha256") == PINNED
         and m.get("expected_actual_gate_count") == GATE_COUNT
         and m.get("expected_input_count") == 7
         and m.get("expected_immutable_AST_files") == 3 and same_files)
    gate(doc, "only bounded current UTF8 JSON proof and source texts are read with no archive or old import",
         len(paths) == 4
         and m.get("all_inputs_are_current_small_texts") is True
         and m.get("legacy_artifact_inputs") == []
         and m.get("old_successful_scientific_calls_allowed") == 0
         and all(p.stat().st_size < 100000 and p.suffix in (".json", ".md", ".py")
                 and not p.read_bytes().startswith(b"\x1f\x8b") for p in paths.values()))
    doc["input_sha256"] = {**PINNED, "manifest": a.manifest_sha}
    doc["verified_original_inputs"] = {
        role: {"bytes": paths[role].stat().st_size, "sha256": sha(paths[role])}
        for role in PINNED
    }
    se = read(paths["st_execution"])
    st = se.get("actual_scientific_receipt", {})
    gate(doc, "original ST execution and its complete embedded science retain all 25 original gates",
         se.get("kind") == ST_EXPECTED["execution_kind"]
         and str(se.get("run_id")) == ST_EXPECTED["run_id"]
         and str(se.get("run_attempt")) == ST_EXPECTED["run_attempt"]
         and se.get("complete") is True and se.get("actual_returncode") == 0
         and se.get("actual_failure") is None
         and se.get("actual_source_budget_processes") == 1
         and se.get("source_budget_source_sha256") == ST_EXPECTED["source_sha256"]
         and se.get("input_manifest_sha256") == ST_EXPECTED["input_manifest_sha256"]
         and successful(st, ST_EXPECTED))
    sw = read(paths["sw_science"])
    gate(doc, "original SW complete science retains its distinct 24-gate schema and same successful target",
         successful(sw, SW_EXPECTED) and sw.get("stage") == "complete"
         and sw.get("complete_new_single_root_first_symbol_bound_proved") is True
         and sw.get("complete_new_ordered_paid_subtotal_proved") is True
         and sw.get("complete_full_Ei_Eo_proved") is False
         and sw.get("full_incoming_inverse_proved") is False
         and sw.get("finite_Schur_inverse_proved") is False)
    doc["accepted_old_receipts"] = {
        "st_execution": {**copy.deepcopy(ST_EXPECTED),
                         "complete": True, "proved": True, "actual_returncode": 0,
                         "input_sha256": PINNED["st_execution"]},
        "sw_science": {**copy.deepcopy(SW_EXPECTED),
                       "complete": True, "proved": True, "actual_returncode": 0,
                       "input_sha256": PINNED["sw_science"]},
    }
    doc["actual_progress"]["completed_old_receipts_read"] = 2
    sp = st["mathematical_parameters"]
    wp = sw["parameters"]
    family = st["complete_accepted_original_conclusion"]["exact_family_identity_read_verbatim"]
    selected = sw["copied_complete_selected_scope"]
    gate(doc, "same repaired real family cut selected parameter root input and original normalizer remain typed",
         sp["exact_real_delta_radius"] == wp["exact_real_delta_radius"]
             == PARAMETERS["exact_real_delta_radius"]
         and sp["fixed_intrinsic_parameter"] == wp["fixed_intrinsic_parameter"] == "eta_0"
         and sp["exact_true_branch_cut"] == wp["exact_strict_cut"] == PARAMETERS["exact_strict_cut"]
         and wp["exact_complete_radial_interval"] == PARAMETERS["exact_complete_radial_interval"]
         and all(family[k] == wp[k] == PARAMETERS[k] for k in
                 ("continuous_centre_definition_sha256", "continuous_response_definition_sha256"))
         and wp["input_cutoff_abs_j"] == 97
         and wp["exact_moving_normalizer_cutoff_abs_j"] == 268435456
         and wp["reference_column"] == PARAMETERS["reference_column"]
         and wp["physical_frequency"] == sp["physical_frequency"] == "n=4|j|"
         and selected["only_same_selected_actual_conjugacy"] is True
         and selected["selected_parameter_absolute_upper"]
             == PARAMETERS["selected_parameter_absolute_upper"]
         and selected["exact_order"] == "S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)")
    product = st["complete_new_strict_propagation_conclusion"]
    end = st["complete_endpoint_and_source_conclusion"]
    matrix = product["complete_reverse_matrix"]
    gate(doc, "saved complete reverse matrix contains both means and every shorter ordered source insertion",
         product["exact_complete_interval"] == PARAMETERS["exact_complete_radial_interval"]
         and product["all_shorter_ordered_subproducts_and_affine_insertions_retained"] is True
         and product["complete_both_mean_and_all_Fourier_coordinates_retained"] is True
         and product["original_prefix_matrices_read_verbatim"] is True
         and product["original_0_ra_curvature_cost_reused_as_one_whole_budget"] is True
         and product["no_old_upper_subtraction_or_division"] is True
         and len(matrix) == 2 and all(len(row) == 2 for row in matrix)
         and all(rb(x).lower() >= 0 for row in matrix for x in row)
         and end["density_impulses_require_their_own_radial_entry_factor"] is True
         and end["both_independent_means_and_complete_finite_blocks_retained"] is True)
    original_source = paths["st_source"].read_text(encoding="utf-8")
    ast.parse(original_source)
    literals = (
        'fullminus=scale(mm(oldminus,minus),up(c2.exp()))',
        'o0=up(up(waist["density_radial_factor_upper"])/gap(waist["q_lower"],"waist q lower").sqrt())',
        'ic=up(k["qhi"].sqrt()/ncminus)',
        'inj=max(up(end["complete_strict_Hminus1_source_injection_upper"]),jtail)',
        'jtail=up(k["CI"]*max(arb(1),maximum["qplus"]))',
        'backsrc=up(o0*ub*inj)',
        'all_shorter_ordered_subproducts_and_affine_insertions_retained=True',
    )
    contract = paths["contract"].read_text(encoding="utf-8")
    gate(doc, "original positive algorithm and exact row proof are only read with true radial endpoint and source directions",
         all(x in original_source for x in literals)
         and all(x in contract for x in (r"\tag{WAD.32}", r"\tag{WAD.35}", r"\tag{WAD.36}"))
         and end["exact_full_radial_length"] == PARAMETERS["exact_strict_cut"]
         and end["affine_impulses_have_no_radial_length_factor"] is True)
    source = sw["complete_new_source_and_interface_conclusion"]
    trial = sw["complete_new_full_and_compressed_trial_conclusion"]
    gate(doc, "SW separately saved primitive full Q mean and all interfaces refer to the same complete compressed trial",
         wp["exact_source"] == "(P[T DW-Q W], -Zy T W)"
         and wp["new_trial"] == "(P T W,0)" and wp["returned_trial"] == "(P TJ W,0)"
         and wp["independent_physical_mean_coordinates"] == 2
         and source["complete_interface_count"] == 3070
         and source["complete_genuine_interface_count"] == 2549
         and source["complete_conservative_interface_count"] == 521
         and source["exact_ordinary_radial_interval"] == PARAMETERS["exact_complete_radial_interval"]
         and source["full_Zy_mean_row_retained"] is True
         and source["original_full_Q_including_F0_F1_T1F2_retained"] is True
         and source["jump_has_no_radial_length_factor"] is True
         and source["original_successful_source_integrals_and_jump_sum_not_recomputed"] is True
         and trial["cut_trial_is_exactly_the_same_Bc"] is True
         and trial["inverse_is_only_same_actual_TJ_not_full_T"] is True
         and trial["source_receiver_already_contains_output_waist_ng"] is True
         and trial["waist_ng_times_FT_W_paid_once"] is True
         and trial["complete_physical_mean_coordinates"] == 2)
    saved = old_scalar_records(st, sw)
    scopes = old_scope_objects(st, sw)
    gate(doc, "fourteen entire old scalar records and nine whole scope objects are copied literally with finite positive budgets",
         len(saved) == 14 and len(scopes) == 9
         and digest(canonical(saved)) == OLD_SCALAR_SHA
         and digest(canonical(scopes)) == OLD_SCOPE_SHA
         and all(set(x) == {"ball"} and rb(x).lower() > 0 for x in saved.values()))
    doc["copied_original_scalar_records"] = saved
    doc["copied_complete_original_scopes"] = scopes
    doc["original_scalar14_canonical_sha256"] = OLD_SCALAR_SHA
    doc["original_scope9_canonical_sha256"] = OLD_SCOPE_SHA
    doc["actual_progress"]["completed_old_scalar_records_copied"] = 14
    doc["actual_progress"]["completed_old_scope_objects_copied"] = 9
    doc["stage"] = "complete_saved_actual_admission"
    save(a.out, doc)
    return paths, saved

def first_row_gains(saved, doc):
    values = {key: up(value) for key, value in saved.items()}
    m11, m12 = values["m11"], values["m12"]
    row_norm = record(up(up(m11 * m11 + m12 * m12).sqrt()))
    cut = record(up(values["O0"] * values["Ic"] * up(row_norm)))
    primitive = record(up(values["O0"] * values["Jstar"] * m11))
    mean = record(up(values["O0"] * values["Jstar"] * m12))
    result = {
        "complete_first_matrix_row_L2_upper": row_norm,
        "complete_density_cut_row_gain_upper": cut,
        "complete_ungauged_primitive_row_gain_upper": primitive,
        "complete_ungauged_mean_row_gain_upper": mean,
        "uses_complete_saved_first_row_not_whole_Frobenius": True,
        "all_shorter_insertions_from_original_positive_algorithm": True,
        "waist_output_and_cut_input_factors_in_true_directions": True,
        "full_mean_source_not_removed": True,
        "physical_frequency_and_ordinary_measure_retained": True,
    }
    gate(doc, "four new first-row scalar records retain cut density and separate ungauged primitive mean source units",
         ball_count(result) == 4
         and all(rb(x).lower() > 0 for x in (row_norm, cut, primitive, mean)))
    return result

def complete_candidate(saved, gains, doc):
    old = {key: up(value) for key, value in saved.items()}
    gy = up(gains["complete_ungauged_primitive_row_gain_upper"])
    gz = up(gains["complete_ungauged_mean_row_gain_upper"])
    gc = up(gains["complete_density_cut_row_gain_upper"])
    cut = record(up(gc * old["Ecut"]))
    primitive = record(up(gy * up(old["Flead"] + old["FQ"])))
    mean = record(up(gz * old["Fmean"]))
    jump = record(up(gy * old["Jy"]))
    candidate = record(up(
        old["C_PC"] + old["C_ST4"] + up(cut) + up(primitive)
        + up(mean) + up(jump) + old["Ewaist"]))
    result = {
        "complete_cut_contribution_upper": cut,
        "complete_primitive_source_contribution_upper": primitive,
        "complete_independent_mean_source_contribution_upper": mean,
        "complete_all_3070_interface_contribution_upper": jump,
        "complete_first_row_candidate_upper": candidate,
        "PC_ST4_and_waist_FT_retained_verbatim_once": True,
        "primitive_source_uses_both_complete_leading_and_Q_parts": True,
        "same_original_single_W_and_compressed_TJ_trial": True,
        "interfaces_have_no_radial_length_factor": True,
        "no_new_source_integral_or_positive_product": True,
        "source_gain_already_contains_waist_output_factor": True,
        "saved_waist_FT_correction_not_multiplied_by_ng_again": True,
    }
    gate(doc, "the complete new candidate sums all four physical contributions PC ST4 and the one saved waist correction",
         ball_count(result) == 5
         and all(rb(x).lower() > 0 for x in (cut, primitive, mean, jump, candidate)))
    return result

def complete_minimum(saved, candidate, doc):
    rows = [
        {"label": "saved_old_complete_Cstar", "upper": copy.deepcopy(saved["Cold"])},
        {"label": "new_complete_first_row_candidate",
         "upper": copy.deepcopy(candidate["complete_first_row_candidate_upper"])},
    ]
    index = 1 if up(rows[1]["upper"]) < up(rows[0]["upper"]) else 0
    result = {
        "comparison": "whole saved old Cstar and complete new first-row candidate",
        "complete_candidates": rows,
        "selected_index": index,
        "selected_label": rows[index]["label"],
        "complete_selected_row_upper": copy.deepcopy(rows[index]["upper"]),
        "new_candidate_upper_strictly_smaller": index == 1,
        "old_candidate_wins_ties": True,
        "entrywise_minimum_used": False,
        "different_trial_or_different_output_unit_minimum_used": False,
    }
    gate(doc, "only final serialized complete same-row uppers are compared with the old complete record retained on a tie",
         len(rows) == 2
         and result["complete_selected_row_upper"] == rows[index]["upper"]
         and rows[0]["upper"] == saved["Cold"]
         and rows[1]["upper"] == candidate["complete_first_row_candidate_upper"]
         and up(result["complete_selected_row_upper"]).is_finite())
    return result

def run(a, doc):
    paths, saved = checked_inputs(a, doc)
    doc["actual_progress"]["entered_new_scalar_stage"] = True
    doc["stage"] = "new_complete_first_row_gain_conclusion"
    save(a.out, doc)
    gains = first_row_gains(saved, doc)
    doc["complete_new_first_row_gain_conclusion"] = gains
    doc["actual_progress"]["complete_first_row_gain_graph_count"] = 1
    doc["actual_progress"]["new_gain_scalar_records_saved"] = 4
    doc["stage"] = "complete_new_first_row_gain_conclusion"
    save(a.out, doc)
    candidate = complete_candidate(saved, gains, doc)
    doc["complete_new_whole_row_candidate_conclusion"] = candidate
    doc["actual_progress"]["complete_whole_candidate_graph_count"] = 1
    doc["actual_progress"]["new_contribution_scalar_records_saved"] = 5
    doc["stage"] = "complete_new_whole_row_candidate_conclusion"
    save(a.out, doc)
    selection = complete_minimum(saved, candidate, doc)
    doc["complete_whole_row_selection"] = selection
    doc["actual_progress"]["complete_whole_selection_count"] = 1
    doc["stage"] = "complete_whole_row_selection"
    save(a.out, doc)
    gate(doc, "all fourteen old balls nine scopes and all independent physical obligations remain unchanged",
         digest(canonical(doc["copied_original_scalar_records"])) == OLD_SCALAR_SHA
         and digest(canonical(doc["copied_complete_original_scopes"])) == OLD_SCOPE_SHA
         and doc["scope"] == SCOPE
         and doc["old_successful_targets_recomputed"] == 0
         and doc["new_reproducible_arrays_persisted"] is False)
    unchanged = all(paths[k].stat().st_size == PIN_SPECS[k]["bytes"]
                    and sha(paths[k]) == PINNED[k] for k in PINNED)
    gate(doc, "every old mathematical byte and the actual manifest still have their original exact hashes",
         unchanged and sha(a.manifest) == a.manifest_sha)
    doc["actual_progress"]["final_readonly_input_check_count"] = 5
    doc["stage"] = "complete_final_readonly_and_schema_checks"
    gate(doc, "all sixteen gates nine new scalar records and the complete 32-field small schema retain their declared scope",
         len(doc["gates"]) == 15 and all(g["passed"] is True for g in doc["gates"])
         and set(doc) == set(SCHEMA) and len(doc) == 32
         and doc["actual_progress"] == EXPECTED_PROGRESS
         and ball_count(doc["complete_new_first_row_gain_conclusion"]) == 4
         and ball_count(doc["complete_new_whole_row_candidate_conclusion"]) == 5
         and len(canonical(doc)) < SCI_LIMIT)
    doc.update(complete=True, proved=True, actual_returncode=0, failure=None, stage="complete")
    save(a.out, doc)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--manifest-sha", required=True)
    for role in PINNED:
        p.add_argument("--" + role.replace("_", "-"), type=Path, required=True)
    p.add_argument("--repo", type=Path, default=Path.cwd())
    p.add_argument("--run-id", default=os.environ.get("GITHUB_RUN_ID"))
    p.add_argument("--run-attempt", default=os.environ.get("GITHUB_RUN_ATTEMPT"))
    p.add_argument("--bits", type=int, default=320)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError("preserve every existing complete or partial physical-row result")
    started = time.monotonic()
    ctx.prec = a.bits
    progress = {k: (False if isinstance(v, bool) else 0) for k, v in EXPECTED_PROGRESS.items()}
    doc = {
        "kind": KIND, "complete": False, "proved": False,
        "stage": "initial_current_input_admission", "failure": None,
        "source_sha256": sha(__file__), "input_manifest_sha256": a.manifest_sha,
        "input_sha256": {}, "verified_original_inputs": {},
        "parameters": copy.deepcopy(PARAMETERS), "runtime": {},
        "arithmetic_bits": a.bits, "public_repository": PUBLIC,
        "run_id": a.run_id, "run_attempt": a.run_attempt,
        "workflow_event_commit": os.environ.get("GITHUB_SHA"),
        "actual_scientific_checkout_commit": os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        "actual_returncode": 1, "gates": [], "actual_progress": progress,
        "accepted_old_receipts": {}, "copied_original_scalar_records": {},
        "copied_complete_original_scopes": {},
        "complete_new_first_row_gain_conclusion": None,
        "complete_new_whole_row_candidate_conclusion": None,
        "complete_whole_row_selection": None,
        "original_scalar14_canonical_sha256": None,
        "original_scope9_canonical_sha256": None,
        "scope": copy.deepcopy(SCOPE), "actual_mathematical_wall_seconds": None,
        "old_successful_targets_recomputed": 0,
        "new_reproducible_arrays_persisted": False,
    }
    save(a.out, doc)
    try:
        run(a, doc)
    except Exception as error:
        doc.update(complete=False, proved=False, actual_returncode=1,
                   failure={"error_type": type(error).__name__, "message": str(error),
                            "actual_progress": copy.deepcopy(doc["actual_progress"]),
                            "complete_new_graphs_preserved": [
                                name for name in ("complete_new_first_row_gain_conclusion",
                                                  "complete_new_whole_row_candidate_conclusion",
                                                  "complete_whole_row_selection")
                                if doc.get(name) is not None]})
        traceback.print_exc()
    doc["actual_mathematical_wall_seconds"] = time.monotonic() - started
    raw = save(a.out, doc)
    print(BEGIN, flush=True)
    print(json.dumps({"bytes": len(raw), "sha256": digest(raw)}, sort_keys=True), flush=True)
    print(raw.decode("utf-8"), end="", flush=True)
    print(END, flush=True)
    if len(raw) > SCI_LIMIT:
        raise ValueError("complete scientific payload preserved before 75000-byte guard")
    return doc["actual_returncode"]

if __name__ == "__main__":
    raise SystemExit(main())
