#!/usr/bin/env python3
"""Nine exact vector minimal polynomials in the whole original torsion space.

Uses complete vector Krylov matrices; no scalar projection or point sampling.
Run under an explicit external time/address-space cap.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import hashlib
import time

import flint
from flint import nmod_mat, nmod_poly


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--state-receipt", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    before = time.monotonic()
    helper_path = Path(__file__).with_name("2026-11-14-r150-torsion-characteristic-789f.py")
    spec = importlib.util.spec_from_file_location("r150_torsion_characteristic", helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    receipt = json.loads(args.state_receipt.read_text())
    if (receipt["status"] != "completed"
            or receipt["outputs"]["state.bin"]["sha256"] != helper.digest(args.state)
            or not receipt["nativeStatistics"]["allTargetsInTorsion"]):
        raise ValueError("not a complete original torsion state")
    state = helper.load_state(args.state)
    d = state["torsionDimension"]
    action = nmod_mat(state["matrices"]["action"], 31)
    results = []
    common = nmod_poly([1], 31)
    for target_number, coordinates in enumerate(state["matrices"]["targetCoordinates"], 2):
        vector = nmod_mat([[a] for a in coordinates], 31)
        columns = []
        for k in range(d + 1):
            columns.append([int(vector[j, 0]) for j in range(d)])
            if k < d:
                vector = action * vector
        krylov = nmod_mat([[columns[k][row] for k in range(d + 1)] for row in range(d)], 31)
        reduced, rank = krylov.rref()
        pivots = []
        for row in range(rank):
            pivot = next((j for j in range(d + 1) if int(reduced[row, j])), None)
            pivots.append(pivot)
        if pivots != list(range(rank)):
            raise ValueError("Krylov pivots are not the initial independent orbit segment")
        coefficients = [(-int(reduced[row, rank])) % 31 for row in range(rank)] + [1]
        polynomial = nmod_poly(coefficients, 31)
        padded = coefficients + [0] * (d + 1 - len(coefficients))
        residual = krylov * nmod_mat([[a] for a in padded], 31)
        if any(int(residual[j, 0]) for j in range(d)):
            raise ValueError("full vector annihilator relation failed")
        common = (common // common.gcd(polynomial)) * polynomial
        item = {"target": target_number, "degree": rank, "coefficientsAscending": coefficients,
                **helper.factored(polynomial), "krylovColumns": d + 1, "krylovRank": rank,
                "independentInitialColumns": pivots, "fullVectorRelationZero": True,
                "krylovColumnMajorSHA256": hashlib.sha256(bytes(a for col in columns for a in col)).hexdigest()}
        results.append(item)
        print(json.dumps({"phase": "target-minimum", "target": target_number, "degree": rank,
                          "factors": item["factors"], "elapsedSeconds": time.monotonic() - before}), flush=True)
    result = {"format": "r150-original-nine-vector-minimum-annihilators-v1", "status": "completed", "field": 31,
              "stateSHA256": helper.digest(args.state), "stateReceiptSHA256": helper.digest(args.state_receipt),
              "sourceSHA256": helper.digest(__file__), "readerSourceSHA256": helper.digest(helper_path),
              "pythonFlintVersion": flint.__version__, "flintVersion": flint.__FLINT_VERSION__,
              "torsionDimension": d, "targets": results,
              "commonMinimum": {"degree": common.degree(), "coefficientsAscending": helper.coefficients(common),
                                **helper.factored(common)}, "elapsedSeconds": time.monotonic() - before,
              "sourceIdentity": "The full vectors are the nine original target normal forms in the saved W basis. Every recurrence follows AK=KJ and CK=0, and all state multiplication and target normal-form reductions have saved original GB source operations. Krylov rank proves minimality; no scalar projection is used."}
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "completed", "degrees": [r["degree"] for r in results],
                      "commonDegree": common.degree(), "commonFactors": result["commonMinimum"]["factors"],
                      "elapsedSeconds": result["elapsedSeconds"]}))


if __name__ == "__main__":
    main()
