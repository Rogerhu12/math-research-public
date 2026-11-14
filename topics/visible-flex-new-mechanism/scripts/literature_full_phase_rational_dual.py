#!/usr/bin/env python3
"""Exact rational-evaluation certificate for the complete P1 bridge problem.

One fixed real polynomial pair is used at every point and in both modes.
Original right-Volterra expressions are evaluated modulo a checked prime;
only a nonzero full 37 by 37 rational minor is a negative certificate.
Research compilation and profile evaluation run only in public Actions.
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
import literature_pure_bulk_exact_membership as exact
import literature_range_profile_algebra as formal
import literature_rational_volterra_polynomial as poly


SCHEMA = "visible-flex-complete-P1-original-rational-dual-v1"
RECEIPT_SHA = "7c2cb9fece518fb6fbb15b6b4e034565dfcc5a10cf0e103a7011cd56dc4ac960"
RECEIPT_BYTES = 157380
PRODUCER_SHA = "d7513321bea70248851e9b71b02c97b7e869531097f290de40257c94507fed0e"
RECEIPT_SOURCE = "26c3f2c0308d179a094d3967cfb7189db426081e"
TOPIC = Path(__file__).resolve().parents[1]
DEFAULT_RECEIPT = TOPIC/"notes/actions-43633746055-1-full_phase_bridge_exact/full-phase-bridge-exact.json"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def file_identity(path):
    data = Path(path).read_bytes()
    return {"filename": Path(path).name, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def dependencies():
    identities = producer.dependencies()
    if identities["driver"]["sha256"] != PRODUCER_SHA:
        raise ValueError("explicitly rebind the frozen v2 producer")
    identities["v2_producer"] = identities.pop("driver")
    identities["polynomial_evaluator"] = file_identity(poly.__file__)
    identities["driver"] = file_identity(__file__)
    return identities


def read_receipt(path):
    raw = path.read_bytes()
    if len(raw) != RECEIPT_BYTES or hashlib.sha256(raw).hexdigest() != RECEIPT_SHA:
        raise ValueError("the original v2 public Actions receipt was not preserved byte for byte")
    data = json.loads(raw)
    if (data["github_run_id"] != "43633746055"
            or data["github_sha"] != RECEIPT_SOURCE
            or data["completion"] != "complete"
            or data["source_hashes"]["driver"]["sha256"] != PRODUCER_SHA):
        raise ValueError("v2 receipt identity/completion mismatch")
    reduction = data["pre_response_reduction"]
    if (reduction["input_template_count"] != 152
            or reduction["template_representative_rank"] != 36
            or len(reduction["verified_original_dependencies"]) != 116):
        raise ValueError("the published full-third spanning certificate changed")
    for component in data["endpoint_components"]:
        key = (component["field_component"]["log_a_power"], component["field_component"]["a_power"])
        if key != (0, 0) and not component["verified_from_original_compiled_expressions"]:
            raise ValueError("the nonrational baseline component was not paid in the published certificate")
    return data


def reachable_jet_bound(ring, expressions):
    seen, maximum, kinds = set(), 0, set()

    def visit(monomial):
        nonlocal maximum
        for atom in monomial[1]:
            if atom in seen:
                continue
            seen.add(atom)
            node = ring.p.atoms[atom]
            if node[0] == "jet":
                maximum = max(maximum, node[2])
                kinds.add(node[1])
            elif node[0] == "int_right":
                visit(node[1])
            else:
                raise ValueError("unsupported original atom")

    for expression in expressions:
        for monomial in expression.terms:
            visit(monomial)
    return {"maximum_input_jet": maximum, "colors": sorted(kinds), "reachable_atoms": len(seen)}


def compile_original_problem(limits, receipt):
    """Use v2's original formulas; no joint word-span computation is repeated."""
    ring = colored.ColoredRing(limits)
    normalizer = colored.ColoredNormalizer(ring)
    targets, _ = producer.compile_constant_targets(ring)
    for mode in producer.MODES:
        if ring.digest(targets[mode]) != receipt["constant_target"]["modes"][str(mode)]["original_sha256"]:
            raise AssertionError("constant target original hash mismatch")
    density, _, _ = producer.compile_colored_local(ring)
    pieces = producer.raw_decomposition(density, normalizer)
    signature, _ = producer.c1_endpoint_signature(ring, pieces)
    all_templates, labels, _ = producer.control_templates(ring, pieces, normalizer)
    expected = receipt["all_original_control_templates"]
    if len(all_templates) != len(expected):
        raise AssertionError("original third template count mismatch")
    for label, recorded in zip(labels, expected):
        if label["original_template_sha256"] != recorded["original_template_sha256"]:
            raise AssertionError("original third template hash mismatch")
    kept = receipt["pre_response_reduction"]["retained_original_indices"]
    templates = [all_templates[index] for index in kept]
    retained_labels = [receipt["control_templates"][i] for i in range(len(kept))]
    for key, expression in signature.items():
        recorded = next(item for item in receipt["baseline_pre_reduction"]
                        if (item["field_component"]["log_a_power"], item["field_component"]["a_power"]) == key)
        if ring.digest(expression) != recorded["original_third_sha256"]:
            raise AssertionError("complete five-leg baseline original hash mismatch")
    baseline_record = next(item for item in receipt["baseline_pre_reduction"]
                           if item["field_component"] == {"log_a_power": 0, "a_power": 0})
    # Work with the ORIGINAL expression minus the published reachable part.
    # This is not the 42-term word representative and uses no new IBP rule.
    baseline = signature[(0, 0)]-sum((F(value)*templates[index]
        for index, value in baseline_record["absorbed_retained_template_coefficients"]), ring.number(0))
    regularity = reachable_jet_bound(ring, [baseline]+templates)
    target_regularity = reachable_jet_bound(ring, [targets[mode] for mode in producer.MODES])
    if regularity["maximum_input_jet"] > 4 or target_regularity["maximum_input_jet"] > 4:
        raise ValueError("update the finite-regularity/continuity proof before raising the jet scope")
    summary = {"original_target_sha256": {str(mode): ring.digest(targets[mode]) for mode in producer.MODES},
        "all_152_original_template_hashes_matched": True,
        "retained_original_indices": kept,
        "retained_original_template_sha256": [ring.digest(value) for value in templates],
        "full_third_spanning_source": "v2 exact 116 original-expression dependencies; not reevaluated as a new research target",
        "nonrational_baseline_components": "already canceled in both modes by the bound v2 original-expression certificates",
        "rational_baseline_original_sha256": ring.digest(signature[(0, 0)]),
        "rational_baseline_original_minus_reachable_sha256": ring.digest(baseline),
        "baseline_absorbed_coefficients": baseline_record["absorbed_retained_template_coefficients"],
        "third_input_regularity": regularity, "constant_target_regularity": target_regularity,
        "original_control_labels": retained_labels,
        "coefficient_nodes": len(ring.algebra.c.nodes), "profile_atoms": len(ring.p.atoms)}
    return ring, {mode: targets[mode] for mode in producer.MODES}, templates, baseline, summary


