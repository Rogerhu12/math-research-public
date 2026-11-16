#!/usr/bin/env python3
"""R479 fixed-role composition of already selected complete39 necessary scalars.

No scientific file, field array, RHS, Jacobian or FD history is evaluated here.
The input is the original R454 assembled necessary document. Only explicit
diagnostic addresses, exact same-candidate records and fixed source metadata
can be shared. Distinct original values remain inline. No arbitrary JSON-tree
dictionary, numerical-value dictionary, byte codec or split transport exists.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

SCHEMA = "R479-complete39-fixed-semantic-context-composition-v1"
RESULT_SCHEMA = "request213-one-necessary-whole-chain-contexts-v1"

# Prefixes are original record addresses, never generated payload identifiers.
CONTEXT_PREFIXES = {
    "original_RMS_checks": (
        "batch_record", "evaluation_role", "original_trial_index"),
    "original_RMS_failure_samples": (
        "batch_record", "evaluation_role", "original_trial_index",
        "original_RMS_check_index"),
    "original_midpoint_failure_points": (
        "batch_record", "evaluation_role", "original_trial_index"),
    "all_original_failed_selected_queries": (
        "batch_record", "original_trial_index"),
    "FD_all_original_failed_contractions": (
        "batch_record", "original_group", "original_direction_index",
        "original_direction"),
    "status_standalone_model_field_relation": ("batch_record",),
    "FD_original_groups": ("batch_record",),
}

# Only these fixed source/role/policy metadata fields may become table headers.
# Errors, gate values, extrema, coefficients and FD errors are not in this list.
SHARED_METADATA = {
    "original_status": ("schema", "latest_warm_file"),
    "model_scalar_results": ("model_damping",),
    "FD_original_report": (
        "schema", "accepted_sha256", "tail_anchor_sha256",
        "tail_config_sha256", "source_sha256",
        "all_original_contracts_false_records_returned_without_recomputing_gate"),
    "FD_original_groups": (
        "individual_level_numeric_histories_not_exported",
        "original_direction_record_count"),
    "QP_local_QP_report": (
        "schema", "original_full_coordinate_count", "local_coordinate_count",
        "original_inequality_row_count", "maximum_working_rows",
        "maximum_dual_sweeps", "no_constraints_or_control_columns_removed"),
    "QP_last_saved_local_stage": (
        "schema", "original_full_coordinate_count", "local_coordinate_count",
        "original_inequality_row_count", "maximum_working_rows",
        "maximum_dual_sweeps", "no_constraints_or_control_columns_removed"),
    "original_midpoint_failure_points": ("classification",),
}

CANDIDATE_ROLES = (
    "physical_argmax", "physical_argmax_component", "physical_argmax_frozen_weight",
    "original_midpoint_failure_points",
)

# These are physical addresses selected by the original reporters. The values
# beta, a, ap, app, curvature, residual, frozen weight and error never enter it.
INTERVAL_FIELDS = {
    "original_RMS_failure_samples": {
        "left": "left_station", "right": "right_station"},
    "original_midpoint_failure_points": {
        "left": "left_station", "right": "right_station",
        "station": "existing_midpoint_station"},
    "physical_argmax": {
        "left_station": "left_station", "right_station": "right_station",
        "existing_midpoint_station": "existing_midpoint_station"},
}


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode("ascii")


def same(left, right):
    """Exact canonical equality, preserving scalar kind and signed zero."""
    return canonical(left) == canonical(right)


def table_parts(table):
    """Recognize only the explicit R454 scalar-table format; otherwise leave it."""
    if not isinstance(table, dict):
        return None
    addresses = table.get("address_columns")
    values = table.get("value_columns")
    rows = table.get("rows")
    if not (isinstance(addresses, list) and isinstance(values, list)
            and isinstance(rows, list)
            and all(isinstance(x, str) for x in addresses + values)
            and len(set(addresses + values)) == len(addresses + values)):
        return None
    width = len(addresses) + len(values)
    if not all(isinstance(row, list) and len(row) == width for row in rows):
        return None
    return addresses, values, rows


def column_map(parts):
    addresses, values, _ = parts
    return {name: index for index, name in enumerate(addresses + values)}


def try_smaller(report, operation, operations):
    """Choose between two faithful necessary-metadata representations only."""
    before = len(canonical(report))
    candidate = copy.deepcopy(report)
    detail = operation(candidate)
    if detail is None:
        operations.append(dict(operation=operation.__name__,
            applied=False, reason="no eligible fixed-semantic repetition"))
        return report
    after = len(canonical(candidate))
    if after >= before:
        operations.append(dict(operation=operation.__name__, applied=False,
            reason="faithful alternative does not reduce representation bytes",
            original_bytes=before, alternative_bytes=after))
        return report
    operations.append(dict(operation=operation.__name__, applied=True,
        original_bytes=before, alternative_bytes=after, **detail))
    return candidate


def share_candidate_components(report):
    """Same actual trial only; do not compare different alpha or model calls."""
    tables = report.get("necessary_scalar_tables")
    if not isinstance(tables, dict):
        return None
    references = {}
    shared_rows = 0
    for role in CANDIDATE_ROLES:
        table = tables.get(role)
        parts = table_parts(table)
        if parts is None:
            continue
        address_names, _, rows = parts
        prefix = ["batch_record", "evaluation_role", "original_trial_index"]
        if address_names[:3] != prefix:
            continue
        contexts = {}
        for row_index, row in enumerate(rows):
            key = canonical(row[:3])
            contexts.setdefault(key, []).append((row_index, row))
        remove = set()
        for group in contexts.values():
            row = group[0][1]
            if row[1] != "complete_RMS":
                continue
            key = canonical([row[0], "candidate", row[2]])
            parent = contexts.get(key)
            if parent is None:
                continue
            # All remaining original row indices and necessary values must
            # match, including null/nonfinite-token values and their order.
            if not same([item[1][3:] for item in group],
                        [item[1][3:] for item in parent]):
                continue
            address = canonical([row[0], row[2]])
            entry = references.setdefault(address, dict(
                batch_record=row[0], original_trial_index=row[2],
                evaluation_role="complete_RMS",
                identical_selected_component_from_evaluation_role="candidate",
                component_roles=[], original_table_row_positions={}))
            entry["component_roles"].append(role)
            entry["original_table_row_positions"][role] = [item[0] for item in group]
            remove.update(item[0] for item in group)
        if remove:
            table["rows"] = [row for i, row in enumerate(rows) if i not in remove]
            shared_rows += len(remove)
    if not references:
        return None
    report["complete_RMS_same_trial_candidate_component_references"] = list(references.values())
    return dict(exactly_shared_original_rows=shared_rows,
        actual_trial_contexts=len(references),
        equality="complete selected role rows, canonical exact, same batch and trial")


def share_interval_addresses(report):
    """Share observed interval coordinates only when every occurrence agrees."""
    tables = report.get("necessary_scalar_tables")
    if not isinstance(tables, dict):
        return None
    observations = {}
    recognized = {}
    for role, fields in INTERVAL_FIELDS.items():
        parts = table_parts(tables.get(role))
        if parts is None:
            continue
        positions = column_map(parts)
        if "interval" not in positions:
            continue
        recognized[role] = (parts, positions)
        for row in parts[2]:
            interval = row[positions["interval"]]
            if type(interval) is not int:
                continue
            for original, name in fields.items():
                if original not in positions:
                    continue
                value = row[positions[original]]
                key = (interval, name)
                item = observations.setdefault(key, dict(
                    value=value, equal=True, occurrences=0))
                item["equal"] = item["equal"] and same(item["value"], value)
                item["occurrences"] += 1
    used = {}
    shared_cells = 0
    for role, (parts, positions) in recognized.items():
        addresses, columns, rows = parts
        if not rows:
            continue
        shared = {}
        for original, name in INTERVAL_FIELDS[role].items():
            if original not in columns:
                continue
            eligible = True
            for row in rows:
                interval = row[positions["interval"]]
                item = observations.get((interval, name)) if type(interval) is int else None
                if (item is None or not item["equal"] or item["occurrences"] < 2
                        or not same(item["value"], row[positions[original]])):
                    eligible = False
                    break
            if eligible:
                shared[original] = name
        if not shared:
            continue
        keep = [i for i, name in enumerate(addresses + columns) if name not in shared]
        table = tables[role]
        table["value_columns"] = [name for name in columns if name not in shared]
        table["rows"] = [[row[i] for i in keep] for row in rows]
        table["coordinate_columns_from_original_interval_address"] = shared
        for row in rows:
            interval = row[positions["interval"]]
            target = used.setdefault(interval, {})
            for original, name in shared.items():
                target[name] = row[positions[original]]
                shared_cells += 1
    if not used:
        return None
    columns = sorted({key for value in used.values() for key in value})
    report["original_observed_interval_coordinate_addresses"] = dict(
        address_columns=["interval"], value_columns=columns,
        rows=[[interval] + [values.get(key) for key in columns]
              for interval, values in sorted(used.items())],
        missing_address_cell_means_not_observed_not_a_derived_coordinate=True,
        same_interval_coordinates_shared_only_after_all_exact_comparisons=True)
    return dict(original_coordinate_cells_shared=shared_cells,
        actual_interval_address_count=len(used),
        no_coordinate_computation_or_mesh_reconstruction=True)


def share_RMS_stations(report):
    """Use the actual reported RMS fraction and interval, never recompute s."""
    tables = report.get("necessary_scalar_tables")
    if not isinstance(tables, dict):
        return None
    check = table_parts(tables.get("original_RMS_checks"))
    samples = table_parts(tables.get("original_RMS_failure_samples"))
    if check is None or samples is None:
        return None
    ci, si = column_map(check), column_map(samples)
    context_names = ["batch_record", "evaluation_role", "original_trial_index",
                     "original_RMS_check_index"]
    if (check[0] != context_names or samples[0][:4] != context_names
            or "fraction" not in ci or "interval" not in si or "s" not in samples[1]
            or not samples[2]):
        return None
    fractions = {}
    ambiguous = set()
    for row in check[2]:
        key = canonical(row[:4])
        value = row[ci["fraction"]]
        if key in fractions and not same(fractions[key], value):
            ambiguous.add(key)
        fractions[key] = value
    observed = {}
    addressed_rows = []
    for row in samples[2]:
        context = canonical(row[:4])
        if context not in fractions or context in ambiguous or type(row[si["interval"]]) is not int:
            return None
        fraction, interval, station = fractions[context], row[si["interval"]], row[si["s"]]
        if not (type(fraction) in (int, float) and type(station) in (int, float)):
            return None
        key = canonical([fraction, interval])
        item = observed.setdefault(key, dict(
            fraction=fraction, interval=interval, station=station, equal=True, count=0))
        item["equal"] = item["equal"] and same(item["station"], station)
        item["count"] += 1
        addressed_rows.append(key)
    if not observed or not all(item["equal"] for item in observed.values()):
        return None
    table = tables["original_RMS_failure_samples"]
    remove = si["s"]
    table["value_columns"] = [name for name in samples[1] if name != "s"]
    table["rows"] = [row[:remove] + row[remove+1:] for row in samples[2]]
    table["s_from_actual_RMS_check_fraction_and_interval"] = True
    report["original_observed_RMS_station_addresses"] = dict(
        address_columns=["fraction", "interval"], value_columns=["s"],
        rows=[[item["fraction"], item["interval"], item["station"]]
              for item in observed.values()],
        fraction_from_same_actual_evaluation_and_original_RMS_check=True,
        station_words_copied_not_formed_from_fraction_or_mesh=True)
    return dict(original_station_cells_shared=len(addressed_rows),
        actual_RMS_station_address_count=len(observed))


def share_selected_query_addresses(report):
    """The one actual complete query definition supplies only its typed address."""
    definitions = report.get("original_typed_query_definitions")
    tables = report.get("necessary_scalar_tables")
    if not (isinstance(definitions, list) and len(definitions) == 1
            and isinstance(definitions[0], list) and isinstance(tables, dict)):
        return None
    table = tables.get("all_original_failed_selected_queries")
    parts = table_parts(table)
    if parts is None or not parts[2]:
        return None
    index = column_map(parts)
    fields = ("kind", "interval", "fraction")
    if "query_index" not in index or any(key not in parts[1] for key in fields):
        return None
    queries = definitions[0]
    for row in parts[2]:
        q = row[index["query_index"]]
        if (type(q) is not int or q < 0 or q >= len(queries)
                or not isinstance(queries[q], dict)
                or any(key not in queries[q] or not same(queries[q][key], row[index[key]])
                       for key in fields)):
            return None
    keep = [i for i, name in enumerate(parts[0] + parts[1]) if name not in fields]
    table["value_columns"] = [name for name in parts[1] if name not in fields]
    table["rows"] = [[row[i] for i in keep] for row in parts[2]]
    table["typed_address_from_original_query_definition"] = dict(
        definition_index=0, original_query_index_column="query_index",
        exact_shared_fields=list(fields))
    return dict(original_failed_query_address_rows=len(parts[2]),
        all_actual_beta_values_and_station_words_remain=True)


def share_fixed_metadata_headers(report):
    tables = report.get("necessary_scalar_tables")
    if not isinstance(tables, dict):
        return None
    counts = {}
    for role, allowed in SHARED_METADATA.items():
        parts = table_parts(tables.get(role))
        if parts is None or len(parts[2]) < 2:
            continue
        positions = column_map(parts)
        shared = {}
        for field in allowed:
            if field not in parts[1]:
                continue
            value = parts[2][0][positions[field]]
            if all(same(value, row[positions[field]]) for row in parts[2][1:]):
                shared[field] = value
        if not shared:
            continue
        keep = [i for i, name in enumerate(parts[0] + parts[1]) if name not in shared]
        table = tables[role]
        table["value_columns"] = [key for key in parts[1] if key not in shared]
        table["rows"] = [[row[i] for i in keep] for row in parts[2]]
        table["same_original_metadata_for_every_returned_row"] = shared
        counts[role] = dict(actual_rows=len(parts[2]), shared_fields=list(shared))
    return dict(roles=counts) if counts else None


def group_fixed_contexts(report):
    tables = report.get("necessary_scalar_tables")
    if not isinstance(tables, dict):
        return None
    counts = {}
    for role, prefix in CONTEXT_PREFIXES.items():
        table = tables.get(role)
        parts = table_parts(table)
        if parts is None or not parts[2] or parts[0][:len(prefix)] != list(prefix):
            continue
        # Only adjacent identical prefixes form one block. The same context
        # appearing later starts a new block, so global row order is retained.
        groups = []
        for row in parts[2]:
            address = row[:len(prefix)]
            if not groups or not same(groups[-1]["address"], address):
                groups.append(dict(address=address, rows=[]))
            groups[-1]["rows"].append(row[len(prefix):])
        if len(groups) == len(parts[2]):
            continue
        del table["address_columns"]
        del table["rows"]
        table["context_columns"] = list(prefix)
        table["row_address_columns"] = parts[0][len(prefix):]
        table["contexts"] = groups
        counts[role] = dict(actual_rows=len(parts[2]), actual_contexts=len(groups))
    return dict(roles=counts) if counts else None


def share_actual_pair_handoffs(report):
    """Only the same complete receipt, after a real preceding produced pair."""
    batches = report.get("batches")
    if not isinstance(batches, list):
        return None
    shared = 0
    for position, batch in enumerate(batches):
        if position == 0 or not isinstance(batch, dict):
            continue
        previous = batches[position-1]
        if not isinstance(previous, dict):
            continue
        current = batch.get("input_pair")
        produced = previous.get("produced_pair")
        if (type(batch.get("batch_index")) is int
                and type(previous.get("batch_index")) is int
                and batch["batch_index"] == previous["batch_index"] + 1
                and previous.get("next_batch_eligible") is True
                and isinstance(current, dict) and isinstance(produced, dict)
                and same(current, produced)):
            del batch["input_pair"]
            batch["input_pair_is_exact_actual_produced_pair_of_batch_record"] = previous.get("batch_record")
            shared += 1
    return dict(exact_actual_pair_handoffs=shared) if shared else None


def compose(document):
    """Return one faithful necessary document; its original90KB rule is external."""
    if not isinstance(document, dict):
        return document
    report = copy.deepcopy(document)
    operations = []
    original_raw = canonical(report) + b"\n"
    original_size = len(original_raw)
    for operation in (
            share_candidate_components,
            share_interval_addresses,
            share_RMS_stations,
            share_selected_query_addresses,
            share_fixed_metadata_headers,
            group_fixed_contexts,
            share_actual_pair_handoffs):
        report = try_smaller(report, operation, operations)
    report["schema"] = RESULT_SCHEMA
    report["necessary_context_composition"] = dict(
        schema=SCHEMA,
        source=dict(file=Path(__file__).name, bytes=Path(__file__).stat().st_size,
            sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),
        original_selected_document_bytes_with_LF=original_size,
        original_selected_document_sha256_with_LF=hashlib.sha256(original_raw).hexdigest(),
        operations=operations,
        address_contexts_and_reported_coordinates_only=True,
        all_original_trial_and_failure_numeric_values_preserved=True,
        all_original_error_strings_and_unreturned_suffixes_preserved=True,
        all_original_FD_failed_contractions_and_selected_group_scalars_preserved=True,
        distinct_original_values_not_shared_by_tolerance=True,
        no_large_scientific_payload_or_generic_tree_codec=True,
        original_90000_byte_limit_and_transport70_unchanged=True,
        fitting_unknown_future_actual_summary_not_guaranteed=True)
    return report
