#!/usr/bin/env python3
"""One NEW complete natural-flux observation of the static W4 coefficient.

Public Actions only. Read the paid R210 pure coordinates; decode one original
static mixed root and nine already exported R139 mixed roots. Do not rerun the
old pure map, old response producer, rank, profile, forcing, or N contraction.
The frozen R406 total-flux mapper is called exactly once, on the pure-corrected
mixed root. All original integrals retain their original common right anchor.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_weight_zero_natural_flux as flux

paid, head, literal = flux.paid, flux.head, flux.literal
colored, exact, formal = flux.colored, flux.exact, flux.formal
canonical, sha, require = flux.canonical, flux.sha, flux.require
REPOSITORY, TOPIC = flux.REPOSITORY, flux.TOPIC
ENTRY = TOPIC + "/scripts/literature_static_minus4_natural_flux.py"
SCHEMA = "visible-flex-static-minus4-one-natural-flux-v1"
REQUEST_SCHEMA = SCHEMA + "-request"
TRUE_WEIGHT = -4
STATE = (-4, 8, 0, 0)
PARAMETERS = dict(flux.PARAMETERS)
FROZEN_SOURCES = {
    **flux.FROZEN_SOURCES,
    TOPIC + "/scripts/literature_weight_zero_natural_flux.py":
        "be12b9338cf5558eacb4d05b43f201871fae5d4262dd330304eaa56df3c2e12f",
    TOPIC + "/scripts/literature_complete_pure_minus4_projection.py":
        "be5d2ffa861968dddd9db085cfef0ecc06d9c96a6f1ca719905e8544458bc946",
}
PAID = {
    "run": "43688302217", "job": "132733352458",
    "source": "1b032593b46210e7a0599a224d5c2110fe1d1606",
    "lane": "complete_pure_minus4_projection",
    "directory": TOPIC + "/notes/actions-43688302217-1-complete_pure_minus4_projection",
    "receipt": {"bytes": 47378,
        "sha256": "f739e4a0ccdcf5ea102a9deb5794486b8f9f022975764e23fd14b16ec6d722c4"},
    "main": {"filename": "complete-pure-minus4-result.json", "bytes": 53292,
        "sha256": "aeea36d3c46f934ec784460367813ef7902f85f1c3492e575152fd6906e7a76a"},
    "log": {"bytes": 127473,
        "sha256": "0cdf6ffa15b97cf926dad70b869945a782ee153dac317ec080d1b9d15c9030d6"},
    "column_line": {"bytes": 346,
        "sha256": "e4982bcf35410059ff9633a3916d9aade4bb36086a91484cd66ad19b77571b43"},
    "result_line": {"bytes": 924,
        "sha256": "c21550ca39e7decce115eeef63bb661df7de2a9c601a27599a75d60152716880"},
    "status_line": {"bytes": 373,
        "sha256": "f91f9abb0b2761c7c82c8b7d46138313d968250801771717f2bc4b23e8e83566"},
}
R_INPUT = {
    "run": "43654534244", "commit": "1177f251dc3d9455adf88b585e4c0e4bd6f7e69b",
    "lane": "g_translation_successor",
    "schema": "visible-flex-G-translation-successor-original-v1",
    "main": {"filename": "G-fifth-translation.json", "bytes": 24966,
        "sha256": "faf6c2a0019ce614bb8d6f28b049f0a38a6c2f6e2e00930a1beab17e6c86f93e"},
    "receipt": {"filename": "receipt.json", "bytes": 34625,
        "sha256": "e8f37f37ba85f822e6eacc17167fb6941017dc05ec7670b8fafa7b450dc4d24d"},
    "artifact": {"filename": "G-fifth-translation-original-expressions.json.gz",
        "stored_bytes": 76352,
        "stored_sha256": "b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b",
        "raw_bytes": 427950,
        "raw_sha256": "6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4"},
    "driver": {"filename": "literature_G_translation_successor.py", "bytes": 39670,
        "sha256": "a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406"},
}
# These are OLD R139 columns, not positions in the retained forty-column list.
# The complete target is raw coefficient = (1/512) normalized R210 column 4.
RESPONSE = {0: F(4, 512), 1: F(8, 512), 2: F(-24, 512),
            3: F(-1, 512), 8: F(36, 512), 9: F(4, 512),
            12: F(-17, 512), 15: F(1, 512), 17: F(-5, 512)}
GLOBAL_COORDINATES = [[0, "4"], [1, "8"], [2, "-24"], [3, "-1"],
                      [8, "36"], [9, "4"], [12, "-17"], [14, "1"], [16, "-5"]]
R_KEEP = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,
          21,22,23,24,26,27,28,29,30,32,34,35,36,37,41,42,43,44,45,49]
R_DEPENDENCIES_SHA = "866e724012d102537c7ff1da010c5deb5d94d1ab19cffb601552248043f8f0ab"
NORMALIZED_PURE_SHA = "25bd3f9cf5823f1e45b55eb344fdd10c818756e4e9f97192a91484c47ccfed59"


def read_request(path, repository):
    raw = path.read_bytes()
    require(len(raw) < 100000, "small UTF-8 request required")
    item = paid.decode_json(raw)
    require(item.get("schema") == REQUEST_SCHEMA
            and item.get("repository") == REPOSITORY
            and item.get("entry_point") == ENTRY
            and item.get("targets") == ["W4"]
            and item.get("state_h_k_omega_logh") == list(STATE)
            and item.get("true_weight") == TRUE_WEIGHT
            and item.get("parameters") == PARAMETERS,
            "the single-target scope or original resource limits changed")
    bindings = item.get("source_sha256", {})
    require(isinstance(bindings, dict)
            and all(bindings.get(k) == v for k, v in FROZEN_SOURCES.items())
            and ENTRY in bindings,
            "the complete frozen source closure or new entry is unbound")
    identities = {}
    for name, digest in sorted(bindings.items()):
        source = flux.safe_path(repository, name)
        data = source.read_bytes()
        require(sha(data) == digest, "source SHA mismatch: " + name)
        identities[name] = {"bytes": len(data), "sha256": digest}
    require(Path(__file__).resolve() == flux.safe_path(repository, ENTRY),
            "the executed entry is not the bound repository file")
    return {"bytes": len(raw), "sha256": sha(raw)}, identities


def framed_exact(raw, tag, spec):
    found = []
    for number, line in enumerate(raw.decode("utf-8-sig").splitlines(), 1):
        clean = paid.ANSI.sub("", line).lstrip("\ufeff")
        clean = paid.TIME_PREFIX.sub("", clean)
        if not clean.startswith(tag + " "):
            continue
        packed = (clean + "\n").encode("utf-8")
        if len(packed) == spec["bytes"] and sha(packed) == spec["sha256"]:
            found.append((paid.decode_json(clean[len(tag) + 1:]), number))
    require(len(found) == 1, "one exact original " + tag + " frame required")
    return found[0]


def bind_paid_pure(repository, report):
    reader = paid.OriginalJobReader()
    receipt, _ = literal.read_small(
        flux.safe_path(repository, PAID["directory"] + "/receipt.json"), PAID["receipt"])
    require(receipt.get("schema") == "visible-new-mechanism-actions-metadata-only-v2"
            and receipt.get("repository") == REPOSITORY
            and str(receipt.get("run_id")) == PAID["run"]
            and receipt.get("source_commit") == PAID["source"]
            and receipt.get("lane") == PAID["lane"]
            and receipt.get("output_payloads_committed_or_uploaded") is False,
            "paid R210 receipt identity changed")
    paid.output_identity(receipt, PAID["main"]["filename"], PAID["main"], True)
    run = reader.api("/actions/runs/" + PAID["run"])
    job = reader.api("/actions/jobs/" + PAID["job"])
    require(str(run.get("id")) == PAID["run"]
            and run.get("head_sha") == PAID["source"]
            and str(job.get("id")) == PAID["job"]
            and str(job.get("run_id")) == PAID["run"]
            and (not job.get("head_sha") or job["head_sha"] == PAID["source"])
            and run.get("status") == job.get("status") == "completed"
            and run.get("conclusion") == job.get("conclusion") == "success"
            and PAID["lane"] in job.get("name", ""),
            "paid R210 run/job source or completion changed")
    raw, redirects = reader.log(PAID["job"])
    require(len(raw) == PAID["log"]["bytes"] and sha(raw) == PAID["log"]["sha256"],
            "complete original R210 log identity changed")
    result, result_line = framed_exact(raw, "MATHEMATICAL_RESULT", PAID["result_line"])
    column, column_line = framed_exact(raw, "MATHEMATICAL_COLUMN", PAID["column_line"])
    status, status_line = framed_exact(raw, "EXECUTION_STATUS", PAID["status_line"])
    require(result.get("weight") == TRUE_WEIGHT
            and result.get("complete_fourteen_family_pure_image") is True
            and result.get("pure_U_minus4_equals_pure_R_minus4") is True
            and result.get("old_response_order") == R_KEEP
            and result.get("independent_global_columns") == [0,1,2,3,8,9,12,14,16]
            and column.get("global_column") == 44
            and column.get("normalized_original_column") == 4
            and column.get("all_family_aliases") == [[0, list(STATE), "1/512"]]
            and column.get("original_sha256") == NORMALIZED_PURE_SHA
            and column.get("exact_coordinates_in_independent_global_original_columns")
                == GLOBAL_COORDINATES
            and status.get("completion") == "complete"
            and status.get("phase") == "complete_pure_minus4_image_decided",
            "the exact paid W4 pure combination changed")
    # Construct exact Fractions from the already paid strings, without evaluating
    # any old profile, word map, or pure root.
    translated = {R_KEEP[j]: F(c) / 512 for j, c in GLOBAL_COORDINATES}
    require(translated == RESPONSE, "old/global response-index translation changed")
    report["inputs"]["paid_R210_pure"] = {
        **PAID, "original_log_lines": {
            "result": result_line, "column": column_line, "status": status_line},
        "credential_not_forwarded_on_log_redirect": redirects,
        "raw_coefficient_scale": "1/512",
        "complete_old_R139_response_coefficients": flux.coefficient_rows(RESPONSE),
        "normalized_pure_sha256_from_paid_log": NORMALIZED_PURE_SHA,
        "old_pure_or_rank_reexecuted": False,
        "old_main_report_rebuilt": False,
    }


def restore_one_static(ring, repository, report):
    _, data = head.bind_input(
        "static",
        flux.safe_path(repository, TOPIC + "/notes/actions-43645177423-1-local_fourth_quotient"),
        report)
    records = data.get("local_roots") or []
    require(Counter(row["mode"] for row in records) == Counter({-4: 197, -2: 197})
            and data.get("projection") == "derivative weight zero",
            "complete static export scope changed")
    selected = []
    for row in records:
        if row["mode"] != -2:
            continue
        state, jets = head.split_key(row["geometry_key"])
        require(not any(jets), "static source contains a derivative state")
        if tuple(state) == STATE:
            selected.append(row)
    require(len(selected) == 1, "one exact static mixed state required")
    row = selected[0]
    roots = head.subset_decode(ring, data, [row["root"]])
    raw = roots[row["root"]]
    value = flux.prior.blocks.ScalingGrading(ring).project(raw, TRUE_WEIGHT)
    report["necessary_input_restore"]["static"] = {
        "mode": -2, "state_h_k_omega_logh": list(STATE),
        "original_root_name": row["root"],
        "raw_mixed_sha256": ring.digest(raw), "raw_mixed_terms": len(raw.terms),
        "true_weight": TRUE_WEIGHT, "projected_mixed_sha256": ring.digest(value),
        "projected_mixed_terms": len(value.terms),
        "original_N0_included_in_saved_L0": True,
        "Gamma_h_minus4_absent_by_R417": True,
        "Gamma_reference_rebuilt": False,
    }
    return value


def restore_nine_responses(ring, repository, report):
    directory = flux.safe_path(
        repository, TOPIC + "/notes/actions-43654534244-1-g_translation_successor")
    main, raw = literal.read_small(directory / R_INPUT["main"]["filename"], R_INPUT["main"])
    receipt, _ = literal.read_small(directory / "receipt.json", R_INPUT["receipt"])
    checkpoint = main.get("checkpoint") or {}
    metadata = checkpoint.get("portable_new_block_expression_export") or {}
    literal.verify_publication(receipt, main, raw, R_INPUT, metadata)
    upper = checkpoint.get("response_upper_bound") or {}
    require(checkpoint.get("requested_order") == 5
            and checkpoint.get("requested_weight") == TRUE_WEIGHT
            and upper.get("original_columns") == 50
            and upper.get("retained_original_columns") == R_KEEP
            and upper.get("verified_original_dependencies_sha256") == R_DEPENDENCIES_SHA,
            "paid R139 response identity changed")
    data = literal.checked_gzip(directory / metadata["filename"], metadata)
    coverage = data.get("response_coverage") or {}
    require(data.get("schema") == R_INPUT["schema"] + "-original-expressions"
            and data.get("source_hashes") == main.get("source_hashes")
            and str(data.get("github_run_id")) == R_INPUT["run"]
            and data.get("github_sha") == R_INPUT["commit"]
            and data.get("content_scope")
                == "one-translation-target-and-complete-new-response-block"
            and data.get("all_compiled_original_columns_included") is True
            and coverage.get("columns") == 50
            and coverage.get("weight") == TRUE_WEIGHT,
            "the complete original mixed response export changed")
    records = data.get("column_records") or []
    require(len(records) == 50 and [r["index"] for r in records] == list(range(50)),
            "original response indices changed")
    selected = [records[i] for i in sorted(RESPONSE)]
    roots = head.subset_decode(ring, data, [row["roots"]["-2"] for row in selected])
    output, descriptions = {}, []
    for old, row in zip(sorted(RESPONSE), selected):
        label = row["label"]
        index = label["quadratic_index"]
        value = roots[row["roots"]["-2"]]
        require(0 <= index < 8 and label["quadratic_name"] == exact.PARAMETERS[index]
                and label["third_weight"] + flux.prior.blocks.PARAMETER_WEIGHTS[index]
                    == TRUE_WEIGHT
                and ring.digest(value) == row["original_mode_sha256"]["-2"]
                and row["original_mode_sha256"] == label["original_mode_sha256"],
                "original mixed response label/digest changed")
        output[old] = value
        descriptions.append({
            "old_R139_column": old, "root_name": row["roots"]["-2"],
            "quadratic": label["quadratic_name"], "W_index": label["third_index"],
            "mixed_sha256": ring.digest(value), "mixed_terms": len(value.terms),
            "subtracted_coefficient": str(RESPONSE[old]),
        })
    report["inputs"]["R139"] = R_INPUT
    report["necessary_input_restore"]["nine_existing_mixed_responses"] = descriptions
    return output


def public_observation(result):
    item = flux.public_observation("W4_pure_corrected", result)
    item["true_cost_weight"] = TRUE_WEIGHT
    item["observed_functional_weight"] = TRUE_WEIGHT - 2
    item["target_original_U_coefficient"] = "[h^-4 k^8 omega^0 (logh)^0] F0"
    item["same_natural_function_as_W4_by_response_annihilation"] = True
    item["pure_zero_source"] = "paid R210 exact original column 44, scale 1/512"
    item["response_original_roots_recompiled"] = False
    item["Gamma_absence_is_a_proved_coefficient_identity_not_a_dropped_term"] = True
    return item


def actual(repository, report):
    began = time.monotonic()
    bind_paid_pure(repository, report)
    report["paid_log_read_seconds"] = time.monotonic() - began
    budget = literal.Budget(PARAMETERS["max_seconds"], PARAMETERS["memory_mib"],
                            PARAMETERS["integer_bits"])
    limits = exact.Limits(
        seconds=PARAMETERS["max_seconds"], nodes=350000, atoms=100000,
        terms=PARAMETERS["max_terms"], rewrites=PARAMETERS["max_IBP_calls"],
        memory_mib=PARAMETERS["memory_mib"], rational_bits=PARAMETERS["integer_bits"])
    ring = colored.ColoredRing(limits)
    report["phase"] = "decode_one_static_and_nine_existing_mixed_roots"
    report["necessary_input_restore"] = {}
    start = time.monotonic()
    normal = restore_one_static(ring, repository, report)
    responses = restore_nine_responses(ring, repository, report)
    mixed = normal - sum((c * responses[i] for i, c in sorted(RESPONSE.items())),
                         ring.number(0))
    report["necessary_input_restore_seconds"] = time.monotonic() - start
    report["necessary_input_restore"]["corrected_mixed_sha256"] = ring.digest(mixed)
    report["necessary_input_restore"]["corrected_mixed_terms"] = len(mixed.terms)
    budget.check()
    report["phase"] = "one_new_complete_natural_flux"
    mapper = flux.TotalFluxMapper(ring, PARAMETERS)
    start = time.monotonic()
    value = mapper.expression(mixed, true_weight=TRUE_WEIGHT)
    report["new_observation_seconds"] = time.monotonic() - start
    report["observation"] = public_observation(value)
    report["new_mapper_statistics"] = dict(mapper.words.stats)
    report["new_primitive_calls"] = mapper.words.run_primitive_calls
    budget.check()
    report.update(
        completion="complete", phase="one_complete_W4_natural_flux_observed",
        new_total_flux_targets=1, new_profile_evaluations=0,
        new_pure_maps=0, new_self_maps=0, new_rank_experiments=0,
        old_Euler_polynomials_recomputed=0, old_forcing_recompiled=False,
        old_static_mixed_roots_decoded=1, old_mixed_response_roots_decoded=9,
        old_response_producers_reexecuted=0, old_pure_roots_decoded=0,
        old_N0_N2_or_reference_contractions_reexecuted=0,
        new_development_or_old_development_executed=0,
        all_original_N0_and_right_anchor_terms_retained=True,
        universal_Euler_decision_only_when_all_nonlocal_terms_absent=True,
        a1_or_remaining_Q2_character_resolved=False,
        actual_joint_control_claimed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if not (os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("this new observation runs only in public repository Actions")
    repository = Path.cwd().resolve()
    began = time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "bind_sources",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "targets": ["W4"], "inputs": {},
        "scope": "one full natural functional from paid original mixed roots",
        "recomputable_payload_publication_permitted": False,
    }
    code = 0
    try:
        identity, sources = read_request(args.request, repository)
        report["request_identity"], report["source_files"] = identity, sources
        report["source_hashes"] = paid.source_identity()
        report["source_hashes"]["paid_R329_driver"] = report["source_hashes"].pop("driver")
        report["source_hashes"]["frozen_R406_mapper"] = literal.identity(flux.__file__)
        report["source_hashes"]["driver"] = literal.identity(__file__)
        actual(repository, report)
    except (literal.Limit, formal.CompilationBudgetExceeded, MemoryError) as error:
        report.update(completion="resource_limit", error=str(error),
                      partial_is_not_a_universal_decision=True)
        code = 2
    except Exception as error:
        report.update(completion="implementation_check_failed",
                      error={"type": type(error).__name__, "message": str(error)})
        code = 1
    report["elapsed_seconds"] = time.monotonic() - began
    report["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["local_execution_performed"] = False
    body = canonical(report) + b"\n"
    if len(body) > PARAMETERS["max_report_bytes"]:
        report = {
            "schema": SCHEMA, "completion": "complete_formula_output_limit",
            "original_complete_report_bytes": len(body),
            "original_complete_report_sha256": sha(body),
            "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
            "no_universal_decision_claimed_from_truncated_formula": True,
            "recomputable_payload_publication_permitted": False,
        }
        body, code = canonical(report) + b"\n", 2
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(body)
    print("COMPLETE_REPORT " + body.decode().rstrip(), flush=True)
    print(canonical({"bytes": len(body), "sha256": sha(body),
                     "payload_publication_permitted": False}).decode(), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
