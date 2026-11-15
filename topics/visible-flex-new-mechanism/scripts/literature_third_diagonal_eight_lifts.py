#!/usr/bin/env python3
"""Eight new diagonal lifts of the published full third templates (R247).

Read the original W36 DAG. Restore only the eighteen already selected
commutator diagonal inputs; solve eight new diagonal targets and verify
each relation from the original colored difference. No old 151/152
compilation, P1 target, fourth response, profile value, or geometry is run.
Both artificial development and research are public-Actions-only.
Only a temporary main JSON is written. Proof data stays in memory.
"""
from __future__ import annotations

import argparse
import ast
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

import literature_colored_profile_algebra as colored
import literature_color_priority_words as priority
import literature_full_m8_tail_response_projection as reader
import literature_pure_bulk_exact_membership as exact

SCHEMA = "visible-flex-third-diagonal-eight-lifts-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = Path(__file__).resolve().parents[1]
REFERENCE_INDICES = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 18, 20, 21, 24)
TARGET_INDICES = (30, 32, 34, 37, 40, 100, 104, 109)
PARAMETERS = ("p0", "p1", "p2", "r0", "r1", "s0", "s1", "t1")
PAIRS = tuple((i, j) for i in range(8) for j in range(i+1, 8))
W_DIRECTORY = "actions-43645177423-1-local_fourth_quotient"
THIRD_DIRECTORY = "actions-43633746055-1-full_phase_bridge_exact"
REFERENCE_DIRECTORY = "actions-43632772378-1-closed_c1_endpoint"
W_RUN = "43645177423"
W_COMMIT = "2f1b809c0b0abb7a26303d36940edc203815f872"
W_MAIN_SHA = "19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a"
W_PUBLICATION_SHA = "c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba"
REFERENCE_SHA = "622cd662e60eed74e58f59bb52981aed6a209eeaf4664bc7304a5e3826b6da86"
REFERENCE_RUN = "43632772378"
REFERENCE_COMMIT = "31a276f6f4b2361d10bea9a46fea307a951bb639"
FROZEN_SOURCES = {
    "literature_full_m8_tail_response_projection.py":
        (32096, "e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345"),
    "literature_color_priority_words.py":
        (21642, "ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9"),
    "literature_colored_profile_algebra.py":
        (15738, "c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f"),
    "literature_pure_bulk_exact_membership.py":
        (33718, "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70"),
    "literature_local_fourth_quotient.py":
        (38857, "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0"),
}
TARGET_SHA = (
    "be8a31110800e396af0d8b2c7d240584f03cd30bcf4e1d1d8f222f2cafc8c199",
    "c8f4568fbddee3985dfd3245aff22592bb065d22dbdc958fc61433ba20279f79",
    "4e76c7b917c4a00138308388d72c40def5837044d287c28242f91d635bf5f312",
    "94b42fb4261209e6e6e72c078b6e873dfe08dd477672afdcb0156f95051ead28",
    "b5155855451e65acb83b0efd8ec51e6467fe343fa80fbeab6c04e1e523c0f368",
    "8aa68ac3defca7d0d88ec9b5c67dc7b30bedc569129d6fbd8705314fbe331e2d",
    "578763eecd81ff4e4bf2f3775b253c4315c6c3d58cfb2e3346524b79d8203f0d",
    "63ec5cb74cb487c52a3e81f1f0b010352f7df57edabb1f08f42dea9093eb52ee",
)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    raw = Path(path).read_bytes()
    return {"filename": Path(path).name, "bytes": len(raw), "sha256": sha(raw)}


def require_public_actions():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise RuntimeError("new development and research run only in the public repository Actions")


def source_inventory():
    """Read source identities, never import or execute an additional target."""
    root = Path(__file__).resolve().parent
    for name, expected in FROZEN_SOURCES.items():
        item = identity(root/name)
        if (item["bytes"], item["sha256"]) != expected:
            raise ValueError("frozen input API source changed: "+name)
    todo, found = [Path(__file__).resolve()], {}
    while todo:
        path = todo.pop()
        if path.name in found:
            continue
        raw = path.read_bytes()
        found[path.name] = {"bytes": len(raw), "sha256": sha(raw)}
        tree = ast.parse(raw, filename=path.name)
        names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names.append(node.module)
        for name in names:
            if "." not in name and name.startswith("literature_"):
                child = root/(name+".py")
                if not child.is_file():
                    raise ValueError("missing imported frozen source: "+name)
                todo.append(child)
    return dict(sorted(found.items()))


