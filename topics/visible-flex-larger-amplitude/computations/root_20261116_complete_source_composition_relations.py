#!/usr/bin/env python3
"""R544: lossless, named source-addition rows for a complete composition record.

This is JSON metadata transport only. It does not import scientific modules,
evaluate fields, change scientific selection, omit a source change, or split
one necessary body. Every unknown or differently shaped change stays literal.
The actual original full record remains on the runner under its own identity.
Author: OpenAI / ChatGPT exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
import hashlib
import json
import re

SCHEMA = "R544-complete-source-composition-addition-relations-v1"
MEMBER = "exact_member_changes"
PREFIX = "/source_sha256/"
ROW_KEYS = ("path", "before_present", "after_present", "after")
COLUMNS = ("original_change_index", "source_basename", "after_sha256")
SHA = re.compile(r"[0-9a-f]{64}\Z")
NAME = re.compile(r"[A-Za-z0-9_.-]+\Z")


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def identity(raw):
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def source_addition(row):
    """Recognize only the original producer's complete source-pin addition."""
    if (not isinstance(row, dict) or set(row) != set(ROW_KEYS)
            or row["before_present"] is not False
            or row["after_present"] is not True
            or not isinstance(row["path"], str)
            or not row["path"].startswith(PREFIX)
            or not isinstance(row["after"], str)
            or SHA.fullmatch(row["after"]) is None):
        return None
    name = row["path"][len(PREFIX):]
    # Existing source names use this direct ASCII basename grammar. JSON-pointer
    # escapes, path separators, unusual names and unknown fields remain literal.
    if (not name or name in (".", "..") or NAME.fullmatch(name) is None
            or "/" in name or "~" in name):
        return None
    return name, row["after"]


def compose(value):
    """Return a strictly smaller complete relation, or the original object.

    The whole comparison includes every table label, original-key-order word
    and original-record identity. The comparison never authorizes a scientific
    result and never promises that either body is below the caller's 90000 B.
    """
    original = canonical(value)
    if (not isinstance(value, dict) or MEMBER not in value
            or not isinstance(value[MEMBER], list)):
        return copy.deepcopy(value)
    additions, literal, addition_order = [], [], None
    for index, row in enumerate(value[MEMBER]):
        found = source_addition(row)
        if found is None or (addition_order is not None and tuple(row) != addition_order):
            literal.append(copy.deepcopy(row))
        else:
            if addition_order is None:
                addition_order = tuple(row)
            additions.append([index, found[0], found[1]])
    if not additions:
        return copy.deepcopy(value)
    rest = copy.deepcopy(value)
    del rest[MEMBER]
    candidate = dict(
        schema=SCHEMA,
        original_canonical_record=identity(original),
        original_member_order=list(value),
        record_except_member_changes=rest,
        exact_member_change_relations=dict(
            member=MEMBER,
            original_change_count=len(value[MEMBER]),
            source_dictionary="source_sha256",
            source_addition_columns=list(COLUMNS),
            source_addition_original_member_order=list(addition_order),
            source_additions=additions,
            other_changes_in_original_order=literal,
        ),
    )
    if len(canonical(candidate)) < len(original):
        return candidate
    return copy.deepcopy(value)


def expand(value):
    """Explicit inverse for this fixed semantic relation; not an execution gate.

    It restores dictionary member order as well as key presence, list order,
    literal types, every source addition, and all unrecognized original rows.
    The scientific caller never invokes this inverse as an added comparison.
    """
    if not isinstance(value, dict) or value.get("schema") != SCHEMA:
        return copy.deepcopy(value)
    required = {
        "schema", "original_canonical_record", "original_member_order",
        "record_except_member_changes", "exact_member_change_relations",
    }
    if set(value) != required:
        raise ValueError("Unknown complete-composition relation member")
    rel = value["exact_member_change_relations"]
    if (not isinstance(rel, dict) or set(rel) != {
            "member", "original_change_count", "source_dictionary",
            "source_addition_columns", "source_addition_original_member_order",
            "source_additions", "other_changes_in_original_order",
        } or rel["member"] != MEMBER or rel["source_dictionary"] != "source_sha256"
            or rel["source_addition_columns"] != list(COLUMNS)):
        raise ValueError("Unknown source-addition role/columns")
    addition_order = rel["source_addition_original_member_order"]
    if (not isinstance(addition_order, list) or len(addition_order) != len(ROW_KEYS)
            or any(not isinstance(key, str) for key in addition_order)
            or set(addition_order) != set(ROW_KEYS)):
        raise ValueError("The complete four source-addition members differ")
    count = rel["original_change_count"]
    additions = rel["source_additions"]
    literal = rel["other_changes_in_original_order"]
    if (type(count) is not int or count < 0 or not isinstance(additions, list)
            or not isinstance(literal, list) or len(additions) + len(literal) != count):
        raise ValueError("Incomplete original member-change universe")
    positions, previous = {}, -1
    for row in additions:
        if (not isinstance(row, list) or len(row) != 3
                or type(row[0]) is not int or not previous < row[0] < count
                or not isinstance(row[1], str) or not row[1]
                or row[1] in (".", "..") or NAME.fullmatch(row[1]) is None
                or not isinstance(row[2], str) or SHA.fullmatch(row[2]) is None):
            raise ValueError("Invalid actual source-addition row")
        index, name, after = row
        complete = dict(path=PREFIX + name, before_present=False,
            after_present=True, after=after)
        positions[index] = {key: complete[key] for key in addition_order}
        previous = index
    changes, next_literal = [], 0
    for index in range(count):
        if index in positions:
            changes.append(positions[index])
        else:
            changes.append(copy.deepcopy(literal[next_literal]))
            next_literal += 1
    rest = value["record_except_member_changes"]
    order = value["original_member_order"]
    if (not isinstance(rest, dict) or MEMBER in rest or not isinstance(order, list)
            or any(not isinstance(key, str) for key in order)
            or len(order) != len(set(order))
            or set(order) != set(rest) | {MEMBER}):
        raise ValueError("The original complete-record members are not preserved")
    restored = {
        key: changes if key == MEMBER else copy.deepcopy(rest[key])
        for key in order
    }
    if identity(canonical(restored)) != value["original_canonical_record"]:
        raise ValueError("The represented original canonical record differs")
    return restored


def breakdown(value):
    """Named selected-metadata byte counts only, never a recovery encoding."""
    if not isinstance(value, dict):
        return dict(whole_selected_body=identity(canonical(value)))
    result = dict(whole_selected_body=identity(canonical(value)),
        body_is_one_complete_original_or_named_relation=True)
    if value.get("schema") == SCHEMA:
        rel = value["exact_member_change_relations"]
        result.update(
            original_canonical_record=value["original_canonical_record"],
            source_addition_count=len(rel["source_additions"]),
            literal_change_count=len(rel["other_changes_in_original_order"]),
            source_additions_bytes=len(canonical(rel["source_additions"])),
            literal_changes_bytes=len(canonical(rel["other_changes_in_original_order"])),
            remaining_complete_record_bytes=len(canonical(value["record_except_member_changes"])),
        )
    elif isinstance(value.get(MEMBER), list):
        result.update(original_change_count=len(value[MEMBER]),
            complete_member_changes_bytes=len(canonical(value[MEMBER])))
    return result
