#!/usr/bin/env python3
"""Two remaining complete weight-zero pure/self gates, after R316 and R323.

Read the thirteen completed R316 T/Euler columns from its original public job
log in runner memory. Read C4/C6 pure coordinates from the already published
R124 normalized packets. Restore only missing raw mixed inputs, map the TWO
new pure-zero targets, and verify each positive answer on its fresh raw sum.
No old self map, pure evaluation, old rank experiment, or forcing is rerun.
All new development and science execute only in this public repository Actions.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
import os
from pathlib import Path
import re
import resource
import time
import urllib.error
import urllib.parse
import urllib.request

import literature_weight_zero_complete_self as completed

prior, selfmap = completed.prior, completed.selfmap
pure, zero, head, literal = completed.pure, completed.zero, completed.head, completed.literal
colored, exact, formal = completed.colored, completed.exact, completed.formal
canonical, sha = completed.canonical, completed.sha
REPOSITORY, TOPIC = completed.REPOSITORY, completed.TOPIC
SCHEMA = "visible-flex-weight-zero-C4-C6-complete-self-v1"
FROZEN_DRIVER = {
    "filename": "literature_weight_zero_complete_self.py", "bytes": 27626,
    "sha256": "9347caeb4ff7ed54cc88f6c38183d4773d8e12125a5a9631412674550d42b78f",
}
R316 = {
    "run": "43735872441", "job": "132878270740",
    "commit": "ca186db057ed753abe565d0c3c2c8305278b5af7",
    "lane": "weight_zero_complete_self",
    "receipt": {"bytes": 55780,
                "sha256": "8d79ddda157153788ae70bb1cc44d6c64d4672541bb2e66f7cfbaf33f9549701"},
    "main": {"filename": "weight-zero-complete-self.json", "bytes": 61441,
             "sha256": "731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd"},
}
R124 = {
    "run": "43649160345", "commit": "c69562728ce9d0f5115ad2710d45bcff15762693",
    "lane": "constrained_static_m8_tail_quotient",
    "schema": "visible-flex-constrained-static-m8-tail-quotient-v1",
    "driver": {"filename": "literature_constrained_static_m8_tail.py", "bytes": 28580,
               "sha256": "8b075b222a1c8ea5579645905f9f3c3efc57a1b286a393cdcd597f384db50417"},
    "main": {"filename": "constrained-static-m8-tail.json", "bytes": 7892,
             "sha256": "297c6716a7cf23d1c6006a273f251640bc4c0da878da07d68ef981af43ba65b7"},
    "receipt": {"bytes": 32633,
                "sha256": "8b8e3aff681ccbb15a879040d4a69aad94900b00eadae0130571c36b9b18679e"},
    "artifact": {
        "filename": "constrained-static-m8-tail-certificate.json.gz",
        "stored_bytes": 57845,
        "stored_sha256": "022cd4f767d40b5ad21089e4cf88f7f6d4e6e051b7d730c038e87ab0e0961175",
        "raw_bytes": 489034,
        "raw_sha256": "ced7357546b2c85610cf200e961c4e568a7a8f53407bf8da033eee8b9cb86ed7",
    },
}
TARGETS = {
    4: {"state": (0, 4, 0, 0),
        "mixed_sha256": "1d67672bb734f602675f84768b8afd62363d3742ca203ea01b23c9b1f3f0b592",
        "pure_sha256": "5d70abb9d4000f457beb9d5d6d0adbf08f19becb953818f362c62b5c04dbb3e9"},
    6: {"state": (1, 1, 1, 0),
        "mixed_sha256": "5ca598f50107cf8f059608f27694ad87bb5cbd26be152ff18d8d0f2e2a95bc02",
        "pure_sha256": "c074cfef87ff0f7b9435092bfce4615b7de12d2cbe4a0eabcb1a457d17b01044"},
}
TIME_PREFIX = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z\s+")
ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
MAX_LOG_BYTES = 8 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_identity():
    value = completed.source_identity()
    require(value["driver"] == FROZEN_DRIVER, "the published R316 driver changed")
    value["completed_R316_driver"] = value.pop("driver")
    value["driver"] = literal.identity(__file__)
    return value


def no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, "duplicate JSON key in a bound input")
        out[key] = value
    return out


def decode_json(value):
    return json.loads(value, object_pairs_hook=no_duplicates,
                      parse_constant=lambda x: (_ for _ in ()).throw(
                          ValueError("non-finite JSON token in a bound input")))


def output_identity(receipt, name, spec, metadata_only):
    rows = [r for r in receipt.get("outputs", []) if r.get("path") == name]
    require(len(rows) == 1, "one source output identity required")
    found = rows[0]
    wanted = {"bytes": spec["bytes"], "sha256": spec["sha256"],
              "raw_bytes": spec["bytes"], "raw_sha256": spec["sha256"]}
    require(all(found.get(k) == v for k, v in wanted.items()), "source output identity mismatch")
    if metadata_only:
        require(found.get("payload_published") is False, "old output was metadata only")


def source_tree_in_receipt(value, receipt):
    """Check every recorded old source leaf; never run the old producer."""
    count = 0
    if isinstance(value, dict):
        if {"filename", "bytes", "sha256"} <= set(value):
            path = "topics/visible-flex-new-mechanism/scripts/" + value["filename"]
            require(receipt.get("source_files", {}).get(path) ==
                    {k: value[k] for k in ("bytes", "sha256")},
                    "old report source differs from its original receipt: " + value["filename"])
            count += 1
        else:
            for child in value.values():
                count += source_tree_in_receipt(child, receipt)
    elif isinstance(value, list):
        for child in value:
            count += source_tree_in_receipt(child, receipt)
    return count


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class OriginalJobReader:
    """Bound public read only. Never forward the API credential to a log host."""
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN", "")
        require(bool(self.token), "GITHUB_TOKEN is required to read the completed original job")
        self.opener = urllib.request.build_opener(NoRedirect())

    def get(self, url, cap, authenticated):
        parsed = urllib.parse.urlsplit(url)
        require(parsed.scheme == "https" and parsed.hostname and
                not parsed.username and not parsed.password, "invalid HTTPS input URL")
        headers = {"User-Agent": "visible-weight-zero-two-self-input",
                   "Accept-Encoding": "identity"}
        if authenticated:
            require(parsed.hostname == "api.github.com", "API credential host mismatch")
            headers.update({"Authorization": "Bearer " + self.token,
                            "Accept": "application/vnd.github+json",
                            "X-GitHub-Api-Version": "2022-11-28"})
        request = urllib.request.Request(url, headers=headers, method="GET")
        try:
            response = self.opener.open(request, timeout=45)
        except urllib.error.HTTPError as error:
            status = error.code
            if status in (301, 302, 303, 307, 308):
                location = error.headers.get("Location")
                error.close()
                require(bool(location), "old log redirect has no Location")
                return None, urllib.parse.urljoin(url, location)
            error.close()
            raise ValueError("old public input HTTP status " + str(status)) from None
        except (urllib.error.URLError, TimeoutError):
            raise ValueError("old public input read failed; credentials and signed URLs omitted") from None
        with response:
            length = response.headers.get("Content-Length")
            require(not length or not length.isdigit() or int(length) <= cap,
                    "old public input exceeds byte cap")
            data = response.read(cap + 1)
            require(len(data) <= cap, "old public input exceeds byte cap")
            return data, None

    def api(self, suffix):
        raw, redirect = self.get("https://api.github.com/repos/" + REPOSITORY + suffix,
                                 2000000, True)
        require(redirect is None, "metadata unexpectedly redirected")
        return decode_json(raw)

    def log(self, job):
        url = "https://api.github.com/repos/" + REPOSITORY + "/actions/jobs/" + job + "/logs"
        raw, redirect = self.get(url, MAX_LOG_BYTES, True)
        count = 0
        while redirect is not None:
            count += 1
            require(count <= 4, "too many old job-log redirects")
            raw, redirect = self.get(redirect, MAX_LOG_BYTES, False)
        require(raw is not None, "empty original job log")
        return raw, count


def report_from_log(raw, spec=R316["main"], schema=completed.SCHEMA):
    """Recover the ORIGINAL JSON substring, adding only its original LF."""
    matches = []
    for number, line in enumerate(raw.decode("utf-8-sig").splitlines(), 1):
        clean = ANSI.sub("", line).lstrip("\ufeff")
        clean = TIME_PREFIX.sub("", clean)
        if not clean.startswith("COMPLETE_REPORT "):
            continue
        payload = clean[len("COMPLETE_REPORT "):]
        item = decode_json(payload)
        if not isinstance(item, dict) or item.get("schema") != schema or "decision" not in item:
            continue
        original = payload.encode("utf-8") + b"\n"
        require(len(original) == spec["bytes"] and sha(original) == spec["sha256"],
                "the completed R316 main bytes/hash differ from its receipt")
        matches.append((item, number))
    require(len(matches) == 1, "exactly one completed original research report is required")
    return matches[0]


def bind_completed_self(args, report):
    receipt, raw_receipt = literal.read_small(args.completed_self_directory/"receipt.json",
                                            R316["receipt"])
    require(receipt.get("schema") == "visible-new-mechanism-actions-metadata-only-v2"
            and receipt.get("repository") == REPOSITORY
            and str(receipt.get("run_id")) == R316["run"]
            and receipt.get("source_commit") == R316["commit"]
            and receipt.get("lane") == R316["lane"]
            and receipt.get("output_payloads_committed_or_uploaded") is False
            and receipt.get("machine_certificates_saved") is False
            and receipt.get("release_assets_created") is False,
            "R316 original metadata-only identity changed")
    output_identity(receipt, R316["main"]["filename"], R316["main"], True)
    reader = OriginalJobReader()
    run = reader.api("/actions/runs/" + R316["run"])
    job = reader.api("/actions/jobs/" + R316["job"])
    require(str(run.get("id")) == R316["run"] and run.get("head_sha") == R316["commit"]
            and str(job.get("id")) == R316["job"] and str(job.get("run_id")) == R316["run"]
            and (not job.get("head_sha") or job["head_sha"] == R316["commit"])
            and run.get("status") == job.get("status") == "completed"
            and run.get("conclusion") == job.get("conclusion") == "success"
            and R316["lane"] in job.get("name", ""),
            "the completed original R316 run/job identity changed")
    started = time.monotonic()
    log, redirects = reader.log(R316["job"])
    old, line = report_from_log(log)
    require(old.get("completion") == "complete" and old.get("complete_self_gate") is True
            and old.get("github_repository") == REPOSITORY
            and str(old.get("github_run_id")) == R316["run"]
            and old.get("github_sha") == R316["commit"]
            and old.get("source_hashes") == completed.source_identity()
            and old.get("new_complete_self_targets") == 14
            and old.get("decision", {}).get("comparison_self_rank") == 7
            and old.get("decision", {}).get("augmented_self_rank") == 7,
            "the completed full comparison space is not the published R316 one")
    source_count = source_tree_in_receipt(old["source_hashes"], receipt)
    report["inputs"]["completed_R316_self"] = {
        **R316, "source_records_checked": source_count,
        "main_bytes_and_sha_exact_from_original_COMPLETE_REPORT": True,
        "original_log_bytes": len(log), "original_log_sha256": sha(log),
        "original_report_line": line, "redirects_without_authorization": redirects,
        "read_elapsed_seconds": time.monotonic()-started,
        "log_and_old_columns_runner_memory_only": True,
        "old_self_mapping_or_development_reexecuted": False,
    }
    return old


def parse_local_rows(rows, degree, max_order):
    out = {}
    require(isinstance(rows, list), "stored local rows must be a list")
    for row in rows:
        require(isinstance(row, list) and len(row) == 3, "stored local row shape")
        power, orders, raw = row
        require(type(power) is int and power >= 0 and isinstance(orders, list)
                and len(orders) == degree and orders == sorted(orders)
                and all(type(k) is int and 0 <= k <= max_order for k in orders),
                "stored local jet monomial changed")
        key = (power, tuple(orders))
        value = F(raw)
        require(value and key not in out, "duplicate or zero stored local term")
        out[key] = value
    return out


def stored_self_coordinates(column):
    """Read, hash, and deserialize. Do not recompute the old Euler polynomial."""
    matrix = column.get("ordered_matrix_T")
    require(isinstance(matrix, list) and len(matrix) == 3
            and all(isinstance(row, list) and len(row) == 3 for row in matrix),
            "complete old ordered matrix required")
    matrix = [[F(v) for v in row] for row in matrix]
    local = parse_local_rows(column["complete_local_density"], 4, 3)
    euler = parse_local_rows(column["complete_Euler_coefficients"], 3, 6)
    require(sha(canonical(selfmap.local_rows(local))) == column["local_density_sha256"]
            and sha(canonical(selfmap.local_rows(euler))) == column["Euler_sha256"],
            "old complete local/Euler serialized identities changed")
    vector = {}
    for i in range(3):
        for j in range(3):
            if matrix[i][j]:
                require(i+j == 4, "the old matrix entry left true weight zero")
                vector[(0, i, j)] = matrix[i][j]
    for (power, orders), value in euler.items():
        require(power-sum(orders) == -3, "old Euler coefficient true weight changed")
        vector[(1, power, orders)] = value
    require(sha(canonical(selfmap.coordinate_rows(vector))) ==
            column["faithful_coordinate_sha256"], "old full coordinate hash changed")
    require(column.get("whole_word_reconstruction_from_T_and_L_exact_zero") is True
            and column.get("true_cost_weight") == 0 and column.get("observed_self_weight") == -2
            and column.get("original_same_right_anchor_and_nested_increments_retained") is True,
            "stored coordinates lack their complete original conversion")
    return vector


def read_comparison(old, labels, pure_values, report):
    keep = list(zero.R0_KEEP)
    records = old["complete_response_pure_kernel"]["new_kernel_coordinate_columns"]
    columns = old["columns"]
    wanted = [j for j in keep if j not in completed.PURE_BASIS_OLD]
    require(len(records) == 13 and len(columns) == 14 and
            [row["nonpivot_old_column"] for row in records] == wanted,
            "all thirteen old pure-kernel branches are required")
    position = {j: i for i, j in enumerate(keep)}
    vectors, combinations = [], []
    for i, (record, column) in enumerate(zip(records, columns[:13])):
        index = record["nonpivot_old_column"]
        require(column["index"] == i and column["label"].get("nonpivot_R126_old_column") == index
                and column["original_mixed_sha256"] == record["original_mixed_sha256"],
                "old complete self column label/original identity changed")
        combination = {}
        for j, raw in record["original_R126_combination"]:
            require(j in position and j not in combination, "bad old response combination")
            value = F(raw)
            require(bool(value), "zero in stored response combination")
            combination[j] = value
        require(combination.get(index) == 1 and
                set(combination) <= {index, *completed.PURE_BASIS_OLD},
                "the old complete pure-kernel triangular form changed")
        sums = [sum((c*pure_values[position[j]][k] for j, c in combination.items()), F(0))
                for k in range(3)]
        require(not any(sums), "old stored kernel combination does not kill its stored pure coordinates")
        vectors.append(stored_self_coordinates(column))
        combinations.append(combination)
    report["old_comparison_reuse"] = {
        "whole_response_pure_kernel_dimension_from_R196_R201": 13,
        "full_self_rank_from_completed_R316": 7,
        "nonpivot_original_R126_labels": wanted,
        "all_thirteen_faithful_columns_read": True,
        "complete_coordinates_sha256": sha(canonical(
            [selfmap.coordinate_rows(v) for v in vectors])),
        "original_kernel_combinations": [
            [[j, str(c)] for j, c in sorted(row.items())] for row in combinations],
        "old_full_self_maps": 0, "old_Euler_polynomials_recomputed": 0,
        "old_rank_experiment_repeated": False,
        "new_target_solver_will_factor_stored_coordinates_once": True,
    }
    return vectors, combinations


def packet_pure_values(records, targets=TARGETS):
    result, bindings = {}, []
    for index, spec in sorted(targets.items()):
        candidates = []
        for row in records:
            state, jets = head.split_key(row["geometry_key"])
            if tuple(state) == tuple(spec["state"]) and not any(jets):
                candidates.append(row)
        require(len(candidates) <= 1, "duplicate completed normalized static packet")
        row = candidates[0] if candidates else {
            "geometry_key": [spec["state"][0], spec["state"][1], spec["state"][2], 0, 0, 0, 0, spec["state"][3]],
            "complete_polynomial": []}
        polynomial = {}
        for term in row["complete_polynomial"]:
            key = (term["c_power"], term["r_power"])
            require(all(type(v) is int and v >= 0 for v in key) and key not in polynomial,
                    "invalid or duplicate saved polynomial monomial")
            value = F(term["coefficient"])
            require(bool(value), "zero stored polynomial term")
            polynomial[key] = value
        values = [polynomial.get(key, F(0)) for key in prior.PURE_ROWS]
        result[index] = values
        bindings.append({
            "normal_index": index, "family": "F0", "state_key": list(spec["state"]),
            "stored_geometry_key": row["geometry_key"],
            "zero_packet_absent_from_complete_saved_normalized_list": not candidates,
            "complete_stored_polynomial_sha256": sha(canonical(row["complete_polynomial"])),
            "stored_pure_coordinate_values": list(map(str, values)),
        })
    return result, bindings


def bind_target_pure_packets(args, report):
    main, _ = literal.read_small(args.static_pure_directory/R124["main"]["filename"], R124["main"])
    receipt, _ = literal.read_small(args.static_pure_directory/"receipt.json", R124["receipt"])
    require(main.get("schema") == R124["schema"] and main.get("completion") == "complete"
            and str(main.get("github_run_id")) == R124["run"] and main.get("github_sha") == R124["commit"]
            and main.get("source_hashes", {}).get("driver") == R124["driver"]
            and main.get("full_matrix_constraint_and_induced_weight_two_accounted_for") is True
            and main.get("complete_certificate") == R124["artifact"],
            "R124 complete static normalization identity changed")
    require(receipt.get("schema") == "visible-new-mechanism-actions-v1"
            and receipt.get("repository") == REPOSITORY and str(receipt.get("run_id")) == R124["run"]
            and receipt.get("source_commit") == R124["commit"] and receipt.get("lane") == R124["lane"],
            "R124 original publisher identity changed")
    output_identity(receipt, R124["main"]["filename"], R124["main"], False)
    rows = [r for r in receipt.get("outputs", []) if r.get("path") == R124["artifact"]["filename"]]
    expected = {"bytes": R124["artifact"]["stored_bytes"],
                "sha256": R124["artifact"]["stored_sha256"],
                "raw_bytes": R124["artifact"]["raw_bytes"],
                "raw_sha256": R124["artifact"]["raw_sha256"]}
    require(len(rows) == 1 and all(rows[0].get(k) == v for k, v in expected.items()),
            "R124 gzip/raw published identities changed")
    source_tree_in_receipt(main["source_hashes"], receipt)
    data = literal.checked_gzip(args.static_pure_directory/R124["artifact"]["filename"], R124["artifact"])
    require(data.get("schema") == R124["schema"]+"-certificate"
            and data.get("source_hashes") == main["source_hashes"]
            and str(data.get("github_run_id")) == R124["run"] and data.get("github_sha") == R124["commit"],
            "R124 complete packet source changed")
    group = data["groups"]["normalized_static"]
    require(group["summary"]["geometry_derivative_weight"] == 0
            and group["summary"]["all_new_complete_polynomial_identities_verified"] is True,
            "completed normalized F0 packets required")
    values, bindings = packet_pure_values(group["geometry_coefficients"])
    report["inputs"]["C4_C6_stored_pure_packets"] = {
        **R124, "selected_packets": bindings,
        "rows": [list(k) for k in prior.PURE_ROWS],
        "same_Gamma_reference_normalization_as_R196": True,
        "each_row_has_c_plus_r_degree_32_so_selects_true_weight_zero": True,
        "query_faithfulness_only_on_pure_U0_from_R201": True,
        "new_profile_evaluations": 0, "old_pure_word_maps": 0,
    }
    return values


def pure_corrections(target_values, response_values, budget):
    position = {j: i for i, j in enumerate(zero.R0_KEEP)}
    basis = completed.PURE_BASIS_OLD
    matrix = [[response_values[position[j]][k] for j in basis] for k in range(3)]
    result = {}
    for index, values in sorted(target_values.items()):
        coefficient = pure.exact_square_solve(matrix, values, budget)
        result[index] = {j: c for j, c in zip(basis, coefficient) if c}
    return result


def restore_two_targets_and_W(ring, data, labels, report):
    records = data["local_roots"]
    require(Counter(r["mode"] for r in records) == Counter({-4: 197, -2: 197}),
            "complete frozen static source coverage changed")
    rows = [r for r in records if r["mode"] == -2]
    states = []
    for row in rows:
        state, jets = head.split_key(row["geometry_key"])
        require(not any(jets), "static source contains geometry derivatives")
        states.append(state)
    require(len(set(states)) == 197, "duplicate raw static state key")
    coordinates, reference = head.constrained.reference_coordinates()
    weights = pure.combine_normalization_rows(
        rows, states, coordinates, {i: s["state"] for i, s in TARGETS.items()},
        head.constrained.BASIS_STATES)
    needed_W = sorted({r["third_index"] for r in labels})
    names = set().union(*(set(v) for v in weights.values()))
    names.update("W"+str(j) for j in needed_W)
    roots = head.subset_decode(ring, data, names)
    grade = prior.blocks.ScalingGrading(ring)
    result, descriptions = {}, []
    for index, spec in sorted(TARGETS.items()):
        raw = sum((c*roots[name] for name, c in sorted(weights[index].items())), ring.number(0))
        value = grade.project(raw, 0)
        require(ring.digest(value) == spec["mixed_sha256"],
                "C%d differs from its original R196 mixed SHA" % index)
        result[index] = value
        descriptions.append({
            "normal_index": index, "state_key": list(spec["state"]), "mode": -2,
            "original_mode_sha256": ring.digest(value), "original_terms": len(value.terms),
            "raw_static_combination": [[name, str(c)] for name, c in sorted(weights[index].items())],
            "raw_combination_sha256": ring.digest(raw),
        })
    report["two_static_mixed_inputs"] = {
        "records": descriptions, "same_Gamma": True,
        "reference_data_sha256": sha(canonical(reference)),
        "new_needed_original_projection_sums": 2,
        "old_C2_or_other_head_roots_restored": False, "pure_roots_restored": 0,
        "source_of_target_hashes": "R196 original job132712596579, exact25121B main838266c7...",
    }
    return result, {j: roots["W"+str(j)] for j in needed_W}


class StoredComparisonSolver:
    """One necessary factorization of stored columns, reused for both new RHS.

    Rank seven is a published premise. Its check here is an input consistency
    check, not a replacement rank proof or an old scientific target.
    """
    def __init__(self, vectors, budget, expected_rank=7):
        self.vectors, self.budget = vectors, budget
        self.basis, self.independent = {}, []
        for index, vector in enumerate(vectors):
            reduced, combination = pure.reduce_column(vector, index, self.basis, budget)
            if reduced:
                self.basis[min(reduced)] = {"vector": reduced, "combination": combination}
                self.independent.append(index)
        require(len(self.basis) == expected_rank, "stored complete self image no longer has its proved rank")
        self.solves = 0

    def solve(self, target):
        self.solves += 1
        index = len(self.vectors)
        reduced, combination = pure.reduce_column(target, index, self.basis, self.budget)
        if not reduced:
            require(bool(combination.get(index)), "target coefficient lost")
            coefficients = {i: -F(c, combination[index]) for i, c in combination.items()
                            if i != index and c}
            fresh = dict(target)
            for i, coefficient in coefficients.items():
                literal.add_fraction_row(fresh, self.vectors[i], -coefficient)
            require(not fresh, "new target minus stored-coordinate combination is nonzero")
            return {"outcome": "MEMBER", "coefficients": coefficients}
        rows = sorted(list(self.basis) + [min(reduced)])
        independent = self.independent + [index]
        all_vectors = self.vectors + [target]
        matrix = [[all_vectors[i].get(row, F(0)) for row in rows] for i in independent]
        values = [F(i == index) for i in independent]
        solution = pure.exact_square_solve(matrix, values, self.budget)
        dual = {row: c for row, c in zip(rows, solution) if c}
        evaluations = [sum((c*v.get(row, F(0)) for row, c in dual.items()), F(0))
                       for v in all_vectors]
        require(evaluations == [F(0)]*index+[F(1)], "new faithful dual does not kill all stored columns")
        return {"outcome": "NONMEMBER", "dual": dual, "dual_values": evaluations}


def merge_old_coefficients(base, kernel_coefficients, combinations):
    result = dict(base)
    for i, amount in kernel_coefficients.items():
        for j, coefficient in combinations[i].items():
            selfmap.add(result, j, amount*coefficient)
    return result


def actual(args, report):
    budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
    limits = exact.Limits(seconds=args.max_seconds, nodes=350000, atoms=100000,
                          terms=args.max_terms, rewrites=args.max_IBP_calls,
                          memory_mib=args.memory_mib, rational_bits=args.integer_bits)
    report["phase"] = "read_completed_comparison_and_old_pure_packets"
    pure.bind_head_receipt(args.head_directory, report)
    prior.bind_pure_identity(args.pure_identity_directory, report)
    labels = zero.read_R0_definition(args.R0_directory, report)
    response_values = prior.bind_stored_pure_rows(args.stored_pure_directory, labels, report)
    old_report = bind_completed_self(args, report)
    stored_vectors, combinations = read_comparison(old_report, labels, response_values, report)
    target_values = bind_target_pure_packets(args, report)
    corrections = pure_corrections(target_values, response_values, budget)
    report["pure_corrections_from_stored_coordinates"] = [
        {"normal_index": i, "C_pure_equals_old_basis": [[j, str(c)] for j, c in sorted(v.items())],
         "basis_original_R126_labels": list(completed.PURE_BASIS_OLD),
         "universal_identity_uses_R201_dimension_and_R116_three_query_isomorphism": True}
        for i, v in sorted(corrections.items())]
    ring = colored.ColoredRing(limits)
    _, data = head.bind_input("static", args.static_directory, report)
    targets, W = restore_two_targets_and_W(ring, data, labels, report)
    del data
    original = prior.restore_old_mixed(ring, W, labels, budget, report)
    del W
    original = dict(zip(zero.R0_KEEP, original))
    new_mapper = selfmap.SelfMapper(ring, args.max_IBP_calls, args.max_terms, args.max_cache_entries)
    results, raw_targets = {}, {}
    report["phase"] = "two_new_complete_self_targets"
    report["columns"] = []
    for index in sorted(TARGETS):
        value = targets[index] - sum((c*original[j] for j, c in corrections[index].items()), ring.number(0))
        raw_targets[index] = value
        result = new_mapper.expression(value, true_cost_weight=0)
        results[index] = result
        report["columns"].append(completed.public_column(
            index, {"kind": "new_pure_zero_static_target", "R196_normal_index": index}, result))
        report["progress"] = {"new_self_targets_completed": len(results), "required": 2}
        budget.check()
    full = [{"coordinates": v} for v in stored_vectors] + [results[i] for i in sorted(TARGETS)]
    numeric, coordinate_labels = completed.signature_vectors(full)
    solver = StoredComparisonSolver(numeric[:13], budget, expected_rank=7)
    calls = new_mapper.words.run_primitive_calls
    decisions, fresh_proofs = [], []
    position = {j: i for i, j in enumerate(zero.R0_KEEP)}
    nonpivots = report["old_comparison_reuse"]["nonpivot_original_R126_labels"]
    report["phase"] = "two_RHS_on_one_stored_coordinate_factorization"
    for ordinal, index in enumerate(sorted(TARGETS)):
        answer = solver.solve(numeric[13+ordinal])
        record = {"normal_index": index, "outcome": answer["outcome"],
                  "comparison": "complete R^(0) intersect ker universal pure, all13 branches",
                  "comparison_full_self_rank_from_R316": 7,
                  "fresh_target_true_weight": 0, "observed_self_weight": -2,
                  "new_target_coordinate_rows": len(results[index]["coordinates"])}
        if answer["outcome"] == "MEMBER":
            coefficients = answer["coefficients"]
            combined = merge_old_coefficients(corrections[index], coefficients, combinations)
            for k in range(3):
                total = sum((c*response_values[position[j]][k] for j, c in combined.items()), F(0))
                require(total == target_values[index][k], "fresh complete original response combination lost pure identity")
            difference = targets[index] - sum((c*original[j] for j, c in sorted(combined.items())), ring.number(0))
            remaining = args.max_IBP_calls-calls
            if remaining <= 0:
                raise literal.Limit("total new primitive budget before independent raw composite")
            report["phase"] = "fresh_original_C%d_composite" % index
            fresh_mapper = selfmap.SelfMapper(ring, remaining, args.max_terms, args.max_cache_entries)
            fresh = fresh_mapper.expression(difference, true_cost_weight=0)
            calls += fresh_mapper.words.run_primitive_calls
            require(not fresh["coordinates"] and fresh["complete_reconstruction_zero"],
                    "fresh original composite does not have zero complete T/Euler")
            proof = {
                "normal_index": index,
                "original_mixed_difference_sha256": ring.digest(difference),
                "original_mixed_difference_terms": len(difference.terms),
                "global_diagonal_sha256": fresh["global_diagonal_sha256"],
                "whole_word_sha256": fresh["whole_word_sha256"],
                "self_word_sha256": fresh["self_word_sha256"],
                "self_word_terms": len(fresh["self_words"]),
                "self_word_is_literal_zero": not fresh["self_words"],
                "fresh_T_and_complete_Euler_zero": True,
                "whole_word_reconstruction_exact_zero": fresh["complete_reconstruction_zero"],
                "independent_mapper_statistics": dict(fresh_mapper.words.stats),
                "NF_zero_not_an_extra_member_gate": True,
            }
            fresh_proofs.append({**proof, "complete_self_words": selfmap.word_rows(fresh["self_words"]),
                                 "complete_local_density": selfmap.local_rows(fresh["local"])})
            record.update(
                complete_self_kernel_combination=[[nonpivots[i], str(c)] for i, c in sorted(coefficients.items())],
                C_equals_response_after_joint_E_projection=[[j, str(c)] for j, c in sorted(combined.items())],
                joint_zero_representative={
                    "definition": "C%d plus the following complete R126 old responses" % index,
                    "original_R126_coefficients": [[j, str(-c)] for j, c in sorted(combined.items())],
                    "universal_pure_zero": True, "whole_universal_self_zero": True},
                fresh_original_verification=proof)
        else:
            dual = answer["dual"]
            record.update(
                faithful_T_Euler_dual=[[selfmap.coordinate_label(coordinate_labels[row]), str(c)]
                                       for row, c in sorted(dual.items())],
                exact_values_on_thirteen_old_columns_then_this_target=list(map(str, answer["dual_values"])),
                comparison_span_complete_by_R316=True,
                actual_cost_semigroup_obstruction_claimed=False)
        decisions.append(record)
        report["decisions"] = decisions
        budget.check()
    both = all(x["outcome"] == "MEMBER" for x in decisions)
    report["mathematical_consequence"] = {
        "both_remaining_weight_zero_joint_E_gates_paid": both,
        "E_means": "universal pure together with whole universal self",
        "weight_zero_of_EU_mod_ER_vanishes": both,
        "conditional_R323_R206_actual_joint_E_control_now_applicable": both,
        "a_nonmember_does_not_disprove_actual_control": not both,
        "full_canonical_signed_cost_control_or_fixed_circle_joint_range_claimed": False,
    }
    proof = {
        "schema": SCHEMA+"-in-memory-proof", "source_hashes": report["source_hashes"],
        "inputs": report["inputs"], "old_comparison_coordinate_sha256":
            report["old_comparison_reuse"]["complete_coordinates_sha256"],
        "new_columns": report["columns"], "decisions": decisions,
        "fresh_composites": fresh_proofs,
    }
    proof_raw = canonical(proof)
    if len(proof_raw) > args.max_certificate_bytes:
        raise literal.Limit("new in-memory proof byte ceiling")
    report["reproducible_certificate"] = {"bytes": len(proof_raw), "sha256": sha(proof_raw), "persisted": False}
    report.update(
        completion="complete", phase="complete_two_remaining_weight_zero_joint_gates",
        complete_two_target_gate=True, new_complete_self_targets=2,
        old_full_self_columns_read=13, old_full_self_columns_remapped=0,
        old_Euler_polynomials_recomputed=0, stored_coordinate_factorizations_for_new_targets=1,
        new_RHS_solves=solver.solves, total_new_primitive_calls=calls,
        new_target_mapper_statistics=dict(new_mapper.words.stats),
        old_mixed_originals_restored=16, old_static_mixed_roots_restored=2,
        pure_roots_restored=0, new_profile_evaluations=0, new_pure_normalizations=0,
        old_full_head_or_response_rank_experiment_repeated=False,
        old_forcing_recompiled=False, new_N_responses=0,
        literal_monitor_operations=budget.operations,
        literal_monitor_maximum_integer_bits=budget.maximum_bits,
        literal_monitor_is_not_all_DAG_arithmetic=True)


def toy_only(args):
    """Eight new parsing/lookup/two-RHS interfaces, no old scientific input."""
    records = []

    def run(name, function):
        try:
            records.append({"name": name, "passed": True, "details": function()})
        except Exception as error:
            records.append({"name": name, "passed": False,
                            "error": {"type": type(error).__name__, "message": str(error)}})

    def refuses(function):
        try:
            function()
        except (ValueError, AssertionError):
            return True
        return False

    def log_parser():
        example = {"schema": "artificial-only", "completion": "complete",
                   "decision": {"outcome": "MEMBER"}, "text": "original UTF8 α"}
        raw = canonical(example)+b"\n"
        spec = {"bytes": len(raw), "sha256": sha(raw)}
        log = ("\ufeff2026-11-15T00:00:00.000Z setup\n"
               "2026-11-15T00:00:01.000Z COMPLETE_REPORT "+raw.decode()).encode("utf-8")
        found, number = report_from_log(log, spec, "artificial-only")
        assert found == example and number == 2
        assert refuses(lambda: report_from_log(log+b"COMPLETE_REPORT "+raw, spec, "artificial-only"))
        assert refuses(lambda: report_from_log(log.replace(b"MEMBER", b"CHANGED"), spec, "artificial-only"))
        return "BOM/timestamp are removed only from framing; exact original JSON+LF binds; duplicates/tampering reject"

    def stored_coordinate_parser():
        local = {(0, (0, 0, 0, 3)): F(1)}
        euler = {(0, (1, 1, 1)): F(-6), (0, (0, 1, 2)): F(-18)}
        matrix = [[F(0) for _ in range(3)] for _ in range(3)]
        matrix[2][2] = F(5, 7)
        vector = {(0, 2, 2): F(5, 7),
                  (1, 0, (1, 1, 1)): F(-6), (1, 0, (0, 1, 2)): F(-18)}
        item = {
            "ordered_matrix_T": [[str(x) for x in row] for row in matrix],
            "complete_local_density": selfmap.local_rows(local),
            "complete_Euler_coefficients": selfmap.local_rows(euler),
            "local_density_sha256": sha(canonical(selfmap.local_rows(local))),
            "Euler_sha256": sha(canonical(selfmap.local_rows(euler))),
            "faithful_coordinate_sha256": sha(canonical(selfmap.coordinate_rows(vector))),
            "whole_word_reconstruction_from_T_and_L_exact_zero": True,
            "true_cost_weight": 0, "observed_self_weight": -2,
            "original_same_right_anchor_and_nested_increments_retained": True}
        assert stored_self_coordinates(item) == vector
        item["complete_Euler_coefficients"].append(item["complete_Euler_coefficients"][0])
        assert refuses(lambda: stored_self_coordinates(item))
        return "complete T and Euler rows are deserialized/hash-bound without a new Euler evaluation"

    def packet_lookup():
        targets = {4: {"state": (0, 4, 0, 0)}, 6: {"state": (1, 1, 1, 0)}}
        rows = [{"geometry_key": [0, 4, 0, 0, 0, 0, 0, 0],
                 "complete_polynomial": [
                     {"c_power": 0, "r_power": 32, "coefficient": "2/7"},
                     {"c_power": 1, "r_power": 31, "coefficient": "-1/9"},
                     {"c_power": 0, "r_power": 31, "coefficient": "991"}]}]
        values, bindings = packet_pure_values(rows, targets)
        assert values == {4: [F(2, 7), F(-1, 9), F(0)], 6: [F(0)]*3}
        assert bindings[1]["zero_packet_absent_from_complete_saved_normalized_list"]
        assert refuses(lambda: packet_pure_values(rows+rows, targets))
        return "only three stored degree32 coefficients are read; other degree ignored; absent complete zero packet is zero"

    def pure_change_of_coordinates():
        values = [[F(0)]*3 for _ in zero.R0_KEEP]
        position = {j: i for i, j in enumerate(zero.R0_KEEP)}
        for j, coordinate, amount in ((0, 0, 2), (2, 1, 3), (3, 2, 5)):
            values[position[j]][coordinate] = F(amount)
        budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
        targets = {4: [F(1, 3), F(-2, 5), F(7)], 6: [F(0)]*3}
        result = pure_corrections(targets, values, budget)
        assert result == {4: {0: F(1, 6), 2: F(-2, 15), 3: F(7, 5)}, 6: {}}
        return "two RHS use the three published basis positions, preserving R126 old labels"

    def two_RHS_solver():
        budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
        columns = [{7: F(3)}, {1: F(2), 7: F(1)}, {7: F(6)}, {}]
        solver = StoredComparisonSolver(columns, budget, expected_rank=2)
        member = solver.solve({1: F(4), 7: F(5)})
        nonmember = solver.solve({1: F(4), 7: F(5), 9: F(2, 3)})
        assert member["outcome"] == "MEMBER"
        assert member["coefficients"] == {0: F(1), 1: F(2)}
        assert nonmember["outcome"] == "NONMEMBER"
        assert nonmember["dual_values"] == [F(0)]*4+[F(1)]
        assert solver.solves == 2 and len(solver.basis) == 2
        return "one saved-coordinate factorization, nonmonotone pivots, member and faithful all-column nonmember"

    def old_label_composition():
        base = {2: F(1, 3)}
        combinations = [{7: F(1), 0: F(-4, 3)}, {19: F(1), 3: F(-2)}]
        got = merge_old_coefficients(base, {0: F(3), 1: F(-2, 5)}, combinations)
        assert got == {2: F(1, 3), 7: F(3), 0: F(-4), 19: F(-2, 5), 3: F(4, 5)}
        assert base == {2: F(1, 3)}
        return "kernel positions map to original old-column labels; no compact-index substitution or mutation"

    def log_redirect_credentials():
        class Response:
            headers = {"Content-Length": "3"}
            def __enter__(self):
                return self
            def __exit__(self, *unused):
                return False
            def read(self, limit):
                return b"abc"

        class Opener:
            def __init__(self):
                self.requests = []
            def open(self, request, timeout):
                self.requests.append(request)
                if len(self.requests) == 1:
                    raise urllib.error.HTTPError(request.full_url, 302, "Found",
                        {"Location": "https://example.invalid/original-log"}, None)
                return Response()

        reader = OriginalJobReader.__new__(OriginalJobReader)
        reader.token = "artificial-not-a-credential"
        reader.opener = Opener()
        raw, redirects = reader.log("7")
        assert raw == b"abc" and redirects == 1
        headers = [dict((k.lower(), v) for k, v in req.header_items())
                   for req in reader.opener.requests]
        assert "authorization" in headers[0] and "authorization" not in headers[1]
        assert refuses(lambda: reader.get("http://example.invalid/x", 20, False))
        return "new original-log input follows one fake redirect without the API credential; no network"

    def source_metadata_check():
        leaf = {"filename": "artificial.py", "bytes": 3, "sha256": "a"*64}
        receipt = {"source_files": {"topics/visible-flex-new-mechanism/scripts/artificial.py":
                                    {"bytes": 3, "sha256": "a"*64}}}
        assert source_tree_in_receipt({"driver": leaf, "nested": [leaf]}, receipt) == 2
        changed = {"source_files": {"topics/visible-flex-new-mechanism/scripts/artificial.py":
                                    {"bytes": 4, "sha256": "a"*64}}}
        assert refuses(lambda: source_tree_in_receipt({"driver": leaf}, changed))
        return "all old nested source leaves bind to their receipt; mismatch is not silently accepted"

    for name, function in (
        ("original_COMPLETE_REPORT_framing_and_hash", log_parser),
        ("stored_complete_T_Euler_reader", stored_coordinate_parser),
        ("completed_Gamma_packet_three_coordinate_lookup", packet_lookup),
        ("two_new_pure_coordinate_changes", pure_change_of_coordinates),
        ("two_RHS_saved_comparison_solver", two_RHS_solver),
        ("original_R126_label_composition", old_label_composition),
        ("original_job_log_redirect_credential_boundary", log_redirect_credentials),
        ("nested_old_source_receipt_binding", source_metadata_check)):
        run(name, function)
    return {"checks": records, "all_passed": all(r["passed"] for r in records),
            "real_inputs_read": False, "network_used": False,
            "old_development_suites_repeated": False, "scientific_targets_evaluated": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, help="runner-temporary summary; never publish its payload")
    parser.add_argument("--static-directory", type=Path, default=TOPIC/"notes"/head.INPUTS["static"]["directory"])
    parser.add_argument("--R0-directory", type=Path, default=TOPIC/"notes/actions-43649525432-1-g_first_translation")
    parser.add_argument("--head-directory", type=Path, default=TOPIC/"notes/actions-43681388902-1-character_head_zero")
    parser.add_argument("--pure-identity-directory", type=Path, default=TOPIC/"notes/actions-43683171512-1-character_zero_pure_readout")
    parser.add_argument("--stored-pure-directory", type=Path, default=TOPIC/"notes/actions-43646543691-1-full_m8_tail_response_projection")
    parser.add_argument("--static-pure-directory", type=Path, default=TOPIC/"notes/actions-43649160345-1-constrained_static_m8_tail_quotient")
    parser.add_argument("--completed-self-directory", type=Path, default=TOPIC/"notes/actions-43735872441-1-weight_zero_complete_self")
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--integer-bits", type=int, default=8192)
    parser.add_argument("--max-terms", type=int, default=100000)
    parser.add_argument("--max-IBP-calls", type=int, default=300000)
    parser.add_argument("--max-cache-entries", type=int, default=250000)
    parser.add_argument("--max-summary-bytes", type=int, default=95000)
    parser.add_argument("--max-certificate-bytes", type=int, default=4000000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.integer_bits, args.max_terms,
           args.max_IBP_calls, args.max_cache_entries, args.max_certificate_bytes) <= 0:
        parser.error("positive resource ceilings are required")
    if not 20000 <= args.max_summary_bytes < 100000:
        parser.error("summary ceiling must be from20KB to below100KB")
    if not (os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("all NEW development and science run only in public repository Actions")
    started = time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "inputs": {}, "scope": "only the two remaining complete weight-zero pure/self targets",
        "recomputable_payload_publication_permitted": False,
    }
    code = 0
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["development"] = toy_only(args)
            passed = report["development"]["all_passed"]
            report.update(completion="complete" if passed else "new_development_failed",
                          phase="new_two_target_input_and_solver_interfaces_only")
            code = 0 if passed else 1
        else:
            actual(args, report)
    except (literal.Limit, formal.CompilationBudgetExceeded, MemoryError) as error:
        report.update(completion="resource_limit", error=str(error),
                      complete_two_target_gate=False, partial_is_not_a_decision=True)
        code = 2
    except Exception as error:
        report.update(completion="implementation_check_failed",
                      error={"type": type(error).__name__, "message": str(error)},
                      complete_two_target_gate=False)
        code = 1
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    body = canonical(report)+b"\n"
    if len(body) > args.max_summary_bytes:
        report = {
            "schema": SCHEMA, "completion": "summary_output_limit",
            "full_summary_bytes": len(body), "full_summary_sha256": sha(body),
            "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
            "source_hashes": report.get("source_hashes"),
            "complete_two_target_gate": False,
            "no_decision_claimed_from_truncated_output": True}
        body = canonical(report)+b"\n"
        code = 2
    if len(body) > args.max_summary_bytes:
        raise ValueError("even minimal summary exceeds the declared ceiling")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    if report.get("completion") == "complete" and "decisions" in report:
        print("MATHEMATICAL_RESULT "+canonical({
            "decisions": report["decisions"],
            "consequence": report["mathematical_consequence"]}).decode(), flush=True)
        for column in report["columns"]:
            print("NEW_SELF_COLUMN "+canonical(column).decode(), flush=True)
    print("COMPLETE_REPORT "+body.decode().rstrip(), flush=True)
    print(canonical({"summary_bytes": len(body), "summary_sha256": sha(body),
                     "payload_publication_permitted": False}).decode(), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
