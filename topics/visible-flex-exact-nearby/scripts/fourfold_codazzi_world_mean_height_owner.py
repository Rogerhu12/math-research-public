"""First complete selected physical mean-height kernel from frozen RHI."""
from __future__ import annotations
import argparse,ast,gzip,hashlib,importlib.util,json,os,platform,sys,tempfile,time,traceback
from pathlib import Path

REPO="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
SOURCE=TOPIC+"/scripts/fourfold_codazzi_world_mean_height_owner.py"
MATH=TOPIC+"/scripts/fourfold_codazzi_world_mean_height_math.py"
RESTORE=TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_restore.py"
WORKER=TOPIC+"/scripts/fourfold_codazzi_world_mean_height_public_worker.py"
GENERATOR=TOPIC+"/scripts/make_world_mean_height_manifest.py"
PROOF=TOPIC+"/results/R147-supplement-original-world-anchor-and-physical-mean-height-reduction.md"
RHI_MANIFEST=TOPIC+"/notes/2026-11-27-relative-nu-carriers-inputs.json"
RHI_BASE=TOPIC+"/notes/relative_nu_carriers_ci/run-45933988440-1"
RHI_SOURCE=TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_owner.py"
RHI_MATH=TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_math.py"
RHI_WORKER=TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_public_worker.py"
KIND="R147_complete_physical_mean_height_nu_kernel_v1"
MANIFEST_KIND="R147_complete_physical_mean_height_nu_kernel_inputs_v1"
STAGE="complete_physical_mean_height_nu_kernel"
RUNTIME={"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS={
    "arithmetic_bits":320,"decimal_record_digits":60,"maximum_scientific_wall_seconds":18000,
    "complete_frozen_NP_arrays":4,"complete_NP_array_shape":[740,193],
    "complete_RHI_carrier_shape":[2048,18],"complete_RHI_carrier_bytes":294912,
    "complete_relative_components":18,"new_contraction_grid":8192,
    "complete_original_interpolant_degree":1024,"complete_kernel_degree_upper":2144,
    "complete_centre_degree":32,"complete_trial_degree":96,
    "exact_relative_interval":["0","9/50"],"physical_period":"pi/2",
    "physical_frequency_factor":4,"normalized_angular_measure":True,
    "original_world_frame_determinant":-1,"relative_frame_determinant":1,
    "reference_vertical_covector_error":"108627/1000000000",
    "complete_selected_state_difference_upper":"1/500000000",
    "background_mean_absolute_lower":"16/15","complete_v_upper":"18/5",
    "J_variation_operator_factor":"525/128","J_background_difference_factor":"7875/1024",
    "true_h_waist_error_comes_from":"complete_true_NP_uniform_L2_error_upper",
    "full_coordinate_variation_term":"dotJ*x",
    "both_moving_means_retained":True,
    "actual_world_position_frame_and_variation_ports_independent":True,
    "original_RHI_targets_recomputed":False,"new_carrier_selected":False,
    "exact_kernel_zero_mean_indices":[1],"new_complete_targets":3,
    "automatic_scientific_retry":False,
}
TARGETS=["complete_selected_physical_mean_height_kernel3",
    "complete_true_physical_mean_height_kernel_L1_upper",
    "complete_original_reference_world_mean_height_nu_body"]
COUNTS=[3,1,1]
SIGNED_INDICES=(0,2)
SCI_FIELDS=sorted(["identity","parameters","runtime","complete","proved","actual_returncode",
    "failure","stage","completed_targets","current_target","candidate_record","new_records",
    "saved_record_count","whole_completed_inputs","reference_identity","selected_member_identity",
    "copied_prior_scalar_records","necessary_original_trial_receipts",
    "necessary_relative_carrier_receipt","complete_kernel_details","result",
    "old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases","wall_seconds"])


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw,
        parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def atomic(path,raw):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    candidate=path.with_name(path.name+".candidate")
    with candidate.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.replace(candidate,path)


