"""One public R146 quadratic-cap true-root-capacity integral; restore old bytes only.

The sole numerical child computes the new positive short-root integral T.
All completed high, signed-root, X and GB targets are immutable inputs.
Only complete small scalar outcomes or genuine unfinished prefixes and
execution receipts are published. No new arrays, artifacts or Releases.
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
    output_name = "quadratic-cap-root-screen.json"
    state = dict(kind="R146_quadratic_cap_root_screen_public_execution_v1", repository=REPO,
                 problem_id=manifest["problem_id"], manifest_sha256=args.manifest_sha,
                 run_id=run, run_attempt=attempt, event_commit=os.environ["GITHUB_SHA"],
                 started_utc=utc(), readme_checks=[], readme_check_count=0,
                 readme_receipt_chain_sha256=None, current_input_receipts=[],
                 historical_restoration=None, scientific_children=0,
                 old_numerical_producers_called=0, old_completed_targets_recomputed=0,
                 new_arrays_published=0, new_artifacts=0, new_Releases=0,
                 complete=False, failure=None, actual_child_returncode=None,
                 publication_attempts=0)
    temporary = Path(tempfile.mkdtemp(prefix="r146-quadratic-cap-root-screen-",
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
                "exact four positive parts, five cubic shards, and one root germ")
        receipt = dict(kind="R146_readonly_original_four_plus_five_plus_germ_v1",
                       originals=[], old_producer_calls=0, new_arrays_published=0)

        def historical(spec):
            fetch_commit(spec["commit"])
            raw = checked_bytes(spec, spec["commit"], small=False)
            receipt["originals"].append(dict(spec, exact_original_bytes_verified=True))
            return raw

        parts = parse(snapshots["positive_parts_index"].read_bytes())
        require(len(parts["parts"]) == 4 and parts["native_complete"] is True
                and parts["complete_native_rows"] == 4650, "complete existing positive container index")
        positive = temporary / parts["original_file"]
        offset = 0
        with positive.open("wb") as stream:
            for number, (item, part) in enumerate(zip(originals[:4], parts["parts"])):
                require(item["role"] == "original_positive_part_" + str(number)
                        and Path(item["path"]).name == part["file"]
                        and item["bytes"] == part["compressed_bytes"]
                        and item["sha256"] == part["compressed_sha256"]
                        and part["index"] == number and part["offset"] == offset,
                        "same complete original positive part and order")
                chunk = gzip.decompress(historical(item))
                require(len(chunk) == part["bytes"] and sha(chunk) == part["sha256"],
                        "unchanged original container chunk")
                stream.write(chunk)
                offset += len(chunk)
            stream.flush()
            os.fsync(stream.fileno())
        raw = positive.read_bytes()
        require(len(raw) == parts["original_bytes"] and sha(raw) == parts["original_sha256"],
                "complete exact accepted positive native container")
        receipt["positive_native"] = dict(bytes=len(raw), sha256=sha(raw))
        candidate_dir = temporary / "original-candidate"
        candidate_dir.mkdir()
        index = snapshots["candidate_index"].read_bytes()
        candidate = parse(index)
        require(len(candidate["parts"]) == 5, "all original candidate shards")
        candidate_path = candidate_dir / Path(by_role["candidate_index"]["path"]).name
        atomic(candidate_path, index)
        for number, (item, part) in enumerate(zip(originals[4:9], candidate["parts"])):
            require(item["role"] == "original_candidate_part_" + str(number)
                    and Path(item["path"]).name == part["file"]
                    and item["bytes"] == part["bytes"] and item["sha256"] == part["sha256"],
                    "same complete original cubic shard")
            raw = historical(item)
            atomic(candidate_dir / part["file"], raw)
        item = originals[9]
        require(item["role"] == "original_root_germ", "same accepted root germ")
        germ = temporary / Path(item["path"]).name
        atomic(germ, historical(item))
        receipt["candidate_index"] = by_role["candidate_index"]
        state["historical_restoration"] = receipt
        return positive, germ, candidate_path

    def validate_output(raw):
        require(0 < len(raw) <= op["maximum_scientific_bytes"], "complete small root-screen result")
        doc = parse(raw)
        require(set(doc) == set(manifest["allowed_scientific_fields"]),
                "complete declared scalar-prefix schema without scientific arrays")
        identity = doc["identity"]
        require(identity["kind"] == manifest["scientific_kind"]
                and identity["source_sha256"] == by_role["science"]["sha256"]
                and identity["definition_source_sha256"] == by_role["definition_helper"]["sha256"]
                and identity["original_positive_sha256"] == manifest["accepted_natives"]["positive"]
                and identity["original_germ_sha256"] == manifest["accepted_natives"]["germ"]
                and identity["original_candidate_sha256"] == by_role["candidate_index"]["sha256"]
                and identity["arithmetic_bits"] == 320
                and identity["fixed_test_length"] == "3/200"
                and identity["test_polynomial_degree"] == 2
                and identity["analytic_test_root_L2_upper"] == "1"
                and identity["analytic_test_root_derivative_L2_upper"] == "377"
                and identity["fixed_subdivisions_per_original_cell"] == 32
                and identity["original_positive_rows"] == 4650
                and identity["original_positive_interfaces"] == 3594
                and identity["original_low_modes"] == [1, 96]
                and identity["original_high_modes"] == "j>=97"
                and identity["reflection_axis_moving_angles"] == ["0", "pi/4"]
                and identity["physical_angles_equal_moving_angles_on_both_axes"] is True,
                "same exact one new short-root integral and complete original object")
        for role, key in (("high", "old_high_sha256"),
                          ("high_execution", "old_high_execution_sha256"),
                          ("two_mode", "old_two_mode_sha256"),
                          ("two_mode_execution", "old_two_mode_execution_sha256"),
                          ("physical", "old_X_sha256"),
                          ("physical_execution", "old_X_execution_sha256"),
                          ("body_budget", "old_GB_sha256"),
                          ("body_execution", "old_GB_execution_sha256"),
                          ("correlated", "old_correlated_sha256"),
                          ("correlated_execution", "old_correlated_execution_sha256")):
            require(identity[key] == by_role[role]["sha256"], "whole original input identity")
        for key in ("expected_common_cells", "completed_common_cells", "expected_subcells",
                    "completed_subcells", "completed_positive_rows"):
            require(type(doc[key]) is int and doc[key] >= 0, "complete real prefix counter")
        require(doc["expected_common_cells"] > 0
                and doc["expected_subcells"] == 32 * doc["expected_common_cells"]
                and doc["completed_common_cells"] <= doc["expected_common_cells"]
                and doc["completed_subcells"] <= doc["expected_subcells"]
                and all(doc[key] == 0 for key in manifest["zero_call_counters"]),
                "the genuine declared prefix and zero old targets or published arrays")

        def saved_record(record):
            return (isinstance(record, dict)
                    and record.get("kind") == "complete_decimal_ball_v1"
                    and record.get("mathematical_direction") == "upper"
                    and all(type(record.get(key)) is str for key in
                            ("midpoint_integer", "radius_integer", "decimal_exponent"))
                    and int(record["radius_integer"]) >= 0)

        require(saved_record(doc["integral_prefix"]), "complete saved cumulative integral prefix")
        scope = doc["scope"]
        require(scope["same_actual_Qrepair_and_original_full_high"] is True
                and scope["exact_independent_mean_and_original_all_interfaces_retained"] is True
                and scope["true_root_not_replaced_by_midpoint"] is True
                and scope["arbitrary_radial_weights_and_free_outer_cuts_compared"] is True
                and scope["selected_correlated_body_budget_retained"] is True
                and all(scope[key] is False for key in (
                    "optimized_body_error_lower_bound_proved", "actual_positive_boundary_problem_singular",
                    "localized_receiver_budget_proved", "positive_inverse_proved", "final_topic_complete")),
                "same precise receiver budget, never a claim about BVP singularity or completion")
        if doc["complete"]:
            require(doc["proved"] is True and doc["failure"] is None
                    and doc["stage"] == "complete-quadratic-cap-true-root-capacity-screen"
                    and doc["completed_common_cells"] == doc["expected_common_cells"]
                    and doc["completed_subcells"] == doc["expected_subcells"]
                    and doc["completed_positive_rows"] == doc["expected_common_cells"] - 1
                    and doc["current_exact_right"] == identity["conservative_integration_interval"][1]
                    and doc["complete_test_integral"] == doc["integral_prefix"]
                    and saved_record(doc["complete_test_integral"])
                    and saved_record(doc["complete_optimized_test_upper"])
                    and scope["complete_integral_target_proved"] is True,
                    "the one whole new integral is saved completely before either comparison")
            gates = doc["strict_gates"]
            excluded = gates["selected_correlated_RA_receiver_budget_excluded"]
            require(type(excluded) is bool
                    and gates["necessary_test"] == "2-148/T2_plus-a_minus-b_minus^2/(4*(1-c_minus))"
                    and gates["root_square_strict_lower_numerator"] == "148"
                    and gates["complete_saved_upper_used"] is True
                    and gates["complete_selected_body_lower_endpoints_used"] is True
                    and gates["exact_capacity_dual_test_used"] is True
                    and gates["false_gate_means_only_this_screen_did_not_exclude"] is True
                    and gates["negative_true_BVP_or_inverse_claimed"] is False
                    and scope["selected_correlated_RA_receiver_budget_excluded"] is excluded,
                    "one complete necessary gate keeps its exact selected CV/RA budget scope")
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
        positive, germ, candidate = restore()
        marker = dict(kind="consumed_R146_quadratic_cap_root_screen_v1", problem_id=manifest["problem_id"],
                      manifest_sha256=args.manifest_sha, run_id=run, run_attempt=attempt,
                      prepared_utc=utc(), output_directory=output_dir,
                      status="original_bytes_restored_one_new_quadratic_cap_integral_reserved",
                      automatic_scientific_retry=False, old_completed_targets_may_be_recomputed=False)
        state["consumed_marker_publication"] = publish(
            lambda: {marker_path: encode(marker)}, "visible-exact: reserve R146 quadratic cap true root capacity screen", True)
        head = pull()
        materialize(head)
        state["actual_scientific_checkout"] = head
        command = [sys.executable, str(snapshots["science"]),
                   "--definition-source", str(snapshots["definition_helper"]),
                   "--positive", str(positive), "--germ", str(germ), "--candidate", str(candidate),
                   "--high", str(snapshots["high"]),
                   "--high-execution", str(snapshots["high_execution"]),
                   "--two-mode", str(snapshots["two_mode"]),
                   "--two-mode-execution", str(snapshots["two_mode_execution"]),
                   "--physical", str(snapshots["physical"]),
                   "--physical-execution", str(snapshots["physical_execution"]),
                   "--body-budget", str(snapshots["body_budget"]),
                   "--body-execution", str(snapshots["body_execution"]),
                   "--correlated", str(snapshots["correlated"]),
                   "--correlated-execution", str(snapshots["correlated_execution"]),
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
    state["completed_subcells"] = (result or {}).get("completed_subcells", 0)
    state["completed_new_short_root_integral_targets"] = 1 if state["complete"] else 0
    state["original_scientific_complete"] = (result or {}).get("complete")
    state["original_scientific_failure"] = (result or {}).get("failure")
    state["scientific_files"] = [dict(path=p, bytes=len(b), sha256=sha(b)) for p, b in staged.items()]
    for path, raw in staged.items():
        emit(path, raw)

    def final_files():
        body = encode(state)
        require(len(body) <= op["maximum_execution_bytes"], "complete execution receipt budget")
        report = ("# R146 quadratic cap true root capacity screen\n\nRun " + run + "/" + attempt
                  + "; complete: " + str(state["complete"]) + ".\n\n"
                  "The new integral uses the quadratic radial cap of length 3/200, both reflection "
                  "axes and 32 whole subdivisions of every original common cell. The true root "
                  "interval, independent mean, complete repair and original intrinsic rows remain "
                  "unchanged. RN root norms, high41, signed96/97, X, GB and R143 CV are read only.\n\n"
                  "The complete saved T2 upper gives a genuine exact-capacity dual lower, 148/T2, "
                  "and the derived complete necessary test is 2-148/T2-a-b^2/(4*(1-c)). A nonpositive "
                  "upper excludes only the fixed CV/RA nonnegative-fee budget. A positive upper is "
                  "an inconclusive necessary screen. Neither outcome asserts true BVP singularity, "
                  "an inverse, or topic completion. No old scientific target or array is produced.\n").encode()
        return {**staged, output_dir + "/execution.json": body, output_dir + "/report.md": report}

    try:
        published = publish(final_files, "visible-exact: preserve R146 quadratic cap true root capacity outcome")
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
