#!/usr/bin/env python3
"""Recover publication of original mathematical run43638830039 without new mathematics.

Called by the fixed ninth-first Actions workflow after real outputs and artifacts
exist. No shared research index is edited. No token is written to a file.
"""
from __future__ import annotations
import argparse
import base64
import gzip
import hashlib
import json
import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
sys.dont_write_bytecode = True

RULES = ("README.md", "topics/invariant-subspace-problem/README.md")
PREFIX = "topics/invariant-subspace-problem/notes/r150-ninth-first-actions-789f"
MAX_PART = 4_500_000

ORIGINAL_RUN = "43638830039"
ORIGINAL_ATTEMPT = "1"
ORIGINAL_SOURCE = "eaa240d96fda143c65a8eccede55b64b87f50ef8"

def classify_push_error(text):
    low = text.lower()
    fatal = ("permission denied", "write access to repository not granted",
             "protected branch", "gh006", "gh013", "authentication failed",
             "requested url returned error: 403", "requested url returned error: 401")
    if any(x in low for x in fatal):
        return "nonretryable-permission-or-policy"
    if "non-fast-forward" in low or "fetch first" in low:
        return "non-fast-forward"
    if ("failed to update ref" in low and "[remote rejected]" in low) or (
            "cannot lock ref" in low and " is at " in low and " expected " in low):
        return "stale-main-ref"
    transient = ("could not resolve host", "failed to connect", "connection reset",
                 "remote end hung up unexpectedly", "connection timed out",
                 "operation timed out", "terminal git timeout", "early eof",
                 "rpc failed; http 5", "requested url returned error: 5",
                 "tls connection was non-properly terminated", "ssl_connect")
    if any(x in low for x in transient):
        return "transient-transport"
    return "nonretryable-unclassified"


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
    manifest = {"format": "r150-ninth-first-actual-publication-files-v1",
                "maximumStoredBytes": MAX_PART, "preservesActualResults": True,
                "largePlainFilesCompressed": True, "files": entries}
    write_json(output / "publication-file-manifest.json", manifest)
    return manifest


class JoinedParts(io.RawIOBase):
    """Stream verified gzip fragments without building a second large file."""
    def __init__(self, paths):
        self.paths = iter(paths)
        self.current = None
    def readable(self):
        return True
    def readinto(self, buffer):
        view = memoryview(buffer)
        done = 0
        while done < len(view):
            if self.current is None:
                try:
                    self.current = next(self.paths).open("rb")
                except StopIteration:
                    break
            n = self.current.readinto(view[done:])
            if n:
                done += n
            else:
                self.current.close()
                self.current = None
        return done
    def close(self):
        if self.current is not None:
            self.current.close()
            self.current = None
        super().close()