class MonitoredLimits(exact.Limits):
    """The added counter concerns calls to rational(), not every DAG operation."""
    def __init__(self, args):
        super().__init__(seconds=args.max_seconds, nodes=args.max_nodes,
            atoms=args.max_atoms, terms=args.max_terms, rewrites=args.max_word_calls,
            memory_mib=args.max_memory_mib, rational_bits=args.max_rational_bits)
        self.monitored_rational_operations = 0
        self.maximum_monitored_rational_bits = 0
        self.max_monitored_operations = args.max_monitored_rational_operations

    def rational(self, value):
        value = super().rational(value)
        self.monitored_rational_operations += 1
        self.maximum_monitored_rational_bits = max(self.maximum_monitored_rational_bits,
            value.numerator.bit_length(), value.denominator.bit_length())
        if self.monitored_rational_operations > self.max_monitored_operations:
            raise exact.formal.CompilationBudgetExceeded("monitored rational operation ceiling")
        self.check()
        return value


def mapper_for(ring, args):
    return priority.PriorityWords(ring, max_calls=args.max_word_calls,
        max_terms=args.max_terms, max_weight=3,
        max_shuffle_entries=args.max_cache_entries,
        max_cache_entries=args.max_cache_entries, color_order=("q",))


def check_word_grammar(value):
    for (local, word), coefficient in value.terms.items():
        priority.local_key(local, ("q",))
        priority.word_key(word, ("q",))
        if len(local[1])+sum(len(letter[1]) for letter in word) != 3:
            raise AssertionError("a third diagonal representative lost degree three")
        if any(not priority.is_remainder_letter(letter, ("q",)) for letter in word):
            raise AssertionError("R179 requires canonical remainder letters")
        if not coefficient:
            raise AssertionError("stored representative contains a zero term")


def check_reference_metadata(data):
    if data.get("schema") != "visible-flex-closed-C1-endpoint-and-pure-P1-v1":
        raise ValueError("old reference report schema")
    if data.get("completion") != "complete":
        raise ValueError("old reference selection was not completed")
    github = data.get("github", {})
    if (github.get("GITHUB_REPOSITORY"), github.get("GITHUB_RUN_ID"), github.get("GITHUB_SHA")) != (
            REPOSITORY, REFERENCE_RUN, REFERENCE_COMMIT):
        raise ValueError("old reference source/run/repository")
    selected = data.get("reachable_space", {})
    if (selected.get("columns"), selected.get("R71_columns"),
            selected.get("C3_coefficient_columns"), selected.get("closed_C1_coefficient_columns")) != (151, 28, 56, 67):
        raise ValueError("old complete third-space coverage metadata")
    if selected.get("independent_column_indices") != list(REFERENCE_INDICES):
        raise ValueError("the eighteen old input labels changed")


