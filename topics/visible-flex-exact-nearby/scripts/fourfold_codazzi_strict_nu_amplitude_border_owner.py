"""PA actual: one new complete physical amplitude pairing of the true nu column.

Restore only NP's necessary exact frozen carriers.  Reuse its full selected
error and the original whole97 physical row, paying selected row change.
"""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, os, platform
from pathlib import Path
import sys, tempfile, time, traceback

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_strict_nu_amplitude_border_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_selected_amplitude_row_transfer_math.py"
RESTORE = TOPIC+"/scripts/fourfold_codazzi_strict_nu_trial_carrier_restore.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_amplitude_border_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_strict_nu_amplitude_border_manifest.py"
PROOF = TOPIC+"/results/R147-supplement-selected-amplitude-border-for-the-strict-parameter-particular.md"
NP_MANIFEST = TOPIC+"/notes/2026-11-27-strict-nu-particular-inputs.json"
NP_BASE = TOPIC+"/notes/strict_nu_particular_ci/run-45893562391-1"
AMP_ROW = TOPIC+"/notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json"
AMP_SHA = "c99e3f6c7fd4975ee8fd1de26fadad7f4e42c6c379a861830d6fa419046b052e"
AMP_PROOF = TOPIC+"/results/R133-supplement-actual-complete-96-waist-amplitude-Jacobi-row.md"
KIND = "R147_complete_strict_nu_amplitude_border_v1"
STAGE = "complete_strict_nu_amplitude_border"
MANIFEST_KIND = "R147_complete_strict_nu_amplitude_border_inputs_v1"
RUNTIME = {"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS = {
    "arithmetic_bits":320,"decimal_record_digits":60,"maximum_scientific_wall_seconds":1800,
    "complete_frozen_trial_nodes":740,"complete_frozen_trial_real_dimension":193,"complete_frozen_arrays":4,
    "whole_original_body_rows":7721,"complete_old_amplitude_directions":97,
    "physical_frequency_factor":4,"physical_period":"pi/2","normalized_angular_measure":True,
    "amplitude_is_physical_unnormalized_A":True,"normalized_row_is_A_over_exact_alpha":True,
    "exact_alpha":"6890507429876859/9007199254740992",
    "continuous_centre_definition_sha256":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "continuous_direction_definition_sha256":"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "original_selected_run":"43588332723/1","original_selected_loss":"1/250",
    "fixed_intrinsic_parameter":"eta_0","selected_state_difference_upper":"8899847/5000000000000000",
    "all_unknown_modes_and_both_means_retained":True,"old_residual_or_pairing_targets_recomputed":False,
    "only_original_exact_trial_carriers_restored":True,"new_complete_scalar_records":8,
}
TARGETS = [
    "complete_original_trial_second_primitive_mean_upper",
    "complete_selected_amplitude_row_change_dual_upper",
    "complete_selected_amplitude_row_dual_upper",
    "complete_original_trial_physical_amplitude_pairing",
    "complete_trial_amplitude_row_transfer_error_upper",
    "complete_true_particular_amplitude_error_upper",
    "complete_true_particular_physical_amplitude_enclosure",
    "complete_true_particular_normalized_amplitude_enclosure",
]
SIGNED_INDICES = (3,6,7)
SCI_FIELDS = sorted([
    "identity","parameters","runtime","complete","proved","actual_returncode","failure","stage",
    "completed_targets","current_target","candidate_record","new_records","saved_record_count",
    "whole_completed_inputs","reference_identity","selected_member_identity","copied_prior_scalar_records",
    "necessary_original_trial_receipts","new_amplitude_input_receipts","result",
    "old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases","wall_seconds",
])


def require(ok,message):
    if not ok:
        raise ValueError(message)


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


