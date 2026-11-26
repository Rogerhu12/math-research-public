#!/usr/bin/env python3
"""V2: certify every mode of one actual native-scope shared-R tail and collar.

Old background lemmas and exact polynomial formulas are reused; no old
nonrotating field bound is reused. Absolute placement remains conditional on
the NEW cut height z_b belonging to the specified R58 window.
"""
import argparse
from fractions import Fraction as Q
import math
from pathlib import Path
import sys
import time

from seam_export_tail_geometry_v2 import (
    HERE, TOPIC, read, sha, ref, checked, canonical_sha, write, fresh_dir, bind_height,
    validate_packet_states,
)
from seam_tail_spectrum_v2 import (
    GEOMETRY_SCHEMA, canonical_contract, degree_argument, validate_spectrum_container,
)
from seam_cut_height_compatibility import load_packet, outward
from seam_restore_true_background import DEFINITION_SHA, KERNEL_SHA, TIGHT_RECORD_SHA


OLD = TOPIC / "scripts/resume_n4"
OLD_SHAS = {
    "certify_q060_shared_r_tail_batch.py":
        "c646bd4a918aa467212870d437718f22451903a0141242fa5ebf3166ba376aac",
    "certify_q060_stage127_r_quintic.py":
        "4a2bcb9f9e749ce62663d3b8768029ed7c19cbde03a7068eaab3f6552f36fe94",
    "q060_true_background_oracle.py":
        "d133b3ed5b9e5b5a8e15e3a6bb49b3969b65abbd77fbb17a9d0af835d28c1901",
}
H = [[Q(0), 0, 0, Q(10), -Q(15), Q(6)],
     [Q(0), 0, 0, -Q(4), Q(7), -Q(3)],
     [Q(0), 0, 0, Q(1, 2), -Q(1), Q(1, 2)]]
HEIGHT_WINDOW = [Q(1, 10), Q(32, 25)]
BACKGROUND_HEIGHT_UPPER = Q(7446320975220351, 288230376151711744)


def fq(x):
    x = float(x)
    if not math.isfinite(x):
        raise ValueError("Nonfinite literal coefficient")
    return Q.from_float(x)


def upper(x):
    return outward(Q(x), 1)


def lower(x):
    return outward(Q(x), -1)


def upper_row(x):
    return {"upper": upper(x), "upper_exact": str(x)}


def lower_row(x):
    return {"lower": lower(x), "lower_exact": str(x)}


