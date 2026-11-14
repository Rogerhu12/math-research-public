#!/usr/bin/env python3
"""Necessary floating tests of the full boundary-row QR against independent LU."""
from __future__ import annotations
import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import scipy
import scipy.integrate._bvp as bvp
from scipy.interpolate import PPoly
from scipy.sparse.linalg import splu
from flint import ctx

from fourfold_codazzi_block_qr_collocation import FullBoundaryQR
from fourfold_codazzi_block_qr_checkpointed import CheckpointBoundaryQR,make_prepare_sys
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_compact_metric_fast_jacobian import FastCompactNormalized
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_phase_symmetric_geometry import load_exact_object


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def synthetic(storage):
    rng = np.random.default_rng(394810)
    n, nodes, left_count = 7, 31, 4
    left, right = np.zeros((n+1, n)), np.zeros((n+1, n))
    left[:left_count] = rng.normal(size=(left_count, n))
    right[left_count:] = rng.normal(size=(n+1-left_count, n))
    parameter = rng.normal(size=(n+1, 1))
    full = np.zeros((n*nodes+1, n*nodes+1))
    blocks = []
    for i in range(nodes-1):
        h = 1/(nodes-1)
        a = np.diag(np.linspace(-55, 55, n)) + .1*rng.normal(size=(n, n))
        l, r, p = -np.eye(n)-h*a/2, np.eye(n)-h*a/2, -h*rng.normal(size=n)
        blocks.append((l, r, p))
        full[i*n:(i+1)*n, i*n:(i+1)*n] = l
        full[i*n:(i+1)*n, (i+1)*n:(i+2)*n] = r
        full[i*n:(i+1)*n, -1] = p
    full[n*(nodes-1):, :n] = left
    full[n*(nodes-1):, n*(nodes-1):n*nodes] = right
    full[n*(nodes-1):, -1] = parameter[:, 0]
    history = []
    factor = CheckpointBoundaryQR(n, nodes, left, right, parameter,
                                  lambda begin,end: iter(blocks[begin:end]), history, span=5 if storage=="memory" else 8)
    tests = []
    for i in range(2):
        known = rng.normal(size=full.shape[0])
        rhs = full@known
        qr_answer = factor.solve(rhs)
        lu_answer = np.linalg.solve(full, rhs)
        tests.append(dict(full_relative_residual=float(np.linalg.norm(full@qr_answer-rhs)/np.linalg.norm(rhs)),
            relative_difference_from_dense_LU=float(np.linalg.norm(qr_answer-lu_answer)/np.linalg.norm(lu_answer)),
            relative_difference_from_known_answer=float(np.linalg.norm(qr_answer-known)/np.linalg.norm(known))))
    return dict(storage=storage, dimension=int(full.shape[0]), matrix_condition_2=float(np.linalg.cond(full)),
                factor_history=history, tests=tests)


