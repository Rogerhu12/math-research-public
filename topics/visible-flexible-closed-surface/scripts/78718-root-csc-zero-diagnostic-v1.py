#!/usr/bin/env python3
"""Small actual-state collocation matrices before/after exact zero removal.

This is a resource/linear-algebra experiment, not a BVP solve, new candidate,
new tail request, or production selection. Coarse node subsets are deliberately
not claimed to satisfy the original residual gate. Each pair has the same real
matrix; its SuperLU ordering and floating solution can nevertheless change.
Only small identity and scalar diagnostic records are written.
"""
import os
for _thread_key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_thread_key] = "1"
import argparse
import gc
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np
import scipy.integrate._bvp as bvp
from scipy.sparse.linalg import splu

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
PINS = {
    "db6f-prefix-flat-geometry-source.py":
        "23299890cebc07c938910995058d8e2ee09fbf289d323a3cac65bc3afc117c6f",
    "db6f-prefix-direct-csc-foundation-v2.py":
        "8e2bb061ef1fee94672601132cedb8ca7565d4006a327474f039f501e5f516cf",
    "db6f-root-spectral-collocation-v2.py":
        "47e1128c8cabb7c77797ebea6534cf77d63964add54f78a2cab827d1f0101854",
}
PLAN_SHA = "232e9c3f3d748a4b9c83673d6627c576b53c80fbadcdff580da5b8c3bdd7cdf9"
CP_SHA = "4776c4c251c4bc6fdadda56aaed78f6fc02175483c5ad3a6fb3cf0359a49cd6a"
TAIL_SHA = "c253eedbf3a4711ad79740d655262a5991e803e38dab2b4a248c386db9efcb7d"
PORT_SHA = "500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def verify(row):
    now = identity(row["path"])
    require(all(now[key] == row[key] for key in ("path", "bytes", "sha256")),
            "Bound bytes changed: " + row["path"])


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def storage_bytes(matrix):
    return int(matrix.data.nbytes + matrix.indices.nbytes + matrix.indptr.nbytes)


