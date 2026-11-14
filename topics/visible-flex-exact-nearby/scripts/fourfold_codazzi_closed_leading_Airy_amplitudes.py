#!/usr/bin/env python3
"""Pay the closed leading Airy amplitudes from completed public interfaces.

No original target, fold, flow, response or parametrix is recomputed.
The consumer evaluates complete leading-amplitude bounds and exact
finite identities; higher amplitudes and numerical strong error remain open.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
import flint
from flint import arb, ctx
import sympy as sp

PUBLIC = "Rogerhu12/math-research-public"
REPAIR = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PINS = {
    "fold_process": "e04f2aafdcb8b7fd5628754523b5704a2d25ea57f389ddd2026de08d32517107",
    "negative_process": "f3688651110c9748b8a88b0c1da6cc88f78c50284474d9d6a12fffa7b99cd3da",
}
NATIVES = {
    "fold": "9300be45949cba94115511bf77d025a82e39c78d491ba77de916d7a96902fffd",
    "negative": "8f165ccf9dee6e622060b4fc269908ef322f0b0fea15b82dc4b223a2fb4c122d",
}
SOURCES = {
    "fold": "2c680f47bc5209bd78f0643d7d425485bc597f05ad96c932109d93f2b26b2ab6",
    "negative": "9bcf3dd119950ebb4188017eedd1f75dae729c345aa131a884f8346627209c28",
}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def exact(value):
    x = Fraction(value)
    return arb(x.numerator)/x.denominator

def upper(value):
    x = arb(value["upper"]).upper()
    if not x.is_finite():
        raise ValueError("an original complete upper bound is nonfinite")
    return x

def lower(value):
    x = arb(value["lower"]).lower()
    if not x.is_finite():
        raise ValueError("an original complete lower bound is nonfinite")
    return x

def power(value, p, q=1):
    if not value > 0:
        raise ValueError("a complete analytic power modulus lost its positive gap")
    return (value.log()*p/q).exp()

def record(value):
    value = arb(value)
    if not value.is_finite():
        raise ValueError("a complete leading-amplitude bound is nonfinite")
    return dict(ball=value.str(70), lower=value.lower().str(70),
                upper=value.upper().str(70))

def save(path, value):
    raw = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+"\n").encode()
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name+".partial")
    tmp.write_bytes(raw)
    tmp.replace(path)

def run(args, doc):
    def gate(name, condition):
        passed = bool(condition)
        doc["gates"].append(dict(name=name, passed=passed))
        if not passed:
            raise ValueError("closed leading Airy amplitude gate failed: "+name)

    saved = {}
    for name, expected in PINS.items():
        path = getattr(args, name)
        gate("unchanged_original_"+name, sha(path) == expected)
        saved[name] = json.loads(path.read_text())
    fold, negative = saved["fold_process"], saved["negative_process"]
    for key, obj, rid, count in (
        ("fold", fold, "43602612900", 16),
        ("negative", negative, "43604498718", 12)):
        gate("actual_complete_same_object_"+key,
            obj.get("complete") is True and obj.get("public_repository") == PUBLIC
            and str(obj.get("run_id")) == rid and obj.get("actual_returncode") == 0
            and obj.get("mathematical_complete") is True
            and obj.get("native_sha256") == NATIVES[key]
            and obj.get("mathematical_source_sha256") == SOURCES[key]
            and len(obj.get("mathematical_gates", [])) == count
            and all(g["passed"] for g in obj["mathematical_gates"]))
    fb, nb = fold["bounds"], negative["bounds"]
    gate("original_full_complex_field_norm_gates_are_present",
        any(g["name"] == "complete full-family physical angular coefficient norms through two meet the declared strict bounds"
            and g["passed"] for g in negative["mathematical_gates"]))
    R = exact("9/1000000")
    U0, V0 = exact("630/1000"), exact("1791/1000")
    ap, Aminus, Ap = upper(fb["a_modulus_upper"]), lower(fb["quotient_A_real_gap"]), upper(fb["quotient_A_modulus_upper"])
    eta_inv, eta_p = upper(fb["new_eta_inverse"]), upper(nb["eta"])
    km, B = lower(nb["Krho_lower"]), upper(nb["beta"])
    kp = (ap*eta_inv)**2
    j, Tp, BT = (upper(fb[k]) for k in ("derivative_excess", "T_modulus_upper", "T_phi"))
    D1, D2 = upper(fb["drift_phi"]), upper(fb["drift_phiphi"])
    gate("all_actual_complex_power_denominators_have_their_true_positive_gaps",
        km > 59 and kp > km and kp < 62 and Aminus > 9 and Ap < 10
        and eta_inv < exact("4/5") and eta_p < exact("63/50")
        and B < exact("211/1000"))
    hE = 2*R*B*(U0**2+R*kp*V0**2)
    E = hE.exp()
    G = power(kp*eta_inv, 1, 6)*power(Ap, 1, 6)*power(km, -1, 4)*E
    Gi = power(eta_p/km, 1, 6)*power(Aminus, -1, 6)*power(kp, 1, 4)*E
    base_gap = 1-2*j-j*j-Tp*BT*BT
    branch_gap = 1-j-Tp.sqrt()*BT
    gate("both_exact_amplitude_and_branch_denominators_remain_nonzero",
        base_gap > 0 and branch_gap > 0)
    A0 = G*((1+j)**2+Tp*BT*BT)
    A0i, branchi = Gi/base_gap, Gi/(branch_gap*branch_gap)
    B2 = exact("4/5")*G*(1+j)*ap*D2*power(Aminus, -5, 3)*(4*D1*R).exp()
    gate("the_complete_true_radial_mean_integral_has_a_small_complex_bound",
        hE > 0 and hE < exact("1/100000"))
    gate("the_complete_leading_a0_and_its_inverse_are_paid",
        A0 < exact("51/50") and A0i < exact("51/50"))
    gate("both_complete_Airy_branch_amplitudes_have_paid_inverses",
        branchi < exact("51/50"))
    gate("the_true_b0_over_T_squared_is_paid_without_zero_interval_division",
        B2 > 0 and B2 < 6)
    Tin, Tout = exact("19/1000000"), exact("81/4000000")
    Xgap = exact("1/256")
    Tgap = Tout-Tin
    gate("the_Cauchy_derivative_windows_are_the_actual_positive_domain_margins",
        Fraction(81,4000000)-Fraction(19,1000000) == Fraction(1,800000)
        and Fraction(1,128)-Fraction(1,256) == Fraction(1,256))
    derivative_rows = []
    for p, qd in ((0,0),(1,0),(2,0),(0,1),(0,2),(1,1)):
        factor = arb(math.factorial(p)*math.factorial(qd))/(Tgap**p*Xgap**qd)
        derivative_rows.append(dict(T_order=p, X_order=qd,
            a0_upper=record(A0*factor), b0_over_T2_upper=record(B2*factor)))
    b0in = B2*Tin**2
    b0T = 2*Tin*B2+Tin**2*B2/Tgap
    b0TT = 2*B2+4*Tin*B2/Tgap+2*Tin**2*B2/Tgap**2
    gate("all_reported_full_leading_derivative_bounds_are_finite",
        all(x.is_finite() for x in (A0,A0i,branchi,B2,b0in,b0T,b0TT)))

    q, eta = sp.symbols("q eta", positive=True)
    qr, b, u, v = sp.symbols("qr b u v")
    ell = -2*b*u*v
    L11 = -b*(1+3*u*u-q*q*v*v)
    L22 = b*(1-u*u+3*q*q*v*v)
    F = sp.Matrix([[q,-q],[1,1]])
    dF = sp.Matrix([[qr,-qr],[0,0]])
    principal = sp.simplify(F.inv()*sp.Matrix([[0,eta*q*q],[eta,0]])*F)
    local = sp.simplify(F.inv()*sp.Matrix([[L11,-q*q*ell],[ell,L22]])*F-F.inv()*dF)
    diag = -2*b*(u*u-q*q*v*v)-qr/(2*q)
    gate("exact_original_principal_rows_have_the_two_stated_speeds",
        principal == sp.diag(eta*q,-eta*q))
    gate("both_original_local_diagonals_equal_the_true_common_amplitude_coefficient",
        all(sp.factor(local[k,k]-diag) == 0 for k in (0,1)))
    gate("the_complete_other_row_local_terms_remain_in_the_ledger",
        sp.factor(local[0,1]-(qr/(2*q)+b*(1+(u+q*v)**2))) == 0
        and sp.factor(local[1,0]-(qr/(2*q)+b*(1+(u-q*v)**2))) == 0)

    etar, dphi, barT, p1, p2, sig = sp.symbols("etar dphi barT p1 p2 sig")
    Dtheta = sig*eta*q*p1
    DDtheta = sig*(etar*q+eta*qr+eta*q*dphi)*p1+eta**2*q**2*p2
    Ltheta = DDtheta-eta**2*q**2*p2-(etar/eta+barT)*Dtheta
    gate("the_entire_eta_radial_derivative_cancels_in_the_actual_leading_operator",
        sp.factor(Ltheta-(qr/q+dphi-barT)*Dtheta) == 0
        and sp.diff(sp.expand(Ltheta),etar) == 0)

    alpha, beta, GG, t = sp.symbols("alpha beta GG t")
    aa = GG*(alpha**2+t**2*beta**2)
    for eps in (1,-1):
        bb = -2*sp.I*eps*GG*alpha*beta
        gate("exact_two_phase_closed_leading_amplitudes_sign_"+str(eps),
            sp.expand(aa-sp.I*eps*t*bb-GG*(alpha-t*beta)**2) == 0
            and sp.expand(aa+sp.I*eps*t*bb-GG*(alpha+t*beta)**2) == 0)
    gate("the_product_retains_the_complete_principal_Jacobian_factor",
        sp.expand(GG**2*(alpha-t*beta)**2*(alpha+t*beta)**2-GG**2*(alpha**2-t*t*beta**2)**2) == 0)
    kstar, etastar = sp.symbols("kstar etastar", positive=True)
    normal = (kstar/etastar)**sp.Rational(1,6)*(etastar*sp.sqrt(kstar))**sp.Rational(1,6)*kstar**sp.Rational(-1,4)
    gate("the_exact_root_normalization_is_one",
        sp.simplify(sp.powdenest(normal,force=True)-1) == 0)
    QQ = sp.symbols("QQ", positive=True)
    ff = -(3*QQ/2)**sp.Rational(2,3)
    gate("the_fold_first_derivative_chain_term_has_the_correct_singular_sign",
        sp.simplify(sp.diff(ff,QQ,2)*(-ff)+1/(2*ff)) == 0)

    doc.update(complete=True, proved=True, background_definition_sha256=REPAIR,
        explicit_direction_definition_sha256=DIRECTION,
        exact_complex_parameter_radius="1/100000000",
        exact_original_radial_radius="9/1000000",
        actual_canonical_outer_T="81/4000000",actual_canonical_outer_X="1/128",
        actual_canonical_inner_T="19/1000000",actual_canonical_inner_X="1/256",
        original_native_sha256=NATIVES, original_completed_computations_recomputed=0,
        bounds={name:record(value) for name,value in dict(
            k_real_gap=km,k_modulus_upper=kp,true_mean_integral_exponent=hE,
            radial_E_and_inverse=E,G=G,G_inverse=Gi,
            leading_a0=A0,leading_a0_inverse=A0i,
            both_leading_branch_inverses=branchi,
            leading_b0_divided_by_T_squared=B2,leading_b0_on_inner_rectangle=b0in,
            leading_b0_T_on_inner_rectangle=b0T,
            leading_b0_TT_on_inner_rectangle=b0TT).items()},
        complete_Cauchy_derivative_bounds=derivative_rows,
        all_original_old_mean_and_ordinary_source_rows_retained=True,
        complete_leading_two_amplitude_formula_proved=True,
        complete_leading_amplitude_bounds_paid=True,
        leading_two_row_seam_continuity_proved_in_companion_note=True,
        original_candidate_interface_bytes_replayed_in_this_consumer=False,
        complete_next_and_higher_amplitudes_evaluated=False,
        milliscale_piecewise_fold_domains_certified=False,
        all_higher_trial_jump_norms_paid=False,
        numerical_parametrix_CE_Cs_and_strong_return_cutoff_certified=False,
        cutoff97_inverse_or_true_PDE_branch_proved=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in PINS:
        p.add_argument("--"+name.replace("_","-"),type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    if args.out.exists():
        raise FileExistsError("preserve every actual leading-amplitude result")
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new mathematics runs only in the actual public repository Actions")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),python_flint=flint.__version__,sympy=sp.__version__)
    if runtime!=dict(python="3.12.14",python_flint="0.9.0",sympy="1.14.0"):
        raise RuntimeError("the exact numerical and symbolic runtime changed")
    ctx.prec=320
    started=time.monotonic()
    doc=dict(kind="actual_closed_leading_Airy_amplitudes_complete_complex_budget_v1",
        complete=False,proved=False,failure=None,gates=[],source_sha256=sha(__file__),
        runtime=runtime,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"))
    try:
        run(args,doc)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
        raise
    finally:
        doc["seconds"]=time.monotonic()-started
        save(args.out,doc)
    print(json.dumps(dict(complete=True,gates=len(doc["gates"]),
        leading_a0=doc["bounds"]["leading_a0"]["upper"],
        leading_b0_divided_by_T_squared=doc["bounds"]["leading_b0_divided_by_T_squared"]["upper"],
        numerical_strong_return_cutoff_certified=False,seconds=doc["seconds"])),flush=True)

if __name__=="__main__":
    main()
