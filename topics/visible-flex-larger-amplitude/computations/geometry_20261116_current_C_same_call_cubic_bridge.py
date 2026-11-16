#!/usr/bin/env python3
"""R570 actual same-call cubic capture and same-evaluation comparison bridge.

Only explicit new callers install this observer around their real unchanged
full-DN solve. The original solve object, native/FD/final acceptance and metric
DFS decisions are unchanged. Original owner clocks and raw retention remain.
Source author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R570-actual-same-call-cubic-capture-and-comparison-v1"
LIBRARY = "geometry_20261116_same_call_cubic_quintic_defect.py"
LIBRARY_SHA = "6d27df22093e339fe8940bf24c57cff880d247a5f7f4fd478135adf2e4032f66"
PINS = {
    LIBRARY: LIBRARY_SHA,
    "geometry_20261116_actual_prefix_coefficient_tube_majorants.py":
        "81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b",
    "geometry_20261116_finite_frenet_tube_residual_majorants.py":
        "4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad",
}
STATUS_NAME = "same-call-cubic-status.json"
CAPTURE_NAME = "same-call-cubic"
ORDINARY = (ArithmeticError, ValueError, TypeError, KeyError, IndexError,
            AttributeError, OSError)
DEADLINES = {"request193-owned-job-science-deadline-v1",
             "request203-owned-job-science-deadline-v1",
             "request205-owned-job-science-deadline-v1"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Scientific evaluation belongs only to the named public Actions")


def current_run():
    return {key: os.environ.get(key) for key in
            ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def value_identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def identity(path):
    path = Path(path).resolve(strict=True)
    h, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
            size += len(block)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def same(left, right):
    return isinstance(left, dict) and isinstance(right, dict) and (
        left.get("bytes"), left.get("sha256")) == (right.get("bytes"), right.get("sha256"))


def error_record(error):
    return dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc())


def read(path, expected=None):
    got = identity(path)
    require(expected is None or (got["sha256"] == expected if isinstance(expected, str)
            else same(got, expected)), "The complete current file bytes/SHA differ")
    return json.loads(Path(path).read_bytes()), got


def fresh_json(path, value):
    path = Path(path)
    with path.open("xb") as stream:
        stream.write(canonical(value))
        stream.flush()
    return identity(path)


def actual_temporary(path, *, exists=False):
    p = Path(path).resolve(strict=exists)
    root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(p != root and p.is_relative_to(root), "Keep actual diagnostic data inside this job's RUNNER_TEMP")
    return p


def library():
    for name, digest in PINS.items():
        require(identity(HERE/name)["sha256"] == digest,
                "An original defining diagnostic source differs: "+name)
    name = "_r570_original_cubic_"+LIBRARY_SHA
    module = sys.modules.get(name)
    if module is None:
        spec = importlib.util.spec_from_file_location(name, HERE/LIBRARY)
        require(spec is not None and spec.loader is not None, "The original R569 loader is unavailable")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        try:
            spec.loader.exec_module(module)
        except BaseException:
            sys.modules.pop(name, None)
            raise
    require(Path(module.__file__).resolve() == (HERE/LIBRARY).resolve()
            and module.SCHEMA == "R569-same-call-literal-cubic-and-accurate-quintic-v1",
            "The actual R569 module owner differs")
    return module


def register_runtime(runtime, source):
    """Register complete new sources in the real checkpoint runtime closure."""
    records = dict(PINS)
    records[Path(__file__).name] = identity(__file__)["sha256"]
    for name, digest in records.items():
        require(identity(HERE/name)["sha256"] == digest,
                "The complete source closure changed: "+name)
        require(name not in runtime.closure or runtime.closure[name] == digest,
                "The actual existing source closure conflicts: "+name)
        runtime.closure[name] = digest
    require(Path(source).resolve().parent == HERE,
            "The actual driver and all runtime sources share their original computations directory")
    return records


class OriginalDeadlineStop(RuntimeError):
    """The same original absolute job science deadline, not a mathematical gate."""


class SolveCapture:
    def __init__(self, runtime, args, problem, phase_dir, phase, driver_source, phase_row):
        actions()
        self.runtime, self.phase_row = runtime, phase_row
        self.phase_dir = actual_temporary(phase_dir, exists=True)
        self.phase = phase
        self.capture = None
        self.active = False
        self.finished = False
        self.deadline = None
        self.report = dict(schema=SCHEMA+"-phase-capture", run=current_run(),
            source=identity(__file__), actual_driver_source=identity(driver_source),
            actual_phase=phase, actual_phase_directory=str(self.phase_dir),
            complete_necessary_status=True, instrumentation_installed=False,
            original_solve_started=False, original_solve_returned=False,
            original_fullDN_status_not_replaced=True,
            original_solver_object_returned_without_mutation=True,
            no_second_solve_or_RHS_evaluation=True,
            original_BVP_or_native_or_FD_acceptance_changed=False,
            source_capture_available=False, capture_result=None,
            original_job_deadline=None, setup_error=None,
            actual_capture_error=None, original_exception=None,
            necessary_arrays_are_complete_member_identities_not_raw_values=True)
        try:
            clock, cid = read(args.job_deadline, args.job_deadline_sha256)
            require(clock.get("schema") in DEADLINES
                    and clock.get("repository") == REPOSITORY
                    and str(clock.get("run_id")) == os.environ["GITHUB_RUN_ID"]
                    and clock.get("source_commit") == os.environ["GITHUB_SHA"],
                    "Use the same original live owner deadline document")
            born, seconds = clock["namespace_created_unix_seconds"], clock["science_seconds_from_namespace"]
            require(type(born) in (int, float) and math.isfinite(born)
                    and seconds == 18900 and clock["readback_reserve_seconds"] == 2700,
                    "Preserve the original absolute whole-job science and readback scopes")
            self.deadline = born+seconds
            self.report["original_job_deadline"] = cid
            self.report["absolute_original_science_deadline_unix_seconds"] = self.deadline
            self.check()
            module = library()
            self.capture = module.SameCallCubicCapture(runtime.core,
                actual_driver_source=driver_source, field_modes=int(problem.flow.M),
                physical_size=int(problem.flow.n), augmented_size=int(problem.flow.dimension),
                budget_check=self.check, actual_clock_receipt=cid)
        except ORDINARY as error:
            self.report["setup_error"] = error_record(error)
            self.report["diagnostic_unpaid_reason"] = "actual_same_call_capture_setup_unavailable"
        self.publish_row()

    def check(self):
        if self.deadline is not None and time.time() >= self.deadline:
            raise OriginalDeadlineStop("original_absolute_job_science_deadline_reached")

    def publish_row(self):
        self.phase_row["actual_same_call_literal_cubic"] = copy.deepcopy(self.report)

    def __enter__(self):
        self.check()
        if self.capture is not None:
            try:
                self.capture.__enter__()
                self.active = True
                self.report["instrumentation_installed"] = True
            except ORDINARY as error:
                self.report["setup_error"] = error_record(error)
                self.report["diagnostic_unpaid_reason"] = "actual_original_solver_recorder_not_installed"
                self.capture = None
        self.report["original_solve_started"] = True
        self.publish_row()
        return self

    def __exit__(self, kind, value, trace):
        if self.active:
            self.capture.__exit__(kind, value, trace)
            self.active = False
        self.report["original_solve_returned"] = kind is None
        if self.capture is not None:
            self.report["actual_solve_call_count"] = self.capture.call_count
            self.report["actual_capture_error"] = copy.deepcopy(self.capture.last_error)
        if kind is not None:
            self.report["original_exception"] = dict(type=kind.__name__, message=str(value))
            self.report["diagnostic_unpaid_reason"] = "original_fullDN_call_did_not_return"
            self.persist()
        self.publish_row()
        return False

    def persist(self):
        if self.finished:
            return
        path = self.phase_dir/STATUS_NAME
        try:
            rec = fresh_json(path, self.report)
            self.report["actual_status_file"] = rec
        except ORDINARY as error:
            self.report["status_write_error"] = error_record(error)
            self.report["complete_necessary_status"] = False
        self.finished = True
        self.publish_row()

    def finish(self, *, original_result, original_status, original_accepted):
        """Called after the original full-DN gates, before the unchanged CP writer."""
        self.report["original_fullDN_exit_status"] = original_status
        self.report["actual_original_main_acceptance"] = original_accepted is True
        if original_status == 0 and original_accepted is True and self.capture is not None:
            try:
                self.check()
                result, rec = self.capture.write_for_accepted_result(
                    original_result=original_result, out=self.phase_dir/CAPTURE_NAME)
                self.report["capture_result"] = rec
                self.report["source_capture_available"] = result.get("complete") is True
                self.report["actual_capture_error"] = result.get("error") or result.get("capture_error")
                self.report["complete_capture_member_count"] = len(result.get("members", {}))
                if result.get("complete") is not True:
                    self.report["diagnostic_unpaid_reason"] = result.get("unpaid")
            except ORDINARY as error:
                self.report["actual_capture_error"] = error_record(error)
                self.report["diagnostic_unpaid_reason"] = "accepted_same_call_capture_freeze_unavailable"
        else:
            self.report["diagnostic_unpaid_reason"] = self.report.get(
                "diagnostic_unpaid_reason", "original_fullDN_not_accepted_or_same_call_capture_unavailable")
        self.persist()
        return copy.deepcopy(self.report)


def phase_capture_necessary(phase):
    """Metadata only: bind all original capsule members; never re-evaluate arrays."""
    phase = Path(phase).resolve()
    status_path, directory = phase/STATUS_NAME, phase/CAPTURE_NAME
    out = dict(schema=SCHEMA+"-phase-necessary", phase_directory=str(phase),
        complete_necessary_scope=True, status_present=status_path.is_file(),
        capture_directory_present=directory.is_dir(), original_status=None,
        capture_result=None, complete_capture_members=[], capture_available=False,
        scientific_values_or_arrays_not_recomputed=True, unregistered_files=[])
    if not phase.exists():
        out["not_started"] = "actual_original_phase_directory_absent"
        return out
    actual_temporary(phase, exists=True)
    if status_path.is_file():
        status, sid = read(status_path)
        require(status.get("schema") == SCHEMA+"-phase-capture" and status.get("run") == current_run(),
                "The full capture status is not this actual job and source")
        require(same(status.get("source"), identity(__file__)),
                "The actual capture status bridge source differs")
        out["original_status"] = dict(identity=sid, value=status)
    else:
        out["not_returned"] = "actual_capture_status_absent"
        status = None
    result_path = directory/"result.json"
    if result_path.is_file():
        value, rid = read(result_path)
        require(value.get("schema") == "R569-same-call-literal-cubic-and-accurate-quintic-v1-capture"
                and value.get("run") == current_run()
                and same(value.get("source"), identity(HERE/LIBRARY)),
                "The complete actual capture result source or run differs")
        if status is not None and status.get("capture_result") is not None:
            require(same(rid, status["capture_result"]), "The actual status points to another capture")
        members = value.get("members")
        require(isinstance(members, dict), "The full captured member table is absent")
        names = {"result.json"}
        for name, descriptor in members.items():
            basename = descriptor.get("file")
            require(isinstance(basename, str) and Path(basename).name == basename
                    and basename not in names, "Do not merge or redirect captured array members")
            path = directory/basename
            require(path.is_file() and not path.is_symlink(), "A retained captured member is absent")
            actual = identity(path)
            require(same(actual, descriptor), "A complete captured member identity differs")
            names.add(basename)
            out["complete_capture_members"].append(dict(member=name,
                original_descriptor=copy.deepcopy(descriptor), actual_identity=actual))
        out["capture_result"] = dict(identity=rid, original_complete_metadata=value)
        out["capture_available"] = value.get("complete") is True
        if value.get("complete") is True:
            require(set(members) == {"mesh", "augmented_states", "original_spline_rhs",
                    "ppoly_coefficients", "original_rms_residuals", "solver_parameters",
                    "physical_states", "frozen_physical_rhs", "recomputed_augmented_rhs"},
                    "Every complete original cubic member, both means and all augmented rows must remain")
        for path in sorted(directory.rglob("*")):
            if path.is_file() and str(path.relative_to(directory)) not in names:
                out["unregistered_files"].append(identity(path))
    elif directory.exists():
        out["not_returned"] = "capture_directory_exists_but_actual_result_not_returned"
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                out["unregistered_files"].append(identity(path))
    if status is not None and status.get("capture_result") is not None:
        require(out["capture_result"] is not None,
                "The recorded actual capture result did not remain available for necessary readback")
    return out


class BoundComparison:
    """Observe the same original prefix target return and DFS retirement."""
    def __init__(self, current, *, angular_count, sqrt_bits, budget_check,
                 original_job_deadline):
        actions()
        self.current, self.budget_check = current, budget_check
        self.actual = None
        self.attempts = self.prefix_terminals = self.paid_polynomials = 0
        self.paid_geometry = self.paid_pair_tubes = 0
        self.unpaid = []
        self.maxima = {}
        self.binding = dict(schema=SCHEMA+"-comparison-binding", source=identity(__file__),
            original_R569_source=identity(HERE/LIBRARY), available=False,
            actual_checkpoint=copy.deepcopy(current.field.saved.checkpoint.receipt),
            actual_job_deadline=copy.deepcopy(original_job_deadline), error=None,
            original_metric_decisions_changed=False)
        try:
            self.budget_check()
            cp = current.field.saved.checkpoint
            checkpoint_path = Path(cp.receipt["file"]).resolve(strict=True)
            phase = checkpoint_path.parent.parent
            capture_path = phase/CAPTURE_NAME/"result.json"
            status, sid = read(phase/STATUS_NAME)
            require(status.get("schema") == SCHEMA+"-phase-capture"
                    and status.get("run") == current_run()
                    and status.get("source_capture_available") is True
                    and same(status.get("source"), identity(__file__))
                    and same(status.get("original_job_deadline"), original_job_deadline),
                    "The same accepted phase's complete capture and original clock are unavailable")
            captured, cid = read(capture_path, status["capture_result"])
            require(same(captured["source_scope"]["actual_clock"], original_job_deadline),
                    "The capture and current measurement use different original deadline documents")
            module = library()
            self.actual = module.bind_loaded_cubic_quintic(current,
                capture_result=capture_path, capture_sha256=cid["sha256"],
                angular_count=angular_count, sqrt_bits=sqrt_bits, budget_check=budget_check)
            self.binding.update(available=True, actual_capture_status=sid,
                actual_capture=cid, actual_full_binding=self.actual.describe())
        except ORDINARY as error:
            self.binding["error"] = error_record(error)
            self.binding["unpaid"] = "same_actual_accepted_call_cubic_binding_unpaid"

    def inspect(self, cell, target_context):
        self.budget_check()
        self.attempts += 1
        if self.actual is None:
            return dict(schema=SCHEMA+"-comparison-cell", original_cell=copy.deepcopy(cell),
                polynomial_comparison_available=False, geometric_gap_available=False,
                whole_pair_tube_available=False, error=copy.deepcopy(self.binding["error"]),
                unpaid=["same_actual_accepted_call_cubic_binding_unpaid"],
                original_metric_decision_changed=False)
        return self.actual.cell(cell, target_context)

    def commit_original_retirement(self, cell, result, *, split):
        if self.current.field.pieces[cell["piece_index"]]["kind"] != "prefix":
            return dict(applies=False, original_cell_is_not_prefix=True)
        if split:
            return dict(applies=True, paid=False, original_cell_split=True,
                        complete_child_frontier_owned_by_original_metric_DFS=True)
        self.prefix_terminals += 1
        status = dict(applies=True, original_cell_split=False,
            polynomial_comparison_available=isinstance(result, dict)
                and result.get("polynomial_comparison_available") is True,
            geometric_gap_available=isinstance(result, dict)
                and result.get("geometric_gap_available") is True,
            whole_pair_tube_available=isinstance(result, dict)
                and result.get("whole_pair_tube_available") is True)
        self.paid_polynomials += int(status["polynomial_comparison_available"])
        self.paid_geometry += int(status["geometric_gap_available"])
        self.paid_pair_tubes += int(status["whole_pair_tube_available"])
        if not all(status[key] for key in ("polynomial_comparison_available",
                "geometric_gap_available", "whole_pair_tube_available")):
            joint = result.get("whole_pair_joint_box", {}) if isinstance(result, dict) else {}
            self.unpaid.append(dict(original_cell=copy.deepcopy(cell), status=copy.deepcopy(status),
                complete_original_diagnostic_identity=value_identity(result),
                original_error=None if not isinstance(result, dict) else copy.deepcopy(result.get("error")),
                original_unpaid=None if not isinstance(result, dict) else copy.deepcopy(result.get("unpaid")),
                original_scalar_box=None if not isinstance(result, dict) else copy.deepcopy(result.get("scalar_box")),
                complete_joint_d_squared=copy.deepcopy(joint.get("d_squared")),
                complete_joint_W=copy.deepcopy(joint.get("W")),
                complete_joint_P=copy.deepcopy(joint.get("P")),
                full_polynomial_rows_and_complete_tube_are_retained_in_actual_cell_ledger=True))
        if isinstance(result, dict):
            poly = result.get("polynomial_comparison", {})
            geometry = result.get("geometric_derivative_gap", {})
            for name, value in (("E0_upper", poly.get("E0_upper")),
                                ("E1_upper", poly.get("E1_upper")),
                                ("E2_upper", poly.get("E2_upper")),
                                ("relative_derivative_operator_upper",
                                 geometry.get("relative_derivative_operator_upper"))):
                if value is not None:
                    exact = Fraction(value)
                    self.maxima[name] = max(self.maxima.get(name, Fraction(0)), exact)
        return status

    def summary(self, *, original_coverage, complete_cell_ledger,
                original_error, original_stop, close_errors):
        full = (original_coverage.get("completed_all_DFS_work") is True
                and self.prefix_terminals > 0 and self.binding["available"] is True
                and original_error is None and original_stop is None and not close_errors
                and complete_cell_ledger is not None)
        poly_complete = full and self.paid_polynomials == self.prefix_terminals
        geometry_complete = full and self.paid_geometry == self.prefix_terminals
        tube_complete = full and self.paid_pair_tubes == self.prefix_terminals
        return dict(schema=SCHEMA+"-comparison-summary", source=identity(__file__),
            binding=copy.deepcopy(self.binding), actual_prefix_cell_evaluations=self.attempts,
            original_terminal_prefix_cells=self.prefix_terminals,
            complete_polynomial_terminal_cells=self.paid_polynomials,
            complete_geometric_gap_terminal_cells=self.paid_geometry,
            complete_joint_positive_tube_terminal_cells=self.paid_pair_tubes,
            retired_partial_maxima={key:str(value) for key,value in self.maxima.items()},
            complete_actual_prefix_polynomial_comparison=poly_complete,
            complete_actual_prefix_derivative_gap=geometry_complete,
            complete_actual_cubic_quintic_joint_positive_tube=tube_complete,
            global_prefix_polynomial_upper=({key:str(self.maxima[key])
                for key in ("E0_upper","E1_upper","E2_upper")} if poly_complete else None),
            global_prefix_relative_derivative_gap_upper=(str(self.maxima["relative_derivative_operator_upper"])
                if geometry_complete else None),
            these_are_prefix_defects_not_a_global_closed_surface_metric_error=True,
            complete_prefix_coverage_not_inferred_from_terminal_counts_alone=True,
            original_complete_coverage=copy.deepcopy(original_coverage),
            complete_diagnostic_cell_ledger=copy.deepcopy(complete_cell_ledger),
            all_unpaid_original_terminal_cells=copy.deepcopy(self.unpaid),
            original_error=copy.deepcopy(original_error), original_stop=copy.deepcopy(original_stop),
            close_errors=copy.deepcopy(close_errors),
            actual_cubic_metric_error_still_unpaid=True,
            FFT_table_scalar_RHS_formation_difference_still_unpaid=True,
            original_BVP_metric_DFS_native_FD_fullDN_final_or_audit_gate_changed=False,
            all_original_frontier_and_unvisited_roots_remain_the_callers_responsibility=True)
