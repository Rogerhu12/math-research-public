#!/usr/bin/env python3
"""Request216: exact source composition for the original214 chain plus R483 ranges.

All original205 scientific inputs, complete native/FD gates, depth2 sampling,
R456 mesh and R464 union-M work remain. Only the actual coast metric/evidence
and their source-bound callers change. The original namespace clock is created
once, before source materialization. No old run or scientific result is reused.
Author: OpenAI / ChatGPT exact_refinement agent (AI), 2026-11-16.
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
ENTRY = "root_20261116_request216_sampling_refinement_composition.py"
SCHEMA = "request216-original214-explicit-coast-refinement-composition-v1"
REQUEST_SCHEMA = "public-actual202-coast-Bernstein-incremental-M-refinement-and-displays-request-v1"
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
    "geometry_20261116_request216_owned_roles.py",
    "geometry_20261116_request216_joint_refinement.py",
    "root_20261116_request216_refinement_necessary.py",
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
DERIVED = "request216-derived205-dispatch.json"
RECEIPT = "request216-composition.json"
MARKER = "request216-composition-readback-complete.json"
HERE = Path(__file__).resolve().parent
OUTER_FILE = "topics/visible-flex-larger-amplitude/notes/current-C-actual202-coast-incremental-M-refinement216-request.json"


PARENT = {
    "file": "topics/visible-flex-larger-amplitude/notes/current-C-actual202-shallow-inverse-incremental-M-refinement214-request.json",
    "bytes": 42062, "sha256": "c81530feca5c61e9a901937abf2e5c2704562f6eeaff0cbb70b817ec48519fe1",
}
PARENT_WORKFLOW = {
    "file": ".github/workflows/visible-current-C-actual202-shallow-inverse-incremental-M-refinement214.yml",
    "bytes": 97252, "sha256": "9ce8515103cae3388330bcabad08164a52a7d22d5e34ead248db5f26bba8565e",
}
COAST_HELPER = {
    "file": "geometry_20261116_complete_coast_bernstein_enclosures.py",
    "bytes": 18291, "sha256": "3730c62b5c1a40fb594c9a2d9ed95a523a9134f12eb0b8def59c764d79e3edae",
}
MATERIALIZATION = "source-materialization216"
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
    specs = [outer["source_view_generation"]] + list(outer["coast_source_generation"])
    require(len(specs) == 3, "Keep the real R464, R483 and R487 generation order")
    expected_schemas = (
        "R464-incremental-M-explicit-source-views-v1",
        "R483-complete-coast-metric-source-view-generation-v1",
        "R487-complete-coast-union-three-level-source-view-generation-v1")
    expected_counts = (15, 5, 13)
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
    require(outer["original214_subcontract"] == PARENT
        and outer["original214_workflow"] == PARENT_WORKFLOW,
        "Bind the actual published214 request and workflow, not its previous run")
    raw = (repo/PARENT["file"]).read_bytes()
    require(match(raw, PARENT) and match((repo/PARENT_WORKFLOW["file"]).read_bytes(), PARENT_WORKFLOW),
        "Published214 complete bytes differ")
    parent = json.loads(raw)
    require(parent["request_number"] == 214, "Use the real214 source contract")
    for key in ("original205_subcontract", "original205_workflow",
        "original209_subcontract", "original209_workflow", "original212_subcontract",
        "original212_workflow", "execution", "refinement_work", "source_view_generation",
        "witness_families", "mode_extension_proof",
        "additional_exact_source_contracts", "display_families", "actual_level_families",
        "scientific_control_change", "current_BVP_readout", "reviewed_README_blobs"):
        require(outer[key] == parent[key], "An original214 scientific/resource member changed: "+key)
    for key in ("original209_subcontract", "original209_workflow",
                "original212_subcontract", "original212_workflow"):
        require(match((repo/parent[key]["file"]).read_bytes(), parent[key]),
            "Complete older source ancestry bytes differ: "+key)
    require(outer["original214_held_source_contract"] == parent["held_source_contract"],
        "Retain the original held source contract as explicit ancestry")
    require(outer["held_source_contract"]["necessary_schema"] ==
        outer["roles"]["modes_held"]["schema"]+"-necessary-v1",
        "Name the actual new held source schema rather than its R464 ancestor")
    require(set(outer["roles"]) == set(parent["roles"]), "Retain every actual214 role")
    mutable = {"owner", "runner", "reader", *COAST_ROLES}
    for name, desc in parent["roles"].items():
        if name not in mutable:
            require(outer["roles"][name] == desc, "An unchanged scientific role differs: "+name)
    old_sources = dict(original["source_sha256"])
    old_sources.update({name: row["sha256"] for name,row in parent["metadata_sources"].items()})
    for name, value in parent["additional_source_sha256"].items():
        require(name not in old_sources or old_sources[name] == value,
            "The original214 public source universe contains a conflict")
        old_sources[name] = value
    require(len(old_sources) == parent["published_source_count"] == 251,
        "Keep all actual251 original214 public sources")
    return parent, old_sources


def compose(request_path, base, comp, expected_outer=None):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "This source composition belongs to the public Actions job")
    repo, temporary = Path(os.environ["GITHUB_WORKSPACE"]).resolve(), Path(os.environ["RUNNER_TEMP"]).resolve()
    request_path, base, comp = request_path.resolve(), base.resolve(), comp.resolve()
    require(comp == HERE and comp == repo/"topics/visible-flex-larger-amplitude/computations",
        "Use the actual public computations HERE, not a relocated partial import tree")
    require(base == temporary/NAMESPACE and base.is_dir() and not base.is_symlink(),
        "Use the original actual205-contract namespace without restarting its clock")
    checkout = repo/OUTER_FILE
    require(request_path in (checkout, base/"refinement216-request.json") and checkout.is_file(),
        "Use the current checkout contract or its sole actual same-job copy")
    outer_raw = request_path.read_bytes()
    require(outer_raw == checkout.read_bytes()
        and (expected_outer is None or sha(outer_raw) == expected_outer),
        "The actual216 request differs from the declared checkout bytes")
    outer = json.loads(outer_raw)
    require(outer.get("schema") == REQUEST_SCHEMA and outer.get("request_number") == 216
        and outer.get("repository") == REPOSITORY, "Bind the actual independent request216")
    require(outer["original205_subcontract"] == ORIGINAL
        and outer["original205_workflow"] == ORIGINAL_WORKFLOW,
        "Retain the whole frozen205 subcontract identities")
    original_raw = (repo/ORIGINAL["file"]).read_bytes()
    require(match(original_raw, ORIGINAL) and match((repo/ORIGINAL_WORKFLOW["file"]).read_bytes(), ORIGINAL_WORKFLOW),
        "The complete published205 bytes differ")
    original = json.loads(original_raw)
    require(original["schema"] == ORIGINAL_SCHEMA and original["request_number"] == 205
        and len(original["source_sha256"]) == original["source_count"] == 154,
        "Keep the real original205 runtime schema and all154 ancestor pins")
    parent, old_public = bind_parent(repo, outer, original)
    declared = outer["metadata_sources"]
    require(set(declared) == set(ADDITIONAL), "Use the actual composition and two scope readers")
    sources = {name: source_identity(comp, declared[name]) for name in ADDITIONAL}
    require(all(declared[name]["file"] == name for name in ADDITIONAL),
        "The actual metadata source keys and basenames differ")
    require(outer["current_BVP_readout"]["schema"] == TWO_PHASE_SCHEMA
        and {k:outer["current_BVP_readout"][k] for k in ("file","bytes","sha256")} == sources[TWO_PHASE_READER],
        "Retain the actual R477 two-phase scope reader")
    specs = generation_specs(outer)
    generated = generated_sources(outer)
    new_public = dict(outer["additional_source_sha256"])
    for name,row in sources.items():
        require(name not in new_public or new_public[name] == row["sha256"],
            "A declared public source has conflicting identities")
        new_public[name] = row["sha256"]
    for name,value in original["source_sha256"].items():
        require(name not in new_public or new_public[name] == value,
            "Never replace a real original205 source")
        new_public[name] = value
    require(all(new_public.get(name) == value for name,value in old_public.items())
        and not set(new_public).intersection(generated),
        "Retain all251 public ancestors and keep generated names separate")
    require(len(new_public) == outer["published_source_count"]
        and len(generated) == outer["generated_source_count"] == 33
        and len(new_public)+len(generated) == outer["complete_source_count"],
        "The actual public/generated source counts differ")
    require(new_public.get(COAST_HELPER["file"]) == COAST_HELPER["sha256"],
        "Keep the published exact R483 complete-coast helper")
    for spec in specs:
        require(new_public.get(spec["generator"]["file"]) == spec["generator"]["sha256"],
            "Bind each actual generator as public source")
        if "plan" in spec:
            require(new_public.get(spec["plan"]["file"]) == spec["plan"]["sha256"],
                "Bind the complete ordinary source plan as public source")
    for name, desc in outer["roles"].items():
        require((new_public.get(desc["file"]) == desc["sha256"])
            or (desc["file"] in generated and generated[desc["file"]]["sha256"] == desc["sha256"]),
            "Every actual role must name a full public or generated source: "+name)
    block = outer["coast_closed_postsolve"]
    require(set(block) == {"orchestrator","runner","reader","held"},
        "Only the four actual first-closed consumer/metadata roles change")
    for name,desc in block.items():
        require(desc["file"] in generated and all(desc[k] == generated[desc["file"]][k]
            for k in ("file","bytes","sha256")), "The actual first coast role differs: "+name)
    require(outer["workflow"] == ".github/workflows/visible-current-C-actual202-coast-incremental-M-refinement216.yml",
        "Bind this independent216 workflow")
    # The original runtime interface remains205; actual bytes, run and source
    # are explicit216 and never labelled as the old205/214 numerical result.
    derived = copy.deepcopy(original)
    require(derived["native_sampling"]["file"] == SAMPLER
        and derived["native_sampling"]["sha256"] == SAMPLER_SHA
        and derived["native_sampling"]["parameters"]["sample_inverse_depth"] == 24,
        "Keep the genuine original complete sampler")
    derived["native_sampling"]["parameters"]["sample_inverse_depth"] = 2
    derived["current_BVP_readout"].update(outer["current_BVP_readout"])
    derived["workflow"] = outer["workflow"]
    derived["source_sha256"].update({name: row["sha256"] for name,row in sources.items()})
    # Put every generated source in the actual dispatch so the unchanged
    # Actions syntax/source pass sees real files, not just declared labels.
    source_additions = {name: row["sha256"] for name,row in generated.items()}
    for spec in specs[1:]:
        for field in ("generator","plan"):
            source_additions[spec[field]["file"]] = spec[field]["sha256"]
    source_additions[COAST_HELPER["file"]] = COAST_HELPER["sha256"]
    require(not set(source_additions).intersection(original["source_sha256"]),
        "Coast sources must use fresh explicit names")
    derived["source_sha256"].update(source_additions)
    derived["source_count"] = len(derived["source_sha256"])
    for role,item in block.items():
        derived["closed_postsolve"][role] = {k:item[k] for k in ("file","bytes","sha256")}
    derived["closed_postsolve"]["schema"] = "request216-R487-first-coast-closed-geometry-composition-v1"
    outer_id = dict(file=OUTER_FILE,bytes=len(outer_raw),sha256=sha(outer_raw))
    derived["explicit216_composition"] = dict(schema=SCHEMA+"-declared-source-composition",
        outer_request=outer_id,actual_request_number=216,original214=PARENT,original205=ORIGINAL,
        embedded_runtime_request_number=205,embedded_runtime_schema=ORIGINAL_SCHEMA,
        embedded_index_is_source_contract_not_old_run_or_unchanged_dispatch=True,
        actual_run_id=os.environ["GITHUB_RUN_ID"],actual_source_commit=os.environ["GITHUB_SHA"],
        source_generation_order=[item["schema"] for item in specs],
        original214_all_scientific_work_and_acceptance_preserved=True,
        original_factory_domain_not_replaced=True,
        same_accurate_C_roots_and_all_ten_parameters=True,
        actual_prefix_range_implementation="published R483 complete coast Bernstein",
        original_first_construction_policy_and_material_unchanged=True,
        source_generation_is_not_scientific_success=True)
    restored = copy.deepcopy(derived)
    restored["native_sampling"]["parameters"]["sample_inverse_depth"] = 24
    restored["current_BVP_readout"] = original["current_BVP_readout"]
    restored["workflow"] = original["workflow"]
    restored["closed_postsolve"] = original["closed_postsolve"]
    restored.pop("explicit216_composition")
    for name in set(sources) | set(source_additions):
        restored["source_sha256"].pop(name)
    restored["source_count"] = original["source_count"]
    require(restored == original and derived["source_count"] == outer["derived205_source_count"],
        "Every other original205 scientific/source/input/resource member must be unchanged")
    raw = canonical(derived)
    receipt = dict(schema=SCHEMA,repository=REPOSITORY,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        source=sources[ENTRY],actual_computations=str(comp),outer_request=outer_id,
        original205_request=ORIGINAL,original205_workflow=ORIGINAL_WORKFLOW,
        original214_request=PARENT,original214_workflow=PARENT_WORKFLOW,
        original209_request=REFINEMENT_ORIGINAL,original212_request=SHALLOW_ORIGINAL,
        derived_dispatch=dict(file=DERIVED,bytes=len(raw),sha256=sha(raw)),
        original_source_count=154,derived_source_count=derived["source_count"],
        actual_published_source_count=len(new_public),actual_generated_source_count=len(generated),
        actual_complete_source_count=len(new_public)+len(generated),
        actual_new_metadata_sources=sources,exact_member_changes=changes(original,derived),
        all_other_original205_members_equal=True,
        original214_scientific_work_and_source_pins_preserved=True,
        original_factory_domain_not_replaced=True,
        scientific_module_imported_or_scientific_value_recomputed=False,
        actual_source_generation_required_before_any_scientific_role=True,
        one_original_namespace_clock_created_only_by_initialize=True,
        composition_generation_verification_and_readback_do_not_restart_clock=True)
    return base, raw, receipt


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
            "The full three-generation source transaction is incomplete")
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
            alias = "_request216_metadata_generator_"+str(index)
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
    print(json.dumps(dict(event="request216_actual_source_materialization",
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
        "Bind the actual216 outer bytes before creating its namespace")
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
    print(json.dumps(dict(event="request216_actual_original_namespace_resource_plan", **deadline),
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
        print("BEGIN_REQUEST216_SOURCE_COMPOSITION_NECESSARY", flush=True)
        print(record.decode("utf-8"), end="", flush=True)
        print("END_REQUEST216_SOURCE_COMPOSITION_NECESSARY", flush=True)
        marker = {"schema": SCHEMA + "-readback-complete", "repository": REPOSITORY,
            "run_id": os.environ["GITHUB_RUN_ID"], "source_commit": os.environ["GITHUB_SHA"],
            "complete": True, "necessary_summary": {"bytes": len(record), "sha256": sha(record)},
            "derived_dispatch": value["derived_dispatch"], "outer_request": value["outer_request"],
            "only_immutable_source_composition_read_no_scientific_success_inferred": True}
        write_new(base / MARKER, canonical(marker))
    print(json.dumps({"event": "request216_explicit_sampling_refinement_composition_" + args.command,
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
        "all_other_original205_members_equal": True, "scientific_success_not_inferred": True},
        ensure_ascii=False, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
