#!/usr/bin/env python3
"""Append exactly one R166 static cut to the published finite positive-character system.

The complete head, 124 equalities, old 63 inequalities, their RREF and six
path integrals are consumed unchanged.  Only a(1/2) is newly assembled.
The archived exact-coordinate/Farkas engine is reused, without rebuilding
any source coefficients, forcing, original functions, or old normal forms.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_character_minus2_finite_necessary as base

SCHEMA = "visible-flex-character-minus2-single-static-cut-v1"
REPOSITORY = "Rogerhu12/math-research-public"
PREVIOUS = {
    "run": "43665971895",
    "commit": "05bb659b59997906316ddd2873aedbf4840f62a5",
    "lane": "character_minus2_finite_necessary",
    "report": {"filename": "character-minus2-finite-necessary.json", "bytes": 10143,
        "sha256": "1e8d751fca7fb6d8b2c33d1152e8651399824be22ffad5496c8bdb48de7fef6c"},
    "publication": {"filename": "receipt.json", "bytes": 40026,
        "sha256": "6fbdf4f3c98bfa14fe6344d988a5df9acad10b4c7e598711aa3f5b57c8515764"},
    "certificate": {"filename": "character-minus2-finite-necessary-certificate.json.gz",
        "stored_bytes": 31976,
        "stored_sha256": "5658e056313fff939356f91c97578a8dfc3e1158661b209c84ba7d2b86aa3634",
        "raw_bytes": 143028,
        "raw_sha256": "dd539b088c354d99c04af46d8d7c63822679f13ebc02b14a673c76767fd745f7"},
    "driver": {"filename": "literature_character_minus2_finite_necessary.py", "bytes": 45116,
        "sha256": "d4c3751cf58f1ef08c534e61a16d7a40cd368980c0cca0ef48a0bce505ce3545"},
}
CUT_K = F(1, 2)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_identity(path):
    path = Path(path)
    raw = path.read_bytes()
    return {"filename": path.name, "bytes": len(raw), "sha256": sha(raw)}


def source_identity():
    reused = file_identity(Path(base.__file__).resolve())
    if reused != PREVIOUS["driver"]:
        raise ValueError("the archived exact finite-system engine source changed")
    return {"driver": file_identity(__file__), "archived_exact_finite_system_engine": reused,
            "head_or_profile_helpers_imported": False}


def read_small(path, expected):
    raw = Path(path).read_bytes()
    if len(raw) != expected["bytes"] or sha(raw) != expected["sha256"]:
        raise ValueError("published small input bytes/SHA changed")
    return json.loads(raw), raw


def verify_publication(publication, main, main_raw, metadata):
    if (publication.get("schema") != "visible-new-mechanism-actions-v1"
        or publication.get("repository") != REPOSITORY
        or str(publication.get("run_id")) != PREVIOUS["run"]
        or publication.get("source_commit") != PREVIOUS["commit"]
        or publication.get("lane") != PREVIOUS["lane"]):
        raise ValueError("the exact previous publication identity changed")
    if (main.get("schema") != base.SCHEMA or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != PREVIOUS["run"]
        or main.get("github_sha") != PREVIOUS["commit"]):
        raise ValueError("the complete previous main is required")
    if main.get("source_hashes", {}).get("driver") != PREVIOUS["driver"]:
        raise ValueError("main is not bound to the archived finite-system source")
    sources = publication.get("source_files", {})
    matches = [v for k, v in sources.items() if Path(k).name == PREVIOUS["driver"]["filename"]]
    if len(matches) != 1 or any(matches[0].get(k) != PREVIOUS["driver"][k]
                               for k in ("bytes", "sha256")):
        raise ValueError("receipt does not bind the archived producer bytes")
    outputs = {Path(row["path"]).name: row for row in publication.get("outputs", [])}
    if len(outputs) != len(publication.get("outputs", [])):
        raise ValueError("ambiguous duplicate publication output basename")
    rec = outputs.get(PREVIOUS["report"]["filename"], {})
    if rec.get("bytes") != len(main_raw) or rec.get("sha256") != sha(main_raw):
        raise ValueError("published previous main output identity changed")
    if any(metadata.get(k) != v for k, v in PREVIOUS["certificate"].items()):
        raise ValueError("main complete certificate metadata changed")
    rec = outputs.get(metadata["filename"], {})
    expected = {"bytes": metadata["stored_bytes"], "sha256": metadata["stored_sha256"],
                "raw_bytes": metadata["raw_bytes"], "raw_sha256": metadata["raw_sha256"]}
    if any(rec.get(k) != v for k, v in expected.items()):
        raise ValueError("receipt certificate packed/raw identity changed")
    return {"repository": REPOSITORY, "run": PREVIOUS["run"], "commit": PREVIOUS["commit"],
            "lane": PREVIOUS["lane"], "main": PREVIOUS["report"],
            "publication": PREVIOUS["publication"], "certificate": PREVIOUS["certificate"]}


def consume_previous(args, report, budget):
    main, raw_main = read_small(args.source_report, PREVIOUS["report"])
    publication, _ = read_small(args.source_publication, PREVIOUS["publication"])
    metadata = main.get("complete_necessary_certificate", {})
    binding = verify_publication(publication, main, raw_main, metadata)
    packed = Path(args.source_certificate).read_bytes()
    expected = PREVIOUS["certificate"]
    if len(packed) != expected["stored_bytes"] or sha(packed) != expected["stored_sha256"]:
        raise ValueError("complete inherited certificate packed bytes/SHA changed")
    raw = gzip.decompress(packed)
    if len(raw) != expected["raw_bytes"] or sha(raw) != expected["raw_sha256"]:
        raise ValueError("complete inherited certificate raw bytes/SHA changed")
    budget.check()
    data = json.loads(raw)
    if (data.get("schema") != base.SCHEMA + "-certificate"
        or data.get("target_weight") != -2
        or data.get("source_hashes") != main["source_hashes"]
        or data.get("input") != main["input"]
        or data.get("all_true_positive_characters_embed_in_this_outer_system") is not True
        or main.get("checkpoint", {}).get("complete_head_consumed") is not True):
        raise ValueError("the complete inherited necessary system is not the expected one")
    n = data["normal_coordinate_count"]
    if (n != main["system"]["all_normal_coordinates"]
        or len(data["normal_coordinate_metadata"]) != n
        or [r["index"] for r in data["normal_coordinate_metadata"]] != list(range(n))
        or len(data["equalities"]) != main["system"]["exact_external_equality_rows"]
        or len(data["inequalities"]) != main["system"]["exact_necessary_inequality_rows"]
        or len(data["reduced_inequalities"]) != main["system"]["nonzero_distinct_reduced_rows"]
        or len(data["free_normal_coordinates"]) != main["system"]["free_external_coordinates"]):
        raise ValueError("inherited exact system counts changed")
    if data.get("decision", {}).get("outer_candidate") is None:
        raise ValueError("the specific R166 already-published candidate is required")
    report["input"] = binding
    report["input"]["inherited_complete_head_identity"] = {
        k: main["input"][k] for k in ("run", "commit", "lane", "main", "publication", "export")}
    return main, data


def inherited_table(records, n, budget):
    """Read archived rows verbatim; do not regenerate or normalize the old rows."""
    table = base.RowTable(budget)
    table.records = deepcopy(records)
    for index, record in enumerate(records):
        if record.get("index") != index:
            raise ValueError("archived row ordering changed")
        row = base.read_row(record["coefficients"], n)
        if not row:
            raise ValueError("old reduced rows must be nonzero")
        key = tuple(sorted(row.items()))
        if key in table.keys:
            raise ValueError("the archived reduced row list has duplicate keys")
        table.keys[key] = index
        table.rows.append(row)
    return table


def append_one_cut(data, budget):
    """Construct only one new static row from the stored normal coefficient forms."""
    n = data["normal_coordinate_count"]
    free = list(data["free_normal_coordinates"])
    if len(set(free)) != len(free) or any(not isinstance(i, int) or not 0 <= i < n for i in free):
        raise ValueError("invalid inherited free-coordinate list")
    dimension = len(free)
    raw_transform = data["normal_coordinates_as_free_linear_forms"]
    if len(raw_transform) != n:
        raise ValueError("inherited x=B*y transform has the wrong length")
    transform = [base.read_row(row, dimension) for row in raw_transform]
    for j, normal_index in enumerate(free):
        if transform[normal_index] != base.unit(j):
            raise ValueError("the inherited free coordinates are not original coordinate variables")
    terms = data["corrected_scalar_k_polynomials"]["F0"]
    if len({p for p, _ in terms}) != len(terms):
        raise ValueError("duplicate stored static polynomial degree")
    static = {}
    for degree, row in terms:
        if not isinstance(degree, int) or degree < 0:
            raise ValueError("static polynomial requires nonnegative integer degrees")
        static[degree] = base.read_row(row, n)
    raw_cut = base.row_add(*((row, CUT_K ** degree) for degree, row in static.items()))
    budget.check(raw_cut)
    reduced_cut = base.substitute(raw_cut, transform)
    budget.check(reduced_cut)
    inherited_rows_digest = sha(canonical(data["reduced_inequalities"]))
    table = inherited_table(data["reduced_inequalities"], dimension, budget)
    old_count = len(table.rows)
    reason = {"kind": "R166_single_candidate_directed_static_cut", "k": str(CUT_K),
              "whole_action_layer": "corrected_F0", "reference": "R166",
              "no_path_integral_is_recomputed": True}
    added_index = table.add(reduced_cut, reason)
    if added_index is None or added_index < old_count:
        raise ValueError("the declared new R166 row is zero or already present")
    point = list(map(F, data["decision"]["outer_candidate"]))
    if len(point) != dimension:
        raise ValueError("inherited exact outer point has the wrong dimension")
    value = base.apply_row(reduced_cut, point)
    if not value < 0:
        raise ValueError("this one directed row does not strictly cut the published candidate")
    if sha(canonical(data["reduced_inequalities"])) != inherited_rows_digest:
        raise AssertionError("reading/continuing the system mutated archived reduced rows")
    inherited = {
        "normal_coordinate_count": n, "external_equality_rank": len(data["rref_equalities"]),
        "free_normal_coordinates": free, "old_reduced_row_count": old_count,
        "old_equality_rows_sha256": sha(canonical(data["equalities"])),
        "old_original_inequality_rows_sha256": sha(canonical(data["inequalities"])),
        "old_rref_sha256": sha(canonical(data["rref_equalities"])),
        "old_transform_sha256": sha(canonical(raw_transform)),
        "old_reduced_rows_sha256": inherited_rows_digest,
        "old_six_path_integrals_sha256": sha(canonical(data["complete_path_integrals"])),
        "old_static_polynomial_forms": deepcopy(terms),
        "old_equalities_or_rows_or_path_integrals_regenerated": False,
    }
    cut = {"static_k": str(CUT_K),
           "normal_coordinate_linear_form": base.serial_row(raw_cut),
           "free_coordinate_linear_form_before_positive_primitive_normalization": base.serial_row(reduced_cut),
           "new_reduced_row_index": added_index,
           "new_reduced_row": deepcopy(table.records[added_index]),
           "parent_saved_outer_candidate_value": str(value),
           "parent_candidate_is_strictly_cut": True,
           "source_static_family": "corrected_scalar_k_polynomials.F0",
           "source_transform": "normal_coordinates_as_free_linear_forms"}
    system = {"reduced": table, "free": free}
    return system, inherited, cut


def actual(args, report, ctx, budget):
    report["phase"] = "read_bound_complete_inherited_system"
    _, data = consume_previous(args, report, budget)
    report["phase"] = "append_exactly_one_published_candidate_directed_static_row"
    system, inherited, cut = append_one_cut(data, budget)
    ctx.update(system=system, inherited=inherited, cut=cut)
    report["inherited_system"] = {k: inherited[k] for k in (
        "normal_coordinate_count", "external_equality_rank", "free_normal_coordinates",
        "old_reduced_row_count", "old_equalities_or_rows_or_path_integrals_regenerated")}
    report["new_cut"] = cut
    report["new_rows_added"] = 1
    report["updated_reduced_rows"] = len(system["reduced"].rows)
    report["phase"] = "new_exact_dual_or_outer_candidate_for_one_cut_continuation"
    print(json.dumps({"phase": report["phase"], "free_coordinates": len(system["free"]),
                      "old_rows": inherited["old_reduced_row_count"],
                      "new_rows": 1, "parent_candidate_cut_value":
                      cut["parent_saved_outer_candidate_value"]}), flush=True)
    decision = base.certify_zero(system, budget)
    ctx["decision"] = decision
    excluded = decision["all_coordinates_forced_zero"]
    report.update(completion="complete", phase="one_static_cut_continuation_complete",
        positive_character_excluded=excluded,
        outcome=("all_nonzero_true_positive_weight_minus2_characters_excluded_by_exact_outer_system"
                 if excluded else "one_static_cut_outer_system_remains_unresolved"))
    report["decision"] = {k: v for k, v in decision.items()
                          if k not in ("certificates", "outer_candidate")}
    report["decision"]["exact_dual_certificates"] = len(decision.get("certificates", []))
    report["decision"]["nonzero_exact_outer_candidate_saved"] = decision.get("outer_candidate") is not None
    report["checkpoint"] = {
        "target_weight": -2, "all_true_positive_characters_embed_in_the_test": True,
        "all_original_generating_coordinates_are_still_covered": True,
        "same_normal_coordinates_and_same_unique_R164_multiplier": True,
        "one_specific_published_outer_point_excluded": True,
        "only_weight_minus2_positive_characters_excluded": excluded,
        "all_positive_characters_excluded": False, "true_character_existence_claimed": False,
        "complete_action_positivity_proved": False, "complete_period_or_ruling_paid": False}


def fake_data():
    # Completely artificial 2-coordinate input, unrelated to the real head.
    return {"normal_coordinate_count": 2, "free_normal_coordinates": [0, 1],
        "normal_coordinates_as_free_linear_forms": [[[0, "1"]], [[1, "1"]]],
        "corrected_scalar_k_polynomials": {"F0": [[0, [[0, "-1"]]], [2, [[1, "-4"]]]]},
        "reduced_inequalities": [
            {"index": 0, "coefficients": [[0, "1"]], "reason": {"kind": "artificial_y0"},
             "additional_reason_count": 0},
            {"index": 1, "coefficients": [[1, "1"]], "reason": {"kind": "artificial_y1"},
             "additional_reason_count": 0}],
        "decision": {"outer_candidate": ["1", "1"]},
        "rref_equalities": [], "equalities": [], "inequalities": [],
        "complete_path_integrals": []}


def toy_only():
    checks = {}
    budget = base.Budget(45, 512)
    forbidden = ("rref", "construct_system", "path_integrals")
    saved = {name: getattr(base, name) for name in forbidden}
    def no_old_work(*_args, **_kwargs):
        raise AssertionError("the one-cut interface tried to regenerate old research")
    try:
        for name in forbidden:
            setattr(base, name, no_old_work)
        data = fake_data()
        digest = sha(canonical(data))
        system, inherited, cut = append_one_cut(data, budget)
        assert cut["normal_coordinate_linear_form"] == [[0, "-1"], [1, "-1"]]
        assert cut["parent_saved_outer_candidate_value"] == "-2"
        checks["only_one_static_evaluation_from_archived_forms"] = True
        assert len(system["reduced"].rows) == 3 and cut["new_reduced_row_index"] == 2
        assert sha(canonical(data)) == digest
        assert system["reduced"].records[:2] == data["reduced_inequalities"]
        checks["old_rows_and_metadata_are_kept_verbatim"] = True
        decision = base.certify_zero(system, budget)
        assert decision["all_coordinates_forced_zero"]
        assert len(decision["certificates"]) == 4
        checks["appended_artificial_cut_can_have_all_coordinate_exact_duals"] = True
        assert inherited["old_equalities_or_rows_or_path_integrals_regenerated"] is False
        checks["no_old_rref_system_or_path_integral_is_called"] = True
        other = fake_data()
        other["corrected_scalar_k_polynomials"]["F0"] = [[0, [[0, "-1"]]]]
        system2, _, _ = append_one_cut(other, budget)
        decision2 = base.certify_zero(system2, budget)
        assert not decision2["all_coordinates_forced_zero"]
        assert decision2["outer_candidate"] is not None
        checks["cutting_one_point_does_not_claim_zero_of_the_whole_outer_cone"] = True
        changed = fake_data()
        changed["normal_coordinates_as_free_linear_forms"][1] = [[0, "1"]]
        try:
            append_one_cut(changed, budget)
        except ValueError:
            checks["changed_archived_free_coordinate_semantics_are_rejected"] = True
        else:
            raise AssertionError("bad free-coordinate map was accepted")
        changed = fake_data()
        changed["decision"]["outer_candidate"] = ["-1", "-1"]
        try:
            append_one_cut(changed, budget)
        except ValueError:
            checks["a_row_not_cutting_the_specific_parent_candidate_is_rejected"] = True
        else:
            raise AssertionError("non-cutting row accepted")
        fake_main = {"schema": base.SCHEMA, "completion": "complete",
            "github_repository": REPOSITORY, "github_run_id": PREVIOUS["run"],
            "github_sha": PREVIOUS["commit"], "source_hashes": {"driver": PREVIOUS["driver"]}}
        raw = b"artificial-main"
        metadata = dict(PREVIOUS["certificate"])
        pub = {"schema": "visible-new-mechanism-actions-v1", "repository": REPOSITORY,
            "run_id": PREVIOUS["run"], "source_commit": PREVIOUS["commit"], "lane": PREVIOUS["lane"],
            "source_files": {"scripts/"+PREVIOUS["driver"]["filename"]:
                {k: PREVIOUS["driver"][k] for k in ("bytes", "sha256")}},
            "outputs": [
                {"path": PREVIOUS["report"]["filename"], "bytes": len(raw), "sha256": sha(raw)},
                {"path": metadata["filename"], "bytes": metadata["stored_bytes"],
                 "sha256": metadata["stored_sha256"], "raw_bytes": metadata["raw_bytes"],
                 "raw_sha256": metadata["raw_sha256"]}]}
        verify_publication(pub, fake_main, raw, metadata)
        pub["outputs"][1]["raw_sha256"] = "0"*64
        try:
            verify_publication(pub, fake_main, raw, metadata)
        except ValueError:
            checks["publication_rejects_changed_complete_parent_certificate"] = True
        else:
            raise AssertionError("mutated inherited raw SHA accepted")
    finally:
        for name, value in saved.items():
            setattr(base, name, value)
    return {"checks": checks, "all_passed": all(checks.values()),
            "artificial_rational_arithmetic_only": True,
            "real_previous_system_or_head_read": False,
            "real_coefficients_or_path_integrals_evaluated": False}


def complete_certificate(report, ctx):
    if "system" not in ctx:
        return None
    return {"schema": SCHEMA+"-certificate", "source_hashes": report["source_hashes"],
        "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
        "input": report.get("input"), "target_weight": -2,
        "inherited_system_identity_and_unchanged_data": ctx["inherited"],
        "one_new_static_cut": ctx["cut"],
        "updated_reduced_inequalities": ctx["system"]["reduced"].records,
        "free_normal_coordinates": ctx["system"]["free"],
        "decision": ctx.get("decision"),
        "all_true_positive_characters_embed_in_this_outer_system": True,
        "old_complete_certificate_is_required_to_interpret_normal_coordinates": True,
        "outer_system_feasibility_does_not_prove_a_true_character": True,
        "old_source_system_or_integrals_recomputed": False}


def write_outputs(args, report, certificate):
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if certificate is not None:
        raw = canonical(certificate)+b"\n"
        packed = gzip.compress(raw, mtime=0)
        if len(packed) > args.max_certificate_bytes:
            raise base.Limit("complete one-cut certificate exceeds its output budget")
        path = args.output.with_name(args.output.stem+"-certificate.json.gz")
        path.write_bytes(packed)
        report["complete_necessary_certificate"] = {
            "filename": path.name, "stored_bytes": len(packed), "stored_sha256": sha(packed),
            "raw_bytes": len(raw), "raw_sha256": sha(raw),
            "contains_inherited_row_binding_new_cut_and_all_exact_dual_multipliers": True}
    raw = canonical(report)+b"\n"
    if len(raw) > args.max_main_bytes:
        raise base.Limit("small one-cut main report exceeds its output budget")
    if len(raw)+len(packed if certificate is not None else b"") > 4800000:
        raise base.Limit("total published one-cut output exceeds 4.8MB")
    args.output.write_bytes(raw)
    return {"output": str(args.output), "completion": report["completion"],
            "bytes": len(raw), "sha256": sha(raw)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    for name in ("source-report", "source-publication", "source-certificate"):
        parser.add_argument("--"+name, type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--rational-bits", type=int, default=16384)
    parser.add_argument("--max-main-bytes", type=int, default=95000)
    parser.add_argument("--max-certificate-bytes", type=int, default=4500000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.rational_bits,
           args.max_main_bytes, args.max_certificate_bytes) <= 0:
        parser.error("positive explicit budgets required")
    if args.max_main_bytes >= 100000 or args.max_main_bytes+args.max_certificate_bytes > 4800000:
        parser.error("small main below100KB and total output at most4.8MB required")
    if not args.toy_only and not all((args.source_report,args.source_publication,args.source_certificate)):
        parser.error("all three published previous files are required")
    if not args.toy_only and (os.environ.get("GITHUB_ACTIONS") != "true"
                              or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        parser.error("all actual one-cut LP research only in this public repository Actions")
    started = time.monotonic()
    budget = base.Budget(args.max_seconds,args.memory_mib,args.rational_bits)
    report = {"schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": {}, "target_weight": -2, "positive_character_excluded": False,
        "complete_action_positivity_proved": False, "true_character_existence_claimed": False,
        "old_equalities_or_rows_or_path_integrals_regenerated": False,
        "forcing_or_original_function_or_old_normal_form_evaluated": False,
        "head_export_read": False, "fixed_new_static_k": str(CUT_K),
        "floating_status_is_never_a_mathematical_certificate": True,
        "limits": {"elapsed_seconds": args.max_seconds, "polled_memory_mib": args.memory_mib,
                   "rational_bit_ceiling": args.rational_bits, "main_bytes": args.max_main_bytes,
                   "certificate_bytes": args.max_certificate_bytes}}
    ctx = {}
    code = 0
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["toy"] = toy_only()
            report.update(completion="toy_passed",phase="new_single_cut_artificial_interfaces_only")
        else:
            actual(args,report,ctx,budget)
    except base.Limit as error:
        code = 2
        report.update(completion="resource_limit", error=str(error))
    except Exception as error:
        code = 1
        report.update(completion="implementation_check_failed",
                      error={"type":type(error).__name__,"message":str(error)})
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    try:
        written = write_outputs(args,report,complete_certificate(report,ctx))
    except base.Limit as error:
        code = 2
        failed = {k: report[k] for k in (
            "schema","phase","github_repository","github_run_id","github_sha","source_hashes",
            "target_weight","elapsed_seconds","peak_rss_mib") if k in report}
        failed.update(completion="output_limit",error=str(error),positive_character_excluded=False,
                      mathematical_exclusion_not_claimed_without_complete_saved_certificate=True)
        if "input" in report:
            failed["input_identity_sha256"] = sha(canonical(report["input"]))
        raw = canonical(failed)+b"\n"
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_bytes(raw)
        written = {"output":str(args.output),"completion":"output_limit","bytes":len(raw),"sha256":sha(raw)}
    print(json.dumps(written),flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())

