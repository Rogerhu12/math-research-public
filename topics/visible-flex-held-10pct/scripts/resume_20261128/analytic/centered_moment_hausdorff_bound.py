#!/usr/bin/env python3
"""R88 exact scalar consequences of the proved centered-moment/Hausdorff lemma.

This verifies rational budgets and source bindings. It does not sample, mesh,
align surfaces, recompute the R83 integrals, or claim a complete metric solve.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path: Path):
    return json.loads(path.read_text())

def certify(r82_path: Path, r84_path: Path, r86_path: Path):
    old = load(r82_path)
    endpoint = load(r84_path)["result"]
    new = load(r86_path)
    cap = new["exact_scalar_entry"]["full_result"]
    assert old["all_phase_C2_geometry_proved"] is True
    assert endpoint["status"] == "exact_rational_endpoint_tensor_consequence_passed"
    assert cap["status"] == "R86_exact_scalar_transfer_and_endpoint_consequence_passed"
    for a, b, c in [
        (old["actual_query"]["sha256"], endpoint["bindings"]["query"], new["actual_source_inputs"]["actual_old_query_sha256"]),
        (old["actual_report"]["sha256"], endpoint["bindings"]["geometry"], new["actual_source_inputs"]["actual_old_geometry_report_sha256"]),
        (old["geometry_bundle"]["sha256"], endpoint["bindings"]["bundle"], new["actual_source_inputs"]["complete_bundle_sha256"]),
    ]:
        assert a == b == c
    assert digest(r82_path) == "d966ce31e136a7c74dddad64e549d02cee5392016f8350d9b75960cc786d635e"
    assert digest(r86_path) == "ee0ca41045a20b0790187ae4cf97629d48b63408c2fcd3e9cad354f3dc55365c"
    actual_radius = Q.from_float(old["whole_radius_upper"])
    actual_support = Q.from_float(old["whole_support_lower"])
    assert actual_radius == Q(cap["whole_radius_upper_exact"])
    assert actual_support == Q(cap["whole_support_lower_exact"])
    radius, support, small_d, shifted_radius = Q(6, 5), Q(3, 5), Q(1, 100), Q(5, 4)
    assert actual_radius < radius and actual_support > support
    translation_factor = Q(3)
    assert support - translation_factor * small_d > 0
    assert radius + translation_factor * small_d < shifted_radius
    pi_upper = Q(22, 7)
    radial_gradient = radius ** 2 / support
    assert radial_gradient == Q(12, 5)
    direction_factor = 2 / support
    angular_factor = pi_upper * direction_factor / 2
    radial_difference_factor = 1 + radial_gradient * angular_factor
    assert radial_difference_factor < 14
    volume_difference_factor = shifted_radius ** 2 * 4 * pi_upper * 14
    assert volume_difference_factor == 275
    volume_upper = Q(4, 3) * pi_upper * radius ** 3
    tensor_norm_upper = volume_upper * radius ** 3
    assert tensor_norm_upper < 13
    translation_tensor_factor = 3 * shifted_radius ** 2 * translation_factor * volume_upper
    assert translation_tensor_factor < 102
    tensor_difference_factor = shifted_radius ** 3 * 275 + translation_tensor_factor
    assert tensor_difference_factor < 640
    invariant_factor = Q(2 * 13 * 640)
    assert invariant_factor == 16640
    gaps = {
        "R84_canonical": Q(endpoint["exact"]["tensor_norm_squared_drop_strict_lower"]),
        "R86_full_disk": Q(cap["endpoint_tensor_gap_strict_lower_exact"]),
    }
    assert gaps["R86_full_disk"] == 51200 * gaps["R84_canonical"]
    clean = {"R84_canonical": Q(4, 10**23), "R86_full_disk": Q(2, 10**18)}
    consequences = {}
    for name, gap in gaps.items():
        assert gap / invariant_factor < small_d
        exact_bound = min(small_d, gap / invariant_factor)
        assert exact_bound > clean[name]
        consequences[name] = {
            "strict_tensor_gap_lower": str(gap),
            "derived_strict_endpoint_E3_Hausdorff_lower": str(exact_bound),
            "clean_strict_endpoint_E3_Hausdorff_lower": str(clean[name]),
            "whole_diameter_upper_used": str(2 * radius),
            "clean_strict_delta_E_over_D_lower": str(clean[name] / (2 * radius)),
            "is_actual_distance_or_optimal_alignment": False,
        }
    return {
        "status": "R88_exact_constants_and_actual_source_consequences_passed",
        "proof": "results/R88-quantitative-euclidean-hausdorff-from-third-moment.md",
        "source_sha256": digest(Path(__file__).resolve()),
        "inputs": {
            "R82": {"path": str(r82_path), "sha256": digest(r82_path)},
            "R84": {"path": str(r84_path), "sha256": digest(r84_path)},
            "R86": {"path": str(r86_path), "sha256": digest(r86_path)},
        },
        "same_actual_bindings": endpoint["bindings"],
        "exact_constants": {
            "actual_radius_upper": str(actual_radius),
            "actual_support_lower": str(actual_support),
            "radius_upper_used": str(radius),
            "support_lower_used": str(support),
            "small_distance_cutoff": str(small_d),
            "translation_factor": str(translation_factor),
            "shifted_radius_upper": str(shifted_radius),
            "spherical_radial_gradient_upper": str(radial_gradient),
            "radial_difference_factor_upper": str(radial_difference_factor),
            "symmetric_difference_volume_factor_upper": str(volume_difference_factor),
            "body_volume_upper": str(volume_upper),
            "centered_tensor_norm_upper": str(tensor_norm_upper),
            "translation_tensor_difference_factor_upper": str(translation_tensor_factor),
            "full_tensor_difference_factor_upper": str(tensor_difference_factor),
            "simplified_squared_norm_difference_factor": str(invariant_factor),
        },
        "consequences": consequences,
        "hypotheses_proved_geometrically_not_sampled": [
            "C3 and z reflection force both centroids and convex-hull Steiner points to zero",
            "positive support and the existing embedded spheres give radial graphs",
            "Steiner translation bound and the centered tensor comparison hold for all O(3), including reflections",
        ],
        "new_integrals_or_BVP_or_alignment_executed": False,
        "new_geometric_quantitative_bound": True,
        "fixed_problem_convergence_or_lambda_one_or_README_completion": False,
    }

def main():
    root = Path(__file__).resolve().parents[3]
    ap = argparse.ArgumentParser()
    ap.add_argument("--r82", type=Path, default=root/"notes/2026-11-28-tail-actual-marked-column-closed-geometry.json")
    ap.add_argument("--r84", type=Path, default=root/"notes/2026-11-28-actual-endpoint-third-tensor-separation.json")
    ap.add_argument("--r86", type=Path, default=root/"notes/2026-11-28-full-disk-marker-geometry-and-endpoint.json")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    result = certify(args.r82.resolve(), args.r84.resolve(), args.r86.resolve())
    result["actual_execution_UTC"] = datetime.now(timezone.utc).isoformat()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"status": result["status"], "out": str(args.out), "sha256": digest(args.out), "consequences": result["consequences"]}, ensure_ascii=False))
if __name__ == "__main__":
    main()
