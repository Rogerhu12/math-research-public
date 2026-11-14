#!/usr/bin/env python3
"""Dense algebra and unsupported-input checks; no numerical BVP is run.

The one valid synthetic call intercepts the module's private solver reference,
checks its four transformed callbacks, and raises before any SciPy solve.
Every invalid-input case must reject before even that reference is called.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np


T = Path(__file__).resolve().parents[1]
P = "2026-11-09-db6f-"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def farray(rows):
    return np.asarray([[float(v) for v in row] for row in rows])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--module-sha", required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    path = T / "scripts/db6f-root-spectral-collocation-v2.py"
    if sha(path) != a.module_sha:
        raise ValueError("Frozen spectral module identity differs")
    out = a.out.resolve()
    if out.exists() or not out.is_relative_to(T / "notes"):
        raise ValueError("Use a new output in topic notes")
    spec = importlib.util.spec_from_file_location("tail_spectral_review_only", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    w = np.array([1., 2., 8., 32.])
    n, k, count = 4, 2, 3
    A = [[F((-1)**(i+j)*(i+2)*(j+1), 16) for j in range(n)] for i in range(n)]
    C = [[F(2*i-j+1, 8) for j in range(k)] for i in range(n)]
    La = [[F((i+1)*(j+2), 32) for j in range(n)] for i in range(n+k)]
    Lb = [[F(3*i-2*j+1, 16) for j in range(n)] for i in range(n+k)]
    Lp = [[F(2*i+3*j+1, 8) for j in range(k)] for i in range(n+k)]
    yf = [[F(2*i+j-3, 8) for j in range(count)] for i in range(n)]
    pf = [F(3, 8), F(-1, 4)]
    xf = [F(0), F(1, 4), F(1)]
    y, p, x = farray(yf), np.asarray([float(z) for z in pf]), np.asarray([float(z) for z in xf])
    Am, Cm, Lam, Lbm, Lpm = map(farray, (A, C, La, Lb, Lp))
    callbacks = {"fun": 0, "jac": 0, "bc": 0, "bc_jac": 0}

    def fun(xx, yy, pp):
        callbacks["fun"] += 1
        return Am @ yy + (Cm @ pp)[:, None] + np.arange(1, n+1)[:, None]*xx

    def jac(xx, yy, pp):
        callbacks["jac"] += 1
        return np.repeat(Am[:, :, None], len(xx), axis=2), np.repeat(Cm[:, :, None], len(xx), axis=2)

    def bc(ya, yb, pp):
        callbacks["bc"] += 1
        return Lam @ ya + Lbm @ yb + Lpm @ pp

    def bc_jac(ya, yb, pp):
        callbacks["bc_jac"] += 1
        return Lam.copy(), Lbm.copy(), Lpm.copy()

    class InterceptedBeforeNumericalSolver(Exception):
        pass

    intercepted = []

    def exact_equal(got, expected):
        if not np.array_equal(np.asarray(got), np.asarray(expected)):
            raise AssertionError("Synthetic dyadic callback identity failed")

    def intercept_solver(wfun, wbc, xx, uu, pp, **opts):
        intercepted.append(True)
        exact_equal(xx, x)
        exact_equal(uu, w[:, None]*y)
        exact_equal(pp, p)
        exact_equal(wfun(xx, uu, pp), farray([
            [F(int(w[i])) * (sum(A[i][l]*yf[l][j] for l in range(n))
                              + sum(C[i][l]*pf[l] for l in range(k))
                              + F(i+1)*xf[j]) for j in range(count)] for i in range(n)]))
        fy, fp = opts["fun_jac"](xx, uu, pp)
        fy_expected = np.empty((n, n, count)); fp_expected = np.empty((n, k, count))
        for i in range(n):
            for j in range(n):
                fy_expected[i, j, :] = float(F(int(w[i]))*A[i][j]/F(int(w[j])))
            for j in range(k):
                fp_expected[i, j, :] = float(F(int(w[i]))*C[i][j])
        exact_equal(fy, fy_expected); exact_equal(fp, fp_expected)
        expected_bc = [sum(La[i][j]*yf[j][0]+Lb[i][j]*yf[j][-1] for j in range(n))
                       + sum(Lp[i][j]*pf[j] for j in range(k)) for i in range(n+k)]
        exact_equal(wbc(uu[:, 0], uu[:, -1], pp), list(map(float, expected_bc)))
        aa, bb, ppj = opts["bc_jac"](uu[:, 0], uu[:, -1], pp)
        exact_equal(aa, farray([[La[i][j]/F(int(w[j])) for j in range(n)] for i in range(n+k)]))
        exact_equal(bb, farray([[Lb[i][j]/F(int(w[j])) for j in range(n)] for i in range(n+k)]))
        exact_equal(ppj, Lpm)
        if opts["tol"] != 2e-9 or opts["bc_tol"] != 1e-10 or opts["max_nodes"] != 37:
            raise AssertionError("Original numerical gates changed")
        raise InterceptedBeforeNumericalSolver("Synthetic callback probe only; no integration")

    original_solver = mod.scipy_solve_bvp
    mod.scipy_solve_bvp = intercept_solver
    try:
        solve, records = mod.make_solver(w)
        try:
            solve(fun, bc, x, y, p=p, fun_jac=jac, bc_jac=bc_jac,
                  tol=2e-9, bc_tol=1e-10, max_nodes=37)
        except InterceptedBeforeNumericalSolver:
            pass
        else:
            raise AssertionError("Synthetic interception did not stop")
        if len(intercepted) != 1 or len(records) != 1 or records[0]["status"] != "WEIGHTED_COLLOCATION_EXCEPTION":
            raise AssertionError("Exception ledger differs")
        if callbacks != {"fun": 1, "jac": 1, "bc": 1, "bc_jac": 1}:
            raise AssertionError("Unexpected synthetic callback count")
    finally:
        mod.scipy_solve_bvp = original_solver

    forbidden = {"solver": 0, "callback": 0}

    def forbidden_solver(*args, **kwargs):
        forbidden["solver"] += 1
        raise AssertionError("Invalid input reached the solver reference")

    def forbidden_callback(*args, **kwargs):
        forbidden["callback"] += 1
        raise AssertionError("Invalid input reached a numerical callback")

    def bad_test(label, weights=w, **changes):
        opts = dict(p=p.copy(), fun_jac=forbidden_callback, bc_jac=forbidden_callback)
        yy = changes.pop("y", y.copy()); xx = changes.pop("x", x.copy())
        opts.update(changes)
        r = []
        try:
            sol, r = mod.make_solver(weights)
            sol(forbidden_callback, forbidden_callback, xx, yy, **opts)
        except (ValueError, FloatingPointError, TypeError) as e:
            if r:
                raise AssertionError("Invalid input was recorded as a solver start")
            return {"case": label, "rejected": True, "exception_type": type(e).__name__, "reason": str(e)}
        raise AssertionError("Unsupported input was accepted")

    mod.scipy_solve_bvp = forbidden_solver
    try:
        cases = [
            bad_test("complex_weight_ndarray", weights=w.astype(complex)+1j),
            bad_test("object_complex_weight", weights=np.array([np.complex128(1+1j)]*4, dtype=object)),
            bad_test("complex_parameter_ndarray", p=p.astype(complex)+1j),
            bad_test("object_complex_parameter", p=np.array([np.complex128(1+1j)]*2, dtype=object)),
            bad_test("complex_grid_ndarray", x=x.astype(complex)+1j),
            bad_test("object_complex_grid", x=np.array([np.complex128(v+1j) for v in x], dtype=object)),
            bad_test("complex_initial_state", y=y.astype(complex)),
            bad_test("unsupported_S", S=np.eye(n)),
            bad_test("empty_parameter", p=np.array([])),
            bad_test("missing_analytic_jacobian", fun_jac=None),
            bad_test("nonfinite_grid", x=np.array([0., np.nan, 1.])),
            bad_test("nonincreasing_grid", x=np.array([0., 1., .5])),
        ]
    finally:
        mod.scipy_solve_bvp = original_solver
    if forbidden != {"solver": 0, "callback": 0}:
        raise AssertionError("Invalid-input gates called numerical code")
    rms_cases = 0
    for weight in map(lambda z: F(int(z)), w):
        for residual in (F(0), F(1, 7), F(-2, 3)):
            for rhs in (F(0), F(1, 11), F(-7, 3)):
                if weight*abs(residual)/(1+weight*abs(rhs)) < abs(residual)/(1+abs(rhs)):
                    raise AssertionError("Relative RMS direction failed")
                rms_cases += 1
    if sha(path) != a.module_sha:
        raise ValueError("Module changed during review")
    report = {
        "status": "PASS_DENSE_CALLBACK_IDENTITIES_AND_ZERO_SOLVER_REJECTIONS",
        "scope": "One synthetic dense dyadic callback interception, twelve invalid-input gates, and rational scalar inequalities. The real SciPy solver is never called. No candidate, root, DN, RK, flow, or BVP integration.",
        "script_sha256": sha(__file__), "module": str(path), "module_sha256": a.module_sha,
        "dense_fixture": {"state_components": n, "parameters": k, "nodes": count,
                          "nonzero_offdiagonal_f_y": True, "nonzero_both_end_jacobians": True,
                          "nonzero_boundary_parameter_jacobian": True,
                          "callback_counts": callbacks, "intercepted_reference_calls": len(intercepted),
                          "real_scipy_calls": 0, "gate_values_unchanged": True,
                          "synthetic_call_stopped_by_exception": True},
        "unsupported_input_cases": cases, "invalid_input_call_counts": forbidden,
        "exact_rational_RMS_inequality_cases": rms_cases,
        "independent_replay_of_author_analytic_BVP": False,
        "physical_graph_or_G5_claim": False,
    }
    data = (json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False)+"\n").encode()
    with out.open("xb") as f:
        f.write(data)
    print(json.dumps({"status": report["status"], "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest(), "real_scipy_calls": 0,
                      "invalid_cases": len(cases)}))


if __name__ == "__main__":
    main()
