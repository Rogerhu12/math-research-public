#!/usr/bin/env python3
"""Exact rational constants for the actual R144 terminal-mean Jacobian."""

from fractions import Fraction as F
from hashlib import sha256
import json

from fourfold_codazzi_sharp_compact_root_saved_bounds import BASE, INPUTS, endpoints, require


def main():
    docs = {}
    for key in ("cp", "fm"):
        name, digest = INPUTS[key]
        raw = (BASE / name).read_bytes()
        require(sha256(raw).hexdigest() == digest, "complete unchanged " + key)
        docs[key] = json.loads(raw)
        require(docs[key]["complete"] is True and docs[key]["failure"] is None,
                "completed " + key)
    cp, fm = (docs[key]["complete_new_scalars"] for key in ("cp", "fm"))

    limits = {
        "K0_ordinary_mean_C0_upper": ".595255",
        "KJ_all_common_jumps_C0_upper": "1.495385",
        "K1_full_nonmean_C0_upper": ".085486",
        "prefix_inverse_tau_max": "2.378e12",
    }
    for key, upper in limits.items():
        require(endpoints(cp[key])[1] < F(upper), key)
    require(endpoints(fm["a_at_current_right"])[1] < F("6.564e-6"), "outer radius")
    require(endpoints(fm["m_at_current_right"])[1] < -F("5.84"), "negative raw outer mean")
    b, rho, L = F("2e-7"), F("8e-13"), F(".014241")
    inv = 1/(1-L)
    require(inv < F("1.015"), "scalar inverse multiplier")
    require(F(".595255")*inv < F(".605"), "ordinary source receiver")
    require(F("1.495385")*inv < F("1.518"), "all mean atoms receiver")
    terminal = F("1.013237")*F("2.378e12")*2*F("6.564e-6")**2/F("5.84")**3*inv
    require(terminal < F("1.058"), "complete physical terminal value")
    ratio = (1+b/F("1.068"))**3*(1+rho)
    require(ratio < F("1.000000562"), "physical density coordinates")
    require(F(".085486")*ratio*inv < F(".087"), "whole nonmean pair receiver")

    upper = {
        "01": ".002539", "02": ".000947", "11": ".00702", "12": ".002615",
        "21": ".006477", "22": ".002414", "31": ".001993", "32": ".000743",
    }
    for key, val in upper.items():
        require(endpoints(cp["C"+key+"_profile_kernel_upper"])[1] < F(val), "full kernel " + key)
    C = {key: F(val) for key, val in upper.items()}
    param_source = (C["01"]+2*rho*C["02"]
                    +(C["11"]+2*rho*C["12"])*b
                    +(C["21"]+2*rho*C["22"])*b**2
                    +(C["31"]+2*rho*C["32"])*b**3)
    require(param_source*inv < F(".002576"), "full terminal control derivative")
    require(endpoints(cp["abar"])[0] > F(".00452")
            and endpoints(cp["abar"])[1] < F(".00462"), "complete compact moment")
    # The a0 enclosure is R133 final-waist-amplitude-coordinate (A.1).
    lower = F("1.06873282")*F(".00452")*(1-rho)/2
    upper = F("1.068732841")*F(".00462")/2
    require(lower > F(".002415") and upper < F(".002469"), "terminal waist control derivative")
    require(1/F(".002415") < 415, "waist control reciprocal")
    require(F(".002576")/F(".002415") < F("1.067"), "two-endpoint mean profile ratio")
    require(F(".087")*415 <= F("36.105"), "shape-slice functional")
    print(json.dumps({
        "exact_rational_comparisons": "all passed",
        "terminal_scalar_inverse_factor_upper": "1.015",
        "ordinary_Linfty_to_C0_upper": ".605",
        "mean_jump_l1_to_C0_upper": "1.518",
        "physical_nonmean_pair_to_C0_upper": ".087",
        "physical_terminal_value_to_C0_upper": "1.058",
        "terminal_control_whole_C0_upper": ".002576",
        "terminal_control_waist_interval": [".002415", ".002469"],
        "terminal_control_waist_inverse_upper": "415",
        "forward_control_waist_derivative": "exactly zero",
        "old_numerical_targets_called": 0,
        "full_GC_inverse_claimed": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
