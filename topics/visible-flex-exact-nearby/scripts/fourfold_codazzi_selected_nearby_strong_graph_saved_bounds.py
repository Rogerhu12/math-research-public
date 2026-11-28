"""True strong high graph around the selected centre and its negative-window consequences."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
FILES = {
    "WLA": ("notes/complete_waist_lifting_ci/run-43749764738-1/execution.json", 25000,
        "936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d"),
    "cap": ("notes/cached_cap_intrinsic_ci/run-43674917925-1-complete-cap-cached-intrinsic/evidence/complete-cap-intrinsic-summary.json", 5275,
        "7a08e94850d66de1d9dba184df205a5a288436fbb0cc005edaa462261976a17f"),
    "QN": ("results/R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md", 32805,
        "1fe88442bb35d0280a54dc416014f59773f1777a1b74998eb9513052b2f5a15e"),
    "PH": ("results/R144-supplement-actual-positive-high-graph-for-compact-centres.md", 24110,
        "634706af859ac5c793a82e50cc93bf2044bb47d92c89310f77bde2d08a802a67"),
    "WP": ("results/R144-supplement-actual-whole-positive-raw-hybrid-fees.md", 6708,
        "f93dfd63242bcfc33fe8efae49c62ab7bcc93a9ec972fae03b2238c03fbb96e4"),
    "NHT": ("results/R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md", 8003,
        "6b4202ede35ed025bb52cd5abcb5a60089353436866a6e32dfac54f0ee5140d9"),
    "NBE": ("results/R149-supplement-nonlinear-background-negative-ordinary-response.md", 7654,
        "35b2075696ece5529e649bc373d81af4c6551cd1d76dea0aad57e5558649a2d0"),
    "OHR": ("results/R149-supplement-strong-physical-outer-residuals-and-complete-independent-right-hand-sides.md", 7715,
        "37f9e72dbdad3dbf19a2d6465424657991d2eb0f06320309bd7ce4dd0d4af387"),
    "NRO": ("results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md", 8294,
        "fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d"),
    "tail": ("notes/known_high_Z_tail_source_ci/run-43628921664-1-complete-known-high-Z-tail-source/evidence/complete-known-high-Z-tail-source-summary.json", 14387,
        "74e7b40d0eb4c79bf511a501467e73d80116d46990d1ab8e5b43f66f4fcd1b35"),
    "tail_receipt": ("notes/known_high_Z_tail_receipt_ci/run-43630093667-1-known-high-math-success-receipt/evidence/known-high-original-success-receipt.json", 12445,
        "cd7aa5f5c21509c629f8508bef21af4254e05716e2868e1804bce60e1ee583fa"),
    "body": ("notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-positive-N97-high-inverse-summary.json", 21555,
        "2da26c59fcbf212fc669cd29efdc9eb27489ae5a11f8dc51bea801b733ba9ef9"),
    "body_run": ("notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/process.json", 11040,
        "1a0be497981ed6e5f47546892c390fec5820b02671ff9eb83a37af47b26ca395"),
    "collar": ("notes/full_delta96_root_collar_ci/run-43606747196-1/consumers/process.json", 11340,
        "f919ecd9da5d447cf8950d1b267c28c7c33c2c396b21318b64a45317646745ae"),
    "outer": ("notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json", 23649,
        "769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6"),
    "Z": ("notes/exact_right_Z_endpoint_ci/run-43611611635-1/consumers/process.json", 92750,
        "9d55a6a01fb9a079c13f0379f1041cd2d61b30f1b31f701df2ebcbd45890f59d"),
    "K": ("notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json", 40659,
        "6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"),
    "helpers": ("scripts/fourfold_codazzi_negative_ordinary_response_saved_bounds.py", 10330,
        "88df151b7ecc9c22bff382cd96e647ba2ea1010baa6332b5dcc8a88baf9ea4b9"),
    "collar_formula": ("results/R133-supplement-full-real-delta96-positive-root-collar.md", 11453,
        "4a2a4f04009258cb9b794068c49fd5b31c77146fc14b4c8f115609055421c23a"),
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    docs = {}
    for key, (fn, size, dig) in FILES.items():
        raw = (TOPIC/fn).read_bytes()
        require(len(raw) == size and sha256(raw).hexdigest() == dig, "whole " + key)
        if fn.endswith(".json"):
            docs[key] = json.loads(raw)
    from fourfold_codazzi_negative_ordinary_response_saved_bounds import endpoints, exponential_upper
    def up(field):
        return endpoints(field)[1]
    body, out, z, collar = (docs[k] for k in ("body","outer","Z","collar"))
    ddoc = docs["K"]["actual_scientific_receipt"]
    tail = docs["tail"]
    require(body["complete"] and out["complete"] and z["mathematical_complete"] and collar["mathematical_complete"]
            and ddoc["complete"] and tail["complete"] and docs["tail_receipt"]["complete"]
            and body["native_sha256"] == docs["body_run"]["complete_native_sha256"]
            and out["native_sha256"] == docs["body_run"]["actual_full_delta_outer_native_sha256"]
            and out["original_complete_endpoint_native_sha256"] == z["native_sha256"]
            and out["explicit_direction_definition_sha256"] == tail["exact_continuous_direction_definition_sha256"]
            == ddoc["derived_continuous_response_definition_sha256"]
            and out["derived_definition_sha256"] == tail["derived_continuous_centre_definition_sha256"]
            == ddoc["derived_continuous_centre_definition_sha256"], "same completed whole physical sources")
    for key, field, count in (("outer","gates",25),("Z","mathematical_gates",14),
                              ("collar","mathematical_gates",19),("tail","gates",8)):
        gates = docs[key][field]
        require(len(gates) == count and all(g["passed"] for g in gates), "original gates "+key)
    require(tail["complete_known_high_bounds"] == docs["tail_receipt"]["original_complete_known_high_bounds"]
            and tail["complete_source_interval"] == ["0","25/8"] and tail["known_Z_exact_mode_support"] == 96
            and tail["background_exact_mode_support"] == 32, "whole saved high tail and its mathematical success")
    wl, cap = docs["WLA"]["actual_scientific_receipt"], docs["cap"]
    intrinsic = cap["complete_cap_intrinsic_constants"]
    core = wl["complete_positive_product_conclusion"]
    require(docs["WLA"]["complete"] and wl["complete"] and wl["proved"] and cap["complete"]
            and wl["mathematical_parameters"]["exact_core_interval"] == ["0","9/10"]
            and wl["mathematical_parameters"]["exact_parameter_half_width"] == "1/10000000000"
            and wl["complete_original_input_conclusion"]["original_small_input_sha256"]["D_execution"] == FILES["K"][2]
            and core["B_star_scope"] == "absolute beta times max(1,absolute K_delta), uniformly on the whole core"
            and core["G_star_scope"] == "absolute G_delta times max(1,absolute K_delta), uniformly on the whole core"
            and cap["exact_interval"] == ["9/10","25/8"]
            and cap["selected_cap_row_count"] == cap["completed_cap_rows"] == 1346
            and len(wl["gates"]) == 18 and len(cap["gates"]) == 9
            and all(g["passed"] for g in wl["gates"]+cap["gates"])
            and intrinsic["meanings"]["k_star"] == "max(1,sup_r K)"
            and intrinsic["meanings"]["b_star"] == "sup_r |beta|"
            and intrinsic["meanings"]["g_star"] == "sup_r gamma", "the adjoining original metric-product domains")
    b_positive = max(up(core["B_star"]),up(intrinsic["b_star"])*up(intrinsic["k_star"]))
    g_positive = max(up(core["G_star"]),up(intrinsic["g_star"])*up(intrinsic["k_star"]))
    tests = {}
    def test(name,left,right):
        require(left < right,name)
        tests[name] = True
    d, rho, ep = F("1e-10"), F("1e-7"), F("9e-10")
    qn_rho, qn_ep = F("1e-6"), F("1e-9")
    # Only the drift/frame weights QN really uses are needed inside the body.
    test("entire_degree96_w", (1+F(384,388))**5,F("3.2")**3)
    test("centre_to_true_weighted_state",F("3.2")*19*d+rho, qn_rho)
    test("centre_to_true_weighted_angular_derivative",F("3.2")*83*d+rho, qn_rho)
    test("exact_coordinate_relative_optical_mean",rho/(F("1.068")-F("3.861e-18")-19*d-rho),rho)
    test("actual_family_terminal_variation",ep/(F("5.8")-ep),rho)
    norms = z["norms"]["0"]["0"]
    endpoint_shift = 129**3*F("3.861e-18")+385**3*d*(up(norms["u"])+up(norms["v_including_mean"]))
    test("whole_selected_and_unknown_endpoint_inside_QN",endpoint_shift+ep,qn_ep)
    c = collar["fresh_coefficient_bounds"]
    test("root_optical_lower",F(1,2),endpoints(c["optical_speed_lower"])[0]-F("1.12")*rho)
    test("root_optical_upper",up(c["optical_speed_upper"])+F("1.12")*rho,F("1.26"))
    test("new_collared_kernel_base",F("9e-6")*(144+92*qn_rho),F(1,750))
    test("new_collared_kernel_minus",F("9e-6")*(F("432.18")+92*qn_rho),F(1,250))
    old = {v["homogeneous_angular_order"]:v["bounds"] for v in body["orders"]}
    # Dominance over the parameter-free old M32 remainder in the true reference.
    lam = 1/(1-rho)+9000*qn_rho
    for order, lim in ((0,F(".310")),(1,F(".801"))):
        test("selected_true_body_feedback_"+str(order),
             lam/(1-4*rho)*up(old[order]["interior_Volterra_norm"])+F(".0025"),lim)

    # Normalized changes of the infinite Fourier perturbation in the strong source.
    eps, eps1, diag = F("3e-6"),F("3e-4"),F("5e-5")
    test("tail_state_weight",1,eps**3*133**8)
    test("tail_derivative_weight",1,eps1**3*133**5)
    test("above96_mean_rank",1,diag**3*389**5)
    alpha, alpha1 = F("7.28")/3,4*F("7.28")
    # Each tuple carries full state/derivative, normalized state/derivative
    # tail paid directly, and state/derivative tail paid by the old T row.
    Q = (33,28,0,0,d*alpha,d*alpha1)
    Z = (139,606,0,0,alpha,alpha1)
    P = (1,1,eps,eps1,0,0)
    words = [(2,Q,P,Z),(2,P,Z,Q),(2,Q,Z,P),(rho,P,P,Z),(2*rho,P,Z,P)]
    uniform, tail_factor = 0,0
    for factor, a,b,h in words:
        def part(j):
            return ((a[j]*b[0]+a[0]*b[j])*(F(h[1])/4+h[0])+
                    a[0]*b[0]*(F(h[j+1])/4+h[j]))
        uniform += factor*b_positive*part(2)
        tail_factor += factor*part(4)
    uniform += g_positive*19*diag
    Htail = up(tail["complete_known_high_bounds"]["full_body"]["new_tail_only_L2_radial"])
    test("whole_positive_radial_length",F(25,8),F("1.768")**2)
    test("true_positive_high_nu_state_change",F("1.768")*uniform+tail_factor*Htail,9)

    # QN's complete zero-width physical angle chart at the ACTUAL new endpoint.
    U0,V0,U1,V1 = (145*F("1.643190e-9")+qn_ep,145*F("9.603792e-9")+qn_ep,
                     3336*F("1.643190e-9")+qn_ep,3336*F("9.603792e-9")+qn_ep)
    C,comp = 1/F("5.84"),F("1.000001")
    z6 = z["norms"]["1/32"]["0"]
    zn,zm = F("1.5")*up(z6["v_including_mean"]), abs(F(z["exact_independent_mean"]))
    xu = F("1.5")*up(z6["u"])
    I = (zn+zm*(1+V0/F("5.8")))/4
    cvar = comp*(C**2*zn+V1*C**3*I)
    bvar = comp*(C*xu+U0*C*C*zn+(U1*C*C+U0*V1*C**3)*I)
    test("true_exterior_Z_Robin",bvar+(1+F(".0012"))*cvar,F("1.23e-11"))
    test("true_exterior_Z_mean",zm/F("5.84")**2+F(".00015")*cvar,F("9.1e-16"))
    test("true_strong_external_Z_rhs",23*F("1.23e-11")+28*F("9.1e-16"),F("3e-10"))
    test("true_strong_interior_two_ports",F(".013070")**2+F(".183170")**2,F(".2")**2)
    test("true_strong_exterior_fourth_port",F("1.452083"),F("1.5"))

    # Nonlinear little positive root sliver in genuine raw low/high state units.
    b,g = F(".53"),F("7.3")
    m1 = b*15/4+g
    m0 = 3*b*15+b*14/2+g
    test("true_sliver_all_low",500+(384*m1+m0)*rho,501)
    test("true_sliver_all_high_to_low",F("11.6")+(b*15*(1+96)+m0)*rho,12)
    w,ws = F("9e-13"),F("9.49e-7")
    test("ordinary_root_sliver_width", w, ws**2)
    E = F("1.005")
    test("true_sliver_growth",exponential_upper(501*w),E)
    test("true_complete_root",F("25.944")+ws*E,F("25.95"))
    test("true_complete_collar_state",ws*(3+36*E*w),F("2.86e-6"))
    test("true_complete_sliver_jump",ws*E,F("9.54e-7"))
    fac = F("25.95")*F("9.00002")+F("2.86e-6")
    constant = F("1.755e-5")+w*E*(F("1.307204e-6")+28000*rho*ws)
    test("all_known_negative_positive_exterior_no_repeated_source",
         constant+fac*(F(".2")*F("1.254870e-9")+F("1.5")*F("3e-10")),F("1.774e-5"))
    test("true_background_complete_state_cost",5100+fac*F(".2")*9,5530)
    test("continuous_actual_sufficiency_example",F("25.95")*F(".000169")+F("2.86e-6")+
         F("1.774e-5")+5530*rho,F(".005"))
    print(json.dumps(dict(proved=True,checks=tests,whole_inputs={k:v[2] for k,v in FILES.items()},
        true_selected_centre_nearby_radius=str(rho),true_selected_independent_endpoint_radius=str(ep),
        positive_Hthird_high_nu_rate=9,strong_outer_nu="3e-10",known_complete_negative_cost="1.774e-5",
        nonlinear_increment_factor=5530,actual_matched_port_bounds_verified=False,
        actual_complete_nonlinear_family_proved=False,old_scientific_target_calls=0),sort_keys=True))


if __name__ == "__main__":
    main()
