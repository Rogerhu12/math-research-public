#!/usr/bin/env python3
"""R606: complete named source contexts, module roles and change rows.

This consumes only the SAME already selected generation/composition object.
It does not select science, read raw, reconstruct a value from a hash, split a
body, raise 90000, or invoke its inverse as a new gate. Unknown fields remain
literal. Each complete candidate must be strictly shorter than the complete
original R586/R544 choice. Source-name factoring is confined to named source
rows and the producer's explicit source-file change values.
Author: OpenAI ChatGPT (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

GEN_SCHEMA = "R606-complete-source-generation-context-and-module-roles-v1"
COMP_SCHEMA = "R606-complete-source-composition-context-and-module-roles-v1"
HEADER = "R606_complete_named_source_relations"
CONTEXT = "$R606_literal_generator_context"
SOURCE_ROWS = "$R606_complete_source_rows"
LITERAL_ROW = "$R606_literal_source_row"
MODULE = "$R606_source_module"
CHANGE_SCHEMA = "R606-adjacent-original-member-change-contexts-v1"
RESERVED = {HEADER, CONTEXT, SOURCE_ROWS, LITERAL_ROW, MODULE}
LIMIT = 90000
HERE = Path(__file__).resolve().parent
DEPENDENCIES = {
    "generation": ("root_20261116_complete_generation_source_relations.py",
        "0ed83517eb6dd726e4e82f6b2b5f6dc391432994f7fcff93ef3b0e0692717484"),
    "composition": ("root_20261116_complete_source_composition_relations.py",
        "7bc351fe46ce6c8bf94ba067b106a0a21bd89950277910fe46006c502815b163"),
}
LITERAL_GENERATOR_SCHEMA = "R496-current-C-zero-linear-three-level-source-generation-v1"
# These are original immutable context facts, not success/error/frontier data.
# Completed, current_view, error, plan and elapsed_seconds are NOT in this list.
CONTEXT_FIELDS = (
    "schema", "repository", "run_id", "run_attempt", "source_commit", "source",
    "actual_computations", "original_sources_modified",
    "original_import_graph_relocated",
    "generated_sources_imported_compiled_or_executed",
    "full_transitive_graph_or_old_source_generation_replaced_by_this_plan",
    "original_numeric_gates_or_absolute_clock_changed",
    "generated_sources_are_not_preexisting_Git_files",
    "actual_science_or_speed_claimed", "scientific_computation_started")
RESULT_ROLES = ("original_result", "current_engine_result")
# Only source modules in these explicitly named lineage families are factored.
# The family and suffix are both stored verbatim. They never imply code equality.
BASE_NAME = re.compile(r"((?:geometry|root|exact)_20[0-9]{6}_)([A-Za-z0-9_.-]+)\Z")
FAMILY_PATTERNS = tuple(re.compile(pattern) for pattern in (
    r"(?:(?:current_C|actual202|continuous_ten)_)?(?:captured|bound)[0-9]+_(?:coast_base_)?zero_linear(?:_gzip)?_",
    r"(?:current_C|actual202|continuous_ten)_(?:coast_base_)?zero_linear(?:_gzip)?_",
    r"request[0-9]+_",
    r"(?:current_C|actual202|continuous_ten|original64|live128|native128)_",
))
SOURCE_CHANGE_ROOTS = {
    "native_sampling", "current_BVP", "current_BVP_launch", "current_BVP_readout",
    "pipeline", "actual202_candidate", "continuous_ten", "execution",
    "pruefer_provider", "closed_postsolve"}
PLUS_KEYS = {"path", "before_present", "after_present", "after"}
MINUS_KEYS = {"path", "before_present", "before", "after_present"}
REPLACE_KEYS = {"path", "before_present", "before", "after_present", "after"}


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("utf-8")


def identity(raw):
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def ordered_signature(value):
    """Preserve nested key order, all JSON types and the sign of float zero."""
    return json.dumps(value, ensure_ascii=True, sort_keys=False,
        separators=(",", ":"), allow_nan=False)


def _dependency(role):
    name, expected = DEPENDENCIES[role]
    path = HERE/name
    raw = path.read_bytes()
    if path.is_symlink() or hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError("The complete original metadata dependency differs: "+role)
    key = "_R606_original_metadata_"+role+"_"+expected
    module = sys.modules.get(key)
    if module is None:
        spec = importlib.util.spec_from_file_location(key, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[key] = module
        spec.loader.exec_module(module)
    return module


def _reserved(value):
    if isinstance(value, dict):
        return any(key in RESERVED for key in value) or any(
            _reserved(child) for child in value.values())
    if isinstance(value, list):
        return any(_reserved(child) for child in value)
    return False


def _root_restore(data, order):
    if (not isinstance(order, list) or any(type(key) is not str for key in order)
            or len(order) != len(set(order)) or set(order) != set(data)):
        raise ValueError("Complete original root key order is unavailable")
    return {key: data[key] for key in order}


class ModuleRoles:
    """A fixed semantic table for source basename = family + role suffix.

    Neither hashes nor arbitrary strings are interned. The only callers are
    source_rows[*][0], R544 source_additions[*][1], and before/after values at
    the explicitly named source change roots ending in /file.
    """
    def __init__(self):
        self.families = []
        self.suffixes = []
        self._family_index = {}
        self._suffix_index = {}
        self.references = 0

    def encode(self, name):
        if type(name) is not str:
            return copy.deepcopy(name)
        matched = BASE_NAME.fullmatch(name)
        if matched is None:
            return name
        stem, tail = matched.groups()
        pieces = [pattern.match(tail) for pattern in FAMILY_PATTERNS]
        pieces = [piece for piece in pieces if piece is not None
            and piece.end() < len(tail)]
        if not pieces:
            return name
        piece = max(pieces, key=lambda item: item.end())
        family, suffix = stem+tail[:piece.end()], tail[piece.end():]
        if family not in self._family_index:
            self._family_index[family] = len(self.families)
            self.families.append(family)
        if suffix not in self._suffix_index:
            self._suffix_index[suffix] = len(self.suffixes)
            self.suffixes.append(suffix)
        self.references += 1
        return [self._family_index[family], self._suffix_index[suffix]]

    def fields(self):
        return dict(source_module_family_prefixes=self.families,
            source_module_role_suffixes=self.suffixes,
            source_name_relation="exact stored family prefix + complete stored role suffix",
            same_suffix_does_not_assert_same_source_or_algorithm=True,
            source_hashes_bytes_matches_and_original_row_order_not_factored=True)


def _module_name(value, header):
    if type(value) is str:
        return value
    if (not isinstance(value, list) or len(value) != 2
            or any(type(index) is not int or index < 0 for index in value)):
        raise ValueError("An explicit complete source-module role pair is required")
    family, suffix = value
    families = header["source_module_family_prefixes"]
    suffixes = header["source_module_role_suffixes"]
    if family >= len(families) or suffix >= len(suffixes):
        raise ValueError("A source-module role index is outside its full table")
    if type(families[family]) is not str or type(suffixes[suffix]) is not str:
        raise ValueError("Source-module family and role are literal strings")
    return families[family]+suffixes[suffix]


def _selected_results(data):
    generations = data.get("generations")
    if not isinstance(generations, list):
        return
    for position, generation in enumerate(generations):
        if not isinstance(generation, dict):
            continue
        for role in RESULT_ROLES:
            result = generation.get(role)
            if isinstance(result, dict):
                yield position, role, result


def _factor_contexts(data):
    """Share only repeated complete original R496 context dictionaries.

    Key absence is never converted to null. The original_fields dictionary's
    complete key order is a layout; all noncontext fields stay literal.
    Context signatures include nested order and distinguish True/1/1.0/-0.0.
    """
    selected, groups = [], {}
    for generation_index, role, result in _selected_results(data):
        fields = result.get("original_fields")
        if (not isinstance(fields, dict)
                or fields.get("schema") != LITERAL_GENERATOR_SCHEMA
                or any(key not in fields for key in CONTEXT_FIELDS)):
            continue
        context = {key: fields[key] for key in fields if key in CONTEXT_FIELDS}
        signature = ordered_signature(context)
        groups.setdefault(signature, []).append((generation_index, role))
        selected.append((result, fields, context, signature))
    contexts, indexes, layouts = [], {}, []
    shared = 0
    for result, fields, context, signature in selected:
        if len(groups[signature]) < 2:
            continue
        if signature not in indexes:
            indexes[signature] = len(contexts)
            contexts.append(copy.deepcopy(context))
        order = list(fields)
        if order not in layouts:
            layouts.append(order)
        literal = {key: copy.deepcopy(value) for key, value in fields.items()
            if key not in CONTEXT_FIELDS}
        result["original_fields"] = {CONTEXT: [
            layouts.index(order), indexes[signature], literal]}
        shared += 1
    return dict(literal_generator_context_fields=list(CONTEXT_FIELDS),
        literal_generator_context_schema=LITERAL_GENERATOR_SCHEMA,
        literal_generator_contexts=contexts,
        original_fields_key_orders=layouts,
        shared_complete_literal_generator_context_occurrences=shared)


def _factor_source_rows(data, modules):
    transformed = 0
    generations = data.get("generations")
    if not isinstance(generations, list):
        return transformed
    for generation in generations:
        if not isinstance(generation, dict) or not isinstance(
                generation.get("source_rows"), list):
            continue
        rows, any_name = [], False
        for row in generation["source_rows"]:
            if isinstance(row, list) and len(row) == 4 and type(row[0]) is str:
                name = modules.encode(row[0])
                rows.append([name]+copy.deepcopy(row[1:]))
                any_name = any_name or type(name) is list
            else:
                rows.append({LITERAL_ROW: copy.deepcopy(row)})
        if any_name:
            generation["source_rows"] = {SOURCE_ROWS: rows}
            transformed += 1
    return transformed


def compose_generation(original, *, namespace, computations):
    """R586 selection plus two actual source-role relations, or R586 unchanged.

    This API consumes the original full selected state, never a prior run's
    necessary body, an omitted producer object, or a source-plan surrogate.
    The legacy and candidate reports remain full named metadata in facts.
    """
    legacy = _dependency("generation")
    baseline, legacy_facts = legacy.compose(original,
        namespace=namespace, computations=computations)
    before = canonical(original)
    baseline_body = canonical(baseline)
    facts = dict(schema=GEN_SCHEMA, original_selected=identity(before),
        original_R586_selected=identity(baseline_body),
        original_R586_transport=legacy_facts,
        fixed_limit_bytes=LIMIT, original_selection_changed=False,
        complete_whole_body_compared=True, no_part_transport=True,
        representation="original-R586-choice")
    if (not isinstance(original, dict) or _reserved(original)
            or "R586_source_metadata_representation" in original
            or not isinstance(original.get("generations"), list)):
        facts.update(reason="unrecognized original named source-generation state",
            transported=identity(baseline_body))
        return baseline, facts
    data = copy.deepcopy(original)
    modules = ModuleRoles()
    contexts = _factor_contexts(data)
    row_groups = _factor_source_rows(data, modules)
    if not contexts["shared_complete_literal_generator_context_occurrences"] and not modules.references:
        facts.update(reason="no applicable complete named context or source role",
            transported=identity(baseline_body))
        return baseline, facts
    header = dict(schema=GEN_SCHEMA, original_root_key_order=list(original),
        original_schema_present="schema" in original,
        original_schema=copy.deepcopy(original.get("schema")),
        original_selected=identity(before), **contexts, **modules.fields(),
        source_row_columns=["source_module_name_or_family_role",
            "actual_bytes", "actual_sha256", "matches_declared_identity"],
        no_source_or_raw_read_required_for_expansion=True,
        original_result_selection_scope_not_broadened=True,
        unknown_fields_errors_frontiers_and_partial_values_remain_literal=True)
    data["schema"] = GEN_SCHEMA
    data[HEADER] = header
    candidate, candidate_facts = legacy.compose(data,
        namespace=namespace, computations=computations)
    body = canonical(candidate)
    facts.update(candidate=identity(body),
        candidate_R586_transport=candidate_facts,
        source_row_groups=row_groups, source_module_name_references=modules.references,
        distinct_source_module_families=len(modules.families),
        distinct_complete_source_role_suffixes=len(modules.suffixes),
        shared_complete_context_occurrences=contexts[
            "shared_complete_literal_generator_context_occurrences"])
    if len(body) < len(baseline_body):
        facts.update(representation="named-original-generator-contexts-and-source-module-roles",
            transported=identity(body),
            byte_reduction_from_original_R586_choice=len(baseline_body)-len(body))
        return candidate, facts
    facts.update(reason="whole named candidate is not strictly smaller",
        transported=identity(baseline_body),
        byte_reduction_from_original_R586_choice=0)
    return baseline, facts


def expand_generation(selected):
    """Exact inverse for the declared metadata form; never a production gate."""
    legacy = _dependency("generation")
    if not isinstance(selected, dict) or selected.get("schema") != GEN_SCHEMA:
        return legacy.expand(selected)
    data = legacy.expand(selected)
    header = data.pop(HEADER)
    if header.get("schema") != GEN_SCHEMA:
        raise ValueError("The explicit generation relation schema differs")
    for _, _, result in _selected_results(data):
        value = result.get("original_fields")
        if not isinstance(value, dict) or set(value) != {CONTEXT}:
            continue
        row = value[CONTEXT]
        if not isinstance(row, list) or len(row) != 3:
            raise ValueError("An original literal-generator context row differs")
        layout, context_index, literal = row
        if (type(layout) is not int or layout < 0
                or type(context_index) is not int or context_index < 0):
            raise ValueError("Literal-generator context indices are integers")
        order = header["original_fields_key_orders"][layout]
        context = header["literal_generator_contexts"][context_index]
        if (not isinstance(literal, dict) or not isinstance(context, dict)
                or set(literal).intersection(context)
                or set(order) != set(literal) | set(context)
                or len(order) != len(set(order))):
            raise ValueError("All original context and literal members must be present")
        complete = {**context, **literal}
        result["original_fields"] = {key: complete[key] for key in order}
    for generation in data["generations"]:
        if not isinstance(generation, dict):
            continue
        value = generation.get("source_rows")
        if not isinstance(value, dict) or set(value) != {SOURCE_ROWS}:
            continue
        restored = []
        for row in value[SOURCE_ROWS]:
            if isinstance(row, dict) and set(row) == {LITERAL_ROW}:
                restored.append(copy.deepcopy(row[LITERAL_ROW]))
            elif isinstance(row, list) and len(row) == 4:
                restored.append([_module_name(row[0], header)]+copy.deepcopy(row[1:]))
            else:
                raise ValueError("A complete named source row differs")
        generation["source_rows"] = restored
    if header["original_schema_present"] is True:
        data["schema"] = copy.deepcopy(header["original_schema"])
    elif header["original_schema_present"] is False:
        data.pop("schema", None)
    else:
        raise ValueError("Original schema presence must be explicit")
    data = _root_restore(data, header["original_root_key_order"])
    if identity(canonical(data)) != header["original_selected"]:
        raise ValueError("The complete original selected generation differs")
    return data


def _change_kind(row):
    if not isinstance(row, dict) or type(row.get("path")) is not str:
        return None
    if set(row) == PLUS_KEYS and row["before_present"] is False and row["after_present"] is True:
        return "add", ("after",)
    if set(row) == MINUS_KEYS and row["before_present"] is True and row["after_present"] is False:
        return "remove", ("before",)
    if set(row) == REPLACE_KEYS and row["before_present"] is True and row["after_present"] is True:
        return "replace", ("before", "after")
    return None


def _change_source_value(path, value, modules):
    # Only actual source-descriptor file cells at original changed source roles.
    # Error strings, numerical strings, hashes, arrays and all other paths are literal.
    parts = path.split("/")
    if len(parts) >= 3 and parts[1] in SOURCE_CHANGE_ROOTS and parts[-1] == "file":
        encoded = modules.encode(value)
        if type(encoded) is list and type(value) is str:
            return {MODULE: encoded}
    return copy.deepcopy(value)


def _factor_changes(rows, modules):
    layouts, blocks = [], []
    named = literal_count = 0
    for row in rows:
        kind = _change_kind(row)
        if kind is None or "/" not in row["path"]:
            blocks.append([1, copy.deepcopy(row)])
            literal_count += 1
            continue
        tag, fields = kind
        parent, _, leaf = row["path"].rpartition("/")
        layout = dict(kind=tag, original_member_order=list(row))
        if layout not in layouts:
            layouts.append(layout)
        values = [_change_source_value(row["path"], row[field], modules) for field in fields]
        record = [layouts.index(layout), leaf, values]
        # Only adjacent rows share a parent; the original global sequence stays intact.
        if blocks and blocks[-1][0] == 0 and blocks[-1][1] == parent:
            blocks[-1][2].append(record)
        else:
            blocks.append([0, parent, [record]])
        named += 1
    return dict(schema=CHANGE_SCHEMA,
        block_tags=dict(adjacent_same_original_path_parent=0, complete_literal_row=1),
        named_row_columns=["original_layout", "original_path_leaf", "complete_before_after_values"],
        value_fields_by_kind=dict(add=["after"], remove=["before"], replace=["before", "after"]),
        layouts=layouts, blocks=blocks, original_row_count=len(rows),
        named_row_count=named, complete_literal_row_count=literal_count,
        consecutive_context_blocks_preserve_complete_global_row_order=True)


def compose_composition(original):
    """R544 source additions plus complete module roles and adjacent change rows."""
    legacy = _dependency("composition")
    baseline = legacy.compose(original)
    baseline_body = canonical(baseline)
    if (not isinstance(original, dict) or _reserved(original)
            or not isinstance(original.get("exact_member_changes"), list)
            or not isinstance(baseline, dict) or baseline.get("schema") != legacy.SCHEMA):
        return baseline
    candidate = copy.deepcopy(baseline)
    relation = candidate["exact_member_change_relations"]
    modules = ModuleRoles()
    for row in relation["source_additions"]:
        row[1] = modules.encode(row[1])
    relation["other_changes_in_original_order"] = _factor_changes(
        relation["other_changes_in_original_order"], modules)
    candidate["schema"] = COMP_SCHEMA
    candidate[HEADER] = dict(schema=COMP_SCHEMA,
        original_R544_root_key_order=list(baseline),
        original_R544_schema=legacy.SCHEMA,
        original_R544_selected=identity(baseline_body),
        original_R544_breakdown=legacy.breakdown(baseline),
        original_selected=identity(canonical(original)), **modules.fields(),
        source_addition_columns=["original_change_index", "source_module_name_or_family_role",
            "complete_after_sha256"],
        original_source_addition_positions_and_all_original_member_changes_preserved=True,
        unknown_changes_stay_complete_literal_rows=True,
        no_source_or_raw_read_required_for_expansion=True,
        original_presence_types_negative_zero_and_key_order_preserved=True,
        complete_whole_body_strictly_smaller_than_original_R544_choice=True,
        fixed_limit_bytes=LIMIT, no_part_transport=True)
    if len(canonical(candidate)) < len(baseline_body):
        return candidate
    return baseline


def _restore_changes(value, header):
    if not isinstance(value, dict) or value.get("schema") != CHANGE_SCHEMA:
        raise ValueError("The explicit adjacent member-change schema differs")
    answer = []
    for block in value["blocks"]:
        if not isinstance(block, list) or not block:
            raise ValueError("A complete change block is required")
        if block[0] == 1 and type(block[0]) is int and len(block) == 2:
            answer.append(copy.deepcopy(block[1]))
            continue
        if (block[0] != 0 or type(block[0]) is not int or len(block) != 3
                or type(block[1]) is not str or not isinstance(block[2], list)):
            raise ValueError("An adjacent original JSON-pointer parent block is required")
        parent = block[1]
        for item in block[2]:
            if (not isinstance(item, list) or len(item) != 3
                    or type(item[0]) is not int or item[0] < 0 or type(item[1]) is not str
                    or not isinstance(item[2], list)):
                raise ValueError("A complete named change row is required")
            layout = value["layouts"][item[0]]
            kind, order = layout["kind"], layout["original_member_order"]
            expected = {"add": ("after",), "remove": ("before",),
                "replace": ("before", "after")}.get(kind)
            if expected is None or len(item[2]) != len(expected):
                raise ValueError("Complete original before/after values are required")
            complete = dict(path=parent+"/"+item[1],
                before_present=kind != "add", after_present=kind != "remove")
            for key, raw in zip(expected, item[2]):
                if isinstance(raw, dict) and set(raw) == {MODULE}:
                    complete[key] = _module_name(raw[MODULE], header)
                else:
                    complete[key] = copy.deepcopy(raw)
            if len(order) != len(set(order)) or set(order) != set(complete):
                raise ValueError("All original change members and their order are required")
            answer.append({key: complete[key] for key in order})
    if len(answer) != value["original_row_count"]:
        raise ValueError("The original complete change count differs")
    return answer


def expand_composition(selected):
    """Exact inverse for the explicitly named R606/R544 composition relation."""
    legacy = _dependency("composition")
    if not isinstance(selected, dict) or selected.get("schema") != COMP_SCHEMA:
        return legacy.expand(selected)
    candidate = copy.deepcopy(selected)
    header = candidate.pop(HEADER)
    if header.get("schema") != COMP_SCHEMA or header["original_R544_schema"] != legacy.SCHEMA:
        raise ValueError("The explicit complete source-composition ancestry differs")
    relation = candidate["exact_member_change_relations"]
    for row in relation["source_additions"]:
        row[1] = _module_name(row[1], header)
    relation["other_changes_in_original_order"] = _restore_changes(
        relation["other_changes_in_original_order"], header)
    candidate["schema"] = header["original_R544_schema"]
    candidate = _root_restore(candidate, header["original_R544_root_key_order"])
    if identity(canonical(candidate)) != header["original_R544_selected"]:
        raise ValueError("The complete original R544 representation differs")
    original = legacy.expand(candidate)
    if identity(canonical(original)) != header["original_selected"]:
        raise ValueError("The complete original selected composition differs")
    return original


def breakdown(selected):
    """Named complete-body facts; these separate member sizes are not additive."""
    legacy = _dependency("composition")
    if not isinstance(selected, dict) or selected.get("schema") != COMP_SCHEMA:
        return legacy.breakdown(selected)
    header = selected[HEADER]
    relation = selected["exact_member_change_relations"]
    changes = relation["other_changes_in_original_order"]
    return dict(schema=COMP_SCHEMA, whole_selected_body=identity(canonical(selected)),
        original_selected=header["original_selected"],
        original_R544_selected=header["original_R544_selected"],
        original_R544_breakdown=copy.deepcopy(header["original_R544_breakdown"]),
        source_addition_count=len(relation["source_additions"]),
        other_original_change_count=changes["original_row_count"],
        named_change_count=changes["named_row_count"],
        literal_change_count=changes["complete_literal_row_count"],
        source_module_family_count=len(header["source_module_family_prefixes"]),
        complete_source_role_suffix_count=len(header["source_module_role_suffixes"]),
        source_additions_bytes=len(canonical(relation["source_additions"])),
        complete_change_blocks_bytes=len(canonical(changes)),
        source_family_table_bytes=len(canonical(header["source_module_family_prefixes"])),
        source_role_suffix_table_bytes=len(canonical(header["source_module_role_suffixes"])),
        member_sizes_are_separate_named_serializations_not_additive=True,
        fixed_limit_bytes=LIMIT, whole_body_not_split_or_truncated=True)