def read_original_inputs(args, limits, report):
    old_path = args.reference_directory/"closed-C1-endpoint.json"
    old_raw = reader.checked_bytes(old_path, 20000)
    if len(old_raw) != 13911 or sha(old_raw) != REFERENCE_SHA:
        raise ValueError("old reference main original-byte binding")
    old = json.loads(old_raw)
    check_reference_metadata(old)
    publication = args.w_directory/"receipt.json"
    publication_raw = reader.checked_bytes(publication, 40000)
    if len(publication_raw) != 31846 or sha(publication_raw) != W_PUBLICATION_SHA:
        raise ValueError("W-only public terminal publication binding")
    bindings = SimpleNamespace(
        source_report=args.w_directory/"local-fourth-quotient.json",
        source_report_sha256=W_MAIN_SHA, source_run=W_RUN, source_commit=W_COMMIT,
        publication_receipt=publication,
        templates=args.w_directory/"local-fourth-quotient-W-original-expressions.json.gz",
        third_receipt=args.third_directory/"full-phase-bridge-exact.json")
    producer_raw = reader.checked_bytes(bindings.source_report, 4000)
    if len(producer_raw) != 3982 or sha(producer_raw) != W_MAIN_SHA:
        raise ValueError("W-only original compact main byte binding")
    producer = json.loads(producer_raw)
    for item in producer["source_hashes"].values():
        observed = report["source_hashes"].get(item["filename"])
        if observed != {"bytes": item["bytes"], "sha256": item["sha256"]}:
            raise ValueError("original W producer dependency changed: "+item["filename"])
    ring, full = reader.load_templates(bindings, limits, report)
    if tuple(reader.blocks.EXPECTED_KEPT) != tuple(range(28))+TARGET_INDICES:
        raise ValueError("W36 retained original order differs from R247")
    if tuple(ring.digest(x) for x in full[28:]) != TARGET_SHA:
        raise ValueError("the eight unsymmetrized original target hashes changed")
    if any(degree != (("a", 1), ("b", 1), ("c", 1))
            for item in full for degree in ring.color_degrees(item)):
        raise AssertionError("original full third slots a;b,c were lost")
    report["old_reference_input"] = {
        "filename": old_path.name, "bytes": len(old_raw), "sha256": sha(old_raw),
        "run_id": REFERENCE_RUN, "source_commit": REFERENCE_COMMIT,
        "selected_original_indices": list(REFERENCE_INDICES),
        "old_151_compilation_or_elimination_repeated": False,
        "old_P1_or_response_target_repeated": False}
    report["template_input"]["decoded_original_roots_for_binding"] = 36
    report["template_input"]["diagonal_inputs_selected"] = 18
    report["template_input"]["new_diagonal_targets_selected"] = 8
    report["template_input"]["remaining_roots_not_diagonalized"] = 10
    return ring, full


def linear_combination(ring, originals, coefficients):
    answer = ring.number(0)
    for index, coefficient in sorted(coefficients.items()):
        answer += coefficient*originals[index]
    return answer


def lift_target(ring, full_target, reference_full, span, mapper, fresh):
    q = ring.color("q")
    diagonal = ring.substitute(full_target, {"a": q, "b": q, "c": q})
    target_word = mapper.expression(diagonal)
    check_word_grammar(target_word)
    coefficients, residual = span.reduce(target_word.terms)
    if residual:
        return {"member": False, "diagonal": diagonal, "word": target_word,
            "residual": residual, "coefficients": coefficients}
    # Form the genuinely colored difference first. Only then take its
    # three-slot diagonal, independently of the solved word row identity.
    gamma = linear_combination(ring, reference_full, coefficients)
    chi = full_target-gamma
    chi_diagonal = ring.substitute(chi, {"a": q, "b": q, "c": q})
    fresh_word = fresh.expression(chi_diagonal)
    check_word_grammar(fresh_word)
    if fresh_word.terms:
        raise AssertionError("fresh original colored difference does not have zero diagonal")
    if any(degree != (("a", 1), ("b", 1), ("c", 1))
            for degree in ring.color_degrees(chi)):
        raise AssertionError("lifting the coordinates changed the full third slots")
    return {"member": True, "diagonal": diagonal, "word": target_word,
        "coefficients": coefficients, "gamma": gamma, "chi": chi,
        "chi_diagonal": chi_diagonal, "fresh_word": fresh_word}


