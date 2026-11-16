#!/usr/bin/env python3
"""Compose request212's explicit shallow-inverse experiment from original205.

Standard-library metadata only. The complete original request is byte-bound;
the sole scientific-control difference is sample_inverse_depth 24 -> 2.
Two independent necessary readers retain original point-inverse pending keys.
All original scientific sources, raw inputs, budgets and acceptance rules stay
bound. The derived runtime contract keeps the actual original205 schema/index
required by the unchanged components; its bytes are never labelled original205.
Author: AI, 2026-11-16.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys

REPOSITORY = "Rogerhu12/math-research-public"
ENTRY = "root_20261116_request212_sampling_work_composition.py"
SCHEMA = "request212-original205-explicit-sampling-work-composition-v1"
REQUEST_SCHEMA = "public-actual202-shallow-inverse-complete-closed212-request-v1"
ORIGINAL_SCHEMA = "public-actual202-accurate-ten450-closed-geometry-request-v1"
NAMESPACE = "visible-current-C-actual202-ten450-closed-geometry205"
ORIGINAL = {
    "file": "topics/visible-flex-larger-amplitude/notes/current-C-actual202-accurate-ten-closed-geometry205-request.json",
    "bytes": 97406,
    "sha256": "06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4",
}
ORIGINAL_WORKFLOW = {
    "file": ".github/workflows/visible-current-C-actual202-accurate-ten-closed-geometry205.yml",
    "bytes": 95760,
    "sha256": "726d97e1aada5d34ddfa949753ce59c6909122d3de8c39bd5a2160fdb8712c36",
}
ORIGINAL_READER = {
    "file": "root_20261116_actual202_accurate_ten_two_phase_necessary_readout.py",
    "bytes": 29882,
    "sha256": "80c26207dea0d393a102dabba9f1e5ed9580460cc40876d2668975ae9499af1f",
    "schema": "actual202-accurate-ten-current-C-live-full453-and-frozen450-necessary-readback-v1",
}
BASE_READER = "root_20261116_current_C_sampling_scope_necessary_readout.py"
TWO_PHASE_READER = "root_20261116_actual202_sampling_scope_two_phase_necessary_readout.py"
TWO_PHASE_SCHEMA = "actual202-complete-sampling-scope-ten-two-phase-necessary-readback-v1"
ADDITIONAL = (ENTRY, BASE_READER, TWO_PHASE_READER)
SAMPLER = "geometry_20261115_current_C_pruefer_joint_radial_sampling.py"
SAMPLER_SHA = "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4"
DERIVED = "request212-derived205-dispatch.json"
RECEIPT = "request212-composition.json"
MARKER = "request212-composition-readback-complete.json"
HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def identity(path):
    path = Path(path)
    raw = path.read_bytes()
    return {"file": path.name, "bytes": len(raw), "sha256": sha(raw)}


def match(raw, item):
    return len(raw) == item["bytes"] and sha(raw) == item["sha256"]


def source_identity(comp, item):
    name = item["file"]
    require(isinstance(name, str) and PurePosixPath(name).name == name,
        "A direct actual computations basename is required")
    require(type(item["bytes"]) is int and item["bytes"] > 0
        and re.fullmatch(r"[0-9a-f]{64}", item["sha256"]) is not None,
        "Complete actual source identity is required")
    path = comp / name
    require(path.resolve().parent == comp and not path.is_symlink(),
        "Bind the actual HERE source, not a redirected metadata label")
    raw = path.read_bytes()
    require(match(raw, item), "Actual independent metadata source differs: " + name)
    return {"file": name, "bytes": len(raw), "sha256": sha(raw)}


def changes(before, after, path=""):
    """JSON member comparison, never a scientific numerical comparison."""
    if isinstance(before, dict) and isinstance(after, dict):
        result = []
        for key in sorted(set(before) | set(after)):
            location = path + "/" + key.replace("~", "~0").replace("/", "~1")
            if key not in before:
                result.append({"path": location, "before_present": False,
                    "after_present": True, "after": after[key]})
            elif key not in after:
                result.append({"path": location, "before_present": True,
                    "before": before[key], "after_present": False})
            else:
                result.extend(changes(before[key], after[key], location))
        return result
    if type(before) is type(after) and before == after:
        return []
    return [{"path": path, "before_present": True, "before": before,
        "after_present": True, "after": after}]


def compose(request_path, base, comp):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "This original source composition belongs to the public Actions job")
    repo = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    tmp = Path(os.environ["RUNNER_TEMP"]).resolve()
    request_path, base, comp = request_path.resolve(), base.resolve(), comp.resolve()
    require(comp == HERE and comp == repo / "topics/visible-flex-larger-amplitude/computations",
        "Use the helper and all independent readers in the actual public computations HERE")
    require(base == tmp / NAMESPACE and base.is_dir() and not base.is_symlink(),
        "Use this job's original205 namespace without restarting its clock")
    require(repo in request_path.parents and request_path.is_file(),
        "The explicit small outer212 request must be an actual checkout file")
    outer_raw = request_path.read_bytes()
    outer = json.loads(outer_raw)
    require(outer.get("schema") == REQUEST_SCHEMA and outer.get("request_number") == 212
        and outer.get("repository") == REPOSITORY, "Bind the independent request212")
    require(outer.get("original205_subcontract") == ORIGINAL
        and outer.get("original205_workflow") == ORIGINAL_WORKFLOW,
        "Bind the complete published205 request and workflow byte identities")
    require(outer.get("scientific_control_change") == {
        "path": "/native_sampling/parameters/sample_inverse_depth",
        "original": 24, "requested": 2},
        "Only the explicit inverse work depth may change")
    baseline_raw = (repo / ORIGINAL["file"]).read_bytes()
    workflow_raw = (repo / ORIGINAL_WORKFLOW["file"]).read_bytes()
    require(match(baseline_raw, ORIGINAL) and match(workflow_raw, ORIGINAL_WORKFLOW),
        "Original205 complete public bytes differ")
    original = json.loads(baseline_raw)
    require(original.get("schema") == ORIGINAL_SCHEMA and original.get("request_number") == 205,
        "The embedded205 runtime schema is required by its actual unchanged helpers")
    require(original["source_count"] == len(original["source_sha256"]) == 154,
        "Retain every original154 source pin")
    sampling = original["native_sampling"]
    require(sampling["file"] == SAMPLER and sampling["sha256"] == SAMPLER_SHA,
        "Use the original complete C/112/far/physical-grid sampler")
    require(sampling["parameters"]["sample_inverse_depth"] == 24
        and sampling["parameters"]["sample_value_bits"] == 32
        and sampling["parameters"]["sample_max_nodes"] == 1000000,
        "Original sampling work controls differ")
    require({k: original["current_BVP_readout"][k] for k in ORIGINAL_READER} == ORIGINAL_READER,
        "Bind the actual205 two-phase reader ancestry")
    declared = outer.get("metadata_sources")
    require(isinstance(declared, dict) and set(declared) == set(ADDITIONAL),
        "Use exactly the composition helper and two new necessary readers")
    sources = {}
    for name in ADDITIONAL:
        require(declared[name]["file"] == name and name not in original["source_sha256"],
            "New metadata names may not overwrite original scientific or reader sources")
        sources[name] = source_identity(comp, declared[name])
    new_reader = outer.get("current_BVP_readout")
    require(isinstance(new_reader, dict) and set(new_reader) == {"file", "bytes", "sha256", "schema"}
        and {k: new_reader[k] for k in ("file", "bytes", "sha256")} == sources[TWO_PHASE_READER]
        and new_reader["schema"] == TWO_PHASE_SCHEMA,
        "The actual new two-phase reader and schema must be wired, not just receipted")
    require(outer.get("workflow") ==
        ".github/workflows/visible-current-C-actual202-shallow-inverse-closed212.yml",
        "Bind this independent212 workflow")
    outer_identity = {"file": str(request_path.relative_to(repo)),
        "bytes": len(outer_raw), "sha256": sha(outer_raw)}
    derived = copy.deepcopy(original)
    derived["native_sampling"]["parameters"]["sample_inverse_depth"] = 2
    derived["source_sha256"].update({name: item["sha256"] for name, item in sources.items()})
    derived["source_count"] = len(derived["source_sha256"])
    derived["current_BVP_readout"].update(new_reader)
    derived["workflow"] = outer["workflow"]
    derived["explicit212_composition"] = {
        "schema": SCHEMA + "-declared-experiment",
        "outer_request": outer_identity, "actual_request_number": 212,
        "original205": ORIGINAL, "embedded_runtime_schema": ORIGINAL_SCHEMA,
        "embedded_request_number": 205,
        "embedded_index_is_source_contract_not_old_run_or_unchanged_dispatch": True,
        "actual_run_id": os.environ["GITHUB_RUN_ID"],
        "actual_source_commit": os.environ["GITHUB_SHA"],
        "scientific_control_change": outer["scientific_control_change"],
        "new_readback_sources": sources,
        "old_actual203_or205_raw_or_acceptance_reused": False,
        "all_physical_points_candidates_far_modes_and_original_gates_preserved": True,
        "same_sampler_source_new_work_allocation_and_fresh_numeric_words": True,
    }
    difference = changes(original, derived)
    allowed = {"/native_sampling/parameters/sample_inverse_depth", "/source_count", "/workflow",
        "/explicit212_composition"}
    allowed.update("/source_sha256/" + name for name in ADDITIONAL)
    allowed.update("/current_BVP_readout/" + key for key in ("file", "bytes", "sha256", "schema"))
    require({item["path"] for item in difference}.issubset(allowed),
        "An undeclared original205 contract member changed")
    restored = copy.deepcopy(derived)
    restored["native_sampling"]["parameters"]["sample_inverse_depth"] = 24
    restored["current_BVP_readout"] = original["current_BVP_readout"]
    restored["workflow"] = original["workflow"]
    restored.pop("explicit212_composition")
    for name in ADDITIONAL:
        restored["source_sha256"].pop(name)
    restored["source_count"] = original["source_count"]
    require(restored == original and derived["source_count"] == 157,
        "Every original205 mathematical/source/input/resource member must be retained")
    raw = canonical(derived)
    receipt = {
        "schema": SCHEMA, "repository": REPOSITORY,
        "run_id": os.environ["GITHUB_RUN_ID"], "source_commit": os.environ["GITHUB_SHA"],
        "source": sources[ENTRY], "actual_computations": str(comp),
        "outer_request": outer_identity, "original205_request": ORIGINAL,
        "original205_workflow": ORIGINAL_WORKFLOW,
        "derived_dispatch": {"file": DERIVED, "bytes": len(raw), "sha256": sha(raw)},
        "original_source_count": 154, "additional_metadata_source_count": 3,
        "derived_source_count": 157, "actual_new_metadata_sources": sources,
        "exact_member_changes": difference,
        "all_other_original205_members_equal": True,
        "fresh_all112_far_and_all_physical_points_required": True,
        "work_resolution_is_not_a_scientific_acceptance_gate": True,
        "completion_or_smaller_error_or_sufficient_work_capacity_promised": False,
        "scientific_module_imported_or_scientific_value_recomputed": False,
        "original_clock_not_created_or_restarted_by_this_helper": True,
    }
    return base, raw, receipt


def write_new(path, raw):
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "verify", "readback"))
    for name in ("request", "base", "computations"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args(argv)
    base, raw, receipt = compose(args.request, args.base, args.computations)
    record = canonical(receipt)
    if args.command == "prepare":
        require(not (base / DERIVED).exists() and not (base / RECEIPT).exists(),
            "Fresh derived metadata files are required; do not overwrite an actual run receipt")
        write_new(base / DERIVED, raw)
        write_new(base / RECEIPT, record)
    else:
        require((base / DERIVED).read_bytes() == raw and (base / RECEIPT).read_bytes() == record,
            "The actual composed request or provenance differs before science")
    if args.command == "readback":
        require(len(record) <= 90000,
            "The independent composition necessary scope exceeds its explicit output bound")
        print("BEGIN_REQUEST212_SOURCE_COMPOSITION_NECESSARY", flush=True)
        print(record.decode("utf-8"), end="", flush=True)
        print("END_REQUEST212_SOURCE_COMPOSITION_NECESSARY", flush=True)
        marker = {"schema": SCHEMA + "-readback-complete", "repository": REPOSITORY,
            "run_id": os.environ["GITHUB_RUN_ID"], "source_commit": os.environ["GITHUB_SHA"],
            "complete": True, "necessary_summary": {"bytes": len(record), "sha256": sha(record)},
            "derived_dispatch": receipt["derived_dispatch"],
            "only_immutable_source_composition_read_no_scientific_success_inferred": True}
        write_new(base / MARKER, canonical(marker))
    print(json.dumps({"event": "request212_explicit_sampling_work_composition_" + args.command,
        "repository": REPOSITORY, "run_id": os.environ["GITHUB_RUN_ID"],
        "source_commit": os.environ["GITHUB_SHA"],
        "receipt": identity(base / RECEIPT), "outer_request": receipt["outer_request"],
        "derived_dispatch": receipt["derived_dispatch"], "original205_request": ORIGINAL,
        "original_inverse_work_depth": 24, "actual_inverse_work_depth": 2,
        "source_counts": {"original": 154, "metadata_additions": 3, "derived": 157},
        "all_other_original205_members_equal": True, "scientific_success_not_inferred": True},
        ensure_ascii=False, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
