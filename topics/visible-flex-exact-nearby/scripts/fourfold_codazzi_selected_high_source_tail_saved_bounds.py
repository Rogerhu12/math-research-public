"""Whole selected high Newton and nu source transfer, exact rational consequences."""
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
NRO = "scripts/fourfold_codazzi_negative_ordinary_response_saved_bounds.py"
OLD = "notes/known_high_Z_tail_source_ci/run-43628921664-1-complete-known-high-Z-tail-source/"
RECEIPT = "notes/known_high_Z_tail_receipt_ci/run-43630093667-1-known-high-math-success-receipt/"
EXTRA = {
    "NRO": (NRO,10330,"88df151b7ecc9c22bff382cd96e647ba2ea1010baa6332b5dcc8a88baf9ea4b9"),
    "NRO_proof": ("results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md",8294,"fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d"),
    "tail": (OLD+"evidence/complete-known-high-Z-tail-source-summary.json",14387,"74e7b40d0eb4c79bf511a501467e73d80116d46990d1ab8e5b43f66f4fcd1b35"),
    "tail_receipt": (RECEIPT+"evidence/known-high-original-success-receipt.json",12445,"cd7aa5f5c21509c629f8508bef21af4254e05716e2868e1804bce60e1ee583fa"),
    "tail_receipt_run": (RECEIPT+"process.json",13672,"cfa6bdfd47ce35bb191770d9ed237b86718de7127968f073f4eecf66822e8dae"),
    "tail_operator": ("scripts/fourfold_codazzi_known_high_source_from_Z_tail.py",16943,"f9104cce14a3f04ebe3271ed19085d9bf4bdc7f9f7c215ed79dd99244e7034bf"),
    "sp_operator": ("scripts/fourfold_codazzi_primitive_mean_strict_propagation.py",44298,"9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a"),
    "global_mean": ("results/R144-supplement-selected-metric-compact-residual-and-full-operator-fees.md",18995,"7091f40daea0522506a3d91974e97e4215906a76c22aa13b99ff0a9f3ca5c60a"),
    "global_direction": ("results/R133-supplement-selected-parameter-cap-row-transfer-with-unknown-high-input.md",13815,"81178d7471ee901ca77fc23ced9089ef6073931e66a597a0ca8741d22a55bd97"),
}


def require(ok,message):
    if not ok:
        raise ValueError(message)


def inputs(descriptors):
    result = {}
    for role,(path,size,sha) in descriptors.items():
        raw = (TOPIC/path).read_bytes()
        require(len(raw) == size and sha256(raw).hexdigest() == sha,"whole "+role)
        if path.endswith(".json"):
            result[role] = json.loads(raw)
    return result


