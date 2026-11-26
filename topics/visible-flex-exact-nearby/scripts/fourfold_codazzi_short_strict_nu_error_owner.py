"""SB: only the missing short radial cost and eleven complete scalar consequences.

Read the whole completed NP/SP outcomes and all forty original body parts.
No old intrinsic, residual, nonradial matrix, trial or pairing target runs.
"""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, os, platform
from pathlib import Path
import sys, time, traceback

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_short_strict_nu_error_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_short_strict_nu_error_math.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_short_strict_nu_error_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_short_strict_nu_error_manifest.py"
PROOF = TOPIC+"/results/R147-supplement-short-interval-parameter-error-and-nonlocal-receiver.md"
TEMPLATE = TOPIC+"/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py"
NP_MANIFEST = TOPIC+"/notes/2026-11-27-strict-nu-particular-inputs.json"
NP_BASE = TOPIC+"/notes/strict_nu_particular_ci/run-45893562391-1"
SP_EXECUTION = TOPIC+"/notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json"
SP_SHA = "a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12"
STC_PROOF = TOPIC+"/results/R144-supplement-actual-full-frequency-strict-propagation-for-compact-centres.md"
NR_PROOF = TOPIC+"/results/R144-supplement-actual-negative-and-root-propagation-in-a-full-tail-neighbourhood.md"
KIND = "R147_complete_short_strict_nu_error_v1"
STAGE = "complete_short_strict_nu_error"
MANIFEST_KIND = "R147_complete_short_strict_nu_error_inputs_v1"
RUNTIME = {"python":"3.12.14","packages":{"python-flint":"0.9.0"}}
PARAMETERS = {
    "arithmetic_bits":320,"decimal_record_digits":60,"maximum_scientific_wall_seconds":1800,
    "new_radial_interval":["0","9/50"],"complete_original_rows":7721,"complete_original_parts":40,
    "complete_original_nonradial_matrix_upper":"433/200","independent_physical_means":2,
    "source_measure":"ordinary_dr_normalized_angular_measure","physical_frequency_factor":4,
    "same_original_selected_member_run":"43588332723/1","fixed_intrinsic_parameter":"eta_0",
    "selected_to_budget_ratio_upper":"936826/1000000","new_complete_scalar_records":11,
    "original_centre_residual_degree":160,"only_original_residual_Hminus1_to_L2_factor":"641",
    "complete_original_strong_nonradial_matrix_upper":"437/200",
    "all_unknown_Fourier_modes_retained":True,"old_scientific_targets_recomputed":False,
}
TARGETS = [
    "complete_base_short_reverse_radial_cost_upper",
    "complete_selected_short_reverse_radial_cost_upper",
    "complete_NP_selected_ordinary_error_source_upper",
    "complete_short_Hminus1_source_to_waist_density_upper",
    "complete_short_Hminus1_source_to_uniform_primitive_mean_upper",
    "complete_true_NP_short_waist_density_error_upper",
    "complete_true_NP_uniform_primitive_mean_error_upper",
    "complete_NP_selected_L1_L2_error_source_upper",
    "complete_short_L2_source_to_uniform_L2_upper",
    "complete_true_NP_uniform_L2_error_upper",
    "complete_true_NP_L2r_L2_error_upper",
]
SCI_FIELDS = sorted([
    "identity","parameters","runtime","complete","proved","actual_returncode","failure","stage",
    "completed_targets","current_target","candidate_record","new_records","saved_record_count",
    "whole_completed_inputs","reference_identity","selected_member_identity","copied_prior_scalar_records",
    "short_radial_receipts","result","old_scientific_target_calls","new_arrays_published",
    "new_artifacts","new_Releases","wall_seconds",
])


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw,
        parse_constant=lambda value:(_ for _ in ()).throw(ValueError(value)))


