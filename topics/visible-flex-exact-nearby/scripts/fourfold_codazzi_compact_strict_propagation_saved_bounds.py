#!/usr/bin/env python3
"""R144-STC exact scalar arithmetic; no native row or scientific target calls."""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re


BASE = Path(__file__).resolve().parents[1] / "notes"
INPUTS = {
    "sp": (
        "primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json",
        "a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12",
    ),
    "d": (
        "selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json",
        "6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071",
    ),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def endpoints(record):
    value = record["ball"]
    if not value.startswith("["):
        return F(value), F(value)
    match = re.fullmatch(r"\[([^\s]+) \+/- ([^\s]+)\]", value)
    require(match is not None, "complete finite saved Arb ball")
    midpoint, radius = map(F, match.groups())
    require(radius >= 0, "nonnegative radius")
    return midpoint - radius, midpoint + radius


def main():
    docs = {}
    for name, (relative, digest) in INPUTS.items():
        raw = (BASE / relative).read_bytes()
        require(sha256(raw).hexdigest() == digest, "unchanged complete " + name + " input")
        doc = json.loads(raw)
        require(doc["complete"] is True and doc["actual_returncode"] == 0
                and doc["actual_failure"] is None, "completed " + name + " execution")
        native = doc["actual_scientific_receipt"]
        require(native["complete"] is True and native["proved"] is True
                and native["failure"] is None, "completed " + name + " mathematics")
        docs[name] = native
    sp = docs["sp"]["complete_strict_propagation_conclusion"]
    endpoint = docs["sp"]["complete_endpoint_readout_conclusion"]
    negative = docs["d"]["complete_scalar_fee_conclusions"]["fixed_negative_window"]
    count = 0

    def less(left, right, message):
        nonlocal count
        require(left < F(right), message)
        count += 1

    def upper(record, bound, message):
        less(endpoints(record)[1], bound, message + " full upper")

    cut = F("2333968743003/10000000000000")
    require(sp["exact_interval"] == ["0", str(cut)]
            and sp["complete_mean_coordinates"] == 2
            and sp["all_shorter_ordered_products_and_source_insertions_included"] is True
            and sp["affine_jumps_are_independent_without_radial_length_factor"] is True,
            "complete strict domain, means and source insertions")
    less(cut, ".234", "true full strict length")
    upper(sp["new_entire_q_upper"], "1.03", "same metric q")
    less(F(".5338"), endpoints(sp["new_entire_q_lower"])[0], "same metric positive q")
    maxima = sp["complete_selected_scalar_maxima"]
    upper(maxima["complete_R"], "1.912", "complete old R")
    upper(maxima["complete_L"], "3.704", "complete old L")

    e0 = 19 * F("1e-10")
    m1 = F("1.294e-8")
    upper(negative["maxima"]["M1"], m1, "complete negative M1")
    less(4 * m1 / (14 * e0 + e0**2), 2, "physical beta from positive domination")
    less(m1 / e0, 7, "physical gamma from positive domination")
    eps_r, eps_l = F("5e-7"), F("1.31e-6")
    less(F("1.03") * F("4.760e-7"), eps_r, "complete weighted state difference")
    less(F("1.03") * F("1.264e-6"), eps_l, "complete weighted angular difference")
    s = 2 * F("1.912") * eps_r + eps_r**2
    p = F("1.912") * eps_l + F("3.704") * eps_r + eps_r * eps_l
    t = 2 * F("3.704") * eps_l + eps_l**2
    d_d, d_rate = 4 * s, 8 * s
    d_a, d_b, d_ny, d_nz, d_ng = 12 * p, 8 * p, 4 * p + t, p, 7 * eps_l
    E = [
        [d_rate + d_d + (d_a + d_ny) / 4,
         d_d / 2 + d_b / 16 + (d_nz + d_ng) / 4],
        [d_a + d_ny, d_rate + d_nz],
    ]
    E_limits = [["4.280e-5", "9.385e-6"], ["7.942e-5", "1.966e-5"]]
    for i in range(2):
        for j in range(2):
            less(E[i][j], E_limits[i][j], "complete comparison increment")
    eps_matrix = F("9.3e-5")
    less(sum(x*x for row in E for x in row), eps_matrix**2,
         "full two-state Frobenius square")

    k_minus, k_plus = F("2.165"), F("2.516")
    for name, bound in (("reverse_nonradial_product", k_minus),
                        ("forward_nonradial_product", k_plus)):
        square = sum(endpoints(record)[1]**2 for row in sp[name] for record in row)
        less(square, bound**2, name + " whole Frobenius square")
    tau_minus = k_minus * eps_matrix * F(".234")
    tau_plus = k_plus * eps_matrix * F(".234")
    less(tau_minus, "4.712e-5", "complete reverse Duhamel feedback")
    less(tau_plus, "5.476e-5", "complete forward Duhamel feedback")
    less(tau_minus, 1, "reverse feedback closed")
    less(tau_plus, 1, "forward feedback closed")

    upper(sp["reverse_complete_operator_upper"], "173.871627", "old complete reverse")
    upper(sp["forward_complete_operator_upper"], "5.867924", "old complete forward")
    less(F("173.871627") / (1 - tau_minus), "173.880", "new complete reverse")
    less(F("5.867924") / (1 - tau_plus), "5.869", "new complete forward")
    # The new exact density factor is 1. This comparison is with the old
    # numerical budget value, not a lower bound for the old physical density.
    ng = endpoint["waist_complete_radial_factors"]["density_radial_factor_upper"]
    less(F(1), endpoints(ng)[0], "new exact waist factor fits old positive budget")
    upper(endpoint["strict_L1_Hminus1_source_to_waist_density_gain"],
          "191.800825", "old complete strict L1 gain")
    upper(endpoint["strict_L2_Hminus1_source_to_waist_density_gain"],
          "92.661215", "old complete strict L2 gain")
    less(F("191.800825") / (1 - tau_minus), "191.810", "new complete strict L1 gain")
    less(F("92.661215") / (1 - tau_minus), "92.666", "new complete strict L2 gain")

    # The four strict SC source bounds give these exact upper-budget sums.
    ru = F("1.107e-7") / 4 + F("1.705e-6")
    rv = F("7.469e-8") / 4 + F("1.594e-6")
    require(ru == F("1.732675e-6") and rv == F("1.6126725e-6"),
            "complete source conversion identities")
    less(ru**2 + rv**2, F("2.368e-6")**2, "complete Hminus1 pair source")
    jump = F("3.370e-13") + F("2.691e-12")
    require(jump == F("3.028e-12"), "complete jump upper sum")
    less(F("92.666") * F("2.368e-6") + F("191.810") * jump,
         "2.195e-4", "actual incoming strict residual column")

    print(json.dumps({
        "all_passed": True,
        "exact_rational_comparisons": count,
        "uniform_real_delta_radius": "1e-10",
        "full_Fourier_and_both_means": True,
        "new_reverse_propagator_upper": "173.880",
        "new_forward_propagator_upper": "5.869",
        "new_strict_L1_Hminus1_to_waist_upper": "191.810",
        "new_strict_L2_Hminus1_to_waist_upper": "92.666",
        "new_centre_strict_residual_incoming_upper": "2.195e-4",
        "native_row_scans_old_products_or_scientific_target_calls": 0,
        "root_Cauchy_positive_inverse_or_nonlinear_solution_transferred": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
