#!/usr/bin/env python3
"""Four true R83 fourth tangents against the bound R98 character extension.

Consumes the published weight-zero 15-row certificate.  It does not rebuild
the old 14 response columns, target, rank test, or a large span.  Only four
new original columns are evaluated, exclusively in public repository Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

import literature_colored_profile_algebra as colored
import literature_full_phase_bridge_exact as producer
import literature_full_phase_rational_dual as dual
import literature_pure_bulk_exact_membership as exact
import literature_range_profile_algebra as formal
import literature_rational_volterra_polynomial as poly
import literature_total_P1_scaling_blocks as blocks


SCHEMA = "visible-flex-R83-fourth-character-transverse-v1"
BLOCKS_SHA = "40ff170136838907ecb4d2557c2ba3b4d06b5f3fcf63746697f3d5248e92d0fa"
CERTIFICATE_SHA = "1146e6789d2f842ecc255930e2394bec5073029b13dcff4cc6f1aa445d07a78d"
CERTIFICATE_BYTES = 56173
CERTIFICATE_SOURCE = "5ba4eceb196f6c899aae45921b3802014a0e09c6"
TOPIC = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = TOPIC/"notes/actions-43638896281-1-total_P1_blocks/total-P1-blocks-weight-p0.json"
TEMPLATE_RECORDS = (
    {"name": "tau_p0_p2", "pair": (0, 2), "v2_original_index": 1,
     "sha256": "74989d9bb1c98d42670b014315707d42bf4cd936c4b1f9251e67badda4462b13",
     "known_zero_by_complete_phase_Jacobi": True},
    {"name": "tau_p1_t1", "pair": (1, 7), "v2_original_index": 12,
     "sha256": "a36765c31af4d4583535ced0ac473d79f8c2a48081a45db7bede1002f7a15d76",
     "known_zero_by_complete_phase_Jacobi": False},
    {"name": "tau_p2_s1", "pair": (2, 6), "v2_original_index": 16,
     "sha256": "4cbaf0a06482ef9788d071ed368e6b811cda237bf910e16a67aeb60f1259c779",
     "known_zero_by_complete_phase_Jacobi": True},
    {"name": "h_shape_k", "pair": None, "v2_original_index": 109,
     "sha256": "63ec5cb74cb487c52a3e81f1f0b010352f7df57edabb1f08f42dea9093eb52ee",
     "known_zero_by_complete_phase_Jacobi": False},
)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def dependencies():
    old = blocks.dependencies()
    if old["driver"]["sha256"] != BLOCKS_SHA:
        raise ValueError("explicitly rebind changed compact response/weight interfaces")
    new = dict(old)
    new["scaling_block_driver"] = new.pop("driver")
    new["driver"] = dual.file_identity(__file__)
    return old, new


def load_certificate(path, expected_sources):
    raw = path.read_bytes()
    if len(raw) != CERTIFICATE_BYTES or hashlib.sha256(raw).hexdigest() != CERTIFICATE_SHA:
        raise ValueError("R98 original weight-zero certificate bytes changed")
    value = json.loads(raw)
    if (value.get("schema") != blocks.BLOCK_SCHEMA or value.get("completion") != "complete"
            or value.get("outcome") != "nonmember_certified" or value.get("weight") != 0
            or value.get("github_run_id") != "43638896281"
            or value.get("github_sha") != CERTIFICATE_SOURCE
            or value.get("source_hashes") != expected_sources):
        raise ValueError("R98 source/scope identity mismatch")
    reduction = value["response_reduction"]
    if (reduction["original_block_columns"] != 16
            or reduction["proved_true_response_dimension_upper_bound"] != 14
            or len(reduction["verified_original_dependencies"]) != 2):
        raise ValueError("R98 true upper-bound certificate mismatch")
    evaluation = value["original_evaluation"]
    witness = evaluation["dual_certificate"]
    prime = evaluation["coefficient_arithmetic"]["prime"]
    if prime != 2147483647 or not witness["rational_nonmembership_certified"]:
        raise ValueError("expected original checked prime and full rational minor")
    matrix = witness["modular_augmented_matrix"]
    coefficients = witness["modular_functional_coefficients"]
    if len(matrix) != 15 or any(len(row) != 15 for row in matrix) or len(coefficients) != 15:
        raise ValueError("expected complete 15-row Cramer certificate")
    values = [sum(c*row[j] for c, row in zip(coefficients, matrix)) % prime for j in range(15)]
    kappa = values[-1]
    if any(values[:-1]) or not kappa or kappa != witness["modular_functional_target_value"]:
        raise AssertionError("bound modular functional does not verify its old matrix")
    if (witness["modular_pivot_determinant"]*kappa) % prime != witness["modular_augmented_determinant"]:
        raise AssertionError("bound exact Schur certificate changed")
    labels = witness["selected_evaluation_labels"]
    if len(labels) != 15:
        raise ValueError("all original evaluation labels required")
    return value, prime, labels, coefficients, kappa


def restore_four_original_templates(limits, report):
    """Restore only the colored local root needed for h_shape(k).

    No old constant fourth target, old 14 response columns, or membership
    problem is compiled.  Three bracket templates are direct raw formulas.
    """
    ring = colored.ColoredRing(limits)
    a, b, c = (ring.color(name) for name in ("a", "b", "c"))
    basis = exact.operator_basis(ring)
    templates = []
    for record in TEMPLATE_RECORDS[:3]:
        i, j = record["pair"]
        templates.append(basis[i](a, basis[j](b, c))-basis[j](a, basis[i](b, c)))
    density, records, expansion_count = producer.compile_colored_local(ring)
    normalizer = colored.ColoredNormalizer(ring)
    pieces = producer.raw_decomposition(density, normalizer)
    key = (0, 1, 0, 0, 0, 0, 0, 0)
    template = pieces["h_shape_obstruction"].terms.get(key)
    if template is None:
        raise AssertionError("h_shape(k) original coefficient missing")
    templates.append(template)
    grading = blocks.ScalingGrading(ring)
    identities = []
    for record, value in zip(TEMPLATE_RECORDS, templates):
        actual_hash = ring.digest(value)
        if actual_hash != record["sha256"]:
            raise AssertionError("new column did not restore its bound original third formula")
        if set(grading.split(value)) != {0}:
            raise AssertionError("new third column is not original weight zero")
        swap = ring.substitute(value, {"b": c, "c": b})
        symmetry = normalizer.word.expression(value-swap)
        if symmetry.terms:
            raise AssertionError("original inner-slot symmetry required by evaluation cache")
        identities.append({**record, "original_hash_matched": True,
            "raw_terms": len(value.terms), "inner_symmetry_original_zero_sha256": symmetry.digest()})
    report["restored_templates"] = identities
    report["restoration"] = {"compiled_roots": "only R56 colored local third root and its exact R73/R79 decomposition",
        "old_constant_fourth_target_compiled": False, "old_response_columns_evaluated": 0,
        "old_rank_or_span_rerun": False, "decomposition_original_reconstruction_verified": True,
        "coefficient_nodes": len(ring.algebra.c.nodes), "profile_atoms": len(ring.p.atoms),
        "geometry_expansion_nodes": expansion_count, "root_records_sha256": digest(records)}
    return ring, templates


def extension_value(column, coefficients, kappa, prime):
    if len(column) != len(coefficients):
        raise ValueError("same 15 original rows required")
    numerator = sum(c*v for c, v in zip(coefficients, column)) % prime
    return numerator, numerator*pow(kappa, prime-2, prime) % prime


def evaluate_four(args, ring, templates, labels, coefficients, kappa, prime, remaining, report):
    context = poly.PolynomialContext(prime, 2, 3, seconds=remaining,
        max_degree=args.max_degree, memory_mib=args.memory_mib, max_operations=args.max_operations)
    _, _, report["same_bound_profile"] = dual.fixed_profiles(context, 8)
    quadratic = exact.matrix_operator(context, blocks.unit(7))
    values = []
    for index, (record, template) in enumerate(zip(TEMPLATE_RECORDS, templates)):
        third = poly.EvaluatedThirdOperator(ring.p, context, template)
        modes = blocks.full_response(context, third, quadratic)
        column = []
        for label in labels:
            part = 0 if label["component"] == "real" else 1
            column.append(modes[label["mode"]].value(F(label["t"]))[part])
        numerator, normalized = extension_value(column, coefficients, kappa, prime)
        if record["known_zero_by_complete_phase_Jacobi"] and numerator:
            raise AssertionError("new values violated the complete-phase Jacobi zero gate")
        result = {"index": index, "third_name": record["name"],
            "quadratic_coordinates": list(map(str, blocks.unit(7))),
            "original_third_sha256": record["sha256"], "projected_weight": 0,
            "original_mode_polynomial_sha256": {str(mode): modes[mode].digest() for mode in producer.MODES},
            "all_15_original_values_mod_p": column,
            "unnormalized_lambda0_value_mod_p": numerator,
            "normalized_Lambda_extension_value_mod_p": normalized,
            "nonzero_exact_rational_extension_value_proved": bool(numerator),
            "real_value_sign_claimed": False,
            "known_exact_zero_from_paper_Jacobi": record["known_zero_by_complete_phase_Jacobi"],
            "zero_mod_p_alone_is_not_exact_zero_proof": not record["known_zero_by_complete_phase_Jacobi"]}
        values.append(result)
        report["completed_new_columns"] = values
        print(json.dumps({"phase": "four_original_transverse_values", "column": index,
                          "nonzero_extension_proved": bool(numerator)}), flush=True)
        context.check(0)
    return values, context.coefficient_report()


def small_toys():
    limits = exact.Limits(seconds=45, nodes=10000, atoms=10000, terms=10000,
                          rewrites=50000, memory_mib=256)
    ring = colored.ColoredRing(limits)
    a, b, c = (ring.color(name) for name in ("a", "b", "c"))
    operations = (lambda f, g: f*g,
                  lambda f, g: f.D()*g.D(),
                  lambda f, g: (f*g).I())
    total = {mode: ring.number(0) for mode in producer.MODES}
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        P, Q, R = operations[i], operations[j], operations[k]
        template = Q(a, R(b, c))-R(a, Q(b, c))
        value = blocks.full_response(ring, colored.ThirdOperator(ring, template), P)
        blocks.add_modes(total, value)
    normalizer = colored.ColoredNormalizer(ring)
    if any(normalizer.word.expression(value).terms for value in total.values()):
        raise AssertionError("complete two-mode Jacobi identity on artificial symmetric operations")
    witness = poly.full_column_dual([[1, 0], [0, 1], [1, 1]], [2, 3, 7], 101)
    coefficients = witness["modular_functional_coefficients"]
    kappa = witness["modular_functional_target_value"]
    zero = extension_value([1, 2, 3], coefficients, kappa, 101)
    nonzero = extension_value([0, 0, 1], coefficients, kappa, 101)
    if zero != (0, 0) or nonzero != (1, 51):
        raise AssertionError("bound Cramer functional extension and true normalization")
    return {"scope": "artificial symmetric-operation Jacobi and a three-row modular extension only",
        "checks": {"complete_phase_Jacobi_both_modes": True,
                   "known_span_column_extension_zero": True,
                   "new_column_extension_nonzero_without_real_sign": True},
        "all_passed": True, "research_root_compiled": False,
        "research_profile_evaluated": False, "geometry_integrated": False}


def write_report(path, report, maximum):
    raw = (json.dumps(report, indent=2, sort_keys=True, allow_nan=False)+"\n").encode()
    if len(raw) > maximum:
        report = {"schema": SCHEMA, "completion": "output_limit", "full_bytes": len(raw),
            "full_sha256": hashlib.sha256(raw).hexdigest(), "source_hashes": report.get("source_hashes"),
            "no_new_mathematical_conclusion_published": True}
        raw = (json.dumps(report, indent=2, sort_keys=True)+"\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return {"completion": report["completion"], "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--input-certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-seconds", type=float, default=120)
    parser.add_argument("--memory-mib", type=int, default=768)
    parser.add_argument("--max-degree", type=int, default=256)
    parser.add_argument("--max-operations", type=int, default=10000000)
    parser.add_argument("--max-output-bytes", type=int, default=100000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.max_degree, args.max_operations) <= 0 or not 20000 <= args.max_output_bytes <= 300000:
        parser.error("positive computational limits and output bytes in [20000,300000] required")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
                                  and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("the actual four-column response is restricted to this public repository's Actions")
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started", "phase": "dependencies",
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"), "source_hashes": {},
        "scope": "explicit query-formula extension of R98 Lambda to four R83 fourth tangents",
        "new_columns_assumed_in_original_V": False, "completed_new_columns": [],
        "some_nonzero_exact_rational_extension_value_proved": False,
        "real_sign_or_global_negative_cost_proved": False, "baseline_cost_removed": False,
        "complete_P0_or_fixed_N_cancellation_paid": False,
        "fourth_ruling_paid": False, "finite_isometric_family_constructed": False,
        "embedding_or_reach_certified": False,
        "limits": {"seconds": args.max_seconds, "memory_polling_mib": args.memory_mib,
            "output_bytes": args.max_output_bytes, "new_columns": 4, "bound_evaluation_rows": 15,
            "coefficient_nodes": 300000, "profile_atoms": 100000,
            "expression_terms": 100000, "rewrite_calls_per_normalizer": 500000,
            "polynomial_degree": args.max_degree, "polynomial_operations": args.max_operations}}
    code = 0
    try:
        expected, report["source_hashes"] = dependencies()
        if args.toy_only:
            report["phase"] = "small_artificial_toys"
            report["toy"] = small_toys()
            report["completion"] = "toy_passed"
        else:
            certificate, prime, labels, coefficients, kappa = load_certificate(args.input_certificate, expected)
            report["bound_certificate"] = {"bytes": CERTIFICATE_BYTES, "sha256": CERTIFICATE_SHA,
                "github_run_id": "43638896281", "source_commit": CERTIFICATE_SOURCE,
                "problem_identity_sha256": certificate["problem_identity_sha256"],
                "all_15_selected_evaluation_labels": labels,
                "checked_prime": prime, "original_modular_functional_coefficients": coefficients,
                "kappa_mod_p": kappa,
                "extension_over_Q": "(ev_last(F)-row_last(A)*inverse(A_pivot)*ev_pivot(F))/kappa, applied to Pi_0(F)",
                "not_a_claim_that_new_F_belongs_to_old_V": True,
                "old_15_by_15_modular_matrix_rechecked_from_receipt_only": True}
            limits = exact.Limits(args.max_seconds, 300000, 100000, 100000,
                                  500000, args.memory_mib, 8192)
            report["phase"] = "restore_only_four_original_third_formulas"
            ring, templates = restore_four_original_templates(limits, report)
            remaining = args.max_seconds-(time.monotonic()-started)
            if remaining <= 0:
                raise poly.PolynomialBudgetExceeded("overall budget before four original evaluations")
            report["phase"] = "four_original_response_values"
            values, arithmetic = evaluate_four(args, ring, templates, labels, coefficients, kappa,
                                                prime, remaining, report)
            report["coefficient_arithmetic"] = arithmetic
            report["some_nonzero_exact_rational_extension_value_proved"] = any(
                value["nonzero_exact_rational_extension_value_proved"] for value in values)
            report["completion"] = "complete"
            report["interpretation"] = (
                "A nonzero new residue proves a nonzero rational value of the explicit query extension, not its real sign. R83 then supplies a nonzero signed fourth tangent around its actual nonzero baseline, keeping lower M/T and the N coefficient unchanged. Neither even parameter costs, the baseline, complete P0, nor fixed-N cancellation is paid. A zero residue in an unknown column is only inconclusive.")
    except (formal.CompilationBudgetExceeded, poly.PolynomialBudgetExceeded) as exc:
        report["completion"], report["error"], code = "resource_limit", str(exc), 2
        report["not_a_negative_mathematical_result"] = True
    except Exception as exc:
        report["completion"], report["error"], code = "implementation_check_failed", type(exc).__name__+": "+str(exc), 2
        report["some_nonzero_exact_rational_extension_value_proved"] = False
    report["elapsed_seconds"] = time.monotonic()-started
    report["max_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    result = write_report(args.output, report, args.max_output_bytes)
    if result["completion"] == "output_limit":
        code = 2
    print(json.dumps({**result, "output": str(args.output)}), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
