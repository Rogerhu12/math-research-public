#!/usr/bin/env python3
"""Stdlib Actions entry: pull current rules, bind source, run one new design lane.

No old numerical receipts or old source files are imported. Private repository
contents and credentials never enter the scientific child or public stdout.
"""
import argparse
import datetime as dt
import difflib
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile

TOPIC = "topics/visible-flex-new-mechanism"
REPOSITORY = "Rogerhu12/math-research-public"
PRIVATE = "Rogerhu12/math-research"


def emit(tag, value):
    text = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False)
    text = text.replace("::", "\\u003a\\u003a").replace("##[", "\\u0023\\u0023[")
    print("INVERSE_ACTIONS_" + tag + " " + text, flush=True)


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def clean_git_env():
    env = dict(os.environ)
    for key in list(env):
        if key.startswith(("GIT_CONFIG_", "GIT_TRACE")) or key in (
                "MR_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "GIT_CURL_VERBOSE",
                "GIT_ASKPASS", "SSH_ASKPASS"):
            env.pop(key, None)
    env["GIT_TERMINAL_PROMPT"] = "0"
    return env


def git(root, *arguments, env=None, checked=True):
    command = ["git", "-c", "credential.helper=", "-c", "http.extraHeader=",
               "-c", "http.https://github.com/.extraHeader=", *arguments]
    # The private environment supplies its credential helper after the reset.
    if env is not None:
        command = ["git", *arguments]
    result = subprocess.run(command, cwd=root, env=env or clean_git_env(),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=120, check=False)
    require(not checked or result.returncode == 0,
            "Git operation failed: " + arguments[0] + "; credentials/output withheld")
    return result


def git_text(root, *arguments, env=None):
    return git(root, *arguments, env=env).stdout.decode().strip()


def public_pull(root, request, source):
    paths = ("README.md", TOPIC + "/README.md")
    expected = request["expected_readme_blobs"]
    require(set(expected) == set(paths), "public rule paths differ")
    before = git_text(root, "rev-parse", "HEAD")
    old = {path: git(root, "show", source + ":" + path).stdout for path in paths}
    started = utc()
    result = git(root, "pull", "--rebase", "--no-autostash",
                 "https://github.com/" + REPOSITORY + ".git", "main", checked=False)
    after = git_text(root, "rev-parse", "HEAD")
    rows = {}
    for path in paths:
        new = git(root, "show", after + ":" + path).stdout
        source_blob = git_text(root, "rev-parse", source + ":" + path)
        current_blob = git_text(root, "rev-parse", after + ":" + path)
        difference = "".join(difflib.unified_diff(
            old[path].decode().splitlines(True), new.decode().splitlines(True),
            fromfile=source + ":" + path, tofile=after + ":" + path))
        rows[path] = {"expected_blob": expected[path], "source_blob": source_blob,
                      "after_pull_blob": current_blob, "diff": difference,
                      "matches": source_blob == current_blob == expected[path]}
    record = {"actual_git_pull": True, "started_at": started, "completed_at": utc(),
              "before": before, "after": after, "returncode": result.returncode,
              "readmes": rows, "git_output_sha256": sha256(result.stdout + result.stderr)}
    emit("PUBLIC_PULL", record)
    require(result.returncode == 0 and all(row["matches"] for row in rows.values()),
            "Public pull failed or README changed: apply the printed exact diff before new science")
    return after


