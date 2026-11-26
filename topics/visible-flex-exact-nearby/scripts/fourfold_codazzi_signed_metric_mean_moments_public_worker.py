#!/usr/bin/env python3
"""Restore the existing mean native, run one new signed moment target, publish scalars."""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import traceback
import urllib.request

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OUTPUT_BASE = TOPIC + "/notes/signed_metric_mean_moments_ci"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode()


def utc():
    return datetime.now(timezone.utc).isoformat()


def atomic(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--manifest-sha", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "authorized public Actions repository")
    root = args.repo.resolve()
    os.chdir(root)
    token = os.environ["GITHUB_TOKEN"]
    auth = base64.b64encode(("x-access-token:" + token).encode()).decode()
    os.environ.update(GIT_CONFIG_COUNT="1",
                      GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
                      GIT_CONFIG_VALUE_0="AUTHORIZATION: basic " + auth)

    def git(*command, check=True, binary=False):
        result = subprocess.run(
            ["git", "-c", "user.name=github-actions[bot]",
             "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
             *command], cwd=root, capture_output=True, text=not binary)
        if check and result.returncode:
            error = result.stderr.decode("utf-8", "replace") if binary else result.stderr
            raise RuntimeError("git " + " ".join(command) + ": " + error)
        return result

    mpath = root / args.manifest
    manifest_raw = mpath.read_bytes()
    require(sha(manifest_raw) == args.manifest_sha, "declared complete input manifest")
    manifest = json.loads(manifest_raw)
    require(manifest["repository"] == REPO
            and manifest["kind"] == "R144_signed_metric_mean_moments_inputs_v1",
            "same new signed-moment task")
    run, attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    destination = OUTPUT_BASE + "/run-" + run + "-" + attempt
    temporary = Path(tempfile.mkdtemp(prefix="r144-signed-metric-mean-",
                                    dir=os.environ.get("RUNNER_TEMP")))
    output = temporary / "signed-metric-mean-moments.json"
    state = dict(kind="R144_signed_metric_mean_moments_execution_v1",
                 repository=REPO, run_id=run, run_attempt=attempt,
                 manifest_sha256=args.manifest_sha, started_utc=utc(),
                 event_commit=os.environ["GITHUB_SHA"],
                 complete=False, failure=None, scientific_children=0,
                 old_producers_called=0, old_scientific_targets_recomputed=0,
                 new_arrays_published=0, new_artifacts=0, new_Releases=0,
                 readme_checks=[], current_inputs=[], restored_inputs=[],
                 publication_attempts=0, actual_child_returncode=None)
    staged, paths = {}, {}

    def pull():
        before = git("rev-parse", "HEAD").stdout.strip()
        git("pull", "--rebase", "origin", "main")
        after = git("rev-parse", "HEAD").stdout.strip()
        diff = git("diff", before, after, "--", *manifest["readmes"]).stdout
        receipt = dict(before=before, after=after, checked_utc=utc(), diff=diff)
        state["readme_checks"].append(receipt)
        for path, expected in manifest["readmes"].items():
            observed = sha(git("show", after + ":" + path, binary=True).stdout)
            if observed != expected:
                baseline = manifest["read_commit"]
                if git("cat-file", "-e", baseline + "^{commit}", check=False).returncode:
                    git("fetch", "--filter=blob:none", "--no-tags", "--depth=1", "origin", baseline)
                full_diff = git("diff", baseline, after, "--", path).stdout
                receipt["new_rules_diff"] = full_diff
                print(full_diff, flush=True)
                raise RuntimeError("README changed; preserve this receipt for the continuing owner: " + path)
        return after

    def emit(relative, raw):
        print("BEGIN COMPLETE PUBLIC FILE " + relative + " bytes=" + str(len(raw))
              + " sha256=" + sha(raw), flush=True)
        sys.stdout.write(raw.decode())
        print("END COMPLETE PUBLIC FILE " + relative, flush=True)

    def publish():
        while True:
            state["publication_attempts"] += 1
            head = pull()
            files = dict(staged)
            files[destination + "/execution.json"] = encode(state)
            # Git ls-tree -l can hydrate missing blobs in a partial clone.
            # Read only public Git-tree size metadata for the rebased topic.
            published_base = git("rev-parse", "origin/main").stdout.strip()
            topic_tree = git("rev-parse", published_base + ":" + TOPIC).stdout.strip()
            request = urllib.request.Request(
                "https://api.github.com/repos/" + REPO + "/git/trees/"
                + topic_tree + "?recursive=1",
                headers={"Authorization": "Bearer " + token,
                         "Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(request, timeout=60) as response:
                tree = json.load(response)
            require(tree.get("sha") == topic_tree and tree.get("truncated") is False,
                    "complete topic size metadata")
            sizes = {TOPIC + "/" + item["path"]: int(item["size"])
                     for item in tree["tree"] if item["type"] == "blob"}
            for path in git("diff", "--name-only", "--no-renames",
                            published_base, head, "--", TOPIC).stdout.splitlines():
                if git("cat-file", "-e", head + ":" + path, check=False).returncode:
                    sizes.pop(path, None)
                else:
                    sizes[path] = int(git("cat-file", "-s", head + ":" + path).stdout)
            projected = sum(sizes.values())
            for path, raw in files.items():
                require(path.startswith(TOPIC + "/") and 0 < len(raw) < 100000,
                        "one complete small result or execution receipt")
                projected += len(raw) - sizes.get(path, 0)
            require(projected <= 200000000, "complete topic exceeds the 200 MB rule")
            for path, raw in files.items():
                atomic(root / path, raw)
            git("add", "--sparse", "--", *files)
            if git("diff", "--cached", "--quiet", check=False).returncode:
                git("commit", "-m", "visible-exact: record actual signed metric-mean moments")
            if git("push", "origin", "HEAD:main", check=False).returncode == 0:
                for path, raw in files.items():
                    emit(path, raw)
                return
            print("Non-fast-forward rejection: immediately rebase, check READMEs, and push again.",
                  flush=True)

    try:
        head = pull()
        # A second workflow start must not repeat an already completed target.
        previous = git("ls-tree", "-r", "--name-only", head, "--", OUTPUT_BASE).stdout
        for path in previous.splitlines():
            if path.endswith("/signed-metric-mean-moments.json"):
                prior = json.loads(git("show", head + ":" + path, binary=True).stdout)
                if prior.get("kind") == manifest["scientific_kind"] and prior.get("complete") is True:
                    print("The declared signed moment target is already complete at " + path,
                          flush=True)
                    return 0
        for spec in manifest["files"]:
            require(spec["path"].startswith(TOPIC + "/"), "current input is in the topic")
            raw = git("show", head + ":" + spec["path"], binary=True).stdout
            require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"],
                    "current input identity: " + spec["role"])
            path = temporary / (spec["role"] + Path(spec["path"]).suffix)
            atomic(path, raw)
            paths[spec["role"]] = path
            state["current_inputs"].append(spec)
        require(sha(Path(__file__).read_bytes()) ==
                next(item["sha256"] for item in manifest["files"] if item["role"] == "worker"),
                "actual running new worker")
        index = json.loads(paths["mean_parts_index"].read_bytes())
        history = manifest["historical_mean_commit"]
        require(len(history) == 40 and all(c in "0123456789abcdef" for c in history),
                "original immutable mean-container commit")
        if git("cat-file", "-e", history + "^{commit}", check=False).returncode:
            git("fetch", "--filter=blob:none", "--no-tags", "--depth=1", "origin", history)
        native = temporary / index["original_file"]
        offset = 0
        with native.open("wb") as stream:
            for number, item in enumerate(index["parts"]):
                require(item["index"] == number and item["offset"] == offset,
                        "original lossless container order")
                path = TOPIC + "/notes/" + item["file"]
                raw = git("show", history + ":" + path, binary=True).stdout
                require(len(raw) == item["compressed_bytes"]
                        and sha(raw) == item["compressed_sha256"], "original compressed input")
                chunk = gzip.decompress(raw)
                require(len(chunk) == item["bytes"] and sha(chunk) == item["sha256"],
                        "original unmodified container chunk")
                stream.write(chunk)
                offset += len(chunk)
                state["restored_inputs"].append(
                    dict(commit=history, path=path, bytes=len(raw), sha256=sha(raw)))
        raw = native.read_bytes()
        require(len(raw) == index["original_bytes"]
                and sha(raw) == index["original_sha256"] == manifest["mean_native_sha256"],
                "complete original mean native")
        state["mean_native"] = dict(bytes=len(raw), sha256=sha(raw))
        state["actual_scientific_checkout"] = head
        state["scientific_started_utc"] = utc()
        state["scientific_children"] = 1
        environment = dict(os.environ)
        for key in ("GITHUB_TOKEN", "GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0"):
            environment.pop(key, None)
        environment.update(PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1",
                           OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
        began = time.monotonic()
        child = subprocess.run(
            [sys.executable, str(paths["science"]), "--mean", str(native),
             "--cp", str(paths["cp"]), "--output", str(output)],
            cwd=temporary, env=environment, capture_output=True, timeout=900)
        state["actual_child_returncode"] = child.returncode
        state["scientific_seconds"] = time.monotonic() - began
        state["scientific_finished_utc"] = utc()
        state["child_stdout"] = dict(bytes=len(child.stdout), sha256=sha(child.stdout))
        state["child_stderr"] = dict(bytes=len(child.stderr), sha256=sha(child.stderr))
        print(child.stdout.decode("utf-8", "replace"), flush=True)
        if child.stderr:
            print(child.stderr.decode("utf-8", "replace"), flush=True)
        require(output.exists(), "new scientific child produced no complete or partial receipt")
        result = json.loads(output.read_bytes())
        require(result["kind"] == manifest["scientific_kind"], "new declared scientific result")
        state["scientific_complete"] = result.get("complete")
        state["scientific_failure"] = result.get("failure")
        require(child.returncode == 0 and result.get("complete") is True,
                "new signed moment target has an actual incomplete outcome")
        state["complete"] = True
    except BaseException as exc:
        state["failure"] = dict(type=type(exc).__name__, message=str(exc),
                                traceback=traceback.format_exc()[-6000:])
        print(traceback.format_exc(), flush=True)

    if output.exists():
        raw = output.read_bytes()
        require(len(raw) < 30000, "complete small mathematical scalar result")
        staged[destination + "/signed-metric-mean-moments.json"] = raw
        state["scientific_result"] = dict(bytes=len(raw), sha256=sha(raw))
    state["finished_utc"] = utc()
    try:
        publish()
    except BaseException:
        traceback.print_exc()
        for path, raw in dict(staged, **{destination + "/execution.json": encode(state)}).items():
            emit(path, raw)
        raise
    return 0 if state["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
