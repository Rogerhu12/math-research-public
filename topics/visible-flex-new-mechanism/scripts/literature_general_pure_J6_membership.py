#!/usr/bin/env python3
"""One original J6 pure target against the nine archived R151 true bases.

J6 is the complete coefficient [h^-2] Abar_kk from R136, not a partial
acceleration forcing. Only its pure root is decoded. The complete mixed
root is source-bound metadata, never normalized or evaluated. No old
forty-column normalization, thirty-one dependence check, new response,
profile evaluation, or forcing compilation is performed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_general_pure_D0_membership as solver

archived, axis, layer = solver.archived, solver.axis, solver.layer
prior = archived.prior
pure, static, old = solver.pure, solver.static, solver.old
exact, colored, blocks = solver.exact, solver.colored, solver.blocks
formal, quotient = solver.formal, solver.quotient

SCHEMA = "visible-flex-general-pure-J6-archived-basis-membership-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = solver.TOPIC
WEIGHT, PURE_MODE = -2, -4
SOLVER_DRIVER = {
    "filename": "literature_general_pure_D0_membership.py",
    "bytes": 25604,
    "sha256": "c296f72becff4366297e3b9f00db97425b1aa5b15c10ba7625932966ae7c8f1f",
}
FAMILY = prior.FAMILY
STATE_KEY = (-2, 0, 0, 0)
FAMILY_NAME = "A_kk"
TARGET_ID = 6
TARGET_NAMES = {"-4": "family_0191_-4", "-2": "family_0191_-2"}
SELECTED_NAMES = {"-4": "selected_0006_-4", "-2": "selected_0006_-2"}
TARGET_HASHES = {
    "-4": "9f28420162242f5899bcbf4bb2398b793935ebad021b8f57bbd1fe129f4a0ab1",
    "-2": "19e1c92b975c9e59df6e2e09432a5cb9c824412fface2b85b47161a7aa10e18f",
}


def source_identity():
    completed = solver.source_identity()
    if completed["driver"] != SOLVER_DRIVER:
        raise ValueError("the completed archived-basis solver changed")
    basis = completed["completed_pure_basis_producer"]
    family = basis["bound_original_inputs"]["five_family_producer"]
    if family["driver"] != FAMILY["driver"]:
        raise ValueError("the complete five-family producer changed")
    return {
        "driver": static.identity(__file__),
        "completed_archived_basis_solver": completed,
        "completed_pure_basis_producer": basis,
        "complete_five_family_producer": family,
    }


def select_record(records, family, state, hashes):
    matches = [
        row for row in records
        if row.get("family") == family
        and tuple(row.get("state_key", [])) == tuple(state)
    ]
    if len(matches) != 1:
        raise ValueError("exactly one complete requested state coefficient is required")
    row = matches[0]
    if row.get("original_mode_sha256") != hashes:
        raise ValueError("the selected complete state coefficient hashes changed")
    return row


def actual_environment_allowed(environment):
    return (
        environment.get("GITHUB_ACTIONS") == "true"
        and environment.get("GITHUB_REPOSITORY") == REPOSITORY
    )


def load_J6(args, ring, report):
    directory = args.family_directory
    main = layer.read_bound_json(directory / FAMILY["main"]["filename"], FAMILY["main"])
    publication = layer.read_bound_json(
        directory / FAMILY["receipt"]["filename"], FAMILY["receipt"]
    )
    expected = report["source_hashes"]["complete_five_family_producer"]
    if (
        main.get("schema") != FAMILY["schema"]
        or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != FAMILY["run"]
        or main.get("github_sha") != FAMILY["commit"]
        or main.get("source_hashes") != expected
    ):
        raise ValueError("the completed R136 original source manifest changed")
    metadata = (main.get("checkpoint") or {}).get(FAMILY["metadata_key"])
    if (
        not metadata
        or not metadata.get("persisted")
        or metadata.get("content_scope") != FAMILY["scope"]
        or metadata.get("root_count") != FAMILY["roots"]
        or any(metadata.get(k) != v for k, v in FAMILY["export"].items())
    ):
        raise ValueError("the complete published acceleration export is required")
    publication_binding = layer.check_publication(
        publication, run=FAMILY["run"], commit=FAMILY["commit"],
        lane=FAMILY["lane"], driver=FAMILY["driver"],
        main_name=FAMILY["main"]["filename"], main_info=FAMILY["main"],
        export_info=metadata,
    )
    data = layer.read_bound_export(directory / FAMILY["export"]["filename"], metadata)
    if (
        data.get("schema") != FAMILY["schema"] + "-original-expressions"
        or data.get("content_scope") != FAMILY["scope"]
        or data.get("github_repository") != REPOSITORY
        or str(data.get("github_run_id")) != FAMILY["run"]
        or data.get("github_sha") != FAMILY["commit"]
        or data.get("source_hashes") != expected
        or data.get("state_coordinate_order") != ["h", "k", "omega", "logh"]
        or data.get("selected_weight") != WEIGHT
        or len(data.get("family_records", [])) != 314
        or len(data.get("selected_weight_records", [])) != 10
        or len(data.get("roots", {})) != FAMILY["roots"]
    ):
        raise ValueError("the complete original family scope changed")
    row = select_record(
        data["family_records"], FAMILY_NAME, STATE_KEY, TARGET_HASHES
    )
    selected = [
        entry for entry in data["selected_weight_records"]
        if entry.get("id") == TARGET_ID
    ]
    if (
        row.get("roots") != TARGET_NAMES
        or row.get("profile_weights") != [WEIGHT]
        or row.get("requested_weight_original_mode_sha256") != TARGET_HASHES
        or len(selected) != 1
        or selected[0].get("roots") != SELECTED_NAMES
        or selected[0].get("original_mode_sha256") != TARGET_HASHES
        or selected[0].get("aliases") != [
            {"family": FAMILY_NAME, "state_key": list(STATE_KEY)}
        ]
    ):
        raise ValueError("the source-bound J6 family and selected coefficient disagree")
    # Validate the two source-bound aliases using stored original SHA metadata.
    # No mixed expression is decoded, normalized, or evaluated here.
    declared = data.get("original_root_sha256") or {}
    for mode in ("-4", "-2"):
        for name in (TARGET_NAMES[mode], SELECTED_NAMES[mode]):
            if name not in data["roots"] or declared.get(name) != TARGET_HASHES[mode]:
                raise ValueError("a selected source original-root identity changed")
    name = TARGET_NAMES[str(PURE_MODE)]
    roots = axis.subset_decode(ring, data, [name])
    if set(roots) != {name}:
        raise ValueError("the one-target original decoder returned extra roots")
    target = roots[name]
    if ring.digest(target) != TARGET_HASHES[str(PURE_MODE)]:
        raise ValueError("the complete pure J6 original root changed")
    pure.require_degree(ring, target, "q", 4)
    if set(blocks.ScalingGrading(ring).split(target)) != {WEIGHT}:
        raise ValueError("J6 has changed true profile weight")
    report["J6_input"] = {
        "publication": publication_binding, "main": FAMILY["main"],
        "receipt": FAMILY["receipt"], "complete_export": metadata,
        "family": FAMILY_NAME, "state_key": list(STATE_KEY),
        "candidate_id": TARGET_ID, "family_record": row,
        "selected_record": selected[0],
        "original_pure_root": name,
        "decoded_research_target_roots": 1,
        "mixed_original_hash_only_source_bound": TARGET_HASHES["-2"],
        "mixed_root_decoded": False,
        "other_family_roots_decoded": 0,
        "producer_W_N2_v4_forcing_recompiled": False,
    }
    return target


def save_certificate(args, report, ring, named, certificate):
    payload = {
        "schema": SCHEMA + "-original-expressions",
        "content_scope": "one-original-J6-pure-solve-against-nine-archived-originals",
        "github_repository": report["github_repository"],
        "github_run_id": report["github_run_id"],
        "github_sha": report["github_sha"],
        "source_hashes": report["source_hashes"],
        "phase": report["phase"],
        "input_J6": report.get("J6_input"),
        "input_pure_basis": report.get("input_pure_basis"),
        "mathematical_result": report.get("result"),
        **certificate,
        **old.serialize_expressions(ring, named),
    }
    path = args.output.with_name(args.output.stem + "-certificate.json.gz")
    metadata = pure.store_gzip(path, payload, args.max_certificate_bytes)
    metadata.update({
        "content_scope": payload["content_scope"],
        "original_root_count": len(named),
        "old_basis_or_dependencies_recomputed": False,
        "mixed_original_roots_decoded": 0,
    })
    report["portable_original_certificate"] = metadata


def run_research(args, report):
    limits = exact.Limits(
        args.max_seconds, args.max_nodes, args.max_atoms, args.max_terms,
        args.max_IBP_calls, args.memory_mib, args.max_rational_bits,
    )
    ring = colored.ColoredRing(limits)
    normalizer = quotient.ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    report["phase"] = "consume_one_bound_original_J6_pure_root"
    target = load_J6(args, ring, report)
    report["original_J6_pure"] = {
        "mode": PURE_MODE, "profile_affine_weight": WEIGHT,
        "original_sha256": ring.digest(target),
        "original_terms": len(target.terms),
    }
    report["phase"] = "decode_nine_archived_pure_originals_and_representatives"
    originals, vectors, labels, rows = solver.load_nine_basis(
        args, ring, normalizer, report
    )
    report["input_regularity"] = archived.dual.reachable_jet_bound(
        ring, [target] + originals
    )
    if report["input_regularity"]["colors"] != ["q"]:
        raise ValueError("a mixed color entered the one pure target")
    named = {"original_J6_minus4": target}
    named.update({
        "archived_original_pure_column_%02d" % position: value
        for position, value in zip(solver.BASIS_POSITIONS, originals)
    })
    certificate = {
        "archived_selected_word_representatives": rows,
        "archived_selected_labels": labels,
        "normalizer_sound_but_not_complete": True,
        "old_research_or_profile_evaluation_repeated": False,
    }
    save_certificate(args, report, ring, named, certificate)
    report["phase"] = "one_new_Q_solve_and_fresh_original_difference"
    coefficients, difference, proof, span, statistics = solver.solve_once(
        ring, normalizer, target, originals, vectors, limits, args
    )
    name = "one_J6_proposed_original_difference"
    named[name] = difference
    proof["original_difference_root"] = name
    proof["coefficients_in_original_global_columns"] = [
        [labels[index]["global_R116_column"], str(value)]
        for index, value in sorted(coefficients.items())
    ]
    certificate["one_J6_proposal"] = proof
    report["one_J6_proposal"] = {
        key: value for key, value in proof.items() if not key.endswith("_rows")
    }
    report["nine_archived_representative_span"] = span
    positive = proof["original_identity_proved"]
    report["result"] = {
        "status": "general_pure_J6_member_identity_proved"
            if positive else "undecided_sound_original_remainder",
        "general_pure_J6_member_proved": positive,
        "general_pure_J6_nonmember_proved": False,
        "complete_two_mode_J6_member_proved": False,
        "balanced_mixed_J6_member_proved": False,
        "actual_cost_sign_or_signed_control_claimed": False,
        "all_general_pure_costs_in_response_proved": False,
        "profile_affine_weight": WEIGHT, "pure_mode": PURE_MODE,
    }
    report["normalizer_statistics"] = statistics
    report["coefficient_arithmetic"] = {
        "field": "Q", "profile_atoms": len(ring.p.atoms),
        "coefficient_nodes": len(ring.algebra.c.nodes),
        "limits_check_calls": limits.calls,
    }
    report["phase"] = "complete_one_J6_general_pure_question"
    report["completion"] = "complete"
    save_certificate(args, report, ring, named, certificate)


def artificial_toys():
    """Small new target selection / subset decoding / solve interfaces only."""
    checks = {}
    hashes = {"-4": "pure", "-2": "mixed"}
    rows = [
        {"family": "toy", "state_key": [1, 0],
         "original_mode_sha256": hashes, "marker": "chosen"},
        {"family": "toy", "state_key": [2, 0],
         "original_mode_sha256": hashes, "marker": "other"},
    ]
    if select_record(rows, "toy", [1, 0], hashes)["marker"] != "chosen":
        raise AssertionError("the requested state selection changed")
    for badrows, expected in (
        (rows + [rows[0]], hashes),
        (rows[1:], hashes),
        (rows, {"-4": "changed", "-2": "mixed"}),
    ):
        try:
            select_record(badrows, "toy", [1, 0], expected)
        except ValueError:
            continue
        raise AssertionError("duplicate, absent, or changed target identity accepted")
    checks["one_state_and_original_hash_binding"] = True

    if (
        actual_environment_allowed({})
        or actual_environment_allowed({"GITHUB_ACTIONS": "true",
            "GITHUB_REPOSITORY": "someone/other"})
        or not actual_environment_allowed({"GITHUB_ACTIONS": "true",
            "GITHUB_REPOSITORY": REPOSITORY})
    ):
        raise AssertionError("the actual environment predicate changed")
    checks["actual_execution_requires_the_named_public_Actions"] = True

    limits = exact.Limits(
        seconds=30, nodes=8000, atoms=4000, terms=8000,
        rewrites=20000, memory_mib=512,
    )
    ring = colored.ColoredRing(limits)
    q, qb, x = ring.jet(), ring.color("qbar"), ring.x()
    basis_originals = [q**4, q*q*q.D()*q.D()]
    names = {"toy_pure": basis_originals[0], "toy_mixed": q*q*qb*qb}
    payload = json.loads(pure.data_bytes(old.serialize_expressions(ring, names)))
    restored = axis.subset_decode(ring, payload, ["toy_pure"])
    if (
        set(restored) != {"toy_pure"}
        or ring.digest(restored["toy_pure"]) != ring.digest(names["toy_pure"])
    ):
        raise AssertionError("the selected original subset changed")
    pure.require_degree(ring, restored["toy_pure"], "q", 4)
    checks["only_the_selected_original_root_is_decoded"] = True

    producer = quotient.ProfileNormalizer(ring, 20000, 8000)
    vectors = [producer.expression(value) for value in basis_originals]
    records = [{
        "original_position": i, "original_root": "basis_%d" % i,
        "original_sha256": ring.digest(value),
        "word_summary": producer.word.summary(vector),
        "word_rows": pure.word_rows(vector),
    } for i, (value, vector) in enumerate(zip(basis_originals, vectors))]
    consumer = quotient.ProfileNormalizer(ring, 20000, 8000)
    archived_vectors = [
        solver.bind_word_row(consumer, row, ring.digest(value), "basis_%d" % i)
        for i, (row, value) in enumerate(zip(records, basis_originals))
    ]
    if consumer.legacy.stats["primitive_calls"] or consumer.word.stats["primitive_calls"]:
        raise AssertionError("archived representative read normalized old originals")
    tiny = argparse.Namespace(max_IBP_calls=20000, max_terms=8000)
    target = F(2, 7)*basis_originals[0] - F(3, 11)*basis_originals[1]
    coefficients, difference, proof, _, _ = solver.solve_once(
        ring, consumer, target, basis_originals, archived_vectors, limits, tiny
    )
    if (
        coefficients != {0: F(2, 7), 1: F(-3, 11)}
        or not proof["original_identity_proved"]
        or not proof["coefficients_are_exact_Q_not_modular_lifts"]
    ):
        raise AssertionError("a rational one-target fresh original proof failed")
    checks["new_target_uses_archived_representatives_and_fresh_original_zero"] = True

    other = quotient.ProfileNormalizer(ring, 20000, 8000)
    other_vectors = [
        solver.bind_word_row(other, row, ring.digest(value), "basis_%d" % i)
        for i, (row, value) in enumerate(zip(records, basis_originals))
    ]
    _, unresolved, pending, _, _ = solver.solve_once(
        ring, other, target + x**3*q**4,
        basis_originals, other_vectors, limits, tiny,
    )
    if (
        pending["original_identity_proved"]
        or not pending["nonzero_representative_is_not_nonmembership"]
    ):
        raise AssertionError("an unresolved remainder was treated as nonmembership")
    checks["unresolved_is_not_a_negative_identity"] = True
    raw = old.serialize_expressions(
        ring, {"target": target, "difference": difference, "unresolved": unresolved}
    )
    decoded = old.decode_expressions(ring, json.loads(pure.data_bytes(raw)))
    if any(ring.digest(decoded[k]) != ring.digest(v)
           for k, v in {"target": target, "difference": difference,
                        "unresolved": unresolved}.items()):
        raise AssertionError("the new original certificate did not round-trip")
    checks["new_original_targets_and_differences_are_portable"] = True
    return {
        "checks": checks, "all_passed": all(checks.values()),
        "published_reports_or_roots_read": False,
        "research_profile_or_geometry_evaluated": False,
        "old_forty_basis_or_thirty_one_relations_recomputed": False,
        "new_response_or_forcing_compiled": False,
    }


def write_main(args, report):
    raw = pure.data_bytes(report, pretty=True)
    if len(raw) > args.max_main_bytes:
        path = args.output.with_name(args.output.stem + "-complete-report.json.gz")
        metadata = pure.store_gzip(path, report, args.max_full_report_bytes)
        compact = {key: value for key, value in report.items()
                   if key not in ("J6_input", "input_pure_basis", "normalizer_statistics")}
        compact["complete_report_file"] = metadata
        raw = pure.data_bytes(compact, pretty=True)
        if len(raw) > args.max_main_bytes:
            compact = {key: report.get(key) for key in (
                "schema", "completion", "phase", "scope", "github_repository",
                "github_run_id", "github_sha", "source_hashes", "result", "error",
                "elapsed_seconds", "peak_rss_mib", "portable_original_certificate")}
            compact["complete_report_file"] = metadata
            compact["full_result_preserved"] = True
            raw = pure.data_bytes(compact, pretty=True)
        if len(raw) > args.max_main_bytes:
            raise ValueError("the complete source binding exceeds the main budget")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    return {"filename": args.output.name, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "completion": report["completion"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--family-directory", type=Path, default=prior.directory(FAMILY))
    parser.add_argument("--basis-directory", type=Path, default=TOPIC / (
        "notes/actions-" + solver.BASIS_RUN + "-1-" + solver.BASIS_LANE))
    parser.add_argument("--max-seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-nodes", type=int, default=500000)
    parser.add_argument("--max-atoms", type=int, default=100000)
    parser.add_argument("--max-terms", type=int, default=120000)
    parser.add_argument("--max-IBP-calls", type=int, default=500000)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    parser.add_argument("--max-main-bytes", type=int, default=90000)
    parser.add_argument("--max-certificate-bytes", type=int, default=1500000)
    parser.add_argument("--max-full-report-bytes", type=int, default=2000000)
    args = parser.parse_args()
    if min(
        args.max_seconds, args.memory_mib, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.max_rational_bits,
        args.max_certificate_bytes, args.max_full_report_bytes,
    ) <= 0:
        parser.error("positive resource bounds required")
    if not 10000 <= args.max_main_bytes < 100000:
        parser.error("reserve a source-bound main strictly below 100KB")
    if (args.max_main_bytes + args.max_certificate_bytes + args.max_full_report_bytes
            > pure.TOTAL_OUTPUT_BYTES):
        parser.error("declared outputs exceed the reserved total byte budget")
    if not args.toy_only and not actual_environment_allowed(os.environ):
        parser.error("the new J6 pure target is public-repository-Actions-only")
    started, code = time.monotonic(), 0
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "bind_frozen_helpers",
        "scope": "one complete J6 pure target against nine archived true bases",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": {},
        "work_scope": {
            "new_general_pure_targets": 0 if args.toy_only else 1,
            "new_response_formulas": 0,
            "old_basis_roots_renormalized": 0,
            "old_pure_dependencies_recomputed": 0,
            "mixed_research_roots_decoded": 0,
            "new_balanced_or_other_mixed_targets": 0,
            "new_profile_evaluations": 0,
            "old_N2_v4_forcing_recompiled": 0,
            "modular_lifts_used_as_Q_coefficients": False,
        },
        "limits": {
            "seconds": args.max_seconds, "memory_polling_mib": args.memory_mib,
            "nodes": args.max_nodes, "atoms": args.max_atoms, "terms": args.max_terms,
            "IBP_calls_per_normalizer": args.max_IBP_calls,
            "rational_bits_in_span": args.max_rational_bits,
            "main_bytes": args.max_main_bytes,
            "certificate_bytes": args.max_certificate_bytes,
            "full_report_bytes": args.max_full_report_bytes,
        },
    }
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["phase"] = "new_target_selector_and_archived_solver_artificial_interfaces"
            report["toy"] = artificial_toys()
            report["completion"] = "toy_passed"
        else:
            run_research(args, report)
    except formal.CompilationBudgetExceeded as error:
        report["completion"], report["error"], code = "resource_limit", str(error), 2
    except Exception as error:
        report["completion"], code = "implementation_check_failed", 1
        report["error"] = {"type": type(error).__name__, "message": str(error)}
    report["elapsed_seconds"] = time.monotonic() - started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    written = write_main(args, report)
    print(json.dumps({"output": str(args.output), **written}), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
