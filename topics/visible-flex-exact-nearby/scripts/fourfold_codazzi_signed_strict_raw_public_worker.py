"""Public RCS entry with the whole original TCXV native/publication transport.

The extracted original prefix stops BEFORE any old reservation, trial, QR,
source or matrix target.  The same original whole native definitions and
restoration hashes are retained.  Only the new RCS owner is a science child.
"""
from __future__ import annotations
import argparse, ast, codecs, hashlib, importlib.util, json, os, selectors
import subprocess, sys, time, traceback
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
REPO = "Rogerhu12/math-research-public"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_signed_strict_raw_public_worker.py"
PARENT_WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_public_worker.py"
PARENT_WORKER_SHA = "0d06ee5d40c86e74e97a803ce8a35a80be98151327db082f694acb691f396a3e"
PARENT_MANIFEST = TOPIC+"/notes/2026-11-28-true-root-trial-complete2677-inputs.json"
PARENT_MANIFEST_SHA = "6b82d09170ed4ec780eccd0910cb69df98615390ef2f73237ed324d1e3f2c692"
TAIL = '''
def prepare_original():
    head = pull()
    materialize_current(head)
    restore_history()
    restore_rows()
    reconstruct_direction()
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
        "only the original necessary same-SHA native reconstruction child has run")
    return head
def configure_publication(marker, operation):
    nonlocal marker_path, op
    marker_path = topic_path(marker)
    require(operation["topic_maximum_bytes"] == LIMIT and operation["reserve_bytes"] == RESERVE,
        "unchanged entire topic capacity units")
    op = operation
return dict(root=root, inputs=inputs_root, temporary=temporary, rows_index=rows_index,
    state=state, pull=pull, capacity=capacity, publish=publish, checked_bytes=checked_bytes,
    git=git, utc=utc, atomic=atomic, encode=encode, fetch_commit=fetch_commit,
    prepare_original=prepare_original, configure_publication=configure_publication)
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(path,label):
    spec = importlib.util.spec_from_file_location(label,path)
    require(spec is not None and spec.loader is not None,"whole pinned source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[label] = module
    spec.loader.exec_module(module)
    return module


def original_input_prefix(root):
    path = Path(root)/PARENT_WORKER
    require(sha(path.read_bytes()) == PARENT_WORKER_SHA,
            "the entire actual original TCXV public worker")
    original = load(path,"_RCS_original_public_transport")
    source = original.patched_source()
    tree = ast.parse(source)
    functions = [node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name == "main"]
    require(len(functions) == 1,"one whole original public main")
    function = functions[0]
    first = ast.parse("head = pull()").body[0]
    stops = [i for i,node in enumerate(function.body) if isinstance(node,ast.Try)
             and node.body and ast.dump(node.body[0]) == ast.dump(first)]
    require(len(stops) == 1,"one exact boundary before the original science branch")
    function.body = function.body[:stops[0]]+ast.parse(TAIL).body
    fragment = ast.Module(body=[function],type_ignores=[])
    ast.fix_missing_locations(fragment)
    namespace = dict(original.__dict__)
    exec(compile(fragment,"<RCS unchanged whole original input/publication prefix>","exec"),namespace)
    return namespace["main"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one first-attempt public RCS entry")
    root = args.repo.resolve()
    mpath = args.manifest if args.manifest.is_absolute() else root/args.manifest
    raw = mpath.read_bytes()
    require(0 < len(raw) < 100000 and sha(raw) == args.manifest_sha,"one whole actual RCS manifest")
    manifest = json.loads(raw)
    files = {item["role"]:item for item in manifest["files"]}
    require(manifest["kind"] == "R149_complete_signed_strict_raw_inputs_v1"
            and manifest["repository"] == REPO and files["worker"]["path"] == SOURCE
            and sha(Path(__file__).read_bytes()) == files["worker"]["sha256"],
            "entire actually executing new worker")
    op = manifest["operation"]
    marker = op["consumed_marker"]
    require(marker.startswith(TOPIC+"/notes/") and ".." not in Path(marker).parts,
            "safe same-topic new target marker")
    present = subprocess.run(["git","cat-file","-e","HEAD:"+marker],cwd=root,
        stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if present.returncode == 0:
        print("This complete RCS target is already reserved; no automatic scientific replay",flush=True)
        return
    old_args = sys.argv[:]
    try:
        sys.argv = [PARENT_WORKER,"--repo",str(root),"--manifest",str(root/PARENT_MANIFEST),
                    "--manifest-sha",PARENT_MANIFEST_SHA]
        shared = original_input_prefix(root)()
    finally:
        sys.argv = old_args
    shared["configure_publication"](marker,op)
    state = shared["state"]
    state.update(kind="R149_complete_signed_strict_raw_execution_v1",manifest_sha256=args.manifest_sha,
        input_manifest_path=str(mpath.relative_to(root)),problem_id=manifest["problem_id"],
        complete=False,failure=None,actual_child_returncode=None,scientific_children=0,
        scientific_files=[],new_target_order=manifest["target_order"],completed_natural_targets=[],
        original_TC_scientific_target_calls=0,old_completed_targets_recomputed=0)
    inputs,temp = shared["inputs"],shared["temporary"]
    run = os.environ["GITHUB_RUN_ID"]
    output_directory = op["output_base"]+"/run-"+run+"-1"
    output,private = temp/"actual-signed-strict-raw.json",temp/"RCS-private"
    private.mkdir()
    immutable = temp/"RCS-manifest.json"
    shared["atomic"](immutable,raw)
    staged = {};document = None;owner = None

    def current(head):
        require(sha(shared["git"]("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)
                == args.manifest_sha,"one unchanged entire new manifest after every pull")
        for spec in manifest["files"]:
            payload,unused = shared["checked_bytes"](spec,head)
            path = inputs/spec["path"]
            if path.exists():
                require(path.read_bytes() == payload,"one whole same shared original input identity")
            else:
                shared["atomic"](path,payload)
        state["whole_new_current_input_count"] = len(manifest["files"])
        state["whole_new_current_input_receipts_sha256"] = sha(encode(manifest["files"]))

    def collect():
        nonlocal document
        if not output.exists():
            return
        payload = output.read_bytes()
        require(0 < len(payload) <= manifest["parameters"]["maximum_actual_bytes"],
                "one whole scientific actual or full prefix")
        value = json.loads(payload)
        owner.validate(value,manifest)
        require(value["identity"]["manifest_sha256"] == args.manifest_sha
                and value["identity"]["source_sha256"] == files["science"]["sha256"]
                and value["identity"]["run_id"] == run and value["identity"]["run_attempt"] == "1"
                and value["original_input_identity"] == state["whole_original_input_admission"],
                "actual whole new source and original raw identity")
        if document is not None:
            require(value["new_coefficient_cells_completed"] >= document["new_coefficient_cells_completed"],
                    "a saved complete coefficient prefix is never replaced by an earlier prefix")
        document = value
        staged[output_directory+"/actual-signed-strict-raw.json"] = payload
        state["scientific_files"] = [{"path":path,"bytes":len(body),"sha256":sha(body)}
                                     for path,body in sorted(staged.items())]
        state["completed_natural_targets"] = value["completed_targets"]
        state["actual_complete_new_cells"] = value["new_coefficient_cells_completed"]

    def outcome_files():
        collect()
        execution = encode(state)
        require(len(execution) < 100000,"whole unchanged original restoration plus new execution fits")
        report = ("# Actual complete signed strict coefficient and angular-inverse input\n\n"
            +"Run "+run+"/1; complete: "+str(state["complete"])+".\n\n"
            +"Every original scalar/cubic seam, the complete signed repaired base and direction, "
             "the same selected intrinsic perturbation, and the original physical mean remain. "
             "The new joint source coefficients and negative Sobolev windows use the complete same angular J. "
             "No old TC, WGS or WSM scientific target is called. The full genuine high boundary response, "
             "complete physical Schur inverse and final exact surface family remain separate obligations.\n").encode()
        return {**staged,output_directory+"/execution.json":execution,
                output_directory+"/report.md":report}

    try:
        head = shared["prepare_original"]()
        current(head)
        owner = load(inputs/files["science"]["path"],"_RCS_whole_new_owner_metadata")
        require(owner.PARAMETERS == manifest["parameters"] and owner.RUNTIME == manifest["runtime"],
                "the whole exact new owner contract")
        admitted = owner.admit(inputs,raw,args.manifest_sha,shared["rows_index"])
        state["whole_original_input_admission"] = admitted[-1][-1]
        del admitted
        require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
                "every old and new input was admitted before numerical import")
        from importlib.metadata import version
        import platform
        runtime = {"python":platform.python_version(),
                   "packages":{name:version(name) for name in manifest["runtime"]["packages"]}}
        require(runtime == manifest["runtime"],"entire fixed actual runtime metadata")
        state["actual_runtime"] = runtime
        capacity,unused = shared["capacity"](head)
        require(capacity["topic_blob_bytes"]+op["maximum_total_publication_bytes"]+op["reserve_bytes"]
                <= op["topic_maximum_bytes"],"whole topic room for every complete new output")
        state["pre_execution_capacity"] = capacity
        reservation = {"kind":"consumed_complete_signed_strict_raw_target_v1",
            "problem_id":manifest["problem_id"],"manifest_sha256":args.manifest_sha,
            "run_id":run,"run_attempt":"1","prepared_utc":shared["utc"](),
            "output_directory":output_directory,"automatic_scientific_retry":False,
            "old_completed_targets_may_be_recomputed":False,
            "target_order":manifest["target_order"],"status":"all_whole_original_inputs_admitted"}
        state["consumed_marker_publication"] = shared["publish"](
            lambda:{marker:encode(reservation)},"visible-exact: reserve complete signed strict raw input",True)
        head = shared["pull"]();current(head)
        state["actual_scientific_checkout"] = head
        command = [sys.executable,str(inputs/files["science"]["path"]),"--repo",str(inputs),
            "--manifest",str(immutable),"--manifest-sha",args.manifest_sha,
            "--rows-index",str(shared["rows_index"]),"--out",str(output),
            "--private",str(private),"--checkout",head]
        environment = dict(os.environ)
        for key in ("GITHUB_TOKEN","GIT_CONFIG_COUNT","GIT_CONFIG_KEY_0","GIT_CONFIG_VALUE_0"):
            environment.pop(key,None)
        environment.update(PYTHONDONTWRITEBYTECODE="1",OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",
                           MKL_NUM_THREADS="1",BLIS_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1")
        state["scientific_children"] = 1
        state["scientific_started_utc"] = shared["utc"]()
        began = time.monotonic();next_pull = began+1800;next_checkpoint = began+1200
        child = subprocess.Popen(command,cwd=temp,env=environment,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector = selectors.DefaultSelector();selector.register(child.stdout,selectors.EVENT_READ)
        decoder = codecs.getincrementaldecoder("utf-8")()
        timed_out = False
        with (temp/"RCS-child.log").open("wb") as log:
            while True:
                for key,unused in selector.select(timeout=5):
                    chunk = os.read(key.fileobj.fileno(),65536)
                    if chunk:
                        log.write(chunk);log.flush()
                        sys.stdout.write(decoder.decode(chunk));sys.stdout.flush()
                    else:
                        selector.unregister(key.fileobj)
                now = time.monotonic()
                if now >= next_pull:
                    head = shared["pull"]();current(head);next_pull = now+1800
                if now >= next_checkpoint:
                    collect()
                    if staged:
                        state["last_whole_prefix_publication"] = shared["publish"](
                            outcome_files,"visible-exact: preserve complete signed raw prefix")
                    next_checkpoint = now+1200
                if now-began > op["child_timeout_seconds"]:
                    child.terminate();timed_out = True
                if child.poll() is not None and not selector.get_map():
                    break
            sys.stdout.write(decoder.decode(b"",final=True));sys.stdout.flush()
        state["actual_child_returncode"] = child.wait()
        state["child_wall_seconds"] = time.monotonic()-began
        state["scientific_ended_utc"] = shared["utc"]()
        state["timed_out"] = timed_out
        collect()
        require(document is not None,"the complete new owner preserved a natural actual/prefix")
        state["original_scientific_complete"] = document["complete"]
        state["original_scientific_failure"] = document["failure"]
        state["complete"] = (state["actual_child_returncode"] == 0 and document["complete"]
                             and document["proved"] and not timed_out)
        require(state["complete"],"the new raw/global-J target did not finish; its whole prefix is retained")
    except Exception as exc:
        state["failure"] = {"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()}
        state["complete"] = False
    finally:
        state["finished_utc"] = shared["utc"]()
        if owner is not None:
            collect()
        state["final_publication"] = shared["publish"](
            outcome_files,"visible-exact: preserve complete signed strict raw result")
    require(state["complete"],"complete actual failure/prefix preserved without automatic replay")


if __name__ == "__main__":
    main()