def main():
    docs = inputs(EXTRA)
    spec = importlib.util.spec_from_file_location("_nro_saved_readers",TOPIC/NRO)
    nro = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nro)
    merged = {role:nro.FILES[role] for role in ("nw","sp","graph","graph_run")}
    docs.update(inputs(merged))
    orig,rec,rproc = (docs[k] for k in ("tail","tail_receipt","tail_receipt_run"))
    nw,sp,graph = (docs[k] for k in ("nw","sp","graph"))
    require(orig["complete"] and rec["complete"] and rproc["complete"]
            and rec["original_publication_failure_retained"] and rec["original_child_returncode"] == 0
            and rec["original_run"] == 43628921664 and rec["original_run_attempt"] == 1
            and rproc["run_id"] == "43630093667" and str(rproc["run_attempt"]) == "1"
            and len(rec["gates"]) == 6 and all(row["passed"] for row in rec["gates"])
            and rec["original_mathematical_gates"] == orig["gates"] and len(orig["gates"]) == 8
            and all(row["passed"] for row in orig["gates"])
            and rec["original_mathematical_source_sha256"] == orig["source_sha256"] == EXTRA["tail_operator"][2]
            and rec["original_native_sha256"] == orig["native_sha256"]
            and rec["original_small_summary_sha256"] == EXTRA["tail"][2]
            and rec["original_complete_source_rows"] == orig["complete_original_common_rows"] == 7721
            and rec["new_mathematical_children"] == rec["new_source_rows"] == 0,
            "original successful science, failed publication and later six-gate receipt")
    require(rec["original_complete_known_high_bounds"] == orig["complete_known_high_bounds"]
            and orig["background_exact_mode_support"] == 32 and orig["known_Z_exact_mode_support"] == 96
            and orig["known_output_mode_support"] == [97,160] and orig["complete_source_interval"] == ["0","25/8"]
            and orig["full_low193_and_independent_mean_unchanged"]
            and orig["derived_continuous_centre_definition_sha256"] == nw["parameters"]["continuous_centre_definition_sha256"]
            and orig["exact_continuous_direction_definition_sha256"] == nw["parameters"]["continuous_direction_definition_sha256"]
            and sp["actual_scientific_receipt"]["exact_family_identity"] == nw["reference_identity"]
            and sp["actual_scientific_receipt"]["source_sha256"] == EXTRA["sp_operator"][2]
            and graph["native_sha256"] == docs["graph_run"]["complete_native_sha256"]
            and graph["given_complete_head_positive_high_inverse_and_root_graph_proved"],
            "same whole sources, globally repaired selected family, same strong response")
    results = []

    def check(label,lhs,rhs):
        require(lhs < rhs,label)
        results.append(label)

    def upper(record):
        return nro.endpoints(record)[1]

    p = sp["actual_scientific_receipt"]["complete_strict_propagation_conclusion"]
    tail = orig["complete_known_high_bounds"]["full_body"]
    T,base = F("1.456147e-10"),F("1.254869143346e-9")
    check("whole_joint_tail_budget_without_selection_min",upper(tail["new_tail_only_L2_radial"]),T)
    check("original_high_strong_source",upper(tail["selected_known_high_H_one_third_L2_radial"]),base)
    max_dk = upper(p["complete_selected_scalar_maxima"]["metric_K_difference_upper"])
    check("signed_metric_coefficient_on_support",max_dk/F("1e-8"),F("10.48"))
    check("whole_metric_modulus",upper(p["new_entire_q_upper"]),F("1.03"))
    d = F("1e-10")
    check("derivative_of_true_metric",nro.exponential_upper(d)*((1+d)*F("10.48")+F("1.03")**2),F(12))
    H,DH = F(19),F(83)
    check("all_second_order_tail_slots",max(H,(6*H+DH/2)/3,2*H),F(52))
    check("all_third_order_tail_slots",max(H**2,H**2+H*DH/6),F(624))
    x = F(nw["selected_member_identity"]["absolute_delta_upper"])
    check("actual_selected_parameter",x,F("9.36826e-11"))
    d0 = 12*x**2+(1+12*x)*(52*x**2+624*x**3)
    d1 = 12*x+(1+12*x)*(104*x+1872*x*x)+12*(x+52*x*x+624*x**3)
    W,WL = F("10.484"),F("7.269")
    check("exact_full_288_frequency",1+1152**2,W**6)
    check("complete_low96_frequency",1+384**2,WL**6)
    nu,newton = F("1.254870e-9"),F("1.17560e-19")
    check("selected_full_nu_Hthird",base+W*T*d1,nu)
    check("selected_full_Newton_Hthird",x*base+W*T*d0,newton)
    c = F(p["exact_interval"][1])
    r,A,U,S = F("1/200"),F("25.943"),F("8.22"),F("1.307204e-6")
    root_weight = F(".070711")
    low_and_strict = F("13.404")
    check("root_radial_sqrt",r,root_weight**2)
    check("mixed_low_root_and_strict",c*c*U*U/2+A*A*r*WL*WL,low_and_strict**2)
    check("selected_negative_known_source",low_and_strict*S+A*root_weight*nu,F("1.754e-5"))
    require(graph["input_order"][1:3] == ["collar_ordinary_Hthird_source","body_ordinary_Hthird_source"],
            "same exact two strong ordinary columns")
    for name in ("full_root_outgoing_unstable_port","collar_Z_sup"):
        row = graph["response_rows"][name]
        require(len(row) == 7,"all high, mean, head and jump slots")
        check(name+"_ordinary_gain",sum(upper(slot)**2 for slot in row[1:3]),F(".182")**2)
    check("ordinary_nu_effect_per_strong_row",F(".182")*nu,F("2.284e-10"))
    check("ordinary_Newton_effect_per_strong_row",F(".182")*newton,F("2.140e-20"))
    check("nu_high_ordinary_to_negative_window",
          (F("25.95")*F("9.00002")+F("2.85e-6"))*F("2.284e-10"),F("5.34e-8"))
    check("whole_fixed_window_known_budget",F("1.754e-5")+F("5.34e-8")
          +F("9e-13")*F("1.005")*S,F("1.760e-5"))
    print(json.dumps(dict(proved=True,inputs={k:v[2] for k,v in {**EXTRA,**merged}.items()},
        new_comparisons=results,selected_nu_high_Hthird="1.254870e-9",
        selected_Newton_high_Hthird="1.17560e-19",nu_full_known_negative_source="1.754e-5",
        nu_full_known_negative_and_positive_high_source="1.760e-5",radial_domain=["0","25/8"],
        positive_only_restriction_for_strong_seven_ports=True,compact_metric_derivative_included=True,
        full_response_or_finite_high_feedback_proved=False,actual_qnu_threshold_proved=False,
        old_scientific_calls=0),sort_keys=True))


if __name__ == "__main__":
    main()
