"""One new complete localized C0 and compact-source target, public Actions only.

Read actual complete TM radii and the original whole mean/cubic Fourier
inputs.  No old numerical target is evaluated.  Publish only whole new
scalar bounds or a genuine saved row prefix and complete execution.
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
    output_name = "localized-full-state-and-compact-sources.json"
    state = dict(kind="R144_localized_full_state_compact_sources_public_execution_v1", repository=REPO,
                 problem_id=manifest["problem_id"], manifest_sha256=args.manifest_sha,
                 run_id=run, run_attempt=attempt, event_commit=os.environ["GITHUB_SHA"],
                 started_utc=utc(), readme_checks=[], readme_check_count=0,
                 readme_receipt_chain_sha256=None, current_input_receipts=[],
                 historical_restoration=None, scientific_children=0,
                 old_numerical_producers_called=0, old_completed_targets_recomputed=0,
                 new_arrays_published=0, new_artifacts=0, new_Releases=0,
                 complete=False, failure=None, actual_child_returncode=None,
                 publication_attempts=0)
    temporary = Path(tempfile.mkdtemp(prefix="r144-localized-full-state-and-compact-sources-",
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
        require(len(originals) == 10 and len({s["path"] for s in originals}) == 10,
                "five original mean parts and five original candidate shards")
        receipt = dict(kind="R144_readonly_original_mean_and_candidate_inputs_v1",
                       originals=[], old_producer_calls=0, new_arrays_published=0)
        parts = parse(snapshots["mean_parts_index"].read_bytes())
        require(len(parts["parts"]) == 5 and parts["native_complete"] is True
                and parts["complete_native_rows"] == 7721,
                "complete existing scalar-mean container index")
        native = temporary / parts["original_file"]
        offset = 0
        with native.open("wb") as stream:
            for number, (item, part) in enumerate(zip(originals[:5], parts["parts"])):
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
        receipt["complete_mean_native"] = dict(bytes=len(raw), sha256=sha(raw))
        candidate_dir = temporary / "original-candidate"
        candidate_dir.mkdir()
        candidate_path = candidate_dir / "candidate.json"
        original_index = snapshots["candidate_index"].read_bytes()
        index = parse(original_index)
        require(sha(original_index) == manifest["accepted_natives"]["candidate"]
                and index["kind"] == "complete_lossless_radial_cubic_shards_v1"
                and index["coefficient_shape"] == [4, 6144, 65]
                and len(index["parts"]) == 5,
                "full unchanged original finite candidate index")
        atomic(candidate_path, original_index)
        next_interval = 0
        for number, (item, part) in enumerate(zip(originals[5:], index["parts"])):
            require(item["role"] == "original_candidate_part_"+str(number)
                    and Path(item["path"]).name == part["file"]
                    and Path(part["file"]).name == part["file"]
                    and item["bytes"] == part["bytes"] and item["sha256"] == part["sha256"]
                    and part["first_interval"] == next_interval,
                    "entire original candidate shard order and identity")
            fetch_commit(item["commit"])
            raw = checked_bytes(item, item["commit"], small=False)
            atomic(candidate_dir/part["file"], raw)
            receipt["originals"].append(dict(item, exact_original_bytes_verified=True))
            next_interval = part["last_interval_exclusive"]
        require(next_interval == 6144, "all original candidate cubic intervals")
        receipt["complete_candidate"] = dict(index_bytes=len(original_index),
            index_sha256=sha(original_index), shard_count=5, original_cubic_pieces=6144)
        state["historical_restoration"] = receipt
        return native, candidate_path

    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"],
                "one complete small localized geometry and source outcome")
        doc = parse(raw)
        require(set(doc) == set(manifest["allowed_scientific_fields"]),
                "complete declared scalar-only science schema")
        identity = doc["identity"]
        for key, role in (
                ("source_sha256", "science"), ("old_process_sha256", "old_process"),
                ("tm_result_sha256", "tm_result"), ("tm_execution_sha256", "tm_execution"),
                ("c0_result_sha256", "c0_result"), ("c0_execution_sha256", "c0_execution"),
                ("raw_bounds_sha256", "raw_bounds"), ("source_proof_sha256", "source_proof"),
                ("localized_proof_sha256", "localized_proof"), ("geometry_proof_sha256", "geometry_proof")):
            require(identity[key] == by_role[role]["sha256"], "actual complete source identity: "+role)
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["original_mean_native_sha256"] == manifest["accepted_natives"]["mean"]
                and identity["original_candidate_sha256"] == manifest["accepted_natives"]["candidate"]
                and identity["original_mean_source_sha256"] == manifest["accepted_natives"]["source"]
                and identity["object_sha256"] == by_role["object"]["sha256"]
                and identity["arithmetic_bits"] == 320 and identity["original_modes"] == 32
                and identity["original_pieces"] == 6144
                and identity["exact_alpha"] == manifest["parameters"]["exact_alpha"]
                and identity["exact_nu"] == manifest["parameters"]["exact_nu"]
                and identity["exact_eta"] == manifest["parameters"]["exact_eta"]
                and identity["original_parameter_half_width"] == "1/1000000000"
                and identity["exact_interval"] == ["0", "25/8"]
                and identity["compact_interval"] == ["1/20", "9/50"]
                and identity["intrinsic_box_used_only_as_enclosure_of_original_centre"] is True
                and identity["geometry_norm"] == manifest["parameters"]["geometry_norm"],
                "same complete original raw centre and correct full-state norm")
        require(doc["expected_common_cells"] == 7721 and doc["expected_mean_interfaces"] == 6143
                and all(type(doc[key]) is int for key in (
                    "completed_common_cells", "completed_mean_interfaces", "completed_compact_cells",
                    "finite_coefficient_rows_evaluated", "current_candidate_piece", "saved_readback_count"))
                and 0 <= doc["completed_common_cells"] <= 7721
                and 0 <= doc["completed_mean_interfaces"] <= 6143
                and 0 <= doc["completed_compact_cells"] <= doc["completed_common_cells"]
                and doc["finite_coefficient_rows_evaluated"] == doc["completed_common_cells"]
                and 0 <= doc["current_candidate_piece"] < 6144
                and all(doc[key] == 0 for key in manifest["zero_call_counters"]),
                "complete accepted-row cursor and zero old target evaluations")
        private = doc["private_trace"]
        require(private["records"] == doc["completed_common_cells"]
                and type(private["bytes"]) is int and private["bytes"] >= 0
                and private["content_published"] is False
                and private["scope"] == "accepted_complete_row_prefix"
                and len(private["sha256"]) == 64
                and all(c in "0123456789abcdef" for c in private["sha256"]),
                "private accepted-prefix metadata only")
        trace_file = temporary / "private-localized-geometry-source.ndjson"
        actual_bytes = trace_file.stat().st_size if trace_file.exists() else 0
        require(actual_bytes >= private["bytes"], "private accepted trace prefix exists")
        digest = hashlib.sha256()
        remaining = private["bytes"]
        if trace_file.exists():
            with trace_file.open("rb") as stream:
                while remaining:
                    chunk = stream.read(min(1024*1024, remaining))
                    require(chunk, "complete actual private accepted prefix")
                    digest.update(chunk)
                    remaining -= len(chunk)
        require(remaining == 0 and digest.hexdigest() == private["sha256"],
                "actual entire accepted trace prefix hash")
        state["private_trace_verification"] = dict(
            saved_prefix_bytes=private["bytes"], saved_prefix_sha256=private["sha256"],
            actual_private_bytes=actual_bytes, uncommitted_tail_bytes=actual_bytes-private["bytes"],
            fine_arrays_published=False)

        def record_ok(value):
            return (isinstance(value, dict)
                    and value.get("kind") == "complete_decimal_ball_v1"
                    and value.get("mathematical_direction") == "upper"
                    and all(type(value.get(key)) is str for key in
                            ("midpoint_integer", "radius_integer", "decimal_exponent"))
                    and int(value["radius_integer"]) >= 0)
        scalars = doc["complete_new_scalars"]
        scalar_keys = set(manifest["allowed_new_scalar_fields"])
        require(set(scalars) <= scalar_keys and all(record_ok(x) for x in scalars.values()),
                "only complete decimal balls for declared whole scalar outputs")
        scope = doc["scope"]
        require(all(scope[key] is True for key in (
                    "original_Qraw_nu0_eta0_only", "same_moving_phi_geometry_norm",
                    "complete_physical_amplitude_retained", "original_all32_modes_retained",
                    "all_original_mean_interfaces_retained", "old_raw_residual_and_jump_sums_read_only",
                    "detailed_rows_private_only", "remaining_exact_correction_must_be_added",
                    "failed_sufficient_gate_is_not_nonexistence"))
                and all(scope[key] is False for key in (
                    "nonmean_equations_solved", "nonmean_jumps_repaired",
                    "same_physical_theta_bound_computed", "selected_delta_or_phase_inherited",
                    "exterior_jet_or_height_matched", "body_inverse_proved", "final_topic_complete")),
                "same-phi complete source scope and all independent obligations retained")
        gates = doc["strict_gates"]
        require(set(gates) == {"full_geometry_state_C0_sufficient_1e4"}
                and (type(gates["full_geometry_state_C0_sufficient_1e4"]) is bool
                     or gates["full_geometry_state_C0_sufficient_1e4"] == "unknown"),
                "one actual new sufficient geometry state gate")
        tm = parse(snapshots["tm_result"].read_bytes())
        if doc["exact_parameters"]:
            require(doc["exact_parameters"] == {key:tm["exact_parameters"][key] for key in ("rho", "b")},
                    "same actual complete saved rational radii")
        if doc["complete"]:
            require(doc["proved"] is True and doc["failure"] is None
                    and doc["scalar_scope"] == "complete_whole_target"
                    and doc["stage"] == "complete-localized-full-state-and-compact-source-receivers"
                    and doc["completed_common_cells"] == 7721
                    and doc["completed_mean_interfaces"] == 6143
                    and doc["completed_compact_cells"] == manifest["parameters"]["expected_compact_cells"]
                    and doc["current_exact_right"] == "25/8" and doc["current_candidate_piece"] == 6143
                    and doc["saved_readback_count"] == 7722
                    and set(scalars) == scalar_keys
                    and scope["actual_complete_TM_radii_consumed"] is True
                    and scope["full_closed_row_sources"] is True
                    and type(gates["full_geometry_state_C0_sufficient_1e4"]) is bool,
                    "whole localized norm and complete source receivers saved before final gate")
        else:
            require(doc["proved"] is False and doc["scalar_scope"] == "accepted_row_prefix_only"
                    and scope["full_closed_row_sources"] is False
                    and gates["full_geometry_state_C0_sufficient_1e4"] == "unknown",
                    "a partial result is only the complete accepted-row prefix")
            count = doc["completed_common_cells"]
            prefix_keys = set(manifest["prefix_state_scalar_fields"])
            if count == 0:
                require(not scalars and doc["saved_readback_count"] == 0,
                        "an empty accepted prefix has no invented scalar accumulators")
            elif set(scalars) == prefix_keys:
                require(doc["saved_readback_count"] == count,
                        "each accepted row has one complete prefix checkpoint")
            else:
                require(set(scalars) == scalar_keys and count == 7721
                        and doc["completed_mean_interfaces"] == 6143
                        and doc["current_exact_right"] == "25/8"
                        and doc["current_candidate_piece"] == 6143
                        and doc["saved_readback_count"] == 7722,
                        "only the full terminal prefix may also contain the final derived balls")
        if doc["completed_common_cells"] > 0:
            require(doc["exact_parameters"] == {key:tm["exact_parameters"][key] for key in ("rho", "b")}
                    and scope["actual_complete_TM_radii_consumed"] is True,
                    "every accepted row used the actual complete TM rational parameters")
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
        mean_native, candidate_path = restore()
        marker = dict(kind="consumed_R144_localized_full_state_compact_sources_v1", problem_id=manifest["problem_id"],
                      manifest_sha256=args.manifest_sha, run_id=run, run_attempt=attempt,
                      prepared_utc=utc(), output_directory=output_dir,
                      status="original_bytes_restored_one_new_localized_full_state_and_source_target_reserved",
                      automatic_scientific_retry=False, old_completed_targets_may_be_recomputed=False)
        state["consumed_marker_publication"] = publish(
            lambda: {marker_path: encode(marker)}, "visible-exact: reserve R144 localized full-state norm and compact sources", True)
        head = pull()
        materialize(head)
        state["actual_scientific_checkout"] = head
        command = [sys.executable, str(snapshots["science"]),
                   "--mean", str(mean_native), "--candidate", str(candidate_path),
                   "--old-process", str(snapshots["old_process"]),
                   "--tm-result", str(snapshots["tm_result"]),
                   "--tm-execution", str(snapshots["tm_execution"]),
                   "--c0-result", str(snapshots["c0_result"]),
                   "--c0-execution", str(snapshots["c0_execution"]),
                   "--raw-bounds", str(snapshots["raw_bounds"]),
                   "--source-proof", str(snapshots["source_proof"]),
                   "--localized-proof", str(snapshots["localized_proof"]),
                   "--geometry-proof", str(snapshots["geometry_proof"]),
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
                result = validate_output(output.read_bytes())
            except BaseException as validation_exc:
                result = None
                state["scientific_validation_failure"] = dict(
                    type=type(validation_exc).__name__, message=str(validation_exc)[:2000],
                    complete_original_scientific_bytes_preserved=True,
                    unvalidated_completed_counts_not_consumed=True)

    state["finished_utc"] = utc()
    state["completed_common_cells"] = (result or {}).get("completed_common_cells", 0)
    state["completed_mean_interfaces"] = (result or {}).get("completed_mean_interfaces", 0)
    state["completed_new_localized_state_and_compact_source_targets"] = 1 if state["complete"] else 0
    state["completed_compact_cells"] = (result or {}).get("completed_compact_cells", 0)
    state["finite_coefficient_rows_evaluated"] = (result or {}).get("finite_coefficient_rows_evaluated", 0)
    state["actual_geometry_state_gate"] = (result or {}).get("strict_gates", {}).get(
        "full_geometry_state_C0_sufficient_1e4", "unknown")
    state["original_scientific_complete"] = (result or {}).get("complete")
    state["original_scientific_failure"] = (result or {}).get("failure")
    state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b)) for p, b in staged.items()]
    for path, raw in staged.items():
        emit(path, raw)

    def final_files():
        body = encode(state)
        require(len(body) <= op["maximum_execution_bytes"], "complete execution receipt budget")
        report = ("# R144 localized complete moving state and compact sources\n\nRun " + run + "/" + attempt
                  + "; complete: " + str(state["complete"]) + ".\n\n"
                  "This new target reads the actual complete terminal-mean radii and all original "
                  "7721 mean rows with the full 32-mode cubic Fourier definition. It computes the "
                  "new same-moving-phi unnormalized geometry state bound, five whole ordinary/flux "
                  "source receivers, their weak norm conversions and the rescaled full moving "
                  "v-jump bound. Outside the compact support the whole mean correction remains. "
                  "Every original mean interface is retained.\n\n"
                  "No old terminal-mean gate, Green/Gamma, compact moment, raw residual, primitive, "
                  "DFT, or forward W target is recomputed. No physical-theta angular grid is "
                  "necessary for the declared geometry norm. Original fixed eta0/nu0 only; "
                  "a false sufficient C0 upper test is not a nonexistence result. "
                  "The remaining exact GC correction must still be added to this state ball. "
                  "Nonmean equations and jumps, selected design phase, full inverse, true exterior "
                  "jets/height/matches and the final topic are not solved by these norms. "
                  "Detailed rows stay in private temporary data; only whole scalar bounds or a "
                  "genuine saved prefix, counts, parameters and input/run hashes are published.\n").encode()
        return {**staged, output_dir + "/execution.json": body, output_dir + "/report.md": report}

    try:
        published = publish(final_files, "visible-exact: preserve R144 localized full-state and compact-source outcome")
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
