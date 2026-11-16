#!/usr/bin/env python3
"""R458 / request207: metadata and ownership for nested same-job consumers.

No scientific formula, source, acceptance or clock is replaced. Every signal
targets an actually observed PID with matching Linux start time. Independent
sessions created by the frozen inner owners are tracked through ancestry and
their recorded process identities. Unresolved ownership prevents deletion.
Author: ChatGPT exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
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
TOPIC = "topics/visible-flex-larger-amplitude"
NAMESPACE = "visible-current-C-actual202-ten450-closed-geometry205"
SCHEMA = "R458-request207-owned-nested-role-v1"
REQUEST_SCHEMA = "public-actual202-joint-refinement-and-fixed-target-evidence-request-v1"
SUBREQUEST_SHA = "06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4"
LIMIT = 90000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPO
        and os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_SHA"),
        "Use the actual public Actions job")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "An actual ordinary file is required: " + str(path))
    a = path.stat(); h = hashlib.sha256(); count = 0
    with path.open("rb") as stream:
        while block := stream.read(1048576):
            h.update(block); count += len(block)
    b = path.stat()
    require((a.st_dev, a.st_ino, a.st_size, a.st_mtime_ns) ==
        (b.st_dev, b.st_ino, b.st_size, b.st_mtime_ns) and count == b.st_size,
        "A consumed file changed: " + str(path))
    return dict(file=str(path.resolve()), bytes=count, sha256=h.hexdigest())


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and (
        a.get("bytes"), a.get("sha256")) == (b.get("bytes"), b.get("sha256"))


def read(path, expected=None):
    rid = receipt(path)
    if expected is not None:
        require(same(rid, expected) if isinstance(expected, dict) else rid["sha256"] == expected,
            "The actual input identity differs: " + str(path))
    raw = Path(path).read_bytes()
    require((len(raw), sha(raw)) == (rid["bytes"], rid["sha256"]), "Input changed before parsing")
    return json.loads(raw), rid


def write(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    raw = canonical(value); pending = path.with_name(path.name + ".writing")
    with pending.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(pending, path)
    return dict(file=str(path.resolve()), bytes=len(raw), sha256=sha(raw))


def current(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"], "Use the actual current run/source")
    if "repository" in value:
        require(value["repository"] == REPO, "The actual repository differs")


def inside(path, root, exists=False):
    root = Path(root).resolve(strict=True)
    value = Path(path).resolve(strict=exists)
    require(value != root and value.is_relative_to(root), "Use an owned child path: " + str(value))
    return value


def locations(base, computations):
    actions()
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    base = inside(base, temporary, True)
    require(base.parent == temporary and base.name == NAMESPACE,
        "Use the new actual job's original205-contract namespace")
    return base, Path(computations).resolve(strict=True)


def selected(value, keys):
    return {k: value[k] for k in keys if k in value}


def error_record(error):
    return dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc(),
        mathematical_rejection_not_inferred=True)


def load(path, expected, alias):
    rid = receipt(path)
    require(same(rid, expected) if isinstance(expected, dict) else rid["sha256"] == expected,
        "Frozen runtime/metadata source differs: " + str(path))
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec); sys.modules[alias] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(alias, None); raise
    return module


def bind_request(path, expected, base, comp):
    request, rid = read(path, expected)
    require(request.get("schema") == REQUEST_SCHEMA and request.get("request_number") == 207,
        "Use the independent request207 outer contract")
    sub = request["original205_subcontract"]
    require(sub["sha256"] == SUBREQUEST_SHA and sub["bytes"] == 97406,
        "Keep the published complete205 atomic subcontract")
    original, sid = read(base / "dispatch-request.json", sub)
    require(original.get("request_number") == 205
        and original.get("schema") == "public-actual202-accurate-ten450-closed-geometry-request-v1",
        "Do not relabel the original205 schema or actual generated recipe")
    require(len(original["source_sha256"]) == 154, "Keep all original205 source pins")
    combined = dict(original["source_sha256"])
    for name, digest in request["additional_source_sha256"].items():
        require(name not in combined or combined[name] == digest, "Do not replace an original source pin")
        combined[name] = digest
    actual = {}
    for name, digest in combined.items():
        require(Path(name).name == name, "Source closure names are basenames")
        actual[name] = receipt(comp / name)
        require(actual[name]["sha256"] == digest, "Complete source closure differs: " + name)
    for role, descriptor in request["roles"].items():
        name = Path(descriptor["file"]).name
        require(name in actual and same(actual[name], descriptor), "Actual role source differs: " + role)
    require(request["execution"]["science_seconds_from_original_namespace"] == 18900
        and request["execution"]["original_readback_reserve_seconds"] == 2700,
        "No new scientific clock is permitted")
    return request, rid, original, sid, actual


def proc(pid):
    directory = Path("/proc") / str(pid)
    try:
        st = directory.stat()
        text = (directory / "stat").read_text()
    except (FileNotFoundError, ProcessLookupError):
        return None
    fields = text.rsplit(")", 1)[1].split()
    return dict(pid=int(pid), state=fields[0], ppid=int(fields[1]), pgid=int(fields[2]),
        sid=int(fields[3]), start_ticks=int(fields[19]), uid=int(st.st_uid))


def same_process(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and a.get("pid") == b.get("pid") \
        and int(a.get("start_ticks", -1)) == int(b.get("start_ticks", -2))


def process_table():
    values, errors = {}, []
    for directory in Path("/proc").iterdir():
        if not directory.name.isdigit():
            continue
        try:
            row = proc(int(directory.name))
            if row is not None and row["uid"] == os.getuid():
                values[row["pid"]] = row
        except (FileNotFoundError, ProcessLookupError):
            pass
        except (PermissionError, OSError, ValueError) as error:
            errors.append(dict(pid=int(directory.name), error=str(error)))
    return values, errors


class OwnedTree:
    """Own only observed descendants, including their independent sessions.

    Persistent /proc start-time identities and inner-owner metadata are used
    for the always readback. A namespace-bearing unregistered live process is
    an unresolved ownership scope; it is not guessed to belong to this tree.
    """
    def __init__(self, process, directory, base, role):
        self.process, self.directory, self.base, self.role = process, Path(directory), Path(base), role
        self.path = self.directory / (role + "-ownership.json")
        self.known, self.groups, self.conflicts = {}, {}, []
        self.claim_files = []; self.complete_scan = False
        self.leader = proc(process.pid)
        require(self.leader is not None and self.leader["pid"] == self.leader["pgid"] == self.leader["sid"],
            "The caller creates and observes this actual exclusive session")
        self.boot_id = Path("/proc/sys/kernel/random/boot_id").read_text().strip()
        self.add(self.leader, "actual-Popen-exclusive-session")
        self.persist()

    def add(self, row, reason):
        key = str(row["pid"]); old = self.known.get(key)
        if old is not None and not same_process(old, row):
            self.conflicts.append(dict(reason="observed-pid-reuse", old=old, actual=row)); return
        self.known[key] = dict(row, ownership_reason=reason)
        self.groups[str(row["pgid"])] = dict(pgid=row["pgid"], sid=row["sid"])

    def observe(self):
        table, errors = process_table()
        live = {int(pid) for pid, old in self.known.items() if same_process(old, table.get(int(pid)))}
        changed = True
        while changed:
            changed = False
            for row in table.values():
                if row["pid"] in live:
                    continue
                owned_group = self.groups.get(str(row["pgid"]))
                group_live = any(table[x]["pgid"] == row["pgid"] and table[x]["sid"] == row["sid"] for x in live)
                if (row["ppid"] in live or (owned_group and group_live and owned_group["sid"] == row["sid"])) \
                        and row["start_ticks"] >= self.leader["start_ticks"]:
                    self.add(row, "observed-descendant-or-still-owned-session")
                    live.add(row["pid"]); changed = True
        self.scan_errors = errors; self.complete_scan = not errors
        return [table[x] for x in live if table[x]["state"] != "Z"]

    def recorded_children(self, path):
        if not Path(path).is_file():
            return
        value, rid = read(path)
        current(value)
        if not any(same(x, rid) for x in self.claim_files):
            self.claim_files.append(rid)
        containers = ("observed_child", "observed_children", "owned_process", "observed_processes",
            "stages", "children", "leader", "actual_procedure_process", "actual_launcher_process")
        def walk(obj):
            if isinstance(obj, dict):
                if type(obj.get("pid")) is int and "start_ticks" in obj:
                    now = proc(obj["pid"])
                    if same_process(now, obj) and now["start_ticks"] >= self.leader["start_ticks"]:
                        self.add(now, "same-run-inner-owner-original-record")
                    elif now is not None and not same_process(now, obj):
                        self.conflicts.append(dict(reason="inner-owner-pid-no-longer-same-process", original=obj, actual=now))
                for key in containers:
                    if key in obj:
                        walk(obj[key])
            elif isinstance(obj, list):
                for item in obj:
                    walk(item)
        walk(value); self.observe(); self.persist()

    def persist(self):
        write(self.path, self.record(observe=False))

    def record(self, observe=True):
        live = self.observe() if observe else [now for old in self.known.values()
            if same_process(old, now := proc(old["pid"])) and now["state"] != "Z"]
        return dict(schema=SCHEMA, repository=REPO, run_id=os.environ["GITHUB_RUN_ID"],
            source_commit=os.environ["GITHUB_SHA"], source=receipt(__file__), role=self.role,
            boot_id=self.boot_id, leader=self.leader, observed_processes=list(self.known.values()),
            observed_groups=list(self.groups.values()), identity_conflicts=self.conflicts,
            inner_owner_claims=self.claim_files, matching_live_processes=live,
            complete_proc_scan=self.complete_scan, proc_scan_errors=getattr(self, "scan_errors", []),
            actual_child_returncode=self.process.poll(),
            observed_tree_quiescent=not live and self.complete_scan and not self.conflicts,
            signals_restricted_to_matching_observed_PID_starttime=True,
            independent_nested_sessions_included=True)

    def signal(self, number):
        self.observe()
        for old in list(self.known.values()):
            now = proc(old["pid"])
            if same_process(old, now) and now["state"] != "Z":
                try:
                    os.kill(now["pid"], number)
                except ProcessLookupError:
                    pass

    def stop(self, seconds):
        end = time.monotonic() + max(0.0, seconds)
        if self.observe():
            self.signal(signal.SIGTERM)
            term_end = end - min(2.0, max(0.0, seconds)/3)
            while self.observe() and time.monotonic() < term_end:
                time.sleep(.1)
            if self.observe():
                self.signal(signal.SIGKILL)
        try:
            self.process.wait(timeout=max(.01, end-time.monotonic()))
        except subprocess.TimeoutExpired:
            pass
        while self.observe() and time.monotonic() < end:
            time.sleep(.1)
        value = self.record(); write(self.path, value); return value


def observe_records(base, directory, *, terminate=False, grace=15.0):
    """Always phase: stop only proven own processes, never namespace guesses."""
    base, directory = Path(base).resolve(), Path(directory)
    boot = Path("/proc/sys/kernel/random/boot_id").read_text().strip()
    records, errors, known = [], [], {}
    for path in sorted(directory.glob("*-ownership.json")):
        try:
            row, rid = read(path); current(row)
            require(row.get("schema") == SCHEMA and row.get("boot_id") == boot,
                "Ownership record belongs to another schema or kernel boot")
            require(row.get("source", {}).get("sha256") == receipt(__file__)["sha256"],
                "Ownership producer source differs")
            for member in row["observed_processes"]:
                key = (member["pid"], int(member["start_ticks"]))
                known[key] = member
            records.append(dict(identity=rid, role=row["role"],
                actual_child_returncode=row.get("actual_child_returncode"),
                inner_owner_claims=row.get("inner_owner_claims", [])))
            errors.extend(row.get("identity_conflicts", []))
        except Exception as error:
            errors.append(dict(file=str(path), error=str(error)))
    def live():
        return [now for old in known.values() if same_process(old, now := proc(old["pid"])) and now["state"] != "Z"]
    if terminate and live():
        end = time.monotonic() + max(0.0, grace)
        for number in (signal.SIGTERM, signal.SIGKILL):
            for row in live():
                try:
                    os.kill(row["pid"], number)
                except ProcessLookupError:
                    pass
            until = end if number == signal.SIGKILL else end-min(2.0, grace/3)
            while live() and time.monotonic() < until:
                time.sleep(.1)
    table, scan_errors = process_table(); errors.extend(scan_errors)
    unknown, retained_groups = [], []
    owned_groups = {(row["pgid"], row.get("sid")) for row in known.values()}
    own_ancestors = {os.getpid()}; cursor = proc(os.getpid())
    while cursor and cursor["ppid"] > 0 and cursor["ppid"] not in own_ancestors:
        own_ancestors.add(cursor["ppid"]); cursor = proc(cursor["ppid"])
    for row in table.values():
        if row["state"] == "Z" or row["pid"] in own_ancestors:
            continue
        if (row["pgid"], row["sid"]) in owned_groups:
            retained_groups.append(row)
        try:
            raw = (Path("/proc")/str(row["pid"])/"cmdline").read_bytes()
        except (FileNotFoundError, ProcessLookupError):
            continue
        except (PermissionError, OSError) as error:
            errors.append(dict(pid=row["pid"], error=str(error))); continue
        if str(base).encode() in raw and (row["pid"], row["start_ticks"]) not in known:
            unknown.append(dict(process=row, reason="namespace-bearing-live-process-not-owned-by-this-receipt"))
    active = live()
    return dict(schema=SCHEMA+"-quiet", records=records, matching_live_processes=active,
        actual_owned_group_members=retained_groups, unknown_namespace_processes=unknown,
        errors=errors, all_actual_owned_processes_quiet=not active and not retained_groups and not unknown and not errors,
        no_unobserved_process_signalled=True, signals_restricted_to_original_PID_starttime=True)
