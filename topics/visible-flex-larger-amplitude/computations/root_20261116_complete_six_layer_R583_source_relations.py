#!/usr/bin/env python3
"""R600: complete named six-layer R583 source relations, no scientific selection.

The unchanged R588 module still handles its five ancestor bindings and every
RootStats section. Only actual R583 preparation/installation/compile bindings,
their explicit owner wrapper and four named source-member records are added.
Each source fact comes from the same already-selected necessary object.
The caller must retain its complete-body strict-smaller comparison and 90000/70
transport. No raw is read, restored by hash, encoded, split or truncated here.
"""
from __future__ import annotations
import hashlib
import importlib.util
import os
from pathlib import Path
import sys

SCHEMA = "R600-complete-six-layer-R583-source-relations-v1"
# Keep the ancestor's actual marker literal. This report has the R600 schema
# and its inverse explicitly accepts the six added named families.
MARKER = "R588_named_metadata_row"
BASE_FILE = "root_20261116_complete_named_source_and_root_statistics_relations.py"
BASE_BYTES = 19120
BASE_SHA256 = "6f7cb8049e8b77b26964deb675e5868d6b374ac2e07c49b6517c8e51d7db0dad"
R583_BINDING = "R583-loop-rounding-observation-source-binding-v1"
R583_BINDINGS = frozenset((R583_BINDING, R583_BINDING + "-installed-v1"))
EXTRA_FAMILIES = (
    "R583_complete_source_binding",
    "R583_complete_loop_mode_contract",
    "R583_complete_original_and_derived_kernel_identity",
    "R583_complete_compiler_function_identity",
    "R583_complete_component_plan_identity",
    "R583_complete_owner_source_binding_wrapper",
)
# The original family names are needed only by the standalone metadata inverse.
# Their numerical/statistics methods remain in the verified unchanged R588 file.
BASE_FAMILIES = frozenset((
    "source_binding", "verified_source_identity", "source_run_context",
    "source_inventory_rows", "source_literal_change_rows",
    "source_identity_catalogue", "source_literal_sha256",
    "root_owner_compilation", "root_physical_source_input_binding",
) + tuple(prefix + suffix for prefix in ("R550", "R561", "R564", "R572")
          for suffix in ("_statistics", "_path", "_last")))
FAMILIES = BASE_FAMILIES | frozenset(EXTRA_FAMILIES)
OBSERVATION_KEYS = (
    "prepared_or_compilation_binding_occurrences",
    "installed_binding_occurrences",
    "owner_source_binding_wrapper_occurrences",
    "loop_mode_contract_occurrences",
    "original_and_derived_kernel_identity_occurrences",
    "compiler_function_identity_occurrences",
    "component_plan_identity_occurrences",
)
_BASE = None
_RELATION_CLASS = None


def require(ok, message):
    if not ok:
        raise ValueError(message)


def require_public_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") ==
            "Rogerhu12/math-research-public",
            "R600 metadata belongs to the actual public Actions run")


def _base():
    """Load one frozen standard-library-only metadata dependency, never science."""
    global _BASE
    if _BASE is None:
        path = Path(__file__).resolve().parent / BASE_FILE
        require(path.is_file() and not path.is_symlink(),
                "The actual original R588 metadata module is present")
        raw = path.read_bytes()
        require(len(raw) == BASE_BYTES and
                hashlib.sha256(raw).hexdigest() == BASE_SHA256,
                "The complete unchanged R588 metadata source identity")
        spec = importlib.util.spec_from_file_location("_R600_original_R588", path)
        require(spec is not None and spec.loader is not None,
                "Explicit original metadata module loader")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        require(module.MARKER == MARKER and module.FAMILIES == BASE_FAMILIES,
                "Exact original marker and named-family contract")
        _BASE = module
    return _BASE


