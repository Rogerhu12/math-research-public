#!/usr/bin/env python3
"""Exact source-only closure of the thirteen paid infinity kernel columns.

No multiplication by the original 4367-row operator is performed.  The input
certificates already carry that identity.  This script verifies only source
support, multiplier degrees, two small finite-field rank witnesses, and nine
exact identities between the complete 6188-entry source columns.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import time
from pathlib import Path

P = 31
EXPECTED_CERT_SHA = "fbd6089ccf043af574e5c6c58c654e259732782c4a36d40af0ba8a7352078758"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def independent_rows(rows):
    basis = {}
    row_ids = []
    for label, vector in rows:
        v = list(vector)
        for k, w in basis.items():
            a = v[k]
            if a:
                v = [(x - a * y) % P for x, y in zip(v, w)]
        k = next((i for i, x in enumerate(v) if x), None)
        if k is not None:
            inv = pow(v[k], -1, P)
            basis[k] = [x * inv % P for x in v]
            row_ids.append(label)
    return row_ids, list(basis)


def det_mod(matrix):
    a = [list(r) for r in matrix]
    n = len(a)
    det = 1
    for k in range(n):
        j = next((j for j in range(k, n) if a[j][k]), None)
        if j is None:
            return 0
        if j != k:
            a[j], a[k] = a[k], a[j]
            det = -det
        z = a[k][k]
        det = det * z % P
        inv = pow(z, -1, P)
        for i in range(k + 1, n):
            c = a[i][k] * inv % P
            if c:
                for j in range(k, n):
                    a[i][j] = (a[i][j] - c * a[k][j]) % P
    return det % P


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificates", required=True)
    ap.add_argument("--selected-model", required=True)
    ap.add_argument("--native-model", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    started = time.monotonic()
    paths = {k: Path(v) for k, v in vars(args).items() if k != "out"}
    raw = {k: p.read_bytes() for k, p in paths.items()}
    assert sha(raw["certificates"]) == EXPECTED_CERT_SHA
    cert = json.loads(gzip.decompress(raw["certificates"]))
    model = json.loads(raw["selected_model"])
    tokens = raw["native_model"].decode().split()
    assert tokens[0] == "R150_NATIVE_NF_V1"
    start = 1 + 11 * (66 + 11 * 11)
    assert int(tokens[start]) == 3333
    pre = [list(map(int, tokens[start + 1 + 4*j:start + 5 + 4*j]))
           for j in range(3333)]
    selected = set(model["selectedSourceRows"]) | {r[3] for r in pre}
    assert len(model["selectedSourceRows"]) == 1021 and len(selected) == 4354
    mon = [v for d in range(4)
           for v in itertools.combinations_with_replacement(range(11), d)]
    mi = {v: i for i, v in enumerate(mon)}
    assert len(mon) * 17 == 6188
    for equation, key, _, source in pre:
        assert source == 17 * mi[tuple(i for i in range(11)
                                      for _ in range((key // (8**i)) % 8))] + equation + 1
    paid = cert["certificates"]
    assert cert["kernelCount"] == len(paid) == 13
    assert all(c["all4367ExactIntegerProductsZero"] for c in paid)
    nums = [[int(v) for v in c["originalIntegerSourceNumerators"]] for c in paid]
    den = [int(c["commonDenominator"]) for c in paid]
    assert all(len(c) == 6188 for c in nums)
    assert all(x > 0 and x % P for x in den)
    free = cert["normalizedFreeOriginalSourceRows"]
    assert len(free) == len(set(free)) == 36
    slots = [c["slot"] for c in paid]
    for j, c in enumerate(nums):
        assert all(not x or r+1 in selected for r, x in enumerate(c))
        assert all(c[r-1] == (den[j] if k == slots[j] else 0)
                   for k, r in enumerate(free))
    degrees = [max(len(mon[r//17]) for r, x in enumerate(c) if x) for c in nums]
    assert degrees == [2, 2, 2, 2] + [3] * 9
    cols_mod = [[x * pow(de, -1, P) % P for x in c]
                for c, de in zip(nums, den)]
    top = 17 * (1 + 11 + 66)
    tr, tc = independent_rows((r+1, [c[r] for c in cols_mod])
                             for r in range(top, 6188))
    tm = [[cols_mod[j][r-1] for j in tc] for r in tr]
    assert len(tr) == 9 and det_mod(tm)
    common = math.lcm(*den)
    all_common = [[x * (common // de) for x in c] for c, de in zip(nums, den)]
    shifts = []
    for j in range(4):
        for variable in range(11):
            v = [0] * 6188
            for r, x in enumerate(all_common[j]):
                if x:
                    new_mon = tuple(sorted(mon[r//17] + (variable,)))
                    target = 17 * mi[new_mon] + r % 17
                    v[target] += x
            shifts.append(v)
    invcommon = pow(common, -1, P)
    smod = [[x * invcommon % P for x in c] for c in shifts]
    outside = [r for r in range(6188) if r+1 not in selected]
    good = [j for j, c in enumerate(shifts) if all(c[r] == 0 for r in outside)]
    assert good == [0, 1, 2, 11, 12, 13, 22, 23, 24]
    br, bc = independent_rows((r+1, [c[r] for c in smod]) for r in outside)
    bm = [[smod[j][r-1] for j in bc] for r in br]
    assert len(br) == 35 and det_mod(bm)
    assert set(bc) == set(range(44)) - set(good)
    identities = []
    for j in good:
        v = shifts[j]
        coefficients = [v[free[slot]-1] for slot in slots]
        for r in range(6188):
            assert common * v[r] == sum(a * c[r] for a, c in zip(coefficients, all_common))
        coeff = []
        for a in coefficients:
            g = math.gcd(a, common)
            coeff.append([str(a // g), str(common // g)])
        identities.append({"shiftIndexZeroBased": j,
                           "baseSlot": slots[j//11], "variableOneBased": j%11+1,
                           "coefficientsInPaidThirteen": coeff,
                           "all6188SourceCoefficientsExactlyEqual": True})
    output = {
        "format": "R150_PAID13_SOURCE_DEGREE_AND_LINEAR_SHIFT_CLOSURE_V1",
        "status": "completed",
        "inputs": {k: {"path": str(paths[k]), "bytes": len(v), "sha256": sha(v)}
                   for k, v in raw.items()},
        "sourceIndexRule": "raw=17*multIndex+equation+1; degree0..3 lex combinations_with_replacement(0..10)",
        "selectedOriginalSourceCount": 4354,
        "paidSlots": slots,
        "allOriginal6188SupportChecksPassed": True,
        "all36FreeCoordinatesExactIdentity": True,
        "sourceMultiplierDegrees": degrees,
        "topDegreeThreeRank": 9,
        "topDegreeThreeMod31Minor": {"originalRows": tr, "paidColumnIndicesZeroBased": tc,
                                        "matrix": tm, "determinant": det_mod(tm)},
        "completeDegreeAtMostTwoSubspacePaidSlots": slots[:4],
        "linearShiftCount": 44,
        "selectedSupportShiftIndicesZeroBased": good,
        "outsideSelectedRank": 35,
        "outsideSelectedMod31Minor": {"originalRows": br, "shiftColumnIndicesZeroBased": bc,
                                         "matrix": bm, "determinant": det_mod(bm)},
        "exactSelectedSupportShiftIdentities": identities,
        "resultingSelectedSupportSpanDimension": 13,
        "noOriginalOperatorMultiplicationPerformed": True,
        "conclusionScope": "Only the paid thirteen-dimensional rational kernel span and all one-variable multiples of its complete multiplier-degree-at-most-two subspace; no conclusion about the other 23 normalized square-kernel directions.",
        "elapsedSeconds": time.monotonic() - started,
    }
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(output, ensure_ascii=False, indent=2) + "\n").encode()
    (out / "infinity-paid13-source-shift-closure-receipt-789f.json").write_bytes(data)
    print(json.dumps({"status": "completed", "topRank": 9, "outsideRank": 35,
                      "completeSelectedSupportSpanDimension": 13,
                      "exactSourceIdentities": 9, "receiptSHA256": sha(data),
                      "elapsedSeconds": output["elapsedSeconds"]}))


if __name__ == "__main__":
    main()
