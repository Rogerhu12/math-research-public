"""Actual full Boolean primitive-Gram adjacent search, not a proof by samples.

The incidence A_j is D**j/j! on the *whole* physical layer.  We obtain
Gamma_j = U.T (A_j A_j.T)^(-1) U using a thin SVD of A_j, never an
inverse of the primitive compression.  U is one common orthonormal kernel
basis.  Every reported ratio is an operator generalized eigenvalue.

Run with OPENBLAS_NUM_THREADS=1 for these small dense matrices.
"""

from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path

import numpy as np
from scipy import linalg, optimize


@lru_cache(None)
def layer(n, s):
    return tuple(combinations(range(n), s))


@lru_cache(None)
def pattern(n, s, j):
    rows, cols, extra = [], [], []
    source = layer(n, s)
    lookup = {v: i for i, v in enumerate(source)}
    for col, target in enumerate(layer(n, s + j)):
        t = set(target)
        for r in combinations(target, s):
            rows.append(lookup[r])
            cols.append(col)
            extra.append(tuple(sorted(t.difference(r))))
    return np.array(rows), np.array(cols), np.array(extra, dtype=int).reshape(-1, j)


def incidence(weights, s, j):
    n = len(weights)
    if j == 0:
        return np.eye(comb(n, s))
    rows, cols, extra = pattern(n, s, j)
    result = np.zeros((comb(n, s), comb(n, s + j)))
    result[rows, cols] = np.prod(np.asarray(weights)[extra], axis=1)
    return result


def actual_grams(weights, s, last=None):
    weights = np.asarray(weights, dtype=float)
    weights = weights / max(weights)
    n, h = len(weights), len(weights) - 2 * s
    if last is not None:
        h = min(h, last)
    d = incidence(weights, s - 1, 1)
    _, ds, v = linalg.svd(d, full_matrices=True, check_finite=False)
    u = v[d.shape[0]:].T
    grams = [np.eye(u.shape[1])]
    cond_a = [1.0]
    for j in range(1, h + 1):
        a = incidence(weights, s, j)
        left, sigma, _ = linalg.svd(a, full_matrices=False, check_finite=False)
        inverse_columns = (left.T @ u) / sigma[:, None]
        grams.append(inverse_columns.T @ inverse_columns)
        cond_a.append(float(sigma[0] / sigma[-1]))
    residual = linalg.norm(d @ u, 2) / linalg.norm(d, 2)
    return weights, u, grams, cond_a, float(residual), float(ds[0] / ds[-1])


def ratios(weights, s=2, details=False, last=None):
    weights, u, grams, cond_a, residual, cond_d = actual_grams(weights, s, last)
    out = []
    for edge in range(1, len(grams) - 1):
        minus, zero, plus = grams[edge - 1:edge + 2]
        lm = linalg.cholesky(minus, lower=True, check_finite=False)
        lp = linalg.cholesky(plus, lower=True, check_finite=False)
        # lm^-1 zero lp^-T has the same singular values as its transpose.
        transfer = linalg.solve_triangular(lm, zero, lower=True, check_finite=False)
        transfer = linalg.solve_triangular(lp, transfer.T, lower=True, check_finite=False).T
        sv = linalg.svdvals(transfer, check_finite=False)
        ratio = float(sv[0] ** 2)
        row = {"edge": edge, "ratio": ratio}
        if details:
            row.update(weights=weights.tolist(), cond_incidence=cond_a,
                       cond_grams=[float(np.linalg.cond(g)) for g in grams],
                       primitive_residual=residual, cond_deletion=cond_d)
        out.append(row)
    return out


def scan(args):
    rng = np.random.default_rng(args.seed)
    record = {"seed": args.seed, "samples_per_span": args.samples,
              "condition_filter": "all_heights" if args.whole_height_filter else "three_required_heights",
              "cases": []}
    for n in args.n:
        h = n - 2 * args.s
        maxima = {edge: None for edge in range(1, h)}
        accepted = failures = flagged = 0
        print(json.dumps({"N": n, "s": args.s, "equal": ratios(np.ones(n), args.s)}), flush=True)
        for span in args.spans:
            local = {edge: None for edge in range(1, h)}
            for _ in range(args.samples):
                logs = rng.uniform(-span, 0, size=n)
                weights = np.exp(logs - max(logs))
                try:
                    rows = ratios(weights, args.s, details=True)
                    for row in rows:
                        row["log_span_bound"] = span
                        edge = row["edge"]
                        indices = slice(None) if args.whole_height_filter else slice(edge - 1, edge + 2)
                        if max(row["cond_incidence"][indices]) > args.max_cond or max(row["cond_grams"][indices]) > args.max_cond:
                            flagged += 1
                            continue
                        accepted += 1
                        if local[edge] is None or row["ratio"] > local[edge]["ratio"]:
                            local[edge] = row
                        if maxima[edge] is None or row["ratio"] > maxima[edge]["ratio"]:
                            maxima[edge] = row
                except (ValueError, linalg.LinAlgError, FloatingPointError):
                    failures += 1
            print(json.dumps({"N": n, "span": span, "maxima": local}), flush=True)
        case = {"N": n, "s": args.s, "maxima": maxima,
                "accepted_edges": accepted, "flagged_edges": flagged, "failures": failures}
        record["cases"].append(case)
    if args.output:
        Path(args.output).write_text(json.dumps(record, indent=2) + "\n")


