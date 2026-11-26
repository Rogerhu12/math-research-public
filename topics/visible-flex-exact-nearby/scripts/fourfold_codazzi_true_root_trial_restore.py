"""Restore TC inputs from Git and the unchanged original nodal answer.

The metadata generator calls build_plan without importing numerical
libraries.  Only public Actions calls reconstruct_direction, in a
separate process, using the original Hermite reconstruction program.
No QR solve, old residual target, or old norm target is run.
"""
from __future__ import annotations
import ast, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
SCRIPT = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_restore.py"
COMMIT = "7c130fb94528de8f003a43e7049fb42768a64eec"
BODY = TOPIC+"/notes/2026-11-14-R133-body-CI-pinned-inputs.json"
ROWS = TOPIC+"/notes/2026-11-15-R133-selected-parameter-core-scalar-fees-CI-inputs.json"
NODAL = TOPIC+"/data/body_regular_nodal_resume_20261114/manifest.json"
RECONSTRUCTOR = TOPIC+"/scripts/fourfold_codazzi_regular_trial_from_fixed_nodes.py"
OBJECT = TOPIC+"/data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"
Q_VECTOR = TOPIC+"/notes/2026-11-13-R133-regular-r25over8-q256-floating.json"
WAIST = TOPIC+"/notes/2026-11-14-R133-final-waist-complete-96-amplitude-row-rational.json"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def descriptor(path, raw):
    return dict(path=path,bytes=len(raw),sha256=sha(raw),git_blob_sha=blob(raw))


