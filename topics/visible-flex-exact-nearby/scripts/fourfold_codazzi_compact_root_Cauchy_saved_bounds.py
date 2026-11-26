#!/usr/bin/env python3
"""R144-RTC: exact arithmetic on completed small root/SP conclusions only."""

from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re


BASE = Path(__file__).resolve().parents[1] / "notes"
ROOT_PATH = (
    "large_root_Cauchy_ci/run-43621934843-1-full-real-large-root-Cauchy/"
    "evidence/full-real-large-root-Cauchy-summary.json"
)
ROOT_SHA = "238a85156791fac2516a23c5f9a6ea1253e648c341bedae139d1c2c5c47cbee5"
SP_PATH = "primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json"
SP_SHA = "a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12"
LIMITS = {
    "1/1000": ("4.287078", "4.650018", "4.793129"),
    "1/500": ("4.665118", "5.544076", "5.714702"),
    "1/200": ("6.531910", "10.936298", "11.272878"),
    "1/100": ("13.916705", "50.807928", "52.371613"),
    "3/200": ("32.146066", "285.574846", "294.363813"),
    "1/50": ("73.587358", "1515.050846", "1561.678666"),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def endpoints(record):
    text = record["ball"]
    if not text.startswith("["):
        return F(text), F(text)
    match = re.fullmatch(r"\[([^\s]+) \+/- ([^\s]+)\]", text)
    require(match is not None, "finite complete saved ball")
    midpoint, radius = map(F, match.groups())
    require(radius >= 0, "nonnegative saved radius")
    return midpoint - radius, midpoint + radius


def read(relative, digest):
    raw = (BASE / relative).read_bytes()
    require(sha256(raw).hexdigest() == digest, "unchanged complete small input")
    return json.loads(raw)


def main():
    root = read(ROOT_PATH, ROOT_SHA)
    sp_doc = read(SP_PATH, SP_SHA)
    require(root["complete"] is True and root["failure"] is None
            and root["same_full_real_family_root_Cauchy_estimate_proved"] is True
            and root["all_frequencies_and_independent_even_mean_retained"] is True,
            "complete original root Cauchy theorem")
    require(sp_doc["complete"] is True and sp_doc["actual_returncode"] == 0
            and sp_doc["actual_failure"] is None, "complete original SP execution")
    sp = sp_doc["actual_scientific_receipt"]
    require(sp["complete"] is True and sp["proved"] is True and sp["failure"] is None,
            "complete original SP mathematics")
    readout = sp["complete_endpoint_readout_conclusion"]
    count = 0

    def less(left, right, message):
        nonlocal count
        require(left < F(right), message)
        count += 1

    def upper(record, bound, message):
        less(endpoints(record)[1], bound, message + " complete upper")

    left, right = map(F, root["exact_root_interval"])
    width = right - left
    require(width == F("9e-13"), "full original root width")
    less(F("9/50"), left - F("1/50"), "all six windows beyond metric support")
    u, v, u1, v1 = map(F, ("4e-18", "3.847e-7", "2e-17", "1.019e-6"))
    less(F("3.861e-18"), u, "complete first-component repair")
    less(F("1.970e-17"), u1, "complete first-angular repair")
    less(F("2e-7") * F("1.923") + F("3.861e-18"), v, "root v state bridge")
    less(F("2e-7") * F("5.438") / F("1.068") + F("1.970e-17"),
         v1, "root v angular bridge")
    U, V, U1, V1 = map(F, (".629", "6.407", "5.438", "5.438"))
    less(F(".628") + F("3.861e-18"), U, "strict repaired u value")
    less(F("6.406213") + F("3.861e-18"), V, "strict repaired v value")
    less(F("5.437241") + F("1.970e-17"), U1, "strict repaired angular values")

    Q, q, W, b, g, CI = map(F, ("1.049", "1.025", "1.432", "2", "7", "1.031"))
    selected = root["selected"]
    less(F("49.1638"), endpoints(selected["k_ratio_lower"])[0], "unchanged root ratio")
    upper(selected["q_squared_upper"], Q, "unchanged full q squared")
    upper(selected["eta_upper"], "1.253802", "old complete angular speed")
    less(Q, q*q, "full q upper")
    less(1 + Q, W*W, "full regular weight upper")
    less(F(17, 16), CI*CI, "complete physical primitive constant")
    less(F("1.253802") + g * (F("2e-7") + F("3.861e-18")),
         "1.253804", "new complete angular speed")
    less(F("1.253804"), F("13/10"), "same root principal weight gate")

    au, av = 2*U*u + u*u, 2*V*v + v*v
    bu, bv = U*u1 + U1*u + u*u1, V*v1 + V1*v + v*v1
    d1, d2 = b*(au + Q*av), 2*b*(bu + Q*bv)
    a0, a1 = 4*b*(au + Q*av), 8*b*(bu + Q*bv)
    l0 = 2*b*(U*v + V*u + u*v)
    l1 = 2*b*(U1*v + V*u1 + u1*v + U*v1 + V1*u + u*v1)
    A, dA = U1 + V1, u1 + v1
    B, dB = W*(U + U1) + Q*(V + V1), W*(u + u1) + Q*(v + v1)
    pm = 8*b*CI*(A*dB + B*dA + dA*dB)
    nm = 4*g*(Q*v1 + u1)
    delta_m = d1/2 + F(40, 3)*(d1 + d2) + 10*(a0 + a1) + 4*(q + W)*(l0 + l1) + pm + nm
    C, dC = W*U + Q*V, W*u + Q*v
    D, dD = F(".41")*(U1 + 128*U1) + V1/4, F(".41")*(u1 + 128*u1) + v1/4
    p0, n0 = 8*b*(C*dD + D*dC + dC*dD), 4*g*(Q*(v1 + 128*v1) + u1)
    delta_0 = F(21, 2)*d1 + 10*a0 + 4*(q + W)*l0 + p0 + n0
    less(delta_m, ".003253", "complete negative-one growth increment")
    less(delta_0, ".006290", "complete L2 growth increment")

    cases = {case["exact_radius"]: case for case in root["cases"]}
    require(set(cases) == set(LIMITS) and all(c["passed"] is True for c in cases.values()),
            "all six completed radii")
    for radius, limits in LIMITS.items():
        R = F(radius)
        length = R + width
        den0, denm = 1 - F(".006290")*length, 1 - F(".003253")*length
        less(F(0), den0, "positive ordinary energy denominator")
        less(F(0), denm, "positive negative-one energy denominator")
        bounds = cases[radius]["bounds"]
        values = (
            endpoints(bounds["H0"]["full_root_to_state"])[1] / den0,
            endpoints(bounds["Hminus1"]["full_root_to_state"])[1] / denm,
            endpoints(bounds["primitive_after_Hminus1"]["full_root_bracket_to_L2"])[1] / denm,
        )
        for value, limit in zip(values, limits):
            less(value, limit, "complete saved root-to-state/primitive value")

    cut = readout["cut_complete_radial_factors"]
    mlo, em = F("1.117244"), F("2.001e-7")
    less(mlo, endpoints(cut["complete_absolute_mean_lower"])[0], "complete cut mean lower")
    upper(cut["complete_absolute_mean_upper"], "1.119492", "complete cut mean upper")
    less(F("2e-7") + F("3.861e-18"), em, "complete root mean bridge")
    less(F(".668124"), endpoints(cut["q_lower"])[0], "complete cut q lower")
    upper(cut["q_upper"], ".723092", "complete cut q upper")
    less(F(".723092"), 1, "exact maximum at unscaled cut")
    ng_lo, ng_hi = F(".958234592"), F(".962284474")
    less(ng_lo, endpoints(cut["density_radial_factor_lower"])[0], "old cut density lower")
    upper(cut["density_radial_factor_upper"], ng_hi, "old cut density upper")
    less(F(".958234"), ng_lo/(1 + em/mlo)**2, "new cut density lower")
    less(ng_hi/(1 - em/mlo)**2, ".962285", "new cut density upper")
    less(F(1), F("1.224")**2 * F(".668124"), "true cut T norm")
    less(F(".962285")*F("1.224"), "1.178", "true cut physical density norm")

    den = 1 - F(".003253")*(F("1/200") + width)
    case = cases["1/200"]["bounds"]["primitive_after_Hminus1"]
    less(F("1.178")*endpoints(case["full_root_bracket_to_L2"])[1]/den,
         "13.280", "new complete cut root and impulse receiver")
    less(F("1.178")*endpoints(case["ordinary_L2_radial_source_to_L2"])[1]/den,
         ".9391", "new complete cut ordinary source receiver")
    upper(readout["waist_complete_radial_factors"]["q_upper"], ".925091",
          "original exact waist q upper")
    less(F(".925091"), F(".962")**2, "waist weighted entry")
    upper(readout["complete_strict_Hminus1_source_injection_upper"], "1.060693",
          "complete strict source injection")
    less(F(".962285")*F("1.224")*F("5.869")*F(".962"),
         "6.651", "new true-cut forward homogeneous receiver")
    less(F(".962285")*F("1.224")*F("5.869")*F("1.060693"),
         "7.333", "new true-cut forward source receiver")

    theta = F("2.165")*F("9.3e-5")*F(".234")
    upper(readout["root_or_affine_jump_to_waist_density_gain"], "2038.396874",
          "complete old root-to-waist product")
    upper(readout["ordinary_root_window_source_to_waist_density_gain"], "144.136426",
          "complete old root-source-to-waist product")
    less(F("2038.396874")/((1 - theta)*den), "2038.527",
         "new complete root-to-waist receiver")
    less(F("144.136426")/((1 - theta)*den), "144.146",
         "new complete root-source-to-waist receiver")
    less(F("92.666")*F("2.368e-6") + F("144.146")*F("1.255e-5")
         + F("2038.527")*F("3.028e-12"),
         ".002029", "complete zero-root negative residual column")
    print(json.dumps({
        "all_passed": True,
        "exact_rational_comparisons": count,
        "same_actual_root_background_for_all_abs_delta_le": "1e-10",
        "complete_original_radii": list(LIMITS),
        "new_true_cut_density_root_upper": "13.280",
        "new_true_cut_density_source_upper": ".9391",
        "new_root_to_waist_upper": "2038.527",
        "new_root_source_to_waist_upper": "144.146",
        "new_complete_negative_residual_incoming_upper": ".002029",
        "native_scans_old_growth_integrals_products_or_exponentials": 0,
        "positive_inverse_full_matching_or_nonlinear_geometry_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
