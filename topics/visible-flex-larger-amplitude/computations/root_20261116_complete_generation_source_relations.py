#!/usr/bin/env python3
"""R586: lossless named source-generation metadata relationships.

Only the already selected immutable source-generation metadata is consumed.
No scientific file, array, ledger, result selector, threshold or clock changes.
The complete original body is returned literally if this named representation
does not reduce its canonical byte length. This is not a scientific gate.
Author: OpenAI / ChatGPT exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
import hashlib
import json

SCHEMA = "R586-complete-generation-source-identity-and-parent-row-relations-v1"
HEADER = "R586_source_metadata_representation"
FILE_REF = "$R586_source_identity"
PARENT_REF = "$R586_parent_generation"
TABLE_ROW = "$R586_named_row"
TABLE_LITERAL = "$R586_literal_row"
RESERVED = {HEADER, FILE_REF, PARENT_REF, TABLE_ROW, TABLE_LITERAL}
GENERATION_FIELDS = (
    "index", "schema", "generator", "plan", "receipt_directory",
    "actual_parent_return", "control_flow_scope", "original_result",
    "current_engine_result", "complete_original_stderr", "current_engine_stderr",
    "source_rows", "declared_source_count", "observed_present_count",
    "observed_matching_count", "errors", "original_result_absent")
PARENT_FIELDS = ("index", "schema", "actual_exit", "stdout", "stderr", "receipt_directory")
IDENTITY_FIELDS = ("file", "bytes", "sha256")
MAXIMUM_BYTES = 90000


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("utf-8")


def exact_same(left, right):
    return (type(left) is type(right)
        and json.dumps(left, ensure_ascii=True, sort_keys=False,
            separators=(",", ":"), allow_nan=False)
        == json.dumps(right, ensure_ascii=True, sort_keys=False,
            separators=(",", ":"), allow_nan=False))


def reserved_present(value):
    if isinstance(value, dict):
        return any(key in RESERVED for key in value) or any(
            reserved_present(item) for item in value.values())
    if isinstance(value, list):
        return any(reserved_present(item) for item in value)
    return False


def scalar_source_identity(value):
    return (isinstance(value, dict) and set(value) == set(IDENTITY_FIELDS)
        and isinstance(value["file"], str)
        and type(value["bytes"]) is int and value["bytes"] >= 0
        and isinstance(value["sha256"], str) and len(value["sha256"]) == 64
        and all(c in "0123456789abcdef" for c in value["sha256"]))


def top_member_sizes(value):
    """Named original selected members; separate serializations are not a sum."""
    return [[key, len(canonical({key: item}))] for key, item in value.items()]


class SourceIdentities:
    """One complete source-file receipt table, with explicit path roots.

    Every row retains the originally selected file string (literal or exact
    root+suffix), byte count, full hash and original three-key order. Observed
    receipts and declared generator/plan identities keep their original paths
    and roles; only exactly equal selected values, including key order, share.
    """
    def __init__(self, namespace, computations):
        self.roots = [str(namespace), str(computations)]
        self.rows = []
        self.orders = []
        self.by_identity = {}
        self.shortened_paths = 0
        self.references = 0

    def file_value(self, text):
        choices = [(len(root), index, root) for index, root in enumerate(self.roots)
            if text.startswith(root+"/")]
        if not choices:
            return text
        _, index, root = max(choices)
        suffix = text[len(root):]
        # Exact string concatenation is the entire path relation. No resolve,
        # normalization, source lookup or recovery from a hash is performed.
        self.shortened_paths += 1
        return [index, suffix]

    def receipt(self, value):
        order = list(value)
        if order not in self.orders:
            self.orders.append(order)
        layout = self.orders.index(order)
        signature = canonical([order, [value[key] for key in order]])
        if signature not in self.by_identity:
            index = len(self.rows)
            self.by_identity[signature] = index
            self.rows.append([self.file_value(value["file"]), value["bytes"],
                value["sha256"], layout])
        self.references += 1
        return {FILE_REF: self.by_identity[signature]}

    def encode(self, value):
        if scalar_source_identity(value):
            return self.receipt(value)
        if isinstance(value, dict):
            return {key: self.encode(item) for key, item in value.items()}
        if isinstance(value, list):
            return [self.encode(item) for item in value]
        return copy.deepcopy(value)


def named_rows(rows, allowed, layouts):
    """Tabulate only the two explicitly named producer row families."""
    answer = []
    for row in rows:
        if isinstance(row, dict) and set(row).issubset(set(allowed)):
            order = list(row)
            if order not in layouts:
                layouts.append(order)
            answer.append({TABLE_ROW: [layouts.index(order), [row[key] for key in order]]})
        else:
            answer.append({TABLE_LITERAL: row})
    return answer


def compose(original, *, namespace, computations):
    """Return the complete selected object and small transport facts.

    The sampler/native/FD/geometry fields are not inputs to this module.
    Unknown source-metadata fields, error text and failure addresses remain
    literal. There is no content-dependent scientific acceptance decision.
    """
    if not isinstance(original, dict):
        raise TypeError("The original selected source-generation object is a dictionary")
    before = canonical(original)
    facts = dict(schema=SCHEMA, original_selected_bytes=len(before),
        original_selected_sha256=hashlib.sha256(before).hexdigest(),
        original_member_sizes=top_member_sizes(original),
        member_sizes_are_separate_named_serializations_not_additive=True,
        fixed_limit_bytes=MAXIMUM_BYTES, scientific_selection_changed=False,
        original_fields_omitted=False, representation="literal-original",
        no_external_source_or_raw_needed_for_expansion=True)
    generations = original.get("generations")
    parent = original.get("original_materialization_record")
    parent_rows = parent.get("generations") if isinstance(parent, dict) else None
    if (reserved_present(original) or not isinstance(generations, list)
            or (parent_rows is not None and not isinstance(parent_rows, list))):
        facts.update(representation_reason="unrecognized named source-metadata shape",
            transported_bytes=len(before), transported_sha256=hashlib.sha256(before).hexdigest())
        return copy.deepcopy(original), facts
    # Link only the actual duplicated original parent row, with strict type,
    # all JSON values, absence, negative zero and original object order equal.
    data = copy.deepcopy(original)
    linked = []
    actual_parent_rows = parent_rows if isinstance(parent_rows, list) else []
    for position, row in enumerate(data["generations"]):
        if not isinstance(row, dict) or "actual_parent_return" not in row:
            continue
        value = row["actual_parent_return"]
        if not isinstance(value, dict):
            continue
        matches = [index for index, item in enumerate(actual_parent_rows)
            if isinstance(item, dict) and exact_same(value, item)]
        if len(matches) == 1:
            row["actual_parent_return"] = {PARENT_REF: matches[0]}
            linked.append([position, matches[0]])
    identities = SourceIdentities(namespace, computations)
    data = identities.encode(data)
    generation_layouts, parent_layouts = [], []
    data["generations"] = named_rows(data["generations"],
        GENERATION_FIELDS, generation_layouts)
    if isinstance(parent_rows, list):
        data["original_materialization_record"]["generations"] = named_rows(
            data["original_materialization_record"]["generations"],
            PARENT_FIELDS, parent_layouts)
    header = dict(schema=SCHEMA, original_schema=original.get("schema"),
        original_root_key_order=list(original), original_selected_bytes=len(before),
        original_selected_sha256=hashlib.sha256(before).hexdigest(),
        fixed_named_source_identity_columns=["original_selected_file_or_root_suffix", "original_selected_bytes",
            "original_selected_sha256", "original_identity_key_order"],
        source_file_roots=identities.roots,
        source_file_root_order=["actual_namespace", "actual_computations"],
        original_identity_key_orders=identities.orders,
        source_identity_rows=identities.rows,
        source_identity_reference_key=FILE_REF,
        source_identity_keeps_declared_or_observed_role_at_each_original_member_path=True,
        no_declared_source_identity_substituted_for_an_actual_observed_identity=True,
        named_row_reference_key=TABLE_ROW, literal_row_key=TABLE_LITERAL,
        generation_row_layouts=generation_layouts,
        parent_generation_row_layouts=parent_layouts,
        fixed_generation_field_universe=list(GENERATION_FIELDS),
        fixed_parent_generation_field_universe=list(PARENT_FIELDS),
        original_parent_row_reference_key=PARENT_REF,
        linked_parent_row_positions=linked,
        all_original_source_rows_and_matches_preserved=True,
        complete_original_errors_frontiers_stdout_stderr_scope_preserved=True,
        absent_null_types_negative_zero_and_order_preserved=True,
        no_arbitrary_object_dictionary_or_scientific_tree_encoding=True,
        no_large_body_split_or_limit_increase=True,
        no_external_original_body_or_source_file_required_to_expand=True)
    data[HEADER] = header
    after = canonical(data)
    facts.update(distinct_source_identity_rows=len(identities.rows),
        source_identity_references=identities.references,
        shortened_original_file_paths=identities.shortened_paths,
        shared_exact_parent_rows=len(linked),
        named_generation_layouts=len(generation_layouts),
        named_parent_layouts=len(parent_layouts),
        candidate_bytes=len(after), candidate_sha256=hashlib.sha256(after).hexdigest())
    if len(after) < len(before):
        facts.update(representation="named-source-file-and-parent-relations",
            transported_bytes=len(after), transported_sha256=hashlib.sha256(after).hexdigest(),
            byte_reduction=len(before)-len(after))
        return data, facts
    facts.update(representation_reason="complete named representation was not smaller",
        transported_bytes=len(before), transported_sha256=hashlib.sha256(before).hexdigest(),
        byte_reduction=0)
    return copy.deepcopy(original), facts


def expand(value):
    """Exact inverse of the named source metadata form; not a runtime gate."""
    if not isinstance(value, dict) or HEADER not in value:
        return copy.deepcopy(value)
    data = copy.deepcopy(value)
    header = data.pop(HEADER)
    if header.get("schema") != SCHEMA:
        raise ValueError("The explicit R586 named source metadata schema")
    def rows(items, layouts):
        out = []
        for item in items:
            if isinstance(item, dict) and set(item) == {TABLE_ROW}:
                layout_index, fields = item[TABLE_ROW]
                order = layouts[layout_index]
                if len(order) != len(fields):
                    raise ValueError("Complete named row length differs")
                out.append(dict(zip(order, fields)))
            elif isinstance(item, dict) and set(item) == {TABLE_LITERAL}:
                out.append(item[TABLE_LITERAL])
            else:
                raise ValueError("An explicit complete named source row")
        return out
    data["generations"] = rows(data["generations"], header["generation_row_layouts"])
    parent = data.get("original_materialization_record")
    if isinstance(parent, dict) and isinstance(parent.get("generations"), list):
        parent["generations"] = rows(parent["generations"],
            header["parent_generation_row_layouts"])
    decoded_receipts = []
    for file_value, count, digest, order_index in header["source_identity_rows"]:
        if isinstance(file_value, list):
            root_index, suffix = file_value
            file_value = header["source_file_roots"][root_index]+suffix
        fields = dict(file=file_value, bytes=count, sha256=digest)
        order = header["original_identity_key_orders"][order_index]
        decoded_receipts.append({key: fields[key] for key in order})
    def decode(item):
        if isinstance(item, dict) and set(item) == {FILE_REF}:
            return copy.deepcopy(decoded_receipts[item[FILE_REF]])
        if isinstance(item, dict):
            return {key: decode(child) for key, child in item.items()}
        if isinstance(item, list):
            return [decode(child) for child in item]
        return item
    data = decode(data)
    parent = data.get("original_materialization_record")
    parent_rows = parent.get("generations") if isinstance(parent, dict) else None
    for row in data["generations"]:
        if isinstance(row, dict):
            item = row.get("actual_parent_return")
            if isinstance(item, dict) and set(item) == {PARENT_REF}:
                row["actual_parent_return"] = copy.deepcopy(parent_rows[item[PARENT_REF]])
    return {key: data[key] for key in header["original_root_key_order"]}