def build_plan(root, original_history):
    """Bind actual historical objects, not hypothetical index-relative paths."""
    require(not any(x in sys.modules for x in ("numpy","scipy","flint")),
            "TC restoration planning is metadata only")
    root = Path(root)
    body = json.loads((root/BODY).read_bytes())
    old_rows = json.loads((root/ROWS).read_bytes())
    nodal = json.loads((root/NODAL).read_bytes())
    require(nodal["complete"] is True and nodal["candidate_sha256"] == body["candidate_sha256"],
            "one complete original nodal state and background")

    def git(*args):
        return subprocess.run(["git",*args],cwd=root,check=True,capture_output=True).stdout

    def historical(path, expected, encoding, role):
        raw = git("show",COMMIT+":"+path)
        require(sha(raw) == expected,"actual original Git bytes: "+path)
        return dict(descriptor(path,raw),commit=COMMIT,encoding=encoding,
                    role=role,restore_only=True)

    # The exact original imports are retained; importing this metadata
    # module never imports or executes those historical numerical modules.
    scripts = root/TOPIC/"scripts"
    pending,seen = [Path(RECONSTRUCTOR).stem],set()
    while pending:
        name = pending.pop()
        if name in seen:
            continue
        seen.add(name)
        source = scripts/(name+".py")
        for node in ast.walk(ast.parse(source.read_text(),filename=str(source))):
            names = ([node.module] if isinstance(node,ast.ImportFrom) else
                     [x.name for x in node.names] if isinstance(node,ast.Import) else [])
            for imported in names:
                if imported and (scripts/(imported.split(".")[0]+".py")).is_file():
                    pending.append(imported.split(".")[0])
    current = []
    paths = [TOPIC+"/scripts/"+name+".py" for name in sorted(seen)]
    paths += [OBJECT,Q_VECTOR,WAIST,NODAL,
              str(Path(NODAL).parent/"response-finite-native.json"),
              str(Path(NODAL).parent/"response-nonmean.json")]
    for path in paths:
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000 and sha(raw) == body["files"][path],
                "entire unchanged original reconstruction input: "+path)
        raw.decode("utf-8")
        current.append(descriptor(path,raw))

    history,generated = [],[]
    for source in original_history:
        item = dict(source)
        if item["role"].startswith("direction_part"):
            # These files were never committed at their index-relative
            # path. Their original exact bytes remain the required output.
            item.pop("commit",None)
            item.update(restore_only=False,reconstruct_only=True,
                        reconstruction="unchanged_original_nodal_Hermite")
            generated.append(item)
        else:
            raw = git("show",item["commit"]+":"+item["path"])
            require(len(raw) == item["bytes"] and sha(raw) == item["sha256"]
                    and ("git_blob_sha" not in item or blob(raw) == item["git_blob_sha"]),
                    "each original restored input has an actually existing complete Git source")
            history.append(item)
    entry = nodal["roles"]["response"]
    for index,part in enumerate(entry["parts"]):
        path = str(Path(NODAL).parent/part["file"])
        item = historical(path,part["compressed_sha256"],"opaque-bytes","nodal_response_%d"%index)
        require(item["bytes"] == part["compressed_bytes"],"complete original nodal range size")
        history.append(item)
    definition = json.loads((root/OBJECT).read_bytes())
    for key in ("origin_inputs","direction"):
        item = definition[key]
        path = TOPIC+"/"+item["path"]
        require(item["sha256"] == body["files"][path],"same geometry input identity")
        history.append(historical(path,item["sha256"],"opaque-bytes","original_geometry_"+key))
    require(len(generated) == 14,"all fourteen original full physical direction shards")

    # All forty original row objects survive in Git. The former archive
    # dependency is unnecessary, and no old enclosure is regenerated.
    expected = {tuple(x["indices"]):x["sha256"] for x in old_rows["original_complete_native_part_sha256"]}
    located = {tuple(x["indices"]):x["path"] for x in old_rows["historical_natural_parts"]}
    prefix = TOPIC+"/notes/correlated_body_ci/run-43583838026-1-rows"
    names = git("ls-tree","-r","--name-only",COMMIT,"--",TOPIC+"/notes/correlated_body_ci").decode().splitlines()
    for path in names:
        match = re.search(r"/native/rows-(\d+)-(\d+)\.json\.gz$",path)
        if path.startswith(prefix) and match:
            key = tuple(map(int,match.groups()))
            if key in expected:
                require(key not in located,"one original row object for each exact natural interval")
                located[key] = path
    require(set(located) == set(expected) and len(located) == 40,
            "all forty original complete row objects are located in actual Git history")
    rows = []
    for key,path in sorted(located.items()):
        item = historical(path,expected[key],"gzip-json","original_rows_%d_%d"%key)
        item["indices"] = list(key)
        rows.append(item)
    plan = dict(kind="TC_exact_original_Git_rows_and_nodal_Hermite_v1",
        nodal_manifest=NODAL,reconstructor=RECONSTRUCTOR,object=OBJECT,
        q_vector=Q_VECTOR,waist_row=WAIST,
        original_runtime={"python":body["python_version"],"packages":body["packages"]},
        original_container="python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7",
        original_reconstruction_OPENBLAS_CORETYPE="unset",
        original_successful_reconstruction_run="43583838026/1",
        original_successful_reconstruction_job=132414020963,
        original_nodal_answer_sha256=entry["original_sha256"],
        original_cubic_sha256=entry["original_cubic"]["sha256"],
        expected_cubic_pieces=6144,expected_direction_shards=14,
        generated_direction_inputs=generated,original_rows=rows,
        reconstruction_timeout_seconds=900,old_QR_or_residual_or_norm_targets=0,
        new_array_publication=False,original_artifacts_required=False)
    return current,history+generated,plan


def restore_rows(plan, inputs_root, checked_bytes, fetch_commit, atomic):
    require(plan["kind"] == "TC_exact_original_Git_rows_and_nodal_Hermite_v1",
            "one actual original-input restoration plan")
    directory = Path(inputs_root)/"original-natural-row-parts"
    parts,receipts = [],[]
    for item in plan["original_rows"]:
        fetch_commit(item["commit"])
        raw,observed = checked_bytes(item,item["commit"],small=False)
        first,last = item["indices"]
        path = directory/("original-%d-%d.json.gz"%(first,last))
        atomic(path,raw)
        receipt = {"indices":item["indices"],"bytes":len(raw),"sha256":sha(raw)}
        receipts.append(receipt)
        parts.append(dict(receipt,file=str(path.relative_to(inputs_root))))
    require(len(parts) == 40,"forty complete original native parts restored from Git")
    return parts,receipts


