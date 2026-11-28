"""Complete PWA96 scalar consumer; admission is metadata-only, science is new.

Only complete actual H96, P96 and APHI publications are admitted.  Their whole
original public validators are applied without invoking any original owner,
carrier, integrator or numerical target.  Importing this file performs no science.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, os, platform, sys, time, traceback
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_pwa_height_phase_saved_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_pwa_height_phase_saved_math.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_pwa_height_phase_saved_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_pwa_height_phase_saved_manifest.py"
PROOF = TOPIC+"/results/R149-supplement-PWA-height-row-and-common-ratio-phase-consumer.md"
BASE_WORKER = TOPIC+"/scripts/fourfold_codazzi_physical_chain_public_worker.py"
KIND = "R149_complete_PWA_height_and_common_ratio_phase_rows_v1"
MANIFEST_KIND = "R149_complete_PWA_height_and_common_ratio_phase_rows_inputs_v1"
STAGE = "complete_PWA_height_and_common_ratio_phase_rows"
RUNTIME = {"python":"3.12.14", "packages":{"python-flint":"0.9.0"}}
TARGETS = ["complete_PWA_actual_cap_height_row96", "complete_PWA_actual_cap_height_joint_radius",
    "complete_same_strict_particular_phase_over_height_ratio", "complete_PWA_height_reduced_phase_row96",
    "complete_PWA_height_reduced_phase_joint_radius", "complete_PWA_reduced_phase_original_negative_receiver4",
    "complete_PWA_reduced_phase_independent_world_receiver2"]
COUNTS = [96,1,1,96,1,4,2]
SIGNED, CENTRED = (0,2,3), (0,3)
PARAMETERS = {"arithmetic_bits":320, "decimal_record_digits":60, "new_complete_targets":7,
    "result_kind":KIND, "reference_vertical_covector_error":"108627/1000000000",
    "reference_world_position_error":"232743/1000000000",
    "PWA_actual_cap_frame_distance":"3649/1000000000",
    "PWA_actual_cap_position_distance":"107/12500000",
    "complete_height_state_receiver_factor":"11367/800", "relative_position_norm_upper":"171/250",
    "PWA_strict_height_interval":["-12685187/500000000","-12614813/500000000"],
    "complete_PRN_negative_receiver4":["2600","184","69","245"],
    "complete_PWA_height_negative_receiver4":["94013","6651","3001","8852"],
    "complete_height_world_receiver2":["27/8","4617/2000"],
    "negative_receiver_order":["D_star_plus_J_minus","F_minus","F_strict","J_strict"],
    "world_receiver_order":["vertical_world_Yb_L2","world_axial_Kb_L2"],
    "physical_frequency_factor":4, "normalized_angular_measure":True,
    "ordinary_radial_dr_and_both_means_retained":True,
    "same_selected_member_not_a_mean_exact_replacement":True,
    "automatic_scientific_retry":False, "old_scientific_targets_recomputed":False}
SCI_FIELDS = sorted(["identity","parameters","runtime","complete","proved","actual_returncode",
    "failure","stage","completed_targets","current_target","candidate_record","new_records",
    "saved_record_count","whole_completed_inputs","reference_identity","selected_member_identity",
    "whole_prior_record_sources","complete_original_TC_arrays","complete_original_NP_arrays",
    "phase_ratio_exact_dyadic_centre","result","old_scientific_target_calls",
    "new_arrays_published","new_artifacts","new_Releases","wall_seconds"])
PREDECESSORS = {
    "H96": {"manifest":TOPIC+"/notes/2026-11-28-finite-trial-height-complete-inputs.json",
        "validator":TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_public_worker.py",
        "validator_sha":"1f98010b06299e843bea939f4a14974aec50b0e0db970edae5b6b836a8e1e8fd",
        "execution_kind":"R149_complete_original_finite_trial_height_rows_execution_v1","count":7},
    "P96": {"manifest":TOPIC+"/notes/2026-11-27-finite-trial-phase-complete-inputs.json",
        "actual":TOPIC+"/notes/finite_trial_phase_ci/run-45926971089-1/actual-finite-trial-phase.json",
        "execution":TOPIC+"/notes/finite_trial_phase_ci/run-45926971089-1/execution.json",
        "validator":TOPIC+"/scripts/fourfold_codazzi_finite_trial_phase_public_worker.py",
        "validator_sha":"a9b24b7b979d6701428255ffeffcfb67b0aad5a399519cfc2d8e192ade17ec4a",
        "execution_kind":"R149_complete_original_finite_trial_phase_execution_v1","count":6},
    "APHI": {"manifest":TOPIC+"/notes/2026-11-27-strict-nu-phase-after-45914123725-inputs.json",
        "actual":TOPIC+"/notes/strict_nu_phase_ci/run-45915169627-1/actual-strict-nu-phase.json",
        "execution":TOPIC+"/notes/strict_nu_phase_ci/run-45915169627-1/execution.json",
        "validator":TOPIC+"/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py",
        "validator_sha":"32569d72195ed7640bd47d2d6e1690d299e1636fb93365dea4855e28432f0eef",
        "execution_kind":"R147_complete_strict_nu_nonlocal_phase_execution_v1","count":6}}
TRUE_FLAGS = ["same_original_selected_member_and_all96_TC_coordinates","same_unnormalized_true_strict_particular",
    "all_four_TC_and_all_four_NP_original_array_identities_retained",
    "whole_canonical_height_G_H_phase_and_APHI_records_used","full_g_f0_and_both_moving_means_retained",
    "same_exact_dyadic_centres_and_complete_joint_radii","common_rho_joint_phase_error_uses_whole_saved_readbacks",
    "original_negative_windows_root_means_and_impulses_retained",
    "independent_Yb_Kb_geometric_impulses_and_raw_phase_ports_retained"]
FALSE_FLAGS = ["new_height_or_phase_integrals_evaluated","old_scientific_targets_recomputed",
    "old_upper_subtotals_subtracted","true_PDE_corrected_columns_proved","actual_cap_input_admissibility_proved",
    "full_regular_Theta_or_Schur_inverse_proved","topic_completion_proved"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def safe(path):
    require(isinstance(path,str) and path.startswith(TOPIC+"/")
            and all(x not in ("",".","..") for x in path.split("/")), "whole safe topic input")
    return path


def atomic(path, raw):
    path = Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    temp = path.with_name(path.name+".candidate")
    with temp.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temp,path)


def gather(root, height_actual, height_execution):
    """Read whole already-completed small files; never expand any old native plan."""
    root = Path(root); files, roles = {}, {}
    def add(role,path,expected=None):
        path = safe(path); raw=(root/path).read_bytes(); raw.decode()
        require(0<len(raw)<100000,"one whole small current file: "+role)
        if path.endswith(".py"):
            ast.parse(raw.decode(),filename=path)
        item={"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
              "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if expected:
            require(all(item[k]==expected[k] for k in ("path","bytes","sha256","git_blob_sha")),
                    "the immutable whole predecessor source: "+role)
        if path in files:
            require(all(files[path][k]==item[k] for k in ("bytes","sha256","git_blob_sha")),
                    "same whole aliased input")
        files.setdefault(path,item); roles[role]=path
    for name,spec in PREDECESSORS.items():
        add(name+"_manifest",spec["manifest"])
        old=parse((root/spec["manifest"]).read_bytes())
        source=next(item for item in old["files"] if item["role"]=="science")
        add(name+"_source",source["path"],source)
        add(name+"_validator",spec["validator"])
        add(name+"_actual",height_actual if name=="H96" else spec["actual"])
        add(name+"_execution",height_execution if name=="H96" else spec["execution"])
    old=parse((root/PREDECESSORS["H96"]["manifest"]).read_bytes())
    review=next(item for item in old["files"] if item["role"]=="reviewed_rules")
    add("reviewed_rules",review["path"],review)
    for role,path in [("science",SOURCE),("saved_math",MATH),("worker",WORKER),
        ("generator",GENERATOR),("proof",PROOF),("base_worker",BASE_WORKER),
        ("PWA_proof",TOPIC+"/results/R147-supplement-physical-angle-cap-GW-and-small-vertical-world-anchors.md"),
        ("HP_proof",TOPIC+"/results/R147-supplement-actual-height-pivot-and-complete-phase-mean-transfer.md"),
        ("PRN_proof",TOPIC+"/results/R149-supplement-complete-phase-receiver-in-original-negative-source-windows.md")]:
        add(role,path)
    return {"files":sorted(files.values(),key=lambda x:x["role"]),"historical_inputs":[],"roles":roles}


def admit(manifest, raws):
    """Validate complete envelopes/identities with only the standard library."""
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),
            "whole input admission precedes numerical imports")
    roles=manifest["roles"]; admitted={}
    for name,spec in PREDECESSORS.items():
        mraw=raws[roles[name+"_manifest"]]; old=parse(mraw)
        araw=raws[roles[name+"_actual"]]; actual=parse(araw)
        execution=parse(raws[roles[name+"_execution"]])
        by_role={item["role"]:item for item in old["files"]}
        require(sha(raws[roles[name+"_source"]])==by_role["science"]["sha256"]
            and sha(raws[roles[name+"_validator"]])==spec["validator_sha"],
            "entire frozen original owner and original public validator: "+name)
        tree=ast.parse(raws[roles[name+"_validator"]].decode())
        texts=[ast.literal_eval(node.value) for node in tree.body if isinstance(node,ast.Assign)
               and len(node.targets)==1 and isinstance(node.targets[0],ast.Name)
               and node.targets[0].id=="VALIDATOR"]
        require(len(texts)==1,"one complete original public validator")
        env={"require":require,"parse":parse,"op":old["operation"],"manifest":old,
             "args":SimpleNamespace(manifest_sha=sha(mraw)),"by_role":by_role,
             "run":execution["run_id"],"attempt":execution["run_attempt"]}
        exec(compile(texts[0],"<whole "+name+" original output validator>","exec"),env)
        require(env["validate_output"](araw)==actual,"whole original result validation")
        ident=actual["identity"]
        require(actual["complete"] is actual["proved"] is execution["complete"] is True
            and actual["actual_returncode"]==execution["actual_child_returncode"]==0
            and actual["failure"] is execution["failure"] is None
            and execution["kind"]==spec["execution_kind"]
            and execution["repository"]==REPO and execution["problem_id"]==old["problem_id"]
            and execution["manifest_sha256"]==ident["manifest_sha256"]==sha(mraw)
            and execution["actual_scientific_checkout"]==ident["actual_checkout_commit"]
            and execution["event_commit"]==ident["event_commit"]
            and execution["run_id"]==ident["run_id"] and execution["run_attempt"]==ident["run_attempt"]=="1"
            and execution["current_input_receipts"]==old["files"]
            and execution["scientific_children"]==1 and execution["child_timeout"] is False
            and execution["actual_runtime"]==old["runtime"]
            and actual["runtime"]=={**old["runtime"],"OPENBLAS_CORETYPE":"Haswell"}
            and execution["completed_new_scalar_targets"]==actual["saved_record_count"]==spec["count"]
            and execution["complete_new_response_target_set"] is execution["original_scientific_complete"] is True
            and execution["original_scientific_failure"] is None
            and all(execution[key]==0 for key in ("old_completed_targets_recomputed",
                "old_numerical_producers_called","new_arrays_published","new_artifacts","new_Releases"))
            and execution["scientific_files"]==[{"path":roles[name+"_actual"],
                "bytes":len(araw),"sha256":sha(araw)}],
            "complete successful actual predecessor, full execution and whole file SHA: "+name)
        admitted[name]=actual
    h,p,a=(admitted[name] for name in ("H96","P96","APHI"))
    require(h["selected_member_identity"]==p["selected_member_identity"]==a["selected_member_identity"]
        and h["reference_identity"]==p["reference_identity"]==a["reference_identity"],
        "one identical selected family, eta, nu and original phase convention")
    tc=h["necessary_original_trial_receipts"]["complete_original_arrays"]
    np=h["necessary_original_NP_receipts"]["complete_original_array_receipts"]
    require(tc==p["necessary_original_trial_receipts"]["complete_original_arrays"]
        and np==a["necessary_original_trial_receipts"]["complete_original_array_receipts"]
        and h["necessary_original_NP_receipts"]["complete_original_trial_definition_sha256"]
            ==a["necessary_original_trial_receipts"]["complete_original_trial_definition_sha256"]
        and h["whole_prior_record_sources"]["P96_actual"]=={
            "path":roles["P96_actual"],"sha256":sha(raws[roles["P96_actual"]]),
            "complete_targets":p["completed_targets"]},
        "all four full original TC and NP array identities and whole original P96 source")
    require(len(tc)==len(np)==4,"all input coordinates and strict particular arrays")
    admitted["TC_arrays"],admitted["NP_arrays"]=tc,np
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),"metadata admission only")
    return admitted


def validate_output(raw, manifest, manifest_sha, source_sha, run, attempt):
    require(0<len(raw)<=manifest["operation"]["maximum_scientific_bytes"],"complete PWA96 output")
    doc=parse(raw); ident=doc["identity"]; count=doc["saved_record_count"]
    require(sorted(doc)==SCI_FIELDS==manifest["allowed_scientific_fields"]
        and doc["parameters"]==PARAMETERS==manifest["parameters"]
        and ident["kind"]==KIND==manifest["scientific_kind"]
        and ident["scalar_stage"]==STAGE==manifest["stage"]
        and ident["manifest_sha256"]==manifest_sha and ident["source_sha256"]==source_sha
        and ident["run_id"]==run and ident["run_attempt"]==attempt
        and ident["arithmetic_bits"]==320 and type(count) is int and 0<=count<=7
        and doc["completed_targets"]==TARGETS[:count] and set(doc["new_records"])==set(TARGETS[:count])
        and all(doc[key]==0 for key in ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
        "entire immutable new target identity and genuine complete prefix")
    for i,name in enumerate(TARGETS[:count]):
        item=doc["new_records"][name]
        keys={"complete_count","bound","balls"}|({"exact_dyadic_centres"} if i in CENTRED else set())
        require(set(item)==keys and item["complete_count"]==COUNTS[i]
            and item["bound"]==("signed_enclosure" if i in SIGNED else "upper")
            and len(item["balls"])==COUNTS[i] and all(isinstance(x,str) for x in item["balls"]),
            "whole complete original coordinates and scalar receivers")
        if i in CENTRED:
            centres=item["exact_dyadic_centres"]
            require(len(centres)==96 and all(isinstance(x,str) and F(x).denominator&(F(x).denominator-1)==0
                                           for x in centres),"all96 exact dyadic centres")
    if doc["complete"]:
        result=doc["result"]
        require(count==7 and doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"]==0 and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"]=="complete_"+STAGE+"_scalar_branch" and doc["runtime"]==RUNTIME
            and result["kind"]==KIND and result["complete_new_target_count"]==7
            and result["complete_new_target_order"]==TARGETS
            and all(result[x] is True for x in TRUE_FLAGS) and all(result[x] is False for x in FALSE_FLAGS)
            and len(doc["complete_original_TC_arrays"])==len(doc["complete_original_NP_arrays"])==4,
            "all seven complete new mathematical outputs with original unpaid ports retained")
        r=F(doc["phase_ratio_exact_dyadic_centre"])
        require(r<0 and r.denominator&(r.denominator-1)==0,"one exact shared dyadic ratio centre")
    return doc


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("manifest","input-map","output"):
        parser.add_argument("--"+key,required=True,type=Path)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--checkout",required=True)
    args=parser.parse_args();sys.dont_write_bytecode=True
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one first authorized public PWA96 scalar target")
    mr=args.manifest.read_bytes();manifest=parse(mr)
    require(sha(mr)==args.manifest_sha and manifest["kind"]==MANIFEST_KIND
        and manifest["parameters"]==PARAMETERS and manifest["runtime"]==RUNTIME
        and manifest["target_order"]==TARGETS and manifest["historical_inputs"]==[],"whole new scalar-only contract")
    inputs=parse(args.input_map.read_bytes());specs=manifest["files"]
    require(set(inputs)=={x["role"] for x in specs},"all and only whole declared small inputs")
    raws,paths={},{}
    for spec in specs:
        p=Path(inputs[spec["role"]]);raw=p.read_bytes()
        require(len(raw)==spec["bytes"] and sha(raw)==spec["sha256"],"whole original file: "+spec["role"])
        raws[spec["path"]],paths[spec["path"]]=raw,p
    source_sha=sha(Path(__file__).read_bytes())
    require(source_sha==next(x["sha256"] for x in specs if x["role"]=="science"),"entire running owner")
    admitted=admit(manifest,raws);roles=manifest["roles"]
    require(not args.output.exists(),"no replay or overwrite of a genuine scientific prefix")
    state={"identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
        "source_sha256":source_sha,"run_id":os.environ["GITHUB_RUN_ID"],"run_attempt":"1",
        "event_commit":os.environ["GITHUB_SHA"],"actual_checkout_commit":args.checkout,"arithmetic_bits":320},
        "parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,"actual_returncode":None,
        "failure":None,"stage":"whole_PWA96_inputs_admitted","completed_targets":[],"current_target":None,
        "candidate_record":None,"new_records":{},"saved_record_count":0,
        "whole_completed_inputs":{"inventory_sha256":sha(encode(specs)),"current_files":len(specs),
            "historical_files":0,"new_or_old_carrier_materializations":0},
        "reference_identity":admitted["H96"]["reference_identity"],
        "selected_member_identity":admitted["H96"]["selected_member_identity"],
        "whole_prior_record_sources":{name:{"path":roles[name+"_actual"],
            "bytes":len(raws[roles[name+"_actual"]]),"sha256":sha(raws[roles[name+"_actual"]]),
            "completed_targets":admitted[name]["completed_targets"]} for name in PREDECESSORS},
        "complete_original_TC_arrays":admitted["TC_arrays"],"complete_original_NP_arrays":admitted["NP_arrays"],
        "phase_ratio_exact_dyadic_centre":None,"result":None,"old_scientific_target_calls":0,
        "new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"wall_seconds":0.}
    began=time.perf_counter()
    def save():
        state["wall_seconds"]=time.perf_counter()-began
        raw=encode(state);require(len(raw)<=manifest["operation"]["maximum_scientific_bytes"],"whole small output")
        atomic(args.output,raw)
    save()
    try:
        from importlib.metadata import version
        import flint
        state["runtime"]={"python":platform.python_version(),"packages":{"python-flint":version("python-flint")}}
        require(state["runtime"]==RUNTIME,"the actual immutable scalar arithmetic runtime")
        flint.ctx.prec=320
        def publish(name,values,bound,centres=None):
            i=state["saved_record_count"]
            require(name==TARGETS[i] and len(values)==COUNTS[i]
                and bound==("signed_enclosure" if i in SIGNED else "upper")
                and all(x.is_finite() for x in values),"one whole new ordered target")
            record={"complete_count":COUNTS[i],"bound":bound,"balls":[x.str(60) for x in values]}
            if i in CENTRED:
                require(centres is not None and len(centres)==96,"the same96 exact centres")
                record["exact_dyadic_centres"]=centres
            else:
                require(centres is None,"centres belong only to the declared full rows")
            state["current_target"]=name;state["candidate_record"]=record;save()
            saved=parse(args.output.read_bytes())["candidate_record"]
            require(saved==record,"whole target readback before any dependent arithmetic")
            state["new_records"][name]=saved;state["completed_targets"].append(name)
            state["saved_record_count"]=i+1;state["candidate_record"]=state["current_target"]=None
            state["stage"]="new_PWA96_target_saved";save()
            print(json.dumps({"new_target":name,"complete_count":COUNTS[i]}),flush=True)
            return [flint.arb(x) for x in parse(args.output.read_bytes())["new_records"][name]["balls"]]
        def ratio(value):
            state["phase_ratio_exact_dyadic_centre"]=value;save()
        math=load(paths[roles["saved_math"]],"_PWA96_new_scalar_combinations")
        require(math.TARGETS==TARGETS and math.COUNTS==COUNTS and math.SIGNED==SIGNED and math.CENTRED==CENTRED,
                "entire new mathematical target definitions")
        state["result"]=math.compute(admitted,PARAMETERS,publish,ratio)
        state.update(complete=True,proved=True,actual_returncode=0,stage="complete_"+STAGE+"_scalar_branch")
        save();validate_output(args.output.read_bytes(),manifest,args.manifest_sha,source_sha,
                              os.environ["GITHUB_RUN_ID"],"1")
    except BaseException as exc:
        state.update(complete=False,proved=False,actual_returncode=1,
            failure={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()})
        save();raise


if __name__=="__main__":
    main()
