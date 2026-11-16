#!/usr/bin/env python3
"""Continue only the unsaved root97 stages from one exact published prefix."""
from __future__ import annotations

import argparse
import ast
import copy
from fractions import Fraction
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import time
import traceback

from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_stable_cutoff97_saved_prefix_recovery.py"
KIND = "complete_root_stable_cutoff97_saved_prefix_recovery"
MANIFEST_KIND = "complete_root_stable_cutoff97_saved_prefix_recovery_public_inputs_v1"
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0"}
GATE_COUNT = 9
COMPLETE_SCIENCE_MAX_BYTES = 75000
PIN_SPECS = {"r97_contract":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-complete-root-cutoff97-scalar-recipe.md","git_blob":"cc0d98891f52a8c6ec1c718c57d7be143db0134c","bytes":20143,"sha256":"543ebc3899931db63bda92c31ce20d8f21013daac906e00eaf761a28ff582f74"},"recovery_contract":{"path":"topics/visible-flex-exact-nearby/results/R133-supplement-exact-root97-saved-prefix-recovery.md","git_blob":"4f4a4adec13ff9eb1d0a2ad4a5ccabadf3efa00e","bytes":14338,"sha256":"fc8bef9cd1db3fc94fe4b401256957544baa315ab30350d719ba4b0de4b03ac9"},"original_source":{"path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_stable_cutoff97_scalar_gate.py","git_blob":"6f7037839126056ff25dec619150f76b0edcb3a7","bytes":58950,"sha256":"d8bb0de64f6755b0c35621d67cfa33a3c1d0b5975cc6476dc81b2d8abb866a06"},"original_manifest":{"path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-root-stable-cutoff97-scalar-gate-CI-inputs.json","git_blob":"e0e74f7281acf11989075cb2e341822230926cad","bytes":19895,"sha256":"acc09858d35934db5743daf892b6edf370d3bb0185a662b2e96db01f1f68bcce"},"saved_prefix":{"path":"topics/visible-flex-exact-nearby/notes/root_stable_cutoff97_scalar_gate_ci/run-43786583355-1/actual-scientific-conclusion.json","git_blob":"98bc2b2c916ae3f1e3e4c19f3309fed20b64cfad","bytes":30812,"sha256":"95aa4c8d15a1b28e432c987735fa69f75463d8227905935ea151ec0258362e11"},"saved_execution":{"path":"topics/visible-flex-exact-nearby/notes/root_stable_cutoff97_scalar_gate_ci/run-43786583355-1/execution.json","git_blob":"457225f983433eb478f64a76da9cc6712c3add36","bytes":15594,"sha256":"a8075eac021a0e1f49390efcd5b04f8526bd69a5c206ff6d365a0243e76f6146"}}
PINNED = {key: entry["sha256"] for key, entry in PIN_SPECS.items()}
HISTORICAL_INPUTS = []
PARAMETERS = {"arithmetic_bits":320,"expected_actual_gate_count":9,"exact_real_delta_radius":"1/100000000","fixed_intrinsic_parameter":"eta_0","exact_intrinsic_parameter":"-7789843107295549/4611686018427387904","exact_root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"physical_root_piece":2549,"physical_period":"pi/2","normalized_angular_measure":True,"input_cutoff_abs_j":97,"physical_minimum_frequency":388,"physical_frequency":"n=4|j|","exact_real_z_interval":["0","1/9409"],"frequency_relation":"z=j^-2=16*n^-2","retained_physical_means":2,"old_target_calls_allowed":0,"old_source_imports_allowed":0,"expected_current_inputs":9,"expected_total_inputs":9,"expected_Python_AST_files":3,"expected_historical_gzip_inputs":0,"strict_failure_is_complete_scalar_result":True,"full_complex_square_claimed":False,"full_incoming_or_finite_Schur_inverse_claimed":False}
RETAINED_SCOPE = {"scientific_target":"one complete ordinary-L2 original-cutoff97 root stable scalar comparison","exact_real_parameter_family_only":True,"fixed_eta0_and_same_root_piece":True,"full_complex_square_result_claimed":False,"full_mean_of_v_and_every_radial_mean_retained":True,"independent_physical_mean_coordinates":2,"original_reflection_and_nonmean_inverse_domains_retained":True,"complete_two_reference_columns_and_two_carrier_signs_retained":True,"root_potential_small_case_does_not_replace_terminal_shear_case":True,"lambda_is_physical_root_kappa_not_frequency_Airy_scale":True,"positive_mean_rank_is_kept":True,"only_proved_diagonal_mean_subterm_vanishes":True,"full_IR0_uses_original_one_quarter":True,"input_diagonals_not_commuted_through_multipliers_or_J":True,"original_J1_is_complete_left_angular_derivative":True,"old_negative_Sobolev_norms_not_inferred_from_L2":True,"true_nonzero_beta_n_retained":True,"actual_PDE_solution_claimed":False,"full_incoming_inverse_claimed":False,"finite_Schur_inverse_claimed":False,"nonlinear_background_or_final_surface_claimed":False,"next_cutoff_or_scientific_rerun_triggered":False}
COUNTS = {"original_current_mathematical_texts":6,"original_historical_natives":0,"complete_old_mixed_entries":40,"selected_complete_mixed_entries":40,"original_auxiliary_successful_cases":2,"original_auxiliary_failed_cases_retained":2,"reciprocal_eta_derivatives":4,"alpha_ordinary_derivatives":4,"Q1_ordinary_derivatives":3,"delta3_positive_groups":5,"DeltaRD_positive_groups":9,"E0_positive_groups":4,"H0_positive_groups":4,"C1_positive_groups":7,"amplitude_positive_groups":2,"R0_positive_groups":8,"old_successful_scientific_targets_recomputed":0,"old_scientific_modules_imported":0,"new_reference_or_potential_or_fold_solutions":0,"new_grid_or_array_outputs":0,"planned_new_original_cutoff_comparisons":1,"saved_prefix_gate_count":14,"saved_complete_math_conclusions_reused":2,"saved_mixed_selections_recomputed":0,"saved_root_domain_recomputed":0}
COMPLETE_FIELDS = ["kind","complete","proved","actual_returncode","failure","stage","source_sha256","input_manifest_sha256","public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit","runtime","arithmetic_bits","parameters","input_sha256","verified_original_inputs","accepted_old_inputs","copied_old_inputs","copied_old_inputs_sha256","complete_mixed_norm_conclusion","complete_root_domain_conclusion","complete_real_radial_interval_conclusion","complete_root_drift_conclusion","complete_rational_quotient_conclusion","complete_correlated_coefficient_conclusion","complete_ordered_operator_conclusion","original_cutoff97_sufficient_gate_passed","retained_scope","counts","gates","actual_mathematical_wall_seconds","preserved_prefix_evidence","actual_progress"]
GATE_NAMES = ["complete saved original97 prefix, original source, manifest and execution identity","complete real moments and neighborhood radial derivatives retain all mean terms","complete mixed drift derivatives and every D squared p term are finite","complete rational quotient retains both gaps and all third ordinary derivatives","complete collected correlations preserve all nine derivative groups and the true mean","all ordered operator terms and genuine positive diagonal bounds are complete","the optional strict comparison has its exact narrow ordinary L2 scope","all original input bytes remain unchanged with zero old target calls","complete scalar schema retains every conclusion whether the sufficient test passes or fails"]
INITIAL_ACTUAL_PROGRESS = {"saved_prefix_validation_passed":False,"preserved_gate_count":0,"saved_complete_math_conclusions_reused":0,"new_radial_conclusion_completed":0,"new_drift_conclusion_completed":0,"new_quotient_conclusion_completed":0,"new_correlated_conclusion_completed":0,"completed_original_cutoff97_comparisons":0,"old_successful_targets_recomputed":0,"saved_mixed_selections_recomputed":0,"saved_root_domain_recomputed":0,"historical_gzip_restores":0}
SUCCESS_ACTUAL_PROGRESS = {"saved_prefix_validation_passed":True,"preserved_gate_count":14,"saved_complete_math_conclusions_reused":2,"new_radial_conclusion_completed":1,"new_drift_conclusion_completed":1,"new_quotient_conclusion_completed":1,"new_correlated_conclusion_completed":1,"completed_original_cutoff97_comparisons":1,"old_successful_targets_recomputed":0,"saved_mixed_selections_recomputed":0,"saved_root_domain_recomputed":0,"historical_gzip_restores":0}
ORIGINAL = {"kind":"complete_root_stable_cutoff97_scalar_gate","manifest_kind":"complete_root_stable_cutoff97_scalar_gate_public_inputs_v1","execution_kind":"actual_public_root_stable_cutoff97_execution_v1","source_path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_root_stable_cutoff97_scalar_gate.py","source_sha256":"d8bb0de64f6755b0c35621d67cfa33a3c1d0b5975cc6476dc81b2d8abb866a06","manifest_sha256":"acc09858d35934db5743daf892b6edf370d3bb0185a662b2e96db01f1f68bcce","worker_sha256":"22124d85263cff85877bd7a1bee388ad0a42af86a0ac49e3a1370502acccff88","run_id":"43786583355","run_attempt":"1","workflow_event_commit":"a24908ab1483ce63d2c82f09c3d15dd089396a3c","actual_scientific_checkout_commit":"a24908ab1483ce63d2c82f09c3d15dd089396a3c","stage":"complete_new_root_domain","failure":{"message":"nonfinite diagnostic","type":"ArithmeticError"},"prefix_fields":["accepted_old_inputs","actual_mathematical_wall_seconds","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_mixed_norm_conclusion","complete_root_domain_conclusion","copied_old_inputs","copied_old_inputs_sha256","counts","failure","gates","input_manifest_sha256","input_sha256","kind","parameters","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"],"gate_count":14,"complete_input_bytes":432366}
PRESERVED_PREFIX_EVIDENCE = {"kind":"exact_original_root97_prefix_inheritance_v1","original_source_sha256":"d8bb0de64f6755b0c35621d67cfa33a3c1d0b5975cc6476dc81b2d8abb866a06","original_input_manifest_sha256":"acc09858d35934db5743daf892b6edf370d3bb0185a662b2e96db01f1f68bcce","original_science_sha256":"95aa4c8d15a1b28e432c987735fa69f75463d8227905935ea151ec0258362e11","original_execution_sha256":"a8075eac021a0e1f49390efcd5b04f8526bd69a5c206ff6d365a0243e76f6146","original_run_id":"43786583355","original_run_attempt":"1","original_workflow_event_commit":"a24908ab1483ce63d2c82f09c3d15dd089396a3c","original_actual_scientific_checkout_commit":"a24908ab1483ce63d2c82f09c3d15dd089396a3c","original_actual_returncode":1,"original_complete":False,"original_proved":False,"original_stage":"complete_new_root_domain","original_failure":{"message":"nonfinite diagnostic","type":"ArithmeticError"},"original_runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"original_arithmetic_bits":320,"original_mathematical_input_sha256":{"auxiliary":"a6783642ae2c49f66c3a7b54f1506389f24771790f3bd5a324646df8229f9728","fa_science":"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2","genuine_execution":"fabe59eed2174e92352f71b8a0e9d80ce8c127580806f5dab917345b05337f57","high_root":"3b06c881b8b00f8bb830653b3eb290b09687b0a2576320b605ba758e2e706abe","majorants_native":"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144","potential_execution":"d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9","r97_contract":"543ebc3899931db63bda92c31ce20d8f21013daac906e00eaf761a28ff582f74","rbg_proof":"157795fdc7fc415156229f5c0b9674b18f92cce1e8cef8ce8df65a271775f268","rbo_proof":"a45e0264875c1a5cded48c6f108004f3c21b6ade73247a7b02231d9b26a30f50","rd_proof":"34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f","rda_proof":"8d2570c7b28304001c785e7b7a6d4261cf127909dd59d594262fd22d42caa205","ri_proof":"01afb86c1d90db86732c4621abe3f35aeb7e2aea38039eaf56725127ffb8be96","root_native":"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f","root_process":"9f1d18061f1b406f028916adc33484b4deea826a8e4175fd28b0fdb5b690342d","root_publication":"89642fd97b7669449f1138d2c3de6840e19ca84dfe06b5a5a76b608239842812"},"original_passed_gates":[{"name":"actual public Actions runtime and frozen new source","passed":True},{"name":"complete current and two-history manifest closure","passed":True},{"name":"all fifteen mathematical originals and sixteen current texts match byte pins","passed":True},{"name":"original high-root intrinsic run is complete at its fixed bump-zero root","passed":True},{"name":"only separately successful auxiliary cases are accepted and its global failure stays visible","passed":True},{"name":"root process and publication bind the same complete sharper native","passed":True},{"name":"potential actual success separates the root case from the full terminal case","passed":True},{"name":"genuine terminal Ai uses its original nonzero shear and both full columns","passed":True},{"name":"FA2 success preserves the complete original mixed-stage payload","passed":True},{"name":"restored root native has its original complete ordinary L2 and left derivative identity","passed":True},{"name":"restored original 4501-byte stage has its complete no-LF payload identity","passed":True},{"name":"all actual inputs restrict to the same real family and single root piece","passed":True},{"name":"every complete original mixed and angular row is finite with full means","passed":True},{"name":"complete mixed selection and actual independent root gaps are finite","passed":True}],"retained_original_plan":{"C1_positive_groups":7,"DeltaRD_positive_groups":9,"E0_positive_groups":4,"H0_positive_groups":4,"Q1_ordinary_derivatives":3,"R0_positive_groups":8,"alpha_ordinary_derivatives":4,"amplitude_positive_groups":2,"complete_old_mixed_entries":40,"delta3_positive_groups":5,"new_grid_or_array_outputs":0,"new_original_cutoff_comparisons":1,"new_reference_or_potential_or_fold_solutions":0,"old_scientific_modules_imported":0,"old_successful_scientific_targets_recomputed":0,"original_auxiliary_failed_cases_retained":2,"original_auxiliary_successful_cases":2,"original_current_mathematical_texts":13,"original_historical_natives":2,"reciprocal_eta_derivatives":4,"selected_complete_mixed_entries":40},"original_actual_completed_cutoff97_comparisons":0,"preserved_object_sha256":{"accepted_old_inputs":"fd08e85b78ebaba6a1ca7ddeb1e66d35590fa262f928d909bda908312ff6a9d4","copied_old_inputs":"e3a718d39ac2cca555ce22ba6f2bb0a34b1daec6d548e2659ff471aa626e6e54","copied_old_inputs_sha256":"b87f95a0809ec44e72cae7a17726d7728cd0113d207d9bdc95a308bb4019d52f","complete_mixed_norm_conclusion":"cbf0af029a0fca9d54f2f700a9638f95a234a65b1b017dc5e0bec985434c5861","complete_root_domain_conclusion":"37ef7b72ecce7d1e562f66c12a81bf7e5d5c3bc1a6376c2da064d2c85eecc1cd"},"inherited_original_input_validation":{"original_current_text_count":16,"original_historical_native_count":2,"original_verified_input_count":18,"original_receipts_canonical_sha256":"58741eb0f9365eb99e9760a07ef457f209bf94e8cfa88c9b56120dbdacd73cc5","original_complete_input_bytes":432366,"original_receipt_location":"saved_execution.actual_original_Git_input_receipts","current_original_input_validation_reexecuted":False,"current_original_gzip_restore_count":0,"original_natives_still_bound_by_full_original_byte_pins":True},"inherited_original_AST_validation":{"original_file_count":2,"original_inventory_sha256":"b812cf9797ee35b08f56bb8522259b26e773cf01c50487ab015b453f4bd87fe3","original_AST_gate_passed":True,"current_AST_closure_is_separate":True},"preserved_complete_math_conclusions":["complete_mixed_norm_conclusion","complete_root_domain_conclusion"],"preserved_objects_copied_verbatim":True,"typed_restore_roles":{"mixed_selected":"complete_saved_ball_upper_endpoint","lower_domain_fields":["eta_low","lambda_low","qgap"],"upper_domain_fields":["eta","lambda_up","Vroot","shear","J0","J1","L0"],"signed_interval_domain_fields":["beta","K","k1","k2","k3"],"signed_positive_denominator_gate":"k1.lower()>0","old_string_objects_reencoded":False},"new_continuation_scope":{"first_new_stage":"real_radial_intervals","original_radial_values_preserved":False,"complete_old_prefix_targets_recomputed":0,"signed_square_replacements":9,"signed_square_bases":["e1","bt","c2","bA"],"replacement":"square(x)=x*x","old_source_execution_or_import":False,"first_actual_comparison_in_prefix":0}}
PRESERVED_OBJECT_HASHES = {"accepted_old_inputs":"fd08e85b78ebaba6a1ca7ddeb1e66d35590fa262f928d909bda908312ff6a9d4","copied_old_inputs":"e3a718d39ac2cca555ce22ba6f2bb0a34b1daec6d548e2659ff471aa626e6e54","copied_old_inputs_sha256":"b87f95a0809ec44e72cae7a17726d7728cd0113d207d9bdc95a308bb4019d52f","complete_mixed_norm_conclusion":"cbf0af029a0fca9d54f2f700a9638f95a234a65b1b017dc5e0bec985434c5861","complete_root_domain_conclusion":"37ef7b72ecce7d1e562f66c12a81bf7e5d5c3bc1a6376c2da064d2c85eecc1cd"}
RULES = {"role":"rules","path":"topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json","git_blob":"5c5d020913d717bb5bc8ce891297e00eaa8944f7","bytes":2461,"sha256":"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1"}
PUBLICATION_LIMITS = {"complete_science_bytes":75000,"complete_report_bytes":8000,"complete_prepublication_science_report_payload_bytes":90000,"complete_execution_bytes":59000,"pre_science_topic_reserve_bytes":150000,"scientific_file_atomic_and_complete_stdout_before_size_guards":True,"new_artifacts":0,"new_Releases":0}

def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")



def gate(doc, name, condition):
    result = bool(condition)
    doc["gates"].append({"name": name, "passed": result})
    if not result:
        raise ValueError("failed root97 structural gate: " + name)


def passed_gates(value, key, count):
    rows = value.get(key)
    return (isinstance(rows, list) and len(rows) == count
            and all(row.get("passed") is True for row in rows))


def persist(path, doc):
    raw = canonical(doc)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".atomic")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)
    return raw


def print_complete_document(doc):
    raw = canonical(doc)
    print("ROOT97_RECOVERY_SCIENTIFIC_JSON_BEGIN", flush=True)
    print(raw.decode("utf-8"), end="", flush=True)
    print("ROOT97_RECOVERY_SCIENTIFIC_JSON_END", flush=True)
    print(json.dumps({"complete": doc.get("complete", False),
        "stage": doc.get("stage"), "gates": len(doc.get("gates", [])),
        "bytes": len(raw), "sha256": sha(raw)}, sort_keys=True), flush=True)


def finite_tree(value):
    if isinstance(value, arb):
        return value.is_finite()
    if isinstance(value, dict):
        return all(finite_tree(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return all(finite_tree(v) for v in value)
    return True

def ex(value):
    q = Fraction(value)
    return arb(q.numerator) / arb(q.denominator)


def ball(value):
    if isinstance(value, dict):
        value = value["ball"]
    x = arb(value)
    if not x.is_finite():
        raise ArithmeticError("nonfinite original or new scalar")
    return x


def up(value):
    x = abs(ball(value)).upper()
    if not x.is_finite() or x < 0:
        raise ArithmeticError("invalid nonnegative upper")
    return x


def lower(value):
    x = ball(value).lower()
    if not x.is_finite() or not x > 0:
        raise ArithmeticError("missing strict positive lower")
    return x


def upper_sum(values):
    return up(sum(values, arb(0)))


def whole_min(values):
    candidates = [up(x) for x in values]
    if not candidates:
        raise ValueError("empty complete-bound choice")
    winner = min(range(len(candidates)), key=lambda i: candidates[i])
    return candidates[winner], winner


def symmetric(value):
    return arb(0, up(value))


def nonnegative_interval(value):
    return arb(0).union(up(value))


def square(value):
    # Direct interval multiplication encloses every x*x, including midpoint zero.
    return value * value


def encoded(value, path="$"):
    if isinstance(value, arb):
        if not value.is_finite():
            raise ArithmeticError("nonfinite diagnostic at " + path)
        return value.str(75)
    if isinstance(value, dict):
        return {str(k): encoded(v, path + "." + str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encoded(v, path + "[" + str(i) + "]") for i, v in enumerate(value)]
    return value


def diagnostic_tree(value, path="$", nonfinite_paths=None):
    if nonfinite_paths is None:
        nonfinite_paths = []
    if isinstance(value, arb):
        if value.is_finite():
            return value.str(75)
        nonfinite_paths.append(path)
        return {"nonfinite": True, "path": path,
                "raw_arb_representation": str(value),
                "certified_finite_ball": False}
    if isinstance(value, dict):
        return {str(k): diagnostic_tree(v, path + "." + str(k), nonfinite_paths)
                for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [diagnostic_tree(v, path + "[" + str(i) + "]", nonfinite_paths)
                for i, v in enumerate(value)]
    return value


def encode_new_stage(doc, field, stage, value):
    try:
        doc[field] = encoded(value, "$." + field)
    except Exception:
        nonfinite_paths = []
        preserved = diagnostic_tree(value, "$." + field, nonfinite_paths)
        doc["failed_new_stage_diagnostic"] = {
            "attempted_stage": stage, "conclusion_field": field,
            "returned_complete_graph_available": True,
            "all_returned_finite_values_and_nonfinite_labels": preserved,
            "nonfinite_paths": nonfinite_paths,
            "nonfinite_labels_are_not_certified_balls": True,
            "original_prefix_objects_modified": False}
        raise


def real_radial_intervals(s, t):
    u, v = t["U"], t["V"]
    beta, betar = s["beta"][:2]
    k1 = s["k1"]
    mu = nonnegative_interval(u[0][0]**2)
    mv = nonnegative_interval(v[0][0]**2)
    mur = symmetric(u[0][0]*u[1][0])
    eta_actual = s["eta_low"].union(s["eta"][0])
    eta_r, eta_rr = symmetric(s["eta"][1]), symmetric(s["eta"][2])
    e1, e2 = eta_r/eta_actual, eta_rr/eta_actual
    M = beta*mu
    Mr = betar*mu + beta*(2*mur + k1*mv)
    Bm, Em = beta-M, -beta-3*M
    Bmr = betar*(1-mu)-beta*(2*mur+3*k1*mv)
    Emr = -betar*(1+3*mu)-beta*(6*mur+k1*mv)
    ac, trad = e1+Em, e1-4*M
    acp = e2-square(e1)+Emr
    tradp = e2-square(e1)-4*Mr
    qrad, qradp = ac-Bm, acp-Bmr
    Vm = ac*Bm-Bmr
    c2, c3 = s["k2"]/(2*k1), s["k3"]/(6*k1)
    L = e1+c2/2
    bt = (2*e1+c2)/5
    bs = ex("2/7")*((e2+c3)/2+e1*(c2-bt)/2
                    +ex("3/8")*square(bt)-c2*bt/4-square(c2)/8)
    bA = (bt-c2)/4-2*M
    bC = square(bA)+(2*bs-square(bt)-2*c3+square(c2))/4-2*Mr
    return dict(m_u=mu, m_v=mv, m_ur=mur, eta_actual=eta_actual,
        eta_r=eta_r, eta_rr=eta_rr, e1=e1, e2=e2, M=M, Mr=Mr,
        Bm=Bm, Em=Em, Bmr=Bmr, Emr=Emr, ac=ac, acp=acp,
        trad=trad, tradp=tradp, qrad=qrad, qradp=qradp, Vm=Vm,
        c2=c2, c3=c3, L=L, bt=bt, bs=bs, bA=bA, bC=bC)


def product_jet(f, ar, g, br, q):
    return upper_sum(math.comb(q, j)*f[ar][j]*g[br][q-j]
                     for j in range(q+1))


def projected_product(f, ar, g, br):
    a = product_jet(f, ar, g, br, 0)
    b = product_jet(f, ar, g, br, 1)/4
    return whole_min([a, b])[0]


def complete_root_drift(s, t, c):
    u, v = t["U"], t["V"]
    b0, b1, b2 = map(up, s["beta"][:3])
    k1, k2 = up(s["k1"]), up(s["k2"])
    ps = projected_product(u, 0, u, 0)
    psr = up(2*projected_product(u, 0, u, 1)
             +k1*projected_product(v, 0, v, 0))
    psrr = up(2*projected_product(u, 1, u, 1)
              +2*projected_product(u, 0, u, 2)
              +k2*projected_product(v, 0, v, 0)
              +4*k1*projected_product(v, 0, v, 1))
    sph = product_jet(u, 0, u, 0, 1)
    sphph = product_jet(u, 0, u, 0, 2)
    srph = up(2*product_jet(u, 0, u, 1, 1)
              +k1*product_jet(v, 0, v, 0, 1))
    old = c["root_drift"]
    aux = c["aux_drift"]
    p_candidates = [up(b0*ps), up(old[1]), up(aux[1])]
    p, p_choice = whole_min(p_candidates)
    d_candidates = [up(p/4), up(old[0]), up(aux[0])]
    d, d_choice = whole_min(d_candidates)
    pph_candidates = [up(b0*sph), up(old[2]), up(aux[2])]
    pph, pph_choice = whole_min(pph_candidates)
    pphph = up(b0*sphph)
    pr = up(b1*ps+b0*psr)
    dr = up(pr/4)
    prph = up(b1*sph+b0*srph)
    prr = up(b2*ps+2*b1*psr+b0*psrr)
    Dp = up(pr+d*pph)
    D2p_terms = [prr, up(2*d*prph), up((dr+d*p)*pph),
                up(d*d*pphph)]
    D2p = upper_sum(D2p_terms)
    values = dict(d=d, p=p, pphi=pph, pphiphi=pphph, dr=dr,
                  pr=pr, prphi=prph, prr=prr, Dp=Dp, D2p=D2p)
    return values, dict(complete_projected_S_Sr_Srr=[ps, psr, psrr],
        complete_Sphi_Sphiphi_Srphi=[sph, sphph, srph],
        complete_bound_candidates=dict(d=d_candidates, p=p_candidates,
                                       pphi=pph_candidates),
        selected_candidate=dict(d=d_choice, p=p_choice, pphi=pph_choice),
        complete_derivative_bounds=values, D2p_four_complete_terms=D2p_terms)


def complete_rational_quotient(s, t, r):
    """R97.17-22 and RBO.3, with distinct alpha frequency quotient."""
    u, v = t["U"], t["V"]
    beta = list(map(up, s["beta"]))
    k1, k2 = up(s["k1"]), up(s["k2"])
    z = ex("1/9409")
    gap = ex("193/9409")
    def pairing(f, ar, g, br, order):
        opts = [up(f[ar][a]*g[br][order-a]/(4**order))
                for a in range(order+1) if a <= 4 and order-a <= 4]
        opts.append(up(96**order*f[ar][0]*g[br][0]))
        return whole_min(opts)[0]
    U = [up(2/gap*upper_sum(math.comb(m,a)*pairing(u,a,u,m-a,2)
                             for a in range(m+1))) for m in range(3)]
    W = [up(2/gap*upper_sum(math.comb(m,a)*pairing(v,a,v,m-a,2)
                             for a in range(m+1))) for m in range(2)]
    alpha = []
    alpha_terms = []
    for m in range(4):
        terms = []
        for a in range(m+1):
            for b in range(m-a+1):
                c = m-a-b
                mult = math.factorial(m)//(math.factorial(a)*math.factorial(b)
                                          *math.factorial(c))
                terms.append(up(mult*beta[a]*pairing(u,b,v,c,1)/gap))
        alpha_terms.append(terms)
        alpha.append(upper_sum(terms))
    alpha_zero = up(beta[0]*pairing(u,0,v,0,1))
    alpha_frequency_one = up(beta[0]*pairing(u,0,v,0,3)/gap)
    em = s["eta_low"]
    E1, E2, E3 = s["eta"][1:4]
    reciprocal = [up(1/em), up(E1/em**2),
        up(E2/em**2+2*E1**2/em**3),
        up(E3/em**2+6*E1*E2/em**3+6*E1**3/em**4)]
    h = [upper_sum(math.comb(j,a)*alpha[a]*reciprocal[j-a]
                   for a in range(j+1)) for j in range(4)]
    q = s["qgap"]
    Qterms = [
        [up(2*beta[0]*U[0]), up(h[1]/q)],
        [up(2*beta[1]*U[0]), up(2*beta[0]*U[1]),
         up(2*beta[0]*k1*W[0]), up(h[2]/q), up(z*h[1]**2/q**2)],
        [up(2*beta[2]*U[0]), up(4*beta[1]*U[1]), up(2*beta[0]*U[2]),
         up((4*beta[1]*k1+2*beta[0]*k2)*W[0]),
         up(4*beta[0]*k1*W[1]), up(h[3]/q),
         up(3*z*h[1]*h[2]/q**2), up(2*z*z*h[1]**3/q**3)]]
    Q = list(map(upper_sum, Qterms))
    qDterms = [up(Q[1]/2), up(up(r["qrad"])*Q[0]/2),
               up(z*Q[0]**2/4)]
    qD = upper_sum(qDterms)
    l2 = s["lambda_low"]**2
    c0 = up(qD/l2)
    d10 = up(32*k1*s["eta"][0]*alpha_zero/l2)
    c1terms = [up(Q[2]/2), up(up(r["qradp"])*Q[0]/2),
        up(up(r["qrad"])*Q[1]/2), up(z*Q[0]*Q[1]/2),
        up(4*up(r["bt"])*qD),
        up(32*k1*s["eta"][0]*alpha_frequency_one),
        up(16*k1*alpha[0]**2)]
    c1 = up(upper_sum(c1terms)/l2)
    values = dict(C0=c0, C1=c1, d10=d10)
    audit = dict(primitive_gap_exact="193/9409", z_interval=["0","1/9409"],
        theta_gap_original=s["qgap"], U_radial_0_2=U, W_radial_0_1=W,
        alpha_radial_0_3=alpha, alpha_Leibniz_terms=alpha_terms,
        alpha_at_z_zero=alpha_zero, alpha_frequency_quotient=alpha_frequency_one,
        reciprocal_eta_ordinary_0_3=reciprocal, h_ordinary_0_3=h,
        Q1_ordinary_0_2=Q, Q1_complete_positive_groups=Qterms,
        qDelta_three_groups=qDterms, qDelta=qD,
        C1_seven_groups_before_lambda_inverse_square=c1terms,
        complete_rational_bounds=values,
        third_radial_derivative_only_in_C1_right_input_power="-10/3")
    return values, audit


def complete_correlated_coefficients(s, t, r, d, q):
    """Exact collected identities first, positive bounds second."""
    u, v = t["U"], t["V"]
    beta, betar = s["beta"][:2]
    b0, b1 = up(beta), up(betar)
    k1, k2, eta = up(s["k1"]), up(s["k2"]), s["eta"][0]
    p, dp, d2p = d["p"], d["Dp"], d["D2p"]
    M, e1, c2 = r["M"], r["e1"], r["c2"]
    A, C, T, Tp = r["bA"], r["bC"], r["trad"], r["tradp"]
    bt, bs, L = r["bt"], r["bs"], r["L"]
    Bm, Bmp, ac, acp, Vm = r["Bm"], r["Bmr"], r["ac"], r["acp"], r["Vm"]
    v1, v1p = ac+4*Bm, acp+4*Bmp
    P1 = (ex("13/10")*C+ex("4/175")*L*(3*A-T)-ex("21/5")*T*A
        +ex("4/15")*bs-ex("4/21")*square(bt)
        +ex("21/10")*(Vm-Tp)+v1*A+v1p)
    P2 = (-ex("523/140")*A-ex("619/140")*T+ex("26/875")*L
        -ex("4/525")*bt+ex("21/10")*v1)
    PD = ex("3/14")*A-ex("29/14")*T+ex("2/21")*bt+v1
    delta3_terms = [up(up(ex("4/15")*bs-ex("4/21")*square(bt))*p),
        up(ex("4/525")*up(bt)*p**2), up(ex("8/7875")*p**3),
        up((ex("2/21")*up(bt)+ex("4/105")*p)*dp),
        up(ex("37/18")*d2p)]
    Pv2 = projected_product(v,0,v,0)
    ZD = up(2*b0*k1*Pv2)
    ZDD_terms = [up(up(4*betar*s["k1"]+2*beta*s["k2"])*Pv2),
        up(4*b0*k1*(2*projected_product(v,0,v,1)
                     +2*d["d"]*v[0][0]*v[0][1]))]
    ZDD = upper_sum(ZDD_terms)
    ell = up(2*b0*u[0][0]*v[0][0])
    WAC_terms = [up(ell**2), up(4*b0*eta*v[0][0]*u[0][1])]
    WAC = upper_sum(WAC_terms)
    RDterms = [up(up(P1)*p), up(up(P2)*p**2),
        up(ex("55127/12600")*p**3), up(up(PD)*dp),
        up(ex("157/84")*p*dp), up(ex("19/18")*d2p),
        up((up(A+Bm-ac)+ex("9/10")*p)*ZD), ZDD, up(k1*WAC)]
    DeltaRD = upper_sum(RDterms)
    ECO = -ex("81/70")*e1+ex("6/35")*c2+3*beta+3*M
    Eterms = [up(up(ECO)*p), up(ex("291/140")*p*p),
              up(ex("15/14")*dp), ZD]
    E = up(upper_sum(Eterms)/s["lambda_low"]**2)
    KH = -beta-M/3-ex("7/15")*e1-ex("2/5")*c2
    Hterms = [up((up(KH)+ex("2/15")*p)*E),
        up(ex("37/30")*p*s["Vroot"]),
        up(DeltaRD/(3*s["lambda_low"]**2)), up(q["d10"]/3)]
    H = upper_sum(Hterms)
    astar_scalar = e1/10-c2/5-beta-M
    astar = up(up(astar_scalar)+ex("11/10")*p)
    # At the true root, bop=beta-M+p=beta*(1-u^2), with the full mean retained.
    bop_candidates = [up(up(Bm)+p), up(b0*(1+u[0][0]**2))]
    bop, bop_choice = whole_min(bop_candidates)
    ellr = up(2*b1*u[0][0]*v[0][0]
               +2*b0*(u[1][0]*v[0][0]+u[0][0]*v[1][0]))
    ellphi = up(2*b0*(u[0][1]*v[0][0]+u[0][0]*v[0][1]))
    eta_low = s["eta_low"]
    Dl_eta_terms = [up(ellr/eta_low),
        up(ell*s["eta"][1]/eta_low**2), up(d["d"]*ellphi/eta_low)]
    Dl_eta = upper_sum(Dl_eta_terms)
    A1terms = [up(ex("6/5")*d["pphi"]), up(Dl_eta/2),
               up(ell*p/(2*eta_low))]
    A1 = upper_sum(A1terms)
    values = dict(E=E, H=H, A=astar, A1=A1, b=bop, V=s["Vroot"],
                  C0=q["C0"], C1=q["C1"], d10=q["d10"])
    audit = dict(radial_signed_collected_coefficients=dict(P1=P1,P2=P2,PD=PD,
        E0_coefficient=ECO, KH=KH, astar_scalar=astar_scalar),
        delta3_five_complete_terms=delta3_terms,
        delta3=upper_sum(delta3_terms), ZD=ZD, ZDD=ZDD,
        ZDD_two_complete_terms=ZDD_terms, WAC_two_complete_terms=WAC_terms,
        DeltaRD_nine_complete_terms=RDterms, DeltaRD=DeltaRD,
        E0_four_terms_before_lambda_inverse_square=Eterms,
        H0_four_complete_terms=Hterms, bop_complete_candidates=bop_candidates,
        bop_selected_candidate=bop_choice, ell=ell, ell_r=ellr, ell_phi=ellphi,
        D_ell_over_eta_three_terms=Dl_eta_terms,
        signed_first_amplitude_three_terms=A1terms, complete_bounds=values,
        two_frequency_signs_share_one_multiplier=True,
        nonzero_constant_d10_kept_without_z=True)
    return values, audit


def complete_profile_and_error(s, f):
    """Every RBO.11-13 term, including the positive mean-rank and I/4."""
    shear = s["shear"]
    if not (1-2*shear > 0):
        raise ArithmeticError("missing original terminal-Ai shear gap")
    Astar = up((1+2*shear)*ex("5/9"))
    Dstar = up((1+2*shear)/3)
    g = ((1-2*shear)*(ex("1/3")
        +4*s["lambda_low"]/(21*s["eta"][0]))).lower()
    if not g.is_finite() or not g > 0:
        raise ArithmeticError("nonpositive genuine diagonal lower")
    powers = {}
    for exponent in ("-1/3","-2/3","-1","-4/3","-2","-10/3","-4","-6"):
        powers[exponent] = up((ex(388).log()*ex(exponent)).exp())
    E,H,A,A1,b,V,C0,C1 = [f[k] for k in ("E","H","A","A1","b","V","C0","C1")]
    n = powers
    amp_terms = [up(Dstar*E*n["-4/3"]), up(16*Dstar*C0*n["-10/3"])]
    eamp = upper_sum(amp_terms)
    rterms = [up(A*Astar), up(A1*Astar*n["-1"]),
        up(H*Dstar*n["-4/3"]),
        up(16*(A*C0+C1/3)*Dstar*n["-10/3"]),
        up(s["lambda_up"]*V*E*Astar*n["-2"]),
        up(16*s["lambda_up"]*(E+V)*C0*Astar*n["-4"]),
        up(256*s["lambda_up"]*C0*C0*Astar*n["-6"]),
        up(b*E*Dstar*n["-4/3"])]
    r0 = upper_sum(rterms)
    IR0 = up(r0/4)
    leading_I = up(s["lambda_up"]*Dstar*n["-1/3"])
    JL = up(s["J1"]*s["L0"])
    inverse_terms = [r0, up(JL*(leading_I+IR0))]
    inverse_error = up(n["-2/3"]/s["eta_low"]*upper_sum(inverse_terms))
    e = up(eamp+inverse_error)
    # Decide on the exact balls that the final receipt will actually retain.
    retained_e = ball(e.str(75))
    retained_g = ball(g.str(75))
    margin = retained_g.lower()-retained_e.upper()
    strict = bool(retained_e.upper() < retained_g.lower())
    result = dict(cutoff_abs_j=97, physical_minimum_frequency=388,
        original_shear_uniform_upper=shear, Ai_A_upper=Astar,
        Ai_D_upper=Dstar, genuine_diagonal_lower=g,
        right_input_powers=powers, amplitude_two_terms=amp_terms,
        complete_unprojected_amplitude_upper=eamp, E2_upper=eamp,
        R0_eight_complete_terms=rterms, R0_upper=r0,
        complete_positive_mean_rank=rterms[-1],
        complete_IR0_upper=IR0, high_leading_primitive_upper=leading_I,
        same_original_J1_L0_product=JL, inverse_error_two_groups=inverse_terms,
        complete_inverse_error_upper=inverse_error,
        complete_stable_error_upper=e, strict_margin=margin,
        strict_comparison_uses_retained_75_digit_ball_endpoints=True,
        original_cutoff97_sufficient_gate_passed=strict,
        root_stable_injectivity_certified=strict,
        same_window_onto_only_with_original_SE_identity=strict,
        negative_window_numerical_inverse_claimed=False,
        complete_incoming_inverse_claimed=False, finite_Schur_inverse_claimed=False,
        physical_independent_means_retained=True, full_IR0_norm_is_not_high_cut=True)
    return result


def require(condition, message):
    if not condition:
        raise ValueError(message)


def literal_original_constants(text):
    # Parsing is read only. No compile, eval, exec, import or old producer call.
    wanted = {"PIN_SPECS", "HISTORICAL_INPUTS", "PARAMETERS", "RETAINED_SCOPE",
              "COUNTS", "COMPLETE_FIELDS", "RUNTIME", "GATE_COUNT"}
    tree = ast.parse(text, filename=PIN_SPECS["original_source"]["path"])
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in wanted:
                    require(target.id not in result, "duplicate original literal")
                    result[target.id] = ast.literal_eval(node.value)
    require(set(result) == wanted, "missing exact original literal")
    gate_calls = sorted((node for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        and node.func.id == "gate"), key=lambda node: node.lineno)
    result["gate_names"] = [
        ast.literal_eval(node.args[1]) for node in gate_calls]
    return result


def restore_saved_working_inputs(prefix):
    # Keep the five original JSON objects verbatim; these are new working values.
    saved_mixed = prefix["complete_mixed_norm_conclusion"]
    saved_domain = prefix["complete_root_domain_conclusion"]
    require(set(saved_mixed["selected"]) == {"U", "V"}, "saved mixed labels")
    for family in ("U", "V"):
        require(len(saved_mixed["selected"][family]) == 4
            and all(len(row) == 5 for row in saved_mixed["selected"][family]),
            "saved mixed 4 by 5 shape")
        require(len(saved_mixed["selected_original_source"][family]) == 4
            and all(len(row) == 5
                for row in saved_mixed["selected_original_source"][family]),
            "saved mixed source-label shape")
    require(saved_mixed["radial_orders"] == [0, 1, 2, 3]
        and saved_mixed["physical_angular_orders"] == [0, 1, 2, 3, 4],
        "saved complete mixed derivative units")
    mixed = {family: [[up(value) for value in row]
                     for row in saved_mixed["selected"][family]]
             for family in ("U", "V")}
    expected = {"J0", "J1", "K", "L0", "Vroot", "beta", "eta", "eta_low",
                "k1", "k2", "k3", "lambda_low", "lambda_up", "qgap", "shear"}
    require(set(saved_domain) == expected, "saved complete domain schema")
    require(all(len(saved_domain[key]) == 4 for key in ("beta", "K", "eta")),
            "saved ordinary radial array shape")
    domain = {key: lower(saved_domain[key])
              for key in ("eta_low", "lambda_low", "qgap")}
    domain.update({key: up(saved_domain[key])
                   for key in ("lambda_up", "Vroot", "shear", "J0", "J1", "L0")})
    domain["eta"] = [up(value) for value in saved_domain["eta"]]
    domain.update({key: [ball(value) for value in saved_domain[key]]
                   for key in ("beta", "K")})
    domain.update({key: ball(saved_domain[key]) for key in ("k1", "k2", "k3")})
    require(finite_tree(mixed) and finite_tree(domain)
        and domain["k1"].lower() > 0 and domain["K"][1].lower() > 0,
        "saved typed root inputs must remain finite with positive denominator")
    require(all(saved_domain["k" + str(i)] == saved_domain["K"][i]
                for i in (1, 2, 3)), "saved duplicated signed K jets differ")
    return mixed, domain


def checked_saved_prefix(args, doc):
    mraw = args.manifest.read_bytes()
    manifest = json.loads(mraw)
    runtime = {"Python": platform.python_version(),
               "python_flint": importlib.metadata.version("python-flint")}
    doc["runtime"] = runtime
    checkout = doc["actual_scientific_checkout_commit"]
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == PUBLIC
        and runtime == RUNTIME and ctx.prec == args.bits == 320
        and isinstance(checkout, str) and len(checkout) == 40
        and all(ch in "0123456789abcdef" for ch in checkout)
        and sha(mraw) == args.manifest_sha,
        "actual public recovery runtime, checkout and manifest identity")
    require(manifest.get("kind") == MANIFEST_KIND
        and manifest.get("public_repository") == PUBLIC
        and manifest.get("source_path") == SOURCE
        and manifest.get("source_sha256") == doc["source_sha256"]
        and manifest.get("scientific_runtime") == RUNTIME
        and manifest.get("parameters") == PARAMETERS
        and manifest.get("scope") == RETAINED_SCOPE
        and manifest.get("publication_limits") == PUBLICATION_LIMITS,
        "complete recovery manifest definition")
    files = manifest["files"]
    fmap = {entry["role"]: entry for entry in files}
    roles = set(PINNED) | {"source", "worker", "rules"}
    require(len(files) == len(fmap) == 9 and set(fmap) == roles
        and manifest.get("historical_inputs") == []
        and manifest.get("legacy_artifact_inputs") == []
        and manifest.get("all_inputs_are_current_small_texts") is True
        and manifest.get("mathematical_input_sha256") == PINNED
        and manifest.get("expected_current_input_count") == 9
        and manifest.get("expected_input_count") == 9
        and manifest.get("expected_immutable_AST_files") == 3
        and manifest.get("expected_actual_gate_count") == GATE_COUNT
        and manifest.get("current_input_paths") == [entry["path"] for entry in files]
        and manifest.get("file_sha256") == {
            entry["path"]: entry["sha256"] for entry in files}
        and manifest.get("input_paths") == {
            entry["role"]: entry["path"] for entry in files}
        and manifest.get("old_successful_scientific_calls_allowed") is False
        and manifest.get("new_native_arrays_or_artifact_persistence_allowed") is False
        and sum(entry["path"].endswith(".py") for entry in files) == 3
        and manifest.get("complete_input_bytes") == sum(entry["bytes"] for entry in files)
        and fmap["source"]["path"] == SOURCE and fmap["rules"] == RULES,
        "exact nine-current three-AST zero-history recovery closure")
    for role, spec in PIN_SPECS.items():
        require(all(fmap[role].get(key) == spec[key]
                    for key in ("path", "git_blob", "bytes", "sha256")),
                "recovery mathematical file tuple: " + role)
    paths, raw, identities = {}, {}, {}
    root = args.repo.resolve()
    for entry in files:
        path = (args.repo / entry["path"]).resolve()
        require(path.is_relative_to(root), "current path outside recovery checkout")
        data = path.read_bytes()
        require(len(data) == entry["bytes"] and sha(data) == entry["sha256"]
            and 0 < len(data) <= 100000,
            "changed current recovery input: " + entry["role"])
        paths[entry["role"]] = path
        if entry["role"] in PINNED:
            raw[entry["role"]] = data
            identities[entry["role"]] = {"bytes": len(data), "sha256": sha(data)}
    require(paths["source"] == Path(__file__).resolve(),
            "actual recovery source must be the verified checkout file")
    old = literal_original_constants(raw["original_source"].decode("utf-8"))
    old_manifest = json.loads(raw["original_manifest"])
    prefix = json.loads(raw["saved_prefix"])
    execution = json.loads(raw["saved_execution"])
    old_specs = old["PIN_SPECS"]
    old_pins = {key: entry["sha256"] for key, entry in old_specs.items()}
    old_gates = PRESERVED_PREFIX_EVIDENCE["original_passed_gates"]
    require(len(old_specs) == 15 and old["GATE_COUNT"] == 22
        and old_pins == PRESERVED_PREFIX_EVIDENCE["original_mathematical_input_sha256"]
        and old["PARAMETERS"] == {**PARAMETERS, "expected_actual_gate_count": 22,
            "expected_current_inputs": 16, "expected_total_inputs": 18,
            "expected_Python_AST_files": 2, "expected_historical_gzip_inputs": 2}
        and old["RETAINED_SCOPE"] == RETAINED_SCOPE
        and old["COUNTS"] == PRESERVED_PREFIX_EVIDENCE["retained_original_plan"]
        and old["RUNTIME"] == RUNTIME
        and len(old["COMPLETE_FIELDS"]) == 33
        and len(old["gate_names"]) == 22
        and old["gate_names"][:14] == [entry["name"] for entry in old_gates],
        "original source literals and exact original gate order")
    operational = {"expected_actual_gate_count", "expected_current_inputs",
        "expected_total_inputs", "expected_Python_AST_files",
        "expected_historical_gzip_inputs"}
    require({k: v for k, v in old["PARAMETERS"].items() if k not in operational}
        == {k: v for k, v in PARAMETERS.items() if k not in operational},
        "all mathematical parameters are unchanged")
    old_files = old_manifest["files"]
    old_fmap = {entry["role"]: entry for entry in old_files}
    histories = old["HISTORICAL_INPUTS"]
    history_roles = {entry["role"] for entry in histories}
    current_old_roles = set(old_pins) - history_roles
    require(old_manifest.get("kind") == ORIGINAL["manifest_kind"]
        and old_manifest.get("public_repository") == PUBLIC
        and old_manifest.get("source_path") == ORIGINAL["source_path"]
        and old_manifest.get("source_sha256") == ORIGINAL["source_sha256"]
        and old_manifest.get("parameters") == old["PARAMETERS"]
        and old_manifest.get("scope") == old["RETAINED_SCOPE"]
        and old_manifest.get("scientific_runtime") == RUNTIME
        and old_manifest.get("mathematical_input_sha256") == old_pins
        and len(old_files) == len(old_fmap) == 16
        and set(old_fmap) == current_old_roles | {"source", "worker", "rules"}
        and len(histories) == 2
        and [entry["role"] for entry in histories] == ["majorants_native", "root_native"]
        and old_manifest.get("historical_inputs") == histories
        and old_manifest.get("expected_current_input_count") == 16
        and old_manifest.get("expected_input_count") == 18
        and old_manifest.get("expected_immutable_AST_files") == 2
        and old_manifest.get("expected_actual_gate_count") == 22
        and old_manifest.get("complete_input_bytes") == ORIGINAL["complete_input_bytes"]
        and old_manifest.get("file_sha256") == {
            entry["path"]: entry["sha256"] for entry in old_files}
        and old_manifest.get("current_input_paths") == [
            entry["path"] for entry in old_files]
        and old_manifest.get("input_paths") == {
            **{entry["role"]: entry["path"] for entry in old_files},
            **{entry["role"]: entry["path"] for entry in histories}},
        "frozen original eighteen-file manifest closure")
    for role in current_old_roles:
        require(all(old_fmap[role].get(key) == old_specs[role][key]
                    for key in ("path", "git_blob", "bytes", "sha256")),
                "original current mathematical tuple: " + role)
    for entry in histories:
        spec = old_specs[entry["role"]]
        require(entry["path"] == spec["path"]
            and entry["git_blob_sha"] == spec["git_blob"]
            and entry["bytes"] == spec["bytes"]
            and entry["sha256"] == spec["sha256"],
            "original historical mathematical tuple")
    require(old_fmap["source"]["path"] == PIN_SPECS["original_source"]["path"]
        and old_fmap["source"]["sha256"] == PINNED["original_source"]
        and old_fmap["source"]["git_blob"] == PIN_SPECS["original_source"]["git_blob"]
        and old_fmap["source"]["bytes"] == PIN_SPECS["original_source"]["bytes"]
        and old_fmap["worker"]["sha256"] == ORIGINAL["worker_sha256"],
        "original scientific and wrapper identity")
    reconstructed_receipts = [
        {"role": entry["role"], "path": entry["path"], "bytes": entry["bytes"],
         "sha256": entry["sha256"], "origin": "exact_current_small_text"}
        for entry in old_files]
    reconstructed_receipts.extend({
        **entry, "origin": "exact_immutable_public_Git_history_temporary_restore",
        "Git_blob_identity_verified": True, "Git_tree_identity_verified": True,
        "old_scientific_producer_executed": False, "original_bytes_unmodified": True}
        for entry in histories)
    require(execution.get("kind") == ORIGINAL["execution_kind"]
        and execution.get("repository") == PUBLIC
        and execution.get("run_id") == ORIGINAL["run_id"]
        and execution.get("run_attempt") == ORIGINAL["run_attempt"]
        and execution.get("workflow_commit") == ORIGINAL["workflow_event_commit"]
        and execution.get("actual_scientific_checkout_commit")
            == ORIGINAL["actual_scientific_checkout_commit"]
        and execution.get("source_sha256") == ORIGINAL["source_sha256"]
        and execution.get("input_manifest_sha256") == ORIGINAL["manifest_sha256"]
        and execution.get("worker_source_sha256") == ORIGINAL["worker_sha256"]
        and execution.get("actual_scientific_runtime") == RUNTIME
        and execution.get("actual_returncode") == 1
        and execution.get("complete") is False
        and execution.get("actual_new_scientific_processes") == 1
        and execution.get("mathematical_input_sha256") == old_pins
        and execution.get("actual_verified_Git_input_count") == 18
        and execution.get("actual_original_Git_input_receipts") == reconstructed_receipts
        and sha(canonical(reconstructed_receipts))
            == execution.get("actual_verified_Git_input_receipts_sha256")
            == PRESERVED_PREFIX_EVIDENCE["inherited_original_input_validation"][
                "original_receipts_canonical_sha256"]
        and execution.get("complete_immutable_Python_AST_closure_passed") is True
        and execution.get("complete_immutable_Python_AST_file_count") == 2
        and execution.get("complete_immutable_Python_AST_inventory_sha256")
            == PRESERVED_PREFIX_EVIDENCE["inherited_original_AST_validation"][
                "original_inventory_sha256"],
        "original execution and inherited eighteen-receipt chain")
    summary = execution["scientific_conclusion"]
    require(summary == {
        "actual_gate_count": 14, "actual_passed_gate_count": 14,
        "actual_returncode": 1, "bytes": PIN_SPECS["saved_prefix"]["bytes"],
        "complete": False, "file": "actual-scientific-conclusion.json",
        "original_result_printed_before_any_format_gate": True,
        "sha256": PINNED["saved_prefix"]},
        "original execution must name the exact complete saved partial file")
    require(set(prefix) == set(ORIGINAL["prefix_fields"])
        and prefix.get("kind") == ORIGINAL["kind"]
        and prefix.get("source_sha256") == PINNED["original_source"]
        and prefix.get("input_manifest_sha256") == PINNED["original_manifest"]
        and prefix.get("input_sha256") == {
            "manifest": PINNED["original_manifest"], **old_pins}
        and prefix.get("verified_original_inputs") == {
            key: {"bytes": entry["bytes"], "sha256": entry["sha256"]}
            for key, entry in old_specs.items()}
        and prefix.get("run_id") == ORIGINAL["run_id"]
        and prefix.get("run_attempt") == ORIGINAL["run_attempt"]
        and prefix.get("workflow_event_commit") == ORIGINAL["workflow_event_commit"]
        and prefix.get("actual_scientific_checkout_commit")
            == ORIGINAL["actual_scientific_checkout_commit"]
        and prefix.get("public_repository") == PUBLIC
        and prefix.get("runtime") == RUNTIME and prefix.get("arithmetic_bits") == 320
        and prefix.get("complete") is False and prefix.get("proved") is False
        and prefix.get("actual_returncode") == 1
        and prefix.get("failure") == ORIGINAL["failure"]
        and prefix.get("stage") == ORIGINAL["stage"]
        and prefix.get("parameters") == old["PARAMETERS"]
        and prefix.get("retained_scope") == old["RETAINED_SCOPE"]
        and prefix.get("counts") == old["COUNTS"]
        and prefix.get("gates") == old_gates
        and passed_gates(prefix, "gates", 14),
        "exact failed prefix, fourteen preserved gates and absent suffix")
    for key, expected in PRESERVED_OBJECT_HASHES.items():
        require(sha(canonical(prefix[key])) == expected,
                "changed original preserved object: " + key)
    require(sha(canonical(prefix["copied_old_inputs"]))
        == prefix["copied_old_inputs_sha256"],
        "exact complete copied-original canonical identity")
    mixed, domain = restore_saved_working_inputs(prefix)
    doc["input_sha256"] = {"manifest": sha(mraw), **PINNED}
    doc["verified_original_inputs"] = identities
    for key in PRESERVED_OBJECT_HASHES:
        doc[key] = copy.deepcopy(prefix[key])
    doc["preserved_prefix_evidence"] = copy.deepcopy(PRESERVED_PREFIX_EVIDENCE)
    doc["actual_progress"].update(saved_prefix_validation_passed=True,
        preserved_gate_count=14, saved_complete_math_conclusions_reused=2)
    gate(doc, GATE_NAMES[0], len(identities) == 6
        and len(paths) == 9 and finite_tree(mixed) and finite_tree(domain))
    return manifest, paths, doc["copied_old_inputs"], mixed, domain


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every exact root97 recovery result")
    ctx.prec = args.bits
    started = time.monotonic()
    attempted_stage = "identity"
    doc = dict(kind=KIND, complete=False, proved=False, actual_returncode=None,
        failure=None, stage="identity",
        source_sha256=sha(Path(__file__).read_bytes()),
        input_manifest_sha256=sha(args.manifest.read_bytes()),
        public_repository=PUBLIC, run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        runtime={}, arithmetic_bits=args.bits, parameters=copy.deepcopy(PARAMETERS),
        retained_scope=copy.deepcopy(RETAINED_SCOPE), counts=copy.deepcopy(COUNTS),
        actual_progress=copy.deepcopy(INITIAL_ACTUAL_PROGRESS), gates=[])
    try:
        manifest, paths, copied, mixed, domain = checked_saved_prefix(args, doc)
        doc["stage"] = "complete_saved_prefix_read"
        persist(args.out, doc)

        attempted_stage = "complete_new_radial_intervals"
        radial = real_radial_intervals(domain, mixed)
        encode_new_stage(doc, "complete_real_radial_interval_conclusion",
                         attempted_stage, radial)
        gate(doc, "complete real moments and neighborhood radial derivatives retain all mean terms",
            finite_tree(radial) and all(k in radial for k in
                ("Mr","Bmr","Emr","acp","qradp","tradp","bA","bC")))
        doc["actual_progress"]["new_radial_conclusion_completed"] = 1
        doc["stage"] = attempted_stage
        persist(args.out, doc)

        attempted_stage = "complete_new_root_drift"
        drift, drift_audit = complete_root_drift(domain, mixed, copied)
        encode_new_stage(doc, "complete_root_drift_conclusion",
                         attempted_stage, drift_audit)
        gate(doc, "complete mixed drift derivatives and every D squared p term are finite",
            finite_tree(drift_audit) and len(drift) == 10
            and len(drift_audit["D2p_four_complete_terms"]) == 4)
        doc["actual_progress"]["new_drift_conclusion_completed"] = 1
        doc["stage"] = attempted_stage
        persist(args.out, doc)

        attempted_stage = "complete_new_rational_quotient"
        quotient, quotient_audit = complete_rational_quotient(domain, mixed, radial)
        encode_new_stage(doc, "complete_rational_quotient_conclusion",
                         attempted_stage, quotient_audit)
        gate(doc, "complete rational quotient retains both gaps and all third ordinary derivatives",
            finite_tree(quotient_audit)
            and len(quotient_audit["reciprocal_eta_ordinary_0_3"]) == 4
            and len(quotient_audit["h_ordinary_0_3"]) == 4
            and len(quotient_audit["Q1_ordinary_0_2"]) == 3
            and list(map(len,quotient_audit["Q1_complete_positive_groups"])) == [2,5,8]
            and len(quotient_audit["C1_seven_groups_before_lambda_inverse_square"]) == 7)
        doc["actual_progress"]["new_quotient_conclusion_completed"] = 1
        doc["stage"] = attempted_stage
        persist(args.out, doc)

        attempted_stage = "complete_new_correlated_coefficients"
        coefficients, coefficient_audit = complete_correlated_coefficients(
            domain, mixed, radial, drift, quotient)
        encode_new_stage(doc, "complete_correlated_coefficient_conclusion",
                         attempted_stage, coefficient_audit)
        gate(doc, "complete collected correlations preserve all nine derivative groups and the true mean",
            finite_tree(coefficient_audit)
            and len(coefficient_audit["delta3_five_complete_terms"]) == 5
            and len(coefficient_audit["DeltaRD_nine_complete_terms"]) == 9
            and len(coefficient_audit["E0_four_terms_before_lambda_inverse_square"]) == 4
            and len(coefficient_audit["H0_four_complete_terms"]) == 4)
        doc["actual_progress"]["new_correlated_conclusion_completed"] = 1
        doc["stage"] = attempted_stage
        persist(args.out, doc)

        attempted_stage = "complete_new_cutoff97_comparison"
        result = complete_profile_and_error(domain, coefficients)
        # Actual invocation completed, even if a later serialization or gate fails.
        doc["actual_progress"]["completed_original_cutoff97_comparisons"] = 1
        encode_new_stage(doc, "complete_ordered_operator_conclusion",
                         attempted_stage, result)
        doc["original_cutoff97_sufficient_gate_passed"] = result["original_cutoff97_sufficient_gate_passed"]
        gate(doc, "all ordered operator terms and genuine positive diagonal bounds are complete",
            finite_tree(result) and result["genuine_diagonal_lower"] > 0
            and result["complete_stable_error_upper"] >= 0
            and len(result["amplitude_two_terms"]) == 2
            and len(result["R0_eight_complete_terms"]) == 8
            and result["complete_positive_mean_rank"] == result["R0_eight_complete_terms"][-1])
        doc["stage"] = attempted_stage
        persist(args.out, doc)
        gate(doc, "the optional strict comparison has its exact narrow ordinary L2 scope",
            type(doc["original_cutoff97_sufficient_gate_passed"]) is bool
            and result["original_cutoff97_sufficient_gate_passed"] == bool(
                ball(doc["complete_ordered_operator_conclusion"]["complete_stable_error_upper"]).upper()
                < ball(doc["complete_ordered_operator_conclusion"]["genuine_diagonal_lower"]).lower())
            and result["cutoff_abs_j"] == 97 and result["physical_minimum_frequency"] == 388
            and result["negative_window_numerical_inverse_claimed"] is False
            and result["complete_incoming_inverse_claimed"] is False
            and result["finite_Schur_inverse_claimed"] is False
            and result["physical_independent_means_retained"] is True)
        attempted_stage = "complete_suffix_final_identity"
        gate(doc, "all original input bytes remain unchanged with zero old target calls",
            sha(args.manifest.read_bytes()) == doc["input_manifest_sha256"]
            and all(sha(paths[entry["role"]].read_bytes()) == entry["sha256"]
                and len(paths[entry["role"]].read_bytes()) == entry["bytes"]
                for entry in manifest["files"])
            and all(sha(canonical(doc[key])) == expected
                for key, expected in PRESERVED_OBJECT_HASHES.items())
            and doc["preserved_prefix_evidence"] == PRESERVED_PREFIX_EVIDENCE
            and doc["actual_progress"]["old_successful_targets_recomputed"] == 0
            and doc["actual_progress"]["saved_mixed_selections_recomputed"] == 0
            and doc["actual_progress"]["saved_root_domain_recomputed"] == 0
            and doc["actual_progress"]["historical_gzip_restores"] == 0
            and doc["counts"]["old_scientific_modules_imported"] == 0)
        doc["actual_mathematical_wall_seconds"] = time.monotonic()-started
        gate(doc, "complete scalar schema retains every conclusion whether the sufficient test passes or fails",
            len(doc["gates"]) == GATE_COUNT-1 and set(doc) == set(COMPLETE_FIELDS)
            and doc["parameters"] == PARAMETERS and doc["retained_scope"] == RETAINED_SCOPE
            and doc["counts"] == COUNTS
            and doc["actual_progress"] == SUCCESS_ACTUAL_PROGRESS)
        doc.update(complete=True, proved=True, actual_returncode=0, failure=None, stage="complete")
    except Exception as exc:
        if "failed_new_stage_diagnostic" not in doc:
            stage_fields = {
                "complete_new_radial_intervals": "complete_real_radial_interval_conclusion",
                "complete_new_root_drift": "complete_root_drift_conclusion",
                "complete_new_rational_quotient": "complete_rational_quotient_conclusion",
                "complete_new_correlated_coefficients": "complete_correlated_coefficient_conclusion",
                "complete_new_cutoff97_comparison": "complete_ordered_operator_conclusion"}
            attempted_field = stage_fields.get(attempted_stage)
            graph_available = attempted_field in doc if attempted_field else False
            doc["failed_new_stage_diagnostic"] = {
                "attempted_stage": attempted_stage,
                "returned_complete_graph_available": graph_available,
                "returned_graph_field_if_already_saved": attempted_field if graph_available else None,
                "exception_before_a_new_complete_graph_was_encoded": not graph_available,
                "last_preserved_stage": doc.get("stage"),
                "nonfinite_labels_are_not_certified_balls": True,
                "original_prefix_objects_modified": False}
        doc["failure"] = {"type":type(exc).__name__, "message":str(exc)}
        doc["actual_returncode"] = 1
        doc["actual_mathematical_wall_seconds"] = time.monotonic()-started
        persist(args.out, doc)
        print_complete_document(doc)
        traceback.print_exc()
        raise
    raw = persist(args.out, doc)
    print_complete_document(doc)
    # Complete science remains saved and printed before any publication guard.
    if len(raw) > COMPLETE_SCIENCE_MAX_BYTES:
        raise RuntimeError("complete recovery science preserved before publication-size guard")


if __name__ == "__main__":
    main()