def fixed_profiles(context, power):
    """The same real rational pair at every point, in every control column."""
    t = context.variable()
    bump = (t*(1-t))**power
    f = bump
    g = bump*(1+2*t+3*t*t+5*t*t*t)
    q = f+context.number((0, 1))*g
    context.colors = {"q": q, "qbar": q.conjugate()}
    return f, g, {"coordinate": "t=(xi-2)/(3-2)", "support": ["2", "3"],
        "f": "[t*(1-t)]^m", "g": "[t*(1-t)]^m*(1+2*t+3*t^2+5*t^3)",
        "m": power, "zero_outside_support": True,
        "zero_extension_regularity": "C^"+str(power-1),
        "common_outer_collars": "choose a larger compact I inside (1,infinity), with support [2,3] in its interior",
        "actual_right_anchor": "the common right collar; on [2,3] it equals the integral from xi=3",
        "three_moment_circle_conditions_imposed": False,
        "a_specific_smooth_circle_claimed": False,
        "f_modular_coefficients_sha256": f.digest(), "g_modular_coefficients_sha256": g.digest()}


def evaluate_problem(context, ring, targets, templates, baseline, point_count, report):
    evaluated = poly.RawExpressionEvaluator(ring.p, context, context.colors)
    constant = {mode: evaluated.expression(expression) for mode, expression in targets.items()}
    baseline_third = poly.EvaluatedThirdOperator(ring.p, context, baseline)
    baseline_response = colored.full_phase_response(context, baseline_third)
    target = {mode: constant[mode]+baseline_response[mode] for mode in producer.MODES}
    points = [F(j, point_count+1) for j in range(1, point_count+1)]
    row_labels = [{"t": str(t), "xi": str(context.left+context.width*t),
                   "mode": mode, "component": component}
                  for t in points for mode in producer.MODES for component in ("real", "imaginary")]

    def rows_of(modes):
        return [value for t in points for mode in producer.MODES for value in modes[mode].value(t)]

    target_values = rows_of(target)
    columns, hashes = [], []
    for index, template in enumerate(templates):
        started = time.monotonic()
        response = colored.full_phase_response(context, poly.EvaluatedThirdOperator(ring.p, context, template))
        columns.append(rows_of(response))
        hashes.append({"index": index, "modes": {str(mode): {"sha256": response[mode].digest(),
            "degree": len(response[mode].coefficients)-1} for mode in producer.MODES},
            "seconds": time.monotonic()-started})
        report["evaluation_checkpoint"] = {"completed_control_columns": index+1,
                                            "total_control_columns": len(templates)}
        if index % 6 == 0:
            print(json.dumps({"phase": "original_polynomial_control_values", "column": index,
                              "degree": context.max_degree_seen}), flush=True)
        context.check(0)
    rows = [[column[i] for column in columns] for i in range(len(row_labels))]
    witness = poly.full_column_dual(rows, target_values, context.prime)
    if witness["rational_nonmembership_certified"]:
        witness["selected_evaluation_labels"] = [row_labels[i] for i in witness["selected_augmented_rows"]]
    return {"all_evaluation_labels": row_labels,
        "same_profile_pair_across_all_modes_points_and_columns": True,
        "matrix_rows": len(rows), "matrix_columns": len(columns),
        "all_matrix_modular_values_sha256": hashlib.sha256(canonical(rows)).hexdigest(),
        "all_target_modular_values_sha256": hashlib.sha256(canonical(target_values)).hexdigest(),
        "target_mode_polynomials": {str(mode): {"sha256": target[mode].digest(),
                "degree": len(target[mode].coefficients)-1} for mode in producer.MODES},
        "control_mode_polynomial_identities": hashes,
        "dual_certificate": witness}


