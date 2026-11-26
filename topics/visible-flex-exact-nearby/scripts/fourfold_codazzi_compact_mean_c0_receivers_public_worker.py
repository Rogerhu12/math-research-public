"""One public R144 compact-moment and complete C0-receiver target.

Read the exact original scalar-mean bytes and already saved Gamma/row
values.  Only new whole receivers and compact positive moments are
computed.  No old producer, primitive, forward W target or future
endpoint is invoked.  Detailed scientific rows remain private.
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
    output_name = "compact-mean-c0-receivers.json"
    state = dict(kind="R144_compact_mean_c0_receivers_public_execution_v1", repository=REPO,
                 problem_id=manifest["problem_id"], manifest_sha256=args.manifest_sha,
                 run_id=run, run_attempt=attempt, event_commit=os.environ["GITHUB_SHA"],
                 started_utc=utc(), readme_checks=[], readme_check_count=0,
                 readme_receipt_chain_sha256=None, current_input_receipts=[],
                 historical_restoration=None, scientific_children=0,
                 old_numerical_producers_called=0, old_completed_targets_recomputed=0,
                 new_arrays_published=0, new_artifacts=0, new_Releases=0,
                 complete=False, failure=None, actual_child_returncode=None,
                 publication_attempts=0)
    temporary = Path(tempfile.mkdtemp(prefix="r144-compact-mean-c0-receivers-",
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
            destination = source_dir / (spec["role"] + Path(spec["path"]).suffix)
            atomic(destination, raw)
            snapshots[spec["role"]] = destination
        require(sha(Path(__file__).read_bytes()) == by_role["worker"]["sha256"],
                "actual running worker is the pinned source")
        require(sha(git("show", head + ":" + str(mpath.relative_to(root)), binary=True).stdout)
                == args.manifest_sha, "manifest unchanged after pull")
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
        require(len(originals) == 5 and len({s["path"] for s in originals}) == 5,
                "exactly the five original scalar-mean container parts")
        receipt = dict(kind="R144_readonly_complete_original_mean_native_v1",
                       originals=[], old_producer_calls=0, new_arrays_published=0)
        parts = parse(snapshots["mean_parts_index"].read_bytes())
        require(len(parts["parts"]) == 5 and parts["native_complete"] is True
                and parts["complete_native_rows"] == 7721,
                "complete existing scalar-mean container index")
        native = temporary / parts["original_file"]
        offset = 0
        with native.open("wb") as stream:
            for number, (item, part) in enumerate(zip(originals, parts["parts"])):
                require(item["role"] == "original_mean_part_" + str(number)
                        and Path(item["path"]).name == part["file"]
                        and item["bytes"] == part["compressed_bytes"]
                        and item["sha256"] == part["compressed_sha256"]
                        and part["index"] == number and part["offset"] == offset,
                        "same complete original mean container part and order")
                fetch_commit(item["commit"])
                raw = checked_bytes(item, item["commit"], small=False)
                receipt["originals"].append(dict(item, exact_original_bytes_verified=True))
                chunk = gzip.decompress(raw)
                require(len(chunk) == part["bytes"] and sha(chunk) == part["sha256"],
                        "unchanged original native container chunk")
                stream.write(chunk)
                offset += len(chunk)
            stream.flush()
            os.fsync(stream.fileno())
        raw = native.read_bytes()
        require(len(raw) == parts["original_bytes"]
                and sha(raw) == parts["original_sha256"] == manifest["accepted_natives"]["mean"],
                "complete exact accepted original mean native container")
        receipt["complete_native"] = dict(bytes=len(raw), sha256=sha(raw))
        state["historical_restoration"] = receipt
        return native

    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"],
                "one complete small new receiver and compact-moment outcome")
        doc = parse(raw)
        require(set(doc) == set(manifest["allowed_scientific_fields"]),
                "complete declared scalar-only science schema")
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["old_process_sha256"] == by_role["old_process"]["sha256"]
                and identity["old_readable_sha256"] == by_role["old_readable"]["sha256"]
                and identity["raw_bounds_sha256"] == by_role["raw_bounds"]["sha256"]
                and identity["strict_proof_sha256"] == by_role["strict_proof"]["sha256"]
                and identity["receiver_proof_sha256"] == by_role["receiver_proof"]["sha256"]
                and identity["kernel_proof_sha256"] == by_role["kernel_proof"]["sha256"]
                and identity["original_mean_native_sha256"] == manifest["accepted_natives"]["mean"]
                and identity["original_candidate_sha256"] == manifest["accepted_natives"]["candidate"]
                and identity["original_mean_source_sha256"] == manifest["accepted_natives"]["source"]
                and identity["arithmetic_bits"] == 320 and identity["original_modes"] == 32
                and identity["exact_alpha"] == manifest["parameters"]["exact_alpha"]
                and identity["exact_nu"] == manifest["parameters"]["exact_nu"]
                and identity["exact_eta"] == manifest["parameters"]["exact_eta"]
                and identity["original_parameter_half_width"] == "1/1000000000"
                and identity["exact_interval"] == ["0", "25/8"]
                and identity["compact_interval"] == ["1/20", "9/50"]
                and identity["intrinsic_box_used_only_as_enclosure_of_its_original_centre"] is True,
                "same original raw centre and every actual input identity")
        require(doc["expected_common_cells"] == 7721
                and doc["expected_mean_interfaces"] == 6143
                and all(type(doc[key]) is int for key in (
                    "completed_common_cells", "completed_mean_interfaces",
                    "completed_prefix_cells", "completed_compact_cells",
                    "completed_weighted_reverse_cells", "weighted_next_original_row",
                    "old_saved_scalar_reads"))
                and 0 <= doc["completed_common_cells"] <= 7721
                and 0 <= doc["completed_mean_interfaces"] <= 6143
                and 0 <= doc["completed_compact_cells"] <= doc["completed_prefix_cells"]
                    <= doc["completed_common_cells"]
                and 0 <= doc["completed_weighted_reverse_cells"] <= 7721
                and doc["weighted_next_original_row"] == 7720-doc["completed_weighted_reverse_cells"]
                and doc["old_saved_scalar_reads"] in (0, 4)
                and all(doc[key] == 0 for key in manifest["zero_call_counters"]),
                "complete actual prefix, exact two-pass cursor, and zero old target calls")
        private = doc["private_trace"]
        require(private["records"] == doc["completed_common_cells"]+doc["completed_weighted_reverse_cells"]
                and type(private["bytes"]) is int and private["bytes"] >= 0
                and private["content_published"] is False
                and private["scope"] == "saved_accepted_checkpoint_prefix"
                and (private["sha256"] is None or
                     (len(private["sha256"]) == 64
                      and all(c in "0123456789abcdef" for c in private["sha256"]))),
                "private accepted-prefix metadata only")
        trace_file = temporary / "private-compact-mean-receiver.ndjson"
        actual_bytes = trace_file.stat().st_size if trace_file.exists() else 0
        require(actual_bytes >= private["bytes"], "private accepted trace prefix exists")
        if private["sha256"] is not None:
            digest = hashlib.sha256()
            remaining = private["bytes"]
            if trace_file.exists():
                with trace_file.open("rb") as stream:
                    while remaining:
                        chunk = stream.read(min(1024*1024, remaining))
                        require(chunk, "complete actual private prefix")
                        digest.update(chunk)
                        remaining -= len(chunk)
            require(remaining == 0 and digest.hexdigest() == private["sha256"],
                    "actual private accepted-prefix hash, not a declared synthetic hash")
        state["private_trace_verification"] = dict(
            saved_prefix_bytes=private["bytes"], saved_prefix_sha256=private["sha256"],
            actual_private_bytes=actual_bytes,
            uncommitted_tail_bytes=actual_bytes-private["bytes"],
            fine_arrays_published=False)

        def record_ok(value):
            return (isinstance(value, dict)
                    and value.get("kind") == "complete_decimal_ball_v1"
                    and value.get("mathematical_direction") in ("enclosure", "upper", "lower")
                    and all(type(value.get(key)) is str for key in
                            ("midpoint_integer", "radius_integer", "decimal_exponent"))
                    and int(value["radius_integer"]) >= 0)
        scalars = doc["complete_new_scalars"]
        scalar_keys = set(manifest["allowed_new_scalar_fields"])
        require(set(scalars) <= scalar_keys
                and all(record_ok(value) for value in scalars.values()),
                "only complete decimal balls for declared new scalar outputs")
        scope = doc["scope"]
        require(all(scope[key] is True for key in (
                    "original_Qraw_nu0_eta0_only",
                    "exact_original_affine_box_identity_required",
                    "all_original_mean_interfaces_retained",
                    "normalized_compact_moments_only_new",
                    "C0_receiver_is_not_old_L2_gain", "detailed_rows_private_only",
                    "structural_bbar_between_zero_and_abar_over_two"))
                and all(scope[key] is False for key in (
                    "old_saved_Gamma_and_row_sums_recomputed",
                    "point_intrinsic_carrier_reconstructed", "forward_W_recomputed",
                    "selected_delta_or_phase_inherited", "nonmean_equations_solved",
                    "outer_cap_or_height_matched", "body_inverse_proved",
                    "final_topic_complete")),
                "exact independent receiver scope without a future endpoint")
        gates = doc["strict_gates"]
        require((type(gates["compact_leverage_positive"]) is bool
                 or gates["compact_leverage_positive"] == "unknown")
                and gates["actual_forward_endpoint_consumed"] is False
                and gates["actual_small_root"] == "unknown"
                and gates["actual_nonlinear_mean_small_ball"] == "unknown",
                "whole moment gate and explicitly unevaluated future gates")
        if doc["complete"]:
            require(type(doc["proved"]) is bool
                    and doc["proved"] == (gates["compact_leverage_positive"] is True)
                    and doc["failure"] is None
                    and doc["scalar_scope"] == "complete_whole_target"
                    and doc["stage"] == "complete-new-compact-moments-and-C0-receivers"
                    and doc["completed_common_cells"] == 7721
                    and doc["completed_mean_interfaces"] == 6143
                    and doc["completed_weighted_reverse_cells"] == 7721
                    and doc["weighted_next_original_row"] == -1
                    and doc["current_exact_right"] == "25/8"
                    and doc["current_H_exact_right"] == "9/50"
                    and doc["old_saved_scalar_reads"] == 4
                    and set(scalars) == scalar_keys
                    and scope["complete_new_receiver_and_moments"] is True,
                    "whole new target completed and saved before its only numerical gate")
        else:
            require(doc["proved"] is False
                    and doc["scalar_scope"] == "accepted_forward_prefix_and_reverse_suffix_only",
                    "a partial target contains only prefix/suffix states, not whole bounds")
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
        runtime = dict(python=platform.python_version(),
                       packages={name: version(name) for name in manifest["runtime"]["packages"]})
        require(runtime == manifest["runtime"], "actual complete fixed runtime metadata")
        state["actual_runtime"] = runtime
        cap, _ = capacity(head)
        require(cap["topic_blob_bytes"] + op["maximum_total_publication_bytes"] + RESERVE <= LIMIT,
                "complete topic room before restoration and science")
        state["pre_execution_capacity"] = cap
        mean_native = restore()
        marker = dict(kind="consumed_R144_compact_mean_c0_receivers_v1", problem_id=manifest["problem_id"],
                      manifest_sha256=args.manifest_sha, run_id=run, run_attempt=attempt,
                      prepared_utc=utc(), output_directory=output_dir,
                      status="original_bytes_restored_one_new_compact_moment_and_C0_receiver_target_reserved",
                      automatic_scientific_retry=False, old_completed_targets_may_be_recomputed=False)
        state["consumed_marker_publication"] = publish(
            lambda: {marker_path: encode(marker)}, "visible-exact: reserve R144 compact positive moments and whole C0 receivers", True)
        head = pull()
        materialize(head)
        state["actual_scientific_checkout"] = head
        command = [sys.executable, str(snapshots["science"]),
                   "--mean", str(mean_native),
                   "--old-process", str(snapshots["old_process"]),
                   "--old-readable", str(snapshots["old_readable"]),
                   "--raw-bounds", str(snapshots["raw_bounds"]),
                   "--strict-proof", str(snapshots["strict_proof"]),
                   "--receiver-proof", str(snapshots["receiver_proof"]),
                   "--kernel-proof", str(snapshots["kernel_proof"]),
                   "--output", str(output)]
        environment = dict(os.environ)
        for key in ("GITHUB_TOKEN", "GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0"):
            environment.pop(key, None)
        environment.update(PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1",
                           OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
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
    state["completed_common_cells"] = (result or {}).get("completed_common_cells", 0)
    state["completed_mean_interfaces"] = (result or {}).get("completed_mean_interfaces", 0)
    state["completed_new_compact_moment_and_C0_receiver_targets"] = 1 if state["complete"] else 0
    state["completed_weighted_reverse_cells"] = (result or {}).get("completed_weighted_reverse_cells", 0)
    state["completed_prefix_cells"] = (result or {}).get("completed_prefix_cells", 0)
    state["completed_compact_cells"] = (result or {}).get("completed_compact_cells", 0)
    state["original_scientific_complete"] = (result or {}).get("complete")
    state["original_scientific_failure"] = (result or {}).get("failure")
    state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b)) for p, b in staged.items()]
    for path, raw in staged.items():
        emit(path, raw)

    def final_files():
        body = encode(state)
        require(len(body) <= op["maximum_execution_bytes"], "complete execution receipt budget")
        report = ("# R144 compact positive moments and whole C0 receivers\n\nRun " + run + "/" + attempt
                  + "; complete: " + str(state["complete"]) + ".\n\n"
                  "This independent new target reads the complete old 7721-row mean native, "
                  "its saved row sums, and the already saved Gamma. It computes new C0 jump "
                  "and weighted receivers, all eleven full profile-weighted feedback kernels, "
                  "whole coefficient bounds, and the two positive "
                  "normalized compact moments supported on [1/20,9/50]. No old Green maximum, "
                  "residual, primitive, DFT, or forward W target is recomputed.\n\n"
                  "The mathematical object is the original piecewise ac1 raw centre at nu0 "
                  "and eta0. Its original affine-box rows provide enclosing inputs; the "
                  "fixed-centre strict metric proof supplies the compact signs. The actual "
                  "forward D_R/G_R is not an input of this target. A positive compact-leverage "
                  "gate does not prove the root, nonlinear small ball, nonmean equations, "
                  "selected design phase, exterior matching, inverse, or final topic. "
                  "Unknown and false numerical gates are retained. Detailed rows stay in "
                  "private temporary data; only whole scalar conclusions, counts, parameters "
                  "and input/run hashes are published.\n").encode()
        return {**staged, output_dir + "/execution.json": body, output_dir + "/report.md": report}

    try:
        published = publish(final_files, "visible-exact: preserve R144 compact moments and C0 receiver outcome")
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