def research(args, report):
    limits = MonitoredLimits(args)
    report["phase"] = "bound_original_inputs"
    ring, full = read_original_inputs(args, limits, report)
    mapper, fresh = mapper_for(ring, args), mapper_for(ring, args)
    q = ring.color("q")
    reference_full = [full[index] for index in REFERENCE_INDICES]
    reference_words, reference_records = [], []
    report["phase"] = "restore_eighteen_reference_diagonals_once"
    for index, original in zip(REFERENCE_INDICES, reference_full):
        limits.formal.time_check()
        diagonal = ring.substitute(original, {"a": q, "b": q, "c": q})
        value = mapper.expression(diagonal)
        check_word_grammar(value)
        reference_words.append(value)
        i, j = PAIRS[index]
        reference_records.append({
            "original_index": index, "quadratic_pair": [PARAMETERS[i], PARAMETERS[j]],
            "full_original_sha256": ring.digest(original),
            "diagonal_original_sha256": ring.digest(diagonal),
            "restored_word": mapper.summary(value)})
    span = colored.JointSpan([item.terms for item in reference_words], limits)
    report["reference_restoration"] = {
        "count": len(reference_words), "input_indices": list(REFERENCE_INDICES),
        "word_span_pivot_count_for_solving": len(span.independent),
        "independent_input_positions_used_by_solver": span.independent,
        "records": reference_records,
        "old_151_span_not_recomputed": True,
        "rank_eighteen_not_assumed": True,
        "full_W_dimension_or_full_response_rank_recomputed": False}
    report["results"] = []
    proof = {"schema": SCHEMA+"-in-memory-original-proof",
        "reference_original_indices": list(REFERENCE_INDICES),
        "reference_word_rows": [priority.rows(value) for value in reference_words],
        "target_proofs": []}
    report["phase"] = "eight_new_diagonal_targets"
    for retained, original_index in enumerate(TARGET_INDICES, start=28):
        limits.formal.time_check()
        outcome = lift_target(ring, full[retained], reference_full, span, mapper, fresh)
        if not outcome["member"]:
            report["unresolved_target"] = {
                "original_index": original_index, "retained_position": retained,
                "residual_rows": [[local, word, str(c)]
                    for (local, word), c in sorted(outcome["residual"].items())],
                "reason": "new diagonal did not close in the eighteen restored references",
                "full_third_or_response_nonmembership_asserted": False}
            raise AssertionError("new diagonal membership not certified; preserve the residual")
        coefficients = outcome["coefficients"]
        dense28 = [F(0)]*28
        for position, coefficient in coefficients.items():
            dense28[REFERENCE_INDICES[position]] = coefficient
        record = {
            "target_original_index": original_index, "retained_position": retained,
            "original_full_target_sha256": ring.digest(full[retained]),
            "original_diagonal_target_sha256": ring.digest(outcome["diagonal"]),
            "gamma_coefficients_in_original_28_order": [str(c) for c in dense28],
            "nonzero_gamma_coefficients": [
                {"original_index": i, "quadratic_pair": [PARAMETERS[PAIRS[i][0]], PARAMETERS[PAIRS[i][1]]],
                 "coefficient": str(c)} for i, c in enumerate(dense28) if c],
            "gamma_full_original_sha256": ring.digest(outcome["gamma"]),
            "chi_full_original_sha256": ring.digest(outcome["chi"]),
            "chi_full_raw_terms": len(outcome["chi"].terms),
            "chi_diagonal_original_sha256": ring.digest(outcome["chi_diagonal"]),
            "chi_diagonal_raw_terms": len(outcome["chi_diagonal"].terms),
            "fresh_original_diagonal_word": fresh.summary(outcome["fresh_word"]),
            "fresh_original_diagonal_zero": True,
            "full_colored_identity": "chi = original_tau - gamma; full chi was not set to zero",
            "full_chi_nonzero_source": "R87/R247 direct-sum classes, not a nonzero raw-term test",
            "right_anchor": "I=int_right_endpoint^xi; all original left tails retained"}
        report["results"].append(record)
        proof["target_proofs"].append({
            **record, "target_word_rows": priority.rows(outcome["word"]),
            "fresh_original_difference_word_rows": priority.rows(outcome["fresh_word"])})
        print("EIGHT_DIAGONAL_LIFT "+json.dumps(record, sort_keys=True, separators=(",", ":")), flush=True)
    limits.formal.time_check()
    proof_raw = canonical(proof)
    if len(proof_raw) > args.max_proof_bytes:
        raise exact.formal.CompilationBudgetExceeded("in-memory proof serialization byte ceiling")
    report["in_memory_proof"] = {
        "bytes": len(proof_raw), "sha256": sha(proof_raw),
        "written_to_repository_release_or_artifact": False,
        "reconstruction": "published original W roots plus printed exact gamma coordinates and this source"}
    report["word_maps"] = {
        "basis_and_new_targets": dict(mapper.stats),
        "fresh_eight_original_differences": dict(fresh.stats),
        "first_map_new_primitive_calls": mapper.run_primitive_calls,
        "fresh_map_new_primitive_calls": fresh.run_primitive_calls,
        "all_surviving_letters_checked_against_R179": True,
        "cycle_fallbacks_used": False}
    report["monitored_cost"] = {
        "rational_calls": limits.monitored_rational_operations,
        "maximum_bits_at_monitored_rational_calls": limits.maximum_monitored_rational_bits,
        "scope": "only MonitoredLimits.rational calls, not all original DAG arithmetic",
        "restored_profile_atoms": len(ring.p.atoms)}
    report["mathematical_result"] = {
        "all_eight_original_diagonal_identities_verified": True,
        "full_colored_chi_definitions_preserved": True,
        "new_target_count": 8,
        "structural_consequence_from_R87_R208_R247":
            "W = W71 direct_sum span(chi_30,chi_32,chi_34,chi_37,chi_40,chi_100,chi_104,chi_109); each chi has zero diagonal",
        "extra_pure_zero_response_generators_are_definitions_only": 64,
        "new_fourth_responses_evaluated": 0,
        "full_response_rank_claimed": False,
        "fixed_circle_period_quotient_computed": False,
        "signed_actual_cost_or_joint_solution_claimed": False}
    report["phase"], report["completion"] = "complete", "complete"


