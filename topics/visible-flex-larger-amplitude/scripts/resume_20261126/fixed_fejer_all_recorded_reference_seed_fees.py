#!/usr/bin/env python3
"""Full recorded-batch fixed-seed fee schedule for the actual deterministic Fejer reference.

Every completed provider batch in one immutable actual report belongs to
the schedule, including batches first requested by arbitrary geometry
points. No angle subset or successful-field status is invented. This
natural-budget coordinator keeps whole source-bound radial journals and
fresh conditional fee outputs. It does not recompute F/J/normal roots,
provide actual node words, or certify the current field.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

SCHEMA = 'complete-fixed-fejer-all-recorded-reference-seed-fee-schedule-v1'
TOPIC = "topics/visible-flex-larger-amplitude"
PINS = {"reader": ["read_fixed_fejer_immutable_point_so3_report.py", "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b"],
 "producer": ["fixed_fejer_reference_accurate_mean_residuals.py", "ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0"],
 "consumer": ["fixed_fejer_reference_seed_angular_profile_error_bounds.py", "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"]}
DRIVER_SHA = '477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd'
REPORT_SCHEMA = 'complete-fixed-fejer-immutable-point-material-envelope-SO3-QP-v1'
DERIVED_FROM_COMPLETE_MATERIAL_ENVELOPE_SCHEDULER_SHA256 = '3feff893d09257748d153f0423e75d64eafe75777933ba85ee67611ce61cad6d'
DERIVED_FROM_COMPLETE_RUN09_SCHEDULER_SHA256 = '0c7efa0726aa27dbde769a8cce7615efc75e1676b49cf3c2602767b8543d915f'
DERIVED_FROM_COMPLETE_RUN10_SCHEDULER_SHA256 = '42624b7f7fb4be694ff1253baf456b8526269a0f20099a40af737b5ffc096cb5'
INPUTS = ("reference_bundle", "carrier", "node_report", "scalar_input", "preparation_report")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Actual report scheduling and all scientific children require public Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def file_record(path):
    p = Path(path).resolve()
    return dict(path=str(p), sha256=sha(p), bytes=p.stat().st_size)


def captured(path):
    value = Path(path).read_bytes()
    return json.loads(value), hashlib.sha256(value).hexdigest()


def write_json(path, value):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    temporary = p.with_name(p.name+".partial")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+"\n")
    temporary.replace(p)


def event(**value):
    print(json.dumps(value, separators=(",", ":"), allow_nan=False), flush=True)


def load_reader(path):
    if sha(path) != PINS["reader"][1]:
        raise ValueError("Bind the complete unchanged material-envelope pure reader")
    name = "_material_envelope_complete_batch_schedule_reader"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(module.read_report.__code__.co_filename) != PINS["reader"][1]:
        raise ValueError("Use the real complete reader body")
    return module


def source_paths(repo):
    directory = repo/TOPIC/"scripts/resume_20261126"
    result = {role: directory/name for role, (name, _) in PINS.items()}
    for role, path in result.items():
        if sha(path) != PINS[role][1]:
            raise ValueError("The complete schedule source changed: "+role)
    return result



def actual_reference_attribution(paths, raw, pure):
    """Use the same complete pure attribution as every batch fee consumer."""
    path = paths["consumer"]
    if sha(path) != PINS["consumer"][1]:
        raise ValueError("The complete actual reference fee consumer changed")
    name = "_fixed_fejer_reference_fee_attribution_"+PINS["consumer"][1]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for function in (module.bind_outer_report_scope, module.bind_fixed_fejer_reference_attribution):
        if sha(function.__code__.co_filename) != PINS["consumer"][1]:
            raise ValueError("Use the real complete reference attribution bodies")
    outer = module.bind_outer_report_scope(raw, pure)
    return outer, outer["actual_fixed_fejer_reference_attribution"]


def bind_actual(args, paths):
    reader = load_reader(paths["reader"])
    raw, digest = captured(args.report)
    pure = reader.read_report(args.repo, args.report, verify_final_bundle=False)
    if pure["report_sha256"] != digest or sha(args.report) != digest:
        raise ValueError("Keep one immutable actual report snapshot")
    if (raw.get("schema") != REPORT_SCHEMA or raw.get("source_sha256") != DRIVER_SHA
            or pure.get("actual_driver_sha256") != DRIVER_SHA):
        raise ValueError("A different complete solver is not this recorded-batch input")
    outer, reference_attribution = actual_reference_attribution(paths, raw, pure)
    inputs = {key: Path(getattr(args, key)).resolve() for key in INPUTS}
    expected = dict(reference_bundle=raw["bundle_sha256"],
        carrier=raw["observation_carrier_sha256"],
        node_report=raw["exact_tail_node_report_sha256"],
        scalar_input=raw["exact_tail_scalar_input_sha256"],
        preparation_report=raw["independent_preparation_report"]["sha256"])
    records = {}
    for key, path in inputs.items():
        records[key] = file_record(path)
        if records[key]["sha256"] != expected[key]:
            raise ValueError("This complete same-seed scientific input changed: "+key)
    diagnostics = pure.get("seed_diagnostics")
    batches = [] if diagnostics is None else diagnostics.get("mean_batch_records")
    if not isinstance(batches, list):
        raise ValueError("Keep the actual completed provider batch records or their actual absence")
    latest = raw.get("latest_operator_metadata")
    if diagnostics is not None:
        actual = latest["base_complete_metadata"]["fixed_supported_unit_seed"]["mean_batch_records"]
        if actual != batches:
            raise ValueError("The pure reader and captured actual seed batch list disagree")
    schedule = []
    full_angles = []
    for index, batch in enumerate(batches):
        angles = batch.get("literal_angle_hex")
        if (not isinstance(angles, list) or not angles
                or any(not isinstance(v, str) or not math.isfinite(float.fromhex(v))
                    or float.fromhex(v).hex() != v for v in angles)
                or batch.get("seed_model_identity_sha256") != raw["supported_unit_seed_identity_sha256"]
                or batch.get("metadata", {}).get("complete") is not True
                or batch.get("fixed_original_core_H_used") is not True
                or batch.get("current_outer_free_point_not_used") is not True):
            raise ValueError("The entire actual completed seed batch and angle order are mandatory")
        record = batch.get("runner_raw_arrays")
        if not isinstance(record, dict):
            raise ValueError("A completed batch without its actual working arrays cannot be paid")
        arrays = Path(record["path"]).resolve()
        if (arrays == args.repo or args.repo in arrays.parents
                or not arrays.is_file() or sha(arrays) != record["sha256"]
                or arrays.stat().st_size != record["bytes"]):
            raise ValueError("Actual complete working batch bytes are absent or changed")
        schedule.append(dict(batch_index=index, actual_complete_batch_metadata=batch,
            actual_raw_batch=file_record(arrays), literal_angle_count=len(angles),
            ordered_literal_angle_words_sha256=canonical(angles)))
        full_angles.extend(angles)
    # This is an exact declared property of the bound provider _means: only
    # previously missing literal angles are recorded, in their actual order.
    if len(full_angles) != len(set(full_angles)):
        raise ValueError("The bound provider records each new literal angle once; preserve this full record contract")
    if diagnostics is not None:
        count = diagnostics.get("completed_literal_angle_count")
        if type(count) is not int or count != len(full_angles):
            raise ValueError("Actual completed seed angle count differs from the complete recorded set")
    policy = dict(batch_selection="every recorded completed provider batch, in original record order",
        no_angle_subset=True, no_batch_subsampling=True,
        full_positive_radial_domain_and_exact_tail_in_each_producer=True,
        precision_bits=args.precision_bits, panels=args.panels,
        width_goal=str(Fraction(args.width_goal)), taylor_order=args.taylor_order,
        profile_series_order=args.profile_series_order,
        natural_batch_quantum_seconds=args.per_batch_seconds,
        request_nodes="none: actual complete node addresses, four working provider jets and accurate node input enclosures remain unpaid",
        same_report_required_on_resume=True,
        invalid_or_missing_batch_is_not_replaced_by_another_batch=True)
    binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
        complete_source_sha256_by_role={k: v[1] for k, v in PINS.items()},
        actual_report=file_record(args.report),
        actual_driver_sha256=DRIVER_SHA, actual_model_identity_sha256=raw["model_identity_sha256"],
        fixed_scalar_metric_identity_sha256=raw["fixed_scalar_metric"]["identity_sha256"],
        supported_unit_seed_identity_sha256=raw["supported_unit_seed_identity_sha256"],
        complete_seed_model=raw["supported_unit_seed_definition"],
        material_envelope_policy_identity_sha256=pure["material_envelope_binding"]["definition_identity_sha256"],
        complete_input_records=records,
        complete_outer_source_attribution=outer,
        actual_fixed_fejer_reference_attribution=reference_attribution,
        actual_all_batch_metadata_sha256=canonical(batches),
        actual_recorded_completed_batches=len(schedule),
        actual_recorded_literal_angles=len(full_angles),
        complete_ordered_literal_angle_words_sha256=canonical(full_angles),
        actual_solver_complete=raw.get("complete") is True,
        actual_seed_diagnostics_present=diagnostics is not None,
        actual_seed_last_failure=None if diagnostics is None else diagnostics["last_recorded_seed_failure"],
        actual_seed_last_failure_phase=None if diagnostics is None else diagnostics["last_seed_failure_phase"],
        actual_seed_last_failure_reason=None if diagnostics is None else diagnostics["last_seed_failure_reason"],
        policy=policy, schedule=schedule)
    all_input_records = [binding["actual_report"], *records.values()]
    all_input_records += [row["actual_raw_batch"] for row in schedule]
    all_input_records += reference_attribution["complete_snapshot_input_records"]
    for record in all_input_records:
        path = Path(record["path"]).resolve()
        if path == args.outdir or args.outdir in path.parents:
            raise ValueError("The complete new output namespace must be disjoint from every actual input")
    recheck(binding)
    return binding, inputs


def recheck(binding):
    records = [binding["actual_report"], *binding["complete_input_records"].values()]
    records += [row["actual_raw_batch"] for row in binding["schedule"]]
    records += binding["actual_fixed_fejer_reference_attribution"]["complete_snapshot_input_records"]
    for record in records:
        if (Path(record["path"]).stat().st_size != record["bytes"]
                or sha(record["path"]) != record["sha256"]):
            raise ValueError("A complete source-bound actual input changed while fees were being processed")


def producer_args(args, paths, inputs, index, out, seconds):
    command = [sys.executable, "-u", str(paths["producer"]),
        "--repo", str(args.repo), "--report", str(args.report),
        "--batch-index", str(index), "--outdir", str(out),
        "--panels", str(args.panels), "--precision-bits", str(args.precision_bits),
        "--width-goal", str(Fraction(args.width_goal)), "--seconds", repr(float(seconds))]
    for key in INPUTS:
        command += ["--"+key.replace("_", "-"), str(inputs[key])]
    return command


def consumer_args(args, paths, index, request, output):
    return [sys.executable, "-u", str(paths["consumer"]),
        "--repo", str(args.repo), "--report", str(args.report),
        "--batch-index", str(index), "--fees", str(request), "--output", str(output),
        "--precision-bits", str(args.precision_bits), "--taylor-order", str(args.taylor_order),
        "--profile-series-order", str(args.profile_series_order)]


def run_child(command, prefix):
    stdout, stderr = prefix.with_suffix(".stdout.log"), prefix.with_suffix(".stderr.log")
    if stdout.exists() or stderr.exists():
        raise FileExistsError("Never overwrite an actual child log")
    started = time.monotonic()
    record = dict(command=command, command_sha256=canonical(command),
        started_time_UTC=time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        returncode=None, seconds=None, launch_error=None)
    try:
        with stdout.open("wb") as out, stderr.open("wb") as err:
            child = subprocess.run(command, stdout=out, stderr=err, check=False)
        record["returncode"] = int(child.returncode)
    except OSError as error:
        record["launch_error"] = repr(error)
    record["seconds"] = time.monotonic()-started
    record["stdout"] = file_record(stdout) if stdout.exists() else None
    record["stderr"] = file_record(stderr) if stderr.exists() else None
    return record


def validate_producer(value, binding, index):
    actual = value["binding"]["actual_batch"]
    if (value.get("source_sha256") != PINS["producer"][1]
            or actual["report_sha256"] != binding["actual_report"]["sha256"]
            or actual["actual_completed_batch_index"] != index
            or actual["actual_raw_batch_sha256"] != binding["schedule"][index]["actual_raw_batch"]["sha256"]
            or actual["literal_angle_hex"] != binding["schedule"][index]["actual_complete_batch_metadata"]["literal_angle_hex"]
            or actual["supported_unit_seed_identity_sha256"] != binding["supported_unit_seed_identity_sha256"]
            or actual["complete_outer_attribution"] != binding["complete_outer_source_attribution"]
            or value.get("current_F_J_or_endpoint_roots_recomputed") is not False
            or value.get("profile_moments_computed_here") is not False
            or value.get("raw_reference_calibration_and_current_normal_fees_paid") is not False
            or value.get("complete_R715_physical_lift_and_sixjet_fees_paid") is not False):
        raise ValueError("A complete mean output changed its own source, whole batch or fee scope")
    return value


def validate_consumer(value, binding, index, request_sha):
    actual = value["binding"]
    if (value.get("source_sha256") != PINS["consumer"][1]
            or actual["report_sha256"] != binding["actual_report"]["sha256"]
            or actual["actual_completed_batch_index"] != index
            or actual["actual_raw_batch_sha256"] != binding["schedule"][index]["actual_raw_batch"]["sha256"]
            or actual["complete_outer_attribution"] != binding["complete_outer_source_attribution"]
            or value.get("fee_request_sha256") != request_sha
            or value.get("all_requested_actual_batch_angles_retained") is not True
            or value.get("requested_angles") != binding["schedule"][index]["literal_angle_count"]
            or value.get("fixed_seed_reference_fees_only") is not True
            or value.get("numerical_raw_reference_calibration_paid") is not False
            or value.get("complete_outer_normal_root_and_implicit_error_paid") is not False
            or value.get("complete_R715_physical_lift_and_sixjet_error_paid") is not False):
        raise ValueError("A conditional fee output is not this complete actual batch and request")
    if value.get("complete") is True:
        expected = binding["schedule"][index]["actual_complete_batch_metadata"]["literal_angle_hex"]
        if ([r["literal_phi_hex"] for r in value["results"]] != expected
                or value.get("actual_completed_angles") != len(expected)
                or any(r.get("complete") is not True or r.get("requested_nodes") != []
                    for r in value["results"])):
            raise ValueError("This full schedule pays all recorded mean angles and no unsupplied node words")
    return value


def initialize_state(binding):
    return dict(schema=SCHEMA, source_sha256=sha(__file__),
        binding=binding, binding_identity_sha256=canonical(binding),
        next_batch=0, invocations=0, child_invocations=0,
        complete=False, all_width_goals_reached=False,
        all_recorded_batch_mean_and_profile_fees_complete=False,
        continuous_phi_cover_paid=False, actual_node_jet_fees_paid=False,
        raw_calibration_and_current_normal_chain_paid=False,
        complete_physical_sixjet_metric_geometry_paid=False,
        missing_node_working_values_are_not_assumed_zero=True,
        current_F_J_normal_roots_recomputed=False,
        batches=[dict(batch_index=row["batch_index"], producer=None, consumers=[],
            complete=False, width_goal_reached=False, failures=[])
            for row in binding["schedule"]], children=[])


def refresh(state):
    entries = state["batches"]
    state["completed_mean_covers"] = sum(v["producer"] is not None and
        v["producer"].get("complete") is True for v in entries)
    state["completed_mean_and_profile_batches"] = sum(v["complete"] is True for v in entries)
    state["width_goals_reached"] = sum(v["width_goal_reached"] is True for v in entries)
    state["all_recorded_batch_mean_and_profile_fees_complete"] = bool(entries) and all(v["complete"] for v in entries)
    state["complete"] = state["all_recorded_batch_mean_and_profile_fees_complete"]
    state["all_width_goals_reached"] = bool(entries) and all(v["width_goal_reached"] for v in entries)
    state["scope"] = ("Complete only for all recorded actual mean batches and their profile moments; "
        "all unrecorded/failed batches, actual nodes, continuous angles and current field fees remain explicit")
    state["actual_node_working_input_status"] = "not supplied; no actual node fee claimed"
    return state


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--report", type=Path, required=True)
    for key in INPUTS:
        p.add_argument("--"+key.replace("_", "-"), type=Path, required=True)
    p.add_argument("--outdir", type=Path, required=True)
    p.add_argument("--execution-mode", choices=("prepare-only", "complete-recorded-batches"),
        default="complete-recorded-batches")
    p.add_argument("--seconds", type=float, default=600.)
    p.add_argument("--per-batch-seconds", type=float, default=60.)
    p.add_argument("--panels", type=int, default=128)
    p.add_argument("--precision-bits", type=int, default=160)
    p.add_argument("--width-goal", default="1/100000000")
    p.add_argument("--taylor-order", type=int, default=48)
    p.add_argument("--profile-series-order", type=int, default=48)
    a = p.parse_args()
    if (any(not math.isfinite(v) or v <= 0 for v in (a.seconds, a.per_batch_seconds))
            or a.panels < 1 or not 64 <= a.precision_bits <= 1024
            or Fraction(a.width_goal) <= 0 or a.taylor_order < 1 or a.profile_series_order < 1):
        p.error("Use complete positive arithmetic and natural-budget parameters")
    a.repo, a.report, a.outdir = a.repo.resolve(), a.report.resolve(), a.outdir.resolve()
    if a.outdir == a.repo or a.repo in a.outdir.parents:
        p.error("Scientific raw and full journals remain outside the repository")
    if (a.outdir == a.report or a.report in a.outdir.parents
            or a.outdir/"report.json" == a.report):
        p.error("The new output cannot replace the actual source report")
    return a


def main():
    args = parse_args()
    require_actions()
    paths = source_paths(args.repo)
    binding, inputs = bind_actual(args, paths)
    args.outdir.mkdir(parents=True, exist_ok=True)
    report_path = args.outdir/"report.json"
    identity = canonical(binding)
    if report_path.exists():
        state, old_digest = captured(report_path)
        if (state.get("schema") != SCHEMA or state.get("source_sha256") != sha(__file__)
                or state.get("binding") != binding or state.get("binding_identity_sha256") != identity):
            raise ValueError("Resume only the same actual full report, all batches, source and fee parameters")
    else:
        state = initialize_state(binding)
    for index, row in enumerate(state["batches"]):
        if row.get("batch_index") != index:
            raise ValueError("Resume every full batch in its original exact order")
        if row["producer"] is not None:
            value, digest = captured(row["producer"]["report"]["path"])
            if digest != row["producer"]["report"]["sha256"]:
                raise ValueError("A recorded producer output changed outside this coordinator")
            validate_producer(value, binding, index)
        for saved in row["consumers"]:
            value, digest = captured(saved["report"]["path"])
            if digest != saved["report"]["sha256"]:
                raise ValueError("A prior complete/partial conditional fee output changed")
            validate_consumer(value, binding, index, saved["fee_request_sha256"])
    state["invocations"] += 1
    state["last_execution_mode"] = args.execution_mode
    state["last_requested_total_seconds"] = args.seconds
    state["actual_complete_original_report"]=binding["actual_report"]
    state["full_source_parameters"] = dict(
        producer_template=[str(paths["producer"]), "all batch indices", "whole original angles"],
        consumer_template=[str(paths["consumer"]), "same batch index and complete request"],
        all_five_input_paths={k: str(v) for k, v in inputs.items()},
        source_pins=PINS, policy=binding["policy"])
    write_json(report_path, refresh(state))
    if args.execution_mode == "prepare-only":
        event(event="all_actual_seed_fee_batches_prepared", actual_batches=len(state["batches"]),
            actual_angles=binding["actual_recorded_literal_angles"], scientific_children_executed=False,
            complete=False, report=file_record(report_path))
        return
    start = time.monotonic()
    attempted_here = set()
    blocked_here = set()
    while state["batches"] and time.monotonic()-start < args.seconds:
        if state["complete"] and state["all_width_goals_reached"]:
            break
        count = len(state["batches"])
        index = state["next_batch"] % count
        state["next_batch"] = (index+1) % count
        row = state["batches"][index]
        if index in blocked_here or (row["complete"] and row["width_goal_reached"]):
            attempted_here.add(index)
            if len(attempted_here) == count:
                break
            continue
        remaining = args.seconds-(time.monotonic()-start)
        if remaining <= 0:
            break
        directory = args.outdir/("batch-"+str(index).zfill(6))
        directory.mkdir(exist_ok=True)
        serial = state["child_invocations"]
        state["child_invocations"] += 1
        producer_dir = directory/"mean"
        command = producer_args(args, paths, inputs, index, producer_dir,
            min(args.per_batch_seconds, remaining))
        event(event="complete_actual_mean_batch_started", batch_index=index,
            all_recorded_batches=count, literal_angles=binding["schedule"][index]["literal_angle_count"],
            whole_angle_list_sha256=binding["schedule"][index]["ordered_literal_angle_words_sha256"])
        record = run_child(command, directory/("producer-"+str(serial).zfill(6)))
        state["children"].append(dict(batch_index=index, role="producer", **record))
        result_path = producer_dir/"report.json"
        if result_path.exists():
            value, digest = captured(result_path)
            validate_producer(value, binding, index)
            row["producer"] = dict(report=file_record(result_path),
                complete=value.get("complete") is True,
                tolerance_reached=value.get("tolerance_reached") is True,
                actual_completed_initial_pieces=value.get("completed_initial_pieces"),
                actual_required_initial_pieces=value.get("required_initial_pieces"),
                actual_complete_leaves=value.get("active_complete_leaves"),
                journal=value.get("journal"), fee_request=value.get("fee_request"),
                maximum_total_equation_component_L1_width=value.get("maximum_total_equation_component_L1_width"))
            row["width_goal_reached"] = value.get("tolerance_reached") is True
        if record["returncode"] != 0:
            row["failures"].append(dict(role="producer", child_serial=serial,
                returncode=record["returncode"], launch_error=record["launch_error"]))
            blocked_here.add(index)
        elif row["producer"] is None:
            raise ValueError("The completed producer child has no actual report")
        request = None if row["producer"] is None else row["producer"].get("fee_request")
        if record["returncode"] == 0 and row["producer"]["complete"] and request is not None:
            request_path = Path(request["path"])
            if sha(request_path) != request["sha256"]:
                raise ValueError("The complete actual mean request changed before conditional consumption")
            previous = next((v for v in row["consumers"]
                if v["fee_request_sha256"] == request["sha256"]), None)
            if previous is None:
                serial = state["child_invocations"]
                state["child_invocations"] += 1
                output = directory/("conditional-fees-"+str(serial).zfill(6)+".json")
                command = consumer_args(args, paths, index, request_path, output)
                child = run_child(command, directory/("consumer-"+str(serial).zfill(6)))
                state["children"].append(dict(batch_index=index, role="consumer", **child))
                if output.exists():
                    checked, digest = captured(output)
                    validate_consumer(checked, binding, index, request["sha256"])
                    saved = dict(report=file_record(output), fee_request_sha256=request["sha256"],
                        complete=checked.get("complete") is True,
                        actual_completed_angles=checked.get("actual_completed_angles"),
                        requested_angles=checked.get("requested_angles"),
                        actual_requested_node_count=0)
                    row["consumers"].append(saved)
                    row["complete"] = saved["complete"]
                if child["returncode"] != 0:
                    row["failures"].append(dict(role="consumer", child_serial=serial,
                        returncode=child["returncode"], launch_error=child["launch_error"]))
                    if row["width_goal_reached"]:
                        blocked_here.add(index)
            else:
                row["complete"] = previous["complete"]
                if not previous["complete"] and row["width_goal_reached"]:
                    blocked_here.add(index)
        row["complete"] = any(saved["complete"] for saved in row["consumers"])
        recheck(binding)
        attempted_here.add(index)
        state["last_invocation_elapsed_seconds"] = time.monotonic()-start
        write_json(report_path, refresh(state))
        if len(attempted_here) == count:
            attempted_here.clear()
    recheck(binding)
    state["last_invocation_elapsed_seconds"] = time.monotonic()-start
    state["natural_budget_return_is_not_a_field_completion"] = True
    state["blocked_batches_this_invocation"] = sorted(blocked_here)
    state["no_recorded_completed_batches"] = not state["batches"]
    write_json(report_path, refresh(state))
    event(event="all_recorded_actual_seed_fee_schedule_returned",
        actual_batches=len(state["batches"]), actual_angles=binding["actual_recorded_literal_angles"],
        complete_mean_covers=state["completed_mean_covers"],
        complete_mean_and_profile_batches=state["completed_mean_and_profile_batches"],
        all_width_goals_reached=state["all_width_goals_reached"], complete=state["complete"],
        actual_node_jet_fees_paid=False, complete_field_error_paid=False,
        report=file_record(report_path))


if __name__ == "__main__":
    main()

