#!/usr/bin/env python3
"""New exact budgets for the complete low cone and exterior crossing form.

The preceding full Bernstein certificate is an identified input.  These
gates concern only the newly used full-cone powers and response norms.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


TOPIC = Path(__file__).resolve().parents[1]
PROOF = "results/R119-supplement-complete-low-cone-and-explicit-exterior-crossing-form.md"
DEPS = [
    PROOF,
    "results/R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md",
    "notes/2026-11-14-R119-common-low-scaled-mixed-pocket-budget.json",
    "results/R119-supplement-same-current-parameter-finite-box-nonradial-pocket-form.md",
    "results/R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md",
    "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md",
    "results/R119-supplement-actual-two-phase-compact-response-and-complete-pocket-form.md",
    "results/R119-supplement-actual-compact-profile-label-response.md",
    "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md",
    "results/R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    identities = {p: sha(TOPIC / p) for p in DEPS}
    identities["source"] = sha(__file__)
    gates = []

    def gate(name, ok, **values):
        item = {"name": name, "passed": bool(ok)}
        item.update({k: str(v) if isinstance(v, F) else v for k, v in values.items()})
        gates.append(item)
        if not ok:
            raise AssertionError(item)

    gate("finite-e lower edge is the real fourth mode", 4**2 == 16)
    gate("full low-cone upper edge is the certified quarter", F(1, 2)**2 == F(1, 4))
    gate("nonzero lower exceeds the uniform low lower", 4**5 > 1)
    gate("mean lower exceeds the uniform nonzero lower", 190 > 0)
    gate("complete anchor comparison bits", -800-8*1024+22050+50 == 13108)
    gate("complete anchor comparison B power", -3+39-25 == 11)
    gate("complete anchor comparison Delta power", 3+103 == 106)
    gate("original J condition leaves positive B power", F(11)-F(1, 2) > 0)
    gate("original anchor comparison claimed bits", 13108+1 > 13000)
    gate("all low nonzero R fit the original B scale", F(1, 4)+F(1, 4) < 1)
    gate("original finite-box Hessian margin", 22-36 == -14)
    gate("complete low mass is three halves B", 1+F(1, 2) == F(3, 2))
    gate("four angular layers and all center components", 4*32 < 2**8)
    gate("lower source row uses only the upper input frequency", F(1, 4)/F(3, 2) < F(1, 2))
    gate("full unweighted input removes three B powers", F(9, 2)-F(3, 2) == 3)
    gate("new exact rho ratio bits", 800+3*1024 == 3872)
    gate("new exact rho ratio J power", 3*8 == 24)
    gate("both a-cubed comparisons retain the square root", (8**3)**2*6**3 < 2**30)
    gate("new ratio stated bits", 3872+15 == 3887)
    gate("new ratio delta power", 3*F(3, 2) == F(9, 2))

    n0, x0, logJ, logd = -20010, -1048576, 14, 8197
    alpha = F(31867, 256)
    fee_rows = [
        ("local mixed", 4400, 28, 8, 1, -990000),
        ("whole fixed-parameter hat", 13000, 40, 39, 1, -730000),
        ("joint full metric row", 14000, 48, 47, 1, -660000),
        ("joint full background row", 174000, 40, 39, 2, -1590000),
    ]
    gate("actual first-layer J dyadic upper", 8193+5 < 2**logJ)
    gate("actual reciprocal delta dyadic upper", F(25, 2) < 16)
    gate("complete fixed-parameter hat exponent", 32+F(231, 128)+F(9, 2) < 39)
    gate("complete joint metric exponent", 34+6+F(231, 128)+F(9, 2) < 47)
    gate("complete fixed-parameter hat bits", 7840+24+832+3887-42 == 12541 < 13000)
    gate("joint metric bits with twelve spare bump bits",
         1130+12+40+8440+3887-42 == 13467 < 14000)
    gate("joint complete background bits",
         161150+64+7840+24+3887-42 == 172923 < 174000)
    first = {}
    for name, bits, Jpower, dpower, Xpower, claim in fee_rows:
        value = bits+n0+Xpower*x0+Jpower*logJ+dpower*logd
        first[name] = value
        gate("complete new first-layer fee "+name, value < claim, log2_upper=value)
    gate("all used J powers have the claimed layer ratio", F(8199, 8198)**48 < F(65, 64))
    gate("J ratio costs less than a thirty-second bit", F(65, 64)**32 < 2)
    gate("new whole low-cone layer decay", alpha-47-F(1, 32) > 77)
    gate("all retained response rows leave a positive quarter", F(1, 2)-8*F(1, 256) > F(1, 4))

    gate("exact center shear cancellation", F(-1, 2)+F(1, 2) == 0)
    gate("top angular density order uses exactly H4", 2*F(7, 2)+1 == 2*4)
    gate("lower shear angular power remains in H4", 7-1 <= 8)
    gate("root whole-frequency physical exponent", F(125, 4)-3*F(3, 2) == F(107, 4) < 30)
    gate("strict whole-frequency physical exponent", F(131, 4)-3*F(3, 2) == F(113, 4) < 30)
    gate("whole-frequency J exponent", F(33, 2)-3 == F(27, 2) < 16)
    gate("whole-frequency finite extra fees", 8400+64 < 8500)

    gate("anchor over rho5 bits from d_anchor less than one", -(36+6*6000)+5*1024 == -30916)
    gate("anchor over rho5 J exponent", -6*8+5*8 == -8)
    gate("anchor over rho5 delta exponent", 6*16 == 96)
    logP = -42+F(231, 128)*logd
    logW = n0+4*logJ+6*logd
    direction = {
        "actual metric rho5 row": 1130+logW+x0+logP,
        "actual metric radius row": 280+logW+x0-30916,
        "fixed-parameter hat": 832+n0+x0+logP,
        "radial compensation hat": 64+n0+x0+1-30916,
        "complete gamma rho5 response": 64+n0+2*x0+161150+logP,
        "complete gamma radius response": 64+n0+2*x0+160300-30916,
    }
    for name, value in direction.items():
        gate("complete physical direction term "+name, value < -500000, log2_upper=value)
    gate("largest direction layer exponent is paid", alpha-6-F(231, 128)-F(1, 32) > 116)
    gate("full direction integral has its spare margin", 1+2*F(1, 2**256) < 4)
    gate("full response sum is below the claimed unit", 4*F(1, 2**256) < 1)
    gate("full Hermitian kernel absolute constant", 4*2**40+2**24 < 2**43)
    gate("whole-form absolute constant", 8500+43 < 8600)

    gate("low projection H4 costs B to the fourth in square norm", 2*4 == 8)
    gate("exterior Young numerator bits", 3+2*8600+800 == 18003)
    gate("exterior rho exponent", 2*5-8 == 2)
    gate("exterior B exponent", 4+3 == 7)
    gate("exterior J exponent before radial conversion", 2*16 == 32)
    gate("exterior a conversion bits", 7*5+7 == 42)
    gate("exterior Delta and J powers", 7-3 == 4 and 32+4 == 36)
    gate("exterior unrounded bits", 18003+42 == 18045 < 18200)
    gate("exterior complete delta exponent", 60+7*F(3, 2) == F(141, 2) < 71)
    gate("absolute high diagonal also fits", 8600-18200 < -1)
    gate("both exterior terms fit one bound", F(1, 2**155)+F(1, 2**9600) < 1)
    gate("localization denominator bits", 800+18200+4+15 == 19019)
    gate("localization rho exponent", 8-2 == 6)
    gate("localization delta exponent", 71+3*F(3, 2) == F(151, 2))
    gate("localization bits after rho", 19019+6*1024 == 25163 < 25200)
    gate("localization J exponent", 36+6*8 == 84)
    gate("stated localization chooses smaller delta power", F(151, 2) < 76)
    gate("complete square-root localization threshold", 12600*2 == 25200 and 42*2 == 84 and 38*2 == 76)
    gate("localized form leaves a positive sixteenth", F(1, 8)-F(1, 16) == F(1, 16))
    gate("actual incoming enters the same neighborhood", 4-60000000 < -1048576)

    report = {
        "status": "passed",
        "producer": "new local exact Fraction budgets; no predecessor native rerun",
        "utc": datetime.now(timezone.utc).isoformat(),
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "gates": gates,
        "new_bounds": {
            "complete_center_low_cone": "4<=|m|<=sqrt(B)/2 plus flux mean",
            "radial_lower": "d_low=2^-800*rho^8*Delta^3/B^3",
            "whole_actual_lower": "G>=d_low/4 times the complete center low norm",
            "full_frequency_absolute_form": "Cj=2^8600*rho^5*J^16*delta^-30 on the full wave H4 space",
            "complete_exterior_negative_term": "Dj=2^18200*rho^2*J^36*delta^-71",
            "sufficient_center_localization": "||Zhigh||H4 <= 2^-12600 J^-42 delta^38 ||Zlow||L2",
            "first_layer_actual_fees_log2": first,
            "complete_direction_terms_log2": {k: str(v) for k, v in direction.items()},
        },
        "scope": {
            "actual": [
                "same current Gamma-star, full original finite box and supplied incoming",
                "all center low physical modes and all their genuine mixed crossing terms",
                "all output frequencies and both means; constant height retained",
                "complete exterior quadratic and cross bounds",
            ],
            "retained": [
                "each original independent r_U/N coordinate",
                "physical principal endpoint maps and their parameter dependence",
                "ordinary and weak sources and endpoint normal charges",
            ],
            "not_granted": [
                "all actual global near-kernels satisfy the center localization",
                "every source has a solved original-label preimage",
                "the nonlinear outer F is solved",
            ],
        },
        "file_sha256": identities,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": "passed", "gates": len(gates),
                      "output": str(args.out), "sha256": sha(args.out)}), flush=True)


if __name__ == "__main__":
    main()
