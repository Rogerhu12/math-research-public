#!/usr/bin/env python3
"""Prepare the inactive complete native-row production binding on public Actions.

The full original source code is loaded but no producer main or matrix is run.
The current heavy workflow and its request remain exactly pinned and inactive
new paths are checked explicitly.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public Actions repository.")

import ast
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOP = "topics/rank2-sha-infinitely-many-p/"
PINNED = {
    "original_pair_reset_row_reduction.py": "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
    "original_native_polynomial_rows.pyx": "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922",
    "original_native_pair_reset.py": "a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28",
    "produce-original-native-row-artinian-shadow.py": "4568461d1d77e5f72aeb26528193a48f4442aa575cb52086c21313c69ae8ba10",
    "launch-original-native-row-artinian-shadow.py": "740169518ace27fa8b567752584930752521f2780ed78a7471951d89338913c2",
}
REQUEST_SHA256 = "25c209ac9daf5a11f1b1cec7b87b86f9d1116d3a0923bebf174f14905471e140"
HEAVY_WORKFLOW_SHA256 = "24be40c3fc98babefcbaa53b03b16d7904e93da5500b8018c14d2e0645677a06"


def main():
    started = time.monotonic()
    source = subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
    assert source == os.environ["GITHUB_SHA"]
    hashes = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
              for name in PINNED}
    assert hashes == PINNED
    for name in PINNED:
        if name.endswith(".py"):
            ast.parse((HERE/name).read_text(), filename=str(HERE/name))
    request_path = ROOT/TOP/"ci/original-native-row-artinian-shadow-request.json"
    request_raw = request_path.read_bytes()
    assert hashlib.sha256(request_raw).hexdigest() == REQUEST_SHA256
    request = json.loads(request_raw)
    previous_request = json.loads(
        (ROOT/TOP/"ci/original-projector-artinian-shadow-request.json").read_bytes())
    expected = dict(previous_request,
                    schema="rank2-original-triangular-artinian-request/v11",
                    linear_algebra="r1035-complete-native-rows-projector-original-linear-fibers")
    assert request == expected
    workflow = (ROOT/".github/workflows/rank2-sha-original-triangular-artinian-shadow.yml").read_bytes()
    assert hashlib.sha256(workflow).hexdigest() == HEAVY_WORKFLOW_SHA256
    for name in ("original-native-row-artinian-shadow-request.json",
                 "launch-original-native-row-artinian-shadow.py",
                 "produce-original-native-row-artinian-shadow.py"):
        assert name.encode() not in workflow
    clean = {key: value for key, value in os.environ.items()
             if key not in {"GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN",
                            "RANK2_ACTIONS_READ_TOKEN", "RANK2_GITHUB_PAT"}}
    pulled = subprocess.run(["docker", "pull", IMAGE], env=clean,
                            capture_output=True, timeout=240)
    if pulled.returncode:
        print("The pinned Sage image pull failed.", file=sys.stderr)
        raise SystemExit(pulled.returncode)
    code = (
        "import importlib.util,json,sys\n"
        "sys.path.insert(0,'/work/" + TOP + "scripts')\n"
        "import original_ys_closed_point_tools as closed\n"
        "previous=closed.decompose_complete_primary_block\n"
        "path='/work/" + TOP + "scripts/produce-original-native-row-artinian-shadow.py'\n"
        "spec=importlib.util.spec_from_file_location('r1035_prepare_only',path)\n"
        "module=importlib.util.module_from_spec(spec)\n"
        "sys.modules[spec.name]=module\n"
        "spec.loader.exec_module(module)\n"
        "entry,state,metadata=module.prepare_source_bindings()\n"
        "assert entry.ENTRY is None\n"
        "assert state['row_records']==[] and not state['bound']\n"
        "assert not state['source_dependencies_extended']\n"
        "assert closed.decompose_complete_primary_block is previous\n"
        "assert metadata['mathematical_instances_executed_by_preparation']==0\n"
        "from sage.version import version\n"
        "metadata['sage_version']=version\n"
        "metadata['original_primary_constructor_unchanged_by_preparation']=True\n"
        "print('R1035_PRODUCTION_PREPARATION '+json.dumps(metadata,sort_keys=True))\n")
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
        print("Native production preparation failed; no original matrix was run.",
              file=sys.stderr)
        raise SystemExit(result.returncode)
    lines = [line for line in result.stdout.decode("utf-8").splitlines()
             if line.startswith("R1035_PRODUCTION_PREPARATION ")]
    assert len(lines) == 1
    metadata = json.loads(lines[0][len("R1035_PRODUCTION_PREPARATION "):])
    assert metadata["native_preparation"]["all_pinned_source_replacements_matched"]
    assert metadata["pinned_v10_main_invoked_by_preparation"] is False
    assert metadata["mathematical_instances_executed_by_preparation"] == 0
    print(json.dumps({
        "kind": "original-R1035-native-production-public-preparation-receipt",
        "status": "PREPARED_INACTIVE_NO_MATHEMATICAL_INSTANCE",
        "source": source, "run_id": os.environ["GITHUB_RUN_ID"],
        "image": IMAGE, "source_file_sha256": hashes,
        "inactive_request_sha256": REQUEST_SHA256,
        "unchanged_heavy_workflow_sha256": HEAVY_WORKFLOW_SHA256,
        "all_original_request_parameters_and_both_char0_pins_unchanged": True,
        "compile_stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
        "compile_stdout_bytes": len(result.stdout),
        "compile_stderr_sha256": hashlib.sha256(result.stderr).hexdigest(),
        "compile_stderr_bytes": len(result.stderr),
        "metadata": metadata, "mathematical_instances_executed": 0,
        "heavy_workflow_or_current_request_changed": False,
        "new_heavy_workflow_queued": False,
        "source_mount_read_only": True, "compiler_network": "none",
        "temporary_compiler_container_removed": True,
        "data_artifacts_persisted": False,
        "elapsed_seconds": time.monotonic()-started,
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
