"""New whole-domain genuine determinant consequences of complete old records.

This reads the complete successful real piecewise root process, WGS result
and the original complete common potential. Only new exact Fraction
comparisons are performed. No old coefficient, flow, fold, potential,
Taylor, Airy, inverse or source target is imported, restored or repeated.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
INPUTS = {
    "root": ("notes/piecewise_real_root_fold_resume_v2_ci/run-43616813816-1/consumers/process.json",
             32670, "c30eb4c5e1efebd3663528418389ececf1ba8f4450f8e667496026915e2dfb64"),
    "root_publication": ("notes/piecewise_real_root_fold_resume_v2_ci/run-43616813816-1/publication.json",
             1981, "c602531ab5732c8f6ec7112814f1a12e29fd0963bca34cb40253f0c2e2fb533c"),
    "global": ("notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json",
             72251, "8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e"),
    "global_execution": ("notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/execution.json",
             18234, "f8ffc01b8277d55980d0622f888f89cc501f3b565268bef046e074f8a6e4b62e"),
    "potential": ("notes/common_radial_potential_budget_ci/run-43685624307-1/execution.json",
             27645, "d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9"),
    "piecewise_proof": ("results/R133-supplement-piecewise-real-root-fold-and-closed-forced-Airy-transport.md",
             12114, "ee319621da07bd95e30708779128f6ac88ba7af5fade2f266cf03f0ee67965af"),
    "global_proof": ("results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md",
             40111, "9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad"),
    "ordered_proof": ("results/R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md",
             22688, "c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e"),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def ends(text):
    match = re.fullmatch(r"\[([^\s]+) \+/- ([^\s]+)\]", text)
    if match:
        center, radius = map(F, match.groups())
        require(radius >= 0, "nonnegative full saved decimal radius")
        return center-radius, center+radius
    point = F(text)
    return point, point


def bound(record, side):
    # Keep the original provider's separate directed endpoints when present.
    return ends(record.get(side, record["ball"]))[0 if side == "lower" else 1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.exists(), "preserve the first entire new consequence; no replay")
    documents, receipts = {}, []
    for role, (name, size, digest) in INPUTS.items():
        path = TOPIC+"/"+name
        raw = (args.repo/path).read_bytes()
        require(len(raw) == size and hashlib.sha256(raw).hexdigest() == digest,
                "whole original input: "+role)
        receipts.append({"role":role, "path":path, "bytes":size, "sha256":digest})
        if name.endswith(".json"):
            documents[role] = json.loads(raw)
    root, rp = documents["root"], documents["root_publication"]
    require(root["complete"] is root["mathematical_complete"] is rp["complete"] is True
            and root["failure"] is root["mathematical_failure"] is None
            and root["actual_returncode"] == rp["actual_returncode"] == 0
            and str(root["run_id"]) == str(rp["run_id"]) == "43616813816"
            and len(root["mathematical_gates"]) == 15
            and all(x["passed"] is True for x in root["mathematical_gates"])
            and root["verified_input_files"] == 204
            and root["full193_direction_and_independent_even_mean"] is True
            and root["radial_domain_is_real_and_original_piecewise_smooth"] is True,
            "the whole actual successful piecewise root family")
    require([x for x in rp["files"] if x["file"] == "consumers/process.json"] == [{
        "file":"consumers/process.json", "bytes":INPUTS["root"][1],
        "sha256":INPUTS["root"][2], "original_sha256":INPUTS["root"][2]}],
        "the original whole publication binds this complete process")
    selected = root["selected"]
    require(selected["exact_radius"] == "1/50" and selected["passed"] is True
            and selected["complete_original_rows"] == 1300 and selected["true_original_seams"] == 1079
            and len(selected["gates"]) == 7 and all(x["passed"] for x in selected["gates"])
            and root["exact_complex_parameter_radius"] == "1/100000000",
            "the actual whole real root window and every original seam")
    global_result, ge = documents["global"], documents["global_execution"]
    require(global_result["complete"] is global_result["proved"] is ge["complete"] is True
            and global_result["actual_returncode"] == ge["actual_returncode"] == 0
            and global_result["failure"] is ge["actual_failure"] is None
            and str(global_result["run_id"]) == str(ge["run_id"]) == "43820816332"
            and len(global_result["gates"]) == 24 and all(x["passed"] for x in global_result["gates"])
            and {"file":"actual-scientific-conclusion.json", "bytes":INPUTS["global"][1],
                 "sha256":INPUTS["global"][2]} in ge["output_hashes"],
            "the complete actual WGS strict geometry and execution")
    parameters = global_result["parameters"]
    require(parameters["fixed_intrinsic_parameter"] == "eta_0"
            and parameters["exact_real_delta_radius"] == "1/100000000"
            and parameters["exact_root_interval"] == root["exact_root_interval"],
            "same fixed intrinsic parameter and actual uncertain root")
    pe = documents["potential"]; potential = pe["actual_scientific_receipt"]
    require(pe["complete"] is potential["complete"] is potential["proved"] is True
            and pe["actual_returncode"] == potential["actual_returncode"] == 0
            and pe["actual_failure"] is potential["failure"] is None
            and len(potential["gates"]) == 16 and all(x["passed"] for x in potential["gates"]),
            "the whole actual potential result, not a root sample")
    cases = [v for v in potential["cases"] if v["exact_complex_radial_radius"] == "1/6000"]
    require(len(cases) == 1, "the one complete accepted potential domain")
    pv = cases[0]
    require(pv["complete"] is pv["proved"] is True and pv["failure"] is None
            and pv["exact_complex_z_square_halfwidth"] == "1/9409"
            and pv["all_integer_modes_abs_j_at_least"] == 97
            and pv["physical_angular_frequency"] == "4j"
            and pv["both_carrier_signs_retained"] is True
            and pv["exact_complex_delta_square_halfwidth"] == "1/100000000"
            and pv["fixed_intrinsic_parameter"] == "eta_0"
            and pv["independent_even_mean_equation_retained"] is True,
            "all original frequencies, parameters and the independent physical mean")
    b = selected["bounds"]
    R, L, M, n0 = F(1,50), F(1,2000), F(276), F(388)
    Y, X, T, D0, eps = F(7,1000), F(81,80), F(4,25), F(977,1000), F(1,10**7)
    lamM = M/(n0*n0)
    fee = lamM*Y*Y
    whole_D = bound(global_result["complete_strict_geometry_conclusion"]["complete_positive_lowers"]["determinant"], "lower")
    root_D = bound(b["fold_noncharacteristic_gap"], "lower")
    checks = []
    def compare(name, a, z, relation="<"):
        passed = a < z if relation == "<" else a > z
        checks.append({"name":name, "left_exact":str(a), "relation":relation,
                       "right_exact":str(z), "passed":passed})
    compare("whole_piecewise_A_lower", bound(b["A_lower"],"lower"), F(4), ">")
    compare("whole_piecewise_ray_derivative_deviation", bound(b["angular_Jacobian_fee"],"upper"), F(1,80))
    compare("whole_piecewise_T_phi", bound(b["T_phi"],"upper"), Y)
    compare("whole_piecewise_T_value", bound(b["T_upper"],"upper"), T)
    compare("whole_piecewise_free_determinant", root_D, D0, ">")
    compare("whole_common_potential", bound(pv["complete_modulus_upper"]["V"],"upper"), M)
    compare("whole_common_potential_image", bound(pv["reference_image"]["complete_image_disk_radius_lower"],"lower"), L, ">")
    compare("true_root_boundary_T_lower_without_fractional_power", F(4)**2*R**3, F(1,20)**3, ">")
    compare("whole_potential_support_strictly_inside_true_root_window", F(1,20), L, ">")
    root_lo, root_hi = map(F, parameters["exact_root_interval"])
    cut = F(parameters["exact_strict_cut"])
    compare("entire_uncertain_root_window_overlaps_strict_domain", root_hi-R, cut)
    compare("strict_cut_precedes_every_true_root", cut, root_lo)
    compare("complete_relative_deformation", fee/D0, eps)
    compare("new_support_layer_deformed_determinant", root_D-fee, D0, ">")
    compare("new_global_deformed_determinant", (1-eps)*whole_D, F(1,720), ">")
    compare("root_deformed_lower_also_covers_global_gap", D0, F(1,720), ">")
    compare("complete_genuine_B_entry_sum_on_root_window", (2*X+Y*(1+T+lamM))/D0, F(21,10))
    compare("complete_free_H_inverse_entry_sum_on_root_window", (2*X+Y*(1+T))/D0, F(21,10))
    compare("complete_signed_inverse_difference_entry_sum", lamM*Y/D0*(1+Y*F(21,10)), F(1,70000))
    require(len(checks) == 18 and all(x["passed"] for x in checks), "all eighteen new exact rational comparisons")
    result = {
        "kind":"R133_GDG_complete_global_genuine_determinant_consequence_v1",
        "complete":True, "proved":True, "new_exact_comparison_count":18,
        "whole_original_input_receipts":receipts, "complete_new_comparisons":checks,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "whole_real_family_delta_radius":"1/100000000", "fixed_intrinsic_parameter":"eta_0",
        "whole_negative_interval":"[0,true original r_star]", "minimum_physical_frequency":388,
        "support_layer_is_contained_in_real_piecewise_root_window":True,
        "true_root_window_radius":"1/50", "outside_window_minus_T_lower":"1/20",
        "deformed_to_free_determinant_ratio_lower":"9999999/10000000",
        "whole_negative_deformed_determinant_lower":"1/720",
        "root_window_deformed_determinant_lower":"977/1000",
        "root_window_B_and_free_inverse_entry_sum_upper":"21/10",
        "whole_negative_B_minus_free_inverse_entry_sum_upper":"1/70000",
        "outside_root_window_B_equals_free_inverse":True,
        "all_original_physical_pieces_and_means_retained":True,
        "nonzero_extended_primitive_tail_retained":True,
        "old_scientific_targets_or_carriers_recomputed":0,
        "uniform_high_response_or_physical_inverse_claimed":False,
        "topic_completion_claimed":False,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    raw = (json.dumps(result,sort_keys=True,separators=(",",":"))+"\n").encode()
    args.output.write_bytes(raw)
    require(args.output.read_bytes() == raw, "entire new consequence readback")
    print(json.dumps({"proved":True,"new_exact_comparisons":18,"bytes":len(raw),
        "sha256":hashlib.sha256(raw).hexdigest(),"old_science":0,"old_restorations":0}))


if __name__ == "__main__":
    main()
