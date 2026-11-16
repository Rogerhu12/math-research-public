#!/usr/bin/env python3
"""R570 / request239: same-call cubic sources under the original clock.

Reproduce the full frozen222 source-classification ancestor, then form the
explicit current source contract from R544 and six metadata views. The public
checkout stays unchanged; all copied and generated files use their real paths
and complete identities. The first namespace timestamp precedes every copy.
No scientific value is imported, restored from a hash, or calculated here.
Author: OpenAI / ChatGPT exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import time
import traceback

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
ENTRY = "root_20261116_request239_actual_source_entry.py"
SCHEMA = "request239-current-C-source-binding-entry-v1"
REQUEST_SCHEMA = "public-current-C-same-semantic-head-bound239-request-v1"
NAMESPACE = "visible-current-C-actual202-ten450-closed-geometry205"
VIEW_NAME = "request239-runtime-metadata-workspace"
OUT_NAME = "source-binding239"
ENV_NAME = "request239-runtime-env.sh"
OUTER_FILE = TOPIC+"/notes/current-C-coast-base-zero-linear-gzip-incremental-M-refinement220-request.json"
ORIGINAL = dict(file=OUTER_FILE, bytes=99218,
    sha256="f6ca63871733d3f5e48ef3eb8d540fc137806ceb1ae74cef01af6b21e25f3aba")
ORIGINAL_WORKFLOW = dict(file=".github/workflows/visible-current-C-coast-base-zero-linear-gzip-incremental-M-refinement220.yml",
    bytes=94508, sha256="c1cb332dc9bd9b9b2c0b94b94477152c55d4448323dbd32f6b727142ae39524f")
DERIVED = dict(file=OUTER_FILE, bytes=99330,
    sha256="2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2")
OLD_PLAN = dict(file="request220-complete-coast-base-native-source-plan.json", bytes=66325,
    sha256="14970cc2fea0f5245218ae0752e5659747a69d6d5a22d25252fe166a48c7a786")
PLAN = dict(file="request222-coast-base-source-only-repair-plan.json", bytes=66182,
    sha256="7a74a8e65b7283bfe9acb36a27a38dbef01e8ee0507eff0ac4c3548015288ddf")
POLICY = dict(file="r503-explicit-coast-base-source-plan.json", bytes=18919,
    sha256="2f6113ce7b1928d2954d8768d2117db4452abf89cbb7f2f8b1a57719228e9dd3")
ORIGINAL_COMPOSER = dict(file="root_20261116_request220_sampling_refinement_composition.py", bytes=47343,
    sha256="f3e8ce8ebdfdd7df7f2ccd78da7c203f185de3f9c17403e0fb489e2f5cf18fca")
COMPOSER = dict(file="root_20261116_request239_sampling_refinement_composition.py", bytes=76607,
    sha256="ebd89315edd17a1e9da8b49c73ec770e108213ef4f4c58d59ddaf0da92224d41")
FOUR = [
    ORIGINAL_COMPOSER,
    dict(file="geometry_20261116_request220_owned_roles.py", bytes=25670,
         sha256="4afc01350bbaa239556f3b3edab6260b727e772df3b04351e357b0831149efc3"),
    dict(file="geometry_20261116_request220_joint_refinement.py", bytes=48824,
         sha256="7dbc1dc3a52a812eef742e892601a539bd8908cf62179e0c68527f6a0b5af55b"),
    dict(file="root_20261116_request220_refinement_necessary.py", bytes=42493,
         sha256="e887a1ced3906a4975d34815c12900a2b817318c02e9354db2e23883b7309a1c"),
]
LIMIT = 90000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")


def same(a, b):
    return isinstance(a, dict) and isinstance(b, dict) and all(
        a.get(k) == b.get(k) for k in ("bytes", "sha256"))


def receipt(path):
    path = Path(path).resolve(strict=True)
    before = path.stat(); h = hashlib.sha256(); size = 0
    with path.open("rb") as stream:
        while raw := stream.read(1048576):
            h.update(raw); size += len(raw)
    after = path.stat()
    require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
        == (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
        and size == after.st_size, "Actual source metadata changed while read")
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def bound(path, expected):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "Use an actual regular source file")
    rid = receipt(path)
    require(same(rid, expected), "Complete source metadata differs: "+str(path))
    raw = path.read_bytes()
    require(len(raw) == rid["bytes"] and sha(raw) == rid["sha256"],
        "Actual complete source changed after its identity was read")
    return raw, rid


def write_new(path, raw):
    path = Path(path)
    with path.open("xb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return receipt(path)


def current(value):
    require(value.get("repository") == REPO
        and value.get("run_id") == os.environ["GITHUB_RUN_ID"]
        and value.get("source_commit") == os.environ["GITHUB_SHA"],
        "Use this actual public job/source")


def context(args):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPO,
        "Source preparation is confined to the named public Actions job")
    primary = Path(os.environ.get("REQUEST239_PRIMARY_WORKSPACE",
        os.environ["GITHUB_WORKSPACE"])).resolve(strict=True)
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    base = args.base.resolve()
    require(base == temporary/NAMESPACE and not base.is_symlink(),
        "Keep the sole original namespace and clock")
    require(not temporary.is_relative_to(primary) and not primary.is_relative_to(temporary),
        "Keep the original checkout and fresh temporary source view separate")
    return primary, temporary, base, temporary/VIEW_NAME


def contract(args):
    raw = Path(args.request).read_bytes()
    require(sha(raw) == args.request_sha256, "The actual239 outer entry request differs")
    outer = json.loads(raw)
    require(outer.get("schema") == REQUEST_SCHEMA and outer.get("request_number") == 239
        and outer.get("repository") == REPO, "Use the independent239 metadata and science caller")
    require(same(receipt(__file__), outer["entry"]), "The actual239 entry source differs")
    ancestor_request = dict(file="topics/visible-flex-larger-amplitude/notes/current-C-prefix-tube-complete-refinement238-request.json",
        bytes=47456,sha256="cd71c4dff1629eeab92961994034b4a18b62b9665554653163dbf6ada444ee6e")
    ancestor_workflow = dict(file=".github/workflows/visible-current-C-generation-complete-refinement238.yml",
        bytes=91505,sha256="006fd8292ac2d177423837484a08c4c2ba8c35c9c72f06064ece6623466559a4")
    require(outer["frozen238_request"] == ancestor_request
        and outer["frozen238_workflow"] == ancestor_workflow,
        "Keep the exact complete238 source and original workflow")
    primary, temporary, base, view = context(args)
    ancestor_raw, _ = bound(primary/ancestor_request["file"],ancestor_request)
    bound(primary/ancestor_workflow["file"],ancestor_workflow)
    ancestor = json.loads(ancestor_raw)
    for key in ("same_C_work","scientific_scope"):
        require(outer[key] == ancestor[key],
            "Preserve every original238 work and scientific-scope member: "+key)
    execution = dict(outer["execution"])
    execution["metadata_working_view"] = ancestor["execution"]["metadata_working_view"]
    require(execution == ancestor["execution"], "Only the actual source-view description may change")
    policy_keys = ("full_scientific_temporary_raw_remains_until_original_and_new_complete_readbacks",
        "each_semantically_distinct_head_metric_measurement_compare_body_limit",
        "no_encoded_or_split_large_payload_transport",
        "original_all_readback_outcomes_and_cleanup_predicates_preserved",
        "new_rule_directories_are_explicit_distinct_semantic_scopes_not_old_raw_partitions",
        "original_full_reports_not_duplicated_into_job_outputs",
        "report_receives_new_identity_and_step_outcomes_only",
        "source_generation_failure_or_unknown_process_scope_retains_actual_raw",
        "original222_repair_necessary_marker_and_cleanup_predicates_preserved",
        "whole_composition_relation_only_if_strictly_smaller",
        "composition_original_file_and_selected_body_identities_separate",
        "source_generation_failure_or_missing_generated_cleanup_reports_skip_without_claiming_removal")
    require(all(outer["retention"][key] == ancestor["retention"][key] for key in policy_keys),
        "Keep every original238 necessary/readback/quiet/deletion policy")
    require(outer["retention"]["generation_scope"]["single_body_limit_bytes"] ==
        ancestor["retention"]["generation_scope"]["single_body_limit_bytes"] == 90000,
        "Keep the original complete generation-scope limit")
    block = outer["source_binding"]
    ancestor = block["original222_request"]
    require(ancestor == dict(
        file=TOPIC+"/notes/current-C-coast-base-source-classification-repair222-request.json",
        bytes=9442,sha256="37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672"),
        "Keep the complete frozen222 classification repair as source ancestry")
    original_raw, original_id = bound(primary/ancestor["file"],ancestor)
    value = json.loads(original_raw)
    require(value["schema"] == "public-frozen220-source-classification-repair-request-v1"
        and value["request_number"] == 222
        and value["frozen220_request"] == ORIGINAL and value["frozen220_workflow"] == ORIGINAL_WORKFLOW
        and value["derived220_request"] == DERIVED
        and value["original_source_plan"] == OLD_PLAN and value["repaired_source_plan"] == PLAN
        and value["original_R503_policy"] == POLICY and value["unchanged_outer_sources"] == FOUR,
        "The entire original222 source-only repair contract remains explicit and unchanged")
    require(block["composer"] == COMPOSER and block["repaired222_request"] == DERIVED,
        "Use the actual new composer and the genuine repaired ancestor")
    value["entry"] = outer["entry"]
    current_contract = block["current_inner_contract"]
    require(set(current_contract) == {"file","schema","request_number","identity_from",
            "published_source_count","generated_source_count","complete_source_count"}
        and current_contract["file"] == OUTER_FILE
        and current_contract["schema"] == "public-current-C-bound239-coast-base-source-closure-request-v1"
        and current_contract["request_number"] == 239
        and current_contract["identity_from"] == OUT_NAME+"/result.json:actual_derived_request"
        and all(type(current_contract[key]) is int and current_contract[key] > 0 for key in
            ("published_source_count","generated_source_count","complete_source_count"))
        and current_contract["generated_source_count"] == 311
        and current_contract["complete_source_count"] ==
            current_contract["published_source_count"]+311,
        "The current inner contract declares a real on-job identity, never a guessed digest")
    value["current_inner_contract"] = current_contract
    value["actual_current_reader"] = outer["upstream"]["reader"]
    value["actual_original222_request"] = original_id
    value["_actual239_outer"] = outer
    return value, dict(file=str(Path(args.request).resolve()), bytes=len(raw), sha256=sha(raw))


def replace_metadata_copy(path, original, replacement):
    """Only an owned metadata copy is replaced; primary checkout is read-only."""
    require(path.is_file() and not path.is_symlink() and path.read_bytes() == original,
        "The actual private metadata copy differs before replacement")
    pending = path.with_name(path.name+".request239-new")
    write_new(pending, replacement)
    os.replace(pending, path)
    return receipt(path)


def copy_checked_out_tree(primary, view, index_path, deadline):
    """Copy checked-out files, never Git objects, untracked science or raw output.

    The initial public Actions checkout is fresh. Every ordinary file is copied
    and inventoried; all mathematical source checks remain the original ones.
    """
    count = size = 0
    with index_path.open("xb") as index:
        for root, dirs, files in os.walk(primary, followlinks=False):
            if time.time() >= deadline:
                raise TimeoutError("Original namespace science allowance exhausted in source preparation")
            root = Path(root)
            dirs[:] = sorted(d for d in dirs if d != ".git")
            for name in dirs:
                require(not (root/name).is_symlink(), "Do not redirect a source-view directory")
            target = view/root.relative_to(primary)
            target.mkdir(parents=True, exist_ok=True)
            for name in sorted(files):
                if root == primary and name == ".git":
                    continue
                source = root/name
                require(source.is_file() and not source.is_symlink(),
                    "Do not redirect an actual checked-out file")
                destination = target/name
                before = source.stat()
                h = hashlib.sha256(); copied = 0
                with source.open("rb") as src, destination.open("xb") as dst:
                    while raw := src.read(1048576):
                        dst.write(raw); h.update(raw); copied += len(raw)
                    dst.flush(); os.fsync(dst.fileno())
                after = source.stat()
                require((before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
                    == (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
                    and copied == after.st_size, "Checkout changed during exact source copying")
                shutil.copymode(source, destination)
                row = dict(file=str(source.relative_to(primary)), bytes=copied,
                    sha256=h.hexdigest())
                index.write(canonical(row))
                count += 1; size += copied
        index.flush(); os.fsync(index.fileno())
    return dict(files=count, bytes=size, complete_copy_index=receipt(index_path),
        scope="Every checked-out ordinary file except .git; source index stays temporary",
        copied_source_files_are_not_scientific_results=True)


def load_composer(comp):
    path = comp/COMPOSER["file"]
    bound(path, COMPOSER)
    alias = "_request239_actual_source_composer"
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec); sys.modules[alias] = module
    spec.loader.exec_module(module)
    require(module.HERE == comp, "The actual current composer must use the true working HERE")
    return module


def initialize(args):
    primary, temporary, base, view = context(args)
    require(args.computations.resolve() == primary/TOPIC/"computations",
        "Begin with the genuine checked-out public source directory")
    env_path = temporary/ENV_NAME
    require(not base.exists() and not view.exists() and not env_path.exists(),
        "Do not restart a previous actual namespace or metadata view")
    # The sole timestamp precedes every new source read/copy/formation.
    started = time.time()
    base.mkdir()
    out = base/OUT_NAME; out.mkdir()
    value = dict(schema=SCHEMA, repository=REPO, run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], source=receipt(__file__),
        actual_entry_request_number=239, internal220_filename_is_a_source_contract_path=True,
        internal205_number_is_a_source_contract=True,
        namespace_created_unix_seconds=started, original_namespace=str(base),
        primary_checkout=str(primary), actual_working_view=str(view),
        completed=False, actual_entry_request=None, original_frozen_request=None,
        actual_derived_request=None, original_plan=None, actual_repaired_plan=None,
        explicit_policy_JSON=None, source_copy=None, unchanged_outer_sources=[],
        actual_derived205=None, actual_composition=None, actual_job_deadline=None,
        original_checkout_files_modified=False, original_python_javascript_bytes_modified=False,
        original46_generated_output_bytes_modified=False,
        current49_bound_views_require_actual_later_materialization=True,
        scientific_computation_started=False,
        original_clock_restarted=False, error=None, raw_deleted=False)
    write_new(out/"namespace-start.json", canonical(dict(schema=SCHEMA+"-namespace-start-v1",
        repository=REPO, run_id=value["run_id"], source_commit=value["source_commit"],
        namespace_created_unix_seconds=started, original_namespace=str(base),
        source=value["source"], original_allowance_seconds=18900,
        original_readback_reserve_seconds=2700)))
    code = 2
    try:
        request, request_id = contract(args); value["actual_entry_request"] = request_id
        old_raw, old_id = bound(primary/ORIGINAL["file"], ORIGINAL)
        _, old_workflow_id = bound(primary/ORIGINAL_WORKFLOW["file"], ORIGINAL_WORKFLOW)
        value["original_frozen_workflow"] = old_workflow_id
        old_plan_raw, old_plan_id = bound(primary/TOPIC/"notes"/OLD_PLAN["file"], OLD_PLAN)
        new_plan_raw, new_plan_id = bound(primary/TOPIC/"notes"/PLAN["file"], PLAN)
        policy_raw, policy_id = bound(primary/TOPIC/"computations"/POLICY["file"], POLICY)
        value.update(original_frozen_request=old_id, original_plan=old_plan_id,
            actual_repaired_plan=new_plan_id, explicit_policy_JSON=policy_id)
        write_new(out/"frozen220-request.json", old_raw)
        write_new(out/"frozen220-source-plan.json", old_plan_raw)
        for item in FOUR:
            bound(primary/TOPIC/"computations"/item["file"], item)
        patch = request["source_plan_literal_patch"]
        before, after = patch["before"].encode("utf-8"), patch["after"].encode("utf-8")
        require(patch["count"] == 1 and old_plan_raw.count(before) == 1
            and old_plan_raw.replace(before, after) == new_plan_raw,
            "The actual repair is the single declared source-list classification edit")
        source_old, source_new = json.loads(old_plan_raw), json.loads(new_plan_raw)
        removed = [row for row in source_old["required_public_sources"] if row == POLICY]
        require(len(removed) == 1 and
            source_new["required_public_sources"] ==
                [row for row in source_old["required_public_sources"] if row != POLICY],
            "Only the explicitly bound R503 JSON leaves the source-only list")
        original_rest, new_rest = dict(source_old), dict(source_new)
        original_rest.pop("required_public_sources"); new_rest.pop("required_public_sources")
        require(original_rest == new_rest, "All46 view outputs and literal applications stay original")
        formed = old_raw.decode("utf-8")
        for row in request["derived_request_literal_patches"]:
            require(type(row["count"]) is int and row["count"] == 1
                and formed.count(row["before"]) == 1,
                "The source request literal occurrence count differs")
            formed = formed.replace(row["before"], row["after"])
        derived_raw = formed.encode("utf-8")
        require(len(derived_raw) == DERIVED["bytes"] and sha(derived_raw) == DERIVED["sha256"],
            "Use the full actual derived220 request, never relabel the frozen hash")
        old, derived = json.loads(old_raw), json.loads(derived_raw)
        require(derived["roles"] == old["roles"]
            and derived["native_registration"] == old["native_registration"]
            and derived["execution"] == old["execution"]
            and derived["refinement_work"] == old["refinement_work"],
            "No source role, mathematical work, threshold or clock changes in the original222 repair")
        value["actual_original222_request"] = request["actual_original222_request"]
        value["repaired222_source_contract"] = write_new(out/"repaired222-source-contract.json", derived_raw)
        C = load_composer(primary/TOPIC/"computations")
        derived = C.form_current_inner(derived,request["_actual239_outer"],primary)
        derived_raw = C.canonical(derived)
        current_expected = request["current_inner_contract"]
        require(all(derived[key] == current_expected[key] for key in
            ("schema","request_number","published_source_count","generated_source_count","complete_source_count")),
            "The actual formed current239 contract differs from its declared source construction")
        value["current_inner_formation_contract"] = current_expected
        value["actual_current_inner_formed_identity"] = dict(
            file=OUTER_FILE,bytes=len(derived_raw),sha256=sha(derived_raw))
        view.mkdir()
        value["source_copy"] = copy_checked_out_tree(primary, view,
            out/"copied-source-index.jsonl", started+18900)
        # This is a working metadata view of the same Git object database.
        # No branch/ref/index/checkout file is changed by this entry.
        gitdir = subprocess.check_output(["git", "-C", str(primary),
            "rev-parse", "--absolute-git-dir"], text=True, timeout=30).strip()
        require(Path(gitdir).is_dir() and "\n" not in gitdir and "\r" not in gitdir,
            "Use the existing real Git object directory")
        head = subprocess.check_output(["git", "-C", str(primary), "rev-parse", "HEAD"],
            text=True, timeout=30).strip()
        require(head == os.environ["GITHUB_SHA"], "The actual checkout head differs")
        write_new(view/".git", ("gitdir: "+gitdir+"\n").encode("utf-8"))
        actual_request = view/OUTER_FILE
        value["actual_derived_request"] = replace_metadata_copy(actual_request, old_raw, derived_raw)
        require(same(value["actual_derived_request"], value["actual_current_inner_formed_identity"]),
            "Actual current inner request bytes changed after their complete on-job formation")
        comp = view/TOPIC/"computations"
        # The old plan remains a real historical public pin alongside the new one.
        historical = comp/OLD_PLAN["file"]
        if historical.exists():
            bound(historical, OLD_PLAN)
        else:
            write_new(historical, old_plan_raw)
        for item in FOUR:
            _, actual = bound(comp/item["file"], item)
            value["unchanged_outer_sources"].append(actual)
        bound(comp/POLICY["file"], POLICY)
        os.environ["REQUEST239_PRIMARY_WORKSPACE"] = str(primary)
        os.environ["REQUEST239_RUNTIME_WORKSPACE"] = str(view)
        os.environ["GITHUB_WORKSPACE"] = str(view)
        os.environ["VISIBLE_BASE"] = str(base)
        os.environ["VISIBLE_COMPUTATIONS"] = str(comp)
        C = load_composer(comp)
        copies = C.stage_public_source_plans(view, comp, derived)
        C.write_new(base/"source-plan-copies.json", C.canonical(dict(
            repository=REPO, run_id=value["run_id"], source_commit=value["source_commit"],
            copies=copies)))
        actual_base, raw, composed = C.compose(actual_request, base, comp, value["actual_derived_request"]["sha256"])
        require(actual_base == base, "No alternate namespace is permitted")
        C.write_new(base/C.DERIVED, raw); C.write_new(base/C.RECEIPT, C.canonical(composed))
        dispatch = json.loads(raw)
        recipe_raw = (comp/"current-C-riccati-full453-physical-DN179-recipe.json").read_bytes()
        require(sha(recipe_raw) == dispatch["current_BVP_recipe"]["sha256"]
            == "d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811",
            "The original resource template recipe differs")
        policy = json.loads(recipe_raw)["execution"]
        require(policy["maximum_elapsed_science_seconds_from_namespace"] == 18900
            and policy["readback_reserve_seconds"] == 2700,
            "The original absolute resource allowance is unchanged")
        owner = dispatch["execution"]["owned_process_helper"]
        descriptor = {k:owner[k] for k in ("file", "bytes", "sha256")}
        owner_raw = C.formed_owner_source(comp, derived, descriptor)
        require(len(owner_raw) == 14823
            and sha(owner_raw) == "9e0286e556bc7035c4254e1e5d3f09d1f96164a497e63e337cd38b6ab28db9b3"
            and len(owner_raw) == descriptor["bytes"] and sha(owner_raw) == descriptor["sha256"],
            "Keep the same actual owner bootstrap bytes")
        # Exactly the existing Actions-only bootstrap syntax operation.
        import ast
        compile(ast.parse(owner_raw, filename="request205_owned_process.py"),
            "request205_owned_process.py", "exec")
        C.write_new(base/"request205_owned_process.py", owner_raw)
        deadline = dict(schema="request205-owned-job-science-deadline-v1",
            repository=REPO, run_id=value["run_id"], source_commit=value["source_commit"],
            request_sha256=sha(raw), template_recipe_sha256=sha(recipe_raw),
            namespace_created_unix_seconds=started, science_seconds_from_namespace=18900,
            readback_reserve_seconds=2700, job_timeout_minutes=360,
            resource_deadline_not_a_scientific_gate=True,
            scope="Startup resource plan before BVP; original BVP launcher enforces its actual namespace deadline",
            no_global_absolute_kill_clock_for_prior_stages=True,
            original_sampling_phase_clocks_exclude_binding_and_setup=True)
        C.write_new(base/"job-science-deadline.json", C.canonical(deadline))
        value.update(actual_derived205=receipt(base/C.DERIVED),
            actual_composition=receipt(base/C.RECEIPT),
            actual_job_deadline=receipt(base/"job-science-deadline.json"),
            actual_runtime_public_source_count=derived["published_source_count"],
            actual_runtime_generated_source_count=derived["generated_source_count"],
            actual_runtime_complete_source_count=derived["complete_source_count"],
            actual_Git_object_directory=gitdir, actual_checkout_head=head)
        script = "# Explicit request239 actual source metadata working view; source-contract bytes are bound separately.\n"
        for key, val in (
            ("REQUEST239_PRIMARY_WORKSPACE", str(primary)),
            ("REQUEST239_RUNTIME_WORKSPACE", str(view)),
            ("GITHUB_WORKSPACE", str(view)),
            ("VISIBLE_BASE", str(base)),
            ("VISIBLE_COMPUTATIONS", str(comp)),
            ("REQUEST239_CURRENT_INNER_SHA256", value["actual_derived_request"]["sha256"]),
        ):
            script += "export "+key+"="+shlex.quote(val)+"\n"
        script += "cd -- "+shlex.quote(str(view))+"\n"
        value["actual_environment_script"] = write_new(env_path, script.encode("utf-8"))
        with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as stream:
            # GitHub-reserved GITHUB_WORKSPACE is changed only by the explicit
            # sourced shell view above, never by a forbidden GITHUB_ENV override.
            for key, val in (("VISIBLE_BASE",str(base)),("VISIBLE_COMPUTATIONS",str(comp)),
                ("REQUEST239_PRIMARY_WORKSPACE",str(primary)),
                ("REQUEST239_RUNTIME_WORKSPACE",str(view)),
                ("REQUEST239_ENVIRONMENT_SCRIPT",str(env_path))):
                stream.write(key+"="+val+"\n")
        # Read the original checkpoint metadata again: it remains frozen220.
        bound(primary/ORIGINAL["file"], ORIGINAL)
        bound(primary/TOPIC/"notes"/OLD_PLAN["file"], OLD_PLAN)
        value["completed"] = True; code = 0
    except BaseException as error:
        value["error"] = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc())
        traceback.print_exc()
    result_id = write_new(out/"result.json", canonical(value))
    print(json.dumps(dict(event="request239_actual_source_metadata_view",
        result=result_id, completed=value["completed"], actual_exit=code,
        actual_derived_request=value["actual_derived_request"],
        actual_job_deadline=value["actual_job_deadline"],
        namespace_created_unix_seconds=started, scientific_computation_started=False,
        original_checkout_files_modified=False, raw_deleted=False), sort_keys=True), flush=True)
    return code


def readback(args):
    primary, temporary, base, view = context(args)
    request, rid = contract(args)
    path = base/OUT_NAME/"result.json"
    actual = receipt(path); raw = path.read_bytes(); value = json.loads(raw)
    require(len(raw) == actual["bytes"] and sha(raw) == actual["sha256"],
        "Source-preparation result changed")
    current(value)
    require(value["schema"] == SCHEMA and same(value["source"],request["entry"]),
        "Read the actual239 source preparation")
    start_path = base/OUT_NAME/"namespace-start.json"
    start_id = receipt(start_path); start = json.loads(start_path.read_bytes()); current(start)
    require(start["schema"] == SCHEMA+"-namespace-start-v1"
        and start["namespace_created_unix_seconds"] == value["namespace_created_unix_seconds"],
        "Keep the single genuine namespace origin")
    require(time.time() < start["namespace_created_unix_seconds"]+21600,
        "The original absolute readback reserve is exhausted")
    if value["completed"]:
        bound(primary/ORIGINAL["file"], ORIGINAL)
        require(value["current_inner_formation_contract"] == request["current_inner_contract"],
            "The current generated request formation contract changed")
        bound(view/OUTER_FILE, value["actual_derived_request"])
        clock_path = base/"job-science-deadline.json"
        clock_id = receipt(clock_path); clock = json.loads(clock_path.read_bytes()); current(clock)
        require(same(clock_id,value["actual_job_deadline"])
            and clock["namespace_created_unix_seconds"] == start["namespace_created_unix_seconds"]
            and clock["science_seconds_from_namespace"] == 18900
            and clock["readback_reserve_seconds"] == 2700
            and clock["request_sha256"] == value["actual_derived205"]["sha256"],
            "The actual original deadline and derived205 request do not agree")
        bound(base/"request220-derived205-dispatch.json", value["actual_derived205"])
        bound(base/"request220-composition.json", value["actual_composition"])
        bound(temporary/ENV_NAME,value["actual_environment_script"])
    summary = dict(schema=SCHEMA+"-necessary-v1", repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
        source=receipt(__file__), actual_entry_request=rid, actual_source_preparation=actual,
        namespace_start=start_id, complete_original_source_preparation_metadata=value,
        complete_necessary_readback=True, mathematical_success_not_inferred=True,
        immutable_source_metadata_only_no_process_quiet_claim=True,
        source_copy_index_full_payload_not_exported=True, raw_deleted=False)
    body = canonical(summary)
    out = base/"request239-source-binding-readback"
    require(not out.exists(), "Read this exact source-preparation scope once")
    out.mkdir()
    sid = write_new(out/"summary.json", body)
    if len(body) > LIMIT:
        print(json.dumps(dict(event="request239_source_scope_over_budget",
            original_summary=sid, maximum_bytes=LIMIT, complete_necessary_readback=False,
            no_part_transport=True, raw_retained=True)),flush=True)
        return 70
    print("BEGIN_REQUEST239_ACTUAL_SOURCE_BINDING_NECESSARY",flush=True)
    sys.stdout.buffer.write(body);sys.stdout.buffer.flush()
    print("END_REQUEST239_ACTUAL_SOURCE_BINDING_NECESSARY",flush=True)
    write_new(base/"request239-source-binding-readback-complete.json",canonical(dict(
        schema=SCHEMA+"-readback-complete-v1",repository=REPO,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        complete=True,necessary_summary={k:sid[k] for k in ("bytes","sha256")},
        source=receipt(__file__),actual_entry_request=rid,
        original_upstream_quiet_and_cleanup_predicates_still_required=True,
        mathematical_success_not_inferred=True)))
    return 0




def guard_cleanup(args, remainder):
    """A public entry reports source-preparation skips before generated cleanup.

    This never authorizes deletion on its own. After the new immutable scope
    is paid, the unchanged current same-C and original owner predicates run.
    """
    try:
        _,_,base,view=context(args)
        request,rid=contract(args)
        actual=request["_actual239_outer"]
        comp=args.computations.resolve()
        require(comp==view/TOPIC/"computations"
            and Path(os.environ["GITHUB_WORKSPACE"]).resolve()==view,
            "Use the actual239 computations for guarded cleanup")
        marker_path=base/"source-generation239-readback"/"readback-complete.json"
        marker=json.loads(marker_path.read_bytes());current(marker)
        require(marker.get("schema")=="request239-current-C-actual-source-composition-v1-generation-readback-complete-v1"
            and marker.get("complete") is True and same(marker.get("source"),COMPOSER),
            "The actual complete source-generation necessary scope is unpaid")
        summary_path=base/"source-generation239-readback"/"summary.json"
        bound(summary_path,marker["necessary_summary"])
        preparation=json.loads((base/OUT_NAME/"result.json").read_bytes());current(preparation)
        require(same(marker.get("actual_request"),preparation.get("actual_derived_request")),
            "The source-generation readback belongs to another actual inner request")
        target=actual["roles"]["composer"]
        path=comp/target["file"]
        bound(path,target)
        require(remainder and remainder[0]=="--",
            "Preserve the complete original cleanup argument suffix")
    except Exception as error:
        print(json.dumps(dict(event="request239_cleanup_skipped_before_generated_entry",
            error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc()),
            actual_generated_cleanup_not_called=True,
            original_upstream_cleanup_not_called=True,raw_deleted=False,
            process_quiet_not_inferred_from_metadata=True)),flush=True)
        return 2
    command=[sys.executable,"-u",str(path),"cleanup",
        "--request",str(args.request),"--request-sha256",args.request_sha256,
        "--base",str(args.base),"--computations",str(args.computations),
        "--new-composition-outcome",args.new_composition_outcome,
        "--new-readback-outcome",args.new_readback_outcome]+list(remainder)
    os.execv(sys.executable,command)


def cleanup(args):
    """Pay the new immutable metadata scope, then delegate unchanged raw cleanup."""
    _, _, base, view = context(args)
    request, rid = contract(args)
    marker_path = base/"request239-source-binding-readback-complete.json"
    try:
        marker = json.loads(marker_path.read_bytes()); current(marker)
        require(marker.get("schema") == SCHEMA+"-readback-complete-v1"
            and marker.get("complete") is True and same(marker.get("source"),request["entry"])
            and same(marker.get("actual_entry_request"),rid),
            "The actual repair necessary marker is absent or incomplete")
        summary = base/"request239-source-binding-readback"/"summary.json"
        bound(summary,marker["necessary_summary"])
        comp = args.computations.resolve()
        require(comp == view/TOPIC/"computations"
            and Path(os.environ["GITHUB_WORKSPACE"]).resolve() == view,
            "Delegate from the actual metadata working view")
        target = comp/request["actual_current_reader"]["file"]
        bound(target,request["actual_current_reader"])
        summary_value = json.loads(summary.read_bytes());current(summary_value)
        source_path = base/OUT_NAME/"result.json"
        _,source_id = bound(source_path,summary_value["actual_source_preparation"])
        preparation = json.loads(source_path.read_bytes());current(preparation)
        require(preparation.get("schema") == SCHEMA and preparation.get("completed") is True
            and same(preparation.get("source"),request["entry"])
            and same(preparation.get("actual_entry_request"),rid)
            and preparation["current_inner_formation_contract"] == request["current_inner_contract"],
            "Cleanup requires the actual complete generated request and its entry receipt")
        current_inner = preparation["actual_derived_request"]
        bound(view/OUTER_FILE,current_inner)
        bound(base/"refinement220-request.json",current_inner)
    except Exception as error:
        print(json.dumps(dict(event="request239_cleanup_skipped",
            error=dict(type=type(error).__name__,message=str(error)),
            original_upstream_cleanup_not_called=True,raw_deleted=False,
            only_runner_destruction_remains=True)),flush=True)
        return 2
    os.execv(sys.executable,[sys.executable,"-u",str(target),"cleanup",
        "--request",str(base/"refinement220-request.json"),
        "--request-sha256",current_inner["sha256"],"--base",str(base),
        "--computations",str(comp)])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("initialize","readback","cleanup","guard-cleanup"))
    for name in ("request","base","computations"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--request-sha256",required=True)
    parser.add_argument("--new-composition-outcome",default="unknown")
    parser.add_argument("--new-readback-outcome",default="unknown")
    args,remainder=parser.parse_known_args(argv)
    if args.command=="guard-cleanup":
        return guard_cleanup(args,remainder)
    require(not remainder,"Unexpected source-entry arguments")
    if args.command=="initialize":
        return initialize(args)
    if args.command=="cleanup":
        return cleanup(args)
    return readback(args)


if __name__=="__main__":
    raise SystemExit(main())
