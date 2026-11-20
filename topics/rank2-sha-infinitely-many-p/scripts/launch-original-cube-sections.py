#!/usr/bin/env python3
"""Host provenance and stdin pipeline for the original complete cube section reader.

Only the existing public PASS reader receives the workflow read token.  The
mathematical process is offline, has a read-only source mount, and writes no
recomputable data file.  This launcher performs no mathematics.
"""
import argparse
import hashlib
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path
from original_shadow_receipt_tools import canonical, digest, add_pinned_arguments, pinned_request

REPOSITORY = "Rogerhu12/math-research-public"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
TOPIC = Path("topics/rank2-sha-infinitely-many-p")
REQUEST = TOPIC/"ci/original-cube-sections-request.json"
WORKFLOW = Path(".github/workflows/rank2-sha-original-cube-sections.yml")
HERE = Path(__file__).resolve().parent


def progress(stage, **kw):
    print("RANK2_CUBE_SECTIONS_HOST "+canonical(dict(stage=stage, **kw)),
          file=sys.stderr, flush=True)


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def request_arguments(root):
    raw = (root/REQUEST).read_bytes()
    assert len(raw) <= 32768
    obj = json.loads(raw)
    assert set(obj) == {"schema", "prime", "first", "packet"}
    assert obj["schema"] == "rank2-original-section-map-request/v1"
    assert type(obj["prime"]) is int and obj["prime"] in (29, 41)
    cli = ["--prime", str(obj["prime"])]
    keys = ("job", "run", "run_head", "source", "result_sha256")
    for stem in ("first", "packet"):
        pin = obj[stem]
        assert isinstance(pin, dict) and set(pin) == set(keys)
        for key in keys:
            if key in ("job", "run"):
                assert type(pin[key]) is int and pin[key] > 0
            else:
                assert isinstance(pin[key], str)
            cli += ["--"+stem+"-"+key.replace("_", "-"), str(pin[key])]
        assert pin["source"] == pin["run_head"]
    parser = argparse.ArgumentParser(add_help=False, allow_abbrev=False)
    add_pinned_arguments(parser)
    checked = pinned_request(parser.parse_args(cli))
    return cli, checked, hashlib.sha256(raw).hexdigest()


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise SystemExit("Use only the public repository Actions host.")
    root = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    assert HERE == root/TOPIC/"scripts"
    source = git(root, "rev-parse", "HEAD")
    assert source == os.environ["GITHUB_SHA"] and len(source) == 40
    run, attempt = os.environ["GITHUB_RUN_ID"], os.environ["GITHUB_RUN_ATTEMPT"]
    assert run.isdecimal() and attempt.isdecimal()
    cli, request, request_hash = request_arguments(root)
    names = (
        "launch-original-cube-sections.py", "produce-original-cube-section-fractions.py",
        "produce-original-map-section-fractions.py", "section_quotient_algebra.py",
        "read-original-shadow-pass-receipts.py", "original_shadow_receipt_tools.py",
        "produce-original-shadow-local-input.py", "original_good_prime_germ_tools.py",
        "check-r873-original-cm-petersson-degree.py", "original_low_weight_cm_tools.py",
        "produce-r917-original-global-rr-q-lattice.py", "original_pari_m2_basis.py",
        "original_shadow_coordinate_tools.py")
    files = [TOPIC/"scripts"/name for name in names]+[
        REQUEST, WORKFLOW, Path("README.md"), TOPIC/"README.md"]
    assert not git(root, "status", "--porcelain", "--", *map(str, files))
    hashes = {str(p):hashlib.sha256((root/p).read_bytes()).hexdigest() for p in files}
    readmes = {"root":git(root, "rev-parse", "HEAD:README.md"),
               "topic":git(root, "rev-parse", "HEAD:"+str(TOPIC/"README.md"))}
    manifest = dict(source=source, run_id=run, run_attempt=attempt, image=IMAGE,
                    parameters=request, request_sha256=request_hash,
                    source_file_sha256=hashes, readme_blobs=readmes,
                    mathematical_scope="same original RF and three Ri with complete 6941/4287 cube identities",
                    token_location="host public PASS reader only", source_mount="read-only",
                    Sage_network_mode="none", recomputable_data_file_written=False)
    progress("pinned original PASS request and source checked", **manifest)
    progress("host manifest digest", sha256=digest(manifest))
    host_env = os.environ.copy()
    host_env["PYTHONDONTWRITEBYTECODE"] = "1"
    clean_env = {key:value for key, value in host_env.items()
                 if key not in ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN")}
    container = "rank2-cube-sections-"+run+"-"+attempt
    values = {
        "GITHUB_ACTIONS":"true", "GITHUB_REPOSITORY":REPOSITORY,
        "RANK2_SOURCE_SHA":source, "RANK2_RUN_ID":run,
        "RANK2_RUN_ATTEMPT":attempt, "RANK2_IMAGE":IMAGE,
        "RANK2_ROOT_README_SHA":readmes["root"],
        "RANK2_TOPIC_README_SHA":readmes["topic"],
        "PYTHONDONTWRITEBYTECODE":"1", "PYTHONUNBUFFERED":"1", "OMP_NUM_THREADS":"4"}
    command = ["docker", "run", "--rm", "--init", "--network", "none",
               "--name", container, "-i"]
    for key, value in values.items():
        command += ["-e", key+"="+value]
    command += ["-v", str(root)+":/work:ro", "-w", "/work",
                "--entrypoint", "/usr/bin/sage", IMAGE, "-python",
                str(TOPIC/"scripts/produce-original-cube-section-fractions.py"), *cli]
    reader, sage, success = None, None, False
    started = time.monotonic()

    def interrupted(signum, frame):
        raise InterruptedError("Public host pipeline interrupted by signal "+str(signum))

    old = {s:signal.signal(s, interrupted) for s in (signal.SIGTERM, signal.SIGINT)}
    try:
        reader = subprocess.Popen([sys.executable, str(HERE/"read-original-shadow-pass-receipts.py"), *cli],
                                  cwd=root, env=host_env, stdout=subprocess.PIPE)
        sage = subprocess.Popen(command, cwd=root, env=clean_env, stdin=reader.stdout)
        reader.stdout.close()
        assert reader.wait(timeout=600) == 0, "Both true original PASS receipts are required."
        remaining = 21000-(time.monotonic()-started)
        assert remaining > 0
        assert sage.wait(timeout=remaining) == 0, "The offline original complete cube reader failed."
        success = True
        progress("both original authentication and complete original cube reader succeeded",
                 source=source, run_id=run, elapsed_seconds=time.monotonic()-started)
    finally:
        if not success:
            progress("pipeline incomplete; no mathematical PASS is asserted", source=source, run_id=run)
            for child in (reader, sage):
                if child is not None and child.poll() is None:
                    child.terminate()
            subprocess.run(["docker", "rm", "-f", container], env=clean_env,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=30, check=False)
            for child in (reader, sage):
                if child is not None:
                    try:
                        child.wait(timeout=15)
                    except subprocess.TimeoutExpired:
                        child.kill()
                        child.wait(timeout=15)
        for sig, handler in old.items():
            signal.signal(sig, handler)


if __name__ == "__main__":
    main()
