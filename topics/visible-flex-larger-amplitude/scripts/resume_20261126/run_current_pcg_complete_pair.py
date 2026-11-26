#!/usr/bin/env python3
"""Run the full current-PCG science and pure reader in one public admission.

The only runtime parameter rule is explicit inheritance of the two finite
positive final damping values from this runner's completed, source-bound
restart report. Full norm, loss, original inputs and checkpoint identities are
verified first; every other declared argv entry is retained. The original
a0e/333e/0d65 scientific and pure sources are not modified. A nonzero scientific
child still permits the declared pure reader. No hard job limit is extended,
missing result inferred, or field/continuous certificate claimed.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import math
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone

SCHEMA = "actual-complete-current-PCG-inherited-damping-science-reader-pair-v1"
PARAMETER_SCHEMA = "complete-current-PCG-inherited-damping-science-reader-parameters-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
PINS = {
    "launcher": (
        TOPIC+"/scripts/resume_20261126/launch_so3_cached_current_pcg_soc.py",
        "333ea5c5f9c06b434c4f16fcb8e93ec202d7f40decf819c152e26ddcef3257e2"),
    "reader": (
        TOPIC+"/scripts/resume_20261126/read_so3_cached_current_pcg_soc_report.py",
        "0d659ab94bff7fe12337cc8f1eb18263ae1623f8fb8bcbb40108e7e03ad3856f"),
    "driver": (
        TOPIC+"/scripts/resume_20261126/fullclosed_so3_cached_current_pcg_soc.py",
        "a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743"),
    "predecessor_deriver": (
        TOPIC+"/scripts/resume_20261126/derive_normalized_parent_cached_soc.py",
        "424311d2a85ab74e14a8aeb3bdb3a0bf4f4cad07fd0abee6e4c4adef6113bacd"),
    "current_deriver": (
        TOPIC+"/scripts/resume_20261126/derive_so3_cached_current_pcg_soc.py",
        "6420bb73edad599da723001fff95c4ab9c64ccecff6e2459cf1fc85a20209d3e"),
    "fixed_parent_binding": (
        TOPIC+"/scripts/resume_20261126/so3_same_parent_fixed_scalar_binding.py",
        "9ca39afd9f840ba89fbb75d7365220c2d85d26ddb26b2d66b6c55e611313fd55"),
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2,
        allow_nan=False)+"\n", encoding="utf-8")
    temporary.replace(path)


def one(arguments, name):
    if arguments.count(name) != 1:
        raise ValueError("Retain exactly one complete argument: "+name)
    i = arguments.index(name)
    if i+1 == len(arguments):
        raise ValueError("Missing value for "+name)
    return arguments[i+1]


def render(value, repo, work):
    if not isinstance(value, str) or "\x00" in value:
        raise ValueError("Every complete argv entry must be a plain text string")
    result = value.replace("{repo}", str(repo)).replace("{work}", str(work))
    if "{repo}" in result or "{work}" in result:
        raise ValueError("A declared source/work placeholder was not rendered")
    return result


def inside_work(path, work, repo):
    value = Path(path).resolve()
    if value == work or work not in value.parents:
        raise ValueError("Every newly produced output must be inside this runner work tree")
    if value == repo or repo in value.parents:
        raise ValueError("Raw output cannot be written into the repository")
    return value


def output_records(paths):
    result = []
    for path in paths:
        path = Path(path)
        if path.is_file():
            result.append(dict(path=str(path), exists=True, bytes=path.stat().st_size,
                sha256=sha(path)))
        else:
            result.append(dict(path=str(path), exists=False))
    return result



def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def load_pure(source, name):
    path = Path(source["path"])
    if sha(path) != source["sha256"]:
        raise ValueError("The complete pure source changed before loading")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def finite_positive(value, name):
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or not math.isfinite(value) or value <= 0):
        raise ValueError("Need the actual finite positive parent value: "+name)
    return float(value)


def bind_damping_from_parent(repo, work, sources, science_args, parent, parameter):
    """Read existing metadata only; no model, F, J, norm or QP is evaluated."""
    expected_policy = {
        "--damping": {"placeholder": "{actual_parent_final_damping}",
            "report_field": "final_damping"},
        "--restoration-damping": {
            "placeholder": "{actual_parent_final_restoration_damping}",
            "report_field": "final_restoration_damping"},
    }
    if parameter.get("damping_inheritance") != expected_policy:
        raise ValueError("Use the complete explicit two-value inheritance policy")
    report_path = Path(one(science_args, "--restart-report")).resolve()
    if work not in report_path.parents or not report_path.is_file():
        raise ValueError("The actual same-run completed restart report is required")
    raw = report_path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    report = json.loads(raw)
    source_pairs = {
        "complete-normalized-parent-cached-interior-separated-SOC-v1":
            ("892f349b140f9a77fde37fc490d7cbb078cfdb21f8b31b7743e50ec6cf5712a8",
             "predecessor_deriver"),
        "complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1":
            ("a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743",
             "current_deriver"),
    }
    pair = source_pairs.get(report.get("schema"))
    if pair is None or report.get("source_sha256") != pair[0]:
        raise ValueError("Use an explicitly supported complete source/schema parent")
    deriver = load_pure(sources[pair[1]], "_complete_current_PCG_pair_parent_deriver")
    source_binding = deriver.bind_report(repo, report_path)
    if source_binding.get("actual_entire_body_match") is not True:
        raise ValueError("The actual entire parent body was not bound")
    if (report.get("complete") is not True
            or report.get("final_bundle_sha256") != sha(parent)
            or str(report.get("github_run_id")) != os.environ.get("GITHUB_RUN_ID")):
        raise ValueError("Use this runner's actual complete parent checkpoint/report")
    fixed_binder = load_pure(sources["fixed_parent_binding"],
        "_complete_current_PCG_pair_fixed_parent_binding")
    fixed_profile = fixed_binder.verify_saved_binding(report,
        expected_binding_source_sha256=sources["fixed_parent_binding"]["sha256"])
    model = report.get("representation")
    if (not isinstance(model, dict)
            or canonical(model) != report.get("model_identity_sha256")
            or model.get("fixed_scalar_metric_identity_sha256") != fixed_profile):
        raise ValueError("The full actual parent model/target identity changed")
    inputs = (
        ("--parent-bundle", report.get("bundle_sha256")),
        ("--parent-report", report.get("original_parent_report", {}).get("sha256")),
        ("--carrier", report.get("observation_carrier_sha256")),
        ("--node-report", report.get("exact_tail_node_report_sha256")),
        ("--scalar-input", report.get("exact_tail_scalar_input_sha256")),
    )
    input_records = {}
    for flag, expected in inputs:
        path = Path(one(science_args, flag)).resolve()
        if work not in path.parents or not path.is_file() or sha(path) != expected:
            raise ValueError("Keep the actual complete restart input: "+flag)
        input_records[flag] = {"path": str(path), "sha256": expected}
    norm = report.get("coordinate_norm")
    if not isinstance(norm, dict):
        raise ValueError("The complete parent coordinate norm is absent")
    definition = dict(norm)
    norm_identity = definition.pop("norm_identity_sha256", None)
    if canonical(definition) != norm_identity:
        raise ValueError("The complete parent norm identity is inconsistent")
    if norm.get("norm_kind") != one(science_args, "--norm-kind"):
        raise ValueError("Do not migrate damping across different norms")
    for key, flag in (("radial_length", "--radial-norm-length"),
            ("angular_transition", "--angular-transition")):
        if finite_positive(norm.get(key), key).hex() != float(one(science_args, flag)).hex():
            raise ValueError("Do not migrate damping across changed norm parameters")
    spectral = report.get("spectral_parameters", {})
    if (spectral.get("p") != int(one(science_args, "--spectral-p"))
            or report.get("selected_scalar_objective_key") != "centered_phi_normalized"):
        raise ValueError("Keep the actual same loss/objective units")
    for key, flag in (("epsilon", "--spectral-epsilon"), ("scale", "--spectral-scale")):
        if finite_positive(spectral.get(key), key).hex() != float(one(science_args, flag)).hex():
            raise ValueError("Do not migrate damping across changed spectral parameters")
    if (finite_positive(report.get("radial_weights", {}).get("legacy_fraction"),
            "legacy_fraction").hex() != float(one(science_args, "--legacy-fraction")).hex()
            or report.get("N") != int(one(science_args, "--angles"))):
        raise ValueError("Keep the same complete positive observation measure")
    declared_manifests = [Path(science_args[i+1]).resolve()
        for i, value in enumerate(science_args[:-1]) if value == "--manifest"]
    if report_path not in declared_manifests:
        raise ValueError("Keep the entire actual restart report as an explicit history manifest")
    before = list(science_args)
    actual = {}
    for flag, policy in expected_policy.items():
        if one(science_args, flag) != policy["placeholder"]:
            raise ValueError("Do not substitute an unobserved literal damping for the declared inheritance")
        value = finite_positive(report.get(policy["report_field"]), policy["report_field"])
        index = science_args.index(flag)+1
        science_args[index] = repr(value)
        actual[flag] = {"report_field": policy["report_field"],
            "value": value, "binary64_hex": value.hex(), "actual_argument": repr(value)}
    expected_changed = {before.index(flag)+1 for flag in expected_policy}
    if {i for i, (a, b) in enumerate(zip(before, science_args)) if a != b} != expected_changed:
        raise ValueError("Only the two declared damping placeholders may be filled")
    if sha(report_path) != digest or sha(parent) != report.get("final_bundle_sha256"):
        raise ValueError("The complete parent changed during metadata binding")
    return dict(report=dict(path=str(report_path), bytes=len(raw), sha256=digest),
        source_schema=report["schema"], source_sha256=report["source_sha256"],
        complete_parent_body_binding=source_binding,
        actual_checkpoint_sha256=report["final_bundle_sha256"],
        actual_current_run_id=report["github_run_id"],
        model_identity_sha256=report["model_identity_sha256"],
        fixed_scalar_metric_identity_sha256=fixed_profile,
        norm_identity_sha256=norm_identity,
        spectral_parameters=spectral,
        same_norm_loss_and_complete_inputs_required=True,
        complete_inputs=input_records, damping_arguments=actual,
        scientific_arrays_recomputed=False, field_calls=0, J_calls=0,
        scientific_modules_imported=False,
        future_reconstructed_values_not_presupposed=True)


def prepare(args):
    repo, work = args.repo.resolve(), args.work.resolve()
    if not repo.is_dir() or not work.is_dir():
        raise ValueError("Use the actual source checkout and existing runner work tree")
    if work == repo or repo in work.parents:
        raise ValueError("The runner scientific work tree must be outside the source checkout")
    parameter_path = args.parameters.resolve()
    if parameter_path == repo or repo not in parameter_path.parents:
        raise ValueError("Use the complete published parameter file in the source checkout")
    raw = parameter_path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != args.parameters_sha256:
        raise ValueError("The complete declared parameter bytes changed")
    parameter = json.loads(raw)
    if parameter.get("schema") != PARAMETER_SCHEMA:
        raise ValueError("Use the complete bound pair parameter schema")
    steps = parameter.get("steps")
    if not isinstance(steps, list) or len(steps) != 2:
        raise ValueError("Keep exactly the complete scientific and pure steps")
    sources = {}
    for role, (relative, expected) in PINS.items():
        path = (repo/relative).resolve()
        if repo not in path.parents or sha(path) != expected:
            raise ValueError("The complete bound source changed: "+role)
        sources[role] = dict(path=str(path), repository_relative_path=relative,
            sha256=expected)
    commands, outputs = [], []
    for role, step in zip(("launcher", "reader"), steps):
        if (not isinstance(step, dict)
                or step.get("script") != PINS[role][0]
                or not isinstance(step.get("id"), str)
                or not isinstance(step.get("args"), list)
                or not isinstance(step.get("outputs"), list)):
            raise ValueError("The complete step identity/source/argv/output declaration is absent")
        arguments = [render(x, repo, work) for x in step["args"]]
        if Path(one(arguments, "--repo")).resolve() != repo:
            raise ValueError("A child cannot silently use a different source checkout")
        commands.append([sys.executable, "-u", sources[role]["path"], *arguments])
        actual_outputs = []
        for relative in step["outputs"]:
            if not isinstance(relative, str) or Path(relative).is_absolute():
                raise ValueError("Declared child outputs must be relative to the actual work tree")
            actual_outputs.append(inside_work(work/relative, work, repo))
        if len(actual_outputs) != len(set(actual_outputs)):
            raise ValueError("A declared child output is duplicated")
        outputs.append(actual_outputs)
    if set(outputs[0]) & set(outputs[1]):
        raise ValueError("The pure child must not overwrite any scientific output")
    science_args, pure_args = commands[0][3:], commands[1][3:]
    science_dir = inside_work(one(science_args, "--outdir"), work, repo)
    scientific_report = science_dir/"report.json"
    pure_report = inside_work(one(pure_args, "--report"), work, repo)
    pure_output = inside_work(one(pure_args, "--output"), work, repo)
    if pure_report != scientific_report or scientific_report not in outputs[0]:
        raise ValueError("The pure child must read exactly this new scientific report")
    if pure_output not in outputs[1]:
        raise ValueError("Keep the actual pure output in its complete declaration")
    if pure_args.count("--verify-final-bundle") != 1 or pure_args.count("--verify-cache-files") != 1:
        raise ValueError("Retain both original complete final-bundle and cache-file checks")
    output = inside_work(args.output, work, repo)
    all_outputs = [x for group in outputs for x in group]
    if output in all_outputs or parameter_path == output:
        raise ValueError("The pair status must not overwrite any child result or parameter")
    if any(path.exists() for path in [output, *all_outputs]):
        raise FileExistsError("Use fresh pair and child outputs; this wrapper does not replay a returned child")
    declared_parent = steps[0].get("parent_bundle")
    if (not isinstance(declared_parent, str)
            or steps[1].get("parent_bundle") != declared_parent
            or Path(declared_parent).is_absolute()):
        raise ValueError("Both steps must retain the same already existing admission parent")
    parent = (work/declared_parent).resolve()
    restart = Path(one(science_args, "--restart-checkpoint")).resolve()
    if parent != restart or work not in parent.parents or not parent.is_file():
        raise ValueError("The admission parent must be the actual complete restart checkpoint")
    damping_binding = bind_damping_from_parent(repo, work, sources,
        science_args, parent, parameter)
    commands[0][3:] = science_args
    return dict(repo=repo, work=work, output=output, parameter=parameter,
        actual_damping_binding=damping_binding,
        parameter_path=parameter_path, parameter_sha256=digest,
        sources=sources, commands=commands, outputs=outputs,
        parent=dict(path=str(parent), sha256=sha(parent)),
        scientific_report=scientific_report, pure_output=pure_output)


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("The complete scientific pair executes only in the actual public repository Actions")


def run_pair(prepared):
    require_actions()
    report = dict(schema=SCHEMA, source_sha256=sha(__file__),
        started_utc=utc(), complete=False, both_children_returned=False,
        scientific_success=False, pure_success=False,
        parameter_file=dict(path=str(prepared["parameter_path"]),
            sha256=prepared["parameter_sha256"]),
        complete_source_bindings=prepared["sources"], actual_admission_parent=prepared["parent"],
        scientific_sources_changed_by_wrapper=False,
        only_declared_actual_parent_damping_placeholders_filled=True,
        actual_damping_binding=prepared["actual_damping_binding"],
        other_declared_numerical_arguments_changed=False,
        extends_actions_hard_job_limit=False,
        new_scientific_report_not_parsed_by_wrapper=True,
        completed_parent_metadata_read_without_scientific_execution=True,
        scientific_field_or_continuous_certificate_claimed=False,
        children=[])
    start = time.monotonic()
    save(prepared["output"], report)
    for index, (role, command, output_paths) in enumerate(zip(
            ("scientific_launcher", "pure_reader"),
            prepared["commands"], prepared["outputs"])):
        child = dict(index=index, role=role,
            declared_step_id=prepared["parameter"]["steps"][index]["id"],
            command=command, started_utc=utc(), state="running",
            returncode=None, science_is_not_rerun_by_pure_reader=index == 1)
        report["children"].append(child)
        save(prepared["output"], report)
        print(json.dumps(dict(event="bound_pair_child_start", role=role,
            declared_step_id=child["declared_step_id"]), sort_keys=True), flush=True)
        child_start = time.monotonic()
        try:
            result = subprocess.run(command, check=False)
            child.update(state="returned", returncode=result.returncode)
        except OSError as error:
            child.update(state="launch_failed", error=repr(error))
        except BaseException as error:
            child.update(state="interrupted", error=repr(error),
                seconds=time.monotonic()-child_start, ended_utc=utc())
            report.update(total_seconds=time.monotonic()-start,
                interrupted=True, interrupted_utc=utc())
            save(prepared["output"], report)
            raise
        child.update(seconds=time.monotonic()-child_start, ended_utc=utc(),
            outputs=output_records(output_paths))
        report["scientific_success" if index == 0 else "pure_success"] = child["returncode"] == 0
        save(prepared["output"], report)
        print(json.dumps(dict(event="bound_pair_child_return", role=role,
            returncode=child["returncode"], state=child["state"],
            seconds=child["seconds"]), sort_keys=True), flush=True)
    report.update(complete=True,
        both_children_returned=all(x["state"] == "returned" for x in report["children"]),
        all_declared_children_attempted=True, ended_utc=utc(),
        total_seconds=time.monotonic()-start,
        scientific_report=output_records([prepared["scientific_report"]])[0],
        pure_output=output_records([prepared["pure_output"]])[0])
    save(prepared["output"], report)
    print(json.dumps(dict(event="bound_pair_return", output=str(prepared["output"]),
        scientific_success=report["scientific_success"],
        pure_success=report["pure_success"],
        total_seconds=report["total_seconds"]), sort_keys=True), flush=True)
    return 0 if report["scientific_success"] and report["pure_success"] else 1


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--parameters", type=Path, required=True)
    parser.add_argument("--parameters-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--print-only", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    prepared = prepare(args)
    if args.print_only:
        print(json.dumps(dict(schema=SCHEMA, executed=False,
            complete_source_bindings=prepared["sources"],
            parameter_sha256=prepared["parameter_sha256"],
            commands=prepared["commands"],
            outputs=[[str(x) for x in group] for group in prepared["outputs"]],
            actual_admission_parent=prepared["parent"],
            actual_damping_binding=prepared["actual_damping_binding"]), indent=2, sort_keys=True))
        return 0
    return run_pair(prepared)


if __name__ == "__main__":
    raise SystemExit(main())

