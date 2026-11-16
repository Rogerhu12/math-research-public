#!/usr/bin/env python3
"""Request217 metadata-only complete necessary readback and cleanup predicate.

Original head/evidence readers select their original required scope. Full
metric necessary objects are emitted independently, never combined into a
large encoded transport. This source retains every actual role error and
unstarted address and separately records original rule/ownership receipts.
No scientific value is calculated, no acceptance is inferred, and no raw
payload is removed here.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

REPO = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "request217-complete-same-C-consumer-necessary-readback-v1"
MARKER_SCHEMA = "request217-complete-same-C-consumer-readback-marker-v1"
LIMIT = 90000
ORIGINAL_READER = "root_20261115_current_C_pruefer_positive_full453_necessary_readout.py"
ORIGINAL_READER_SHA = "34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")


def receipt(path):
    path = Path(path).resolve(strict=True); before = path.stat()
    h = hashlib.sha256(); size = 0
    with path.open("rb") as stream:
        while raw := stream.read(1048576):
            h.update(raw); size += len(raw)
    after = path.stat()
    require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
        == (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
        and size == after.st_size, "Actual metadata changed while being read")
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and all(
        a.get(k) == b.get(k) for k in ("bytes", "sha256"))


def read(path, expected=None):
    rid = receipt(path)
    require(expected is None or (rid["sha256"] == expected if isinstance(expected, str)
        else same(rid, expected)), "The actual complete metadata identity differs")
    raw = Path(rid["file"]).read_bytes()
    require(len(raw) == rid["bytes"] and hashlib.sha256(raw).hexdigest() == rid["sha256"],
        "Metadata changed after identity binding")
    return json.loads(raw), rid


def current(value):
    require(value.get("repository", REPO) == REPO
        and value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "Metadata belongs to another actual job/source")


def write(path, value):
    path = Path(path); raw = canonical(value)
    with path.open("xb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return receipt(path)


def load(path, expected, alias):
    require(receipt(path)["sha256"] == expected, "The actual metadata source differs")
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec); sys.modules[alias] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(alias, None); raise
    return module


def emit_existing(path, frame, expected_schema, source, result=None):
    value, sid = read(path); current(value)
    require(value.get("schema") == expected_schema and same(value.get("source"), source),
        "The original necessary schema/source differs")
    if result is not None:
        recorded = value.get("result", value.get("actual_complete_result", value.get("original_result")))
        require(same(recorded, result), "The necessary body points to another original result")
    if sid["bytes"] > LIMIT:
        print(json.dumps(dict(event="request217_original_necessary_body_over_budget",
            original_summary=sid, limit=LIMIT, complete_necessary_emitted=False,
            no_part_transport=True, raw_retained=True), separators=(",", ":")), flush=True)
        return sid, False, value
    raw = Path(sid["file"]).read_bytes()
    require(len(raw) == sid["bytes"] and hashlib.sha256(raw).hexdigest() == sid["sha256"],
        "Necessary bytes changed before emission")
    print("BEGIN_"+frame, flush=True)
    sys.stdout.buffer.write(raw)
    if not raw.endswith(b"\n"):
        sys.stdout.buffer.write(b"\n")
    sys.stdout.buffer.flush()
    print("END_"+frame, flush=True)
    return sid, True, value



RULE_FILE_COLUMNS = {
    "json": ["file", "identity", "necessary_original_metadata"],
    "json_readme": ["file", "identity", "README_blobs_set",
                    "necessary_original_metadata_without_README_blobs"],
    "text": ["file", "identity", "lines", "selected_error_text"],
    "literal": ["original_row"],
}
RULE_IDENTITY_COLUMNS = ["file", "bytes", "sha256"]
RULE_JSON_KEYS = {"file", "identity", "necessary_original_metadata",
                  "full_member_tree_not_exported"}
RULE_TEXT_KEYS = {"file", "identity", "lines", "selected_error_text",
                  "complete_original_text_not_exported"}
RULE_README_SCHEMAS = {"current576-rules-sync-attempt-v1",
                      "current576-rules-sync-completed-v1"}
RULE_README_PATHS = ("README.md", "topics/visible-flex-larger-amplitude/README.md")


def hex_word(value, length):
    return (type(value) is str and len(value) == length
        and all(c in "0123456789abcdef" for c in value))


def tabulate_rule_files(value):
    """Only fixed original rule-file columns and identical two-README maps.

    Other containers and unfamiliar rows remain literal. This is a necessary
    metadata representation, not compression of scientific arrays.
    """
    result = dict(value)
    phases = []
    sets = []
    lookup = {}
    counts = dict(json=0, text=0, readme_uses=0, literal=0)
    for phase in value["rule_resources"]:
        if (type(phase) is not dict
                or set(phase) != {"phase", "available", "files"}
                or phase["available"] is not True or type(phase["files"]) is not list):
            phases.append(phase)
            continue
        rows = []
        for row in phase["files"]:
            ident = row.get("identity") if type(row) is dict else None
            valid = (type(ident) is dict and set(ident) == set(RULE_IDENTITY_COLUMNS)
                and type(ident["file"]) is str and type(ident["bytes"]) is int
                and ident["bytes"] >= 0 and hex_word(ident["sha256"], 64))
            if (type(row) is dict and set(row) == RULE_JSON_KEYS and valid
                    and row["full_member_tree_not_exported"] is True):
                identity_row = [ident[k] for k in RULE_IDENTITY_COLUMNS]
                meta = row["necessary_original_metadata"]
                maps = meta.get("README_blobs") if type(meta) is dict else None
                eligible = (type(meta) is dict and type(meta.get("schema")) is str
                    and meta["schema"] in RULE_README_SCHEMAS
                    and type(maps) is dict and set(maps) == set(RULE_README_PATHS)
                    and all(hex_word(maps[k], 40) for k in RULE_README_PATHS))
                if eligible:
                    key = tuple(maps[k] for k in RULE_README_PATHS)
                    if key not in lookup:
                        lookup[key] = len(sets); sets.append(dict(maps))
                    rest = dict(meta); del rest["README_blobs"]
                    rows.append(["json_readme", row["file"], identity_row, lookup[key], rest])
                    counts["readme_uses"] += 1
                else:
                    rows.append(["json", row["file"], identity_row, meta])
                counts["json"] += 1
            elif (type(row) is dict and set(row) == RULE_TEXT_KEYS and valid
                    and row["complete_original_text_not_exported"] is True):
                rows.append(["text", row["file"],
                    [ident[k] for k in RULE_IDENTITY_COLUMNS],
                    row["lines"], row["selected_error_text"]])
                counts["text"] += 1
            else:
                rows.append(["literal", row]); counts["literal"] += 1
        phases.append(dict(phase=phase["phase"], available=True, files_table=rows))
    original = canonical(value)
    result["rule_resources"] = phases
    result["rule_file_representation"] = dict(
        schema=SCHEMA+"-fixed-rule-file-columns-v1",
        identity_columns=RULE_IDENTITY_COLUMNS, file_columns=RULE_FILE_COLUMNS,
        README_blobs_sets=sets, counts=counts,
        original_selected_ascii_identity=dict(bytes=len(original),
            sha256=hashlib.sha256(original).hexdigest()),
        omitted_true_fields=dict(json="full_member_tree_not_exported",
            json_readme="full_member_tree_not_exported",
            text="complete_original_text_not_exported"),
        all_other_objects_and_unfamiliar_rows_kept_literal=True,
        original_row_order_types_missing_null_negative_zero_and_errors_preserved=True,
        original_full_stderr_reading_scope_not_reduced=True,
        no_arbitrary_object_or_number_encoding=True)
    return result


def expand_rule_files(value):
    """Documented inverse of the fixed columns; not invoked as a runtime gate."""
    rep = value["rule_file_representation"]
    require(rep["schema"] == SCHEMA+"-fixed-rule-file-columns-v1"
        and rep["identity_columns"] == RULE_IDENTITY_COLUMNS
        and rep["file_columns"] == RULE_FILE_COLUMNS, "Unknown rule-file columns")
    result = {k:v for k,v in value.items() if k != "rule_file_representation"}
    phases = []
    for phase in value["rule_resources"]:
        if not (type(phase) is dict and set(phase) == {"phase", "available", "files_table"}):
            phases.append(phase); continue
        files = []
        for row in phase["files_table"]:
            kind = row[0]
            if kind == "literal":
                files.append(row[1]); continue
            ident = dict(zip(RULE_IDENTITY_COLUMNS, row[2]))
            if kind in ("json", "json_readme"):
                if kind == "json_readme":
                    meta = dict(row[4])
                    meta["README_blobs"] = dict(rep["README_blobs_sets"][row[3]])
                else:
                    meta = row[3]
                files.append(dict(file=row[1], identity=ident,
                    necessary_original_metadata=meta, full_member_tree_not_exported=True))
            elif kind == "text":
                files.append(dict(file=row[1], identity=ident, lines=row[3],
                    selected_error_text=row[4], complete_original_text_not_exported=True))
            else:
                raise ValueError("Unknown original rule-file row kind")
        phases.append(dict(phase=phase["phase"], available=True, files=files))
    result["rule_resources"] = phases
    return result


class Reader:
    def __init__(self, args):
        self.args = args
        require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "Read actual metadata only in the named public Actions")
        self.request, self.rid = read(args.request, args.request_sha256)
        require(same(receipt(__file__), self.request["roles"]["reader"]),
            "Use the current independent reader identity")
        self.comp = Path(args.computations).resolve(strict=True)
        require(self.comp == HERE, "Keep the real same-directory source graph")
        runner_desc = self.request["roles"]["runner"]
        self.Runner = load(self.comp/runner_desc["file"], runner_desc["sha256"],
            "_request217_complete_necessary_orchestration_source")
        self.B = self.Runner.Binding(args, complete_sources=False)
        self.H, self.base = self.B.H, self.B.base
        self.directory = self.base/self.Runner.OUT_NAME
        self.out = self.base/"same-C217-readback"
        require(not self.out.exists(), "Retain any preceding actual necessary readback")
        self.out.mkdir(); (self.out/"ownership").mkdir()
        self.value = dict(schema=SCHEMA, repository=REPO, source=receipt(__file__),
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            outer_request=self.rid, upstream_request=self.B.parent_id,
            actual_step_outcomes=dict(prepare=args.prepare_outcome, first=args.first_outcome,
                successors=args.successors_outcome),
            independent_source_generation=None, original_orchestration_result=None,
            original_orchestration=None, ownership=[], rule_resources=[], required_bodies=[],
            reader_children=[], errors=[], original_logs=[],
            complete_necessary_readback=False, quiescent=False, raw_deleted=False,
            no_new_scientific_value_or_acceptance_computed=True,
            full_scientific_success_ledgers_are_original_identities_not_independent_recomputations=True,
            full_necessary_scopes_are_separate_semantic_roles_not_encoded_parts=True)
        self.signals = []; self.handlers = {}; self.child = None
        self.deadline = None; self.report = None
        self.quiet = False; self.complete = True
        self.ownership_observation_completed = False

    def fail(self, label, error):
        self.complete = False
        self.value["errors"].append(dict(scope=label, type=type(error).__name__,
            message=str(error), traceback=traceback.format_exc()))

    def receive(self, number, frame):
        self.signals.append(dict(number=int(number), name=signal.Signals(number).name))
        if self.child is not None:
            self.child.signal(signal.SIGTERM)

    def check(self):
        if self.signals:
            raise RuntimeError("External interruption of necessary metadata readback")
        if self.deadline is not None and time.time() >= self.deadline:
            raise RuntimeError("The unchanged original readback deadline was reached")

    def bind(self):
        path = self.base/self.request["source_generation"]["receipt"]
        if path.is_file():
            made, mid = read(path); current(made)
            require(made.get("schema") == self.request["source_generation"]["receipt_schema"]
                and same(made.get("outer_request"), self.rid),
                "The actual independent source preparation differs")
            self.value["independent_source_generation"] = dict(actual_file=mid,
                original_value=made)
        else:
            self.value["independent_source_generation"] = dict(available=False,
                actual_prepare_step_outcome=self.args.prepare_outcome)
        try:
            origin, oid, clock, did = self.B.origin()
            self.value["actual_original_launch"] = oid
            if clock is not None:
                self.deadline = clock["namespace_created_unix_seconds"]+21600
                self.value["actual_original_job_deadline"] = did
        except Exception as error:
            self.fail("actual-origin-deadline", error)
        if self.deadline is None:
            clock, cid = read(self.base/"job-science-deadline.json"); current(clock)
            require(clock.get("schema") == self.B.upstream["deadline_schema"]
                and clock.get("science_seconds_from_namespace") == 18900
                and clock.get("readback_reserve_seconds") == 2700
                and type(clock.get("namespace_created_unix_seconds")) in (int, float)
                and math.isfinite(clock["namespace_created_unix_seconds"]),
                "No invented transport clock replaces the actual namespace receipt")
            self.deadline = clock["namespace_created_unix_seconds"]+21600
            self.value["startup_transport_deadline_only"] = cid
        self.value["original_absolute_readback_deadline_unix_seconds"] = self.deadline
        path = self.directory/"result.json"
        if path.is_file():
            self.report, rid = read(path); current(self.report)
            require(self.report.get("schema") == self.Runner.SCHEMA
                and same(self.report.get("source"), self.request["roles"]["runner"])
                and same(self.report.get("outer_request"), self.rid),
                "Read the genuine same-C orchestration, not an earlier or generic result")
            require(type(self.report.get("stages")) is list
                and [row.get("name") for row in self.report["stages"]] == list(self.Runner.STAGES),
                "Keep the complete original eight-stage address order")
            self.value["original_orchestration_result"] = rid
            self.value["original_orchestration"] = self.report
        else:
            self.value["original_orchestration"] = dict(available=False,
                new_actual_scientific_output_not_inferred=True)
        quiet = True
        for phase in ("first", "successors"):
            run_dir = self.base/("same-C217-"+phase+"-run-owner")
            rules_dir = self.base/("same-C217-"+phase+"-rule-owner")
            for directory in (run_dir,):
                # Even an absent receipt directory does not establish quiet:
                # the original observer still checks live namespace processes.
                existed = directory.exists()
                observed = self.H.observe_records(self.base, directory,
                    terminate=True, grace=max(0.0, min(15.0, self.deadline-time.time())))
                self.value["ownership"].append(dict(directory=str(directory),
                    original_directory_present=existed, observation=observed))
                quiet = quiet and observed["all_actual_owned_processes_quiet"]
            launched = rules_dir/"parent-launch.json"
            if launched.is_file():
                parent, pid = read(launched); current(parent)
                require(same(parent.get("source"), self.request["roles"]["runner"]),
                    "The actual rules parent source differs")
                old = parent.get("actual_process")
                now = None if old is None else self.H.proc(old["pid"])
                live = bool(old is not None and self.H.same_process(old, now) and now["state"] != "Z")
                row = dict(phase=phase, actual_parent=pid, matching_PID_starttime_still_live=live)
                returned = rules_dir/"parent-return.json"
                if returned.is_file():
                    rv, rr = read(returned); current(rv); row["actual_return"] = rr
                    row["original_return_values"] = rv
                else:
                    row["actual_return_absent"] = True
                    self.complete = False
                self.value["ownership"].append(row)
                quiet = quiet and not live and old is not None
            actual_phase = None if self.report is None else next(
                (r for r in self.report.get("phases", []) if r["phase"] == phase), None)
            outcome = getattr(self.args, phase+"_outcome")
            if actual_phase is not None and actual_phase.get("returned") is not True:
                self.complete = False
                self.value["errors"].append(dict(scope=phase,
                    message="Actual independent run scope did not return; partial raw retained"))
            elif actual_phase is None and outcome not in ("skipped", "cancelled"):
                self.complete = False
                self.value["errors"].append(dict(scope=phase,
                    message="A non-skipped independent slot has no completed actual run receipt"))
        owned = self.directory/"ownership"
        observed = self.H.observe_records(self.base, owned, terminate=True,
            grace=max(0.0, min(15.0, self.deadline-time.time())))
        self.value["ownership"].append(dict(directory=str(owned),
            original_directory_present=owned.is_dir(), observation=observed))
        quiet = quiet and observed["all_actual_owned_processes_quiet"]
        if self.report is not None and self.report.get("all_owned_processes_quiescent") is not True:
            # A final fresh process observation is still retained; do not erase
            # the producer's unresolved ownership claims.
            quiet = False
        self.quiet = quiet
        self.ownership_observation_completed = True
        self.value["quiescent"] = self.quiet
        self.value["ownership_observation_completed"] = True
        self.check()

    def invoke_reader(self, name, command):
        allowance = min(float(self.request["same_C_work"]["metadata_reader_cap_seconds"]),
            max(0.0, self.deadline-time.time()-15))
        row = dict(role=name, command=command, started=False, actual_cap_seconds=allowance)
        self.value["reader_children"].append(row)
        if allowance <= 0 or self.signals:
            row["reason"] = "original-readback-reserve-or-external-interruption"
            return False
        stdout = self.out/(name+".stdout.log"); stderr = self.out/(name+".stderr.log")
        env = dict(os.environ)
        for key in ("GITHUB_OUTPUT", "GH_TOKEN", "GITHUB_TOKEN", "MR_TOKEN"):
            env.pop(key, None)
        with stdout.open("xb") as so, stderr.open("xb") as se:
            process = subprocess.Popen(command, cwd=self.comp, env=env, shell=False,
                start_new_session=True, stdout=so, stderr=se)
            self.child = self.H.OwnedTree(process, self.out/"ownership", self.base, name)
            row["started"] = True; born = time.monotonic()
            try:
                while process.poll() is None and time.monotonic()-born < allowance and not self.signals:
                    self.child.observe(); self.child.persist()
                    try:
                        process.wait(timeout=.5)
                    except subprocess.TimeoutExpired:
                        pass
            finally:
                state = self.child.stop(max(0.0, min(15.0, self.deadline-time.time())))
                row.update(actual_child_exit=state["actual_child_returncode"],
                    observed_tree_quiescent=state["observed_tree_quiescent"],
                    actual_owner=receipt(self.child.path))
                self.child = None; so.flush(); se.flush()
        row.update(stdout=receipt(stdout), stderr=receipt(stderr))
        self.quiet = self.quiet and row["observed_tree_quiescent"]
        raw = stderr.read_bytes()
        if raw:
            row["complete_original_stderr"] = raw.decode("utf-8", errors="surrogateescape")
            row["all_stderr_bytes_represented_by_utf8_surrogateescape"] = True
        return row["observed_tree_quiescent"]

    def body(self, stage):
        name = stage["name"]
        if not stage["started"]:
            self.value["required_bodies"].append(dict(role=name, actual_started=False,
                actual_unpaid_reason=stage.get("reason"), complete_known_unstarted_scope=True))
            return
        if not self.quiet:
            raise RuntimeError("Do not read a mutable actual scientific stream")
        directory = self.B.inside(stage["output_directory"])
        result_path = directory/"result.json"
        result, rid = read(result_path); current(result)
        self.check()
        if name == "head_recompute":
            source = self.request["roles"]["head"]
            require(result.get("schema") == source["schema"] and same(result.get("source"), source),
                "The actual full-head producer tuple differs")
            out = self.out/"head-necessary"
            command = [sys.executable, "-u", str(self.comp/source["file"]), "readback",
                "--directory", str(directory), "--result-sha256", rid["sha256"], "--out", str(out)]
            require(self.invoke_reader("head-necessary-reader", command),
                "The full-head original metadata reader did not return quiescent")
            path = out/"summary.json"
            attempted, attempted_id = read(path); current(attempted)
            if attempted.get("schema") == source["schema"]+"-necessary-v1-over-budget":
                self.value["required_bodies"].append(dict(role=name, actual_result=rid,
                    original_necessary=attempted_id, original_over_budget=attempted,
                    complete_original_necessary_scope=False))
                self.complete = False
                return
            sid, emitted, summary = emit_existing(path, source["frame"],
                source["schema"]+"-necessary-v1", source, rid)
            marker, mid = read(out/"readback-complete.json"); current(marker)
            require(marker.get("schema") == source["schema"]+"-necessary-v1-complete-marker",
                "The actual full-head readback marker schema differs")
            complete = bool(emitted and summary.get("complete_necessary_readback") is True
                and marker.get("complete") is True and marker.get("quiescent") is True
                and same(marker.get("necessary_summary"), sid))
            row = dict(role=name, actual_result=rid, original_necessary=sid,
                original_readback_marker=mid, complete_original_necessary_scope=complete)
        elif name.endswith("_metric"):
            index = int(name[5]); source = self.request["roles"]["metric%d" % index]
            require(result.get("schema") == source["schema"] and same(result.get("source"), source),
                "The actual complete metric source differs")
            sid, emitted, summary = emit_existing(directory/"summary.json", source["frame"],
                source["schema"]+"-necessary-summary", source, rid)
            row = dict(role=name, actual_result=rid, original_necessary=sid,
                complete_original_necessary_scope=emitted,
                mathematical_result_not_changed_by_readback=True)
        else:
            source = self.request["roles"]["evidence"]
            expected = source["schema"]+("-actual-series-v1" if name == "compare" else "")
            require(result.get("schema") == expected and same(result.get("source"), source),
                "The actual complete measurement/comparison source differs")
            out = self.out/(name+"-necessary")
            command = [sys.executable, "-u", str(self.comp/source["file"]), "readback",
                "--directory", str(directory), "--result-sha256", rid["sha256"], "--out", str(out)]
            require(self.invoke_reader(name+"-necessary-reader", command),
                "The original evidence reader did not return quiescent")
            path = out/"summary.json"
            # The original compare necessary object keeps the original series schema.
            summary, sid = read(path); current(summary)
            require(summary.get("schema") == expected,
                "The original evidence/series necessary schema differs")
            require(same(summary.get("actual_complete_result"), rid),
                "The evidence necessary body points to another actual result")
            require(same(summary.get("source"), source),
                "The original evidence necessary source differs")
            if sid["bytes"] > LIMIT:
                print(json.dumps(dict(event="request217_evidence_necessary_over_budget",
                    original_summary=sid, limit=LIMIT, complete_necessary_emitted=False,
                    no_part_transport=True, raw_retained=True), separators=(",", ":")), flush=True)
                emitted = False
            else:
                raw = Path(sid["file"]).read_bytes()
                require(len(raw) == sid["bytes"] and hashlib.sha256(raw).hexdigest() == sid["sha256"],
                    "The actual evidence necessary bytes changed")
                print("BEGIN_"+source["frame"], flush=True)
                sys.stdout.buffer.write(raw); sys.stdout.buffer.flush()
                print("END_"+source["frame"], flush=True)
                emitted = True
            row = dict(role=name, actual_result=rid, original_necessary=sid,
                complete_original_necessary_scope=emitted)
        self.value["required_bodies"].append(row)
        if row["complete_original_necessary_scope"] is not True:
            self.complete = False

    def logs_and_rules(self):
        R = load(self.comp/ORIGINAL_READER, ORIGINAL_READER_SHA,
            "_request217_original_rule_metadata_selector")
        if not self.quiet:
            raise RuntimeError("Original rule/child streams are not known quiescent")
        if self.report is not None:
            for stage in self.report.get("stages", []):
                if not stage.get("started"):
                    continue
                for kind in ("stdout", "stderr"):
                    descriptor = stage.get(kind)
                    path = self.directory/"logs"/(stage["name"]+"."+kind+".log")
                    if not path.is_file():
                        self.complete = False
                        self.value["original_logs"].append(dict(role=stage["name"], kind=kind,
                            available=False, reason="started-child-log-absent"))
                        continue
                    rid = receipt(path)
                    require(descriptor is None or same(rid, descriptor),
                        "An actual child log changed after its producer receipt")
                    row = dict(role=stage["name"], kind=kind, original_file=rid)
                    if kind == "stderr":
                        row["complete_original_text"] = path.read_bytes().decode("utf-8", errors="surrogateescape")
                        row["all_original_bytes_represented_by_utf8_surrogateescape"] = True
                    else:
                        row["scope"] = "Complete stdout identity; required result/error/pending objects emitted separately"
                    self.value["original_logs"].append(row)
                    self.check()
        for phase in ("first", "successors"):
            directory = self.base/("same-C217-"+phase+"-rules")
            if not directory.is_dir():
                self.value["rule_resources"].append(dict(phase=phase, available=False,
                    original_slot_outcome=getattr(self.args, phase+"_outcome")))
                continue
            files = []
            for path in sorted(directory.rglob("*")):
                self.check()
                if path.is_symlink():
                    raise ValueError("An actual owned rule file is an unresolved symlink")
                if not path.is_file():
                    continue
                label = str(path.relative_to(self.base))
                if path.suffix == ".json":
                    value, rid = R.document(path, "same-C-rules/"+label)
                    files.append(dict(file=label, identity=rid,
                        necessary_original_metadata=R.small(value),
                        full_member_tree_not_exported=True))
                else:
                    value = R.log_view(path, "same-C-rules/"+label)
                    files.append(dict(file=label, identity=value["original_file"],
                        lines=value["complete_lines"],
                        selected_error_text=value if value["original_error_matched_lines"] else None,
                        complete_original_text_not_exported=True))
            self.value["rule_resources"].append(dict(phase=phase, available=True, files=files))
        self.value["original_rule_read_errors"] = R.ERRORS
        self.value["original_rule_omission_scope"] = dict(
            count=len(R.OMISSIONS), original_index_identity=dict(bytes=len(R.canonical(R.OMISSIONS)),
                sha256=R.sha(R.canonical(R.OMISSIONS))),
            full_success_metadata_trees_not_transported=True)
        if R.ERRORS:
            self.complete = False

    def run(self):
        for number in (signal.SIGTERM, signal.SIGINT):
            self.handlers[number] = signal.signal(number, self.receive)
        try:
            self.bind()
            if self.quiet and self.report is not None:
                for stage in self.report.get("stages", []):
                    try:
                        self.body(stage)
                    except BaseException as error:
                        self.fail("original-necessary-"+stage["name"], error)
            try:
                self.logs_and_rules()
            except BaseException as error:
                self.fail("original-logs-and-rules", error)
        except BaseException as error:
            self.fail("readback-binding-or-quiescence", error)
        finally:
            if self.child is not None:
                try:
                    result = self.child.stop(10.0)
                    self.quiet = self.quiet and result["observed_tree_quiescent"]
                except BaseException as error:
                    self.fail("reader-child-shutdown", error); self.quiet = False
            for number, previous in self.handlers.items():
                signal.signal(number, previous)
        self.value.update(quiescent=self.quiet,
            ownership_observation_completed=self.ownership_observation_completed,
            complete_necessary_readback=bool(self.complete and self.quiet
                and self.ownership_observation_completed and not self.signals),
            actual_external_interruptions=self.signals)
        self.value = tabulate_rule_files(self.value)
        raw = canonical(self.value)
        attempt = write(self.out/"full-necessary-attempt.json", self.value)
        if len(raw) > LIMIT:
            fallback = dict(schema=SCHEMA+"-over-budget", repository=REPO,
                run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
                attempted_necessary=attempt, limit=LIMIT, complete_necessary_readback=False,
                quiescent=self.quiet, no_part_transport=True, all_raw_retained=True)
            sid = write(self.out/"summary.json", fallback)
            print(canonical(fallback).decode(), end="", flush=True)
            return 70
        sid = write(self.out/"summary.json", self.value)
        print("BEGIN_REQUEST217_SAME_C_COMPLETE_NECESSARY", flush=True)
        print(raw.decode(), end="", flush=True)
        print("END_REQUEST217_SAME_C_COMPLETE_NECESSARY", flush=True)
        if os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as stream:
                for key, value in (("same_C_summary", sid["file"]),
                    ("same_C_summary_bytes", sid["bytes"]), ("same_C_summary_sha256", sid["sha256"])):
                    stream.write(key+"="+str(value)+"\n")
        if self.value["complete_necessary_readback"]:
            write(self.out/"readback-complete.json", dict(schema=MARKER_SCHEMA,
                repository=REPO, run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
                complete=True, quiescent=True, necessary_summary={k:sid[k] for k in ("bytes", "sha256")},
                original_upstream_cleanup_conditions_not_removed=True,
                scientific_success_not_inferred=True))
        return 0 if self.value["complete_necessary_readback"] else 2


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--request-sha256", required=True)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--computations", type=Path, required=True)
    for name in ("prepare", "first", "successors"):
        parser.add_argument("--"+name+"-outcome", required=True)
    args = parser.parse_args(argv)
    return Reader(args).run()


if __name__ == "__main__":
    raise SystemExit(main())
