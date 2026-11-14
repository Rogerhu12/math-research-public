#!/usr/bin/env python3
"""Exact rational combination for the conditional alpha-only height lemma.

This checks the ledger only; the reviewed alpha/source enclosure is an input.
It does not certify the numerical height sampler's other error contributions.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=Path,
                        default=Path("notes/2026-11-09-db6f-tail-tight-alpha.json"))
    parser.add_argument("--helper", type=Path,
                        default=Path("scripts/db6f-tail-sample-background-height.mjs"))
    parser.add_argument("--proof", type=Path,
                        default=Path("notes/2026-11-09-db6f-tail-height-alpha-transfer.md"))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError("refusing to replace an existing ledger")
    if sha(args.alpha) != "04aae85c19f78fd82808ac32b104537dbb584c39cac8a648107722c855685c62":
        raise ValueError("requires the reviewed fixed-background alpha input")
    if sha(args.helper) != "106061533820a1639387b33b535408d312ade7a8337d59ed8c2b48ec80bc08a4":
        raise ValueError("requires the frozen height sampler")
    data = json.loads(args.alpha.read_text())
    lo, hi = map(F.from_float, data["exactRadialAlpha"])
    mid = F.from_float(data["savedNumericalAlpha"])
    b_upper = F.from_float(data["totalB"][1])
    gap = max(mid - lo, hi - mid)
    height = F(16, 15) * b_upper * gap
    if not (lo <= mid <= hi and b_upper > 0 and
            gap < F(2372, 10**14) and height < F(456, 10**16)):
        raise ValueError("the exact rational gates failed")

    def pack(value):
        return {"numerator": str(value.numerator),
                "denominator": str(value.denominator)}

    report = {
        "status": "conditional-alpha-only-height-transfer-exact-rational-ledger-pending-review",
        "inputs": {str(p): {"sha256": sha(p), "bytes": p.stat().st_size}
                   for p in [args.alpha, args.helper, args.proof]},
        "BUpperExact": pack(b_upper),
        "alphaGapUpperExactFromDisplayedEndpoints": pack(gap),
        "heightDifferenceUpperExact": pack(height),
        "strictThresholdExact": pack(F(456, 10**16)),
        "thresholdPassed": True,
        "heightDifferenceUpperDiagnostic": float(height),
        "scope": "Only exact-source height change from alpha representative, with cut anchored and cuff constant extension. Finite numerical quadrature/inverse/source evaluation/rounding errors are not certified.",
    }
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"thresholdPassed": True,
                      "heightDifferenceUpperDiagnostic": float(height),
                      "outputSHA256": sha(args.out)}))


if __name__ == "__main__":
    main()
