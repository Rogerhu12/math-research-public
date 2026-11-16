#!/usr/bin/env python3
"""Request218: original216 science with explicit R494, R498 and R499 sources.

The original accurate C/ten candidate, depth2 work, full453 then frozen450,
R456 five-count refinement, complete old112/new-M union, all geometric callers,
and original acceptance/clock contracts remain. Complete source identities
register the finite-qualified zero-linear caller and complete gzip ledgers.
No old run, raw ledger, response, finite field or success is reused.
Author: OpenAI / ChatGPT amplitude agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import copy
import contextlib
import importlib.util
import traceback
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
ENTRY = "root_20261116_request218_sampling_refinement_composition.py"
SCHEMA = "request218-original216-zero-linear-gzip-refinement-composition-v1"
REQUEST_SCHEMA = "public-current-C-zero-linear-gzip-incremental-M-refinement-and-displays-request-v1"
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
    "geometry_20261116_request218_owned_roles.py",
    "geometry_20261116_request218_joint_refinement.py",
    "root_20261116_request218_refinement_necessary.py",
)
ORIGINAL_READER = {
    "file": "root_20261116_actual202_accurate_ten_two_phase_necessary_readout.py",
    "bytes": 29882,
    "sha256": "80c26207dea0d393a102dabba9f1e5ed9580460cc40876d2668975ae9499af1f",
    "schema": "actual202-accurate-ten-current-C-live-full453-and-frozen450-necessary-readback-v1",
}
BASE_READER = "root_20261116_current_C_gzip_sampling_scope_necessary_readout.py"
TWO_PHASE_READER = "root_20261116_actual202_zero_linear_gzip_two_phase_necessary_readout.py"
TWO_PHASE_SCHEMA = "R496-actual202-zero-linear-ten-two-phase-necessary-readback-v1"
RULE_READER = "root_20261116_zero_linear_gzip_rule_resource_readback.py"
ADDITIONAL = (ENTRY, BASE_READER, TWO_PHASE_READER, RULE_READER)
SAMPLER = "geometry_20261115_current_C_pruefer_joint_radial_sampling.py"
SAMPLER_SHA = "32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4"
DERIVED = "request218-derived205-dispatch.json"
RECEIPT = "request218-composition.json"
MARKER = "request218-composition-readback-complete.json"
HERE = Path(__file__).resolve().parent
OUTER_FILE = "topics/visible-flex-larger-amplitude/notes/current-C-zero-linear-gzip-incremental-M-refinement218-request.json"


PARENT = {
    "file": "topics/visible-flex-larger-amplitude/notes/current-C-actual202-coast-incremental-M-refinement216-request.json",
    "bytes": 57819, "sha256": "994c1f2ef39e27e793b977f913f84bee4f4c4406431e23da5dc7dcf716cbdd55",
}
PARENT_WORKFLOW = {
    "file": ".github/workflows/visible-current-C-actual202-coast-incremental-M-refinement216.yml",
    "bytes": 97966, "sha256": "bcb85d7399009698fac7cbbc34424ea28c73edc1927730302c3460dbc372baf8",
}
COAST_HELPER = {
    "file": "geometry_20261116_complete_coast_bernstein_enclosures.py",
    "bytes": 18291, "sha256": "3730c62b5c1a40fb594c9a2d9ed95a523a9134f12eb0b8def59c764d79e3edae",
}
MATERIALIZATION = "source-materialization218"
COAST_ROLES = ("same_far_post", "same_far_post_reader", "same_far_held",
               "modes_post", "modes_post_reader", "modes_held", "evidence")

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


def generation_specs(outer):
    specs = ([outer["source_view_generation"]] + list(outer["coast_source_generation"])
        + list(outer["native_source_generation"]))
    require(len(specs) == 5, "Keep all original three generations, then R496 and R498 source layers")
    expected_schemas = (
        "R464-incremental-M-explicit-source-views-v1",
        "R483-complete-coast-metric-source-view-generation-v1",
        "R487-complete-coast-union-three-level-source-view-generation-v1",
        "R496-current-C-zero-linear-three-level-source-generation-v1",
        "R496-current-C-zero-linear-three-level-source-generation-v1")
    expected_counts = (15, 5, 13, 49, 51)
    names, dirs = set(), set()
    for item, schema, count in zip(specs, expected_schemas, expected_counts):
        require(item["schema"] == schema and len(item["expected_generated_sources"]) == count,
            "Bind the exact complete source-view family and count")
        directory = item["receipt_directory"]
        require(Path(directory).name == directory and directory not in dirs,
            "Keep each actual generation receipt in a distinct namespace child")
        dirs.add(directory)
        for name, desc in item["expected_generated_sources"].items():
            require(Path(name).name == name and desc["file"] == name and name not in names,
                "Every generated source needs a distinct actual basename")
            require(type(desc["bytes"]) is int and 0 < desc["bytes"] < 100000
                and re.fullmatch(r"[0-9a-f]{64}", desc["sha256"]),
                "Bind the complete generated source bytes")
            names.add(name)
    return specs


def generated_sources(outer):
    result = {}
    for item in generation_specs(outer):
        result.update(item["expected_generated_sources"])
    return result


def bind_parent(repo, outer, original):
    require(outer["original216_subcontract"] == PARENT
        and outer["original216_workflow"] == PARENT_WORKFLOW,
        "Bind the published216 source contract, never its running state")
    parent_raw = (repo/PARENT["file"]).read_bytes()
    require(match(parent_raw,PARENT) and
        match((repo/PARENT_WORKFLOW["file"]).read_bytes(),PARENT_WORKFLOW),
        "The complete original216 bytes differ")
    parent = json.loads(parent_raw)
    require(parent["request_number"] == 216, "Use the genuine216 source ancestry")
    for key in ("original205_subcontract","original205_workflow",
        "original209_subcontract","original209_workflow","original212_subcontract",
        "original212_workflow","original214_subcontract","original214_workflow",
        "execution","refinement_work","source_view_generation","coast_source_generation",
        "mode_extension_proof","additional_exact_source_contracts",
        "display_families","actual_level_families","scientific_control_change",
        "reviewed_README_blobs"):
        require(outer[key] == parent[key],
            "Keep the original216 input/work/clock/source-generation member: "+key)
    for key in ("original209_subcontract","original209_workflow",
        "original212_subcontract","original212_workflow",
        "original214_subcontract","original214_workflow"):
        require(match((repo/parent[key]["file"]).read_bytes(),parent[key]),
            "Older complete source contract differs: "+key)
    expected_witnesses = copy.deepcopy(parent["witness_families"])
    expected_witnesses["incrementalM"] = dict(cut=descriptor(outer,"union_cut"),
        atlas=descriptor(outer,"union_atlas"))
    require(outer["witness_families"] == expected_witnesses,
        "Only the actual new incremental-M witness source tuple may change")
    require(set(outer["roles"]) == set(parent["roles"]),
        "Keep every original actual role")
    old_public = dict(original["source_sha256"])
    for name,row in parent["metadata_sources"].items():
        require(name not in old_public or old_public[name] == row["sha256"],
            "Conflicting original metadata source")
        old_public[name] = row["sha256"]
    for name,digest in parent["additional_source_sha256"].items():
        require(name not in old_public or old_public[name] == digest,
            "Conflicting original216 source")
        old_public[name] = digest
    require(len(old_public) == parent["published_source_count"] == 260,
        "Retain all actual260 published216 sources")
    return parent,old_public


def descriptor(outer, role):
    item = outer["native_registration"]["current_roles"][role]
    require(set(item) >= {"file","bytes","sha256"},
        "A complete current source descriptor is required: "+role)
    result = {key:item[key] for key in ("file","bytes","sha256")}
    expected = generated_sources(outer).get(item["file"])
    require(expected == result,
        "The current role must name its actual generated source: "+role)
    return result


def declared_source_identity(comp,item,outer):
    expected = generated_sources(outer).get(item["file"])
    if expected is not None:
        require({k:item[k] for k in ("file","bytes","sha256")} == expected,
            "A deferred generated metadata descriptor differs")
        # This is a declaration before materialization, never a receipt that
        # falsely claims a source file has already been created or executed.
        return dict(expected)
    return source_identity(comp,item)


def current_dispatch(original,outer,published,generated):
    """Explicit source/storage bindings; scientific values come from original205.

    No current scientific parameter is copied from a new source role table.
    The only original sampling-work change is the already published depth2.
    """
    derived = copy.deepcopy(original)
    roles = outer["native_registration"]["current_roles"]
    def rebind(value,role):
        out = copy.deepcopy(value)
        out.update(descriptor(outer,role))
        if "schema" in roles[role]:
            out["schema"] = roles[role]["schema"]
        return out
    require(derived["native_sampling"]["file"] == SAMPLER
        and derived["native_sampling"]["sha256"] == SAMPLER_SHA
        and derived["native_sampling"]["parameters"]["sample_inverse_depth"] == 24,
        "Keep the actual original native sampler/work baseline")
    derived["native_sampling"] = rebind(derived["native_sampling"],"first_sampler")
    derived["native_sampling"]["parameters"]["sample_inverse_depth"] = 2
    derived["current_BVP"] = rebind(derived["current_BVP"],"first_driver")
    derived["current_BVP_launch"] = rebind(derived["current_BVP_launch"],"first_launcher")
    derived["current_BVP_launch"]["actual_tail_client_argv_names_joint02e164_client"] = False
    derived["current_BVP_launch"]["actual_current_client_source"] = descriptor(outer,"first_client")
    derived["current_BVP_readout"] = rebind(derived["current_BVP_readout"],"first_reader")
    derived["pipeline"] = rebind(derived["pipeline"],"pipeline")
    derived["actual202_candidate"]["adapter"] = rebind(
        derived["actual202_candidate"]["adapter"],"candidate")
    derived["actual202_candidate"]["driver"] = rebind(
        derived["actual202_candidate"]["driver"],"first_driver")
    derived["continuous_ten"]["hooks"] = rebind(derived["continuous_ten"]["hooks"],"first_hook")
    derived["execution"]["owned_process_helper"] = rebind(
        derived["execution"]["owned_process_helper"],"first_owner")
    provider = derived["pruefer_provider"]
    provider["schema"] = "request218-explicit-zero-linear-gzip-joint-provider-v1"
    provider["recipe_schema"] = roles["first_driver"]["recipe_schema"]
    provider["sampler"] = rebind(provider["sampler"],"first_sampler")
    provider["driver"] = rebind(provider["driver"],"first_driver")
    replacements = copy.deepcopy(provider["native_source_replacements"])
    for item,role in zip(replacements,("first_sampler","first_worker","first_client")):
        require(item["file"] == original["pruefer_provider"]["native_source_replacements"][
            ("first_sampler","first_worker","first_client").index(role)]["file"],
            "Bind the original explicit native replacement order")
        item.update(file=descriptor(outer,role)["file"],sha256=descriptor(outer,role)["sha256"])
    provider["native_source_replacements"] = replacements
    additions = dict(provider["new_native_source_additions"])
    old_native = original["pruefer_provider"]["complete_current_native_source_sha256"]
    for name in ("geometry_20261115_current_C_pruefer_joint_native_worker.mjs",
                 "geometry_20261115_current_C_pruefer_joint_tail_client.py"):
        require(name not in additions,"A current ancestor was already an addition")
        additions[name] = old_native[name]
    for item in outer["native_registration"]["unchanged_helpers"]:
        require(item["file"] in published and published[item["file"]] == item["sha256"],
            "Keep each true public native/storage helper")
        require(item["file"] not in additions,"Duplicate actual native helper")
        additions[item["file"]] = item["sha256"]
    provider["new_native_source_additions"] = additions
    native = dict(old_native)
    native.pop(original["native_sampling"]["file"])
    native[descriptor(outer,"first_sampler")["file"]] = descriptor(outer,"first_sampler")["sha256"]
    for role in ("first_worker","first_client"):
        item = descriptor(outer,role); native[item["file"]] = item["sha256"]
    for item in outer["native_registration"]["unchanged_helpers"]:
        require(item["file"] not in native,"Duplicate current helper in native configuration")
        native[item["file"]] = item["sha256"]
    provider["complete_current_native_source_sha256"] = native
    provider["original205_complete_driver_source_count"] = provider.pop("complete_driver_source_count")
    provider["complete_current_driver_closure_is_recorded_by_the_actual_driver"] = True
    provider["complete_native_source_count"] = len(native)
    provider["original205_complete_native_source_count"] = original["pruefer_provider"]["complete_native_source_count"]
    provider["actual_native_implementation_scope"] = outer["native_registration"]["scope"]
    closed = derived["closed_postsolve"]
    for role,current_role in (("orchestrator","first_post_entry"),("runner","first_post"),
        ("reader","first_postreader"),("held","first_held"),("helper","first_policy"),("owner","first_owner")):
        closed[role] = rebind(closed[role],current_role)
    closed["schema"] = "request218-explicit-zero-linear-gzip-first-closed-composition-v1"
    closed["upstream_kind"] = "actual202218"
    derived["workflow"] = outer["workflow"]
    derived["source_sha256"] = dict(published)
    derived["source_sha256"].update({name:row["sha256"] for name,row in generated.items()})
    derived["source_count"] = len(derived["source_sha256"])
    # Restore complete explicitly rebound members. Every other input, field,
    # budget, threshold and policy word must still be the original205 member.
    changed = ("native_sampling","current_BVP","current_BVP_launch","current_BVP_readout",
        "pipeline","actual202_candidate","continuous_ten","execution","pruefer_provider",
        "closed_postsolve","workflow","source_sha256","source_count")
    restored = copy.deepcopy(derived)
    for key in changed:
        restored[key] = original[key]
    require(restored == original,"An undeclared original205 member changed")
    for key in ("scientific_parameters","inputs","construction_inputs","construction",
        "selected_construction","actual180_selection","query_recipe","finite_head","deep_far"):
        require(derived[key] == original[key],"Original mathematical/source input changed: "+key)
    require(derived["native_sampling"]["parameters"] ==
        dict(original["native_sampling"]["parameters"],sample_inverse_depth=2),
        "Only the already published depth2 work allocation differs")
    original_execution = copy.deepcopy(derived["execution"])
    original_execution["owned_process_helper"] = original["execution"]["owned_process_helper"]
    require(original_execution == original["execution"],
        "Keep every original resource/clock/threshold value")
    return derived


def compose(request_path,base,comp,expected_outer=None):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "This source composition belongs to the public Actions job")
    repo = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
    request_path,base,comp = request_path.resolve(),base.resolve(),comp.resolve()
    require(comp == HERE and comp == repo/"topics/visible-flex-larger-amplitude/computations",
        "Use actual computations HERE for every current driver and checkpoint")
    require(base == temporary/NAMESPACE and base.is_dir() and not base.is_symlink(),
        "Use the original actual205-contract namespace without restarting its clock")
    checkout = repo/OUTER_FILE
    require(request_path in (checkout,base/"refinement218-request.json") and checkout.is_file(),
        "Use current checkout bytes or their unique same-job copy")
    outer_raw = request_path.read_bytes()
    require(outer_raw == checkout.read_bytes()
        and (expected_outer is None or sha(outer_raw) == expected_outer),
        "Actual218 request bytes differ")
    outer = json.loads(outer_raw)
    require(outer.get("schema") == REQUEST_SCHEMA and outer.get("request_number") == 218
        and outer.get("repository") == REPOSITORY,"Bind independent request218")
    require(outer["original205_subcontract"] == ORIGINAL
        and outer["original205_workflow"] == ORIGINAL_WORKFLOW,"Keep frozen205 source ancestry")
    original_raw = (repo/ORIGINAL["file"]).read_bytes()
    require(match(original_raw,ORIGINAL)
        and match((repo/ORIGINAL_WORKFLOW["file"]).read_bytes(),ORIGINAL_WORKFLOW),
        "The complete published205 bytes differ")
    original = json.loads(original_raw)
    require(original["schema"] == ORIGINAL_SCHEMA and original["request_number"] == 205
        and len(original["source_sha256"]) == original["source_count"] == 154,
        "Keep the true original205 interface and all154 ancestor pins")
    parent,old_public = bind_parent(repo,outer,original)
    specs,generated = generation_specs(outer),generated_sources(outer)
    declared = outer["metadata_sources"]
    require(set(declared) == set(ADDITIONAL),
        "Use the current composer and actual generated metadata readers")
    sources = {name:declared_source_identity(comp,declared[name],outer) for name in ADDITIONAL}
    require(all(declared[name]["file"] == name for name in ADDITIONAL),
        "Metadata source keys and basenames differ")
    new_public = dict(outer["additional_source_sha256"])
    for name,digest in old_public.items():
        require(name not in new_public or new_public[name] == digest,
            "Never overwrite a published216 source identity")
        new_public[name] = digest
    for name,row in sources.items():
        if name not in generated:
            require(name not in new_public or new_public[name] == row["sha256"],
                "Conflicting current public metadata source")
            new_public[name] = row["sha256"]
    require(not set(new_public).intersection(generated),
        "Public files and actual generated views are distinct")
    require(len(new_public) == outer["published_source_count"]
        and len(generated) == outer["generated_source_count"] == 133
        and len(new_public)+len(generated) == outer["complete_source_count"],
        "Actual public/generated source counts differ")
    for spec in specs:
        for field in ("generator","plan"):
            if field in spec:
                require(new_public.get(spec[field]["file"]) == spec[field]["sha256"],
                    "Bind every complete public source-generation input")
    for role,item in outer["roles"].items():
        require(new_public.get(item["file"]) == item["sha256"] or
            generated.get(item["file"],{}).get("sha256") == item["sha256"],
            "Every actual role needs its true source identity: "+role)
    require(outer["current_BVP_readout"] == outer["native_registration"]["current_roles"]["first_reader"],
        "Name the current full two-phase reader")
    require(outer["workflow"] ==
        ".github/workflows/visible-current-C-zero-linear-gzip-incremental-M-refinement218.yml",
        "Bind this independent218 workflow")
    derived = current_dispatch(original,outer,new_public,generated)
    for role,key in (("orchestrator","first_post_entry"),("runner","first_post"),
        ("reader","first_postreader"),("held","first_held")):
        require({k:outer["coast_closed_postsolve"][role][k] for k in ("file","bytes","sha256")}
            == descriptor(outer,key),"Current closed source role differs")
    require(derived["source_count"] == outer["derived205_source_count"],
        "Actual derived source universe differs")
    outer_id = dict(file=OUTER_FILE,bytes=len(outer_raw),sha256=sha(outer_raw))
    derived["explicit218_composition"] = dict(
        schema=SCHEMA+"-declared-source-composition",outer_request=outer_id,
        actual_request_number=218,original216=PARENT,original205=ORIGINAL,
        embedded_runtime_request_number=205,embedded_runtime_schema=ORIGINAL_SCHEMA,
        embedded_index_is_source_interface_not_old_run_or_old_dispatch=True,
        actual_run_id=os.environ["GITHUB_RUN_ID"],actual_source_commit=os.environ["GITHUB_SHA"],
        source_generation_order=[item["schema"] for item in specs],
        original_thresholds_full_rows_and_work_budgets_preserved=True,
        actual_noJ_caller_and_original_f9b_ancestor_are_separate=True,
        complete_gzip_stored_and_decoded_original_streams_required=True,
        original_32GiB_startup_gate_not_reduced=True,
        no_scientific_result_or_speed_promised=True)
    raw = canonical(derived)
    receipt = dict(schema=SCHEMA,repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        source=sources[ENTRY],actual_computations=str(comp),outer_request=outer_id,
        original205_request=ORIGINAL,original205_workflow=ORIGINAL_WORKFLOW,
        original216_request=PARENT,original216_workflow=PARENT_WORKFLOW,
        original209_request=REFINEMENT_ORIGINAL,original212_request=SHALLOW_ORIGINAL,
        derived_dispatch=dict(file=DERIVED,bytes=len(raw),sha256=sha(raw)),
        original_source_count=154,derived_source_count=derived["source_count"],
        actual_published_source_count=len(new_public),actual_generated_source_count=len(generated),
        actual_complete_source_count=len(new_public)+len(generated),
        declared_new_metadata_sources=sources,exact_member_changes=changes(original,derived),
        declared_generated_descriptors_are_not_pre_materialization_file_receipts=True,
        all_original_numeric_parameters_gates_and_absolute_budgets_preserved=True,
        original216_all_public_and_generated_source_ancestors_retained=True,
        original_factory_domain_not_replaced=True,
        scientific_module_imported_or_scientific_value_recomputed=False,
        actual_source_generation_required_before_any_scientific_role=True,
        one_original_namespace_clock_created_only_by_initialize=True,
        composition_generation_verification_and_readback_do_not_restart_clock=True)
    return base,raw,receipt


def formed_owner_source(comp,outer,item):
    """Form only the actual private owner's complete source before materialization.

    Plans are ordinary pinned JSON literal replacements. No generated module is
    evaluated. The later full generation still creates its real same-HERE file.
    """
    cache = {}
    def form(expected,active):
        name = expected["file"]
        require(name not in active,"Cyclic owner source declaration")
        if name in cache:
            require(match(cache[name],expected),"Conflicting bootstrap identity")
            return cache[name]
        path = comp/name
        if path.is_file():
            source_identity(comp,expected)
            raw = path.read_bytes();cache[name] = raw
            return raw
        candidates = []
        for spec in outer["native_source_generation"]:
            source_identity(comp,spec["plan"])
            plan = json.loads((comp/spec["plan"]["file"]).read_bytes())
            require(plan["schema"] == "R496-current-C-zero-linear-three-level-source-view-plan-v1",
                "Only the explicit R496 literal owner source construction is used")
            for row in plan["views"]:
                if row["output"]["file"] == name:
                    candidates.append((plan,row))
        require(len(candidates) == 1,"Owner source must have exactly one declared construction")
        plan,row = candidates[0]
        require(row["output"] == expected,"Actual owner output descriptor differs")
        text = form(row["baseline"],active|{name}).decode("utf-8")
        for application in row["applications"]:
            patch = plan["literal_patches"][application["patch"]]
            require(text.count(patch["before"]) == application["count"],
                "Owner source literal occurrence count differs")
            text = text.replace(patch["before"],patch["after"])
        raw = text.encode("utf-8")
        require(match(raw,expected),"Actual owner complete generated bytes differ")
        cache[name] = raw
        return raw
    return form(item,set())

def materialization_receipt(outer, base, comp, *, require_complete=True):
    path = base/MATERIALIZATION/"result.json"
    value = json.loads(path.read_bytes())
    require(value.get("schema") == SCHEMA+"-materialization-v1"
        and value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"]
        and value.get("actual_computations") == str(comp),
        "Use the current actual generation transaction")
    expected = generated_sources(outer)
    actual = {}
    for spec in generation_specs(outer):
        file = "source-view-result.json" if spec["schema"].startswith("R464-") else "result.json"
        result_path = base/spec["receipt_directory"]/file
        if not result_path.is_file():
            if require_complete:
                raise ValueError("An actual generation result is absent: "+str(result_path))
            continue
        result = json.loads(result_path.read_bytes())
        require(result.get("schema") == spec["schema"]
            and result.get("run_id") == os.environ["GITHUB_RUN_ID"]
            and result.get("source_commit") == os.environ["GITHUB_SHA"],
            "An actual generation source/run/schema differs")
        source = result["source"]
        require(source["bytes"] == spec["generator"]["bytes"]
            and source["sha256"] == spec["generator"]["sha256"],
            "The actual generator differs")
        if require_complete:
            require(result.get("completed") is True, "A source family did not complete")
        rows = result.get("generated_sources",[]) if file == "source-view-result.json" else result.get("outputs",[])
        for row in rows:
            rid = row["actual_source"]; name = Path(rid["file"]).name
            require(name in spec["expected_generated_sources"] and name not in actual,
                "Unknown or duplicated actual generated source")
            actual[name] = source_identity(comp, spec["expected_generated_sources"][name])
            require(rid["bytes"] == actual[name]["bytes"] and rid["sha256"] == actual[name]["sha256"]
                and Path(rid["file"]).resolve() == comp/name,
                "An actual generated receipt does not match its real source")
    if require_complete:
        require(value.get("completed") is True and set(actual) == set(expected),
            "The complete five-generation source transaction is incomplete")
    return value, identity(path), actual


def materialize(args):
    base, raw, composition = compose(args.request,args.base,args.computations,args.request_sha256)
    comp = args.computations.resolve()
    verify_runtime(args.request,args.request_sha256,base,comp,require_dispatch=False)
    outer = json.loads(args.request.read_bytes())
    directory = base/MATERIALIZATION
    require(not directory.exists(), "Do not replace a prior generation transaction")
    directory.mkdir()
    value = dict(schema=SCHEMA+"-materialization-v1",repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        source=identity(__file__),actual_computations=str(comp),outer_request=identity(args.request),
        completed=False,current_generation=None,generations=[],error=None,
        original_sources_overwritten=False,scientific_module_imported_or_executed=False,
        original_absolute_clock_restarted=False,raw_deleted=False)
    code = 2
    try:
        dispatch = json.loads(raw)
        all_public = {name:digest for name,digest in dispatch["source_sha256"].items()
            if name not in generated_sources(outer)}
        for name,digest in outer["additional_source_sha256"].items():
            require(name not in all_public or all_public[name] == digest,
                "Public source declarations conflict")
            all_public[name] = digest
        require(len(all_public) == outer["published_source_count"],
            "Bind the complete actual public source universe before generating")
        for name,digest in all_public.items():
            require(Path(name).name == name and sha((comp/name).read_bytes()) == digest,
                "Actual public source differs before generation: "+name)
        for index,spec in enumerate(generation_specs(outer)):
            value["current_generation"] = dict(index=index,schema=spec["schema"])
            path = comp/spec["generator"]["file"]
            source_identity(comp,spec["generator"])
            alias = "_request218_metadata_generator_"+str(index)
            module_spec = importlib.util.spec_from_file_location(alias,path)
            module = importlib.util.module_from_spec(module_spec)
            sys.modules[alias] = module
            # Each exact pinned generator is standard-library source text
            # construction only; no target scientific source is imported.
            module_spec.loader.exec_module(module)
            argv = ["--computations",str(comp),"--out",str(base/spec["receipt_directory"])]
            if "plan" in spec:
                source_identity(comp,spec["plan"])
                argv += ["--plan",str(comp/spec["plan"]["file"]),"--plan-sha256",spec["plan"]["sha256"]]
            stdout,stderr = directory/(str(index)+".stdout.log"),directory/(str(index)+".stderr.log")
            with stdout.open("x",encoding="utf-8") as out,stderr.open("x",encoding="utf-8") as err:
                with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                    status = module.main(argv)
            value["generations"].append(dict(index=index,schema=spec["schema"],actual_exit=status,
                stdout=identity(stdout),stderr=identity(stderr),
                receipt_directory=spec["receipt_directory"]))
            if status != 0:
                sys.stderr.write(stderr.read_text(encoding="utf-8"))
                sys.stderr.flush()
            require(status == 0, "The actual source generator did not complete: "+spec["schema"])
        value["completed"] = True
        value["current_generation"] = None
        code = 0
    except BaseException as error:
        value["error"] = dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
    write_new(directory/"result.json",canonical(value))
    if value["completed"]:
        materialization_receipt(outer,base,comp)
    print(json.dumps(dict(event="request218_actual_source_materialization",
        result=identity(directory/"result.json"),completed=value["completed"],
        current_generation=value["current_generation"],error=value["error"],actual_exit=code,
        scientific_computation_started=False,raw_deleted=False),sort_keys=True),flush=True)
    return code


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
            "The science dispatch is not the actual explicitly derived218 contract")
    return json.loads(raw), identity(base / DERIVED), identity(base / RECEIPT)



def stage_public_source_plans(repo,comp,outer):
    """Copy explicit published notes JSON into actual computations before use.

    These are complete public source plans, not generated scientific sources.
    No existing file with different bytes is overwritten.
    """
    records = []
    for item in outer["public_source_plan_copies"]:
        expected = {key:item[key] for key in ("file","bytes","sha256")}
        source = repo/item["repository_file"]
        require(source.is_file() and not source.is_symlink()
            and source.resolve().is_relative_to(repo),
            "Use the actual complete published source plan")
        raw = source.read_bytes()
        require(match(raw,expected) and len(raw)<100000,
            "Published source-plan bytes differ")
        target = comp/item["file"]
        require(target.parent == comp and not target.is_symlink(),
            "Source-plan copy must remain in actual computations")
        existed = target.exists()
        if existed:
            require(target.is_file() and target.read_bytes() == raw,
                "Do not replace an existing source-plan copy")
        else:
            write_new(target,raw)
        records.append(dict(published_file=item["repository_file"],
            actual_source=source_identity(comp,expected),
            existing_identical_copy=existed,complete_public_bytes_copied=True))
    return records


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
        "Bind the actual218 outer bytes before creating its namespace")
    namespace_started = time.time()
    base.mkdir(exist_ok=False)
    actual_plan_copies = stage_public_source_plans(repo,comp,json.loads(args.request.read_bytes()))
    write_new(base/"source-plan-copies.json",canonical(dict(
        repository=REPOSITORY,run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],copies=actual_plan_copies)))
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
    owner_descriptor = {k:owner[k] for k in ("file","bytes","sha256")}
    outer = json.loads(args.request.read_bytes())
    owner_raw = formed_owner_source(comp,outer,owner_descriptor)
    require(match(owner_raw,owner_descriptor) and len(owner_raw) == 14812
        and sha(owner_raw) == "419215a322b4ab0763d9e8a7b192225422a3453fec11485cd0f8f28c09c77f96",
        "Use the real R496 owner bytes, not an old source label")
    # This is the original Actions-only syntax check moved out of YAML.
    # Source authoring does not execute this branch or import project science.
    import ast
    compile(ast.parse(owner_raw, filename="request205_owned_process.py"),
        "request205_owned_process.py", "exec")
    write_new(base / "request205_owned_process.py", owner_raw)
    deadline = dict(schema="request205-owned-job-science-deadline-v1",
        repository=os.environ["GITHUB_REPOSITORY"], run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], request_sha256=sha(raw),
        template_recipe_sha256=sha(recipe_raw), namespace_created_unix_seconds=namespace_started,
        science_seconds_from_namespace=18900, readback_reserve_seconds=2700,
        job_timeout_minutes=360, resource_deadline_not_a_scientific_gate=True,
        scope="Startup resource plan before BVP; original BVP launcher enforces its actual namespace deadline",
        no_global_absolute_kill_clock_for_prior_stages=True,
        original_sampling_phase_clocks_exclude_binding_and_setup=True)
    write_new(base / "job-science-deadline.json", canonical(deadline))
    print(json.dumps(dict(event="request218_actual_original_namespace_resource_plan", **deadline),
        sort_keys=True), flush=True)
    with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as stream:
        stream.write("VISIBLE_BASE=" + str(base) + "\n")
        stream.write("VISIBLE_COMPUTATIONS=" + str(comp) + "\n")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("initialize", "materialize", "prepare", "verify", "readback"))
    for name in ("request", "base", "computations"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--request-sha256", required=True)
    args = parser.parse_args(argv)
    if args.command == "initialize":
        return initialize(args)
    if args.command == "materialize":
        return materialize(args)
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
        print("BEGIN_REQUEST218_SOURCE_COMPOSITION_NECESSARY", flush=True)
        print(record.decode("utf-8"), end="", flush=True)
        print("END_REQUEST218_SOURCE_COMPOSITION_NECESSARY", flush=True)
        marker = {"schema": SCHEMA + "-readback-complete", "repository": REPOSITORY,
            "run_id": os.environ["GITHUB_RUN_ID"], "source_commit": os.environ["GITHUB_SHA"],
            "complete": True, "necessary_summary": {"bytes": len(record), "sha256": sha(record)},
            "derived_dispatch": value["derived_dispatch"], "outer_request": value["outer_request"],
            "only_immutable_source_composition_read_no_scientific_success_inferred": True}
        write_new(base / MARKER, canonical(marker))
    print(json.dumps({"event": "request218_explicit_sampling_refinement_composition_" + args.command,
        "repository": REPOSITORY, "run_id": os.environ["GITHUB_RUN_ID"],
        "source_commit": os.environ["GITHUB_SHA"],
        "receipt": identity(base / RECEIPT), "outer_request": value["outer_request"],
        "derived_dispatch": value["derived_dispatch"], "original205_request": ORIGINAL,
        "original209_request": REFINEMENT_ORIGINAL, "original212_request": SHALLOW_ORIGINAL,
        "original_inverse_work_depth": 24, "actual_all_three_levels_inverse_work_depth": 2,
        "source_counts": {"original205": 154, "derived205": value["derived_source_count"],
            "all_published": value["actual_published_source_count"],
            "generated": value["actual_generated_source_count"],
            "all_runtime": value["actual_complete_source_count"]},
        "all_original_numeric_parameters_gates_and_absolute_budgets_preserved": True, "scientific_success_not_inferred": True},
        ensure_ascii=False, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
