#!/usr/bin/env python3
"""Exact characteristic polynomial of the entire certified F31 torsion space.

Run under an external explicit time/address-space cap. The whole-space
characteristic polynomial is the affine maximal-minor gcd, up to a unit.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import struct
import time

import flint
from flint import nmod_mat


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_state(path):
    data = Path(path).read_bytes()
    if data[:8] != b"R150FW31":
        raise ValueError("state binary magic")
    q, degree, n, nf, dim, nt, observed, stable = struct.unpack_from("<8I", data, 8)
    if (q, degree, n, nf, nt) != (1034, 8, 820, 13, 9) or dim + observed != n:
        raise ValueError("state dimensions")
    offset = 40
    coordinates = []
    for _ in range(n):
        component, exponent = struct.unpack_from("<HB", data, offset)
        offset += 3
        coordinates.append([component, exponent])
    free_components = list(struct.unpack_from(f"<{nf}H", data, offset))
    offset += 2 * nf
    matrices = {}
    for name, rows, cols in [("A", n, n), ("C", nf, n), ("targets", nt, n),
                              ("kernelTranspose", dim, n), ("action", dim, dim),
                              ("targetCoordinates", nt, dim)]:
        count = rows * cols
        block = data[offset:offset + count]
        offset += count
        if len(block) != count or any(a >= 31 for a in block):
            raise ValueError("noncanonical or truncated matrix")
        matrices[name] = [list(block[j * cols:(j + 1) * cols]) for j in range(rows)]
    pivots, echelon = [], []
    for _ in range(observed):
        pivots.append(struct.unpack_from("<H", data, offset)[0])
        offset += 2
        echelon.append(list(data[offset:offset + n]))
        offset += n
    selected = []
    for _ in range(observed):
        selected.append(list(struct.unpack_from("<HH", data, offset)))
        offset += 4
    if offset != len(data):
        raise ValueError("trailing or truncated state data")
    return {"components": q, "maximumBasisDegree": degree, "stateDimension": n,
            "leakageDimension": nf, "torsionDimension": dim,
            "observabilityRank": observed, "stableAtPower": stable,
            "coordinates": coordinates, "freeComponents": free_components,
            "matrices": matrices, "pivotStateCoordinates": pivots,
            "observabilityEchelon": echelon, "selectedObservations": selected}


def coefficients(poly):
    return [int(poly[i]) for i in range(poly.degree() + 1)]


def factored(poly):
    unit, factors = poly.factor()
    return {"unit": int(unit), "factors": [{"coefficientsAscending": coefficients(p),
                                             "exponent": e, "degree": p.degree()}
                                            for p, e in factors]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    before = time.monotonic()
    receipt = json.loads(args.receipt.read_text())
    if (receipt["status"] != "completed"
            or receipt["outputs"]["state.bin"]["sha256"] != digest(args.state)
            or not receipt["nativeStatistics"]["allTargetsInTorsion"]):
        raise ValueError("not a completed whole torsion state")
    state = load_state(args.state)
    action = nmod_mat(state["matrices"]["action"], 31)
    characteristic = action.charpoly()
    minimum = action.minpoly()
    result = {"format": "r150-whole-torsion-characteristic-v1", "status": "completed", "field": 31,
              "stateSHA256": digest(args.state), "stateReceiptSHA256": digest(args.receipt),
              "sourceSHA256": digest(__file__), "pythonFlintVersion": flint.__version__,
              "flintVersion": flint.__FLINT_VERSION__, "torsionDimension": state["torsionDimension"],
              "observabilityRank": state["observabilityRank"], "stableAtPower": state["stableAtPower"],
              "characteristic": {"degree": characteristic.degree(),
                                 "coefficientsAscending": coefficients(characteristic),
                                 **factored(characteristic)},
              "minimum": {"degree": minimum.degree(), "coefficientsAscending": coefficients(minimum),
                          **factored(minimum)}, "elapsedSeconds": time.monotonic() - before,
              "meaning": "The characteristic polynomial is the monic affine gcd of all rank-1021 minors of the complete reduced module, equivalently all rank-4354 minors of the original module over F31[s]. Its minimum polynomial is generally a different object."}
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
