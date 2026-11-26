"""One complete true-root finite-trial target with whole old input restoration.

Only the new TC owner is a numerical child.  Old whole arrays are restored
from their exact original history/archives and named pure readers only.
A new complete natural conclusion is published immediately.  Every public
radial checkpoint is a whole all96/all5-source prefix, never a progress
counter standing in for a residual.  No private coefficient array is uploaded.
"""
from __future__ import annotations
import argparse, ast, base64, codecs, gc, gzip, hashlib, importlib.util, json, math, os
from pathlib import Path
import selectors, shutil, subprocess, sys, tempfile, time, traceback
import urllib.request, urllib.error, urllib.parse, zipfile
from datetime import datetime, timezone
from types import SimpleNamespace

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
LIMIT, RESERVE = 200000000, 120000
OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py"
TARGETS = ["complete_signed_finite_trial_matrices_and_waist96",
           "complete_negative_finite_trial_sources96",
           "complete_positive_finite_trial_sources96"]
FILES = {"state":"actual-trial-state.json","matrix":"complete-signed-trial-matrices.json",
         "negative":"complete-negative-trial-sources.json",
         "positive":"complete-positive-trial-sources.json",
         "prefix":"complete-radial-integration-prefix.json"}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


def atomic(path,raw):
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp = path.with_name(path.name+".candidate")
    with tmp.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    require(tmp.read_bytes() == raw,"whole metadata candidate readback")
    tmp.replace(path)
    require(path.read_bytes() == raw,"whole formal metadata readback")


def topic_path(value):
    require(isinstance(value,str) and value.startswith(TOPIC+"/")
            and all(x not in ("",".","..") for x in value.split("/")),
            "safe authorized topic path")
    return value


def emit(name,raw):
    print("BEGIN COMPLETE PUBLIC FILE "+name+" bytes="+str(len(raw))+" sha256="+sha(raw),flush=True)
    sys.stdout.write(raw.decode())
    sys.stdout.flush()
    print("END COMPLETE PUBLIC FILE "+name,flush=True)


