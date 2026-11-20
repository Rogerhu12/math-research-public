#!/usr/bin/env sage-python
"""Original F zero/pole divisors from the complete mixed low-section kernel.

The authenticated base section ratios, full original rank-306 normalization,
and both original yF divisors are recomputed in one offline public Actions
process.  The full mixed denominator ideal, its complete integral image,
and both effective ideal quotients retain all multiplicities on both charts.
Only receipts and hashes are printed; coefficient objects stay in memory.
No cube root, large E divisor, closed-point decomposition or shadow is claimed.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest
from original_shadow_receipt_tools import add_pinned_arguments, pinned_request, validate_envelope
from original_affine_fast_operations import build_original_affine_fast_operations
from original_section_ring_embedding import build_original_section_ring_embedding
from original_ys_fraction_bridge import OriginalFractionModel
from original_ys_divisor_ideal_tools import OriginalAffineIdealEngine
from original_ys_artinian_norm_tools import OriginalArtinianNormTools
from original_low_f_complete_divisors import OriginalLowFCompleteDivisors

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"
SOURCE_FILES = (
    "launch-original-low-f-divisors.py", "produce-original-low-f-divisors.py",
    "original_low_f_complete_divisors.py", "original_ys_integral_image_tools.py",
    "original_ys_artinian_norm_tools.py", "original_ys_exact_reuse.py", "original_ys_fraction_bridge.py",
    "original_affine_fast_operations.py", "original_section_ring_embedding.py",
    "original_ys_divisor_ideal_tools.py", "original_ys_closed_point_tools.py",
    "original_ys_local_value_tools.py", "original_shadow_relative_six_tools.py",
    "original_shadow_coefficient_tools.py", "original_shadow_tate_trace_tools.py",
    "original_affine_multiplication.py", "produce-original-y-affine-normalization.py",
    "produce-original-y-colon-apery.py", "produce-original-y-global-section-and-ys.py",
    "produce-original-tuv-section-fractions.py",
    "produce-original-map-section-fractions.py", "section_quotient_algebra.py",
    "read-original-shadow-pass-receipts.py", "original_shadow_receipt_tools.py",
    "produce-original-shadow-local-input.py", "original_good_prime_germ_tools.py",
    "check-r873-original-cm-petersson-degree.py", "original_low_weight_cm_tools.py",
    "produce-r917-original-global-rr-q-lattice.py", "original_pari_m2_basis.py",
    "original_shadow_coordinate_tools.py")


def progress(stage, **record):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_LOW_F_DIVISORS_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **record)), flush=True)


def emit(name, receipt):
    payload = canonical(receipt)
    print(name+"_RESULT "+payload, flush=True)
    print(name+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


def load_source(name, alias):
    spec = importlib.util.spec_from_file_location(alias, str(HERE/name))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_original_f_divisors(affine, maps, progress_callback=None,
                             kernel_method="minimal"):
    """Build the actual yF zero/pole ideals in the same complete original Y."""
    report = progress_callback or progress
    assert int(maps["prime"]) == 29 and kernel_method == "minimal"
    embedding, embedding_receipt = build_original_section_ring_embedding(
        affine, maps, progress=report, with_map_fractions=False)
    assert embedding["original_affine_context"] is affine
    assert embedding["original_map_sections_context"] is maps
    assert embedding["certificate"] is embedding_receipt
    assert embedding_receipt["F_and_P_fractions_built"] is False
    assert not embedding["F"] and all(not embedding["P"][i] for i in (0, 1, 2))
    model = OriginalFractionModel(embedding, affine)
    k = model.k
    assert k is maps["constants"] is maps["local_context"]["constants"]
    assert int(k.characteristic()) == 29 and k.cardinality() == 29**2
    omega = maps["original_omega"]
    assert omega is maps["local_context"]["omega"] and omega.parent() is k
    assert omega != 1 and omega**2+omega+1 == 0
    assert tuple(maps["sigma_a_index"]) == (2, 0, 1)
    identity = {
        "original_curve":"X0(3468)",
        "original_complete_normalization_signature":affine["certificate"]["exact_multiplication_signature_sha256"],
        "original_Y_M2_basis":embedding["coordinate_basis_id"],
    }
    tools_by_chart = {}
    for flag in (False, True):
        engine = OriginalAffineIdealEngine(
            model.operations["chart"](infinity=flag), progress=report,
            kernel_method=kernel_method)
        tools_by_chart[flag] = OriginalArtinianNormTools(
            engine, affine, identity, omega, progress=report)
    reader = OriginalLowFCompleteDivisors(model, tools_by_chart, progress=report)
    assert reader.maps is maps and reader.affine is affine and reader.model is model
    assert reader.embedding is embedding and reader.kernel_context["maps"] is maps
    assert set(reader.source_receipt["source_dependencies"]).issubset(SOURCE_FILES)
    assert reader.source_receipt["underlying_embedding_F_and_P_fractions_built"] is False
    assert reader.source_receipt["underlying_embedding_certificate_unchanged"] is True
    assert reader.source_receipt["same_original_constant_routine_and_root_order_used"] is True
    assert reader.source_receipt["original_SY_over_J_and_both_scalar_cusp_sections_returned"] is True
    assert reader.source_receipt["actual_original_yF_equals_vF_over_epsilon_theta_cubed"] is True
    kernel = reader.kernel_receipt
    assert kernel["full_rows"] == 1429 and kernel["full_columns"] == 1260
    assert kernel["original_numerator_dimension"] == 936
    assert kernel["original_denominator_dimension"] == 324
    assert kernel["entire_kernel_dimension"] == 144
    for key in (
            "all_original_equations_and_both_entire_projections_returned",
            "all_free_columns_and_entire_nullity_verified",
            "first_original_selected_pair_is_first_entire_kernel_row",
            "original_S_cubed_factor_and_global_zero_bound_preserved"):
        assert kernel[key] is True
    assert kernel["degree_of_original_denominator_bundle"] == 228
    assert kernel["degree_of_original_D_prime"] == 180
    actual = reader.original_function
    assert actual.model is model and not actual.is_zero()
    assert reader.original_vF.model is model and not reader.original_vF.is_zero()
    report("complete original low-F zero and pole ideals start")
    item = reader.complete_first_factor_divisor(actual, "original central yF")
    assert item["function"] is actual
    assert item["positive_degree"] == item["negative_degree"] == 1296
    charts = item["charts"]
    assert set(charts) == {False, True}
    lengths = {}
    for sign in ("positive", "negative"):
        finite = charts[False][sign]
        full_infinity = charts[True][sign]
        boundary = charts[True][sign+"_boundary"]
        assert finite.engine is tools_by_chart[False].engine
        assert full_infinity.engine is boundary.engine is tools_by_chart[True].engine
        assert finite.length+boundary.length == 1296
        lengths[sign] = {
            "finite_length":int(finite.length),
            "full_infinity_chart_ideal_length":int(full_infinity.length),
            "infinity_boundary_length":int(boundary.length),
            "full_projective_degree":int(finite.length+boundary.length),
        }
    for flag in (False, True):
        record = item["records"][str(flag)]
        assert record["original_kernel_rows_total"] == 144
        assert 1 <= record["used_full_A_generator_blocks"] <= 144
        assert record["every_remaining_original_denominator_returned"] is True
        assert record["same_source_subset_on_both_charts"] is True
        image = record["entire_image_return"]
        assert image["completed_operations"] == 1
        assert image["same_original_complete_nonreduced_ideals_only"] is True
        numerator = record["full_numerator_from_entire_integral_image"]
        assert numerator["entire_source_module_maps_integrally"] is True
        whole_image = numerator["complete_original_integral_image"]
        assert whole_image["all_306_original_source_basis_rows_divided_exactly"] is True
        assert whole_image["every_image_row_times_original_denominator_returned"] is True
        assert whole_image["full_source_basis_preserved_without_rescaling"] is True
        for sign in ("positive", "negative"):
            quotient = record[sign+"_quotient"]
            assert quotient["full_dividend_in_divisor_inclusion_verified"] is True
            assert quotient["complete_norm_equality_used_only_with_proved_containment"] is True
            assert quotient["full_quotient_times_divisor_hnf_equals_dividend"] is True
    source = item["records"]["entire_original_mixed_source"]
    assert source["full_kernel"] is kernel
    assert source["full_projective_degrees"] == dict(
        D_prime=1080, A=4752, D=4752, common=3456, zero=1296, pole=1296)
    for key in (
            "actual_supplied_original_yF_crossed_on_both_charts",
            "original_theta17_and_both_cusp_frames_preserved",
            "all_original_cusp_multiplicities_and_residue_degrees_retained",
            "complete_ideal_quotients_with_full_products_returned"):
        assert source[key] is True
    assert embedding_receipt["F_and_P_fractions_built"] is False
    summary = reader.receipt_summary()
    assert summary["completed_first_factor_divisors"] == 1
    assert summary["source"] is reader.source_receipt
    receipt = {
        "kind":"rank2_original_low_F_complete_divisors",
        "status":"original_F_zero_and_pole_ideals_certified",
        "prime":29, "original_level":3468,
        "original_normalization_module_rank":306,
        "same_original_section_embedding":embedding_receipt,
        "complete_original_mixed_F_kernel":kernel,
        "same_original_yF_function":actual.receipt(),
        "same_original_pi2_vF_function":reader.original_vF.receipt(),
        "same_original_yF_section_pair":reader.selected_pair["certificate"],
        "complete_zero_and_pole_lengths":lengths,
        "complete_divisor_records":item["records"],
        "complete_low_F_reader_summary":summary,
        "complete_zero_degree":1296, "complete_pole_degree":1296,
        "all_144_paired_rows_and_remaining_denominators_returned":True,
        "complete_integral_image_and_both_effective_quotients_returned":True,
        "complete_infinity_boundary_ideals_verified":True,
        "same_original_constant_field_and_omega_retained":True,
        "same_original_Artin_order":[2, 0, 1],
        "generic_embedding_F_and_P_fraction_flag_left_false":True,
        "original_cube_roots_computed":False,
        "complete_P_endpoint_divisors_computed":False,
        "complete_large_intersection_divisors_computed":False,
        "all_closed_points_computed":False,
        "original_shadow_computed":False,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
    }
    context = {
        "kind":"rank2_original_low_F_complete_divisors_context",
        "original_map_sections_context":maps,
        "original_affine_context":affine, "embedding_context":embedding,
        "model":model, "original_function":actual,
        "tools_by_chart":tools_by_chart, "reader":reader,
        "complete_first_factor_divisor":item, "certificate":receipt,
    }
    return context, receipt


def main():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    add_pinned_arguments(parser)
    parser.add_argument("--q-precision", type=int, default=2453)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--kernel-method", choices=("minimal",), default="minimal")
    args = parser.parse_args()
    assert args.prime == 29 and args.q_precision == 2453 and args.batch_size == 64
    assert args.kernel_method == "minimal"
    request = pinned_request(args)
    incoming = sys.stdin.buffer.read(2*1024*1024+1)
    assert len(incoming) <= 2*1024*1024
    envelope = json.loads(incoming.decode("utf-8"))
    host_hash = hashlib.sha256((HERE/"read-original-shadow-pass-receipts.py").read_bytes()).hexdigest()
    first, packet = validate_envelope(envelope, request, host_hash)
    progress("both original complete characteristic-zero PASS authenticated",
             public_pass_envelope_sha256=envelope["envelope_sha256"])
    map_module = load_source("produce-original-map-section-fractions.py", "low_f_original_map_sections")
    maps, map_receipt = map_module.build_original_map_section_fractions(
        args.prime, first, packet, q_precision=1429)
    emit("RANK2_MAP_SECTIONS", map_receipt)
    normalization_module = load_source(
        "produce-original-y-affine-normalization.py", "low_f_original_normalization")
    affine, normalization_receipt = normalization_module.build_original_y_affine_normalization(
        prime=args.prime, q_precision=args.q_precision, batch_size=args.batch_size)
    emit("RANK2_Y_AFFINE", normalization_receipt)
    progress("complete original coefficient-operation adapter start")
    affine, fast_receipt = build_original_affine_fast_operations(affine, progress=progress)
    emit("RANK2_Y_FAST_OPERATIONS", fast_receipt)
    context, divisor_receipt = build_original_f_divisors(
        affine, maps, progress_callback=progress, kernel_method=args.kernel_method)
    assert context["original_affine_context"] is affine
    assert context["original_map_sections_context"] is maps
    assert divisor_receipt["status"] == "original_F_zero_and_pole_ideals_certified"
    assert divisor_receipt["complete_zero_degree"] == divisor_receipt["complete_pole_degree"] == 1296
    receipt = {
        "kind":"rank2_original_low_F_complete_divisor_pipeline",
        "status":"all_requested_original_low_F_divisor_gates_completed",
        "prime":args.prime, "level":3468,
        "q_precision":args.q_precision, "base_map_q_precision":1429,
        "batch_size":args.batch_size, "kernel_method":args.kernel_method,
        "same_original_map_sections_result_sha256":digest(map_receipt),
        "same_original_normalization_result_sha256":digest(normalization_receipt),
        "complete_fast_operations_initial_receipt":fast_receipt,
        "complete_coefficient_operation_summary":affine["coefficient_contraction_summary"](),
        "complete_first_factor_divisor":divisor_receipt,
        "all_objects_retained_in_same_offline_process":True,
        "complete_original_F_zero_and_pole_ideals_computed":True,
        "complete_original_zero_and_pole_degree":1296,
        "original_cube_roots_computed":False,
        "complete_P_endpoint_divisors_computed":False,
        "complete_large_intersection_divisors_computed":False,
        "all_closed_points_computed":False,
        "original_shadow_computed":False,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "public_pass_envelope_sha256":envelope["envelope_sha256"],
        "authenticated_public_jobs":envelope["authentication"],
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID"),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"), "sage_version":SAGE_VERSION,
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in SOURCE_FILES},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    retained = {"maps":maps, "affine":affine, "F_divisors":context,
                "certificate":receipt}
    globals()["ORIGINAL_LOW_F_COMPLETE_DIVISORS_CONTEXT"] = retained
    emit("RANK2_LOW_F_DIVISORS", receipt)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
