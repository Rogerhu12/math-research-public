"""PO: new even96 observation inverse for the original physical nu column.

Complete NP/NH/JC/RW outcomes are mandatory.  Only the exact necessary RW
carriers are rematerialized; old targets and NP trial/pairings never rerun.
"""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, os, platform
from pathlib import Path
import sys, tempfile, time, traceback

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_physical_nu_observation_inverse_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_physical_nu_observation_inverse_math.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_physical_nu_observation_inverse_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_physical_nu_observation_inverse_manifest.py"
PROOF = TOPIC+"/results/R147-supplement-observation-inverse-for-physical-parameter-tail.md"
NH_MANIFEST = TOPIC+"/notes/2026-11-27-strict-nu-high-forcing-inputs.json"
NH_BASE = TOPIC+"/notes/strict_nu_high_forcing_ci/run-45897599620-1"
NW_EXECUTION = TOPIC+"/notes/cohomological_normalizer_windows_sign_ci/run-43775614821-1/execution.json"
NW_SHA = "1e327e83dafb5d09ec98acc6ba887ae28962a7f242be7e82692a864c2f93cb0b"
WBP_PROOF = TOPIC+"/results/R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md"
KIND = "R147_complete_physical_nu_observation_inverse_v1"
STAGE = "complete_physical_nu_observation_inverse"
MANIFEST_KIND = "R147_complete_physical_nu_observation_inverse_inputs_v1"
RUNTIME = {"python":"3.12.14","packages":{"python-flint":"0.9.0"}}
PARAMETERS = {
    "arithmetic_bits":320,"decimal_record_digits":60,"private_carrier_digits":80,
    "maximum_scientific_wall_seconds":1800,"row_modes":96,"grid_points":4096,
    "complete_original_RW_fourier_cutoff":1024,"trial_recovered_degree":96,
    "recovered_subspace":"even nonmean physical half-sum primitive only",
    "true_unknown_remains_full_Fourier":True,"physical_frequency_factor":4,
    "physical_period":"pi/2","normalized_angular_measure":True,
    "translation_removed":"mean(H-Id), not H(0)",
    "original_conjugacy_strip":"1/128","original_selected_run":"43588332723/1",
    "original_selected_loss":"1/250","fixed_original_waist_normalizer_cutoff":268435456,
    "same_complete_high_index":"2^4608","new_complete_scalar_records":12,
    "complete_NP_true_observations":194,"complete_NP_raw_signed_trial_observations":192,
    "both_independent_physical_means_retained":True,"old_scientific_targets_recomputed":False,
    "old_carriers_restored_only_as_necessary_exact_inputs":True,
}
TARGETS = [
    "complete_RW_even96_inverse_identity_defect_upper",
    "complete_RW_even96_inverse_L2_upper",
    "complete_NP_even_physical_trial_reconstruction_radius_upper",
    "complete_NP_even_physical_trial_L2_upper",
    "complete_NP_even_physical_trial_angle_derivative_L2_upper",
    "same_true_H_mean_translation_removed_displacement_upper",
    "complete_NP_physical_trial_true_angle_high97_upper",
    "complete_true_NP_physical_primitive_L2_upper",
    "complete_true_NP_physical_high97_upper",
    "complete_true_NP_target_normalized_physical_L2_upper",
    "complete_true_NP_target_normalized_physical_highJ_upper",
    "complete_true_NP_physical_cosine96_error_upper",
]
SCI_FIELDS = sorted([
    "identity","parameters","runtime","complete","proved","actual_returncode","failure","stage",
    "completed_targets","current_target","candidate_record","new_records","saved_record_count",
    "whole_completed_inputs","reference_identity","selected_member_identity","copied_prior_scalar_records",
    "necessary_old_carrier_receipts","private_new_inverse_receipt","result",
    "old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases","wall_seconds",
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
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def atomic(path,raw):
    path = Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    candidate = path.with_name(path.name+".candidate")
    with candidate.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.replace(candidate,path)


def gather(root,nh_actual,nh_execution,nh_manifest=NH_MANIFEST):
    """Whole readonly existing conclusions and exact original definitions."""
    root = Path(root);current,roles = {},{}
    def add(role,path,expected=None):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,"safe complete topic input")
        raw = (root/path).read_bytes();raw.decode()
        require(0 < len(raw) < 100000,"whole small current object: "+path)
        if path.endswith(".py"):
            ast.parse(raw.decode(),filename=path)
        item = {"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if expected is not None:
            require(all(item[key] == expected[key] for key in ("path","bytes","sha256","git_blob_sha")),
                    "whole unchanged original input: "+role)
        current.setdefault(path,item);roles[role] = path
        return parse(raw) if path.endswith(".json") else raw
    nhm = add("NH_manifest",nh_manifest)
    reviewed = next(x for x in nhm["files"] if x["role"] == "reviewed_rules")
    add("reviewed_rules",reviewed["path"],reviewed)
    for item in nhm["files"]:
        add("NH_"+item["role"],item["path"],item)
    add("NH_actual",nh_actual);add("NH_execution",nh_execution)
    npm = parse((root/nhm["roles"]["NP_manifest"]).read_bytes())
    for role in ("RW_actual","RW_execution"):
        item = next(x for x in npm["files"] if x["role"] == role)
        add(role,item["path"],item)
    for role,path in (("NW_execution",NW_EXECUTION),("original_B_proof",WBP_PROOF),
        ("science",SOURCE),("observation_math",MATH),("worker",WORKER),("generator",GENERATOR),("proof",PROOF)):
        add(role,path)
    history = []
    for item in nhm["historical_inputs"]:
        item = dict(item,role="NH_"+item["role"])
        history.append(item);roles[item["role"]] = item["path"]
    require(len(history) == 4 and len({x["path"] for x in history+list(current.values())})
            == len(history)+len(current),"all and only four original native definitions, distinct from current inputs")
    return {"files":sorted(current.values(),key=lambda x:x["role"]),"historical_inputs":history,"roles":roles}


def admit(manifest,raws,paths):
    """No numerical imports: actual complete outcomes and their entire objects."""
    roles = manifest["roles"]
    def raw(role):return raws[roles[role]]
    nhm = parse(raw("NH_manifest"))
    nh_owner = load(paths[roles["NH_science"]],"_PO_complete_NH_admission")
    prior = nh_owner.admit(nhm,raws,paths)
    nh,nhe = parse(raw("NH_actual")),parse(raw("NH_execution"))
    nh_specs = {x["role"]:x for x in nhm["files"]}
    require(nh["complete"] is nh["proved"] is nhe["complete"] is True
        and nh["actual_returncode"] == nhe["actual_child_returncode"] == 0
        and nh["failure"] is nhe["failure"] is None
        and nh["identity"]["kind"] == nh_owner.KIND
        and nh["identity"]["manifest_sha256"] == sha(raw("NH_manifest"))
        and nh["identity"]["source_sha256"] == nh_specs["science"]["sha256"]
        and nh["identity"]["run_id"] == nhe["run_id"] == "45897599620"
        and nh["identity"]["run_attempt"] == nhe["run_attempt"] == "1"
        and nh["parameters"] == nhm["parameters"] == nh_owner.PARAMETERS
        and nh["completed_targets"] == nh_owner.TARGETS and nh["saved_record_count"] == 12
        and set(nh["new_records"]) == set(nh_owner.TARGETS)
        and sorted(nh) == nhm["allowed_scientific_fields"]
        and nh["candidate_record"] is nh["current_target"] is None
        and nh["copied_prior_scalar_records"] == prior["old_bounds"]
        and nh["reference_identity"] == prior["NP"]["reference_identity"]
        and nh["selected_member_identity"] == prior["NP"]["selected_member_identity"]
        and nhe["scientific_files"] == [{"path":roles["NH_actual"],"bytes":len(raw("NH_actual")),
                                        "sha256":sha(raw("NH_actual"))}],
        "one whole genuinely completed NH12, from the same entire NP/JC predecessors")
    for key in ("whole_true_paired_high97_forcing_proved","all_high_modes_and_two_means_retained",
                "mean_leakage_uses_original_full_Wiener_derivative",
                "Jacobian_lower_includes_same_true_H_endpoint",
                "only_true_paid_cosine_head_energy_lower_subtracted",
                "unobserved_low_sine_energy_not_subtracted"):
        require(nh["result"][key] is True,"complete NH mathematical qualification: "+key)
    # The old metadata admission returns the exact finite H/K coefficients
    # needed as numerical INPUTS.  It evaluates no old norm or row target.
    jcm = parse(raws[nhm["roles"]["JC_manifest"]])
    jc_specs = {x["role"]:x for x in jcm["files"]+jcm["historical_inputs"]}
    jc_owner = load(paths[nhm["roles"]["JC_science"]],"_PO_necessary_RW_definitions")
    rw,unused_records = jc_owner.admit_complete_inputs(
        {key:raws[item["path"]] for key,item in jc_specs.items()},jc_specs)
    rwa,rwe = parse(raw("RW_actual")),parse(raw("RW_execution"))
    rwm = parse(raws[jc_specs["RW_manifest"]["path"]])
    require(rwa["complete"] is rwa["proved"] is rwe["complete"] is True
        and rwa["actual_returncode"] == rwe["actual_child_returncode"] == 0
        and rwa["failure"] is rwe["failure"] is None
        and rwa["completed_targets"] == ["row_%03d"%j for j in range(1,97)]
        and set(rwa["new_records"]) == set(rwa["completed_targets"])
        and rwa["saved_record_count"] == rwa["private_complete_row_count"] == 96
        and rwa["identity"]["run_id"] == rwe["run_id"] == "45787309600"
        and rwa["identity"]["manifest_sha256"] == sha(raws[jc_specs["RW_manifest"]["path"]])
        and rwa["parameters"] == rwm["parameters"]
        and rwa["reference_identity"] == rw["family"] == prior["NP"]["reference_identity"]
        and rwe["scientific_files"] == [{"path":roles["RW_actual"],"bytes":len(raw("RW_actual")),
                                         "sha256":sha(raw("RW_actual"))}],
        "the complete same original RW96 outcome, including all necessary private carrier receipts")
    require(rwa["result"]["exact_trial_is_original_DFT_not_a_midpoint"] is True
        and rwa["result"]["whole_private_grid_and_rows_saved_and_read_back"] is True,
        "exact finite input definitions, not arbitrary enclosure centers")
    nw = parse(raw("NW_execution"));nwa = nw["actual_scientific_receipt"]
    require(sha(raw("NW_execution")) == NW_SHA
        and nw["complete"] is nwa["complete"] is nwa["proved"] is True
        and nw["actual_returncode"] == nwa["actual_returncode"] == 0
        and nw["actual_failure"] is nwa["failure"] is None
        and nw["run_id"] == nwa["run_id"] == "43775614821"
        and nwa["gates"] and all(x["passed"] is True for x in nwa["gates"]),
        "whole original NW same-normalizer successful execution")
    fourier = nwa["complete_new_Fourier_budgets_conclusion"]
    for key in ("V_budgets_bound_v_W_budgets_bound_w_P_budgets_bound_p",
                "bounds_are_direct_series_inequalities_not_inversion_of_operator_norms",
                "full_infinite_two_sign_series_included","same_selected_bounded15_rotation"):
        require(fourier[key] is True,"complete same-coefficient NW qualification: "+key)
    bounds = dict(prior["old_bounds"],**{key:fourier["complete_Wiener_bounds"][key]
                                       for key in ("W0","Wone_third")})
    require(not any(name in sys.modules for name in ("flint","numpy","scipy")),
            "whole admission contains no scientific computation")
    return dict(prior,NH=nh,RW=rw,RW_actual=rwa,RW_math_path=jc_specs["row_math"]["path"],
                old_bounds=bounds,NH_records=nh["new_records"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-map","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--checkout",required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1","one new authorized public observation inverse")
    manifest_raw = args.manifest.read_bytes();manifest = parse(manifest_raw)
    require(sha(manifest_raw) == args.manifest_sha and manifest["kind"] == MANIFEST_KIND
        and manifest["scientific_kind"] == KIND and manifest["stage"] == STAGE
        and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
        and manifest["target_order"] == TARGETS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
        "the complete new observation inverse contract")
    specs = manifest["files"]+manifest["historical_inputs"]
    input_map = parse(args.input_map.read_bytes())
    require(set(input_map) == {x["role"] for x in specs},"every complete immutable input")
    raws,paths = {},{}
    for item in specs:
        path = Path(input_map[item["role"]]);raw = path.read_bytes()
        require(len(raw) == item["bytes"] and sha(raw) == item["sha256"],"entire pinned input")
        raws[item["path"]],paths[item["path"]] = raw,path
    require(sha(Path(__file__).read_bytes()) == next(x["sha256"] for x in specs if x["role"] == "science"),
            "the entire actual running source")
    sys.dont_write_bytecode = True;prior = admit(manifest,raws,paths)
    require(not args.output.exists(),"never overwrite a true accepted prefix")
    state = {"identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
        "source_sha256":sha(Path(__file__).read_bytes()),"run_id":os.environ["GITHUB_RUN_ID"],
        "run_attempt":"1","event_commit":os.environ["GITHUB_SHA"],"actual_checkout_commit":args.checkout,
        "arithmetic_bits":320},"parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,
        "actual_returncode":None,"failure":None,"stage":"complete_actual_NP_NH_JC_RW_NW_inputs_admitted",
        "completed_targets":[],"current_target":None,"candidate_record":None,"new_records":{},"saved_record_count":0,
        "whole_completed_inputs":{"all_input_descriptors_sha256":sha(canonical(specs)),
            "current_objects":len(manifest["files"]),"historical_objects":4,
            "NP_all194_true_and192_raw_signed_balls_read":True,"NH_all12_and_JC_all7_records_read":True,
            "RW_all96_rows_and_carrier_definitions_read":True,"NW_entire_execution_read":True},
        "reference_identity":prior["NP"]["reference_identity"],
        "selected_member_identity":prior["NP"]["selected_member_identity"],
        "copied_prior_scalar_records":{"original_bounds":prior["old_bounds"],"NH_all12":prior["NH_records"]},
        "necessary_old_carrier_receipts":{"complete_grid":False,"complete_rows":0,
            "original_RW_definition_sha256":prior["RW_actual"]["definition_sha256"]},
        "private_new_inverse_receipt":None,"result":None,
        "old_scientific_target_calls":0,"new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"wall_seconds":0.0}
    require(sorted(state) == SCI_FIELDS,"the complete scientific envelope")
    started = time.perf_counter()
    def save():
        state["wall_seconds"] = time.perf_counter()-started
        require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],"new inverse time budget")
        raw = canonical(state)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],"whole small public conclusion")
        atomic(args.output,raw)
    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),"packages":{"python-flint":version("python-flint")}}
        require(runtime == RUNTIME,"the complete fixed directed runtime")
        state["runtime"] = runtime;flint.ctx.prec = 320;arb = flint.arb
        def ball(record):
            value = arb(record["ball"])
            if "lower" in record and "upper" in record:
                value = value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite(),"whole finite original scalar or signed observation")
            return value
        def publish(name,value,direction):
            require(name == TARGETS[state["saved_record_count"]] and direction == "upper",
                    "the next complete new upper bound")
            point = value.upper()
            require(point.is_finite() and point >= 0,"finite nonnegative complete bound")
            record = {"ball":point.str(PARAMETERS["decimal_record_digits"]),"bound":"upper"}
            require(arb(record["ball"]).contains(point),"the whole stored ball contains its directed bound")
            state["current_target"] = name;state["candidate_record"] = {"name":name,"record":record};save()
            require(parse(args.output.read_bytes())["candidate_record"] == state["candidate_record"],
                    "complete candidate readback")
            state["new_records"][name] = record;state["completed_targets"].append(name)
            state["saved_record_count"] += 1;state["current_target"] = state["candidate_record"] = None;save()
            return ball(parse(args.output.read_bytes())["new_records"][name]).upper()
        rw_math = load(paths[prior["RW_math_path"]],"_PO_necessary_exact_RW_carrier_inputs")
        rw,actual = prior["RW"],prior["RW_actual"]
        factory = rw_math.ReflectedRowFactory(flint,rw["H_sines"],rw["H_cosines"],rw["K_sines"],rw["K_cosines"],
            H_constant=rw["zero_translation_qualification"]["H_constant"],
            K_constant=rw["zero_translation_qualification"]["K_constant"])
        def same_carrier(kind,values,extra,expected):
            values = list(values)
            document = {"kind":kind,"definition_sha256":actual["definition_sha256"],**extra,
                        "all_real_balls":[x.str(PARAMETERS["private_carrier_digits"]) for x in values]}
            raw = canonical(document)
            require(len(raw) == expected["bytes"] and sha(raw) == expected["sha256"]
                and len(values) == expected["complete_real_count"],"the same whole necessary original RW carrier")
            return [arb(x) for x in parse(raw)["all_real_balls"]]
        grid = same_carrier("R149_complete_exact_compound_cosine_grid_carrier_v1",
            factory.materialize_whole_compound_grid(),{"grid_points":4096},actual["private_grid_receipt"])
        factory.base_cosines,factory.previous,factory.current = grid,[arb(1) for _ in grid],list(grid)
        state["necessary_old_carrier_receipts"]["complete_grid"] = True
        state["stage"] = "restoring_only_necessary_exact_RW_input_carriers";save()
        rows = {}
        for index in range(1,97):
            j,coefficients = factory.next_complete_row();require(j == index,"all complete original rows in order")
            name = "row_%03d"%j
            rows[name] = same_carrier("R149_complete_exact_DFT_real_row_carrier_v1",coefficients,
                {"mode":j,"nonnegative_modes":[0,1024],
                 "negative_modes":"equal by exact evenness, not selected by midpoint"},actual["new_records"][name]["carrier"])
            state["necessary_old_carrier_receipts"]["complete_rows"] = j
            if j%16 == 0:
                save();print(json.dumps({"stage":state["stage"],"whole_rows":j,"old_scientific_targets":0}),flush=True)
        state["stage"] = "new_full96_physical_observation_inverse";save()
        math = load(paths[manifest["roles"]["observation_math"]],"_PO_new_inverse_and_whole_physical_tail")
        require(list(math.OUTPUT_ORDER) == TARGETS,"complete new output order")
        with tempfile.TemporaryDirectory(prefix="private-complete-PO-") as private:
            def retain(matrix,inverse,coefficients):
                def array(value):
                    return [[value[i,j].str(PARAMETERS["private_carrier_digits"])
                             for j in range(value.ncols())] for i in range(value.nrows())]
                document = {"kind":"R147_complete_new_even96_observation_inverse_enclosure_v1",
                    "matrix":array(matrix),"inverse":array(inverse),"coefficients":array(coefficients)}
                raw = canonical(document);path = Path(private)/"complete-new-inverse.json";atomic(path,raw)
                reread = path.read_bytes();require(reread == raw,"complete private inverse readback")
                restored = parse(reread)
                values = [arb(row[0]) for row in restored["coefficients"]]
                require(all(values[i].contains(coefficients[i,0]) for i in range(96)),
                        "all recovered signed coefficients retained as entire intervals")
                state["private_new_inverse_receipt"] = {"kind":document["kind"],"bytes":len(raw),"sha256":sha(raw),
                    "matrix_shape":[96,96],"inverse_shape":[96,96],"coefficient_shape":[96,1],
                    "complete_readback":True,"arrays_published":False};save()
                return values
            observations = {"row_%03d"%j:ball(prior["raw_pairings"]["original_physical_primitive96"]["row_%03d"%j])
                            for j in range(1,97)}
            math.complete_observation_inverse(flint,rows,observations,
                {key:ball(value) for key,value in prior["old_bounds"].items()},
                {key:ball(value) for key,value in prior["NH_records"].items()},publish,retain)
        state["result"] = {"kind":KIND,"complete_new_record_count":12,"complete_new_record_order":list(TARGETS),
            "complete_even96_observation_inverse_proved":True,"original_uninflated_whole_NP_pairings_used":True,
            "only_actual_even_nonmean_physical_trial_reconstructed":True,
            "mean_translation_not_H_zero_value_removed":True,"same_true_H_full_Wiener_and_Jacobian_used":True,
            "complete_infinite_physical_tail_and_PDE_error_paid":True,"both_independent_density_means_retained":True,
            "same_sign_original_target_B_and_same_high_index_retained":True,
            "every_dependent_scalar_uses_whole_formal_readback":True,
            "old_pairings_or_trials_or_norm_targets_recomputed":False,"unobserved_h2_sine_phase_or_amplitude_recovered":False,
            "actual_rotated_signed_entries_proved":False,"complete_high_inverse_or_full_nu_Schur_proved":False,
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

