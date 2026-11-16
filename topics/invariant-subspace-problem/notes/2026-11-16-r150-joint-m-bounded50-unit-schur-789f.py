#!/usr/bin/env python3
"""Exact F_31[[t]] truncated unit-Schur solver, with full high-jet backfill.

No mathematical job runs on import.  CLI input/output is documented in the
companion interface note.  Uses only the official python-flint nmod_mat API:
https://python-flint.readthedocs.io/en/latest/nmod_mat.html

A successful receipt certifies G*q == rhs modulo t**precision in every original
row and every RHS column.  It is a local jet certificate, not a global integer
source or a characteristic-zero solution.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
from typing import Any

try:
    from flint import nmod_mat
except ImportError as exc:
    raise SystemExit("python-flint is required; no mathematics was run") from exc

P = 31
FORMAT = "isp-local-unit-schur-f31-bounded50-v1"
MAX_FILE_BYTES = 11_000_000
MAX_DECODED_BYTES = 50 * 461 * 448
MAX_PRECISION = 50
COMPRESS_AT = 1_000_000


class LocalInconsistent(RuntimeError):
    pass


class Deadline(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(x: Any) -> bytes:
    return (json.dumps(x, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def emit(event: str, **fields: Any) -> None:
    print(json.dumps({"event": event, **fields}, sort_keys=True), flush=True)


def zero(m: int, n: int):
    return nmod_mat(m, n, [0] * (m * n), P)


def identity(n: int):
    return nmod_mat(n, n, [int(i == j) for i in range(n) for j in range(n)], P)


def dims(series):
    if not series:
        raise ValueError("empty precision is not a series")
    return len(series), series[0].nrows(), series[0].ncols()


def zero_series(L: int, m: int, n: int):
    return [zero(m, n) for _ in range(L)]


def pick(M, rows, cols):
    return nmod_mat(len(rows), len(cols),
                    [int(M[i, j]) for i in rows for j in cols], P)


def pick_series(A, rows, cols):
    return [pick(M, rows, cols) for M in A]


def series_mul(A, B, L: int, tick=lambda: None):
    _, m, k = dims(A)
    _, kb, n = dims(B)
    if k != kb:
        raise ValueError("series product dimension mismatch")
    if k == 0 or m == 0 or n == 0:
        return zero_series(L, m, n)
    out = []
    for ell in range(L):
        tick()
        v = zero(m, n)
        for i in range(max(0, ell - len(B) + 1), min(ell, len(A) - 1) + 1):
            v = v + A[i] * B[ell - i]
        out.append(v)
    return out


def series_sub(A, B):
    if dims(A) != dims(B):
        raise ValueError("series subtraction dimension mismatch")
    return [a - b for a, b in zip(A, B)]


def series_zero(A) -> bool:
    _, m, n = dims(A)
    z = zero(m, n)
    return all(M == z for M in A)


def unit_inverse(A, tick=lambda: None):
    L, n, n2 = dims(A)
    if n != n2:
        raise ValueError("unit block is not square")
    if n == 0:
        return zero_series(L, 0, 0)
    X0 = A[0].inv()
    out = [X0]
    for ell in range(1, L):
        tick()
        v = zero(n, n)
        for i in range(1, ell + 1):
            v = v + A[i] * out[ell - i]
        out.append(-(X0 * v))
    expected = [identity(n)] + zero_series(L - 1, n, n)
    if series_mul(A, out, L, tick) != expected:
        raise AssertionError("complete unit inverse check failed")
    return out


def pivot_columns(M):
    R, rank = M.rref()
    cols = []
    for i in range(rank):
        col = next((j for j in range(R.ncols()) if int(R[i, j]) != 0), None)
        if col is None:
            raise AssertionError("rref rank/pivot mismatch")
        cols.append(col)
    return cols


def maximal_unit_minor(G0):
    """Return actual row/column indices of a maximal nonsingular minor."""
    cols = pivot_columns(G0)
    r = len(cols)
    if r == 0:
        return [], []
    selected = pick(G0, list(range(G0.nrows())), cols)
    rows = pivot_columns(selected.transpose())
    if len(rows) != r:
        raise AssertionError("row rank profile differs from column rank")
    A0 = pick(G0, rows, cols)
    # The subsequent actual inv() is both used and checked in unit_inverse.
    if int(A0.det()) == 0:
        raise AssertionError("selected constant minor is singular")
    return rows, cols


def encode_series(A) -> bytes:
    L, m, n = dims(A)
    data = bytearray(L * m * n)
    at = 0
    for M in A:
        for x in M.entries():
            value = int(x)
            if not 0 <= value < P:
                raise ValueError("noncanonical field element")
            data[at] = value
            at += 1
    if at != len(data):
        raise AssertionError("matrix entry count mismatch")
    return bytes(data)


def decode_series(data: bytes, L: int, m: int, n: int):
    if len(data) != L * m * n:
        raise ValueError("coefficient-major byte length mismatch")
    if any(x >= P for x in data):
        raise ValueError("input coefficient outside F_31 canonical range")
    stride = m * n
    return [nmod_mat(m, n, list(data[k * stride:(k + 1) * stride]), P)
            for k in range(L)]


def put_series(directory: Path, stem: str, A):
    L, m, n = dims(A)
    if not (0 < L <= MAX_PRECISION and 0 <= m <= 1034 and 0 <= n <= 1021) or L * m * n > MAX_DECODED_BYTES:
        raise ValueError("bounded50 checkpoint exceeds its declared original-series dimensions")
    data = encode_series(A)
    compressed = len(data) > COMPRESS_AT
    stored = gzip.compress(data, compresslevel=6, mtime=0) if compressed else data
    suffix = ".bin.gz" if compressed else ".bin"
    if len(stored) > MAX_FILE_BYTES:
        raise ValueError("bounded50 checkpoint exceeds 11,000,000 stored bytes")
    path = directory / (stem + suffix)
    atomic_write(path, stored)
    return {"file": path.name, "precision": L, "rows": m, "cols": n,
            "sha256": sha(stored), "decoded_sha256": sha(data),
            "bytes": len(stored), "decoded_bytes": len(data),
            "compression": "gzip" if compressed else "none"}


def get_series(directory: Path, desc):
    path = directory / desc["file"]
    if path.stat().st_size > MAX_FILE_BYTES or int(desc["decoded_bytes"]) > MAX_DECODED_BYTES:
        raise ValueError("bounded50 stored checkpoint exceeds declared byte bounds")
    stored = path.read_bytes()
    if sha(stored) != desc["sha256"]:
        raise ValueError("checkpoint stored hash mismatch: " + str(path))
    data = gzip.decompress(stored) if desc["compression"] == "gzip" else stored
    if sha(data) != desc["decoded_sha256"]:
        raise ValueError("checkpoint decoded hash mismatch: " + str(path))
    return decode_series(data, int(desc["precision"]), int(desc["rows"]), int(desc["cols"]))


def nonzero_rhs_columns(A):
    L, m, n = dims(A)
    bad = []
    first = {}
    for j in range(n):
        witness = next(((ell, i, int(A[ell][i, j]))
                        for ell in range(L) for i in range(m)
                        if int(A[ell][i, j]) != 0), None)
        if witness is not None:
            bad.append(j)
            first[str(j)] = list(witness)
    return bad, first


class SchurSolver:
    def __init__(self, checkpoint: Path, binding: str, max_divisions: int,
                 expected_free: int, seconds: float | None = None):
        self.checkpoint = checkpoint
        self.binding = binding
        self.max_divisions = max_divisions
        self.expected_free = expected_free
        self.started = time.monotonic()
        self.deadline = None if seconds is None else self.started + seconds
        checkpoint.mkdir(parents=True, exist_ok=True)

    def tick(self):
        if self.deadline is not None and time.monotonic() > self.deadline:
            raise Deadline("shared helper deadline reached; durable stages are resumable")

    def record_inconsistent(self, directory, kind, residual, depth):
        desc = put_series(directory, "inconsistent-residual", residual)
        bad, first = nonzero_rhs_columns(residual)
        receipt = {"format": FORMAT, "binding": self.binding, "depth": depth,
                   "status": "local-inconsistent", "kind": kind,
                   "bad_rhs_columns": bad, "first_nonzero": first, "residual": desc}
        atomic_write(directory / "inconsistent.json", canonical_json(receipt))
        raise LocalInconsistent(json.dumps(receipt, sort_keys=True))

    def solve(self, G, rhs, depth=0, row_labels=None, col_labels=None):
        self.tick()
        L, m, n = dims(G)
        Lb, mb, nrhs = dims(rhs)
        if Lb != L or mb != m or m < n:
            raise ValueError("invalid truncated rectangular system")
        if m - n != self.expected_free:
            raise ValueError("free-row count changed or input metadata is inconsistent")
        row_labels = list(range(m)) if row_labels is None else list(row_labels)
        col_labels = list(range(n)) if col_labels is None else list(col_labels)
        directory = self.checkpoint / ("stage-%02d" % depth)
        directory.mkdir(parents=True, exist_ok=True)
        incoming = {"G": sha(encode_series(G)), "rhs": sha(encode_series(rhs)),
                    "precision": L, "rows": m, "cols": n, "nrhs": nrhs,
                    "row_labels": row_labels, "column_labels": col_labels}
        manifest_path = directory / "stage.json"
        if manifest_path.exists():
            stage = json.loads(manifest_path.read_text())
            if stage["binding"] != self.binding or stage["incoming"] != incoming:
                raise ValueError("checkpoint belongs to different inputs or source code")
            mats = {name: get_series(directory, desc)
                    for name, desc in stage["matrices"].items()}
            emit("resumed-stage", depth=depth, rows=m, cols=n, precision=L,
                 unit_rank=stage["unit_rank"])
        else:
            rows, cols = maximal_unit_minor(G[0])
            r = len(rows)
            row_set, col_set = set(rows), set(cols)
            row_rest = [i for i in range(m) if i not in row_set]
            col_rest = [j for j in range(n) if j not in col_set]
            A = pick_series(G, rows, cols)
            B = pick_series(G, rows, col_rest)
            C = pick_series(G, row_rest, cols)
            D = pick_series(G, row_rest, col_rest)
            U = pick_series(rhs, rows, list(range(nrhs)))
            V = pick_series(rhs, row_rest, list(range(nrhs)))
            Ai = unit_inverse(A, self.tick)
            AiB = series_mul(Ai, B, L, self.tick)
            AiU = series_mul(Ai, U, L, self.tick)
            schur = series_sub(D, series_mul(C, AiB, L, self.tick))
            residual = series_sub(V, series_mul(C, AiU, L, self.tick))
            if schur[0] != zero(m-r, n-r):
                raise AssertionError("maximal constant rank did not annihilate Schur constant")
            mats = {"G": G, "rhs": rhs, "unit_inverse": Ai,
                    "Ainv_B": AiB, "Ainv_rhs": AiU,
                    "schur": schur, "schur_rhs": residual}
            descriptions = {key: put_series(directory, key, value)
                            for key, value in mats.items()}
            stage = {"format": FORMAT, "binding": self.binding, "depth": depth,
                     "incoming": incoming, "unit_rank": r,
                     "unit_rows": rows, "unit_columns": cols,
                     "remaining_rows": row_rest, "remaining_columns": col_rest,
                     "unit_row_labels": [row_labels[i] for i in rows],
                     "unit_column_labels": [col_labels[j] for j in cols],
                     "remaining_row_labels": [row_labels[i] for i in row_rest],
                     "remaining_column_labels": [col_labels[j] for j in col_rest],
                     "row_label_meaning": "retained row slots after preceding Schur eliminations",
                     "matrices": descriptions}
            atomic_write(manifest_path, canonical_json(stage))
            emit("saved-stage", depth=depth, rows=m, cols=n, precision=L, unit_rank=r)

        r = int(stage["unit_rank"])
        rows = stage["unit_rows"]
        cols = stage["unit_columns"]
        row_rest = stage["remaining_rows"]
        col_rest = stage["remaining_columns"]
        if n - r == 0:
            # All unknowns eliminated.  Every remaining free row and every jet
            # of every RHS must vanish, not only the constant term.
            if m-r != self.expected_free:
                raise AssertionError("terminal free-row count is not the declared value")
            if not series_zero(mats["schur_rhs"]):
                self.record_inconsistent(directory, "terminal-free-rows",
                                         mats["schur_rhs"], depth)
            q_rest = zero_series(L, 0, nrhs)
        else:
            # The coefficient t^0 is a necessary condition before division.
            if mats["schur_rhs"][0] != zero(m-r, nrhs):
                self.record_inconsistent(directory, "constant-before-t-division",
                                         [mats["schur_rhs"][0]], depth)
            if depth >= self.max_divisions:
                raise ValueError("claimed maximum Smith exponent exceeded")
            if L <= 1:
                raise ValueError("insufficient jet precision for remaining columns")
            q_low = self.solve(mats["schur"][1:], mats["schur_rhs"][1:],
                               depth + 1,
                               stage["remaining_row_labels"],
                               stage["remaining_column_labels"])
            # Division by t loses the last coefficient of q_rest.  Setting it
            # to zero is legal; the current unit equation then fills *all*
            # L coefficients of q_unit.  Do not truncate the final solution.
            q_rest = q_low + [zero(n-r, nrhs)]
        q_unit = series_sub(mats["Ainv_rhs"],
                            series_mul(mats["Ainv_B"], q_rest, L, self.tick))
        q = []
        for ell in range(L):
            self.tick()
            out = zero(n, nrhs)
            for i, original in enumerate(cols):
                for j in range(nrhs):
                    out[original, j] = q_unit[ell][i, j]
            for i, original in enumerate(col_rest):
                for j in range(nrhs):
                    out[original, j] = q_rest[ell][i, j]
            q.append(out)
        complete_residual = series_sub(series_mul(G, q, L, self.tick), rhs)
        residual_desc = put_series(directory, "backsubstitution-residual", complete_residual)
        if not series_zero(complete_residual):
            raise AssertionError("complete high-jet backsubstitution verification failed")
        solution_desc = put_series(directory, "solution-all-jets", q)
        receipt = {"format": FORMAT, "binding": self.binding, "depth": depth,
                   "status": "verified", "precision": L,
                   "verified_rows": m, "verified_rhs_columns": nrhs,
                   "all_coefficients_verified": True,
                   "solution": solution_desc, "residual": residual_desc}
        atomic_write(directory / "backsubstitution.json", canonical_json(receipt))
        emit("verified-stage", depth=depth, precision=L, rows=m, cols=n, nrhs=nrhs)
        return q


def read_input_series(root: Path, desc, precision: int):
    path = Path(desc["file"])
    if not path.is_absolute():
        path = root / path
    if path.stat().st_size > MAX_FILE_BYTES or int(desc["decoded_bytes"]) > MAX_DECODED_BYTES:
        raise ValueError("bounded50 stored checkpoint exceeds declared byte bounds")
    stored = path.read_bytes()
    if sha(stored) != desc["sha256"]:
        raise ValueError("input SHA256 mismatch: " + str(path))
    compression = desc.get("compression", "gzip" if path.suffix == ".gz" else "none")
    if compression not in ("none", "gzip"):
        raise ValueError("unknown input compression")
    data = gzip.decompress(stored) if compression == "gzip" else stored
    if "decoded_sha256" in desc and sha(data) != desc["decoded_sha256"]:
        raise ValueError("input decoded SHA256 mismatch")
    return decode_series(data, precision, int(desc["rows"]), int(desc["cols"])), {
        "file": str(path), "sha256": sha(stored), "decoded_sha256": sha(data),
        "decoded_bytes": len(data), "compression": compression}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata", required=True)
    ap.add_argument("--checkpoint-dir", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--max-seconds", type=float, default=None)
    args = ap.parse_args(argv)
    metadata_path = Path(args.metadata).resolve()
    raw_metadata = metadata_path.read_bytes()
    meta = json.loads(raw_metadata)
    if meta.get("format") != FORMAT or int(meta.get("modulus", 0)) != P:
        raise ValueError("metadata format/modulus mismatch")
    L = int(meta["precision"])
    max_div = int(meta["max_smith_exponent"])
    free = int(meta["expected_free_rows"])
    if not (0 <= max_div < L):
        raise ValueError("max Smith exponent must be strictly below the jet precision")
    G, G_info = read_input_series(metadata_path.parent, meta["G"], L)
    rhs, rhs_info = read_input_series(metadata_path.parent, meta["rhs"], L)
    if dims(G)[1] != dims(rhs)[1]:
        raise ValueError("input row mismatch")
    script_hash = sha(Path(__file__).read_bytes())
    binding_data = {"format": FORMAT, "metadata_sha256": sha(raw_metadata),
                    "script_sha256": script_hash,
                    "G": {k: v for k, v in G_info.items() if k != "file"},
                    "rhs": {k: v for k, v in rhs_info.items() if k != "file"},
                    "precision": L, "max_smith_exponent": max_div,
                    "expected_free_rows": free}
    binding = sha(canonical_json(binding_data))
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    atomic_write(output / "input-binding.json",
                 canonical_json({**binding_data, "binding": binding,
                                 "metadata": meta,
                                 "resolved_input_files": {"G": G_info["file"],
                                                          "rhs": rhs_info["file"]}}))
    solver = SchurSolver(Path(args.checkpoint_dir), binding, max_div, free,
                         args.max_seconds)
    if args.max_seconds is not None and hasattr(signal, "setitimer"):
        def expired(signum, frame):
            raise Deadline("helper wall-clock limit reached; complete stages are durable")
        signal.signal(signal.SIGALRM, expired)
        signal.setitimer(signal.ITIMER_REAL, args.max_seconds)
    started = time.monotonic()
    try:
        q = solver.solve(G, rhs)
        solution = put_series(output, "q-all-jets", q)
        # solver.solve has already verified this complete original system.
        receipt = {"format": FORMAT, "binding": binding, "status": "verified",
                   "source_code_sha256": script_hash,
                   "precision": L, "rows": dims(G)[1], "cols": dims(G)[2],
                   "rhs_columns": dims(rhs)[2], "free_rows": free,
                   "verified_original_system": True,
                   "all_coefficients_verified": True,
                   "max_divisions_allowed": max_div,
                   "solution": solution,
                   "wall_seconds": time.monotonic() - started,
                   "scope": "F_31[[t]] modulo t^precision only; no global integer lift"}
        atomic_write(output / "receipt.json", canonical_json(receipt))
        emit("complete", **receipt)
        return 0
    except (Deadline, LocalInconsistent) as exc:
        status = "checkpointed-deadline" if isinstance(exc, Deadline) else "local-inconsistent"
        atomic_write(output / "receipt.json", canonical_json({
            "format": FORMAT, "binding": binding, "status": status,
            "wall_seconds": time.monotonic() - started, "message": str(exc),
            "verified_original_system": False}))
        emit(status, binding=binding, message=str(exc))
        return 75 if isinstance(exc, Deadline) else 2
    except Exception as exc:
        atomic_write(output / "receipt.json", canonical_json({
            "format": FORMAT, "binding": binding, "status": "failed",
            "wall_seconds": time.monotonic() - started,
            "exception_type": type(exc).__name__, "message": str(exc),
            "verified_original_system": False}))
        raise
    finally:
        if args.max_seconds is not None and hasattr(signal, "setitimer"):
            signal.setitimer(signal.ITIMER_REAL, 0)


if __name__ == "__main__":
    raise SystemExit(main())