def _relations():
    """Add explicit R583 roles without mutating any R588 global or method."""
    global _RELATION_CLASS
    if _RELATION_CLASS is not None:
        return _RELATION_CLASS
    base = _base()

    class ExtraRows(base.NamedRows):
        def __init__(self, name):
            require(name in EXTRA_FAMILIES, "One declared R583 source-member family")
            self.name = name
            self.originals = []
            self.displays = []
            self.by_word = {}

    class SixLayerRelations(base.Relations):
        def __init__(self, source_hashes, computations):
            super().__init__(source_hashes, computations)
            for name in EXTRA_FAMILIES:
                self.rows[name] = ExtraRows(name)
            self.r583_observed = {name: 0 for name in OBSERVATION_KEYS}

        def source_binding(self, value):
            if not isinstance(value, dict) or not isinstance(value.get("schema"), str) \
                    or value["schema"] not in R583_BINDINGS:
                # The five original schemas and their exact original methods.
                return super().source_binding(value)
            if value["schema"] == R583_BINDING:
                self.r583_observed["prepared_or_compilation_binding_occurrences"] += 1
            else:
                self.r583_observed["installed_binding_occurrences"] += 1
            result = {}
            for name, item in value.items():
                if name == "actual_R572_source_binding":
                    # This is the sixth-layer edge missing from the R588 list.
                    # Unknown or malformed ancestor values remain literal.
                    result[name] = super().source_binding(item)
                elif name == "actual_loop_mode_source_contract" and isinstance(item, dict):
                    self.r583_observed["loop_mode_contract_occurrences"] += 1
                    result[name] = self.put("R583_complete_loop_mode_contract", item)
                elif name == "complete_R564_kernel_original_and_derived" and isinstance(item, dict):
                    self.r583_observed["original_and_derived_kernel_identity_occurrences"] += 1
                    result[name] = self.put(
                        "R583_complete_original_and_derived_kernel_identity", item)
                elif name in ("actual_compiler_function_source",
                              "original_compiler_function_source") and isinstance(item, dict):
                    self.r583_observed["compiler_function_identity_occurrences"] += 1
                    result[name] = self.put("R583_complete_compiler_function_identity", item)
                elif name == "source_plan" and isinstance(item, dict):
                    # Its complete absolute file/bytes/SHA object stays in this
                    # same relation; no file lookup or hash-only recovery.
                    self.r583_observed["component_plan_identity_occurrences"] += 1
                    result[name] = self.put("R583_complete_component_plan_identity", item)
                elif name in base.BINDING_IDENTITY_KEYS:
                    result[name] = self.source_identity(item)
                elif name in base.BINDING_IDENTITY_LISTS and isinstance(item, list):
                    result[name] = [self.source_identity(v) for v in item]
                elif name == "run" and isinstance(item, dict):
                    result[name] = self.put("source_run_context", item)
                else:
                    # Includes actual compile argv/exit/files, flags, errors,
                    # all future unknown members and malformed named members.
                    result[name] = item
            return self.put("R583_complete_source_binding", value, result)

        def source_scope(self, value):
            if isinstance(value, dict) and isinstance(value.get("schema"), str) \
                    and value["schema"] in R583_BINDINGS:
                return self.source_binding(value)
            # Original recursion and all existing named source families remain.
            return super().source_scope(value)

        def root_record(self, family, value):
            if family == "root_finite_word_cache_source_binding" and \
                    isinstance(value, dict):
                actual = value.get("actual_binding")
                if isinstance(actual, dict) and isinstance(actual.get("schema"), str) \
                        and actual["schema"] in R583_BINDINGS:
                    self.r583_observed["owner_source_binding_wrapper_occurrences"] += 1
                    result = {}
                    for name, item in value.items():
                        result[name] = (self.source_binding(item)
                            if name == "actual_binding" else item)
                    # Preserve actual_file and every unknown wrapper member.
                    return self.put("R583_complete_owner_source_binding_wrapper",
                                    value, result)
            # No numerical/statistics section, path, counter or last is changed.
            return super().root_record(family, value)

        def describe(self, domain):
            report = super().describe(domain)
            report["schema"] = SCHEMA
            report["unchanged_R588_source"] = dict(
                file=BASE_FILE, bytes=BASE_BYTES, sha256=BASE_SHA256)
            report["sixth_layer_binding_schemas"] = list(sorted(R583_BINDINGS))
            report["actual_named_R583_occurrences"] = dict(self.r583_observed)
            report["occurrence_counts_are_metadata_visits_not_scientific_calls"] = True
            report["original_R588_statistics_sections_paths_counters_and_last_unchanged"] = True
            report["complete_six_layer_source_members_and_unknown_columns_retained"] = True
            report["actual_compile_dependency_lists_not_reconstructed_or_reordered"] = True
            report["no_expected_dependency_or_success_flag_fabricated"] = True
            report["no_external_raw_or_source_fact_loaded_by_reference"] = True
            report["caller_must_choose_only_if_the_entire_same_body_is_strictly_smaller"] = True
            report["original_single_body90000_limit_and_real_overflow70_unchanged"] = True
            report["inverse"] = (
                "Apply R600.restore_relation to this selected metadata and this "
                "same-body report. Reconstruct each complete row in its recorded "
                "column order, including all six added R583 families. Resolve the "
                "original source_literal_sha256 family only to its original string. "
                "Then apply the unchanged outer or ancestor inverse at its original "
                "explicit scope. No R588-encoded parent subtree was reinterpreted.")
            return report

    _RELATION_CLASS = SixLayerRelations
    return _RELATION_CLASS


def _unchanged(value, domain):
    return value, dict(schema=SCHEMA, domain=domain, applied=False,
        reference_member=MARKER,
        reason="Existing original named marker is present; complete input left literal",
        existing_ancestor_relation_not_decoded_or_reinterpreted=True,
        original_complete_scope_retained=True,
        scientific_success_or_size_fit_inferred=False)


