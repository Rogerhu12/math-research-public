#!/usr/bin/env python3
"""Read-only selected original infinity minor from the already paid jet DAG.

No original normal form or whole infinity jet is recomputed. The saved P
coefficients are retained, so the cokernel is that of the selected constant
image even when its rank is smaller than 1007.
"""
import argparse
import gzip
import hashlib
import json
import struct
import sys
import time
import traceback
from pathlib import Path
sys.dont_write_bytecode = True

EXPECTED = {
    "graded": (90567, "d5c1a753a3869a702a84d723a4fb7b68c778e19e2fc7d0a4e4b55fe95327a0b9"),
    "core": (20633, "95bfdf3fdbfd5146ae84557fbe73b6538b5e0291266d373013031f0c54b8dc8d"),
    "receipt": (72072, "d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e"),
    "operations": (4706546, "bfcc10520abedfab362b91adc6414481660d4a951aae0d7dfd13da3efba4e3ec"),
}
RAW_OPS_BYTES = 8548344
RAW_OPS_SHA = "d2555a117c9f79db448e8eb183d5420952fe001707f5ca81e20e98705b83a3ad"
P = 31

def sha(b):
    return hashlib.sha256(b).hexdigest()

def matrix_bytes(M):
    return bytes(int(x) for x in M.entries())