def small_toys():
    result = poly.small_toys()
    limits = exact.Limits(seconds=30, nodes=5000, atoms=1000, terms=1000,
                          rewrites=5000, memory_mib=256)
    ring = colored.ColoredRing(limits)
    a, b = ring.color("a"), ring.color("b")
    context = poly.PolynomialContext(101, 2, 5, seconds=30, max_degree=30)
    x = context.x()
    evaluator = poly.RawExpressionEvaluator(ring.p, context, {"a": x*x, "b": 2*x+1})
    original = (a.D()*b+a*b.D()).I()+a*b.I()
    actual = evaluator.expression(original)
    expected = ((x*x)*(2*x+1)).D().I()+(x*x)*(2*x+1).I()
    if actual.key() != expected.key():
        raise AssertionError("original nested primitive/jet evaluation")
    result["checks"]["original_DAG_without_IBP_rewrite"] = True
    result["checks"]["nonzero_right_boundary_not_silently_removed"] = (
        evaluator.expression((a*b).D().I()).value(1) == (0, 0)
        and evaluator.expression(a*b).value(1) != (0, 0))
    if not all(result["checks"].values()):
        raise AssertionError("raw evaluator artificial boundary toy")
    result["all_passed"] = True
    return result


def write_report(path, payload, max_bytes):
    raw = (json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n").encode()
    if len(raw) > max_bytes:
        payload = {"schema": SCHEMA, "completion": "output_limit", "full_bytes": len(raw),
            "full_json_sha256": hashlib.sha256(raw).hexdigest(),
            "source_hashes": payload.get("source_hashes"),
            "rational_nonmembership_certified": False,
            "mathematical_result": "the required independently checkable witness was not published"}
        raw = (json.dumps(payload, indent=2, sort_keys=True)+"\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return len(raw), hashlib.sha256(raw).hexdigest(), payload["completion"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--input-receipt", type=Path, default=DEFAULT_RECEIPT)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--prime", type=int, default=2147483647)
    parser.add_argument("--points", type=int, default=48)
    parser.add_argument("--bump-power", type=int, default=8)
    parser.add_argument("--max-seconds", type=float, default=300)
    parser.add_argument("--max-degree", type=int, default=256)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-operations", type=int, default=20000000)
    parser.add_argument("--max-output-bytes", type=int, default=300000)
    args = parser.parse_args()
    if min(args.points, args.max_seconds, args.max_degree, args.memory_mib,
           args.max_operations, args.max_output_bytes) <= 0 or args.bump_power < 8:
        parser.error("positive budgets and bump-power >=8 are required")
    if args.points+1 >= args.prime:
        parser.error("evaluation denominators must be smaller than the prime")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
                                  and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("actual target/profile evaluation is allowed only in this public repository's Actions")
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started", "phase": "dependencies",
        "source_hashes": {}, "github_sha": os.environ.get("GITHUB_SHA"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "limits": {"seconds": args.max_seconds, "polynomial_degree": args.max_degree,
            "memory_polling_mib": args.memory_mib, "operations": args.max_operations,
            "output_bytes": args.max_output_bytes},
        "rational_nonmembership_certified": False,
        "primary_scope": "one original rational polynomial pair disproves a universal whole-function identity only if a full separating minor is certified",
        "three_moment_circle_paid": False, "specific_C_infinity_circle_certified": False,
        "all_profiles_excluded": False, "all_geometries_excluded": False,
        "P0_paid": False, "fourth_ruling_paid": False,
        "finite_isometric_family_constructed": False, "embedding_or_reach_certified": False,
        "word_normalization_used_to_evaluate_values": False}
    context = None
    code = 0
    try:
        report["source_hashes"] = dependencies()
        if args.toy_only:
            report["phase"] = "small_artificial_toys"
            report["toy"] = small_toys()
            report["completion"] = "toy_passed"
        else:
            receipt = read_receipt(args.input_receipt)
            report["input_receipt"] = {"bytes": RECEIPT_BYTES, "sha256": RECEIPT_SHA,
                "github_run_id": receipt["github_run_id"], "source_commit": RECEIPT_SOURCE,
                "producer_sha256": PRODUCER_SHA}
            limits = exact.Limits(args.max_seconds, 600000, 160000, 120000,
                                  750000, args.memory_mib, 8192)
            report["phase"] = "original_formulas_and_published_control_basis"
            ring, targets, templates, baseline, summary = compile_original_problem(limits, receipt)
            report["original_problem"] = summary
            print(json.dumps({"completed": report["phase"], "retained_controls": len(templates),
                              "baseline_raw_terms": len(baseline.terms)}), flush=True)
            remaining = args.max_seconds-(time.monotonic()-started)
            if remaining <= 0:
                raise poly.PolynomialBudgetExceeded("total budget exhausted before polynomial evaluation")
            context = poly.PolynomialContext(args.prime, 2, 3, seconds=remaining,
                max_degree=args.max_degree, memory_mib=args.memory_mib,
                max_operations=args.max_operations)
            _, _, report["fixed_profiles"] = fixed_profiles(context, args.bump_power)
            report["phase"] = "original_rational_profile_values_and_joint_minor"
            report["evaluation"] = evaluate_problem(context, ring, targets, templates, baseline,
                                                     args.points, report)
            report["rational_nonmembership_certified"] = report["evaluation"]["dual_certificate"]["rational_nonmembership_certified"]
            report["completion"] = "complete"
            report["interpretation"] = (
                "A certified nonzero augmented minor is a characteristic-zero rational certificate: its cofactor-defined functional annihilates all 36 original retained columns and hence the full proved third-control space. It excludes a universal identity and this finite-regularity test pair; no three-moment circle or global surface is asserted. Without that minor the result is inconclusive.")
    except (formal.CompilationBudgetExceeded, poly.PolynomialBudgetExceeded) as exc:
        report["completion"], report["error"], code = "resource_limit", str(exc), 2
        report["not_a_negative_mathematical_result"] = True
    except Exception as exc:
        report["completion"], report["error"], code = "implementation_check_failed", type(exc).__name__+": "+str(exc), 2
        report["rational_nonmembership_certified"] = False
    report["elapsed_seconds"] = time.monotonic()-started
    report["max_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    if context is not None:
        report["coefficient_arithmetic"] = context.coefficient_report()
    size, digest, completion = write_report(args.output, report, args.max_output_bytes)
    if completion == "output_limit":
        code = 2
    print(json.dumps({"completion": completion, "bytes": size, "sha256": digest,
                      "output": str(args.output)}), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