def load(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def atomic(path,raw):
    path = Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    candidate = path.with_name(path.name+".candidate")
    with candidate.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.replace(candidate,path)


def gather(root):
    root = Path(root);files,roles = {},{}
    def add(role,path,expected=None):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,"safe complete topic input")
        raw = (root/path).read_bytes();raw.decode()
        require(0 < len(raw) < 100000,"whole small original outcome, definition or new source")
        if path.endswith(".py"):ast.parse(raw.decode(),filename=path)
        item = {"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if expected is not None:
            require(all(item[key] == expected[key] for key in ("path","bytes","sha256","git_blob_sha")),
                "unchanged whole accepted input: "+role)
        require(path not in files,"one physical complete current input")
        files[path] = item;roles[role] = path
        return parse(raw) if path.endswith(".json") else raw
    npm = add("NP_manifest",NP_MANIFEST);original = {x["role"]:x for x in npm["files"]}
    for role,prior in (("reviewed_rules","reviewed_rules"),("NP_source","science"),
        ("D_execution","SL_D_execution"),("old_body_manifest","old_body_manifest"),
        ("row_inputs","inputs_math"),("SP_proof","SL_proof_SP"),("NP_math","nu_math"),("NP_proof","proof")):
        item = original[prior];add(role,item["path"],item)
    for role,path in (("NP_actual",NP_BASE+"/actual-strict-nu-particular.json"),
        ("NP_execution",NP_BASE+"/execution.json"),("SP_execution",SP_EXECUTION),
        ("STC_proof",STC_PROOF),("NR_proof",NR_PROOF),("science",SOURCE),("short_math",MATH),("worker",WORKER),
        ("generator",GENERATOR),("proof",PROOF),("worker_template",TEMPLATE)):
        add(role,path)
    history = [dict(item) for item in npm["historical_inputs"] if item["role"].startswith("original_rows_")]
    require(len(history) == 40,"only all forty necessary original body parts")
    for item in history:roles[item["role"]] = item["path"]
    return {"files":sorted(files.values(),key=lambda x:x["role"]),"historical_inputs":history,"roles":roles}


def admit(manifest,raws,paths):
    """Whole old scientific outcomes; no numerical imports or repeated targets."""
    roles = manifest["roles"]
    def raw(role):return raws[roles[role]]
    npm = parse(raw("NP_manifest"));np_owner = load(paths[roles["NP_source"]],"_SB_old_NP_definitions")
    specs = {x["role"]:x for x in npm["files"]}
    actual,execution = parse(raw("NP_actual")),parse(raw("NP_execution"))
    require(actual["complete"] is actual["proved"] is execution["complete"] is True
        and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
        and actual["failure"] is execution["failure"] is None
        and actual["identity"]["kind"] == np_owner.KIND
        and actual["identity"]["source_sha256"] == specs["science"]["sha256"] == sha(raw("NP_source"))
        and actual["identity"]["manifest_sha256"] == sha(raw("NP_manifest"))
        and actual["identity"]["run_id"] == execution["run_id"] == "45893562391"
        and actual["identity"]["run_attempt"] == execution["run_attempt"] == "1"
        and actual["parameters"] == npm["parameters"] == np_owner.PARAMETERS
        and actual["completed_targets"] == np_owner.TARGETS and actual["saved_record_count"] == 2
        and set(actual["new_records"]) == set(np_owner.TARGETS)
        and sorted(actual) == npm["allowed_scientific_fields"]
        and actual["candidate_record"] is actual["current_target"] is None
        and execution["scientific_files"] == [{"path":roles["NP_actual"],"bytes":len(raw("NP_actual")),
                                               "sha256":sha(raw("NP_actual"))}],
        "entire genuine completed NP trial, source and error outcome")
    first = actual["new_records"][np_owner.TARGETS[0]]
    require(first["all_source_and_mean_components_retained"] is first["selected_operator_difference_paid"] is True
        and first["complete_trial_jumps_exact"] == "0" and first["full_domain"] == ["0","9/50"]
        and actual["parameters"]["terminal_data"] == "entire_pair_zero_at_9_over_50_then_exact_zero_extension"
        and actual["parameters"]["selected_to_budget_ratio_upper"] == PARAMETERS["selected_to_budget_ratio_upper"]
        and actual["parameters"]["complete_centre_residual_degree"] == 160
        and actual["parameters"]["complete_centre_fourier_degree"] == 32
        and actual["parameters"]["trial_fourier_degree"] == 96
        and sha(raw("NP_math")) == specs["nu_math"]["sha256"]
        and actual["result"]["complete_selected_strict_nu_particular_certified"] is True
        and actual["result"]["unknown_true_solution_remains_full_Fourier"] is True
        and actual["result"]["both_physical_density_means_retained"] is True,
        "true full-frequency error with both means and no uncharged short-interval impulses")
    dex = parse(raw("D_execution"));D = dex["actual_scientific_receipt"]
    require(sha(raw("D_execution")) == specs["SL_D_execution"]["sha256"]
        and dex["complete"] is D["complete"] is D["proved"] is True
        and dex["actual_returncode"] == D["actual_returncode"] == 0
        and dex["actual_failure"] is D["failure"] is None
        and D["complete_original_rows_verified"] == 7721 and len(D["original_part_receipts"]) == 40
        and D["original_rows_canonical_payload_sha256"] == actual["original_full_row_payload_sha256"]
        and D["derived_continuous_centre_definition_sha256"] == actual["reference_identity"]["continuous_centre_definition_sha256"]
        and D["derived_continuous_response_definition_sha256"] == actual["reference_identity"]["continuous_response_definition_sha256"]
        and all(g["passed"] is True for g in D["gates"]),
        "entire already completed D result and original whole body-row definition")
    original_history = [x for x in npm["historical_inputs"] if x["role"].startswith("original_rows_")]
    require(manifest["historical_inputs"] == original_history and len(original_history) == 40,
        "all and only necessary original whole row descriptors")
    spex = parse(raw("SP_execution"));SP = spex["actual_scientific_receipt"]
    require(sha(raw("SP_execution")) == SP_SHA and spex["complete"] is SP["complete"] is SP["proved"] is True
        and spex["actual_returncode"] == SP["actual_returncode"] == 0
        and spex["actual_failure"] is SP["failure"] is None
        and SP["kind"] == "actual_complete_primitive_mean_strict_propagation_v1"
        and SP["exact_family_identity"] == actual["reference_identity"]
        and len(SP["gates"]) == 20 and all(g["passed"] is True for g in SP["gates"])
        and SP["scope"]["all_Fourier_variations_and_two_means_retained"] is True
        and SP["scope"]["full_ordinary_sources_and_affine_impulses_retained"] is True,
        "same original full selected family and complete SP scalar and matrix conclusion")
    comparison,endpoint = SP["complete_strict_propagation_conclusion"],SP["complete_endpoint_readout_conclusion"]
    require(comparison["exact_interval"] == ["0","2333968743003/10000000000000"]
        and comparison["complete_mean_coordinates"] == 2
        and comparison["all_shorter_ordered_products_and_source_insertions_included"] is True
        and comparison["affine_jumps_are_independent_without_radial_length_factor"] is True
        and len(comparison["reverse_nonradial_product"]) == 2
        and all(len(row) == 2 for row in comparison["reverse_nonradial_product"]),
        "whole original chronological matrix including every source insertion and both means")
    integrals,prior = first["whole_trial_integrals"],actual["copied_prior_scalar_records"]
    waist = endpoint["waist_complete_radial_factors"]
    saved = {"Jq":comparison["new_compact_log_variation_fee_upper"],
        "injection":endpoint["complete_strict_Hminus1_source_injection_upper"],
        "waist_n_upper":waist["density_radial_factor_upper"],"waist_q_lower":waist["q_lower"],
        "whole_q_lower":comparison["new_entire_q_lower"],"whole_q_upper":comparison["new_entire_q_upper"],
        "R":integrals["residual_L1_Hminus1"],
        "H0":integrals["trial_L1_L2"],"H1":integrals["trial_angle_L1_L2"],
        "M0":prior["M0"],"M1":prior["M1"],"NC":prior["N_C"],
        "old_D":first["complete_selected_waist_density_error_upper"]}
    require(not any(name in sys.modules for name in ("flint","numpy","scipy")),"metadata-only old outcome consumption")
    return {"NP":actual,"D":D,"SP":SP,"saved":saved}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-map","output"):parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--checkout",required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT") == "1","one new short radial target only in public Actions")
    raw = args.manifest.read_bytes();manifest = parse(raw)
    require(sha(raw) == args.manifest_sha and manifest["kind"] == MANIFEST_KIND
        and manifest["scientific_kind"] == KIND and manifest["stage"] == STAGE
        and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
        and manifest["target_order"] == TARGETS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
        "complete immutable short-interval scientific contract")
    specs = manifest["files"]+manifest["historical_inputs"];input_map = parse(args.input_map.read_bytes())
    require(set(input_map) == {x["role"] for x in specs},"all complete current and necessary original inputs")
    raws,paths = {},{}
    for item in specs:
        path = Path(input_map[item["role"]]);content = path.read_bytes()
        require(len(content) == item["bytes"] and sha(content) == item["sha256"],"whole immutable input")
        raws[item["path"]],paths[item["path"]] = content,path
    require(sha(Path(__file__).read_bytes()) == next(x["sha256"] for x in specs if x["role"] == "science"),
        "entire actual running source")
    sys.dont_write_bytecode = True;admitted = admit(manifest,raws,paths)
    require(not args.output.exists(),"never overwrite an actual accepted prefix")
    state = {"identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
        "source_sha256":sha(Path(__file__).read_bytes()),"run_id":os.environ["GITHUB_RUN_ID"],"run_attempt":"1",
        "event_commit":os.environ["GITHUB_SHA"],"actual_checkout_commit":args.checkout,"arithmetic_bits":320},
        "parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,"actual_returncode":None,
        "failure":None,"stage":"whole_original_completed_NP_and_SP_admitted",
        "completed_targets":[],"current_target":None,"candidate_record":None,"new_records":{},"saved_record_count":0,
        "whole_completed_inputs":{"all_input_descriptors_sha256":sha(canonical(specs)),
            "current_objects":len(manifest["files"]),"historical_objects":40,
            "all7721_original_rows_admitted":False,"original_full_row_payload_sha256":None},
        "reference_identity":admitted["NP"]["reference_identity"],
        "selected_member_identity":admitted["NP"]["selected_member_identity"],
        "copied_prior_scalar_records":admitted["saved"],"short_radial_receipts":None,"result":None,
        "old_scientific_target_calls":0,"new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"wall_seconds":0.0}
    require(sorted(state) == SCI_FIELDS,"whole new scientific envelope")
    started = time.perf_counter()
    def save():
        state["wall_seconds"] = time.perf_counter()-started
        require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],"new short radial time budget")
        content = canonical(state);require(len(content) <= manifest["operation"]["maximum_scientific_bytes"],"whole small conclusion")
        atomic(args.output,content)
    save()
    try:
        helper = load(paths[manifest["roles"]["row_inputs"]],"_SB_same_original_row_reader")
        rows,receipts = helper.admit_all_rows([paths[x["path"]] for x in manifest["historical_inputs"]],
            {"old_body_manifest":parse(raws[manifest["roles"]["old_body_manifest"]]),"NW":{"difference":admitted["D"]}})
        state["whole_completed_inputs"].update(all7721_original_rows_admitted=True,
            original_full_row_payload_sha256=helper.ROW_PAYLOAD,original40_part_receipts_sha256=sha(canonical(receipts)))
        state["stage"] = "all_whole_original_rows_admitted_new_short_radial_target";save()
        import flint
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),"packages":{"python-flint":version("python-flint")}}
        require(runtime == RUNTIME,"complete fixed directed runtime")
        state["runtime"] = runtime;flint.ctx.prec = 320;arb = flint.arb
        def ball(record):
            value = arb(record["ball"])
            if "lower" in record and "upper" in record:
                value = value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite(),"whole finite scalar ball");return value
        def publish(name,value,direction):
            require(name == TARGETS[state["saved_record_count"]] and direction == "upper","next entire new upper target")
            value = value.upper();require(value.is_finite() and value >= 0,"finite nonnegative full result")
            record = {"ball":value.str(PARAMETERS["decimal_record_digits"]),"bound":"upper"}
            require(arb(record["ball"]).contains(value),"outward complete written ball")
            state["current_target"] = name;state["candidate_record"] = {"name":name,"record":record};save()
            require(parse(args.output.read_bytes())["candidate_record"] == state["candidate_record"],"whole candidate readback")
            state["new_records"][name] = record;state["completed_targets"].append(name);state["saved_record_count"] += 1
            state["current_target"] = state["candidate_record"] = None;save()
            return ball(parse(args.output.read_bytes())["new_records"][name]).upper()
        math = load(paths[manifest["roles"]["short_math"]],"_SB_new_short_radial_math")
        require(list(math.OUTPUT_ORDER) == TARGETS,"complete new scalar order")
        state["short_radial_receipts"] = math.complete_short_error(flint,rows,ball,
            {key:ball(value) for key,value in admitted["saved"].items()},publish)
        state["result"] = {"kind":KIND,"complete_new_record_count":11,"complete_new_record_order":list(TARGETS),
            "same_original_selected_full_frequency_particular":True,"whole_original_SP_nonradial_matrix_retained":True,
            "all_shorter_source_insertion_intervals_retained":True,"both_physical_means_retained":True,
            "full_NP_error_sources_reused_without_subtracting_uppers":True,
            "true_short_waist_error_uses_min_with_complete_old_D":True,
            "uniform_interior_primitive_plus_mean_error_proved":True,"whole_formal_readback_for_each_dependency":True,
            "uniform_interior_and_radial_L2_error_proved":True,
            "degree160_factor_applies_only_to_original_centre_residual":True,
            "all_selected_operator_and_parameter_difference_terms_keep_full_L2_units":True,
            "old_trial_residual_pairings_or_nonradial_matrix_recomputed":False,"new_trial_chosen":False,
            "nonlocal_phase_or_height_signed_column_proved":False,"full_incoming_inverse_or_Schur_proved":False,
            "topic_completion_proved":False}
        state["complete"] = state["proved"] = True;state["actual_returncode"] = 0
        state["stage"] = "complete_"+STAGE+"_scalar_branch";save();return 0
    except BaseException as exc:
        state["complete"] = state["proved"] = False;state["actual_returncode"] = 1
        state["failure"] = {"type":type(exc).__name__,"message":str(exc)[:2000],"traceback":traceback.format_exc()[-6000:]}
        state["stage"] = "failed_with_actual_complete_prefix_retained"
        state["wall_seconds"] = time.perf_counter()-started;atomic(args.output,canonical(state));traceback.print_exc();return 1


if __name__ == "__main__":
    sys.exit(main())
