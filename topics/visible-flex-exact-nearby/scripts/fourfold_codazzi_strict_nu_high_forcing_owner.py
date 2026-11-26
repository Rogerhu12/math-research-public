"""NH: twelve new complete scalar consequences of an actual NP particular.

Whole NP and JC successes are mandatory. Original W derivative data and the
entire old RW admission are read as metadata. No trial, native PDE carrier,
DFT, old row error, pairing or old norm target is evaluated.
"""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, importlib.util, json, os, platform
from pathlib import Path
import sys, time, traceback

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_strict_nu_high_forcing_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_strict_nu_high_forcing_math.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_high_forcing_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_strict_nu_high_forcing_manifest.py"
PROOF = TOPIC+"/results/R147-supplement-mean-aware-complete-high-parameter-forcing.md"
JC_MANIFEST = TOPIC+"/notes/2026-11-27-joint-compound-waist-row-inputs.json"
JC_ACTUAL = TOPIC+"/notes/joint_compound_row_ci/run-45887337009-1/actual-joint-compound-waist-row-error.json"
JC_EXECUTION = TOPIC+"/notes/joint_compound_row_ci/run-45887337009-1/execution.json"
NP_MANIFEST = TOPIC+"/notes/2026-11-27-strict-nu-particular-inputs.json"
NP_PUBLIC_WORKER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py"
SL_ADAPTER = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_public_worker.py"
OLD_ENGINE = TOPIC+"/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py"
KIND = "R147_complete_true_strict_nu_high_forcing_v1"
STAGE = "complete_true_strict_nu_high_forcing"
MANIFEST_KIND = "R147_complete_true_strict_nu_high_forcing_inputs_v1"
RUNTIME = {"python":"3.12.14","packages":{"python-flint":"0.9.0"}}
PARAMETERS = {
    "arithmetic_bits":320,"decimal_record_digits":60,"maximum_scientific_wall_seconds":120,
    "row_modes":96,"complete_high_target_modes":"every |j|>=97, both branches",
    "physical_frequency_factor":4,"physical_period":"pi/2","normalized_angular_measure":True,
    "original_conjugacy_strip":"1/128","original_selected_run":"43588332723/1",
    "original_selected_loss":"1/250","fixed_original_waist_normalizer_cutoff":268435456,
    "complete_NP_true_observations":194,"complete_NP_raw_signed_trial_observations":192,
    "both_independent_physical_means_retained":True,"new_complete_scalar_records":12,
    "unobserved_low_sine_energy_subtracted":False,"original_pairings_or_trials_recomputed":False,
}
TARGETS = [
    "same_true_H_constant_density_nonmean_leakage_upper",
    "complete_trial_two_mean_norm_lower","complete_trial_two_mean_norm_upper",
    "complete_trial_primitive_pair_norm_upper","complete_trial_true_angle_nonmean_pair_norm_upper",
    "complete_raw_paired_cosine96_norm_lower","complete_true_angle_trial_paired_cosine96_norm_lower",
    "complete_trial_paired_high97_norm_upper","complete_true_strict_nu_paired_L2_norm_upper",
    "complete_true_strict_nu_paired_high97_norm_upper",
    "complete_true_strict_nu_incoming_cosine96_error_upper",
    "complete_true_strict_nu_physical_cosine96_error_upper",
]
LOWER_TARGETS = {TARGETS[i] for i in (1,5,6)}
SCI_FIELDS = sorted([
    "identity","parameters","runtime","complete","proved","actual_returncode","failure","stage",
    "completed_targets","current_target","candidate_record","new_records","saved_record_count",
    "whole_completed_inputs","reference_identity","selected_member_identity","copied_prior_scalar_records",
    "result","old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases","wall_seconds",
])


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw,
        parse_constant=lambda value:(_ for _ in ()).throw(ValueError(value)))


def load(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def atomic(path,raw):
    path = Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+".candidate")
    with temporary.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.replace(temporary,path)