def pivots_of_rref(M, rank):
    result = []
    last = -1
    for i in range(rank):
        j = next((j for j in range(last + 1, M.ncols()) if M[i, j]), None)
        if j is None or int(M[i, j]) != 1:
            raise ValueError("invalid RREF source pivot")
        if any(M[i, k] for k in range(j)):
            raise ValueError("RREF pivot not leading")
        result.append(j)
        last = j
    if any(M[i, j] for i in range(rank, M.nrows()) for j in range(M.ncols())):
        raise ValueError("nonzero RREF row below rank")
    return result

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--graded-profile", type=Path, required=True)
    a.add_argument("--core-profile", type=Path, required=True)
    a.add_argument("--paid-receipt", type=Path, required=True)
    a.add_argument("--paid-operations", type=Path, required=True)
    a.add_argument("--out", type=Path, required=True)
    a.add_argument("--seconds", type=float, default=10)
    args = a.parse_args()
    if not 0 < args.seconds <= 60:
        raise ValueError("explicit small positive time budget")
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    receipt_path = out / "selected-infinity-minor-dag-receipt.json"
    rec = {
        "format": "r150-selected-infinity-minor-paid-dag-v1",
        "status": "running",
        "field": 31,
        "secondsLimit": args.seconds,
        "oldNormalFormsRecomputed": False,
        "oldFullInfinityJetRecomputed": False,
        "sameOriginalHomogeneousMinorDegree": 8770,
        "leadingCoefficientUnitProved": False,
        "completeInfinitySmithLengthComputed": False,
        "files": {},
        "stages": [],
    }
    def save():
        rec["elapsedSeconds"] = time.monotonic() - started
        receipt_path.write_text(json.dumps(rec, indent=2) + "\n")
    def tick(stage):
        elapsed = time.monotonic() - started
        rec["stages"].append({"stage": stage, "elapsedSeconds": elapsed})
        save()
        print(json.dumps({"stage": stage, "elapsedSeconds": elapsed}), flush=True)
        if elapsed >= args.seconds:
            raise TimeoutError("explicit mathematical deadline reached")
    def payload(name, rows, cols, values):
        body = bytes(values)
        if len(body) != rows * cols or any(x >= 31 for x in body):
            raise ValueError("matrix payload shape or residue")
        raw = b"R150DM31" + struct.pack("<III", 31, rows, cols) + body
        filename = name + (".bin.gz" if len(raw) > 1_000_000 else ".bin")
        data = gzip.compress(raw, compresslevel=1, mtime=0) if len(raw) > 1_000_000 else raw
        if len(data) > 4_500_000:
            raise ValueError("small matrix output exceeds 4,500,000 bytes")
        (out / filename).write_bytes(data)
        rec["files"][name] = {
            "file": filename, "rows": rows, "columns": cols,
            "bytes": len(data), "sha256": sha(data),
            "uncompressedBytes": len(raw), "uncompressedSHA256": sha(raw),
            "layout": "R150DM31/u32(field,rows,cols)/row-major uint8",
        }
    try:
        from flint import nmod_mat
        import flint
        rec["pythonFlintVersion"] = flint.__version__
        files = {
            "graded": args.graded_profile, "core": args.core_profile,
            "receipt": args.paid_receipt, "operations": args.paid_operations,
        }
        blobs = {}
        rec["inputs"] = {}
        for key, path in files.items():
            data = path.read_bytes()
            if (len(data), sha(data)) != EXPECTED[key]:
                raise ValueError("frozen paid input changed: " + key)
            blobs[key] = data
            rec["inputs"][key] = {"bytes": len(data), "sha256": sha(data), "path": str(path)}
        own = Path(__file__).read_bytes()
        rec["sourceSHA256"] = sha(own)
        rec["semanticBinding"] = sha(json.dumps({
            "format": rec["format"], "inputs": EXPECTED, "sourceSHA256": sha(own)
        }, sort_keys=True, separators=(",", ":")).encode())
        graded = json.loads(blobs["graded"])
        core = json.loads(blobs["core"])
        paid = json.loads(blobs["receipt"])
        if paid["status"] != "completed":
            raise ValueError("paid full infinity run was incomplete")
        summary = paid["summary"]
        if (summary["field"], summary["components"], summary["sources"],
            summary["constantRank"], summary["connectingRank"]) != (31, 1034, 2855, 1007, 4):
            raise ValueError("paid full infinity dimensions")
        var = [8 ** i for i in range(11)]
        mon = [[] for _ in range(6)]
        def enumerate_monomials(left, lo, key, result):
            if not left:
                result.append(key)
                return
            for i in range(lo, 11):
                enumerate_monomials(left - 1, i, key + var[i], result)
        for d in range(6):
            enumerate_monomials(d, 0, 0, mon[d])
        multipliers = sum(mon[:4], [])
        multiplier_index = {key: i for i, key in enumerate(multipliers)}
        rows = [(int(e), int(k), int(c), 17 * multiplier_index[k] + int(e) + 1)
                for e, k, c in graded["selectedRows"]]
        if len(rows) != 4191:
            raise ValueError("old homogeneous original profile")
        pre = [r for r in rows if r[0] < 11]
        if len(pre) != 3333:
            raise ValueError("same constant original N prebasis")
        for r in core["extraRows"]:
            row = (r["generator"], r["multiplierKey"], r["pivotKey"], r["originalRow"])
            if row[3] != 17 * multiplier_index[row[1]] + row[0] + 1:
                raise ValueError("extra row original source identity")
            rows.append(row)
        if len(rows) != 4354 or len({r[3] for r in rows}) != 4354 or len({r[2] for r in rows}) != 4354:
            raise ValueError("same selected full original minor")
        pre_raw = {r[3] for r in pre}
        pre_columns = {r[2] for r in pre}
        selected_raw = [r[3] for r in rows if r[3] not in pre_raw]
        selected_keys = [r[2] for r in rows if r[2] not in pre_columns]
        components = [key for d in range(5, 0, -1) for key in mon[d] if key not in pre_columns]
        component_index = {key: i + 1 for i, key in enumerate(components)}
        selected_columns = [component_index[key] for key in selected_keys]
        if len(selected_raw) != 1021 or len(selected_keys) != 1021 or len(components) != 1034:
            raise ValueError("selected Schur dictionary")
        const_list = summary["constantPivots"]
        conn_list = summary["connectingPivots"]
        const_map = {int(row[0]): i for i, row in enumerate(const_list)}
        conn_map = {int(row[0]): i for i, row in enumerate(conn_list)}
        const_receipt = {int(row[0]): row for row in const_list}
        conn_receipt = {int(row[0]): row for row in conn_list}
        if len(const_map) != 1007 or len(conn_map) != 4:
            raise ValueError("distinct paid pivots")
        if not set(const_map).isdisjoint(conn_map):
            raise ValueError("constant and connecting pivots overlap")
        if not (set(const_map) | set(conn_map)) <= set(selected_columns):
            raise ValueError("selected outputs do not contain the complete paid two-layer pivot set")
        rec["selectedSourceRows"] = selected_raw
        rec["selectedOutputComponents"] = selected_columns
        rec["selectedOutputMonomialKeys"] = selected_keys
        rec["excluded13OutputComponents"] = sorted(set(range(1, 1035)) - set(selected_columns))
        rec["paidConstantPivotComponents"] = list(const_map)
        rec["paidConnectingPivotComponents"] = list(conn_map)
        rec["outputRestrictionInjectiveOnPaidFirstImage"] = True
        rec["selectedOriginalMinorRetained"] = True
        tick("paid-input-and-original-minor-identities")

        data = gzip.decompress(blobs["operations"])
        if len(data) != RAW_OPS_BYTES or sha(data) != RAW_OPS_SHA:
            raise ValueError("paid DAG decompressed bytes changed")
        if data[:8] != b"R150IJ31" or struct.unpack_from("<II", data, 8) != (2855, 1034):
            raise ValueError("paid DAG header")
        pos = 16
        def word():
            nonlocal pos
            if pos + 2 > len(data):
                raise ValueError("truncated paid DAG word")
            z = data[pos] | (data[pos+1] << 8)
            pos += 2
            return z
        def value():
            nonlocal pos
            if pos >= len(data):
                raise ValueError("truncated paid DAG value")
            z = data[pos]
            pos += 1
            if not 1 <= z < 31:
                raise ValueError("noncanonical nonzero paid factor")
            return z
        selected_index = {raw: i for i, raw in enumerate(selected_raw)}
        C = bytearray(1021 * 1007)
        E = bytearray(1021 * 1011)
        originals = [raw for raw in range(1, 6189) if raw not in pre_raw]
        zero_rows = []
        seen_const = set()
        seen_conn = set()
        reductions = projections = conn_reductions = 0
        for idx, raw in enumerate(originals, 1):
            if data[pos] != ord("I"):
                raise ValueError("paid source record boundary")
            pos += 1
            if (word(), word()) != (idx, raw):
                raise ValueError("paid full original source ordering")
            outrow = selected_index.get(raw)
            while True:
                op = data[pos]
                pos += 1
                if op == ord("R"):
                    c, a = word(), value()
                    if c not in seen_const:
                        raise ValueError("constant reduction references unavailable original basis")
                    reductions += 1
                    if outrow is not None:
                        p = outrow * 1007 + const_map[c]
                        C[p] = (C[p] + a) % 31
                elif op == ord("B"):
                    c = word()
                    if c in seen_const or c not in const_receipt:
                        raise ValueError("paid constant basis identity")
                    if const_receipt[c][1:3] != [idx, raw]:
                        raise ValueError("constant original source witness differs")
                    seen_const.add(c)
                    if outrow is not None:
                        p = outrow * 1007 + const_map[c]
                        C[p] = (C[p] + 1) % 31
                    break
                elif op == ord("Z"):
                    zero_rows.append((idx, raw))
                    break
                else:
                    raise ValueError("invalid constant paid DAG opcode")
        if len(seen_const) != 1007 or len(zero_rows) != 1848:
            raise ValueError("paid constant source partition")
        for idx, raw in zero_rows:
            if data[pos] != ord("J"):
                raise ValueError("paid connecting source boundary")
            pos += 1
            if (word(), word()) != (idx, raw):
                raise ValueError("paid complete kernel source ordering")
            outrow = selected_index.get(raw)
            while True:
                op = data[pos]
                pos += 1
                if op == ord("P"):
                    c, a = word(), value()
                    if c not in seen_const:
                        raise ValueError("paid P coordinate missing constant basis")
                    projections += 1
                    if outrow is not None:
                        p = outrow * 1011 + const_map[c]
                        E[p] = (E[p] + a) % 31
                elif op == ord("Q"):
                    c, a = word(), value()
                    if c not in seen_conn:
                        raise ValueError("paid Q coordinate missing connecting basis")
                    conn_reductions += 1
                    if outrow is not None:
                        p = outrow * 1011 + 1007 + conn_map[c]
                        E[p] = (E[p] + a) % 31
                elif op == ord("C"):
                    c = word()
                    if c in seen_conn or c not in conn_receipt:
                        raise ValueError("paid connecting basis identity")
                    if conn_receipt[c][1:3] != [idx, raw]:
                        raise ValueError("connecting original source witness differs")
                    seen_conn.add(c)
                    if outrow is not None:
                        p = outrow * 1011 + 1007 + conn_map[c]
                        E[p] = (E[p] + 1) % 31
                    break
                elif op == ord("0"):
                    break
                else:
                    raise ValueError("invalid connecting paid DAG opcode")
        if pos != len(data) or len(seen_conn) != 4:
            raise ValueError("paid DAG complete tail")
        if (reductions, projections, conn_reductions) != (
            summary["constantReductions"], summary["cokernelProjections"], summary["connectingReductions"]):
            raise ValueError("paid operation counts changed")
        rec["paidOperationCounts"] = {
            "constantReductions": reductions, "fullConstantProjections": projections,
            "connectingReductions": conn_reductions,
        }
        rec["allPaidTraceEventsVerified"] = True
        rec["allOriginalSourceIdentitiesVerified"] = True
        payload("selected-constant-in-paid-basis", 1021, 1007, C)
        payload("selected-first-adjusted-in-paid-basis", 1021, 1011, E)
        tick("all-paid-dag-records-reconstructed")

        Cmat = nmod_mat(1021, 1007, list(C), 31)
        Emat = nmod_mat(1021, 1011, list(E), 31)
        rr, r0 = Cmat.transpose().rref()
        independent = pivots_of_rref(rr, r0)
        free = [j for j in range(1021) if j not in set(independent)]
        h = len(free)
        K = nmod_mat(h, 1021, 31)
        for i, f in enumerate(free):
            K[i, f] = 1
            for k, p in enumerate(independent):
                K[i, p] = -rr[k, f]
        if K * Cmat != nmod_mat(h, 1007, 31):
            raise ValueError("selected full constant kernel identity failed")
        Bflat = []
        for i in independent:
            Bflat.extend(C[i * 1007:(i+1) * 1007])
            Bflat.extend([0] * 4)
        Bconst = nmod_mat(r0, 1011, Bflat, 31)
        br, brank = Bconst.rref()
        if brank != r0:
            raise ValueError("selected source basis rank")
        cp = pivots_of_rref(br, r0)
        D = K * Emat
        Dcoeff = nmod_mat(h, r0, [int(D[i, j]) for i in range(h) for j in cp], 31)
        residual = D - Dcoeff * br
        if any(residual[i, j] for i in range(h) for j in cp):
            raise ValueError("selected image was not exactly quotiented")
        r1 = residual.rank()
        if not 0 <= r1 <= h:
            raise ValueError("selected connecting rank")
        fullstack = nmod_mat(r0+h, 1011, Bflat + [int(x) for x in D.entries()], 31)
        if fullstack.rank() != r0 + r1:
            raise ValueError("independent connecting rank identity")
        payload("selected-constant-source-kernel", h, 1021, matrix_bytes(K))
        payload("selected-connecting-before-quotient", h, 1011, matrix_bytes(D))
        payload("selected-connecting-after-selected-quotient", h, 1011, matrix_bytes(residual))
        rec.update({
            "selectedConstantRank": r0,
            "selectedFullConstantRankModulo31": 3333 + r0,
            "selectedConnectingRank": r1,
            "selectedMod31SchurSize": h,
            "selectedExactlySimpleSmithFactorsModulo31": r1,
            "selectedSmithFactorsOfOrderAtLeastTwoModulo31": h-r1,
            "selectedDeterminantInfinityOrderLowerBoundModulo31": 2*h-r1,
            "independentSelectedSourceIndicesZeroBased": independent,
            "independentSelectedOriginalRows": [selected_raw[i] for i in independent],
            "selectedConstantKernelFreeSourceIndicesZeroBased": free,
            "selectedConstantKernelFreeOriginalRows": [selected_raw[i] for i in free],
            "selectedConstantCoordinatePivotColumnsZeroBased": cp,
            "allConstantKernelRowsVerified": True,
            "onlySelectedConstantImageQuotiented": True,
            "char0SelectedConstantRankProved": r0 == 1007,
            "char0SelectedFullConstantRank": 4340 if r0 == 1007 else None,
            "char0SelectedFullConstantRankBounds": [3333+r0, 4340],
            "char0DvrSchurSize": 14 if r0 == 1007 else None,
            "char0UpperBoundSource": "R150-appendix-rank-one-physical-mean-at-infinity-full-critical-emptiness.md",
        })
        if r0 == 1007:
            square = nmod_mat(1007, 1007,
                [int(Cmat[i, j]) for i in independent for j in range(1007)], 31)
            coordinate_det = int(square.det())
            echelon_det = 1
            for row in const_list:
                echelon_det = echelon_det * int(row[3]) % 31
            value_det = coordinate_det * echelon_det % 31
            if not value_det:
                raise ValueError("actual selected constant minor is not a unit")
            rec["actualSelectedSchurUnitMinor"] = {
                "originalRows": [selected_raw[i] for i in independent],
                "outputComponents": list(const_map),
                "outputMonomialKeys": [components[c-1] for c in const_map],
                "coordinateDeterminantModulo31": coordinate_det,
                "paidEchelonDeterminantModulo31": echelon_det,
                "actualSchurMinorDeterminantModulo31": value_det,
                "remainingOriginalRows": [selected_raw[i] for i in free],
                "remainingOutputComponents": [c for c in selected_columns if c not in const_map],
                "source": "same selected 4354 minor after its original 3333 constant N block",
            }
        tick("selected-constant-kernel-and-true-connection-complete")
        rec["status"] = "completed"
        rec["nativeStatus"] = "selected-infinity-minor-dag-complete"
        save()
        print(json.dumps({k: rec[k] for k in (
            "status", "nativeStatus", "selectedConstantRank", "selectedConnectingRank",
            "selectedMod31SchurSize", "char0SelectedConstantRankProved",
            "selectedDeterminantInfinityOrderLowerBoundModulo31", "elapsedSeconds"
        )}), flush=True)
    except BaseException as exc:
        rec["status"] = "checkpointed-time-budget" if isinstance(exc, TimeoutError) else "failed"
        rec["error"] = repr(exc)
        rec["traceback"] = traceback.format_exc()
        save()
        raise

if __name__ == "__main__":
    main()