def gather(root,np_actual,np_execution,np_manifest=NP_MANIFEST):
    root = Path(root);current,roles = {},{}
    def add(role,path,expected=None):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,"safe entire current topic input")
        raw = (root/path).read_bytes();raw.decode()
        require(0 < len(raw) < 100000,"whole small current source or completed result")
        if path.endswith(".py"):ast.parse(raw.decode(),filename=path)
        spec = {"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if expected is not None:
            require(all(spec[key] == expected[key] for key in ("path","bytes","sha256","git_blob_sha")),
                    "entire unchanged original input: "+role)
        current.setdefault(path,spec);roles[role] = path
        return parse(raw) if path.endswith(".json") else raw
    npm = add("NP_manifest",np_manifest)
    reviewed = next(x for x in npm["files"] if x["role"] == "reviewed_rules")
    add("reviewed_rules",reviewed["path"],reviewed)
    for item in npm["files"]:add("NP_"+item["role"],item["path"],item)
    add("NP_actual",np_actual);add("NP_execution",np_execution)
    for role,path in (("old_amplitude_row",AMP_ROW),("old_amplitude_proof",AMP_PROOF),
        ("science",SOURCE),("amplitude_math",MATH),("trial_restore",RESTORE),
        ("worker",WORKER),("generator",GENERATOR),("proof",PROOF)):
        add(role,path)
    history = []
    for item in npm["historical_inputs"]:
        spec = dict(item,role="NP_"+item["role"]);history.append(spec);roles[spec["role"]] = spec["path"]
    require(len(history) == 51 and len({x["path"] for x in history+list(current.values())})
            == len(history)+len(current),"all complete original NP descriptors and distinct current inputs")
    return {"files":sorted(current.values(),key=lambda x:x["role"]),"historical_inputs":history,"roles":roles}


def admit(manifest,raws,paths):
    """Only small complete old outcomes/definitions; no numerical imports."""
    roles = manifest["roles"]
    def raw(role):return raws[roles[role]]
    npm = parse(raw("NP_manifest"));np_specs = {x["role"]:x for x in npm["files"]}
    np_owner = load(paths[roles["NP_science"]],"_PA_original_NP_metadata")
    prior = np_owner.admit_current(npm,raws,paths)
    actual,execution = parse(raw("NP_actual")),parse(raw("NP_execution"))
    require(actual["complete"] is actual["proved"] is execution["complete"] is True
        and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
        and actual["failure"] is execution["failure"] is None
        and actual["identity"]["kind"] == np_owner.KIND
        and actual["identity"]["manifest_sha256"] == sha(raw("NP_manifest"))
        and actual["identity"]["source_sha256"] == np_specs["science"]["sha256"]
        and actual["identity"]["run_id"] == execution["run_id"] == "45893562391"
        and actual["identity"]["run_attempt"] == execution["run_attempt"] == "1"
        and actual["parameters"] == npm["parameters"] == np_owner.PARAMETERS
        and actual["completed_targets"] == np_owner.TARGETS and actual["saved_record_count"] == 2
        and set(actual["new_records"]) == set(np_owner.TARGETS)
        and sorted(actual) == npm["allowed_scientific_fields"]
        and actual["candidate_record"] is actual["current_target"] is None
        and actual["reference_identity"] == prior["R147"]["reference_identity"]
        and actual["selected_member_identity"] == prior["R147"]["selected_member_identity"]
        and execution["scientific_files"] == [{"path":roles["NP_actual"],"bytes":len(raw("NP_actual")),
                                               "sha256":sha(raw("NP_actual"))}],
        "one genuine entire completed NP outcome with its original actual trial and source")
    for key in ("complete_selected_strict_nu_particular_certified","unknown_true_solution_remains_full_Fourier",
        "both_physical_density_means_retained","all_trial_jumps_proved_zero_from_shared_exact_endpoint_data"):
        require(actual["result"][key] is True,"whole original NP qualification: "+key)
    first,second = (actual["new_records"][key] for key in np_owner.TARGETS)
    names = {"row_%03d"%j for j in range(1,97)}
    require(second["complete_signed_output_count"] == 194 and second["complete_signed_trial_pairing_count"] == 192
        and second["trial_pairings_exclude_PDE_and_RW_error_fees"] is True
        and set(second["complete_signed_output_balls"]["independent_density_means"]) == {"plus","minus"}
        and all(set(second["complete_signed_trial_pairings"][key]) == names for key in
                ("declared_incoming_cosine96","original_physical_primitive96"))
        and len(actual["trial_receipts"]["complete_arrays"]) == 4
        and all(x["shape"] == [740,193] and x["bytes"] == 1142560
                for x in actual["trial_receipts"]["complete_arrays"]),
        "all existing signed objects and all four complete original trial receipts retained")
    row = parse(raw("old_amplitude_row"))
    require(sha(raw("old_amplitude_row")) == AMP_SHA and row["complete"] is row["executed"] is True
        and row["gate_count"] == len(row["gates"]) == 12 and all(x["passed"] is True for x in row["gates"])
        and row["candidate_sha256"] == "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
        and row["whole_original_eta"] is row["all_96_head_columns_retained"] is True
        and row["new_centre_row_not_transferred_to_unknown_Wiener_ball"] is True
        and len(row["rows"]) == 96 and int(row["exact_interval_denominator"]) == 2**384
        and row["exact_inputs"]["alpha"] == PARAMETERS["exact_alpha"] == actual["parameters"]["exact_alpha"]
        and all(actual["parameters"][key] == PARAMETERS[key] for key in
            ("continuous_centre_definition_sha256","continuous_direction_definition_sha256","fixed_intrinsic_parameter")),
        "whole original97 amplitude row, exact centre and explicitly unpaid selected row change")
    require(prior["D"]["chosen_global_constants"]["response_pair_A0"] == "19"
        and not any(name in sys.modules for name in ("flint","numpy","scipy")),
        "same original full selected state bound, no old target arithmetic in admission")
    return {"NP":actual,"NP_manifest":npm,"prior":prior,"old_row":row,
        "saved":{"selected_mean":second["whole_selected_waist_mean_enclosure"],
            "D":first["complete_selected_waist_density_error_upper"],"H":second["trial_waist_density_norm_upper"]}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-map","output"):parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--checkout",required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT") == "1","one new authorized physical amplitude pairing")
    manifest_raw = args.manifest.read_bytes();manifest = parse(manifest_raw)
    require(sha(manifest_raw) == args.manifest_sha and manifest["kind"] == MANIFEST_KIND
        and manifest["scientific_kind"] == KIND and manifest["stage"] == STAGE
        and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
        and manifest["target_order"] == TARGETS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
        "entire new amplitude-border contract")
    specs = manifest["files"]+manifest["historical_inputs"];input_map = parse(args.input_map.read_bytes())
    require(set(input_map) == {x["role"] for x in specs},"every complete old and new input")
    raws,paths = {},{}
    for item in specs:
        path = Path(input_map[item["role"]]);raw = path.read_bytes()
        require(len(raw) == item["bytes"] and sha(raw) == item["sha256"],"entire immutable input")
        raws[item["path"]],paths[item["path"]] = raw,path
    require(sha(Path(__file__).read_bytes()) == next(x["sha256"] for x in specs if x["role"] == "science"),
            "the entire actual running source")
    sys.dont_write_bytecode = True;admitted = admit(manifest,raws,paths)
    npm,prior = admitted["NP_manifest"],admitted["prior"];roles = npm["roles"]
    helper = load(paths[roles["inputs_math"]],"_PA_original_full_input_admission")
    old_body = parse(raws[roles["old_body_manifest"]])
    rows,part_receipts = helper.admit_all_rows(
        [paths[item["path"]] for item in npm["historical_inputs"] if item["role"].startswith("original_rows_")],
        {"old_body_manifest":old_body,"NW":{"difference":prior["D"]}})
    repair = parse(raws[roles["old_centre_repair"]])
    require(repair["complete"] is True and repair["derived_definition_sha256"]
        == PARAMETERS["continuous_centre_definition_sha256"] and all(x["passed"] is True for x in repair["gates"]),
        "entire original continuous centre definition")
    require(not args.output.exists(),"never overwrite a real accepted prefix")
    state = {"identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
        "source_sha256":sha(Path(__file__).read_bytes()),"run_id":os.environ["GITHUB_RUN_ID"],"run_attempt":"1",
        "event_commit":os.environ["GITHUB_SHA"],"actual_checkout_commit":args.checkout,"arithmetic_bits":320},
        "parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,"actual_returncode":None,
        "failure":None,"stage":"complete_actual_NP_and_original_amplitude_inputs_admitted",
        "completed_targets":[],"current_target":None,"candidate_record":None,"new_records":{},"saved_record_count":0,
        "whole_completed_inputs":{"all_input_descriptors_sha256":sha(canonical(specs)),
            "current_objects":len(manifest["files"]),"historical_objects":51,"all40_original_row_parts_read":True,
            "all7721_original_rows_admitted":True,"old_amplitude_all97_signed_directions_read":True},
        "reference_identity":admitted["NP"]["reference_identity"],
        "selected_member_identity":admitted["NP"]["selected_member_identity"],
        "copied_prior_scalar_records":admitted["saved"],"necessary_original_trial_receipts":None,
        "new_amplitude_input_receipts":None,"result":None,"old_scientific_target_calls":0,
        "new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"wall_seconds":0.0}
    require(sorted(state) == SCI_FIELDS,"whole new scientific envelope")
    started = time.perf_counter()
    def save():
        state["wall_seconds"] = time.perf_counter()-started
        require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],"new amplitude scientific time budget")
        raw = canonical(state);require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],"whole small public result")
        atomic(args.output,raw)
    def progress(stage,detail):
        state["stage"] = stage;save();print(json.dumps({"stage":stage,**detail}),flush=True)
    save()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),"packages":{key:version(key) for key in RUNTIME["packages"]}}
        require(runtime == RUNTIME,"the same complete original floating and directed runtime")
        state["runtime"] = runtime;flint.ctx.prec = 320;arb = flint.arb
        def ball(record):
            value = arb(record["ball"])
            if "lower" in record and "upper" in record:
                value = value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite(),"whole finite original or new scientific ball");return value
        def publish(name,value,direction):
            index = state["saved_record_count"]
            require(name == TARGETS[index] and direction == ("signed_enclosure" if index in SIGNED_INDICES else "upper"),
                    "next whole new target with its exact sign convention")
            value = value if direction == "signed_enclosure" else value.upper()
            require(value.is_finite() and (direction == "signed_enclosure" or value >= 0),"finite complete scientific value")
            record = {"ball":value.str(PARAMETERS["decimal_record_digits"]),"bound":direction}
            require(arb(record["ball"]).contains(value),"whole signed or upper result retained")
            state["current_target"] = name;state["candidate_record"] = {"name":name,"record":record};save()
            require(parse(args.output.read_bytes())["candidate_record"] == state["candidate_record"],"full candidate readback")
            state["new_records"][name] = record;state["completed_targets"].append(name);state["saved_record_count"] += 1
            state["current_target"] = state["candidate_record"] = None;save()
            restored = ball(parse(args.output.read_bytes())["new_records"][name])
            return restored if direction == "signed_enclosure" else restored.upper()
        restore = load(paths[manifest["roles"]["trial_restore"]],"_PA_necessary_same_frozen_carrier_restore")
        math = load(paths[manifest["roles"]["amplitude_math"]],"_PA_new_complete_signed_amplitude_pairing")
        require(list(math.OUTPUT_ORDER) == TARGETS and math.SIGNED_INDICES == SIGNED_INDICES,"complete exact new scalar order")
        with tempfile.TemporaryDirectory(prefix="private-PA-original-NP-") as private:
            trial,waist,receipts = restore.restore(np,flint,npm,admitted["NP"],raws,paths,
                helper,rows,part_receipts,private,progress,atomic)
            state["necessary_original_trial_receipts"] = receipts
            state["new_amplitude_input_receipts"] = {"old_row_sha256":AMP_SHA,
                "whole_waist_K":{"ball":waist["waist_K"].str(80)},
                "whole_waist_a":{"ball":waist["waist_a"].str(80)},
                "physical_trial_coefficient_count":193,"original_input_mean_retained":True}
            state["stage"] = "new_complete_physical_amplitude_pairing";save()
            saved = {key:ball(value) for key,value in admitted["saved"].items()}
            reread = parse(args.output.read_bytes())["new_amplitude_input_receipts"]
            saved.update(waist_K=ball(reread["whole_waist_K"]),waist_a=ball(reread["whole_waist_a"]))
            math.complete_selected_amplitude(flint,admitted["old_row"],trial,saved,publish)
        state["result"] = {"kind":KIND,"complete_new_record_count":8,"complete_new_record_order":list(TARGETS),
            "same_original_NP_complete_trial_carriers_restored":True,"same_selected_Q_delta_amplitude_row_paid":True,
            "whole_original97_amplitude_entries_and_their_signs_retained":True,
            "full_infinite_error_paid_in_primitive_plus_mean_dual":True,"both_physical_density_means_retained":True,
            "physical_and_original_alpha_normalized_signed_balls_separate":True,
            "every_dependent_scalar_uses_whole_formal_readback":True,
            "new_trial_selected":False,"old_residual_or_signed_pairings_recomputed":False,
            "old_amplitude_Bessel_or_row_targets_recomputed":False,"nonlocal_phase_column_proved":False,
            "true_nu_or_phase_Schur_nonzero_proved":False,"topic_completion_proved":False}
        state["complete"] = state["proved"] = True;state["actual_returncode"] = 0
        state["stage"] = "complete_"+STAGE+"_scalar_branch";save();return 0
    except BaseException as exc:
        state["complete"] = state["proved"] = False;state["actual_returncode"] = 1
        state["failure"] = {"type":type(exc).__name__,"message":str(exc)[:2000],"traceback":traceback.format_exc()[-6000:]}
        state["stage"] = "failed_with_actual_complete_prefix_retained"
        state["wall_seconds"] = time.perf_counter()-started;atomic(args.output,canonical(state));traceback.print_exc();return 1


if __name__ == "__main__":
    sys.exit(main())

