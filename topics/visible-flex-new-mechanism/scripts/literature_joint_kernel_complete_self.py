#!/usr/bin/env python3
"""R443: new complete self-current image of the 53 paid Q/current relations.

The old 18 operators and 85/53 exact relations are READ from the original
successful Actions stdout. No old Q/current map, rank, or check is executed.
Only a reviewed public Actions caller may execute this new observation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
ENTRY = TOPIC + "/scripts/literature_joint_kernel_complete_self.py"
DESIGN = TOPIC + "/notes/joint-kernel-complete-self-design-20261116.md"
WORKFLOW = ".github/workflows/visible-joint-kernel-complete-self.yml"
SCHEMA = "visible-flex-joint-kernel-complete-self-v1"
PAID = {
    "run_id": 43796872698, "job_id": 133067569306,
    "source_commit": "563defb46bc785295265c3f48fcad3fc8897c617",
    "log_bytes": 1322512,
    "log_sha256": "1edd4dd8ac34e2a9fe6fc1cf7ae08dc2d91fa279c02e6c32365bff9830e013b1",
    "records": 1020, "record_file_bytes": 1170464,
    "record_file_sha256": "dd936dc713d3461cfbf2652c4e88c89ac4b918eb7949bb379f3b940d62cb8ec7",
    "record_identity_chain_sha256": "673061557c1b53e78bf300d18e11e510d091378ad3431e159f6049404cde5101",
    "request_path": TOPIC + "/computations/request-complete-response-self-current.json",
    "request_bytes": 9269,
    "request_sha256": "fd6e8526d6f7e9492911848b17a852d64a31654513a267ba61e5bdb9390ffb01",
    "report_bytes": 15639,
    "report_sha256": "c4b4031bddacca0c84050c7efdf8b43f80e7553553305d55dd52637f96af292d",
}
PINNED = {
    "literature_complete_response_self_current.py": (54281, "18d5578869860f9da52d31137352f6a503a27610eab5e133b9a1c0f9ca85e8f5"),
    "literature_full_self_euler_coordinates.py": (10966, "95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba"),
    "literature_color_priority_words.py": (21642, "ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9"),
    "literature_colored_profile_algebra.py": (15738, "c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f"),
    "literature_pure_bulk_exact_membership.py": (33718, "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70"),
    "literature_pure_bulk_word_normal_form.py": (32310, "d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65"),
    "literature_range_profile_algebra.py": (33169, "a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52"),
}
# This constant is deliberately independent of the old driver's DOMAIN.
DOMAIN = {
    "paid_operator_records": 18, "paid_Q_kernel_columns": 85,
    "paid_current_null_relations": 53, "original_labels": 144,
    "new_self_columns": 53, "new_development_checks": 2,
    "self_normalization": "2K_not_K_over_4",
    "root_substitution": "only_outer_t_to_r_squared_over_3p",
    "original_right_anchor": True,
    "reference_K_columns": 11, "paid_reference_formal_dimension": 22,
    "profile_or_actual_root_evaluations": 0,
    "old_operator_constructions": 0, "old_Q_maps": 0, "old_Q_ranks": 0,
    "old_current_maps": 0, "old_current_ranks": 0, "old_checks": 0,
    "new_problem": "complete_self_image_of_paid_joint_kernel_plus_exact_comparison_with_paid_22",
}
LIMITS = {
    "seconds": 180, "development_seconds": 20, "memory_mib": 1024,
    "nodes": 500000, "atoms": 60000, "terms": 80000,
    "word_calls": 500000, "cache_entries": 300000,
    "rational_bits": 8192, "monitored_rational_operations": 5000000,
    "mathematical_stdout_bytes": 2500000, "stdout_final_reserve_bytes": 131072,
    "original_log_read_bytes": 8388608, "network_json_bytes": 2097152,
    "network_timeout_seconds": 40,
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class InputFailure(Exception):
    pass


def validate_sources(request, repo):
    if (request.get("schema") != SCHEMA or request.get("repository") != REPOSITORY
            or request.get("entry_point") != ENTRY or request.get("domain") != DOMAIN
            or request.get("limits") != LIMITS or request.get("paid_input") != PAID):
        raise InputFailure("reviewed request/domain/limits/paid identities changed")
    manifest = request.get("source_manifest")
    required = {TOPIC + "/scripts/" + name for name in PINNED}
    required.update((ENTRY, DESIGN, WORKFLOW, TOPIC + "/scripts/read_original_actions_log.py"))
    if (not isinstance(manifest, list) or len(manifest) != len(required)
            or {row.get("path") for row in manifest} != required):
        raise InputFailure("manifest must bind exactly the seven paid modules and four new/execution sources")
    identities = []
    for row in sorted(manifest, key=lambda item: item["path"]):
        path = (repo / row["path"]).resolve()
        if repo not in path.parents or not path.is_file():
            raise InputFailure("source path is absent or outside the repository")
        raw = path.read_bytes()
        identity = {"path": row["path"], "bytes": len(raw), "sha256": sha(raw)}
        if identity != row:
            raise InputFailure("source bytes/hash mismatch: " + row["path"])
        if path.name in PINNED and (len(raw), sha(raw)) != PINNED[path.name]:
            raise InputFailure("paid algebra/interface source changed: " + path.name)
        identities.append(identity)
    if request.get("source_sha256") != {row["path"]: row["sha256"] for row in identities}:
        raise InputFailure("workflow and entry source bindings differ")
    return identities


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def read_limited(response, limit):
    chunks, count = [], 0
    while True:
        chunk = response.read(min(65536, limit + 1 - count))
        if not chunk:
            break
        count += len(chunk)
        if count > limit:
            raise InputFailure("bounded original-input read exceeded")
        chunks.append(chunk)
    return b"".join(chunks)


def github_get(path, accept="application/vnd.github+json", limit=None):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise InputFailure("a read-only Actions token is required for the original log")
    if not path.startswith("/repos/" + REPOSITORY + "/"):
        raise InputFailure("unexpected GitHub API path")
    headers = {
        "Accept": accept, "Authorization": "Bearer " + token,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "visible-flex-paid-input-reader",
    }
    request = urllib.request.Request("https://api.github.com" + path, headers=headers)
    opener = urllib.request.build_opener(NoRedirect())
    try:
        with opener.open(request, timeout=LIMITS["network_timeout_seconds"]) as response:
            return read_limited(response, limit or LIMITS["network_json_bytes"])
    except urllib.error.HTTPError as exc:
        if exc.code not in (301, 302, 303, 307, 308):
            raise InputFailure("original input GitHub GET failed with HTTP " + str(exc.code)) from None
        location = exc.headers.get("Location")
    # Signed-URL requests never receive the API Authorization header.
    for _ in range(3):
        parsed = urllib.parse.urlsplit(location or "")
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise InputFailure("original log redirect is not a credential-free HTTPS URL")
        request = urllib.request.Request(location, headers={"User-Agent": "visible-flex-paid-input-reader"})
        try:
            with opener.open(request, timeout=LIMITS["network_timeout_seconds"]) as response:
                return read_limited(response, limit or LIMITS["network_json_bytes"])
        except urllib.error.HTTPError as exc:
            if exc.code not in (301, 302, 303, 307, 308):
                raise InputFailure("original signed-log GET failed with HTTP " + str(exc.code)) from None
            location = exc.headers.get("Location")
    raise InputFailure("original log exceeded the finite redirect bound")


def paid_input(progress):
    """Read paid output; no mathematical coordinate or null relation is checked again."""
    started = time.perf_counter()
    prefix = "/repos/" + REPOSITORY
    run = json.loads(github_get(prefix + "/actions/runs/" + str(PAID["run_id"])))
    job = json.loads(github_get(prefix + "/actions/jobs/" + str(PAID["job_id"])))
    if (run.get("id") != PAID["run_id"] or job.get("id") != PAID["job_id"]
            or job.get("run_id") != PAID["run_id"]
            or run.get("head_sha") != PAID["source_commit"]
            or job.get("head_sha") != PAID["source_commit"]
            or run.get("status") != "completed" or run.get("conclusion") != "success"
            or job.get("status") != "completed" or job.get("conclusion") != "success"):
        raise InputFailure("original run/job/source/status binding failed")
    request_raw = github_get(prefix + "/contents/" + PAID["request_path"]
                             + "?ref=" + PAID["source_commit"],
                             accept="application/vnd.github.raw+json")
    if (len(request_raw), sha(request_raw)) != (PAID["request_bytes"], PAID["request_sha256"]):
        raise InputFailure("original source-commit request changed")
    old_request = json.loads(request_raw)
    log_raw = github_get(prefix + "/actions/jobs/" + str(PAID["job_id"]) + "/logs",
                         accept="application/vnd.github+json",
                         limit=LIMITS["original_log_read_bytes"])
    if (len(log_raw), sha(log_raw)) != (PAID["log_bytes"], PAID["log_sha256"]):
        raise InputFailure("original complete log identity changed")
    records, identity_chain, jsonl_digest = [], hashlib.sha256(), hashlib.sha256()
    jsonl_bytes = 0
    reports = []
    for line in log_raw.decode("utf-8").splitlines():
        marker = "CURRENT_Q_RECORD "
        if marker in line:
            envelope = json.loads(line.split(marker, 1)[1])
            if set(envelope) != {"sequence", "kind", "payload_bytes", "payload_sha256", "payload"}:
                raise InputFailure("original record envelope schema changed")
            if envelope["sequence"] != len(records) + 1:
                raise InputFailure("original record sequence changed")
            raw = canonical(envelope["payload"])
            if (len(raw), sha(raw)) != (envelope["payload_bytes"], envelope["payload_sha256"]):
                raise InputFailure("original record payload identity failed")
            identity = {name: envelope[name] for name in
                        ("sequence", "kind", "payload_bytes", "payload_sha256")}
            identity_chain.update(canonical(identity) + b"\n")
            encoded = canonical(envelope) + b"\n"
            jsonl_digest.update(encoded)
            jsonl_bytes += len(encoded)
            records.append(envelope)
        marker = "COMPLETE_CURRENT_Q_REPORT "
        if marker in line:
            report_raw = line.split(marker, 1)[1].encode("utf-8") + b"\n"
            reports.append((json.loads(report_raw), len(report_raw), sha(report_raw)))
    if (len(records) != PAID["records"] or jsonl_bytes != PAID["record_file_bytes"]
            or jsonl_digest.hexdigest() != PAID["record_file_sha256"]
            or identity_chain.hexdigest() != PAID["record_identity_chain_sha256"]):
        raise InputFailure("original record file/chain identity failed")
    if len(reports) != 1 or reports[0][1:] != (PAID["report_bytes"], PAID["report_sha256"]):
        raise InputFailure("original complete final report identity failed")
    final = reports[0][0]
    if (final.get("entry_outcome") != "complete_new_observation"
            or final.get("workflow_source") != PAID["source_commit"]
            or str(final.get("run_id")) != str(PAID["run_id"])
            or not final["science"].get("all_required_fresh_source_certificates_completed")
            or final["request"] != {"bytes": PAID["request_bytes"], "sha256": PAID["request_sha256"]}):
        raise InputFailure("the paid observation was not fully completed")
    if old_request["source_manifest"] != final["source_manifest"]:
        raise InputFailure("original request/report source manifests differ")
    by_kind = {}
    for record in records:
        by_kind.setdefault(record["kind"], []).append(record)
    operators = by_kind.get("science.original_operator", [])
    qkernel = by_kind.get("science.complete_kernel_current_column", [])
    dependent = [record for record in by_kind.get("science.current_image_elimination_step", [])
                 if record["payload"].get("kind") == "dependent"]
    label_records = by_kind.get("science.original_cost_labels", [])
    if (len(operators), len(qkernel), len(dependent), len(label_records)) != (18, 85, 53, 1):
        raise InputFailure("paid input counts changed")
    if [row["payload"]["kernel_index"] for row in qkernel] != list(range(85)):
        raise InputFailure("paid kernel indices changed")
    if any(not row["payload"].get("complete_Q_coordinates_zero")
           or not row["payload"].get("all_three_moments_emitted") for row in qkernel):
        raise InputFailure("paid kernel-column completion flags changed")
    evidence = {
        "original": PAID, "original_run_created_at": run.get("created_at"),
        "original_job_started_at": job.get("started_at"), "original_job_completed_at": job.get("completed_at"),
        "original_job_steps": [{key: step.get(key) for key in
                               ("number", "name", "status", "conclusion", "started_at", "completed_at")}
                              for step in job.get("steps", [])],
        "original_source_manifest": final["source_manifest"],
        "consumed_operator_records": [row["sequence"] for row in operators],
        "consumed_85_kernel_record_sequences": [row["sequence"] for row in qkernel],
        "consumed_53_dependent_record_sequences": [row["sequence"] for row in dependent],
        "log_and_request_only_in_memory": True,
        "old_mathematical_checks_repeated": 0,
        "read_and_identity_seconds": time.perf_counter() - started,
    }
    progress.update(evidence)
    return {
        "operators": [row["payload"] for row in operators],
        "kernel": [row["payload"] for row in qkernel],
        "relations": [row["payload"] for row in dependent],
        "relation_envelopes": [dict(sequence=row["sequence"], payload_sha256=row["payload_sha256"])
                               for row in dependent],
        "labels": [tuple(label) for label in label_records[0]["payload"]],
    }


class Journal:
    def __init__(self, path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        self.file = path.open("wb")
        self.file_digest, self.chain = hashlib.sha256(), hashlib.sha256()
        self.sequence = self.file_bytes = self.stdout_bytes = 0
        self.by_kind = {}
        self.last_record = None
        self.unemitted = []

    def record(self, kind, payload):
        raw = canonical(payload)
        self.sequence += 1
        identity = {"sequence": self.sequence, "kind": kind,
                    "payload_bytes": len(raw), "payload_sha256": sha(raw)}
        envelope = {**identity, "payload": payload}
        encoded = canonical(envelope) + b"\n"
        self.file.write(encoded)
        self.file.flush()
        self.file_digest.update(encoded)
        self.file_bytes += len(encoded)
        self.chain.update(canonical(identity) + b"\n")
        self.by_kind[kind] = self.by_kind.get(kind, 0) + 1
        self.last_record = identity
        line = b"SELF_KERNEL_RECORD " + encoded
        if self.stdout_bytes + len(line) > LIMITS["mathematical_stdout_bytes"] - LIMITS["stdout_final_reserve_bytes"]:
            self.unemitted.append(identity)
            raise paid.OutputBudgetExceeded("completed new self record exceeds stdout allowance")
        self.stdout_bytes += len(line)
        sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()
        return identity

    def receipt(self):
        return {
            "completed_record_count": self.sequence, "record_counts": dict(self.by_kind),
            "record_identity_chain_sha256": self.chain.hexdigest(),
            "temporary_record_file_bytes": self.file_bytes,
            "temporary_record_file_sha256": self.file_digest.hexdigest(),
            "mathematical_record_stdout_bytes": self.stdout_bytes,
            "reserved_final_stdout_bytes": LIMITS["stdout_final_reserve_bytes"],
            "last_completed_record": self.last_record,
            "completed_but_not_emitted_records": list(self.unemitted),
            "machine_payload_committed_uploaded_or_blobbed": False,
        }


def make_mapper(ring):
    class GuardedPriority(paid.priority.PriorityWords):
        def cache_guard(self):
            ring.limits.shared_usage()
            super().cache_guard()
            ring.limits.check()
    owner = GuardedPriority(
        ring, max_calls=LIMITS["word_calls"], max_terms=LIMITS["terms"],
        max_weight=5, max_shuffle_entries=LIMITS["cache_entries"],
        max_cache_entries=LIMITS["cache_entries"], color_order=("q",))
    ring.limits.monitored_owners.append(owner)
    ring.limits.check()
    return owner


def load_local(ring, rows):
    result = ring.number(0)
    for power, jets, coefficient in rows:
        if type(power) is not int or power < 0 or jets != sorted(jets):
            raise InputFailure("paid local input monomial schema changed")
        term = ring.x() ** power
        for order in jets:
            if type(order) is not int or order < 0:
                raise InputFailure("invalid paid jet index")
            term *= ring.color("q", order)
        result += F(coefficient) * term
        ring.limits.check()
    return result


def original_sources(data, ring, progress):
    """Only deserialize the 18 paid triples; never invoke original_operators."""
    operators = {}
    for row in data["operators"]:
        name = row["label"]
        if name in operators:
            raise InputFailure("duplicate paid operator label")
        operators[name] = tuple(load_local(ring, row[key]) for key in ("a", "b", "c"))
    if tuple(operators) != tuple(paid.Z_ORDER):
        raise InputFailure("paid operator order differs from the pinned source")
    labels = data["labels"]
    if labels != [(e, z) for z in paid.Z_ORDER for e in paid.E_ORDER]:
        raise InputFailure("paid 144-label order changed")
    index = {label: position for position, label in enumerate(labels)}
    combinations = []
    for position, relation in enumerate(data["relations"]):
        combo = {}
        for kernel_index, coefficient in relation["kernel_column_combination"]:
            if type(kernel_index) is not int or not 0 <= kernel_index < 85:
                raise InputFailure("dependent relation refers outside the paid 85 columns")
            coefficient = F(coefficient)
            for label, value in data["kernel"][kernel_index]["original_combination"]:
                paid.add(combo, index[tuple(label)], coefficient * F(value), ring.limits)
        combinations.append(combo)
        progress.unit("new_self_source_compositions", position)
        progress.record("paid_relation_new_self_source", {
            "self_column_index": position,
            "paid_dependent_record": data["relation_envelopes"][position],
            "paid_85_column_combination": relation["kernel_column_combination"],
            "original_144_combination": paid.original_combination_rows(combo, labels),
            "old_Q_or_current_coordinate_check_performed": False,
        })
    # Only the published E8 diagonal constructors are used. No old 144 Q or
    # current column, original 18 construction, or old main/science is called.
    q, _, _ = paid.quadratic_operators(ring)
    return operators, q, labels, combinations


def serialize_word(word):
    return [[power, [[color, order] for color, order in jets]] for power, jets in word]


def af_rows(poly):
    # key = (x power, u power, p power, r power, higher OUTER jets, untouched word)
    return [[power, n0, n1, n2, list(high), serialize_word(word), str(value)]
            for (power, n0, n1, n2, high, word), value in sorted(poly.items())]


def af_outer(words, budget, expected_degree=None):
    """Substitute only OUTER t. No integral-letter or derivative of Af is changed."""
    result = {}
    for (local, word), value in words.terms.items():
        power, colored_jets = local
        if any(color != "q" for color, order in colored_jets):
            raise paid.InterfaceFailure("the new self current is not one-color")
        jets = tuple(order for color, order in colored_jets)
        if expected_degree is not None:
            degree = len(jets) + sum(len(letter[1]) for letter in word)
            if degree != expected_degree:
                raise paid.InterfaceFailure("new self current has wrong complete profile degree", {
                    "whole_word_rows": paid.priority.rows(words), "expected_degree": expected_degree})
        n0, n1, n2, n3 = (jets.count(order) for order in range(4))
        high = tuple(order for order in jets if order > 3)
        key = (power, n0, n1 - n3, n2 + 2*n3, high, word)
        paid.add(result, key, value / F(3)**n3, budget)
    return result


def classify_af(poly):
    local, nonlocal_terms, high = {}, {}, {}
    for key, value in poly.items():
        if key[-1]:
            nonlocal_terms[key] = value
        elif key[-2]:
            high[key] = value
        else:
            local[key] = value
    return local, nonlocal_terms, high


def construct_self(ring, operators, q, labels, combo):
    x, u, p, r = ring.x(), ring.color("q"), ring.color("q", 1), ring.color("q", 2)
    integrand, pre, differential = (ring.number(0) for _ in range(3))
    for index, coefficient in sorted(combo.items()):
        ename, zname = labels[index]
        a, b, c = operators[zname]
        w = q[ename]
        h = (a*r).D() + b*p
        integrand += coefficient*c*w
        pre += coefficient*(a*(p*w.D().D() - r*w.D()) + w*h)
        differential += coefficient*((a*w.D().D()).D() + b*w.D())
        ring.limits.check()
    primitive = integrand.I()
    current = 2*(pre + u*primitive)
    second = 2*(differential + primitive)
    return current, second


def development(progress):
    progress.start()
    progress.stage("two_new_self_adapter_checks")
    budget = paid.make_budget(LIMITS["development_seconds"], development=True)
    ring = paid.colored.ColoredRing(budget)
    owner, fresh = make_mapper(ring), make_mapper(ring)
    progress.bind(budget=budget, ring=ring, owners=[("new_adapter", owner), ("fresh_adapter", fresh)])
    u, p, r, t, x = tuple(ring.color("q", j) for j in range(4)) + (ring.x(),)
    # Invented quadratic primitive input, not one of the paid 144 cost labels.
    a, b = ring.number(0), x*u*u
    c = -u*p - 2*x*p*p - x*u*r
    w = (u*u).J() + x*u*p
    h = b*p
    current = 2*(w*h + u*(c*w).I())
    second = 2*(b*w.D() + (c*w).I())
    difference = fresh.expression(current.D() - p*second)
    if difference.terms:
        raise AssertionError("new quadratic-self Green adapter failed")
    preserved = owner.expression(current)
    progress.record("new_adapter_check", {
        "name": "invented_quadratic_self_same_anchor_Green",
        "passed": True, "source": {"a": "0", "b": "x*u^2", "c": "-u*p-2*x*p^2-x*u*r",
                                  "w": "J(u^2)+x*u*p"},
        "new_current_word_sha256": sha(canonical(paid.priority.rows(preserved))),
        "derivative_difference_zero": True,
        "old_development_check_executed": False,
    })
    progress.unit("new_adapter_checks", "quadratic_self_Green")
    A = 6*p*t - 2*r*r
    probe = u*A*(u*u).I() + u*p*t*(r*r).I() + u*p*p*(t*t).I() + u**4*ring.color("q", 4)
    observed = af_outer(owner.expression(probe), budget, expected_degree=5)
    word_r = ((0, (("q", 2), ("q", 2))),)
    word_t = ((0, (("q", 3), ("q", 3))),)
    expected = {
        (0, 1, 0, 2, (), word_r): F(1, 3),
        (0, 1, 2, 0, (), word_t): F(1),
        (0, 4, 0, 0, (4,), ()): F(1),
    }
    if observed != expected:
        raise AssertionError("new Af adapter changed an inner jet or erased a higher jet")
    progress.record("new_adapter_check", {
        "name": "outer_only_Af_keeps_inner_t_and_higher_outer_jet",
        "passed": True, "complete_observed_rows": af_rows(observed),
        "old_development_check_executed": False,
    })
    progress.unit("new_adapter_checks", "outer_only_Af")
    progress.data["all_passed"] = True
    progress.data["old_checks_executed"] = 0
    progress.finish("two_new_self_adapter_checks_passed")


def local_poly(rows):
    result = {}
    for key, value in rows:
        power, n0, n1, n2 = key
        paid.add(result, (power, n0, n1, n2, (), ()), F(value))
    return result


def reference_nonK():
    """Read the eleven published non-K currents; no old rank is recomputed."""
    R = [
        ("J_sigma", [((0,0,2,3),"2/3")]),
        ("J_1", [((0,0,1,4),"4/3")]),
        ("J_2", [((1,0,1,4),"8/3"),((0,0,2,3),"-8/3")]),
        ("J_3", [((2,0,1,4),4),((1,0,2,3),"-8/3")]),
        ("W_sigma", [((1,0,2,3),"2/3"),((0,0,3,2),-2)]),
        ("W_2", [((2,0,1,4),"8/3"),((1,0,2,3),"-32/3"),((0,0,3,2),8)]),
        ("W_3", [((3,0,1,4),4),((2,0,2,3),"-44/3"),((1,0,3,2),8)]),
        ("Xi_0", [((2,0,1,4),"8/3"),((1,0,2,3),"-32/3"),
                  ((0,0,3,2),"32/3"),((0,1,1,3),"-32/3")]),
        ("Xi_1", [((0,1,2,2),16),((1,1,1,3),"-32/3"),((0,0,4,1),-16),
                  ((1,0,3,2),"80/3"),((2,0,2,3),-16),((3,0,1,4),"8/3")]),
        ("Xi_2", [((0,2,1,2),16),((0,1,3,1),-32),((0,0,5,0),16),
                  ((1,0,4,1),-32),((1,1,2,2),32),((2,0,3,2),"80/3"),
                  ((2,1,1,3),"-32/3"),((3,0,2,3),"-32/3"),((4,0,1,4),"4/3")]),
        ("U_star", [((0,1,0,4),1)]),
    ]
    return [(name, local_poly(rows)) for name, rows in R]


def poly_mul(a, b, budget):
    result = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            paid.add(result, tuple(x+y for x, y in zip(ka, kb)), va*vb, budget)
        budget.check()
    return result


def poly_pow(a, n, budget):
    result = {(0,0,0,0,0): F(1)}
    for _ in range(n):
        result = poly_mul(result, a, budget)
    return result


def reference_K(budget):
    """Encode the already proved finite R435 generating identity, not its old rank."""
    # Keys are (z,x,u,p,r). F_z=A_z^3/15*(4A_z^2-10z^2*u*A_z-20*w^4*r^2/3).
    A = {(0,0,0,0,1):F(1), (1,1,0,0,1):F(-2), (1,0,0,1,0):F(2),
         (2,2,0,0,1):F(1), (2,1,0,1,0):F(-2), (2,0,1,0,0):F(2)}
    w = {(0,0,0,0,0):F(1), (1,1,0,0,0):F(-1)}
    inside = {}
    for key, value in poly_pow(A, 2, budget).items():
        paid.add(inside, key, 4*value, budget)
    for key, value in poly_mul({(2,0,1,0,0):F(1)}, A, budget).items():
        paid.add(inside, key, -10*value, budget)
    for key, value in poly_mul(poly_pow(w, 4, budget), {(0,0,0,0,2):F(1)}, budget).items():
        paid.add(inside, key, -F(20,3)*value, budget)
    full = poly_mul(poly_pow(A, 3, budget), inside, budget)
    result = [dict() for _ in range(11)]
    for (degree, power, n0, n1, n2), value in full.items():
        if degree > 10:
            raise paid.InterfaceFailure("reference K generating identity exceeded its published degree")
        paid.add(result[degree], (power,n0,n1,n2,(),()), value*math.factorial(degree)/15, budget)
    return result


def coordinate_rows(poly):
    return af_rows(poly)


def to_original(combo, combinations, labels, budget, prefix=0):
    original, K = {}, {}
    for index, coefficient in combo.items():
        if index < prefix:
            paid.add(K, index, coefficient, budget)
        else:
            for label_index, value in combinations[index-prefix].items():
                paid.add(original, label_index, coefficient*value, budget)
    return {
        "K_generating_columns": [[index, str(value)] for index, value in sorted(K.items())],
        "original_144_combination": paid.original_combination_rows(original, labels),
    }


def science(data, progress):
    progress.start()
    progress.stage("new_self_input_composition")
    budget = paid.make_budget(LIMITS["seconds"])
    ring = paid.colored.ColoredRing(budget)
    owner, fresh = make_mapper(ring), make_mapper(ring)
    progress.bind(budget=budget, ring=ring, owners=[("new_self", owner), ("new_derivative_certificate", fresh)])
    operators, q, labels, combinations = original_sources(data, ring, progress)
    progress.data["scope"] = {
        **DOMAIN, "concrete_profile_or_Af_values_computed": 0,
        "full_response_space_classified": False, "actual_joint_section_claimed": False,
        "all_internal_period_conditions_resolved": False,
        "nonlocal_representative_nonzero_is_functional_nonmembership": False,
        "known_22_rank_is_reused_as_published_not_an_independent_target": True,
    }
    progress.data["normalization"] = {
        "I": "integral_from_the_original_common_right_endpoint_to_x",
        "full_self": "2*K_tau(q_E)",
        "current": "2*(sum a*(p*qpp-r*qp)+sum q*((a*r)prime+b*p)+u*I(sum c*q))",
        "derivative": "p*(full_self)pp",
        "left_integration_constant": "zero_by_flat_outer_u,p,r_at_the_actual_left_collar",
        "Af": "outer t=r^2/(3p), p_nonzero; inner words and higher jets unchanged",
        "paid_whole_Q_rows_used_as_primitive": False,
    }
    polynomials, unresolved = [], []
    p = ring.color("q", 1)
    progress.stage("fifty_three_complete_self_currents")
    for index, combo in enumerate(combinations):
        progress.data["active_input"] = {"kind": "new_complete_self", "self_column_index": index}
        current, second = construct_self(ring, operators, q, labels, combo)
        whole = owner.expression(current)
        observed = af_outer(whole, budget, expected_degree=5)
        local, nonlocal_terms, higher = classify_af(observed)
        # This is a certificate of this NEW self current, not a re-run of Q,
        # ordered currents, the old operator recurrence, or any old check.
        derivative = fresh.expression(current.D() - p*second)
        if derivative.terms:
            raise paid.InterfaceFailure("new full-self Green source certificate failed", {
                "self_column_index": index, "derivative_difference": paid.priority.rows(derivative)})
        supported = not nonlocal_terms and not higher
        if not supported:
            unresolved.append(index)
        polynomials.append(local if supported else None)
        progress.unit("new_complete_self_columns", index)
        progress.record("complete_self_column", {
            "self_column_index": index,
            "paid_relation_identity": data["relation_envelopes"][index],
            "original_144_combination": paid.original_combination_rows(combo, labels),
            "whole_current_before_Af": paid.priority.rows(whole),
            "complete_Af_rows": af_rows(observed),
            "local_Af_rows": af_rows(local),
            "nonlocal_Af_rows": af_rows(nonlocal_terms),
            "higher_outer_jet_Af_rows": af_rows(higher),
            "fresh_new_self_Green_derivative_zero": True,
            "complete_local_Laurent_interface": supported,
            "p_denominator_order": max((max(0,-key[2]) for key in observed), default=0),
            "nonlocal_terms_discarded": 0, "higher_jets_discarded": 0,
            "old_Q_or_current_check_executed": False,
        })
    progress.data["new_self_mapping_completed"] = True
    progress.data["unresolved_self_columns"] = unresolved
    if unresolved:
        progress.finish("complete_self_mapping_with_exact_unresolved_nonlocal_or_higher_jet_interface")
        return
    progress.stage("new_self_image_and_reference_union")
    K = reference_K(budget)
    refs = reference_nonK()
    keys = sorted(set().union(*(set(poly) for poly in polynomials + K + [poly for _,poly in refs])))
    positions = {key: index for index, key in enumerate(keys)}
    def coordinates(poly):
        return {positions[key]: value for key, value in poly.items()}
    columns = [coordinates(poly) for poly in polynomials]
    kcolumns = [coordinates(poly) for poly in K]
    progress.record("new_self_coordinate_labels", [
        [key[0],key[1],key[2],key[3],list(key[4]),serialize_word(key[5])] for key in keys])
    for index, poly in enumerate(K):
        progress.record("paid_K_reference_encoding", {
            "K_index": index, "source": "R435(12); coefficient times factorial",
            "complete_Af_rows": af_rows(poly), "standalone_old_rank_executed": False})
    def self_done(index, value, rep, independent, null_count):
        progress.unit("new_self_image_columns", index)
        progress.record("new_self_image_step", {
            "self_column_index": index, "kind": "pivot" if value else "new_self_dependency",
            "pivot_coordinate": min(value) if value else None,
            "new_53_column_combination": paid.vector_rows(rep),
            "source": to_original(rep, combinations, labels, budget),
            "normalized_current_coordinates": paid.vector_rows(value),
        })
    image = paid.ExactSpace(columns, budget, completed_column=self_done)
    progress.data["new_53_self_image_dimension"] = len(image.independent)
    progress.data["new_53_self_kernel_dimension"] = len(image.kernel)
    progress.data["new_53_self_basis_indices"] = list(image.independent)
    # This is one NEW union-image question. No standalone rank of the eleven K
    # currents or the published twenty-two-current module is executed.
    def union_done(index, value, rep, independent, null_count):
        progress.unit("new_union_image_columns", index)
        progress.record("new_K_plus_paid_kernel_self_image_step", {
            "union_column_index": index,
            "kind": "pivot" if value else "new_union_dependency",
            "pivot_coordinate": min(value) if value else None,
            "union_combination": paid.vector_rows(rep),
            "source": to_original(rep, combinations, labels, budget, prefix=11),
            "normalized_current_coordinates": paid.vector_rows(value),
        })
    union = paid.ExactSpace(kcolumns + columns, budget, completed_column=union_done)
    all_members = True
    for name, poly in refs:
        coefficients, residual = image.reduce(coordinates(poly))
        # The membership is a new comparison with the 53 paid relations; the
        # published current formula itself is never recomputed from a cost.
        if residual:
            all_members = False
        progress.unit("new_reference_comparisons", name)
        progress.record("published_reference_in_new_self_image", {
            "name": name, "complete_Af_rows": af_rows(poly),
            "outcome": "MEMBER" if not residual else "SOURCE_COMPARISON_UNRESOLVED",
            "new_53_coefficients": paid.vector_rows(coefficients),
            "original_source": to_original(coefficients, combinations, labels, budget),
            "full_current_residual": paid.vector_rows(residual),
        })
    progress.data["all_eleven_published_nonK_references_in_new_53_image"] = all_members
    progress.data["new_K_plus_53_self_image_dimension"] = len(union.independent)
    progress.data["new_union_basis_indices"] = list(union.independent)
    progress.data["new_union_kernel_dimension"] = len(union.kernel)
    if not all_members or len(union.independent) < 22:
        progress.finish("new_self_image_complete_but_published_reference_comparison_unresolved")
        return
    extra = len(union.independent) - 22
    progress.data["additional_formal_dimensions_over_paid_22"] = extra
    progress.data["paid_22_is_entire_augmented_formal_image"] = extra == 0
    progress.data["mirror_scope"] = {
        "known_six_blind_currents_complete_for_augmented_module_if_no_extra_dimension": extra == 0,
        "new_actual_mirror_rank_evaluation": False,
        "formal_rank_is_actual_all_root_rank": False,
        "if_extra_dimensions": "the emitted complete union basis is new; no unchanged mirror rank or actual section is inferred",
    }
    progress.data["active_input"] = None
    progress.finish("complete_new_self_image_no_extra_formal_direction" if extra == 0
                    else "complete_new_self_image_with_additional_formal_directions")


def main():
    global paid
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise RuntimeError("only the reviewed public Actions entry may execute this observation")
    repo = Path(__file__).resolve().parents[3]
    request_path = Path(args.request).resolve()
    if repo not in request_path.parents:
        raise InputFailure("request must be the source-commit repository request")
    raw = request_path.read_bytes()
    request = json.loads(raw)
    identities = validate_sources(request, repo)
    out = Path(args.out).resolve()
    if out == repo or repo in out.parents:
        raise InputFailure("all machine outputs must stay outside the Git checkout")
    out.parent.mkdir(parents=True, exist_ok=True)
    paid = importlib.import_module("literature_complete_response_self_current")
    journal = Journal(out.with_suffix(".records.jsonl"))
    development_phase = paid.PhaseProgress("development", journal)
    scientific_phase = paid.PhaseProgress("science", journal)
    started = time.perf_counter()
    input_progress = {"started": True, "completed": False, "old_science_executions": 0}
    report = {
        "schema": SCHEMA, "repository": REPOSITORY,
        "run_id": os.environ.get("GITHUB_RUN_ID"), "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "workflow_source": os.environ.get("GITHUB_SHA"),
        "request": {"path": str(request_path.relative_to(repo)), "bytes": len(raw), "sha256": sha(raw)},
        "source_manifest": identities, "domain": DOMAIN, "limits": LIMITS,
        "paid_input_read": input_progress,
        "development": development_phase.data, "science": scientific_phase.data,
        "old_Q_current_operator_rank_or_check_executions": 0,
        "original_log_written_to_file": False, "actual_joint_period_resolved": False,
    }
    phase, exit_code = None, 0
    try:
        data = paid_input(input_progress)
        input_progress["completed"] = True
        journal.record("input.paid_original_output_identity", input_progress)
        paid.load_algebra()
        phase = development_phase
        development(development_phase)
        phase = scientific_phase
        science(data, scientific_phase)
        if "unresolved" in scientific_phase.data["outcome"]:
            report["entry_outcome"] = "unresolved_structural_or_source_interface"
            exit_code = 2
        else:
            report["entry_outcome"] = "complete_new_observation"
    except Exception as exc:
        if isinstance(exc, (InputFailure, paid.InterfaceFailure)):
            exit_code, outcome = 2, "unresolved_input_or_structural_interface"
        elif isinstance(exc, paid.OutputBudgetExceeded):
            exit_code, outcome = 3, "finite_stdout_budget_failure"
        elif hasattr(paid, "exact") and isinstance(exc, paid.exact.formal.CompilationBudgetExceeded):
            exit_code, outcome = 3, "finite_budget_failure"
        else:
            exit_code, outcome = 4, "entry_error"
        report["entry_outcome"] = outcome
        report["entry_error"] = {"type": type(exc).__name__, "message": str(exc)}
        report["failure_phase"] = None if phase is None else phase.name
        if phase is not None:
            try:
                phase.fail(outcome, exc)
            except Exception as reporting_error:
                report["secondary_reporting_error"] = {
                    "type": type(reporting_error).__name__, "message": str(reporting_error)}
    finally:
        development_phase.snapshot()
        scientific_phase.snapshot()
        journal.file.close()
        report["total_elapsed_seconds"] = time.perf_counter() - started
        report["peak_RSS_KiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report["record_journal"] = journal.receipt()
    encoded = canonical(report) + b"\n"
    line = b"COMPLETE_SELF_KERNEL_REPORT " + encoded
    if journal.stdout_bytes + len(line) + 1024 > LIMITS["mathematical_stdout_bytes"]:
        full = out.with_suffix(".unemitted-summary.json")
        full.write_bytes(encoded)
        report["unabridged_summary_identity"] = {"bytes": len(encoded), "sha256": sha(encoded),
                                                  "runner_temporary_filename": full.name}
        report.pop("source_manifest", None)
        report["source_manifest_identity"] = {"entries": len(identities), "sha256": sha(canonical(identities))}
        report["entry_outcome"] = "finite_stdout_budget_failure"
        report["complete_mathematical_publication"] = False
        encoded = canonical(report) + b"\n"
        line = b"COMPLETE_SELF_KERNEL_REPORT " + encoded
        exit_code = 3
    out.write_bytes(encoded)
    sys.stdout.buffer.write(line)
    sys.stdout.buffer.flush()
    receipt = {
        "bytes": len(encoded), "sha256": sha(encoded), "exit_code": exit_code,
        "record_file_bytes": journal.file_bytes, "record_file_sha256": journal.file_digest.hexdigest(),
        "record_stdout_bytes": journal.stdout_bytes,
        "entry_elapsed_seconds_through_final_summary": time.perf_counter() - started,
    }
    sys.stdout.buffer.write(b"SELF_KERNEL_REPORT_IDENTITY " + canonical(receipt) + b"\n")
    sys.stdout.buffer.flush()
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
