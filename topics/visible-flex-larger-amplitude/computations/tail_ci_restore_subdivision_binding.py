#!/usr/bin/env python3
"""Restore one original read-only source binding for the tail candidate.

Only 950f-tail-subdivision.mjs is materialized from the frozen 91-file
manifest and commit. Existing different bytes are never replaced. The
candidate JSON, numerical source, configuration and acceptance gates are
unchanged. No Node, ODE, Arb, or numerical child is started.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import time

PINNED = "869436630c99aa5a68afb55bd8877c826034d117"
MANIFEST_SHA = "7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941"
SOURCE_REL = "topics/visible-flexible-closed-surface/scripts/950f-tail-subdivision.mjs"
SOURCE_SHA = "e44317579d483147aa7fe73b086aba059695aa0f675b831c178902a2c0cb62e6"
SOURCE_BYTES = 5118
TARGET = Path("/workspace/scratch/c0de65fac774/visible-flex-source/topics/"
              "visible-flexible-closed-surface/scripts/950f-tail-subdivision.mjs")
TOPIC = Path("topics/visible-flex-larger-amplitude")


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def snapshot():
    exists = os.path.lexists(TARGET)
    is_file = TARGET.is_file()
    result = dict(path=str(TARGET), lexists=exists, is_file=is_file,
                  is_symlink=TARGET.is_symlink(), sha256=None, bytes=None)
    if is_file:
        result.update(sha256=digest(TARGET), bytes=TARGET.stat().st_size,
                      resolved=str(TARGET.resolve()),
                      mode=oct(stat.S_IMODE(TARGET.stat().st_mode)))
    return result


def same(record):
    return (record["is_file"] and record["sha256"] == SOURCE_SHA
            and record["bytes"] == SOURCE_BYTES)


def save(path, data):
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2, allow_nan=False)
        stream.write("\n")
    temporary.replace(path)


def run_checked(argv, *, env=None):
    value = subprocess.run(argv, env=env, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, check=False)
    if value.returncode:
        # No environment, authentication header or command stderr is recorded.
        raise RuntimeError("Fixed source recovery command failed with exit "
                           +str(value.returncode)+": "+argv[0])
    return value.stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--work-root", type=Path,
                    default=Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())))
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError("Use a fresh binding report")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    began = time.monotonic()
    report = dict(status="Actual preflight before any binding mutation",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        source_revision=PINNED, source_relative_path=SOURCE_REL,
        expected_source_sha256=SOURCE_SHA, expected_source_bytes=SOURCE_BYTES,
        before=snapshot(), numerical_child_started=False, Node_started=False,
        candidate_or_mathematical_source_modified=False,
        existing_different_binding_never_overwritten=True,
        entry_sha256=digest(__file__))
    save(args.out, report)
    print(json.dumps(dict(event="original_source_binding_preflight",
                          before=report["before"])), flush=True)
    try:
        candidate_hash = digest(args.candidate)
        candidate = read(args.candidate)
        manifest_path = args.repo/TOPIC/"computations/source-dependencies.json"
        if digest(manifest_path) != MANIFEST_SHA:
            raise ValueError("The fixed source-dependencies manifest bytes differ")
        manifest = read(manifest_path)
        if (manifest["source_revision"] != PINNED or len(manifest["files"]) != 91
                or manifest["total_bytes"] != 866846):
            raise ValueError("The original 91-file source manifest identity differs")
        rows = [row for row in manifest["files"] if row["path"] == SOURCE_REL]
        if (len(rows) != 1 or rows[0]["sha256"] != SOURCE_SHA
                or rows[0]["bytes"] != SOURCE_BYTES or not rows[0]["matches_commit"]):
            raise ValueError("The unique frozen subdivision source differs")
        if candidate["input_hashes"].get(str(TARGET)) != SOURCE_SHA:
            raise ValueError("The candidate does not bind this exact original source")
        report.update(candidate=str(args.candidate), candidate_sha256=candidate_hash,
            source_manifest=str(manifest_path), source_manifest_sha256=MANIFEST_SHA,
            original_candidate_expected_sha256=candidate["input_hashes"][str(TARGET)],
            original_other_inputs_not_rewritten=True)
        if report["before"]["lexists"] and not same(report["before"]):
            raise FileExistsError("Existing original-path data differ; no replacement attempted")
        if not report["before"]["lexists"]:
            # Fetch only this immutable commit/tree and lazily request its one blob.
            probe = subprocess.run(["git", "-C", str(args.repo), "cat-file", "-e",
                PINNED+"^{commit}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if probe.returncode:
                run_checked(["git", "-C", str(args.repo), "fetch", "--no-tags",
                    "--filter=blob:none", "--depth=1", "origin", PINNED])
            revision = run_checked(["git", "-C", str(args.repo), "rev-parse",
                                    PINNED+"^{commit}"]).decode().strip()
            if revision != PINNED:
                raise ValueError("The materialized source commit changed")
            payload = run_checked(["git", "-C", str(args.repo), "show",
                                   PINNED+":"+SOURCE_REL])
            if len(payload) != SOURCE_BYTES or hashlib.sha256(payload).hexdigest() != SOURCE_SHA:
                raise ValueError("The immutable commit blob failed both saved SHA checks")
            args.work_root.mkdir(parents=True, exist_ok=True)
            owned = Path(tempfile.mkdtemp(prefix="visible-tail-subdivision-",
                                          dir=args.work_root))
            source = owned/"950f-tail-subdivision.mjs"
            fd = os.open(source, os.O_WRONLY|os.O_CREAT|os.O_EXCL, 0o444)
            with os.fdopen(fd, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(source, 0o444)
            if digest(source) != SOURCE_SHA:
                raise ValueError("The read-only recovered blob changed before binding")
            # The only privileged target is the exact old binding, never a glob.
            # Refuse symlinked ancestors while creating a missing binding.
            if any(parent.is_symlink() for parent in TARGET.parents):
                raise ValueError("A missing binding has an unexpected symlinked ancestor")
            clean_env = {k:v for k,v in os.environ.items()
                         if not k.startswith("GIT_CONFIG_") and k not in
                         ("GH_TOKEN", "GITHUB_TOKEN", "GIT_ASKPASS", "SSH_ASKPASS")}
            try:
                TARGET.parent.mkdir(parents=True, exist_ok=True)
            except PermissionError:
                run_checked(["sudo", "-n", "mkdir", "-p", "--", str(TARGET.parent)],
                            env=clean_env)
            try:
                os.symlink(str(source.resolve()), str(TARGET))
            except PermissionError:
                # No -f: an existing destination can never be overwritten.
                attempt = subprocess.run(["sudo", "-n", "ln", "-sT", "--",
                    str(source.resolve()), str(TARGET)], env=clean_env,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if attempt.returncode and not same(snapshot()):
                    raise RuntimeError("Exclusive original-path link creation failed")
            except FileExistsError:
                if not same(snapshot()):
                    raise FileExistsError("The binding appeared with different data; no overwrite")
            report.update(action="One verified read-only blob and exclusive original-path alias",
                          owned_source=str(source), owned_source_sha256=digest(source),
                          owned_source_mode=oct(stat.S_IMODE(source.stat().st_mode)))
        else:
            report["action"] = "Reused existing identical binding without modifying it"
        report["after"] = snapshot()
        if not same(report["after"]) or digest(args.candidate) != candidate_hash:
            raise ValueError("The restored binding or unchanged candidate failed final identity")
        report.update(status="Complete exact original source binding restored",
            all_gates=True, gates=dict(fixed_manifest_and_commit=True,
                original_candidate_source_SHA_equal=True,actual_before_and_after_recorded=True,
                existing_different_bytes_not_overwritten=True,
                candidate_bytes_unchanged=True,no_numerical_or_Node_execution=True),
            elapsed_seconds=time.monotonic()-began)
        save(args.out, report)
        print(json.dumps(dict(event="original_source_binding_complete",out=str(args.out),
            action=report["action"],after=report["after"],all_gates=True)), flush=True)
    except BaseException as error:
        report.update(status="Formal original-binding recovery failure",all_gates=False,
                      error=dict(type=type(error).__name__,message=str(error)),
                      elapsed_seconds=time.monotonic()-began)
        save(args.out, report)
        raise


if __name__ == "__main__":
    main()
