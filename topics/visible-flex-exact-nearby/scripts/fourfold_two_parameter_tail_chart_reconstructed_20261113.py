#!/usr/bin/env python3
"""Independent reconstruction of R119 bundle 47 after environment loss.

This script does NOT reproduce or impersonate the unavailable original native.
It checks the newly written proof's exact rational gates and hashes real inputs.
Python standard library only. Run from any directory with --output PATH.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
PROOF = TOPIC / "results/R119-supplement-two-parameter-full-tail-chart-reconstructed.md"
DEPS = [
    "results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md",
    "results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md",
    "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
    "results/R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md",
    "results/R119-supplement-retuned-fourth-connector-and-common-bumps.md",
    "results/R119-supplement-actual-exterior-Schur-and-full-weak-Wronskian.md",
    "results/R119-supplement-actual-complete-radial-return-first-phase.md",
    "results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md",
]
def dy(k: int) -> F:
    return F(2**k) if k >= 0 else F(1, 2**(-k))
def rat(q: F | int) -> str:
    q = F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"
gates = []
def lt(name: str, lhs: F | int, rhs: F | int) -> None:
    lhs, rhs = F(lhs), F(rhs)
    gates.append({"name": name, "relation": "<", "lhs": rat(lhs),
                  "rhs": rat(rhs), "passed": lhs < rhs})
def le(name: str, lhs: F | int, rhs: F | int) -> None:
    lhs, rhs = F(lhs), F(rhs)
    gates.append({"name": name, "relation": "<=", "lhs": rat(lhs),
                  "rhs": rat(rhs), "passed": lhs <= rhs})
def eq(name: str, lhs: F | int, rhs: F | int) -> None:
    lhs, rhs = F(lhs), F(rhs)
    gates.append({"name": name, "relation": "=", "lhs": rat(lhs),
                  "rhs": rat(rhs), "passed": lhs == rhs})

r1, r2, rr1, rr2, Delta = dy(-15), dy(-29), dy(-16), dy(-30), F(80)
Sprime = lambda x: 30*x*x*(1-x)*(1-x)
xmin, xmax = F(3,16), F(7,32)
lt("second_bump_Sprime_lower", F(1,2), Sprime(xmin))
lt("second_bump_Sprime_upper", Sprime(xmax), 1)
lt("second_bump_absolute_monotonicity", 384*r2, Delta/2)
lt("first_bump_log_first", Delta*F(3375,2048)+96*r1, F(15,8)*Delta)
lt("second_bump_log_first", Delta+384*r2, F(15,8)*Delta)
lt("first_bump_log_second", Delta*F(45,8)+6144*r1, 6*Delta)
lt("second_bump_log_second", Delta*F(29,5)+98304*r2, 6*Delta)
le("all_jet_orders_zero_through_four", 4**4*r2/r1, F(1,64))
lt("full_complex_variation", 5+4*(r1+r2), F(28,3))
lt("full_material_integral_margin", 10+8*r2, 64)

sqrt_delta129 = dy(-64)/5
eq("delta129_exact_square", sqrt_delta129**2, F(2,25)*dy(-129))
e129 = dy(31)*sqrt_delta129
lt("fourth_matrix_error", e129, dy(-35))
b11,b12,b21,b22 = F(-1299),F(325,16),F(1235,64),F(-309,1024)
eq("fourth_ideal_determinant", b11*b22-b12*b21, F(1,64))
radius = F(1,16)
den_lower = 1299-b12*radius-e129*(1+radius)
lt("full_complex_cone_denominator", 1297, den_lower)
image_upper = (b21+abs(b22)*radius+e129*(1+radius))/den_lower
lt("full_complex_cone_invariance", image_upper, radius)
lt("actual_Mobius_derivative", F(1,64*1297**2), dy(-26))
lt("ideal_line_one_step_error", F(65,64)/1297, F(1,1000))
eq("unchanged_old_cell_count", 4096-128, 3968)
lt("initial_deep_line_difference", F(1,16)+F(1,64), F(1,8))
lt("infinite_error_geometric_sum", 1/(1000*(1-dy(-26))), F(1,999))
lt("deep_initial_error_below_surrogate", 100, 26*3968+3)
slope_error_upper = 70*(e129/999+dy(-100))
lt("true_fourth_physical_error", slope_error_upper, dy(-38))
lt("sqrt12_coefficient_lower_square", 69**2, 20**2*12)
lt("sqrt12_coefficient_upper_square", 20**2*12, 70**2)
lt("true_fourth_lower", 14, 16-F(70,64)-dy(-38))
lt("true_fourth_upper", 16-F(69*7,480)+dy(-38), 15)
le("first_parameter_Cauchy_fee", dy(-38)/(r1-rr1), dy(-22))
le("second_parameter_Cauchy_fee", dy(-38)/(r2-rr2), dy(-8))
lt("retuned_stop_difference", 15*dy(-37)/512, dy(-41))
x = 2*(rr1+rr2)
geometry_bound = F(1,1)/(1-x)*(1+8*rr1+32*rr2)*F(9375,131072)
lt("actual_geometric_profile_margin", geometry_bound, F(1,8))
lt("full_outer_good_set_positive", 0, 1-F(83,16384))
lt("real_gamma2_actual_unit_beta_shift_inside", dy(-86), rr2)
lt("real_gamma1_target_inside", dy(-24)+dy(-86), rr1)

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    files = [PROOF, Path(__file__).resolve()] + [TOPIC/x for x in DEPS]
    missing = [str(p) for p in files if not p.is_file()]
    if missing:
        raise FileNotFoundError("Required real input files missing: " + ", ".join(missing))
    hashes = {}
    for p in files:
        hashes[str(p.relative_to(TOPIC))] = sha(p)
    report = {
        "kind": "R119-bundle47-independent-reconstruction",
        "status": "passed" if all(g["passed"] for g in gates) else "failed",
        "arithmetic": "fractions.Fraction; exact rational comparisons; no float gates",
        "gates_count": len(gates),
        "passed_count": sum(bool(g["passed"]) for g in gates),
        "gates": gates,
        "file_sha256": hashes,
        "historical_unavailable_native_sha256":
            "7822dcf1b53b5cfe82be4360999ae9fdd7eef3ab6cc6e04b3c538c7a0722ae88",
        "historical_native_reproduced": False,
        "scope": [
            "New two-bump complex profile gates and inherited full-label realization",
            "Actual fourth line including all 3968 changed-prefix matrices",
            "Retuned stop and exact epsilon invariance",
            "Pointwise reselection of the actual all-mode external good set",
            "Actual new lambda and curvature q interface; ordinary/weak/mean retained",
        ],
        "not_claimed": [
            "same-width whole-network interior inverse",
            "nonradial complete beta counterterm",
            "solution of the full nonlinear exterior equation F",
            "original unavailable native bytes or original script reproduction",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "gates": len(gates),
                      "passed": report["passed_count"], "output": str(args.output),
                      "output_sha256": sha(args.output)}, ensure_ascii=False))
    if report["status"] != "passed":
        raise SystemExit(1)
if __name__ == "__main__":
    main()
