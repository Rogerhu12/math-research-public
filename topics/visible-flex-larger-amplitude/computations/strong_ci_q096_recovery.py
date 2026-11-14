#!/usr/bin/env python3
"""Fresh GitHub Actions recovery of the original actual q096 continuation.

This is an orchestration/storage entry. It does not modify the numerical
Python modules, any MJS, any saved accepted array, the physical target, the
discrete equations, or the complete full-H/final-audit gates.
The inaccessible local r7/session80885 remains terminal-status UNKNOWN.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys

TOPIC = Path("topics/visible-flex-larger-amplitude")
PINNED = "869436630c99aa5a68afb55bd8877c826034d117"
MANIFEST_SHA = "7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941"
PLAN_REL = "notes/2026-11-12-strong-actual-q096-combined-m24-tol7-prefixcache-radial8-heap96-r6-command-plan.json"
PLAN_SHA = "fecb01effac42b8945d2bd29612c76373d3afa1982d021c2f3b576306ed9c9e3"
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
THREAD_ENV = {k: "1" for k in (
    "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"
)}
EXPECTED_INPUTS = {
    "notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1.json.gz":
        "1d7f6f0ab3b7b51b8d647cf823f9aa72d5de9b6925fc87fd1b687b864a9e3423",
    "notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1-raw-collocation.json.gz":
        "8fe885fe87eec09e4d0d9508099a82c48a9627f8568021e2bfe28907f62d1f5e",
    "notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1-tail-response_0003.json.gz":
        "32ee699bd596bf397db66a73f9e7470b315286d05e2f13b97a818a64a2c271cb",
    "notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1-config.json":
        "6dad973d9d6e992d13663e8100eeddcf93a45d41703982767ce175b3b3dcb3a3",
    "notes/2026-11-12-strong-q095-actual-fixed-control-response.json":
        "72d6615a3699769451dd9af11bb89a769ba2fb9651438cde72da5fe485efb36c",
    "notes/2026-11-12-strong-actual-q096-cached-iteration-tail-audit-heap96-young4-r11-response_0001.json.gz":
        "c8420b9b33df6472b05bd31604c69feb2470cf6d41310c8d8ca785942d15efd2",
    "notes/2026-11-12-strong-actual-q096-cached-iteration-tail-audit-heap96-young4-r11-ready.json":
        "e2be7cb8c4e136624d804faf3da394d1f859ba73427d17be89680cbbf6b0fde5",
}


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def atomic_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp-" + str(os.getpid()))
    data = (json.dumps(value, indent=2, allow_nan=False) + "\n").encode()
    with temporary.open("xb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def checked_file(path, expected=None):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError("Required committed input is absent: " + str(path))
    actual = digest(path)
    if expected is not None and actual != expected:
        raise ValueError("Committed input SHA256 differs: " + str(path))
    return dict(path=str(path), bytes=path.stat().st_size, sha256=actual)


def substitute(argv, flag, value):
    if argv.count(flag) != 1:
        raise ValueError("Expected one retained argument: " + flag)
    argv[argv.index(flag) + 1] = str(value)


def output_arg(argv, name):
    return argv[argv.index(name) + 1]


def numerical_environment(environment):
    # Git authentication is needed only while materializing promised source
    # blobs. Never pass it to the numerical supervisor or any Node process.
    return {key: value for key, value in environment.items()
        if not key.startswith('GIT_CONFIG_') and key not in (
            'GH_TOKEN', 'GITHUB_TOKEN', 'GIT_ASKPASS', 'SSH_ASKPASS')}


def runtime_versions(env):
    import numpy
    import scipy
    if platform.python_version() != "3.12.14":
        raise ValueError("Use the explicitly recorded Python3.12.14")
    if numpy.__version__ != "2.3.5" or scipy.__version__ != "1.17.0":
        raise ValueError("Use NumPy2.3.5 and SciPy1.17.0 for this recovery")
    info = json.loads(subprocess.check_output([
        "node", "-p",
        "JSON.stringify({node:process.versions.node,v8:process.versions.v8,"
        "platform:process.platform,arch:process.arch})"
    ], env=env, text=True))
    if info["node"] != "24.22.1":
        raise ValueError("Use the recorded Node24.22.1; do not spoof cache identity")
    return dict(python=platform.python_version(), numpy=numpy.__version__,
        scipy=scipy.__version__, node=info, platform=platform.platform(),
        machine=platform.machine(), source_and_runtime_cache_keys_recomputed=True,
        old_runtime_byte_replay_not_claimed=True)


def restore_source(repo, topic, destination, env):
    manifest_path = topic / "computations/source-dependencies.json"
    checked_file(manifest_path, MANIFEST_SHA)
    manifest = read_json(manifest_path)
    if (manifest["source_revision"] != PINNED or len(manifest["files"]) != 91
            or manifest["total_bytes"] != 866846):
        raise ValueError("Pinned91 source manifest identity differs")
    probe = subprocess.run(["git", "-C", str(repo), "cat-file", "-e",
        PINNED + "^{commit}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if probe.returncode:
        # Fetch only this commit/tree and lazily requested blobs; never clone a
        # whole topic. Authentication is inherited, not written by this script.
        subprocess.run(["git", "-C", str(repo), "fetch", "--no-tags",
            "--filter=blob:none", "--depth=1", "origin", PINNED], env=env, check=True)
    helper = topic / "computations/prepare-source-dependencies.py"
    subprocess.run([sys.executable, str(helper), "--repo", str(repo),
        "--dest", str(destination), "--manifest", str(manifest_path)],
        cwd=topic, env=env, check=True)
    for item in manifest["files"]:
        relative = Path(item["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Invalid pinned source path")
        path = destination / relative
        checked_file(path, item["sha256"])
        if path.stat().st_size != item["bytes"]:
            raise ValueError("Pinned source byte count differs")
    source_topic = destination / "topics/visible-flexible-closed-surface"
    origin = read_json(source_topic / "source-origin.json")
    expected = dict(source_revision=PINNED, files=91, bytes=866846,
        manifest_sha256=MANIFEST_SHA)
    if origin != expected:
        raise ValueError("Materialized source-origin differs")
    return source_topic, dict(**expected,
        source_topic=str(source_topic), all91_individual_files_verified=True,
        helper=checked_file(helper))


def verify_inputs(topic, retained_plan, source_topic):
    records = [checked_file(topic / name, value) for name, value in EXPECTED_INPUTS.items()]
    for name, value in retained_plan["source_sha256"].items():
        records.append(checked_file(topic / "computations" / name, value))
    argv = retained_plan["run_argv"]
    for flag in ("--frozen-reference-ready", "--frozen-calibration-ledger", "--port"):
        records.append(checked_file(topic / output_arg(argv, flag)))
    raw_path = topic / output_arg(argv, "--actual-reference-raw")
    raw = read_json(raw_path)
    for array in raw["arrays"].values():
        first = 0
        for chunk in array["chunks"]:
            if (Path(chunk["file"]).name != chunk["file"] or chunk["first"] != first):
                raise ValueError("Accepted raw chunk layout differs")
            records.append(checked_file(raw_path.parent / chunk["file"], chunk["sha256"]))
            first += chunk["count"]
    response = read_json(topic / output_arg(argv, "--response-data"))
    for item in response["tangent_arrays"]:
        # Preserve the old relative notes paths and accepted file bytes.
        # This does not rewrite source/provenance dictionaries.
        path = Path(item["file"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("This response requires an explicit old-path alias, not relabelling")
        records.append(checked_file(topic / path, item["sha256"]))
    packet = read_json(topic / output_arg(argv, "--initial-audited-tail-packet"))
    for name, value in packet["source_sha256"].items():
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("A recorded source requires an explicit old-path alias: " + name)
        local = topic / "computations" / relative
        records.append(checked_file(local if local.is_file() else source_topic / "scripts" / relative, value))
    # Keep every referenced physical-PPoly chunk next to its original primary.
    primary_path = topic / output_arg(argv, "--actual-reference")
    primary = read_json(primary_path)
    physical_chunks = []
    def visit(value):
        if isinstance(value, dict):
            if "file" in value and "sha256" in value and isinstance(value["file"], str):
                relative = Path(value["file"])
                candidates = ([primary_path.parent / relative] if relative.name == str(relative)
                    else [topic / relative] if not relative.is_absolute() and ".." not in relative.parts else [])
                for path in candidates:
                    if path.is_file():
                        physical_chunks.append(checked_file(path, value["sha256"]))
                        break
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(primary)
    records.extend(physical_chunks)
    unique = {record["path"]: record for record in records}
    return list(unique.values())


def collect_outputs(topic, prefix):
    files = []
    for path in sorted(prefix.parent.glob(prefix.name + "*")):
        if not path.is_file() or ".tmp-" in path.name:
            continue
        # Logs are auxiliary; primary manifests/arrays are never rewritten.
        if path.stat().st_size > 1_000_000 and path.suffix in (".log", ".jsonl"):
            target = path.with_name(path.name + ".gz")
            if target.exists():
                raise FileExistsError("Refuse to overwrite an auxiliary log archive")
            with path.open("rb") as source, target.open("xb") as output:
                with gzip.GzipFile(filename="", fileobj=output, mode="wb", mtime=0) as compressed:
                    shutil.copyfileobj(source, compressed, 1024 * 1024)
            path = target
        item = checked_file(path)
        item["path"] = str(path.relative_to(topic))
        item["git_file_size_gate"] = item["bytes"] < 5_000_000
        files.append(item)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--work-root", type=Path, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--prepare-only", action="store_true")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}", args.run_id):
        raise ValueError("Use a fresh simple CI run ID")
    repo = args.repo.resolve()
    topic = repo / TOPIC
    work = args.work_root.resolve() / ("strong-q096-" + args.run_id)
    work.mkdir(parents=True, exist_ok=False)
    prefix = topic / "notes" / ("2026-11-12-strong-actual-q096-ci-" + args.run_id)
    if any(prefix.parent.glob(prefix.name + "*")):
        raise FileExistsError("Fresh CI output prefix already exists")
    temporary = work / "temporary-arenas"
    temporary.mkdir()
    stage_cache, prefix_cache = work / "tail-stage-cache", work / "prefix-call-cache"
    stage_cache.mkdir()
    prefix_cache.mkdir()
    env = dict(os.environ)
    env.update(THREAD_ENV)
    env.update(PYTHONUNBUFFERED="1", TMPDIR=str(temporary))
    if shutil.disk_usage(temporary).free < 1_000_000_000:
        raise OSError("Need room for 576500856 arena bytes plus outputs; select a roomier owned disk")
    for key, value in THREAD_ENV.items():
        os.environ[key] = value
    versions = runtime_versions(numerical_environment(env))
    plan_path = topic / PLAN_REL
    checked_file(plan_path, PLAN_SHA)
    retained = read_json(plan_path)
    source_topic, origin = restore_source(repo, topic, work / "source", env)
    env = numerical_environment(env)
    for key in tuple(os.environ):
        if key not in numerical_environment({key: os.environ[key]}):
            os.environ.pop(key, None)
    inputs = verify_inputs(topic, retained, source_topic)
    command = list(retained["run_argv"])
    if command[1:3] != ["-u", "computations/strong_cached_prefix_actual_bvp.py"]:
        raise ValueError("Retained production entry changed")
    command[0] = sys.executable
    relative_prefix = str(prefix.relative_to(topic))
    replacements = {
        "--source-topic": str(source_topic),
        "--out-prefix": relative_prefix,
        "--stage-cache-directory": str(stage_cache),
        "--prefix-cache-directory": str(prefix_cache),
    }
    for flag, value in replacements.items():
        substitute(command, flag, value)
    supervisor = [sys.executable, "-u", "computations/strong_foreground_resource_run.py",
        "--out", relative_prefix + "-resource.json",
        "--heartbeat", relative_prefix + "-heartbeat.json",
        "--ownership", relative_prefix + "-ownership.json",
        "--task-prefix", relative_prefix, "--", *command]
    metadata = dict(scope=__doc__, status="prepared-not-executed",
        created_utc=utc(), entry_sha256=SELF_SHA, source_plan=str(plan_path),
        source_plan_sha256=PLAN_SHA, source_restore=origin, inputs=inputs,
        command=command, supervisor_command=supervisor, cwd=str(topic),
        environment={**THREAD_ENV, "PYTHONUNBUFFERED": "1", "TMPDIR": str(temporary)},
        versions=versions, git_head=subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip(),
        readme_sha256={str(path): digest(repo/path) for path in (Path("README.md"), TOPIC/"README.md")},
        path_changes=replacements, cache_directories_fresh=True,
        git_authentication_environment_removed_before_numerical_supervisor_and_Node=True,
        full_environment_never_serialized=True,
        original_r7_session80885_terminal_status="unknown",
        original_r6_status="formal exit1, explicit ENOSPC, no accepted prefix step",
        original_r6_complete334_Jacobian_cache_available_on_this_runner=False,
        old_prefix_cache_identity_not_relabelled=True,
        exact_r11_audited_response_reused_only_through_original_full_H_gates=True,
        original_all_equations_gauges_target_grid_tolerance_true_H_audit_gates_preserved=True,
        all_MJS_unchanged=True, initial_disk_free_bytes=shutil.disk_usage(temporary).free)
    atomic_json(str(prefix) + "-ci-plan.json", metadata)
    print(json.dumps(dict(event="ci_q096_prepared", out=relative_prefix,
        source_files=91, source_bytes=866846, old_r7="unknown",
        prepared_only=bool(args.prepare_only))), flush=True)
    if args.prepare_only:
        return
    log = Path(str(prefix) + ".log")
    code = None
    try:
        with log.open("xb") as stream:
            child = subprocess.Popen(supervisor, cwd=topic, env=env,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for block in iter(child.stdout.readline, b""):
                stream.write(block)
                stream.flush()
                sys.stdout.buffer.write(block)
                sys.stdout.buffer.flush()
            code = child.wait()
    finally:
        resource_path = Path(str(prefix) + "-resource.json")
        resource_record = read_json(resource_path) if resource_path.is_file() else None
        summary_path = Path(str(prefix) + "-summary.json")
        summary = read_json(summary_path) if summary_path.is_file() else None
        terminal = dict(scope="CI supervisor completion only; numerical success comes from the original audited summary.",
            finished_utc=utc(), entry_sha256=SELF_SHA, supervisor_returncode=code,
            owned_wait4_record=resource_record, original_r7_session80885_terminal_status="unknown",
            summary_file=str(summary_path.relative_to(topic)) if summary is not None else None,
            solver_success=None if summary is None else summary.get("solver_success"),
            audit_pending=None if summary is None else summary.get("audit_pending"),
            numerical_solution_not_inferred_from_process_exit=True,
            final_disk_free_bytes=shutil.disk_usage(temporary).free,
            cache_paths_for_artifact_only=[str(prefix_cache), str(stage_cache)])
        atomic_json(str(prefix) + "-ci-terminal.json", terminal)
        files = collect_outputs(topic, prefix)
        atomic_json(str(prefix) + "-ci-stable-files.json", dict(
            scope="Completed output snapshot after this supervisor returned; caches are separately reproducible.",
            files=files, any_oversize_file=any(not item["git_file_size_gate"] for item in files),
            original_solver_success_and_audit_complete=bool(summary is not None and summary.get("solver_success")
                and not summary.get("audit_pending", True)),
            complete_topic_acceptance_claimed=False))
    if code is None:
        raise RuntimeError("The local supervisor did not produce a formal return")
    raise SystemExit(code if code >= 0 else 128-code)


if __name__ == "__main__":
    main()
