#!/usr/bin/env python3
"""Independent exact-rational audit of the N160 cuff-radius rescaling.

This does not import either construction or the submitted bound script.  It
checks the symbolic majorants against the retained candidate output, and only
certifies the unchanged rotational cells n >= 160.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def rational(v: Q) -> dict:
    return {"numerator": str(v.numerator), "denominator": str(v.denominator),
            "decimal_diagnostic": float(v)}


def run(root: Path) -> dict:
    delta, slope, eta0, n = Q(3, 500), Q(1, 2), Q(3, 10000), 160
    # exp(7Y/sqrt(12)) < 10/9 and 2^(11/4) > 6, as in R8.
    y_upper = 6 * delta + 6 * eta0 * Q(8, 5)
    assert Q(4, 3) ** 2 < 2
    assert 7 * y_upper / 3 < Q(1, 10)
    assert 6 ** 4 < 2 ** 11
    w = slope * 64 * Q(10, 9) / (6 * delta * 2 ** 280)
    assert w == Q(80000, 81) / 2 ** 280
    eta = eta0 / 2 ** 240
    h_upper = (2 * n + 7) * Q(7, 10) + 12
    assert h_upper < 241
    assert Q(7, 6) ** 4 < 2
    step_ratio = Q(6, 7) * (h_upper + Q(7, 5)) / h_upper
    assert step_ratio < 1

    candidate = json.loads((root / "notes/closing_deep_background_radius_family.json").read_text())
    radius_bounds = [(Q(1, 10), Q(1, 20)), (Q(3, 20), Q(1, 30)),
                     (Q(1, 5), Q(1, 40)), (Q(1, 4), Q(1, 50)),
                     (Q(7, 20), Q(1, 70))]
    rows = []
    for radius, k_bound in radius_bounds:
        b = Q(7, 2) * w * Q(15, 8) * 241 / (radius * eta) + 7 * w / radius
        angular = w / radius
        radial_extent = 2 * radius * y_upper / (3 * 2 ** n)
        height = w * radial_extent
        assert b < k_bound
        assert angular < Q(1, 10 ** 79)
        assert height < Q(1, 10 ** 131)
        submitted = next(row for row in candidate["rows"] if Q(row["rCuff"]) == radius)
        for key, expected in [("meridian_curvature_upper", b),
                              ("angular_curvature_upper", angular),
                              ("remaining_height_upper", height)]:
            item = submitted[key]
            assert Q(int(item["numerator"]), int(item["denominator"])) == expected
        rows.append({"radius": str(radius), "strict_meridian_bound": str(k_bound),
                     "meridian_majorant": rational(b), "angular_majorant": rational(angular),
                     "remaining_height_majorant": rational(height)})

    files = ["results/R8-default-n160-deep-background.md",
             "notes/2026-11-09-closing-deep-radius-family.md",
             "scripts/closing_deep_background_radius_family.py",
             "scripts/closing_deep_background_rational.py",
             "scripts/closing_recalibrated_tail.mjs",
             "scripts/closing_weighted_tail.mjs"]
    return {"status": "PASS for unchanged rotational deep cells only",
            "independence": "Self-contained Fraction arithmetic; no construction or candidate certificate module imported.",
            "source_sha256": {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in files},
            "source_r28_git_blob": "cf9881e3ae2c2797a61213ab099dbec239be5f0d",
            "fixed_parameters": {"N": n, "delta0": str(delta), "wCut": str(slope),
                                  "R": 64, "a": "11/4", "eta0": str(eta0)},
            "W160_upper": rational(w), "first_term_step_ratio_upper": rational(step_ratio),
            "rows": rows,
            "unpaid": ["finite warped cells", "nonaxisymmetric correction",
                       "infinite nonlinear extension", "all-surface reach"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("Refusing to overwrite an independent audit record")
    result = run(args.root)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "r_c_3_20": result["rows"][1]["meridian_majorant"]["decimal_diagnostic"], "report": str(args.out)}))
