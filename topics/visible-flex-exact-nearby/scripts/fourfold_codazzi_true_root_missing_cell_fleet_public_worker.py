"""TCF public transport: terminal parent, exclusive assignment, whole state.

The original TCXV input-restoration and Git publication closures are copied
as an exact whole-source prefix. Its old target reservation and science
branch are not entered. One common parent marker prevents a second fleet
from owning the same missing cells under a different partition.
"""
from __future__ import annotations
import argparse, ast, codecs, hashlib, importlib.util, json, os, selectors
import subprocess, sys, time, traceback, urllib.request
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
REPO="Rogerhu12/math-research-public"
PARENT_WORKER=TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_public_worker.py"
PARENT_WORKER_SHA="0d06ee5d40c86e74e97a803ce8a35a80be98151327db082f694acb691f396a3e"
TAIL='''
def prepare_original():
    head = pull()
    materialize_current(head)
    restore_history()
    restore_rows()
    reconstruct_direction()
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
        "only the original necessary native reconstruction child has run")
    return head
def configure_publication(marker, operation):
    nonlocal marker_path, op
    marker_path=topic_path(marker)
    require(operation["topic_maximum_bytes"]==LIMIT and operation["reserve_bytes"]==RESERVE,
        "unchanged complete original topic capacity units")
    op=operation
return dict(root=root, inputs=inputs_root, temporary=temporary, rows_index=rows_index,
    state=state, pull=pull, capacity=capacity, publish=publish, checked_bytes=checked_bytes,
    git=git, utc=utc, atomic=atomic, encode=encode, fetch_commit=fetch_commit,
    prepare_original=prepare_original, materialize_original_metadata=materialize_current,
    configure_publication=configure_publication)
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def parent_marker(manifest,manifest_sha):
    return {"kind":"R149_exclusive_terminal_TC_missing_cell_fleet_v1",
        "parent_identity_sha256":manifest["parent_identity_sha256"],"manifest_sha256":manifest_sha,
        "fleet_identity_sha256":manifest["fleet_identity_sha256"],"all_assignments":manifest["assignments"],
        "same_parent_may_not_be_repartitioned_while_this_fleet_owns_cells":True}


def assignment_marker(manifest,manifest_sha,ordinal,run,output_directory):
    return {
            "kind":"consumed_original_TC_whole_missing_interval_v1","run_id":run,"run_attempt":"1",
            "manifest_sha256":manifest_sha,"fleet_identity_sha256":manifest["fleet_identity_sha256"],
            "assignment":manifest["assignments"][ordinal],"output_directory":output_directory,
            "automatic_scientific_retry":False,"old_completed_targets_may_be_recomputed":False}


def compact_execution(state,shared,temporary,manifest,manifest_sha,role):
    """One complete new public contract; the entire transport state is private.

    All original restoration receipts, printed README diffs, retry details
    and unshortened failure traces are saved and byte-read-back before the
    whole private SHA is published. They are not repeated in every job's
    public execution. No scientific vector or old conclusion is removed.
    """
    raw=encode(state);digest=sha(raw)
    path=temporary/("TCF-private-"+role+"-transport-"+digest+".json")
    shared["atomic"](path,raw)
    require(path.read_bytes()==raw,"the entire private transport state has a complete byte readback")
    failure=state.get("failure")
    if failure is not None:
        trace=failure.get("traceback","").encode()
        failure={"type":failure["type"],"message":failure["message"],
            "complete_private_traceback_bytes":len(trace),"complete_private_traceback_sha256":sha(trace)}
    reads=[]
    for item in state.get("readme_checks",[]):
        reads.append({key:item[key] for key in
            ("started_utc","finished_utc","before","after","read_commit","reviewed_rules_sha256","readme_sha256")})
        reads[-1].update(complete_private_receipt_bytes=len(encode(item)),complete_private_receipt_sha256=sha(encode(item)),
            actual_diff_present=bool(item["actual_diff"]),diff_from_read_commit_present=bool(item["diff_from_read_commit"]))
    keys=("kind","repository","problem_id","input_manifest_path","run_id","run_attempt","event_commit",
        "started_utc","entry_checkout","actual_scientific_checkout","scientific_started_utc","scientific_finished_utc",
        "scientific_wall_seconds","finished_utc","actual_child_returncode","scientific_children","complete",
        "assignment","complete_assignment","accepted_complete_cells","next_cell","complete_original_domain",
        "original_TC_global_targets_complete","completed_natural_targets","old_completed_targets_recomputed",
        "old_numerical_producers_called","old_accepted_cells_evaluated","new_arrays_published","new_artifacts","new_Releases",
        "private_arrays_restored","whole_original_input_identity","complete_original_array_restoration",
        "terminal_parent_API","terminal_original_run_API","terminal_previous_fleet_API","terminal_jobs_API",
        "whole_private_scientific_log","failed_final_collection")
    result={key:state[key] for key in keys if key in state}
    result.update(public_execution_contract="TCF_complete_small_public_execution_v1",
        manifest_sha256=manifest_sha,fleet_identity_sha256=manifest["fleet_identity_sha256"],
        parent_identity_sha256=manifest["parent_identity_sha256"],failure=failure,
        scientific_files=state["scientific_files"],
        complete_original_manifest=manifest["terminal_parent_objects"]["manifest"],
        whole_input_graph="entire fleet manifest plus complete original manifest and every admitted carry edge",
        each_assignment_actual_with_accepted_cells_requires_four_whole_array_receipts=True,
        parameters_sha256=sha(encode(manifest["parameters"])),
        whole_private_transport_state={"file":path.name,"bytes":len(raw),"sha256":digest,
            "complete_readback":True,"original_restoration_and_retry_and_README_records_retained":True},
        readme_check_count=state["readme_check_count"],readme_receipt_chain_sha256=state["readme_receipt_chain_sha256"],
        complete_readme_audit=reads,publication_attempts=state["publication_attempts"])
    capacity=state.get("latest_publication_capacity")
    if capacity is not None:
        result["complete_capacity_receipt"]={"whole_private_bytes":len(encode(capacity)),"whole_private_sha256":sha(encode(capacity)),
            **{key:capacity[key] for key in ("head","topic_tree","topic_blob_bytes","blob_count")}}
    body=encode(result)
    require(len(body)<manifest["operation"]["maximum_execution_bytes"]==20000,
        "the entire new public execution contract fits its declared 20 KB limit")
    return body


def original_input_prefix(root):
    path=Path(root)/PARENT_WORKER
    require(sha(path.read_bytes())==PARENT_WORKER_SHA,"the entire actual TCXV public worker")
    original=load(path,"_TCF_original_public_transport")
    source=original.patched_source();tree=ast.parse(source)
    functions=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=="main"]
    require(len(functions)==1,"one whole original public main")
    function=functions[0];first=ast.parse("head = pull()").body[0]
    stops=[i for i,node in enumerate(function.body) if isinstance(node,ast.Try)
        and node.body and ast.dump(node.body[0])==ast.dump(first)]
    require(len(stops)==1,"one exact boundary before the old reservation and mathematical branch")
    function.body=function.body[:stops[0]]+ast.parse(TAIL).body
    fragment=ast.Module(body=[function],type_ignores=[]);ast.fix_missing_locations(fragment)
    namespace=dict(original.__dict__)
    exec(compile(fragment,"<TCF unchanged original native/publication prefix>","exec"),namespace)
    return namespace["main"]


def terminal_actions_parent(run):
    headers={"Accept":"application/vnd.github+json"}
    token=os.environ.get("GITHUB_TOKEN")
    if token:headers["Authorization"]="Bearer "+token
    request=urllib.request.Request("https://api.github.com/repos/"+REPO+"/actions/runs/"+run,headers=headers)
    with urllib.request.urlopen(request,timeout=60) as response:body=response.read()
    value=json.loads(body)
    require(str(value["id"])==run and value["run_attempt"]==1 and value["status"]=="completed"
        and value["conclusion"] is not None,"the real original public run has ended before any missing-cell allocation")
    return {"whole_API_response_bytes":len(body),"whole_API_response_sha256":sha(body),
        **{key:value[key] for key in ("id","run_attempt","status","conclusion","updated_at","html_url")}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True);parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);parser.add_argument("--ordinal",type=int,required=True)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one first-attempt public missing-cell assignment")
    root=args.repo.resolve();mpath=args.manifest if args.manifest.is_absolute() else root/args.manifest
    raw=mpath.read_bytes();manifest=json.loads(raw)
    require(len(raw)<100000 and sha(raw)==args.manifest_sha,"the whole actual fleet manifest")
    files={item["role"]:item for item in manifest["files"]}
    require(sha(Path(__file__).read_bytes())==files["worker"]["sha256"],"the actual public worker bytes")
    helper=load(root/files["helper"]["path"],"_TCF_public_metadata")
    ordinal=args.ordinal
    require(0<=ordinal<len(manifest["assignments"]),"one predeclared disjoint interval")
    op=manifest["operation"];marker=op["assignment_marker_base"]+"-%03d.json"%ordinal
    present=subprocess.run(["git","cat-file","-e","HEAD:"+marker],cwd=root,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if present.returncode==0:
        print("This complete missing-cell assignment is already reserved; no replay",flush=True);return
    actual_parent=terminal_actions_parent(helper.PARENT_RUN)
    old_args=sys.argv[:]
    try:
        sys.argv=[PARENT_WORKER,"--repo",str(root),"--manifest",str(root/helper.PARENT_MANIFEST),"--manifest-sha",helper.PARENT_MANIFEST_SHA]
        shared=original_input_prefix(root)()
    finally:sys.argv=old_args
    shared["configure_publication"](marker,op)
    state=shared["state"]
    state.update(kind="R149_original_TC_missing_cell_assignment_execution_v1",manifest_sha256=args.manifest_sha,
        input_manifest_path=str(mpath.relative_to(root)),problem_id=manifest["problem_id"],fleet_identity_sha256=manifest["fleet_identity_sha256"],
        assignment=manifest["assignments"][ordinal],terminal_parent_API=actual_parent,
        complete_assignment=False,original_TC_global_targets_complete=False,actual_child_returncode=None,
        scientific_files=[],complete=False,failure=None,new_target_order=[],completed_natural_targets=[])
    inputs,temp=shared["inputs"],shared["temporary"]
    run=os.environ["GITHUB_RUN_ID"]
    output_directory=op["output_base"]+"/run-"+run+"-1/assignment-%03d"%ordinal
    output=temp/("actual-missing-cells-%03d.json"%ordinal)
    immutable=temp/"TCF-manifest.json";shared["atomic"](immutable,raw)
    staged={};document=None;last_accepted=-1;child=None;began=None;log_path=None

    def current(head):
        require(sha(shared["git"]("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)==args.manifest_sha,
            "the same complete fleet manifest after every pull")
        def restore(spec):
            payload,unused=shared["checked_bytes"](spec,head)
            path=inputs/spec["path"]
            if path.exists():require(path.read_bytes()==payload,"shared original source has one entire identity")
            else:shared["atomic"](path,payload)
            return payload
        for spec in manifest["files"]:restore(spec)
        helper.materialize_carry(manifest["carry_union"],restore)
        state["fleet_whole_input_count"]=len(manifest["files"])
        state["fleet_whole_input_receipts_sha256"]=sha(encode(manifest["files"]))

    def collect():
        nonlocal document
        if not output.exists():return 0
        payload=output.read_bytes();require(0<len(payload)<manifest["parameters"]["maximum_actual_bytes"],"whole small actual assignment")
        document=json.loads(payload);helper.validate_slice(document,manifest,ordinal)
        require(document["manifest_sha256"]==args.manifest_sha and document["run_id"]==run
            and document["run_attempt"]=="1" and document["parameters"]==manifest["parameters"]
            and document["old_completed_matrix_or_norm_targets_called"]==document["new_arrays_published"]==0,
            "every preserved whole result has the actual source and input identity")
        staged[output_directory+"/actual-missing-cells.json"]=payload
        state["scientific_files"]=[{"path":path,"bytes":len(body),"sha256":sha(body)} for path,body in sorted(staged.items())]
        state["accepted_complete_cells"]=document["accepted_complete_cells"]
        state["next_cell"]=document["next_cell"];state["complete_assignment"]=document["complete_assignment"]
        restored=document["carrier_restoration"]
        if restored is not None:
            state["complete_original_array_restoration"]={
                "complete_original_arrays":restored["complete_original_arrays"],
                "whole_definition_sha256":restored["whole_definition_sha256"],"whole_plan_sha256":restored["whole_plan_sha256"],
                "whole_restoration_record_sha256":sha(encode(restored)),
                "whole_scientific_actual_sha256":sha(payload)}
        return document["accepted_complete_cells"]

    def outcome_files():
        body=compact_execution(state,shared,temp,manifest,args.manifest_sha,"assignment-%03d"%ordinal)
        return {**staged,output_directory+"/execution.json":body}

    global_marker=parent_marker(manifest,args.manifest_sha)

    def reservation_files():
        head=shared["git"]("rev-parse","HEAD").stdout.strip()
        if shared["git"]("cat-file","-e",head+":"+op["parent_marker"],check_return=False).returncode==0:
            previous=shared["git"]("show",head+":"+op["parent_marker"],binary=True).stdout
            require(previous==encode(global_marker),"one terminal parent has one exclusive fixed missing-cell fleet")
        return {op["parent_marker"]:encode(global_marker),marker:encode(assignment_marker(manifest,args.manifest_sha,ordinal,run,output_directory))}

    try:
        head=shared["pull"]();shared["materialize_original_metadata"](head);current(head)
        parent=helper.resolve_parent(inputs,manifest)
        if manifest["carry_union"] is not None:
            carry=json.loads((inputs/manifest["carry_union"]["union"]["path"]).read_bytes())
            state["terminal_previous_fleet_API"]=terminal_actions_parent(carry["run_id"])
        cap,unused=shared["capacity"](head)
        require(cap["topic_blob_bytes"]+op["maximum_fleet_publication_bytes"]+op["reserve_bytes"]<=op["topic_maximum_bytes"],
            "the full declared fleet publication fits the same topic capacity")
        shared["publish"](reservation_files,"visible-exact: reserve one exclusive TC missing interval",before_science=True)
        state["assignment_reserved_before_native_restoration"]=True
        shared["prepare_original"]()
        head=shared["pull"]();current(head)
        owner=load(inputs/files["science"]["path"],"_TCF_complete_new_scientific_owner")
        admitted=owner.admit(inputs,raw,args.manifest_sha,ordinal,shared["rows_index"])
        state["whole_original_input_identity"]=admitted[-1][-1];del admitted
        state["actual_scientific_checkout"]=head
        command=[sys.executable,"-u",str(inputs/files["science"]["path"]),"--manifest",str(immutable),
            "--manifest-sha",args.manifest_sha,"--ordinal",str(ordinal),"--input-root",str(inputs),
            "--rows-index",str(shared["rows_index"]),"--output",str(output),"--checkout",head]
        environment=dict(os.environ)
        for key in ("GITHUB_TOKEN","GIT_CONFIG_COUNT","GIT_CONFIG_KEY_0","GIT_CONFIG_VALUE_0"):environment.pop(key,None)
        environment.update(PYTHONDONTWRITEBYTECODE="1",OPENBLAS_CORETYPE="Haswell",OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",
            MKL_NUM_THREADS="1",BLIS_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1",NUMEXPR_NUM_THREADS="1")
        state["scientific_children"],state["scientific_started_utc"]=1,shared["utc"]()
        began=time.monotonic();next_pull=began+1800;next_scan=began+5;last_push=began
        child=subprocess.Popen(command,cwd=temp,env=environment,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector=selectors.DefaultSelector();selector.register(child.stdout,selectors.EVENT_READ)
        decoder=codecs.getincrementaldecoder("utf-8")();log_path=temp/"TCF-scientific.log"
        with log_path.open("wb") as log:
            try:
                while selector.get_map():
                    for key,unused in selector.select(timeout=2):
                        block=os.read(key.fileobj.fileno(),65536)
                        if block:log.write(block);log.flush();print(decoder.decode(block),end="",flush=True)
                        else:selector.unregister(key.fileobj)
                    now=time.monotonic()
                    if now>=next_scan:
                        count=collect();next_scan=now+5
                        if count>last_accepted and (now-last_push>=300 or document and document["complete_assignment"]):
                            state["intermediate_publication"]=shared["publish"](outcome_files,"visible-exact: preserve whole TC missing-cell prefix")
                            last_accepted=count;last_push=now
                    if now>=next_pull:current(shared["pull"]());next_pull=time.monotonic()+1800
                    require(now-began<op["child_timeout_seconds"],"save the complete assignment prefix at the actual child timeout")
            finally:
                if child.poll() is None:
                    child.terminate()
                    try:child.wait(timeout=30)
                    except subprocess.TimeoutExpired:child.kill();child.wait()
        state["actual_child_returncode"]=child.wait();state["scientific_finished_utc"]=shared["utc"]()
        state["scientific_wall_seconds"]=time.monotonic()-began
        state["whole_private_scientific_log"]={"bytes":log_path.stat().st_size,"sha256":sha(log_path.read_bytes())}
        collect()
        require(child.returncode==0 and document is not None and document["complete_assignment"] is True
            and document["actual_returncode"]==0 and document["failure"] is None,
            "every cell of this one fixed assignment completed; global TC is still separate")
        state["complete"]=True
    except BaseException as exc:
        state["complete"]=False
        state["failure"]={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()}
        if child is not None:
            if child.poll() is None:
                child.terminate()
                try:child.wait(timeout=30)
                except subprocess.TimeoutExpired:child.kill();child.wait()
            state["actual_child_returncode"]=child.returncode
            state["scientific_finished_utc"]=shared["utc"]()
            state["scientific_wall_seconds"]=time.monotonic()-began
            if log_path is not None and log_path.exists():
                state["whole_private_scientific_log"]={"bytes":log_path.stat().st_size,"sha256":sha(log_path.read_bytes())}
        try:collect()
        except BaseException as collection:
            state["failed_final_collection"]={"type":type(collection).__name__,"message":str(collection)}
    state["finished_utc"]=shared["utc"]()
    shared["publish"](outcome_files,"visible-exact: save complete TC missing-interval outcome")
    if state["failure"] is not None:raise RuntimeError(state["failure"]["message"])


if __name__=="__main__":main()