def import_source(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo","manifest","manifest-sha"):
        parser.add_argument("--"+name,required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one first-attempt public target")
    root = Path(args.repo).resolve()
    os.chdir(root)
    def git(*argv,check_return=True,binary=False,stdout=None):
        command = ["git","-c","user.name=github-actions[bot]",
            "-c","user.email=41898282+github-actions[bot]@users.noreply.github.com",*argv]
        if stdout is None:
            p = subprocess.run(command,cwd=root,capture_output=True,text=not binary)
        else:
            p = subprocess.run(command,cwd=root,stdout=stdout,stderr=subprocess.PIPE)
        if check_return and p.returncode:
            err = p.stderr.decode("utf-8","replace") if isinstance(p.stderr,bytes) else p.stderr
            raise RuntimeError("git "+" ".join(argv)+" failed: "+err)
        return p
    token = os.environ["GITHUB_TOKEN"]
    auth = base64.b64encode(("x-access-token:"+token).encode()).decode()
    os.environ.update(GIT_CONFIG_COUNT="1",GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
                      GIT_CONFIG_VALUE_0="AUTHORIZATION: basic "+auth)
    run,attempt = os.environ["GITHUB_RUN_ID"],os.environ["GITHUB_RUN_ATTEMPT"]
    mpath = Path(args.manifest)
    if not mpath.is_absolute():
        mpath = root/mpath
    raw_manifest = mpath.read_bytes()
    require(0 < len(raw_manifest) < 100000 and sha(raw_manifest) == args.manifest_sha,
            "one complete exact finite-trial manifest")
    manifest = parse(raw_manifest)
    require(manifest["repository"] == REPO
            and manifest["kind"] == "R149_true_root_finite_trial_complete_inputs_v1"
            and manifest["scientific_kind"] == "R149_complete_true_root_finite_trial_residuals_v1"
            and manifest["stage"] == "true_root_finite_trial_residuals"
            and manifest["target_order"] == TARGETS
            and (manifest["continuation"] is None or
                 (isinstance(manifest["continuation"],dict)
                  and manifest["continuation"].get("kind")
                      == "R149_same_exact_trial_complete_prefix_continuation_v1")),
            "complete finite trial only, with an optional whole actual predecessor")
    op = manifest["operation"]
    require(op["topic_maximum_bytes"] == LIMIT and op["reserve_bytes"] == RESERVE
            and op["readme_pull_interval_seconds"] == 1800
            and op["automatic_scientific_retry"] is False
            and op["maximum_total_publication_bytes"] == 170000,
            "same full capacity, hourly rules and explicit no-repeat scope")
    specs,history_specs = manifest["files"],manifest["historical_inputs"]
    all_specs = specs+history_specs
    by_path = {item["path"]:item for item in all_specs}
    require(len(by_path) == len(all_specs)
            and len(specs) == manifest["expected_current_input_count"]
            and len(history_specs) == manifest["expected_historical_input_count"],
            "complete unique current and original input closure")
    roles = {role:by_path[path] for role,path in manifest["roles"].items()}
    require(roles["owner"]["path"] == OWNER and roles["worker"]["path"] == WORKER,
            "one fixed actual owner and public worker")
    marker_path = topic_path(op["consumed_marker"])
    output_dir = topic_path(op["output_base"]+"/run-"+run+"-"+attempt)
    temporary = Path(tempfile.mkdtemp(prefix="actual-true-root-trials-",dir=os.environ.get("RUNNER_TEMP")))
    inputs_root,output,private = temporary/"complete-input-tree",temporary/"conclusions",temporary/"private"
    for directory in (inputs_root,output,private):
        directory.mkdir()
    immutable_manifest,rows_index = temporary/"manifest.json",inputs_root/"original-row-parts-index.json"
    atomic(immutable_manifest,raw_manifest)
    state = dict(kind="R149_complete_true_root_finite_trial_execution_v1",repository=REPO,
        problem_id=manifest["problem_id"],manifest_sha256=args.manifest_sha,
        input_manifest_path=str(mpath.relative_to(root)),new_target_order=manifest["new_target_order"],
        run_id=run,run_attempt=attempt,event_commit=os.environ["GITHUB_SHA"],started_utc=utc(),
        readme_checks=[],readme_check_count=0,readme_receipt_chain_sha256=None,
        complete=False,failure=None,actual_child_returncode=None,scientific_children=0,
        old_numerical_producers_called=0,old_completed_targets_recomputed=0,
        new_arrays_published=0,new_artifacts=0,new_Releases=0,publication_attempts=0,
        whole_current_input_count=0,whole_current_input_receipts_sha256=None,
        historical_restoration={},original_row_restoration={},
        completed_natural_targets=[],scientific_files=[])
    staged,result = {},None

    def fetch_commit(commit):
        require(isinstance(commit,str) and len(commit) == 40
                and all(c in "0123456789abcdef" for c in commit),"immutable original Git commit")
        if git("cat-file","-e",commit+"^{commit}",check_return=False).returncode:
            git("fetch","--filter=blob:none","--no-tags","--depth=1","origin",commit)

    def checked_bytes(spec,head,small=True):
        path = topic_path(spec["path"])
        observed = git("rev-parse",head+":"+path).stdout.strip()
        require("git_blob_sha" not in spec or observed == spec["git_blob_sha"],
                "whole exact original Git identity: "+path)
        raw = git("show",head+":"+path,binary=True).stdout
        require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"] and blob(raw) == observed,
                "whole exact original bytes: "+path)
        if small:
            require(0 < len(raw) < 100000,"whole small UTF8 current input")
            raw.decode()
        return raw,observed

    entry_head = git("rev-parse","HEAD").stdout.strip()
    state["entry_checkout"] = entry_head
    review_spec = roles["reviewed_rules"]
    review = parse(checked_bytes(review_spec,entry_head)[0])
    require(review["repository"] == REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True,
            "explicit actual unchanged two-README review")
    require(review["large_data_policy"]["maximum_topic_bytes"] == LIMIT
            and review["large_data_policy"]["keep_only_scripts_parameters_runs_output_hashes_and_conclusions"] is True
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True,
            "same complete original capacity and no-recomputation rules")
    read_commit = review["read_commit"]
    fetch_commit(read_commit)
    for path,expected in review["readme_sha256"].items():
        require(sha(git("show",read_commit+":"+path,binary=True).stdout) == expected,
                "the exact explicitly reviewed README text")
    def pull():
        before, began = git("rev-parse", "HEAD").stdout.strip(), utc()
        git("pull", "--rebase", "origin", "main")
        after = git("rev-parse", "HEAD").stdout.strip()
        paths = list(review["readme_sha256"])
        actual_diff = git("diff", before, after, "--", *paths).stdout
        review_diff = git("diff", read_commit, after, "--", *paths).stdout
        observed = {p: sha(git("show", after + ":" + p, binary=True).stdout) for p in paths}
        receipt = dict(started_utc=began, finished_utc=utc(), before=before, after=after,
                       actual_diff=actual_diff, diff_from_read_commit=review_diff,
                       read_commit=read_commit, reviewed_rules_sha256=review_spec["sha256"],
                       readme_sha256=observed)
        state["readme_check_count"] += 1
        state["readme_receipt_chain_sha256"] = sha(encode(dict(
            previous=state["readme_receipt_chain_sha256"], receipt=receipt)))
        state["readme_checks"].append(receipt)
        if len(state["readme_checks"]) > 4:
            state["readme_checks"] = [state["readme_checks"][0], *state["readme_checks"][-3:]]
            state["readme_retention"] = "First and latest three full receipts; all printed before hash chaining."
        print("COMPLETE PULL AND README RECEIPT " + encode(receipt).decode(), end="", flush=True)
        require(observed == review["readme_sha256"] and not review_diff,
                "README changed: preserve prefix and apply the printed change before further science")
        return after

    capacity_tree_cache = {}
    def capacity(head):
        """Published whole-tree metadata plus the exact complete local Git delta.

        After a rejected push and a real rebase, HEAD may contain our unpushed
        output commit.  Such a local tree is not a GitHub REST resource.  The
        fetched origin/main is published; only changed local blob sizes need
        Git object reads.  This is administrative byte accounting only.
        """
        tree_sha=git("rev-parse",head+":"+TOPIC).stdout.strip()
        base_head=git("rev-parse","origin/main").stdout.strip()
        base_tree=git("rev-parse",base_head+":"+TOPIC).stdout.strip()
        if base_tree not in capacity_tree_cache:
            request=urllib.request.Request(
                "https://api.github.com/repos/"+REPO+"/git/trees/"+base_tree+"?recursive=1",
                headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json"})
            with urllib.request.urlopen(request,timeout=60) as response:
                raw=response.read()
            data=parse(raw)
            require(data.get("truncated") is False and data["sha"]==base_tree,
                  "complete published-base capacity metadata")
            base_sizes={};base_blobs={}
            for row in data["tree"]:
                if row["type"]=="blob":
                    require(type(row["size"]) is int and row["size"]>=0,
                          "complete Git-tree size")
                    relative=topic_path(TOPIC+"/"+row["path"])
                    require(relative not in base_sizes,"unique whole published-tree path")
                    base_sizes[relative]=row["size"]
                    base_blobs[relative]=row["sha"]
            capacity_tree_cache.clear()
            capacity_tree_cache[base_tree]=(len(raw),sha(raw),base_sizes,base_blobs)
        metadata_bytes,metadata_sha256,base_sizes,base_blobs=capacity_tree_cache[base_tree]
        sizes=dict(base_sizes);blobs=dict(base_blobs)
        delta=git("diff","--raw","--no-abbrev","--no-renames","-z",
                  base_head,head,"--",TOPIC,binary=True).stdout
        tokens=delta.split(b"\0")
        require(tokens[-1]==b"" and (len(tokens)-1)%2==0,
              "complete NUL-delimited local topic delta")
        changes=[];null_sha="0"*40
        for i in range(0,len(tokens)-1,2):
            parts=tokens[i].decode("ascii").split()
            relative=topic_path(tokens[i+1].decode("utf-8"))
            require(len(parts)==5 and parts[0].startswith(":")
                  and parts[4] in ("A","D","M","T"),
                  "complete ordinary local file delta")
            old_sha,new_sha=parts[2],parts[3]
            require(old_sha==blobs.get(relative,null_sha),
                  "local delta starts at the exact published-base blob")
            before=sizes.get(relative,0)
            if new_sha==null_sha:
                after=0
                require(relative in sizes,"complete original deleted local blob")
                del sizes[relative];del blobs[relative]
            else:
                require(git("cat-file","-t",new_sha).stdout.strip()=="blob",
                      "changed local topic object is a complete blob")
                after=int(git("cat-file","-s",new_sha).stdout.strip())
                require(after>=0,"exact complete changed local blob size")
                sizes[relative]=after;blobs[relative]=new_sha
            changes.append({"path":relative,"status":parts[4],
                            "old_git_blob_sha":old_sha,"new_git_blob_sha":new_sha,
                            "old_bytes":before,"new_bytes":after})
        return {"head":head,"topic_tree":tree_sha,"topic_blob_bytes":sum(sizes.values()),
                "metadata_bytes":metadata_bytes,"metadata_sha256":metadata_sha256,
                "blob_count":len(sizes),"published_metadata_base_head":base_head,
                "published_metadata_base_topic_tree":base_tree,
                "complete_local_delta_bytes":len(delta),
                "complete_local_delta_sha256":sha(delta),
                "complete_changed_local_blobs":changes},sizes


    def materialize_current(head):
        receipts = []
        for spec in specs:
            raw,observed = checked_bytes(spec,head)
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(),filename=spec["path"])
            atomic(inputs_root/spec["path"],raw)
            receipts.append({"path":spec["path"],"bytes":len(raw),"sha256":sha(raw),
                             "git_blob_sha":observed})
        require(sha(Path(__file__).read_bytes()) == roles["worker"]["sha256"],
                "the actual executing public worker is the entire pinned source")
        require(sha(git("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)
                == args.manifest_sha,"same complete manifest after every actual pull")
        state["whole_current_input_count"] = len(receipts)
        state["whole_current_input_receipts_sha256"] = sha(encode(receipts))

    def restore_history():
        receipts = []
        for spec in history_specs:
            require(spec["restore_only"] is True
                    and spec["encoding"] in ("gzip-json","gzip-npz","utf-8-json"),
                    "whole original metadata/native restoration without science")
            fetch_commit(spec["commit"])
            raw,observed = checked_bytes(spec,spec["commit"],small=False)
            atomic(inputs_root/spec["path"],raw)
            receipts.append({"path":spec["path"],"commit":spec["commit"],
                             "bytes":len(raw),"sha256":sha(raw),"git_blob_sha":observed})
        state["historical_restoration"] = {
            "whole_original_file_count":len(receipts),
            "complete_receipts":receipts,
            "scientific_target_calls":0,"original_bytes_changed":0}

    def restore_rows():
        old_manifest = parse((inputs_root/roles["old_rows_manifest"]["path"]).read_bytes())
        old_source = (inputs_root/roles["old_rows_worker"]["path"]).read_bytes()
        require(sha(old_source) == "2e1527bfecb2b33ca911d7f8215d8c09e896e36b58144446b34b4a6f01fcc52f"
                and old_manifest["historical_input_commit"] == "7c130fb94528de8f003a43e7049fb42768a64eec"
                and old_manifest["original_body_manifest_sha256"]
                    == roles["old_body_manifest"]["sha256"]
                and old_manifest["original_accepted_response_summary_sha256"]
                    == roles["old_response_summary"]["sha256"],
                "entire exact original restoration definition and accepted old receipts")
        helper = import_source(inputs_root/roles["inputs_math"]["path"],"_TC_worker_pure_inputs")
        names = ("sha","read","relpath","compact","api_json","download_original_archive","restore_original_parts")
        namespace = {"Path":Path,"hashlib":hashlib,"json":json,"urllib":urllib,
                     "shutil":shutil,"gzip":gzip,"zipfile":zipfile,
                     "PUBLIC":REPO,"TOPIC":Path(TOPIC)}
        extraction = helper.pure_definitions(old_source,names,namespace,"same_old_original_archive_reader")
        restoration = {}
        next_check = [time.monotonic()+1800]
        def checkpoint():
            state["original_row_restoration"] = {**restoration,
                "pure_restoration_AST_receipt":extraction,
                "all_old_scientific_producer_calls":0}
            print(encode({"complete_old_original_parts_restored":
                restoration.get("actual_original_natural_parts_restored",0)}).decode(),end="",flush=True)
            if time.monotonic() >= next_check[0]:
                pull()
                next_check[0] = time.monotonic()+1800
        fetch_commit(old_manifest["historical_input_commit"])
        paths = namespace["restore_original_parts"](
            old_manifest,inputs_root,root,git,token,restoration,checkpoint)
        table,parts = [],[]
        for path in paths:
            raw = path.read_bytes()
            data = parse(gzip.decompress(raw))
            entry = {"indices":data["selected_indices"],"bytes":len(raw),"sha256":sha(raw)}
            table.append(entry)
            parts.append({"file":str(path.relative_to(rows_index.parent)),**entry})
        table.sort(key=lambda item:item["indices"])
        require(len(table) == len(parts) == 40,"whole40 original parts restoration")
        document = {"kind":"TC_restored_complete_original_40_parts_v1",
            "original_manifest_sha256":roles["old_body_manifest"]["sha256"],
            "parts":parts,"part_receipts":table}
        atomic(rows_index,encode(document))
        checkpoint()
        state["original_row_restoration"].update(
            complete_original_part_count=40,
            complete_original_part_receipts_sha256=sha(encode(table)),
            complete_private_restoration_index_sha256=sha(encode(document)),
            original_arrays_recomputed=0,original_arrays_published=0)

    def scalar(record):
        return isinstance(record,dict) and set(record) == {"ball"} and isinstance(record["ball"],str)

    def capture(final=False):
        """Read one stable complete owner checkpoint; never invent a missing file."""
        path = output/FILES["state"]
        if not path.exists():
            return None
        for _ in range(4):
            raw_state = path.read_bytes()
            doc = parse(raw_state)
            require(sorted(doc) == manifest["allowed_scientific_fields"]
                    and doc["kind"] == manifest["scientific_kind"]
                    and doc["parameters"] == manifest["parameters"]
                    and doc["run_id"] == run and doc["run_attempt"] == attempt
                    and doc["input_identity"]["manifest_sha256"] == args.manifest_sha
                    and doc["old_scientific_target_calls"] == 0
                    and doc["private_arrays_published"] == 0
                    and (doc["continuation"] is None or isinstance(doc["continuation"],dict)),
                    "whole exact actual new owner state and retained scientific scope")
            count = len(doc["completed_targets"])
            require(doc["completed_targets"] == TARGETS[:count],"whole ordered natural-target prefix")
            files = {output_dir+"/"+FILES["state"]:raw_state}
            documents = {}
            stale = False
            for name in ("matrix","negative","positive","prefix"):
                entry = doc[name+"_receipt"]
                p = output/FILES[name]
                if not p.exists():
                    if entry is not None:
                        stale = True
                        break
                    continue
                # A formal complete natural object or whole prefix may lead
                # the subsequent state receipt.  Its complete bytes are kept
                # and independently validated; the old marker is not edited.
                raw = p.read_bytes()
                require(0 < len(raw) <= op["maximum_"+name+"_bytes"],"whole natural result byte budget")
                files[output_dir+"/"+FILES[name]] = raw
                documents[name] = parse(raw)
            if stale or path.read_bytes() != raw_state:
                continue
            for index,name in enumerate(("matrix","negative","positive")):
                require(TARGETS[index] not in doc["completed_targets"] or name in documents,
                        "each original marked complete conclusion has its entire result")
                if name not in documents:
                    continue
                value = documents[name]
                origin = value["input_manifest_sha256"]
                if origin != args.manifest_sha:
                    prior_role = "prior_"+name
                    raw = files[output_dir+"/"+FILES[name]]
                    require(manifest["continuation"] is not None and prior_role in roles
                            and roles[prior_role]["bytes"] == len(raw)
                            and roles[prior_role]["sha256"] == sha(raw),
                            "a copied formal conclusion keeps its entire original producer identity")
                owner.validate_complete_result(value,name,doc["proposal"],origin,
                                               doc["input_identity"]["same_selected_family"])
                require(value["complete"] is value["proved"] is True
                        and value["proposal_identity"] == doc["proposal"]
                        and value["same_selected_family"] == doc["input_identity"]["same_selected_family"]
                        and value["true_PDE_columns_or_inverse_proved"] is False,
                        "whole actual finite-trial conclusion, without claiming actual PDE columns")
            if "matrix" in documents:
                value = documents["matrix"]
                expected = {"column_%03d"%j for j in range(1,97)}
                require(value["kind"] == "R149_complete_signed_finite_trial_matrices_v1"
                        and value["complete_rows"] == value["complete_columns"] == 96
                        and value["density_independent_mean_coordinates"] == 2
                        and value["original_RW_scalar_targets_recomputed"] == 0
                        and set(value["complete_waist_trial_norms"]) == expected
                        and all(scalar(r) for r in value["complete_waist_trial_norms"].values())
                        and set(value["matrices"]) == {"physical_primitive96","declared_incoming_cosine96"},
                        "all96 finite waist norms and both entire signed matrices")
                for matrix in value["matrices"].values():
                    require(matrix["rows"] == matrix["columns"] == 96
                            and matrix["complete_entries_read_back"] == 9216
                            and matrix["true_PDE_matrix_claimed"] is False
                            and all(scalar(matrix[key]) for key in
                                ("infinity_upper","one_upper","two_upper","Frobenius_upper"))
                            and len(matrix["whole_private_carrier"]["sha256"]) == 64,
                            "whole saved signed matrix carrier identity and all4 complete new bounds")
            for name,windows in (("negative",("negative_root","negative_strict")),
                                ("positive",("positive_low","positive_high_collar","positive_high_body"))):
                if name not in documents:
                    continue
                value = documents[name]
                require(value["kind"] == "R149_complete_"+name+"_finite_trial_sources96_v1"
                        and value["complete_columns"] == 96
                        and value["ordinary_radial_measure"] == "dr"
                        and value["normalized_circle"] is True
                        and value["all_boundary_and_jump_errors_exact"] == "0"
                        and value["complete_original_coefficient_cover"] == 7721
                        and set(value["complete_source_records"]) == {"column_%03d"%j for j in range(1,97)}
                        and value["source_windows"] == {key:manifest["parameters"]["source_windows"][key] for key in windows}
                        and all(set(row) == set(windows) and all(scalar(r) for r in row.values())
                                for row in value["complete_source_records"].values()),
                        "every one of96 columns retains all complete declared whole-window sources")
                if name == "negative":
                    require(value["complete_waist_trial_norms"] == documents["matrix"]["complete_waist_trial_norms"]
                            and value["independent_waist_mean_coordinates"] == 2,
                            "same whole waist96 and both physical mean coordinates")
            if "prefix" in documents:
                value = documents["prefix"]
                require(value["kind"] == "R149_true_root_residual_full_cell_prefix_v1"
                        and value["proposal_identity"] == doc["proposal"]
                        and value["next_cell"] == value["complete_cell_count"]
                        and 0 <= value["next_cell"] <= value["total_cells"]
                        and value["total_cells"] == doc["proposal"]["complete_certificate_cells"]
                        and value["complete_cells_have_all_declared_sources"] is True
                        and value["all96_columns_and_all_declared_source_components_retained"] is True
                        and value["arbitrary_midpoint_not_used_as_an_upper"] is True
                        and set(value["squared_norm_upper_exact_binary64"]) == set(manifest["parameters"]["source_windows"]),
                        "whole all-source complete-cell mathematical prefix")
                for values in value["squared_norm_upper_exact_binary64"].values():
                    require(len(values) == 96 and all(
                        isinstance(x,str) and math.isfinite(float.fromhex(x)) and float.fromhex(x) >= 0
                        for x in values),"all96 exact finite directed squared-norm accumulators")
            qualified = [target for name,target in zip(("matrix","negative","positive"),TARGETS)
                         if name in documents]
            require(qualified == TARGETS[:len(qualified)],
                    "formal natural conclusions remain an ordered full prefix")
            if "negative" in documents:
                require("prefix" in documents
                        and documents["prefix"]["next_cell"] > 0
                        and documents["prefix"]["last_complete_cell"]["side"] in ("negative","positive"),
                        "a complete negative source has its preceding formal radial prefix")
            if "positive" in documents:
                require("prefix" in documents
                        and documents["prefix"]["next_cell"] == documents["prefix"]["total_cells"],
                        "a complete positive source retains the whole radial prefix")
            if doc["complete"]:
                require(doc["proved"] is True and doc["failure"] is None and doc["actual_returncode"] == 0
                        and doc["completed_targets"] == TARGETS
                        and set(documents) == {"matrix","negative","positive","prefix"}
                        and documents["prefix"]["whole_mathematical_target_complete"] is True
                        and documents["prefix"]["next_cell"] == documents["prefix"]["total_cells"],
                        "all three complete finite-trial-only mathematical conclusions")
            return files,doc
        require(not final,"final owner checkpoint changed or lacked its complete formal file")
        return None

    def adopt(snapshot):
        nonlocal staged,result
        if snapshot is None:
            return False
        staged,result = snapshot
        state["completed_natural_targets"] = [target for name,target in
            zip(("matrix","negative","positive"),TARGETS) if output_dir+"/"+FILES[name] in staged]
        state["formal_completed_targets_may_lead_original_marker"] = (
            state["completed_natural_targets"] != result["completed_targets"])
        prefix_raw = staged.get(output_dir+"/"+FILES["prefix"])
        state["qualified_complete_cells"] = -1 if prefix_raw is None else parse(prefix_raw)["next_cell"]
        state["original_scientific_complete"] = result["complete"]
        state["original_scientific_failure"] = result["failure"]
        state["scientific_files"] = [{"path":p,"bytes":len(raw),"sha256":sha(raw)}
                                     for p,raw in sorted(staged.items())]
        return True

    def final_files():
        body = encode(state)
        require(len(body) <= op["maximum_execution_bytes"],"whole actual execution receipt budget")
        report = ("# Actual true-root finite trial columns\n\nRun "+run+"/"+attempt
            +". Complete finite-trial target: "+str(state["complete"])+".\n\n"
            "The 96 exact finite columns share their true root value and retain both means. "
            "Their whole signed waist matrices and full selected ordinary residual sources "
            "are the new mathematical objects. All complete original intrinsic rows and repair "
            "chains are read unchanged. Exact private arrays remain temporary; complete small "
            "conclusions, saved all-source radial prefixes and whole hashes are preserved. "
            "SC true-PDE-column errors and the full inverse remain separate, unexecuted targets.\n").encode()
        return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
    def publish(factory, message, before_science=False):
        while True:
            state["publication_attempts"] += 1
            head = pull()
            cap, sizes = capacity(head)
            state["latest_publication_capacity"] = cap
            files = factory()
            if before_science and git("cat-file", "-e", head + ":" + marker_path,
                                      check_return=False).returncode == 0:
                prior = parse(git("show", head + ":" + marker_path, binary=True).stdout)
                require(prior.get("run_id") == run and prior.get("run_attempt") == attempt,
                        "another attempt already consumed this exact new target")
            require(sum(len(b) for b in files.values()) <= op["maximum_total_publication_bytes"],
                    "whole publication budget")
            projected = cap["topic_blob_bytes"]
            for path, raw in files.items():
                topic_path(path)
                require(0 < len(raw) < 100000, "one complete small UTF8 publication")
                raw.decode("utf-8")
                projected += len(raw) - sizes.get(path, 0)
            allowance = op["maximum_total_publication_bytes"] + RESERVE if before_science else 0
            require(projected + allowance <= LIMIT, "actual rebased complete topic exceeds 200MB")
            for path, raw in files.items():
                atomic(root / path, raw)
            git("add", "--sparse", "--", *files)
            if git("diff", "--cached", "--quiet", check_return=False).returncode:
                git("commit", "-m", message)
            # An unchanged index may still have an unpushed commit after rebase.
            # Always push, including that case; return only after actual success.
            pushed = git("push", "origin", "HEAD:main", check_return=False)
            if pushed.returncode == 0:
                for path, raw in files.items():
                    emit(path, raw)
                return dict(commit=git("rev-parse", "HEAD").stdout.strip(),
                            projected_topic_bytes=projected)
            print("Push rejected; immediately pull --rebase, recheck READMEs, and push again.", flush=True)
            pull()


    try:
        head = pull()
        if git("cat-file","-e",head+":"+marker_path,check_return=False).returncode == 0:
            prior = parse(git("show",head+":"+marker_path,binary=True).stdout)
            require(prior.get("problem_id") == manifest["problem_id"],"same already consumed target")
            print("Existing consumed finite-trial target retained; no automatic numerical replay.",flush=True)
            print(encode(prior).decode(),end="",flush=True)
            return
        materialize_current(head)
        restore_history()
        restore_rows()
        require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
                "whole old restoration and preflight begin without numerical imports")
        owner = import_source(inputs_root/roles["owner"]["path"],"_TC_whole_owner_admission")
        require(owner.PARAMETERS == manifest["parameters"] and owner.RUNTIME == manifest["runtime"]
                and owner.STATE_FIELDS == manifest["allowed_scientific_fields"]
                and owner.TARGETS == TARGETS and owner.FILES == FILES,
                "actual owner definitions equal the entire frozen new launch contract")
        owner_args = SimpleNamespace(repo=str(inputs_root),manifest=str(immutable_manifest),
            manifest_sha=args.manifest_sha,input_root=str(inputs_root),rows_index=str(rows_index),
            out=str(output),private=str(private))
        admitted = owner.preflight(owner_args)
        state["whole_old_input_admission_before_target_reservation"] = admitted[-1]
        if manifest["continuation"] is not None:
            prior_admission = owner.admit_prior_metadata(
                manifest,roles,{spec["path"]:(inputs_root/spec["path"]).read_bytes()
                    for spec in specs if spec["path"] in set(manifest["roles"].values())},admitted[-1])
            state["whole_actual_prior_natural_object_admission"] = prior_admission
        del admitted
        gc.collect()
        require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
                "whole native/source/actual admission called no old numerical target")
        import platform
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),
                   "packages":{name:version(name) for name in manifest["runtime"]["packages"]}}
        require(runtime == manifest["runtime"],"whole actual fixed runtime metadata")
        state["actual_runtime"] = runtime
        cap,_ = capacity(head)
        require(cap["topic_blob_bytes"]+op["maximum_total_publication_bytes"]+RESERVE <= LIMIT,
                "whole topic room before any new finite-trial science")
        state["pre_execution_capacity"] = cap
        marker = {"kind":"consumed_R149_complete_true_root_finite_trial_target_v1",
            "problem_id":manifest["problem_id"],"manifest_sha256":args.manifest_sha,
            "run_id":run,"run_attempt":attempt,"prepared_utc":utc(),"output_directory":output_dir,
            "automatic_scientific_retry":False,"old_completed_targets_may_be_recomputed":False,
            "new_target_order":manifest["new_target_order"],
            "status":"all_original_inputs_admitted_for_one_complete_new_finite_trial_target"}
        state["consumed_marker_publication"] = publish(
            lambda:{marker_path:encode(marker)},"visible-exact: reserve complete true-root finite trials",True)
        head = pull()
        materialize_current(head)
        state["actual_scientific_checkout"] = head
        command = [sys.executable,str(inputs_root/roles["owner"]["path"]),
            "--repo",str(inputs_root),"--manifest",str(immutable_manifest),"--manifest-sha",args.manifest_sha,
            "--input-root",str(inputs_root),"--rows-index",str(rows_index),
            "--out",str(output),"--private",str(private)]
        environment = dict(os.environ)
        for key in ("GITHUB_TOKEN","GIT_CONFIG_COUNT","GIT_CONFIG_KEY_0","GIT_CONFIG_VALUE_0"):
            environment.pop(key,None)
        environment.update(PYTHONDONTWRITEBYTECODE="1",ACTUAL_CHECKOUT_COMMIT=head,
            OPENBLAS_CORETYPE="Haswell",OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",
            MKL_NUM_THREADS="1",BLIS_NUM_THREADS="1",VECLIB_MAXIMUM_THREADS="1",NUMEXPR_NUM_THREADS="1")
        state["scientific_children"] = 1
        state["scientific_started_utc"] = utc()
        began,next_pull,next_snapshot = time.monotonic(),time.monotonic()+1800,time.monotonic()+5
        last_published_targets,last_published_cells = [],-1
        child = subprocess.Popen(command,cwd=temporary,env=environment,
                                 stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        selector = selectors.DefaultSelector()
        selector.register(child.stdout,selectors.EVENT_READ)
        decoder = codecs.getincrementaldecoder("utf-8")()
        timed_out,periodic_failure = False,None
        log = temporary/"scientific-child.log"
        with log.open("wb") as stream:
            while selector.get_map():
                now = time.monotonic()
                if child.poll() is None and periodic_failure is None and now >= next_pull:
                    try:
                        pull()
                        if adopt(capture()):
                            current_cells = state["qualified_complete_cells"]
                            if current_cells > last_published_cells:
                                state["intermediate_publication"] = True
                                publish(final_files,"visible-exact: preserve complete true-root radial prefix")
                                last_published_cells = current_cells
                                last_published_targets = list(state["completed_natural_targets"])
                    except BaseException as exc:
                        periodic_failure = exc
                        child.kill()
                    next_pull = time.monotonic()+1800
                if child.poll() is None and periodic_failure is None and now >= next_snapshot:
                    try:
                        if adopt(capture()) and state["completed_natural_targets"] != last_published_targets:
                            state["intermediate_publication"] = True
                            publish(final_files,"visible-exact: preserve complete true-root finite-trial objects")
                            last_published_targets = list(state["completed_natural_targets"])
                            last_published_cells = state["qualified_complete_cells"]
                    except BaseException as exc:
                        periodic_failure = exc
                        child.kill()
                    next_snapshot = time.monotonic()+5
                if child.poll() is None and time.monotonic()-began > op["child_timeout_seconds"]:
                    child.kill()
                    timed_out = True
                for key,_ in selector.select(timeout=1):
                    chunk = os.read(key.fd,65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        continue
                    stream.write(chunk)
                    stream.flush()
                    sys.stdout.write(decoder.decode(chunk))
                    sys.stdout.flush()
            sys.stdout.write(decoder.decode(b"",final=True))
            sys.stdout.flush()
        selector.close()
        state["actual_child_returncode"] = child.wait()
        state["child_wall_seconds"] = time.monotonic()-began
        state["child_timeout"] = timed_out
        state["scientific_finished_utc"] = utc()
        raw_log = log.read_bytes()
        state["complete_child_stdout"] = {"bytes":len(raw_log),"sha256":sha(raw_log),
                                         "body_not_published_or_split":True}
        adopt(capture(final=True))
        if periodic_failure is not None:
            raise periodic_failure
        require(not timed_out and state["actual_child_returncode"] == 0
                and result is not None and result["complete"] is True,
                "the one new finite-trial scientific child did not complete all three targets")
        materialize_current(pull())
        state["complete"] = True
    except BaseException as exc:
        trace = traceback.format_exc()
        print(trace,flush=True)
        state["failure"] = {"type":type(exc).__name__,"message":str(exc)[:2000],
                          "traceback":trace[-6000:],"whole_trace_in_job_log":True}
        try:
            adopt(capture(final=True))
        except BaseException:
            traceback.print_exc()
            # Preserve every entire small formal object even if its wrapper
            # validation failed.  No completion or scientific flag is repaired.
            for name in FILES.values():
                p = output/name
                if p.exists():
                    raw = p.read_bytes()
                    if 0 < len(raw) < 100000:
                        raw.decode()
                        staged[output_dir+"/"+name] = raw
            state["scientific_files"] = [{"path":p,"bytes":len(raw),"sha256":sha(raw)}
                                         for p,raw in sorted(staged.items())]
    state["finished_utc"] = utc()
    state["intermediate_publication"] = False
    for path,raw in staged.items():
        emit(path,raw)
    try:
        published = publish(final_files,"visible-exact: preserve complete true-root finite-trial outcome")
        print("Published exact complete finite-trial outcome "+published["commit"],flush=True)
    except BaseException:
        traceback.print_exc()
        for path,raw in final_files().items():
            emit(path,raw)
        raise
    if not state["complete"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
