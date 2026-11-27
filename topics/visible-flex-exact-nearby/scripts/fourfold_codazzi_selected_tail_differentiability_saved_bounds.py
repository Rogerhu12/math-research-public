#!/usr/bin/env python3
"""SDIF: new exact exponent and inward-domain arithmetic only."""
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "results/R119-supplement-higher-regularity-of-selected-tail-and-local-uniqueness.md":
        "98724a93f890a0a33efefac41b5ba90eaf3e74df88433b55b6655790854a9b7c",
    "results/R144-supplement-separated-end-A0-parameter-forcing-with-complete-mixed-height.md":
        "fe9ca3abf47430f2374add9fc3bec905cdf119cc8e5fb018cbbf8a3499394ae1",
}

def main():
    for path, digest in PINS.items():
        assert sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
    rows = []
    def eq(name, a, b):
        assert a == b, (name, a, b)
        rows.append(dict(name=name, left=a, right=b, relation="="))
    def lt(name, a, b):
        assert a < b, (name, a, b)
        rows.append(dict(name=name, left=a, right=b, relation="<"))
    eq("common A0 Lipschitz exponent", 16777216+2-48000000, -31222782)
    eq("full high first-source exponent", 16777216+1-48000000, -31222783)
    eq("full high low-source exponent", 71303172+2-48000000, 23303174)
    eq("combined high coefficient ceiling", 23303174+1, 23303175)
    eq("complete separate endpoint derivative exponent", 131072+2-57000000, -56868926)
    lt("endpoint derivative below physical difference budget", -56868926, -31222782+3)
    eq("physical nonmean height exponent", -31222782+3+1, -31222778)
    eq("normalized far-height exponent", -31222782-440, -31223222)
    eq("uniform order3121 tail exponent", 184549391-1500000, 183049391)
    lt("seed below uniform high budget", -49999999, 183049391)
    eq("uniform selected high exponent", 183049391+1, 183049392)
    eq("uniform high difference exponent", 183049392+1, 183049393)
    eq("full interpolation gap", 3121-20, 3101)
    eq("actual forcing background continuity exponent numerator", 3121-2960, 161)
    eq("highest source remainder continuity exponent numerator", 3121-2898, 223)
    lt("forcing background strictly within interpolation window", 2960, 3121)
    eq("highest actual a-priori source", 1164+1734, 2898)
    lt("highest source below actual selected direction order", 2898, 2960)
    eq("inward low coefficient", 256, 2*128)
    eq("inward lower scale at endpoint", 2*256, 512)
    eq("two admitted low increment coefficients", 3+2, 5)
    eq("direct linear response low exponent", 16777216+1-48000000, -31222783)
    lt("direct linear response fits stated common coefficient", -31222783, -31222782)
    eq("direct high low-source exponent", 71303172+1-48000000, 23303173)
    lt("whole linear high response fits stated coefficient", 23303173+1, 23303175)
    print(json.dumps({
        "schema": "visible-flex-exact-nearby/SDIF-saved-exponents/v1",
        "all_passed": True, "new_comparisons": len(rows),
        "records": rows, "pins": PINS,
        "old_scientific_targets_executed": 0,
        "old_carriers_or_integrals_restored": 0,
        "value_domain": "original closed real-even H8193/A0 domain",
        "continuous_derivative_topology": "H8193 directions to E20 and E64..E1164",
        "bounded_derivative_direction_cost": "A0/r_gamma",
        "open_A0_value_extension_claimed": False,
        "A0_operator_continuity_claimed": False
    }, indent=2))

if __name__ == "__main__":
    main()