def gather(root,np_actual,np_execution,np_manifest=NP_MANIFEST):
    """Complete small existing conclusions and new source metadata only."""
    root = Path(root)
    current,roles = {},{}
    def add(role,path,expected=None):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,"safe complete topic input")
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000,"whole small current object: "+path)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(),filename=path)
        item = {"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if expected is not None:
            require(all(item[key] == expected[key] for key in ("path","bytes","sha256","git_blob_sha")),
                    "whole unchanged completed input: "+role)
        current.setdefault(path,item);roles[role] = path
        return parse(raw) if path.endswith(".json") else raw
    jc = add("JC_manifest",JC_MANIFEST)
    reviewed = next(x for x in jc["files"] if x["role"] == "reviewed_rules")
    add("reviewed_rules",reviewed["path"],reviewed)
    for item in jc["files"]:
        add("JC_"+item["role"],item["path"],item)
    add("JC_actual",JC_ACTUAL);add("JC_execution",JC_EXECUTION)
    np_manifest_doc = add("NP_manifest",np_manifest)
    np_specs = {x["role"]:x for x in np_manifest_doc["files"]}
    for role in ("science","nu_math","nu_proposal","trial_math","proof"):
        item = np_specs[role]
        add("NP_"+role,item["path"],item)
    add("NP_actual",np_actual);add("NP_execution",np_execution)
    for role,path in (("worker_parent",NP_PUBLIC_WORKER),("worker_SL_adapter",SL_ADAPTER),
                      ("worker_original_engine",OLD_ENGINE),("science",SOURCE),("nu_high_math",MATH),
                      ("worker",WORKER),("generator",GENERATOR),("proof",PROOF)):
        add(role,path)
    history = []
    for item in jc["historical_inputs"]:
        history.append(dict(item,role="JC_"+item["role"]))
        roles["JC_"+item["role"]] = item["path"]
    require(len(history) == 4 and len({x["path"] for x in history+list(current.values())})
            == len(history)+len(current),"all four original W/R31/K/H objects and distinct current files")
    return {"files":sorted(current.values(),key=lambda x:x["role"]),
            "historical_inputs":history,"roles":roles}


def admit(manifest,raws,paths):
    """Whole genuine NP/JC outcomes; no numerical library or old target call."""
    roles = manifest["roles"]
    def raw(role):
        return raws[roles[role]]
    jcm = parse(raw("JC_manifest"))
    jc_specs = {x["role"]:x for x in jcm["files"]+jcm["historical_inputs"]}
    jc_owner = load(paths[roles["JC_science"]],"_NH_whole_JC_admission")
    prior,records = jc_owner.admit_complete_inputs(
        {key:raws[item["path"]] for key,item in jc_specs.items()},jc_specs)
    jc,jce = parse(raw("JC_actual")),parse(raw("JC_execution"))
    require(jc["complete"] is jc["proved"] is jce["complete"] is True
            and jc["actual_returncode"] == jce["actual_child_returncode"] == 0
            and jc["failure"] is jce["failure"] is None
            and jc["identity"]["kind"] == jc_owner.KIND
            and jc["identity"]["manifest_sha256"] == sha(raw("JC_manifest"))
            and jc["identity"]["source_sha256"] == jc_specs["science"]["sha256"]
            and jc["identity"]["joint_math_sha256"] == jc_specs["joint_math"]["sha256"]
            and jc["identity"]["run_id"] == jce["run_id"] == "45887337009"
            and jc["parameters"] == jcm["parameters"] == jc_owner.PARAMETERS
            and jc["completed_targets"] == jc_owner.TARGETS and jc["saved_record_count"] == 7
            and set(jc["new_records"]) == set(jc_owner.TARGETS)
            and sorted(jc) == jcm["allowed_scientific_fields"]
            and jc["copied_prior_scalar_records"] == records
            and jce["scientific_files"] == [{"path":roles["JC_actual"],"bytes":len(raw("JC_actual")),
                                            "sha256":sha(raw("JC_actual"))}],
            "the entire true completed JC7 result with original W derivative balls")
    for name in ("complete_joint_row_operator_error_proved","strict_positive_saved_homotopy_lower",
                 "all_DFT_alias_and_infinite_compound_tails_paid","original_RW_trials_unchanged"):
        require(jc["result"][name] is True,"whole completed JC qualification: "+name)
    npm = parse(raw("NP_manifest"))
    np_specs = {x["role"]:x for x in npm["files"]}
    np_owner = load(paths[roles["NP_science"]],"_NH_whole_NP_metadata")
    np_actual,npe = parse(raw("NP_actual")),parse(raw("NP_execution"))
    require(np_actual["complete"] is np_actual["proved"] is npe["complete"] is True
            and np_actual["actual_returncode"] == npe["actual_child_returncode"] == 0
            and np_actual["failure"] is npe["failure"] is None
            and np_actual["identity"]["kind"] == np_owner.KIND
            and np_actual["identity"]["manifest_sha256"] == sha(raw("NP_manifest"))
            and np_actual["identity"]["source_sha256"] == np_specs["science"]["sha256"]
            and np_actual["identity"]["run_id"] == npe["run_id"]
            and np_actual["identity"]["run_attempt"] == npe["run_attempt"] == "1"
            and np_actual["parameters"] == npm["parameters"] == np_owner.PARAMETERS
            and np_actual["completed_targets"] == np_owner.TARGETS and np_actual["saved_record_count"] == 2
            and set(np_actual["new_records"]) == set(np_owner.TARGETS)
            and sorted(np_actual) == npm["allowed_scientific_fields"]
            and np_actual["candidate_record"] is np_actual["current_target"] is None
            and npe["scientific_files"] == [{"path":roles["NP_actual"],"bytes":len(raw("NP_actual")),
                                            "sha256":sha(raw("NP_actual"))}],
            "one entire actually completed full NP particular and all its signed outputs")
    for name in ("complete_selected_strict_nu_particular_certified","unknown_true_solution_remains_full_Fourier",
                 "both_physical_density_means_retained","all_trial_jumps_proved_zero_from_shared_exact_endpoint_data"):
        require(np_actual["result"][name] is True,"whole completed NP qualification: "+name)
    require(np_actual["reference_identity"] == jc["reference_identity"] == prior["family"]
            and all(doc[key] == 0 for doc in (np_actual,jc) for key in
                    ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
            "the same original selected family and completed scopes")
    first,second = (np_actual["new_records"][key] for key in np_owner.TARGETS)
    observations,trial = second["complete_signed_output_balls"],second["complete_signed_trial_pairings"]
    names = {"row_%03d"%j for j in range(1,97)}
    require(second["complete_signed_output_count"] == 194
            and set(observations) == {"declared_incoming_cosine96","original_physical_primitive96","independent_density_means"}
            and set(observations["independent_density_means"]) == {"plus","minus"}
            and second["complete_signed_trial_pairing_count"] == 192
            and second["trial_pairings_exclude_PDE_and_RW_error_fees"] is True
            and set(trial) == {"declared_incoming_cosine96","original_physical_primitive96"}
            and all(set(observations[name]) == set(trial[name]) == names for name in trial),
            "all194 true observations and all192 uninflated signed trial balls")
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),
            "whole-input admission never executes old numerical mathematics")
    return {"NP":np_actual,"JC":jc,"old_bounds":{
        "H1":records["H1"],"m":jc["new_records"][jc_owner.TARGETS[2]],
        "E":jc["new_records"][jc_owner.TARGETS[6]],
        "BH":np_actual["copied_prior_scalar_records"]["BH"],
        "KW":np_actual["copied_prior_scalar_records"]["KW"],
        "D":first["complete_selected_waist_density_error_upper"],
        "H":second["trial_waist_density_norm_upper"]},
        "true_means":observations["independent_density_means"],"raw_pairings":trial}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-map","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--checkout",required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1","one new authorized public scalar child")
    manifest_raw = args.manifest.read_bytes();manifest = parse(manifest_raw)
    require(sha(manifest_raw) == args.manifest_sha and manifest["kind"] == MANIFEST_KIND
            and manifest["scientific_kind"] == KIND and manifest["stage"] == STAGE
            and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
            and manifest["target_order"] == TARGETS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "the entire new scalar contract")
    specs = manifest["files"]+manifest["historical_inputs"]
    paths_by_role = parse(args.input_map.read_bytes())
    require(set(paths_by_role) == {x["role"] for x in specs},"every complete declared input")
    raws,paths = {},{}
    for item in specs:
        path = Path(paths_by_role[item["role"]]);raw = path.read_bytes()
        require(len(raw) == item["bytes"] and sha(raw) == item["sha256"],"complete immutable input")
        raws[item["path"]],paths[item["path"]] = raw,path
    require(sha(Path(__file__).read_bytes()) == next(x["sha256"] for x in specs if x["role"] == "science"),
            "the full actual running source")
    sys.dont_write_bytecode = True
    prior = admit(manifest,raws,paths)
    require(not args.output.exists(),"never overwrite an actual prefix")
    state = {"identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
        "source_sha256":sha(Path(__file__).read_bytes()),"run_id":os.environ["GITHUB_RUN_ID"],
        "run_attempt":"1","event_commit":os.environ["GITHUB_SHA"],"actual_checkout_commit":args.checkout,
        "arithmetic_bits":320},"parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,
        "actual_returncode":None,"failure":None,"stage":"complete_actual_NP_JC_W_inputs_admitted",
        "completed_targets":[],"current_target":None,"candidate_record":None,"new_records":{},"saved_record_count":0,
        "whole_completed_inputs":{"manifest_sha256":args.manifest_sha,"all_input_descriptors_sha256":sha(canonical(specs)),
            "current_objects":len(manifest["files"]),"historical_objects":4,
            "NP_complete_true_and_raw_signed_outputs_read":True,"JC_all_seven_complete_records_read":True,
            "whole_original_W_not_only_a_derivative_sup_read":True},
        "reference_identity":prior["NP"]["reference_identity"],
        "selected_member_identity":prior["NP"]["selected_member_identity"],
        "copied_prior_scalar_records":prior["old_bounds"],"result":None,
        "old_scientific_target_calls":0,"new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"wall_seconds":0.0}
    require(sorted(state) == SCI_FIELDS,"the complete scientific envelope")
    started = time.perf_counter()
    def save():
        state["wall_seconds"] = time.perf_counter()-started
        require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],"new scalar time budget")
        raw = canonical(state)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],"whole small scalar result")
        atomic(args.output,raw)
    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),"packages":{"python-flint":version("python-flint")}}
        require(runtime == RUNTIME,"the full fixed directed scalar runtime")
        state["runtime"] = runtime;flint.ctx.prec = 320;arb = flint.arb
        def ball(record):
            value = arb(record["ball"])
            if "lower" in record and "upper" in record:
                value = value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite(),"whole finite original scalar or signed observation")
            return value
        def publish(name,value,direction):
            require(name == TARGETS[state["saved_record_count"]]
                    and direction == ("lower" if name in LOWER_TARGETS else "upper"),
                    "exact next new bound and its proper direction")
            point = value.lower() if direction == "lower" else value.upper()
            require(point.is_finite() and point >= 0,"finite actual directed bound")
            record = {"ball":point.str(PARAMETERS["decimal_record_digits"]),"bound":direction}
            require(arb(record["ball"]).contains(point),"whole stored ball contains the original bound")
            state["current_target"] = name;state["candidate_record"] = {"name":name,"record":record};save()
            require(parse(args.output.read_bytes())["candidate_record"] == state["candidate_record"],
                    "complete new candidate readback")
            state["new_records"][name] = record;state["completed_targets"].append(name)
            state["saved_record_count"] += 1;state["current_target"] = state["candidate_record"] = None;save()
            restored = ball(parse(args.output.read_bytes())["new_records"][name])
            return restored.lower() if direction == "lower" else restored.upper()
        class API:
            zero,one = arb(0),arb(1)
            @staticmethod
            def rational(numerator,denominator=1):return arb(numerator)/denominator
            @staticmethod
            def sqrt(value):return value.sqrt()
            @staticmethod
            def lower(value):return value.lower()
        math = load(paths[manifest["roles"]["nu_high_math"]],"_NH_new_scalar_algebra")
        require(list(math.OUTPUT_ORDER) == TARGETS,"the complete new scalar order")
        math.complete_high_forcing(API,
            {key:ball(value) for key,value in prior["old_bounds"].items()},
            {key:ball(value) for key,value in prior["true_means"].items()},
            {key:{name:ball(value) for name,value in group.items()} for key,group in prior["raw_pairings"].items()},
            publish)
        state["result"] = {"kind":KIND,"complete_new_record_count":12,"complete_new_record_order":list(TARGETS),
            "whole_true_paired_high97_forcing_proved":True,"all_high_modes_and_two_means_retained":True,
            "mean_leakage_uses_original_full_Wiener_derivative":True,
            "Jacobian_lower_includes_same_true_H_endpoint":True,
            "only_true_paid_cosine_head_energy_lower_subtracted":True,
            "unobserved_low_sine_energy_not_subtracted":True,
            "rotation_used_only_for_commuting_high_projection_norm":True,
            "every_dependent_scalar_uses_whole_formal_readback":True,
            "old_pairings_or_trials_recomputed":False,"actual_rotated_signed_entries_proved":False,
            "complete_high_inverse_or_full_nu_Schur_proved":False,"topic_completion_proved":False}
        state["complete"] = state["proved"] = True;state["actual_returncode"] = 0
        state["stage"] = "complete_"+STAGE+"_scalar_branch";save();return 0
    except BaseException as exc:
        state["complete"] = state["proved"] = False;state["actual_returncode"] = 1
        state["failure"] = {"type":type(exc).__name__,"message":str(exc)[:2000],"traceback":traceback.format_exc()[-6000:]}
        state["stage"] = "failed_with_actual_complete_prefix_retained"
        state["wall_seconds"] = time.perf_counter()-started;atomic(args.output,canonical(state));traceback.print_exc();return 1


if __name__ == "__main__":
    sys.exit(main())
