#!/usr/bin/env python3
"""Enclose an actual source-x second-derivative jump in the 4.625 tail.

The sign bracket and positive second derivative prove a unique simple zero
of w_x.  One-sided limits are then evaluated analytically at that root,
without differencing neighboring floating samples or solving a tail BVP.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import time

from q060_true_background_oracle import Q060TrueBackgroundOracle, file_sha256


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--constants", type=Path, required=True)
    ap.add_argument("--normalization-certificate", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    start = time.monotonic()
    oracle = Q060TrueBackgroundOracle(args.constants, args.normalization_certificate)
    k = oracle.k
    piece = oracle.piece(0, 1)
    center = Q.from_float(0.001724566341278432)
    left, right = center - Q(1, 10**10), center + Q(1, 10**10)

    def phase(x):
        return piece.zjet(k.J.var(oracle.qi(x)))[0]

    assert oracle.hi(phase(left).c[1]) < 0
    assert oracle.lo(phase(right).c[1]) > 0
    whole = piece.zjet(k.J.var(oracle.interval(left, right)))[0]
    assert oracle.lo(2 * whole.c[2]) > 0
    bisections = 0
    while right - left > Q(1, 10**28):
        middle = (left + right) / 2
        value = phase(middle).c[1]
        if oracle.hi(value) < 0:
            left = middle
        elif oracle.lo(value) > 0:
            right = middle
        else:
            raise ArithmeticError("Root interval precision exhausted before the requested width.")
        bisections += 1

    z, S = piece.zjet(k.J.var(oracle.interval(left, right)))
    assert oracle.lo(2 * z.c[2]) > 0
    w = oracle.iv.exp(z.c[0])
    # At the unique root z_x=w_x=0 exactly.  Keep that identity instead
    # of subtracting two small interval point evaluations.
    wxx = 2 * w * z.c[2]
    E = 1 + w * w
    old_rx = piece.r0 * piece.rd * oracle.iv.exp(piece.rd * oracle.interval(left, right))
    weight = piece.weight0 * oracle.iv.exp(piece.weights * S.c[0])
    B = old_rx * weight / E
    Bx = B * (piece.rd + piece.weights * S.c[1])
    rx = oracle.alpha * B
    cusp = wxx / (8 * E * oracle.iv.sqrt(E))
    rxx_minus = oracle.alpha * Bx - cusp
    rxx_plus = oracle.alpha * Bx + cusp
    jump_rxx = 2 * cusp
    jump_zxx = w * jump_rxx
    assert oracle.lo(rx) > 0 and oracle.lo(jump_rxx) > 0 and oracle.lo(jump_zxx) > 0

    # Physical-radius h_R and h_RR agree across source piece and cell
    # joins. These overlap checks catch a wrong piece/affine convention;
    # the all-join identity is proved in the accompanying note.
    joins = []
    for inner, outer in [((0, 4, 1), (0, 5, 0)), ((1, 8, 1), (0, 0, 0))]:
        a, b = oracle.local_jets(*inner), oracle.local_jets(*outer)
        intersections = {name: oracle._intersection(a[name], b[name]) for name in ("h_R", "h_RR")}
        joins.append({"inner": inner, "outer": outer, "common_jets": oracle.json_value(intersections)})

    result = {
        "status": "actual_source_x_not_C2_physical_R_graph_C2",
        "scope": __doc__, "source_sha256": file_sha256(__file__),
        "oracle_provenance": oracle.provenance,
        "root": {"cell": 0, "segment": 1, "left_exact": str(left),
                 "right_exact": str(right), "width_exact": str(right - left),
                 "bisections": bisections,
                 "bracket_verified": True, "unique_simple_zero_verified": True},
        "at_root": oracle.json_value({
            "w": w, "w_xx": wxx, "r_x": rx,
            "r_xx_left": rxx_minus, "r_xx_right": rxx_plus,
            "r_xx_jump": jump_rxx, "Z_xx_left": w * rxx_minus,
            "Z_xx_right": w * rxx_plus, "Z_xx_jump": jump_zxx,
            "h_R_common": w, "h_RR_common": oracle.zero}),
        "join_checks": joins,
        "nonrotating_warning": "For H(x), [H_RR]=[H_xx]/r_x^2-H_x[r_xx]/r_x^3. A globally C2 x-quintic generally does not satisfy the physical-R C2 compatibility condition.",
        "bvp_solves_executed": 0, "seconds": time.monotonic() - start,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "seconds": result["seconds"],
                      "r_xx_jump": oracle.bounds(jump_rxx), "Z_xx_jump": oracle.bounds(jump_zxx),
                      "out_sha256": file_sha256(args.out)}))


if __name__ == "__main__":
    main()