def factor_diagnostic(matrix, rhs, label):
    start = time.monotonic()
    lu = splu(matrix, permc_spec="COLAMD")
    elapsed = time.monotonic() - start
    solution = lu.solve(rhs)
    residual = matrix @ solution - rhs
    matrix_norm = float(np.max(np.asarray(abs(matrix).sum(axis=1))))
    denominator = matrix_norm * float(np.max(abs(solution))) + float(np.max(abs(rhs)))
    left, upper = lu.L, lu.U
    result = {
        "label": label, "factor_seconds": elapsed,
        "matrix_stored_nnz": int(matrix.nnz),
        "matrix_nonzero_values": int(np.count_nonzero(matrix.data)),
        "matrix_storage_bytes": storage_bytes(matrix),
        "L_nnz": int(left.nnz), "U_nnz": int(upper.nnz),
        "exported_LU_storage_bytes": storage_bytes(left) + storage_bytes(upper),
        "permutation_storage_bytes": int(lu.perm_r.nbytes + lu.perm_c.nbytes),
        "backward_error_inf": float(np.max(abs(residual))) / denominator,
        "solution_inf": float(np.max(abs(solution))),
        "column_permutation_sha256": hashlib.sha256(lu.perm_c.tobytes()).hexdigest(),
        "row_permutation_sha256": hashlib.sha256(lu.perm_r.tobytes()).hexdigest(),
        "peak_RSS_not_inferred_from_exported_factors": True,
    }
    del left, upper, lu
    gc.collect()
    return result, solution


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--nodes", nargs="+", type=int, default=[65, 129])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), "Output must be new")
    require(all(8 <= x <= 257 for x in args.nodes), "Only small node subsets permitted")
    started = time.monotonic()
    resource.setrlimit(resource.RLIMIT_DATA, (1536 * 1024**2, 1536 * 1024**2))
    resource.setrlimit(resource.RLIMIT_FSIZE, (4999999, 4999999))
    plan_id = identity(args.plan)
    require(plan_id["sha256"] == PLAN_SHA, "Unexpected successful production plan")
    plan = json.loads(args.plan.read_text())
    require(plan["plan_ready"] and plan["complete_final_audit_replayed"],
            "No actually completed finite source route")
    cp_id, tail_id = plan["own_successful_checkpoint"], plan["own_final_audited_tail"]
    verify(cp_id)
    verify(tail_id)
    require(cp_id["sha256"] == CP_SHA and tail_id["sha256"] == TAIL_SHA,
            "Different source candidate")
    port = Path(plan["fixed_input_roles"]["linear_port"])
    port_id = identity(port)
    require(port_id["sha256"] == PORT_SHA, "Different fixed linear background")
    for name, sha in PINS.items():
        require(identity(HERE / name)["sha256"] == sha, "Changed fixed source " + name)
    loader = module("zero_diagnostic_geometry", HERE / "db6f-prefix-flat-geometry-source.py")
    foundation = module("zero_diagnostic_foundation", HERE / "db6f-prefix-direct-csc-foundation-v2.py")
    weights_source = module("zero_diagnostic_weights", HERE / "db6f-root-spectral-collocation-v2.py")
    selected = foundation.make_functions(bvp)
    cp_path = Path(cp_id["path"])
    small = json.loads(gzip.decompress(cp_path.read_bytes()))
    inputs = [plan_id, cp_id, tail_id, port_id]
    for item in small["pp_coefficient_chunks"]:
        row = identity(cp_path.parent / item["file"])
        require(row["bytes"] == item["bytes"] and row["sha256"] == item["sha256"],
                "Changed source coefficient chunk")
        inputs.append(row)
    rec, preliminary, _, sol = loader.source(cp_path, port, args.source_root)
    # The geometry loader intentionally uses its own safe angular default;
    # construct the same class at the actual original N512 for this diagnostic.
    obj = type(preliminary)(preliminary.cfg, preliminary.port, preliminary.q,
                            preliminary.M, 512, True, rec["warp_reference_q"])
    obj.bcweights = np.full(obj.M, 2e-11 / 1e-8)
    obj.initial(sol.p)
    flow = obj.flow(sol.p[0])
    n, k = obj.n, obj.M
    require(obj.fixed and n == 43 and k == 14 and flow.nt == 512,
            "Expected the actual fixed M14/N512 class")
    w = weights_source.power2_weights(k)
    tail = json.loads(gzip.decompress(Path(tail_id["path"]).read_bytes()))
    response = tail["response"]
    require(response["converged"] and tail["request"]["jacobian"],
            "Own final tail did not contain a converged derivative")
    TJ = np.asarray(response["heightJetJacobian"]).reshape(3*k + 2, k)[:k]
    native_s = np.asarray(rec["mesh"], dtype=float)
    endpoint = sol.sol(np.array([native_s[-1]]))[:, 0]
    height_difference = float(np.max(abs(
        obj.bridge.sigma * obj.q * endpoint[obj.iz:] -
        np.asarray(tail["request"]["height"]))))
    require(height_difference < 2e-14, "Own derivative is not at this saved endpoint")
    results = []
    for count in args.nodes:
        index = np.unique(np.linspace(0, len(native_s)-1, count, dtype=int))
        physical_s = native_s[index]
        t = obj.inverse_chart(physical_s, sol.p[0])
        y = sol.sol(physical_s)
        u = w[:, None] * y
        h = np.diff(t)
        require(len(t) == count and np.all(h > 0), "Invalid coarse diagnostic grid")

        def weighted_fun(xx, uu, pp):
            return w[:, None] * obj.fun(xx, uu / w[:, None], pp)

        _, umid, _, _ = bvp.collocation_fun(weighted_fun, u, sol.p, t, h)
        fy, fp = obj.fun_jac(t, y, sol.p)
        fymid, fpmid = obj.fun_jac(t[:-1] + .5*h, umid / w[:, None], sol.p)
        require(np.count_nonzero(fp) == 0 and np.count_nonzero(fpmid) == 0,
                "Unexpected nonzero fixed-metric parameter derivative")
        fy = w[:, None, None] * fy / w[None, :, None]
        fymid = w[:, None, None] * fymid / w[None, :, None]
        fp = w[:, None, None] * fp
        fpmid = w[:, None, None] * fpmid
        aa, bb, pp = obj.bc_jac(y[:, 0], y[:, -1], sol.p)
        # Same TailMixin derivative formula, using the already frozen own DN.
        # This does not call a tail backend or claim a new tail response.
        end_jac, _ = flow.fun_jac(np.array([flow.end]),
                                  y[:, -1].astype(np.longdouble)[:, None], sol.p)
        terminal = obj.q * end_jac[obj.iz:, :, 0]
        terminal[:, obj.iz:] -= obj.bridge.sigma * obj.q * TJ / math.sqrt(obj.port["cut"]["E"])
        bb[n:] = terminal / obj.bcweights[:, None]
        aa = aa / w[None, :]
        bb = bb / w[None, :]
        matrix = selected.construct_global_jac(
            n, count, k, h, fy, fymid, fp, fpmid, aa, bb, pp)
        require(np.all(np.isfinite(matrix.data)), "Nonfinite actual diagnostic Jacobian")
        before_nnz = int(matrix.nnz)
        nonzero_count = int(np.count_nonzero(matrix.data))
        compact = matrix.copy()
        compact.eliminate_zeros()
        require(compact.nnz == nonzero_count and (matrix - compact).nnz == 0,
                "Exact zero removal altered a nonzero entry")
        require(compact.has_canonical_format, "Zero removal lost canonical structure")
        rhs = np.sin(np.arange(matrix.shape[0], dtype=float) + 1.)
        original, z0 = factor_diagnostic(matrix, rhs, "original_explicit_zeros")
        changed, z1 = factor_diagnostic(compact, rhs, "exact_zeros_removed")
        comparison = {
            "nodes": count, "state_components": n, "parameters": k,
            "unknowns": int(matrix.shape[0]), "removed_exact_zeros": before_nnz - nonzero_count,
            "exact_same_sparse_difference": True,
            "parameter_collocation_block_nonzero_count": 0,
            "original": original, "compacted": changed,
            "solution_difference_relative_inf":
                float(np.max(abs(z1-z0))) / max(float(np.max(abs(z0))), 1.),
            "LU_nnz_ratio_after_before":
                (changed["L_nnz"] + changed["U_nnz"]) / (original["L_nnz"] + original["U_nnz"]),
            "coarse_subset_is_not_a_new_accepted_solution": True,
        }
        results.append(comparison)
        print(json.dumps({"nodes": count,
                          "removed_exact_zeros": comparison["removed_exact_zeros"],
                          "LU_nnz_ratio_after_before": comparison["LU_nnz_ratio_after_before"],
                          "status": "SMALL_LINEAR_ALGEBRA_DIAGNOSTIC_COMPLETED"}), flush=True)
        del matrix, compact, z0, z1, fy, fymid, fp, fpmid
        gc.collect()
    sources = [identity(__file__)]
    for loaded in list(sys.modules.values()):
        filename = getattr(loaded, "__file__", None)
        if filename:
            filename = Path(filename).resolve()
            if filename.suffix == ".py" and (
                filename.is_relative_to(TOPIC) or filename.is_relative_to(args.source_root)):
                sources.append(identity(filename))
    sources.append(identity(bvp.__file__))
    sources = list({row["path"]: row for row in sources}.values())
    for row in [*sources, *inputs]:
        verify(row)
    output = {
        "schema": "78718-actual-state-csc-zero-diagnostic-v1",
        "status": "COMPLETED_SMALL_MATRIX_DIAGNOSTIC",
        "scope": __doc__, "sources": sources, "inputs": inputs,
        "frozen_tail_height_max_difference": height_difference,
        "source_angular": 512, "spectral_weights": "original_W14_power2",
        "experiments": results, "BVP_calls": 0, "tail_calls": 0,
        "production_engine_changed": False, "full_mesh_memory_claimed": False,
        "seconds": time.monotonic() - started,
    }
    args.out.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "output": identity(args.out),
                      "BVP_calls": 0, "tail_calls": 0}), flush=True)


if __name__ == "__main__":
    main()
