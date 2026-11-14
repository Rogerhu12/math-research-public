#!/usr/bin/env python3
"""Publish only this run's complete, bounded ISP result directory.

Called by the fixed one31*h0 Actions workflow after real outputs and artifacts
exist. No shared research index is edited. No token is written to a file.
"""
from __future__ import annotations
import argparse
import base64
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
sys.dont_write_bytecode = True

RULES = ("README.md", "topics/invariant-subspace-problem/README.md")
PREFIX = "topics/invariant-subspace-problem/notes/r150-one31-h0-actions-789f"
MAX_PART = 4_500_000

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1048576), b""):
            h.update(b)
    return h.hexdigest()

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")

def pack_tree(results, output):
    """Keep every actual result, compress large plain files and split at4.5MB."""
    output.mkdir(parents=True, exist_ok=False)
    entries = []
    for source in sorted(results.rglob("*")):
        if not source.is_file():
            continue
        if source.is_symlink():
            raise ValueError("symlink in actual result tree")
        relative = source.relative_to(results)
        if relative.parts[0] == "publication":
            continue
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        item = {"originalFile": str(relative), "originalBytes": source.stat().st_size,
                "originalSHA256": sha(source), "stored": []}
        already_compressed = ".gz" in source.name
        compress = source.stat().st_size > 1_000_000 and not already_compressed
        if compress:
            temporary = output.parent / (hashlib.sha256(str(relative).encode()).hexdigest() + ".packing.gz")
            with source.open("rb") as src, temporary.open("wb") as dst:
                with gzip.GzipFile(filename="", mode="wb", fileobj=dst, mtime=0) as zipped:
                    shutil.copyfileobj(src, zipped)
            candidate = temporary
            target = Path(str(target) + ".gz")
            item.update(storage="gzip", compressedBytes=candidate.stat().st_size,
                        compressedSHA256=sha(candidate))
        else:
            temporary = None
            candidate = source
            item["storage"] = "unchanged"
        if candidate.stat().st_size <= MAX_PART:
            shutil.copyfile(candidate, target)
            item["stored"].append({"file": str(target.relative_to(output)),
                "bytes": target.stat().st_size, "sha256": sha(target)})
        else:
            item["storage"] += "-parts"
            with candidate.open("rb") as src:
                part = 1
                while data := src.read(MAX_PART):
                    piece = Path(str(target) + f".part{part:03d}")
                    piece.write_bytes(data)
                    item["stored"].append({"file": str(piece.relative_to(output)),
                        "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
                    part += 1
        if temporary:
            temporary.unlink()
        entries.append(item)
    manifest = {"format": "r150-one31-h0-actual-publication-files-v1",
                "maximumStoredBytes": MAX_PART, "preservesActualResults": True,
                "largePlainFilesCompressed": True, "files": entries}
    write_json(output / "publication-file-manifest.json", manifest)
    return manifest

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--checkout", type=Path, required=True)
    p.add_argument("--results", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    args = p.parse_args()
    checkout, results, work = [x.resolve() for x in (args.checkout, args.results, args.work)]
    run_id, attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    if not run_id.isdigit() or not attempt.isdigit():
        raise ValueError("numeric run and attempt required")
    if os.environ["GITHUB_REPOSITORY"] != "Rogerhu12/math-research-public":
        raise ValueError("fixed public repository only")
    if not os.environ.get("GH_TOKEN"):
        raise ValueError("Actions secret GH_TOKEN is required for terminal git")
    source_commit = os.environ["GITHUB_SHA"]
    authentication = base64.b64encode(("x-access-token:" + os.environ["GH_TOKEN"]).encode()).decode()
    git_environment = dict(os.environ)
    git_environment.update(GIT_CONFIG_COUNT="2",
        GIT_CONFIG_KEY_0="http.https://github.com/.extraheader",
        GIT_CONFIG_VALUE_0="AUTHORIZATION: basic " + authentication,
        GIT_CONFIG_KEY_1="credential.helper", GIT_CONFIG_VALUE_1="")
    source = json.loads((results / "actions-source.json").read_text())
    expected = source["rules_sha256"]
    if set(expected) != set(RULES):
        raise ValueError("exact two README rules required")
    if source["source_commit"] != source_commit:
        raise ValueError("same actual source commit")
    work.mkdir(parents=True, exist_ok=True)
    publication = results / "publication"
    publication.mkdir(exist_ok=True)
    receipt_path = publication / "publication-receipt.json"
    state = {"format": "r150-one31-h0-terminal-publication-v1", "status": "preparing",
        "run_id": run_id, "run_attempt": attempt, "source_commit": source_commit,
        "allowedResultDirectory": PREFIX + "/" + run_id + "-" + attempt,
        "sharedResearchIndicesEdited": False, "forcePushUsed": False,
        "rulesAtSource": expected, "pulls": [], "pushes": [],
        "actualOutputsPreservedBeforeGit": True}
    log = publication / "terminal-git.log"
    def save():
        write_json(receipt_path, state)
    def git(*arguments, check=True):
        # Command-scoped Git environment only: no expanded credential is written.
        command = ["git"] + list(arguments)
        proc = subprocess.run(command, cwd=checkout, env=git_environment,
                              capture_output=True, text=True, timeout=180)
        safe_stdout, safe_stderr = proc.stdout, proc.stderr
        token = os.environ.get("GH_TOKEN", "")
        if token:
            safe_stdout = safe_stdout.replace(token, "***")
            safe_stderr = safe_stderr.replace(token, "***")
        safe_stdout = safe_stdout.replace(authentication, "***")
        safe_stderr = safe_stderr.replace(authentication, "***")
        with log.open("a") as f:
            f.write("$ git " + " ".join(arguments) + "\n")
            f.write(safe_stdout + safe_stderr)
            f.write("exit=" + str(proc.returncode) + "\n")
        if check and proc.returncode:
            raise RuntimeError("terminal git failed: " + " ".join(arguments[:3]))
        return proc, safe_stdout, safe_stderr
    save()
    try:
        if git("status", "--porcelain")[1].strip():
            raise RuntimeError("source checkout must be clean before publication")
        pack_dir = work / "prepared-result-tree"
        manifest = pack_tree(results, pack_dir)
        state["preparedStoredFiles"] = sum(len(x["stored"]) for x in manifest["files"]) + 1
        state["preparedOriginalBytes"] = sum(x["originalBytes"] for x in manifest["files"])
        state["status"] = "prepared-before-pull"
        save()
        branch = "isp-one31-h0-output-" + run_id + "-" + attempt
        git("switch", "-c", branch)
        git("config", "user.name", "github-actions[bot]")
        git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        last_read = source_commit
        def pull_and_check():
            nonlocal last_read
            before = last_read
            proc, stdout, stderr = git("pull", "--rebase", "origin", "main", check=False)
            origin = git("rev-parse", "origin/main")[1].strip()
            change = git("diff", before, origin, "--", *RULES)[1]
            actual = {}
            for rule in RULES:
                body = subprocess.run(["git", "show", origin + ":" + rule], cwd=checkout,
                    capture_output=True, check=True, env=git_environment).stdout
                actual[rule] = hashlib.sha256(body).hexdigest()
            item = {"beforeReadCommit": before, "originMainAfterPull": origin,
                    "exitCode": proc.returncode, "rulesSHA256": actual,
                    "rulesDiffer": bool(change) or actual != expected}
            state["pulls"].append(item)
            last_read = origin
            state["lastRulesReadCommit"] = origin
            diff_path = publication / ("readme-diff-after-pull-" + str(len(state["pulls"])) + ".patch")
            diff_path.write_text(change)
            item["diffFile"] = diff_path.name
            save()
            if item["rulesDiffer"]:
                state["status"] = "publication-stopped-readme-change"
                state["reason"] = "Root must read this actual diff and apply changed rules; all actual artifacts retained."
                save()
                return False
            if proc.returncode:
                state["status"] = "publication-stopped-pull-rebase-error"
                state["reason"] = "No force or conflict resolution performed; actual artifacts retained."
                save()
                return False
            return True
        if not pull_and_check():
            return
        target_rel = Path(state["allowedResultDirectory"])
        target = checkout / target_rel
        if target.exists():
            raise RuntimeError("this exact run/attempt result directory already exists; do not overwrite")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(pack_dir, target)
        write_json(target / "publication-before-push.json",
            {"source_commit": source_commit, "run_id": run_id, "run_attempt": attempt,
             "lastRulesReadCommit": last_read, "rules_sha256": expected,
             "publishScope": str(target_rel), "forcePushUsed": False,
             "actualPushResultIsInThePublicationArtifact": True})
        git("add", "--", str(target_rel))
        staged = git("diff", "--cached", "--name-only", "-z")[1].split("\0")
        if any(name and not name.startswith(str(target_rel) + "/") for name in staged):
            raise RuntimeError("staged path outside this exact result directory")
        git("commit", "-m", "ISP R150: save actual original31h0 lift and recovery " + run_id)
        while True:
            commit = git("rev-parse", "HEAD")[1].strip()
            proc, stdout, stderr = git("push", "origin", "HEAD:refs/heads/main", check=False)
            state["pushes"].append({"commit": commit, "exitCode": proc.returncode})
            save()
            if proc.returncode == 0:
                state.update(status="pushed", publishedCommit=commit,
                             publishedResultDirectory=str(target_rel), lastRulesReadCommit=last_read)
                save()
                return
            # A rejected non-fast-forward is immediately followed by the real
            # pull --rebase and the two-rule diff, with no artificial retry cap.
            rejection = (stdout + stderr).lower()
            if not any(word in rejection for word in ("non-fast-forward", "fetch first", "[rejected]")):
                state.update(status="publication-stopped-other-push-error",
                             reason="Actual non-fast-forward retry applies only to a rejection; artifacts retained.")
                save()
                return
            if not pull_and_check():
                return
    except Exception as error:
        state.update(status="publication-failed", errorType=type(error).__name__, error=str(error))
        save()
    finally:
        print(json.dumps({k: state.get(k) for k in
            ("status", "publishedCommit", "publishedResultDirectory", "lastRulesReadCommit")}), flush=True)
        if state["status"] not in ("pushed", "publication-stopped-readme-change"):
            raise SystemExit(1)

if __name__ == "__main__":
    main()
