"""Public wrapper for two selected physical Robin and mean residual values.

Restore one original complete84KB endpoint native without old production.
Run the new two-value consumer against a private snapshot of all small inputs.
Preserve every genuine prefix and all independent height and inverse obligations.
"""
from __future__ import annotations
import argparse, ast, base64, codecs, gzip, hashlib, json, os
from pathlib import Path
import selectors, subprocess, sys, tempfile, time, traceback, urllib.request
from datetime import datetime, timezone

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
LIMIT = 200000000
RESERVE = 120000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def utc():
    return datetime.now(timezone.utc).isoformat()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, path)


def topic_path(value):
    require(isinstance(value, str) and value.startswith(TOPIC + "/")
            and all(x not in ("", ".", "..") for x in value.split("/")),
            "safe current topic path")
    return value


def emit(name, raw):
    print("BEGIN COMPLETE PUBLIC FILE " + name + " bytes=" + str(len(raw))
          + " sha256=" + sha(raw), flush=True)
    sys.stdout.write(raw.decode("utf-8"))
    sys.stdout.flush()
    print("END COMPLETE PUBLIC FILE " + name, flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--manifest-sha", required=True)
    args = ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "only the authorized public Actions repository")
    root = Path(args.repo).resolve()
    os.chdir(root)

    def git(*argv, check_return=True, binary=False):
        p = subprocess.run(["git", "-c", "user.name=github-actions[bot]",
             "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
             *argv], cwd=root, capture_output=True, text=not binary)
        if check_return and p.returncode:
            err = p.stderr.decode("utf-8", "replace") if binary else p.stderr
            raise RuntimeError("git " + " ".join(argv) + " failed: " + err)
        return p

    token = os.environ["GITHUB_TOKEN"]
    auth = base64.b64encode(("x-access-token:" + token).encode()).decode()
    os.environ["GIT_CONFIG_COUNT"] = "1"
    os.environ["GIT_CONFIG_KEY_0"] = "http.https://github.com/.extraheader"
    os.environ["GIT_CONFIG_VALUE_0"] = "AUTHORIZATION: basic " + auth
    run, attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    mpath = Path(args.manifest)
    if not mpath.is_absolute():
        mpath = root / mpath
    raw_manifest = mpath.read_bytes()
    require(0 < len(raw_manifest) < 100000 and sha(raw_manifest) == args.manifest_sha,
            "complete pinned manifest")
    manifest = parse(raw_manifest)
    require(manifest["repository"] == REPO, "same repository")
    op = manifest["operation"]
    require(op["topic_maximum_bytes"] == LIMIT and op["reserve_bytes"] == RESERVE,
            "original actual topic capacity rule")
    marker_path = topic_path(op["consumed_marker"])
    output_dir = topic_path(op["output_base"] + "/run-" + run + "-" + attempt)
    output_name = "selected-physical-outer-values.json"
    state = dict(kind="R141_selected_physical_outer_values_public_execution_v1", repository=REPO,
                 problem_id=manifest["problem_id"], manifest_sha256=args.manifest_sha,
                 run_id=run, run_attempt=attempt, event_commit=os.environ["GITHUB_SHA"],
                 started_utc=utc(), readme_checks=[], readme_check_count=0,
                 readme_receipt_chain_sha256=None, current_input_receipts=[],
                 historical_restoration=None, scientific_children=0,
                 old_numerical_producers_called=0, old_completed_targets_recomputed=0,
                 new_arrays_published=0, new_artifacts=0, new_Releases=0,
                 complete=False, failure=None, actual_child_returncode=None,
                 publication_attempts=0)
    temporary = Path(tempfile.mkdtemp(prefix="r141-selected-physical-outer-values-",
                                    dir=os.environ.get("RUNNER_TEMP")))
    output = temporary / output_name
    source_dir = temporary / "current-small-inputs"
    source_dir.mkdir()
    specs = manifest["files"]
    require(len(specs) == manifest["expected_current_input_count"]
            and len({s["role"] for s in specs}) == len(specs)
            and len({s["path"] for s in specs}) == len(specs),
            "unique complete current input definitions")
    by_role = {s["role"]: s for s in specs}
    snapshots = {}
    staged = {}
    result = None

    def fetch_commit(commit):
        require(isinstance(commit, str) and len(commit) == 40
                and all(c in "0123456789abcdef" for c in commit), "immutable history commit")
        if git("cat-file", "-e", commit + "^{commit}", check_return=False).returncode:
            git("fetch", "--filter=blob:none", "--no-tags", "--depth=1", "origin", commit)

    def checked_bytes(spec, head, small=True):
        path = topic_path(spec["path"])
        observed = git("rev-parse", head + ":" + path).stdout.strip()
        require(observed == spec["git_blob_sha"], "input Git identity: " + path)
        raw = git("show", head + ":" + path, binary=True).stdout
        require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                and blob(raw) == observed, "input byte identity: " + path)
        if small:
            require(0 < len(raw) < 100000, "complete small current input")
            raw.decode("utf-8")
        return raw

    entry_head = git("rev-parse", "HEAD").stdout.strip()
    state["entry_checkout"] = entry_head
    review_spec = by_role["reviewed_rules"]
    review = parse(checked_bytes(review_spec, entry_head))
    require(review["repository"] == REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True,
            "explicit unchanged repository rule review")
    policy = review["large_data_policy"]
    require(policy["maximum_topic_bytes"] == LIMIT
            and policy["keep_only_scripts_parameters_runs_output_hashes_and_conclusions"] is True
            and policy["original_completed_mathematics_must_not_be_recomputed"] is True,
            "same no-recomputation and no-array policy")
    read_commit = review["read_commit"]
    fetch_commit(read_commit)
    for path, expected in review["readme_sha256"].items():
        require(sha(git("show", read_commit + ":" + path, binary=True).stdout) == expected,
                "explicitly reviewed README bytes")

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

    def materialize(head):
        for spec in specs:
            raw = checked_bytes(spec, head)
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(), filename=spec["path"])
            destination = source_dir / spec["path"]
            atomic(destination, raw)
            snapshots[spec["role"]] = destination
        require(sha(Path(__file__).read_bytes()) == by_role["worker"]["sha256"],
                "actual running worker is the pinned source")
        require(sha(git("show", head + ":" + str(mpath.relative_to(root)), binary=True).stdout)
                == args.manifest_sha, "manifest unchanged after pull")
        atomic(source_dir / mpath.relative_to(root), raw_manifest)
        state["current_input_receipts"] = specs

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

    def restore():
        originals = manifest["historical_inputs"]
        require(len(originals) == 1
                and originals[0]["role"] == "original_raw_boundary_native"
                and originals[0]["sha256"] == manifest["accepted_natives"]["raw_boundary"]
                and originals[0]["bytes"] == 84003,
                "exact one whole original raw physical boundary native")
        spec = originals[0]
        fetch_commit(spec["commit"])
        raw = checked_bytes(spec,spec["commit"],small=False)
        require(raw[:2] == b"\x1f\x8b", "unchanged complete original gzip container")
        destination = temporary/"original-raw-physical-boundary-native.json.gz"
        atomic(destination,raw)
        receipt = dict(kind="R141_readonly_original_raw_boundary_v1",
                       original_inputs=originals, original_bytes_verified=True,
                       old_producer_calls=0, new_arrays_published=0)
        state["historical_restoration"] = receipt
        receipt_path = temporary/"exact-original-restoration-receipts.json"
        atomic(receipt_path,encode(receipt))
        return destination,receipt_path

    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "complete small two-physical-value result")
        doc = parse(raw)
        require(set(doc) == set(manifest["allowed_scientific_fields"]),
                "complete declared scalar-prefix schema")
        require(doc["kind"] == manifest["scientific_kind"]
                and doc["repository"] == REPO and doc["problem_id"] == manifest["problem_id"]
                and doc["source_sha256"] == by_role["science"]["sha256"]
                and doc["input_manifest_sha256"] == args.manifest_sha
                and doc["parameters"] == manifest["parameters"]
                and doc["retained_scope"] == manifest["scope"]
                and doc["target_order"] == manifest["target_order"]
                and str(doc["run_id"]) == run and str(doc["run_attempt"]) == attempt
                and doc["actual_scientific_checkout_commit"] == state["actual_scientific_checkout"],
                "same selected member, exact whole inputs, and actual new source run")
        require(type(doc["saved_record_count"]) is int and 0 <= doc["saved_record_count"] <= 2,
                "genuine complete scalar prefix count")
        targets = manifest["target_order"][:doc["saved_record_count"]]
        require(set(doc["complete_new_scalar_records"]) == set(targets)
                and all(isinstance(x, dict) and isinstance(x.get("ball"), str)
                        for x in doc["complete_new_scalar_records"].values())
                and all(doc[key] == 0 for key in (
                    "old_numerical_producers_called", "old_scientific_source_imports",
                    "old_successful_targets_recomputed", "new_arrays_published", "new_artifacts", "new_Releases"))
                and doc["automatic_scientific_retry"] is False,
                "only the actually saved new scalar prefix and no old numerical targets")
        gates = doc["gates"]
        require(len(gates) <= len(manifest["gate_order"])
                and [x["name"] for x in gates] == manifest["gate_order"][:len(gates)],
                "original ordered admission or actual complete gates")
        if doc["complete"]:
            require(doc["proved"] is True and doc["failure"] is None
                    and doc["actual_returncode"] == 0 and doc["saved_record_count"] == 2
                    and len(gates) == 18 and all(x["passed"] is True for x in gates)
                    and doc["runtime"] == manifest["runtime"]
                    and doc["metadata_admission_complete"] is True
                    and doc["all_saved_records_readback_verified"] is True
                    and doc["current_input_receipts"] == manifest["files"]
                    and doc["restoration_receipts"] == state["historical_restoration"]
                    and doc["actual_progress"]["stage"] == "complete_two_physical_values"
                    and doc["actual_progress"]["completed_targets"] == 2
                    and doc["actual_progress"]["current_target"] is None
                    and doc["actual_progress"]["last_complete_budget_stage"] == "complete_fixed_theta_state_difference"
                    and set(doc["actual_progress"]["unfinished_complete_budget_records"]) ==
                        {"complete_moving_increment", "complete_same_physical_angle",
                         "complete_fixed_theta_state_difference"},
                    "both complete same-member physical values saved and read back")
            scope = doc["complete_physical_value_conclusion"]
            require(scope["complete"] is True and scope["completed_target_count"] == 2
                    and scope["same_selected_member_by_uniform_delta10_restriction"] is True
                    and scope["same_fixed_physical_theta_and_complete_Fourier_tail"] is True
                    and scope["same_background_fB_within_original_permitted_ball"] is True
                    and scope["independent_physical_mean_is_reciprocal_moving_mean"] is True
                    and scope["raw_physical_amplitude_not_applied_again"] is True
                    and scope["endpoint_Theta_weight_not_applied_to_physical_sources"] is True
                    and scope["Robin_output_norm"] == "normalized physical-circle H^-5/6"
                    and scope["mean_output_norm"] == "absolute physical scalar",
                    "complete physical-circle Robin and independent reciprocal mean qualifications")
            for key in ("height_actual_rhs_value_proved", "far_regular_label_or_height_gauge_equation_proved",
                        "actual_nu_response_boundary_discrepancy_of_Z_proved",
                        "negative_germ_interface_and_root_inputs_proved", "both_complete_WPN_rhs_proved",
                        "complete_infinite_inverse_proved", "nonlinear_solution_proved"):
                require(scope[key] is False, "unpaid independent obligation: "+key)
        return doc

    try:
        head = pull()
        if git("cat-file", "-e", head + ":" + marker_path, check_return=False).returncode == 0:
            prior = parse(git("show", head + ":" + marker_path, binary=True).stdout)
            require(prior.get("problem_id") == manifest["problem_id"], "same consumed target")
            print("Consumed target retained. No scientific child or retry is allowed.", flush=True)
            print(encode(prior).decode(), end="", flush=True)
            return
        materialize(head)
        # Version inspection is metadata only; no numerical module is imported.
        import platform
        from importlib.metadata import version
        runtime = {"Python": platform.python_version(), "python_flint": version("python-flint")}
        require(runtime == manifest["runtime"], "actual complete fixed runtime metadata")
        state["actual_runtime"] = runtime
        cap, _ = capacity(head)
        require(cap["topic_blob_bytes"] + op["maximum_total_publication_bytes"] + RESERVE <= LIMIT,
                "complete topic room before restoration and science")
        state["pre_execution_capacity"] = cap
        raw_boundary, restoration_receipts = restore()
        marker = dict(kind="consumed_R141_selected_physical_outer_values_v1", problem_id=manifest["problem_id"],
                      manifest_sha256=args.manifest_sha, run_id=run, run_attempt=attempt,
                      prepared_utc=utc(), output_directory=output_dir,
                      status="whole_original_endpoint_restored_two_new_physical_values_reserved",
                      automatic_scientific_retry=False, old_completed_targets_may_be_recomputed=False)
        state["consumed_marker_publication"] = publish(
            lambda: {marker_path: encode(marker)}, "visible-exact: reserve two new selected physical outer residual values", True)
        head = pull()
        materialize(head)
        state["actual_scientific_checkout"] = head
        command = [sys.executable, str(snapshots["science"]),
                   "--repo", str(source_dir),
                   "--manifest", str(source_dir / mpath.relative_to(root)),
                   "--manifest-sha", args.manifest_sha,
                   "--raw-boundary", str(raw_boundary),
                   "--restoration-receipts", str(restoration_receipts), "--out", str(output)]
        environment = dict(os.environ)
        for key in ("GITHUB_TOKEN", "GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0"):
            environment.pop(key, None)
        environment.update(PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1",
                           OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
        environment["CURRENT_SCIENCE_COMMIT"] = head
        state["scientific_children"] = 1
        state["scientific_started_utc"] = utc()
        began, next_pull = time.monotonic(), time.monotonic() + 1800
        child = subprocess.Popen(command, cwd=temporary, env=environment,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        selector = selectors.DefaultSelector()
        selector.register(child.stdout, selectors.EVENT_READ)
        decoder = codecs.getincrementaldecoder("utf-8")()
        timed_out, periodic_failure = False, None
        log = temporary / "scientific-child.log"
        with log.open("wb") as stream:
            while selector.get_map():
                if child.poll() is None and periodic_failure is None and time.monotonic() >= next_pull:
                    try:
                        pull()
                    except BaseException as exc:
                        periodic_failure = exc
                        child.kill()
                    next_pull = time.monotonic() + 1800
                if child.poll() is None and time.monotonic() - began > op["child_timeout_seconds"]:
                    child.kill()
                    timed_out = True
                for key, _ in selector.select(timeout=1):
                    chunk = os.read(key.fd, 65536)
                    if not chunk:
                        selector.unregister(key.fileobj)
                        continue
                    stream.write(chunk)
                    stream.flush()
                    sys.stdout.write(decoder.decode(chunk))
                    sys.stdout.flush()
            sys.stdout.write(decoder.decode(b"", final=True))
            sys.stdout.flush()
        selector.close()
        state["actual_child_returncode"] = child.wait()
        state["child_wall_seconds"] = time.monotonic() - began
        state["child_timeout"] = timed_out
        state["scientific_finished_utc"] = utc()
        raw_log = log.read_bytes()
        state["complete_child_stdout"] = dict(bytes=len(raw_log), sha256=sha(raw_log),
                                               body_not_published_or_split=True)
        if output.exists():
            staged[output_dir + "/" + output_name] = output.read_bytes()
            result = validate_output(output.read_bytes())
        if periodic_failure is not None:
            raise periodic_failure
        require(not timed_out and state["actual_child_returncode"] == 0
                and result is not None and result["complete"] is True,
                "the single new scientific child did not complete")
        materialize(pull())
        state["complete"] = True
    except BaseException as exc:
        full_trace = traceback.format_exc()
        print(full_trace, flush=True)
        state["failure"] = dict(type=type(exc).__name__, message=str(exc)[:2000],
                                traceback=full_trace[:8000], full_trace_in_job_log=True)
        if output.exists():
            staged[output_dir + "/" + output_name] = output.read_bytes()
            try:
                result = parse(output.read_bytes())
            except Exception:
                result = None

    state["finished_utc"] = utc()
    state["completed_new_physical_value_records"] = (result or {}).get("saved_record_count", 0)
    state["complete_scientific_metadata"] = (result or {}).get("complete_metadata")
    state["original_scientific_complete"] = (result or {}).get("complete")
    state["original_scientific_failure"] = (result or {}).get("failure")
    state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b)) for p, b in staged.items()]
    for path, raw in staged.items():
        emit(path, raw)

    def final_files():
        body = encode(state)
        require(len(body) <= op["maximum_execution_bytes"], "complete execution receipt budget")
        report = ("# R141 selected physical outer residual values\n\nRun " + run + "/" + attempt
                  + "; complete: " + str(state["complete"]) + ".\n\n"
                  "One original complete84KB boundary native is restored unchanged. The complete "
                  "raw nonlinear Robin and mean values, repaired/full-family outer graphs, exact193 "
                  "direction endpoint and selected-member receipts are read without old production. "
                  "Two new values pay the full fixed-physical-angle state change and independent "
                  "reciprocal mean for the same permitted background height.\n\n"
                  "The background height radius is not a Newton height RHS. Far label, height gauge, "
                  "the known Z boundary discrepancy, negative/germ/interface/root inputs, both full "
                  "WPN right sides, complete inverse and nonlinear solution remain independent. "
                  "No old targets, physical Fourier arrays, artifacts or Releases are produced.\n").encode()

        return {**staged, output_dir + "/execution.json": body, output_dir + "/report.md": report}

    try:
        published = publish(final_files, "visible-exact: preserve the complete selected physical outer values")
        print("Published complete outcome receipt " + published["commit"], flush=True)
    except BaseException:
        # A new unread rule may prevent even publication; keep the full small
        # prefix and receipt visible in the job log for the continuing owner.
        traceback.print_exc()
        for path, raw in final_files().items():
            emit(path, raw)
        raise
    if not state["complete"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