def maximize(args):
    n, s, edge = args.n[0], args.s, args.edge
    best = {"ratio": -1.0}
    generations = 0
    def objective(logs):
        nonlocal best
        # One weight is fixed to one; all others are independently variable.
        weights = np.exp(np.r_[np.sort(logs), 0.0])
        try:
            row = ratios(weights, s, details=True, last=edge + 1)[edge - 1]
            if max(row["cond_incidence"][edge - 1:edge + 2]) > args.max_cond or max(row["cond_grams"][edge - 1:edge + 2]) > args.max_cond:
                return 1e3
            if row["ratio"] > best["ratio"]:
                best = row
            return -row["ratio"]
        except (ValueError, linalg.LinAlgError, FloatingPointError):
            return 1e3
    def checkpoint(_vector, _convergence):
        nonlocal generations
        generations += 1
        if args.output and generations % 10 == 0:
            Path(args.output).write_text(json.dumps({"N": n, "s": s, "edge": edge,
                "span": args.spans[-1], "generations": generations,
                "status": "running_checkpoint", "best": best}, indent=2) + "\n")
    result = optimize.differential_evolution(
        objective, [(-args.spans[-1], 0)] * (n - 1), seed=args.seed,
        maxiter=args.iterations, popsize=args.population, polish=True,
        tol=1e-9, updating="immediate", callback=checkpoint)
    output = {"N": n, "s": s, "edge": edge, "span": args.spans[-1],
              "evaluations": result.nfev, "success": bool(result.success),
              "message": str(result.message), "best": best}
    print(json.dumps(output, indent=2), flush=True)
    if args.output:
        Path(args.output).write_text(json.dumps(output, indent=2) + "\n")


def exact(args):
    import sympy as sp
    import mpmath as mp
    mp.mp.dps = args.digits
    weights = tuple(map(sp.Rational, args.weights.split(',')))
    n, s = len(weights), args.s
    def exact_incidence(j, source_s=s):
        mat = sp.zeros(comb(n, source_s), comb(n, source_s + j))
        for i, source in enumerate(layer(n, source_s)):
            source = set(source)
            for k, target in enumerate(layer(n, source_s + j)):
                if source.issubset(target):
                    mat[i, k] = sp.prod(weights[a] for a in set(target) - source)
        return mat
    d = exact_incidence(1, s - 1)
    z = sp.Matrix.hstack(*d.nullspace())
    assert d * z == sp.zeros(d.rows, z.cols)
    grams = [z.T * z]
    for j in range(1, n - 2 * s + 1):
        a = exact_incidence(j)
        grams.append(z.T * (a * a.T).inv(method="DM") * z)
    result = {"weights": [str(w) for w in weights], "N": n, "s": s, "checks": []}
    def mp_matrix(mat):
        return mp.matrix([[mp.mpf(str(v.p)) / mp.mpf(str(v.q)) for v in mat.row(i)] for i in range(mat.rows)])
    for edge in range(1, len(grams) - 1):
        minus, zero, plus = grams[edge - 1:edge + 2]
        lm = mp.cholesky(mp_matrix(minus))
        lp = mp.cholesky(mp_matrix(plus))
        transfer = lm ** -1 * mp_matrix(zero) * (lp.T ** -1)
        eigs = mp.eigsy(transfer * transfer.T, eigvals_only=True)
        approximation = mp.nstr(eigs[eigs.rows - 1, 0], min(40, args.digits // 2))
        defect = minus - zero * plus.inv(method="DM") * zero
        assert defect == defect.T
        ell = sp.eye(defect.rows)
        pivots = []
        for i in range(defect.rows):
            p = defect[i, i] - sum(ell[i, k] ** 2 * pivots[k] for k in range(i))
            pivots.append(p)
            if p <= 0:
                check = {"edge": edge, "status": "negative" if p < 0 else "zero_pivot", "pivot": i,
                         "mp_ratio_not_certificate": approximation, "mp_digits": args.digits}
                if p < 0:
                    direction = ell[:i + 1, :i + 1].T.inv()[:, i]
                    direction = direction.col_join(sp.zeros(defect.rows - i - 1, 1))
                    value = (direction.T * defect * direction)[0]
                    assert value == p and value < 0
                    check.update(vector=[str(v) for v in direction], quadratic=str(value))
                result["checks"].append(check)
                break
            for row in range(i + 1, defect.rows):
                ell[row, i] = (defect[row, i] - sum(ell[row, k] * ell[i, k] * pivots[k] for k in range(i))) / p
        else:
            result["checks"].append({"edge": edge, "status": "strictly_positive", "dimension": defect.rows,
                                     "mp_ratio_not_certificate": approximation, "mp_digits": args.digits})
    print(json.dumps(result, indent=2), flush=True)
    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["scan", "maximize", "exact"])
    parser.add_argument("--n", nargs="+", type=int, default=[6, 7, 8])
    parser.add_argument("--s", type=int, default=2)
    parser.add_argument("--edge", type=int, default=1)
    parser.add_argument("--spans", nargs="+", type=float, default=[2, 4, 6])
    parser.add_argument("--samples", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=789277)
    parser.add_argument("--max-cond", type=float, default=1e9)
    parser.add_argument("--whole-height-filter", action="store_true")
    parser.add_argument("--iterations", type=int, default=250)
    parser.add_argument("--population", type=int, default=20)
    parser.add_argument("--weights", default="1,2,3,4,5,6")
    parser.add_argument("--digits", type=int, default=100)
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.mode == "scan":
        scan(args)
    elif args.mode == "maximize":
        maximize(args)
    else:
        exact(args)


if __name__ == "__main__":
    main()
