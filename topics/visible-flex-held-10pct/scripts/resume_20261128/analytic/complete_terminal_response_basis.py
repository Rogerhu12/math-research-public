#!/usr/bin/env python3
"""Cold-read the actual full M24 matrix and compute its terminal response columns.

This is a numerical basis for the explicitly supplied frozen matrix.  It does
not import a physical Flow, assemble a Jacobian, query the tail, solve a BVP,
or certify an inverse.  Complete response vectors stay outside the repository.
Every completed column has its original full-matrix residual and durable hash.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import resource
import shutil
import sys
import time
import traceback

import numpy as np
from scipy.sparse import load_npz

SOURCE = Path(__file__).resolve()
REPO = SOURCE.parents[5]
EVIDENCE = (REPO / "topics/visible-flex-held-10pct/notes/"
            "2026-11-28-design-complete-csr-assembly-qr-bitwise.json")
EVIDENCE_BLOB = "fa77bf9a0ebc5efddb5f971937f2719b9bf9856e"
FACTOR = SOURCE.parents[1] / "block_qr_v2.py"


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def save(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def available_memory():
    with Path("/proc/meminfo").open() as stream:
        for line in stream:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise RuntimeError("The requested actual prelaunch MemAvailable observation is unavailable")


def finite_number(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("Nonfinite numerical response diagnostic")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--minimum-available-mib", type=float, default=1024.)
    parser.add_argument("--disk-reserve-mib", type=float, default=64.)
    args = parser.parse_args()
    if (not math.isfinite(args.minimum_available_mib) or args.minimum_available_mib <= 0
            or not math.isfinite(args.disk_reserve_mib) or args.disk_reserve_mib < 0):
        raise ValueError("Resource estimates must be explicit finite positive/nonnegative values")
    matrix_path, snapshot, run_path, out = (
        x.resolve() for x in (args.matrix, args.snapshot, args.source_run, args.outdir))
    if out == REPO or REPO in out.parents:
        raise ValueError("Complete numerical responses must remain outside the repository")
    evidence_bytes = EVIDENCE.read_bytes()
    if git_blob_sha(evidence_bytes) != EVIDENCE_BLOB:
        raise ValueError("The literal published complete-M24 evidence changed")
    comparison = json.loads(evidence_bytes)["comparison"]
    if comparison["status"] != "actual_complete_CSR_and_QR_bitwise_check_passed":
        raise ValueError("Expected the actual complete CSR and QR evidence")
    for key in ("original_vs_direct", "installed_prepare_sys_vs_direct",
                "prior_saved_matrix_vs_direct"):
        if not comparison[key] or not all(v is True for v in comparison[key].values()):
            raise ValueError("The complete matrix comparison is not the published one")
    expected = {
        matrix_path: comparison["actual_direct_matrix_sha256"],
        snapshot: comparison["snapshot_sha256"],
        run_path: comparison["source_run_sha256"],
    }
    for path, digest in expected.items():
        if sha(path) != digest:
            raise ValueError("An actual cold matrix/snapshot/source identity differs: " + str(path))
    factor_sources = [v for k, v in comparison["source_hashes"].items()
                      if Path(k).name == FACTOR.name]
    if len(factor_sources) != 1 or sha(FACTOR) != factor_sources[0]:
        raise ValueError("The reviewed complete BlockQR implementation changed")
    n, nodes, modes = comparison["n"], comparison["m"], comparison["k"]
    dimension = n * nodes + modes
    if (n, nodes, modes, comparison["shape"]) != (73, 879, 24, [64191, 64191]):
        raise ValueError("This narrow entry is for the actual published M24 matrix only")
    source_run = json.loads(run_path.read_text())
    gauge = finite_number(source_run["gauge_q"])
    if gauge <= 0 or source_run["modes"] != modes:
        raise ValueError("The original source gauge or mode count differs")
    # This exact original R53 source has the inward ShortBridge orientation.
    # It is not a parameter-dependent physical support amplitude.
    sigma = -1
    with np.load(snapshot, allow_pickle=False) as saved:
        x, y, p = saved["x"], saved["y"], saved["p"]
        if (x.shape != (nodes,) or y.shape != (n, nodes) or p.shape != (modes,)
                or not np.all(np.isfinite(x)) or not np.all(np.diff(x) > 0)
                or not np.all(np.isfinite(y)) or not np.all(np.isfinite(p))):
            raise ValueError("The actual Jacobian input does not retain all original unknowns")
    del x, y, p
    identity = dict(
        evidence_path=str(EVIDENCE), evidence_git_blob_sha1=EVIDENCE_BLOB,
        matrix=dict(path=str(matrix_path), sha256=expected[matrix_path]),
        matrix_input=dict(path=str(snapshot), sha256=expected[snapshot]),
        origin_design_run=dict(path=str(run_path), sha256=expected[run_path]),
        factor_source=dict(path=str(FACTOR), sha256=factor_sources[0]),
        n=n, nodes=nodes, parameters=modes, dimension=dimension,
        gauge_q=gauge, sigma=sigma, height_columns=[n*(nodes-1)+2*modes+1, n*nodes],
        terminal_rows=[dimension-modes, dimension],
        matrix_role="Actual saved c9c4906f snapshot; frozen-chord unless same-point identity is separately established",
    )
    if args.resume:
        state = json.loads((out / "response-basis.json").read_text())
        if state.get("identity") != identity or state.get("entry_sha256") != sha(SOURCE):
            raise ValueError("Resume requires the same complete matrix, coordinates and entry bytes")
    else:
        out.mkdir(parents=True, exist_ok=False)
        state = dict(
            scope=__doc__, identity=identity, entry_sha256=sha(SOURCE),
            status="no_new_numerical_column_yet", columns=[], invocations=[],
            complete_jacobian_assembled=False, physical_flow_imported=False,
            tail_requested=False, BVP_solved=False, accepted_physical_field=False,
            derivative_or_inverse_interval_certified=False,
        )
    report = out / "response-basis.json"
    invocation = dict(start_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                      resumed=args.resume, new_columns=0, reused_columns=0)
    state["invocations"].append(invocation)
    save(report, state)
    start = time.monotonic()
    factor = matrix = None
    try:
        recorded = {}
        for row in state["columns"]:
            j = row["column"]
            if not isinstance(j, int) or not 0 <= j < modes or j in recorded:
                raise ValueError("Duplicate or invalid previously journaled column")
            path = out / ("response-%03d.npy" % j)
            if sha(path) != row["response_sha256"]:
                raise ValueError("A completed original response changed")
            vector = np.load(path, allow_pickle=False)
            if (vector.shape != (dimension,) or vector.dtype != np.dtype("float64")
                    or not np.all(np.isfinite(vector))):
                raise ValueError("A saved complete response lost an original coordinate")
            h = sigma * gauge * vector[identity["height_columns"][0]:n*nodes]
            if not np.array_equal(h, np.asarray(row["physical_height_response"])):
                raise ValueError("A saved endpoint response differs from its full vector")
            del vector
            recorded[j] = row
        invocation["reused_columns"] = len(recorded)
        pending = [j for j in range(modes) if j not in recorded]
        memory = available_memory()
        disk = shutil.disk_usage(out).free
        response_bytes = len(pending) * (dimension * 8 + 256)
        required_disk = response_bytes + int(args.disk_reserve_mib * 1024**2)
        invocation["prelaunch"] = dict(
            available_memory_bytes=memory, disk_free_bytes=disk,
            minimum_available_bytes=int(args.minimum_available_mib * 1024**2),
            remaining_response_file_budget_bytes=response_bytes,
            disk_reserve_bytes=int(args.disk_reserve_mib * 1024**2),
            estimated_gate_is_not_a_memory_guarantee=True,
            automatic_wait_or_spawn_used=False,
        )
        save(report, state)
        if pending and (memory < int(args.minimum_available_mib * 1024**2)
                        or disk < required_disk):
            raise MemoryError("The explicit one-shot matrix-only resource gate did not pass")
        if pending:
            for j in pending:
                pending_path = out / ("response-%03d.npy" % j)
                if pending_path.with_suffix(".npy.tmp").exists() and not pending_path.exists():
                    raise ValueError("An interrupted incomplete vector write needs explicit recovery before refactorization")
            matrix = load_npz(matrix_path)
            if (matrix.format != "csr" or matrix.shape != (dimension, dimension)
                    or matrix.nnz != comparison["stored_entries"]
                    or not np.all(np.isfinite(matrix.data))):
                raise ValueError("The literal full saved CSR differs")
            module_spec = importlib.util.spec_from_file_location("_original_complete_response_qr", FACTOR)
            module = importlib.util.module_from_spec(module_spec)
            sys.modules[module_spec.name] = module
            module_spec.loader.exec_module(module)
            # The original factor may eliminate stored zero entries in memory;
            # every original mathematical matrix entry and parameter stays.
            factor = module.BlockQR(matrix, n, nodes, modes)
            state["status"] = "complete_matrix_columns_running"
            save(report, state)
        for j in pending:
            path = out / ("response-%03d.npy" % j)
            rhs = np.zeros(dimension)
            rhs[dimension-modes+j] = 1.
            if path.exists():
                # A completed file can outlive a killed pre-journal process.
                # It is treated only as a supplied approximate vector and is
                # audited against the same actual full matrix before adoption.
                vector = np.load(path, allow_pickle=False)
                origin = "existing_unjournaled_full_vector_rechecked"
            else:
                vector = factor.solve(rhs)
                origin = "original_complete_BlockQR_solve"
            if (vector.shape != (dimension,) or vector.dtype != np.dtype("float64")
                    or not np.all(np.isfinite(vector))):
                raise ValueError("The numerical response is not a finite complete vector")
            residual = matrix @ vector - rhs
            h = sigma * gauge * vector[identity["height_columns"][0]:n*nodes]
            row = dict(
                column=j, generation=origin,
                original_full_matrix_residual_max=finite_number(np.max(np.abs(residual))),
                original_full_matrix_residual_l2=finite_number(np.linalg.norm(residual)),
                numerical_values_are_not_interval_bounds=True,
                physical_height_response=h.tolist(),
                original_delta_parameter_response=finite_number(vector[n*nodes]),
                maximum_absolute_response=finite_number(np.max(np.abs(vector))),
            )
            if not path.exists():
                temporary = path.with_suffix(".npy.tmp")
                with temporary.open("xb") as stream:
                    np.save(stream, np.asarray(vector, dtype=np.float64), allow_pickle=False)
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary.replace(path)
            row["response_sha256"] = sha(path)
            row["response_bytes"] = path.stat().st_size
            state["columns"].append(row)
            state["columns"].sort(key=lambda value: value["column"])
            invocation["new_columns"] += 1
            invocation["elapsed_seconds"] = time.monotonic() - start
            invocation["maximum_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            state["factor_stats"] = dict(factor.stats)
            save(report, state)
            print(json.dumps(dict(event="complete_terminal_response_column", **row)), flush=True)
            del vector, residual, rhs, h
        del factor, matrix
        factor = matrix = None
        gc.collect()
        for path, digest in expected.items():
            if sha(path) != digest:
                raise ValueError("A bound original input changed during the response calculation")
        if sha(FACTOR) != factor_sources[0] or sha(SOURCE) != state["entry_sha256"]:
            raise ValueError("A bound complete solver or entry changed")
        state["status"] = "complete_matrix_response_basis_returned"
        state["complete_columns"] = modes
        state["small_S_constructed"] = False
        state["actual_DN_slope_Jacobian_consumed"] = False
        invocation["elapsed_seconds"] = time.monotonic() - start
        invocation["maximum_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        save(report, state)
        return 0
    except Exception as error:
        state["status"] = "response_basis_stopped_with_partial_columns_preserved"
        invocation.update(error=repr(error), traceback=traceback.format_exc(),
                          elapsed_seconds=time.monotonic()-start,
                          maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(report, state)
        raise


if __name__ == "__main__":
    sys.exit(main())
