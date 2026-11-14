#!/usr/bin/env python3
"""Independent exact support-value recomputation for the frozen Poisson note.

Uses full j=1..1024 support sums at three angles, rather than the author's
256 odd-term displacement sum. No author module, solver or geometry backend
is imported, and no future closed surface is created.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
PINS = {
    "notes/2026-11-09-db6f-prefix-c3-poisson-core.md": "df2f2857c8330dc9fd851d09e194ae731c46336e4dafba2a5cb9afd90cfd761f",
    "scripts/db6f-prefix-c3-poisson-bounds.py": "6f804847b44a8395c4abb5b325ed2b83f855c056b8bbc51ed1b7768e7f46c7b9",
    "notes/2026-11-09-db6f-prefix-c3-poisson-bounds.json": "4d84a5f3533f367fc8acfb2501c20e16c157e0a41d02f5207e0ea05c3fc0908e",
    "notes/2026-11-09-db6f-tail-review-c3-poisson-replay.json": "4d84a5f3533f367fc8acfb2501c20e16c157e0a41d02f5207e0ea05c3fc0908e",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source(path):
    return {"path": str(path.relative_to(REPO)), "bytes": path.stat().st_size, "sha256": sha(path)}


def read_q(d):
    return Q(int(d["numerator"]), int(d["denominator"]))


def outer(d):
    return read_q(d["lower"]), read_q(d["upper"])


def rounded_interval(lo, hi, scale=10**16):
    require(lo <= hi, "Interval order")
    low = Q((lo.numerator * scale) // lo.denominator, scale)
    high = -Q(((-hi).numerator * scale) // hi.denominator, scale)
    return {"lower_exact": str(low), "upper_exact": str(high),
            "lower_display_only": float(low), "upper_display_only": float(high)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists() and args.out.resolve().is_relative_to(TOPIC), "New topic output required")
    bindings = []
    for rel, expected in PINS.items():
        path = TOPIC / rel
        require(sha(path) == expected, "Changed frozen input: " + rel)
        bindings.append(source(path))
    author = json.loads((TOPIC / "notes/2026-11-09-db6f-prefix-c3-poisson-bounds.json").read_text())
    for item in author["source_bindings"]:
        path = (REPO / item["path"]).resolve()
        require(source(path) == item, "Author source identity")
        if source(path) not in bindings:
            bindings.append(source(path))
    require(len(author["cases"]) == 5, "Frozen case count")
    rows = []
    expected_cases = [(Q(9, 10), Q(3, 20)), (Q(19, 20), Q(3, 20)),
                      (Q(97, 100), Q(3, 20)), (Q(99, 100), Q(3, 20)), (Q(99, 100), Q(1, 10))]
    J = 1024
    for index, item in enumerate(author["cases"]):
        q, r = read_q(item["q"]), read_q(item["r"])
        require((q, r) == expected_cases[index] and item["terms"] == 256, "Frozen parameters")
        power = Q(1)
        zero_sum = Q(0)
        minus_sum = Q(0)
        width_sum = Q(0)
        odd_sum = Q(0)
        for j in range(1, J + 1):
            power *= q
            value = power / (9 * j * j - 1)
            zero_sum += value
            minus_sum += value if j % 2 else -value
            if j % 2:
                odd_sum += value
            else:
                width_sum += value if (j // 2) % 2 else -value
        factor = 2 * (1 - r)
        first = power * q / (9 * (J + 1) ** 2 - 1)
        hmin = (1 - factor * (zero_sum + first / (1 - q)), 1 - factor * zero_sum)
        hmax = (1 + factor * minus_sum, 1 + factor * (minus_sum + first))
        delta = (hmax[0] - hmin[1], hmax[1] - hmin[0])
        require(delta[0] == 4 * (1 - r) * odd_sum, "Independent support subtraction identity")
        first_width = power * q * q / (9 * (J + 2) ** 2 - 1)
        diameter = (2 + 2 * factor * width_sum, 2 + 2 * factor * (width_sum + first_width))
        require(delta[0] > 0 and diameter[0] > 0, "Positive displacement and diameter")
        rho_min = r + (1 - r) * (1 - q) / (1 + q)
        rho_max = r + (1 - r) * (1 + q) / (1 - q)
        require(rho_min == read_q(item["rho_min"]) and rho_max == read_q(item["rho_max"]), "Exact curvature-radius endpoints")
        independent = {"delta": delta, "diameter": diameter, "inradius": hmin,
                       "plane_ratio": (delta[0] / diameter[1], delta[1] / diameter[0]),
                       "five_delta": (5 * delta[0], 5 * delta[1]),
                       "height_squared_allowance": (25 * delta[0] ** 2 - diameter[1] ** 2,
                                                    25 * delta[1] ** 2 - diameter[0] ** 2)}
        for name, (lo, hi) in independent.items():
            low, high = outer(item[name])
            require(low <= lo <= hi <= high, "Finer support-based interval leaves author bound: " + name)
        budget_rows = []
        for budget_name in ("conditional_whole_budget", "optional_leakage_budget"):
            if budget_name not in item:
                continue
            b = item[budget_name]
            D, length, eta = [read_q(b[key]) for key in ("whole_D_budget", "z_span_budget", "projection_leakage_budget")]
            # Deliberately use the published rounded endpoints, not our tighter values.
            dl, du = outer(item["delta"])[0], outer(item["diameter"])[1]
            lower_inradius = outer(item["inradius"])[0]
            disk = read_q(b["unconstructed_grip_disk_radius"])
            margins = {"whole_diameter_squared": D * D - (du + 2 * eta) ** 2 - length * length,
                       "held_target": dl - eta - D / 5,
                       "core_reach_target_only": rho_min - 3 * D / 100,
                       "possible_grip_disk_projection": lower_inradius - disk,
                       "possible_grip_disk_diameter": 2 * disk - D / 5}
            for key, value in margins.items():
                low, high = outer(b["strict_margins"][key])
                require(value > 0 and low <= value <= high, "Published rational budget margin: " + key)
            budget_rows.append({"name": budget_name, "D": str(D), "length": str(length), "eta": str(eta),
                                "reconstructed_exact_margins": {key: str(value) for key, value in margins.items()}})
        rows.append({"q": str(q), "r": str(r), "full_support_terms": J,
                     "finer_support_based_bounds_inside_published_intervals": True,
                     "bounds": {key: rounded_interval(*value) for key, value in independent.items()},
                     "hmax_independent": rounded_interval(*hmax), "rho_min": str(rho_min), "rho_max": str(rho_max),
                     "budgets": budget_rows})
    result = {"status": "PASS-independent-full-support-Fraction-reconstruction",
              "script_sha256": sha(Path(__file__).resolve()), "sources": bindings,
              "author_replay_byte_identical": True, "rows": rows,
              "scope": "Auxiliary planar section and conditional whole-image scalar inequalities only.",
              "solver_root_RK_geometry_backend_calls": 0, "future_closed_surface_constructed": False,
              "README_complete": False}
    with args.out.open("x") as handle:
        handle.write(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({"status": result["status"], "sha256": sha(args.out), "cases": len(rows),
                      "budgets": sum(len(row["budgets"]) for row in rows), "solver_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
