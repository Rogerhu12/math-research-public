#!/usr/bin/env python3
"""Complete original collocation matrix with pivoted LAPACK band LU.

Only equation rows are permuted: left boundary, interval blocks, right
boundary.  Node-major unknowns, every physical/core/control column and all
original finite equations are retained.  No shooting transfer matrix,
truncated SVD, row deletion, or changed boundary operator is used.

The band is allocated once in Fortran order and factored in place.  Original
L/R blocks remain on disk for residuals against the unfactored matrix.
Residual correction uses this same LU and the same original matrix, with
long-double accumulation; it changes the linear algorithm, not the system.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import tempfile
import time

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import numpy as np
from scipy.linalg.lapack import dgbtrf, dgbtrs


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value, compressed=False):
    path = Path(path)
    raw = (json.dumps(value, indent=None if compressed else 2,
                      separators=(",", ":") if compressed else None,
                      allow_nan=False) + "\n").encode()
    if compressed:
        raw = gzip.compress(raw, mtime=0)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    result = dict(file=path.name, bytes=len(raw), sha256=sha(path),
                  single_git_file_under_5MB=len(raw) < 5_000_000)
    if not result["single_git_file_under_5MB"]:
        # RUNNER_TEMP is an Actions artifact workspace, not a Git commit.
        # Keep the complete numerical checkpoint; the existing publisher
        # enforces its own repository limit without vetoing mathematics.
        print(json.dumps(dict(event="large_complete_artifact_retained",
                              **result, git_size_policy_applied_by_publisher=True)), flush=True)
    return result


class CompleteBandFactor:
    """DiskQRFactor-compatible exact row permutation and full band factor."""

    def __init__(self, n, m, left, right, left_count, work,
                 verify_residual=True, *, report_dir, field_modes,
                 mesh=None, factor_index=1, max_refinements=4):
        if (os.environ.get("GITHUB_ACTIONS") != "true"
                or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
            raise RuntimeError("Numerical work belongs to the public repository Actions")
        self.n, self.m, self.nl = int(n), int(m), int(left_count)
        self.k, self.dimension = self.n - self.nl, self.n * self.m
        self.shape, self.nnz = (self.dimension, self.dimension), 2*self.m*self.n*self.n
        self.left = np.asarray(left[:self.nl], dtype=float).copy()
        self.right = np.asarray(right[self.nl:], dtype=float).copy()
        if (np.any(left[self.nl:] != 0) or np.any(right[:self.nl] != 0)
                or self.left.shape != (self.nl, self.n)
                or self.right.shape != (self.k, self.n)):
            raise ValueError("The original full boundary must remain separated")
        self.M = int(field_modes)
        self.physical, self.core_end = 3*self.M+2, 4*self.M+2
        if not self.physical <= self.core_end <= self.n:
            raise ValueError("Complete physical/core/control rows are required")
        self.report_dir, self.factor_index = Path(report_dir), int(factor_index)
        self.report_dir.mkdir(parents=True, exist_ok=True)
        self.mesh = None if mesh is None else np.asarray(mesh, float).copy()
        if self.mesh is not None and self.mesh.shape != (self.m,):
            raise ValueError("The diagnostic mesh must be this original collocation mesh")
        self.directory = Path(tempfile.mkdtemp(prefix="complete-band-", dir=work))
        self.kl, self.ku = self.n + self.nl - 1, 2*self.n - self.nl - 1
        self.ldab = 2*self.kl + self.ku + 1
        # dgbtrf requires the extra kl rows reserved for pivot fill.
        self.ab = np.zeros((self.ldab, self.dimension), dtype=np.float64, order="F")
        if not self.ab.flags.f_contiguous or self.ab.dtype != np.dtype("float64"):
            raise RuntimeError("The LAPACK band must already be native float64 Fortran storage")
        self.next_interval, self.solve_count = 0, 0
        self.verify_residual, self.max_refinements = bool(verify_residual), int(max_refinements)
        self.started = time.monotonic()
        self.matrix_infinity_norm = max(float(np.sum(abs(self.left), axis=1).max(initial=0)),
                                        float(np.sum(abs(self.right), axis=1).max(initial=0)))
        self._put(self.left, 0, 0)
        self._put(self.right, self.nl + (self.m-1)*self.n, (self.m-1)*self.n)
        self.report = dict(
            schema="complete-original-banded-collocation-factor-v1",
            source_sha256=sha(__file__), factor=self.factor_index,
            n=self.n, nodes=self.m, dimension=self.dimension,
            physical_rows=self.physical, complete_core_rows=self.M,
            complete_scalar_rows=self.n-self.core_end, left_rows=self.nl, right_rows=self.k,
            lower_bandwidth=self.kl, upper_bandwidth=self.ku, lapack_band_rows=self.ldab,
            band_shape=list(self.ab.shape), band_bytes=int(self.ab.nbytes),
            initial_band_Fortran_contiguous=True,
            equation_order="left boundary, all original interval blocks, right boundary",
            original_RHS_order="all original interval blocks, left boundary, right boundary",
            variable_order="Unchanged node-major complete augmented state",
            stored_original_blocks="Unfactored complete binary64 L and R, one file per interval",
            singular_values_truncated=False, mathematical_equations_changed=False,
            nonlinear_acceptance_thresholds_changed=False)
        write(self.report_dir / f"factor-{self.factor_index:03d}.json", self.report)

    def _put(self, values, row_start, column_start):
        values = np.asarray(values, dtype=float)
        if not np.all(np.isfinite(values)):
            raise FloatingPointError("Nonfinite original collocation or boundary block")
        rows = row_start + np.arange(values.shape[0])[:, None]
        columns = column_start + np.arange(values.shape[1])[None, :]
        band_rows = self.kl + self.ku + rows - columns
        if np.any(band_rows < self.kl) or np.any(band_rows >= self.ldab):
            raise ValueError("An original matrix entry lies outside the derived full band")
        self.ab[band_rows, columns] = values

    def append(self, j, L, R):
        if j != self.next_interval:
            raise ValueError("Append every original interval exactly once in order")
        L, R = np.asarray(L), np.asarray(R)
        if L.shape != (self.n, self.n) or R.shape != L.shape:
            raise ValueError("A physical, core or control row was removed from a local block")
        row = self.nl + j*self.n
        self._put(L, row, j*self.n)
        self._put(R, row, (j+1)*self.n)
        self.matrix_infinity_norm = max(self.matrix_infinity_norm,
            float(np.max(np.sum(abs(L), axis=1)+np.sum(abs(R), axis=1))))
        np.savez(self.directory / f"{j:05d}.npz", L=L, R=R)
        self.next_interval += 1

    def finish(self):
        if self.next_interval != self.m-1:
            raise ValueError("The complete original collocation matrix has not been supplied")
        started = time.monotonic()
        pointer = self.ab.__array_interface__["data"][0]
        lu, piv, info = dgbtrf(self.ab, self.kl, self.ku, overwrite_ab=1)
        shared = bool(np.shares_memory(lu, self.ab))
        same_pointer = pointer == lu.__array_interface__["data"][0]
        self.ab, self.piv = lu, piv
        self.report.update(
            factorization="LAPACK dgbtrf with its original partial pivoting",
            lapack_info=int(info), factorization_seconds=time.monotonic()-started,
            complete_construction_seconds=time.monotonic()-self.started,
            LU_shares_input_storage=shared, LU_retains_input_pointer=same_pointer,
            final_band_Fortran_contiguous=bool(lu.flags.f_contiguous),
            original_matrix_infinity_norm=self.matrix_infinity_norm,
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        write(self.report_dir / f"factor-{self.factor_index:03d}.json", self.report)
        print(json.dumps(dict(event="complete_banded_factor", **self.report)), flush=True)
        if not shared or not same_pointer:
            raise RuntimeError("The requested in-place LAPACK band storage was not preserved")
        if info < 0:
            raise RuntimeError("LAPACK dgbtrf rejected argument " + str(-info))
        if info > 0:
            raise RuntimeError("The complete band factor has a zero pivot at LAPACK index " + str(info))
        return self

    def _solve_once(self, rhs):
        split = (self.m-1)*self.n
        b = np.empty((self.dimension, 1), dtype=np.float64, order="F")
        b[:self.nl, 0] = rhs[split:split+self.nl]
        b[self.nl:self.nl+split, 0] = rhs[:split]
        b[self.nl+split:, 0] = rhs[split+self.nl:]
        solution, info = dgbtrs(self.ab, self.kl, self.ku, b, self.piv, overwrite_b=1)
        if info:
            raise RuntimeError("LAPACK dgbtrs failed with info=" + str(info))
        answer = np.asarray(solution[:, 0]).copy()
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError("The complete original band solve returned a nonfinite direction")
        return answer

    def _residual(self, answer, rhs):
        """Original row order; accumulation in platform long double."""
        X = np.asarray(answer).reshape(self.m, self.n).astype(np.longdouble)
        rhs_ld = np.asarray(rhs, dtype=np.longdouble)
        residual = np.empty(self.dimension, dtype=np.longdouble)
        intervals, per_state = [], np.zeros(self.n, dtype=np.longdouble)
        for j in range(self.m-1):
            with np.load(self.directory / f"{j:05d}.npz") as block:
                error = (block["L"].astype(np.longdouble) @ X[j]
                         + block["R"].astype(np.longdouble) @ X[j+1]
                         - rhs_ld[j*self.n:(j+1)*self.n])
            residual[j*self.n:(j+1)*self.n] = error
            per_state = np.maximum(per_state, abs(error))
            row = int(np.argmax(abs(error)))
            record = dict(interval=j, residual_max=float(abs(error[row])), state_row=row,
                physical_max=float(np.max(abs(error[:self.physical]), initial=0)),
                constant_core_max=float(np.max(abs(error[self.physical:self.core_end]), initial=0)),
                constant_parameter_max=float(np.max(abs(error[self.core_end:]), initial=0)))
            if self.mesh is not None:
                record.update(s_left=float(self.mesh[j]), s_right=float(self.mesh[j+1]))
            intervals.append(record)
        split = (self.m-1)*self.n
        residual[split:split+self.nl] = self.left.astype(np.longdouble) @ X[0] - rhs_ld[split:split+self.nl]
        residual[split+self.nl:] = self.right.astype(np.longdouble) @ X[-1] - rhs_ld[split+self.nl:]
        if not np.all(np.isfinite(residual)):
            raise FloatingPointError("Residual against the complete unfactored matrix is nonfinite")
        absolute, scale = float(np.max(abs(residual))), float(np.max(abs(rhs_ld)))
        solution_max = float(np.max(abs(X)))
        denominator = self.matrix_infinity_norm*solution_max + scale
        report = dict(
            accumulation_dtype=str(np.dtype(np.longdouble)),
            accumulation_mantissa_bits=int(np.finfo(np.longdouble).nmant),
            residual_max=absolute, rhs_max=scale,
            relative_residual=absolute/max(scale, np.finfo(float).tiny),
            normwise_backward_error=absolute/max(denominator, np.finfo(float).tiny),
            backward_error_denominator="||A_original||_infinity ||step||_infinity + ||rhs||_infinity",
            solution_max=solution_max,
            residual_max_by_block=dict(
                physical=float(np.max(per_state[:self.physical], initial=0)),
                constant_core=float(np.max(per_state[self.physical:self.core_end], initial=0)),
                constant_parameters=float(np.max(per_state[self.core_end:], initial=0)),
                left_boundary=float(np.max(abs(residual[split:split+self.nl]), initial=0)),
                right_boundary=float(np.max(abs(residual[split+self.nl:]), initial=0))),
            maximum_collocation_residual_by_state=per_state.astype(float).tolist(),
            intervals=intervals)
        return residual.astype(float), report

    def solve(self, rhs):
        rhs = np.asarray(rhs, dtype=float)
        if rhs.shape != (self.dimension,) or not np.all(np.isfinite(rhs)):
            raise ValueError("Supply the complete finite original one-column RHS")
        started = time.monotonic()
        answer = self._solve_once(rhs)
        residual, report = self._residual(answer, rhs)
        history = [dict(refinement=0, residual_max=report["residual_max"],
                        relative_residual=report["relative_residual"],
                        solution_max=report["solution_max"])]
        # This is a linear-solve accuracy target, not a nonlinear acceptance
        # threshold.  The original Newton and all its acceptance gates remain.
        target = 1e-10*report["rhs_max"]
        for refinement in range(1, self.max_refinements+1):
            if report["residual_max"] <= target:
                break
            correction = self._solve_once(-residual)
            trial = answer + correction
            next_residual, next_report = self._residual(trial, rhs)
            better = next_report["residual_max"] < report["residual_max"]
            history.append(dict(refinement=refinement,
                residual_max=next_report["residual_max"],
                relative_residual=next_report["relative_residual"],
                solution_max=next_report["solution_max"],
                correction_max=float(np.max(abs(correction))), retained=bool(better)))
            if not better:
                break
            previous = report["residual_max"]
            answer, residual, report = trial, next_residual, next_report
            if report["residual_max"] >= .95*previous:
                break
        self.solve_count += 1
        report.update(
            schema="complete-original-banded-linear-solve-v1", factor=self.factor_index,
            solve=self.solve_count, seconds=time.monotonic()-started,
            original_row_order_retained_in_residual=True,
            linear_accuracy_target_relative=1e-10,
            linear_accuracy_target_met=report["residual_max"] <= target,
            same_matrix_residual_corrections=history,
            actual_original_full_matrix_used=True, mathematical_rank_certified=False,
            maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if self.solve_count == 1:
            stem = f"factor-{self.factor_index:03d}-first"
            report["step_artifact"] = write(self.report_dir / f"{stem}-step.json.gz",
                dict(n=self.n, nodes=self.m, field_modes=self.M,
                     layout="Unchanged node-major complete augmented Newton direction",
                     values=answer.reshape(self.m, self.n).tolist()), True)
            report["rhs_artifact"] = write(self.report_dir / f"{stem}-rhs.json.gz",
                dict(n=self.n, nodes=self.m, left_rows=self.nl,
                     layout="Original intervals, left boundary, right boundary",
                     values=rhs.tolist()), True)
        write(self.report_dir / f"factor-{self.factor_index:03d}-solve-{self.solve_count:03d}.json", report)
        print(json.dumps({key: report[key] for key in (
            "factor", "solve", "residual_max", "rhs_max", "relative_residual",
            "normwise_backward_error", "solution_max", "linear_accuracy_target_met",
            "same_matrix_residual_corrections", "seconds", "maximum_RSS_kib")}
            | {"event": "complete_banded_solve"}), flush=True)
        return answer

    def close(self):
        self.ab = None
        directory = getattr(self, "directory", None)
        if directory is not None:
            shutil.rmtree(directory, ignore_errors=True)
            self.directory = None

    def __del__(self):
        self.close()
