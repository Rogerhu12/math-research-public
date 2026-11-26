#!/usr/bin/env python3
"""R144-PH: rational transfer of complete saved high-graph budgets.

No native coefficient, reference ODE, kernel sweep, Fourier matrix, target,
or nonlinear exterior solve is evaluated.  All new arithmetic consists of
the inequalities and finite positive combinations proved in PH.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path

from fourfold_codazzi_selected_metric_compact_residual_saved_bounds import (
    arb_text_endpoints, require,
)


BASE = Path(__file__).resolve().parents[1] / "notes"
SOURCES = {
    "body": (
        "full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/"
        "evidence/full-delta-complete-positive-N97-high-inverse-summary.json",
        "2da26c59fcbf212fc669cd29efdc9eb27489ae5a11f8dc51bea801b733ba9ef9"),
    "collar": (
        "full_delta96_root_collar_ci/run-43606747196-1/consumers/process.json",
        "f919ecd9da5d447cf8950d1b267c28c7c33c2c396b21318b64a45317646745ae"),
    "negative": (
        "full_delta_negative_one_positive_ci/"
        "run-43627228225-1-full-real-delta-negative-one-positive-graph/evidence/"
        "full-real-delta-negative-one-positive-graph-summary.json",
        "0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef"),
    "raw_outer": (
        "2026-11-14-R133-final-regular-Hs-Riccati-rational.json",
        "b62e06091e0d46198b80f0442da3627fe0ea79d23500bf823a9a96ee2f95e117"),
}


def read(name):
    path, digest = SOURCES[name]
    raw = (BASE / path).read_bytes()
    require(sha256(raw).hexdigest() == digest, "unchanged completed small " + name)
    doc = json.loads(raw)
    require(doc["complete"] is True, "complete " + name)
    return doc


def upper(record):
    return arb_text_endpoints(record)[1]


def lower(record):
    return arb_text_endpoints(record)[0]


def strict_decimal_upper(value, places=6):
    scale = 10**places
    numerator = (value.numerator * scale) // value.denominator + 1
    return F(numerator, scale)


def strict_sqrt_upper(value, places=6):
    require(value >= 0, "nonnegative exact squared bound")
    scale = 10**places
    floor = isqrt((value.numerator * scale * scale) // value.denominator)
    result = F(floor + 1, scale)
    require(result * result > value, "strict whole rational square-root upper")
    return result


def response_rows(*, chi, qb, Bf, qc, rc, Bc, Cb):
    """Exact PH seven-port formulas, retaining both signed cut inputs."""
    rb = chi * qb
    loop = rc * rb
    require(loop < 1, "new complete positive collar/body interface")
    sigma = 1 / (1 - loop)
    rows = {k: [] for k in ("body_state_sup", "root_outgoing", "raw_L2",
                            "outer_even_Hminus5over6_base",
                            "outer_even_Hminus5over6_negative")}
    for j in range(7):
        port = [F(int(i == j)) for i in range(7)]
        s, fc, fb, boundary, jc, js, ju = port
        x = sigma * (qc * s + qc * (Bc * fc + jc)
                     + js + rc * (qb * (Bf * fb + boundary) + ju))
        y = rb * x + qb * (Bf * fb + boundary) + ju
        out = rc * s + qc * y + qc * (Bc * fc + jc)
        body = qb * (x + Bf * fb + boundary)
        collar = qc * (s + y + Bc * fc + jc)
        raw2 = F(81, 1000000) * collar * collar + Cb * Cb * body * body
        rows["body_state_sup"].append(strict_decimal_upper(body))
        rows["root_outgoing"].append(strict_decimal_upper(out))
        rows["raw_L2"].append(strict_sqrt_upper(raw2))
        rows["outer_even_Hminus5over6_base"].append(
            strict_decimal_upper(F(5, 388) * body))
        rows["outer_even_Hminus5over6_negative"].append(
            strict_decimal_upper(4 * body))
    return loop, rows


def main():
    body, collar, negative, outer = (read(k) for k in SOURCES)
    require(body["full_delta_positive_high_inverse_proved"] is True
            and body["complete_original_rows"] == 4650
            and body["original_right_interfaces_preserved"] == 3594
            and len(body["orders"]) == 2, "complete original high body scope")
    require(collar["actual_returncode"] == 0 and collar["mathematical_complete"] is True
            and all(g["passed"] for g in collar["mathematical_gates"]),
            "all original root-collar gates")
    require(negative["negative_one_source_window_proved"] is True
            and negative["complete_negative_order_physical_outer_graph_proved"] is True,
            "same completed negative-one body and physical outer graph")
    require(len(outer["gates"]) == 33 and all(g["passed"] for g in outer["gates"])
            and outer["candidate_sha256"] == body["original_candidate_sha256"],
            "exact raw endpoint and its complete nonlinear physical graph")
    checks = 0

    def less(x, y, why):
        nonlocal checks
        require(x < F(y), why)
        checks += 1

    eps, tau, sigma = map(F, ("1.893e-7", "1.894e-7", "3.788e-7"))
    less(eps / (1 - eps), tau, "whole direct and inverse speed comparison")
    less((F("3.861e-18") + 19 * F("1e-10")) / F("5.84"),
         tau, "actual terminal form coefficient comparison")
    less(1 - (1 - eps) * (1 - tau), sigma, "whole damping comparison")
    less(4 * 45 / (1 - tau), 181, "new complete body K over W")

    U, V, U1, V1 = map(F, (".629", "6.407", "5.438", "5.438"))
    eu, ev, eu1, ev1 = map(F, ("4e-18", "3.847e-7", "2e-17", "1.019e-6"))
    dU2, dV2 = 2 * U * eu + eu * eu, 2 * V * ev + ev * ev
    dUV = U * ev + V * eu + eu * ev
    dS = dU2 + 4 * dV2
    dB = 4 * dS + 2 * (181 + 4) * dUV
    dFN = (U1 * eu + U * eu1 + eu * eu1
           + 4 * (V1 * ev + V * ev1 + ev * ev1)
           + 181 * (U1 * ev + V * eu1 + eu1 * ev)
           + 4 * (V1 * eu + U * ev1 + eu * ev1))
    dE = F(37, 2) * dS + (2 + F(8 * 9 * 32, 97)) * dB + F(8, 65) * dFN
    less(dE, ".004753", "all new complete degree32 body lower terms")
    less(1 / (1 - tau) + dE / 2, "1.003", "relative complete body high remainder")

    # Degree32 analytic strip 1/1024 costs exp(1/8)<8/7.
    # The latter follows from exp(x)<=1/(1-x), strictly for 0<x<1.
    scale = F(8, 7)
    us, vs, u1s, v1s = [scale * q for q in (U, V, U1, V1)]
    eus, evs, eu1s, ev1s = [scale * q for q in (eu, ev, eu1, ev1)]
    du2, dv2 = 2 * us * eus + eus * eus, 2 * vs * evs + evs * evs
    duv = us * evs + vs * eus + eus * evs
    beta, K, gamma = F(".211"), F(".00061"), F("1.12")
    da = beta * (3 * du2 + K * dv2)
    de = beta * (du2 + 3 * K * dv2)
    db = 2 * beta * duv
    dd = beta * (du2 + K * dv2)
    dn = beta / 2 * ((eu1s + ev1s) * (us + K * vs)
                    + (u1s + v1s) * (eus + K * evs)
                    + (eu1s + ev1s) * (eus + K * evs))
    dm = gamma * (eu1s + K * ev1s)
    df = ((eu1s + 4 * ev1s) * (us + vs)
          + (u1s + 4 * v1s) * (eus + evs)
          + (eu1s + 4 * ev1s) * (eus + evs))
    c = collar["fresh_coefficient_bounds"]
    for field, error, limit in (
        ("local_A", da, "1/2"), ("local_E", de, "3/10"),
        ("local_B_and_C", db, "1/2"), ("dphi", dd, "9/100"),
        ("d", dd / 4, "11/500"),
        ("raw_local", da + de + (1 + K) * db, 2),
        ("full_primitive", dn, 1), ("independent_mean_rank", dm, 3),
        ("global_frame_dyad", df, 34),
    ):
        less(upper(c[field]) + error, limit, "whole compact collar " + field)
    dEH = F(25, 2) * dd + 28 * (da + de + 5 * db) + 6 * beta * df
    less(dEH, ".0001", "complete actual collar high increment")
    less(upper(collar["fresh_full_high_remainder_upper"]) + dEH,
         "136569/1000", "unchanged complete collar high contract")
    less(F("1/2"), lower(c["optical_speed_lower"]) - gamma * F("2.001e-7"),
         "new collar speed lower")
    less(upper(c["optical_speed_upper"]) + gamma * F("2.001e-7"),
         "63/50", "new collar speed upper")
    less(F(29), F("59.74380437") / F("63/50"), "new optical K slope lower")
    less(F("60.465470") / F("1/2"), 122, "new optical K slope upper")

    # Raw endpoint budgets are dominated by the saved full-delta positive
    # budget FUNCTIONS, not inferred as lower bounds on a function value.
    outn = negative["actual_complete_negative_order_outer_constants"]
    for key, raw in (("actual_angle_displacement_Aone_eighth", "1.480385e-11"),
                     ("actual_U_Aone_eighth", "1.643190e-9"),
                     ("actual_Vnonmean_Aone_eighth", "9.603792e-9"),
                     ("actual_mean_upper", "7")):
        less(F(raw), lower(outn[key]), "whole saved outer upper budget dominates raw " + key)
    less(upper(outn["actual_mean_lower"]), "5.84461145233",
         "whole saved mean lower budget is conservative for raw endpoint")
    less(upper(outn["complete_high_reflection"]), ".000505292",
         "complete raw negative-window exterior reflection")

    orders = {o["homogeneous_angular_order"]: o["bounds"] for o in body["orders"]}
    rate_factor = F("1.003") / (1 - 2 * sigma)
    less(rate_factor * upper(orders[0]["interior_Volterra_norm"]) + F(".0000222"),
         ".305", "complete new order0 body and physical exterior gate")
    less(rate_factor * upper(orders[1]["interior_Volterra_norm"])
         + upper(outn["complete_high_reflection"]),
         ".792", "complete new negative-one body and physical exterior gate")
    frame_factor, source_factor = F("1.0000001"), F("1.000000474")
    less(1 / (1 - tau), frame_factor * frame_factor, "full reconstruction and jump frame factor")
    less(1 / ((1 - tau) * (1 - 2 * sigma)),
         source_factor * source_factor, "both ordinary-source branches")
    less(source_factor * upper(orders[0]["ordinary_source_to_unperturbed_Z_sup"]),
         ".126140", "complete new order0 source gain")
    less(source_factor * upper(negative["constants"]["body_unperturbed_source_gain"]),
         ".126141", "complete new negative-one source gain")
    for order in (0, 1):
        less(frame_factor * upper(orders[order]["raw_reconstruction_L2_multiplier"]),
             "2.517", "complete new physical raw reconstruction")
    less(frame_factor * upper(orders[0]["maximum_source_frame"]),
         "4.952399", "all new body Hthird affine jump entries")
    less(frame_factor * upper(negative["constants"]["uniform_body_raw_Hminus2over3_jump_to_Y_gain"]),
         "4.952410", "all new body Hminus2over3 affine jump entries")
    kstar = upper(negative["constants"]["source_homogeneous_Bessel_factor"])
    less(3 * kstar, "3.000007", "complete negative collar/cut jump entry")
    less(9 * kstar, "9.000020", "complete raw negative root input conversion")
    less(F(".009") * kstar, ".009000020", "complete negative collar ordinary source")

    base_loop, base_rows = response_rows(
        chi=F(".305"), qb=F(200, 139), Bf=F(".126140"),
        qc=F(750, 749), rc=F(1, 749), Bc=F(".009"), Cb=F("2.517"))
    neg_loop, neg_rows = response_rows(
        chi=F(".792"), qb=F(125, 26), Bf=F(".126141"),
        qc=F(250, 249), rc=F(1, 249), Bc=F(".009000020"), Cb=F("2.517"))
    less(base_loop, ".000586", "whole new base-order interface loop")
    less(neg_loop, ".015293", "whole new negative-order interface loop")
    less(base_rows["root_outgoing"][0], ".442", "whole new base-order root reflection")
    less(neg_rows["root_outgoing"][0], "3.902", "whole new negative-order root reflection")
    for rows, limit in ((base_rows, ".442"), (neg_rows, "3.902")):
        reflection = rows["root_outgoing"][0]
        old_root = (tau + reflection) / (1 - tau)
        less(old_root, limit, "exact triangular old-root reflection conversion")
        less(old_root, F("1.000002") * reflection,
             "uniform table enlargement also pays the root diagonal term")
    less((1 + 3 * tau) * (1 + 4 * tau), "1.000002",
         "complete state-output and prescribed-jump input frame conversion")
    less(frame_factor * (1 + 4 * tau), "1.000002",
         "triangular old-root output and prescribed-jump input conversion")

    def display(rows, neg):
        def exact_decimal(q):
            integer = q * 1000000
            require(integer.denominator == 1, "exact six-decimal rational upper")
            n = integer.numerator
            return str(n // 1000000) + "." + str(n % 1000000).zfill(6)
        output = {}
        for key in ("body_state_sup", "root_outgoing", "raw_L2"):
            output[key] = [exact_decimal(q) for q in rows[key]]
        key = "outer_even_Hminus5over6_" + ("negative" if neg else "base")
        output["outer_even_Hminus5over6"] = [exact_decimal(q) for q in rows[key]]
        return output

    print(json.dumps({
        "all_passed": True,
        "exact_rational_comparisons": checks,
        "new_complete_body_feedback": {"base_order": ".305", "negative_one": ".792"},
        "new_complete_root_reflection": {"base_order": ".442", "negative_one": "3.902"},
        "input_order": ["root_stable", "collar_source", "body_source", "body_external",
                        "collar_jumps", "cut_stable_jump", "cut_unstable_jump"],
        "base_order": display(base_rows, False),
        "negative_one": display(neg_rows, True),
        "new_compact_given_head_high_inverse_proved": True,
        "original_native_rows_reference_ODEs_or_kernel_sweeps": 0,
        "original_low193_reference_or_weights_changed": False,
        "full_low_high_physical_Schur_or_nonlinear_solution_proved": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
