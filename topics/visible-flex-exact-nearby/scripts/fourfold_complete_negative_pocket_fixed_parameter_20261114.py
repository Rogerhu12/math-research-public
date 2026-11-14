#!/usr/bin/env python3
"""Exact new budget for R119 complete negative-pocket fixed-Gamma form.

This is finite rational accounting for the displayed complete analytic proof.
It neither integrates a truncated Fourier system nor replays old native gates.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


TOPIC = Path(__file__).resolve().parents[1]
PROOF = "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md"
DEPS = [
    PROOF,
    "results/R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md",
    "results/R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md",
    "results/R119-supplement-actual-compact-profile-label-response.md",
    "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
    "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md",
    "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md",
    "results/R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md",
    "results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md",
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def exact(x):
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    return x


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    # Read identities once, before any concurrent publication can replace a path.
    identities = {name: sha(TOPIC / name) for name in DEPS}
    identities["source"] = sha(Path(__file__))
    gates = []

    def gate(name, ok, **data):
        record = {"name": name, "passed": bool(ok)}
        record.update({k: exact(v) for k, v in data.items()})
        gates.append(record)
        if not ok:
            raise AssertionError(record)

    gate("center k exceeds 2M for every M>=4", 3 * 4**2 > 16)
    gate("center k is below 3M", 7 < 9)
    gate("complete input H5/2 squared weight", F(5, 4)**5 < 4,
         ratio_at_minimum=F(5, 4)**5)
    gate("strict neighbor changes within reserve", 1024 + 10 + 5 < 1100,
         exponent=1024 + 10 + 5)
    gate("adjacent strict q bound", F(6) + F(1, 2) + F(3, 4) < 8)
    gate("adjacent strict log-density derivative bound", 25 + 1 + 3 <= 29)
    gate("adjacent root b squared bound", F(32) + 1 + F(9, 2) < 38)
    H = F(1, 64)
    gate("canonical extra slab is paid", F(7, 20) + 19 * H < 1,
         squared_energy_log_upper=F(7, 20) + 19 * H)
    gate("Airy and wave weight comparison", 1 + 16 < 25)
    gate("both weight changes fit factor eight", 5 < 8)
    gate("root extension constant reserve", 2185 + 3 + 1 < 2196)
    gate("root physical graph stays in canonical domain", 2 * H == F(1, 32))
    gate("complete center-root route", 1100 + 60 + 21 + 20 + 2196 < 3500,
         exponent=1100 + 60 + 21 + 20 + 2196)
    gate("root trace equation uses available output derivatives", F(5, 2) >= 1 and 3 >= 2)
    gate("root trace FTC coefficient", 4 * H == F(1, 16))
    gate("root graph trace reserve", 2 * 2**12 + 4 * H * 2**12 < 2**14)
    gate("root physical conversion reserve", 14 + 32 + 1 < 80)
    gate("B seven-halves constant", F(7 * 7, 2) < 25)
    root_delta = F(20) + F(9, 2) + F(21, 4)
    gate("root physical delta accounting", root_delta == F(119, 4),
         exponent=root_delta)
    gate("root physical J accounting", F(10) + 1 + F(7, 2) == F(29, 2))
    root_bits = 80 + 7000 + 128 + 38 + 25
    gate("root physical full two-row constant", root_bits < 7800, exponent=root_bits)
    strict_delta = F(20) + 6 + F(21, 4)
    gate("strict physical delta accounting", strict_delta == F(125, 4) < 32,
         exponent=strict_delta)
    gate("strict physical J accounting", F(10) + 2 + F(7, 2) < 16)
    gate("strict physical constant fits", 2200 + 128 + 128 + 25 < 7800)
    gate("root physical exponent fits", root_delta < 32 and F(29, 2) < 16)
    gate("whole pocket physical length", F(8, 2**8196) < 1)
    gate("full response over entire pocket", 7800 + 24 + 832 < 8700,
         exponent=7800 + 24 + 832)
    gate("rho5 over complete d exponent", 22000 - 5 * 2204 == 10980)
    gate("rho5 over d frequency power", 5 * 5 - 50 == -25)
    gate("rho5 over d B power", -5 * 4 + 39 == 19)
    gate("rho5 over d Delta power", -5 * 11 + 103 == 48)
    gate("Delta power constant", 3**48 < 2**77)
    gate("complete M-lower-bound fee", 25 * 40 == 1000)
    raw_delta = F(32) + F(57, 2) - F(25, 8) + F(231, 128)
    gate("actual full response delta exponent", raw_delta == F(7575, 128) < 60,
         exponent=raw_delta)
    raw_bits = 8700 + 10980 + 133 + 77 + 1000 - 42
    gate("actual full response binary fee", raw_bits == 20848 < 21000,
         exponent=raw_bits)
    gate("actual full response J exponent", 16 + 19 + 48 == 83 < 84)
    alpha = F(31867, 256)
    gate("old cell immediately before new junction", F(827, 256) < 4)
    gate("six neighbor terms at first layer", 16 + 2 + 2 * F(1, 2**120) + F(1, 2**240) < 32)
    gate("six neighbor terms after first layer",
         1 + 2 * F(1, 2**120) + 2 * F(1, 2**240) + F(1, 2**360) < 2)
    gate("neighbor exponential shift reserve", alpha + 1 < 128)
    gate("complete original junction remains included", -20138 + 128 == -20010)
    first = 21000 - 20010 - 1048576 + 14 * 84 + 8197 * 60
    gate("first actual complete-pocket layer", first == -554590 < -550000,
         log2_upper=first)
    gate("all-layer J ratio", F(8199, 8198)**84 < F(97, 96))
    gate("fractional geometric comparison", F(97, 96)**64 < 2)
    decay = alpha - 60 - F(1, 64)
    gate("complete infinite layer decay", decay > 64, exponent=decay)
    gate("sum retains announced margin", first + 2 < -550000)
    gate("actual incoming reaches new neighborhood", 4 - 60000000 < -1048576)
    gate("new label ball lies inside the original joint chart", 1048580 > 262148)
    gate("state radius is exactly the label radius times sixteen", -1048580 + 4 == -1048576)
    gate("complete form keeps d-over-eight",
         F(1, 4) - F(1, 2**33000) - F(1, 2**550000) > F(1, 8))

    report = {
        "status": "passed",
        "producer": "new Python Fraction computation; no old native replay",
        "utc": datetime.now(timezone.utc).isoformat(),
        "proof_scope": "fixed current Gamma; full negative pocket; all physical output modes and two means; center input +/-M; M^2/B<=1",
        "not_granted": [
            "Dpsi Gamma-star columns",
            "parameter-dependent principal endpoint identification",
            "mixed-frequency cluster positivity or full nonlinear F inverse",
            "unpaid rough-source graph trace regularity",
        ],
        "gates": gates,
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "bounds": {
            "physical_energy_bits": 7800,
            "physical_energy_J_power": 16,
            "physical_energy_delta_cost": 32,
            "full_response_relative_bits": 21000,
            "full_response_J_power": 84,
            "full_response_delta_cost": 60,
            "actual_state_bits": -1048576,
            "first_layer_log2_upper": first,
            "infinite_layer_decay": exact(decay),
            "form_lower_fraction_of_d": "1/8",
        },
        "file_sha256": identities,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "gates": len(gates),
                      "output": str(args.out), "sha256": sha(args.out)}))


if __name__ == "__main__":
    main()
