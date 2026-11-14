#!/usr/bin/env python3
"""Recover the complete R97 source-transfer arithmetic from pinned whole inputs.

This is a new recovery entry, not a claim that its bytes equal the original
successful fifth-window source. Read/hash the old originals first; regenerate
only if they are lost. All proof arithmetic uses Fraction and upward dyadics.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

EXPECTED = {
    "r83": "4ec6d30adb9eb639e658bcaa86873cfed0675ab975d3a8f92778888339f966b2",
    "r92": "9ef88cdeef25ed0dd688082e53b25b5f8aacda2bd67c9dada61c250cefa4052a",
    "r94": "5eb45673a9080ae251e77c3203cfc2142ba31850fc244c7e2c8500df774249bc",
    "r78": "9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930",
}

def p2(e):
    return F(1 << e) if e >= 0 else F(1, 1 << (-e))

def upper(x):
    if isinstance(x, bool):
        raise TypeError("Boolean is not a mathematical bound")
    if isinstance(x, (int, str)):
        return F(x)
    if not isinstance(x, dict):
        raise TypeError("Use exact fraction or dyadic records, never floats")
    if "upper" in x:
        return upper(x["upper"])
    if "numerator" in x and "denominator" in x:
        return F(int(x["numerator"]), int(x["denominator"]))
    if "mantissa" in x and "binary_exponent" in x:
        return F(int(x["mantissa"])) * p2(int(x["binary_exponent"]))
    raise ValueError("Unrecognized exact bound record")

def up(x, bits=192):
    x = F(x)
    if x < 0:
        raise ValueError("R97 positive arithmetic only")
    if not x:
        return F(0)
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < p2(e):
        e -= 1
    quantum = p2(e - bits + 1)
    y = x / quantum
    return ((y.numerator + y.denominator - 1) // y.denominator) * quantum

def record(x):
    v = up(x)
    den = v.denominator
    if den & (den - 1):
        raise ArithmeticError("Directed result is not dyadic")
    with localcontext() as ctx:
        ctx.prec = 28
        ctx.rounding = ROUND_CEILING
        shown = str(Decimal(v.numerator) / Decimal(den))
    return {"upper": {"mantissa": str(v.numerator),
                      "binary_exponent": -(den.bit_length()-1)},
            "display_upward": shown}

def cauchy(x):
    return {"uniform_value_upper": record(x),
            "first_derivative_product_norm_upper": record(4*x),
            "second_derivative_product_norm_pair_upper": record(64*x)}

def digest_bytes(b):
    return hashlib.sha256(b).hexdigest()

def read_verified(path, wanted):
    b = path.read_bytes()
    sha = digest_bytes(b)
    if sha != wanted:
        raise ValueError("Pinned complete input changed: " + str(path))
    d = json.loads(b, parse_float=str)
    if d.get("all_gates") is not True:
        raise ValueError("Prerequisite did not pass all gates: " + str(path))
    return d, {"path": str(path), "sha256": sha, "bytes": len(b)}

def transfer(a, delta, old, far, q2):
    direct = a + q2*delta + far
    bridge = (q2+1)*delta + 2*far
    return {"direct_complete_source": record(direct),
            "transverse_difference_from_zero": cauchy(bridge),
            "old_chosen_plus_complete_bridge": record(old+bridge),
            "chosen_complete_true_DN_minus_exact_linear": cauchy(min(direct, old+bridge)),
            "ratio_to_old_chosen": record(min(direct, old+bridge)/old)}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in EXPECTED:
        ap.add_argument("--"+key, type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--rss-kib", type=int, default=98304)
    a = ap.parse_args()
    if a.out.exists():
        raise FileExistsError("Use a fresh complete output path")
    began = time.monotonic()
    data, identities = {}, {}
    for key, wanted in EXPECTED.items():
        data[key], identities[key] = read_verified(getattr(a, key), wanted)
    old, constants = data["r83"], data["r92"]["constants"]
    scale = upper(constants["moving_centre_scale"])
    old_radius = upper(constants["old_R74_radius_coefficient"])
    new_radius = upper(constants["new_radius_coefficient"])
    lift = upper(constants["transverse_lift_budget"])
    rho = upper(constants["rho"])
    kt = upper(constants["transverse_unknown_lipschitz"])
    q = (new_radius+lift)/old_radius
    q2 = q*q
    rows = old["old_envelope_complete_correction_rows"]
    if [r["cell"] for r in rows] != list(range(12,225)):
        raise ValueError("Retain all213 complete old correction rows")
    es = [upper(r["bound"]) for r in rows]
    if [r["mode"] for r in old["selected_mode_rows"]] != list(range(2,93,2)):
        raise ValueError("Retain all46 original low modes")
    far = upper(old["whole46_complete_true_far_upper"])
    mode_rows = []
    for row in old["selected_mode_rows"]:
        av = upper(row["uniform_R74_auxiliary_source_Wsigma1_upper"])
        dv = upper(row["complete_difference_source_Wsigma1_upper"])
        ov = upper(row["chosen_complete_true_DN_minus_exact_linear_Wsigma1"]
                   ["uniform_value_upper"])
        tr = transfer(av, dv, ov, far, q2)
        mode_rows.append({"mode": row["mode"],
                          "old_auxiliary_source_Wsigma1": record(av),
                          "old_complete_difference_Wsigma1": record(dv),
                          "old_chosen_complete_Wsigma1": record(ov),
                          "new_complete_Wsigma1": tr})
    whole = {}
    for strip in ("Wsigma1", "Wtau_b1"):
        av = upper(old["whole46_auxiliary_source_"+strip+"_upper"])
        dv = upper(old["whole46_complete_difference_source_"+strip+"_upper"])
        ov = upper(old["whole46_chosen_true_DN_minus_exact_linear_"+strip]
                   ["uniform_value_upper"])
        whole[strip] = transfer(av, dv, ov, far, q2)
    factor = 1 + kt/old_radius
    high = {}
    for strip, row in data["r78"]["complete_coarse_trace_rows"].items():
        if strip not in ("outer", "head"):
            continue
        bands = row["high_bands_value_upper"]
        if len(bands) != 3:
            raise ValueError("Retain near/rest/infinite high blocks")
        all_old = upper(row["complete_high_balanced_P_K"]["uniform_value_upper"])
        values = [factor*upper(v) for v in bands]
        whole_high = factor*all_old
        high[strip] = {
            "bands": [{"name": name, "uniform": cauchy(v),
                       "transverse_global_lipschitz": record((kt/old_radius)*upper(oldv))}
                      for name, v, oldv in zip(("near94to184", "rest186to8190",
                                               "infinite8192up"), values, bands)],
            "complete_balanced_P_K": cauchy(whole_high),
            "complete_P": cauchy(whole_high/F(592)),
            "transverse_complete_balanced_global_lipschitz":
                record((kt/old_radius)*all_old)}
    beta_head = upper(whole["Wtau_b1"]["chosen_complete_true_DN_minus_exact_linear"]
                      ["uniform_value_upper"])
    bridge_head = upper(whole["Wtau_b1"]["transverse_difference_from_zero"]
                        ["uniform_value_upper"])
    gates = {
        "four_whole_pinned_input_hashes": len(identities) == 4,
        "all_prerequisite_gates": all(v["all_gates"] is True for v in data.values()),
        "same_scale_257_over256": scale == F(257,256),
        "old_radius256": old_radius == 256,
        "new_radius1048832": new_radius == 1048832,
        "full_transverse_lift4096": lift == 4096,
        "q4113": q == 4113,
        "q_squared16916769": q2 == 16916769,
        "all213_positive_complete_old_rows": len(es) == 213 and min(es) > 0,
        "all_new_paths_in_complete_domain": all(q*e < scale*rho for e in es),
        "all_cubic_comparisons": all(q*e*e < 3*scale*scale for e in es),
        "uniform_cubic_comparison": q*rho*rho < 3,
        "positive_complete_far_retained": far > 0,
        "far_below_saved_R83_display": far < F("5.633e-2341"),
        "all46_mode_caps": len(mode_rows) == 46,
        "low_Q_P_exactly_zero": old["low_Q_and_P_nonlinear_remainder_identically_zero"] is True,
        "same_transverse_lipschitz": kt == upper(data["r94"]["new_K"]),
        "complete_high_factor_below2704": factor < 2704,
        "both_high_strips": set(high) == {"head", "outer"},
        "new_low_head_improves_R94": beta_head < upper(data["r94"]["low_nonlinear_K_value"]),
        "new_low_head_below_1p17e48": beta_head < F("1.17e-48"),
        "transverse_bridge_below_1p79e60": bridge_head < F("1.79e-60"),
        "new_high_near_below_5p51e48":
            upper(high["head"]["bands"][0]["uniform"]["uniform_value_upper"]) < F("5.51e-48"),
        "new_high_rest_below_1p25e45":
            upper(high["head"]["bands"][1]["uniform"]["uniform_value_upper"]) < F("1.25e-45"),
        "new_high_infinite_below_1p53e54":
            upper(high["head"]["bands"][2]["uniform"]["uniform_value_upper"]) < F("1.53e-54"),
    }
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > a.rss_kib:
        raise MemoryError("Owned peak RSS exceeds declared guard")
    out = {
        "status": "Fresh complete recovery computation, not original fifth-window output identity",
        "author": "/root (GPT-6 Astra Pro, AI-assisted)",
        "all_gates": all(gates.values()), "gates": gates,
        "input_identities": identities,
        "source_sha256": digest_bytes(Path(__file__).read_bytes()),
        "parameter_domain": "R92 original20 complex polydisc times weighted-l1 transverse26 unit ball",
        "parameter_norm": "max(original20 normalized linf, transverse26 weighted-l1)",
        "cauchy_radius": "3/4",
        "old_radius": record(old_radius), "full_new_difference_radius": record(new_radius+lift),
        "q": record(q), "q_squared": record(q2),
        "maximum_old_e": record(max(es)), "maximum_new_e": record(q*max(es)),
        "all213_cubic_rows_paid": len(es),
        "true_far_added_once_per_whole_mass": record(far),
        "mode_rows": mode_rows, "whole_low46": whole,
        "high_factor": record(factor), "complete_high": high,
        "low_Q_and_P_nonlinear_remainder_identically_zero": True,
        "mean_and_single_cuff_bounds_retained_from_R94": True,
        "transverse_low_Schwarz_scope":
            "Difference from d=0 is at most bridge*norm(d); arbitrary pairs only after interior Cauchy",
        "no_Arb": True, "no_ODE": True, "no_new_source_integral": True, "no_Node": True,
        "middle_joint_feedback_cut_consistency_or_closed_surface_claimed": False,
        "elapsed_seconds": time.monotonic()-began, "owned_peak_rss_kib": rss,
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    with a.out.open("x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",",":"))
        f.write("\n")
    b = a.out.read_bytes()
    print(json.dumps({"event":"done", "all_gates":out["all_gates"],
                      "gates":len(gates), "output":str(a.out),
                      "bytes":len(b), "sha256":digest_bytes(b),
                      "seconds":out["elapsed_seconds"], "RSS_KiB":rss}), flush=True)
    if not out["all_gates"]:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
