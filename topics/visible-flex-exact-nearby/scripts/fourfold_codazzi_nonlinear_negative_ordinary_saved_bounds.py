"""Original positive fee rows, new nonlinear state/source/energy consequences only."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


TOPIC = Path(__file__).resolve().parents[1]
FILE = {
    "D_execution":("notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json",40659,
        "6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"),
    "D_manifest":("notes/2026-11-15-R133-selected-parameter-core-scalar-fees-CI-inputs.json",23692,
        "14271d7d61c70996092f105768ca29cc0dd355665be0becea4386441b38c907f"),
    "D_source":("scripts/fourfold_codazzi_selected_parameter_core_scalar_fees.py",25571,
        "827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"),
    "D_formula":("results/R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md",15214,
        "92fd222bbcc4495cce091cedee2628f83d014be23a40328a7292d47616621635"),
    "root_formula":("results/R133-supplement-full-real-large-root-Cauchy-two-source-windows.md",11952,
        "60ceb9c93e80984c67c2e9847e08815f83bc772f7bf2b8f397a57095617ef78b"),
    "root_actual":("notes/large_root_Cauchy_ci/run-43621934843-1-full-real-large-root-Cauchy/evidence/full-real-large-root-Cauchy-summary.json",50621,
        "238a85156791fac2516a23c5f9a6ea1253e648c341bedae139d1c2c5c47cbee5"),
    "root_process":("notes/large_root_Cauchy_ci/run-43621934843-1-full-real-large-root-Cauchy/process.json",11652,
        "82bf0467ccaaece38dcb606e537552e5c59dedf6ac8cb9cd4375458fab951c1c"),
    "NRO_proof":("results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md",8294,
        "fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d"),
    "NHT_proof":("results/R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md",8003,
        "6b4202ede35ed025bb52cd5abcb5a60089353436866a6e32dfac54f0ee5140d9"),
    "rational_helpers":("scripts/fourfold_codazzi_negative_ordinary_response_saved_bounds.py",10330,
        "88df151b7ecc9c22bff382cd96e647ba2ea1010baa6332b5dcc8a88baf9ea4b9"),
    "NHT_reader":("scripts/fourfold_codazzi_selected_high_source_tail_saved_bounds.py",8468,
        "dea4960fbf4b3388387c1c755b6c708373f019896c5d0d2abd49cf538670cb90"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    data = {}
    for role,(name,size,want) in FILE.items():
        raw = (TOPIC/name).read_bytes()
        require(len(raw) == size and sha256(raw).hexdigest() == want, "whole "+role)
        if name.endswith(".json"):
            data[role] = json.loads(raw)
    from fourfold_codazzi_negative_ordinary_response_saved_bounds import endpoints, exponential_upper
    def upper(field):
        return endpoints(field)[1]
    orig = data["D_execution"]
    actual = orig["actual_scientific_receipt"]
    raw = (json.dumps(actual,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                      allow_nan=False)+"\n").encode()
    require(orig["complete"] and str(orig["run_id"]) == "43713242980" and str(orig["run_attempt"]) == "1"
            and actual["complete"] and actual["proved"] and actual["actual_returncode"] == orig["actual_returncode"] == 0
            and actual["failure"] is None and len(actual["gates"]) == 12 and all(g["passed"] for g in actual["gates"])
            and len(raw) == orig["output_hashes"][0]["bytes"] == 27895
            and sha256(raw).hexdigest() == orig["output_hashes"][0]["sha256"]
            == "55076dbd11edf8aaae03d27d53e5cbf5bc8bffc8911568fecedce33d1d7bd80b"
            and actual["source_sha256"] == FILE["D_source"][2]
            and actual["input_manifest_sha256"] == orig["input_manifest_sha256"] == FILE["D_manifest"][2]
            and orig["actual_original_part_count"] == 40 and actual["complete_original_rows_verified"] == 7721,
            "entire original 40-part fee source and saved native conclusion")
    sub = actual["complete_scalar_fee_conclusions"]["fixed_negative_window"]
    r = data["root_actual"]
    rrun = data["root_process"]
    require(rrun["complete"] and str(rrun["run_id"]) == "43621934843" and str(rrun["run_attempt"]) == "1"
            and rrun["complete_native_sha256"] == r["native_sha256"] and r["complete"]
            and len(r["gates"]) == 8 and all(g["passed"] for g in r["gates"])
            and r["background_definition_sha256"] == actual["derived_continuous_centre_definition_sha256"]
            and r["explicit_direction_definition_sha256"] == actual["derived_continuous_response_definition_sha256"]
            and sub["exact_interval"] == ["0",r["exact_root_interval"][1]]
            and actual["parameters"]["exact_compact_support"] == ["1/20","9/50"],
            "one selected explicit background and the actual root and strict scopes")
    radius = F(1,200)
    lo,hi = map(F,r["exact_root_interval"])
    c = hi-radius
    cases = [x for x in r["cases"] if F(x["exact_radius"]) == radius]
    require(len(cases) == 1 and cases[0]["passed"] and c > F("9/50"),"one full genuine root window")
    root = cases[0]
    checks = {}
    def check(name,lhs,rhs):
        require(lhs < rhs,name)
        checks[name] = True
    d,t = F(1,10**10),F(1,10**7)
    E,H = 19*d,83*d
    U,D = 14*E+E**2,(7+E)**2
    M,N = upper(sub["maxima"]["M0"]),upper(sub["maxima"]["N_nu"])
    b,g = F(".53"),F("7.3")
    check("beta_times_intrinsic_weight",M,b*(3*U+(6*E+(7+E)*H)/2))
    check("gamma_times_intrinsic_weight",M,g*H)
    check("beta_times_parameter_K",N,4*(6*U/4+D*H/4+7*U+D*E))
    check("whole_intrinsic_principal_parameter",N,24*(6*E+(7+E)*H))
    states = actual["verified_global_state_bounds"]
    q,h,z,w = (upper(states[k]) for k in ("background_pair_A0","background_pair_angle_A0",
                                           "response_pair_A0","response_pair_angle_A0"))
    check("raw_selected_Q",q+d*z,7)
    check("raw_selected_Qphi",h+d*w,6)
    check("exact_degree32_weight",129,F("5.06")**3)
    check("exact_degree96_weight",385,F("7.28")**3)
    check("whole_background_weighted_state",F("5.06")*q+d*F("7.28")*z,33)
    check("whole_background_weighted_derivative",F("5.06")*h+d*F("7.28")*w,28)
    check("whole_direction_weighted_state",F("7.28")*z,139)
    check("whole_direction_weighted_derivative",F("7.28")*w,606)
    def source(a,ap,z,zp):
        a,ap,z,zp = map(F,(a,ap,z,zp))
        m1 = b*(2*a+1)/4+g
        m0 = 3*b*(2*a+1)+b*(ap+a+1)/2+g
        metric = 4*((2*a+1)*(ap/4+a)+(a+1)**2*F(5,4))+24*(ap+a+1)
        return m1*zp+m0*z,metric
    perturb,metric = source(33,28,139,606)
    raw_perturb,raw_metric = source(7,6,19,83)
    check("true_full_nu_strong_rate",perturb+metric,46000)
    check("true_root_nu_strong_rate",perturb,28000)
    check("true_strict_nu_ordinary_rate",raw_perturb+raw_metric,2600)
    check("true_Newton_strong_quadratic",b*(F(28,4)+F(33,2)+99+F(1,4)+1)+g,74)
    require(hi-lo == F("9e-13"),"true uncertainty bracket")
    qmax,W = F("1.03"),F("1.44")
    check("root_true_speed_margin",upper(root["eta_upper"])+g*t,F("1.3"))
    check("root_q",upper(root["q_squared_upper"]),qmax**2)
    check("root_W",upper(root["W_upper"]),W)
    check("changed_raw_energy_rate",F("3.5")*b*15+b*qmax**2*14/2+g*qmax/2,36)
    check("changed_root_energy_rate",F("1.5")*b*67+4*b*67+4*(qmax+W)*2*b*8
          +2*4*W*F(".41")*b*36+4*g,600)
    Up,Cp,Ap = F("8.22001"),F("6.53171"),F("25.944")
    check("strict_transfer_true_background",F("8.22")*exponential_upper(36*c*t),Up)
    check("root_transfer_true_background",F("6.531704")*exponential_upper(600*radius*t),Cp)
    check("true_root_atom",Cp**2*(radius+c*Up**2),Ap**2)
    check("true_strict_atom",c*Up**2,F("3.973")**2)
    check("known_fee_transfer_scaling",max(Up/F("8.22"),Ap/F("25.943")),F("1.00004"))
    check("known_source_on_true_operator",F("1.754e-5")*F("1.00004"),F("1.755e-5"))
    rem = 5100-28000*Ap*radius
    require(rem > 0,"positive remaining strict time cost")
    check("actual_nonlinear_extra_radial_source",(2600*Up)**2*c**3/3,rem**2)
    check("whole_positive_root_uncertainty",hi-lo,F("9.49e-7")**2)
    check("true_response_sufficient_example",Ap*F(".000170")+F("9.49e-7")+F("1.755e-5")+5100*t,F(".005"))
    print(json.dumps(dict(proved=True,whole_inputs={k:v[2] for k,v in FILE.items()},comparisons=checks,
        fixed_negative_window=["0",str(hi)],true_negative_background_radius=str(t),
        nonlinear_correction_angular_norm="sup radius max(Wiener_one_third(p),Wiener_one_third(p_phi))",
        strong_Newton_quadratic_upper=74,full_nu_strong_rate=46000,root_nu_strong_rate=28000,
        strict_nu_ordinary_rate=2600,whole_negative_new_nonlinear_budget_factor=5100,
        full_negative_root_atoms=str(Ap),full_negative_strict_atoms="3.973",narrow_positive_true_sup="9.49e-7",
        known_source_contribution="1.755e-5",actual_background_root_and_positive_trace_verified=False,
        actual_nonlinear_solution_or_full_qnu_threshold_proved=False,old_science_target_calls=0),sort_keys=True))


if __name__ == "__main__":
    main()
