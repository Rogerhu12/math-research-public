#!/usr/bin/env python3
"""True pole-height and local shoulder reach budgets for R262 with a new R302 arm belt."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

BUDGET = "2026-11-09-db6f-prefix-m12-segment-ball-budget.json"
HEIGHT = "2026-11-09-db6f-tail-background-height-rigorous.json"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--notes", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    budget_path = a.notes / BUDGET
    height_path = a.notes / HEIGHT
    assert sha(budget_path) == "f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c"
    assert sha(height_path) == "dd64e00bf25124b03e725792e321e961106c6ee643f5526e0b5b95383161ff01"
    b = json.loads(budget_path.read_text())
    c = json.loads(height_path.read_text())["cell0"]
    alpha = F(b["exact_alpha_interval"][0]["exact"])
    ah, bh = F(c["AH"][0]), F(c["BH"][0])
    assert min(ah, bh, alpha) > 0
    pole = F(b["cut_height_lower"]["exact"]) + ah + alpha*bh
    assert pole > F("1.8182480")
    reach = F(23,200)*(1+F(1,250))
    ratio = F(3,100)
    rows = []
    for half_belt in (F(233,1000), F(6,25), F(39,50)):
        span = 2*(pole+half_belt)
        reduction = pole + half_belt-reach/(2*ratio)
        rows.append(dict(halfBelt=str(half_belt),diameterLower=str(span),
                         reachOverDiameterUpper=str(reach/span),
                         necessaryAxialReductionPerHalf=str(reduction)))
    assert F(rows[1]["reachOverDiameterUpper"])<F(".02805")
    assert F(rows[1]["necessaryAxialReductionPerHalf"])>F(".1339146")
    out=dict(schema="R262-true-flat-pole-and-R302-shoulder-local-budget-v1",
             shapeSource="R262 original Q-free source; terminal W and C vanish; height perturbation at cuff vanishes",
             heightInputs=[sha(budget_path),sha(height_path)],sourceSHA256=sha(Path(__file__)),
             poleHeightLower=str(pole),shoulderReachUpper=str(reach),rows=rows)
    with a.out.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")
if __name__ == "__main__":
    main()
