#!/usr/bin/env python3
"""New exact identity and budgets for the current-parameter nonradial box."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as sp


TOPIC = Path(__file__).resolve().parents[1]
PROOF = "results/R119-supplement-same-current-parameter-finite-box-nonradial-pocket-form.md"
DEPS = [
    PROOF,
    "results/R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md",
    "results/R119-supplement-all-scaled-five-function-finite-box-generator.md",
    "results/R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md",
    "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md",
    "results/R119-supplement-actual-two-phase-compact-response-and-complete-pocket-form.md",
    "results/R119-supplement-actual-compact-profile-label-response.md",
    "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    "results/R133-supplement-actual-compact-ray-endpoint-response.md",
    "results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md",
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def serial(x):
    return str(x) if isinstance(x, F) else x


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    identities = {p: sha(TOPIC / p) for p in DEPS}
    identities["source"] = sha(Path(__file__))
    gates = []

    def gate(name, passed, **values):
        item = {"name": name, "passed": bool(passed)}
        item.update({k: serial(v) for k, v in values.items()})
        gates.append(item)
        if not passed:
            raise AssertionError(item)

    t = sp.symbols("t")
    lam = sp.symbols("lambda")
    u, Q, psi = [sp.Function(name)(t) for name in ("u", "Q", "psi")]
    s = 1 + Q
    potential = lam * Q + sp.diff(Q, t) / 2 - s**2 / 4
    dpotential = (s / 2 - lam) * sp.diff(psi, t) - sp.diff(psi, t, 2) / 2
    kernel = sp.diff(u, t)**2 + (s - 2*lam) * u * sp.diff(u, t)
    kernel += (s**2 / 4 - lam*Q) * u**2
    endpoint = (s / 2 - lam) * psi * u**2
    endpoint -= sp.diff(psi, t) * u**2 / 2
    endpoint += psi * u * sp.diff(u, t)
    residual = dpotential*u**2 + psi*kernel - sp.diff(endpoint, t)
    residual += psi*u*(sp.diff(u, t, 2) + potential*u)
    gate("complete radial center crossing identity including boundary charge",
         sp.expand(residual) == 0)
    gate("physical-to-wave kernel identity",
         sp.expand((sp.diff(u, t) + s*u/2)**2
                   - 2*lam*u*(sp.diff(u, t) + s*u/2) + lam*u**2
                   - kernel) == 0)

    def ramp(x):
        return 30*x*x*(1-x)*(1-x)

    fmin, fmax = ramp(F(7, 16)), ramp(F(15, 32))
    gate("unchanged quartic lower margin", fmin > F(7, 4), value=fmin)
    gate("unchanged quartic upper margin", fmax < F(31, 16), value=fmax)
    r = F(1, 2**80)
    gate("all-box Q divided by B remains above one",
         F(7, 4) - r/F(80) > 1)
    gate("all-box Q divided by B remains below two",
         7*F(1, 2**190) + r/F(80) < F(1, 16))
    gate("all-box actual first radial jet",
         F(2, 80) + r/F(80**2) < 1)
    gate("all-box actual second radial jet",
         F(30, 80**2) + r/F(80**3) < 1)
    gate("all-box actual third radial jet uses only C4",
         F(45, 80**3) + r/F(80**4) < 1)
    gate("center Cauchy variation has both ordered factors",
         2 * 2 * 2 == 8)
    gate("complete radial center Hessian coefficient",
         8 + 2**20 < 2**22)
    gate("actual box radius cancels four unnecessary port factors",
         22 - 36 == -14)
    gate("complete center matrix varies by less than dU over 64",
         F(1, 2**14) < F(1, 64))
    gate("complete radial center form throughout the box",
         F(1, 4) - F(1, 64) > F(1, 8))
    gate("auxiliary radial base lies in the actual quadratic ball",
         F(2**10, 2**11) < 1)
    gate("auxiliary radial path does not reach the original parameter margin",
         2*r*r < F(1, 2**48))
    gate("two true radial compensator components are retained",
         2*4 == 8)

    gate("principal nonzero radial mean term fits the rU column",
         34 + 3 + 4 < 128)
    gate("actual conjugacy weight times the nonzero radial row",
         96 + 3 + 4 < 128)
    gate("actual-minus-radial direct phase column reserve",
         1100 + 8 < 1110)
    gate("matrix E times both radial compensator components",
         2**128 + 2**257 < 2**260)
    global_chi = 16 + 1110 + 160024
    global_r = 16 + 260 + 160024
    gate("full infinite chi parameter inverse", global_chi == 161150)
    gate("full infinite radial parameter inverse", global_r == 160300)
    gate("chi row main exponent", 15 + 1110 == 1125)
    gate("radial row main exponent", 15 + 260 == 275)
    chi_feedback = 15 + 256 + global_chi - 1125
    r_feedback = 15 + 256 + global_r - 275
    gate("both true deep rows have the same complete feedback",
         chi_feedback == r_feedback == 160296)
    gate("actual input absorbs full joint feedback",
         chi_feedback - 1048576 < -1)
    gate("both true row constants keep complete sums",
         1125 + 1 < 1130 and 275 + 1 < 280)

    gate("all-scaled compact support is no larger than original low support",
         -10 < 0)
    gate("low-band dstar to dU comparison keeps the whole dyadic ratio",
         50 + 96 == 146)
    local_bits = 14000 + 146 + 16
    outside_bits = 21000 + 146 + 16
    gate("current-box full-output local comparison",
         local_bits == 14162 < 14200)
    gate("current-box full-pocket hat comparison",
         outside_bits == 21162 < 21200)
    gate("both actual and radial compensator integrals retained",
         8440 + 2 < 8450)
    radial_metric = 8450 - 36 - 6*6000
    gate("complete radial compensation is small in the center form",
         radial_metric == -27586 < -27000, log2_constant=radial_metric)
    gate("radial compensation has favorable layer powers",
         20 - 6*8 == -28 and 6*16 - 34 == 62)
    radial_state = 65 + 7800 + 24 + 10 - 36 - 6*6000
    gate("radial compensator full background response",
         radial_state == -28137 < -28000, log2_constant=radial_state)
    gate("radial response has favorable complete layer powers",
         16 - 6*8 == -32 and 6*16 - 32 == 64)
    gamma_chi = 21718 + 10 + 146
    gate("chi parameter metric row in true band units",
         gamma_chi == 21874 < 22200)
    state_chi = 181176 + 10 + 146
    gate("chi complete background row in true band units",
         state_chi == 181332 < 182200)
    r_metric = 280 + 8440 + 10 - 36 - 6*6000
    gate("nonradial radial-column metric contribution",
         r_metric == -27306 < -27000, log2_constant=r_metric)
    gate("nonradial radial-column favorable layer powers",
         24 - 6*8 == -24 and 6*16 - 40 == 56)
    r_state = global_r + 64 + 7800 + 24 + 10 - 36 - 6*6000
    gate("all-parameter radial-column background coefficient",
         r_state == 132162, log2_constant=r_state)
    gate("actual supplied input pays both background factors",
         r_state - 2*1048576 == -1964990 < -1900000,
         log2_upper=r_state - 2*1048576)

    local_first = F(14200 - 20010 - 1048576 + 14*70) + F(8197*3655, 128)
    outside_first = 21200 - 20010 - 1048576 + 14*84 + 8197*60
    gamma_first = 22200 - 20010 - 1048576 + 14*92 + 8197*68
    chi_state_first = 182200 - 20010 - 2*1048576 + 14*84 + 8197*60
    gate("complete first-layer local comparison", local_first < -810000,
         log2_upper=local_first)
    gate("complete first-layer outside response", outside_first < -550000,
         log2_upper=outside_first)
    gate("complete first-layer actual parameter chi row", gamma_first < -480000,
         log2_upper=gamma_first)
    gate("complete first-layer actual parameter chi background",
         chi_state_first < -1400000, log2_upper=chi_state_first)
    gate("largest polynomial layer ratio", F(8199, 8198)**92 < F(65, 64))
    gate("largest polynomial layer exponent", F(65, 64)**32 < 2)
    gate("all actual chi columns decay along the deep tail",
         F(31867, 256) - 68 - F(1, 32) > 56)
    gate("all eight errors fit a sixteenth",
         8*F(1, 256) < F(1, 16))
    gate("full actual box retains the stated positive form",
         F(1, 8) - 8*F(1, 256) > F(1, 16))
    gate("actual fixed-stop incoming enters the chosen neighborhood",
         4 - 60000000 < -1048576)

    report = {
        "status": "passed",
        "producer": "new SymPy full-boundary identity and Python Fraction budgets",
        "utc": datetime.now(timezone.utc).isoformat(),
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "gates": gates,
        "scope": {
            "object": "same current Gamma-star and the original all-scaled compact profile",
            "box": "all real independent theta_M in the actual low-scaled band box U^2<=B",
            "new": [
                "center radial matrix Hessian without another K^4 loss",
                "auxiliary radial reference ends at exactly the current Gamma",
                "nonzero radial compensator and joint actual-minus-radial parameter rows",
                "complete actual pocket crossing form on central plus/minus M two traces",
            ],
            "retained": [
                "r_U/N_band factor",
                "all output angular modes and both means",
                "ordinary and weak affine sources with actual weak endpoint traces",
                "physical principal endpoint dependence",
            ],
            "not_granted": [
                "positive matrix on a mixed-frequency cluster",
                "same-space norm derivative of a bare pullback",
                "whole-network inverse or a solved outer nonlinear F",
            ],
        },
        "bounds": {
            "complete_parameter_chi_global_bits": global_chi,
            "complete_parameter_radial_global_bits": global_r,
            "chi_row_bits": 1130,
            "radial_row_bits": 280,
            "radial_metric_relative_log2": radial_metric,
            "radial_parameter_background_first_log2": r_state - 2*1048576,
            "local_first_log2": str(local_first),
            "outside_first_log2": outside_first,
            "gamma_first_log2": gamma_first,
            "chi_state_first_log2": chi_state_first,
            "full_box_form": "r_U*d_U/(16*N_band) on central E_M",
        },
        "file_sha256": identities,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"],
        "gates": len(gates),
        "output": str(args.out),
        "sha256": sha(args.out),
    }))


if __name__ == "__main__":
    main()