def gather(root,rhi_actual,rhi_execution,rhi_manifest=RHI_MANIFEST):
    root=Path(root);current={};roles={}
    def add(role,path,expected=None):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,
            "whole current topic input")
        raw=(root/path).read_bytes();raw.decode()
        require(0<len(raw)<100000,"small whole current UTF8 input")
        if path.endswith(".py"):
            ast.parse(raw.decode(),filename=path)
        spec={"role":role,"path":path,"bytes":len(raw),"sha256":sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if expected is not None:
            require(all(spec[k]==expected[k] for k in ("path","bytes","sha256","git_blob_sha")),
                "same whole frozen predecessor object: "+role)
        current.setdefault(path,spec);roles[role]=path
        return parse(raw) if path.endswith(".json") else raw
    rhim=add("RHI_manifest",rhi_manifest)
    for item in rhim["files"]:
        add("RHI_"+item["role"],item["path"],item)
    # The unchanged NP/SB admission consumes these paths from the new
    # full inventory, before any numerical import.
    for key,path in rhim["roles"].items():
        roles.setdefault(key,path)
    for role,path in [
        ("RHI_actual",rhi_actual),("RHI_execution",rhi_execution),
        ("RHI_source",RHI_SOURCE),("RHI_math",RHI_MATH),("RHI_worker",RHI_WORKER),
        ("science",SOURCE),("kernel_math",MATH),("relative_restore",RESTORE),
        ("worker",WORKER),("generator",GENERATOR),("proof",PROOF),
        ("saved_bounds",TOPIC+"/scripts/fourfold_codazzi_world_mean_height_saved_bounds.py"),
        ("proof_G",TOPIC+"/results/R133-supplement-complete-141-block-continuous-model-geometry.md"),
        ("proof_C",TOPIC+"/results/R133-supplement-complete-C0-state-and-nu-geometry-response.md"),
        ("proof_Waist",TOPIC+"/results/R133-supplement-exact-waist-grid-and-complete-canonical-alignment.md"),
        ("proof_RRM",TOPIC+"/results/R149-supplement-relative-frame-position-means-in-original-negative-source-windows.md"),
        ("waist_model_identity",TOPIC+"/notes/2026-11-14-R133-complete-exact-waist-grid-alignment-identities.json")]:
        add(role,path)
    history=[dict(item,role="RHI_"+item["role"]) for item in rhim["historical_inputs"]]
    specs=list(current.values())+history
    require(len(history)==51 and len({s["path"] for s in specs})==len(specs)
        and len({s["role"] for s in specs})==len(specs),"all necessary whole inputs without role collisions")
    return {"files":sorted(current.values(),key=lambda x:x["role"]),
            "historical_inputs":history,"roles":roles}


def admit(manifest,raws,paths):
    roles=manifest["roles"]
    old=load(paths[roles["RHI_source"]],"_WMR_original_complete_RHI_metadata")
    prior=old.admit(manifest,raws,paths)
    rhim=parse(raws[roles["RHI_manifest"]])
    actual,execution=(parse(raws[roles[k]]) for k in ("RHI_actual","RHI_execution"))
    source=next(x for x in rhim["files"] if x["role"]=="science")
    require(actual["complete"] is actual["proved"] is execution["complete"] is True
        and actual["actual_returncode"]==execution["actual_child_returncode"]==0
        and actual["failure"] is execution["failure"] is None
        and actual["identity"]["kind"]==old.KIND==rhim["scientific_kind"]
        and actual["identity"]["source_sha256"]==source["sha256"]
        and actual["identity"]["manifest_sha256"]==sha(raws[roles["RHI_manifest"]])
        and actual["parameters"]==old.PARAMETERS==rhim["parameters"]
        and actual["runtime"]==old.RUNTIME==RUNTIME
        and actual["completed_targets"]==old.TARGETS==rhim["target_order"]
        and actual["saved_record_count"]==4 and set(actual["new_records"])==set(old.TARGETS)
        and sorted(actual)==rhim["allowed_scientific_fields"]
        and actual["current_target"] is actual["candidate_record"] is None
        and actual["identity"]["run_id"]==execution["run_id"]=="45933988440"
        and actual["identity"]["run_attempt"]==execution["run_attempt"]=="1"
        and actual["reference_identity"]==prior["NP"]["reference_identity"]
        and actual["selected_member_identity"]==prior["NP"]["selected_member_identity"]
        and execution["scientific_files"]==[{"path":roles["RHI_actual"],
            "bytes":len(raws[roles["RHI_actual"]]),"sha256":sha(raws[roles["RHI_actual"]])}],
        "whole actually completed RHI4 on the same selected particular")
    for target,count in zip(old.TARGETS,old.COUNTS):
        value=actual["new_records"][target]
        require(value["complete_count"]==count and len(value["balls"])==count,
            "every whole predecessor vector: "+target)
    for key in ("same_original_selected_Q_delta","whole_four_original_NP_arrays_restored",
        "all_original2472_cells_and_every_true_join_retained","complete_relative18_component_carrier",
        "all2048_grid_labels_and_complete_angular_interpolation_errors",
        "real_orthogonal_residual_propagation_and_all_rounding_impulses",
        "complete_selected_background_direct_metric_and_both_means",
        "full_infinite_PDE_response_error_paid",
        "world_anchors_rigid_ports_and_physical_coordinate_term_independent"):
        require(actual["result"][key] is True,"complete RHI qualification: "+key)
    require(actual["result"]["actual_world_anchor_carrier_computed"] is False
        and actual["result"]["full_world_height_signed_value_proved"] is False,
        "an old relative carrier is not an already computed world height")
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),
        "whole metadata admission precedes numerical calls")
    return dict(prior,RHI=actual,RHI_manifest=rhim)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","input-map","output"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--checkout",required=True)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one public first physical mean-height target")
    manifest=parse(args.manifest.read_bytes())
    require(sha(args.manifest.read_bytes())==args.manifest_sha
        and manifest["kind"]==MANIFEST_KIND and manifest["scientific_kind"]==KIND
        and manifest["stage"]==STAGE and manifest["parameters"]==PARAMETERS
        and manifest["runtime"]==RUNTIME and manifest["target_order"]==TARGETS
        and manifest["allowed_scientific_fields"]==SCI_FIELDS,
        "whole immutable new kernel contract")
    input_map=parse(args.input_map.read_bytes())
    specs=manifest["files"]+manifest["historical_inputs"]
    require(set(input_map)=={x["role"] for x in specs},"every complete declared input")
    raws,paths={},{}
    for item in specs:
        path=Path(input_map[item["role"]]);raw=path.read_bytes()
        require(len(raw)==item["bytes"] and sha(raw)==item["sha256"],
            "whole input: "+item["role"])
        raws[item["path"]],paths[item["path"]]=raw,path
    require(sha(Path(__file__).read_bytes())==next(x["sha256"] for x in specs if x["role"]=="science"),
        "whole actual new owner")
    sys.dont_write_bytecode=True
    admitted=admit(manifest,raws,paths)
    npm=admitted["NP_manifest"];nr=npm["roles"];roles=manifest["roles"]
    helper=load(paths[nr["inputs_math"]],"_WMR_original_whole_rows")
    rows,part_receipts=helper.admit_all_rows(
        [paths[x["path"]] for x in npm["historical_inputs"] if x["role"].startswith("original_rows_")],
        {"old_body_manifest":parse(raws[nr["old_body_manifest"]]),
         "NW":{"difference":admitted["prior"]["D"]}})
    require(not args.output.exists(),"preserve every genuine first execution")
    state={"identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
        "source_sha256":sha(Path(__file__).read_bytes()),"run_id":os.environ["GITHUB_RUN_ID"],
        "run_attempt":"1","event_commit":os.environ["GITHUB_SHA"],
        "actual_checkout_commit":args.checkout,"arithmetic_bits":320},
        "parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,
        "actual_returncode":None,"failure":None,"stage":"whole_inputs_admitted",
        "completed_targets":[],"current_target":None,"candidate_record":None,"new_records":{},
        "saved_record_count":0,"whole_completed_inputs":{"complete_inventory_sha256":sha(canonical(specs)),
            "current_files":len(manifest["files"]),"historical_files":len(manifest["historical_inputs"]),
            "whole_original_rows":len(rows),"all40_original_parts_admitted":True,
            "RHI_complete_targets":4,"same_original_implicit_selected_member":True},
        "reference_identity":admitted["NP"]["reference_identity"],
        "selected_member_identity":admitted["NP"]["selected_member_identity"],
        "copied_prior_scalar_records":admitted["saved"],
        "necessary_original_trial_receipts":None,"necessary_relative_carrier_receipt":None,
        "complete_kernel_details":None,"result":None,"old_scientific_target_calls":0,
        "new_arrays_published":0,"new_artifacts":0,"new_Releases":0,"wall_seconds":0.}
    require(sorted(state)==SCI_FIELDS,"whole scientific envelope")
    started=time.perf_counter()
    def save(enforce=True):
        state["wall_seconds"]=time.perf_counter()-started
        if enforce:
            require(state["wall_seconds"]<=PARAMETERS["maximum_scientific_wall_seconds"],
                "new kernel computation budget")
        raw=canonical(state)
        require(len(raw)<=manifest["operation"]["maximum_scientific_bytes"],
            "whole small scientific result")
        atomic(args.output,raw)
    def progress(stage,detail):
        state["stage"]=stage;save()
        print(json.dumps({"stage":stage,**detail}),flush=True)
    save()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime={"python":platform.python_version(),
            "packages":{name:version(name) for name in RUNTIME["packages"]}}
        require(runtime==RUNTIME,"same exact required carrier runtime")
        state["runtime"]=runtime;flint.ctx.prec=320;arb=flint.arb
        def ball(record):
            value=arb(record["ball"])
            if "lower" in record and "upper" in record:
                value=value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite(),"whole finite original ball")
            return value
        def record(value,direction):
            value=value if direction=="signed_enclosure" else value.upper()
            require(value.is_finite() and (direction=="signed_enclosure" or value>=0),
                "complete finite directed scalar")
            out={"ball":value.str(PARAMETERS["decimal_record_digits"]),"bound":direction}
            require(arb(out["ball"]).contains(value),"whole outward serialized scalar")
            return out
        def publish(name,values,direction,centres=None):
            index=state["saved_record_count"]
            require(name==TARGETS[index] and len(values)==COUNTS[index]
                and direction==("signed_enclosure" if index in SIGNED_INDICES else "upper"),
                "one next complete kernel target")
            saved={"complete_count":len(values),"bound":direction,
                "balls":[record(value,direction)["ball"] for value in values]}
            if centres is not None:
                require(index==0 and len(centres)==3,"all exact joint-centre choices")
                saved["exact_dyadic_centres"]=centres
            state["current_target"]=name;state["candidate_record"]={"name":name,"record":saved};save()
            require(parse(args.output.read_bytes())["candidate_record"]==state["candidate_record"],
                "whole candidate record readback")
            state["new_records"][name]=saved;state["completed_targets"].append(name)
            state["saved_record_count"]+=1;state["current_target"]=state["candidate_record"]=None;save()
            restored=parse(args.output.read_bytes())["new_records"][name]
            return [arb(value) if direction=="signed_enclosure" else arb(value).upper()
                    for value in restored["balls"]]
        def save_details(details):
            state["complete_kernel_details"]=details;save()
        core=load(paths[nr["trial_math"]],"_WMR_original_directed_algebra")
        nu=load(paths[nr["nu_math"]],"_WMR_original_strict_trial_math")
        rhi=load(paths[roles["RHI_math"]],"_WMR_original_RHI_coefficients_and_recipe")
        np_restore=load(paths[roles["trial_restore"]],"_WMR_original_NP_restore")
        rel_restore=load(paths[roles["relative_restore"]],"_WMR_necessary_RHI_restore")
        math=load(paths[roles["kernel_math"]],"_WMR_first_complete_height_kernel")
        require(math.TARGETS==TARGETS and math.GRID==8192,"all three new complete targets")
        with tempfile.TemporaryDirectory(prefix="private-WMR-height-") as private:
            waist,unused_intrinsic,receipts=np_restore.restore(np,flint,npm,admitted["NP"],
                raws,paths,helper,rows,part_receipts,private,progress,atomic)
            state["necessary_original_trial_receipts"]=receipts;save()
            jets=[np.memmap(Path(private)/("original_NP_endpoint_derivative_%d.f64"%k),
                dtype="<f8",mode="r",shape=(740,193)) for k in range(4)]
            backend,_=helper.directed_backend(np,flint,raws[nr["box_math"]],raws[nr["fft_math"]])
            c=core.DirectedContext(np,arb,backend["Box"],backend["CBox"],backend["zeros"],
                backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
            reader,_=helper.candidate_reader(np,raws[nr["candidate_reader"]])
            iterator,_=helper.repair_iterator(raws[nr["repair_source"]])
            base=reader(paths[nr["base_index"]])
            nodes,original_plan=nu.complete_plan(rows,base["radial_nodes"])
            offsets={name:np.zeros((6144,65)) for name in ("lower","upper")}
            last=max(item["background_piece"] for item in original_plan)
            for piece,values,unused in iterator(base,nu.ALPHA):
                if piece>last:
                    break
                for j,value in enumerate(values):
                    converted=c.box(value)
                    offsets["lower"][piece,j]=float(converted.lo)
                    offsets["upper"][piece,j]=float(converted.hi)
            endpoint,restoration=rel_restore.restore(np,c,core,nu,rhi,base,offsets,rows,nodes,
                original_plan,jets,ball,admitted["RHI"],private,progress,atomic)
            state["necessary_relative_carrier_receipt"]=restoration;save()
            progress("new_complete_physical_mean_height_contraction",
                {"grid":8192,"complete_degree":2144,"old_scientific_targets":0})
            result=math.compute(c,endpoint,base,offsets,rows[0],waist,ball,nu.ALPHA,
                admitted["RHI"],admitted["SB"],publish,save_details)
        state["result"]=dict(result,kind=KIND,complete_new_record_count=3,
            complete_new_record_order=TARGETS,same_original_implicit_selected_Q_delta=True,
            original_det_minus_one_world_frame_retained=True,
            no_long_original_geometry_ODE_repeated=True,
            actual_world_frame_position_and_rigid_ports_independent=True,
            all_true_PDE_and_coordinate_mean_errors_included=True,
            original_RHI_targets_recomputed=False,original_NP_targets_recomputed=False,
            new_trial_selected=False,full_nu_phase_height_Schur_or_topic_complete=False)
        state.update(complete=True,proved=True,actual_returncode=0,
            stage="complete_"+STAGE+"_scalar_branch")
        save();return 0
    except BaseException as error:
        state.update(complete=False,proved=False,actual_returncode=1,
            failure={"type":type(error).__name__,"message":str(error)[:2500],
                     "traceback":traceback.format_exc()[-5000:]})
        save(False)
        print(json.dumps({"actual_failure":state["failure"],
            "saved_record_count":state["saved_record_count"]}),flush=True)
        return 1


if __name__=="__main__":
    raise SystemExit(main())
