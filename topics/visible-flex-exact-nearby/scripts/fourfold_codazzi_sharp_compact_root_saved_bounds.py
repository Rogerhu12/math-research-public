#!/usr/bin/env python3
"""Exact rational checks for R144-SR; no numerical producer is called."""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


BASE = Path(__file__).resolve().parents[1] / "notes"
INPUTS = {
    "fm": (
        "fixed_eta0_mean_retraction_ci/run-45778507038-1/fixed-eta0-correlated-mean-retraction.json",
        "c45df5750f1e888998d6b3ff47714fa23aa5b4c0163bcdb060bc3ba42cc9b124",
    ),
    "cp": (
        "compact_mean_c0_receivers_ci/run-45787608966-1/compact-mean-c0-receivers.json",
        "0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641",
    ),
    "tm": (
        "terminal_mean_small_scalar_gate_ci/run-45791979634-1/terminal-mean-small-scalar-gate.json",
        "a74d11052da41570a7588d5a79545cfb7295ccf437b3bae971390d59f2b99de6",
    ),
    "lc": (
        "localized_full_state_compact_sources_ci/run-45797426031-1/localized-full-state-and-compact-sources.json",
        "60ac20418b405281a3150216e45f7bffd0e73b7625ccc8c383cf4204968b5748",
    ),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def endpoints(ball):
    require(ball["kind"] == "complete_decimal_ball_v1", "complete ball kind")
    scale = F(10) ** int(ball["decimal_exponent"])
    midpoint, radius = int(ball["midpoint_integer"]), int(ball["radius_integer"])
    require(radius >= 0, "nonnegative saved radius")
    return (midpoint - radius) * scale, (midpoint + radius) * scale


def main():
    docs = {}
    for key, (relative, digest) in INPUTS.items():
        raw = (BASE / relative).read_bytes()
        require(sha256(raw).hexdigest() == digest, f"unchanged {key} input")
        doc = json.loads(raw)
        require(doc["complete"] is True and doc["failure"] is None,
                f"complete {key} record")
        if key != "fm":
            require(doc["proved"] is True, f"original {key} proof scope")
        docs[key] = doc

    same = {
        "original_candidate_sha256": "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
        "exact_alpha": "6890507429876859/9007199254740992",
        "exact_eta": "-7789843107295549/4611686018427387904",
        "exact_nu": "-2572625729470897/72057594037927936",
        "exact_interval": ["0", "25/8"],
    }
    for name, doc in docs.items():
        require(all(doc["identity"][key] == value for key, value in same.items()),
                f"same fixed raw object for {name}")
    fm, cp, tm, lc = (docs[key]["complete_new_scalars"] for key in ("fm", "cp", "tm", "lc"))

    def below(table, field, bound):
        require(endpoints(table[field])[1] < F(bound), field + " full upper endpoint")

    def inside(table, field, lower, upper):
        lo, hi = endpoints(table[field])
        require(F(lower) < lo and hi < F(upper), field + " full enclosure")

    inside(fm, "D_at_current_right", "-3.301986e-15", "-3.301985e-15")
    inside(fm, "forward_multiplier_at_current_right", "1.0078", "1.008")
    inside(cp, "abar", ".00452", ".00462")
    inside(cp, "bbar", ".00168", ".00172")
    # Division of a negative interval by a positive interval keeps this ordering.
    dlo, dhi = endpoints(fm["D_at_current_right"])
    hlo, hhi = endpoints(fm["forward_multiplier_at_current_right"])
    require(F("-3.277e-15") < dlo / hlo and dhi / hhi < F("-3.275e-15"), "Dbar enclosure")
    rho, b = F("8e-13"), F("2e-7")
    require(F("-3.277e-15") + F(".00452") * rho - F(".00172") * rho**2 > 0, "P(-rho)>0")
    require(F("-3.275e-15") + F(".00462") * F("7e-13") < 0, "P(-7e-13)<0")
    require(F(".00452") - 2 * F(".00172") * rho > 0, "strict negative derivative")

    constants = {
        "01": ".002539", "02": ".000947", "10": ".01424", "11": ".00702",
        "12": ".002615", "20": ".95313", "21": ".006477", "22": ".002414",
        "30": ".23503", "31": ".001993", "32": ".000743",
    }
    for key, value in constants.items():
        below(cp, "C" + key + "_profile_kernel_upper", value)
    C = {key: F(value) for key, value in constants.items()}
    below(tm, "E_ordinary_and_mean_jumps_upper", "1.894e-7")
    A = {0: rho*C["01"] + rho**2*C["02"]}
    for k in (1, 2, 3):
        A[k] = C[str(k)+"0"] + rho*C[str(k)+"1"] + rho**2*C[str(k)+"2"]
    selfmap = F("1.894e-7") + A[0] + A[1]*b + A[2]*b**2 + A[3]*b**3
    lipschitz = A[1] + 2*A[2]*b + 3*A[3]*b**2
    require(selfmap < F("1.923e-7") < b, "complete mean self-map")
    require(lipschitz < F(".014241") < 1, "complete mean contraction")
    require(endpoints(cp["mean_abs_lower"])[0] > F("1.068") > b, "negative mean")
    below(cp, "variance_upper", ".474")
    require(F(".474") < F(".689")**2, "variance square root")
    require(endpoints(cp["raw_v_gap_lower"])[0] > F(".09") > 8*rho*F(".689"), "positive density")

    below(lc, "density_A0_upper", "1.923")
    below(lc, "cosine_nonmean_A0_upper", ".986")
    state = b*F("1.923") + rho*F(".986")
    require(state < F("3.847e-7"), "full same-phi pair A0 state")
    selected = F("3.847e-7") + F("3.861e-18") + 19*F(9368259853002, 10**23)
    require(selected < F("3.865e-7"), "selected-reference state bridge")

    old_rho = F(docs["tm"]["exact_parameters"]["rho"])
    old_b = F(docs["tm"]["exact_parameters"]["b"])
    theta, sigma = F(".77"), F("4e-8")
    require(rho < old_rho and b < theta*old_b and rho < sigma*old_rho, "monotone source scaling")
    source_uppers = {
        "fu_L2_upper": "8.105e-8", "qu_L2_upper": "1.815e-6", "cv_operator_upper": "1.190",
        "fv_chi_L2_upper": "9.757e-5", "qv_L2_upper": "1.695e-6",
        "unchanged_raw_Ru_L2_upper": "3.214e-8", "unchanged_raw_Rv_L2_upper": "6.269e-8",
        "new_complete_v_jump_A0_upper": "2.691e-12", "unchanged_raw_u_jump_A0_upper": "3.370e-13",
    }
    for key, value in source_uppers.items():
        below(lc, key, value)
    fu_new = theta*F("8.105e-8")
    qu_new = theta*F("1.815e-6")
    fchi_new = sigma*F("9.757e-5")
    qv_new = theta*F("1.695e-6")
    require(fchi_new < F("3.903e-12"), "complete cutoff derivative source")
    require(F("3.214e-8") + fu_new < F("9.455e-8"), "full first ordinary source")
    require(F("1.190")*F("6.269e-8") + fchi_new < F("7.461e-8"), "full second ordinary source")
    require(F(".397")**3 > F(1, 16) and F("7.27")**3 > 384, "angular frequency factors")
    first = F(".397")*F("9.455e-8") + F("7.27")*qu_new
    second = F(".397")*F("7.461e-8") + F("7.27")*qv_new
    second_h1 = F("7.461e-8")/4 + qv_new
    require(first < F("1.020e-5") and second < F("9.519e-6") and second_h1 < F("1.324e-6"), "complete weak rows")
    require(first**2 + second**2 < F("1.395e-5")**2, "complete isotropic pair")
    require(first**2 + second_h1**2 < F("1.030e-5")**2, "complete anisotropic pair")
    print(json.dumps({
        "exact_rational_comparisons": "all passed",
        "root_interval": ["-8e-13", "-7e-13"],
        "same_old_compact_root": True,
        "mean_radius": str(b),
        "same_phi_pair_A0_upper": "3.847e-7",
        "selected_reference_pair_A0_upper": "3.865e-7",
        "cutoff_ordinary_L2_upper": "3.903e-12",
        "second_ordinary_L2_upper": "7.461e-8",
        "second_Hminus1_upper": "1.324e-6",
        "native_scans_or_old_scientific_target_calls": 0,
        "full_GC_solution_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
