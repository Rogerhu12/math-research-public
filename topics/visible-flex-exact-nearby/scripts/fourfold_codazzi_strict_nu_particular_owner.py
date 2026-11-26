"""NP actual full selected strict parameter particular and194 signed waist balls.

Only public Actions performs the new forced trial, complete PDE residual,
selected transfer and signed output targets.  Current-input admission and
manifest construction are standard-library metadata only.  No old norm,
source integral, direction reconstruction, homogeneous QR or inverse runs.
"""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, importlib.util, json, os, platform
from pathlib import Path
import subprocess, sys, tempfile, time, traceback
from fractions import Fraction

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_math.py"
PROPOSAL = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_proposal.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_strict_nu_particular_manifest.py"
PROOF = TOPIC+"/results/R147-supplement-independent-strict-nu-particular-and-signed-waist-column.md"
SL_MANIFEST = TOPIC+"/notes/2026-11-27-support-localized-nu-inputs.json"
RW_MANIFEST = TOPIC+"/notes/2026-11-26-reflected-waist-rows-inputs.json"
TC_MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-separated-grid-inputs.json"
WX_EXECUTION = TOPIC+"/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json"
WX_SHA = "e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12"
KIND = "R147_true_selected_strict_nu_particular_signed_waist_v1"
STAGE = "true_selected_strict_nu_particular"
MANIFEST_KIND = "R147_true_selected_strict_nu_particular_inputs_v1"
TARGETS = ["complete_selected_strict_nu_trial_error", "complete_signed_strict_nu_waist_column"]
RUNTIME = {"python":"3.12.14", "packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS = {
    "arithmetic_bits":320, "decimal_record_digits":60, "private_RW_digits":80,
    "maximum_scientific_wall_seconds":7200,
    "trial_fourier_degree":96, "complete_centre_fourier_degree":32,
    "complete_centre_source_degree":96, "complete_centre_residual_degree":160,
    "trial_mesh_denominator":4096, "floating_max_RK4_step":"1/32768",
    "strict_trial_interval":["0","9/50"], "true_source_support":["1/20","9/50"],
    "compact_source_length":"13/100", "independent_density_means":2,
    "whole_incoming_signed_rows":96, "whole_physical_primitive_signed_rows":96,
    "continuous_centre_definition_sha256":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "continuous_direction_definition_sha256":"6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "exact_alpha":"6890507429876859/9007199254740992",
    "fixed_intrinsic_parameter":"eta_0", "selected_member_run":"43588332723/1",
    "selected_member_loss":"1/250", "delta_budget_radius":"1/10000000000",
    "selected_to_budget_ratio_upper":"936826/1000000", "original_direction_A0_upper":"19",
    "source":"partial_nu_F_at_the_original_implicit_selected_member",
    "terminal_data":"entire_pair_zero_at_9_over_50_then_exact_zero_extension",
    "trial_basis":"sqrt2_sin4j_mean1_sqrt2_cos4j",
    "source_measure":"ordinary_dr_normalized_angular_measure",
    "direction_array_reconstruction_required":False,
    "positive_inverse_or_incoming_inverse_used":False,
}
SCI_FIELDS = sorted(["identity","parameters","runtime","complete","proved","actual_returncode",
    "failure","stage","completed_targets","current_target","candidate_record","new_records",
    "saved_record_count","whole_completed_inputs","reference_identity","selected_member_identity",
    "copied_prior_scalar_records","result","trial_definition","trial_receipts","integral_prefix",
    "original_full_row_payload_sha256","old_scientific_target_calls","new_arrays_published",
    "new_artifacts","new_Releases","wall_seconds"])


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw,
                      parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


def descriptor(role,path,raw):
    return {"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def atomic(path,raw):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_name(path.name+".candidate")
    with temporary.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary,path)


