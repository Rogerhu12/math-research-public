#!/usr/bin/env python3
"""R518 explicit live128 radial-cache source views in the actual checkout.

This program performs only source/JSON/identity preparation. It does not import
or execute a scientific module, compile a translation unit, start a solver, or
create a scientific clock. The frozen221 component contract is an ancestor;
its new complete request bytes are bound by their actual returned SHA.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

HERE = Path(__file__).resolve().parent
REPO = "Rogerhu12/math-research-public"
TOPIC = Path("topics/visible-flex-larger-amplitude")
SCHEMA = "R518-live128-radial-cache-source-view-preparation-v1"
PLAN_SCHEMA = "R518-live128-radial-cache-complete-source-plan-v1"
REQUEST_SCHEMA = "R518-live128-cached-radial-original-full112-component-contract-v1"
NAMESPACE = "visible-live128-cached-radial-R518"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")
ORIGINAL_REQUEST = dict(file="public-live128-scoped-original-full112-FD-fullDN-request.json",
    bytes=54884, sha256="0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e")
MAX_BYTES = 90000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii")+b"\n"


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def receipt(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=sha(path))


def checked(path, expected, label):
    path = Path(path)
    require(not path.is_symlink() and path.is_file(), label+": actual regular file")
    require(path.stat().st_size == expected["bytes"] and sha(path) == expected["sha256"],
            label+": complete bytes/SHA")
    return path.resolve(strict=True)


def basename(name):
    require(isinstance(name, str) and name and Path(name).name == name
            and name not in (".", "..") and "\x00" not in name,
            "An explicit single source basename")
    return name


def atomic_json(path, value, replace=False):
    path = Path(path)
    temporary = path.with_name(path.name+".writing")
    require(not temporary.exists() and (replace or not path.exists()),
            "Exclusive source-metadata output")
    with temporary.open("xb") as stream:
        stream.write(canonical(value))
    os.replace(temporary, path)


def run_identity():
    return {key:os.environ.get(key) for key in RUN_KEYS}


def request_view(original, plan, plan_id, generation_receipt_path, sources):
    # All original numerical inputs, scientific policy and resource values
    # remain the same JSON objects; only the explicitly listed metadata changes.
    result = dict(original)
    result.update(schema=REQUEST_SCHEMA,
        operation="R518 source component: frozen221 original full112/live128 with the R515 local physical radial-mode cache",
        namespace=NAMESPACE,
        execution_entry=plan["roles"]["runtime"],
        scientific_entry=plan["roles"]["fullDN"],
        necessary_reader=plan["roles"]["necessary"],
        source_sha256=sources)
    result["source_contract"] = dict(
        inherited_frozen221_source_contract=original["source_contract"],
        original_public_pin_count=len(original["source_sha256"]),
        additional_public_pin_count=len(plan["additional_public_sources"]),
        generated_source_count=len(plan["views"]),
        explicit_source_pin_count=len(sources),
        original_336_file_words_retained=True,
        public_metadata_file_is_not_misclassified_as_executable_source=True,
        complete_original_math_inputs_and_policy_unchanged=True,
        R515_source_change_is_not_an_acceptance_claim=True,
        actual_generated_sources_live_in_original_computations=True,
        local_scientific_import_compile_AST_or_test_performed=False)
    result["R518_source_composition"] = dict(
        schema=SCHEMA+"-component-contract-binding",
        original_request=ORIGINAL_REQUEST,
        original_published_source_ref=plan["original_published_source_ref"],
        plan=plan_id, generator=receipt(__file__),
        generation_receipt_file=str(generation_receipt_path),
        actual_checkout_source=os.environ["GITHUB_SHA"],
        component_request_number=original["request_number"],
        component_number_is_only_frozen221_internal_identifier=True,
        no_new_public_request_number_or_actual_run_is_assigned_by_this_component=True,
        actual_inputs_and_success_never_inferred_from_source_identity=True)
    result["results"] = dict(inherited_frozen221_results_metadata=original["results"],
        source_composition="R518", local_cache_source_theorem="R515",
        new_actual_result_or_acceptance_not_assigned=True)
    result["publication"] = dict(inherited_frozen221_publication_metadata=original["publication"],
        source_component_only=True, no_workflow_or_dispatch_performed=True)
    return result


def prepare(args):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "Only the actual public repository Actions job prepares these views")
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(HERE == workspace/TOPIC/"computations",
            "Every generated loader has its true original HERE and repository parents")
    actual_head = subprocess.check_output(
        ["git", "-C", str(workspace), "rev-parse", "HEAD"], text=True).strip()
    require(actual_head == os.environ["GITHUB_SHA"], "The actual source checkout head")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    supplied = args.out
    require(supplied.is_absolute() and ".." not in supplied.parts and not supplied.is_symlink(),
            "An actual absolute source-metadata directory")
    out = supplied.resolve()
    require(out.parent == runner and out.name == "R518-live128-source-view-metadata"
            and not out.exists(), "One fresh explicit source-metadata directory")
    out.mkdir(mode=0o700)
    report_path = out/"source-views.json"
    record = dict(schema=SCHEMA, run=run_identity(), source=receipt(__file__),
        actual_checkout=str(workspace), actual_computations=str(HERE),
        complete=False, scientific_module_imported=False, compiler_started=False,
        numerical_function_evaluated=False, scientific_clock_created=False,
        original_public_files_modified=False, original_frozen221_request_modified=False,
        namespace_science_started=False, public_inputs_verified=[],
        generated=[], ungenerated_view_roles=[], derived_request=None, error=None)
    atomic_json(report_path, record)
    try:
        plan_path = args.plan.resolve(strict=True)
        require(not args.plan.is_symlink() and sha(plan_path) == args.plan_sha256,
                "The complete explicitly supplied source plan SHA")
        plan = json.loads(plan_path.read_bytes())
        require(plan["schema"] == PLAN_SCHEMA, "The R518 full source plan")
        checked(__file__, plan["generator"], "The declared source generator")
        require(plan["baseline_request"] == ORIGINAL_REQUEST,
                "The exact frozen221 request ancestor")
        record["plan"] = receipt(plan_path)
        ancestor = checked(args.upstream_request, ORIGINAL_REQUEST, "Frozen221 request")
        require(ancestor == HERE/ORIGINAL_REQUEST["file"],
                "The unchanged original request remains at its actual Git path")
        original = json.loads(ancestor.read_bytes())
        require(original["schema"] == "public-live128-scoped-original-full112-FD-fullDN-request-v1"
                and original["request_number"] == 221 and original["repository"] == REPO
                and len(original["source_sha256"]) == 336,
                "The complete original component contract")
        record["original_request"] = receipt(ancestor)
        public = dict(original["source_sha256"])
        for row in plan["additional_public_sources"]:
            name = basename(row["file"])
            require(name not in public, "A separately named new public dependency")
            public[name] = row["sha256"]
        require(len(public) == plan["counts"]["public_files"],
                "Actual public union cardinality")
        for name, digest in public.items():
            name = basename(name)
            path = HERE/name
            require(not path.is_symlink() and path.is_file() and sha(path) == digest,
                    "Complete actual public dependency: "+name)
            record["public_inputs_verified"].append(receipt(path))
        for row in plan.get("published_metadata_dependencies", []):
            relative = Path(row["file"])
            require(not relative.is_absolute() and ".." not in relative.parts,
                    "Declared original repository metadata path")
            path = checked(workspace/relative, row, "Complete published plan metadata")
            record.setdefault("published_metadata_verified", []).append(receipt(path))
        views = plan["views"]
        require(len(views) == plan["counts"]["generated_files"], "All declared new views")
        record["ungenerated_view_roles"] = [row["role"] for row in views]
        changed_sources = {}
        expected_names = set()
        prepared = []
        for view in views:
            source = HERE/basename(view["baseline"]["file"])
            checked(source, view["baseline"], "Unmodified full view baseline")
            require(public.get(source.name) == view["baseline"]["sha256"],
                    "Every view begins with its pinned public original file")
            output = view["output"]
            name = basename(output["file"])
            target = HERE/name
            require(name not in public and name not in expected_names and not target.exists()
                    and not target.is_symlink(), "A fresh independent generated source name")
            expected_names.add(name)
            text = source.read_bytes().decode("utf-8")
            patch_receipts = []
            for patch in view["patches"]:
                require(isinstance(patch["before"], str) and patch["before"]
                        and isinstance(patch["after"], str)
                        and type(patch["count"]) is int and patch["count"] > 0,
                        "One explicit literal source substitution")
                require(text.count(patch["before"]) == patch["count"],
                        "Complete original substitution count: "+view["role"]+"/"+patch["id"])
                text = text.replace(patch["before"], patch["after"])
                patch_receipts.append(dict(id=patch["id"], count=patch["count"],
                    before_sha256=hashlib.sha256(patch["before"].encode("utf-8")).hexdigest(),
                    after_sha256=hashlib.sha256(patch["after"].encode("utf-8")).hexdigest()))
            raw = text.encode("utf-8")
            require(len(raw) == output["bytes"] and hashlib.sha256(raw).hexdigest() == output["sha256"],
                    "The complete final generated source: "+name)
            prepared.append((view, target, raw, patch_receipts))
            changed_sources[name] = output["sha256"]
        require(len(changed_sources) == plan["counts"]["generated_files"],
                "The full distinct generated source set")
        # These are source identity checks, not scientific validation calls.
        for view, target, raw, patch_receipts in prepared:
            with target.open("xb") as stream:
                stream.write(raw)
            record["generated"].append(dict(role=view["role"],
                baseline=receipt(HERE/view["baseline"]["file"]),
                actual=receipt(target), literal_substitutions=patch_receipts))
            record["ungenerated_view_roles"].remove(view["role"])
            atomic_json(report_path, record, replace=True)
        sources = dict(public)
        sources.update(changed_sources)
        require(len(sources) == plan["counts"]["complete_files"],
                "The complete actual public plus generated union")
        derived = request_view(original, plan, record["plan"], report_path, sources)
        derived_path = out/"derived-component-contract.json"
        atomic_json(derived_path, derived)
        record["derived_request"] = receipt(derived_path)
        record["derived_request_schema"] = derived["schema"]
        record["frozen_internal_component_number"] = 221
        record["actual_namespace_for_original_lifecycle"] = str(runner/NAMESPACE)
        record["source_count"] = dict(public=len(public), generated=len(changed_sources),
                                     complete=len(sources))
        record["complete"] = True
        atomic_json(report_path, record, replace=True)
        env = dict(R518_COMPONENT_REQUEST=str(derived_path),
            R518_COMPONENT_REQUEST_SHA256=record["derived_request"]["sha256"],
            R518_COMPONENT_RUNTIME=str(HERE/plan["roles"]["runtime"]),
            R518_COMPONENT_READER=str(HERE/plan["roles"]["necessary"]),
            R518_COMPONENT_NAMESPACE=str(runner/NAMESPACE),
            R518_SOURCE_VIEW_RECEIPT=str(report_path))
        if os.environ.get("GITHUB_ENV"):
            with open(os.environ["GITHUB_ENV"], "a") as stream:
                for key, value in env.items():
                    require("\n" not in value and "\r" not in value, "One environment value per line")
                    stream.write(key+"="+value+"\n")
        return record, 0
    except Exception as error:
        record["complete"] = False
        record["error"] = dict(type=type(error).__name__, message=str(error),
                              traceback=traceback.format_exc())
        atomic_json(report_path, record, replace=True)
        return record, 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--plan-sha256", required=True)
    parser.add_argument("--upstream-request", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        result, code = prepare(args)
    except Exception as error:
        result = dict(schema=SCHEMA, run=run_identity(), complete=False,
            source=receipt(__file__), scientific_module_imported=False,
            numerical_function_evaluated=False, scientific_clock_created=False,
            error=dict(type=type(error).__name__, message=str(error), traceback=traceback.format_exc()))
        code = 2
    full_path = args.out/"source-views.json"
    selected = {key:result[key] for key in (
        "schema","run","source","actual_checkout","actual_computations","complete",
        "scientific_module_imported","compiler_started","numerical_function_evaluated",
        "scientific_clock_created","original_public_files_modified",
        "original_frozen221_request_modified","namespace_science_started",
        "plan","original_request","published_metadata_verified","derived_request",
        "derived_request_schema","frozen_internal_component_number",
        "actual_namespace_for_original_lifecycle","source_count",
        "ungenerated_view_roles","error") if key in result}
    selected["actual_verified_public_dependency_count"] = len(result.get("public_inputs_verified",[]))
    selected["generated"] = result.get("generated",[])
    selected["necessary_scope"] = dict(
        complete_new_source_outputs_and_literal_substitution_receipts_returned=True,
        original_public_input_rows_remain_in_complete_local_receipt=True,
        original_public_pin_map_bound_by_complete_frozen221_request=True,
        no_scientific_output_claimed_read_or_generated=True)
    if full_path.is_file():
        selected["complete_local_source_preparation_receipt"] = receipt(full_path)
    raw = canonical(selected)
    if len(raw) > MAX_BYTES:
        raw = canonical(dict(schema=SCHEMA, run=run_identity(), complete=False,
            source_preparation_returned=result.get("complete") is True,
            complete_local_receipt=str(args.out/"source-views.json"),
            necessary_metadata_returned=False, transport_exit_code=70,
            unreturned_bytes=len(raw), unreturned_sha256=hashlib.sha256(raw).hexdigest(),
            no_prefix_segments_or_encoded_tree_returned=True,
            source_success_is_not_scientific_success=True))
        code = 70
    print("BEGIN_R518_SOURCE_VIEW_PREPARATION", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_R518_SOURCE_VIEW_PREPARATION", flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
