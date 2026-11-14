#!/usr/bin/env python3
"""Finite exact checks for the full-prefix analytic-source note.

No candidate arrays, ODE/PDE, root solve, or tail call.  These checks supplement
the written proof; they are not certificates for a nonlinear surface.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    gates: list[str] = []

    def check(name: str, statement: bool) -> None:
        if not statement:
            raise AssertionError(name)
        gates.append(name)

    check("sqrt_bridge_length", F(21, 10) < F(3, 2) ** 2)
    check("green_source_sum", F(21, 10) * F(3, 2) / 4 + F(3, 2) == F(183, 80))
    check("negative_length_potential", 1200 * F(21, 10) == 2520)
    check("outer_source_coefficient", 3100 * F(3, 2) == 4650)
    check("y_source_coefficient", 4650 + F(183, 80) < 4653)
    check("xplusy_endpoint_exact", 1 + 2521 * 3100 == 7815101)
    check("xplusy_source_exact", 2521 * 4653 + F(3, 2) == F(23460429, 2))
    check("xplusy_endpoint_upper", 7815101 < 12000000)
    check("xplusy_source_upper", F(23460429, 2) < 12000000)
    check("bridge_L2_coefficient", F(3, 2) * 12000000 == 18000000)
    check("endpoint_ports_sqrt2", F(3, 2) ** 2 > 2)
    check("bridge_port_coefficient", F(3, 2) * 18000000 == 27000000)
    check("bridge_flux_outgoing", 4 * 27000000 < 110000000)
    check("bridge_internal_incoming", 2 * 27000000 < 10 ** 8)
    check("bridge_internal_source_exact", 27000000 * (110000000 + 1) == 2970000027000000)
    check("bridge_internal_source_upper", 2970000027000000 < 4 * 10 ** 15)
    check("feedback_transmission", 2 * 17 ** 2 == 578)
    check("feedback_band", 2 * F(459, 1000) == F(459, 500))
    check("combined_module_source", 400 ** 2 + 110000000 ** 2 < 120000000 ** 2)
    check("interface_incoming_exact", 578 * F(3, 2) == 867)
    check("interface_source_exact", 578 * 120000000 == 69360000000)
    check("module_incoming_upper", 2 + 867 < 1000)
    check("module_source_upper", 69360000000 + 400 < 7 * 10 ** 10)
    full_in = (200 + 10 ** 8) * 1000
    full_source = (200 + 10 ** 8) * 7 * 10 ** 10 + 40100 + 4 * 10 ** 15
    check("full_incoming_exact", full_in == 100000200000)
    check("full_incoming_upper", full_in < 2 * 10 ** 11)
    check("full_source_exact", full_source == 7004014000000040100)
    check("full_source_upper", full_source < 9 * 10 ** 18)
    full_out = 2 * 69360000000 + 110000000 + 2 * 400
    check("full_outgoing_exact", full_out == 138830000800)
    check("full_outgoing_upper", full_out < F(3, 2) * 10 ** 11)
    check("full_length", F(3, 2) + F(21, 10) == F(18, 5))
    check("source_units", F(43, 40) ** 2 < F(5, 4))
    check("pointwise_U_first", 6 / F(59, 100) < 216)
    check("L2_U_bound", 6 ** 7 < 540 ** 2)
    check("physical_incoming", 540 * 2 * 10 ** 11 < 2 * 10 ** 14)
    check("physical_source", 540 * F(5, 4) * 9 * 10 ** 18 < 7 * 10 ** 21)
    check("physical_outgoing", F(5, 4) * F(3, 2) * 10 ** 11 < 2 * 10 ** 11)

    script = Path(__file__).resolve()
    topic = script.parent.parent
    sources = [
        topic / "notes/2026-11-10-78718-geometry-full-prefix-analytic-source-v1.md",
        topic / "notes/2026-11-10-78718-geometry-bridge-two-barrier-feedback-v1.md",
        topic / "results/R75-flat17-sturm-frequency-propagator.md",
        topic / "results/R76-flat17-internal-ordinary-source-provider.md",
    ]
    report = {
        "kind": "finite-exact-arithmetic-only",
        "success": True,
        "gate_count": len(gates),
        "gates": gates,
        "script_sha256": sha(script),
        "sources": [
            {"path": str(p.relative_to(topic)), "bytes": p.stat().st_size, "sha256": sha(p)}
            for p in sources
        ],
        "pde_runs": 0,
        "tail_calls": 0,
        "candidate_arrays_read": 0,
    }
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "rational_gates": len(gates),
        "report_bytes": args.report.stat().st_size,
        "report_sha256": sha(args.report),
        "script_sha256": sha(script),
        "pde_runs": 0,
        "tail_calls": 0,
        "candidate_arrays_read": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