def load(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    require(spec is not None and spec.loader is not None,"complete pinned source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def gather(root):
    """Current small objects and original historical metadata; no native science."""
    root = Path(root)
    current,history,roles = {},{},{}
    def add(role,path,expected=None):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,"safe declared topic input")
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000,"whole current UTF8 object: "+path)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(),filename=path)
        got = descriptor(role,path,raw)
        if expected is not None:
            require(all(got[k] == expected[k] for k in ("path","bytes","sha256","git_blob_sha")),
                    "whole unchanged original current input: "+role)
        if path not in current:
            current[path] = got
        roles[role] = path
        return parse(raw) if path.endswith(".json") else raw
    sl = add("SL_manifest",SL_MANIFEST)
    review = next(x for x in sl["files"] if x["role"] == "reviewed_rules")
    add("reviewed_rules",review["path"],review)
    for item in sl["files"]:
        add("SL_"+item["role"],item["path"],item)
    rw = add("RW_manifest",RW_MANIFEST)
    require(len(rw["historical_inputs"]) == 4,"the existing complete small RW closure")
    for item in rw["files"]:
        add("RW_"+item["role"],item["path"],item)
    tc = add("TC_carrier_manifest",TC_MANIFEST)
    tc_by_path = {x["path"]:x for x in tc["files"]+tc["historical_inputs"]}
    for role in ("inputs_math","trial_math","proposal_math","box_math","fft_math",
                 "candidate_reader","repair_source","old_body_manifest","RW_actual","RW_execution"):
        path = tc["roles"][role]
        add(role,path,tc_by_path[path])
    add("WX_execution",WX_EXECUTION)
    require(current[WX_EXECUTION]["sha256"] == WX_SHA,"the entire completed selected WX receiver")
    for role,path in (("science",SOURCE),("nu_math",MATH),("nu_proposal",PROPOSAL),
                      ("worker",WORKER),("generator",GENERATOR),("proof",PROOF)):
        add(role,path)
    def historical(role,item):
        item = dict(item,role=role)
        path,commit = item["path"],item["commit"]
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,
                "complete original historical topic input")
        if "git_blob_sha" not in item:
            item["git_blob_sha"] = subprocess.run(
                ["git","rev-parse",commit+":"+path],cwd=root,capture_output=True,text=True,check=True).stdout.strip()
        require(len(item["git_blob_sha"]) == 40,"original complete Git object metadata")
        item.pop("restore_only",None)
        history[path] = item
        roles[role] = path
    for role in ("base_index","old_centre_repair"):
        historical(role,tc_by_path[tc["roles"][role]])
    for item in tc["historical_inputs"]:
        if item.get("role","").startswith("base_part"):
            historical(item["role"],item)
    for item in tc["input_restoration"]["original_rows"]:
        historical(item["role"],item)
    for item in rw["historical_inputs"]:
        historical("RW_"+item["role"],item)
    require(len(history) == 51 and len({x["role"] for x in current.values()}) == len(current),
            "47 original native objects and all four complete saved RW definition objects")
    return {"files":sorted(current.values(),key=lambda x:x["role"]),
            "historical_inputs":sorted(history.values(),key=lambda x:x["role"]),"roles":roles}


