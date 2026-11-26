#!/usr/bin/env python3
"""Exact rational readouts for TH; no old enclosure, integral or solver runs."""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "D": (
        "notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json",
        "6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071",
    ),
    "WL": (
        "notes/complete_waist_lifting_ci/run-43749764738-1/execution.json",
        "936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d",
    ),
    "cap": (
        "notes/cached_cap_intrinsic_ci/run-43674917925-1-complete-cap-cached-intrinsic/evidence/complete-cap-intrinsic-summary.json",
        "7a08e94850d66de1d9dba184df205a5a288436fbb0cc005edaa462261976a17f",
    ),
}


def endpoints(value):
    if isinstance(value, dict):
        value = value["ball"]
    value = value.strip()
    m = re.fullmatch(r"\[([^\[\]]+?)\s+\+/-\s+([^\[\]]+)\]", value)
    if m:
        centre, radius = (F(x.strip()) for x in m.groups())
        if radius < 0:
            raise ValueError("negative serialized radius")
        return centre - radius, centre + radius
    q = F(value)
    return q, q


def upper(value):
    return endpoints(value)[1]


def decimal_upper(q, digits=6):
    scale = 10**digits
    n = q.numerator * scale // q.denominator + 1
    return f"{n // scale}.{n % scale:0{digits}d}"


