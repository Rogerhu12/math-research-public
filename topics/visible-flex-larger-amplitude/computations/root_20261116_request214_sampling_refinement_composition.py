#!/usr/bin/env python3
"""Compose request214 from the byte-bound original205,209,212 contracts.

Standard-library metadata only. The complete original request is byte-bound;
the sole scientific-control difference is sample_inverse_depth 24 -> 2.
Two independent necessary readers retain original point-inverse pending keys.
The same depth2 is inherited by the actual R456 and R462 successors; all
original209 scientific roles, caps, ownership and fifteen generated views stay.
The original namespace/owner/deadline setup is moved here without a second clock.
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
import time

REPOSITORY = "Rogerhu12/math-research-public"
ENTRY = "root_20261116_request214_sampling_refinement_composition.py"
SCHEMA = "request214-original205-and209-explicit-shallow-refinement-composition-v1"
REQUEST_SCHEMA = "public-actual202-shallow-inverse-incremental-M-joint-refinement-and-displays-request-v1"
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
REFINEMENT_ORIGINAL = {
    "file": "topics/visible-flex-larger-amplitude/notes/current-C-actual202-incremental-M-refinement209-request.json",
    "bytes": 36220,
    "sha256": "aaf74021bbd952b24a3ba3d45b0cbbd1df070bf9866c79f6925808c836a74009",
}
REFINEMENT_WORKFLOW = {
    "file": ".github/workflows/visible-current-C-actual202-incremental-M-refinement209.yml",
    "bytes": 96476,
    "sha256": "1c53b3c27ab531b99308150a7213e15d17717c57cff846b1dbffe0ffc9e5d65a",
}
SHALLOW_ORIGINAL = {
    "file": "topics/visible-flex-larger-amplitude/notes/current-C-actual202-shallow-inverse-closed212-request.json",
    "bytes": 9965,
    "sha256": "8803750dbb21bcc24e0809e7bdc4389c567de9b8a10532d52b42b2f7a7ee30bf",
}
SHALLOW_WORKFLOW = {
    "file": ".github/workflows/visible-current-C-actual202-shallow-inverse-closed212.yml",
    "bytes": 99644,
    "sha256": "d1022e74a6217d582f08692b2458bb4d20a3a5dec61ba4dc88907a27e13c3cc0",
}
CHAIN_SOURCES = (
    "geometry_20261116_request214_owned_roles.py",
    "geometry_20261116_request214_joint_refinement.py",
    "root_20261116_request214_refinement_necessary.py",
)
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
DERIVED = "request214-derived205-dispatch.json"
RECEIPT = "request214-composition.json"
MARKER = "request214-composition-readback-complete.json"
HERE = Path(__file__).resolve().parent
OUTER_FILE = "topics/visible-flex-larger-amplitude/notes/current-C-actual202-shallow-inverse-incremental-M-refinement214-request.json"


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


def bind_refinement_ancestry(repo, outer, original):
    """Byte-bind both published designs and keep the actual209 science plan."""
    pairs = (("original209_subcontract", REFINEMENT_ORIGINAL),
        ("original209_workflow", REFINEMENT_WORKFLOW),
        ("original212_subcontract", SHALLOW_ORIGINAL),
        ("original212_workflow", SHALLOW_WORKFLOW))
    raw = {}
    for key, item in pairs:
        require(outer.get(key) == item, "Complete published ancestry differs: " + key)
        raw[key] = (repo / item["file"]).read_bytes()
        require(match(raw[key], item), "Published ancestry bytes differ: " + key)
    parent = json.loads(raw["original209_subcontract"])
    shallow = json.loads(raw["original212_subcontract"])
    require(parent.get("request_number") == 209 and shallow.get("request_number") == 212,
        "Bind both original request identities without relabelling either old run")
    require(shallow.get("scientific_control_change") == outer["scientific_control_change"],
        "Use the same explicit shallow-inverse work allocation as published212")
    for key in ("original205_subcontract", "original205_workflow", "execution", "refinement_work",
            "source_view_generation", "witness_families", "mode_extension_proof",
            "held_source_contract", "additional_exact_source_contracts", "display_families",
            "actual_level_families", "reviewed_README_blobs"):
        require(outer[key] == parent[key], "An original209 scientific/source/resource member changed: " + key)
    require(set(outer["roles"]) == set(parent["roles"]), "Keep all original209 actual roles")
    for role, item in parent["roles"].items():
        if role not in ("owner", "runner", "reader"):
            require(outer["roles"][role] == item, "A frozen scientific role changed: " + role)
    old = parent["additional_source_sha256"]
    new = outer["additional_source_sha256"]
    require(all(new.get(name) == value for name, value in old.items())
        and set(new) - set(old) == set(CHAIN_SOURCES),
        "Retain every original209 source and add only the three actual214 caller/readers")
    old_union = dict(original["source_sha256"])
    for name, value in old.items():
        require(name not in old_union or old_union[name] == value,
            "Original209 ancestry contains a conflicting original205 source")
        old_union[name] = value
    require(len(old_union) == parent["published_source_count"] == 245
        and parent["generated_source_count"] == 15 and parent["complete_source_count"] == 260,
        "Keep the full actual245 plus fifteen generated original209 source universe")
    return parent


def compose(request_path, base, comp, expected_outer=None):
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
    checkout = repo / OUTER_FILE
    require(request_path in (checkout, base / "refinement214-request.json")
        and request_path.is_file() and checkout.is_file(),
        "Use the actual checkout request or its sole explicit same-job refinement copy")
    outer_raw = request_path.read_bytes()
    require(outer_raw == checkout.read_bytes(),
        "The retained same-job outer request must equal the full original checkout bytes")
    if expected_outer is not None:
        require(sha(outer_raw) == expected_outer, "The actual214 outer request bytes differ")
    outer = json.loads(outer_raw)
    require(outer.get("schema") == REQUEST_SCHEMA and outer.get("request_number") == 214
        and outer.get("repository") == REPOSITORY, "Bind the independent request214")
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
    refinement = bind_refinement_ancestry(repo, outer, original)
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
        ".github/workflows/visible-current-C-actual202-shallow-inverse-incremental-M-refinement214.yml",
        "Bind this independent214 workflow")
    outer_identity = {"file": OUTER_FILE,
        "bytes": len(outer_raw), "sha256": sha(outer_raw)}
    derived = copy.deepcopy(original)
    derived["native_sampling"]["parameters"]["sample_inverse_depth"] = 2
    derived["source_sha256"].update({name: item["sha256"] for name, item in sources.items()})
    derived["source_count"] = len(derived["source_sha256"])
    derived["current_BVP_readout"].update(new_reader)
    derived["workflow"] = outer["workflow"]
    derived["explicit214_composition"] = {
        "schema": SCHEMA + "-declared-experiment",
        "outer_request": outer_identity, "actual_request_number": 214,
        "original205": ORIGINAL, "embedded_runtime_schema": ORIGINAL_SCHEMA,
        "embedded_request_number": 205,
        "embedded_index_is_source_contract_not_old_run_or_unchanged_dispatch": True,
        "actual_run_id": os.environ["GITHUB_RUN_ID"],
        "actual_source_commit": os.environ["GITHUB_SHA"],
        "scientific_control_change": outer["scientific_control_change"],
        "new_readback_sources": sources,
        "original209_refinement_contract": REFINEMENT_ORIGINAL,
        "original212_shallow_contract": SHALLOW_ORIGINAL,
        "inverse_depth2_inherited_by_level0_level1_and_level2_sampling": True,
        "all_three_levels_keep_value_bits32_as_work_only_and_complete_candidate_cover": True,
        "old_actual203_or205_raw_or_acceptance_reused": False,
        "all_physical_points_candidates_far_modes_and_original_gates_preserved": True,
        "same_sampler_source_new_work_allocation_and_fresh_numeric_words": True,
    }
    difference = changes(original, derived)
    allowed = {"/native_sampling/parameters/sample_inverse_depth", "/source_count", "/workflow",
        "/explicit214_composition"}
    allowed.update("/source_sha256/" + name for name in ADDITIONAL)
    allowed.update("/current_BVP_readout/" + key for key in ("file", "bytes", "sha256", "schema"))
    require({item["path"] for item in difference}.issubset(allowed),
        "An undeclared original205 contract member changed")
    restored = copy.deepcopy(derived)
    restored["native_sampling"]["parameters"]["sample_inverse_depth"] = 24
    restored["current_BVP_readout"] = original["current_BVP_readout"]
    restored["workflow"] = original["workflow"]
    restored.pop("explicit214_composition")
    for name in ADDITIONAL:
        restored["source_sha256"].pop(name)
    restored["source_count"] = original["source_count"]
    require(restored == original and derived["source_count"] == 157,
        "Every original205 mathematical/source/input/resource member must be retained")
    combined = dict(derived["source_sha256"])
    for name, value in outer["additional_source_sha256"].items():
        require(name not in combined or combined[name] == value,
            "No original or new scientific source may be overwritten")
        combined[name] = value
    generated = refinement["source_view_generation"]["expected_generated_sources"]
    require(len(combined) == outer["published_source_count"] == 251
        and len(generated) == outer["generated_source_count"] == 15
        and len(combined) + len(generated) == outer["complete_source_count"] == 266
        and not set(combined).intersection(generated),
        "Bind the actual251 published and fifteen separately generated source sets")
    raw = canonical(derived)
    receipt = {
        "schema": SCHEMA, "repository": REPOSITORY,
        "run_id": os.environ["GITHUB_RUN_ID"], "source_commit": os.environ["GITHUB_SHA"],
        "source": sources[ENTRY], "actual_computations": str(comp),
        "outer_request": outer_identity, "original205_request": ORIGINAL,
        "original205_workflow": ORIGINAL_WORKFLOW,
        "original209_request": REFINEMENT_ORIGINAL,
        "original209_workflow": REFINEMENT_WORKFLOW,
        "original212_request": SHALLOW_ORIGINAL,
        "original212_workflow": SHALLOW_WORKFLOW,
        "actual_published_source_count": len(combined),
        "actual_generated_source_count": len(generated),
        "actual_complete_source_count": len(combined) + len(generated),
        "original209_mathematical_sources_and_all_role_caps_preserved": True,
        "inverse_depth2_inherited_by_all_three_actual_sampling_levels": True,
        "actual_three_level_sampling_not_completed_by_source_composition": True,
        "derived_dispatch": {"file": DERIVED, "bytes": len(raw), "sha256": sha(raw)},
        "original_source_count": 154, "additional_metadata_source_count": 3,
        "derived_source_count": 157, "actual_new_metadata_sources": sources,
        "exact_member_changes": difference,
        "all_other_original205_members_equal": True,
        "fresh_all112_far_and_all_physical_points_required": True,
        "work_resolution_is_not_a_scientific_acceptance_gate": True,
        "completion_or_smaller_error_or_sufficient_work_capacity_promised": False,
        "scientific_module_imported_or_scientific_value_recomputed": False,
        "one_original_namespace_clock_created_only_by_initialize": True,
        "composition_verification_and_readback_do_not_create_or_restart_a_clock": True,
    }
    return base, raw, receipt


def write_new(path, raw):
    with path.open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


def verify_runtime(request_path, expected_outer, base, comp, *, require_dispatch=True):
    base, raw, value = compose(request_path, base, comp, expected_outer)
    record = canonical(value)
    require((base / DERIVED).read_bytes() == raw and (base / RECEIPT).read_bytes() == record,
        "The actual derived contract or complete source-composition receipt differs")
    if require_dispatch:
        require((base / "dispatch-request.json").read_bytes() == raw,
            "The science dispatch is not the actual explicitly derived214 contract")
    return json.loads(raw), identity(base / DERIVED), identity(base / RECEIPT)


def initialize(args):
    """The original namespace/owner/deadline setup, once, before any science."""
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY, "Use this public Actions job")
    repo = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    base, comp = args.base.resolve(), args.computations.resolve()
    require(base == temporary / NAMESPACE and comp == HERE
        and comp == repo / "topics/visible-flex-larger-amplitude/computations",
        "Use the sole original205 namespace and actual computations directory")
    require(sha(args.request.read_bytes()) == args.request_sha256,
        "Bind the actual214 outer bytes before creating its namespace")
    base.mkdir(exist_ok=False)
    base, raw, value = compose(args.request, base, comp, args.request_sha256)
    write_new(base / DERIVED, raw)
    write_new(base / RECEIPT, canonical(value))
    request = json.loads(raw)
    recipe_raw = (comp / "current-C-riccati-full453-physical-DN179-recipe.json").read_bytes()
    require(sha(recipe_raw) == request["current_BVP_recipe"]["sha256"]
        == "d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811",
        "Bind the actual original BVP recipe before creating its single resource clock")
    policy = json.loads(recipe_raw)["execution"]
    require(policy["maximum_elapsed_science_seconds_from_namespace"] == 18900
        and policy["readback_reserve_seconds"] == 2700, "Keep the original namespace resource plan")
    owner = request["execution"]["owned_process_helper"]
    owner_raw = (comp / owner["file"]).read_bytes()
    require(match(owner_raw, owner) and len(owner_raw) == 14815
        and sha(owner_raw) == "f779c6a296b8579469dffb27c46642d5d5aaffc08d53a027537d2ddb23ee9357",
        "Use the unchanged original205 owner and its actual seven role scopes")
    # This is the original Actions-only syntax check moved out of YAML.
    # Source authoring does not execute this branch or import project science.
    import ast
    compile(ast.parse(owner_raw, filename="request205_owned_process.py"),
        "request205_owned_process.py", "exec")
    write_new(base / "request205_owned_process.py", owner_raw)
    deadline = dict(schema="request205-owned-job-science-deadline-v1",
        repository=os.environ["GITHUB_REPOSITORY"], run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], request_sha256=sha(raw),
        template_recipe_sha256=sha(recipe_raw), namespace_created_unix_seconds=time.time(),
        science_seconds_from_namespace=18900, readback_reserve_seconds=2700,
        job_timeout_minutes=360, resource_deadline_not_a_scientific_gate=True,
        scope="Startup resource plan before BVP; original BVP launcher enforces its actual namespace deadline",
        no_global_absolute_kill_clock_for_prior_stages=True,
        original_sampling_phase_clocks_exclude_binding_and_setup=True)
    write_new(base / "job-science-deadline.json", canonical(deadline))
    print(json.dumps(dict(event="request214_actual_original_namespace_resource_plan", **deadline),
        sort_keys=True), flush=True)
    with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as stream:
        stream.write("VISIBLE_BASE=" + str(base) + "\n")
        stream.write("VISIBLE_COMPUTATIONS=" + str(comp) + "\n")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("initialize", "prepare", "verify", "readback"))
    for name in ("request", "base", "computations"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--request-sha256", required=True)
    args = parser.parse_args(argv)
    if args.command == "initialize":
        return initialize(args)
    base, raw, value = compose(args.request, args.base, args.computations, args.request_sha256)
    record = canonical(value)
    if args.command == "prepare":
        require(not (base / DERIVED).exists() and not (base / RECEIPT).exists(),
            "Fresh composition files are required; never overwrite an actual receipt")
        write_new(base / DERIVED, raw)
        write_new(base / RECEIPT, record)
    else:
        verify_runtime(args.request, args.request_sha256, base, args.computations,
            require_dispatch=args.command == "readback")
    if args.command == "readback":
        require(len(record) <= 90000,
            "The independent necessary source scope exceeds its original explicit transport bound")
        print("BEGIN_REQUEST214_SOURCE_COMPOSITION_NECESSARY", flush=True)
        print(record.decode("utf-8"), end="", flush=True)
        print("END_REQUEST214_SOURCE_COMPOSITION_NECESSARY", flush=True)
        marker = {"schema": SCHEMA + "-readback-complete", "repository": REPOSITORY,
            "run_id": os.environ["GITHUB_RUN_ID"], "source_commit": os.environ["GITHUB_SHA"],
            "complete": True, "necessary_summary": {"bytes": len(record), "sha256": sha(record)},
            "derived_dispatch": value["derived_dispatch"], "outer_request": value["outer_request"],
            "only_immutable_source_composition_read_no_scientific_success_inferred": True}
        write_new(base / MARKER, canonical(marker))
    print(json.dumps({"event": "request214_explicit_sampling_refinement_composition_" + args.command,
        "repository": REPOSITORY, "run_id": os.environ["GITHUB_RUN_ID"],
        "source_commit": os.environ["GITHUB_SHA"],
        "receipt": identity(base / RECEIPT), "outer_request": value["outer_request"],
        "derived_dispatch": value["derived_dispatch"], "original205_request": ORIGINAL,
        "original209_request": REFINEMENT_ORIGINAL, "original212_request": SHALLOW_ORIGINAL,
        "original_inverse_work_depth": 24, "actual_all_three_levels_inverse_work_depth": 2,
        "source_counts": {"original205": 154, "derived205": 157,
            "all_published": 251, "generated": 15, "all_runtime": 266},
        "all_other_original205_members_equal": True, "scientific_success_not_inferred": True},
        ensure_ascii=False, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
