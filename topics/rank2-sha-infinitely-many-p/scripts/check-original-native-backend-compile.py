#!/usr/bin/env python3
"""Compile the complete native-row adapter in the pinned public Sage image.

No mathematical matrix is constructed or reduced.  The existing original
geometric production job is neither started, retried, cancelled nor read.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public Actions repository.")

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOP = "topics/rank2-sha-infinitely-many-p/scripts/"
PINNED = {
    "original_pair_reset_row_reduction.py": "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
    "original_native_polynomial_rows.pyx": "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922",
    "original_native_pair_reset.py": "a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28",
}


def main():
    started = time.monotonic()
    source = subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
    assert source == os.environ["GITHUB_SHA"]
    hashes = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
              for name in PINNED}
    assert hashes == PINNED
    clean = {key: value for key, value in os.environ.items()
             if key not in {"GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN",
                            "RANK2_ACTIONS_READ_TOKEN", "RANK2_GITHUB_PAT"}}
    pulled = subprocess.run(["docker", "pull", IMAGE], env=clean,
                            capture_output=True, timeout=240)
    if pulled.returncode:
        print("The pinned Sage image pull failed.", file=sys.stderr)
        raise SystemExit(pulled.returncode)
    code = (
        "import json,sys\n"
        "sys.path.insert(0,'/work/" + TOP + "')\n"
        "from original_native_pair_reset import prepare_backend\n"
        "from sage.version import version\n"
        "record=prepare_backend()\n"
        "record['sage_version']=version\n"
        "print('R1035_NATIVE_COMPILE '+json.dumps(record,sort_keys=True))\n")
    command = [
        "docker", "run", "--rm", "--init", "--network", "none",
        "-e", "GITHUB_ACTIONS=true",
        "-e", "GITHUB_REPOSITORY=Rogerhu12/math-research-public",
        "-e", "PYTHONDONTWRITEBYTECODE=1",
        "-v", str(ROOT)+":/work:ro", "-w", "/work",
        "--entrypoint", "/usr/bin/sage", IMAGE, "-python", "-c", code]
    result = subprocess.run(command, env=clean, capture_output=True, timeout=600)
    if result.returncode:
        print(result.stderr.decode("utf-8", errors="replace")[-10000:], file=sys.stderr)
        print("Native compilation/preparation failed; no mathematical instance was run.",
              file=sys.stderr)
        raise SystemExit(result.returncode)
    lines = [line for line in result.stdout.decode("utf-8").splitlines()
             if line.startswith("R1035_NATIVE_COMPILE ")]
    assert len(lines) == 1
    metadata = json.loads(lines[0][len("R1035_NATIVE_COMPILE "):])
    assert metadata["all_pinned_source_replacements_matched"]
    assert metadata["mathematical_instance_executed_by_preparation"] is False
    print(json.dumps({
        "kind": "original-R975-native-backend-public-compile-receipt",
        "status": "COMPILED_AND_PREPARED_NO_MATHEMATICAL_INSTANCE",
        "source": source, "run_id": os.environ["GITHUB_RUN_ID"],
        "image": IMAGE, "source_file_sha256": hashes,
        "compile_stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
        "compile_stdout_bytes": len(result.stdout),
        "compile_stderr_sha256": hashlib.sha256(result.stderr).hexdigest(),
        "compile_stderr_bytes": len(result.stderr),
        "metadata": metadata,
        "mathematical_instances_executed": 0,
        "original_geometric_workflow_changed": False,
        "source_mount_read_only": True,
        "compiler_network": "none",
        "temporary_compiler_container_removed": True,
        "data_artifacts_persisted": False,
        "elapsed_seconds": time.monotonic()-started,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