def private_pull(request):
    token = os.environ.get("MR_TOKEN", "")
    require(bool(token), "MR_TOKEN is required for the authorized private rule pull")
    env = clean_git_env()
    env.update({"GITHUB_TOKEN": token, "GIT_CONFIG_COUNT": "2",
                "GIT_CONFIG_KEY_0": "credential.helper", "GIT_CONFIG_VALUE_0": "",
                "GIT_CONFIG_KEY_1": "credential.helper",
                "GIT_CONFIG_VALUE_1":
                    "!f() { printf '%s\\n' 'username=x-access-token' \"password=$GITHUB_TOKEN\"; }; f"})
    expected = request["expected_private_readme_blobs"]
    require(set(expected) == {"README.md"}, "private root rule binding differs")
    with tempfile.TemporaryDirectory(prefix="inverse-private-rules-",
                                     dir=os.environ["RUNNER_TEMP"]) as folder:
        private = Path(folder) / "private"
        git(Path(folder), "clone", "--filter=blob:none", "--depth", "1", "--no-checkout",
            "--branch", "main", "https://github.com/" + PRIVATE + ".git", str(private), env=env)
        git(private, "config", "gc.auto", "0", env=env)
        git(private, "config", "maintenance.auto", "false", env=env)
        git(private, "sparse-checkout", "init", "--no-cone", env=env)
        git(private, "sparse-checkout", "set", "--no-cone", "/README.md", "/QUEUE.md", env=env)
        git(private, "checkout", "main", env=env)
        before = git_text(private, "rev-parse", "HEAD", env=env)
        started = utc()
        git(private, "pull", "--rebase", "--no-autostash", "origin", "main", env=env)
        after = git_text(private, "rev-parse", "HEAD", env=env)
        current = git_text(private, "rev-parse", "HEAD:README.md", env=env)
        rows = [line for line in (private / "QUEUE.md").read_text().splitlines()
                if chr(96) + TOPIC + chr(96) in line]
        ongoing = (len(rows) == 1 and "进行中" in rows[0]
                   and request["queue_session"] in rows[0])
        record = {"actual_git_pull": True, "repository": PRIVATE,
                  "started_at": started, "completed_at": utc(), "before": before,
                  "after": after, "expected_root_blob": expected["README.md"],
                  "after_pull_root_blob": current, "root_matches": current == expected["README.md"],
                  "queue_unique_and_ongoing_for_this_session": ongoing,
                  "private_contents_not_published": True}
        if current != expected["README.md"]:
            prior = request["private_rules_read_commit"]
            git(private, "fetch", "--depth", "1", "origin", prior, env=env)
            old = git(private, "show", prior + ":README.md", env=env).stdout
            new = git(private, "show", "HEAD:README.md", env=env).stdout
            difference = "".join(difflib.unified_diff(
                old.decode().splitlines(True), new.decode().splitlines(True)))
            record["private_diff"] = {"path": "README.md", "from_commit": prior,
                                      "to_commit": after, "bytes": len(difference.encode()),
                                      "sha256": sha256(difference.encode()),
                                      "read_privately_before_continuing": True}
        emit("PRIVATE_PULL", record)
        require(record["root_matches"], "Private README changed; exact blob/diff identity printed, read the diff privately")
        require(ongoing, "Private QUEUE no longer lists this session as ongoing")
        return after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True)
    parser.add_argument("--lane", required=True)
    args = parser.parse_args()
    root = Path.cwd()
    source = os.environ["GITHUB_SHA"]
    require(re.fullmatch(r"[0-9a-f]{40}", source) is not None, "invalid Actions source commit")
    raw_request = Path(args.request).read_bytes()
    request = json.loads(raw_request)
    require(request["repository"] == REPOSITORY, "repository identity differs")
    require(args.lane in request["lanes"], "unknown inverse design lane")
    require(platform.python_version() == request["runtime"]["python"], "Python version differs")
    try:
        public_after = public_pull(root, request, source)
        private_after = private_pull(request)
    finally:
        for name in ("MR_TOKEN", "GITHUB_TOKEN", "GH_TOKEN"):
            os.environ.pop(name, None)
    git(root, "checkout", "--detach", source)
    require(Path(args.request).read_bytes() == raw_request, "request differs at pinned source")
    bindings = {}
    for path, expected in request["source_sha256"].items():
        actual = sha256(Path(path).read_bytes())
        require(actual == expected, "source hash differs: " + path)
        bindings[path] = actual
    parameters = dict(request["common_parameters"])
    parameters.update(request["lanes"][args.lane])
    command = [sys.executable, request["entry_point"]]
    for name, value in parameters.items():
        option = "--" + name.replace("_", "-")
        if isinstance(value, bool):
            if value:
                command.append(option)
        else:
            command.extend((option, str(value)))
    emit("SOURCE", {"source_commit": source, "run_id": os.environ["GITHUB_RUN_ID"],
                    "run_attempt": os.environ["GITHUB_RUN_ATTEMPT"], "lane": args.lane,
                    "public_rules_read_commit": public_after,
                    "private_rules_read_commit": private_after,
                    "request_path": args.request, "request_bytes": len(raw_request),
                    "request_sha256": sha256(raw_request), "source_sha256": bindings,
                    "parameters": parameters, "command": command,
                    "runtime": request["runtime"], "old_scope_replayed": False})
    packages = request["runtime"]["packages"]
    subprocess.run([sys.executable, "-m", "pip", "install", "--disable-pip-version-check",
                    "--no-cache-dir", *[name + "==" + version for name, version in packages.items()]],
                   check=True)
    actual_versions = {name: importlib.metadata.version(name) for name in packages}
    require(actual_versions == packages, "installed numerical versions differ")
    emit("RUNTIME", {"python": platform.python_version(), "packages": actual_versions,
                     "credentials_removed_before_science": True})
    started = utc()
    result = subprocess.run(command, check=False)
    emit("FINISHED", {"lane": args.lane, "started_at": started, "completed_at": utc(),
                      "returncode": result.returncode, "stdout_only": True,
                      "frozen_metric_convergence_claim": False, "README_completion_claim": False})
    return result.returncode


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        emit("ERROR", {"type": type(error).__name__, "message": str(error)})
        raise SystemExit(2) from None

