#!/usr/bin/env python3
"""R489: fresh same-C1440/six head, original full cut readout, honest intersection.

Only the original f12f and1c39 scientific entry points are called. The new
wrapper owns their actual processes under the existing original205 deadline;
it neither replaces the original C/CP/definition nor selects a deep root.
No accepted field, run, new work parameter or narrower bound is predeclared.
Scientific execution is restricted to the named public repository Actions.
Author: geometry agent (AI),2026-11-16.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as Q
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

REPO = "Rogerhu12/math-research-public"
SCHEMA = "R489-same-job-same-C-complete-head-and-cut-refinement-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
NECESSARY_SCHEMA = SCHEMA + "-necessary-v1"
LIMIT = 90000
C_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
C_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
C_SCHEMA = "R286-original-stored-convention-C-continuous-E-cover-v3"
MODEL_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
CUT_NAME = "geometry_20261115_stored_C_v3_cut_twojet_readout.py"
CUT_SHA = "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed"
CUT_SCHEMA = "R286-v3-original-binary-cut-complete-twojet-hull-v1"
OWNER_NAME = "geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py"
OWNER_SHA = "5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95"
LAUNCH_NAME = "geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py"
LAUNCH_SHA = "227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7"
LAUNCH_SCHEMA = "R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1"
DRIVER_NAME = "geometry_20261116_actual202_accurate_ten_full453_frozen450.py"
DRIVER_SHA = "56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615"
DEADLINE_SCHEMA = "request205-owned-job-science-deadline-v1"
PINS = {C_NAME:C_SHA, CUT_NAME:CUT_SHA, OWNER_NAME:OWNER_SHA,
        LAUNCH_NAME:LAUNCH_SHA, DRIVER_NAME:DRIVER_SHA}
WORK_KEYS = ("precision_bits", "integral_absolute_bits", "integral_relative_bits",
    "analytic_guard_bits", "integral_evaluation_limit", "value_width_bits",
    "max_depth", "query_depth", "max_panels", "max_query_nodes", "budget_seconds")
INPUT_ROLES = {"config":"config", "ledger_ready":"calibration_ledger",
    "stored_ready":"stored_reference", "queries":"query_input", "proof":"proof"}
FIELDS = ("E", "E_r", "E_rr")
SIX = ("A", "B", "sqrtE_A", "sqrtE_B", "w_A", "w_B")
SEMANTIC_OMISSIONS = ("runtime", "work_parameters")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPO
        and os.environ.get("GITHUB_RUN_ID") and os.environ.get("GITHUB_SHA"),
        "Only this repository's actual public Actions may execute this source")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def unique(items):
    value = {}
    for key, item in items:
        require(key not in value, "Duplicate JSON key: " + key)
        value[key] = item
    return value


def finite_number(token):
    value = float(token)
    require(math.isfinite(value), "No nonfinite JSON number")
    return value


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique,
        parse_int=lambda token:-0.0 if token == "-0" else int(token),
        parse_float=finite_number,
        parse_constant=lambda token:(_ for _ in ()).throw(ValueError("Nonfinite JSON token")))


def receipt(path, check=None):
    path = Path(path).resolve(strict=True)
    require(path.is_file() and not path.is_symlink(), "Use an actual ordinary input file")
    before = path.stat(); size = 0; h = hashlib.sha256()
    with path.open("rb") as stream:
        while raw := stream.read(1048576):
            if check is not None:
                check()
            size += len(raw); h.update(raw)
    after = path.stat()
    require((before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns)
        == (after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns)
        and size == after.st_size, "An input changed while being read")
    return dict(file=str(path),bytes=size,sha256=h.hexdigest())


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and all(
        a.get(key) == b.get(key) for key in ("bytes", "sha256"))


def read(path, expected=None, check=None):
    actual = receipt(path, check)
    if expected is not None:
        if isinstance(expected, str):
            require(actual["sha256"] == expected, "The actual input SHA differs")
        else:
            require(same(actual, expected), "The actual input bytes/SHA differ")
    raw = Path(actual["file"]).read_bytes()
    require(len(raw) == actual["bytes"] and digest(raw) == actual["sha256"],
        "A JSON file changed after its receipt")
    return decode(raw), actual


def write(path, value, *, replace=False):
    path = Path(path); raw = canonical(value)
    if replace:
        temporary = path.with_name(path.name + ".writing")
        with temporary.open("wb") as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, path)
    else:
        with path.open("xb") as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return dict(file=str(path.resolve()),bytes=len(raw),sha256=digest(raw))


def inside(path, root, *, exists=True):
    path = Path(path).resolve(strict=exists)
    require(path.is_relative_to(Path(root).resolve(strict=True)),
        "Use the same original job-owned temporary namespace")
    return path


def current(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "The original object must belong to this actual run/source")
    if "repository" in value:
        require(value["repository"] == REPO, "The original repository differs")


def local_member(directory, row):
    require(isinstance(row, dict) and isinstance(row.get("file"), str),
        "The complete original member descriptor is missing")
    path = Path(row["file"])
    require(not path.is_absolute() and ".." not in path.parts,
        "Use an original relative producer member")
    return inside(Path(directory)/path, directory)


def load_owner(comp):
    path = Path(comp)/OWNER_NAME
    require(receipt(path)["sha256"] == OWNER_SHA, "The frozen OwnedChild source differs")
    name = "_r489_original_r438_owned_child"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def valid_positive(value, label):
    require(type(value) in (int, float) and math.isfinite(value) and value > 0,
        "Declare an explicit positive resource: " + label)
    return float(value)


def endpoint(value):
    require(isinstance(value, dict) and set(("mantissa", "binary_exponent")) <= set(value),
        "Use complete original exact dyadic endpoints, not displays")
    m = int(value["mantissa"]); e = value["binary_exponent"]
    require(type(e) is int, "An original binary exponent must be an integer")
    return Q(m << e) if e >= 0 else Q(m, 1 << (-e))


def interval(value):
    lo, hi = endpoint(value["lower"]), endpoint(value["upper"])
    require(lo <= hi, "A complete original interval is reversed")
    return lo, hi


def intersect(a, b):
    al, ah = interval(a); bl, bh = interval(b)
    lo, hi = max(al, bl), min(ah, bh)
    require(lo <= hi, "Two complete same-C enclosures have empty intersection; no refutation inferred")
    return dict(lower_exact=str(lo),upper_exact=str(hi),full_width_exact=str(hi-lo),
        original_bounds=[copy.deepcopy(a),copy.deepcopy(b)],
        no_endpoint_was_moved_inside_either_proved_interval=True,
        strict_width_improvement_over_baseline=(hi-lo < ah-al))


def semantic_bindings(old, new):
    require(old.get("schema") == C_SCHEMA+"-input-binding"
        and new.get("schema") == C_SCHEMA+"-input-binding"
        and old.get("source_sha256") == new.get("source_sha256") == C_SHA,
        "Both input bindings must be the actual original f12f source")
    require(set(old) == set(new), "The complete input-binding key set differs")
    before = {k:v for k,v in old.items() if k not in SEMANTIC_OMISSIONS}
    after = {k:v for k,v in new.items() if k not in SEMANTIC_OMISSIONS}
    require(canonical(before) == canonical(after),
        "Same-C equality includes every original non-work binding field and signed JSON word")
    require(old["work_parameters"]["deep_definition"]
        == new["work_parameters"]["deep_definition"] == "original-exact-root-family",
        "Do not select or change the original deep-root family")
    changed = {key:dict(old=old["work_parameters"].get(key),new=new["work_parameters"].get(key))
        for key in set(old["work_parameters"]) | set(new["work_parameters"])
        if canonical(old["work_parameters"].get(key)) != canonical(new["work_parameters"].get(key))}
    require(set(changed) <= set(WORK_KEYS), "A non-work original input was changed")
    return dict(all_non_work_input_binding_fields_exactly_equal=True,
        complete_compared_key_set=sorted(before),
        compared_canonical_bytes=len(canonical(before)),
        compared_canonical_sha256=digest(canonical(before)),
        ignored_sections=list(SEMANTIC_OMISSIONS),
        original_runtime=old["runtime"],new_runtime=new["runtime"],
        actual_work_parameter_changes=changed,deep_definition="original-exact-root-family",
        global_lambda_shallow_rows_cap_flat_weight_cut_and_root_scope_unchanged=True,
        unknown_new_math_keys_are_not_ignored=True)


def checked_C(directory, expected):
    value, rid = read(Path(directory)/"result.json", expected)
    current(value)
    require(value.get("schema") == C_SCHEMA and value.get("source_sha256") == C_SHA
        and value.get("target_model_schema") == MODEL_SCHEMA,
        "Use a genuine same-run original complete-or-partial C producer result")
    binding, bid = read(local_member(directory,value["input_binding"]),value["input_binding"])
    require(binding.get("source_sha256") == C_SHA, "The actual original C binding differs")
    return value, rid, binding, bid


def checked_cut(path, expected, source_result, source_binding):
    value, rid = read(path, expected); current(value)
    require(value.get("schema") == CUT_SCHEMA and value.get("source_sha256") == CUT_SHA
        and value.get("actual_producer", {}).get("sha256") == C_SHA
        and same(value.get("actual_source_result"),source_result)
        and same(value.get("actual_input_binding"),source_binding),
        "Use the original full cut reader actually bound to this C result/binding")
    return value, rid


class Stop(RuntimeError):
    pass


class Recompute:
    def __init__(self, path, expected):
        actions()
        self.input, self.input_id = read(path, expected)
        self.started = time.monotonic(); self.wall_started = time.time()
        self.child = None; self.active = None; self.handlers = {}; self.signals = []
        self.comp = None; self.H = None; self.deadline = None; self.readback_end = None
        self.phase_end = None; self.reserve = None; self.out = None
        self.report = dict(schema=SCHEMA,source=receipt(__file__),repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            actual_input=self.input_id,binding_complete=False,
            new_complete_C_enclosures=False,new_complete_cut_enclosures=False,
            same_semantic_C_proved_by_actual_bindings=False,intersection=None,
            new_accepted_field_created=False,old_CP_definition_or_raw_overwritten=False,
            downstream_R400_R416_refined_leaf_consumer_registered=False,
            phases=[dict(name=name,started=False,status="not_started")
                    for name in ("head_recompute", "complete_cut_readout")],
            error=None,resource_stop=None,external_interruption=None,
            all_owned_children_quiescent=True,
            original_baseline_is_retained_independently_of_new_computation=True,
            new_scientific_acceptance_gate_added=False,raw_deleted=False)

    def persist(self):
        if self.out is not None:
            self.report["elapsed_seconds_including_binding"] = time.monotonic()-self.started
            write(self.out/"result.json",self.report,replace=True)

    def receive(self, number, frame):
        self.signals.append(dict(number=int(number),name=signal.Signals(number).name,
            elapsed_seconds=time.monotonic()-self.started))
        self.report["external_interruption"] = copy.deepcopy(self.signals)
        # No asynchronous exception can strand Popen before OwnedChild assignment.
        if self.child is not None:
            self.child.signal_observed(signal.SIGTERM)

    def check(self):
        if self.signals:
            raise Stop("external_interruption; not a mathematical or wall-clock rejection")
        if self.phase_end is not None and time.time() >= self.phase_end-self.reserve:
            raise Stop("actual_original_deadline_or_declared_complete_phase_budget_reached")
        if self.out is not None and self.reserve is not None:
            free = shutil.disk_usage(self.out).free
            if free < self.input["resources"]["free_bytes_reserve"]:
                raise Stop("declared_temporary_storage_reserve_reached")

    def bind(self):
        d = self.input
        require(d.get("schema") == INPUT_SCHEMA, "Use the explicit independent R489 input")
        current(d)
        self.comp = Path(d["computations"]).resolve(strict=True)
        require(self.comp == Path(__file__).resolve().parent, "Use the actual source HERE")
        self.namespace = inside(d["namespace"],os.environ["RUNNER_TEMP"])
        self.out = inside(d["out"],self.namespace,exists=False)
        require(not self.out.exists(), "Use a new owned R489 output directory")
        require(not self.comp.is_relative_to(self.out), "New output must not own its source directory")
        self.out.mkdir(parents=True); (self.out/"large-arrays").mkdir()
        for number in (signal.SIGTERM,signal.SIGINT):
            self.handlers[number] = signal.signal(number,self.receive)
        resources = d["resources"]
        require(set(resources) == {"complete_phase_budget_seconds", "cut_readout_budget_seconds",
            "child_shutdown_reserve_seconds", "free_bytes_reserve"},
            "Declare the complete phase, original cut-readout and shutdown/storage resources")
        phase = valid_positive(resources["complete_phase_budget_seconds"],"complete phase")
        self.reserve = valid_positive(resources["child_shutdown_reserve_seconds"],"child shutdown")
        valid_positive(resources["cut_readout_budget_seconds"],"cut readout")
        require(type(resources["free_bytes_reserve"]) is int and resources["free_bytes_reserve"] > 0,
            "Declare the temporary free-byte resource")
        self.phase_end = self.wall_started+phase
        self.report["actual_declared_resources"] = copy.deepcopy(resources)
        self.report["producer_process"] = None
        sources = {name:receipt(self.comp/name) for name in PINS}
        require(all(sources[name]["sha256"] == expected for name,expected in PINS.items()),
            "Retain every actual original scientific/lifecycle source")
        self.H = load_owner(self.comp)
        self.report["producer_process"] = self.H.proc_record(os.getpid())
        self.report["actual_direct_sources"] = sources
        launch, lid = read(inside(d["clock"]["launch_result"]["file"],self.namespace),
            d["clock"]["launch_result"]); current(launch)
        require(launch.get("schema") == LAUNCH_SCHEMA
            and launch.get("source_sha256") == LAUNCH_SHA
            and launch.get("driver") == dict(file=DRIVER_NAME,sha256=DRIVER_SHA),
            "This component registers actual202205, not an invented generic origin")
        deadline, did = read(inside(d["clock"]["actual_job_deadline"]["file"],self.namespace),
            d["clock"]["actual_job_deadline"]); current(deadline)
        require(same(did,launch.get("actual_job_deadline"))
            and deadline.get("schema") == DEADLINE_SCHEMA
            and deadline.get("science_seconds_from_namespace") == 18900
            and deadline.get("readback_reserve_seconds") == 2700
            and deadline.get("recipe_sha256") == launch.get("recipe",{}).get("sha256"),
            "Use the unchanged actual launch-bound original deadline, never a new clock")
        began = deadline.get("namespace_created_unix_seconds")
        require(type(began) in (int,float) and math.isfinite(began), "The original start is absent")
        self.deadline = began+18900; self.readback_end = self.deadline+2700
        self.phase_end = min(self.phase_end,self.deadline)
        self.report.update(actual_original_launch=lid,actual_job_deadline=did,
            original_science_deadline_unix_seconds=self.deadline,
            original_readback_deadline_unix_seconds=self.readback_end,
            phase_deadline_unix_seconds=self.phase_end,clock_restarted=False,
            source_scope="actual202205 original clock; not all other historical origins")
        self.persist(); self.check()
        b = d["baseline_C"]
        self.old_dir = inside(b["directory"],self.namespace)
        require(not self.old_dir.is_relative_to(self.out), "Never own or overwrite the baseline C")
        self.old, oid, self.old_binding, obid = checked_C(self.old_dir,b["result_sha256"])
        self.old_cut, ocid = checked_cut(inside(d["baseline_cut"]["file"],self.namespace),
            d["baseline_cut"],oid,obid)
        self.report["baseline"] = dict(C_result=oid,C_input_binding=obid,cut_readout=ocid,
            original_complete_C=self.old.get("continuous_convention_C_query_enclosures_complete"),
            original_complete_cut=self.old_cut.get("point_twojet_enclosure_complete"),
            original_C_and_cut_objects_remain_unmodified=True)
        require(set(d["original_inputs"]) == set(INPUT_ROLES), "Keep all original five input roles")
        self.original = {}
        for role,key in INPUT_ROLES.items():
            desc = d["original_inputs"][role]
            path = Path(desc["file"]).resolve(strict=True)
            require(not path.is_relative_to(self.out), "Do not place an original input under new output")
            actual = receipt(path,self.check)
            require(same(actual,desc) and same(actual,self.old_binding[key]),
                "An original exact input was changed: "+role)
            self.original[role] = actual
        self.source_topic = inside(d["source_topic"],self.namespace)
        require(receipt(self.source_topic/"source-origin.json")["sha256"]
            == self.old_binding["original_source_origin"]["sha256"],
            "Use the same restored actual original formula source topic")
        work = d["head_work"]
        require(isinstance(work,dict) and set(work) == set(WORK_KEYS),
            "Only the eleven explicit original head/query work controls may be supplied")
        for key in WORK_KEYS:
            if key == "budget_seconds":
                valid_positive(work[key],key)
            else:
                require(type(work[key]) is int, "Original integer work parameter required: "+key)
        # Exact original CLI domains remain checked by f12f itself, not a new science gate.
        self.report["requested_head_work"] = copy.deepcopy(work)
        self.report["original_work_parameters"] = copy.deepcopy(self.old_binding["work_parameters"])
        self.report["actual_original_inputs"] = self.original
        query_recipe, query_receipt = read(self.original["queries"]["file"],self.original["queries"])
        self.report["complete_original_requested_query_plan"] = dict(
            actual_file=query_receipt,original_value=query_recipe)
        self.report["new_declared_source_responsibility"] = dict(
            ordered_source_pieces=dict(first=0,stop=1440,order="n159..0/j0..8"),
            all_six_primitive_names=list(SIX),deep_cells="n>=160; all original admissible roots",
            all_original_queries_in_the_unchanged_recipe=True)
        self.report["binding_complete"] = True; self.persist()

    def invoke(self, name, argv, allowance):
        self.check(); row = next(x for x in self.report["phases"] if x["name"] == name)
        remaining = self.phase_end-time.time()-self.reserve
        if remaining <= 0:
            raise Stop("no_startable_allowance_before_"+name)
        allowance = min(float(allowance),remaining)
        require(allowance > 0, "A child allowance must be positive")
        end = min(self.phase_end-self.reserve,time.time()+allowance)
        so, se = self.out/(name+".stdout.log"), self.out/(name+".stderr.log")
        row.update(command=argv,actual_allowance_seconds=allowance,
            child_absolute_stop_unix_seconds=end)
        env = dict(os.environ)
        for key in ("GH_TOKEN","GITHUB_TOKEN","MR_TOKEN","GITHUB_OUTPUT"):
            env.pop(key,None)
        with so.open("xb") as out, se.open("xb") as err:
            process = subprocess.Popen(argv,cwd=self.comp,env=env,shell=False,
                start_new_session=True,stdout=out,stderr=err)
            self.child = self.H.OwnedChild(process); self.active = row
            row.update(started=True,status="running",observed_child=self.child.record())
            self.report["all_owned_children_quiescent"] = False; self.persist()
            try:
                while process.poll() is None:
                    self.child.observe()
                    if self.signals or time.time() >= end:
                        row["stop_reason"] = ("external_interruption" if self.signals
                            else "original_clock_or_declared_child_allowance")
                        break
                    if shutil.disk_usage(self.out).free < self.input["resources"]["free_bytes_reserve"]:
                        row["stop_reason"] = "declared_temporary_storage_reserve_reached"; break
                    try:
                        process.wait(timeout=min(.25,max(.01,end-time.time())))
                    except subprocess.TimeoutExpired:
                        pass
            finally:
                grace = max(.001,min(self.reserve,self.phase_end-time.time()))
                state = self.child.stop(grace,external=bool(self.signals))
                row.update(status="returned",actual_child_exit=process.returncode,
                    observed_child=state,owned_group_quiescent=state["owned_group_quiescent"])
                self.report["all_owned_children_quiescent"] = all(
                    not r["started"] or r.get("owned_group_quiescent") is True
                    for r in self.report["phases"])
                self.child = None; self.active = None; self.persist()
        row["stdout"] = receipt(so); row["stderr"] = receipt(se); self.persist()
        if row.get("owned_group_quiescent") is not True:
            raise Stop("owned_child_quiescence_unresolved_after_"+name)
        return row["actual_child_exit"]

    def compute(self):
        self.bind(); d = self.input; work = copy.deepcopy(d["head_work"])
        self.check()
        available = (self.phase_end-time.time()-self.reserve
            -d["resources"]["cut_readout_budget_seconds"])
        if available <= 0:
            raise Stop("original_remaining_allowance_cannot_start_head_and_reserve_cut_readout")
        work["budget_seconds"] = min(float(work["budget_seconds"]),available)
        self.report["actual_clipped_head_work"] = copy.deepcopy(work)
        new_dir = self.out/"refined-C"; cut_dir = self.out/"refined-cut"
        argv = [sys.executable,"-u",str(self.comp/C_NAME)]
        for role in ("config","ledger_ready","stored_ready"):
            option = "--"+role.replace("_","-")
            argv += [option,self.original[role]["file"],option+"-sha256",self.original[role]["sha256"]]
        argv += ["--runtime-computations",str(self.comp),"--source-topic",str(self.source_topic),
            "--proof",self.original["proof"]["file"],"--queries",self.original["queries"]["file"],
            "--queries-sha256",self.original["queries"]["sha256"],"--out",str(new_dir),
            "--deep-definition","original-exact-root-family"]
        for key in WORK_KEYS:
            argv += ["--"+key.replace("_","-"),str(work[key])]
        self.invoke("head_recompute",argv,work["budget_seconds"])
        self.check()
        if not (new_dir/"result.json").is_file():
            self.report["new_source_unpaid"] = dict(reason="original_f12f_final_result_not_returned",
                all1440_six_primitive_and_query_responsibilities_remain_unpaid=True,
                raw_directory=str(new_dir),baseline_bound_retained=True)
            return 2
        fresh, fid, binding, bid = checked_C(new_dir,None)
        equality = semantic_bindings(self.old_binding,binding)
        self.report.update(actual_refined_C=fid,actual_refined_C_input_binding=bid,
            semantic_input_equivalence=equality,same_semantic_C_proved_by_actual_bindings=True,
            new_complete_C_enclosures=fresh.get("continuous_convention_C_query_enclosures_complete") is True,
            original_new_C_result_scope=copy.deepcopy(fresh))
        self.persist(); self.check()
        args = [sys.executable,"-u",str(self.comp/CUT_NAME),"--directory",str(new_dir),
            "--result-sha256",fid["sha256"],"--config",self.original["config"]["file"],
            "--config-sha256",self.original["config"]["sha256"],
            "--query-recipe",self.original["queries"]["file"],
            "--query-recipe-sha256",self.original["queries"]["sha256"],"--out",str(cut_dir)]
        self.invoke("complete_cut_readout",args,d["resources"]["cut_readout_budget_seconds"])
        self.check()
        if not (cut_dir/"cut-twojet-readout.json").is_file():
            self.report["new_cut_unpaid"] = dict(reason="original_complete_cut_reader_not_returned",
                complete_E_Er_Err_leaf_hull_not_inferred=True,baseline_bound_retained=True)
            return 2
        cut, cid = checked_cut(cut_dir/"cut-twojet-readout.json",None,fid,bid)
        self.report.update(actual_refined_cut=cid,original_new_cut_readout_scope=copy.deepcopy(cut),
            new_complete_cut_enclosures=cut.get("point_twojet_enclosure_complete") is True)
        if not self.report["new_complete_cut_enclosures"]:
            self.report["new_cut_unpaid"] = dict(reason=cut.get("unpaid_reason"),
                original_source_and_query_scope_retained=True,baseline_bound_retained=True)
            return 2
        require(canonical(cut["original_binary_cut"]) == canonical(self.old_cut["original_binary_cut"]),
            "No nominal-cut reidentification or radius renormalisation")
        joined = dict(schema=SCHEMA+"-same-semantic-enclosures",baseline=self.report["baseline"],
            actual_refined_C=fid,actual_refined_cut=cid,semantic_input_equivalence=equality,
            source_scope="every identical admissible original root sequence",
            simultaneous_realization_of_all_independent_box_points_not_claimed=True,
            same_original_binary_cut=cut["original_binary_cut"],
            exact_real_coefficients_are_not_replaced_by_new_midpoints=True,
            complete_original_definition_or_checkpoint_not_modified=True)
        if self.old_cut.get("point_twojet_enclosure_complete") is True:
            joined["cut_twojet_intersections"] = {key:intersect(
                self.old_cut["same_point_E_Er_Err_enclosures"][key],
                cut["same_point_E_Er_Err_enclosures"][key]) for key in FIELDS}
            joined["semantic_cut_leaf_enclosures"] = {
                name:dict(lower=joined["cut_twojet_intersections"][key]["lower_exact"],
                    upper=joined["cut_twojet_intersections"][key]["upper_exact"])
                for name,key in zip(("E0","E1","E2"),FIELDS)}
        else:
            joined["cut_twojet_intersections"] = None
            joined["baseline_cut_not_complete_new_bound_only"] = True
            joined["semantic_cut_leaf_enclosures"] = {name:dict(lower=str(interval(
                cut["same_point_E_Er_Err_enclosures"][key])[0]),upper=str(interval(
                cut["same_point_E_Er_Err_enclosures"][key])[1]))
                for name,key in zip(("E0","E1","E2"),FIELDS)}
        if self.old.get("full_finite_head_complete") is True and fresh.get("full_finite_head_complete") is True:
            joined["natural_outer_radius_intersection"] = intersect(
                self.old["natural_outer_radius"],fresh["natural_outer_radius"])
            require(self.old["primitive_names"] == fresh["primitive_names"] == list(SIX),
                "Every one of the original six primitives is retained")
            for key in ("finite_head_all_six_primitives","full_deep_plus_head_all_six_primitives"):
                require(len(self.old[key]) == len(fresh[key]) == 6, "No primitive slot may disappear")
                joined[key+"_intersections"] = [dict(name=name,enclosure=intersect(a,b))
                    for name,a,b in zip(SIX,self.old[key],fresh[key])]
        self.check()
        jid = write(self.out/"same-C-refined-enclosures.json",joined)
        self.report["intersection"] = dict(actual_file=jid,necessary_original_values=joined)
        self.report["completed_source_and_cut_recomputation"] = True
        return 0 if self.report["new_complete_C_enclosures"] else 2

    def run(self):
        code = 2
        try:
            code = self.compute()
        except Stop as error:
            self.report["resource_stop"] = dict(type=type(error).__name__,message=str(error),
                no_mathematical_failure_inferred=True)
            code = 128+self.signals[0]["number"] if self.signals else 124
        except BaseException as error:
            self.report["error"] = dict(type=type(error).__name__,message=str(error),
                traceback=traceback.format_exc())
            code = 2
        finally:
            if self.child is not None:
                try:
                    state = self.child.stop(min(self.reserve or 10,10),external=True)
                    self.active.update(observed_child=state,owned_group_quiescent=state["owned_group_quiescent"])
                    self.report["all_owned_children_quiescent"] = state["owned_group_quiescent"]
                except BaseException as error:
                    self.report["shutdown_error"] = dict(type=type(error).__name__,message=str(error))
                    self.report["all_owned_children_quiescent"] = False
            for number, previous in self.handlers.items():
                signal.signal(number,previous)
            self.report["actual_exit_code"] = code
            self.report["run_returned"] = True
            for row in self.report["phases"]:
                if not row["started"]:
                    row["unstarted_reason"] = (
                        self.report.get("resource_stop") or self.report.get("error")
                        or self.report.get("new_source_unpaid")
                        or "An earlier original phase did not return the required real input")
            self.persist()
        if self.out is not None:
            print(json.dumps(dict(event="R489_same_C_recompute_return",actual_result=receipt(self.out/"result.json"),
                actual_exit_code=code,original_baseline_not_removed=True),sort_keys=True),flush=True)
        else:
            print(canonical(self.report).decode(),end="",flush=True)
        return code


def stream_identity(path, check=None):
    identity = receipt(path,check); rows = 0; h = hashlib.sha256(); size = 0
    ends_with_lf = True
    with Path(path).open("rb") as stream:
        for line in stream:
            if check is not None:
                check()
            rows += 1; size += len(line); h.update(line)
            ends_with_lf = line.endswith(b"\n")
    require(size == identity["bytes"] and h.hexdigest() == identity["sha256"],
        "A completed source ledger changed during full identity read")
    return dict(identity,rows=rows,final_physical_line_complete=ends_with_lf)


def readback(directory, expected, out):
    actions()
    directory = inside(directory,os.environ["RUNNER_TEMP"])
    value, rid = read(directory/"result.json",expected); current(value)
    require(value.get("schema") == SCHEMA and value.get("source",{}).get("sha256")
        == receipt(__file__)["sha256"], "Use the actual source's complete producer metadata")
    out = inside(out,os.environ["RUNNER_TEMP"],exists=False)
    require(not out.exists() and not directory.is_relative_to(out), "Use a fresh independent readback directory")
    out.mkdir(parents=True)
    comp = Path(value["actual_input"]["file"])
    input_value, _ = read(comp,value["actual_input"])
    H = load_owner(input_value["computations"])
    original_owner = value.get("producer_process")
    now_owner = None if original_owner is None else H.proc_record(original_owner["pid"])
    still_owner = (original_owner is not None
        and H.same_process(original_owner,now_owner) and now_owner["state"] != "Z")
    unknown = original_owner is None or value.get("run_returned") is not True
    live = []; conflicts = []
    for phase in value.get("phases",[]):
        if not phase.get("started"):
            continue
        state = phase.get("observed_child")
        if not isinstance(state,dict):
            unknown = True; continue
        conflicts.extend(state.get("identity_conflicts",[]))
        for old in state.get("observed_processes",[]):
            now = H.proc_record(old["pid"])
            if H.same_process(old,now) and now["state"] != "Z":
                live.append(now)
        live.extend(row for row in H.group_rows(state["pid"]) if row["state"] != "Z")
    quiet = not(still_owner or unknown or live or conflicts)
    summary = dict(schema=NECESSARY_SCHEMA,source=receipt(__file__),repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        original_result=rid,quiescent=quiet,owner_still_live=still_owner,
        unknown_owner_scope=unknown,actual_matching_live_processes=live,identity_conflicts=conflicts,
        complete_necessary_readback=False,original_result_metadata=copy.deepcopy(value),
        source_member_readback=[],error_logs=[],read_errors=[],
        full_success_primitive_and_inverse_arrays_transported=False,
        baseline_and_new_raw_not_deleted=True,downstream_field_acceptance_not_inferred=True)
    end = value.get("original_readback_deadline_unix_seconds")
    def check_readback():
        if type(end) not in (int,float) or not math.isfinite(end):
            raise Stop("The actual original readback deadline is unavailable")
        if time.time() >= end:
            raise Stop("The unchanged original readback deadline was reached")
    if quiet:
        fresh = value.get("original_new_C_result_scope")
        if not isinstance(fresh,dict) and (directory/"refined-C"/"result.json").is_file():
            try:
                check_readback()
                recovered, recovered_id, _, recovered_binding = checked_C(directory/"refined-C",None)
                fresh = recovered
                summary["actual_uncommitted_original_child_result"] = dict(
                    actual_file=recovered_id,input_binding=recovered_binding,original_value=recovered,
                    original_producer_flags_are_read_not_new_helper_completion=True,
                    no_cut_intersection_or_semantic_comparison_executed_by_readback=True)
            except BaseException as error:
                summary["read_errors"].append(dict(type=type(error).__name__,message=str(error)))
        if isinstance(fresh,dict):
            newdir = directory/"refined-C"
            try:
                for name, desc in fresh.get("ledgers",{}).items():
                    check_readback()
                    actual = stream_identity(local_member(newdir,desc),check_readback)
                    require(same(actual,desc) and actual["rows"] == desc["rows"],
                        "The complete original ledger receipt differs: "+name)
                    summary["source_member_readback"].append(dict(name=name,actual=actual,
                        full_identity_and_line_count_read=True,all_scientific_rows_independently_recomputed=False))
                qv, qid = read(local_member(newdir,fresh["query_results"]),fresh["query_results"])
                summary["actual_original_query_results"] = dict(actual_file=qid,value=qv)
            except BaseException as error:
                summary["read_errors"].append(dict(type=type(error).__name__,message=str(error)))
        else:
            # An external stop may precede f12f's final result. Read all real
            # existing raw identities; do not infer a paid mathematical prefix.
            for name in ("six-primitive-panels.jsonl", "complete-source-radial-panels.jsonl",
                         "query-closed-inverse-cover.jsonl", "unpaid-complete-scope.jsonl"):
                path = directory/"refined-C"/"large-arrays"/name
                try:
                    check_readback()
                    actual = stream_identity(path,check_readback) if path.is_file() else None
                    summary["source_member_readback"].append(dict(name=name,actual=actual,
                        original_final_result_absent=True,
                        mathematical_paid_prefix_not_inferred_from_partial_rows=True,
                        all_new_source_and_query_responsibilities_remain_unpaid=True))
                except BaseException as error:
                    summary["read_errors"].append(dict(type=type(error).__name__,message=str(error)))
        for phase in value.get("phases",[]):
            for kind in ("stdout","stderr"):
                path = directory/(phase["name"]+"."+kind+".log")
                if not path.is_file():
                    if phase.get("started"):
                        summary["read_errors"].append(dict(role=phase["name"],kind=kind,
                            message="A started child log is absent"))
                    continue
                try:
                    check_readback()
                    actual = receipt(path,check_readback)
                    require(kind not in phase or same(actual,phase[kind]), "A child log differs from its receipt")
                    row = dict(role=phase["name"],kind=kind,actual_file=actual)
                    if kind == "stderr":
                        raw = path.read_bytes()
                        row.update(complete_original_text=raw.decode("utf-8",errors="surrogateescape"),
                            original_all_bytes_represented_by_utf8_surrogateescape=True)
                    else:
                        row["scope"] = "Complete stdout identity; original result/error and query metadata returned separately"
                    summary["error_logs"].append(row)
                except BaseException as error:
                    summary["read_errors"].append(dict(type=type(error).__name__,message=str(error)))
    summary["complete_necessary_readback"] = quiet and not summary["read_errors"]
    raw = canonical(summary)
    write(out/"full-necessary-attempt.json",summary)
    if len(raw) > LIMIT:
        fallback = dict(schema=NECESSARY_SCHEMA+"-over-budget",repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            original_result=rid,attempted_summary=dict(bytes=len(raw),sha256=digest(raw)),
            complete_necessary_readback=False,quiescent=quiet,no_part_transport=True,
            all_original_raw_retained=True)
        write(out/"summary.json",fallback)
        print(canonical(fallback).decode(),end="",flush=True)
        return 70
    sid = write(out/"summary.json",summary)
    print("BEGIN_R489_SAME_C_FULL_HEAD_REFINEMENT_NECESSARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_R489_SAME_C_FULL_HEAD_REFINEMENT_NECESSARY",flush=True)
    if summary["complete_necessary_readback"]:
        write(out/"readback-complete.json",dict(schema=NECESSARY_SCHEMA+"-complete-marker",
            repository=REPO,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            complete=True,quiescent=True,necessary_summary={k:sid[k] for k in ("bytes","sha256")},
            scientific_recomputation_completion=value.get("completed_source_and_cut_recomputation") is True))
    return 0 if summary["complete_necessary_readback"] else 2


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command",required=True)
    run = sub.add_parser("run")
    run.add_argument("--input",type=Path,required=True); run.add_argument("--input-sha256",required=True)
    back = sub.add_parser("readback")
    back.add_argument("--directory",type=Path,required=True)
    back.add_argument("--result-sha256",required=True); back.add_argument("--out",type=Path,required=True)
    args = parser.parse_args(argv); actions()
    if args.command == "run":
        return Recompute(args.input,args.input_sha256).run()
    return readback(args.directory,args.result_sha256,args.out)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(json.dumps(dict(event="R489_original_source_interface_exception",
            type=type(error).__name__,message=str(error)),ensure_ascii=True),flush=True)
        traceback.print_exc()
        raise SystemExit(2)