def source_necessary_relation(value, source_hashes, computations):
    """Same API: the caller supplies its complete unencoded source selection."""
    require_public_actions()
    base = _base()
    domain = "complete-original-source-preparation-necessary-with-R583-sixth-layer"
    if base.contains_marker(value):
        return _unchanged(value, domain)
    relation = _relations()(source_hashes, computations)
    selected = relation.source_scope(value)
    report = relation.describe(domain)
    report["applied"] = True
    return selected, report


def root_catalogue_relation(values, source_hashes, computations):
    """Same eight catalogue API; all R588 RootStats methods are unchanged."""
    require_public_actions()
    base = _base()
    require(isinstance(values, dict), "Original named RootWordMetadata catalogues")
    domain = "eight-original-root-word-metadata-catalogues-with-R583-sixth-layer"
    if base.contains_marker(values):
        return _unchanged(values, domain)
    relation = _relations()(source_hashes, computations)
    result = {}
    for name, records in values.items():
        if name in base.ROOT_CATALOGUE_NAMES and isinstance(records, list):
            result[name] = [relation.root_record(name, value) for value in records]
        else:
            result[name] = records
    report = relation.describe(domain)
    report["applied"] = True
    return result, report


def choose_complete_body(original_body, candidate_body, serialize):
    """Choose only a strict byte reduction of the same complete necessary body.

    The caller must already include the complete relation and its inverse scope
    in candidate_body and must pass its original complete-body serializer,
    including its unchanged original nonfinite-display policy when applicable.
    This function adds no post-comparison field and performs no scientific work.
    The original body-limit/70 decision is still applied to the returned body.
    """
    require(callable(serialize), "The original complete-body serialization function")
    original = serialize(original_body)
    candidate = serialize(candidate_body)
    require(type(original) is bytes and type(candidate) is bytes,
            "Both complete candidate bodies are compared as actual byte strings")
    return candidate_body if len(candidate) < len(original) else original_body


def restore_relation(value, report):
    """Standalone exact inverse of these metadata rows; no file or science read."""
    require(isinstance(report, dict) and report.get("schema") == SCHEMA and
            report.get("reference_member") == MARKER,
            "Actual R600 complete relation and explicit marker")
    if report.get("applied") is False:
        return value
    require(report.get("applied") is True, "Explicit applied R600 relation")
    tables = report["complete_named_tables"]
    require(isinstance(tables, dict), "Complete same-body named tables")
    rows = {}
    for family, table in tables.items():
        require(family in FAMILIES and isinstance(table, dict),
                "One original or six-layer named table family")
        count = table["record_count"]
        require(type(count) is int and count >= 0, "Original metadata record count")
        records = [None] * count
        for group in table["groups"]:
            columns = group["columns"]
            indices = group["original_record_indices"]
            values = group["column_values"]
            require(isinstance(columns, list) and all(isinstance(k, str) for k in columns)
                    and len(columns) == len(set(columns)) and len(columns) == len(values),
                    "Exactly the complete original ordered columns")
            for position, index in enumerate(indices):
                require(type(index) is int and 0 <= index < count and
                        records[index] is None, "Each complete original row index once")
                record = {}
                for key, column in zip(columns, values):
                    require(isinstance(column, dict) and
                            set(column) in ({"constant"}, {"original_values"}),
                            "Constant or every original column value")
                    if "constant" in column:
                        record[key] = column["constant"]
                    else:
                        require(isinstance(column["original_values"], list) and
                                len(column["original_values"]) == len(indices),
                                "Complete original column length")
                        record[key] = column["original_values"][position]
                records[index] = record
        require(all(row is not None for row in records), "All original rows present")
        rows[family] = records
    memo = {}
    active = set()

    def expand(item):
        if isinstance(item, list):
            return [expand(v) for v in item]
        if not isinstance(item, dict):
            return item
        if set(item) == {MARKER}:
            reference = item[MARKER]
            require(isinstance(reference, list) and len(reference) == 2 and
                    isinstance(reference[0], str) and type(reference[1]) is int,
                    "Exact explicit named metadata reference")
            family, index = reference
            require(family in rows and 0 <= index < len(rows[family]),
                    "Reference points to a present complete same-body row")
            key = family, index
            if key in memo:
                return memo[key]
            require(key not in active, "Finite acyclic source/statistics relation")
            active.add(key)
            restored = expand(rows[family][index])
            active.remove(key)
            if family == "source_literal_sha256":
                require(set(restored) == {"sha256"},
                        "The original named literal-SHA string row")
                restored = restored["sha256"]
            memo[key] = restored
            return restored
        return {name: expand(v) for name, v in item.items()}

    return expand(value)
