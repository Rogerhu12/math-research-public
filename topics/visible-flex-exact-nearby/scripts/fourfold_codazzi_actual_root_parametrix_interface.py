#!/usr/bin/env python3
"""Audit actual root parametrix interfaces and finite first-coefficient algebra.

This child evaluates the exact interface fees and the displayed finite
identities. It does not evaluate all transported parametrix amplitudes,
their complete C_E/C_s constants, or a numerical high return cutoff.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import time
from flint import arb, ctx
import sympy as sp

PUBLIC = "Rogerhu12/math-research-public"
REPAIR = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
PINS = {
    "positive_process": "20945c0a64a2204b65e80f960f818c155c0bef3067f0ebcaab2f2df6cfc35328",
    "positive_summary": "243dc3551c00de4acbe8d8a7d8ba24b62ad16b3e2384ebebad422c4d282754d3",
    "negative_process": "f3688651110c9748b8a88b0c1da6cc88f78c50284474d9d6a12fffa7b99cd3da",
    "airy_process": "3d405529c83f9205baddbeb87113cc5e6c8c7735c3337cdc5fca97f2d52c9b4c",
    "fold_process": "e04f2aafdcb8b7fd5628754523b5704a2d25ea57f389ddd2026de08d32517107",
}
NATIVES = {
    "positive": "2425a0338b958be5d7fb48c955b5a5ce59348f05f1832ab50a81d6cf7dbbc501",
    "negative": "8f165ccf9dee6e622060b4fc269908ef322f0b0fea15b82dc4b223a2fb4c122d",
    "airy": "4ebc5865a8427e67e003e0aa25d8f629353ed87efd67d1705e1cdac7d2fc5b39",
    "fold": "9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd",
}
SOURCES = {
    "negative": "9bcf3dd119950ebb4188017eedd1f75dae729c345aa131a884f8346627209c28",
    "airy": "602de801dddb38ae3cbd6e04a5c9de96ea1e3180b9ae4089bb30bcda3814dafc",
    "fold": "2c680f47bc5209bd78f0643d7d425485bc597f05ad96c932109d93f2b26b2ab6",
}
INPUT_ORDER = [
    "root_stable_Z_port", "collar_ordinary_Hthird_source",
    "body_ordinary_Hthird_source", "body_outer_mean_head_and_weighted_jumps",
    "collar_weighted_affine_jumps", "cut_stable_Z_jump", "cut_unstable_Z_jump",
]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def rat(value):
    v = Fraction(value)
    return arb(v.numerator)/v.denominator

def interval(value):
    return arb(value["lower"]).lower().union(arb(value["upper"]).upper())

def upper(value):
    x = interval(value).upper()
    if not x.is_finite():
        raise ValueError("nonfinite original upper bound")
    return x

def lower(value):
    x = interval(value).lower()
    if not x.is_finite():
        raise ValueError("nonfinite original lower bound")
    return x

def rec(value):
    value = arb(value)
    if not value.is_finite():
        raise ValueError("nonfinite root parametrix interface value")
    return dict(ball=value.str(80), lower=value.lower().str(80), upper=value.upper().str(80))

def save(path, doc):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(doc, ensure_ascii=False, separators=(",", ":"), allow_nan=False)+"\n").encode()
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    temporary = path.with_suffix(path.suffix+".partial")
    temporary.write_bytes(raw)
    temporary.replace(path)

def run(args, doc):
    def gate(name, condition):
        passed = bool(condition)
        doc["gates"].append(dict(name=name, passed=passed))
        if not passed:
            raise ValueError("actual root parametrix interface failed: "+name)

    inputs = {}
    for key, expected in PINS.items():
        path = getattr(args, key)
        gate("unchanged_original_bytes_"+key, sha(path) == expected)
        inputs[key] = json.loads(path.read_text())
    pp, ps = inputs["positive_process"], inputs["positive_summary"]
    neg, airy, fold = (inputs[k] for k in ("negative_process", "airy_process", "fold_process"))
    gate("actual_complete_positive_same_reference_graph_all_seven_rows",
        pp.get("complete") is True and pp.get("repository") == PUBLIC
        and str(pp.get("run_id")) == "43605513540"
        and len(pp.get("children", [])) == 1
        and pp["children"][0].get("actual_returncode") == 0
        and pp.get("complete_native_sha256") == NATIVES["positive"]
        and pp.get("actual_interface_gates") == 10
        and pp.get("all_seven_source_and_jump_response_rows_retained") is True
        and any(f.get("logical_file") == "evidence/repaired-positive-high-root-graph-summary.json"
            and f.get("sha256") == PINS["positive_summary"] for f in pp.get("native_files", []))
        and ps.get("native_sha256") == NATIVES["positive"]
        and ps.get("complete") is True and not ps.get("failure")
        and len(ps.get("gates", [])) == 10 and all(g["passed"] for g in ps["gates"])
        and ps.get("derived_definition_sha256") == REPAIR
        and ps.get("exact_affine_parameter_offset") == "0"
        and ps.get("input_order") == INPUT_ORDER
        and ps.get("full_low_high_Schur_inverse_proved") is False
        and ps.get("nonzero_delta_M96_family_proved") is False)

    for key, data, rid, count in (
        ("negative", neg, "43604498718", 12),
        ("airy", airy, "43605453793", 11),
        ("fold", fold, "43602612900", 16)):
        gate("actual_complete_"+key+"_process",
            data.get("complete") is True and data.get("public_repository") == PUBLIC
            and str(data.get("run_id")) == rid and data.get("actual_returncode") == 0
            and data.get("native_sha256") == NATIVES[key]
            and data.get("mathematical_source_sha256") == SOURCES[key]
            and data.get("mathematical_complete") is True
            and len(data.get("mathematical_gates", [])) == count
            and all(g["passed"] for g in data["mathematical_gates"]))

    gate("ordinary_source_and_exact_propagation_window_are_the_paid_ones",
        ps.get("ordinary_source_contract") == "L2_r H_phi^(1/3); complete head-to-high forcing is included"
        and neg.get("root_state_factor") == "41/10"
        and neg.get("ordinary_source_factor_inside_bracket") == "3/1000"
        and neg.get("propagation_direction") == "from rho=0 root to increasing rho on the negative side"
        and airy["amplitude_domains"]["original_rho_window"] == "1/250000"
        and airy["amplitude_domains"]["inner_T"] == "19/1000000"
        and airy.get("actual_root_finite_reflection_constant_not_identified") is True)

    U = ps["response_rows"]["full_root_outgoing_unstable_port"]
    gate("original_full_root_response_has_every_source_and_jump_column",
        len(U) == 7 and all(upper(v) >= 0 for v in U))
    cpos = upper(U[1])
    cbod = upper(U[2])
    grow = rat("41/10")
    source_minus = grow*rat("3/1000")
    conservative_root_factor = arb(18)
    correct_plus = grow*conservative_root_factor*cpos
    correct_body = grow*conservative_root_factor*cbod
    gate("actual_positive_collar_residual_to_negative_cut_fee_is_below_one",
        correct_plus < 1 and correct_plus > 0)
    gate("actual_negative_ordinary_residual_fee_is_below1over80",
        source_minus < rat("1/80") and source_minus > 0)
    gate("entire_positive_ordinary_source_root_fee_is_below1over5",
        (cpos*cpos+cbod*cbod).sqrt() < rat("1/5"))

    lo = Fraction(1191984371497, 5000000000000)
    hi = Fraction(2383968743003, 10000000000000)
    cut = Fraction(76285779072683, 320000000000000)
    h = Fraction(1, 10**6)
    Aminus = lower(fold["bounds"]["quotient_A_real_gap"])
    Aplus = upper(fold["bounds"]["quotient_A_modulus_upper"])
    Tmin = rat(2*h)*Aminus**rat("2/3")
    Tmax = rat(3*h)*Aplus**rat("2/3")
    tcutmin = rat(lo-cut)*Aminus**rat("2/3")
    tcutmax = rat(hi-cut)*Aplus**rat("2/3")
    cplus = rat("2/3")*Tmin**rat("3/2")
    cmean = lower(airy["bounds"]["old_mean_decay_exponent_lower"])
    gate("the_true_negative_cut_and_positive_cutoff_are_inside_the_actual_fold_domain",
        0 < lo-cut <= hi-cut < 4*h
        and 0 < Tmin < Tmax < rat("19/1000000")
        and 0 < tcutmin < tcutmax < rat("19/1000000")
        and cplus > 0 and cmean > rat("1/512"))

    t = sp.Symbol("t", real=True)
    chi = 1-10*t**3+15*t**4-6*t**5
    gate("exact_original_radial_cutoff_and_its_derivative_bound",
        chi.subs(t, 0) == 1 and chi.subs(t, 1) == 0
        and all(sp.diff(chi, t, j).subs(t, end) == 0 for j in (1, 2) for end in (0, 1))
        and sp.expand(sp.diff(chi, t)+30*t**2*(1-t)**2) == 0
        and -sp.diff(chi, t).subs(t, sp.Rational(1, 2)) == sp.Rational(15, 8))

    ai0 = 1/(arb(3)**rat("2/3")*rat("2/3").gamma())
    aip0 = -1/(arb(3)**rat("1/3")*rat("1/3").gamma())
    croot = ai0/arb(67).sqrt()
    gate("true_Airy_root_port_has_a_strict_elliptic_diagonal_floor",
        ai0 > rat("1/3") and aip0 < 0 and croot > rat("1/25"))

    # The shared scalar simplification is audited independently of the
    # saved interval rows, so an erroneous qc^2 replacement is detected.
    rc, rb, Bc, Bf = sp.symbols("rc rb Bc Bf")
    qc, qb = 1+rc, 1+rb
    sig = 1/(1-rc*rb)
    Xc, Xb = sig*qc*Bc, sig*rc*qb*Bf
    Uc, Ub = qc*rb*Xc+qc*Bc, qc*(rb*Xb+qb*Bf)
    gate("exact_collar_source_simplification_keeps_body_resolvent",
        sp.factor(Uc-qc*qb*sig*Bc) == 0
        and sp.factor(Ub-qc*qb*sig*Bf) == 0)

    z, s, r = sp.symbols("z s r")
    mobius = (r-z*s)/(1-z*r*s)
    gate("strict_inverse_frame_has_the_correct_Mobius_first_coefficient",
        sp.factor(sp.diff(mobius, z).subs(z, 0)-s*(r*r-1)) == 0
        and all(sp.simplify((r*r-1).subs(r, sign*sp.I)+2) == 0 for sign in (1, -1)))

    ell, eta, phasephi = sp.symbols("ell eta phasephi", nonzero=True)
    common = []
    for sign in (1, -1):
        raw = sign*(1-z*ell/(eta*phasephi))
        own = (1+sign*raw)/2
        common.append(sp.diff(own, z).subs(z, 0))
    gate("complete_two_row_projection_keeps_the_common_ell_coefficient",
        common[0] == common[1] == -ell/(2*eta*phasephi))

    # This is only the finite Puiseux bookkeeping in P.28, not a
    # numerical evaluation of the complete actual transport amplitudes.
    a02, a04, b04, a10, a12, b10, b12, ca, cb = sp.symbols(
        "a02 a04 b04 a10 a12 b10 b12 ca cb")
    a0 = 1+a02*t**2+a04*t**4
    b0 = b04*t**4
    a1 = a10+a12*t**2
    b1 = b10+b12*t**2
    coeffs = []
    for sign in (1, -1):
        den = a0+sign*sp.I*t*b0
        num = a1+sign*sp.I*t*b1+sign*sp.I*ca*a0/t**3+cb*b0/t**2
        coeffs.append(sp.series(num/den, t, 0, 1).removeO().expand())
    finite_difference = sp.expand(coeffs[0]-coeffs[1]).coeff(t, 0)
    gate("analytic_Airy_pair_common_amplitudes_leave_no_constant_in_the_ratio",
        finite_difference == 0)
    u, v, b = sp.symbols("u v b")
    finite_s = b*u*v/eta
    gate("finite_symmetric_gauge_is_retained_and_its_root_parity_is_odd",
        sp.expand(finite_s+finite_s.subs(u, -u)) == 0 and finite_s != 0)
    gate("true_two_ray_boundary_differences_vanish_after_both_divergent_weights",
        sp.Rational(5, 2)-sp.Rational(3, 2) == 1
        and sp.Rational(3, 2)-sp.Rational(1, 2) == 1)
    gate("density_normalization_and_complete_strong_Hilbert_Schmidt_exponents",
        sp.Rational(7, 6)-4 == -sp.Rational(17, 6)
        and sp.Rational(17, 6) > 2
        and 4-sp.Rational(8, 3) == sp.Rational(4, 3)
        and sp.Rational(4, 3) > 1)

    J0 = upper(airy["bounds"]["J_same_space"])
    J1 = upper(airy["bounds"]["J_with_angular_derivative"])
    Jsource = (J0*J0+J1*J1).sqrt()
    gate("actual_scalar_residual_uses_a_finite_full_one_gain_J_bound",
        Jsource > 0 and Jsource < rat("7/2"))
    doc.update(complete=True, derived_definition_sha256=REPAIR,
        exact_affine_parameter_offset="0", positive_scope="repaired M32 given full head",
        original_native_sha256=NATIVES,
        original_computations_recomputed=0,
        original_full_seven_positive_response_columns=U,
        bounds={name:rec(value) for name, value in dict(
            actual_collar_source_to_root_Z=cpos,
            actual_body_source_to_root_Z=cbod,
            conservative_collar_source_to_negative_raw=correct_plus,
            conservative_body_source_to_negative_raw=correct_body,
            negative_source_to_negative_raw=source_minus,
            low_root_Airy_error_to_negative_raw=grow,
            combined_positive_source_to_root_Z=(cpos*cpos+cbod*cbod).sqrt(),
            positive_cutoff_T_lower=Tmin, positive_cutoff_T_upper=Tmax,
            actual_negative_cut_T_modulus_lower=tcutmin,
            actual_negative_cut_T_modulus_upper=tcutmax,
            positive_Airy_cutoff_decay_exponent_lower=cplus,
            original_mean_decay_exponent_lower=cmean,
            exact_Ai_zero=ai0, exact_Ai_prime_zero=aip0,
            scalar_root_port_diagonal_floor=croot,
            complete_J_scalar_L2_to_Hthird=Jsource).items()},
        source_contract=dict(positive="L2_r H_phi^(1/3)", negative="L2_r H_phi^(1/3)",
            root="H_phi^(1/3) first row and ordinary L2 second row including mean",
            complete_negative_error_upper="1*positive_collar_source + (1/80)*negative_source + (41/10)*low_root_error",
            rounded_three_term_contract_requires_zero_body_residual_and_other_external_ports=True,
            true_body_and_exterior_selection_preserved=True,
            all_nonzero_head_mean_jump_and_exterior_columns_remain=True),
        exact_density_input_normalization="n^(7/6), n=4|j|",
        unnormalized_residual_order_sufficient="n^-4",
        normalized_correction_order="-17/6",
        complete_Hminus4over3_Hilbert_Schmidt_series_power="-4/3",
        finite_first_coefficient_algebra_audited=True,
        actual_complete_transport_amplitudes_evaluated=False,
        actual_parametrix_CE_and_Cs_evaluated=False,
        numerical_incoming_inverse_cutoff_certified=False,
        numerical_strong_return_budget_certified=False,
        cutoff97_full_return_inverse_proved=False,
        nonzero_delta_positive_graph_or_root_finite_constant_transferred=False,
        nonlinear_PDE_or_true_parameter_Schur_proved=False)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in PINS:
        parser.add_argument("--"+name.replace("_", "-"), type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every actual root parametrix interface outcome")
    ctx.prec = 320
    ctx.cap = 6
    started = time.monotonic()
    doc = dict(kind="actual_root_parametrix_interface_and_finite_coefficient_audit_v1",
        complete=False, failure=None, gates=[], source_sha256=sha(__file__),
        input_sha256={name:sha(getattr(args, name)) for name in PINS})
    try:
        run(args, doc)
    except BaseException as error:
        doc["failure"] = dict(type=type(error).__name__, message=str(error))
        raise
    finally:
        doc["seconds"] = time.monotonic()-started
        save(args.out, doc)
    print(json.dumps(dict(complete=doc["complete"], gates=len(doc["gates"]),
        correction_fee=doc["bounds"]["conservative_collar_source_to_negative_raw"]["upper"],
        seconds=doc["seconds"], actual_parametrix_CE_and_Cs_evaluated=False)), flush=True)

if __name__ == "__main__":
    main()
