#!/usr/bin/env python3
"""Host-only launcher for the SAME original, pinned shadow consumer.

The future committed request contains two real complete PASS receipts.
This launcher performs only JSON/provenance/process work.  The reader alone
receives the read token; its authenticated envelope is piped directly into
the offline Sage process.  No certificate/output data file is created.
"""
import argparse
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "rank2-original-shadow-consumer-request/v1"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
TOPIC = Path("topics/rank2-sha-infinitely-many-p")
REQUEST_PATH = TOPIC / "ci/original-shadow-consumer-request.json"
DIRECTORY = Path(__file__).resolve().parent
sys.path.insert(0, str(DIRECTORY))
from original_shadow_receipt_tools import (
    canonical, digest, add_pinned_arguments, pinned_request)

DEPENDENCIES = (
    "launch-original-shadow-consumer.py",
    "read-original-shadow-pass-receipts.py",
    "original_shadow_receipt_tools.py",
    "produce-original-shadow-consumer.py",
    "produce-original-shadow-local-input.py",
    "original_good_prime_germ_tools.py",
    "check-r873-original-cm-petersson-degree.py",
    "original_low_weight_cm_tools.py",
    "produce-original-shadow-rr-eta48.py",
    "original_shadow_coordinate_tools.py",
    "original_shadow_relative_six_tools.py",
    "original_shadow_coefficient_tools.py",
)
WORKFLOW_PATH = Path(".github/workflows/rank2-sha-original-shadow-consumer.yml")
LIMIT_SECONDS = 21000
READER_LIMIT_SECONDS = 600


def progress(stage, **data):
    print("RANK2_SHADOW_LAUNCHER " + canonical(dict(stage=stage, **data)),
          file=sys.stderr, flush=True)


def checked_git(root, *arguments):
    return subprocess.check_output(
        ["git", "-C", str(root), *arguments], text=True).strip()


