"""TCF terminal fleet merge: whole accepted union, then missing full norms.

Runs only after every fixed interval job has ended. No original trial,
coefficient, old matrix or accepted cell is evaluated. Each new complete
conclusion is pushed before the scalar child may form the next one.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, selectors, subprocess, sys, time, traceback, urllib.request
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
REPO="Rogerhu12/math-research-public"


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def merge_marker(manifest,manifest_sha,run,output_directory):
    return {"kind":"consumed_complete_original_TC_terminal_union_merge_v1","run_id":run,"run_attempt":"1",
            "manifest_sha256":manifest_sha,"fleet_identity_sha256":manifest["fleet_identity_sha256"],
            "old_completed_targets_may_be_recomputed":False,"automatic_scientific_retry":False,
            "output_directory":output_directory}


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def terminal_jobs(run,count):
    receipts=[];jobs=[];page=1
    while True:
        request=urllib.request.Request("https://api.github.com/repos/"+REPO+"/actions/runs/"+run+
            "/jobs?filter=latest&per_page=100&page="+str(page),headers={
                "Authorization":"Bearer "+os.environ["GITHUB_TOKEN"],"Accept":"application/vnd.github+json"})
        with urllib.request.urlopen(request,timeout=60) as response:raw=response.read()
        value=json.loads(raw);receipts.append({"page":page,"bytes":len(raw),"sha256":sha(raw)})
        jobs.extend(value["jobs"])
        if len(jobs)>=value["total_count"]:break
        require(value["jobs"],"the entire real job listing is present");page+=1
    selected=[]
    for ordinal in range(count):
        found=[job for job in jobs if job["name"]=="TCF original cells %d"%ordinal]
        require(len(found)==1 and str(found[0]["run_id"])==run and found[0]["run_attempt"]==1
            and found[0]["status"]=="completed" and found[0]["conclusion"] is not None,
            "every declared original-cell job has really ended")
        selected.append({key:found[0][key] for key in
            ("id","run_id","run_attempt","name","status","conclusion","started_at","completed_at","html_url")})
    return selected,{"whole_pages":receipts,"complete_assignment_job_count":count,
        "all_assignment_jobs_really_terminal":True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True);parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one first public terminal-union merge")
    root=args.repo.resolve();mpath=args.manifest if args.manifest.is_absolute() else root/args.manifest
    raw=mpath.read_bytes();manifest=json.loads(raw)
    require(len(raw)<100000 and sha(raw)==args.manifest_sha,"the entire real fleet manifest")
    roles={item["role"]:item for item in manifest["files"]}
    require(sha(Path(__file__).read_bytes())==roles["merge_worker"]["sha256"],"the whole actual merge worker")
    helper=load(root/roles["helper"]["path"],"_TCF_merge_metadata")
    transport=load(root/roles["worker"]["path"],"_TCF_original_transport_reuse")
    old_args=sys.argv[:]
    try:
        sys.argv=[transport.PARENT_WORKER,"--repo",str(root),"--manifest",str(root/helper.PARENT_MANIFEST),
            "--manifest-sha",helper.PARENT_MANIFEST_SHA]
        shared=transport.original_input_prefix(root)()
    finally:sys.argv=old_args
    op=dict(manifest["operation"]);op["maximum_total_publication_bytes"]=op["maximum_merge_publication_bytes"]
    marker=op["merge_marker"];shared["configure_publication"](marker,op)
    state=shared["state"];run=os.environ["GITHUB_RUN_ID"]
    state.update(kind="R149_original_TC_terminal_union_execution_v1",manifest_sha256=args.manifest_sha,
        input_manifest_path=str(mpath.relative_to(root)),problem_id=manifest["problem_id"],
        fleet_identity_sha256=manifest["fleet_identity_sha256"],complete=False,failure=None,
        new_target_order=[],completed_natural_targets=[],old_accepted_cells_evaluated=0,
        private_arrays_restored=0,scientific_files=[])
    inputs,temp=shared["inputs"],shared["temporary"]
    output=temp/"terminal-union-output";immutable=temp/"TCF-manifest.json";shared["atomic"](immutable,raw)
    output_directory=op["output_base"]+"/run-"+run+"-1/aggregate"
    staged={};captured={};published=set();child=None;began=None;log_path=None;parent=None

    def current(head):
        require(sha(shared["git"]("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)==args.manifest_sha,
            "the same complete fleet contract after every pull")
        def restore(spec):
            body,unused=shared["checked_bytes"](spec,head);path=inputs/spec["path"]
            if path.exists():require(path.read_bytes()==body,"one immutable whole shared input")
            else:shared["atomic"](path,body)
            return body
        for spec in manifest["files"]:restore(spec)
        helper.materialize_carry(manifest["carry_union"],restore)

    def observe(head,path):
        if shared["git"]("cat-file","-e",head+":"+path,check_return=False).returncode:return None
        body=shared["git"]("show",head+":"+path,binary=True).stdout
        require(0<len(body)<100000,"one entire published interval object")
        body.decode();shared["atomic"](inputs/path,body)
        return helper.descriptor(inputs,path)

    def collect():
        if not output.exists() or not (output/"actual-accepted-union.json").exists():return
        if any(not (output/parent["owner"].FILES[key]).exists() for key in parent["completed_natural_keys"]):return
        body=(output/"actual-accepted-union.json").read_bytes();union=json.loads(body)
        require(0<len(body)<95000 and union["kind"]==helper.UNION_KIND and union["aggregation_complete"] is True
            and union["actual_returncode"]==0 and union["failure"] is None
            and union["manifest_sha256"]==args.manifest_sha and union["run_id"]==run and union["run_attempt"]=="1"
            and union["fleet_identity_sha256"]==manifest["fleet_identity_sha256"]
            and union["source_records"]==merge["source_records"]
            and union["terminal_jobs_API"]==merge["terminal_jobs_API"]
            and union["old_accepted_cells_evaluated"]==union["old_completed_matrix_or_norm_targets_called"]==0
            and union["private_arrays_restored"]==union["new_arrays_published"]==0,
            "the complete new scalar-union output and its exact inputs")
        helper.validate_sums(union["squared_norm_upper_exact_binary64"])
        require(union["accepted_intervals"]==expected_intervals
            and union["accepted_complete_cells"]==sum(b-a for a,b in expected_intervals)
            and union["missing_intervals"]==helper.missing_intervals(expected_intervals)
            and union["complete_original_domain"] is (union["accepted_complete_cells"]==7724),
            "every original accepted cell occurs exactly once in the complete recorded domain")
        captured["union"]=union;staged[output_directory+"/actual-accepted-union.json"]=body
        for key in ("matrix","negative","positive"):
            path=output/parent["owner"].FILES[key]
            if not path.exists():continue
            data=path.read_bytes();document=json.loads(data)
            if key in parent["completed_natural_keys"]:
                require(data==helper.require_whole(inputs,parent["specs"][key]),"every old completed conclusion copied verbatim")
            else:
                require(union["complete_original_domain"] is True,"no incomplete norm is presented as complete")
                parent["owner"].validate_complete_result(document,key,parent["documents"]["state"]["proposal"],
                    args.manifest_sha,parent["documents"]["state"]["input_identity"]["same_selected_family"])
            require(len(data)<100000,"one whole original natural-target conclusion")
            captured[key]=document;staged[output_directory+"/"+path.name]=data
        state["accepted_complete_cells"]=union["accepted_complete_cells"]
        state["complete_original_domain"]=union["complete_original_domain"]
        state["completed_natural_targets"]=[target for key,target in zip(("matrix","negative","positive"),parent["owner"].TARGETS)
            if key in captured]
        state["scientific_files"]=[{"path":path,"bytes":len(data),"sha256":sha(data)} for path,data in sorted(staged.items())]

    def files():
        body=transport.compact_execution(state,shared,temp,manifest,args.manifest_sha,"whole-union")
        return {**staged,output_directory+"/execution.json":body}

    try:
        head=shared["pull"]()
        if shared["git"]("cat-file","-e",head+":"+marker,check_return=False).returncode==0:
            print("The exact whole-union merge was already consumed; no numerical replay",flush=True);return
        shared["materialize_original_metadata"](head);current(head)
        parent=helper.resolve_parent(inputs,manifest)
        state["whole_original_input_identity"]=parent["documents"]["state"]["input_identity"]
        state["complete_original_array_restoration"]={
            "original_four_array_identity":parent["documents"]["state"]["proposal"]["complete_endpoint_arrays"],
            "arrays_restored_in_merge":False,
            "all_new_job_whole_restoration_records_bound_by_source_records":True}
        state["terminal_original_run_API"]=transport.terminal_actions_parent(helper.PARENT_RUN)
        if manifest["carry_union"] is not None:
            previous=json.loads((inputs/manifest["carry_union"]["union"]["path"]).read_bytes())
            state["terminal_previous_fleet_API"]=transport.terminal_actions_parent(previous["run_id"])
        jobs,api_receipt=terminal_jobs(run,len(manifest["assignments"]))
        source_records=[]
        for ordinal,job in enumerate(jobs):
            directory=op["output_base"]+"/run-"+run+"-1/assignment-%03d"%ordinal
            source_records.append({"ordinal":ordinal,"job":job,
                "actual":observe(head,directory+"/actual-missing-cells.json"),
                "execution":observe(head,directory+"/execution.json")})
        merge={"manifest_sha256":args.manifest_sha,"run_id":run,"run_attempt":"1",
            "all_original_assignment_jobs_really_terminal":True,"terminal_jobs_API":api_receipt,"source_records":source_records}
        validation=dict(manifest);validation["_whole_manifest_sha256"]=args.manifest_sha
        documents=helper.read_job_records(inputs,validation,source_records,run)
        expected_intervals=helper.accepted_with_documents(parent,manifest,documents)
        state["terminal_jobs_API"]=api_receipt
        merge_path=temp/"complete-terminal-merge-input.json";shared["atomic"](merge_path,encode(merge))
        reservation=merge_marker(manifest,args.manifest_sha,run,output_directory)
        shared["publish"](lambda:{marker:encode(reservation)},"visible-exact: reserve whole TC terminal-union merge",before_science=True)
        command=[sys.executable,"-u",str(inputs/roles["science"]["path"]),"--aggregate","--manifest",str(immutable),
            "--manifest-sha",args.manifest_sha,"--input-root",str(inputs),"--merge-input",str(merge_path),
            "--output",str(output),"--checkout",head]
        environment=dict(os.environ)
        for key in ("GITHUB_TOKEN","GIT_CONFIG_COUNT","GIT_CONFIG_KEY_0","GIT_CONFIG_VALUE_0"):environment.pop(key,None)
        environment["PYTHONDONTWRITEBYTECODE"]="1"
        state["scientific_children"],state["scientific_started_utc"]=1,shared["utc"]()
        began=time.monotonic();log_path=temp/"TCF-whole-union.log"
        child=subprocess.Popen(command,cwd=temp,env=environment,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector=selectors.DefaultSelector();selector.register(child.stdout,selectors.EVENT_READ)
        with log_path.open("wb") as log:
            while selector.get_map():
                for key,unused in selector.select(timeout=.5):
                    block=os.read(key.fileobj.fileno(),65536)
                    if block:log.write(block);log.flush();print(block.decode("utf-8","replace"),end="",flush=True)
                    else:selector.unregister(key.fileobj)
                collect()
                for key in ("union","negative","positive"):
                    if key not in captured or key in published or key in parent["completed_natural_keys"]:continue
                    shared["publish"](files,"visible-exact: save complete TC "+key+" conclusion")
                    shared["atomic"](output/("published-"+key+".ack"),(args.manifest_sha+"\n").encode())
                    published.add(key)
                require(time.monotonic()-began<1200,"whole scalar aggregation timeout preserves every completed target")
        state["actual_child_returncode"]=child.wait();state["scientific_finished_utc"]=shared["utc"]()
        state["scientific_wall_seconds"]=time.monotonic()-began
        state["whole_private_scientific_log"]={"bytes":log_path.stat().st_size,"sha256":sha(log_path.read_bytes())}
        collect();require(child.returncode==0 and "union" in captured,"one actual complete accepted-union aggregation")
        require(not captured["union"]["complete_original_domain"] or all(key in captured for key in ("matrix","negative","positive")),
            "a complete original domain has every original full source conclusion")
        state["complete"]=True
    except BaseException as exc:
        state["complete"]=False
        state["failure"]={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()}
        if child is not None:
            if child.poll() is None:
                child.terminate()
                try:child.wait(timeout=30)
                except subprocess.TimeoutExpired:child.kill();child.wait()
            state["actual_child_returncode"]=child.returncode;state["scientific_finished_utc"]=shared["utc"]()
            state["scientific_wall_seconds"]=time.monotonic()-began
            if log_path is not None and log_path.exists():
                state["whole_private_scientific_log"]={"bytes":log_path.stat().st_size,"sha256":sha(log_path.read_bytes())}
        try:collect()
        except BaseException as collection:state["failed_final_collection"]={"type":type(collection).__name__,"message":str(collection)}
    state["finished_utc"]=shared["utc"]()
    shared["publish"](files,"visible-exact: save whole terminal TC fleet outcome")
    if state["failure"] is not None:raise RuntimeError(state["failure"]["message"])


if __name__=="__main__":main()
