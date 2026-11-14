#!/usr/bin/env python3
"""Independent integer-count reconstruction of the squared Fejer sections.

Counts all ordered four-tuples of Dirichlet monomial indices rather than
importing or repeating the author's triangular-coefficient convolution.
Only scalar exact arithmetic; no closed geometry or future solver fixture.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
PINS = {
    "notes/2026-11-09-db6f-prefix-c3-finite-core.md": "812a4e2ec8c1d54dcf3004b1c7ff275a0a84973fb22808c7ceac4cdeb0145d08",
    "scripts/db6f-prefix-c3-finite-bounds.py": "6ca39830537b2f63f444fb3de71f8ba69251211b2485a3f698dcc749e5063e69",
    "notes/2026-11-09-db6f-prefix-c3-finite-bounds.json": "2d5e300efe5f7fd33756235ee59e9c64466c5c0b0c441327f9248a8cb5c532fa",
    "notes/2026-11-09-db6f-tail-review-c3-finite-replay.json": "2d5e300efe5f7fd33756235ee59e9c64466c5c0b0c441327f9248a8cb5c532fa",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(path):
    return {"path": str(path.relative_to(REPO)), "bytes": path.stat().st_size, "sha256": sha(path)}


def read_q(value):
    return Q(int(value["numerator"]), int(value["denominator"]))


def interval(value):
    return read_q(value["lower"]), read_q(value["upper"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists() and args.out.resolve().is_relative_to(TOPIC), "New topic output required")
    bindings = []
    for rel, expected in PINS.items():
        path = TOPIC / rel
        require(sha(path) == expected, "Changed frozen input")
        bindings.append(binding(path))
    author = json.loads((TOPIC / "notes/2026-11-09-db6f-prefix-c3-finite-bounds.json").read_text())
    for row in author["source_bindings"]:
        path = (REPO / row["path"]).resolve()
        require(binding(path) == row, "Frozen dependency mismatch")
        if row not in bindings:
            bindings.append(row)
    require(len(author["cases"]) == 4, "Frozen case count")
    expected = [(3, Q(1, 10)), (4, Q(3, 20)), (7, Q(3, 20)), (7, Q(1, 10))]
    rows = []
    for index, item in enumerate(author["cases"]):
        N, r = item["Fejer_order"], read_q(item["r"])
        require((N, r) == expected[index], "Frozen case parameters")
        counts = Counter(i - j + k - ell for i, j, k, ell in product(range(N + 1), repeat=4))
        require(sum(counts.values()) == (N + 1) ** 4 and set(counts) == set(range(-2 * N, 2 * N + 1)),
                "Dirichlet four-tuple enumeration")
        require(all(counts[j] == counts[-j] for j in counts), "Four-tuple symmetry")
        c0 = Q(counts[0], (N + 1) ** 2)
        require(c0 == Q(2 * N * N + 4 * N + 3, 3 * (N + 1)) == read_q(item["normalization_c0"]),
                "Independent normalization")
        coefficients = {j: Q(counts[j], counts[0]) for j in range(1, 2 * N + 1)}
        require(all(0 < value < 1 for value in coefficients.values()), "Strict positive coefficients")
        require(coefficients == {row["j"]: read_q(row) for row in item["positive_fourier_b"]},
                "All saved b_j independently reconstructed")
        h0 = 1 - 2 * (1 - r) * sum((value / (9 * j * j - 1) for j, value in coefficients.items()), Q(0))
        hhalf = 1 - 2 * (1 - r) * sum(((-1) ** j * value / (9 * j * j - 1)
                                      for j, value in coefficients.items()), Q(0))
        delta = hhalf - h0
        diameter = 2 + 4 * (1 - r) * sum((value / (9 * j * j - 1)
                                         for j, value in coefficients.items() if j % 2 == 0), Q(0))
        peak = r + (1 - r) * Q(sum(counts.values()), counts[0])
        require(delta == read_q(item["delta_exact"]) and diameter == read_q(item["diameter_upper_exact"])
                and h0 == read_q(item["inradius_exact"]) and r == read_q(item["rho_min_exact"])
                and peak == read_q(item["rho_max_exact"]), "Exact derived geometric scalars")
        for name, value in (("delta", delta), ("diameter_upper", diameter), ("inradius", h0),
                            ("plane_ratio_lower", delta / diameter)):
            lo, hi = interval(item[name])
            require(lo <= value <= hi, "Published outward interval")
        dl = interval(item["delta"])[0]
        du = interval(item["diameter_upper"])[1]
        hl = interval(item["inradius"])[0]
        D, height = read_q(item["whole_D_budget"]), read_q(item["z_span_budget"])
        margins = {"whole_diameter_squared": D * D - du * du - height * height,
                   "held_target": dl - D / 5, "core_reach_target_only": r - 3 * D / 100,
                   "unconstructed_grip_disk_projection": hl - Q(3, 10),
                   "unconstructed_grip_disk_diameter": Q(3, 5) - D / 5}
        for name, value in margins.items():
            lo, hi = interval(item["strict_margins"][name])
            require(value > 0 and lo <= value <= hi, "Rounded-endpoint whole budget")
        require((item["rho_and_support_C3_harmonics"], item["rho_and_support_max_normal_angle_frequency"],
                 item["Cartesian_max_normal_angle_frequency"]) == (2 * N, 6 * N, 6 * N + 1)
                and item["finite_in_arclength_Fourier_basis_asserted"] is False,
                "Finite-mode scope")
        rows.append({"N": N, "r": str(r), "four_tuples_counted": sum(counts.values()),
                     "coefficients_all_equal": True, "c0": str(c0), "delta_exact": str(delta),
                     "diameter_upper_exact": str(diameter), "inradius_exact": str(h0),
                     "rho_min": str(r), "rho_max": str(peak),
                     "published_endpoint_budget_margins": {key: str(value) for key, value in margins.items()}})
    report = {"status": "PASS-independent-integer-four-tuple-kernel-reconstruction",
              "script_sha256": sha(Path(__file__).resolve()), "sources": bindings,
              "author_replay_byte_identical": True, "rows": rows,
              "scope": "Finite normal-angle kernel and conditional whole-image scalar inequalities only.",
              "solver_root_RK_geometry_backend_calls": 0, "future_closed_surface_constructed": False,
              "README_complete": False}
    with args.out.open("x") as handle:
        handle.write(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({"status": report["status"], "sha256": sha(args.out), "cases": len(rows), "solver_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