def file_sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_request(root):
    raw = (root / REQUEST_PATH).read_bytes()
    if len(raw) > 32768:
        raise ValueError("The fixed request must contain only the two receipt pins.")
    obj = json.loads(raw)
    required = {"schema", "prime", "first", "packet"}
    if not required.issubset(obj) or set(obj) - required - {"note"}:
        raise ValueError("Unexpected original-shadow request fields.")
    if obj["schema"] != SCHEMA or type(obj["prime"]) is not int:
        raise ValueError("Use the original shadow request schema and integer prime.")
    cli = ["--prime", str(obj["prime"])]
    keys = ("job", "run", "run_head", "source", "result_sha256")
    for stem in ("first", "packet"):
        pin = obj[stem]
        if not isinstance(pin, dict) or set(pin) != set(keys):
            raise ValueError("Pin exactly job/run/run_head/source/result_sha256.")
        for suffix in keys:
            value = pin[suffix]
            if suffix in ("job", "run"):
                if type(value) is not int or value <= 0:
                    raise ValueError("Use an actual positive public run/job ID.")
            elif not isinstance(value, str):
                raise ValueError("Source and result pins must be full strings.")
            cli.extend(["--" + stem + "-" + suffix.replace("_", "-"), str(value)])
    parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
    add_pinned_arguments(parser)
    request = pinned_request(parser.parse_args(cli))
    # These two existing original producers explicitly recorded GITHUB_SHA
    # as RANK2_SOURCE_SHA.  No alternate source interpretation is accepted.
    for stem in ("first", "packet"):
        if request[stem + "_source"] != request[stem + "_run_head"]:
            raise ValueError("For these original producers source must equal run.head_sha.")
    return cli, request, hashlib.sha256(raw).hexdigest()


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise SystemExit("Launch only in the original public research Actions.")
    root = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    if DIRECTORY != root / TOPIC / "scripts":
        raise RuntimeError("Run the committed launcher from the actual checkout.")
    source = checked_git(root, "rev-parse", "HEAD")
    if (not re.fullmatch(r"[0-9a-f]{40}", source)
            or source != os.environ.get("GITHUB_SHA")):
        raise RuntimeError("The source checkout must be exactly this workflow head.")
    run = os.environ["GITHUB_RUN_ID"]
    attempt = os.environ["GITHUB_RUN_ATTEMPT"]
    if not run.isdecimal() or not attempt.isdecimal():
        raise RuntimeError("Missing actual public run identity.")
    cli, request, request_hash = read_request(root)
    files = [TOPIC / "scripts" / name for name in DEPENDENCIES]
    files += [REQUEST_PATH, WORKFLOW_PATH, Path("README.md"), TOPIC / "README.md"]
    # This checks committed source, not any mathematical result.  Runtime
    # data remain only in the pipe and in the public log.
    if checked_git(root, "status", "--porcelain", "--", *map(str, files)):
        raise RuntimeError("The pinned source/request files must remain unmodified.")
    hashes = {str(path): file_sha256(root / path) for path in files}
    readmes = {
        "root": checked_git(root, "rev-parse", "HEAD:README.md"),
        "topic": checked_git(root, "rev-parse", "HEAD:" + str(TOPIC / "README.md")),
    }
    manifest = dict(
        kind="rank2_original_shadow_host_pipeline",
        source=source, run_id=run, run_attempt=attempt, image=IMAGE,
        parameters=request, request_sha256=request_hash,
        dependency_sha256=hashes, readme_blobs=readmes,
        token_location="host receipt reader only",
        Sage_network_mode="none", source_mount="read-only",
        recomputable_data_file_written=False,
    )
    progress("pinned source and request loaded", **manifest)
    progress("host manifest hash", sha256=digest(manifest))

    token_keys = ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN")
    host_env = os.environ.copy()
    host_env["PYTHONDONTWRITEBYTECODE"] = "1"
    docker_env = {k: v for k, v in host_env.items() if k not in token_keys}
    name = "rank2-original-shadow-" + run + "-" + attempt
    container_values = {
        "GITHUB_ACTIONS": "true",
        "GITHUB_REPOSITORY": REPOSITORY,
        "RANK2_SOURCE_SHA": source,
        "RANK2_RUN_ID": run,
        "RANK2_RUN_ATTEMPT": attempt,
        "RANK2_ROOT_README_SHA": readmes["root"],
        "RANK2_TOPIC_README_SHA": readmes["topic"],
        "RANK2_IMAGE": IMAGE,
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONUNBUFFERED": "1",
        "OMP_NUM_THREADS": "4",
    }
    command = ["docker", "run", "--rm", "--init", "--network", "none",
               "--name", name, "-i"]
    for key, value in container_values.items():
        command.extend(["-e", key + "=" + value])
    command += ["-v", str(root) + ":/work:ro", "-w", "/work",
                "--entrypoint", "/usr/bin/sage", IMAGE, "-python",
                str(TOPIC / "scripts/produce-original-shadow-consumer.py"), *cli]
    reader = None
    sage = None
    completed = False
    started = time.monotonic()

    def interrupted(signum, _frame):
        raise InterruptedError("Host pipeline interrupted by signal " + str(signum))

    old_handlers = {s: signal.signal(s, interrupted)
                    for s in (signal.SIGTERM, signal.SIGINT)}
    try:
        reader = subprocess.Popen(
            [sys.executable, str(DIRECTORY / "read-original-shadow-pass-receipts.py"), *cli],
            cwd=root, env=host_env, stdout=subprocess.PIPE)
        sage = subprocess.Popen(
            command, cwd=root, env=docker_env, stdin=reader.stdout)
        # Only the offline container retains the read end; no envelope is
        # copied into a file or into a shell argument.
        reader.stdout.close()
        reader_status = reader.wait(timeout=READER_LIMIT_SECONDS)
        if reader_status != 0:
            raise RuntimeError("Public PASS authentication failed: exit " + str(reader_status))
        remaining = LIMIT_SECONDS - (time.monotonic() - started)
        if remaining <= 0:
            raise TimeoutError("The public original consumer exhausted its time limit.")
        sage_status = sage.wait(timeout=remaining)
        if sage_status != 0:
            raise RuntimeError("Offline Sage consumer failed: exit " + str(sage_status))
        completed = True
        progress("both pipeline processes exited successfully",
                 source=source, run_id=run, reader_exit=reader_status,
                 Sage_exit=sage_status, elapsed_seconds=time.monotonic() - started)
    finally:
        if not completed:
            progress("pipeline not completed; no mathematical PASS is asserted",
                     source=source, run_id=run)
            # Stop children and the named container on any reader/consumer
            # failure or the public workflow timeout.
            for child in (reader, sage):
                if child is not None and child.poll() is None:
                    child.terminate()
            subprocess.run(["docker", "rm", "-f", name], env=docker_env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=30, check=False)
            for child in (reader, sage):
                if child is not None:
                    try:
                        child.wait(timeout=15)
                    except subprocess.TimeoutExpired:
                        child.kill()
                        child.wait(timeout=15)
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)


if __name__ == "__main__":
    main()
