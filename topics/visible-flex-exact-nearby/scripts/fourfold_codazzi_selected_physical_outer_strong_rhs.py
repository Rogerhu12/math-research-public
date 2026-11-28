"""Strong fixed-angle physical residuals and complete positive independent-data forcing."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
FILES = {
    "OA": ("notes/selected_physical_outer_values_ci/run-44769445246-1/selected-physical-outer-values.json", 33599,
        "db6f827c7eaa410a7769c673eba39838b6f35ba7e683c99cea62c8e0dcda3caa"),
    "OA_run": ("notes/selected_physical_outer_values_ci/run-44769445246-1/execution.json", 13544,
        "70ad7e1994a5ab228ac202d1ab1ce64a4db6ca0c279a2ae260c309479b357674"),
    "OA_formula": ("results/R141-supplement-selected-physical-outer-residual-values.md", 12786,
        "ed1967fa654c6951611a5a7aeb9322f20b7fab2a98a8a0f68bbbe668d2f94521"),
    "NP": ("results/R145-selected-nu-proposal-positive-source-and-outer-rows.md", 10867,
        "8fc5bf6263c30f327b4a146d309d093054dd1d97f7bc874cbae7a26502d6876c"),
    "Z": ("notes/exact_right_Z_endpoint_ci/run-43611611635-1/consumers/process.json", 92750,
        "9d55a6a01fb9a079c13f0379f1041cd2d61b30f1b31f701df2ebcbd45890f59d"),
    "outer": ("notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json", 23649,
        "769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6"),
    "outer_run": ("notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/process.json", 11040,
        "1a0be497981ed6e5f47546892c390fec5820b02671ff9eb83a37af47b26ca395"),
    "outer_formula": ("results/R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md", 21757,
        "03ddbc285ab03ee53a17ad3940d2c789695338854cf7cafdbfd38e75f3a11711"),
    "graph": ("notes/full_delta_positive_root_graph_ci/run-43617150971-1-full-real-delta-positive-root-graph/evidence/full-real-delta-positive-root-high-graph-summary.json", 27047,
        "410e8f07545c862425673a2c0cc37eebfc6f950217167f2b72c44d5a7b5676e7"),
    "graph_run": ("notes/full_delta_positive_root_graph_ci/run-43617150971-1-full-real-delta-positive-root-graph/process.json", 7437,
        "d35bb44e4cd7d933778d3234b6b0fe6c271fa9a8e744466a3fa9fd40f0e1f454"),
    "WOB": ("notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/actual-scientific-conclusion.json", 60416,
        "ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79"),
    "WOB_run": ("notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/execution.json", 15866,
        "b9022fe012e2e0f5db8186dda91a5ec1f2eb3222eb7af4ea02a9dd5ec41fdb57"),
    "WOB_formula": ("results/R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md", 41683,
        "f13024a72e09d9b388fc51eac39d675b656d4d75ee72cdafe449a1c325e92979"),
    "NHT": ("results/R149-supplement-selected-complete-high-Newton-and-nu-from-the-Z-tail.md", 8003,
        "6b4202ede35ed025bb52cd5abcb5a60089353436866a6e32dfac54f0ee5140d9"),
    "NRO": ("results/R149-supplement-ordinary-negative-response-from-the-strong-positive-root.md", 8294,
        "fb1e034f04c79c4a893cdd1407b7a590959f5383dddb1ea786abb34366dfa91d"),
    "NA": ("notes/positive_Newton_ordinary_source_ci/run-44765046846-1/positive-Newton-ordinary-source.json", 35749,
        "223461e2bf67ee35054b15a713928c5fa90bbf315f442c9f394a8e3403a20166"),
    "NA_run": ("notes/positive_Newton_ordinary_source_ci/run-44765046846-1/execution.json", 18244,
        "fb7782433762b9e1d4e69c78f319b7b5b15cfae827311cf600654e655bf89198"),
    "inverse_units": ("results/R133-supplement-rough-stable-inputs-and-complete-positive-head-feedback.md", 29127,
        "3e2742586113ccdc44023063caa99ab8b3b240667d01a018345529b11f656136"),
    "helpers": ("scripts/fourfold_codazzi_negative_ordinary_response_saved_bounds.py", 10330,
        "88df151b7ecc9c22bff382cd96e647ba2ea1010baa6332b5dcc8a88baf9ea4b9"),
}


def require(test, message):
    if not test:
        raise ValueError(message)


def saved():
    docs = {}
    for role, (name, size, digest) in FILES.items():
        raw = (TOPIC / name).read_bytes()
        require(len(raw) == size and sha256(raw).hexdigest() == digest, "whole " + role)
        if name.endswith(".json"):
            docs[role] = json.loads(raw)
    ids = {"OA_run": 44769445246, "Z": 43611611635, "outer_run": 43615531666,
           "graph_run": 43617150971, "WOB_run": 43844596176, "NA_run": 44765046846}
    for key, run in ids.items():
        process = docs[key]
        terminal = (process["scientific_complete"] and process["original_scientific_complete_flag"]
                    if key == "WOB_run" else process["complete"])
        require(terminal and str(process["run_id"]) == str(run)
                and str(process["run_attempt"]) == "1", "original process " + key)
    for role in ("OA", "NA", "WOB"):
        process, science = docs[role+"_run"], docs[role]
        name, size, digest = FILES[role]
        require(process["scientific_files"] == [dict(path="topics/visible-flex-exact-nearby/"+name,
                                                     bytes=size, sha256=digest)]
                and process["actual_child_returncode"] == science["actual_returncode"] == 0
                and process["failure"] is None and process["original_scientific_failure"] is None
                and process["problem_id"] == science["problem_id"] and not process["child_timeout"],
                "whole executed physical science and process " + role)
    for role in ("outer", "graph"):
        name, size, digest = FILES[role]
        files = docs[role+"_run"]["native_files"]
        require(sum(record["sha256"] == digest and record["bytes"] == size
                    and name.endswith("/"+record["file"]) for record in files) == 1,
                "whole native summary listed by original process " + role)
    for key, gates in (("OA", 18), ("NA", 18), ("Z", 14), ("outer", 25), ("graph", 10), ("WOB", 18)):
        doc = docs[key]
        rows = doc["mathematical_gates" if key == "Z" else "gates"]
        require(doc["complete"] and doc["failure"] is None and len(rows) == gates
                and all(x["passed"] for x in rows), "original complete gates " + key)
    oa, out, graph, z = (docs[k] for k in ("OA", "outer", "graph", "Z"))
    for key, role in (("endpoint_process", "Z"), ("family_summary", "outer"), ("wobsa_actual", "WOB")):
        item = oa["whole_old_evidence"][key]
        require(item["complete"] and item["identity"]["sha256"] == FILES[role][2], "common physical " + role)
    require(oa["parameters"]["direction_definition"] == z["explicit_direction_definition_sha256"]
            == out["explicit_direction_definition_sha256"] == graph["explicit_direction_definition_sha256"]
            and oa["parameters"]["centre_definition"] == out["derived_definition_sha256"] == graph["derived_definition_sha256"]
            and docs["outer_run"]["actual_full_delta_outer_native_sha256"] == out["native_sha256"]
            == graph["original_complete_outer_native_sha256"]
            and docs["graph_run"]["complete_native_sha256"] == graph["native_sha256"]
            and out["original_complete_endpoint_native_sha256"] == z["native_sha256"], "identical full original states")
    require(out["full_Hone_sixth_Riccati_graph_proved"] and graph["physical_minimum"] == 388
            and graph["unknown_head_is_supplied_as_a_source_not_set_to_zero"]
            and graph["input_order"][1:4] == ["collar_ordinary_Hthird_source", "body_ordinary_Hthird_source",
                                              "body_outer_mean_head_and_weighted_jumps"],
            "genuine strong physical inputs")
    return docs


def main():
    docs = saved()
    from fourfold_codazzi_negative_ordinary_response_saved_bounds import endpoints
    def up(row):
        return endpoints(row)[1]
    checked = {}
    def test(name, lhs, rhs):
        require(lhs < rhs, name)
        checked[name] = True
    oa, out, z, graph = (docs[k] for k in ("OA", "outer", "Z", "graph"))
    bounds, dn = out["bounds"], out["actual_DN"]
    M = F("5.84")
    U, V = F("1.646e-9"), F("9.616e-9")
    C = F(".172")
    test("true_mean_floor", M, endpoints(bounds["corrected_endpoint_mean_absolute_lower"])[0])
    test("whole_inverse_lift", up(bounds["actual_inverse_angle_displacement_Aone_sixtyfourth"]), F(1,64))
    test("full_moving_u_strip", up(bounds["corrected_moving_U_Aone_eighth"]), U)
    test("full_moving_v_strip", up(bounds["corrected_moving_Vnonmean_Aone_eighth"]), V)
    test("true_reciprocal_strip", 1/(M-V), C)
    X, Y = F("2.31e-11"), F("1.35e-10")
    mz = abs(F(z["exact_independent_mean"]))
    test("complete_u_direction", up(z["norms"]["1/32"]["0"]["u"]), X)
    test("complete_v_direction_including_mean", up(z["norms"]["1/32"]["0"]["v_including_mean"]), Y)
    test("nonzero_independent_mean", 0, mz)
    ph = C*(Y+mz*V/M)/4
    Bdot = C*X+U*C*C*Y+(16*U*C+16*U*V*C*C)*ph
    Cdot = C*C*Y+16*V*C*C*ph
    test("sixth_strip_embedding", 1, F(3,2)**6*F(6,64))
    test("strong_same_angle_nu_Robin", F(3,2)*(Bdot+(1+up(dn["Z_to_d_Hone_sixth"]))*Cdot), F("1.21e-11"))
    RR = oa["complete_new_scalar_records"]
    nr = up(RR["complete_selected_physical_Robin_Hminus5over6_upper"])
    nc = up(RR["complete_selected_independent_physical_mean_residual_upper"])
    ur, vr, Z1 = F("2e-12"), F("1e-11"), up(bounds["corrected_outer_physical_Z_theta_A0"])
    old = oa["copied_old_scalar_records"]["complete_nineteen_intervals"]
    # OA copied these small upper balls with their original full records.
    def oldup(key):
        v = old[key]
        return up(v["complete_record"] if "complete_record" in v else v)
    d = F(1,10**10)
    test("actual_real_u_endpoint", oldup("raw_U")+oldup("repair_Eu")+d*oldup("direction_Zu"), ur)
    test("actual_real_v_nonmean_endpoint", oldup("raw_V")+oldup("repair_Ev")+d*oldup("direction_Zv"), vr)
    jac = 1-vr/M
    Btheta = 384*(ur*C+ur*C*C*vr)/jac
    deriv = Btheta+(1+up(dn["Z_to_d_L2"]))*Z1+up(dn["fB_to_d_L2"])*16*F(1,2**60)
    test("complete_Newton_Robin_Hone", nr+deriv, F("2e-10"))
    test("complete_Newton_Robin_Hsixth", nr**5*F("2e-10"), F("1e-14")**6)
    wob = docs["WOB"]["copied_original_scalar_records"]
    rows = graph["response_rows"]
    ops = {"frame": F(".182"), "raw": F(".459")}
    for k in ("body_Z_sup", "collar_Z_sup", "full_root_outgoing_unstable_port", "entire_positive_raw_L2"):
        row = rows[k]
        israw = k == "entire_positive_raw_L2"
        test("disjoint_source_pair_"+k, up(row[1])**2 + up(row[2])**2, ops["raw" if israw else "frame"]**2)
        test("outer_source_"+k, up(row[3]), F("3.62" if israw else "1.439"))
    test("true_terminal_p", F(1,8), endpoints(bounds["actual_reference_outer_p_lower"])[0])
    rt, mt = up(bounds["ordinary_Robin_outer_source"]), up(bounds["independent_mean_outer_source"])
    direct, mport = up(wob["B_a"]), up(wob["C_a"])
    em, mu, muc = (up(wob[k]) for k in ("E_minus", "mu_minus", "mu_C"))
    L = up(wob["L_star"])
    lowN = up(docs["NA"]["complete_new_scalar_records"]["complete_positive_selected_Newton_low193_L2_upper"])
    estimates = {}
    inputs = (("Newton", F("1e-14"), nr, nc, F("1.17560e-19"), lowN,
               ("2.2e-13","3.2e-13","8.0e-13","7.051e-8","9e-15")),
              ("nu", F("1.21e-11"), F("9e-12"), F("4e-18"), F("1.254870e-9"), F("2.9476e-5"),
               ("2.55e-10","6.0e-10","1.51e-9","2.958e-5","6.31e-11")))
    for key, strong, weak, mean, high, low, caps in inputs:
        B, frame, raw, lowtotal, right = map(F,caps)
        test(key+"_whole_strong_exterior_input", rt*strong+mt*mean, B)
        test(key+"_actual_high_frame", ops["frame"]*high+F("1.439")*B, frame)
        test(key+"_actual_raw_positive_body", ops["raw"]*high+F("3.62")*B, raw)
        test(key+"_actual_whole_low_forcing", low+L*raw, lowtotal)
        yh = 4*frame/388
        odd = direct*weak+mport*mean+em*yh
        evenmean = muc*mean+mu*yh
        test(key+"_actual_whole_charted_right97", odd**2+evenmean**2, right**2)
        estimates[key] = dict(physical_Robin_H_one_sixth=str(strong), high_frame=str(frame),
                              ordinary_high_raw_L2=str(raw), combined_low_ordinary=str(lowtotal),
                              charted_right97=str(right), direct_strong_exterior_input=str(B))
    extra = (F("25.95")*F("9.00002")+F("2.85e-6"))*F("1.439")*F("2.55e-10")
    test("selected_known_negative_plus_positive_sources_and_exterior", F("1.760e-5")+extra, F("1.769e-5"))
    print(json.dumps(dict(proved=True, source_columns=estimates, rational_comparisons=checked,
        negative_known_sources_and_high_exterior="1.769e-5", whole_inputs={k:v[2] for k,v in FILES.items()},
        independent_height_and_root_retained=True, actual_matched_root_or_full_inverse_proved=False,
        actual_true_nonlinear_solution_proved=False, old_producer_calls=0),sort_keys=True))


if __name__ == "__main__":
    main()