def sqrt_upper(x):
    x = Q(x)
    if x < 0:
        raise ValueError("Negative exact square")
    scale = 10 ** 100
    k = math.isqrt(x.numerator * scale * scale // x.denominator)
    if k * k * x.denominator < x.numerator * scale * scale:
        k += 1
    return Q(k, scale)


def derivative(poly):
    return [(i + 1) * poly[i + 1] for i in range(len(poly) - 1)]


def value(poly, x):
    result = Q(0)
    for coefficient in poly[::-1]:
        result = result * x + coefficient
    return result


def bernstein(poly):
    n = len(poly) - 1
    return [sum((poly[j] * Q(math.comb(k, j), math.comb(n, j))
                 for j in range(k + 1)), Q(0)) for k in range(n + 1)]


def normal_difference_bound(eta):
    # In a background orthonormal tangent frame, |A|_F <= eta gives a
    # cross-product perturbation <= sqrt(2)*eta + eta^2/2. Normalization
    # then gives the following conservative all-angle bound.
    cross = sqrt_upper(Q(2)) * eta + eta * eta / 2
    if cross >= 1:
        return None
    return min(Q(2), 2 * cross / (1 - cross))


def conditional_placement(eta, position):
    normal = normal_difference_bound(eta)
    radius0 = sqrt_upper(fq(.3) ** 2 +
                         (HEIGHT_WINDOW[1] + BACKGROUND_HEIGHT_UPPER) ** 2)
    radius = radius0 + position
    support = None if normal is None else Q(1, 11) - radius0 * normal - position
    return {
        "condition": "The new original cut placement z_b = Z_c + mu_cut lies in [1/10,32/25].",
        "condition_proved_here": False,
        "cut_height_window_exact": list(map(str, HEIGHT_WINDOW)),
        "background_radius_upper": upper_row(radius0),
        "normal_difference_upper": None if normal is None else upper_row(normal),
        "radius_upper": upper_row(radius),
        "support_lower": None if support is None else lower_row(support),
        "radius_below_1_34": radius < Q(67, 50),
        "positive_support": support is not None and support > 0,
    }


def deep_collar(data, entry, node_index, constants, outpath):
    """Use the NEW deepest canonical node, never an old collar anchor."""
    S = node_index["finite_stage_count"]
    spectrum = canonical_contract(data["spectrum"])
    validate_spectrum_container(data, spectrum, stage=True)
    if data["stage"] != S - 1 or data["rawCell"] != 7 or data["rawSegment"] != 0 or data["rawLeft"] != 0:
        raise ValueError("The actual finite-depth-8 deep endpoint was not exported")
    node = data["nodes"][0]
    if (node["canonicalNode"] != S or node["xi"] != 0 or node["sourceX"] != 0 or
            node["meanPerturbation"] != 0 or node["meanBackground"] != 0):
        raise ValueError("Deep node is not the original shared zero mean anchor")
    value_hash = canonical_sha({"radius": node["radiusJS"], "coefficients": node["coefficients"]})
    if value_hash != node_index["deep_node"]["value_sha256"]:
        raise ValueError("Deep collar and shared stages use different literal jets")
    params = constants["parameters"]
    if not all(data["physicalParameters"].get(k) == v for k, v in params.items()):
        raise ValueError("Deep map uses another physical background")
    R0, cuff = fq(node["radiusJS"]), fq(params["rCuff"])
    Ri, L = (R0 + cuff) / 2, (R0 - cuff) / 2
    if not Q(1, 25) < cuff < Ri < R0 < fq(.3):
        raise ValueError("No nonempty collar inside the actual deep endpoint")
    planar, height = data["planarModes"], data["heightModes"]
    if height != spectrum["height_modes"] or planar != spectrum["planar_modes"]:
        raise ValueError("The deep anchor lost part of the declared complete Fourier map")
    modes, P = planar + height, len(planar)
    jet = [[fq(x) * (1 if i < P else -1) for i, x in enumerate(row)]
           for row in node["coefficients"]]
    if len(jet) != 3 or any(len(row) != len(modes) for row in jet):
        raise ValueError("Incomplete literal full Cartesian two-jet")
    B, matched = [[Q(0)] * 3 for _ in range(3)], 0
    for index, mode in enumerate(modes):
        poly = [sum((L ** j * jet[j][index] * H[j][k] for j in range(3)), Q(0))
                for k in range(6)]
        current = poly
        for radial in range(3):
            if value(current, Q(0)) != 0 or value(current, Q(1)) / L ** radial != jet[radial][index]:
                raise ArithmeticError("Deep collar exact endpoint identity failed")
            matched += 2
            bound = max(map(abs, bernstein(current))) / L ** radial
            for angular in range(3):
                B[radial][angular] += abs(mode) ** angular * bound
            current = derivative(current)
    eta = sqrt_upper(B[1][0] ** 2 + (B[0][1] / Q(1, 25)) ** 2)
    second = sqrt_upper(B[2][0] ** 2 + 2 * (B[1][1] / Q(1, 25)) ** 2 +
                        (B[0][2] / Q(1, 25) ** 2) ** 2)
    metric = 2 * eta + eta * eta
    normal = normal_difference_bound(eta)
    curvature = None
    if eta < 1 and normal is not None:
        # R58 gives |II_0| <= 8; its coordinate Hessian Frobenius norm
        # in the target frame is <45 on R>=.04. This uses actual new B.
        if not Q(64) * (1 + Q(41, 100) ** 2) + 3 / Q(1, 25) ** 2 < 45 ** 2:
            raise ArithmeticError("Fixed background coordinate bound failed")
        curvature = (8 + 45 * normal + second) / (1 - eta) ** 2
    passed = metric < Q(1, 10 ** 6) and curvature is not None and curvature < 10
    result = {
        "status": ("new_deep_C2_collar_metric_curvature_certified" if passed
                   else "new_deep_C2_collar_bounds_not_within_allocations"),
        "source": ref(__file__), "stage_data": entry,
        "geometry_schema": GEOMETRY_SCHEMA, "spectrum_contract": data["spectrumContract"],
        "finite_scope": spectrum["finite_scope"], "degree": spectrum["degree"],
        "source_stage": S - 1, "canonical_deep_node": S,
        "canonical_deep_value_sha256": value_hash,
        "true_background_definition_sha256": DEFINITION_SHA,
        "outer_R_exact": str(R0), "inner_R_exact": str(Ri), "cuff_R_exact": str(cuff),
        "collar_width_exact": str(L),
        "definition": "u=(R-Ri)/L; perturbation=sum_j L^j H_j(u) J_j, with the actual shared upper Cartesian perturbation jets J_j.",
        "right_Hermite_basis_exact": [[str(v) for v in row] for row in H],
        "upper_height_sign": -1, "exact_endpoint_scalar_equalities": matched,
        "C2_outer_match_exact": True, "C2_inner_zero_two_jet_exact": True,
        "deep_mean_contract": "Original mean chain is zero here. No reset of any outer stage mean.",
        "physical_height_contract": "Literal r_JS^4 u source coefficients; no substitution of true_R^4 u.",
        "planar_rr_contract": "Chosen finite nodal parameters; no exact unprojected PDE rr claim.",
        "derivative_bounds_exact": [[str(v) for v in row] for row in B],
        "normalized_first_jet_upper": upper_row(eta),
        "normalized_coordinate_second_jet_upper": upper_row(second),
        "metric_relative_operator_upper": upper_row(metric),
        "principal_curvature_upper": None if curvature is None else upper_row(curvature),
        "position_perturbation_upper": upper_row(B[0][0]),
        "conditional_placement": conditional_placement(eta, B[0][0]),
        "planar_projection_derivative_less_than_one": eta < 1,
        "rotational_inside_collar": "The identical R58 true background, continued C2 to its fixed planar cuff/disk.",
        "metric_gate_passed": metric < Q(1, 10 ** 6),
        "curvature_allocation_passed": curvature is not None and curvature < 10,
        "nonlinear_solves_executed": 0, "old_field_bounds_reused": False,
        "whole_closed_surface": False,
    }
    write(outpath, result)
    return result


def validate_inputs(bundle_path, constants_path, norm_path):
    bundle = read(bundle_path)
    if (bundle["status"] != "accepted_new_tail_shared_R_representation_exported"
            or bundle.get("geometry_schema") != GEOMETRY_SCHEMA):
        raise ValueError("Require an actually completed new shared-R export")
    if sha(bundle["source"]["path"]) != bundle["source"]["sha256"]:
        raise ValueError("The actual exporter source changed")
    packet = checked(bundle["accepted_packet"])
    checked(bundle["source_port"])
    background = TOPIC / "notes/2026-11-20-m3-m24-warm050-execution.json"
    _, _, _, spacing, M, _ = load_packet(
        Path(bundle["accepted_packet"]["path"]), Path(bundle["source_port"]["path"]), background)
    spectrum = checked(bundle["spectrum_contract"])
    canonical_contract(spectrum)
    if (spectrum != bundle["spectrum"] or spectrum["finite_scope"] != bundle["finite_scope"]
            or validate_packet_states(packet, M, spacing, degree_argument(spectrum)) != spectrum):
        raise ValueError("The new finite Fourier definition differs from the accepted actual scope")
    for name in ("seam_tail_spectrum_v2.py", "seam_export_shared_r_tail_v2.mjs"):
        if bundle["representation_sources"].get(name) != ref(HERE / name):
            raise ValueError("A bound finite representation source changed: " + name)
    identity = bundle["height_identity"]
    checked(identity["reference"])
    if bind_height(packet, Path(identity["reference"]["path"]), identity["reference_key"],
                   identity["factor"], identity["original_arithmetic"]) != identity:
        raise ValueError("Warm/unscaled accepted height identity changed")
    chain, manifest, index = [checked(bundle[key]) for key in
                              ("mean_chain", "shared_R_manifest", "canonical_node_index")]
    if (chain["status"] != "all_saved_initial_states_matched_single_mean_chain" or
            chain["checkpoint"] != bundle["accepted_packet"] or
            chain["native_record"] != bundle["native_record"] or
            chain["all_stage_input_maximum_difference"] != 0):
        raise ValueError("Shared map does not preserve this original mean chain")
    if (manifest["status"] != "selected_stages_share_one_literal_R_C2_definition" or
            manifest["existingCheckpoint"] != bundle["accepted_packet"] or
            manifest["input"] != bundle["mean_chain"] or
            index["manifest"] != bundle["shared_R_manifest"]):
        raise ValueError("Shared map/input/index binding differs")
    validate_spectrum_container(manifest, spectrum)
    if (manifest["spectrumContract"] != bundle["spectrum_contract"]
            or index["spectrum_contract"] != bundle["spectrum_contract"]):
        raise ValueError("Manifest and complete common-node index use a different finite map")
    constants, norm = read(constants_path), read(norm_path)
    definition = {key: constants[key] for key in
                  ("parameters", "cells", "checkpoint_sha256", "factory_sha256")}
    if canonical_sha(definition) != DEFINITION_SHA:
        raise ValueError("Different true background")
    if norm["status"] != "previously_proved_intervals_rebound_to_identical_definition":
        raise ValueError("Use the explicit same-definition normalization reuse record")
    if (norm["source_sha256"] != KERNEL_SHA or norm["input_sha256"] != sha(constants_path) or
            norm["definition_sha256"] != DEFINITION_SHA or
            norm["original_execution_record"]["sha256"] != TIGHT_RECORD_SHA):
        raise ValueError("Normalization reuse identity differs")
    original = checked(norm["original_execution_record"])
    if any(norm[key] != original[key] for key in
           ("complete_integrals", "exact_normalization", "exact_height", "cell0_inner_radius")):
        raise ValueError("Previously proved bounds were changed")
    for name, digest in OLD_SHAS.items():
        if sha(OLD / name) != digest:
            raise ValueError("Analysed polynomial/oracle source changed: " + name)
    return bundle, chain, manifest, index, constants


def certify(args):
    start = time.monotonic()
    outdir = fresh_dir(args.outdir)
    bundle, chain, manifest, index, constants = validate_inputs(
        args.geometry_bundle, args.constants, args.normalization_certificate
    )
    sys.path.insert(0, str(OLD))
    import certify_q060_shared_r_tail_batch as kernel
    from q060_true_background_oracle import Q060TrueBackgroundOracle
    oracle = Q060TrueBackgroundOracle(args.constants, args.normalization_certificate)
    files = {row["stage"]: row for row in manifest["files"]}
    stages = sorted(files) if args.stages == "all" else sorted(set(map(int, args.stages.split(","))))
    if not stages or not set(stages).issubset(files) or args.quadratic_mode_cutoff < 0:
        raise ValueError("Only actually exported stages with a valid cutoff may be certified")
    result = {
        "status": "running", "source": ref(__file__), "geometry_bundle": ref(args.geometry_bundle),
        "geometry_schema": GEOMETRY_SCHEMA, "spectrum": bundle["spectrum"],
        "spectrum_contract": bundle["spectrum_contract"],
        "representation_sources": bundle["representation_sources"],
        "accepted_packet": bundle["accepted_packet"], "height_identity": bundle["height_identity"],
        "shared_R_manifest": bundle["shared_R_manifest"], "original_mean_chain": bundle["mean_chain"],
        "constants": ref(args.constants), "normalization": ref(args.normalization_certificate),
        "mathematical_sources": {name: ref(OLD / name) for name in OLD_SHAS},
        "oracle_provenance": oracle.provenance, "selected_stages": stages, "stages": [],
        "global_tail_complete": False, "whole_closed_surface": False,
        "original_BVP_solves": 0, "shooting_iterations": 0, "old_field_bounds_reused": False,
        "true_background": "The identical R58 true-integral function, not the JS quadrature profile.",
        "upper_height_definition": "z_b - (true h(R)-true h(R_cut)) - mu(R,theta), with z_b=Z_c+mu_cut and the original entire cumulative perturbation mean.",
        "absolute_cut_placement_proved": False,
    }
    summary = outdir / "summary.json"
    write(summary, result)
    try:
        for stage in stages:
            entry, data = files[stage], checked(files[stage])
            validate_spectrum_container(data, bundle["spectrum"], stage=True)
            if data["spectrumContract"] != bundle["spectrum_contract"]:
                raise ValueError("A stage refers to another explicit finite map contract")
            if (data["stage"] != stage or data["sharing"]["mapHash"] != entry["mapHash"] or
                    data["boundInput"] != manifest["input"] or
                    data["status"] != "literal_R_stage_with_exact_common_boundary_two_jets"):
                raise ValueError("New stage map identity differs")
            if not all(data["physicalParameters"].get(k) == v
                       for k, v in constants["parameters"].items()):
                raise ValueError("New stage physical background differs")
            t0 = time.monotonic()
            row = kernel.certify(oracle, data, args.quadratic_mode_cutoff)
            eta = Q(row["normalized_first_jet_upper"]["upper_exact"])
            pos = Q(row["position_perturbation_upper"]["upper_exact"])
            curvature = Q(row["principal_curvature_upper"]["upper_exact"])
            row.update(data=entry, seconds=time.monotonic() - t0,
                       conditional_placement=conditional_placement(eta, pos),
                       curvature_allocation_passed=curvature < 10,
                       planar_projection_derivative_less_than_one=eta < 1)
            path = outdir / ("stage-" + str(stage).zfill(4) + ".json")
            write(path, row)
            small = {k: v for k, v in row.items()
                     if k not in ("rows", "background_cover", "mean_definition")}
            small["certificate"] = ref(path)
            result["stages"].append(small)
            result["seconds"] = time.monotonic() - start
            write(summary, result)
            import json
            print(json.dumps({"stage": stage, "metric_upper": row["continuous_metric_operator_upper"]["upper"],
                              "curvature_upper": row["principal_curvature_upper"]["upper"],
                              "status": row["status"], "seconds": row["seconds"]}), flush=True)
        S = index["finite_stage_count"]
        if index["deep_node"] is not None and S - 1 in files:
            entry = files[S - 1]
            deep_path = outdir / "new-deep-collar.json"
            deep = deep_collar(checked(entry), entry, index, constants, deep_path)
            result["deep_collar"] = {**deep, "certificate": ref(deep_path)}
        else:
            deep = None
        all_selected = index["all_stages_exported"] and set(stages) == set(range(S))
        stage_metric = all(row["metric_gate_passed"] for row in result["stages"])
        stage_curvature = all(row["curvature_allocation_passed"] for row in result["stages"])
        complete_metric = all_selected and stage_metric and deep is not None and deep["metric_gate_passed"]
        complete_curvature = all_selected and stage_curvature and deep is not None and deep["curvature_allocation_passed"]
        planar_embedding = (all_selected and deep is not None and
            deep["planar_projection_derivative_less_than_one"] and
            all(row["planar_projection_derivative_less_than_one"] for row in result["stages"]))
        result.update(
            status=("new_whole_tail_disk_metric_curvature_certified" if complete_metric and complete_curvature
                    else "new_selected_tail_geometry_bounds_recorded"),
            all_finite_stages_audited=all_selected,
            all_finite_stages_certified=all_selected and stage_metric and stage_curvature,
            all_selected_stage_metric_gates_passed=stage_metric,
            all_selected_stage_curvature_allocations_passed=stage_curvature,
            complete_tail_disk_metric_gate_passed=complete_metric,
            complete_tail_disk_curvature_allocation_passed=complete_curvature,
            complete_tail_disk_planar_projection_injective=planar_embedding,
            planar_injectivity_reason=(
                "The same Cartesian perturbation is C1 on the entire convex Euclidean radius-R_cut disk, "
                "is zero inside the new collar, and has derivative operator norm below one on every "
                "new span/collar. Integrating on each straight segment proves that Id+V_xy is injective."
                if planar_embedding else None),
            finite_tail_to_its_own_deep_disk_C2=all_selected and deep is not None,
            prefix_Cartesian_seam_proved=False, global_tail_complete=False,
            seconds=time.monotonic() - start,
        )
    except Exception as exc:
        result.update(status="failed", error=repr(exc), seconds=time.monotonic() - start)
        write(summary, result)
        raise
    write(summary, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("geometry-bundle", "constants", "normalization-certificate", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--stages", default="all")
    parser.add_argument("--quadratic-mode-cutoff", type=int, default=12)
    args = parser.parse_args()
    result = certify(args)
    import json
    print(json.dumps({key: result[key] for key in (
        "status", "complete_tail_disk_metric_gate_passed",
        "complete_tail_disk_curvature_allocation_passed",
        "complete_tail_disk_planar_projection_injective", "seconds"
    )}), flush=True)


if __name__ == "__main__":
    main()
