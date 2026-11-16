#!/usr/bin/env python3
"""Request205: actual202450 -> R452 registration of original first closed geometry -> R425.

This independent lifecycle/metadata source changes no mathematical producer.
The actual upstream deadline, eight original finite work caps and original
Original mathematical binders with explicit R452 provenance remain authoritative. No absent field is manufactured.
Readback emits the two existing necessary frames separately, then one small
resource/identity conclusion. It never uploads, splits or deletes raw output.
Author: ChatGPT geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import traceback

ENTRY = "geometry_20261116_request205_actual202_closed_postsolve.py"
REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
NAMESPACE = "visible-current-C-actual202-ten450-closed-geometry205"
SCHEMA = "request205-actual202450-first-closed-postsolve-orchestration-v1"
READBACK_SCHEMA = SCHEMA + "-necessary-v1"
MARKER_SCHEMA = "request205-closed-postsolve-readback-complete-v1"
REQUEST_SCHEMA = "public-actual202-accurate-ten450-closed-geometry-request-v1"
DEADLINE_SCHEMA = "request205-owned-job-science-deadline-v1"
RECIPE_SCHEMA = "R449-explicit-actual202-projected-accurate-ten-joint-full453-to-frozen450-recipe-v1"
UPSTREAM_SCHEMA = "R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1"
UPSTREAM_SHA = "227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7"
RUNNER_SCHEMA = "R452-actual202-accurate-ten450-first-parameter-block-postsolve-v1"
READER_SCHEMA = "R452-actual202-ten450-parameter-block-postsolve-one-necessary-conclusion-v1"
HELD_SCHEMA = "R452-actual202-ten450-parameter-block-same-job-held-after-shared-v1"
LIMIT = 90000
SOURCE_ROLES = {
    "runner": ("geometry_20261116_actual202_ten450_parameter_block_postsolve.py", 26899,
        "89a90b2d5d762510c228c5d3a4f6fe27a573c890b760268aecace2a44ab9e010"),
    "reader": ("root_20261116_actual202_ten450_parameter_block_postsolve_necessary.py", 10412,
        "e3a4a70277c3267ff412e1ac3f63590be135ed28f5cfc3c1e553e4e2e9cd7f3c"),
    "held": ("geometry_20261116_actual202_ten450_parameter_block_postsolve_held.py", 5449,
        "8d0927cc335faa6a0a639f0f0ecec063ee2d65bbc0ef11bd990eb118aa971ffb"),
    "helper": ("geometry_20261116_actual202_ten450_closed_parameter_policy.py", 37958,
        "b49769f13f69bf30b82988b1ca57382c602d4b74bc3ae8a6c2b5d1e0ee3df7a8"),
    "owner": ("geometry_20261116_actual202_closed_owned_process.py", 14815,
        "f779c6a296b8579469dffb27c46642d5d5aaffc08d53a027537d2ddb23ee9357"),
}
DATA_ROLES = {
    "parameter_policy": ("current-ten450-first-closed-parameter-policy.json", 2198,
        "fe932b50f25bd8d77709be1efd26da8c24a7d87f9ad1423bd6a9ebc34c1d0a41"),
    "work_choices": ("current-ten450-first-closed-work-choices.json", 3356,
        "8a03c854c93194f6bb3f2f75f06c20bf8397e5b85451ce6a1e7247f0a95c7d08"),
}
LIFECYCLE = ("geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py", 66873,
    "5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95")
RULE_READER = ("root_20261115_current_C_pruefer_positive_full453_necessary_readout.py", 51108,
    "34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9")
INNER_STAGES = ("radial_replay", "construction_parameters", "original_cuff_atlas",
    "shared_field", "held_witnesses", "metric", "reach", "held")
OUTPUTS = dict(journal="closed-postsolve-orchestration", postsolve="closed-postsolve",
    held="closed-held", readback="closed-postsolve-readback",
    marker="closed-postsolve-readback-complete.json")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPO
        and os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_SHA"),
        "Use this public repository Actions with the actual run/source identity")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def receipt(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "An actual ordinary file is required: " + str(path))
    before = path.stat()
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        while block := stream.read(1048576):
            h.update(block)
            size += len(block)
    after = path.stat()
    require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) ==
        (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
        and size == after.st_size, "A consumed file changed: " + str(path))
    return dict(file=str(path.resolve()), bytes=size, sha256=h.hexdigest())


def same(left, right):
    return isinstance(left, dict) and isinstance(right, dict) and (
        left.get("bytes"), left.get("sha256")) == (right.get("bytes"), right.get("sha256"))


def read(path, expected=None):
    original = receipt(path)
    if expected is not None:
        require(same(original, expected), "Actual original bytes differ: " + str(path))
    raw = Path(path).read_bytes()
    require(len(raw) == original["bytes"] and digest(raw) == original["sha256"],
        "File changed before parsing: " + str(path))
    return json.loads(raw), original


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = canonical(value)
    temporary = path.with_name(path.name + ".writing")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    return dict(file=str(path.resolve()), bytes=len(raw), sha256=digest(raw))


def inside(path, root, *, exists=False):
    path, root = Path(path).resolve(strict=exists), Path(root).resolve(strict=True)
    require(path != root and path.is_relative_to(root), "Use an owned child path: " + str(path))
    return path


def current(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "Use the actual same-job/source record")
    if "repository" in value:
        require(value["repository"] == REPO, "The actual repository differs")


def selected(value, keys):
    return {key: value[key] for key in keys if key in value}


def error_record(error):
    return dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc(),
        mathematical_rejection_not_inferred=True)


def load_pinned(comp, descriptor, role):
    name, size, sha = descriptor
    path = comp / name
    original = receipt(path)
    require((original["bytes"], original["sha256"]) == (size, sha),
        "Frozen lifecycle or metadata source differs: " + name)
    module_name = "_request205_closed_" + role + "_" + sha[:16]
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(module_name, None)
        raise
    return module


def locations(args):
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    base = inside(args.base, temporary, exists=True)
    require(base.parent == temporary and base.name == NAMESPACE,
        "Use the actual exclusive request205 namespace")
    return base, Path(args.computations).resolve(strict=True)


def bind_request(args, base, comp):
    request, rid = read(args.request)
    require(request.get("schema") == REQUEST_SCHEMA and request.get("request_number") == 205,
        "Bind the explicit independent request205")
    require(same(receipt(base / "dispatch-request.json"), rid),
        "Use the actual namespace dispatch-request bytes")
    block = request.get("closed_postsolve")
    required = set(SOURCE_ROLES) | set(DATA_ROLES) | {"orchestrator"}
    require(isinstance(block, dict) and required.issubset(block),
        "Declare all eight closed_postsolve source/parameter identities")
    source_ids = {}
    for role, (name, size, sha) in SOURCE_ROLES.items():
        item = block[role]
        require(isinstance(item, dict) and item.get("file") in
            (name, TOPIC + "/computations/" + name)
            and (item.get("bytes"), item.get("sha256")) == (size, sha),
            "The explicit frozen source identity differs: " + role)
        actual = receipt(comp / name)
        require(same(actual, item), "Actual source bytes differ: " + name)
        source_ids[role] = actual
    own = receipt(__file__)
    item = block["orchestrator"]
    require(isinstance(item, dict) and item.get("file") in
        (ENTRY, TOPIC + "/computations/" + ENTRY) and same(own, item),
        "The request must bind this independent actual orchestrator source")
    source_ids["orchestrator"] = own
    for name, size, sha in (LIFECYCLE, RULE_READER):
        actual = receipt(comp / name)
        require((actual["bytes"], actual["sha256"]) == (size, sha),
            "Keep the exact inherited process/readback implementation: " + name)
        source_ids[name] = actual
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    data = {}
    for role, (name, size, sha) in DATA_ROLES.items():
        item = block[role]
        expected_name = TOPIC + "/notes/" + name
        require(isinstance(item, dict) and item.get("file") == expected_name
            and (item.get("bytes"), item.get("sha256")) == (size, sha),
            "Copy the original published small parameter JSON exactly: " + role)
        path = inside(workspace / expected_name, workspace, exists=True)
        body, identity = read(path, item)
        data[role] = dict(path=path, body=body, identity=identity)
    require(data["work_choices"]["body"].get("schema") ==
        "R437-explicit-first-closed-experiment-work-choices-v1"
        and data["work_choices"]["body"]["construction_mode"] == "initial-construction",
        "Use the original explicit first-construction work choices")
    return request, rid, source_ids, data


def fresh_copy(source, destination):
    require(not destination.exists(), "Do not replace an earlier actual input")
    original = receipt(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Path(source).open("rb") as src, destination.open("xb") as out:
        shutil.copyfileobj(src, out)
        out.flush()
        os.fsync(out.fileno())
    actual = receipt(destination)
    require(same(original, actual), "Exact small-input copy changed bytes")
    return actual


class Run:
    def __init__(self, args):
        self.args = args
        self.base, self.comp = locations(args)
        self.out = self.base / OUTPUTS["journal"]
        require(not self.out.exists(), "Do not replace an earlier closed orchestration")
        self.out.mkdir()
        self.H = load_pinned(self.comp, LIFECYCLE, "lifecycle")
        self.started = time.monotonic()
        self.deadline = None
        self.reserve = 30.0
        self.signals = []
        self.handlers = {}
        self.child = None
        self.active_row = None
        self.report = dict(schema=SCHEMA, source=receipt(__file__), repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            actual_orchestrator_process=self.H.proc_record(os.getpid()),
            actual_base=str(self.base), run_returned=False, error=None,
            external_interruption=None, resource_stop=None, upstream_stop=None,
            all_outer_owned_processes_quiet=True,
            stages=[dict(name=name, started=False, status="unvisited",
                output_directory=str(self.base / OUTPUTS[name])) for name in ("postsolve", "held")],
            all_eight_original_role_names=list(INNER_STAGES),
            old_R437_or_R425_scientific_source_modified=False,
            metric_or_reach_success_is_not_a_held_prerequisite=True,
            raw_cleanup_performed=False, cleanup_allowed=False)
        self.persist()

    def persist(self):
        self.report["elapsed_seconds"] = time.monotonic() - self.started
        write(self.out / "result.json", self.report)

    def receive(self, number, frame):
        self.signals.append(dict(number=int(number), name=signal.Signals(number).name,
            elapsed_seconds=time.monotonic() - self.started))
        self.report["external_interruption"] = dict(received_signals=self.signals,
            not_mathematical_or_ordinary_wall_stop=True)
        if self.child is not None:
            try:
                self.child.signal_observed(signal.SIGTERM)
            except BaseException as error:
                self.report["external_signal_forward_error"] = dict(
                    type=type(error).__name__, message=str(error))

    def install(self):
        for number in (signal.SIGTERM, signal.SIGINT):
            self.handlers[number] = signal.signal(number, self.receive)

    def restore(self):
        for number, previous in self.handlers.items():
            signal.signal(number, previous)

    def skip(self, name, reason):
        row = next(row for row in self.report["stages"] if row["name"] == name)
        require(not row["started"], "Never overwrite a real started role with a skip")
        row.update(status="not-started", reason=reason)
        self.persist()

    def stop_child(self):
        if self.child is None:
            return
        allowance = self.reserve
        if self.deadline is not None:
            allowance = max(0.0, min(allowance, self.deadline - time.time()))
        # This is one extra lifecycle layer. Its R437 child has already
        # received TERM and uses its own original two-second external stop
        # for the scientific group. Give that inner finally time to record
        # quiet, while staying inside the rule owner's 15-second escalation.
        if self.signals:
            allowance = min(allowance, 10.0)
        state = self.child.stop(allowance, external=False)
        self.active_row["observed_child"] = state
        self.active_row["actual_child_exit"] = state["actual_child_returncode"]
        self.active_row["owned_group_quiescent"] = state["owned_group_quiescent"]
        self.report["all_outer_owned_processes_quiet"] = bool(
            self.report["all_outer_owned_processes_quiet"] and state["owned_group_quiescent"])
        self.child = None
        self.active_row = None
        self.persist()

    def invoke(self, name, argv):
        row = next(row for row in self.report["stages"] if row["name"] == name)
        row["command"] = argv
        if self.signals:
            self.skip(name, "external-interruption-before-role")
            return 128 + self.signals[0]["number"]
        remaining = self.deadline - time.time()
        row["actual_seconds_remaining_before_original_deadline"] = remaining
        if remaining <= self.reserve:
            self.report["resource_stop"] = dict(kind="actual-original-science-deadline",
                before_role=name, actual_seconds_remaining=remaining,
                shutdown_reserve_seconds=self.reserve, scientific_role_not_started=True)
            self.skip(name, "original-absolute-clock-has-no-startable-science-allowance")
            return 124
        free = shutil.disk_usage(self.base).free
        if free < self.work["resources"]["free_bytes_reserve"]:
            self.report["resource_stop"] = dict(kind="owned-temporary-free-storage", before_role=name,
                actual_free_bytes=free, scientific_role_not_started=True)
            self.skip(name, "original-explicit-free-storage-resource-unavailable")
            return 124
        stdout, stderr = self.out / (name + ".stdout.log"), self.out / (name + ".stderr.log")
        env = dict(os.environ)
        for key in ("GH_TOKEN", "GITHUB_TOKEN", "MR_TOKEN", "GITHUB_OUTPUT"):
            env.pop(key, None)
        with stdout.open("xb") as so, stderr.open("xb") as se:
            # The frozen R438 owner takes the true newly-created group. A
            # parent Python shared runner PGID is never used as science PGID.
            process = subprocess.Popen(argv, cwd=self.comp, env=env, shell=False,
                stdout=so, stderr=se, start_new_session=True)
            self.child = self.H.OwnedChild(process)
            self.active_row = row
            row.update(started=True, status="running", actual_child_exit=None,
                observed_child=self.child.record(), owned_group_quiescent=False,
                hard_original_science_deadline_unix_seconds=self.deadline)
            self.persist()
            last_disk = time.monotonic()
            try:
                while process.poll() is None:
                    self.child.observe()
                    if self.signals:
                        break
                    now = time.time()
                    if now >= self.deadline - self.reserve:
                        self.report["resource_stop"] = dict(kind="actual-original-science-deadline",
                            during_role=name, absolute_science_deadline_unix_seconds=self.deadline,
                            shutdown_reserve_seconds=self.reserve,
                            scientific_result_not_inferred=True)
                        break
                    if time.monotonic() - last_disk >= 5:
                        free = shutil.disk_usage(self.base).free
                        last_disk = time.monotonic()
                        row["latest_actual_free_bytes"] = free
                        if free < self.work["resources"]["free_bytes_reserve"]:
                            self.report["resource_stop"] = dict(kind="owned-temporary-free-storage",
                                during_role=name, actual_free_bytes=free,
                                scientific_result_not_inferred=True)
                            break
                    try:
                        process.wait(timeout=min(.5, max(.01, self.deadline - self.reserve - now)))
                    except subprocess.TimeoutExpired:
                        pass
            finally:
                self.stop_child()
                so.flush()
                os.fsync(so.fileno())
                se.flush()
                os.fsync(se.fileno())
        row.update(status="returned", stdout=receipt(stdout), stderr=receipt(stderr))
        self.persist()
        if self.signals:
            return 128 + self.signals[0]["number"]
        if self.report["resource_stop"] is not None:
            return 124
        code = row.get("actual_child_exit")
        return code if type(code) is int and 0 <= code <= 255 else 2

    def bind(self):
        request, rid, sources, data = bind_request(self.args, self.base, self.comp)
        self.report.update(request=rid, direct_sources=sources,
            original_published_parameter_files={key: item["identity"] for key, item in data.items()})
        self.work = data["work_choices"]["body"]
        self.reserve = float(self.work["resources"]["child_shutdown_reserve_seconds"])
        self.report["original_eight_role_work_caps_seconds"] = dict(
            self.work["resources"]["stage_budgets_seconds"],
            **self.work["resources"]["parameter_budgets_seconds"],
            held=self.work["held_resources"]["held_budget_seconds"])
        self.report["all_original_parameter_objects_copied_without_resource_changes"] = True
        launch_path = self.base / "BVP-launch" / "result.json"
        if not launch_path.is_file():
            self.report["upstream_stop"] = "actual-BVP-launch-result-absent"
            self.report["actual_deadline_absent_no_template_substitution"] = True
            return False
        launch, lid = read(launch_path)
        current(launch)
        require(launch.get("schema") == UPSTREAM_SCHEMA and launch.get("source_sha256") == UPSTREAM_SHA,
            "Use the actual independent actual202205 launcher")
        self.report["actual_BVP_launch"] = lid
        self.report["actual_BVP_scope"] = selected(launch, (
            "current_finite_BVP_accepted", "completed_driver_return", "actual_child_exit",
            "actual_child_process_started", "owned_group_quiescent_before_readback",
            "resource_stop", "external_interruption", "error"))
        did = launch.get("actual_job_deadline")
        require(isinstance(did, dict) and isinstance(did.get("file"), str),
            "The actual BVP deadline is required; a namespace template is not a replacement")
        deadline_path = inside(did["file"], self.base, exists=True)
        deadline, actual_deadline = read(deadline_path, did)
        current(deadline)
        require(deadline.get("schema") == DEADLINE_SCHEMA and deadline.get("repository") == REPO
            and deadline.get("recipe_sha256") == launch.get("recipe", {}).get("sha256")
            and deadline.get("science_seconds_from_namespace") == 18900
            and deadline.get("readback_reserve_seconds") == 2700,
            "Keep the actual original joint recipe and whole-job clock")
        start = deadline.get("namespace_created_unix_seconds")
        require(type(start) in (int, float) and math.isfinite(start) and start > 0,
            "The actual namespace origin is required")
        self.deadline = start + deadline["science_seconds_from_namespace"]
        self.report.update(actual_job_deadline=actual_deadline,
            original_absolute_science_deadline_unix_seconds=self.deadline,
            original_readback_reserve_seconds=deadline["readback_reserve_seconds"],
            no_new_clock_origin_or_work_budget_created=True)
        recipe_path = self.base / "actual202-ten-BVP-input" / "actual202-accurate-ten-full453-frozen450-recipe.json"
        recipe, recipe_id = read(recipe_path, launch["recipe"])
        require(recipe.get("schema") == RECIPE_SCHEMA and recipe.get("request_number") == 205,
            "Use the true generated actual202205 recipe")
        self.report["actual_ten_BVP_recipe"] = recipe_id
        # Only the old launcher's explicit original finite acceptance controls
        # whether its field can be supplied. There is no replacement test here.
        if (launch.get("current_finite_BVP_accepted") is not True
                or launch.get("completed_driver_return") is not True
                or launch.get("actual_child_exit") != 0
                or launch.get("owned_group_quiescent_before_readback") is not True
                or launch.get("resource_stop") is not None
                or launch.get("external_interruption") is not None):
            self.report["upstream_stop"] = "original-complete450-acceptance-or-quiet-not-returned"
            return False
        cdir, geometry = self.base / "continuous-E", self.base / "current-geometry"
        cid, gid = receipt(cdir / "result.json"), receipt(geometry / "result.json")
        self.report.update(actual_continuous_C_result=cid, actual_geometry_result=gid)
        policy = fresh_copy(data["parameter_policy"]["path"],
            self.out / DATA_ROLES["parameter_policy"][0])
        work = fresh_copy(data["work_choices"]["path"], self.out / DATA_ROLES["work_choices"][0])
        self.report["actual_parameter_copies"] = dict(parameter_policy=policy, work_choices=work)
        source_topic = Path(self.args.source_topic).resolve(strict=True)
        proof_directory = Path(self.args.proof_directory).resolve(strict=True)
        self.spec = dict(schema=RUNNER_SCHEMA + "-input-v1", upstream_kind="actual202205",
            namespace=str(self.base), upstream_launch_directory=str(launch_path.parent),
            upstream_result_sha256=lid["sha256"], job_deadline=str(deadline_path),
            job_deadline_sha256=actual_deadline["sha256"], geometry_directory=str(geometry),
            continuous_e_directory=str(cdir), continuous_e_result_sha256=cid["sha256"],
            computations=str(self.comp), source_topic=str(source_topic), proof_directory=str(proof_directory),
            out=str(self.base / OUTPUTS["postsolve"]),
            construction_policy=dict(file=policy["file"], sha256=policy["sha256"]),
            construction_mode=self.work["construction_mode"],
            **{key: self.work[key] for key in ("resources", "metric", "c_queries", "reach", "witness_resolution")})
        self.spec_id = write(self.out / "actual-R452-input.json", self.spec)
        self.report["actual_postsolve_input"] = self.spec_id
        self.persist()
        return True

    def held_input(self):
        row = self.report["stages"][0]
        path = self.base / OUTPUTS["postsolve"] / "procedure.json"
        if not row["started"] or row.get("owned_group_quiescent") is not True or not path.is_file():
            self.skip("held", "actual-postsolve-procedure-or-outer-quiet-unavailable")
            return None
        procedure, pid = read(path)
        require(procedure.get("schema") == RUNNER_SCHEMA
            and procedure.get("source", {}).get("sha256") == SOURCE_ROLES["runner"][2],
            "Keep the actual returned R452 procedure identity")
        current(procedure)
        self.report["actual_postsolve_procedure"] = pid
        R = load_pinned(self.comp, SOURCE_ROLES["reader"], "postsolve_quiet")
        quiet = R.process_quiet(procedure)
        self.report["actual_nested_postsolve_quiet"] = quiet
        if (procedure.get("procedure_returned") is not True
                or procedure.get("all_owned_children_quiescent") is not True
                or quiet.get("all_actual_owned_processes_quiet") is not True):
            self.skip("held", "actual-postsolve-nested-owners-not-completely-quiet")
            return None
        witness = procedure.get("actual_witness_plan")
        descriptor = witness.get("witness_plan") if isinstance(witness, dict) else None
        shared = self.base / OUTPUTS["postsolve"] / "shared_field" / "result.json"
        if not isinstance(descriptor, dict) or not shared.is_file():
            self.skip("held", "actual-original-shared-field-or-generated-witness-plan-unavailable")
            return None
        witness_path = inside(descriptor["file"], self.base / OUTPUTS["postsolve"], exists=True)
        require(same(receipt(witness_path), descriptor), "The actual generated witness bytes differ")
        self.report["actual_witness_plan"] = descriptor
        self.report["actual_shared_field_result"] = receipt(shared)
        # The original held binder rechecks radial/atlas/shared, the complete
        # current450/C/marker source closure and its old transport-aware flags.
        # Neither metric nor reach flags are read by this scheduling decision.
        spec = dict(schema=HELD_SCHEMA + "-input-v1",
            postsolve_directory=str(path.parent), postsolve_procedure_sha256=pid["sha256"],
            postsolve_input=self.spec_id["file"], postsolve_input_sha256=self.spec_id["sha256"],
            witness_plan=str(witness_path), witness_plan_sha256=descriptor["sha256"],
            held=self.work["held"], resources=self.work["held_resources"],
            out=str(self.base / OUTPUTS["held"]))
        original = write(self.out / "actual-R452-held-input.json", spec)
        self.report["actual_held_input"] = original
        self.persist()
        return original

    def run(self):
        code = 2
        self.install()
        try:
            if self.bind():
                code = self.invoke("postsolve", [sys.executable, "-u", str(self.comp / SOURCE_ROLES["runner"][0]),
                    "--input", self.spec_id["file"], "--input-sha256", self.spec_id["sha256"]])
                held = self.held_input()
                if held is not None:
                    held_code = self.invoke("held", [sys.executable, "-u", str(self.comp / SOURCE_ROLES["held"][0]),
                        "run", "--input", held["file"], "--input-sha256", held["sha256"]])
                    if code == 0:
                        code = held_code
            else:
                code = 3
                for name in ("postsolve", "held"):
                    self.skip(name, self.report["upstream_stop"])
        except BaseException as error:
            code = 2
            self.report["error"] = error_record(error)
        finally:
            try:
                self.stop_child()
            except BaseException as error:
                self.report["shutdown_error"] = error_record(error)
                self.report["all_outer_owned_processes_quiet"] = False
                code = 2
            for row in self.report["stages"]:
                if row["status"] == "unvisited":
                    row.update(status="not-started", reason="preceding-orchestration-error-or-interruption")
            if self.signals:
                code = 128 + self.signals[0]["number"]
            self.report.update(run_returned=True, actual_exit_code=code,
                unstarted_outer_roles=[row["name"] for row in self.report["stages"] if not row["started"]],
                necessary_readback_still_required=True)
            self.persist()
            self.restore()
        print(json.dumps(dict(event="request205-closed-postsolve-orchestration-returned",
            result=receipt(self.out / "result.json"), actual_exit_code=code,
            raw_cleanup_performed=False, complete_task_certified=False), separators=(",", ":")), flush=True)
        return code


@contextlib.contextmanager
def no_job_outputs():
    previous = os.environ.pop("GITHUB_OUTPUT", None)
    try:
        yield
    finally:
        if previous is not None:
            os.environ["GITHUB_OUTPUT"] = previous


def actual_quiet(H, report):
    owner = report.get("actual_orchestrator_process")
    now = H.proc_record(owner["pid"]) if isinstance(owner, dict) and type(owner.get("pid")) is int else None
    owner_live = bool(H.same_process(owner, now) and now["state"] != "Z")
    groups, unknown = [], []
    if not isinstance(owner, dict):
        unknown.append("missing-actual-orchestrator-pid-starttime")
    rows = report.get("stages")
    if not isinstance(rows, list) or [r.get("name") for r in rows] != ["postsolve", "held"]:
        unknown.append("missing-complete-outer-stage-addresses")
        rows = []
    for row in rows:
        if row.get("started") is not True:
            if row.get("status") != "not-started" or not row.get("reason"):
                unknown.append("unclassified-outer-role:" + str(row.get("name")))
            continue
        child = row.get("observed_child")
        pid = child.get("pid") if isinstance(child, dict) else None
        if type(pid) is not int:
            unknown.append("missing-owned-group-identity:" + str(row["name"]))
            continue
        live = [r for r in H.group_rows(pid) if r["state"] != "Z"]
        groups.append(dict(name=row["name"], original_owned_child=child,
            actual_live_group_members=live, currently_quiet=not live))
    return dict(actual_orchestrator_process=owner, same_original_owner_still_live=owner_live,
        actual_owned_groups=groups, unknown_scope=unknown,
        quiescent=not owner_live and not unknown and all(r["currently_quiet"] for r in groups),
        parent_shared_runner_PGID_not_treated_as_scientific_group=True,
        no_process_signalled_by_readback=True)


def original_reader(comp, role, directory, output):
    module = load_pinned(comp, SOURCE_ROLES[role], "necessary_" + role)
    argv = (["--directory", str(directory), "--out", str(output)] if role == "reader" else
        ["readback", "--directory", str(directory), "--computations", str(comp), "--out", str(output)])
    with no_job_outputs():
        code = module.main(argv)
    value, original = read(output)
    expected = READER_SCHEMA if role == "reader" else HELD_SCHEMA + "-necessary-v1"
    require(value.get("schema") in (expected, expected + "-over-budget"),
        "An original necessary reader returned an unregistered schema")
    return dict(actual_source=receipt(comp / SOURCE_ROLES[role][0]), actual_argv=argv,
        actual_exit_code=code, original_necessary_summary=original,
        actual_schema=value["schema"], necessary_readback_complete=(code == 0
            and value.get("schema") == expected and value.get("necessary_readback_complete") is True),
        complete_original_necessary_frame_printed_by_unchanged_reader=True,
        scientific_flags_not_duplicated_in_combined_job_output=True)


def postsolve_rules(base, comp, report, R):
    owner = load_pinned(comp, SOURCE_ROLES["owner"], "rules_owner")
    before = os.environ.get("VISIBLE_BASE")
    if before is not None:
        require(Path(before).resolve() == base, "The actual owner namespace differs")
    os.environ["VISIBLE_BASE"] = str(base)
    try:
        observation = owner.observe()
    finally:
        if before is None:
            os.environ.pop("VISIBLE_BASE", None)
        else:
            os.environ["VISIBLE_BASE"] = before
    require(owner.ROLES.get("postsolve") == "postsolve-rule-sync",
        "Use the actual extended seven-role owner")
    result = dict(actual_owner_source=receipt(comp / SOURCE_ROLES["owner"][0]),
        original_global_quiet_observation={key: observation[key] for key in (
            "schema", "repository", "run_id", "source_commit", "unix_seconds",
            "live_original_owned_processes", "unknown_owner_scopes", "quiescent") if key in observation},
        all_seven_role_launch_receipts_identity=dict(
            canonical_bytes=len(canonical(observation.get("original_process_receipts", []))),
            canonical_sha256=digest(canonical(observation.get("original_process_receipts", [])))),
        actual_postsolve_launch_observation=[r for r in observation.get("original_process_receipts", [])
            if r.get("role") == "postsolve"], original_rule_documents=[], original_error_logs=[],
        postsolve_owner_receipts=[], original_metadata_reader_source=receipt(comp / RULE_READER[0]))
    if observation.get("quiescent") is not True:
        result.update(files_not_read_while_any_original_owner_or_unknown_scope_active=True,
            complete=False)
        return result
    root = base / "postsolve-rule-sync"
    if not root.is_dir():
        result["missing_actual_postsolve_rule_directory"] = True
        result["complete"] = False
        return result
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("A rules receipt must not be a symlink: " + str(path))
        if not path.is_file():
            continue
        inside(path, root, exists=True)
        scope = str(path.relative_to(base))
        if path.suffix == ".json":
            body, identity = R.document(path, scope, required=True)
            result["original_rule_documents"].append(dict(file=identity,
                original_value=R.small(body, (scope,)), parsed=body is not None))
        else:
            result["original_error_logs"].append(R.log_view(path, scope))
    directory = base / "owned-rule-sync-processes"
    for path in sorted(directory.glob("postsolve-*.json")):
        body, original = R.document(path, path.name, required=True)
        if body is not None:
            current(body)
            require(body.get("schema") == "request205-owned-process-receipt-v1"
                and body.get("role") == "postsolve", "Actual postsolve owner role differs")
        result["postsolve_owner_receipts"].append(dict(file=original,
            original_value=R.small(body, (path.name,)), parsed=body is not None))
    names = {Path(row["file"]["file"]).name for row in result["postsolve_owner_receipts"] if row["file"]}
    required = {"postsolve-parent-launch.json", "postsolve-parent-return.json",
        "postsolve-science-launch.json", "postsolve-science-return.json"}
    result["missing_original_owner_receipts"] = sorted(required - names)
    result["complete"] = not result["missing_original_owner_receipts"] and not R.ERRORS
    result["original_log_selection_scope"] = (
        "34b49f exact log_view: full bytes/lines hashed; first two and last literal exception, "
        "traceback, signal or storage-error matches; original short(...,1200) excerpts. "
        "small() retains original key presence, hashes declared raw members and lists longer than16, "
        "and uses the original1800-character string limit; no complete large log is transported.")
    return result


def build_readback(args):
    base, comp = locations(args)
    request, rid, sources, data = bind_request(args, base, comp)
    out = base / OUTPUTS["readback"]
    require(not out.exists(), "Do not replace an earlier actual closed necessary readback")
    out.mkdir()
    value = dict(schema=READBACK_SCHEMA, source=receipt(__file__), repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        request=rid, original_direct_sources=sources, necessary_readback_complete=False,
        quiescent=False, scientific_success_not_inferred=True, metadata_errors=[],
        original_geometric_readers={}, raw_cleanup_performed=False)
    H = load_pinned(comp, LIFECYCLE, "readback_lifecycle")
    R = load_pinned(comp, RULE_READER, "rules_metadata")
    report = None
    try:
        report, original = read(base / OUTPUTS["journal"] / "result.json")
        current(report)
        require(report.get("schema") == SCHEMA and same(report.get("source"), receipt(__file__))
            and same(report.get("request"), rid), "The actual orchestration result is not this dispatch")
        value["original_orchestration_result"] = original
        value["original_orchestration_scope"] = selected(report, (
            "run_returned", "actual_exit_code", "elapsed_seconds", "error", "shutdown_error",
            "external_interruption", "resource_stop", "upstream_stop", "actual_BVP_launch",
            "actual_BVP_scope", "actual_job_deadline", "actual_ten_BVP_recipe",
            "original_absolute_science_deadline_unix_seconds", "original_readback_reserve_seconds",
            "actual_continuous_C_result", "actual_geometry_result", "actual_parameter_copies",
            "actual_postsolve_input", "actual_held_input", "actual_witness_plan",
            "actual_shared_field_result", "original_eight_role_work_caps_seconds", "unstarted_outer_roles",
            "actual_deadline_absent_no_template_substitution"))
        value["original_outer_role_states"] = [selected(row, (
            "name", "started", "status", "reason", "actual_child_exit", "owned_group_quiescent",
            "actual_seconds_remaining_before_original_deadline", "hard_original_science_deadline_unix_seconds",
            "latest_actual_free_bytes", "stdout", "stderr")) for row in report.get("stages", [])]
        quiet = actual_quiet(H, report)
        value["actual_outer_process_quiet"] = quiet
        value["quiescent"] = bool(quiet["quiescent"] and report.get("run_returned") is True
            and report.get("all_outer_owned_processes_quiet") is True)
        if not value["quiescent"]:
            value["mutable_or_incomplete_orchestration_tree_not_read"] = True
        else:
            value["original_outer_logs"] = []
            for row in report["stages"]:
                name = row["name"]
                for kind in ("stdout", "stderr"):
                    path = base / OUTPUTS["journal"] / (name + "." + kind + ".log")
                    if path.is_file():
                        if isinstance(row.get(kind), dict):
                            require(same(receipt(path), row[kind]), "A quiet actual outer log changed")
                        value["original_outer_logs"].append(R.log_view(path, name + "-" + kind))
                procedure = base / OUTPUTS[name] / "procedure.json"
                if procedure.is_file():
                    try:
                        role = "reader" if name == "postsolve" else "held"
                        value["original_geometric_readers"][name] = original_reader(comp, role,
                            procedure.parent, out / (name + "-necessary.json"))
                    except BaseException as error:
                        value["metadata_errors"].append(dict(role=name, **error_record(error)))
                        value["original_geometric_readers"][name] = dict(necessary_readback_complete=False,
                            actual_procedure=receipt(procedure), original_reader_did_not_return=True)
                elif row["started"] is False and row.get("status") == "not-started" and row.get("reason"):
                    require(not (base / OUTPUTS[name]).exists(),
                        "An explicitly unstarted role unexpectedly has unbound raw output")
                    value["original_geometric_readers"][name] = dict(necessary_readback_complete=True,
                        original_role_not_started=True, original_reason=row["reason"],
                        original_producer_result_not_fabricated=True)
                else:
                    value["original_geometric_readers"][name] = dict(necessary_readback_complete=False,
                        original_started_role_missing_actual_procedure=True,
                        scope_unknown_raw_retained=True)
            require(same(receipt(base / OUTPUTS["journal"] / "result.json"), original),
                "The original orchestration record changed during necessary readback")
    except BaseException as error:
        value["metadata_errors"].append(error_record(error))
    # Independently retain the new rules/owner scope even if a prior original
    # geometry reader failed. A parse/read failure never enables deletion.
    try:
        value["postsolve_rule_and_owner_scope"] = postsolve_rules(base, comp, report, R)
    except BaseException as error:
        value["metadata_errors"].append(dict(role="postsolve-rules", **error_record(error)))
        value["postsolve_rule_and_owner_scope"] = dict(complete=False, unknown_scope=True)
    value["original_metadata_selection_errors"] = list(R.ERRORS)
    value["original_metadata_omitted_members"] = list(R.OMISSIONS)
    value["necessary_readback_complete"] = bool(value["quiescent"]
        and set(value["original_geometric_readers"]) == {"postsolve", "held"}
        and all(r.get("necessary_readback_complete") is True for r in value["original_geometric_readers"].values())
        and value["postsolve_rule_and_owner_scope"].get("complete") is True
        and not value["metadata_errors"] and not R.ERRORS)
    return value, out


def publish_metadata(value, out, base):
    raw = canonical(value)
    complete = value.get("necessary_readback_complete") is True and value.get("quiescent") is True
    if len(raw) > LIMIT:
        value = dict(schema=READBACK_SCHEMA + "-over-budget", repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            necessary_readback_complete=False, quiescent=value.get("quiescent"),
            attempted_summary_bytes=len(raw), attempted_summary_sha256=digest(raw), limit=LIMIT,
            original_geometric_readers=value.get("original_geometric_readers"),
            original_orchestration_result=value.get("original_orchestration_result"),
            complete_task_not_certified=True, cleanup_marker_not_written=True,
            raw_deleted_uploaded_split_or_encoded=False)
        complete = False
    original = write(out / "summary.json", value)
    raw = (out / "summary.json").read_bytes()
    require(len(raw) <= LIMIT, "The fallback itself must remain one small necessary document")
    marker = base / OUTPUTS["marker"]
    require(not marker.exists(), "Never replace an existing completion marker")
    marker_id = None
    if complete:
        marker_id = write(marker, dict(schema=MARKER_SCHEMA, repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            complete=True, quiescent=True,
            necessary_summary=selected(original, ("bytes", "sha256")),
            raw_cleanup_performed=False, not_a_scientific_acceptance_certificate=True))
    print("BEGIN_REQUEST205_CLOSED_POSTSOLVE_METADATA", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_REQUEST205_CLOSED_POSTSOLVE_METADATA", flush=True)
    print(json.dumps(dict(event="request205-closed-postsolve-necessary-identity",
        original_summary=original, complete=complete, completion_marker=marker_id,
        raw_cleanup_performed=False), separators=(",", ":")), flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        delimiter = "CLOSED205_" + original["sha256"]
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="ascii") as stream:
            stream.write("closed_postsolve_summary<<" + delimiter + "\n" + raw.decode("ascii") + delimiter + "\n")
            stream.write("closed_postsolve_summary_bytes=" + str(original["bytes"]) + "\n")
            stream.write("closed_postsolve_summary_sha256=" + original["sha256"] + "\n")
            stream.write("closed_postsolve_readback_complete=" + ("true" if complete else "false") + "\n")
    return 0 if complete else 70


def readback_command(args):
    base, comp = locations(args)
    require(not (base / OUTPUTS["readback"]).exists()
        and not (base / OUTPUTS["marker"]).exists(),
        "Never replace a previous necessary readback or cleanup marker")
    try:
        value, out = build_readback(args)
    except BaseException as error:
        out = base / OUTPUTS["readback"]
        out.mkdir(exist_ok=True)
        value = dict(schema=READBACK_SCHEMA, repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            source=receipt(__file__), necessary_readback_complete=False, quiescent=False,
            metadata_errors=[error_record(error)], original_scope_unknown=True,
            no_missing_result_reconstructed_from_a_digest=True, raw_cleanup_performed=False)
    return publish_metadata(value, out, base)


def main(argv=None):
    actions()
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("run", "readback"):
        sub = commands.add_parser(command)
        sub.add_argument("--request", type=Path, required=True)
        sub.add_argument("--base", type=Path, required=True)
        sub.add_argument("--computations", type=Path, required=True)
        if command == "run":
            sub.add_argument("--source-topic", type=Path, required=True)
            sub.add_argument("--proof-directory", type=Path, required=True)
    args = parser.parse_args(argv)
    return Run(args).run() if args.command == "run" else readback_command(args)


if __name__ == "__main__":
    raise SystemExit(main())
