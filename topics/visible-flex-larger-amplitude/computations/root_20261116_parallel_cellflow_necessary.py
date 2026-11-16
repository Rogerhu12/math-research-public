#!/usr/bin/env python3
"""R531 necessary metadata for complete parallel576 cellflows.

Callable from the original bounded reader after the real owner is quiet.
No scientific module, V8 payload, RHS, root, J, norm, FD or audit is evaluated.
This function adds one fixed semantic section to that reader's one90000-byte
summary; it does not print a second frame, create a success marker or delete.
The caller retains original exit70 and unknown-owner/raw-retention behavior.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

SCHEMA = "R531-complete576-parallel-cellflow-necessary-v1"
POOL_SCHEMA = "R531-complete576-current-cellflow-worker-pool-v1"
ADDRESS_COLUMNS = ("stage", "rawCell", "rawSegment", "engine_index", "worker_index")
STATUSES = ("unvisited", "assigned_not_started", "started_without_completed_return",
            "completed", "stage_error", "interrupted_without_completed_return")


def signature(value):
    # Used only for the expressly named semantic catalogues below. JSON
    # keeps bool/int/float, -0.0 and absent keys distinct in these records.
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
                      separators=(",", ":"), allow_nan=False)


class Catalogue:
    def __init__(self):
        self.values = []
        self.seen = {}

    def add(self, value):
        key = signature(value)
        if key not in self.seen:
            self.seen[key] = len(self.values)
            self.values.append(value)
        return self.seen[key]


def table(rows):
    """Fixed semantic column groups; keep every value, key set and row address."""
    key_sets = {}
    groups = []
    for index, row in enumerate(rows):
        key = tuple(row)
        if key not in key_sets:
            key_sets[key] = len(groups)
            groups.append(dict(columns=list(key), original_row_indices=[], records=[]))
        group = groups[key_sets[key]]
        group["original_row_indices"].append(index)
        group["records"].append(row)
    packed = []
    for group in groups:
        data = []
        for key in group["columns"]:
            values = [row[key] for row in group["records"]]
            first = signature(values[0])
            if all(signature(value) == first for value in values):
                data.append(dict(constant=values[0]))
            else:
                data.append(dict(original_values=values))
        packed.append(dict(columns=group["columns"],
            original_row_indices=group["original_row_indices"], column_data=data))
    return dict(original_row_count=len(rows), groups=packed,
                absent_key_is_not_null=True,
                constants_shared_only_after_complete_value_and_type_equality=True)

def complete_counter_catalogue(values):
    """Separate only the three declared complete algorithm-statistics records.

    Each original dictionary is reconstructed by its row index from main,
    then by adding the components at their explicit original row indices.
    Missing and present-null components are distinct. Every original key,
    counter, histogram, reason, flag and last_observation is retained.
    """
    roles = ("zero_nonlinear_flux", "factor_contraction", "linear_input_support")
    main = []
    components = {key: dict(original_row_indices=[], records=[],
                            non_dictionary_original_values=[]) for key in roles}
    non_dictionary = []
    for index, value in enumerate(values):
        if not isinstance(value, dict):
            main.append({})
            non_dictionary.append(dict(original_row_index=index, original_value=value))
            continue
        main.append({key: item for key, item in value.items() if key not in roles})
        for key in roles:
            if key not in value:
                continue
            component = components[key]
            if isinstance(value[key], dict):
                component["original_row_indices"].append(index)
                component["records"].append(value[key])
            else:
                component["non_dictionary_original_values"].append(
                    dict(original_row_index=index, original_value=value[key]))
    for component in components.values():
        component["complete_dictionary_values"] = table(component.pop("records"))
    return dict(original_row_count=len(values), main_complete_values=table(main),
                actual_components=components, non_dictionary_original_values=non_dictionary,
                all_original_values_retained=True, absent_is_not_null=True)


def selected(value, keys):
    return {key: value[key] for key in keys if key in value}


def stored_identity(r, relative):
    file = r.path(relative)
    if not file.is_file():
        return dict(file=relative, exists=False)
    value = r.record(file)
    return dict(exists=True, **value, complete_bytes_read_for_identity=True)


def event_prefix(r, relative):
    """Read the entire actual event stream; select only fixed semantic roles."""
    file = r.path(relative)
    result = dict(file=relative, exists=file.is_file(), rows=0, bytes=0,
                  complete_stream_read=False, worker_events=[], evaluations={},
                  last_worker_positions={}, read_errors=[])
    if not file.is_file():
        return result
    h = hashlib.sha256()
    with file.open("rb") as stream:
        for line, raw in enumerate(stream, 1):
            h.update(raw)
            result["bytes"] += len(raw)
            result["rows"] += 1
            try:
                event = json.loads(raw)
            except Exception as error:
                row = dict(file=relative, line=line, error=repr(error),
                           bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
                result["read_errors"].append(row)
                r.errors.append(row)
                continue
            kind = event.get("event")
            seq = event.get("evaluation_sequence")
            if kind == "position":
                result["last_worker_positions"][str(event["worker_index"])] = dict(
                    line=line, **event)
                continue
            if kind in ("assigned", "started", "completed", "stage_error"):
                ev = result["evaluations"].setdefault(str(seq), {})
                ev[str(event["stage"])] = dict(line=line, **event)
                continue
            # Every original readiness, exit, uncaught error, control error
            # and shutdown event is retained, not reduced to worker counts.
            result["worker_events"].append(dict(line=line, **event))
    if file.stat().st_size != result["bytes"]:
        raise ValueError("R531 event stream changed after owned quiet")
    result["sha256"] = h.hexdigest()
    result["complete_stream_read"] = not result["read_errors"]
    r.files[relative] = dict(bytes=result["bytes"], sha256=result["sha256"],
                            records=result["rows"])
    return result


def collect_parallel_cellflows(r, relative, *, owned_quiet):
    """Return the selected complete pool metadata; source caller supplies Reader.

    Reader.path/json/jsonl/record/log/files/errors are the original224 metadata
    API. owned_quiet must be the actual original owner's returned bool, never
    a newly inferred scientific decision. No accepting condition is created.
    """
    if owned_quiet is not True:
        raise RuntimeError("Mutable R531 output is not read before actual owned quiet")
    base = r.path(relative)
    if not base.is_dir():
        return dict(schema=SCHEMA, started=False, actual_directory=relative,
                    no_parallel_execution_inferred=True)
    addresses, contexts, sources, statuses = Catalogue(), Catalogue(), Catalogue(), Catalogue()
    engine_metadata, counters, observations = Catalogue(), Catalogue(), Catalogue()
    preparations = Catalogue()
    json_name = lambda name: relative + "/" + name
    records = {name: r.json(json_name(name)) for name in
               ("launch.json", "spawn.json", "pool-owner.json", "pool-ready.json",
                "progress.json", "pool-closed.json", "parent-close.json")}
    launch = records["launch.json"]
    if isinstance(launch, dict) and launch.get("schema") != POOL_SCHEMA:
        raise ValueError("R531 actual pool launch schema differs")
    for name in ("coordinator.stdout.log", "coordinator.stderr.log"):
        r.log(json_name(name))
    events = event_prefix(r, json_name("events.jsonl"))

    def status_view(value):
        if not isinstance(value, dict):
            return value
        view = {k: v for k, v in value.items() if k not in
                ("context", "stage_address_columns", "stage_addresses",
                 "actual_stage_status_indices")}
        if "context" in value:
            view["context_ref"] = contexts.add(value["context"])
        if "stage_addresses" in value:
            view["stage_address_ref"] = addresses.add(dict(
                columns=value.get("stage_address_columns", list(ADDRESS_COLUMNS)),
                rows=value["stage_addresses"]))
        if "actual_stage_status_indices" in value:
            view["status_groups_ref"] = statuses.add(value["actual_stage_status_indices"])
        return view

    evaluations = []
    for directory in sorted(base.glob("evaluation-*")):
        if not directory.is_dir() or not re.fullmatch(r"evaluation-[0-9]+", directory.name):
            continue
        rel = directory.relative_to(r.root).as_posix()
        start = r.json(rel + "/evaluation-start.json")
        input_id = r.json(rel + "/input-identity.json")
        returned = r.json(rel + "/result.json")
        consumed = r.json(rel + "/parent-consumed.json")
        failure = r.json(rel + "/parent-failure.json")
        prep = r.jsonl(rel + "/preparation-events.jsonl")
        row = dict(directory=rel)
        for key, value in (("actual_start", start), ("input_identity_record", input_id)):
            if isinstance(value, dict):
                selected_value = {k: v for k, v in value.items() if k not in
                                  ("engines", "stage_addresses", "stage_address_columns",
                                   "context", "preparation")}
                if "context" in value:
                    selected_value["context_ref"] = contexts.add(value["context"])
                if "stage_addresses" in value:
                    selected_value["stage_address_ref"] = addresses.add(dict(
                        columns=value.get("stage_address_columns", list(ADDRESS_COLUMNS)),
                        rows=value["stage_addresses"]))
                if "engines" in value:
                    selected_value["engine_sources_ref"] = sources.add(value["engines"])
                if "preparation" in value:
                    selected_value["actual_preparation"] = value["preparation"]
                row[key] = selected_value
            else:
                row[key] = value
        # Each record below is an actual original preparation event. Neither
        # a prepared profile nor a worker assignment is a completed cell.
        address_map = (start or input_id or {}).get("stage_addresses") or []
        lookup = {signature(address): i for i, address in enumerate(address_map)}
        prep_rows = []
        for event in prep:
            value = dict(event)
            if all(key in value for key in ADDRESS_COLUMNS):
                address = [value[key] for key in ADDRESS_COLUMNS]
                key = signature(address)
                if key in lookup:
                    for column in ADDRESS_COLUMNS:
                        del value[column]
                    value["actual_stage_address_index"] = lookup[key]
            # The sequence is already present in this evaluation record;
            # remove it only after exact actual equality, never by an offset.
            if "evaluation_sequence" in value and signature(value["evaluation_sequence"]) == signature(
                    (start or input_id or {}).get("evaluation_sequence")):
                del value["evaluation_sequence"]
                value["same_actual_evaluation_sequence"] = True
            prep_rows.append(value)
        row["complete_profile_preparation_trace_ref"] = preparations.add(table(prep_rows))
        if isinstance(returned, dict):
            view = {k: v for k, v in returned.items() if k not in
                    ("context", "actual_status", "completed")}
            if "context" in returned:
                view["context_ref"] = contexts.add(returned["context"])
            if "actual_status" in returned:
                view["actual_status"] = status_view(returned["actual_status"])
            if "completed" in returned:
                raw = signature(returned["completed"]).encode("ascii")
                view["successful_stage_payload_identity_table"] = dict(
                    rows=len(returned["completed"]), canonical_parsed_JSON_bytes=len(raw),
                    canonical_parsed_JSON_sha256=hashlib.sha256(raw).hexdigest(),
                    all_successful_stage_addresses_in_actual_status=True,
                    full_state_tangent_payloads_not_reopened_by_necessary_reader=True,
                    complete_identity_table_in_original_result_json=True)
            row["original_return"] = view
        else:
            row["original_return"] = returned
        row["actual_parent_consumption"] = consumed
        row["actual_parent_failure"] = failure
        # Only event prefixes actually on disk are represented. They do not
        # retrospectively fill missing last-stage engine counters.
        seq = (start or input_id or {}).get("evaluation_sequence")
        actual_events = events["evaluations"].get(str(seq), {})
        if not isinstance(returned, dict):
            actual_rows = []
            for key in sorted(actual_events, key=int):
                event = actual_events[key]
                if event.get("event") == "stage_error":
                    actual_rows.append(event)
                else:
                    actual_rows.append(selected(event, ("line", "event", "evaluation_sequence",
                        "stage", "worker_index", "thread_id")))
            row["last_actual_stage_events"] = table(actual_rows)
            row["successful_payload_identifiers_and_event_timestamps_remain_in_original_journal"] = True
        else:
            row["all_observed_stage_events_covered_by_original_result_status"] = True
            row["full_success_event_timestamps_and_payload_paths_in_original_journal_only"] = True
        if not isinstance(returned, dict) and isinstance(start, dict) and isinstance(start.get("stage_addresses"), list):
            stage_map = start["stage_addresses"]
            row["event_prefix_unassigned_stage_indices"] = [
                i for i, address in enumerate(stage_map)
                if str(address[0]) not in actual_events]
            row["unassigned_is_only_no_observed_assigned_event_not_a_runtime_guess"] = True
        evaluations.append(row)

    terminal = records["pool-closed.json"]
    progress = records["progress.json"]
    chosen = terminal if isinstance(terminal, dict) else progress
    workers = []
    if isinstance(chosen, dict):
        for value in chosen.get("workers", []):
            row = {k: v for k, v in value.items() if k not in ("statistics", "sources")}
            if "sources" in value:
                row["source_receipts_ref"] = sources.add(value["sources"])
            stats = []
            for engine in value.get("statistics", []):
                item = {}
                metadata = {k: v for k, v in engine.items() if k not in
                            ("counters", "actual_split_RHS_statistics", "snapshot_position")}
                item["engine_metadata_ref"] = engine_metadata.add(metadata)
                if "counters" in engine:
                    # All R466/R471/R523 counters, scopes, fallback reasons,
                    # every last_observation and incomplete failure survive.
                    item["complete_counters_ref"] = counters.add(engine["counters"])
                if "actual_split_RHS_statistics" in engine:
                    item["actual_split_RHS_statistics"] = engine["actual_split_RHS_statistics"]
                if "snapshot_position" in engine:
                    item["actual_statistics_position_ref"] = observations.add(engine["snapshot_position"])
                stats.append(item)
            row["engines"] = stats
            workers.append(row)
    for directory in sorted(base.glob("worker-*")):
        if directory.is_dir():
            for name in ("stdout.log", "stderr.log"):
                r.log(directory.relative_to(r.root).as_posix() + "/" + name)
    launch_view = None
    if isinstance(launch, dict):
        launch_view = {k: v for k, v in launch.items() if k != "source_files"}
        if "source_files" in launch:
            raw = signature(launch["source_files"]).encode("ascii")
            launch_view["complete_runtime_source_paths"] = dict(
                count=len(launch["source_files"]), canonical_parsed_JSON_bytes=len(raw),
                canonical_parsed_JSON_sha256=hashlib.sha256(raw).hexdigest(),
                full_paths_in_actual_launch_identity=True,
                necessary_reader_does_not_reimport_these_sources=True)
    result = dict(schema=SCHEMA, started=True, actual_directory=relative,
        actual_launch=launch_view,
        actual_spawn=records["spawn.json"], actual_coordinator_owner=records["pool-owner.json"],
        actual_ready=records["pool-ready.json"], actual_parent_close=records["parent-close.json"],
        statistics_source="pool-closed.json" if isinstance(terminal, dict) else
                          "progress.json" if isinstance(progress, dict) else None,
        actual_workers=table(workers), actual_evaluations=table(evaluations),
        current_unreturned_evaluation=status_view((progress or {}).get("current_evaluation")),
        actual_terminal_fields=None if not isinstance(terminal, dict) else
            {k: v for k, v in terminal.items() if k not in ("workers", "evaluations")},
        complete_event_stream_identity=selected(events, ("file", "exists", "rows", "bytes",
            "sha256", "complete_stream_read", "read_errors")),
        all_worker_lifecycle_events=table(events["worker_events"]),
        last_actual_worker_positions=events["last_worker_positions"],
        exact_semantic_catalogues=dict(stage_addresses=addresses.values, contexts=contexts.values,
            source_records=sources.values, status_groups=statuses.values,
            engine_metadata=engine_metadata.values, complete_engine_counters=complete_counter_catalogue(counters.values),
            actual_statistics_positions=observations.values,
            complete_preparation_traces=preparations.values),
        scope=dict(
            actual_main_engine_counters_remain_in_original_R273_section=True,
            every_observed_worker_engine_cumulative_counter_and_last_observation_retained=True,
            missing_inflight_counters_not_inferred_from_profile_events=True,
            source_or_transport_errors_not_reclassified_as_original_mathematical_failure=True,
            successful_numeric_state_J_and_full_RK_tapes_are_temporary_identity_only=True,
            complete_stage_address_maps_and_all_observed_stage_statuses_retained=True,
            no_actual_nonlinear_iteration_inferred_from_evaluation_sequence=True,
            original_single90000_exit70_and_raw_retention_required=True,
            no_summary_capacity_or_speed_or_acceptance_guarantee=True,
            no_new_scientific_gate_or_scientific_computation=True))
    return result


def add_parallel_cellflows(r, original_summary, *, owned_quiet,
                          relative="science/full-DN/true-tail-input-support-contracted-trace-r273/parallel-cellflows"):
    """Add this actual section before the unchanged original one-frame cap."""
    if not isinstance(original_summary, dict):
        raise TypeError("A genuine original necessary summary dictionary is required")
    if "parallel_cellflows" in original_summary:
        raise ValueError("R531 metadata is attached exactly once")
    original_summary["parallel_cellflows"] = collect_parallel_cellflows(
        r, relative, owned_quiet=owned_quiet)
    return original_summary
