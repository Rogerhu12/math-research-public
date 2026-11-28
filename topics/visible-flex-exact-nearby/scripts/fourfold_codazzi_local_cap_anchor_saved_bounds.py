#!/usr/bin/env python3
"""New exact cap-anchor combinations from an entire saved C0 geometry native.

The input is restored byte-for-byte from commit1352e025222a3dac0740a7ec3a9b64cdd30bdb0a.
This reader checks the whole native and coverage, copies existing cumulative
records at L and b, and performs only NEW exact rational combinations.  It
does not integrate any old coefficient, repeat any norm, or run any producer.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import re

SHA = "00efc0322a9aa82cd1f234899599ed3fbaff87edd35b8c9ac1331b229b276a55"
CANDIDATE = "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"


def upper(record):
    value = record["upper"].strip()
    if value == "0":
        return F(0)
    match = re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]", value)
    if match:
        mid, radius = map(F, match.groups())
        assert radius >= 0
        return mid+radius
    return F(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--complete-native", required=True)
    args = parser.parse_args()
    with open(args.complete_native, "rb") as stream:
        raw = stream.read()
    assert len(raw) == 4073131 and hashlib.sha256(raw).hexdigest() == SHA
    native = json.loads(gzip.decompress(raw))
    assert native["kind"] == "complete_actual_C0_state_and_nu_to_model_geometry_response_v1"
    assert native["complete"] is True and native["candidate_sha256"] == CANDIDATE
    assert native["source_sha256"] == "3f5acd223d3d378c371cac24b38ce7e88644f9c7137f83619e3326bbe82810bd"
    assert native["exact_interval"] == ["0", "25/8"]
    assert native["common_parameter_half_width"] == "0"
    assert native["actual_affine_center"] == "-7789843107295549/4611686018427387904"
    assert native["state_C0_radius"] == "1/1000" and native["nu_radius"] == "1/100000"
    rows = native["rows"]
    assert len(rows) == native["original_coefficient_cells"] == native["common_control_split_cells"] == 7722
    assert F(rows[0]["interval"][0]) == 0 and F(rows[-1]["interval"][1]) == F(25, 8)
    assert all(F(left["interval"][1]) == F(right["interval"][0])
               for left, right in zip(rows, rows[1:]))
    lrow, brow = rows[6376], rows[1753]
    assert F(lrow["interval"][0]) <= F(9, 10) <= F(lrow["interval"][1])
    assert F(brow["interval"][0]) == F(9, 50)
    lc, bc = (row["outward_anchor_to_inner_integrals"] for row in (lrow, brow))
    assert upper(lc["nu_to_frame"]) == upper(lc["nu_to_position"]) == 0
    assert upper(bc["nu_to_frame"]) == upper(bc["nu_to_position"]) == 0
    checks = []

    def lt(name, value, bound):
        value, bound = F(value), F(bound)
        assert value < bound, (name, value, bound)
        checks.append({"name": name, "exact_value": str(value), "strict_upper": str(bound)})

    ol, pl, jl = F("13.237875"), F("7.722048"), F("0.583398")
    pb, jb = F("26.219222"), F("1.713494")
    for name, record, bound in (("copied_cap_connection", lc["state_to_frame"], ol),
        ("copied_cap_ordered_position", lc["state_to_position"], pl),
        ("copied_cap_reference_path", lc["frame_anchor_to_position"], jl),
        ("copied_b_ordered_position", bc["state_to_position"], pb),
        ("copied_b_reference_path", bc["frame_anchor_to_position"], jb)):
        lt(name, upper(record), bound)
    e, rq, rf = F("0.000099309"), F(1, 10**12), F(6, 10**21)
    a0l, p0l = F("0.001314641"), F("0.000766936")
    lt("new_actual_L_frame", rq+ol*e, a0l)
    lt("new_actual_L_position_mod_same_constant", rf+jl*rq+pl*e, p0l)
    a0, p0 = F("0.001314673"), F("0.002603805")
    lt("new_actual_b_frame", a0l+F("0.00000003148"), a0)
    lt("new_actual_b_position_mod_same_constant", rf+jb*rq+pb*e, p0)
    eq, ef = F("0.00000003127699"), F("0.00000004956566")
    a1l, b1l = F("0.003242"), F("0.005672")
    lt("new_actual_L_frame_derivative", F("2.157")*a0l+F("4.073")*e+eq, a1l)
    lt("new_actual_L_position_derivative", F("4.001")*a0l+F("4.131")*e+ef, b1l)
    a1, b1 = F("0.008949"), F("0.028185")
    lt("new_ACT_b_frame_derivative", a1l+F("4.312")*a0l+F("0.000036461"), a1)
    lt("new_ACT_b_position_derivative", b1l+F("1.950541")*a1l
       +F("12.205365")*a0l+F("0.000141"), b1)
    lt("new_weak_root_height", 94000+86061*a0+12531*a1+4590*b1, 94360)
    lt("new_weak_root_source_height", 6650+6086*a0+887*a1+325*b1, 6676)
    lt("new_weak_strict_source_height", 3000+2919*a0+441*a1+210*b1, 3014)
    lt("new_weak_strict_jump_height", 8850+8098*a0+1180*a1+432*b1, 8884)
    height_error = F("0.031082487")*a0+F("0.006877446")*p0
    lt("new_actual_particular_height_anchor_fee", height_error, F("0.00005878"))
    lt("new_actual_particular_height_lower", -F("0.025429"),
       -F("0.0253702")-F("0.00005878"))
    lt("new_actual_particular_height_upper", -F("0.0252298")+F("0.00005878"),
       -F("0.025171"))
    lt("new_actual_height_pivot_reciprocal", F(1)/F("0.025171"), F("39.73"))
    lt("new_H96_frame_anchor_coefficient", F("14.20875")*a0, F("0.018681"))
    lt("new_H96_density_anchor_coefficient", p0+F("0.684")*a0, F("0.003503042"))
    print(json.dumps({"kind": "new_actual_local_cap_anchor_exact_combinations_v1",
        "complete": True, "whole_native_sha256": SHA, "old_scientific_targets_recomputed": 0,
        "copied_original_row_indices": [6376, 1753], "new_exact_comparison_count": len(checks),
        "new_exact_comparisons": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
