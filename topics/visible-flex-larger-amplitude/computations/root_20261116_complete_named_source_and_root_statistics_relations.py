#!/usr/bin/env python3
"""R588: exact named source and RootStats relations for original necessary scopes.

This module performs only metadata operations after the caller has selected its
complete original scope. It neither chooses scientific fields nor reads arrays,
solves, compiles, starts clocks, creates files, splits a body, or changes a gate.
The source interface is exclusively for an original source-preparation necessary
object. The statistics interface is exclusively for the eight named R573
RootWordMetadata catalogues, before their existing outer column table.
"""
from __future__ import annotations
import json
import math
import os

SCHEMA = "R588-complete-named-source-and-root-statistics-relations-v1"
MARKER = "R588_named_metadata_row"
BINDINGS = (
    "R535-native-root-finite-words-source-binding-v1",
    "R550-accepted-root-evaluation-source-binding-v1",
    "R561-exact-dyadic-average-source-binding-v1",
    "R564-exact-lifted-factor-product-source-binding-v1",
    "R572-exact-root-synthesis-products-source-binding-v1",
)
BINDING_SCHEMAS = frozenset(BINDINGS + tuple(v + "-installed-v1" for v in BINDINGS))
ANCESTOR_BINDING_KEYS = frozenset((
    "actual_R535_source_binding", "actual_R550_source_binding",
    "actual_R561_source_binding", "actual_R564_source_binding",
))
BINDING_IDENTITY_KEYS = frozenset((
    "actual_adapter", "source_plan", "actual_cpp_source",
    "actual_compiler_function_source", "original_compiler_function_source",
))
BINDING_IDENTITY_LISTS = frozenset((
    "actual_headers", "actual_original_sources", "actual_generated_sources",
))
SOURCE_CATALOGUE_SCHEMAS = frozenset((
    "R551-named-source-identity-catalogue-v1",
    "R562-named-source-identity-catalogue-v1",
    "R565-named-source-identity-catalogue-v1",
    "R573-named-source-identity-catalogue-v1",
))
SOURCE_INVENTORY_SCHEMAS = frozenset(
    prefix + "-ordered-source-inventory-rows-v1"
    for prefix in ("R551", "R562", "R565", "R573"))
SOURCE_CHANGE_SCHEMAS = frozenset(
    prefix + "-ordered-literal-change-identity-rows-v1"
    for prefix in ("R551", "R562", "R565", "R573"))
ROOT_CATALOGUE_NAMES = (
    "root_statistics", "root_finite_word_cache", "owner_compilation",
    "root_cache_compile_binding", "root_finite_word_cache_source_preparation",
    "root_finite_word_cache_source_binding",
    "root_finite_word_cache_compiler_installation",
    "physical_source_input_binding",
)
STAT_SECTIONS = {
    "root_accepted_evaluation_reuse": (
        "R550-same-root-next-iteration-complete-evaluation-reuse-v1",
        "R550", ("primal", "trace_variation")),
    "exact_dyadic_angular_average": (
        "R561-exact-normal-dyadic-angular-average-v1",
        "R561", ("root_residual", "root_gram", "primal_flux")),
    "exact_lifted_factor_product": (
        "R564-exact-lifted-factor-product-v1",
        "R564", ("root_residual", "root_gram", "primal_flux")),
    "exact_root_synthesis_products": (
        "R572-exact-root-synthesis-products-v1", "R572",
        ("fixed_fallback_P", "fixed_fallback_Pt", "L",
         "evaluation_u_words", "evaluation_u_fallback")),
}
FAMILIES = frozenset((
    "source_binding", "verified_source_identity", "source_run_context",
    "source_inventory_rows", "source_literal_change_rows",
    "source_identity_catalogue", "source_literal_sha256",
    "root_owner_compilation", "root_physical_source_input_binding",
) + tuple(prefix + suffix for prefix in ("R550", "R561", "R564", "R572")
          for suffix in ("_statistics", "_path", "_last")))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def require_public_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") ==
            "Rogerhu12/math-research-public",
            "R588 metadata belongs to the actual public Actions run")


