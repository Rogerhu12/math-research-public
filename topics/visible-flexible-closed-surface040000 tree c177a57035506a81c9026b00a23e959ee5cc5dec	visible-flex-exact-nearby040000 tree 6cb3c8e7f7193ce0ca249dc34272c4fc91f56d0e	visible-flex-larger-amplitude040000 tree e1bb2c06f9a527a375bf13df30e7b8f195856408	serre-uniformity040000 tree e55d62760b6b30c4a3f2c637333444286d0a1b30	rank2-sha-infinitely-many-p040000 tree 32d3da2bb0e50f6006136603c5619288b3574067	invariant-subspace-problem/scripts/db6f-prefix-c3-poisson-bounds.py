#!/usr/bin/env python3
"""Exact scalar bounds for an auxiliary C3 convex section; no surface solver."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


SCALE = 10**12


def rational(x: Q) -> dict:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def decimal(n: int) -> str:
    sign = "-" if n < 0 else ""
    n = abs(n)
    return f"{sign}{n // SCALE}.{n % SCALE:012d}"


def down(x: Q) -> Q:
    return Q((x.numerator * SCALE) // x.denominator, SCALE)


def up(x: Q) -> Q:
    return -down(-x)


def interval(lo: Q, hi: Q) -> dict:
    assert lo <= hi
    a, b = down(lo), up(hi)
    return {
        "lower": rational(a), "upper": rational(b),
        "lower_decimal": decimal(a.numerator * (SCALE // a.denominator)),
        "upper_decimal": decimal(b.numerator * (SCALE // b.denominator)),
    }


def poisson(q: Q, r: Q, n: int) -> dict:
    assert 0 < q < 1 and 0 < r < 1 and n >= 2 and n % 2 == 0
    odd = sum((q**(2*k+1) / (9*(2*k+1)**2-1) for k in range(n)), Q(0))
    j = 2*n+1
    delta_lo = 4*(1-r)*odd
    delta_hi = delta_lo + 4*(1-r)*q**j / ((1-q*q)*(9*j*j-1))
    even = sum(((-1)**(k+1)*q**(2*k)/(36*k*k-1) for k in range(1,n+1)), Q(0))
    diameter_lo = 2+4*(1-r)*even
    diameter_hi = diameter_lo+4*(1-r)*q**(2*n+2)/(36*(n+1)**2-1)
    hsum = sum((q**j/(9*j*j-1) for j in range(1,n+1)), Q(0))
    htail = q**(n+1)/((1-q)*(9*(n+1)**2-1))
    inradius_lo = 1-2*(1-r)*(hsum+htail)
    inradius_hi = 1-2*(1-r)*hsum
    rho_min = r+(1-r)*(1-q)/(1+q)
    rho_max = r+(1-r)*(1+q)/(1-q)
    return {
        "q": rational(q), "r": rational(r), "terms": n,
        "delta": interval(delta_lo, delta_hi),
        "diameter": interval(diameter_lo, diameter_hi),
        "inradius": interval(inradius_lo, inradius_hi),
        "rho_min": rational(rho_min), "rho_max": rational(rho_max),
        "plane_ratio": interval(delta_lo/diameter_hi, delta_hi/diameter_lo),
        "five_delta": interval(5*delta_lo, 5*delta_hi),
        "height_squared_allowance": interval(25*delta_lo**2-diameter_hi**2,
                                               25*delta_hi**2-diameter_lo**2),
    }


def read_q(d: dict) -> Q:
    return Q(int(d["numerator"]), int(d["denominator"]))


def budget(row: dict, D: Q, height: Q, leakage: Q = Q(0)) -> dict:
    # Use only already rounded rational report endpoints for every acceptance.
    delta = read_q(row["delta"]["lower"])
    diameter = read_q(row["diameter"]["upper"])
    rho_min = read_q(row["rho_min"])
    inradius = read_q(row["inradius"]["lower"])
    radius = Q(3,10)
    margins = {
        "whole_diameter_squared": D*D-(diameter+2*leakage)**2-height*height,
        "held_target": delta-leakage-D/5,
        "core_reach_target_only": rho_min-3*D/100,
        "possible_grip_disk_projection": inradius-radius,
        "possible_grip_disk_diameter": 2*radius-D/5,
    }
    assert all(x > 0 for x in margins.values())
    return {
        "whole_D_budget": rational(D), "z_span_budget": rational(height),
        "projection_leakage_budget": rational(leakage),
        "unconstructed_grip_disk_radius": rational(radius),
        "strict_margins": {k: interval(x,x) for k,x in margins.items()},
        "scope": "CONDITIONAL_ON_FULL_PROJECTION_AND_ROTATED_SECTION; core reach is not whole-surface reach",
        "all_strict_rational_checks_passed": True,
    }


def bind(path: Path, root: Path) -> dict:
    b = path.read_bytes()
    return {"path": str(path.relative_to(root)), "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest()}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    cases = [
        (Q(9,10), Q(3,20), Q(43,20), Q(59,100)),
        (Q(19,20), Q(3,20), Q(23,10), Q(99,100)),
        (Q(97,100), Q(3,20), Q(12,5), Q(6,5)),
        (Q(99,100), Q(3,20), Q(5,2), Q(69,50)),
        (Q(99,100), Q(1,10), Q(13,5), Q(31,20)),
    ]
    rows = []
    for q,r,D,height in cases:
        row = poisson(q,r,256)
        row["conditional_whole_budget"] = budget(row,D,height)
        rows.append(row)
    rows[-1]["optional_leakage_budget"] = budget(rows[-1],Q(13,5),Q(3,2),Q(1,100))
    script = Path(__file__).resolve()
    root = script.parents[3]
    inputs = [script, root/"topics/visible-flexible-closed-surface/README.md",
              root/"topics/visible-flexible-closed-surface/results/R10-positive-support-offset-reach.md"]
    out = {
        "status": "EXACT_RATIONAL_AUXILIARY_SECTION_BOUNDS_ONLY",
        "same_as_current_frozen_g": False,
        "new_closed_surface_or_flexible_family_asserted": False,
        "source_bindings": [bind(x,root) for x in inputs],
        "rounding_scale": SCALE,
        "rounding": "integer floor/ceiling of exact Fraction; no binary floating arithmetic",
        "cases": rows,
        "solver_root_RK_geometry_backend_calls": 0,
    }
    args.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    b=args.out.read_bytes()
    print(json.dumps({"status":"PASS","cases":len(rows),"bytes":len(b),
                      "sha256":hashlib.sha256(b).hexdigest(),"solver_calls":0}))


if __name__ == "__main__":
    main()
