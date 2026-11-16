#!/usr/bin/env python3
# Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.
"""Runtime-size R150 local jet solve, retaining every original row and source.

The pinned unit-Schur helper is imported without modification.  This wrapper
supports SG31/SF31/SQ31 and an optional actual old197 five-jet prefix.  A success
is an F_31[[s-2]] jet identity only, never a global polynomial or integer lift.
No mathematical job runs on import.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import struct
import sys
import time

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

P, ROWS, COLS = 31, 1034, 1021
CONSTANTS, FREE, SMITH_MAX = 573, 13, 5
MAX_PRECISION, MAX_TARGETS, PREFIX_LENGTH = 50, 229, 5
SCHUR = "2026-11-16-r150-joint-m-bounded50-unit-schur-789f.py"
SCHUR_SHA = "71295507dddb64dc7f60172910158d0d9043721597e397df0fb264dfd51fdcd9"
FORMAT = "r150-joint-m-root-one-local-unit-solve-v1"
OUTPUT_NAME = "complete-G-q-root1.bin"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(x) -> bytes:
    return (json.dumps(x, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def hex_binding(value: str) -> str:
    if len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise ValueError("binding must be 64 lowercase hexadecimal characters")
    return value


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("r150_saturated_exact_unit_schur", path)
    if spec is None or spec.loader is None:
        raise ValueError("cannot import the pinned unit-Schur helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def checked_header(data: bytes, magic: bytes):
    if len(data) < 88 or data[:8] != magic:
        raise ValueError("bad complete local input header: " + repr(magic))
    header = struct.unpack_from("<4I", data, 8)
    binding = hex_binding(data[24:88].decode("ascii"))
    return header, binding


def read_inputs(args):
    g, rhs = args.G.read_bytes(), args.rhs.read_bytes()
    gh, gb = checked_header(g, b"R150SG31")
    rh, rb = checked_header(rhs, b"R150SF31")
    if gh[:3] != (P, ROWS, COLS) or rh[:2] != (P, ROWS):
        raise ValueError("actual 1034 by 1021 original G and full original RHS required")
    cache_L, nt, L = gh[3], rh[2], rh[3]
    if not (SMITH_MAX < L <= cache_L <= MAX_PRECISION):
        raise ValueError("need 5 < used precision <= G-cache precision <= 50")
    if not 1 <= nt <= MAX_TARGETS:
        raise ValueError("runtime target count must be in 1..229")
    if gb != args.binding or rb != args.binding:
        raise ValueError("G and RHS must carry the supplied pipeline binding")
    gp = 88 + 4 * COLS
    rp = 88 + 2 * nt + 8 * ROWS
    if len(g) != gp + cache_L * ROWS * COLS:
        raise ValueError("complete G-cache byte length, including unused high jets, is required")
    if len(rhs) != rp + L * ROWS * nt:
        raise ValueError("complete dynamic RHS byte length is required")
    records = [struct.unpack_from("<HBB", g, 88 + 4 * j) for j in range(COLS)]
    leading = [rec[0] for rec in records]
    if leading != sorted(set(leading)) or not all(1 <= c <= ROWS for c in leading):
        raise ValueError("actual sorted distinct G leading-component dictionary required")
    if sum(rec[1] for rec in records) != 716:
        raise ValueError("actual original G degree total 716 required")
    if any(not (0 <= degree <= 8 and 1 <= lc < P) for _, degree, lc in records):
        raise ValueError("bad actual G degree or original leading coefficient")
    labels = list(struct.unpack_from("<%dH" % nt, rhs, 88))
    if len(set(labels)) != nt or any(label == 0 for label in labels):
        raise ValueError("all dynamic target labels must be positive and distinct")
    free_keys_bytes = rhs[88 + 2 * nt:rp]
    # All 1034 physical row keys are retained in order; no projected row is used.
    free_keys = list(struct.unpack("<%dQ" % ROWS, free_keys_bytes))
    if max(memoryview(g)[gp:], default=0) >= P:
        raise ValueError("noncanonical field coefficient in complete G cache")
    if any(memoryview(g)[gp + 9 * ROWS * COLS:]):
        raise ValueError("original G has degree at most 8; all cache jets above 8 must vanish")
    if max(memoryview(rhs)[rp:], default=0) >= P:
        raise ValueError("noncanonical field coefficient in complete RHS")
    constants = [j for j, rec in enumerate(records) if rec[1] == 0]
    rows = [records[j][0] - 1 for j in constants]
    if len(constants) != CONSTANTS or len(set(rows)) != CONSTANTS:
        raise ValueError("actual 573 distinct constant-unit pivot columns and rows required")
    cs, rs = set(constants), set(rows)
    restc = [j for j in range(COLS) if j not in cs]
    restr = [i for i in range(ROWS) if i not in rs]
    if (len(restr), len(restc)) != (461, 448):
        raise AssertionError("actual constant prestrip dimensions changed")
    return {
        "g": g, "rhs": rhs, "gp": gp, "rp": rp, "cache_L": cache_L,
        "nt": nt, "L": L, "records": records, "labels": labels,
        "free_keys": free_keys, "free_keys_sha256": sha(free_keys_bytes),
        "constants": constants, "rows": rows, "restc": restc, "restr": restr,
    }


def read_fixed_prefix(path: Path | None, inp, S):
    if path is None:
        return [], None
    data = path.read_bytes()
    header, old_binding = checked_header(data, b"R1503Q31")
    if header != (P, COLS, 197, 10):
        raise ValueError("fixed prefix must be the actual old197 ten-jet source")
    old_nt, old_L = 197, 10
    off = 88 + 2 * old_nt
    stride = 4 + old_L * old_nt
    if len(data) != off + COLS * stride:
        raise ValueError("complete old197 source bytes required")
    old_labels = list(struct.unpack_from("<197H", data, 88))
    if len(set(old_labels)) != old_nt:
        raise ValueError("duplicate labels in old197 fixed source")
    if inp["nt"] != old_nt or set(inp["labels"]) != set(old_labels):
        raise ValueError("fixed prefix must match the complete old197 target-label set")
    old_index = {label: j for j, label in enumerate(old_labels)}
    order = [old_index[label] for label in inp["labels"]]
    raw = [bytearray(COLS * old_nt) for _ in range(PREFIX_LENGTH)]
    for j, rec in enumerate(inp["records"]):
        at = off + j * stride
        if struct.unpack_from("<HBB", data, at) != rec:
            raise ValueError("fixed-prefix source uses different original G metadata")
        body = data[at + 4:at + stride]
        if max(body, default=0) >= P:
            raise ValueError("noncanonical coefficient in old fixed source")
        for k in range(PREFIX_LENGTH):
            raw[k][j * old_nt:(j + 1) * old_nt] = bytes(
                body[k * old_nt + old_col] for old_col in order
            )
    qlow = [S.decode_series(bytes(x), 1, COLS, old_nt)[0] for x in raw]
    return qlow, {
        "sha256": sha(data), "bytes": len(data),
        "old_pipeline_binding": old_binding, "old_precision": old_L,
        "locked_coefficients": PREFIX_LENGTH,
        "old_target_labels": old_labels, "current_target_labels": inp["labels"],
        "column_metadata_matched": True,
    }


def descriptor_matrix(S, directory: Path, desc, rows: int, cols: int):
    matrices = S.get_series(directory, desc)
    if S.dims(matrices) != (1, rows, cols):
        raise ValueError("checkpoint matrix shape mismatch")
    return matrices[0]


def read_json(path: Path):
    return json.loads(path.read_text())


def solve(args, start: float):
    helper_path = args.notes_root / SCHUR
    if sha(helper_path.read_bytes()) != SCHUR_SHA:
        raise ValueError("the exact pinned unit-Schur helper is required")
    S = load_module(helper_path)
    inp = read_inputs(args)
    qlow, prefix_info = read_fixed_prefix(args.fixed_prefix_q, inp, S)
    lock = PREFIX_LENGTH if qlow else 0
    L, nt = inp["L"], inp["nt"]
    work_L = L - lock
    if work_L <= SMITH_MAX:
        raise ValueError("after locking five jets, remaining precision must exceed Smith bound 5")
    script_sha = sha(Path(__file__).read_bytes())
    semantic = {
        "format": FORMAT, "pipeline_binding": args.binding,
        "wrapper_sha256": script_sha, "unit_schur_sha256": SCHUR_SHA,
        "G_sha256": sha(inp["g"]), "G_bytes": len(inp["g"]),
        "rhs_sha256": sha(inp["rhs"]), "rhs_bytes": len(inp["rhs"]),
        "G_cache_precision": inp["cache_L"], "used_precision": L,
        "target_count": nt, "target_labels": inp["labels"],
        "original_row_keys_sha256": inp["free_keys_sha256"],
        "fixed_prefix": prefix_info, "locked_coefficients": lock,
        "solve_precision": work_L, "maximum_Smith_exponent": SMITH_MAX,
        "expected_free_rows": FREE,
    }
    binding = sha(canonical(semantic))
    checkpoint = args.checkpoint_dir or (args.out / "local-solve-checkpoints")
    checkpoint.mkdir(parents=True, exist_ok=True)
    binding_path = checkpoint / "input-binding.json"
    if binding_path.exists():
        old = read_json(binding_path)
        if old.get("binding") != binding or old.get("semantic") != semantic:
            raise ValueError("checkpoint input content, labels, or source code changed")
    S.atomic_write(binding_path, S.canonical_json({"binding": binding, "semantic": semantic}))
    # Paths are audit data only, deliberately absent from the effective binding.
    S.atomic_write(args.out / "local-solve-input-audit.json", S.canonical_json({
        "binding": binding, "semantic": semantic,
        "paths": {"G": str(args.G.resolve()), "rhs": str(args.rhs.resolve()),
                  "fixed_prefix_q": None if args.fixed_prefix_q is None
                  else str(args.fixed_prefix_q.resolve()),
                  "checkpoint": str(checkpoint.resolve()),
                  "helper": str(helper_path.resolve())},
    }))

    reserved = min(30.0, args.remaining_seconds / 4.0)
    deadline = start + args.remaining_seconds - reserved
    cancellation = {"reason": None}
    old_handlers = {}

    class SharedClockSolver(S.SchurSolver):
        def tick(self):
            if cancellation["reason"] is not None:
                raise S.Deadline(cancellation["reason"])
            super().tick()

    solver = SharedClockSolver(checkpoint / "unit-schur", binding, SMITH_MAX, FREE,
                               max(0.000001, deadline - time.monotonic()))
    solver.deadline = deadline

    def request_stop(signum, frame):
        cancellation["reason"] = "external signal %d at shared wall-clock boundary" % signum

    for signame in ("SIGTERM", "SIGINT"):
        if hasattr(signal, signame):
            sig = getattr(signal, signame)
            old_handlers[sig] = signal.signal(sig, request_stop)

    constants, rows = inp["constants"], inp["rows"]
    restc, restr = inp["restc"], inp["restr"]
    g_cache = {}
    zero_g = S.zero(ROWS, COLS)

    def decode_g(k):
        if not 0 <= k < inp["cache_L"]:
            raise ValueError("G coefficient outside complete cache")
        if k >= 9:
            return zero_g
        if k not in g_cache:
            stride = ROWS * COLS
            at = inp["gp"] + k * stride
            Gk = S.decode_series(inp["g"][at:at + stride], 1, ROWS, COLS)[0]
            if k and S.pick(Gk, range(ROWS), constants) != S.zero(ROWS, CONSTANTS):
                raise ValueError("claimed constant G column has a positive jet coefficient")
            g_cache[k] = Gk
        return g_cache[k]

    def decode_rhs(k):
        stride = ROWS * nt
        at = inp["rp"] + k * stride
        return S.decode_series(inp["rhs"][at:at + stride], 1, ROWS, nt)[0]

    def adjusted_rhs(k):
        answer = decode_rhs(k)
        for j in range(max(0, k - 8), min(k, lock - 1) + 1):
            solver.tick()
            answer -= decode_g(k - j) * qlow[j]
        return answer

    def save_receipt(status, **extra):
        result = {
            "format": FORMAT, "status": status, "bindingSHA256": args.binding,
            "helperBindingSHA256": binding, "wrapperSHA256": script_sha,
            "unitSchurSHA256": SCHUR_SHA, "targetCount": nt, "targets": nt,
            "targetLabels": inp["labels"], "TaylorCenter": 1,
            "TaylorPrecision": L, "GCachePrecision": inp["cache_L"],
            "lockedPrefixLength": lock, "solvePrecision": work_L,
            "elapsedSeconds": time.monotonic() - start,
            "sharedRemainingSecondsAtEntry": args.remaining_seconds,
            "saveReserveSeconds": reserved,
            "localSolutionOnly": True, "globalOriginalPolynomialSourceClaimed": False,
            "characteristicZeroIdentityAsserted": False,
            **extra,
        }
        S.atomic_write(args.out / "local-unit-solve-receipt.json", S.canonical_json(result))
        message = dict(result)
        if status == "completed":
            message["status"] = "saturated-local-unit-solve-complete"
        print(json.dumps(message, sort_keys=True), flush=True)
        return result

    try:
        solver.tick()
        # Check every coefficient below the lock before dividing by t**5.
        prefix_check_path = checkpoint / "fixed-prefix-check.json"
        done_low = 0
        if prefix_check_path.exists():
            check = read_json(prefix_check_path)
            if check.get("binding") != binding:
                raise ValueError("fixed-prefix verification checkpoint binding mismatch")
            done_low = check["verified_coefficients"]
            if not isinstance(done_low, int) or not 0 <= done_low <= lock:
                raise ValueError("invalid fixed-prefix checkpoint progress")
        for ell in range(done_low, lock):
            solver.tick()
            residual = adjusted_rhs(ell)
            if residual != S.zero(ROWS, nt):
                desc = S.put_series(checkpoint, "fixed-prefix-invalid-residual", [residual])
                S.atomic_write(checkpoint / "fixed-prefix-inconsistent.json",
                               S.canonical_json({"binding": binding, "coefficient": ell,
                                                 "residual": desc}))
                raise S.LocalInconsistent("old five-jet source does not solve the new low RHS")
            S.atomic_write(prefix_check_path, S.canonical_json({
                "binding": binding, "verified_coefficients": ell + 1,
                "all_original_rows": ROWS, "target_count": nt,
            }))

        prefile = checkpoint / "constant-prestrip.json"
        pre_expected = {
            "binding": binding, "constant_rows": rows, "constant_columns": constants,
            "remaining_rows": restr, "remaining_columns": restc,
            "solve_precision": work_L, "locked_coefficients": lock,
            "target_count": nt,
        }
        if prefile.exists():
            pre = read_json(prefile)
            if any(pre.get(k) != v for k, v in pre_expected.items()):
                raise ValueError("constant-unit checkpoint belongs to another true source")
            Ainv = descriptor_matrix(S, checkpoint, pre["constant_inverse"], CONSTANTS, CONSTANTS)
            C0 = descriptor_matrix(S, checkpoint, pre["constant_C"], 461, CONSTANTS)
            if not isinstance(pre.get("jets"), list) or len(pre["jets"]) > work_L:
                raise ValueError("invalid constant-prestrip checkpoint progress")
        else:
            solver.tick()
            G0 = decode_g(0)
            A0 = S.pick(G0, rows, constants)
            Ainv = A0.inv()
            C0 = S.pick(G0, restr, constants)
            if A0 * Ainv != S.identity(CONSTANTS):
                raise AssertionError("actual 573 by 573 constant-unit inverse failed")
            pre = dict(pre_expected)
            pre["constant_inverse"] = S.put_series(checkpoint, "constant-inverse", [Ainv])
            pre["constant_C"] = S.put_series(checkpoint, "constant-C", [C0])
            pre["jets"] = []
            S.atomic_write(prefile, S.canonical_json(pre))

        # Each completed coefficient is durable; no prefix is replaced by zeros.
        for k in range(len(pre["jets"]), work_L):
            solver.tick()
            Gk, Rk = decode_g(k), adjusted_rhs(k + lock)
            B = S.pick(Gk, rows, restc)
            D = S.pick(Gk, restr, restc)
            U = S.pick(Rk, rows, range(nt))
            V = S.pick(Rk, restr, range(nt))
            solver.tick()
            AB, AU = Ainv * B, Ainv * U
            solver.tick()
            values = {"Gprime": D - C0 * AB, "rhsprime": V - C0 * AU,
                      "AinvB": AB, "AinvRHS": AU}
            jet = {"coefficient": k, "matrices": {
                name: S.put_series(checkpoint, "pre-%02d-%s" % (k, name), [mat])
                for name, mat in values.items()
            }}
            pre["jets"].append(jet)
            S.atomic_write(prefile, S.canonical_json(pre))
            S.emit("saved-constant-prestrip-coefficient", coefficient=k,
                   precision=work_L, targets=nt)
        Gp, Rp, AiB, AiU = [], [], [], []
        for k, jet in enumerate(pre["jets"]):
            if jet.get("coefficient") != k:
                raise ValueError("constant-prestrip coefficient ordering changed")
            desc = jet["matrices"]
            Gp.append(descriptor_matrix(S, checkpoint, desc["Gprime"], 461, 448))
            Rp.append(descriptor_matrix(S, checkpoint, desc["rhsprime"], 461, nt))
            AiB.append(descriptor_matrix(S, checkpoint, desc["AinvB"], CONSTANTS, 448))
            AiU.append(descriptor_matrix(S, checkpoint, desc["AinvRHS"], CONSTANTS, nt))

        verify_file = checkpoint / "complete-G-verification.json"
        if verify_file.exists():
            verified = read_json(verify_file)
            if verified.get("binding") != binding or verified.get("precision") != L:
                raise ValueError("complete source checkpoint binding/precision mismatch")
            descriptions = verified.get("solution")
            if not isinstance(descriptions, list) or len(descriptions) != L:
                raise ValueError("complete source checkpoint must contain every jet")
            q = [descriptor_matrix(S, checkpoint, desc, COLS, nt) for desc in descriptions]
            completed = verified["verified_coefficients"]
            if not isinstance(completed, int) or not 0 <= completed <= L:
                raise ValueError("invalid full original verification progress")
        else:
            qrest = solver.solve(Gp, Rp, row_labels=restr, col_labels=restc)
            qconst = S.series_sub(AiU, S.series_mul(AiB, qrest, work_L, solver.tick))
            q = list(qlow)
            for k in range(work_L):
                solver.tick()
                value = S.zero(COLS, nt)
                for i, j in enumerate(constants):
                    for target in range(nt):
                        value[j, target] = qconst[k][i, target]
                for i, j in enumerate(restc):
                    for target in range(nt):
                        value[j, target] = qrest[k][i, target]
                q.append(value)
            if S.dims(q) != (L, COLS, nt):
                raise AssertionError("full original source was not backfilled at every jet")
            descriptions = []
            for k, value in enumerate(q):
                solver.tick()
                descriptions.append(S.put_series(checkpoint, "actual-q-%02d" % k, [value]))
            verified = {"binding": binding, "precision": L, "solution": descriptions,
                        "verified_coefficients": 0}
            S.atomic_write(verify_file, S.canonical_json(verified))
            completed = 0

        if lock and any(q[k] != qlow[k] for k in range(lock)):
            raise AssertionError("backsubstitution changed a locked old coefficient")
        for ell in range(completed, L):
            solver.tick()
            actual = S.zero(ROWS, nt)
            for k in range(min(ell, 8) + 1):
                solver.tick()
                actual += decode_g(k) * q[ell - k]
            expected = decode_rhs(ell)
            if actual != expected:
                desc = S.put_series(checkpoint, "full-G-invalid-residual", [actual - expected])
                S.atomic_write(checkpoint / "full-G-inconsistent.json",
                               S.canonical_json({"binding": binding, "coefficient": ell,
                                                 "residual": desc}))
                raise AssertionError("full 1034-row original G*q identity failed")
            verified["verified_coefficients"] = ell + 1
            S.atomic_write(verify_file, S.canonical_json(verified))
            S.emit("verified-original-G-coefficient", coefficient=ell,
                   precision=L, rows=ROWS, targets=nt)

        # Output has the original G-column dictionary and the actual target order.
        solver.tick()
        output = bytearray(b"R150SQ31")
        output += struct.pack("<4I", P, COLS, nt, L)
        output += args.binding.encode("ascii")
        output += struct.pack("<%dH" % nt, *inp["labels"])
        for j, record in enumerate(inp["records"]):
            if j % 32 == 0:
                solver.tick()
            output += struct.pack("<HBB", *record)
            for k in range(L):
                output += bytes(int(q[k][j, target]) for target in range(nt))
        data = bytes(output)
        S.atomic_write(args.out / OUTPUT_NAME, data)
        save_receipt("completed", fullOriginalGJetIdentityVerified=True,
                     fullOriginalGIdentityVerified=True,
                     allOriginalGJetCoordinatesVerified=L * ROWS * nt,
                     all13FreeConditionsRetained=True, actualConstantColumns=CONSTANTS,
                     remainingRows=461, remainingColumns=448, maximumSmithExponent=SMITH_MAX,
                     fixedPrefixAllOriginalLowRowsVerified=bool(lock),
                     allLockedSourceCoefficientsRetained=bool(lock),
                     outputFile=OUTPUT_NAME, outputSHA256=sha(data), outputBytes=len(data))
        return 0
    except S.Deadline as exc:
        save_receipt("checkpointed-deadline", fullOriginalGJetIdentityVerified=False,
                     message=str(exc))
        return 75
    except S.LocalInconsistent as exc:
        save_receipt("local-inconsistent", fullOriginalGJetIdentityVerified=False,
                     message=str(exc))
        return 2
    except Exception as exc:
        save_receipt("failed", fullOriginalGJetIdentityVerified=False,
                     exceptionType=type(exc).__name__, message=str(exc))
        raise
    finally:
        for sig, handler in old_handlers.items():
            signal.signal(sig, handler)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--G", type=Path, required=True)
    parser.add_argument("--rhs", type=Path, required=True)
    parser.add_argument("--binding", required=True)
    parser.add_argument("--notes-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--remaining-seconds", type=float, required=True)
    parser.add_argument("--fixed-prefix-q", type=Path)
    parser.add_argument("--checkpoint-dir", type=Path)
    args = parser.parse_args(argv)
    start = time.monotonic()
    hex_binding(args.binding)
    if not math.isfinite(args.remaining_seconds) or args.remaining_seconds <= 0:
        raise ValueError("remaining-seconds must be finite and strictly positive")
    args.out.mkdir(parents=True, exist_ok=True)
    return solve(args, start)


if __name__ == "__main__":
    raise SystemExit(main())