def artificial_checks(args):
    """New lift/colored-difference/selection checks, without reading a real input."""
    limits = MonitoredLimits(args)
    ring = colored.ColoredRing(limits)
    mapper, fresh = mapper_for(ring, args), mapper_for(ring, args)
    a, b, c, q = (ring.color(name) for name in ("a", "b", "c", "q"))
    base0, base1 = a*b*c, a*(b*c).I()
    hook = (a*(b*c).I()).I()-(b*(a*c).I()).I()/2-(c*(a*b).I()).I()/2
    refs = [base0, base1, 2*base0-base1]
    refwords = [mapper.expression(ring.substitute(v, {"a": q, "b": q, "c": q})) for v in refs]
    span = colored.JointSpan([v.terms for v in refwords], limits)
    target = F(3, 7)*base0-F(5, 11)*base1+hook
    answer = lift_target(ring, target, refs, span, mapper, fresh)
    checks = {}
    assert answer["member"] and answer["coefficients"] == {0: F(3, 7), 1: F(-5, 11)}
    checks["new_target_uses_one_exact_rational_combination_of_the_fixed_references"] = True
    assert span.independent == [0, 1] and len(span.basis) == 2
    checks["dependent_reference_does_not_create_a_false_pivot_or_an_assumed_rank"] = True
    assert answer["chi"].key() == hook.key() and hook.terms and not answer["fresh_word"].terms
    checks["colored_hook_is_retained_while_its_fresh_three_slot_diagonal_is_zero"] = True
    nested = (a*(b*c).I()).I()
    assert ring.substitute(nested, {"a": q, "b": q, "c": q}).key() == (q*(q*q).I()).I().key()
    checks["simultaneous_substitution_keeps_both_nested_original_primitive_levels"] = True
    wrong = lift_target(ring, a*b.D()*c.D(), refs, span, mapper, fresh)
    assert not wrong["member"] and wrong["residual"] and len(span.basis) == 2
    checks["a_target_residual_is_neither_zero_nor_added_as_a_new_reference"] = True
    assert not fresh.expression((q*q*q).D().I()-q*q*q).terms
    checks["right_primitive_keeps_the_original_plus_integral_orientation"] = True
    bad_letter = (0, (("q", 0), ("q", 0), ("q", 1)))
    invalid = mapper.term((0, ()), (bad_letter,))
    rejected = False
    try:
        check_word_grammar(invalid)
    except (ValueError, AssertionError):
        rejected = True
    assert rejected
    checks["noncanonical_surviving_letter_cannot_receive_the_R179_flag"] = True
    metadata = {"schema": "visible-flex-closed-C1-endpoint-and-pure-P1-v1", "completion": "complete",
        "github": {"GITHUB_REPOSITORY": REPOSITORY, "GITHUB_RUN_ID": REFERENCE_RUN, "GITHUB_SHA": REFERENCE_COMMIT},
        "reachable_space": {"columns": 151, "R71_columns": 28, "C3_coefficient_columns": 56,
            "closed_C1_coefficient_columns": 67, "independent_column_indices": list(REFERENCE_INDICES)}}
    check_reference_metadata(metadata)
    metadata["reachable_space"]["independent_column_indices"][-1] = 25
    rejected = False
    try:
        check_reference_metadata(metadata)
    except ValueError:
        rejected = True
    assert rejected
    checks["changed_old_reference_selection_is_rejected_without_opening_old_targets"] = True
    return {"all_passed": all(checks.values()), "checks": checks,
        "artificial_only": True, "real_input_files_opened": False,
        "old_151_or_152_or_P1_or_response_checks_repeated": False}


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--w-directory", type=Path, default=TOPIC/"notes"/W_DIRECTORY)
    p.add_argument("--third-directory", type=Path, default=TOPIC/"notes"/THIRD_DIRECTORY)
    p.add_argument("--reference-directory", type=Path, default=TOPIC/"notes"/REFERENCE_DIRECTORY)
    p.add_argument("--toy-only", action="store_true")
    p.add_argument("--output", type=Path, required=True,
                   help="runner-temporary main only; publisher records metadata and stdout")
    p.add_argument("--max-seconds", type=float, default=120)
    p.add_argument("--max-memory-mib", type=int, default=512)
    p.add_argument("--max-nodes", type=int, default=300000)
    p.add_argument("--max-atoms", type=int, default=40000)
    p.add_argument("--max-terms", type=int, default=40000)
    p.add_argument("--max-word-calls", type=int, default=150000)
    p.add_argument("--max-cache-entries", type=int, default=150000)
    p.add_argument("--max-rational-bits", type=int, default=8192)
    p.add_argument("--max-monitored-rational-operations", type=int, default=1000000)
    p.add_argument("--max-proof-bytes", type=int, default=8000000)
    p.add_argument("--max-summary-bytes", type=int, default=95000)
    args = p.parse_args(argv)
    for key, value in vars(args).items():
        if key.startswith("max_") and value <= 0:
            p.error(key+" must be positive")
    return args