def admit_current(manifest,raws,paths):
    """Admit complete saved bounds and row definitions before any numerical import."""
    roles = manifest["roles"]
    def raw(role):
        return raws[roles[role]]
    sl = parse(raw("SL_manifest"))
    sl_specs = {x["role"]:x for x in sl["files"]}
    sl_owner = load(paths[roles["SL_science"]],"_NP_complete_old_admission")
    old,saved = sl_owner.admit({k:raws[x["path"]] for k,x in sl_specs.items()},sl_specs)
    rw_manifest = parse(raw("RW_manifest"))
    rw_specs = {x["role"]:x for x in rw_manifest["files"]+rw_manifest["historical_inputs"]}
    rw_owner = load(paths[roles["RW_science"]],"_NP_original_RW_admission")
    rw = rw_owner.admit_complete_inputs({k:raws[x["path"]] for k,x in rw_specs.items()},rw_specs)
    actual,execution = parse(raw("RW_actual")),parse(raw("RW_execution"))
    actual_path = roles["RW_actual"]
    actual_raw = raw("RW_actual")
    require(actual["complete"] is actual["proved"] is execution["complete"] is True
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and actual["failure"] is execution["failure"] is None
            and actual["completed_targets"] == ["row_%03d"%j for j in range(1,97)]
            and actual["saved_record_count"] == actual["private_complete_row_count"] == 96
            and actual["identity"]["run_id"] == execution["run_id"] == "45787309600"
            and actual["identity"]["manifest_sha256"] == sha(raw("RW_manifest"))
            and actual["parameters"] == rw_manifest["parameters"]
            and execution["scientific_files"] == [{"path":actual_path,"bytes":len(actual_raw),"sha256":sha(actual_raw)}]
            and actual["reference_identity"] == rw["family"] == old["reference_identity"],
            "the entire already completed96 rows and the same original selected family")
    wx = parse(raw("WX_execution"))
    w = wx["actual_scientific_receipt"]
    require(sha(raw("WX_execution")) == WX_SHA
            and wx["complete"] is w["complete"] is w["proved"] is True
            and wx["actual_returncode"] == w["actual_returncode"] == 0
            and wx["actual_failure"] is w["failure"] is None
            and wx["run_id"] == w["run_id"] == "43763424840"
            and len(w["gates"]) == 20 and all(x["passed"] is True for x in w["gates"])
            and w["mathematical_parameters"]["fixed_intrinsic_parameter"] == "eta_0"
            and w["mathematical_parameters"]["exact_root_interval"] == old["parameters"]["exact_root_interval"],
            "whole completed same-selected left coordinate receiver")
    qualification = w["complete_selected_H_coordinate_conclusion"]
    require(qualification["only_same_selected_actual_conjugacy"] is True
            and qualification["all_density_Jacobians_and_normalized_measures_retained"] is True
            and qualification["independent_physical_mean_block_is_identity"] is True,
            "the full actual inverse-density receiver, including both means")
    d = parse(raw("SL_D_execution"))["actual_scientific_receipt"]
    negative = d["complete_scalar_fee_conclusions"]["fixed_negative_window"]
    for key in ("continuous_centre_definition_sha256","continuous_direction_definition_sha256",
                "exact_alpha","fixed_intrinsic_parameter","selected_member_run","selected_member_loss"):
        require(PARAMETERS[key] == old["parameters"][key],"same complete original mathematical parameter")
    require(d["chosen_global_constants"]["response_pair_A0"] == PARAMETERS["original_direction_A0_upper"]
            and not any(x in sys.modules for x in ("numpy","flint","scipy")),
            "all original bounds admitted without numerical calls")
    return {"R147":old,"D":d,"RW":rw,"RW_actual":actual,"RW_specs":rw_specs,
            "old_bounds":{"C1":saved["C1"],"M0":negative["maxima"]["M0"],
                          "M1":negative["maxima"]["M1"],"N_C":saved["N_C"],
                          "BH":qualification["complete_inverse_density_L2_upper"],
                          "KW":actual["copied_prior_scalar_records"]["fixed_Js_same_inverse_L2"]}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-map","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--checkout",required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "only one explicitly authorized public new target run")
    manifest_raw = args.manifest.read_bytes()
    require(sha(manifest_raw) == args.manifest_sha,"whole frozen current manifest")
    manifest = parse(manifest_raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["runtime"] == RUNTIME,
            "the complete true parameter particular contract")
    specs = manifest["files"]+manifest["historical_inputs"]
    input_map = parse(args.input_map.read_bytes())
    require(set(input_map) == {x["role"] for x in specs}
            and len({x["path"] for x in specs}) == len(specs), "all complete immutable input objects")
    raws,paths = {},{}
    for item in specs:
        path = Path(input_map[item["role"]])
        raw = path.read_bytes()
        require(len(raw) == item["bytes"] and sha(raw) == item["sha256"],"whole current or historical input")
        raws[item["path"]],paths[item["path"]] = raw,path
    require(sha(Path(__file__).read_bytes()) == next(x["sha256"] for x in specs if x["role"] == "science"),
            "this exact entire new owner")
    sys.dont_write_bytecode = True
    prior = admit_current(manifest,raws,paths)
    roles = manifest["roles"]
    helper = load(paths[roles["inputs_math"]],"_NP_original_input_arithmetic")
    old_body = parse(raws[roles["old_body_manifest"]])
    rows,part_receipts = helper.admit_all_rows(
        [paths[x["path"]] for x in manifest["historical_inputs"] if x["role"].startswith("original_rows_")],
        {"old_body_manifest":old_body,"NW":{"difference":prior["D"]}})
    repair = parse(raws[roles["old_centre_repair"]])
    require(repair["complete"] is True and repair["derived_definition_sha256"]
            == PARAMETERS["continuous_centre_definition_sha256"]
            and all(x["passed"] is True for x in repair["gates"]), "the full original exact continuous centre definition")
    require(not args.output.exists(),"a fresh actual scientific result")
    state = {
        "identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
            "source_sha256":sha(Path(__file__).read_bytes()),"run_id":os.environ["GITHUB_RUN_ID"],
            "run_attempt":"1","event_commit":os.environ["GITHUB_SHA"],"actual_checkout_commit":args.checkout,
            "arithmetic_bits":320},
        "parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,
        "actual_returncode":None,"failure":None,"stage":"complete_original_inputs_admitted",
        "completed_targets":[],"current_target":None,"candidate_record":None,"new_records":{},
        "saved_record_count":0,"whole_completed_inputs":{
            "complete_current_input_count":len(manifest["files"]),
            "complete_historical_input_count":len(manifest["historical_inputs"]),
            "full_input_list_manifest_sha256":args.manifest_sha,
            "complete_input_descriptor_list_sha256":sha(canonical(specs)),
            "all40_original_row_parts_read":True,"direction_shards_materialized":0},
        "reference_identity":prior["R147"]["reference_identity"],
        "selected_member_identity":prior["R147"]["selected_member_identity"],
        "copied_prior_scalar_records":prior["old_bounds"],"result":None,
        "trial_definition":None,"trial_receipts":None,"integral_prefix":None,
        "original_full_row_payload_sha256":helper.ROW_PAYLOAD,
        "old_scientific_target_calls":0,"new_arrays_published":0,"new_artifacts":0,"new_Releases":0,
        "wall_seconds":0.0,
    }
    require(sorted(state) == manifest["allowed_scientific_fields"],"the exact declared whole scientific envelope")
    began = time.perf_counter()
    def save():
        state["wall_seconds"] = time.perf_counter()-began
        require(state["wall_seconds"] < PARAMETERS["maximum_scientific_wall_seconds"],"actual scientific time budget")
        raw = canonical(state)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],"whole small actual result")
        atomic(args.output,raw)
    def progress(stage,extra):
        state["stage"] = stage
        print(json.dumps({"stage":stage,**extra},sort_keys=True),flush=True)
        save()
    save()
    private = Path(tempfile.mkdtemp(prefix="NP-complete-private-trial-",dir=str(args.output.parent)))
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),"packages":{key:version(key) for key in RUNTIME["packages"]}}
        require(runtime == RUNTIME,"the declared directed and floating runtime")
        flint.ctx.prec = 320
        arb = flint.arb
        state["runtime"] = runtime
        core = load(paths[roles["trial_math"]],"_NP_original_directed_trial_algebra")
        math = load(paths[roles["nu_math"]],"_NP_complete_new_source_math")
        proposal = load(paths[roles["nu_proposal"]],"_NP_new_forced_proposal")
        old_proposal = load(paths[roles["proposal_math"]],"_NP_original_centre_carrier")
        backend,_ = helper.directed_backend(np,flint,raws[roles["box_math"]],raws[roles["fft_math"]])
        c = core.DirectedContext(np,arb,backend["Box"],backend["CBox"],backend["zeros"],
                    backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
        def ball(record):
            value = arb(record["ball"])
            if "lower" in record and "upper" in record:
                value = value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite(),"whole finite original ball")
            return value
        def upper(record):
            value = ball(record)
            require(value.lower() >= 0,"whole nonnegative saved upper")
            return value.upper()
        def record(value,signed=False):
            value = value if signed else value.upper()
            require(value.is_finite() and (signed or value >= 0),"finite whole scientific value")
            result = {"ball":value.str(PARAMETERS["decimal_record_digits"]),
                      "bound":"signed_enclosure" if signed else "upper"}
            require(arb(result["ball"]).contains(value),"entire serialized scientific ball contains the original")
            return result
        def finish(name,result):
            require(name == TARGETS[state["saved_record_count"]],"next complete declared scientific target")
            state["candidate_record"] = {"name":name,"record":result}
            save()
            require(parse(args.output.read_bytes())["candidate_record"] == state["candidate_record"],
                    "complete target candidate readback")
            state["new_records"][name] = copy.deepcopy(result)
            state["completed_targets"].append(name)
            state["saved_record_count"] += 1
            state["candidate_record"] = state["current_target"] = None
            save()
            return parse(args.output.read_bytes())["new_records"][name]
        reader,_ = helper.candidate_reader(np,raws[roles["candidate_reader"]])
        iterator,_ = helper.repair_iterator(raws[roles["repair_source"]])
        base = reader(paths[roles["base_index"]])
        require(base["piece_coefficients"].shape == (4,6144,65),"all original centre coefficients")
        nodes,plan = math.complete_plan(rows,base["radial_nodes"])
        definition = {"kind":"NP_fixed_rational_septic_forced_nu_trial_v1",
            "node_labels":list(map(str,nodes)),"maximum_step":"1/4096",
            "terminal":"entire value and first three jets zero at9/50",
            "basis":PARAMETERS["trial_basis"],"selected_parameter_is_not_a_numeric_point":True}
        state["trial_definition"] = {"definition_sha256":sha(canonical(definition)),
            "certificate_plan_sha256":sha(canonical(plan)),"complete_nodes":len(nodes),
            "complete_certificate_cells":len(plan),"complete_original_rows":len(rows),
            "direction_shards_materialized":0,"original_full_part_receipts_sha256":sha(canonical(part_receipts))}
        offsets = {key:np.zeros((6144,65)) for key in ("lower","upper","midpoint")}
        last_piece = max(item["background_piece"] for item in plan)
        offset_digest = hashlib.sha256()
        for piece,values,_ in iterator(base,math.ALPHA):
            if piece > last_piece:
                break
            offset_digest.update(canonical({"piece":piece,"physical_offset":list(map(str,values))}))
            for k,value in enumerate(values):
                converted = c.arb_box(c.exact(value))
                offsets["lower"][piece,k],offsets["upper"][piece,k] = float(converted.lo),float(converted.hi)
                offsets["midpoint"][piece,k] = float(value)
        state["trial_definition"]["necessary_complete_centre_prefix"] = {
            "pieces":last_piece+1,"signed_offset_sequence_sha256":offset_digest.hexdigest(),
            "entire_scientific_domain":"[0,9/50]","all_preceding_interface_offsets_included":True}
        ref = old_proposal.FloatingCentreReference(np,rows,base,offsets["midpoint"],math.ALPHA,ball)
        forced = proposal.ForcedCentreReference(np,ref,rows,ball)
        state["current_target"] = TARGETS[0]
        jets,selection = proposal.choose_particular(np,forced,nodes,progress)
        receipts = []
        for order,value in enumerate(jets):
            require(value.shape == (len(nodes),193) and np.all(np.isfinite(value)),"whole exact dyadic endpoint array")
            path = private/("new_endpoint_derivative_%d.f64"%order)
            payload = np.asarray(value,dtype='<f8').tobytes(order='C')
            atomic(path,payload)
            receipts.append({"derivative":order,"shape":[len(nodes),193],"bytes":len(payload),"sha256":sha(payload)})
            jets[order] = np.memmap(path,dtype='<f8',mode='r',shape=(len(nodes),193))
        state["trial_receipts"] = {"complete_arrays":receipts,"selection":selection,
            "shared_endpoint_jets_define_exact_C3_trial":True,"complete_trial_state_jump_sum":"0"}
        totals = {name:c.Box(np.zeros(1)) for name in
                  ("residual_L1_Hminus1","trial_L1_L2","trial_angle_L1_L2")}
        for index,item in enumerate(plan):
            cell = math.certify_cell(c,core,base,offsets,rows[item["row"]],item,nodes,jets,ball)
            totals = {name:c.add_upper(totals[name],cell[name]) for name in totals}
            prefix = {name:record(arb(float(value.hi[0]))) for name,value in totals.items()}
            state["integral_prefix"] = {"complete_cells":index+1,"total_cells":len(plan),
                "actual_complete_interval_end":item["interval"][1],"whole_upper_records":prefix,
                "full_domain_complete":index+1 == len(plan)}
            if index%16 == 0 or index+1 == len(plan):
                progress("new_complete_strict_nu_residual_cells",{"complete_cells":index+1,"total_cells":len(plan)})
        save()
        saved_integrals = parse(args.output.read_bytes())["integral_prefix"]["whole_upper_records"]
        old_bounds = {name:upper(prior["old_bounds"][name]) for name in ("C1","M0","M1","N_C")}
        error = math.selected_error(flint,{name:upper(value) for name,value in saved_integrals.items()},old_bounds)
        first = finish(TARGETS[0],{"whole_trial_integrals":saved_integrals,
            "complete_selected_waist_density_error_upper":record(error),
            "complete_trial_jumps_exact":"0","all_source_and_mean_components_retained":True,
            "selected_operator_difference_paid":True,"full_domain":["0","9/50"],
            "positive_or_incoming_inverse_used":False})
        # The signed column uses the formal whole saved first result.
        error = upper(first["complete_selected_waist_density_error_upper"])
        state["current_target"] = TARGETS[1]
        progress("new_signed_strict_nu_waist_column",{"rows":96,"mean_rows":2})
        row0 = rows[0]
        left,right = map(Fraction,row0["interval"])
        scalar0 = {name:core.scalar_taylor(c,row0["intrinsic_midpoint_jets"],row0["intrinsic_whole_third_jets"],
                     name,*row0["interval"],left,right,ball) for name in ("beta","K","gamma","s")}
        background0 = math.base_background(c,core,base,offsets,0,left,right,scalar0["s"])
        def scalar_point(field):
            require(field.degree == 0,"complete radial scalar at the true waist")
            value = core.trial_value(c,field.coefficients,c.box(-1))[0,0]
            e = float(np.max(field.error.hi))
            value = value+c.Box(-e,e)
            return arb(float(value.lo)).union(arb(float(value.hi)))
        K0 = scalar_point(scalar0["K"])
        mean0 = scalar_point(background0[1].mean())
        uncertainty = c.exact(Fraction(19,10**10)*Fraction(936826,1000000))
        selected_mean = mean0+(-uncertainty).union(uncertainty)
        radius0 = ball(row0["intrinsic_whole_third_jets"]["a"])
        require(K0.upper() < 0 and selected_mean.upper() < 0 and radius0.lower() > 0,
                "the whole selected physical waist denominator, never frozen to the centre")
        q0,ng0 = (-K0).sqrt(),radius0*radius0/(selected_mean*selected_mean)
        density = core.full_waist_density(c,c.Box(np.asarray(jets[0][0,:,None])),q0,ng0)
        Y = record(arb(float(c.sqrt_upper(core.density_norm_squared(c,density)).hi[0])))
        whole_Y = upper(Y)
        rw_math = load(paths[prior["RW_specs"]["row_math"]["path"]],"_NP_necessary_RW_carriers")
        rw = prior["RW"]
        factory = rw_math.ReflectedRowFactory(flint,rw["H_sines"],rw["H_cosines"],rw["K_sines"],rw["K_cosines"],
            H_constant=rw["zero_translation_qualification"]["H_constant"],
            K_constant=rw["zero_translation_qualification"]["K_constant"])
        actual = prior["RW_actual"]
        def same_carrier(kind,values,extra,expected):
            values = list(values)
            document = {"kind":kind,"definition_sha256":actual["definition_sha256"],**extra,
                        "all_real_balls":[x.str(PARAMETERS["private_RW_digits"]) for x in values]}
            raw = canonical(document)
            require(len(raw) == expected["bytes"] and sha(raw) == expected["sha256"]
                    and len(values) == expected["complete_real_count"],"same entire necessary old RW carrier")
            return [arb(x) for x in parse(raw)["all_real_balls"]]
        grid = same_carrier("R149_complete_exact_compound_cosine_grid_carrier_v1",
                factory.materialize_whole_compound_grid(),{"grid_points":4096},actual["private_grid_receipt"])
        factory.base_cosines,factory.previous,factory.current = grid,[arb(1) for _ in grid],list(grid)
        BH,KW = upper(prior["old_bounds"]["BH"]),upper(prior["old_bounds"]["KW"])
        halfroot = (arb(1)/2).sqrt().upper()
        signed = {"declared_incoming_cosine96":{},"original_physical_primitive96":{},"independent_density_means":{}}
        trial_pairings = {"declared_incoming_cosine96":{},"original_physical_primitive96":{}}
        for index in range(1,97):
            j,coefs = factory.next_complete_row()
            require(j == index,"each complete original row in its proper order")
            old_row = actual["new_records"]["row_%03d"%j]
            coefs = same_carrier("R149_complete_exact_DFT_real_row_carrier_v1",coefs,
                {"mode":j,"nonnegative_modes":[0,1024],
                 "negative_modes":"equal by exact evenness, not selected by midpoint"},old_row["carrier"])
            row_error = upper(old_row["compound_error"])*whole_Y
            for label,incoming in (("declared_incoming_cosine96",True),("original_physical_primitive96",False)):
                value = core.real_signed_density_pairing(c,coefs,density,incoming=incoming)
                app = arb(float(value.lo[0])).union(arb(float(value.hi[0])))
                trial_pairings[label]["row_%03d"%j] = record(app,signed=True)
                fee = (BH*KW*error+row_error).upper() if incoming else (halfroot*(BH*error+row_error)).upper()
                signed[label]["row_%03d"%j] = record(app+(-fee).union(fee),signed=True)
            if index%16 == 0:
                progress("new_signed_strict_nu_rows",{"complete_rows":index,"rows":96})
        for index,field in enumerate(density["means"]):
            value = scalar_point(field)
            signed["independent_density_means"]["plus" if index == 0 else "minus"] = record(
                value+(-error).union(error),signed=True)
        require(sum(map(len,signed.values())) == 194,"all declared signed outputs and both means")
        require(sum(map(len,trial_pairings.values())) == 192,
                "all same-run uninflated signed trial pairings, without any recomputation")
        finish(TARGETS[1],{"complete_signed_output_balls":signed,"complete_signed_output_count":194,
            "complete_signed_trial_pairings":trial_pairings,"complete_signed_trial_pairing_count":192,
            "trial_pairings_exclude_PDE_and_RW_error_fees":True,
            "trial_waist_density_norm_upper":Y,"whole_selected_waist_mean_enclosure":record(selected_mean,True),
            "same_fixed_Js_finite_complement_identity_used_only_for_the_trial":True,
            "full_infinite_PDE_error_keeps_BH_KW":True,"original_RW_error_targets_recomputed":0,
            "positive_or_incoming_inverse_used":False})
        state["result"] = {"kind":KIND,"complete_new_record_count":2,"complete_new_record_order":list(TARGETS),
            "complete_selected_strict_nu_particular_certified":True,"whole_signed_waist_output_count":194,
            "unknown_true_solution_remains_full_Fourier":True,"both_physical_density_means_retained":True,
            "all_trial_jumps_proved_zero_from_shared_exact_endpoint_data":True,
            "old_direction_array_or_QR_reconstructed":False,"positive_inverse_used":False,
            "direct_positive_and_root_state_exactly_zero":True,
            "complete_incoming_inverse_proved":False,"full_parameter_boundary_column_proved":False,
            "true_nu_or_phase_Schur_proved":False,"topic_completion_proved":False}
        state["complete"] = state["proved"] = True
        state["actual_returncode"] = 0
        state["stage"] = "complete_"+STAGE+"_scalar_branch"
        save()
        return 0
    except BaseException as exc:
        state["complete"] = state["proved"] = False
        state["actual_returncode"] = 1
        state["failure"] = {"type":type(exc).__name__,"message":str(exc)[:2000],"traceback":traceback.format_exc()[-6000:]}
        state["stage"] = "failed_with_actual_complete_prefix_retained"
        state["wall_seconds"] = time.perf_counter()-began
        atomic(args.output,canonical(state))
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
