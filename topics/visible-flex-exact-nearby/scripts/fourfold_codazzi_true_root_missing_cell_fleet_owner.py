"""TCF public science: one disjoint missing interval, all96/all5 per cell.

Every parent arithmetic process must have ended. The complete original
trial/offset arrays are restored with their old whole SHA identities.
No old signed matrix, old completed norm, or accepted cell is evaluated.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, math, os, platform, sys, time, traceback
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace

TOPIC="topics/visible-flex-exact-nearby"
SOURCE=TOPIC+"/scripts/fourfold_codazzi_true_root_missing_cell_fleet_owner.py"
HELPER=TOPIC+"/scripts/fourfold_codazzi_true_root_missing_cell_fleet.py"
MANIFEST_KIND="R149_original_TC_terminal_missing_cell_fleet_inputs_v1"
PARAMETERS={"arithmetic_bits":320,"whole_original_columns":96,"whole_original_source_windows":5,
    "whole_original_certificate_cells":7724,"maximum_scientific_seconds":16800,
    "cell_grace_seconds":180,"private_array_limit_bytes":12884901888,
    "per_job_arithmetic_processes":1,"per_cell_Legendre_identity_memo":True,
    "memo_lifetime":"one_complete_original_cell","memo_input_and_output_readonly":True,
    "cell_formula_or_operation_order_changed":False,"old_accepted_cells_evaluated":0,
    "old_completed_matrix_or_norm_targets_called":0,"maximum_actual_bytes":65000}
RUNTIME={"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def atomic(path,raw):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".partial")
    with temporary.open("wb") as stream:stream.write(raw);stream.flush();os.fsync(stream.fileno())
    os.replace(temporary,path);require(path.read_bytes()==raw,"whole atomic byte readback")


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def admit(root,raw,digest,ordinal,rows_index):
    root=Path(root)
    require(0<len(raw)<100000 and sha(raw)==digest,"one entire concrete TCF manifest")
    manifest=json.loads(raw)
    require(manifest["kind"]==MANIFEST_KIND and manifest["parameters"]==PARAMETERS
        and manifest["runtime"]==RUNTIME and manifest["repository"]=="Rogerhu12/math-research-public",
        "the declared same-cell public continuation contract")
    files={item["role"]:item for item in manifest["files"]}
    for spec in files.values():
        body=(root/spec["path"]).read_bytes()
        require(len(body)==spec["bytes"] and sha(body)==spec["sha256"],"the whole actual new input: "+spec["path"])
    require(files["science"]["path"]==SOURCE and sha(Path(__file__).read_bytes())==files["science"]["sha256"],
        "the whole actually executing new scientific owner")
    helper=load(root/HELPER,"_TCF_terminal_whole_admission")
    parent=helper.resolve_parent(root,manifest)
    require(type(ordinal) is int and 0<=ordinal<len(manifest["assignments"]),"one declared mutually exclusive job")
    old=parent["owner"]
    original=old.preflight(SimpleNamespace(repo=str(root),input_root=str(root),
        manifest=str(root/helper.PARENT_MANIFEST),manifest_sha=helper.PARENT_MANIFEST_SHA,rows_index=str(rows_index)))
    require(original[-1]==parent["documents"]["state"]["input_identity"],
        "all original inputs, selected family, endpoint arrays and scientific sources are identical")
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
        "whole terminal and original input admission finishes before numerical import")
    return manifest,helper,parent,original


def restore_original(np,flint,helper,admitted,parent,root,private,progress):
    manifest,roles,raws,inputs,prior,rows,identity=admitted
    module=load(root/roles["trial_math"]["path"],"_TCF_original_directed_math")
    proposal=load(root/roles["proposal_math"]["path"],"_TCF_original_exact_array_factory")
    backend,backend_receipts=inputs.directed_backend(np,flint,raws[roles["box_math"]["path"]],raws[roles["fft_math"]["path"]])
    c=module.DirectedContext(np,flint.arb,backend["Box"],backend["CBox"],backend["zeros"],
        backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
    reader,reader_receipt=inputs.candidate_reader(np,raws[roles["candidate_reader"]["path"]])
    iterator,repair_receipt=inputs.repair_iterator(raws[roles["repair_source"]["path"]])
    base=reader(root/roles["base_index"]["path"]);direction=reader(root/roles["direction_index"]["path"])
    arrays={}
    def allocate(name,shape):
        size=math.prod(shape)*8
        require(name not in arrays and sum(x["bytes"] for x in arrays.values())+size<=PARAMETERS["private_array_limit_bytes"],
            "the entire original private array budget")
        path=private/(name+".f64");require(not path.exists(),"no original private array overwritten")
        value=np.memmap(path,dtype="<f8",mode="w+",shape=shape,order="C")
        arrays[name]={"path":path,"shape":shape,"bytes":size,"array":value};return value
    def release(name):
        item=arrays.pop(name);item["array"].flush();del item["array"];item["path"].unlink()
    offsets,offset_receipts=inputs.materialize_repairs(c,base,direction,iterator,prior,allocate,progress)
    definition,nodes,plan=inputs.complete_plan(rows,base["radial_nodes"])
    old=parent["documents"]["state"]["proposal"]
    require(sha(encode(definition))==old["definition_sha256"]
        and sha(encode(plan))==old["certificate_plan_sha256"]
        and len(nodes)==old["complete_trial_nodes"]==7671 and len(plan)==old["complete_certificate_cells"]==7724,
        "the original complete true-root definition and every exact cell")
    def read_ball(record):
        value=(flint.arb(record["lower"]).lower().union(flint.arb(record["upper"]).upper())
            if "lower" in record and "upper" in record else flint.arb(record["ball"]))
        require(value.is_finite(),"the entire original saved ball");return value
    reference=proposal.FloatingCentreReference(np,rows,base,offsets["base"]["midpoint"],inputs.ALPHA,read_ball)
    proposal.choose_all_columns(np,reference,nodes,definition["root_index"],allocate,release,progress)
    saved,receipts=[],[]
    for name,expected in zip(("trial_value","trial_derivative_1","trial_derivative_2","trial_derivative_3"),old["complete_endpoint_arrays"]):
        item=arrays[name];item["array"].flush();digest=hashlib.sha256()
        with item["path"].open("rb") as stream:
            for block in iter(lambda:stream.read(1<<20),b""):digest.update(block)
        observed={"name":name,"shape":list(item["shape"]),"bytes":item["bytes"],"sha256":digest.hexdigest(),
            "encoding":"little-endian binary64 row-major exact dyadics"}
        require(observed==expected,"each entire original TC array is unchanged")
        saved.append(np.memmap(item["path"],dtype="<f8",mode="r",shape=item["shape"],order="C"));receipts.append(observed)
    require(np.array_equal(saved[0][definition["root_index"],97:,:],np.eye(96)),"the original full root-even96 identity")
    for item in arrays.values():item["array"].flags.writeable=False
    namespace={"c":c,"np":np,"module":module,"helper":inputs,"base":base,"direction":direction,
        "offsets":offsets,"rows":rows,"plan":plan,"definition":definition,"saved_arrays":saved,
        "read_ball":read_ball,"Fraction":Fraction,"PARAMETERS":manifest["parameters"],"require":require}
    tree=ast.parse((root/helper.BASE_OWNER).read_bytes())
    functions=[node for node in ast.walk(tree) if isinstance(node,ast.FunctionDef) and node.name=="scalar_inputs"]
    require(len(functions)==1,"the entire original selected-scalar function")
    fragment=ast.Module(body=functions,type_ignores=[]);ast.fix_missing_locations(fragment)
    exec(compile(fragment,"<TCF unchanged selected scalar inputs>","exec"),namespace)
    code,cell_receipt=helper.original_cell_factory(root)
    receipt={"complete_original_arrays":receipts,"whole_original_offset_receipts":offset_receipts,
        "whole_definition_sha256":old["definition_sha256"],"whole_plan_sha256":old["certificate_plan_sha256"],
        "directed_backend":backend_receipts,"candidate_reader":reader_receipt,"repair_iterator":repair_receipt,
        "whole_original_cell_evaluator":cell_receipt,"old_completed_matrix_or_norm_targets_called":0}
    return c,namespace,code,receipt


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("manifest","input-root","rows-index","output"):parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--ordinal",type=int,required=True)
    parser.add_argument("--checkout",required=True);parser.add_argument("--preflight-only",action="store_true")
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one first actual public assignment execution")
    manifest,helper,parent,admitted=admit(args.input_root,args.manifest.read_bytes(),args.manifest_sha,args.ordinal,args.rows_index)
    if args.preflight_only:
        print(encode({"complete_admission":True,"assignment":manifest["assignments"][args.ordinal],"scientific_calls":0}).decode());return 0
    require(not args.output.exists(),"every earlier actual assignment state remains intact")
    assignment=manifest["assignments"][args.ordinal]
    first,stop=assignment["first_cell"],assignment["stop_cell"]
    started=time.monotonic()
    state={"kind":helper.SLICE_KIND,"manifest_sha256":args.manifest_sha,"fleet_identity_sha256":manifest["fleet_identity_sha256"],
        "parent_identity_sha256":manifest["parent_identity_sha256"],"assignment":assignment,
        "run_id":os.environ["GITHUB_RUN_ID"],"run_attempt":"1","checkout":args.checkout,
        "parameters":PARAMETERS,"runtime":None,"next_cell":first,"accepted_complete_cells":0,
        "complete_assignment":False,"actual_returncode":None,"failure":None,"stage":"whole_original_inputs_admitted",
        "progress":{},"wall_seconds":0,"complete_columns":96,"all_original_source_windows":list(helper.NORMS),
        "old_accepted_cells_evaluated":0,"old_completed_matrix_or_norm_targets_called":0,
        "squared_norm_upper_exact_binary64":{name:[float(0).hex()]*96 for name in helper.NORMS},
        "carrier_restoration":None,"memo_statistics":{"whole_cell_calls":0,"Legendre_requests":0,"identical_object_hits":0},
        "original_TC_global_targets_complete":False,"new_arrays_published":0}
    def save():
        state["wall_seconds"]=time.monotonic()-started
        helper.validate_slice(state,manifest,args.ordinal)
        raw=encode(state);require(len(raw)<PARAMETERS["maximum_actual_bytes"],"one full small assignment result")
        atomic(args.output,raw)
    def progress(stage,details):
        state["stage"],state["progress"]=stage,details;save()
        print(encode({"ordinal":args.ordinal,"stage":stage,**details}).decode(),end="",flush=True)
    def budget():
        require(time.monotonic()-started<PARAMETERS["maximum_scientific_seconds"],"all prior complete cells saved before the wall allowance")
    save()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime={"python":platform.python_version(),"packages":{name:version(name) for name in RUNTIME["packages"]}}
        require(runtime==RUNTIME and os.environ.get("OPENBLAS_CORETYPE")=="Haswell"
            and all(os.environ.get(key)=="1" for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","BLIS_NUM_THREADS","VECLIB_MAXIMUM_THREADS")),
            "the identical original fixed arithmetic and trial-selection runtime")
        state["runtime"]=runtime;flint.ctx.prec,flint.ctx.cap=320,9
        private=args.output.parent/("private-TCF-%03d"%args.ordinal);private.mkdir()
        c,namespace,code,receipt=restore_original(np,flint,helper,admitted,parent,args.input_root,private,progress)
        state["carrier_restoration"]=receipt;namespace["budget"]=budget
        exec(code,namespace);evaluate=namespace["make_original_cell"]()
        sums={name:c.Box(np.zeros(96)) for name in helper.NORMS}
        parallel=parent["owner"]._TCX_parallel_module()
        progress("same_original_missing_cells_started",{"first_cell":first,"stop_cell":stop})
        for index in range(first,stop):
            if time.monotonic()-started>=PARAMETERS["maximum_scientific_seconds"]-PARAMETERS["cell_grace_seconds"]:break
            began=time.monotonic()
            with helper.OneCellLegendreMemo(c) as memo:
                contributions=evaluate(index)
            require(set(contributions)==set(namespace["plan"][index]["norms"]),"all original active source windows of this cell")
            updates={}
            for name,value in contributions.items():
                require(value.hi.shape==(96,) and np.all(np.isfinite(value.hi)) and np.all(value.hi>=0),
                    "all96 complete directed cell contributions")
                updates[name]=parallel._whole96_add_upper(c,sums[name],value)
            sums.update(updates)
            state["squared_norm_upper_exact_binary64"]={name:[float(x).hex() for x in c.upper(sums[name]).hi] for name in helper.NORMS}
            state["next_cell"]=index+1;state["accepted_complete_cells"]=index+1-first
            state["complete_assignment"]=index+1==stop
            stats=state["memo_statistics"];stats["whole_cell_calls"]+=1;stats["Legendre_requests"]+=memo.calls;stats["identical_object_hits"]+=memo.hits
            state["stage"]="complete_original_missing_cell_saved"
            state["progress"]={"last_complete_cell":index,"cell_wall_seconds":time.monotonic()-began,
                "all96_columns_saved":True,"all_declared_windows_saved":True,"memo_released":not memo.cache}
            save()
            if (index+1-first)%8==0 or index+1==stop:
                print(encode({"ordinal":args.ordinal,"next_cell":index+1,"stop_cell":stop,"accepted_complete_cells":index+1-first,
                    "last_cell_wall_seconds":state["progress"]["cell_wall_seconds"]}).decode(),end="",flush=True)
        require(state["complete_assignment"] is True,"assigned interval incomplete; every accepted whole cell is retained")
        state["actual_returncode"]=0;state["stage"]="whole_missing_interval_completed_global_TC_still_separate";save();return 0
    except BaseException as exc:
        state["failure"]={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()[-6000:]}
        state["actual_returncode"]=1;save();raise


def aggregate_main():
    """Finish only the previously unfinished original source norms.

    All accepted cell vectors already exist. This child performs one new
    complete scalar-upper aggregation and, only for a complete domain,
    takes the remaining original norm square roots. It restores no array.
    """
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--aggregate",action="store_true")
    for key in ("manifest","input-root","merge-input","output"):
        parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--checkout",required=True)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one public terminal-union aggregation")
    raw=args.manifest.read_bytes();manifest=json.loads(raw)
    require(sha(raw)==args.manifest_sha and manifest["kind"]==MANIFEST_KIND
        and manifest["parameters"]==PARAMETERS and manifest["runtime"]==RUNTIME,"the complete new fleet contract")
    roles={item["role"]:item for item in manifest["files"]}
    for spec in roles.values():
        data=(args.input_root/spec["path"]).read_bytes()
        require(len(data)==spec["bytes"] and sha(data)==spec["sha256"],"the whole saved aggregation input")
    require(roles["science"]["path"]==SOURCE and sha(Path(__file__).read_bytes())==roles["science"]["sha256"],
        "the same complete actual fleet owner")
    helper=load(args.input_root/HELPER,"_TCF_whole_aggregation_metadata")
    parent=helper.resolve_parent(args.input_root,manifest)
    merge_raw=args.merge_input.read_bytes();merge=json.loads(merge_raw)
    run=os.environ["GITHUB_RUN_ID"]
    require(merge["manifest_sha256"]==args.manifest_sha and merge["run_id"]==run and merge["run_attempt"]=="1"
        and merge["all_original_assignment_jobs_really_terminal"] is True,"all public interval jobs ended before aggregation")
    manifest["_whole_manifest_sha256"]=args.manifest_sha
    documents=helper.read_job_records(args.input_root,manifest,merge["source_records"],run)
    for doc in documents:
        if doc is not None and doc["accepted_complete_cells"]:
            restored=doc["carrier_restoration"]
            require(restored["complete_original_arrays"]==parent["documents"]["state"]["proposal"]["complete_endpoint_arrays"]
                and restored["whole_definition_sha256"]==parent["documents"]["state"]["proposal"]["definition_sha256"]
                and restored["whole_plan_sha256"]==parent["documents"]["state"]["proposal"]["certificate_plan_sha256"]
                and restored["old_completed_matrix_or_norm_targets_called"]==0,
                "every new accepted cell used all four unchanged original endpoint arrays")
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),"all complete metadata precedes new scalar aggregation")
    require(not args.output.exists(),"a prior whole aggregation is never overwritten")
    args.output.mkdir()
    def published(key):
        acknowledgement=args.output/("published-"+key+".ack")
        started=time.monotonic()
        while not acknowledgement.is_file():
            require(time.monotonic()-started<600,"whole completed conclusion awaits its immediate public push")
            time.sleep(.2)
        require(acknowledgement.read_text()==args.manifest_sha+"\n","actual same-manifest publication acknowledgment")
    intervals,sums=helper.aggregate_accepted(parent,manifest,documents)
    accepted=sum(stop-first for first,stop in intervals)
    union={"kind":helper.UNION_KIND,"aggregation_complete":True,"actual_returncode":0,"failure":None,
        "manifest_sha256":args.manifest_sha,"fleet_identity_sha256":manifest["fleet_identity_sha256"],
        "parent_identity_sha256":parent["parent_identity"],"original_parent_identity_sha256":parent["original_parent_identity"],
        "run_id":run,"run_attempt":"1","checkout":args.checkout,"proposal_identity":parent["documents"]["state"]["proposal"],
        "same_selected_family":parent["documents"]["state"]["input_identity"]["same_selected_family"],
        "complete_columns":96,"all_original_source_windows":list(helper.NORMS),"total_cells":helper.TOTAL,
        "accepted_intervals":intervals,"accepted_complete_cells":accepted,"missing_intervals":helper.missing_intervals(intervals),
        "complete_original_domain":accepted==helper.TOTAL,"squared_norm_upper_exact_binary64":sums,
        "source_records":merge["source_records"],"terminal_jobs_API":merge["terminal_jobs_API"],
        "whole_private_merge_input_sha256":sha(merge_raw),"old_accepted_cells_evaluated":0,
        "old_completed_matrix_or_norm_targets_called":0,"private_arrays_restored":0,"new_arrays_published":0,
        "true_PDE_columns_or_inverse_proved":False}
    raw_union=encode(union);require(len(raw_union)<95000,"one whole all96/all5 accepted-union record")
    atomic(args.output/"actual-accepted-union.json",raw_union)
    print("complete accepted union saved: "+str(accepted)+"/7724",flush=True)
    for key in parent["completed_natural_keys"]:
        spec=parent["specs"][key]
        atomic(args.output/parent["owner"].FILES[key],helper.require_whole(args.input_root,spec))
    published("union")
    if accepted<helper.TOTAL:
        print("partial union retained; no incomplete original source norm is published",flush=True);return 0
    import flint
    from importlib.metadata import version
    require(platform.python_version()==RUNTIME["python"] and version("python-flint")==RUNTIME["packages"]["python-flint"],
        "the declared complete final directed scalar arithmetic")
    flint.ctx.prec,flint.ctx.cap=320,9
    def scalar_upper(value):
        require(value.is_finite() and value.lower()>=0,"finite nonnegative complete norm")
        point=value.upper();record={"ball":point.str(50)}
        require(flint.arb(record["ball"]).contains(point),"whole serialized directed upper readback")
        return record
    matrix=parent["documents"]["matrix"]
    old=parent["owner"]
    for key in ("negative","positive"):
        if key in parent["completed_natural_keys"]:continue
        windows=(("negative_root","negative_strict") if key=="negative" else
            ("positive_low","positive_high_collar","positive_high_body"))
        doc={"kind":"R149_complete_"+key+"_finite_trial_sources96_v1","complete":True,"proved":True,
            "trial_definition_sha256":matrix["trial_definition_sha256"],"proposal_identity":matrix["proposal_identity"],
            "input_manifest_sha256":args.manifest_sha,"same_selected_family":matrix["same_selected_family"],
            "true_PDE_columns_or_inverse_proved":False,"complete_columns":96,
            "source_windows":{name:old.PARAMETERS["source_windows"][name] for name in windows},
            "ordinary_radial_measure":"dr","normalized_circle":True,"complete_original_coefficient_cover":7721,
            "all_boundary_and_jump_errors_exact":"0","complete_source_records":{}}
        if key=="negative":
            doc.update(complete_waist_trial_norms=matrix["complete_waist_trial_norms"],
                waist_norms_copied_verbatim_from_same_new_matrix_result={
                    k:parent["specs"]["matrix"][k] for k in ("path","bytes","sha256")},
                independent_waist_mean_coordinates=2)
        else:
            doc.update(complete_original_14_ports_nonzero_indices={"1":"positive_high_collar","2":"positive_high_body","7":"positive_low"},
                stable_high_root_and_even96_errors_exact="0")
        for j in range(96):
            doc["complete_source_records"]["column_%03d"%(j+1)]={
                name:scalar_upper(flint.arb(float.fromhex(sums[name][j])).sqrt()) for name in windows}
        old.validate_complete_result(doc,key,matrix["proposal_identity"],args.manifest_sha,matrix["same_selected_family"])
        result=encode(doc);require(len(result)<(50000 if key=="negative" else 52000),"one whole complete original source result")
        atomic(args.output/old.FILES[key],result)
        readback=json.loads((args.output/old.FILES[key]).read_bytes())
        old.validate_complete_result(readback,key,matrix["proposal_identity"],args.manifest_sha,matrix["same_selected_family"])
        print("new complete original source target saved: "+key,flush=True)
        published(key)
    return 0


if __name__=="__main__":
    sys.exit(aggregate_main() if "--aggregate" in sys.argv else main())
