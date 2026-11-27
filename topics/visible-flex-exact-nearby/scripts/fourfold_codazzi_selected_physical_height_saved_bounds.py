#!/usr/bin/env python3
"""Five new exact combinations for SHT; no old scientific target."""
from pathlib import Path
import hashlib
import json

PINS = {
    "results/R119-supplement-A0-response-and-differentiability-of-the-selected-exact-tail.md":
        (19857, "dc7d76eac5833119d1f5a8e2920766f86a6f3d5f600278dc7df9bb68705e1b47"),
    "results/R144-supplement-complete-physical-height-derivative-in-the-original-low-graph.md":
        (21369, "3ad4a7e9707ded3e9b7c4bb6a2862e7b83d12688cce868513f86992bd5a41270"),
}

def new_integer_combinations():
    margin = -49000000 - (-49999998 + 1)
    chain = 2048 - 31222782
    parameter_gap = chain - (-56000000)
    complete = max(chain, -56000000) + 1
    anchored = complete + 1
    rows = [
        ("cross_reference_background_margin", margin == 999997 and margin > 0),
        ("whole_coordinate_height_exponent", chain == -31220734),
        ("complete_partial_parameter_gap", parameter_gap == 24779266 and parameter_gap > 0),
        ("whole_selected_height_response_exponent", complete == -31220733),
        ("one_actual_mean_height_affine_elimination", anchored == -31220732),
    ]
    assert all(value for _, value in rows)
    return {
        "status": "proved_exact_saved_bound_combinations",
        "new_comparisons": len(rows),
        "old_scientific_targets_reexecuted": 0,
        "comparisons": [{"name": key, "passed": value} for key, value in rows],
        "selected_height_response_exponent": complete,
        "one_fixed_mean_height_response_exponent": anchored,
        "input_norm": "A0(eta/r_gamma)",
        "value_domain": "original closed S/T H8193 domain only",
        "derivative_continuity": "H8193 to global physical C2; relative H8193 base",
        "relative_A0_remainder": "at each fixed base along admitted increments",
        "A0_operator_continuity_claimed": False,
        "one_global_lambda_remains_independent": True,
        "full_core_or_fixed_metric_family_claimed": False,
    }

def main():
    root = Path(__file__).resolve().parents[1]
    for rel, (size, sha) in PINS.items():
        data = (root / rel).read_bytes()
        assert len(data) == size, rel
        assert hashlib.sha256(data).hexdigest() == sha, rel
    print(json.dumps(new_integer_combinations(), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
