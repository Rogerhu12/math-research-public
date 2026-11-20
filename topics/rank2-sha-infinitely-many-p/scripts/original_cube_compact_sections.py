#!/usr/bin/env sage-python
"""Lower-degree sections for the SAME four already certified original roots.

The source cube context is retained by object identity and never modified.
Its complete old cube identities remain prerequisites.  The new fractions
are certified by their full low kernels AND full same-function cross products
in R8/R7; old high identities are not relabelled as identities of new sections.
Mathematical execution is public Actions only.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
import importlib.util
import time
from pathlib import Path
from sage.all import matrix
from section_quotient_algebra import canonical, digest


HERE = Path(__file__).resolve().parent


def _progress(stage, **record):
    print("RANK2_COMPACT_CUBE_STAGE " + canonical(dict(stage=stage, **record)), flush=True)


def _source_module():
    path = HERE/"produce-original-cube-section-fractions.py"
    spec = importlib.util.spec_from_file_location("original_compact_cube_kernel_owner", str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def exact_pole_degree_from_complete_kernel(item, label):
    """h0>g forces nonspeciality, and therefore determines deg(Pole f) exactly."""
    genus, degree_L = 85, 204
    power = int(item["section_power"])
    certificate = item["certificate"]
    old_identity = item["complete_global_identity"]
    kernel = item["full_kernel_coordinates"]
    source_dimension = degree_L*power+1-genus
    assert old_identity["original_global_identity_certified"] is True
    assert certificate["all_original_equations_returned"] is True
    assert certificate["both_entire_kernel_projections_injective"] is True
    assert certificate["original_fraction_leading_value"] == 1
    assert int(certificate["same_complete_section_dimension"]) == source_dimension
    h0 = int(certificate["actual_complete_kernel_dimension"])
    assert kernel.nrows() == h0 and kernel.ncols() == 2*source_dimension
    assert h0 > genus
    pole_degree = degree_L*power+1-genus-h0
    assert pole_degree > 0
    return pole_degree, {
        "original_root": label,
        "original_base_genus": genus,
        "original_line_bundle_degree": degree_L,
        "source_section_power": power,
        "actual_complete_source_kernel_dimension": h0,
        "kernel_is_complete_H0_L_power_minus_actual_pole_divisor": True,
        "h0_strictly_greater_than_genus": True,
        "H1_zero_by_nonzero_dual_map_into_canonical_bundle": True,
        "exact_actual_pole_degree": pole_degree,
        "source_low_kernel_certificate_sha256": digest(certificate),
        "source_complete_global_cube_identity_sha256": digest(old_identity),
    }


def build_original_compact_cube_sections(cube_context, progress=None):
    progress = progress or _progress
    started = time.monotonic()
    cube = cube_context
    assert cube["kind"] == "rank2_original_cube_section_fractions_context"
    prime = int(cube["prime"])
    assert prime in (29, 41)
    source = _source_module()
    codec = cube["original_omega_codec"]
    assert codec.field is cube["constants"]
    assert codec.omega == cube["original_omega"]
    rows = cube["extended_original_M2_rows"]
    assert rows.base_ring() is cube["original_fp"]
    assert rows.nrows() == 120 and rows.ncols() >= 1633
    recipes = cube["complete_product_recipes"]
    assert len(recipes[2]) == 324 and len(recipes[3]) == 528
    assert len(recipes[4]) == 732 and len(recipes[6]) == 1140
    evaluator = source.OriginalSectionEvaluator(rows, codec, 1633)
    compact_items, pole_records, kernel_records, cross_records = {}, [], [], []
    dimensions = {}
    for label, old in [("RF", cube["RF"])]+[
            ("RP_%d" % i, cube["RP"][i]) for i in (0, 1, 2)]:
        target_power = 2 if label == "RF" else 3
        source_power = 6 if label == "RF" else 4
        assert int(old["section_power"]) == source_power
        pole_degree, pole_record = exact_pole_degree_from_complete_kernel(old, label)
        if prime == 29:
            expected = {"RF": 240, "RP_0": 452, "RP_1": 454, "RP_2": 454}[label]
            assert pole_degree == expected
        difference_bound = 204*target_power+pole_degree
        low_length = difference_bound+1
        minimum = 204*target_power+1-85-pole_degree
        assert minimum > 0
        assert low_length <= 1633
        root = old["original_root_series"]
        assert root.precision_absolute() >= low_length and root[0] == 1
        root = root.add_bigoh(low_length)
        basis = evaluator.complete_basis(recipes[target_power], low_length)
        supplied = None
        if label == "RP_2":
            first = compact_items["RP_1"]
            assert low_length == int(first["compact_low_window_length"])
            root1 = cube["RP"][1]["original_root_series"]
            assert all(root[i] == root1[i]**prime for i in range(low_length))
            supplied = matrix(codec.field, [
                [c**prime for c in row] for row in first["full_kernel_coordinates"].rows()])
        progress("same original root compact full kernel start",
                 original_root=label, source_power=source_power,
                 compact_power=target_power, exact_pole_degree=pole_degree,
                 full_coefficients=low_length, proved_kernel_lower_bound=minimum)
        item, kernel_record = source.fraction_kernel(
            basis, root, minimum, codec, label, supplied_kernel=supplied)
        item.update({
            "section_power": target_power,
            "original_coordinate": old["original_coordinate"],
            "certified_pole_degree": pole_degree,
            "compact_low_window_length": low_length,
        })
        if label != "RF":
            item["embedding"] = old["embedding"]
            item["vnew"] = old["vnew"]
        # The two terms are genuine sections of the SAME L^(m_new+m_old).
        # Their full degree+1 window proves equality as global sections.
        combined_power = target_power+source_power
        cross_length = 204*combined_power+1
        assert cross_length == (1633 if label == "RF" else 1429)
        arithmetic = source.PairPolynomials(codec, cross_length)
        new_N = arithmetic.truncate(evaluator.section(
            recipes[target_power], item["numerator_coordinates"], target_power))
        new_E = arithmetic.truncate(evaluator.section(
            recipes[target_power], item["denominator_coordinates"], target_power))
        old_N = arithmetic.truncate(evaluator.section(
            recipes[source_power], old["numerator_coordinates"], source_power))
        old_E = arithmetic.truncate(evaluator.section(
            recipes[source_power], old["denominator_coordinates"], source_power))
        residual = arithmetic.sub(
            arithmetic.mul(new_N, old_E), arithmetic.mul(old_N, new_E))
        assert residual == arithmetic.zero
        assert new_N != arithmetic.zero and new_E != arithmetic.zero
        assert old_N != arithmetic.zero and old_E != arithmetic.zero
        if label == "RF":
            assert not new_N[1] and not new_E[1]
        cross_record = {
            "original_root": label,
            "source_section_power": source_power,
            "compact_section_power": target_power,
            "same_complete_section_power": combined_power,
            "complete_global_zero_degree_bound": cross_length-1,
            "full_checked_coefficients": cross_length,
            "full_checked_coefficients_inclusive": [0, cross_length-1],
            "same_original_function_certified": True,
            "all_original_omega_components_zero": True,
            "same_original_M2_owner_and_recipe_basis": True,
            "original_cube_context_and_old_fractions_unchanged": True,
            "original_branch_leading_value": 1,
            "new_numerator_full_cross_window_sha256": arithmetic.hash(new_N),
            "new_denominator_full_cross_window_sha256": arithmetic.hash(new_E),
            "old_numerator_full_cross_window_sha256": arithmetic.hash(old_N),
            "old_denominator_full_cross_window_sha256": arithmetic.hash(old_E),
            "entire_cross_residual_sha256": arithmetic.hash(residual),
            "source_complete_global_cube_identity_sha256": digest(old["complete_global_identity"]),
        }
        item["same_original_function_certified"] = True
        item["same_original_function_certificate"] = cross_record
        item["exact_pole_degree_certificate"] = pole_record
        if label == "RP_2":
            for name in ("numerator_coordinates", "denominator_coordinates"):
                assert list(item[name]) == [
                    c**prime for c in compact_items["RP_1"][name]]
        compact_items[label] = item
        pole_records.append(pole_record)
        kernel_records.append(kernel_record)
        cross_records.append(cross_record)
        dimensions[label] = int(item["full_kernel_coordinates"].nrows())
        progress("same original root compact fraction globally certified",
                 original_root=label, compact_power=target_power,
                 complete_low_kernel_dimension=dimensions[label],
                 full_cross_coefficients=cross_length)
    receipt = {
        "kind": "rank2_original_compact_cube_sections",
        "status": "same_original_RF_and_Ri_in_lower_section_degrees_certified",
        "prime": prime, "base_level": 867, "base_genus": 85,
        "exact_actual_pole_degree_certificates": pole_records,
        "complete_compact_low_kernel_certificates": kernel_records,
        "complete_same_function_cross_identities": cross_records,
        "actual_compact_kernel_dimensions": dimensions,
        "compact_RF_section_power": 2, "compact_RP_section_power": 3,
        "original_cube_context_preserved_by_object_identity": True,
        "source_RF_R6_and_RP_R4_coefficients_not_replaced": True,
        "old_complete_global_cube_identities_not_relabelled_as_new_section_identities": True,
        "original_omega_and_P2_own_full_equations_preserved": True,
        "old_high_6941_and_all_4287_gates_are_prerequisites": True,
        "same_original_complete_product_recipes_sha256": digest(recipes),
        "source_cube_producer_sha256": hashlib.sha256(Path(source.__file__).read_bytes()).hexdigest(),
        "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "large_divisors_or_original_shadow_computed": False,
        "elapsed_seconds": time.monotonic()-started,
    }
    compact = {
        "kind": "rank2_original_compact_cube_sections_context",
        "cube_context": cube,
        "prime": prime, "constants": cube["constants"],
        "original_omega": cube["original_omega"],
        "complete_product_recipes": recipes,
        "RF": compact_items["RF"],
        "RP": {i: compact_items["RP_%d" % i] for i in (0, 1, 2)},
        "certificate": receipt,
    }
    assert compact["cube_context"] is cube_context
    assert compact["complete_product_recipes"] is cube_context["complete_product_recipes"]
    return compact, receipt