def reconstruct_direction(plan, inputs_root, temporary, roles, state):
    """One separately counted necessary input reconstruction, no target replay."""
    import importlib.metadata, platform
    inputs_root,temporary = Path(inputs_root),Path(temporary)
    runtime = {"python":platform.python_version(),"packages":{
        name:importlib.metadata.version(name) for name in plan["original_runtime"]["packages"]}}
    require(runtime == plan["original_runtime"],"the unchanged original Hermite runtime")
    work,trials,out = temporary/"reconstruct-work",temporary/"reconstructed-direction",temporary/"input-reconstruction.json"
    command = [sys.executable,"-u",str(inputs_root/plan["reconstructor"]),
        "--nodal-manifest",str(inputs_root/plan["nodal_manifest"]),"--role","response",
        "--candidate",str(inputs_root/roles["base_index"]["path"]),
        "--object",str(inputs_root/plan["object"]),"--q-vector",str(inputs_root/plan["q_vector"]),
        "--waist-row",str(inputs_root/plan["waist_row"]),"--work",str(work),
        "--trial-directory",str(trials),"--out",str(out)]
    environment = dict(os.environ)
    for key in ("GITHUB_TOKEN","GIT_CONFIG_COUNT","GIT_CONFIG_KEY_0","GIT_CONFIG_VALUE_0"):
        environment.pop(key,None)
    require(plan["original_reconstruction_OPENBLAS_CORETYPE"] == "unset",
            "the original successful reconstruction did not force a BLAS core")
    environment.pop("OPENBLAS_CORETYPE",None)
    environment.update(PYTHONDONTWRITEBYTECODE="1",
        OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",MKL_NUM_THREADS="1",
        BLIS_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1",NUMEXPR_NUM_THREADS="1")
    record = dict(necessary_input_reconstruction=True,old_QR_solve_called=False,
        old_residual_or_norm_targets_called=0,complete=False,actual_returncode=None,
        runtime=runtime,new_arrays_published=0,
        reconstruction_OPENBLAS_CORETYPE="unset",
        original_container=plan["original_container"],
        actual_platform=platform.platform(),actual_libc=list(platform.libc_ver()))
    state["necessary_input_reconstruction"] = record
    state["necessary_input_reconstruction_children"] = 1
    state["old_numerical_producers_called"] = 1
    began = time.monotonic()
    with (temporary/"input-reconstruction.log").open("wb") as log:
        child = subprocess.run(command,cwd=inputs_root/TOPIC,env=environment,
            stdout=log,stderr=subprocess.STDOUT,timeout=plan["reconstruction_timeout_seconds"])
    record.update(actual_returncode=child.returncode,wall_seconds=time.monotonic()-began)
    if out.exists():
        raw = out.read_bytes()
        require(len(raw) < 15000,"small complete original reconstruction outcome")
        actual = json.loads(raw)
        record.update(actual_report=actual,actual_report_bytes=len(raw),actual_report_sha256=sha(raw))
    require(child.returncode == 0 and out.exists(),"the original nodal Hermite input reconstruction completed")
    require(actual["complete"] is True and actual["failure"] is None
        and actual["finite_QR_solve_reexecuted"] is False
        and actual["original_answer_sha256"] == plan["original_nodal_answer_sha256"]
        and actual["actual_reconstructed_cubic_sha256"] == plan["original_cubic_sha256"]
        and actual["all_original_shards_match"] is True
        and actual["trial_piece_count"] == plan["expected_cubic_pieces"],
        "entire original nodal answer, original cubic and original full shards match")
    receipts = []
    for item in plan["generated_direction_inputs"]:
        source = trials/Path(item["path"]).name
        raw = source.read_bytes()
        require(len(raw) == item["bytes"] and sha(raw) == item["sha256"],
                "each entire original physical direction shard is reconstructed exactly")
        destination = inputs_root/item["path"]
        require(not destination.exists(),"do not overwrite any original restored direction input")
        destination.parent.mkdir(parents=True,exist_ok=True)
        source.replace(destination)
        receipts.append({"path":item["path"],"bytes":len(raw),"sha256":sha(raw)})
    require(len(receipts) == plan["expected_direction_shards"],"all fourteen exact direction inputs")
    record.update(complete=True,complete_direction_input_receipts=receipts,
                  whole_original_cubic_SHA_verified=True)
    return record