def ordered(value):
    return json.dumps(value, sort_keys=False, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii")


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii") + b"\n"


def same(left, right):
    """Complete JSON type/value/member-order equality; no nonfinite sharing."""
    if type(left) is not type(right):
        return False
    if isinstance(left, float):
        if not math.isfinite(left) or not math.isfinite(right):
            return False
        return left == right and (left != 0 or
            math.copysign(1, left) == math.copysign(1, right))
    if isinstance(left, dict):
        return tuple(left) == tuple(right) and all(
            same(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(
            same(a, b) for a, b in zip(left, right))
    return left == right


def contains_marker(value):
    # Collision detection only; this does not encode an arbitrary tree.
    if isinstance(value, dict):
        return MARKER in value or any(contains_marker(v) for v in value.values())
    if isinstance(value, list):
        return any(contains_marker(v) for v in value)
    return False


class NamedRows:
    """A fixed semantic record family; complete original keys remain columns."""
    def __init__(self, name):
        require(name in FAMILIES, "Explicit R588 named metadata family")
        self.name = name
        self.originals = []
        self.displays = []
        self.by_word = {}

    def add(self, value, display=None):
        if not isinstance(value, dict):
            return value
        try:
            word = ordered(value)
        except (ValueError, TypeError):
            return value
        prior = self.by_word.get(word)
        if prior is not None and same(self.originals[prior], value):
            return {MARKER: [self.name, prior]}
        index = len(self.originals)
        self.by_word[word] = index
        self.originals.append(value)
        self.displays.append(value if display is None else display)
        return {MARKER: [self.name, index]}

    def describe(self):
        groups = []
        indices = {}
        for index, value in enumerate(self.displays):
            keys = tuple(value)
            if keys not in indices:
                indices[keys] = len(groups)
                groups.append(dict(columns=list(keys),
                    original_record_indices=[], records=[]))
            group = groups[indices[keys]]
            group["original_record_indices"].append(index)
            group["records"].append(value)
        result = []
        for group in groups:
            columns = []
            for name in group["columns"]:
                values = [row[name] for row in group["records"]]
                if all(same(value, values[0]) for value in values):
                    columns.append(dict(constant=values[0]))
                else:
                    columns.append(dict(original_values=values))
            result.append(dict(columns=group["columns"],
                original_record_indices=group["original_record_indices"],
                column_values=columns))
        return dict(record_count=len(self.displays), groups=result)


class Relations:
    """The only row families and traversals are the named domains above."""
    def __init__(self, source_hashes, computations):
        require(isinstance(source_hashes, dict), "Actual complete source map")
        require(isinstance(computations, str) and computations.startswith("/"),
                "Actual absolute computations source directory")
        self.sources = dict(source_hashes)
        self.computations = computations.rstrip("/")
        self.rows = {name: NamedRows(name) for name in sorted(FAMILIES)}

    def put(self, family, original, display=None):
        return self.rows[family].add(original, display)

    def source_identity(self, value):
        if not isinstance(value, dict) or set(value) != {"file", "bytes", "sha256"}:
            return value
        path, size, digest = value["file"], value["bytes"], value["sha256"]
        if not isinstance(path, str) or type(size) is not int or size < 0:
            return value
        name = path.rsplit("/", 1)[-1]
        if path not in (name, self.computations + "/" + name):
            return value
        if not isinstance(digest, str) or self.sources.get(name) != digest:
            return value
        # Full original path/size/SHA, not a digest-only external reference.
        return self.put("verified_source_identity", value)

    def source_binding(self, value):
        if not isinstance(value, dict) or not isinstance(value.get("schema"), str) or \
                value["schema"] not in BINDING_SCHEMAS:
            return value
        result = {}
        for name, item in value.items():
            if name in ANCESTOR_BINDING_KEYS:
                result[name] = self.source_binding(item)
            elif name in BINDING_IDENTITY_KEYS:
                result[name] = self.source_identity(item)
            elif name in BINDING_IDENTITY_LISTS and isinstance(item, list):
                result[name] = [self.source_identity(v) for v in item]
            elif name == "run" and isinstance(item, dict):
                result[name] = self.put("source_run_context", item)
            else:
                # Includes all unknown fields and all actual compile returns.
                result[name] = item
        return self.put("source_binding", value, result)

    def literal_sha_list(self, values):
        if not isinstance(values, list) or not all(
                isinstance(v, str) and len(v) == 64 and
                all(c in "0123456789abcdef" for c in v) for v in values):
            return values
        # This one fixed source column only; no arbitrary string dictionary.
        return [self.put("source_literal_sha256", {"sha256": value})
                for value in values]

    def source_scope(self, value):
        """Only an original complete source-preparation necessary selection."""
        if isinstance(value, list):
            return [self.source_scope(item) for item in value]
        if not isinstance(value, dict):
            return value
        observed_schema = value.get("schema")
        schema = observed_schema if isinstance(observed_schema, str) else None
        if schema in BINDING_SCHEMAS:
            return self.source_binding(value)
        identity = self.source_identity(value)
        if identity is not value:
            return identity
        result = {}
        for name, item in value.items():
            if schema in SOURCE_CATALOGUE_SCHEMAS and name == "literal_sha256_values":
                result[name] = self.literal_sha_list(item)
            else:
                result[name] = self.source_scope(item)
        if schema in SOURCE_CATALOGUE_SCHEMAS:
            return self.put("source_identity_catalogue", value, result)
        if schema in SOURCE_INVENTORY_SCHEMAS:
            return self.put("source_inventory_rows", value, result)
        if schema in SOURCE_CHANGE_SCHEMAS:
            return self.put("source_literal_change_rows", value, result)
        return result

    def statistics_section(self, field, value):
        expected, prefix, paths = STAT_SECTIONS[field]
        if not isinstance(value, dict) or value.get("schema") != expected:
            return value
        result = {}
        for name, item in value.items():
            if name in paths and isinstance(item, dict):
                path = dict(item)
                if isinstance(item.get("last"), dict):
                    path["last"] = self.put(prefix + "_last", item["last"])
                result[name] = self.put(prefix + "_path", item, path)
            else:
                result[name] = item
        return self.put(prefix + "_statistics", value, result)

    def root_record(self, family, value):
        if not isinstance(value, dict):
            return value
        if family == "root_statistics":
            result = dict(value)
            for name in STAT_SECTIONS:
                if name in value:
                    result[name] = self.statistics_section(name, value[name])
            return result
        if family in ("root_cache_compile_binding",
                "root_finite_word_cache_source_preparation",
                "root_finite_word_cache_source_binding",
                "root_finite_word_cache_compiler_installation"):
            return self.source_binding(value)
        if family == "owner_compilation":
            result = {}
            for name, item in value.items():
                if name == "root_finite_word_cache_compilation_source_binding":
                    result[name] = self.source_binding(item)
                else:
                    # Generated binary/include receipts do not match source map.
                    result[name] = self.source_identity(item)
            return self.put("root_owner_compilation", value, result)
        if family == "physical_source_input_binding":
            # This is a named source receipt only. Unknown values are retained.
            result = {name: self.source_identity(item) for name, item in value.items()}
            return self.put("root_physical_source_input_binding", value, result)
        # R535 finite-word rows remain in the existing original column table.
        return value

    def describe(self, domain):
        nonempty = {name: rows.describe() for name, rows in self.rows.items()
                    if rows.displays}
        return dict(schema=SCHEMA, domain=domain, reference_member=MARKER,
            complete_named_tables=nonempty,
            original_member_order_and_complete_unknown_columns_retained=True,
            absent_null_bool_int_float_negative_zero_distinguished=True,
            nonfinite_values_never_shared_or_converted_here=True,
            numerical_array_encoding_or_new_scientific_selection=False,
            external_raw_reconstruction_by_hash=False,
            inverse="Expand only this relation's marker references using complete_named_tables; reconstruct each row in its recorded column order. For source_literal_sha256 used in the named literal_sha256_values column, take the reconstructed row's sha256 string. Other families reconstruct their entire original dictionary. Then apply the unchanged ancestor necessary-table inverse where present.",
            scientific_success_or_size_fit_inferred=False)


def source_necessary_relation(value, source_hashes, computations):
    """Return the same complete source selection, with explicitly named relations."""
    require_public_actions()
    if contains_marker(value):
        return value, dict(schema=SCHEMA, applied=False,
            reason="Reserved marker already present; complete input left literal")
    rel = Relations(source_hashes, computations)
    selected = rel.source_scope(value)
    report = rel.describe("complete-original-source-preparation-necessary")
    report["applied"] = True
    return selected, report


def root_catalogue_relation(values, source_hashes, computations):
    """Factor only the eight original RootWordMetadata catalogue families."""
    require_public_actions()
    require(isinstance(values, dict), "Original named RootWordMetadata catalogues")
    if contains_marker(values):
        return values, dict(schema=SCHEMA, applied=False,
            reason="Reserved marker already present; complete input left literal")
    rel = Relations(source_hashes, computations)
    result = {}
    for name, records in values.items():
        if name in ROOT_CATALOGUE_NAMES and isinstance(records, list):
            result[name] = [rel.root_record(name, value) for value in records]
        else:
            # A future unknown catalogue is retained in full and not reinterpreted.
            result[name] = records
    report = rel.describe("eight-original-root-word-metadata-catalogues")
    report["applied"] = True
    return result, report


def restore_relation(value, report):
    """Exact metadata inverse; no scientific function, file read or runtime gate."""
    require(report.get("schema") == SCHEMA, "Actual R588 relation schema")
    if report.get("applied") is False:
        return value
    require(report.get("applied") is True, "Explicit applied relation")
    tables = report["complete_named_tables"]
    rows = {}
    for family, table in tables.items():
        require(family in FAMILIES, "Explicit named table family")
        count = table["record_count"]
        require(type(count) is int and count >= 0, "Original record count")
        records = [None] * count
        for group in table["groups"]:
            columns = group["columns"]
            indices = group["original_record_indices"]
            values = group["column_values"]
            require(len(columns) == len(set(columns)) and len(columns) == len(values),
                    "Exactly the original ordered columns")
            for position, index in enumerate(indices):
                require(type(index) is int and 0 <= index < count and
                        records[index] is None, "Each original row index once")
                record = {}
                for key, col in zip(columns, values):
                    require(set(col) in ({"constant"}, {"original_values"}),
                            "Constant or every original column value")
                    if "constant" in col:
                        record[key] = col["constant"]
                    else:
                        require(len(col["original_values"]) == len(indices),
                                "Complete original column length")
                        record[key] = col["original_values"][position]
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
            ref = item[MARKER]
            require(isinstance(ref, list) and len(ref) == 2 and
                    isinstance(ref[0], str) and type(ref[1]) is int,
                    "Exact named metadata reference")
            family, index = ref
            require(family in rows and 0 <= index < len(rows[family]),
                    "Reference points to a present complete row")
            key = (family, index)
            if key in memo:
                return memo[key]
            require(key not in active, "Finite acyclic source/statistics relation")
            active.add(key)
            restored = expand(rows[family][index])
            active.remove(key)
            if family == "source_literal_sha256":
                require(set(restored) == {"sha256"}, "Named literal SHA string row")
                restored = restored["sha256"]
            memo[key] = restored
            return restored
        return {name: expand(v) for name, v in item.items()}
    return expand(value)
