#!/usr/bin/env python3
"""Rebuild the four numerical H2 fields leading to R262 from the public source.

Usage: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
    python r262_regenerate.py --scripts TOPIC/scripts --directory RUNNER_TEMP/r262
The output JSON identifies the new byte digests and compares each historical
field digest. Reapply the R262 certificate only if its byte identity matches.
Requires a fresh directory, numpy, scipy, and public GitHub blob access.
"""
import argparse
import base64
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import urllib.request

for variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                 "NUMEXPR_NUM_THREADS"):
    os.environ[variable] = "1"
import numpy as np

PREFIX_BLOB = "26ce0426c60ef868c53597a82252e0559c1cc21e"
PREFIX_SHA = "359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0"
FIELD_DIGESTS = [
    "b6425243454a6a019d06a729405b0ebdaa0dbbc68b73b7f62745b1587174be1c",
    "201de8909dc707c7d91749d812585233d49120c076468e9f2aebe97271114aed",
    "6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61",
    "5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8",
]


def read(path):
    return json.loads(path.read_text())


def write(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fetch_blob(oid, size, sha, target):
    url = "https://api.github.com/repos/Rogerhu12/math-research-public/git/blobs/" + oid
    headers = {"User-Agent": "R262-public-reproduction", "Accept": "application/vnd.github+json"}
    if os.environ.get("M12_RECOVERY_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["M12_RECOVERY_TOKEN"]
    for attempt in range(4):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=120) as response:
                payload = json.load(response)
            break
        except OSError:
            if attempt == 3:
                raise
            time.sleep(2 ** (attempt + 1))
    if payload["sha"] != oid or payload["encoding"] != "base64":
        raise ValueError("Git source mismatch for " + target.name)
    data = base64.b64decode(payload["content"])
    framed = b"blob " + str(len(data)).encode() + b"\0" + data
    if (len(data) != size or hashlib.sha1(framed).hexdigest() != oid
            or hashlib.sha256(data).hexdigest() != sha):
        raise ValueError("Source data mismatch for " + target.name)
    target.write_bytes(data)


def field_path(result):
    return Path(str(result) + ".field.npz")


def query_path(grid):
    return Path(str(grid) + ".queries.json")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scripts", type=Path, required=True)
    parser.add_argument("--directory", type=Path, required=True)
    args = parser.parse_args()
    scripts = args.scripts.resolve()
    work = args.directory.resolve()
    work.mkdir(parents=True, exist_ok=True)
    if any(work.iterdir()):
        raise ValueError("Use a fresh output directory")
    prefix = work / "m12-prefix-data.npz.gz"
    raw_dir = work / "raw-cache"
    raw_dir.mkdir()
    fetch_blob(PREFIX_BLOB, 3112330, PREFIX_SHA, prefix)
    manifest = scripts.parent / "notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json"
    endpoint = scripts / "6a65-m12-stream-tail-exact-endpoint.py"
    spec = importlib.util.spec_from_file_location("r262_endpoint", endpoint)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    files = read(manifest)["files"]
    if len(files) != 24:
        raise ValueError("The finite original source has 24 raw files")
    for row in files:
        name = Path(row["path"]).name
        key = name.split("-raw")[1].split(".f64")[0].replace("-part", "-")
        fetch_blob(module.BLOBS[key], row["bytes"], row["sha256"], raw_dir / name)

    safe_env = {k: v for k, v in os.environ.items()
                if k not in ("M12_RECOVERY_TOKEN", "GH_TOKEN", "GITHUB_TOKEN")}
    source_env = dict(safe_env)
    if "M12_RECOVERY_TOKEN" in os.environ:
        source_env["M12_RECOVERY_TOKEN"] = os.environ["M12_RECOVERY_TOKEN"]

    def run(name, *params):
        command = [sys.executable, str(scripts / name), *map(str, params)]
        print("stage", name, flush=True)
        subprocess.run(command, check=True, env=safe_env)

    common = ("--scripts", scripts, "--data", prefix)
    base = work / "h487-base"
    plan = json.loads(subprocess.check_output(
        [sys.executable, str(scripts / "6a65-m12-entire-half-two-hotspot-cold-run.py"),
         *map(str, common), "--directory", str(base), "--plan-only"],
        text=True, env=safe_env))
    expected = ["prepare-base-grid", "recover-original-local-knots",
                "retain-first-hotspot-source-knot-h-refinement",
                "second-hotspot-transitive-h-refinement",
                "exact-tail-queries-and-continuous-source"]
    if plan["stage_names"][:5] != expected:
        raise ValueError("Unexpected original h487 preparation graph")
    for label, command in zip(expected, plan["commands"][:5]):
        print("stage", label, flush=True)
        subprocess.run(command, check=True, env=source_env if label in
                       (expected[1], expected[4]) else safe_env)

    base_grid = base / "entire-half-grid.json"
    base_report = base / "entire-half-exact-tail-queries.json"
    base_cache = Path(str(base_report) + ".npz")
    grid_data = read(base_grid)
    mesh = grid_data["unit_mesh"]
    if len(mesh) != 488 or grid_data["order"] != 32:
        raise ValueError("The cold field requires the original 487 unique spans and M32")
    knots = np.asarray([0.] * 6 + mesh[1:-1] + [1.] * 6)
    modes = np.arange(-32, 33) * 3 + 1
    heights = np.arange(33) * 3
    zero = work / "zero-binding.json"
    np.savez_compressed(field_path(zero), coefficients=np.zeros((486, 98)),
                        unit_knots=knots, planar_modes=modes, vertical_modes=heights)
    write(zero, {"schema": "R262-real-zero-initial-field",
                 "field_sha256": digest(field_path(zero)), "grid_sha256": digest(base_grid)})
    stage_dirs = [work / name for name in ("h2-cold-cache-01", "h2-c2-02",
                  "h2-c2-m48-03", "h2-c2-m48-g12-04r1")]
    for directory in stage_dirs:
        directory.mkdir()
    c2_grid = stage_dirs[1] / "grid.json"
    m48_grid = stage_dirs[2] / "grid.json"
    g12_grid = stage_dirs[3] / "grid.json"
    run("2ecf-m12-local-c2-knot-enrichment.py", "--old-grid", base_grid,
        "--coarse-grid", base / "entire-half-base-grid.json",
        "--old-queries", query_path(base_grid), "--out", c2_grid)
    if len(read(c2_grid)["unit_knots"]) != 748:
        raise ValueError("The C2 enrichment must give 736 free radial columns")
    run("6a65-m12-frequency-only-grid-prepare.py", "--old-grid", c2_grid,
        "--order", "48", "--angular", "768", "--out", m48_grid)
    run("2ecf-m12-quadrature-refinement-prepare.py", *common, "--old-grid", m48_grid,
        "--gauss", "12", "--out", g12_grid)
    g12_report = stage_dirs[3] / "exact-tail-queries.json"
    run("2ecf-m12-extend-exact-tail-queries-local.py", "--scripts", scripts,
        "--manifest", manifest, "--raw-directory", raw_dir, "--old-report", base_report,
        "--old-cache", base_cache, "--old-queries", query_path(base_grid),
        "--queries", query_path(g12_grid), "--out", g12_report)
    stages = [(base_grid, base_report, "2ecf-m12-h2-cached-direct-lm.py"),
              (c2_grid, base_report, "2ecf-m12-h2-cached-direct-lm-v2.py"),
              (m48_grid, base_report, "2ecf-m12-h2-cached-direct-lm-v2.py"),
              (g12_grid, g12_report, "2ecf-m12-h2-inplace-cached-lm.py")]
    receipts = []
    initial, old_result, old_grid, old_bounds = field_path(zero), zero, base_grid, None
    for i, ((grid, queries, solver), stage_dir) in enumerate(zip(stages, stage_dirs)):
        extra = []
        if i:
            transfer = stage_dir / "warm-transfer.json"
            run("6a65-m12-exact-radial-angular-warm-transfer.py", "--scripts", scripts,
                "--old-grid", old_grid, "--old-field", field_path(old_result),
                "--old-result", old_result, "--old-correction-bounds", old_bounds,
                "--new-grid", grid, "--out", transfer)
            initial = field_path(transfer)
            extra = ["--transfer-receipt", transfer]
        result = stage_dir / "result.json"
        run(solver, *common, "--grid", grid, "--query-report", queries, "--query-cache",
            str(queries) + ".npz", "--initial-field", initial, "--initial-result", old_result,
            *extra, "--lambda-step", "1e-12" if i == 0 else "1e-13", "--steps", "1",
            "--hessian-step-cap", ".05", "--out", result)
        actual = digest(field_path(result))
        record = read(result)
        observed = record["independent_observer_after"]
        receipts.append({"stage": stage_dir.name, "field": str(field_path(result)),
                         "field_sha256": actual, "historical_sha256": FIELD_DIGESTS[i],
                         "historical_bytes_matched": actual == FIELD_DIGESTS[i],
                         "accepted_steps": record["accepted_steps_this_refinement"],
                         "independent_observer_after": observed})
        write(work / "regenerated-fields.json", receipts)
        if record["accepted_steps_this_refinement"] != 1:
            raise ArithmeticError("The four-step lineage needs an actual accepted step")
        if i < 3:
            old_bounds = stage_dir / "correction-bounds.json"
            run("6a65-m12-entire-half-continuous-correction-bounds.py", *common,
                "--grid", grid, "--field", field_path(result), "--result", result,
                "--out", old_bounds)
        old_grid, old_result = grid, result
    print(json.dumps(receipts[-1], indent=2), flush=True)


if __name__ == "__main__":
    main()
