#!/usr/bin/env python3
"""New exact physical-angle cap world-anchor combinations; no old targets.

Consume the entire original C0 geometry native and complete already-successful
cap-intrinsic summary/process. Only new PWA inequalities are evaluated. No
coefficient producer, radial integral, residual target or old iteration runs.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import re


GEOMETRY_SHA = "00efc0322a9aa82cd1f234899599ed3fbaff87edd35b8c9ac1331b229b276a55"
SUMMARY_SHA = "7a08e94850d66de1d9dba184df205a5a288436fbb0cc005edaa462261976a17f"
PROCESS_SHA = "02ad407e992974d6c5505e2d2a6774f34692731091fb375ec6ef00d0d26769d4"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"


def checked(path, size, sha, compressed=False):
    raw = Path(path).read_bytes()
    assert len(raw) == size and hashlib.sha256(raw).hexdigest() == sha
    return json.loads(gzip.decompress(raw) if compressed else raw)


def upper(record):
    value = record["upper"].strip()
    match = re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]", value)
    if match:
        mid, radius = map(F, match.groups())
        assert radius >= 0
        return mid+radius
    return F(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--geometry-native", required=True)
    parser.add_argument("--intrinsic-summary", required=True)
    parser.add_argument("--intrinsic-process", required=True)
    args = parser.parse_args()
    geo = checked(args.geometry_native, 4073131, GEOMETRY_SHA, True)
    summary = checked(args.intrinsic_summary, 5275, SUMMARY_SHA)
    process = checked(args.intrinsic_process, 6912, PROCESS_SHA)
    assert geo["complete"] is True and geo["candidate_sha256"] == CANDIDATE
    assert geo["kind"] == "complete_actual_C0_state_and_nu_to_model_geometry_response_v1"
    assert geo["source_sha256"] == "3f5acd223d3d378c371cac24b38ce7e88644f9c7137f83619e3326bbe82810bd"
    assert geo["actual_affine_center"] == "-7789843107295549/4611686018427387904"
    assert geo["common_parameter_half_width"] == "0" and geo["exact_interval"] == ["0", "25/8"]
    assert geo["state_C0_radius"] == "1/1000" and geo["nu_radius"] == "1/100000"
    rows = geo["rows"]
    assert len(rows) == geo["original_coefficient_cells"] == geo["common_control_split_cells"] == 7722
    assert F(rows[0]["interval"][0]) == 0 and F(rows[-1]["interval"][1]) == F(25, 8)
    assert all(F(a["interval"][1]) == F(b["interval"][0]) for a, b in zip(rows, rows[1:]))
    lrow, brow = rows[6376], rows[1753]
    assert F(lrow["interval"][0]) <= F(9, 10) <= F(lrow["interval"][1])
    assert F(brow["interval"][0]) == F(9, 50)
    assert upper(lrow["outward_anchor_to_inner_integrals"]["frame_anchor_to_position"]) < F(".583398")
    assert upper(brow["outward_anchor_to_inner_integrals"]["frame_anchor_to_position"]) < F("1.713494")
    assert summary["complete"] is True and summary["failure"] is None
    assert summary["kind"] == "actual_cached_complete_cap_intrinsic_beta_gamma_K_maxima_v1"
    assert all(row["passed"] is True for row in summary["gates"]) and len(summary["gates"]) == 9
    assert summary["exact_interval"] == ["9/10", "25/8"]
    assert summary["original_complete_row_count"] == 4650 and summary["completed_cap_rows"] == 1346
    assert summary["input_sha256"]["original_candidate"] == CANDIDATE
    assert summary["input_sha256"]["exact_eta"] == geo["actual_affine_center"]
    assert process["complete"] is True and len(process["children"]) == 1
    assert process["children"][0]["actual_returncode"] == 0
    assert process["complete_native_sha256"] == summary["native_sha256"]
    constants = summary["complete_cap_intrinsic_constants"]
    assert upper(constants["b_star"]) < F("5.64")
    assert upper(constants["g_star"]) < F("5.64")
    assert upper(constants["K_star"]) < F(".255")
    checks = []

    def lt(name, value, bound):
        value, bound = F(value), F(bound)
        assert value < bound, (name, str(value), str(bound))
        checks.append({"name": name, "exact_value": str(value), "strict_upper": str(bound)})

    # Exact relationships defining the already-certified reference enclosures.
    lt("ell_lower_from_exact_K0_definition", F(".523455817"), F(10, 19))
    lt("ell_upper_from_original_suffix_upper_root", F("1.389936764")**2, 2)
    eps = F(5, 10**18)
    vgap, u, up, vp, kval = F("2.9"), F(".021"), F(".084"), F(".376"), F(".255")
    a_state = kval + 2*u/vgap+u*u/vgap**2
    b_state = 1/vgap+u/vgap**2
    c_state = 1/vgap**2
    a_angle = kval*vp+2*u*up/vgap+u*u*vp/vgap**2
    b_angle = up/vgap+u*vp/vgap**2
    c_angle = vp/vgap**2
    lt("raw_repair_readout_state_sum", a_state+b_state+c_state, 1)
    lt("raw_repair_readout_known_angular_sum", a_angle+b_angle+c_angle, 1)
    lt("raw_repair_inverse_angle_multiplier", F(32,31)/4, 1)
    lt("raw_repair_complete_physical_readout", 2*eps, 20*eps)
    lt("raw_physical_B_inherited_with_repair", F(".006235726")+20*eps, F(".0063"))
    lt("raw_physical_C_inherited_with_repair", F(".318181201")+20*eps, F(".319"))
    er, vr = F(9, 10**9), F(".421")
    lt("complete_mean_retaining_angle_residual_L1", F(65,384)*F("5.237515e-8"), er)
    lt("whole_raw_physical_inverse_radial_variation", F(89,40)*F("5.64")
       *(F(".051433")/4+F(32,31*50))+F(32,31)*er, vr)
    angle_jumps = F(65,372)*F("6.408789e-13")
    lt("all_raw_physical_frame_jumps", F("2.156")*angle_jumps, F(1,10**12))
    lt("all_raw_physical_position_jumps", 4*angle_jumps, F(1,10**12))
    eq, ef = F("3.127699e-8"), F("4.956566e-8")
    zq, zf = F("3.33e-8"), F("5.81e-8")
    lt("all_physical_frame_defect_and_jump_forcing", F("2.157")*F(32,31)*er+eq*vr+F(1,10**12), zq)
    lt("all_physical_position_defect_and_jump_forcing", F("4.131")*er+ef*vr+F(1,10**12), zf)
    lt("raw_rotational_reciprocal_ratio_error", (F(".051432066")+F(1,50)**2)/F(".9"), F(".058"))
    lt("positive_same_branch_ratio_lower", F(".97")**2, 1-F(".058"))
    lt("complete_raw_physical_C_minus_Cref", F(".319")*F(".058")/F("1.97"), F(".0094"))
    lt("complete_raw_A_minus_Aref_and_B", 2*F(".0094")
       +6*(F(".0063")**2+2*F(".0094")**2)+F(".0063"), F(".0264"))
    S, J, r0 = F(".583398"), F("1.713494"), F(".015402")
    lt("raw_physical_vertical_frame_to_rotational", S*F(".0264")+zq, r0)
    Gz, Fz = F(".0787"), F(".061624")
    lt("raw_vertical_moving_frame_derivative", F(33,32)*r0+F("4.001")*(F(".0063")+F(".0094"))+eq, Gz)
    lt("raw_vertical_moving_position_derivative", F("4.001")*r0+ef, Fz)
    lt("physical_Gauss_B_linear_coefficient", 1+F(".039196064"), F("2.052"))
    lt("physical_Gauss_C_linear_coefficient", 2+F(".051432066"), F("2.052"))
    t, rq, rf = F("2.684e-6"), F(1,10**12), F(6,10**21)
    Qp, Al, Pl = F("3.247e-6"), F("3.617e-6"), F("2.243e-6")
    lt("actual_cap_physical_vertical_frame", rq+S*(F("2.052")*t+13*t*t+20*eps)+zq, Qp)
    lt("actual_cap_L_original_angle_frame", Qp+Gz*(F(7,4)*t+eps), Al)
    lt("actual_cap_L_original_angle_position", rf+S*Qp+zf+Fz*(F(7,4)*t+eps), Pl)
    a0, p0 = F("3.649e-6"), F("8.56e-6")
    D, E = F("15.736315")*F(2,10**9), F("30.196406")*F(2,10**9)
    lt("actual_selected_b_vertical_frame", Al+F("3.148e-8"), a0)
    lt("actual_selected_b_vertical_position_same_lambda", Pl+J*(Al+D)+E, p0)
    emoving = F(".000099309")
    A1l, B1l = F(".000413"), F(".000425")
    lt("actual_L_frame_derivative_from_true_GW", F("2.157")*Al+F("4.073")*emoving+eq, A1l)
    lt("actual_L_position_derivative_from_true_GW", F("4.001")*Al+F("4.131")*emoving+ef, B1l)
    a1, b1 = F(".000466"), F(".001417")
    lt("actual_selected_b_frame_derivative", A1l+F("4.312")*Al+F(".000036461"), a1)
    lt("actual_selected_b_position_derivative", B1l+F("1.950541")*A1l+F("12.205365")*Al+F(".000141"), b1)
    lt("new_full_weak_root_height", 94000+86061*a0+12531*a1+4590*b1, 94013)
    lt("new_full_weak_root_source_height", 6650+6086*a0+887*a1+325*b1, 6651)
    lt("new_full_weak_strict_source_height", 3000+2919*a0+441*a1+210*b1, 3001)
    lt("new_full_weak_strict_jump_height", 8850+8098*a0+1180*a1+432*b1, 8852)
    hfee = F("1.73e-7")
    lt("same_supported_particular_actual_anchor_height_fee", F(".031082487")*a0+F(".006877446")*p0, hfee)
    lt("same_supported_particular_height_lower", -F(".025370374"), -F(".0253702")-hfee)
    lt("same_supported_particular_height_upper", -F(".0252298")+hfee, -F(".025229626"))
    lt("same_supported_particular_height_reciprocal", 1/F(".025229626"), F("39.64"))
    lt("H96_whole_frame_anchor_coefficient", F("14.20875")*a0, F(".00005185"))
    lt("H96_whole_density_anchor_coefficient", p0+F(".684")*a0, F(".000011056"))
    print(json.dumps({"kind": "new_actual_physical_angle_cap_world_anchor_exact_combinations_v1",
        "complete": True, "whole_original_geometry_sha256": GEOMETRY_SHA,
        "whole_intrinsic_summary_sha256": SUMMARY_SHA, "whole_intrinsic_process_sha256": PROCESS_SHA,
        "original_row_indices_read": [6376,1753], "old_scientific_targets_recomputed": 0,
        "new_exact_comparison_count": len(checks), "new_exact_comparisons": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
