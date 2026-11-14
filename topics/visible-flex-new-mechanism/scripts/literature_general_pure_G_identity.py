#!/usr/bin/env python3
"""One arbitrary-profile pure identity suggested by the published m8 projection.

Restore the published original G and W; create only B_p2(W1) in mode -4.
Reduce G_-4-B_p2(W1)_-4/128 as one original same-anchor expression. A zero
is an exact positive identity. A nonzero word representative is unresolved,
never actual-function nonmembership. Genuine work is public-Actions-only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_static_G_rational_dual as original
import literature_linear_third_bridge_quotient as quotient

static = original.static
old = static.old
exact = static.exact
colored = static.colored
blocks = static.blocks
formal = static.formal
dual = static.dual
SCHEMA = "visible-flex-general-pure-G-fixed-identity-v1"
REPOSITORY = "Rogerhu12/math-research-public"
ORIGINAL_HELPER_SHA = "0872f0fc8b561a547342d530239e35c6ac9a37a5bddc5c472bf16c0df73ac477"
NORMALIZER_SHA = "0627875fe06950c9e7c360baaf0429451697a460e2cf10aa6b3434c501363bd2"
TARGET_SHA = "4608912701e99a514cff0dcb93b896200beeb6e3cbead9a70547b78e00d18c7a"
THIRD_INDEX = 1
QUADRATIC_INDEX = 2
R116_COLUMN = 10
COEFFICIENT = F(1, 128)
TOTAL_OUTPUT_BYTES = 4800000


def sha(data):
    return hashlib.sha256(data).hexdigest()


def data_bytes(value, pretty=False):
    return (json.dumps(value, sort_keys=True, allow_nan=False,
        indent=2 if pretty else None,
        separators=None if pretty else (",", ":"))+"\n").encode()


def sources():
    answer = original.sources()
    if answer["driver"]["sha256"] != ORIGINAL_HELPER_SHA:
        raise ValueError("explicitly rebind the original G input helper")
    answer["original_G_input_helper"] = answer.pop("driver")
    normalizer = static.identity(quotient.__file__)
    if normalizer["sha256"] != NORMALIZER_SHA:
        raise ValueError("the sound pure right-anchor normalizer changed")
    answer["pure_normalizer"] = normalizer
    answer["pure_normalizer_dependencies"] = quotient.dependency_info()
    answer["driver"] = static.identity(__file__)
    return answer


def pure_response(ring, diagonal, quadratic):
    """R71/R80 complete -4 coefficient, including the original phase factor."""
    q = ring.jet()
    return (ring.variation(diagonal, quadratic(q, q))
            - 2*quadratic(q, diagonal))/8


def require_degree(ring, expression, color, degree, *, allow_zero=False):
    actual = ring.color_degrees(expression)
    expected = {((color, degree),)}
    if actual != expected and not (allow_zero and not actual):
        raise ValueError("unexpected colors or degree in the original pure expression")


def word_rows(value):
    return [[list(local), [list(letter) for letter in word], c.numerator, c.denominator]
        for (local, word), c in sorted(value.terms.items())]


def store_gzip(path, data, maximum):
    raw = data_bytes(data)
    packed = gzip.compress(raw, mtime=0)
    if len(packed) > maximum:
        raise formal.CompilationBudgetExceeded("complete certificate byte budget")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(packed)
    return {"filename": path.name, "stored_bytes": len(packed),
        "stored_sha256": sha(packed), "raw_bytes": len(raw), "raw_sha256": sha(raw)}


def run_research(args, report):
    limits = exact.Limits(args.max_seconds, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.memory_mib, args.max_rational_bits)
    ring = colored.ColoredRing(limits)
    report["phase"] = "restore_bound_original_G_and_W"
    templates, targets, labels = original.load_G_and_bound(args, ring, report)
    target = targets[-4]
    if ring.digest(target) != TARGET_SHA:
        raise ValueError("the specified original G_-4 root changed")
    label = next((row for row in labels if
        (row["quadratic_index"], row["third_index"]) ==
        (QUADRATIC_INDEX, THIRD_INDEX)), None)
    if (label is None or exact.PARAMETERS[QUADRATIC_INDEX] != "p2"
        or 8*THIRD_INDEX+QUADRATIC_INDEX != R116_COLUMN
        or label["v2_original_third_index"] != 1
        or blocks.THIRD_WEIGHTS[THIRD_INDEX] != 0
        or blocks.PARAMETER_WEIGHTS[QUADRATIC_INDEX] != 1):
        raise ValueError("the fixed R123 column10 = B_p2(W1) identity changed")
    template = templates[THIRD_INDEX]
    if ring.digest(template) != label["third_original_sha256"]:
        raise ValueError("the exact retained W1 original root changed")
    q = ring.jet()
    diagonal = ring.substitute(template, {"a": q, "b": q, "c": q})
    require_degree(ring, diagonal, "q", 3)
    require_degree(ring, target, "q", 4)
    report["phase"] = "one_new_complete_pure_response"
    quadratic = exact.operator_basis(ring)[QUADRATIC_INDEX]
    response = pure_response(ring, diagonal, quadratic)
    require_degree(ring, response, "q", 4, allow_zero=True)
    difference = target-COEFFICIENT*response
    grade = blocks.ScalingGrading(ring)
    for expression in (target, response, difference):
        if set(grade.split(expression))-{1}:
            raise ValueError("the full fixed comparison left its true weight-one block")
    report["fixed_comparison"] = {
        "formula": "G[-4] - B_p2(W1)[-4]/128",
        "mode": -4, "profile_affine_weight": 1,
        "quadratic_index": QUADRATIC_INDEX, "quadratic_name": "p2",
        "third_index": THIRD_INDEX, "v2_original_third_index": 1,
        "R116_column_index": R116_COLUMN, "response_coefficient": str(COEFFICIENT),
        "third_original_sha256": ring.digest(template),
        "diagonal_original_sha256": ring.digest(diagonal),
        "target_original_sha256": ring.digest(target),
        "response_original_sha256": ring.digest(response),
        "difference_original_sha256": ring.digest(difference),
        "target_original_terms": len(target.terms),
        "response_original_terms": len(response.terms),
        "difference_original_terms": len(difference.terms),
        "pure_factor_formula": "(D tau_diag[A(q,q)] - 2 A(q,tau_diag))/8",
        "additional_one_sixteenth_applied": False,
        "new_pure_response_formulas": 1, "new_mixed_response_formulas": 0,
        "new_profile_evaluations": 0, "new_tail_substitutions": 0,
        "old_W_or_local_density_compiles": 0,
        "primitive_values_assigned_independently": False,
        "diagonal_only_used_for_pure_mode": True}
    named = {"original_W1": template, "W1_diagonal": diagonal,
        "original_G_minus4": target, "original_response_minus4": response,
        "original_fixed_difference": difference}
    certificate = {"schema": SCHEMA+"-original-expressions",
        "content_scope": "one complete arbitrary-profile pure original difference",
        "source_hashes": report["source_hashes"],
        "input": report["input"], "fixed_comparison": report["fixed_comparison"],
        **old.serialize_expressions(ring, named)}
    path = args.output.with_name(args.output.stem+"-certificate.json.gz")
    # Preserve the one newly built raw difference even if sound word reduction
    # subsequently reaches its explicitly bounded resource limit.
    report["portable_original_certificate"] = store_gzip(
        path, certificate, args.max_certificate_bytes)
    report["phase"] = "one_sound_original_difference_reduction"
    normalizer = quotient.ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    reduced = normalizer.expression(difference)
    positive = not reduced.terms
    report["result"] = {
        "status": "original_identity_proved" if positive else "unresolved_nonzero_representative",
        "arbitrary_profile_pure_identity_proved": positive,
        "normal_form": normalizer.word.summary(reduced),
        "original_difference_reduced_directly": True,
        "normalizer_sound_but_not_complete": True,
        "function_nonmembership_proved": False,
        "general_pure_U4_equals_response_range_proved": False,
        "complete_two_mode_identity_proved": False,
        "left_endpoint_or_period_reset": False}
    report["normalizer_statistics"] = {
        "right_IBP": normalizer.legacy.stats, "word": normalizer.word.stats}
    certificate["result"] = report["result"]
    certificate["normalizer_statistics"] = report["normalizer_statistics"]
    certificate["entire_reduced_word_expression"] = word_rows(reduced)
    certificate["negative_representative_is_not_nonmembership"] = True
    report["portable_original_certificate"] = store_gzip(
        path, certificate, args.max_certificate_bytes)
    report["coefficient_arithmetic"] = {
        "field": "Q", "profile_atoms": len(ring.p.atoms),
        "coefficient_nodes": len(ring.algebra.c.nodes),
        "limits_check_calls": limits.calls}
    report["phase"] = "complete_fixed_original_comparison"
    report["completion"] = "complete"


def artificial_toys():
    """Only small hand-built algebra; no published research root is loaded."""
    limits = exact.Limits(seconds=30, nodes=10000, atoms=2000,
        terms=5000, rewrites=15000, memory_mib=512)
    ring = colored.ColoredRing(limits)
    norm = quotient.ProfileNormalizer(ring, 15000, 5000)
    q = ring.jet()
    checks = {}
    pointwise = lambda f, g: f*g
    simple = pure_response(ring, q**3, pointwise)
    if norm.expression(simple-q**4/8).terms:
        raise AssertionError("the complete pure phase coefficient must be 1/8")
    checks["complete_pure_factor_one_eighth"] = True
    # The inner slots are symmetric, while the first slot is genuinely distinct.
    def T(a, b, c):
        return a*(b.D()*c+b*c.D())+2*a.D()*b*c+a.I()*b*c+a*(b*c).I()
    A = lambda f, g: f*g+(f.D()*g.D()).I()/3
    diagonal = T(q, q, q)
    aq = A(q, q)
    literal_K = 2*T(aq, q, q)
    literal_L = -4*T(q, q, aq)+4*A(q, diagonal)
    response = pure_response(ring, diagonal, A)
    if norm.expression(response-(literal_K-literal_L)/16).terms:
        raise AssertionError("asymmetric exterior slot and exact original K/L phase")
    checks["asymmetric_outer_inner_slots_and_K_minus_L_over_16"] = True
    if norm.expression((q*q.D()).I()-q*q/2).terms:
        raise AssertionError("right collar boundary or signed primitive")
    checks["signed_right_primitive_and_zero_right_collar"] = True
    fake_target = response/128
    if norm.expression(fake_target-COEFFICIENT*response).terms:
        raise AssertionError("fixed rational identity coefficient")
    if not norm.expression(simple/128-simple/64).terms:
        raise AssertionError("a nonzero representative was discarded")
    checks["one_over_128_and_unmatched_terms_retained"] = True
    a, b, c = (ring.color(name) for name in ("a", "b", "c"))
    template = T(a, b, c)
    specialized = ring.substitute(template, {"a": q, "b": q, "c": q})
    if norm.expression(specialized-diagonal).terms:
        raise AssertionError("simultaneous colored diagonal with fixed primitives")
    require_degree(ring, specialized, "q", 3)
    rejected = False
    try:
        require_degree(ring, q**3*ring.color("qbar"), "q", 4)
    except ValueError:
        rejected = True
    if not rejected:
        raise AssertionError("mixed colors must not enter the pure target")
    checks["colored_diagonal_and_pure_color_scope"] = True
    exported = old.serialize_expressions(ring, {"artificial": fake_target})
    restored_ring = colored.ColoredRing(limits)
    decoded = old.decode_expressions(restored_ring, exported)
    if restored_ring.digest(decoded["artificial"]) != ring.digest(fake_target):
        raise AssertionError("portable original-expression roundtrip")
    checks["complete_original_DAG_roundtrip"] = True
    return {"checks": checks, "all_passed": all(checks.values()),
        "published_research_DAG_loaded": False,
        "research_target_or_profile_evaluated": False,
        "old_forcing_or_response_compiled": False}


def write_main(args, report):
    raw = data_bytes(report, pretty=True)
    if len(raw) > args.max_main_bytes:
        path = args.output.with_name(args.output.stem+"-complete-report.json.gz")
        report_file = store_gzip(path, report, args.max_full_report_bytes)
        main = {key: report.get(key) for key in (
            "schema", "completion", "phase", "scope", "github_repository", "github_run_id",
            "github_sha", "source_hashes", "limits", "fixed_comparison", "result", "toy",
            "portable_original_certificate", "elapsed_seconds", "peak_rss_mib", "error")}
        main["complete_report_file"] = report_file
        raw = data_bytes(main, pretty=True)
        if len(raw) > args.max_main_bytes:
            # The full report remains preserved; this status is a storage bound,
            # not a mathematical failure or a new result.
            main = {"schema": SCHEMA, "completion": "output_limit",
                "github_repository": report.get("github_repository"),
                "github_run_id": report.get("github_run_id"), "github_sha": report.get("github_sha"),
                "source_hashes": report.get("source_hashes"),
                "computation_completion": report.get("completion"),
                "complete_report_file": report_file,
                "portable_original_certificate": report.get("portable_original_certificate"),
                "error": "complete result retained in gzip; selected main exceeded its byte limit"}
            raw = data_bytes(main, pretty=True)
        if len(raw) > args.max_main_bytes:
            raise ValueError("the source-bound compact main exceeds its reserved limit")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    return {"filename": args.output.name, "bytes": len(raw), "sha256": sha(raw),
        "completion": json.loads(raw)["completion"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-report", type=Path, default=static.DEFAULT_DIR/"local-fourth-quotient.json")
    parser.add_argument("--source-report-sha256", default=static.REPORT_SHA)
    parser.add_argument("--source-run", default=static.SOURCE_RUN)
    parser.add_argument("--source-commit", default=static.SOURCE_COMMIT)
    parser.add_argument("--publication-receipt", type=Path, default=static.DEFAULT_DIR/"receipt.json")
    parser.add_argument("--publication-receipt-sha256", default=static.PUBLICATION_SHA)
    parser.add_argument("--input-export", type=Path, default=static.DEFAULT_DIR/"local-fourth-quotient-original-expressions.json.gz")
    parser.add_argument("--export-sha256", default=static.EXPORT_SHA)
    parser.add_argument("--third-receipt", type=Path, default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--block-receipt", type=Path, default=static.DEFAULT_DIR/"local-fourth-quotient-weight-+1.json")
    parser.add_argument("--max-seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-nodes", type=int, default=400000)
    parser.add_argument("--max-atoms", type=int, default=100000)
    parser.add_argument("--max-terms", type=int, default=100000)
    parser.add_argument("--max-IBP-calls", type=int, default=250000)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    parser.add_argument("--max-main-bytes", type=int, default=90000)
    parser.add_argument("--max-certificate-bytes", type=int, default=2500000)
    parser.add_argument("--max-full-report-bytes", type=int, default=2000000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.max_rational_bits,
        args.max_certificate_bytes, args.max_full_report_bytes) <= 0:
        parser.error("positive finite resource bounds required")
    if not 10000 <= args.max_main_bytes < 100000:
        parser.error("reserve 10000..99999 bytes for the complete or compact main")
    if args.max_main_bytes+args.max_certificate_bytes+args.max_full_report_bytes > TOTAL_OUTPUT_BYTES:
        parser.error("total potential published output exceeds the declared byte bound")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("genuine original-symbolic research only in this public Actions repository")
    start = time.monotonic()
    code = 0
    report = {"schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "scope": "one arbitrary-profile pure identity; neither full mixed membership nor all pure costs",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": {}, "limits": {"seconds": args.max_seconds,
            "memory_polling_mib": args.memory_mib, "nodes": args.max_nodes,
            "atoms": args.max_atoms, "terms": args.max_terms, "IBP_calls": args.max_IBP_calls,
            "rational_bits": args.max_rational_bits, "main_bytes": args.max_main_bytes,
            "certificate_bytes": args.max_certificate_bytes,
            "full_report_bytes": args.max_full_report_bytes},
        "function_nonmembership_proved": False, "finite_isometric_family_constructed": False}
    try:
        report["source_hashes"] = sources()
        if args.toy_only:
            report["phase"] = "small_artificial_interfaces"
            report["toy"] = artificial_toys()
            report["completion"] = "toy_passed"
        else:
            run_research(args, report)
    except formal.CompilationBudgetExceeded as error:
        report["completion"] = "resource_limit"
        report["error"] = str(error)
        code = 2
    except Exception as error:
        report["completion"] = "implementation_check_failed"
        report["error"] = {"type": type(error).__name__, "message": str(error)}
        code = 1
    report["elapsed_seconds"] = time.monotonic()-start
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written = write_main(args, report)
    if written["completion"] == "output_limit":
        code = 2
    print(json.dumps({"output": str(args.output), **written}), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
