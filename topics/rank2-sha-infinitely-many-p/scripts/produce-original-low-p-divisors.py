#!/usr/bin/env sage-python
"""Six original P endpoint zero/pole divisors from the complete low kernels.

The authenticated base section ratios, full original rank-306 normalization,
and all six endpoint divisors are recomputed in one offline public Actions
process.  Only receipts and hashes are printed; coefficient objects stay in
memory.  No cube root, F fraction on Y, large E divisor or shadow is claimed.
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
from sage.all import vector
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest
from original_shadow_receipt_tools import add_pinned_arguments, pinned_request, validate_envelope
from original_affine_fast_operations import build_original_affine_fast_operations
from original_section_ring_embedding import build_original_section_ring_embedding
from original_ys_fraction_bridge import OriginalFractionModel
from original_ys_divisor_ideal_tools import OriginalAffineIdealEngine
from original_ys_artinian_norm_tools import OriginalArtinianNormTools
from original_low_p_complete_divisors import OriginalLowPCompleteDivisors

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"
SOURCE_FILES = (
    "launch-original-low-p-divisors.py", "produce-original-low-p-divisors.py",
    "original_low_p_complete_divisors.py",
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
    print("RANK2_LOW_P_DIVISORS_STAGE " + canonical(dict(
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


def build_original_six_p_divisors(affine, maps, progress_callback=None,
                                 kernel_method="minimal"):
    """Build only the actual six P endpoints in the same complete original Y.

    The optional endpoint_section_fractions argument on the low-P reader
    authenticates these actual generic-section pairs without changing the
    embedding's truthful F_and_P_fractions_built=False certificate.
    """
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
    k, R = model.k, model.P
    assert k is maps["constants"] is maps["local_context"]["constants"]
    omega = maps["original_omega"]
    assert omega is maps["local_context"]["omega"] and omega.parent() is k
    assert omega != 1 and omega**2+omega+1 == 0
    assert tuple(maps["sigma_a_index"]) == (2, 0, 1)
    recipes = maps["complete_RR_product_recipes"][3]
    assert len(recipes) == 528
    pairs, functions, pair_records = {i:{} for i in (0, 1, 2)}, {}, []
    for i in (0, 1, 2):
        original = maps["P"][i]
        assert int(original["section_power"]) == 3
        assert original["vnew"] == maps["local_context"]["packet"][i]["vnew"]
        assert original["vnew"].parent() is k and original["vnew"] != 0
        for j in (1, 4):
            report("same original P homogeneous endpoint sections start",
                   original_embedding=i, degeneracy_exponent=j)
            N = embedding["section_coordinates"](
                3, recipes, original["numerator_coordinates"], j)
            D = embedding["section_coordinates"](
                3, recipes, original["denominator_coordinates"], j)
            pair = embedding["same_degree_fraction"](
                N, D, 3, "original Y_%d; pi_%d" % (i, j))
            assert pair["section_power"] == 3 and pair["common_infinity_shift"] == 12
            assert pair["numerator"].base_ring() is R
            assert pair["denominator"].base_ring() is R
            if i == 2:
                # Constant conjugation is checked on every actual coordinate;
                # the separate original Artin ordering (2,0,1) stays intact.
                for key in ("numerator_coordinates", "denominator_coordinates"):
                    assert tuple(original[key]) == tuple(c**29 for c in maps["P"][1][key])
                assert original["vnew"] == maps["P"][1]["vnew"]**29
                for key in ("numerator", "denominator", "infinity_numerator", "infinity_denominator"):
                    parent = pairs[1][j][key].base_ring()
                    conjugate = vector(parent, [
                        parent([c**29 for c in polynomial.list()])
                        for polynomial in pairs[1][j][key]])
                    assert pair[key] == conjugate
            pairs[i][j] = pair
            Y = model.same_degree_section_fraction(pair)
            y = model.coerce(k(2)/original["vnew"])*Y+model.one
            assert y.model is model and not y.is_zero()
            functions[(i, j)] = y
            pair_records.append({
                "original_embedding":i, "degeneracy_exponent":j,
                "same_original_section_fraction":pair["certificate"],
                "endpoint_formula":"(2/vnew_i)*pi_j(Y_i)+1",
                "original_endpoint_fraction":y.receipt(),
                "both_logarithmic_factors_j_cubed_retained":True,
                "constant_Frobenius_complete_return_checked":i == 2,
                "original_Artin_order_retained":[2, 0, 1],
            })
    assert set(functions) == {(i, j) for i in (0, 1, 2) for j in (1, 4)}
    assert embedding_receipt["F_and_P_fractions_built"] is False
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
    reader = OriginalLowPCompleteDivisors(
        model, tools_by_chart, progress=report,
        endpoint_section_fractions=pairs)
    assert reader.maps is maps and reader.affine is affine and reader.model is model
    assert set(reader.source_receipt["source_dependencies"]).issubset(SOURCE_FILES)
    assert reader.kernel_context["maps"] is maps
    kernel_records = reader.kernel_receipt["all_three_original_embeddings"]
    assert len(kernel_records) == 3
    for i, record in enumerate(kernel_records):
        assert record["original_embedding"] == i
        assert record["full_rows"] == 1226
        assert record["complete_section_dimension"] == 528
        assert record["entire_kernel_dimension"] == 152
        assert record["all_kernel_rows_return_on_every_original_coefficient"] is True
        assert record["both_paired_projections_injective"] is True
        assert record["selected_original_fraction_is_first_full_kernel_row"] is True
    divisors, endpoint_records = {}, []
    for i in (0, 1, 2):
        for j in (1, 4):
            actual = functions[(i, j)]
            report("complete original low-P zero and pole ideals start",
                   original_embedding=i, degeneracy_exponent=j)
            item = reader.complete_endpoint_divisor(
                i, j, actual, "original P_%d endpoint pi_%d" % (i, j))
            assert item["function"] is actual
            assert item["positive_degree"] == item["negative_degree"] == 2256
            charts = item["charts"]
            assert set(charts) == {False, True}
            lengths = {}
            for sign in ("positive", "negative"):
                finite = charts[False][sign]
                full_infinity = charts[True][sign]
                boundary = charts[True][sign+"_boundary"]
                assert finite.engine is tools_by_chart[False].engine
                assert full_infinity.engine is boundary.engine is tools_by_chart[True].engine
                assert finite.length+boundary.length == 2256
                lengths[sign] = {
                    "finite_length":int(finite.length),
                    "full_infinity_chart_ideal_length":int(full_infinity.length),
                    "infinity_boundary_length":int(boundary.length),
                    "full_projective_degree":int(finite.length+boundary.length),
                }
            for flag in (False, True):
                record = item["records"][str(flag)]
                assert record["every_remaining_original_N_and_D_vector_returned"] is True
                assert record["original_kernel_rows_total"] == 152
                assert 1 <= record["used_full_A_generator_blocks"] <= 152
                assert record["same_source_subset_on_both_charts"] is True
            source = item["records"]["entire_original_low_section_source"]
            assert source["original_embedding"] == i and source["degeneracy_exponent"] == j
            assert source["actual_supplied_original_function_crossed_on_both_charts"] is True
            assert source["whole_nonreduced_ideals_and_all_residue_degrees_retained"] is True
            assert source["full_original_zero_and_pole_degrees"] == 2256
            endpoint_record = {
                "original_embedding":i, "degeneracy_exponent":j,
                "complete_zero_and_pole_lengths":lengths,
                "same_supplied_original_function":actual.receipt(),
                "complete_divisor_records":item["records"],
            }
            divisors[(i, j)] = item
            endpoint_records.append(endpoint_record)
            emit("RANK2_LOW_P_ENDPOINT", endpoint_record)
    assert set(divisors) == set(functions) and len(divisors) == 6
    summary = reader.receipt_summary()
    assert summary["completed_endpoint_divisors"] == 6
    receipt = {
        "kind":"rank2_original_six_low_P_complete_divisors",
        "status":"all_six_original_P_zero_and_pole_ideals_certified",
        "prime":29, "original_level":3468,
        "original_normalization_module_rank":306,
        "same_original_section_embedding":embedding_receipt,
        "same_original_six_endpoint_pairs":pair_records,
        "complete_original_low_P_kernels":reader.kernel_receipt,
        "complete_endpoint_divisors":endpoint_records,
        "complete_low_P_reader_summary":summary,
        "endpoint_count":6, "each_complete_zero_degree":2256,
        "each_complete_pole_degree":2256,
        "all_152_paired_rows_returned_on_both_charts":True,
        "complete_infinity_boundary_ideals_verified":True,
        "same_original_constant_field_and_omega_retained":True,
        "same_original_Artin_order":[2, 0, 1],
        "generic_embedding_F_and_P_fraction_flag_left_false":True,
        "original_F_fraction_on_Y_computed":False,
        "original_cube_roots_computed":False,
        "complete_large_intersection_divisors_computed":False,
        "all_intersection_closed_points_computed":False,
        "original_shadow_computed":False,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
    }
    context = {
        "kind":"rank2_original_six_low_P_complete_divisors_context",
        "original_map_sections_context":maps,
        "original_affine_context":affine, "embedding_context":embedding,
        "model":model, "endpoint_section_fractions":pairs,
        "endpoint_functions":functions, "tools_by_chart":tools_by_chart,
        "reader":reader, "complete_endpoint_divisors":divisors,
        "certificate":receipt,
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
    map_module = load_source("produce-original-map-section-fractions.py", "low_p_original_map_sections")
    maps, map_receipt = map_module.build_original_map_section_fractions(
        args.prime, first, packet, q_precision=1429)
    emit("RANK2_MAP_SECTIONS", map_receipt)
    normalization_module = load_source(
        "produce-original-y-affine-normalization.py", "low_p_original_normalization")
    affine, normalization_receipt = normalization_module.build_original_y_affine_normalization(
        prime=args.prime, q_precision=args.q_precision, batch_size=args.batch_size)
    emit("RANK2_Y_AFFINE", normalization_receipt)
    progress("complete original coefficient-operation adapter start")
    affine, fast_receipt = build_original_affine_fast_operations(affine, progress=progress)
    emit("RANK2_Y_FAST_OPERATIONS", fast_receipt)
    context, divisor_receipt = build_original_six_p_divisors(
        affine, maps, progress_callback=progress, kernel_method=args.kernel_method)
    assert context["original_affine_context"] is affine
    assert context["original_map_sections_context"] is maps
    assert divisor_receipt["status"] == "all_six_original_P_zero_and_pole_ideals_certified"
    assert divisor_receipt["endpoint_count"] == 6
    receipt = {
        "kind":"rank2_original_low_P_complete_divisor_pipeline",
        "status":"all_requested_original_low_P_divisor_gates_completed",
        "prime":args.prime, "level":3468,
        "q_precision":args.q_precision, "base_map_q_precision":1429,
        "batch_size":args.batch_size, "kernel_method":args.kernel_method,
        "same_original_map_sections_result_sha256":digest(map_receipt),
        "same_original_normalization_result_sha256":digest(normalization_receipt),
        "complete_fast_operations_initial_receipt":fast_receipt,
        "complete_coefficient_operation_summary":affine["coefficient_contraction_summary"](),
        "complete_six_endpoint_divisors":divisor_receipt,
        "all_objects_retained_in_same_offline_process":True,
        "complete_original_six_P_zero_and_pole_ideals_computed":True,
        "each_complete_original_endpoint_zero_and_pole_degree":2256,
        "original_F_fraction_on_Y_computed":False,
        "original_cube_roots_computed":False,
        "complete_large_intersection_divisors_computed":False,
        "all_intersection_closed_points_computed":False,
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
    retained = {"maps":maps, "affine":affine, "six_P_divisors":context,
                "certificate":receipt}
    globals()["ORIGINAL_LOW_P_COMPLETE_DIVISORS_CONTEXT"] = retained
    emit("RANK2_LOW_P_DIVISORS", receipt)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
