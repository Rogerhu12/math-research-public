#!/usr/bin/env python3
"""One new exact whole-Q/current image on the 144 original B(E,Z) costs.

No original fourth forcing or prior rank/profile target is compiled.
Only a public Actions caller may execute this entry. All primitives use
I(F)(x)=integral_(right)^x F, and no left tail is reset.
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

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
ENTRY = TOPIC + "/scripts/literature_complete_response_self_current.py"
SCHEMA = "visible-flex-complete-response-self-current-v1"
REPORT_TAG = "COMPLETE_CURRENT_Q_REPORT"
WORKFLOW = ".github/workflows/visible-complete-response-self-current.yml"
RULE_READER = (50679, "b7b16d0917bf99e4183421ab6d5c1dd33b9c0fe8009ad59a5141a17d798e5c4a")
E_ORDER = ("P", "R", "S", "L", "U", "V", "T", "Y")
Z_ORDER = tuple("H%d" % j for j in range(7)) + tuple("J%d" % j for j in range(3)) + (
    "chi30", "chi32", "chi34", "chi37", "chi40", "chi100", "chi104", "chi109")
PARAMETERS = ("A0", "A1", "A2", "B0", "B1", "C0",
              "p3", "p2r", "xp2r", "pr2", "xpr2", "x2pr2", "S7")
DOMAIN = {
    "E_order": list(E_ORDER), "Z_order": list(Z_ORDER),
    "original_cost_labels": 144, "true_tail_moments": 3,
    "label_order": "Z_major_then_E",
    "current_coordinate_order": list(PARAMETERS),
    "formal_u_targets": 18,
    "scope": "span_B_E_Z_intersect_complete_Q_kernel",
    "development_checks": 2,
}
DEPENDENCIES = {
    "literature_full_self_euler_coordinates.py": (10966, "95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba"),
    "literature_color_priority_words.py": (21642, "ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9"),
    "literature_colored_profile_algebra.py": (15738, "c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f"),
    "literature_pure_bulk_exact_membership.py": (33718, "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70"),
    "literature_pure_bulk_word_normal_form.py": (32310, "d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65"),
    "literature_range_profile_algebra.py": (33169, "a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52"),
}
LIMITS = {
    "seconds": 180, "memory_mib": 1024, "nodes": 500000, "atoms": 60000,
    "terms": 80000, "word_calls": 500000, "cache_entries": 300000,
    "rational_bits": 8192, "monitored_rational_operations": 5000000,
    "mathematical_stdout_bytes": 2500000, "stdout_final_reserve_bytes": 131072,
    "development_seconds": 20,
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


class InterfaceFailure(Exception):
    def __init__(self, message, evidence=None):
        super().__init__(message)
        self.evidence = evidence or {}



class OutputBudgetExceeded(Exception):
    pass


class OutputJournal:
    """Emit each completed payload once; reserve an independent final receipt.

    Exact records also remain in a runner-only JSONL file. If a completed record
    cannot fit in stdout, retain its full temporary record and fingerprint, stop
    the observation, and report the cap failure without deleting prior charges.
    """
    def __init__(self, path):
        self.path = path
        path.parent.mkdir(parents=True, exist_ok=True)
        self.file = path.open("wb")
        self.file_digest = hashlib.sha256()
        self.chain = hashlib.sha256()
        self.sequence = 0
        self.file_bytes = 0
        self.stdout_bytes = 0
        self.by_kind = {}
        self.last_record = None
        self.unemitted_records = []
        self.closed = False

    def record(self, kind, payload):
        payload_raw = canonical(payload)
        self.sequence += 1
        identity = {
            "sequence": self.sequence, "kind": kind,
            "payload_bytes": len(payload_raw), "payload_sha256": sha(payload_raw)}
        envelope = {**identity, "payload": payload}
        encoded = canonical(envelope)+b"\n"
        self.file.write(encoded)
        self.file.flush()
        self.file_digest.update(encoded)
        self.file_bytes += len(encoded)
        self.chain.update(canonical(identity)+b"\n")
        self.by_kind[kind] = self.by_kind.get(kind, 0)+1
        self.last_record = identity
        line = b"CURRENT_Q_RECORD "+encoded
        record_limit = LIMITS["mathematical_stdout_bytes"]-LIMITS["stdout_final_reserve_bytes"]
        if self.stdout_bytes+len(line)>record_limit:
            self.unemitted_records.append(identity)
            raise OutputBudgetExceeded("completed record exceeds remaining mathematical stdout allowance")
        self.stdout_bytes += len(line)
        sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()
        return identity

    def receipt(self):
        return {
            "protocol": "one_payload_per_CURRENT_Q_RECORD_then_final_summary_v2",
            "runner_temporary_filename": self.path.name,
            "completed_record_count": self.sequence,
            "record_counts": dict(self.by_kind),
            "record_identity_chain_sha256": self.chain.hexdigest(),
            "temporary_record_file_bytes": self.file_bytes,
            "temporary_record_file_sha256": self.file_digest.hexdigest(),
            "mathematical_record_stdout_bytes": self.stdout_bytes,
            "reserved_final_stdout_bytes": LIMITS["stdout_final_reserve_bytes"],
            "last_completed_record": self.last_record,
            "completed_but_not_emitted_records": list(self.unemitted_records),
            "machine_payload_committed_uploaded_or_blobbed": False}

    def close(self):
        if not self.closed:
            self.file.close()
            self.closed = True


class PhaseProgress:
    """Shared mutable receipt survives every normal finite/error exit."""
    def __init__(self, name, journal):
        self.name, self.journal = name, journal
        self.started_at = None
        self.ended_at = None
        self.stage_at = None
        self.active_stage = None
        self.budget = self.ring = None
        self.owners = []
        self.data = {
            "started": False, "completed": False, "outcome": "not_started",
            "stages": [], "completed_units": {}, "records": {},
            "actual_joint_period_resolved": False}

    def start(self):
        self.started_at = time.perf_counter()
        self.data.update(started=True, outcome="running")

    def bind(self, budget=None, ring=None, owners=None):
        if budget is not None:
            self.budget = budget
        if ring is not None:
            self.ring = ring
        if owners is not None:
            self.owners = list(owners)
        self.snapshot()

    def stage(self, name):
        if self.active_stage is not None:
            self.finish_stage()
        self.active_stage = {"name": name, "status": "started",
                             "started_elapsed_seconds": time.perf_counter()-self.started_at}
        self.data["stages"].append(self.active_stage)
        self.stage_at = time.perf_counter()
        self.data["active_stage"] = name
        self.snapshot()

    def finish_stage(self):
        if self.active_stage is not None:
            self.active_stage["elapsed_seconds"] = time.perf_counter()-self.stage_at
            self.active_stage["status"] = "completed"
            self.active_stage = None
            self.stage_at = None
            self.data["active_stage"] = None
        self.snapshot()

    def unit(self, name, identifier=None):
        units = self.data["completed_units"]
        units[name] = units.get(name, 0)+1
        self.data["last_completed_unit"] = {"name": name, "identifier": identifier}
        self.snapshot()

    def record(self, kind, payload):
        identity = self.journal.record(self.name+"."+kind, payload)
        values = self.data["records"].setdefault(kind, {"count": 0, "last": None})
        values["count"] += 1
        values["last"] = identity
        self.snapshot()
        return identity

    def snapshot(self):
        if self.data.get("final_receipt_frozen"):
            return
        now = self.ended_at if self.ended_at is not None else time.perf_counter()
        if self.started_at is not None:
            self.data["elapsed_seconds"] = now-self.started_at
        if self.active_stage is not None:
            self.active_stage["elapsed_seconds"] = now-self.stage_at
        self.data["peak_RSS_KiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if self.budget is not None:
            b = self.budget
            self.data["monitored_rational_operations"] = b.rational_operations
            self.data["maximum_monitored_rational_bits"] = b.maximum_monitored_rational_bits
            self.data["limit_check_calls"] = b.calls
            self.data["shared_mapper_usage"] = b.shared_usage()
            self.data["rational_monitor_scope"] = (
                "calls routed through Limits.rational; not all inherited Expr arithmetic")
        if self.ring is not None:
            self.data["profile_atoms"] = len(self.ring.p.atoms)
        if self.owners:
            self.data["mappers"] = [
                {"name": name, "statistics": dict(owner.stats),
                 "primitive_calls": owner.run_primitive_calls,
                 "cache_entries": sum(len(getattr(owner, key)) for key in
                                      ("atom_cache", "monomial_cache", "primitive_cache", "shuffle_cache"))}
                for name, owner in self.owners]

    def finish(self, outcome):
        self.finish_stage()
        self.ended_at = time.perf_counter()
        self.data.update(completed=True, outcome=outcome)
        self.snapshot()
        self.data["final_receipt_frozen"] = True

    def fail(self, outcome, exc):
        self.snapshot()
        if self.active_stage is not None:
            self.active_stage["status"] = "interrupted"
        self.data.update(completed=False, outcome=outcome,
                         error_type=type(exc).__name__, error=str(exc))
        try:
            if isinstance(exc, InterfaceFailure) and exc.evidence:
                payload = exc.evidence
                payload_raw = canonical(payload)
                identity = {"bytes": len(payload_raw), "sha256": sha(payload_raw)}
                self.data["failure_evidence_identity"] = identity
                try:
                    self.record("unresolved_exact_evidence", payload)
                    identity["emitted"] = True
                except OutputBudgetExceeded as cap:
                    identity["emitted"] = False
                    self.data["secondary_stdout_error"] = str(cap)
        finally:
            self.ended_at = time.perf_counter()
            self.snapshot()
            self.data["final_receipt_frozen"] = True


def add(out, key, value, budget=None):
    value = F(value)
    if budget is not None:
        value = budget.rational(value)
    value += out.get(key, F(0))
    if budget is not None:
        value = budget.rational(value)
    if value:
        out[key] = value
    else:
        out.pop(key, None)


def combine_vectors(vectors, coefficients, budget):
    out = {}
    for index, coefficient in sorted(coefficients.items()):
        for key, value in vectors[index].items():
            add(out, key, coefficient * value, budget)
        budget.check()
    return out


def vector_rows(vector):
    return [[index, str(value)] for index, value in sorted(vector.items()) if value]


class ExactSpace:
    """One rational column space; retain all original-coordinate null relations."""
    def __init__(self, columns, budget, completed_column=None, started_column=None):
        self.columns, self.budget = columns, budget
        self.basis, self.independent, self.kernel = {}, [], []
        for index, column in enumerate(columns):
            if started_column is not None:
                started_column(index)
            value, rep = dict(column), {index: F(1)}
            while value:
                budget.check()
                pivot = min(value)
                if pivot not in self.basis:
                    scale = value[pivot]
                    value = {k: budget.rational(v / scale) for k, v in value.items()}
                    rep = {k: budget.rational(v / scale) for k, v in rep.items()}
                    self.basis[pivot] = (value, rep)
                    self.independent.append(index)
                    break
                row, relation = self.basis[pivot]
                scale = value[pivot]
                self.subtract(value, row, scale)
                self.subtract(rep, relation, scale)
            if not value:
                self.kernel.append(rep)
            if completed_column is not None:
                completed_column(index, value, rep, list(self.independent), len(self.kernel))

    def subtract(self, target, source, scale):
        for key, value in source.items():
            add(target, key, -scale * value, self.budget)
        self.budget.check()

    def reduce(self, target):
        residual, coefficients = dict(target), {}
        for pivot in sorted(self.basis):
            if pivot not in residual:
                continue
            row, relation = self.basis[pivot]
            scale = residual[pivot]
            self.subtract(residual, row, scale)
            for index, value in relation.items():
                add(coefficients, index, scale * value, self.budget)
        if combine_vectors(self.columns, coefficients, self.budget) != {
                k: target.get(k, F(0)) - residual.get(k, F(0))
                for k in set(target) | set(residual)
                if target.get(k, F(0)) != residual.get(k, F(0))}:
            raise AssertionError("fresh exact column reconstruction failed")
        return coefficients, residual

    def annihilators(self, dimension, completed_annihilator=None):
        pivots = set(self.basis)
        out = []
        for free in range(dimension):
            if free in pivots:
                continue
            value = {free: F(1)}
            for pivot in sorted(self.basis, reverse=True):
                row = self.basis[pivot][0]
                coefficient = -sum((c * value.get(k, F(0))
                                    for k, c in row.items() if k != pivot), F(0))
                if coefficient:
                    value[pivot] = self.budget.rational(coefficient)
            for column in self.columns:
                if sum((c * column.get(k, F(0)) for k, c in value.items()), F(0)):
                    raise AssertionError("fresh current annihilator pairing failed")
            out.append(value)
            if completed_annihilator is not None:
                completed_annihilator(len(out)-1, value)
        return out


def source_identity(request, repo):
    if request.get("schema") != SCHEMA or request.get("repository") != REPOSITORY:
        raise ValueError("wrong request schema or repository")
    if request.get("entry_point") != ENTRY or request.get("domain") != DOMAIN:
        raise ValueError("the frozen one-observation domain changed")
    if request.get("limits") != LIMITS:
        raise ValueError("finite limits differ from the reviewed request")
    manifest = request.get("source_manifest")
    if not isinstance(manifest, list):
        raise ValueError("source manifest is required")
    expected_paths = {TOPIC + "/scripts/" + name for name in DEPENDENCIES}
    expected_paths.update({ENTRY, TOPIC + "/notes/complete-response-self-current-design-20261116.md",
                           TOPIC + "/scripts/read_original_actions_log.py", WORKFLOW})
    if {entry.get("path") for entry in manifest} != expected_paths or len(manifest) != len(expected_paths):
        raise ValueError("source manifest must contain the exact six dependencies, driver, design, rule reader and workflow")
    rows = []
    for item in sorted(manifest, key=lambda v: v["path"]):
        path = (repo / item["path"]).resolve()
        if repo not in path.parents or not path.is_file():
            raise ValueError("source path escapes the repository")
        raw = path.read_bytes()
        found = {"path": item["path"], "bytes": len(raw), "sha256": sha(raw)}
        if found != item:
            raise ValueError("pinned source bytes/hash mismatch: " + item["path"])
        name = path.name
        if name in DEPENDENCIES and (len(raw), sha(raw)) != DEPENDENCIES[name]:
            raise ValueError("a frozen algebra/helper dependency changed")
        if name == "read_original_actions_log.py" and (len(raw), sha(raw)) != RULE_READER:
            raise ValueError("the paid rule-reader source changed")
        rows.append(found)
    if request.get("source_sha256") != {item["path"]: item["sha256"] for item in rows}:
        raise ValueError("workflow and driver source bindings disagree")
    return rows


def load_algebra():
    global selfmap, priority, colored, exact
    import literature_full_self_euler_coordinates as selfmap
    priority = selfmap.priority
    colored, exact = priority.colored, priority.exact


def make_budget(seconds, development=False):
    class MonitoredLimits(exact.Limits):
        def __init__(self):
            self.monitored_owners = []
            self.shared_primitive_peak = 0
            self.shared_cache_peak = 0
            super().__init__(
                seconds=seconds, nodes=LIMITS["nodes"], atoms=LIMITS["atoms"],
                terms=LIMITS["terms"], rewrites=LIMITS["word_calls"],
                memory_mib=LIMITS["memory_mib"], rational_bits=LIMITS["rational_bits"])
            self.rational_operations = 0
            self.maximum_monitored_rational_bits = 0

        def shared_usage(self):
            calls = sum(owner.run_primitive_calls for owner in self.monitored_owners)
            caches = sum(len(getattr(owner, key)) for owner in self.monitored_owners
                         for key in ("atom_cache", "monomial_cache", "primitive_cache", "shuffle_cache"))
            self.shared_primitive_peak = max(self.shared_primitive_peak, calls)
            self.shared_cache_peak = max(self.shared_cache_peak, caches)
            return {
                "primitive_calls": calls, "cache_entries": caches,
                "primitive_calls_peak": self.shared_primitive_peak,
                "cache_entries_peak": self.shared_cache_peak,
                "primitive_call_limit": LIMITS["word_calls"],
                "cache_entry_limit": LIMITS["cache_entries"],
                "primitive_overshoot": max(0, self.shared_primitive_peak-LIMITS["word_calls"]),
                "cache_overshoot": max(0, self.shared_cache_peak-LIMITS["cache_entries"]),
                "scope": "sum_across_all_new_and_fresh_mappers_in_this_phase"}

        def check(self):
            usage = self.shared_usage()
            if usage["primitive_calls"]>LIMITS["word_calls"]:
                raise exact.formal.CompilationBudgetExceeded("aggregate new/fresh primitive call ceiling")
            if usage["cache_entries"]>LIMITS["cache_entries"]:
                raise exact.formal.CompilationBudgetExceeded("aggregate new/fresh cache entry ceiling")
            super().check()

        def rational(self, value):
            self.rational_operations += 1
            value = F(value)
            self.maximum_monitored_rational_bits = max(
                self.maximum_monitored_rational_bits,
                value.numerator.bit_length(), value.denominator.bit_length())
            if self.rational_operations > LIMITS["monitored_rational_operations"]:
                raise exact.formal.CompilationBudgetExceeded("new monitored rational operation ceiling")
            return super().rational(value)
    return MonitoredLimits()


def mapper(ring):
    class SharedGuardPriority(priority.PriorityWords):
        def cache_guard(self):
            # Observe the actual size before the inherited guard can undo a
            # failed insertion. The finite-fail receipt retains any overshoot.
            ring.limits.shared_usage()
            super().cache_guard()
            ring.limits.check()
    result = SharedGuardPriority(
        ring, max_calls=LIMITS["word_calls"], max_terms=LIMITS["terms"],
        max_weight=4, max_shuffle_entries=LIMITS["cache_entries"],
        max_cache_entries=LIMITS["cache_entries"], color_order=("q",))
    ring.limits.monitored_owners.append(result)
    ring.limits.check()
    return result


def local_expression_rows(ring, expr):
    result = {}
    for (power, atoms), value in expr.terms.items():
        jets = []
        for index in atoms:
            atom = ring.p.atoms[index]
            if atom[0] != "jet" or atom[1] != "q":
                raise InterfaceFailure("a local source expression contains an integral or another color")
            jets.append(atom[2])
        add(result, (power, tuple(sorted(jets))), value)
    return selfmap.local_rows(result)


def plain_local(words, evidence_name):
    out = {}
    remainder = {}
    for (local, word), value in words.terms.items():
        if word:
            remainder[(local, word)] = value
        else:
            power, jets = selfmap.plain_letter(local)
            add(out, (power, jets), value)
    if remainder:
        raise InterfaceFailure(evidence_name + " retains genuine right words", {
            "complete_word_rows": priority.rows(words)})
    return out


def frechet_delta(ring, triple):
    a, b, c = triple
    x, u, p = ring.x(), ring.color("q"), ring.color("q", 1)
    direction = x*x*p - 2*x*u
    return (
        x*x*a.D() - 2*x*a - ring.variation(a, direction),
        x*x*b.D() + 2*x*b + 2*a.D() - ring.variation(b, direction),
        x*x*c.D() + 6*x*c + 2*b.D() - ring.variation(c, direction),
    )


def original_operators(ring):
    """Published R258 recurrence and R261 full a,d,c tables, not old roots."""
    x = ring.x()
    u, p, r, t, j4, j5 = (ring.color("q", j) for j in range(6))
    zero = ring.number(0)
    H = (6*p*t - 2*r*r, -6*(r*t).D(), zero)
    J = (-4*(p*p + u*r), 12*r*r + 8*p*t - 4*u*j4,
         8*t*t + 12*r*j4 + 4*p*j5)
    values = {}
    for i in range(7):
        values["H%d" % i] = H
        if i != 6:
            H = frechet_delta(ring, H)
    for i in range(3):
        values["J%d" % i] = J
        if i != 2:
            J = frechet_delta(ring, J)

    barred = {
        30: (
            -3*u*t-2*p*r+x*(-3*p*t+r*r),
            -3*u*j5-14*p*j4+2*r*t+x*(-3*p*j5-r*j4+2*t*t),
            3*r*j5+9*t*j4),
        32: (
            4*u*r+6*x*u*t+x*x*(-3*p*t+r*r),
            18*u*j4+12*p*t+x*(6*u*j5-4*r*t)+x*x*(-3*p*j5-r*j4+2*t*t),
            -2*p*j5-22*r*j4-20*t*t+x*(-6*r*j5-18*t*j4)),
        34: (
            4*u*r+18*x*u*t+x*x*(-9*p*t+3*r*r),
            38*u*j4+28*p*t+x*(18*u*j5-12*r*t)+x*x*(-9*p*j5-3*r*j4+6*t*t),
            2*p*j5-42*r*j4-44*t*t+x*(-18*r*j5-54*t*j4)),
        37: (
            -8*x*u*r+x*x*(-36*u*t+12*p*r)+x**3*(24*p*t-8*r*r),
            -64*u*t+x*(-136*u*j4+16*p*t)+x*x*(-36*u*j5+84*p*j4+24*r*t)
                +x**3*(24*p*j5+8*r*j4-16*t*t),
            -40*p*j4+80*r*t+x*(-16*p*j5+144*r*j4+160*t*t)
                +x*x*(36*r*j5+108*t*j4)),
        40: (
            4*x*x*u*r+x**3*(12*u*t-4*p*r)+x**4*(-6*p*t+2*r*r),
            64*x*u*t+x*x*(68*u*j4-8*p*t)+x**3*(12*u*j5-28*p*j4-8*r*t)
                +x**4*(-6*p*j5-2*r*j4+4*t*t),
            32*p*t+x*(40*p*j4-80*r*t)+x*x*(8*p*j5-72*r*j4-80*t*t)
                +x**3*(-12*r*j5-36*t*j4)),
        100: (
            -32*u*p+64*x*u*r+x*x*(48*u*t-32*p*r)+x**3*(-48*p*t+16*r*r),
            256*u*t+x*(288*u*j4-128*p*t)+x*x*(48*u*j5-224*p*j4-32*r*t)
                +x**3*(-48*p*j5-16*r*j4+32*t*t),
            -64*p*j4-320*r*t+x*(-32*p*j5-352*r*j4-320*t*t)
                +x*x*(-48*r*j5-144*t*j4)),
        104: (
            96*u*u-64*x*u*p+x*x*(-32*u*r-32*p*p)+x**3*(-192*u*t+96*p*r)
                +x**4*(120*p*t-40*r*r),
            -832*x*u*t+x*x*(-1024*u*j4+608*p*t)+x**3*(-192*u*j5+672*p*j4+128*r*t)
                +x**4*(120*p*j5+40*r*j4-80*t*t),
            -96*u*j4-768*p*t+x*(-768*p*j4+1088*r*t)
                +x*x*(-160*p*j5+1056*r*j4+1216*t*t)+x**3*(192*r*j5+576*t*j4)),
        109: (
            -64*x*x*u*p+x**3*(64*u*r+64*p*p)+x**4*(192*u*t-96*p*r)
                +x**5*(-96*p*t+32*r*r),
            1792*x*x*u*t+x**3*(1408*u*j4-768*p*t)
                +x**4*(192*u*j5-672*p*j4-128*r*t)+x**5*(-96*p*j5-32*r*j4+64*t*t),
            2048*x*p*t+x*x*(1472*p*j4-2048*r*t)
                +x**3*(192*p*j5-1472*r*j4-1664*t*t)+x**4*(-192*r*j5-576*t*j4)),
    }
    for index, (a_bar, d_bar, c_bar) in barred.items():
        a = a_bar/256
        values["chi%d" % index] = (a, d_bar/256-a.D().D(), c_bar/256)
    if tuple(values) != Z_ORDER:
        raise AssertionError("original Z-label order changed")
    return values


def quadratic_operators(ring):
    x, u, p, r = ring.x(), ring.color("q"), ring.color("q", 1), ring.color("q", 2)
    J0, J1, J2 = (r*r).J(), (x*r*r).J(), (x*x*r*r+2*p*p).J()
    q = {
        "P": J0, "R": p*p+x*J0, "S": J1,
        "L": u*p-x*p*p/2-x*x*J0/4+J2/4,
        "U": x*p*p+x*J1+J2/2,
        "V": -u*u/2+x*u*p-x*x*p*p/2-x*x*J1/4,
        "T": x*x*p*p+x*J2,
        "Y": -x*u*u+x*x*u*p-x**3*p*p/2-x*x*J2/4,
    }
    z, one = ring.number(0), ring.number(1)
    tails = {
        "P": (one, z, z), "R": (x, z, z), "S": (z, one, z),
        "L": (-x*x/4, z, one/4), "U": (z, x, one/2),
        "V": (z, -x*x/4, z), "T": (z, z, x), "Y": (z, z, -x*x/4),
    }
    weights = {"P": -3, "R": -2, "S": -2, "L": -1,
               "U": -1, "V": 0, "T": 0, "Y": 1}
    return q, tails, weights


def z_weight(label):
    if label.startswith("H"):
        return -5+int(label[1:])
    if label.startswith("J"):
        return -3+int(label[1:])
    return {30: -4, 32: -3, 34: -3, 37: -2, 40: -1,
            100: -2, 104: -1, 109: 0}[int(label[3:])]


def map_Q(raw, word_owner, budget, weight=None):
    whole = word_owner.expression(raw)
    left = selfmap.left_coefficient(whole, 0, maximum_power=0)
    result = selfmap.split_self(left, budget, true_cost_weight=weight)
    result["whole_word_rows"] = priority.rows(whole)
    result["left_word_rows"] = selfmap.word_rows(left)
    return result


def public_Q(result):
    return {
        "ordered_matrix": [[str(v) for v in row] for row in result["matrix"]],
        "local_density": selfmap.local_rows(result["local"]),
        "complete_Euler": selfmap.local_rows(result["euler"]),
        "coordinates": selfmap.coordinate_rows(result["coordinates"]),
        "whole_word_rows": result["whole_word_rows"],
        "left_word_rows": result["left_word_rows"],
        "complete_reconstruction_zero": result["complete_reconstruction_zero"],
        "full_self_function_zero": result["full_self_function_zero"],
    }


def expression_sum(ring, expressions, coefficients):
    out = ring.number(0)
    for index, coefficient in sorted(coefficients.items()):
        out += coefficient*expressions[index]
        ring.limits.check()
    return out


def af_polynomial(local, name):
    """Only t=r^2/(3p); no derivative of the root identity is imposed."""
    out = {}
    for (power, jets), value in local.items():
        if any(j > 3 for j in jets):
            raise InterfaceFailure(name+" has a surviving higher jet", {
                "local_current": selfmap.local_rows(local)})
        n0, n1, n2, n3 = (jets.count(j) for j in range(4))
        if sum((n0, n1, n2, n3)) != 3:
            raise InterfaceFailure(name+" is not a cubic current")
        add(out, (power, n0, n1-n3, n2+2*n3), value/F(3)**n3)
    if any(power < 0 or min(n0, n1, n2) < 0
           for power, n0, n1, n2 in out):
        raise InterfaceFailure(name+" retains an unproved denominator", {
            "Af_Laurent_rows": [[list(k), str(v)] for k, v in sorted(out.items())]})
    return out


def poly_add_scaled(out, poly, coefficient):
    for key, value in poly.items():
        add(out, key, coefficient*value)


def formal_basis():
    """R433 full six canonical representatives, including p-only terms."""
    def polynomial(rows):
        return {tuple(key): F(value) for key, value in rows if F(value)}
    six = [
        polynomial([((0,1,2,0),1),((1,0,3,0),-2),((2,0,2,1),3),((3,0,1,2),"-4/3")]),
        polynomial([((1,1,2,0),-2),((2,1,1,1),3),((3,1,0,2),"-1/3"),
                    ((2,0,3,0),2),((3,0,2,1),-4),((4,0,1,2),"5/3")]),
        polynomial([((0,3,0,0),"2/3"),((2,1,2,0),-2),((3,1,1,1),2),
                    ((4,1,0,2),"-1/6"),((3,0,3,0),"4/3"),
                    ((4,0,2,1),-2),((5,0,1,2),"2/3")]),
        polynomial([((0,1,1,1),-1),((1,1,0,2),"1/3"),((0,0,3,0),"2/3"),
                    ((2,0,1,2),"-2/3")]),
        polynomial([((0,1,2,0),"1/2"),((1,1,1,1),-1),((2,1,0,2),"1/6"),
                    ((1,0,3,0),-1),((2,0,2,1),"5/2"),((3,0,1,2),"-4/3")]),
        polynomial([((0,1,0,2),"-1/6"),((1,0,1,2),"2/3")]),
    ]
    seven = [polynomial([(key,1)]) for key in (
        (0,0,3,0),(0,0,2,1),(1,0,2,1),(0,0,1,2),(1,0,1,2),(2,0,1,2))]
    seven.append(polynomial([((1,0,3,0),2),((2,0,2,1),-5),((3,0,1,2),3)]))
    return six+seven


def decompose_current(poly):
    def get(key):
        return poly.get(key, F(0))
    A2 = F(3,2)*get((0,3,0,0))
    B0 = -get((0,1,1,1))
    B1 = -get((1,1,1,1))
    A1 = get((2,1,1,1))/3
    C0 = -6*get((0,1,0,2))
    A0 = get((0,1,2,0))-B1/2
    coordinates = [A0,A1,A2,B0,B1,C0]
    basis = formal_basis()
    residual = dict(poly)
    for coefficient, column in zip(coordinates,basis[:6]):
        poly_add_scaled(residual,column,-coefficient)
    keys = ((0,0,3,0),(0,0,2,1),(1,0,2,1),
            (0,0,1,2),(1,0,1,2),(2,0,1,2))
    ponly = [residual.get(key,F(0)) for key in keys]
    ponly.append(residual.get((1,0,3,0),F(0))/2)
    for coefficient,column in zip(ponly,basis[6:]):
        poly_add_scaled(residual,column,-coefficient)
    if residual:
        raise InterfaceFailure("current is outside the proved full thirteen-coordinate space", {
            "Af_current": [[list(k),str(v)] for k,v in sorted(poly.items())],
            "full_reconstruction_residual": [[list(k),str(v)] for k,v in sorted(residual.items())]})
    return coordinates+ponly


def original_combination_rows(combination, labels):
    return [[labels[i],str(v)] for i,v in sorted(combination.items()) if v]


def current_record(ring, operators, tails, labels, combination, owner, fresh_owner,
                   completed_moment=None, started_moment=None):
    x,u,p,r = ring.x(),ring.color("q"),ring.color("q",1),ring.color("q",2)
    records, flat = [], {}
    for moment in range(3):
        if started_moment is not None:
            started_moment(moment)
        integrand = ring.number(0)
        pre = ring.number(0)
        second_source = ring.number(0)
        for index, coefficient in sorted(combination.items()):
            ename,zname = labels[index]
            a,b,c = operators[zname]
            w = tails[ename][moment]
            h = (a*r).D()+b*p
            integrand += coefficient*c*w
            pre += coefficient*(a*(p*w.D().D()-r*w.D())+w*h)
            second_source += coefficient*((a*w.D().D()).D()+b*w.D()+(c*w).I())
        primitive_words = owner.expression(integrand.I())
        primitive_local = plain_local(primitive_words,"whole-Q-kernel tail primitive")
        primitive_expr = owner.to_old(primitive_words)
        quarter = (pre+u*primitive_expr)/2
        mapped = owner.expression(quarter)
        local = plain_local(mapped,"complete quarter current")
        difference = fresh_owner.expression(quarter.D()-p*second_source/2)
        if difference.terms:
            raise InterfaceFailure("fresh original Green derivative difference is nonzero", {
                "moment":moment,"difference_word_rows":priority.rows(difference)})
        polynomial = af_polynomial(local,"complete quarter current")
        coordinates = decompose_current(polynomial)
        for j,value in enumerate(coordinates):
            if value:
                flat[moment*13+j] = value
        records.append({
            "moment":moment,
            "right_tail_source":local_expression_rows(ring,integrand),
            "complete_local_tail_primitive":selfmap.local_rows(primitive_local),
            "complete_quarter_current_before_Af":selfmap.local_rows(local),
            "Af_current": [[list(k),str(v)] for k,v in sorted(polynomial.items())],
            "coordinates": [[name,str(v)] for name,v in zip(PARAMETERS,coordinates)],
            "fresh_Green_derivative_zero":True,
            "full_thirteen_coordinate_reconstruction_zero":True,
        })
        if completed_moment is not None:
            completed_moment(moment, records[-1])
    return flat,records


def development(progress):
    progress.start()
    progress.stage("initialize_development_budget_and_ring")
    budget = make_budget(LIMITS["development_seconds"], development=True)
    progress.bind(budget=budget)
    ring = colored.ColoredRing(budget)
    progress.bind(ring=ring)
    owner = mapper(ring)
    progress.bind(owners=[("development", owner)])
    progress.data["scope"] = "exactly_two_new_adapter_checks_no_original_targets"
    progress.data["checks"] = {}
    progress.stage("manufactured_full_Green_with_nonzero_c_and_true_constant_tail")
    x,u,p,r = ring.x(),ring.color("q"),ring.color("q",1),ring.color("q",2)
    a,b,c = ring.number(0),u*u,-2*p*p-u*r
    w = 1+x+x*x
    h = (a*r).D()+b*p
    second = (a*w.D().D()).D()+b*w.D()+(c*w).I()
    current = 2*(a*(p*w.D().D()-r*w.D())+w*h+u*(c*w).I())
    if owner.expression(current.D()-2*p*second).terms:
        raise AssertionError("new manufactured Green derivative/anchor check failed")
    constant_current = 2*(h+u*c.I())
    expected = -2*u*(p*p).I()
    if owner.expression(constant_current-expected).terms:
        raise AssertionError("new manufactured constant-tail sign check failed")
    retained = owner.expression(expected)
    if not any(word for local,word in retained.terms):
        raise AssertionError("the manufactured nonlocal tail was silently discarded")
    progress.data["checks"]["manufactured_full_Green_with_nonzero_c_and_true_constant_tail"] = True
    progress.unit("adapter_checks", "manufactured_Green")
    progress.record("adapter_check", {
        "name": "manufactured_full_Green_with_nonzero_c_and_true_constant_tail",
        "passed": True,
        "a": "0", "b": "u^2", "c": "-2p^2-u*r", "w": "1+x+x^2",
        "derivative_identity_zero": True,
        "w_equals_one_current": "-2*u*I(p^2)",
        "retained_constant_tail_words": priority.rows(retained)})
    progress.stage("one_coefficient_vector_for_joint_kernel_and_strict_image")
    qcolumns = [{0:F(1)},{0:F(1)},{}]
    qspace = ExactSpace(qcolumns,budget)
    currents = [{0:F(1)},{1:F(1)},{0:F(1),1:F(1)}]
    kernel_currents = [combine_vectors(currents,v,budget) for v in qspace.kernel]
    space = ExactSpace(kernel_currents,budget)
    coefficient,residual = space.reduce({0:F(1)})
    if residual:
        raise AssertionError("new synthetic simultaneous target unexpectedly unresolved")
    original = combine_vectors(qspace.kernel,coefficient,budget)
    if combine_vectors(qcolumns,original,budget) or combine_vectors(currents,original,budget)!={0:F(1)}:
        raise AssertionError("different synthetic coefficients were used for Q/current")
    strict = ExactSpace(kernel_currents[:1],budget)
    _,missing = strict.reduce({0:F(1)})
    annihilators = strict.annihilators(2)
    if not missing or not any(v.get(0,F(0)) for v in annihilators):
        raise AssertionError("new synthetic strict-image certificate failed")
    progress.data["checks"]["one_coefficient_vector_for_joint_kernel_and_strict_image"] = True
    progress.unit("adapter_checks", "synthetic_joint_kernel")
    progress.record("adapter_check", {
        "name": "one_coefficient_vector_for_joint_kernel_and_strict_image",
        "passed": True,
        "joint_input": {"Q": [vector_rows(v) for v in qcolumns],
                        "current": [vector_rows(v) for v in currents]},
        "joint_original_certificate": vector_rows(original),
        "strict_image_residual": vector_rows(missing),
        "strict_image_annihilators": [vector_rows(v) for v in annihilators]})
    budget.formal.time_check()
    progress.data["all_passed"] = True
    progress.finish("all_two_new_adapter_checks_passed")


def science(request, progress):
    progress.start()
    progress.stage("initialize_science_budget_and_ring")
    budget = make_budget(LIMITS["seconds"])
    progress.bind(budget=budget)
    ring = colored.ColoredRing(budget)
    progress.bind(ring=ring)
    owner,fresh = mapper(ring),mapper(ring)
    progress.bind(owners=[("new",owner),("fresh",fresh)])
    progress.data["definitions"] = {
        "I": "integral_from_common_right_endpoint_to_x",
        "Q": "-1/4 integral c_tau Phi_E(u,u)",
        "current": "K/4 = 1/2*(a*(p*wpp-r*wp)+w*((a*r)prime+b*p)+u*I(c*w))",
        "root_relation_only": "t=r^2/(3*p), p nonzero; no differentiated Af relation",
        "formal_coordinate_order": list(PARAMETERS),
        "actual_C_conversion": "C_i=a_i^3*K(n_i), with the same suffix n_i and original common cost"}
    progress.data["scope_boundaries"] = {
        "old_pure_or_diagonal_or_operator_rank_executions": 0,
        "old_fourth_forcing_compilations": 0,
        "old_development_suite_executions": 0,
        "profile_or_Af_point_evaluations": 0,
        "concrete_root_configuration_rank_claimed": False,
        "full_response_kernel_image_claimed": False,
        "signed_image_is_actual_control": False,
        "actual_joint_period_resolved": False,
        "same_gauge_thirteen_rows_resolved": False,
        "all_genuine_right_constants_and_left_tails_retained": True}
    progress.stage("published_local_input_assembly")
    operators = original_operators(ring)
    q,tails,eweights = quadratic_operators(ring)
    labels=[(e,z) for z in Z_ORDER for e in E_ORDER]
    raw_Q=[(operators[z][2]*q[e]).I()/4 for e,z in labels]
    for z in Z_ORDER:
        source_operator = {
            "label":z,"true_weight":z_weight(z),
            "a":local_expression_rows(ring,operators[z][0]),
            "b":local_expression_rows(ring,operators[z][1]),
            "c":local_expression_rows(ring,operators[z][2])}
        progress.unit("assembled_original_operators", z)
        progress.record("original_operator", source_operator)
    progress.record("original_cost_labels", [list(v) for v in labels])

    progress.stage("new_complete_Q_mapping")
    Qresults=[]
    for index,((e,z),raw) in enumerate(zip(labels,raw_Q)):
        progress.data["active_input"]={"kind":"complete_Q_column","index":index,"label":[e,z]}
        result=map_Q(raw,owner,budget,eweights[e]+z_weight(z))
        Qresults.append(result)
        progress.unit("complete_Q_columns", index)
        progress.record("complete_Q_column", {
            "index":index,"label":[e,z],"true_cost_weight":eweights[e]+z_weight(z),
            **public_Q(result)})
    Qkeys=sorted(set().union(*(set(item["coordinates"]) for item in Qresults)))
    Qpositions={key:i for i,key in enumerate(Qkeys)}
    Qcolumns=[{Qpositions[k]:v for k,v in item["coordinates"].items()} for item in Qresults]
    progress.record("complete_Q_coordinate_labels", [selfmap.coordinate_label(key) for key in Qkeys])

    progress.stage("new_joint_Q_kernel")
    def Q_column_done(index, value, rep, independent, kernel_count):
        progress.unit("Q_elimination_columns",index)
        progress.data["Q_elimination_partial"]={
            "columns_completed":index+1,"pivot_count":len(independent),"kernel_count":kernel_count}
        payload={"input_column":index,"label":list(labels[index]),
                 "kind":"pivot" if value else "kernel_relation",
                 "pivot_coordinate":min(value) if value else None,
                 "original_combination":original_combination_rows(rep,labels)}
        if value:
            payload["normalized_coordinate_fingerprint"]=sha(canonical(vector_rows(value)))
        else:
            payload["kernel_index"]=kernel_count-1
            payload["fresh_coordinate_reconstruction_pending"]=True
        progress.record("Q_elimination_step",payload)
    def Q_column_start(index):
        progress.data["active_input"]={"kind":"Q_elimination_column","index":index}
        progress.snapshot()
    Qspace=ExactSpace(Qcolumns,budget,completed_column=Q_column_done,
                      started_column=Q_column_start)
    progress.data["new_joint_Q_pivot_columns"]=list(Qspace.independent)
    progress.data["new_joint_Q_kernel_dimension"]=len(Qspace.kernel)
    for index,relation in enumerate(Qspace.kernel):
        progress.data["active_input"]={"kind":"Q_kernel_verification","kernel_index":index}
        if combine_vectors(Qcolumns,relation,budget):
            raise AssertionError("fresh complete Q-kernel relation failed")
        progress.unit("verified_Q_kernel_relations",index)
        progress.record("Q_kernel_coordinate_verification",{
            "kernel_index":index,"complete_coordinate_reconstruction_zero":True})

    progress.stage("new_complete_kernel_currents")
    current_vectors=[]
    for index,relation in enumerate(Qspace.kernel):
        progress.data["active_input"]={"kind":"kernel_current","kernel_index":index}
        def moment_done(moment, record):
            progress.unit("kernel_current_moments",[index,moment])
            progress.record("kernel_current_moment",{
                "kernel_index":index,"moment":moment,**record})
        def moment_start(moment):
            progress.data["active_input"]={"kind":"kernel_current","kernel_index":index,"moment":moment}
            progress.snapshot()
        vector,_=current_record(ring,operators,tails,labels,relation,owner,fresh,
                                completed_moment=moment_done,started_moment=moment_start)
        current_vectors.append(vector)
        progress.unit("complete_kernel_current_columns",index)
        progress.record("complete_kernel_current_column",{
            "kernel_index":index,
            "original_combination":original_combination_rows(relation,labels),
            "complete_Q_coordinates_zero":True,
            "all_three_moments_emitted":True,
            "complete_current_coordinates":vector_rows(vector)})

    progress.stage("new_complete_current_image")
    def image_column_done(index,value,rep,independent,kernel_count):
        progress.unit("current_image_elimination_columns",index)
        progress.data["current_image_partial"]={
            "columns_completed":index+1,"pivot_count":len(independent),"kernel_count":kernel_count}
        progress.record("current_image_elimination_step",{
            "kernel_index":index,"kind":"pivot" if value else "dependent",
            "pivot_coordinate":min(value) if value else None,
            "kernel_column_combination":vector_rows(rep),
            "normalized_coordinate_fingerprint":sha(canonical(vector_rows(value)))})
    def image_column_start(index):
        progress.data["active_input"]={"kind":"current_image_elimination_column","kernel_index":index}
        progress.snapshot()
    image=ExactSpace(current_vectors,budget,completed_column=image_column_done,
                     started_column=image_column_start)
    progress.data["complete_current_image_basis_kernel_indices"]=list(image.independent)
    progress.data["complete_current_image_dimension"]=len(image.independent)
    def annihilator_done(index,value):
        progress.unit("complete_current_annihilators",index)
        progress.record("complete_current_annihilator",{
            "index":index,"complete_39_coordinates":vector_rows(value),
            "all_kernel_current_pairings_zero":True})
    progress.data["active_input"]={"kind":"current_image_annihilators"}
    annihilators=image.annihilators(39,completed_annihilator=annihilator_done)
    for annihilator in annihilators:
        if any(index%13>=6 for index in annihilator):
            raise InterfaceFailure("joint image contradicts the published p-only lifting interface",{
                "annihilator":vector_rows(annihilator),
                "interpretation":"source_interface_unresolved_not_new_R432_obstruction"})
    progress.data["u_quotient_image_dimension"]=len(image.independent)-21
    progress.data["published_p_only_lifting_interface_consistent"]=True
    targets=[]
    pending={}
    for moment in range(3):
        for parameter in range(6):
            progress.data["active_input"]={
                "kind":"formal_u_target","moment":moment,"parameter":PARAMETERS[parameter]}
            unit={13*moment+parameter:F(1)}
            coefficients,residual=image.reduce(unit)
            original=combine_vectors(Qspace.kernel,coefficients,budget)
            witness=None
            if residual:
                witness=next((v for v in annihilators
                              if v.get(13*moment+parameter,F(0))),None)
                if witness is None:
                    raise AssertionError("nonmember has no exact separating annihilator")
            else:
                pending[tuple(sorted(original.items()))]=(original,unit)
            target={
                "moment":moment,"parameter":PARAMETERS[parameter],
                "coordinate_outcome":"MEMBER" if not residual else "NOT_IN_THIS_144_COLUMN_Q_KERNEL",
                "member_fresh_original_source_certificate_pending":not bool(residual),
                "original_combination":original_combination_rows(original,labels),
                "complete_current_residual":vector_rows(residual),
                "separating_annihilator":None if witness is None else vector_rows(witness)}
            targets.append(target)
            progress.unit("formal_targets",[moment,PARAMETERS[parameter]])
            progress.record("formal_target_coordinate_result",target)
    for kernel_index in image.independent:
        original=Qspace.kernel[kernel_index]
        pending.setdefault(tuple(sorted(original.items())),(original,current_vectors[kernel_index]))
    progress.data["required_distinct_fresh_source_certificates"]=len(pending)

    progress.stage("fresh_new_joint_certificates")
    for index,(original,expected) in enumerate(pending.values()):
        progress.data["active_input"]={"kind":"fresh_joint_source_certificate","index":index}
        qraw=expression_sum(ring,raw_Q,original)
        result=map_Q(qraw,fresh,budget)
        progress.unit("fresh_complete_Q_source_results",index)
        progress.record("fresh_complete_Q_source",{
            "certificate_index":index,
            "original_combination":original_combination_rows(original,labels),
            "complete_Q":public_Q(result)})
        if result["coordinates"]:
            raise InterfaceFailure("fresh original Q source reconstruction is nonzero",{
                "certificate_index":index,"Q_record_already_emitted":True})
        def certificate_moment_done(moment,record):
            progress.unit("fresh_current_source_moments",[index,moment])
            progress.record("fresh_current_source_moment",{
                "certificate_index":index,"moment":moment,**record})
        def certificate_moment_start(moment):
            progress.data["active_input"]={
                "kind":"fresh_joint_source_certificate","index":index,"moment":moment}
            progress.snapshot()
        observed,_=current_record(ring,operators,tails,labels,original,fresh,owner,
                                  completed_moment=certificate_moment_done,
                                  started_moment=certificate_moment_start)
        if observed!=expected:
            raise InterfaceFailure("fresh complete current source certificate failed",{
                "certificate_index":index,"observed":vector_rows(observed),
                "expected":vector_rows(expected)})
        progress.unit("fresh_joint_source_certificates",index)
        progress.record("fresh_joint_source_certificate",{
            "certificate_index":index,
            "original_combination":original_combination_rows(original,labels),
            "fresh_complete_current_coordinates":vector_rows(observed),
            "fresh_Q_and_three_current_records_already_emitted":True,
            "Q_and_all_current_reconstructions_zero":True})
    budget.formal.time_check()
    progress.data["active_input"]=None
    progress.data["all_required_fresh_source_certificates_completed"]=True
    progress.data["formal_target_summary"]=[
        {"moment":target["moment"],"parameter":target["parameter"],
         "outcome":target["coordinate_outcome"]} for target in targets]
    outcome="all_eighteen_formal_targets_lift" if all(
        target["coordinate_outcome"]=="MEMBER" for target in targets
    ) else "strict_current_image_in_this_original_module"
    progress.finish(outcome)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--request",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("only the reviewed public Actions entry may execute this new observation")
    repo=Path(__file__).resolve().parents[3]
    request_path=Path(args.request).resolve()
    raw=request_path.read_bytes()
    request=json.loads(raw)
    identities=source_identity(request,repo)
    out=Path(args.out).resolve()
    if repo==out or repo in out.parents:
        raise ValueError("machine output must remain outside the Git checkout")
    out.parent.mkdir(parents=True,exist_ok=True)
    journal=OutputJournal(out.with_suffix(".records.jsonl"))
    dev=PhaseProgress("development",journal)
    scientific=PhaseProgress("science",journal)
    started=time.perf_counter()
    report={
        "schema":SCHEMA,"repository":REPOSITORY,
        "run_id":os.environ.get("GITHUB_RUN_ID"),
        "run_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
        "workflow_source":os.environ.get("GITHUB_SHA"),
        "request":{"bytes":len(raw),"sha256":sha(raw)},
        "source_manifest":identities,
        "domain":DOMAIN,"limits":LIMITS,
        "development":dev.data,"science":scientific.data,
        "old_science_executions":0,
        "actual_joint_period_resolved":False,
        "report_payloads_are_emitted_once_as_sequential_records":True,
    }
    exit_code=0
    phase=None
    try:
        load_algebra()
        phase=dev
        development(dev)
        phase=scientific
        science(request,scientific)
        report["entry_outcome"]="complete_new_observation"
    except Exception as exc:
        if isinstance(exc,InterfaceFailure):
            exit_code,outcome=2,"unresolved_structural_interface"
        elif isinstance(exc,OutputBudgetExceeded):
            exit_code,outcome=3,"finite_stdout_budget_failure"
        elif "exact" in globals() and isinstance(exc,exact.formal.CompilationBudgetExceeded):
            exit_code,outcome=3,"finite_budget_failure"
        else:
            exit_code,outcome=4,"entry_error"
        report["entry_outcome"]=outcome
        report["failure_phase"]=None if phase is None else phase.name
        report["entry_error"]={"type":type(exc).__name__,"message":str(exc)}
        if phase is not None:
            try:
                phase.fail(outcome,exc)
            except Exception as reporting_exc:
                # Preserve the first failure and its live counters even if an
                # evidence-file/stdout operation itself fails.
                report["secondary_reporting_error"]={
                    "type":type(reporting_exc).__name__,"message":str(reporting_exc)}
    finally:
        dev.snapshot()
        scientific.snapshot()
        journal.close()
        report["total_elapsed_seconds"]=time.perf_counter()-started
        report["peak_RSS_KiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report["record_journal"]=journal.receipt()
    encoded=canonical(report)+b"\n"
    line=b"COMPLETE_CURRENT_Q_REPORT "+encoded
    # Normally this bounded summary is far below the reserved 128 KiB. The
    # fallback removes only descriptive/duplicate metadata, never costs, stage
    # status, counters, fingerprints, development evidence identity or errors.
    if journal.stdout_bytes+len(line)+1024>LIMITS["mathematical_stdout_bytes"]:
        full=out.with_suffix(".unemitted-summary.json")
        full.write_bytes(encoded)
        identity={"runner_temporary_filename":full.name,"bytes":len(encoded),"sha256":sha(encoded)}
        report.pop("source_manifest",None)
        report["source_manifest_identity"]={
            "entries":len(identities),"bytes":len(canonical(identities)),
            "sha256":sha(canonical(identities))}
        report.pop("domain",None)
        report["domain_identity"]={"bytes":len(canonical(DOMAIN)),"sha256":sha(canonical(DOMAIN))}
        scientific.data.pop("definitions",None)
        report["entry_outcome"]="finite_stdout_budget_failure"
        report["unabridged_summary_identity"]=identity
        report["complete_mathematical_publication"]=False
        encoded=canonical(report)+b"\n"
        line=b"COMPLETE_CURRENT_Q_REPORT "+encoded
        exit_code=3
    # All unbounded mathematical rows are journal records, so no charged phase
    # or its counters are removed to satisfy this final-summary boundary.
    out.write_bytes(encoded)
    sys.stdout.buffer.write(line)
    sys.stdout.buffer.flush()
    receipt={
        "bytes":len(encoded),"sha256":sha(encoded),"exit_code":exit_code,
        "record_stdout_bytes":journal.stdout_bytes,
        "record_file_bytes":journal.file_bytes,
        "record_file_sha256":journal.file_digest.hexdigest(),
        "entry_elapsed_seconds_through_final_summary":time.perf_counter()-started}
    receipt_line=b"CURRENT_Q_REPORT_IDENTITY "+canonical(receipt)+b"\n"
    sys.stdout.buffer.write(receipt_line)
    sys.stdout.buffer.flush()
    return exit_code


if __name__=="__main__":
    raise SystemExit(main())
