#!/usr/bin/env python3
"""Exact scalar ledger for conditional phase/cap obstruction lemmas.

Only stdlib file hashes, JSON metadata and Fraction/integer arithmetic are used.
This is not a new geometry certificate or a replay of the accepted R21 backends.
The analytic lemmas and the retained-body identity are in the frozen proof.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path


TOPIC = Path(__file__).resolve().parents[1]
STEM = "2026-11-09-db6f-tail-phase-marker-obstructions"
PINNED = {
    "problem": ("README.md", "dce2fa84bc32a898dcdb19d77f210169b7faa2e9b3b92a72bb7193121581b719"),
    "R16": ("results/R16-fixed-cap-volume-moment-noncongruence.md", "278753736f651a82e64bc9d6de61b290395eb3d48390c7b8aef73f939dd565f1"),
    "R17": ("results/R17-exact-finite-visible-closed-geometry.md", "d7ad70cfb98d552ce0832555c230b644e49a21cd5cef2ae16a291013ad66e725"),
    "R21": ("results/R21-m12-whole-map-and-actual-metric-decrease.md", "3d8e20c610ac322e2f4a7093c44b4b37cde314724136cee489dae73c44497c0c"),
    "R24": ("results/R24-cap-marking-quotient-upper-bound.md", "611401f48cd15594ee663b92950d1828e101005de6e4be1d762ef35245940d5e"),
    "R25_context_only": ("results/R25-m12-sharper-enclosing-ball.md", "faf9c254abad7376249277b336468db19d6598ac9520f999265be139b4dc845b"),
    "background_height_proof": ("notes/2026-11-09-db6f-tail-background-height-interval-proof.md", "46e06ce3740b14c2c68fd33dbfc397d42d05452e83769fdfb956a87be6635e1c"),
    "budget_source": ("scripts/db6f-root-closed-budget-v2.py", "0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641"),
    "budget": ("notes/2026-11-09-db6f-root-closed-budget-m12-critical-r01.json", "50410a4e57b8a21937dd3a99c25942b36cebd5c5819f1e10982584412ae601a7"),
    "first": ("notes/2026-11-09-db6f-tail-first-flat17-m12-critical-r01.json", "5c2ddbfc230416cf7805bf84ea5686ed9db1427c2df2b8f1b3a8379b453e848d"),
    "manifest": ("notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json", "cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104"),
    "geometry": ("notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json", "253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2"),
    "proof_v1_history": ("notes/" + STEM + ".md", "bd3a3b8dd611def263826a5ba9559404d77db2b928648d4f327a896ecf17d1fb"),
    "proof_v2": ("notes/" + STEM + "-v2.md", "5766e8ea650b13b8bd32244496db9d67ecd7c223d4eca6d4a67e2c1e84812486"),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path):
    def reject_constant(value):
        raise ValueError("Nonfinite JSON constant: " + value)
    return json.loads(path.read_text(), parse_constant=reject_constant)


def scalar(value):
    require(type(value) in (int, float), "Expected non-boolean saved numeric scalar")
    require(type(value) is int or math.isfinite(value), "Expected finite saved scalar")
    return Q(value)  # exact saved binary number, never its decimal rendering


def record(value):
    return {"exact": str(value), "approximate_display_only": float(value)}


def sqrt_interval(value, places=35):
    """A rational interval using integer isqrt, with exact endpoint checks."""
    require(value >= 0 and type(places) is int and places > 0, "Square-root arguments")
    scale = 10 ** places
    k = math.isqrt((value.numerator * scale * scale) // value.denominator)
    lo = Q(k, scale)
    hi = lo if lo * lo == value else Q(k + 1, scale)
    require(lo * lo <= value <= hi * hi, "Invalid rational square-root interval")
    require(lo >= 0, "Square root sign")
    return lo, hi


def interval_record(lo, hi):
    require(lo <= hi, "Reversed rational interval")
    return {"lower": record(lo), "upper": record(hi)}


def topic_path(path):
    path = Path(path)
    result = path.resolve() if path.is_absolute() else (TOPIC / path).resolve()
    require(result.is_relative_to(TOPIC), "Source is outside the topic")
    return result


def file_binding(path):
    return {"file": str(path.relative_to(TOPIC)), "sha256": sha(path), "bytes": path.stat().st_size}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--sources", type=Path, required=True)
    args = parser.parse_args()
    out, source_out = args.out.resolve(), args.sources.resolve()
    require(out != source_out and not out.exists() and not source_out.exists(), "Refusing an overwrite")
    require(out.is_relative_to(TOPIC) and source_out.is_relative_to(TOPIC), "Outputs must stay in the topic")
    bindings, data = {}, {}
    for key, (relative, expected) in PINNED.items():
        path = topic_path(relative)
        binding = file_binding(path)
        require(binding["sha256"] == expected, "Changed frozen source: " + key)
        bindings[key] = binding
        if path.suffix == ".json":
            data[key] = load_json(path)

    budget, first, manifest, geometry = [data[k] for k in ("budget", "first", "manifest", "geometry")]
    require(budget["script_sha256"] == PINNED["budget_source"][1], "Budget implementation identity")
    require(first["manifestSHA256"] == geometry["tail_manifest_sha256"] == PINNED["manifest"][1], "Actual tail identities")
    require(manifest["finished"] is True, "Actual tail export is not complete")
    require(geometry["representation"] == "exact-common-cut-prefix" and
            geometry["mirror_inlet_C2_exact"] is True and geometry["exact_common_cut_C2_by_definition"] is True,
            "Actual assembly and mirror identities")
    for key, source in (("geometry", "geometry"), ("tail_first", "first")):
        require(budget["inputs"][key]["sha256"] == PINNED[source][1], "Budget input identity: " + key)
    linked = {}
    for key, item in budget["inputs"].items():
        path = topic_path(item["file"])
        binding = file_binding(path)
        require(binding["sha256"] == item["sha256"], "Changed budget dependency: " + key)
        linked["budget_" + key] = binding
    transfer_ref = budget["same_background_transfer"]
    transfer_path = topic_path(transfer_ref["file"])
    require(sha(transfer_path) == transfer_ref["sha256"], "Changed accepted background transfer")
    transfer = load_json(transfer_path)
    require(transfer["finite_tail_manifest_sha256"] == PINNED["manifest"][1] and transfer["finished"] is True,
            "Background transfer refers to a different map")
    linked["background_transfer"] = file_binding(transfer_path)
    height = load_json(topic_path(budget["inputs"]["height"]["file"]))
    require(transfer["background_definition_hashes"]["checkpoint"]["sha256"] == height["checkpointSHA256"],
            "Height positivity source identity")

    V = max(scalar(first[part]["r0theta0Height"]) for part in ("finite", "collar"))
    require(V == scalar(first["entireTail"]["heightDisplacementUpper"]), "Whole-tail height bound identity")
    # In the frozen source: zmin=Hlo-vz.  Thus this exactly recovers its Hlo.
    Hlo = Q(budget["tail_height_lower"]["exact"]) + V
    a, cut, width = [scalar(manifest["parameters"][key]) for key in ("rCuff", "rCut", "width")]
    require(a == cut - width and a == Q(2702159776422297, 18014398509481984), "Exact actual cuff")
    require(Hlo == Q(7977247853389765, 4503599627370496), "Exact recovered cut-height lower endpoint")
    require(Hlo > Q(177, 100) and 0 < a < Q(3, 20), "Positive source boxes")
    Dlo = 2 * Hlo
    # This cross-check is not the proof of the arbitrary-new-cap D bound.
    # That proof uses the retained pair of actual seam-circle points.
    require(Dlo == Q(budget["held_region_diameter_lower"]["exact"]), "Source constant cross-check")
    x0 = a / Dlo
    require(x0 == Q(2702159776422297, 63817982827118120) and x0 < Q(1, 20), "Basic cylinder obstruction")
    denominator = 1 + 3 * x0 + 3 * x0 * x0
    quotient_squared = x0 * x0 / denominator
    margin = denominator - 625 * x0 * x0
    require(margin == Q(24218466148102856714953454068661, 2036367466061171636096032216167200) > 0,
            "Strict balanced 1/25 comparison")
    require(quotient_squared < Q(1, 625), "Squared quotient bound")
    f_lo, f_hi = sqrt_interval(quotient_squared)

    # 400 x^2 >= 1+3x+3x^2 is exactly 397x^2-3x-1>=0.
    root_lo, root_hi = sqrt_interval(Q(1597))
    threshold_lo, threshold_hi = (3 + root_lo) / 794, (3 + root_hi) / 794
    polynomial = lambda x: 397 * x * x - 3 * x - 1
    require(polynomial(threshold_lo) <= 0 <= polynomial(threshold_hi) and threshold_lo > 0,
            "Positive threshold root bracket")
    require(x0 < threshold_lo, "Current cylinder below necessary threshold")

    epsilon, tau = Q(1, 20), Q(3, 100)
    polynomial_width_squared = 6 * tau * epsilon
    general_width_squared = 4 * tau * epsilon - epsilon * epsilon
    require(polynomial_width_squared == Q(9, 1000) and general_width_squared == Q(7, 2000),
            "Target-specific exact width constants")
    require(0 < epsilon <= 2 * tau, "General radial lemma epsilon range")
    root3_lo, root3_hi = sqrt_interval(Q(3))
    packing_lo, packing_hi = 1 + 2 / root3_hi, 1 + 2 / root3_lo
    polynomial_lo, polynomial_hi = sqrt_interval(polynomial_width_squared)
    general_lo, general_hi = sqrt_interval(general_width_squared)
    old_b = Q(3, 100)
    old_radius_bound = old_b * old_b / (6 * tau * Dlo * Dlo)
    require(old_radius_bound == Q(633825300114114700748351602688, 1590912082860290340700025168880625)
            and old_radius_bound < Q(1, 2500), "Original-support-radius obstruction")

    report = {
        "status": "PASS-exact-scalar-arithmetic-for-conditional-obstructions",
        "script_sha256": sha(Path(__file__).resolve()),
        "proof_sha256": PINNED["proof_v2"][1],
        "bindings": bindings, "rehash_linked_accepted_inputs": linked,
        "retained_body": "Exactly the R21 M12 activity set, including seam circles and excluding replaced cap interiors.",
        "new_cap_scope": "Any fixed compact caps wholly inside the original axis cylinder; actual new D is bounded below by retained seam points.",
        "source_height_displacement_upper": record(V),
        "recovered_cut_height_lower": record(Hlo),
        "actual_cuff_radius": record(a),
        "actual_cut_radius": record(cut), "actual_background_width": record(width),
        "new_diameter_lower_from_retained_seams": record(Dlo),
        "cylinder_radius_over_new_diameter_upper": record(x0),
        "balanced_quotient_upper_squared": record(quotient_squared),
        "balanced_quotient_upper_rational_interval": interval_record(f_lo, f_hi),
        "strict_one_over_25_margin": record(margin),
        "strong_target": record(epsilon), "local_curvature_necessary_reach_ratio": record(tau),
        "C3_cylinder_necessary_radius_formula": "(3+sqrt(1597))/794",
        "C3_cylinder_necessary_radius_interval": interval_record(threshold_lo, threshold_hi),
        "C3_threshold_polynomial_endpoint_signs": [record(polynomial(threshold_lo)), record(polynomial(threshold_hi))],
        "packing_factor_formula": "1+2/sqrt(3)",
        "packing_factor_interval": interval_record(packing_lo, packing_hi),
        "same_polynomial_profile": {
            "width_over_D_necessary_squared": record(polynomial_width_squared),
            "width_over_D_threshold_interval": interval_record(polynomial_lo, polynomial_hi),
            "cap_radius_over_D_threshold_interval": interval_record(packing_lo * polynomial_lo, packing_hi * polynomial_hi),
            "original_support_radius": record(old_b),
            "original_support_quotient_upper": record(old_radius_bound),
            "original_support_quotient_strictly_below_one_over_2500": True,
        },
        "general_nonnegative_radial_center_peak": {
            "width_over_D_necessary_squared": record(general_width_squared),
            "width_over_D_threshold_interval": interval_record(general_lo, general_hi),
            "cap_radius_over_D_threshold_interval": interval_record(packing_lo * general_lo, packing_hi * general_hi),
            "two_Kb_cases_accounted_for_in_proof": True,
        },
        "strict_balanced_quotient_below_one_over_25": True,
        "accepted_source_certificates_reproved_here": False,
        "map_or_metric_modified": False, "new_candidate_certificate_issued": False,
        "root_flow_solver_export_integration_backend_calls": 0,
        "README_complete": False,
    }
    payload = (json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()
    source_ledger = {
        "status": "closed-source-ledger-for-obstruction-proof-v2",
        "proof": bindings["proof_v2"], "superseded_display_only_v1": bindings["proof_v1_history"],
        "script": file_binding(Path(__file__).resolve()),
        "arithmetic_report": {"file": str(out.relative_to(TOPIC)), "sha256": hashlib.sha256(payload).hexdigest(), "bytes": len(payload)},
        "accepted_dependencies": {k: v for k, v in bindings.items() if not k.startswith("proof_")},
        "linked_dependencies": linked,
        "logical_inputs": [
            "The proved R17/R21 image-set phase mechanism and exact C3 symmetry.",
            "The actual R6 seam has V and both jets zero; mirror seam heights are plus/minus Zc.",
            "The accepted exact background has w>=0.",
            "The accepted first-jet and closed-budget reports are valid for this actual manifest.",
            "README reach condition entails the local principal-curvature bound used only as a necessary condition.",
        ],
        "not_inferred": [
            "No stronger-goal lower bound, sharpness, candidate existence or new full reach certificate.",
            "No reuse of the numerical R21 seam-height bound for a future M15 map without its own identity.",
            "No new D lower bound from old marked-cap points or old D upper bounds.",
        ],
    }
    with out.open("xb") as handle:
        handle.write(payload)
    with source_out.open("x") as handle:
        handle.write(json.dumps(source_ledger, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({"status": report["status"], "output_sha256": sha(out),
                      "sources_sha256": sha(source_out), "quotient_strict_bound": "1/25",
                      "new_backend_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
