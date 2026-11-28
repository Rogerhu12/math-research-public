"""CFC public entry using the unchanged SC transport/publication machinery.

Only the SC main prefix for complete original input restoration is called.
Its consumed-target branch and scientific owner are never called. Original
pull/README, capacity and non-fast-forward push loops are retained verbatim.
"""
from __future__ import annotations
import argparse, ast, codecs, hashlib, importlib.util, json, os, selectors
import subprocess, sys, time, traceback
from pathlib import Path
from types import SimpleNamespace

REPO="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby"
SC_WORKER=TOPIC+"/scripts/fourfold_codazzi_signed_finite_actual_public_worker.py"
SC_WORKER_SHA="ff4d9c4b0daa3fd1d6735447daa90d1649d854a97c5d1b6c507a865b8151a56a"
PREFIX_TAIL='''
def prepare_original():
    nonlocal owner
    head = pull()
    materialize_current(head)
    tc_manifest, tc_roles = materialize_original_TC()
    owner = load(inputs/by_role['science']['path'], '_CFC_original_SC_metadata')
    metadata = owner.metadata(inputs, raw_manifest, args.manifest_sha)
    state['whole_actual_predecessor_admission_before_native_restore'] = {
        'positive_records':[58,224,32], 'TC_targets':len(metadata['TC_owner'].TARGETS),
        'RW_rows':96, 'actual_JC_records':7, 'old_targets_called':0}
    del metadata
    restore_original_native(tc_manifest, tc_roles)
    admitted = owner.preflight(SimpleNamespace(input_root=str(inputs), manifest=str(immutable_manifest),
        manifest_sha=args.manifest_sha, rows_index=str(rows_index)))
    state['whole_original_input_admission_before_science'] = admitted['preflight_receipt']
    del admitted
    gc.collect()
    require(not any(name in sys.modules for name in ('numpy','flint','scipy')),
        'necessary original input restoration did not run an old scientific target')
    return head
def configure_publication(new_marker, new_operation):
    nonlocal marker_path, operation
    marker_path = topic_path(new_marker)
    require(new_operation['topic_maximum_bytes'] == LIMIT and new_operation['reserve_bytes'] == RESERVE,
        'same actual capacity units with the explicit new target reservation')
    operation = new_operation
return dict(root=root, inputs=inputs, temporary=temporary, rows_index=rows_index,
    state=state, pull=pull, capacity=capacity, publish=publish, checked_bytes=checked_bytes,
    fetch_commit=fetch_commit, git=git, utc=utc, atomic=atomic, encode=encode,
    prepare_original=prepare_original, configure_publication=configure_publication)
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def parse(raw):
    return json.loads(raw,parse_constant=lambda value:(_ for _ in ()).throw(ValueError(value)))


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def original_input_prefix(root):
    path=Path(root)/SC_WORKER;raw=path.read_bytes()
    require(sha(raw)==SC_WORKER_SHA,"whole frozen SC public input/publication machinery")
    original=load(path,"_CFC_frozen_original_SC_public_worker")
    tree=ast.parse(raw)
    functions=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=="main"]
    require(len(functions)==1,"one entire original SC main")
    function=functions[0]
    first=ast.parse("head = pull()").body[0]
    stops=[i for i,node in enumerate(function.body) if isinstance(node,ast.Try)
           and node.body and ast.dump(node.body[0])==ast.dump(first)]
    require(len(stops)==1,"one exact boundary before reservation and original scientific branch")
    function.body=function.body[:stops[0]]+ast.parse(PREFIX_TAIL).body
    fragment=ast.Module(body=[function],type_ignores=[]);ast.fix_missing_locations(fragment)
    namespace=dict(original.__dict__)
    exec(compile(fragment,"<CFC unchanged original input preparation prefix>","exec"),namespace)
    return namespace["main"]


def validate_actual(raw,manifest,digest,run):
    require(0<len(raw)<manifest["parameters"]["public_bytes"],"whole small CFC output")
    doc=parse(raw);count=len(doc["completed_targets"])
    require(doc["kind"]==manifest["scientific_kind"] and doc["manifest_sha256"]==digest
        and doc["run_id"]==run and doc["run_attempt"]=="1"
        and doc["parameters"]==manifest["parameters"] and sorted(doc)==manifest["allowed_scientific_fields"]
        and 0<=count<=10 and doc["completed_targets"]==manifest["target_order"][:count]
        and set(doc["new_records"])==set(doc["completed_targets"])
        and doc["old_scientific_targets_called"]==doc["new_arrays_published"]==0,
        "the entire same-input CFC target prefix")
    for index,name in enumerate(doc["completed_targets"]):
        value=doc["new_records"][name]
        if index in (0,1):
            require(value["complete_count"]==96 and len(value["bounds"])==96,"every complete96 scalar error")
        if index==2:require(value["all96_squared_column_errors_used"] is True,"whole joint norm, never column max")
        if index==3:
            require(value["stored_rows"]==2 and value["physical_mean_rank"]==1
                and value["complete_columns"]==96 and value["two_free_mean_unknowns_claimed"] is False,
                "the complete physical mean storage and rank")
        if index in (4,5,6):
            require(value["complete_count"]==96 and len(value["all96_PDE_correction_bounds"])==96
                and value["independent_Yb_Kb_and_raw_chart_ports_retained"] is True,"every corrected physical row")
        if index in (7,8):
            require(value["rows"]==value["columns"]==96 and value["signed_entry_count"]==9216
                and value["same_original_model_phase_and_C_inverse"] is True
                and value["complete_opposite_head_and_tail_retained"] is True,"whole signed original Theta block")
    if doc["complete"]:
        require(count==10 and doc["proved"] is True and doc["actual_returncode"]==0
            and doc["failure"] is None and doc["runtime"]==manifest["runtime"]
            and doc["result"]["physical_square_assembled"] is False
            and doc["result"]["full_Schur_inverse_proved"] is False
            and doc["result"]["topic_completion_proved"] is False,
            "all new columns and observations, with the remaining square independent")
    return doc


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True);parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True);args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one original public CFC execution")
    root=args.repo.resolve();mpath=args.manifest if args.manifest.is_absolute() else root/args.manifest
    raw_manifest=mpath.read_bytes();manifest=parse(raw_manifest)
    require(sha(raw_manifest)==args.manifest_sha and len(raw_manifest)<100000
        and manifest["kind"]=="R149_complete_original_TC96_full_target_columns_inputs_v1",
        "the whole CFC actual-entry manifest")
    by_role={item["role"]:item for item in manifest["files"]}
    require(len(by_role)==len(manifest["files"]) and sha(Path(__file__).read_bytes())==by_role["worker"]["sha256"],
        "the entire actually running CFC public source")
    already=subprocess.run(["git","cat-file","-e","HEAD:"+manifest["operation"]["consumed_marker"]],
        cwd=root,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if already.returncode==0:
        print("CFC target already reserved; no input or science replay",flush=True);return
    sc=manifest["parents"]["SC"];old_args=sys.argv[:]
    try:
        sys.argv=[SC_WORKER,"--repo",str(root),"--manifest",str(root/sc["manifest"]["path"]),
                  "--manifest-sha",sc["manifest"]["sha256"]]
        shared=original_input_prefix(root)()
    finally:sys.argv=old_args
    shared["configure_publication"](manifest["operation"]["consumed_marker"],manifest["operation"])
    state=shared["state"]
    state.update(kind="R149_complete_original_TC96_full_target_columns_execution_v1",
        problem_id=manifest["problem_id"],manifest_sha256=args.manifest_sha,
        original_SC_manifest_sha256=sc["manifest"]["sha256"],
        additional_parent_closures=[],CFC_current_input_receipts=[],scientific_children=0,
        complete=False,failure=None,actual_child_returncode=None,completed_natural_targets=[],scientific_files=[])
    inputs,temp=shared["inputs"],shared["temporary"]
    run=os.environ["GITHUB_RUN_ID"];op=manifest["operation"]
    output_dir=op["output_base"]+"/run-"+run+"-1"
    output=temp/"actual-complete-finite-columns.json"
    immutable=temp/"CFC-manifest.json";shared["atomic"](immutable,raw_manifest)
    staged={};doc=None;last_count=-1

    def restore(spec,head,small=True):
        raw,unused=shared["checked_bytes"](spec,head,small=small)
        path=inputs/spec["path"]
        if path.exists():require(path.read_bytes()==raw,"one common original input has one whole identity")
        else:shared["atomic"](path,raw)

    def current(head):
        require(sha(shared["git"]("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)==args.manifest_sha,
            "the same whole new manifest after every pull")
        for spec in manifest["files"]:restore(spec,head)
        state["CFC_current_input_receipts"]=manifest["files"]

    def parent_closure(tag):
        descriptor=manifest["parents"][tag]
        pm=parse((inputs/descriptor["manifest"]["path"]).read_bytes())
        execution=parse((inputs/descriptor["execution"]["path"]).read_bytes())
        checkout=execution["actual_scientific_checkout"]
        shared["fetch_commit"](checkout);receipts=[]
        for spec in pm["files"]+pm.get("historical_inputs",[]):
            if spec.get("reconstruct_only") is True:
                require((inputs/spec["path"]).is_file(),"the original SC direction reconstruction already supplied this whole input")
                raw=(inputs/spec["path"]).read_bytes()
                require(len(raw)==spec["bytes"] and sha(raw)==spec["sha256"],"whole reconstructed original input")
            else:
                commit=spec.get("commit",checkout);shared["fetch_commit"](commit)
                restore(spec,commit,small=spec in pm["files"])
            receipts.append({key:spec[key] for key in ("path","bytes","sha256")})
        state["additional_parent_closures"].append({"parent":tag,"original_checkout":checkout,
            "manifest_sha256":descriptor["manifest"]["sha256"],"complete_file_count":len(receipts),
            "whole_file_receipt_list_sha256":sha(encode(receipts))})

    def collect():
        nonlocal doc
        if not output.exists():return 0
        raw=output.read_bytes();doc=validate_actual(raw,manifest,args.manifest_sha,run)
        staged[output_dir+"/actual-complete-finite-columns.json"]=raw
        state["completed_natural_targets"]=doc["completed_targets"]
        state["scientific_files"]=[{"path":path,"bytes":len(value),"sha256":sha(value)} for path,value in sorted(staged.items())]
        state["original_scientific_complete"],state["original_scientific_failure"]=doc["complete"],doc["failure"]
        return len(doc["completed_targets"])

    def files():
        body=encode(state);require(len(body)<op["maximum_execution_bytes"],"whole CFC execution receipt")
        report=("# Original TC96 complete target columns and physical rows\n\nRun "+run+"/1; complete: "+str(state["complete"])+".\n\n"
            "Whole SC root96/P224, BFP/DCP and H96/AP96 precede the new all96 batch. The finite512 target trials, "
            "complete2560 images, all8192 points and full opposite2048 heads plus infinite tails are retained. "
            "The true target tail is paid as a whole Hilbert-space error. The same original columns receive full "
            "mean, phase and height corrections. Private arrays remain private. Complete signed high-response, "
            "world/chart/parameter rows and the remaining physical square are independent obligations.\n").encode()
        return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}

    try:
        shared["prepare_original"]()
        head=shared["pull"]();current(head)
        marker=op["consumed_marker"]
        if shared["git"]("cat-file","-e",head+":"+marker,check_return=False).returncode==0:
            print("CFC complete target already reserved; no scientific retry",flush=True);return
        for tag in ("DCP","H96","PWA96"):parent_closure(tag)
        owner=load(inputs/by_role["science"]["path"],"_CFC_new_whole_owner")
        admitted=owner.admit(inputs,raw_manifest,args.manifest_sha,shared["rows_index"])
        require(admitted["SC"]["TC"]["state"]["complete"] is True,"all complete old TC residuals precede new columns")
        del admitted
        cap,unused=shared["capacity"](head)
        require(cap["topic_blob_bytes"]+op["maximum_total_publication_bytes"]+op["reserve_bytes"]<=200000000,
            "whole topic capacity before all96 science")
        state["pre_execution_capacity"]=cap
        reservation={"kind":"consumed_complete_TC96_full_columns_v1","manifest_sha256":args.manifest_sha,
            "problem_id":manifest["problem_id"],"run_id":run,"run_attempt":"1","prepared_utc":shared["utc"](),
            "output_directory":output_dir,"automatic_scientific_retry":False,"old_completed_targets_may_be_recomputed":False}
        state["consumed_marker_publication"]=shared["publish"](lambda:{marker:encode(reservation)},
            "visible-exact: reserve complete original TC96 target columns",before_science=True)
        head=shared["pull"]();current(head);state["actual_scientific_checkout"]=head
        command=[sys.executable,"-u",str(inputs/by_role["science"]["path"]),"--manifest",str(immutable),
            "--manifest-sha",args.manifest_sha,"--input-root",str(inputs),"--rows-index",str(shared["rows_index"]),
            "--output",str(output),"--checkout",head]
        env=dict(os.environ)
        for key in ("GITHUB_TOKEN","GIT_CONFIG_COUNT","GIT_CONFIG_KEY_0","GIT_CONFIG_VALUE_0"):env.pop(key,None)
        env.update(PYTHONDONTWRITEBYTECODE="1",OPENBLAS_CORETYPE="Haswell",OPENBLAS_NUM_THREADS="1",
            OMP_NUM_THREADS="1",MKL_NUM_THREADS="1",BLIS_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1",NUMEXPR_NUM_THREADS="1")
        state["scientific_children"],state["scientific_started_utc"]=1,shared["utc"]()
        began=time.monotonic();next_pull=began+1800;next_scan=began+5
        child=subprocess.Popen(command,cwd=temp,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector=selectors.DefaultSelector();selector.register(child.stdout,selectors.EVENT_READ)
        decoder=codecs.getincrementaldecoder("utf-8")();log_path=temp/"CFC-scientific.log"
        with log_path.open("wb") as log:
            try:
                while selector.get_map():
                    now=time.monotonic()
                    if now>=next_scan:
                        count=collect()
                        if count>last_count and count>0:
                            shared["publish"](files,"visible-exact: preserve complete TC96 column conclusions")
                            last_count=count
                        next_scan=now+5
                    if now>=next_pull:
                        head=shared["pull"]();current(head);next_pull=now+1800
                    require(now-began<op["child_timeout_seconds"],"whole CFC timeout with actual prefix retained")
                    for key,unused in selector.select(timeout=1):
                        chunk=os.read(key.fileobj.fileno(),65536)
                        if chunk:log.write(chunk);sys.stdout.write(decoder.decode(chunk));sys.stdout.flush()
                        else:selector.unregister(key.fileobj)
            finally:
                if child.poll() is None:
                    child.terminate()
                    try:child.wait(timeout=20)
                    except subprocess.TimeoutExpired:child.kill();child.wait()
        state["actual_child_returncode"]=child.wait();collect()
        raw=log_path.read_bytes();state["complete_child_stdout"]={"bytes":len(raw),"sha256":sha(raw)}
        require(state["actual_child_returncode"]==0 and doc is not None and doc["complete"] is True
            and state["completed_natural_targets"]==manifest["target_order"],"all ten genuine new complete CFC conclusions")
        state["complete"]=True
    except BaseException as exc:
        state["failure"]={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()[-7000:]}
        try:collect()
        except BaseException as error:state["output_validation_failure"]={"type":type(error).__name__,"message":str(error)}
    state["finished_utc"]=shared["utc"]()
    shared["publish"](files,"visible-exact: preserve complete TC96 actual outcome")
    if not state["complete"]:raise RuntimeError("CFC actual outcome preserved; no automatic scientific retry")


if __name__=="__main__":main()
