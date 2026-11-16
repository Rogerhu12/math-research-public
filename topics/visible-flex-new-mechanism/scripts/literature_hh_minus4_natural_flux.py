#!/usr/bin/env python3
"""Two NEW complete natural-flux observations of weight-minus4 Qhh.

Public Actions only. Read the complete old factor export and paid R210 pure
coordinates. Assemble only the two required complete SELF diagonals, including
both original N0/N2 potential terms. Do not compile old forcing, pure, rank,
profiles, full mixed responses, or the old development suites.
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

import literature_static_minus4_natural_flux as common
import literature_complete_pure_minus6_projection as original_import

flux = common.flux
paid, head, literal = flux.paid, flux.head, flux.literal
colored, exact, formal = flux.colored, flux.exact, flux.formal
blocks = flux.prior.blocks
canonical, sha, require = flux.canonical, flux.sha, flux.require
REPOSITORY, TOPIC = flux.REPOSITORY, flux.TOPIC
ENTRY = TOPIC + "/scripts/literature_hh_minus4_natural_flux.py"
SCHEMA = "visible-flex-hh-minus4-two-natural-flux-v1"
REQUEST_SCHEMA = SCHEMA + "-request"
TRUE_WEIGHT = -4
PARAMETERS = dict(flux.PARAMETERS)
FROZEN_SOURCES = {
    **common.FROZEN_SOURCES,
    TOPIC + "/scripts/literature_static_minus4_natural_flux.py":
        "c734956045b19a324f76397f251385ecc2aeb8daaf8f4aaa1beb8530da859e2b",
    TOPIC + "/scripts/literature_complete_pure_minus6_projection.py":
        "c57776cfc75ed437bf3b7f8cbcae45072b295892ecee6c93c6297519eee22c2e",
}
TARGETS = {
    "hh_k0": {
        "state": (-6, 0, 0, 0), "normalized_column": 60, "global_column": 100,
        "scale": "-1/512",
        "normalized_pure_sha256":
            "c78a807cad73491058fad4fa02d90b6e39cde3b9e67956dffba5746822adc54d",
        "coordinates": [[1,"-24"],[2,"-56"],[3,"-8"],[8,"40"],[9,"8"],
                        [12,"-14"],[14,"10"],[16,"-10"]],
        "column_line": {"bytes": 345,
            "sha256": "925fb9b481effb95b2ce71bfd50ecf1f2b308d5a2aa80f1c12fa364f6877178e"},
    },
    "hh_k6": {
        "state": (-6, 6, 0, 0), "normalized_column": 63, "global_column": 103,
        "scale": "-5/512",
        "normalized_pure_sha256":
            "ded90de054ec9adad817d6c189b0c0247a53aee3210884e143e9d3fbacdd38ea",
        "coordinates": [[0,"4"],[1,"12/5"],[2,"-156/5"],[3,"-12/5"],
                        [8,"192/5"],[9,"36/5"],[12,"-78/5"],
                        [14,"23/5"],[16,"-32/5"]],
        "column_line": {"bytes": 372,
            "sha256": "04c01596d395d85a8614341f28533f655971f11c38641cc325470e21d5a92c00"},
    },
}
RESPONSE = {
    name: {common.R_KEEP[i]: F(spec["scale"]) * F(value)
           for i, value in spec["coordinates"]}
    for name, spec in TARGETS.items()
}
RESPONSE_INDICES = sorted(set().union(*(set(row) for row in RESPONSE.values())))
TARGET_BY_STATE = {spec["state"]: name for name, spec in TARGETS.items()}
FACTOR_DIRECTORY = TOPIC + "/notes/actions-43651096112-1-local_fourth_derivative_factors"
QUADRATIC_VELOCITY = (2, 0, 0, 0, 0, 0)
H_ACCELERATION = (0, 0, 1, 0, 0, 0)
FAMILY_ORDER = ["F0","Q2_0","Q2_1","Q2_2","A_hh","A_hk","A_kk",
                "H1","H2","Q4_0","Q4_1","Q4_2","Q4_3","Q4_4"]


def read_request(path, repository):
    raw = path.read_bytes()
    require(len(raw) < 100000, "small UTF-8 request required")
    item = paid.decode_json(raw)
    require(item.get("schema") == REQUEST_SCHEMA
            and item.get("repository") == REPOSITORY
            and item.get("entry_point") == ENTRY
            and item.get("targets") == list(TARGETS)
            and item.get("target_states") ==
                {name: list(spec["state"]) for name, spec in TARGETS.items()}
            and item.get("true_weight") == TRUE_WEIGHT
            and item.get("parameters") == PARAMETERS,
            "the two-target scope or original limits changed")
    bindings = item.get("source_sha256", {})
    require(isinstance(bindings, dict)
            and all(bindings.get(k) == v for k, v in FROZEN_SOURCES.items())
            and ENTRY in bindings,
            "complete frozen source closure or new entry is unbound")
    identities = {}
    for name, digest in sorted(bindings.items()):
        data = flux.safe_path(repository, name).read_bytes()
        require(sha(data) == digest, "source SHA mismatch: " + name)
        identities[name] = {"bytes": len(data), "sha256": digest}
    require(Path(__file__).resolve() == flux.safe_path(repository, ENTRY),
            "executed entry is not the bound repository file")
    return {"bytes": len(raw), "sha256": sha(raw)}, identities


def bind_paid_pure(repository, report):
    """Read TWO old column receipts; do not recompute any old pure map."""
    spec = common.PAID
    reader = paid.OriginalJobReader()
    receipt, _ = literal.read_small(
        flux.safe_path(repository, spec["directory"] + "/receipt.json"), spec["receipt"])
    require(receipt.get("schema") == "visible-new-mechanism-actions-metadata-only-v2"
            and receipt.get("repository") == REPOSITORY
            and str(receipt.get("run_id")) == spec["run"]
            and receipt.get("source_commit") == spec["source"]
            and receipt.get("lane") == spec["lane"]
            and receipt.get("output_payloads_committed_or_uploaded") is False,
            "paid R210 receipt identity changed")
    paid.output_identity(receipt, spec["main"]["filename"], spec["main"], True)
    run = reader.api("/actions/runs/" + spec["run"])
    job = reader.api("/actions/jobs/" + spec["job"])
    require(str(run.get("id")) == spec["run"]
            and run.get("head_sha") == spec["source"]
            and str(job.get("id")) == spec["job"]
            and str(job.get("run_id")) == spec["run"]
            and (not job.get("head_sha") or job["head_sha"] == spec["source"])
            and run.get("status") == job.get("status") == "completed"
            and run.get("conclusion") == job.get("conclusion") == "success"
            and spec["lane"] in job.get("name", ""),
            "paid R210 run/job source or completion changed")
    raw, redirects = reader.log(spec["job"])
    require(len(raw) == spec["log"]["bytes"] and sha(raw) == spec["log"]["sha256"],
            "complete original R210 log identity changed")
    result, result_line = common.framed_exact(raw, "MATHEMATICAL_RESULT", spec["result_line"])
    status, status_line = common.framed_exact(raw, "EXECUTION_STATUS", spec["status_line"])
    require(result.get("weight") == TRUE_WEIGHT
            and result.get("complete_fourteen_family_pure_image") is True
            and result.get("family_order") == FAMILY_ORDER
            and result.get("pure_U_minus4_equals_pure_R_minus4") is True
            and result.get("old_response_order") == common.R_KEEP
            and result.get("independent_global_columns") == [0,1,2,3,8,9,12,14,16]
            and status.get("completion") == "complete"
            and status.get("phase") == "complete_pure_minus4_image_decided",
            "paid complete pure theorem or original response order changed")
    columns = {}
    for name, target in TARGETS.items():
        column, line = common.framed_exact(raw, "MATHEMATICAL_COLUMN", target["column_line"])
        require(column.get("global_column") == target["global_column"]
                and column.get("normalized_original_column") == target["normalized_column"]
                and column.get("all_family_aliases") ==
                    [[3, list(target["state"]), target["scale"]]]
                and column.get("original_sha256") == target["normalized_pure_sha256"]
                and column.get("exact_coordinates_in_independent_global_original_columns")
                    == target["coordinates"],
                "the exact paid pure coordinate row changed: " + name)
        columns[name] = {
            **target, "original_log_line": line,
            "complete_old_R139_response_coefficients": flux.coefficient_rows(RESPONSE[name]),
        }
    report["inputs"]["paid_R210_pure"] = {
        "run": spec["run"], "job": spec["job"], "source": spec["source"],
        "receipt": spec["receipt"], "main": spec["main"], "log": spec["log"],
        "result_line": spec["result_line"], "status_line": spec["status_line"],
        "original_result_log_line": result_line, "original_status_log_line": status_line,
        "credential_not_forwarded_on_log_redirect": redirects, "columns": columns,
        "old_pure_or_rank_reexecuted": False, "old_main_report_rebuilt": False,
    }


def restore_responses(ring, repository, report):
    """The SAME nine saved R139 mixed roots, each decoded once."""
    spec = common.R_INPUT
    directory = flux.safe_path(
        repository, TOPIC + "/notes/actions-43654534244-1-g_translation_successor")
    main, raw = literal.read_small(directory / spec["main"]["filename"], spec["main"])
    receipt, _ = literal.read_small(directory / "receipt.json", spec["receipt"])
    checkpoint = main.get("checkpoint") or {}
    metadata = checkpoint.get("portable_new_block_expression_export") or {}
    literal.verify_publication(receipt, main, raw, spec, metadata)
    upper = checkpoint.get("response_upper_bound") or {}
    require(checkpoint.get("requested_order") == 5
            and checkpoint.get("requested_weight") == TRUE_WEIGHT
            and upper.get("original_columns") == 50
            and upper.get("retained_original_columns") == common.R_KEEP
            and upper.get("verified_original_dependencies_sha256") == common.R_DEPENDENCIES_SHA,
            "paid R139 response identity changed")
    data = literal.checked_gzip(directory / metadata["filename"], metadata)
    coverage = data.get("response_coverage") or {}
    require(data.get("schema") == spec["schema"] + "-original-expressions"
            and data.get("source_hashes") == main.get("source_hashes")
            and str(data.get("github_run_id")) == spec["run"]
            and data.get("github_sha") == spec["commit"]
            and data.get("content_scope") == "one-translation-target-and-complete-new-response-block"
            and data.get("all_compiled_original_columns_included") is True
            and coverage.get("columns") == 50 and coverage.get("weight") == TRUE_WEIGHT,
            "complete original mixed response export changed")
    records = data.get("column_records") or []
    require(len(records) == 50 and [row["index"] for row in records] == list(range(50))
            and RESPONSE_INDICES == [0,1,2,3,8,9,12,15,17],
            "original response indices changed")
    selected = [records[i] for i in RESPONSE_INDICES]
    roots = original_import.subset_decode(
        ring, data, [row["roots"]["-2"] for row in selected], {"q", "qbar"},
        report, "nine-paid-R139-mixed-roots")
    answer, descriptions = {}, []
    for old, row in zip(RESPONSE_INDICES, selected):
        label, value = row["label"], roots[row["roots"]["-2"]]
        a = label["quadratic_index"]
        require(0 <= a < 8 and label["quadratic_name"] == exact.PARAMETERS[a]
                and label["third_weight"] + blocks.PARAMETER_WEIGHTS[a] == TRUE_WEIGHT
                and ring.digest(value) == row["original_mode_sha256"]["-2"]
                and row["original_mode_sha256"] == label["original_mode_sha256"],
                "original mixed response label/digest changed")
        answer[old] = ring.substitute(value, {"qbar": ring.color("q")})
        descriptions.append({
            "old_R139_column": old, "root_name": row["roots"]["-2"],
            "quadratic": label["quadratic_name"], "W_index": label["third_index"],
            "mixed_sha256": ring.digest(value), "mixed_terms": len(value.terms),
            "self_mode_minus2_diagonal_sha256": ring.digest(answer[old]),
            "subtracted_coefficients_by_target":
                {name: str(row.get(old, F(0))) for name, row in RESPONSE.items()},
        })
    report["inputs"]["R139"] = spec
    report["necessary_input_restore"]["nine_saved_response_roots"] = descriptions
    return answer


def h_derivative_state(state):
    """Exact X=d/dh, including a possible original log h coefficient."""
    h, k, omega, logh = state
    if h:
        yield (h-1, k, omega, logh), F(h)
    if logh:
        yield (h-1, k, omega, logh-1), F(logh)


def select_two_targets(data, report):
    require(data.get("geometry_names") == list(head.layer.factors.GEOMETRY_NAMES)
            and data.get("real_s_derivatives_before_history_zero") is True
            and data.get("potential_two_assumed_in_W") is False
            and data.get("potential_definition") ==
                "unreduced P_acc+P_h+R79 endpoint_potential, fixed base (1,1,1)"
            and data.get("complete_L2_formula") == "v2 - B_m0(N2) - B_m2(N0)"
            and data.get("phase") ==
                "original complete minus-four and minus-two coefficients; no additional division",
            "complete original N/v2/right-anchor semantics changed")
    potential = data.get("potential_records") or []
    generators = data.get("local_generator_records") or []
    require(Counter(row["geometry_derivative_weight"] for row in potential)
                == Counter({0:79, 2:93})
            and Counter((row["mode"], row["geometry_derivative_weight"])
                        for row in generators)
                == Counter({(-4,2):665, (-2,2):665, (-4,4):1236, (-2,4):1236}),
            "the complete original factor inventory changed")
    matrix = head.read_matrix(data)
    # Gamma(m2), and N0 reference-subtraction times m2, are both supported on
    # these SAME scalar m2 monomials. The target h^-6 cannot occur. This is an
    # exact support statement, not a compactness assumption on N0.
    m2_states = sorted(set(state for coordinate in matrix[2]
                           for state, velocity in coordinate))
    require(m2_states and all(state[0] >= -4 for state in m2_states),
            "Gamma/reference absence at h^-6 is no longer justified")
    raw_uses, potential_uses = [], []
    seen = set()
    for row in generators:
        token = (row["mode"], row["geometry_derivative_weight"], tuple(row["geometry_key"]))
        require(token not in seen, "duplicate raw v2/v4 geometric coefficient")
        seen.add(token)
        if row["mode"] != -2 or row["geometry_derivative_weight"] != 2:
            continue
        state, jets = head.split_key(row["geometry_key"])
        destinations = []
        if jets == QUADRATIC_VELOCITY:
            destinations = [(state, F(1), "raw_gamma_squared")]
        elif jets == H_ACCELERATION:
            destinations = [(s, -c, "minus_X_raw_alpha") for s, c in h_derivative_state(state)]
        for destination, coefficient, role in destinations:
            if destination in TARGET_BY_STATE and coefficient:
                raw_uses.append({
                    "target": TARGET_BY_STATE[destination], "root": row["root"],
                    "geometry_key": row["geometry_key"], "role": role,
                    "coefficient": str(coefficient),
                })
    seen = set()
    for row in potential:
        dw = row["geometry_derivative_weight"]
        state, jets = head.split_key(row["geometry_key"])
        token = (dw, tuple(row["geometry_key"]))
        require(token not in seen and not any(jets[2:]) and sum(jets[:2]) == dw,
                "potential derivative support or uniqueness changed")
        seen.add(token)
        mw = 2-dw
        for a, coordinate in enumerate(matrix[mw]):
            for (mstate, mvelocity), coefficient in coordinate.items():
                velocity = tuple(x+y for x, y in zip(jets[:2], mvelocity))
                if velocity != (2, 0):
                    continue
                destination = tuple(x+y for x, y in zip(state, mstate))
                if destination not in TARGET_BY_STATE or not coefficient:
                    continue
                # On qbar=q, the literal R78 formula is
                # B_E(N)_{-2}=-N(Phi_E(q,q);q,q)/2.
                # Therefore the NORMAL minus B term contributes PLUS one half.
                potential_uses.append({
                    "target": TARGET_BY_STATE[destination], "root": row["root"],
                    "potential_derivative_weight": dw,
                    "geometry_key": row["geometry_key"],
                    "matrix_derivative_weight": mw, "matrix_state": list(mstate),
                    "matrix_velocity": list(mvelocity), "parameter_index": a,
                    "parameter_name": exact.PARAMETERS[a],
                    "required_third_weight": TRUE_WEIGHT-blocks.PARAMETER_WEIGHTS[a],
                    "matrix_coefficient": str(coefficient),
                    "mode_minus2_self_coefficient": str(coefficient/2),
                })
    raw_uses.sort(key=lambda row: (row["target"], row["root"], row["role"]))
    potential_uses.sort(key=lambda row: (
        row["target"], row["root"], row["parameter_index"], row["matrix_state"]))
    selected = sorted({row["root"] for row in raw_uses + potential_uses})
    require(selected and {row["target"] for row in raw_uses} == set(TARGETS),
            "two declared raw hh inputs must be present")
    plan = {
        "selected_raw_generator_uses": raw_uses,
        "selected_potential_matrix_uses": potential_uses,
        "selected_original_roots": [
            {"root": name, "sha256": data["original_root_sha256"][name]} for name in selected],
        "all_m2_scalar_states": [list(s) for s in m2_states],
        "Gamma_m2_and_N0_reference_h_minus6_absent_by_exact_scalar_support": True,
        "other_local_or_potential_roots_not_decoded": True,
        "complete_raw_and_both_potential_terms_retained": True,
        "no_natural_CA_N2_cancellation_used_to_delete_raw_terms": True,
    }
    report["necessary_input_restore"]["target_plan"] = plan
    report["necessary_input_restore"]["target_plan_sha256"] = sha(canonical(plan))
    return raw_uses, potential_uses, selected


def check_quartic(ring, grade, value, label):
    require(not (ring.color_degrees(value)-{(("q",4),)})
            and all(grade.monomial(m) == TRUE_WEIGHT for m in value.terms),
            "wrong complete self degree/true weight: " + label)


def assemble_complete_self(ring, repository, report):
    """Only the two original normal self diagonals; no full mixed compiler."""
    _, data = head.bind_input("factors", flux.safe_path(repository, FACTOR_DIRECTORY), report)
    raw_uses, potential_uses, selected = select_two_targets(data, report)
    decoded = original_import.subset_decode(
        ring, data, selected, {"a","b","c","q","qbar"}, report,
        "two-hh-original-v2-N0-N2-dependency-closure")
    grade, q = blocks.ScalingGrading(ring), ring.color("q")
    answer = {name: ring.number(0) for name in TARGETS}
    raw_cache, projected_cache, contraction_cache, quadratic_cache = {}, {}, {}, {}
    descriptions = []
    for row in raw_uses:
        name = row["root"]
        if name not in raw_cache:
            value = grade.project(decoded[name], TRUE_WEIGHT)
            raw_cache[name] = ring.substitute(value, {"qbar": q})
            check_quartic(ring, grade, raw_cache[name], name)
            descriptions.append({
                "root": name, "kind": "saved_raw_mixed_self_diagonal",
                "original_sha256": data["original_root_sha256"][name],
                "original_terms": len(decoded[name].terms),
                "projected_mixed_sha256": ring.digest(value),
                "self_mode_minus2_sha256": ring.digest(raw_cache[name]),
                "self_mode_minus2_terms": len(raw_cache[name].terms),
            })
        answer[row["target"]] += F(row["coefficient"]) * raw_cache[name]
    quadratics = exact.operator_basis(ring)
    contraction_records = []
    for row in potential_uses:
        root, a = row["root"], row["parameter_index"]
        wanted = row["required_third_weight"]
        token = (root, wanted)
        if token not in projected_cache:
            require(not (ring.color_degrees(decoded[root]) -
                         {(("a",1),("b",1),("c",1))}),
                    "original potential lost exterior/inner colors")
            projected_cache[token] = grade.project(decoded[root], wanted)
        typed = projected_cache[token]
        key = (ring.digest(typed), a)
        if key not in contraction_cache:
            if a not in quadratic_cache:
                quadratic_cache[a] = quadratics[a](q, q)
            # This is the NEW necessary self-slot contraction. The actual outer
            # quadratic has its original left tail; substitute() keeps every I.
            full = ring.substitute(
                typed, {"a": quadratic_cache[a], "b": q, "c": q})
            check_quartic(ring, grade, full, root + ":outer-" + str(a))
            contraction_cache[key] = full
            contraction_records.append({
                "potential_root": root, "original_sha256": data["original_root_sha256"][root],
                "required_third_weight": wanted,
                "projected_typed_sha256": key[0], "projected_typed_terms": len(typed.terms),
                "parameter_index": a, "parameter_name": exact.PARAMETERS[a],
                "outer_quadratic_sha256": ring.digest(quadratic_cache[a]),
                "new_complete_self_slot_sha256": ring.digest(full),
                "new_complete_self_slot_terms": len(full.terms),
                "original_all_right_integrals_preserved": True,
                "noncompact_outer_quadratic_left_tail_retained": True,
            })
        answer[row["target"]] += F(row["mode_minus2_self_coefficient"]) * contraction_cache[key]
    for name, value in answer.items():
        check_quartic(ring, grade, value, name)
    report["necessary_input_restore"]["raw_diagonal_identities"] = descriptions
    report["new_required_self_contractions"] = contraction_records
    report["new_required_self_contraction_count"] = len(contraction_cache)
    report["necessary_typed_input_projection_count"] = len(projected_cache)
    report["raw_mixed_factor_roots_decoded"] = len(raw_cache)
    report["typed_potential_roots_decoded"] = len({r["root"] for r in potential_uses})
    report["complete_self_before_paid_response"] = {
        name: {"mode_minus2_diagonal_sha256": ring.digest(value),
               "mode_minus2_diagonal_terms": len(value.terms)}
        for name, value in answer.items()}
    return answer, grade


def public_observation(name, result):
    item = flux.public_observation(name, result)
    item["true_cost_weight"] = TRUE_WEIGHT
    item["observed_functional_weight"] = TRUE_WEIGHT-2
    item["target_original_U_coefficient"] = (
        "[h^-6 k^" + str(TARGETS[name]["state"][1]) +
        " omega^0 (logh)^0] Qhat_hh")
    item["original_complete_mixed_function_recompiled"] = False
    item["complete_mode_minus2_self_diagonal_assembled"] = True
    item["self_representative_sha256"] = item.pop("original_mixed_sha256")
    item["self_representative_terms"] = item.pop("original_mixed_terms")
    item["pure_zero_source"] = {
        "paid_R210_global_column": TARGETS[name]["global_column"],
        "scale": TARGETS[name]["scale"]}
    item["same_natural_function_as_original_target_by_response_annihilation"] = True
    item["no_natural_identity_used_to_drop_a_raw_self_or_pure_term"] = True
    return item


def actual(repository, report):
    started = time.monotonic()
    bind_paid_pure(repository, report)
    report["paid_log_read_seconds"] = time.monotonic()-started
    budget = literal.Budget(PARAMETERS["max_seconds"], PARAMETERS["memory_mib"],
                            PARAMETERS["integer_bits"])
    limits = exact.Limits(
        seconds=PARAMETERS["max_seconds"], nodes=350000, atoms=100000,
        terms=PARAMETERS["max_terms"], rewrites=PARAMETERS["max_IBP_calls"],
        memory_mib=PARAMETERS["memory_mib"], rational_bits=PARAMETERS["integer_bits"])
    ring = colored.ColoredRing(limits)
    report["necessary_input_restore"] = {}
    report["phase"] = "necessary_two_complete_self_assemblies_from_original_factors"
    began = time.monotonic()
    normal, grade = assemble_complete_self(ring, repository, report)
    responses = restore_responses(ring, repository, report)
    corrected = {}
    for name, value in normal.items():
        corrected[name] = value - sum(
            (amount*responses[old] for old, amount in RESPONSE[name].items()),
            ring.number(0))
        check_quartic(ring, grade, corrected[name], name + ":paid-pure-corrected")
    report["necessary_input_and_new_self_assembly_seconds"] = time.monotonic()-began
    report["complete_self_after_paid_response"] = {
        name: {"mode_minus2_diagonal_sha256": ring.digest(value),
               "mode_minus2_diagonal_terms": len(value.terms)}
        for name, value in corrected.items()}
    budget.check()
    mapper = flux.TotalFluxMapper(ring, PARAMETERS)
    report["observations"] = []
    began = time.monotonic()
    for name in TARGETS:
        report["phase"] = "new_complete_natural_flux_" + name
        result = mapper.expression(corrected[name], true_weight=TRUE_WEIGHT)
        report["observations"].append(public_observation(name, result))
        budget.check()
    report["new_total_flux_mapping_seconds"] = time.monotonic()-began
    report["new_mapper_statistics"] = dict(mapper.words.stats)
    report["new_primitive_calls"] = mapper.words.run_primitive_calls
    report.update(
        completion="complete", phase="two_complete_hh_minus4_natural_functions_observed",
        new_total_flux_targets=2, new_complete_self_assemblies=2,
        new_profile_evaluations=0, new_pure_maps=0, new_rank_experiments=0,
        old_Euler_polynomials_recomputed=0, old_forcing_recompiled=False,
        old_N0_N2_producers_reexecuted=False, old_response_producers_reexecuted=0,
        old_mixed_response_roots_decoded=9, old_pure_roots_decoded=0,
        old_normal_family_or_full_mixed_target_recompiled=False,
        new_development_or_old_development_executed=0,
        original_all_N0_N2_right_anchor_and_left_tail_terms_retained=True,
        universal_Euler_decision_only_when_all_nonlocal_terms_absent=True,
        remaining_minus4_Q2_character_or_actual_joint_resolved=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if not (os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("this new observation runs only in public repository Actions")
    repository, began = Path.cwd().resolve(), time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "bind_sources",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "targets": list(TARGETS), "inputs": {},
        "scope": "two new complete natural functions; only their necessary full self contractions",
        "recomputable_payload_publication_permitted": False,
    }
    code = 0
    try:
        identity, sources = read_request(args.request, repository)
        report["request_identity"], report["source_files"] = identity, sources
        report["source_hashes"] = paid.source_identity()
        report["source_hashes"]["paid_R329_driver"] = report["source_hashes"].pop("driver")
        report["source_hashes"]["frozen_R406_mapper"] = literal.identity(flux.__file__)
        report["source_hashes"]["original_selected_DAG_reader"] = literal.identity(original_import.__file__)
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
    report["elapsed_seconds"] = time.monotonic()-began
    report["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["local_execution_performed"] = False
    body = canonical(report)+b"\n"
    if len(body) > PARAMETERS["max_report_bytes"]:
        report = {
            "schema": SCHEMA, "completion": "complete_formula_output_limit",
            "original_complete_report_bytes": len(body),
            "original_complete_report_sha256": sha(body),
            "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
            "no_universal_decision_claimed_from_truncated_formula": True,
            "recomputable_payload_publication_permitted": False,
        }
        body, code = canonical(report)+b"\n", 2
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(body)
    print("COMPLETE_REPORT " + body.decode().rstrip(), flush=True)
    print(canonical({"bytes": len(body), "sha256": sha(body),
                     "payload_publication_permitted": False}).decode(), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
