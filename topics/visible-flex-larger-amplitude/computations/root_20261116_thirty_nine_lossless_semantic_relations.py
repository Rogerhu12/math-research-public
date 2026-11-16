#!/usr/bin/env python3
"""R533 complete39 necessary semantic relations, after the exact R512 selectors.

Only the already selected necessary document is consumed. The original eight
model/FD pairs, numerical values, errors and all failed addresses are untouched.
These are named file/parameter/FD/QP/address relations, not a generic JSON-tree
dictionary or scientific-array codec. Expansion restores the input canonical
JSON including scalar kind, signed zero, absent fields, list order and null.
The original one-body90000-byte limit remains external and unchanged.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

SCHEMA = "R533-complete39-lossless-necessary-semantic-relations-v1"
RESULT_SCHEMA = "R533-one-complete39-necessary-whole-chain-v1"
RELATIONS = "necessary_semantic_relations"
PREVIOUS_FILE = "root_20261116_thirty_nine_actual_role_contexts.py"
PREVIOUS_SHA = "f79328ed83fee9757de1f5987067a0187b5cba53d7daf5b82a610149540ebd54"
PREVIOUS_RESULT_SCHEMA = "request223-one-necessary-whole-chain-contexts-v1"
_PREVIOUS = None

# Each path is an actual R454/R512 necessary producer member. Deepest members
# precede their parents; inverse restoration uses the reverse order.
BATCH_NODE_ROLES = (
    ("trial_tree_identity", ("full_original_trial_tree_identity",),
        ("canonical_bytes", "canonical_sha256")),
    ("QP_identity", ("QP", "full_original_QP_summary_identity"),
        ("canonical_bytes", "canonical_sha256")),
    ("FD_sources_identity", ("FD", "complete_consumed_source_mapping_identity"),
        ("source_count", "canonical_bytes", "canonical_sha256")),
    ("FD_direct_history_identity",
        ("FD", "groups", "direct_boundary", "full_original_direction_history_identity"),
        ("canonical_bytes", "canonical_sha256")),
    ("FD_separated_history_identity",
        ("FD", "groups", "separated_boundary", "full_original_direction_history_identity"),
        ("canonical_bytes", "canonical_sha256")),
    ("scalar_profile_identity",
        ("actual_pair_parameters", "complete_scalar_profile_identity"),
        ("canonical_bytes", "canonical_sha256")),
    ("native_height_identity",
        ("actual_pair_parameters", "original_native_height_identity"),
        ("canonical_bytes", "canonical_sha256")),
    ("parameter_source_presence",
        ("actual_pair_parameters", "original_parameter_sources_present"),
        ("frozen_design_parameters", "actual_global_scalar_parameters")),
    ("parameter_values", ("actual_pair_parameters",),
        ("original_frozen_design_parameters", "original_global_scalar_parameters",
         "original_parameter_readout_complete")),
    ("field_subset_identity", ("field_subset_identity",),
        ("schema", "complete_selected_fields_present", "sha256")),
    ("FD_direct_metadata", ("FD", "groups", "direct_boundary"),
        ("original_group_present", "schedule_equals_first_actual_group_schedule")),
    ("FD_separated_metadata", ("FD", "groups", "separated_boundary"),
        ("original_group_present", "schedule_equals_first_actual_group_schedule")),
    ("FD_metadata", ("FD",),
        ("original_report_present", "original_failed_contraction_record_count")),
    ("QP_metadata", ("QP",),
        ("original_report_present", "QP_arrays_and_iteration_history_not_exported",
         "actual_returned_scalar_sections", "final_actual_full_model_evidence_present")),
    ("input_pair", ("input_pair",),
        ("warm_file", "warm_bytes", "warm_sha256", "status_file", "status_bytes",
         "status_sha256", "JSON_reserialized", "materialized_for_this_job")),
    ("produced_pair", ("produced_pair",),
        ("warm_file", "warm_bytes", "warm_sha256", "status_file", "status_bytes",
         "status_sha256", "JSON_reserialized", "materialized_for_this_job")),
    ("batch_envelope", (),
        ("batch_index", "original_trial_source", "returned_original_trial_count",
         "returned_trial_indices", "not_recorded_original_trial_indices",
         "nearest_rejected_original_trial_index", "actual_parent_optimizer_schema",
         "original_model_exit_code", "original_FD_exit_code", "next_batch_eligible",
         "actual_surviving_batch", "actual_surviving_parent_carrier", "actual_namespace",
         "no_process_exit_or_missing_phase_inferred",
         "no_model_FD_success_or_completed_handoff_inferred", "original_status_present",
         "input_pair_is_exact_actual_produced_pair_of_batch_record")),
)
NODE_MAP = {role: (path, columns) for role, path, columns in BATCH_NODE_ROLES}

PRIMARY_FILES = (
    "thirty-nine-condensed-warm/model-000.json",
    "thirty-nine-condensed-warm/driver-status.json",
    "thirty-nine-condensed-warm/condensed-QP-summary.json",
    "physical-response/response-check.json",
    "thirty-nine-condensed-warm/warm-001.json.gz",
)
INDEX_RELATIONS = {
    "original_domain_index_sets": (
        "batch_record", "evaluation_role", "original_trial_index",
        "original_bad_midpoint_index_ranges"),
    "original_selected_query_index_sets": (
        "batch_record", "original_trial_index",
        "evaluated_selected_query_index_ranges"),
}

# Constant-column sharing is restricted to bool/null and the following named
# policy, identity, cardinality or fixed producer fields. Floating norm/error/
# residual/weight/coordinate/extremum columns are never in this set.
CONSTANT_METADATA_FIELDS = frozenset((
    "schema", "original_trial_source", "actual_parent_optimizer_schema",
    "warm_file", "status_file", "latest_warm_file", "canonical_sha256",
    "source_count", "actual_returned_scalar_sections",
    "original_frozen_design_parameters", "returned_original_trial_count",
    "original_model_exit_code", "original_FD_exit_code",
    "original_direction_record_count", "original_failed_contraction_record_count",
    "midpoint_point_record_count", "midpoint_returned_failure_record_count",
    "selected_query_count", "points", "invalid_count", "finite_count",
    "negative_count", "nonfinite_count", "zero_count",
    "original_full_coordinate_count", "local_coordinate_count",
    "original_inequality_row_count", "maximum_working_rows", "maximum_dual_sweeps",
    "accepted_sha256", "tail_anchor_sha256", "tail_config_sha256", "source_sha256",
    "classification",
))
SCALAR_TABLE_ROLES = frozenset((
    "model_scalar_results", "original_status", "status_standalone_model_field_relation",
    "domain_returns", "original_RMS_checks", "original_RMS_returned_failure_samples",
    "original_midpoint_failure_records", "original_physical_argmax",
    "original_physical_argmax_component", "original_physical_argmax_frozen_weight",
    "all_original_trials", "selected_linear_beta_squared",
    "all_selected_linear_reserve_slack", "independent_actual_directional_check",
    "all_original_failed_selected_queries", "FD_original_report", "FD_original_groups",
    "FD_all_original_failed_contractions", "QP_comparison", "QP_original_C_selection",
    "QP_condensed_candidate_selection", "QP_local_QP_report",
    "QP_last_saved_local_stage", "QP_final_actual_full_model_evidence",
    "QP_all_original_linear_slack",
))
RMS_CONTEXT_ROLES = (
    "original_RMS_checks", "original_RMS_returned_failure_samples",
)


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode("ascii")


def same(left, right):
    return canonical(left) == canonical(right)


def source_identity():
    path = Path(__file__)
    raw = path.read_bytes()
    return dict(file=path.name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def previous():
    global _PREVIOUS
    if _PREVIOUS is None:
        path = Path(__file__).resolve().parent / PREVIOUS_FILE
        raw = path.read_bytes()
        if path.is_symlink() or hashlib.sha256(raw).hexdigest() != PREVIOUS_SHA:
            raise RuntimeError("The real frozen R512 necessary formatter source is required")
        spec = importlib.util.spec_from_file_location("_R533_original_R512", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _PREVIOUS = module
    return _PREVIOUS


def _node(batch, path):
    current = batch
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current if isinstance(current, dict) else None


def _prune_empty_path(batch, path):
    # Only containers actually emptied by a recorded named relation are pruned.
    for depth in range(len(path), 0, -1):
        parent = _node(batch, path[:depth-1])
        if parent is None or parent.get(path[depth-1]) != {}:
            break
        del parent[path[depth-1]]


def _restore_node(batch, path):
    current = batch
    for key in path:
        if key not in current:
            current[key] = {}
        if not isinstance(current[key], dict):
            raise ValueError("Named necessary relation collides with an original literal")
        current = current[key]
    return current


def _value_allowed(field, value):
    if value is None or type(value) in (str, int, float, bool):
        return True
    if (isinstance(value, dict) and set(value) == {"original_nonfinite_JSON_token"}
            and isinstance(value["original_nonfinite_JSON_token"], str)):
        return True
    if field in ("original_frozen_design_parameters", "original_global_scalar_parameters"):
        return isinstance(value, list) and len(value) == 3 and all(
            item is None or type(item) in (str, int, float, bool)
            or (isinstance(item, dict) and set(item) == {"original_nonfinite_JSON_token"})
            for item in value)
    if field in ("returned_trial_indices", "not_recorded_original_trial_indices"):
        return isinstance(value, list) and all(type(item) is int for item in value)
    if field == "actual_returned_scalar_sections":
        return isinstance(value, list) and all(isinstance(item, str) for item in value)
    return False


def pack_batch_nodes(report):
    batches = report.get("batches")
    if not isinstance(batches, list):
        return False
    made = {}
    for role, path, allowed in BATCH_NODE_ROLES:
        blocks = []
        for position, batch in enumerate(batches):
            obj = _node(batch, path)
            if obj is None:
                continue
            columns = [key for key in allowed if key in obj and _value_allowed(key, obj[key])]
            if not columns:
                continue
            if not blocks or blocks[-1]["value_columns"] != columns:
                blocks.append(dict(value_columns=columns, rows=[]))
            blocks[-1]["rows"].append([position] + [obj.pop(key) for key in columns])
            if path:
                _prune_empty_path(batch, path)
        if blocks:
            made[role] = dict(address_columns=["original_batch_position"], blocks=blocks)
    if not made:
        return False
    report[RELATIONS]["batch_nodes"] = made
    return True


def unpack_batch_nodes(report, relations):
    batches = report["batches"]
    made = relations.get("batch_nodes", {})
    for role, path, _ in reversed(BATCH_NODE_ROLES):
        entry = made.get(role)
        if entry is None:
            continue
        for block in entry["blocks"]:
            columns = block["value_columns"]
            for row in block["rows"]:
                position = row[0]
                if type(position) is not int or not 0 <= position < len(batches):
                    raise ValueError("Original necessary batch position is invalid")
                obj = _restore_node(batches[position], path)
                if any(key in obj for key in columns) or len(row) != len(columns)+1:
                    raise ValueError("Named batch values collide or have a different width")
                obj.update(zip(columns, row[1:]))


def pack_primary_files(report):
    batches = report.get("batches")
    if not isinstance(batches, list):
        return False
    files = {}
    addressed = []
    for batch_position, batch in enumerate(batches):
        rows = batch.get("primary_outputs") if isinstance(batch, dict) else None
        if not isinstance(rows, list):
            continue
        # This operation accepts this whole known member or leaves it literal.
        if not all(isinstance(row, dict) and row.get("file") in PRIMARY_FILES
                and set(row) <= {"file", "present", "bytes", "sha256"}
                and type(row.get("present")) is bool
                and all(_value_allowed(key, value) for key, value in row.items())
                for row in rows):
            continue
        addressed.append(batch_position)
        for file_position, obj in enumerate(rows):
            file = obj["file"]
            columns = [key for key in ("present", "bytes", "sha256") if key in obj]
            blocks = files.setdefault(file, [])
            if not blocks or blocks[-1]["value_columns"] != columns:
                blocks.append(dict(value_columns=columns, rows=[]))
            blocks[-1]["rows"].append([batch_position, file_position]
                + [obj[key] for key in columns])
        del batch["primary_outputs"]
    if not addressed:
        return False
    report[RELATIONS]["primary_files"] = dict(
        original_batch_positions=addressed,
        address_columns=["original_batch_position", "original_file_position"],
        files={file: dict(blocks=blocks) for file, blocks in files.items()})
    return True


def unpack_primary_files(report, relations):
    entry = relations.get("primary_files")
    if entry is None:
        return
    batches = report["batches"]
    restored = {position: [] for position in entry["original_batch_positions"]}
    for file, item in entry["files"].items():
        if file not in PRIMARY_FILES:
            raise ValueError("Unrecognized fixed producer file role")
        for block in item["blocks"]:
            columns = block["value_columns"]
            for row in block["rows"]:
                if len(row) != len(columns)+2 or row[0] not in restored:
                    raise ValueError("Primary receipt row has no original member")
                restored[row[0]].append((row[1], dict(file=file, **dict(zip(columns, row[2:])))))
    for position, rows in restored.items():
        rows.sort(key=lambda item: item[0])
        if [item[0] for item in rows] != list(range(len(rows))):
            raise ValueError("Every original primary file position must be present exactly once")
        if "primary_outputs" in batches[position]:
            raise ValueError("Primary receipt literal and relation collide")
        batches[position]["primary_outputs"] = [item[1] for item in rows]


def pack_index_sets(report):
    made = []
    for name, columns in INDEX_RELATIONS.items():
        rows = report.get(name)
        if not (isinstance(rows, list) and rows and all(
                isinstance(row, dict) and set(row) == set(columns) for row in rows)):
            continue
        report[name] = dict(columns=list(columns),
            rows=[[row[key] for key in columns] for row in rows])
        made.append(name)
    if made:
        report[RELATIONS]["index_set_tables"] = made
    return bool(made)


def unpack_index_sets(report, relations):
    for name in relations.get("index_set_tables", []):
        if name not in INDEX_RELATIONS:
            raise ValueError("Unrecognized original index-set role")
        item = report[name]
        columns = item["columns"]
        if columns != list(INDEX_RELATIONS[name]):
            raise ValueError("Original index-set columns differ")
        if not all(len(row) == len(columns) for row in item["rows"]):
            raise ValueError("Incomplete original index-set row")
        report[name] = [dict(zip(columns, row)) for row in item["rows"]]


def share_RMS_candidate_contexts(report):
    tables = report.get("necessary_scalar_tables")
    if not isinstance(tables, dict):
        return False
    shared = {}
    for role in RMS_CONTEXT_ROLES:
        table = tables.get(role)
        if not isinstance(table, dict):
            continue
        columns, contexts = table.get("context_columns"), table.get("contexts")
        if not (isinstance(columns, list) and isinstance(contexts, list)
                and "evaluation_role" in columns and "batch_record" in columns
                and "original_trial_index" in columns):
            continue
        phase = columns.index("evaluation_role")
        count = 0
        for original_context_index, item in enumerate(contexts):
            address = item.get("address") if isinstance(item, dict) else None
            rows = item.get("rows") if isinstance(item, dict) else None
            if (not isinstance(address, list) or len(address) != len(columns)
                    or address[phase] != "complete_RMS" or not isinstance(rows, list)
                    or "rows_from_actual_candidate_context" in item):
                continue
            wanted = list(address)
            wanted[phase] = "candidate"
            for candidate_index, candidate in enumerate(contexts):
                if (isinstance(candidate, dict) and same(candidate.get("address"), wanted)
                        and isinstance(candidate.get("rows"), list)
                        and same(candidate["rows"], rows)):
                    # Original context and global context order stay visible.
                    del item["rows"]
                    item["rows_from_actual_candidate_context"] = candidate_index
                    count += 1
                    break
        if count:
            shared[role] = count
    if shared:
        report[RELATIONS]["RMS_same_candidate_context_counts"] = shared
    return bool(shared)


def expand_RMS_candidate_contexts(report, relations):
    tables = report["necessary_scalar_tables"]
    for role, expected in relations.get("RMS_same_candidate_context_counts", {}).items():
        if role not in RMS_CONTEXT_ROLES:
            raise ValueError("Unexpected RMS semantic role")
        table = tables[role]
        contexts = table["contexts"]
        phase = table["context_columns"].index("evaluation_role")
        restored = 0
        for item in contexts:
            if "rows_from_actual_candidate_context" not in item:
                continue
            index = item.pop("rows_from_actual_candidate_context")
            if type(index) is not int or not 0 <= index < len(contexts):
                raise ValueError("Actual candidate context reference is out of range")
            candidate = contexts[index]
            wanted = list(item["address"])
            wanted[phase] = "candidate"
            if ("rows" in item or item["address"][phase] != "complete_RMS"
                    or not same(candidate["address"], wanted)
                    or not isinstance(candidate.get("rows"), list)):
                raise ValueError("Same-call candidate context reference differs")
            item["rows"] = copy.deepcopy(candidate["rows"])
            restored += 1
        if restored != expected:
            raise ValueError("RMS role reference count differs")


def _known_blocks(report, relations):
    for role, table in report.get("necessary_scalar_tables", {}).items():
        if role not in SCALAR_TABLE_ROLES or not isinstance(table, dict):
            continue
        values = table.get("value_columns")
        if not isinstance(values, list) or not all(isinstance(key, str) for key in values):
            continue
        if isinstance(table.get("rows"), list) and isinstance(table.get("address_columns"), list):
            yield "necessary_scalar_tables/"+role, table, len(table["address_columns"]), [table["rows"]]
        elif isinstance(table.get("contexts"), list) and isinstance(table.get("row_address_columns"), list):
            groups = [item["rows"] for item in table["contexts"]
                if isinstance(item, dict) and isinstance(item.get("rows"), list)]
            yield "necessary_scalar_tables/"+role, table, len(table["row_address_columns"]), groups
    for role, item in relations.get("batch_nodes", {}).items():
        for index, block in enumerate(item["blocks"]):
            yield "batch_nodes/"+role+"/"+str(index), block, 1, [block["rows"]]
    for file, item in relations.get("primary_files", {}).get("files", {}).items():
        for index, block in enumerate(item["blocks"]):
            yield "primary_files/"+file+"/"+str(index), block, 2, [block["rows"]]


def share_constant_columns(report):
    relations = report[RELATIONS]
    changed = []
    for label, table, address_count, groups in _known_blocks(report, relations):
        if "shared_original_column_values" in table:
            continue
        columns = table["value_columns"]
        rows = [row for group in groups for row in group]
        if len(rows) < 2 or not all(isinstance(row, list)
                and len(row) == address_count+len(columns) for row in rows):
            continue
        constants = []
        for position, field in enumerate(columns):
            first = rows[0][address_count+position]
            allowed = (first is None or type(first) is bool
                or field in CONSTANT_METADATA_FIELDS)
            if allowed and all(same(first, row[address_count+position]) for row in rows[1:]):
                constants.append([position, field, copy.deepcopy(first)])
        if not constants:
            continue
        kept = [position for position in range(len(columns))
                if position not in {item[0] for item in constants}]
        old_bytes = len(canonical(table))
        original_columns = table["value_columns"]
        original_groups = [list(group) for group in groups]
        table["value_columns"] = [columns[position] for position in kept]
        table["shared_original_column_values"] = constants
        for group in groups:
            group[:] = [row[:address_count]
                + [row[address_count+position] for position in kept] for row in group]
        if len(canonical(table)) >= old_bytes:
            table["value_columns"] = original_columns
            del table["shared_original_column_values"]
            for group, original in zip(groups, original_groups):
                group[:] = original
        else:
            changed.append(label)
    if changed:
        relations["constant_column_tables"] = changed
    return bool(changed)


def expand_constant_columns(report, relations):
    seen = []
    for label, table, address_count, groups in _known_blocks(report, relations):
        constants = table.get("shared_original_column_values")
        if constants is None:
            continue
        columns = list(table["value_columns"])
        by_position = {item[0]: item for item in constants}
        if len(by_position) != len(constants):
            raise ValueError("Repeated original constant-column position")
        width = len(columns)+len(constants)
        if any(type(position) is not int or not 0 <= position < width for position in by_position):
            raise ValueError("Original constant-column position out of range")
        original_columns = []
        at = 0
        for position in range(width):
            if position in by_position:
                original_columns.append(by_position[position][1])
            else:
                original_columns.append(columns[at])
                at += 1
        for group in groups:
            restored = []
            for row in group:
                if len(row) != address_count+len(columns):
                    raise ValueError("Original necessary scalar row width differs")
                values = []
                at = address_count
                for position in range(width):
                    if position in by_position:
                        values.append(copy.deepcopy(by_position[position][2]))
                    else:
                        values.append(row[at])
                        at += 1
                restored.append(row[:address_count]+values)
            group[:] = restored
        table["value_columns"] = original_columns
        del table["shared_original_column_values"]
        seen.append(label)
    if (len(seen) != len(relations.get("constant_column_tables", []))
            or set(seen) != set(relations.get("constant_column_tables", []))):
        raise ValueError("Constant-column table addresses differ")


def share_query_definition(report):
    definitions = report.get("original_typed_query_definitions")
    binding = report.get("source_and_actual_input_binding")
    if not isinstance(definitions, list) or len(definitions) != 1:
        return False
    entries = [binding] if isinstance(binding, dict) else binding
    if not isinstance(entries, list):
        return False
    positions = []
    for index, item in enumerate(entries):
        if (isinstance(item, dict) and "exact_query_specs" in item
                and same(item["exact_query_specs"], definitions[0])):
            del item["exact_query_specs"]
            positions.append(index)
    if not positions:
        return False
    report[RELATIONS]["binding_query_definition"] = dict(
        original_binding_is_list=isinstance(binding, list),
        original_binding_positions=positions, original_typed_query_definition_index=0)
    return True


def expand_query_definition(report, relations):
    reference = relations.get("binding_query_definition")
    if reference is None:
        return
    binding = report["source_and_actual_input_binding"]
    entries = binding if reference["original_binding_is_list"] else [binding]
    definition = report["original_typed_query_definitions"][
        reference["original_typed_query_definition_index"]]
    for index in reference["original_binding_positions"]:
        if "exact_query_specs" in entries[index]:
            raise ValueError("Query definition literal and semantic reference collide")
        entries[index]["exact_query_specs"] = copy.deepcopy(definition)


def share_chain_pair_receipts(report):
    batches = report.get("batches")
    state = report.get("actual_chain_state")
    if not isinstance(batches, list) or not isinstance(state, dict):
        return False
    references = []
    def visit(current, address):
        if not isinstance(current, dict):
            return
        for member in ("current_real_input_pair", "last_actual_completed_pair"):
            value = current.get(member)
            if not isinstance(value, dict):
                continue
            for position, batch in enumerate(batches):
                produced = batch.get("produced_pair") if isinstance(batch, dict) else None
                if isinstance(produced, dict) and same(value, produced):
                    del current[member]
                    references.append(dict(original_saved_state_positions=address,
                        original_pair_member=member, original_batch_position=position))
                    break
        for index, child in enumerate(current.get("actual_saved_chain_states", [])):
            visit(child, address+[index])
    visit(state, [])
    if references:
        report[RELATIONS]["chain_actual_pair_receipts"] = references
    return bool(references)


def expand_chain_pair_receipts(report, relations):
    for row in relations.get("chain_actual_pair_receipts", []):
        current = report["actual_chain_state"]
        for index in row["original_saved_state_positions"]:
            current = current["actual_saved_chain_states"][index]
        member = row["original_pair_member"]
        if member not in ("current_real_input_pair", "last_actual_completed_pair") or member in current:
            raise ValueError("Original same-pair state address differs")
        current[member] = copy.deepcopy(
            report["batches"][row["original_batch_position"]]["produced_pair"])


def compose_selected(document):
    """Apply to a complete R512 necessary object, without re-reading any science."""
    if (not isinstance(document, dict) or RELATIONS in document
            or document.get("schema") != PREVIOUS_RESULT_SCHEMA):
        return copy.deepcopy(document)
    original_raw = canonical(document)+b"\n"
    report = copy.deepcopy(document)
    report["schema"] = RESULT_SCHEMA
    report[RELATIONS] = dict(
        schema=SCHEMA, input_schema=document["schema"], source=source_identity(),
        original_selected_body=dict(bytes=len(original_raw),
            sha256=hashlib.sha256(original_raw).hexdigest(),
            scope="complete original R512 selected ASCII canonical JSON with one LF"),
        applied_operations=[],
        all_values_errors_addresses_and_list_order_preserved=True,
        no_generic_JSON_or_numeric_value_dictionary=True,
        one_body90000_limit_unchanged=True,
        unknown_future_actual_capacity_not_guaranteed=True)
    for operation in (
            share_RMS_candidate_contexts, share_query_definition,
            share_chain_pair_receipts, pack_index_sets,
            pack_primary_files, pack_batch_nodes, share_constant_columns):
        candidate = copy.deepcopy(report)
        if not operation(candidate):
            continue
        candidate[RELATIONS]["applied_operations"].append(operation.__name__)
        if len(canonical(candidate)) < len(canonical(report)):
            report = candidate
    # Include every new header and source/operation receipt in this comparison.
    # If there is no strict whole-body saving, preserve the original object.
    if len(canonical(report)+b"\n") >= len(original_raw):
        return copy.deepcopy(document)
    return report


def expand_selected(document):
    """Exact inverse of this named composition; no scientific action or gate."""
    if not isinstance(document, dict) or document.get("schema") != RESULT_SCHEMA:
        return copy.deepcopy(document)
    report = copy.deepcopy(document)
    relations = report.get(RELATIONS)
    if not isinstance(relations, dict) or relations.get("schema") != SCHEMA:
        raise ValueError("R533 semantic relation schema required")
    expand_constant_columns(report, relations)
    unpack_batch_nodes(report, relations)
    unpack_primary_files(report, relations)
    unpack_index_sets(report, relations)
    expand_chain_pair_receipts(report, relations)
    expand_query_definition(report, relations)
    expand_RMS_candidate_contexts(report, relations)
    report["schema"] = relations["input_schema"]
    del report[RELATIONS]
    return report


def transport_breakdown(document):
    """Small size/address metadata for a future real overflow, never a payload."""
    if not isinstance(document, dict):
        return dict(original_type=type(document).__name__)
    sections = []
    for key in ("source_and_actual_input_binding", "actual_chain_state", "batches",
            "original_domain_index_sets", "original_selected_query_index_sets",
            "all_actual_original_observer_errors", "original_typed_query_definitions",
            "original_FD_first_actual_direction_schedules", "necessary_context_composition",
            RELATIONS):
        if key in document:
            sections.append([key, len(canonical(document[key]))])
    scalar_roles = []
    for role, table in document.get("necessary_scalar_tables", {}).items():
        if role in SCALAR_TABLE_ROLES:
            scalar_roles.append([role, len(canonical(table))])
    return dict(schema="R533-necessary-semantic-section-byte-counts-v1",
        canonical_whole_body_bytes_with_LF=len(canonical(document)+b"\n"),
        size_columns=["actual_selected_semantic_member", "canonical_value_bytes_without_LF"],
        sections=sections, scalar_roles=scalar_roles,
        these_are_sizes_not_scientific_values_or_completion=True,
        no_summary_reconstruction_from_sizes_or_SHA=True)


def compose(document):
    """Actual assemble_chain integration: unchanged R512 selection, then R533."""
    return compose_selected(previous().compose(document))