def main():
    data = {}
    for name, (path, digest) in INPUTS.items():
        raw = (ROOT / path).read_bytes()
        if sha256(raw).hexdigest() != digest:
            raise ValueError(f"changed completed input {name}")
        data[name] = json.loads(raw)
        if not data[name]["complete"]:
            raise ValueError(f"incomplete input {name}")

    checks = {}

    def lt(name, a, b):
        checks[name] = a < b
        if not checks[name]:
            raise AssertionError(name)

    ds = data["D"]["actual_scientific_receipt"]
    ws = data["WL"]["actual_scientific_receipt"]
    cap = data["cap"]["complete_cap_intrinsic_constants"]
    products = ws["complete_positive_product_conclusion"]
    lt("saved full core beta product below 6", upper(products["B_star"]), F(6))
    lt("saved full core gamma product below 14", upper(products["G_star"]), F(14))
    lt("whole cap beta below 6", upper(cap["b_star"]), F(6))
    lt("whole cap gamma below 6", upper(cap["g_star"]), F(6))
    lt("whole cap K below 1", upper(cap["K_star"]), F(1))

    # These are the original strictly positive coefficients of knp and jnp
    # in selected_parameter_fees.N_nu, not reconstructed row data.
    d = F(1, 10**10)
    e0, e1 = 19*d, 83*d
    u = 14*e0 + e0**2
    v = (7+e0)**2
    ck = u*6/4 + v*e1/4 + u*7 + v*e0
    cj = e0*6 + (7+e0)*e1
    n = ds["complete_scalar_fee_conclusions"]["compact_metric_support"]
    nmax = upper(n["maxima"]["N_nu"])
    nl2 = upper(n["ordinary_L2_bounds"]["N_nu"])
    b1, j1 = nmax/ck, nmax/cj
    b1_l2, j1_l2 = nl2/ck, nl2/cj
    lt("complete beta K_nu below 4", b1, F(4))
    lt("complete C_nu below 24", j1, F(24))
    lt("complete beta K_nunu below 8", 2*b1, F(8))
    lt("complete C_nunu below 24", j1, F(24))
    lt("complete L2 beta K_nu below 1.014", b1_l2, F("1.014"))
    lt("complete L2 C_nu below 6.139", j1_l2, F("6.139"))

    state = ds["verified_global_state_bounds"]
    q0, qphi = F("6.407"), F("5.438")
    lt("same-metric compact pair A0", upper(state["background_pair_A0"])+F("3.861e-18")+F("4.739e-7"), q0)
    lt("same-metric compact angle A0", upper(state["background_pair_angle_A0"])+F("1.970e-17")+F("1.255e-6"), qphi)
    lt("2^(1/3) below 1.26", F(2), F("1.26")**3)
    lt("5^(1/3) below 1.71", F(5), F("1.71")**3)
    lt("129^(4/3)/128 below 5.1", F(129)**4, (128*F("5.1"))**3)
    lt("5^(4/3)/4 below 5.1", F(5)**4, (4*F("5.1"))**3)
    qa_base, qa_negative = F("34.141"), F("8.732")
    lt("complete compact A4/3", q0+qphi*F("5.1"), qa_base)
    lt("complete compact A1/3", q0+qphi*F(".4275"), qa_negative)

    rho = F(1, 10**4)

    def remainder_coefficient(c, qa):
        a = 1+c/4+c*c/2
        return 6*(c*(qa+q0/2)+qa+2*q0+a*rho)+14

    base = remainder_coefficient(F("1.26"), qa_base)
    negative = remainder_coefficient(F(1), qa_negative)
    lt("whole H1/3 source below 579 rho X4/3", base, F(579))
    lt("whole Hminus2/3 source below 215 rho X1/3", negative, F(215))
    mean = 6*(3*q0+rho)
    lt("complete nonzero mean below 115.327 rho L2", mean, F("115.327"))
    lt("normalized fourfold H1 to A0 constant below 1.1", 1+F(10,48), F(11,10)**2)

    # Pure parameter second derivative, with the complete saved radial L2
    # budget; no support-length substitution or new integral is made.
    a_base = 1+F("1.26")/4+F("1.26")**2/2
    a_negative = F(7,4)
    pure_base = (2*b1_l2*a_base*q0*q0+j1_l2*q0)*qa_base
    pure_negative = (2*b1_l2*a_negative*q0*q0+j1_l2*q0)*qa_negative

    # Two disjoint ordinary source windows of the proved compact high graph.
    # This is a response to H N only; the finite head and physical ports stay
    # independent. The old high-coordinate conversion is included.
    old_frame = F("1.000002")
    high_rows = {
        "base raw L2": (".032658", ".457708", 579, "266"),
        "base root outgoing": (".012975", ".181846", 579, "106"),
        "base physical outer": (".000168", ".002344", 579, "1.362"),
        "negative raw Hminus1": (".111046", "1.556368", 215, "336"),
        "negative root outgoing": (".044118", ".618339", 215, "134"),
        "negative physical outer": (".176471", "2.473353", 215, "534"),
    }
    for name, (collar, body, source, bound) in high_rows.items():
        lt(name+" full nonlinear-body response", (F(collar)**2+F(body)**2)*(source*old_frame)**2, F(bound)**2)

    print(json.dumps({
        "all_passed": all(checks.values()),
        "exact_rational_comparisons": len(checks),
        "new_metric_coefficients_from_complete_positive_budget": {
            "beta_K_nu_sup": decimal_upper(b1),
            "C_nu_sup": decimal_upper(j1),
            "beta_K_nunu_sup": decimal_upper(2*b1),
            "C_nunu_sup": decimal_upper(j1),
            "beta_K_nu_L2": decimal_upper(b1_l2),
            "C_nu_L2": decimal_upper(j1_l2),
        },
        "whole_compact_state_remainder": {
            "H1over3_over_rho_X4over3": "579",
            "Hminus2over3_over_rho_X1over3": "215",
            "complete_mean_over_rho_L2": "115.327",
        },
        "pure_parameter_second_derivative_L2_upper": {
            "H1over3": decimal_upper(pure_base),
            "Hminus2over3": decimal_upper(pure_negative),
        },
        "actual_compact_given_head_high_body_response": {
            name: row[3] for name, row in high_rows.items()
        },
        "low_norm_smallness_only": True,
        "unknown_angular_band_truncated": False,
        "old_rows_integrals_or_solvers_recomputed": 0,
        "full_regular_inverse_or_complete_nonlinear_iteration_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