def actual(guess, obj):
    saved = load_candidate(guess)
    meta = json.loads(str(saved["metadata"]))
    previous = int(meta["modes"])
    geometry, _ = load_exact_object(obj, 512)
    body, graft = RotationalBodyTarget(geometry), RotationalGraftTarget(geometry, obj)
    modes, angles = 4, 64
    system = FastCompactNormalized(geometry, modes, angles, body, graft)
    system.alpha = float(meta["amplitude"])
    n = 2*modes+1
    x = np.unique(np.r_[saved["radial_nodes"][::70], saved["radial_nodes"][-1]])
    values = PPoly(saved["piece_coefficients"], saved["radial_nodes"])(x).T
    y = np.vstack((values[:modes], values[previous:previous+modes+1]))
    p = np.array([float(meta["nu"])])
    qstar = 1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)

    def bc(left, right, parameter):
        return np.r_[left[:modes], right[modes], left[modes+1]+1,
                     right[:modes]+qstar*right[modes+1:]]

    def bc_jac(left, right, parameter):
        jl, jr, jp = np.zeros((n+1, n)), np.zeros((n+1, n)), np.zeros((n+1, 1))
        jl[np.arange(modes), np.arange(modes)] = 1
        jr[modes, modes] = 1
        jl[modes+1, modes+1] = 1
        jr[np.arange(modes+2, n+1), np.arange(modes)] = 1
        jr[np.arange(modes+2, n+1), np.arange(modes+1, n)] = qstar
        return jl, jr, jp

    old_col, old_jac = bvp.prepare_sys(n, len(x), 1, system.evaluate, bc,
                                      system.jacobian, bc_jac, x, np.diff(x))
    col, ym, f, fm = old_col(y, p)
    boundary = bc(y[:, 0], y[:, -1], p)
    original = old_jac(y, p, ym, f, fm, boundary)
    original_lu = splu(original)
    history = []
    prepare = make_prepare_sys(np.r_[np.arange(1, modes+1), np.arange(modes+1)],
        system=system, band=0, drop=0., chunk=3, history=history,span=6)
    new_col, new_jac = prepare(n, len(x), 1, system.evaluate, bc, system.jacobian,
                              bc_jac, x, np.diff(x))
    factor = new_jac(y, p, ym, f, fm, boundary)
    rng = np.random.default_rng(28733)
    tests = []
    for rhs in (np.r_[col.ravel(order="F"), boundary], rng.normal(size=original.shape[0])):
        answer = factor.solve(rhs)
        reference = original_lu.solve(rhs)
        probe = rng.normal(size=original.shape[0])
        tests.append(dict(
            independent_sparse_LU_residual=float(np.linalg.norm(original@reference-rhs)/np.linalg.norm(rhs)),
            full_QR_residual_against_original_scipy_Jacobian=float(np.linalg.norm(original@answer-rhs)/np.linalg.norm(rhs)),
            relative_QR_difference_from_independent_LU=float(np.linalg.norm(answer-reference)/np.linalg.norm(reference)),
            full_FFT_action_difference=float(np.linalg.norm(factor.operator@probe-original@probe)/np.linalg.norm(original@probe))))
    return dict(original_complete_candidate_sha256=sha(guess), object_sha256=sha(obj),
        projected_test_modes=modes, projected_test_angles=angles, radial_nodes=len(x),
        projection_is_only_a_linear_algorithm_test=True, input_finite_BVP_success_not_assumed=True,
        scipy_version=scipy.__version__, scipy_bvp_sha256=sha(bvp.__file__),
        factor_history=history, tests=tests)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--guess", type=Path, default=Path("notes/2026-11-13-R133-compact-metric-m128-alpha070-v9-candidate.json"))
    ap.add_argument("--object", type=Path, default=Path("data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve the original audit run")
    tick = time.monotonic()
    ctx.prec = 192
    report = dict(kind="floating_complete_checkpointed_block_QR_algorithm_audit",
        synthetic_memory=synthetic("memory"), synthetic_file=synthetic("file"),
        actual_finite=actual(args.guess, args.object))
    tests = report["synthetic_memory"]["tests"]+report["synthetic_file"]["tests"]
    passed = all(max(row.values()) < 5e-8 for row in tests)
    passed = passed and all(max(row.values()) < 5e-8 for row in report["actual_finite"]["tests"])
    report.update(complete=True, all_original_linear_backward_gates_passed=bool(passed),
        continuous_PDE_certificate=False, full_M128_BVP_solved=False,
        source_sha256=sha(__file__),
        complete_QR_source_sha256=sha(Path(__file__).with_name("fourfold_codazzi_block_qr_collocation.py")),
        checkpointed_QR_source_sha256=sha(Path(__file__).with_name("fourfold_codazzi_block_qr_checkpointed.py")),
        wall_seconds=time.monotonic()-tick)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(dict(complete=True, all_original_linear_backward_gates_passed=passed,
               wall_seconds=report["wall_seconds"]), flush=True)
    if not passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