def preserve_recovery(recovery, results, work):
    """Verify every real recovery byte; cover an interrupted runner with lossless fallback."""
    if not recovery.is_dir():
        raise ValueError("actual recovery directory missing")
    binaries = {}
    texts = {}
    path = results / "certificate-manifest.json"
    if path.exists():
        binaries = {x["originalFile"]: x for x in json.loads(path.read_text()).get("files", [])}
    path = results / "text-recovery-manifest.json"
    if path.exists():
        texts = {x["originalFile"]: x for x in json.loads(path.read_text()).get("files", [])}
    def result_path(name):
        value = (results / name).resolve()
        if not value.is_relative_to(results) or not value.is_file() or value.is_symlink():
            raise ValueError("recovery certificate path outside actual results")
        return value
    records = []
    for source in sorted(recovery.rglob("*")):
        if not source.is_file():
            continue
        if source.is_symlink():
            raise ValueError("symlink in actual recovery tree")
        relative = str(source.relative_to(recovery))
        size, expected = source.stat().st_size, sha(source)
        record = {"originalFile": relative, "originalBytes": size,
                  "originalSHA256": expected, "allBytesPreserved": False}
        covered = False
        item = texts.get(relative)
        if item and item.get("bytes") == size and item.get("sha256") == expected:
            stored = result_path(item["file"])
            if stored.stat().st_size == size and sha(stored) == expected:
                record.update(storage="runner-exact-text", resultFiles=[item["file"]])
                covered = True
        item = binaries.get(relative)
        if not covered and item and item.get("uncompressedBytes") == size and item.get("uncompressedSHA256") == expected:
            paths = []
            compressed = hashlib.sha256()
            compressed_size = 0
            for fragment in item.get("parts", []):
                part = result_path(fragment["file"])
                if part.stat().st_size != fragment["bytes"] or sha(part) != fragment["sha256"] or part.stat().st_size > MAX_PART:
                    raise ValueError("actual recovery fragment differs: " + relative)
                with part.open("rb") as stream:
                    for block in iter(lambda: stream.read(1048576), b""):
                        compressed.update(block)
                        compressed_size += len(block)
                paths.append(part)
            if not paths or compressed_size != item["compressedBytes"] or compressed.hexdigest() != item["compressedSHA256"]:
                raise ValueError("actual complete compressed recovery differs: " + relative)
            restored = hashlib.sha256()
            restored_size = 0
            with io.BufferedReader(JoinedParts(paths), buffer_size=1048576) as joined:
                with gzip.GzipFile(fileobj=joined, mode="rb") as zipped:
                    for block in iter(lambda: zipped.read(1048576), b""):
                        restored.update(block)
                        restored_size += len(block)
            if restored_size != size or restored.hexdigest() != expected:
                raise ValueError("actual decompressed recovery differs: " + relative)
            record.update(storage="runner-lossless-gzip-parts",
                          resultFiles=[x["file"] for x in item["parts"]])
            covered = True
        if not covered:
            # A whole-process termination may precede the runner's finally block.
            # The original recovery array/prefix is still real and must be kept.
            fallback = results / "recovery-fallback"
            fallback.mkdir(exist_ok=True)
            key = hashlib.sha256(relative.encode()).hexdigest()
            temporary = work / (key + ".recovery.gz")
            with source.open("rb") as src, temporary.open("wb") as dst:
                with gzip.GzipFile(filename="", mode="wb", fileobj=dst, mtime=0) as zipped:
                    shutil.copyfileobj(src, zipped)
            compressed_size = temporary.stat().st_size
            compressed_sha = sha(temporary)
            fragments = []
            with temporary.open("rb") as src:
                part = 1
                while block := src.read(MAX_PART):
                    name = key + ".gz" if compressed_size <= MAX_PART else key + f".gz.part{part:03d}"
                    stored = fallback / name
                    stored.write_bytes(block)
                    fragments.append({"file": str(stored.relative_to(results)), "bytes": len(block),
                                      "sha256": hashlib.sha256(block).hexdigest()})
                    part += 1
            temporary.unlink()
            record.update(storage="publication-lossless-fallback", resultFiles=[x["file"] for x in fragments],
                          compressedBytes=compressed_size, compressedSHA256=compressed_sha, parts=fragments)
        record["allBytesPreserved"] = True
        records.append(record)
    result = {"format": "r150-ninth-first-complete-actual-recovery-publication-v1",
              "allActualRecoveryFilesPreserved": True,
              "allStageCachesIncluded": True,
              "originalFiles": len(records),
              "originalBytes": sum(x["originalBytes"] for x in records),
              "fallbackFiles": sum(x["storage"] == "publication-lossless-fallback" for x in records),
              "files": records}
    write_json(results / "complete-actual-recovery-publication-manifest.json", result)
    return result

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--checkout", type=Path, required=True)
    p.add_argument("--results", type=Path, required=True)
    p.add_argument("--recovery", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    args = p.parse_args()
    checkout, results, recovery, work = [x.resolve() for x in (args.checkout, args.results, args.recovery, args.work)]
    recovery_run, recovery_attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    run_id, attempt = ORIGINAL_RUN, ORIGINAL_ATTEMPT
    if not run_id.isdigit() or not attempt.isdigit():
        raise ValueError("numeric run and attempt required")
    if os.environ["GITHUB_REPOSITORY"] != "Rogerhu12/math-research-public":
        raise ValueError("fixed public repository only")
    if not os.environ.get("GH_TOKEN"):
        raise ValueError("Actions secret GH_TOKEN is required for terminal git")
    source_commit = ORIGINAL_SOURCE
    recovery_source_commit = os.environ["GITHUB_SHA"]
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
    if source["source_commit"] != source_commit or str(source.get("run_id")) != run_id or str(source.get("run_attempt")) != attempt:
        raise ValueError("same actual source commit")
    work.mkdir(parents=True, exist_ok=True)
    publication = results / "publication"
    publication.mkdir(exist_ok=True)
    receipt_path = publication / "publication-receipt.json"
    state = {"format": "r150-ninth-first-original-run-publication-recovery-v1", "status": "preparing",
        "run_id": run_id, "run_attempt": attempt, "source_commit": source_commit,
        "publicationRecoveryRunId": recovery_run, "publicationRecoveryRunAttempt": recovery_attempt,
        "publicationRecoverySourceCommit": recovery_source_commit, "newMathematicalStagesExecuted": False,
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
        try:
            proc = subprocess.run(command, cwd=checkout, env=git_environment,
                                  capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired as error:
            out = error.stdout.decode(errors="replace") if isinstance(error.stdout, bytes) else (error.stdout or "")
            err = error.stderr.decode(errors="replace") if isinstance(error.stderr, bytes) else (error.stderr or "")
            proc = subprocess.CompletedProcess(command, 124, out, err + "\nterminal git timeout\n")
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
        recovery_manifest = preserve_recovery(recovery, results, work)
        state["actualRecoveryPreservation"] = {k: recovery_manifest[k] for k in
            ("allActualRecoveryFilesPreserved", "allStageCachesIncluded", "originalFiles", "originalBytes", "fallbackFiles")}
        write_json(publication / "complete-recovery-preservation.json", recovery_manifest)
        save()
        pack_dir = work / "prepared-result-tree"
        manifest = pack_tree(results, pack_dir)
        state["preparedStoredFiles"] = sum(len(x["stored"]) for x in manifest["files"]) + 1
        state["preparedOriginalBytes"] = sum(x["originalBytes"] for x in manifest["files"])
        state["status"] = "prepared-before-pull"
        save()
        branch = "isp-ninth-first-output-" + run_id + "-" + attempt + "-recovery-" + recovery_run + "-" + recovery_attempt
        git("switch", "-c", branch)
        git("config", "user.name", "github-actions[bot]")
        git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        if git("cat-file", "-e", source_commit + "^{commit}", check=False)[0].returncode:
            while True:
                fetched, stdout, stderr = git("fetch", "--no-tags", "origin", source_commit, check=False)
                if fetched.returncode == 0:
                    break
                if classify_push_error(stdout + stderr) != "transient-transport":
                    raise RuntimeError("cannot restore the original mathematical source commit")
                time.sleep(2)
        last_read = source_commit
        input_receipt = json.loads((results / "publication-recovery-inputs.json").read_text())
        essential = input_receipt["originalResultsFiles"]
        def remote_bytes(ref, path, missing_ok=False):
            command = ["git", "show", ref + ":" + path]
            result = subprocess.run(command, cwd=checkout, env=git_environment,
                                    capture_output=True, timeout=180)
            if result.returncode:
                if missing_ok:
                    return None
                raise RuntimeError("existing main result missing " + path)
            return result.stdout
        def remote_already_saved():
            ref = git("rev-parse", "origin/main")[1].strip()
            base = state["allowedResultDirectory"]
            raw = remote_bytes(ref, base + "/publication-file-manifest.json", True)
            if raw is None:
                return False
            remote_manifest = json.loads(raw)
            mapping = {x["originalFile"]: x for x in remote_manifest["files"]}
            verified = []
            for expected_file in essential:
                name = expected_file["file"]
                item = mapping.get(name)
                if not item or item["originalBytes"] != expected_file["bytes"] or item["originalSHA256"] != expected_file["sha256"]:
                    raise RuntimeError("existing original run directory differs; no overwrite: " + name)
                fragments = []
                for stored in item["stored"]:
                    body = remote_bytes(ref, base + "/" + stored["file"])
                    if len(body) != stored["bytes"] or hashlib.sha256(body).hexdigest() != stored["sha256"]:
                        raise RuntimeError("existing main stored result hash differs: " + name)
                    fragments.append(body)
                restored = b"".join(fragments)
                if item["storage"].startswith("gzip"):
                    restored = gzip.decompress(restored)
                if len(restored) != expected_file["bytes"] or hashlib.sha256(restored).hexdigest() != expected_file["sha256"]:
                    raise RuntimeError("existing main original result bytes differ: " + name)
                verified.append(name)
            state.update(status="already-published-verified", publishedCommit=ref,
                         publishedResultDirectory=base, lastRulesReadCommit=last_read,
                         existingOriginalResultFilesVerified=verified,
                         networkUncertainPushResolvedWithoutOverwrite=True)
            save()
            return True
        def pull_once():
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
                kind = classify_push_error(stdout + stderr)
                item["failureClass"] = kind
                save()
                if kind == "transient-transport":
                    time.sleep(2)
                    return None
                if remote_already_saved():
                    return False
                state["status"] = "publication-stopped-pull-rebase-error"
                state["reason"] = "Non-transport pull/rebase failure; no force or unreviewed conflict resolution."
                save()
                return False
            if remote_already_saved():
                return False
            return True
        def pull_and_check():
            while True:
                result = pull_once()
                if result is not None:
                    return result
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
             "publicationRecoveryRunId": recovery_run, "publicationRecoveryRunAttempt": recovery_attempt,
             "publicationRecoverySourceCommit": recovery_source_commit, "newMathematicalStagesExecuted": False,
             "publishScope": str(target_rel), "forcePushUsed": False,
             "actualPushResultIsInThePublicationArtifact": True})
        git("add", "--", str(target_rel))
        staged = git("diff", "--cached", "--name-only", "-z")[1].split("\0")
        if any(name and not name.startswith(str(target_rel) + "/") for name in staged):
            raise RuntimeError("staged path outside this exact result directory")
        git("commit", "-m", "ISP R150: recover actual ninth first publication " + run_id + " via " + recovery_run)
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
            # Exact stale-main-ref races and genuine non-fast-forward failures
            # immediately perform a real pull/rebase. Permission/policy errors do not loop.
            kind = classify_push_error(stdout + stderr)
            state["pushes"][-1]["failureClass"] = kind
            save()
            if kind not in ("non-fast-forward", "stale-main-ref", "transient-transport"):
                state.update(status="publication-stopped-other-push-error",
                             reason="Actual nonretryable push response; full artifacts and stderr retained.")
                save()
                return
            # A transport failure may follow a successful remote update. The
            # next pull verifies all original result bytes on main before retry.
            if not pull_and_check():
                return
    except Exception as error:
        state.update(status="publication-failed", errorType=type(error).__name__, error=str(error))
        save()
    finally:
        print(json.dumps({k: state.get(k) for k in
            ("status", "publishedCommit", "publishedResultDirectory", "lastRulesReadCommit")}), flush=True)
        if state["status"] not in ("pushed", "already-published-verified", "publication-stopped-readme-change"):
            raise SystemExit(1)

if __name__ == "__main__":
    main()