def emit_report(args, report):
    raw = canonical(report)+b"\n"
    if len(raw) > args.max_summary_bytes:
        report = {
            "schema": SCHEMA, "completion": "output_limit", "phase": report.get("phase"),
            "complete_report_bytes": len(raw), "complete_report_sha256": sha(raw),
            "mathematical_result": report.get("mathematical_result"),
            "completed_target_count": len(report.get("results", [])),
            "target_records_already_printed": True,
            "error": "full temporary main exceeds the explicit byte ceiling",
            "task_complete": False}
        raw = canonical(report)+b"\n"
        if len(raw) > args.max_summary_bytes:
            raise ValueError("summary byte ceiling cannot contain even the failure receipt")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    print("MATHEMATICAL_RESULT "+json.dumps(report.get("mathematical_result", {
        "completion": report.get("completion"), "phase": report.get("phase"),
        "development": report.get("development"), "error": report.get("error")}),
        sort_keys=True, separators=(",", ":")), flush=True)
    print("COMPLETE_REPORT "+raw.decode().rstrip(), flush=True)
    print("TEMPORARY_MAIN "+json.dumps({"bytes": len(raw), "sha256": sha(raw),
        "filename": args.output.name, "payload_to_be_published": False},
        sort_keys=True, separators=(",", ":")), flush=True)
    return report.get("completion")


def main(argv=None):
    args = parse_args(argv)
    started = time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "public_gate",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "driver": identity(__file__),
        "parameters": {key: str(value) if isinstance(value, Path) else value
                       for key, value in vars(args).items()},
        "metadata_only": True, "task_complete": False,
        "new_scientific_work": "eight exact third-diagonal lifts; zero fourth responses",
        "scope": "universal same-right-anchor functions; no fixed-circle range or actual signed cost"}
    try:
        require_public_actions()
        report["source_hashes"] = source_inventory()
        if args.toy_only:
            report["phase"] = "new_artificial_lift_checks"
            report["development"] = artificial_checks(args)
            report["phase"], report["completion"] = "complete", "complete"
        else:
            research(args, report)
    except exact.formal.CompilationBudgetExceeded as error:
        report.update(completion="resource_limit", error_type=type(error).__name__, error=str(error),
                      unfinished_targets_are_not_zero=True)
    except Exception as error:
        report.update(completion="implementation_check_failed", error_type=type(error).__name__,
                      error=str(error), unfinished_targets_are_not_zero=True)
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_resident_mib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    status = emit_report(args, report)
    return 0 if status == "complete" else 2


if __name__ == "__main__":
    sys.exit(main())
