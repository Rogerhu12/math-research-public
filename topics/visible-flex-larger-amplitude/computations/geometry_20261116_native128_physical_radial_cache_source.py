#!/usr/bin/env python3
"""R515 explicit physical128 radial-mode cache source adapter.

This is an Actions-only compiler-input adapter. The original owner, stage,
boundary and every numerical threshold are unchanged. Only an actual R493
physical translation unit receives the three declared source substitutions.
The upstream factory receipt is retained as prepared ancestry; the original
process manager executes only the final compiler command returned here.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SCHEMA = "R515-physical128-finite-radial-mode-cache-source-composition-v1"
BASE = "geometry_20261116_native128_live_scalar_source.py"
BASE_SHA = "06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b"
MARKER = "LIVE128_RADIAL_MODE_CACHE_SOURCE "
PLAN = json.loads(r'''{
  "schema": "R515-original-physical128-finite-radial-mode-cache-source-plan-v1",
  "upstream": {
    "published_source_ref": "f0c787340f29734e17c9428ba7588e2a58ae665e",
    "factory": {
      "file": "geometry_20261116_native128_live_scalar_source.py",
      "bytes": 15897,
      "sha256": "06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b"
    },
    "public_cpp": {
      "file": "geometry_20261115_native_physical_final128.cpp",
      "bytes": 18055,
      "sha256": "a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415"
    },
    "qualified_cpp_sha256": "ecf14bf4d5cfd7a9f7796d0fa513822a05ca6cdc5a3ecc291859cff58a91b265",
    "unchanged_physical_header": {
      "file": "geometry_20261115_native_physical128.hpp",
      "bytes": 12683,
      "sha256": "4b0569a245147e346149d462d974a80cac853bcf9d5abf13700b743acd33af35"
    },
    "unchanged_shared_header": {
      "file": "geometry_20261115_native_shared_trace128.hpp",
      "bytes": 13605,
      "sha256": "bcca73719ffb98d5d0aed5bc4c88c789343be048475aae22a3b495097f345c6b"
    }
  },
  "baseline": {
    "file": "geometry_20261116_native_physical_live_scalar128.cpp",
    "bytes": 19958,
    "sha256": "5f6b2d3c641befb6816c3e411ba00b7faf6eb3407b210f8b4c68b1c655746502",
    "storage_kind": "actual_R493_factory_generated_source_not_a_public_Git_file"
  },
  "additional_source": {
    "file": "geometry_20261116_native_physical_radial_mode_cache128.hpp",
    "bytes": 5253,
    "sha256": "959d43bffc27665f30dffe4e98bb00fc007ee10fc3f3e519589c0c3d854fcd51"
  },
  "patches": [
    {
      "id": "actual-include",
      "before": "#include \"geometry_20261115_native_physical128.hpp\"",
      "after": "#include \"geometry_20261116_native_physical_radial_mode_cache128.hpp\"",
      "count": 1
    },
    {
      "id": "all-three-actual-cut-queries",
      "before": "cut_readout(p,physical,",
      "after": "cut_readout_radial_mode_cache(p,physical,",
      "count": 3
    },
    {
      "id": "complete-audit-query",
      "before": "physical_jets(p,physical,",
      "after": "physical_jets_radial_mode_cache(p,physical,",
      "count": 1
    }
  ],
  "output": {
    "file": "geometry_20261116_native_physical_live_scalar_mode_cache128.cpp",
    "bytes": 20048,
    "sha256": "c0364bcdb302c0909d31ae4737257891640eeb25c91b56c9f646006bc9f47ea8"
  },
  "scope": {
    "current_owner_and_fresh_replay_cpp_unchanged": true,
    "all_576_by_224_stage_math_unchanged": true,
    "complete_226_rows_and_two_means_preserved": true,
    "complete_338_by_112_original_mixed_endpoint_preserved": true,
    "all_actual_independent_audit_queries_preserved": true,
    "only_finite_per_call_radial_mode_words_shared": true,
    "all_original_angular_additions_and_C_solve_unchanged": true,
    "zero_j_elision_or_trigonometric_identity_used": false,
    "cross_call_cache": false,
    "new_scientific_acceptance_gate": false,
    "no_performance_measurement_claimed": true,
    "current_published_launchers_are_not_registered_for_this_new_source": true
  },
  "construction": {
    "method": "Invoke the pinned R493 factory.prepare_compile on the existing original physical compiler command in the owned compiler directory. Its complete generated source is an unexecuted ancestor at this point. Bind all generated baseline words, apply every exact literal count in order, and bind the actual new output. Copy the new cache header and the two pinned original physical/shared headers into the same directory. Use only the explicit new translation-unit path in the existing compiler command; keep the original factory receipt as prepared ancestry, not the compiler's executed input.",
    "output_is_temporary_expanded_source": true,
    "original_compiler_policy": [
      "-std=gnu++17",
      "-O3",
      "-fopenmp",
      "-frounding-math",
      "-ffp-contract=off",
      "-fno-fast-math"
    ],
    "not_an_additional_scientific_test": true
  }
}''')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def receipt(path):
    path = Path(path)
    return dict(file=path.name, bytes=path.stat().st_size, sha256=digest(path))


def same_file(path, expected, label):
    raw = Path(path).read_bytes()
    require(len(raw) == expected["bytes"]
            and hashlib.sha256(raw).hexdigest() == expected["sha256"], label)
    return raw


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY", "").lower()
            == "rogerhu12/math-research-public",
            "Source preparation belongs to the actual public Actions job")


def baseline():
    path = HERE / BASE
    require(digest(path) == BASE_SHA, "Exact R493 scalar-source adapter")
    name = "_R515_original_R493_scalar_source"
    if name in sys.modules:
        module = sys.modules[name]
        require(Path(module.__file__).resolve() == path.resolve()
                and getattr(module, "SCHEMA", None)
                == "R493-physical128-live-scalar-export-source-composition-v1",
                "The cached source module has the actual pinned origin")
        return module
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def copy_named_source(name, directory):
    # The current complete stage caller still uses its original fallback.
    return baseline().copy_named_source(name, directory)


def forward_lines(path, label):
    # Original complete error-line selection and limits, without new packing.
    return baseline().forward_lines(path, label)


def prepare_compile(command):
    actions()
    original = list(command)
    upstream = baseline()
    physical = PLAN["upstream"]["public_cpp"]["file"]
    matches = [i for i, word in enumerate(original)
               if Path(str(word)).name == physical]
    if not original or Path(str(original[0])).name != "g++" or not matches:
        return upstream.prepare_compile(original)
    require(len(matches) == 1 and original.count("-o") == 1,
            "One existing physical translation unit and executable")
    index = matches[0]
    # No subprocess has run: this original function prepares source files.
    prepared, ancestry = upstream.prepare_compile(original)
    require(ancestry is not None and ancestry.get("schema") == upstream.SCHEMA,
            "The actual original R493 physical-source construction returned")
    directory = Path(prepared[prepared.index("-o") + 1]).resolve().parent
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(directory.is_dir() and directory != runner
            and directory.is_relative_to(runner),
            "The same original owned temporary compiler directory")
    prior = Path(prepared[index]).resolve(strict=True)
    require(prior.parent == directory
            and prior.name == PLAN["baseline"]["file"],
            "The actual R493 generated source is the complete baseline")
    raw = same_file(prior, PLAN["baseline"], "Complete R493 source bytes/SHA")
    changed = raw.decode("utf-8")
    changes = []
    for item in PLAN["patches"]:
        require(type(item["count"]) is int and item["count"] > 0
                and changed.count(item["before"]) == item["count"],
                "Exact physical caller substitution: " + item["id"])
        changed = changed.replace(item["before"], item["after"])
        changes.append(dict(id=item["id"], replacements=item["count"],
            before_sha256=hashlib.sha256(item["before"].encode()).hexdigest(),
            after_sha256=hashlib.sha256(item["after"].encode()).hexdigest()))
    output = changed.encode("utf-8")
    expected = PLAN["output"]
    require(len(output) == expected["bytes"]
            and hashlib.sha256(output).hexdigest() == expected["sha256"],
            "Complete new physical translation-unit identity")
    copies = []
    for expected_header in (PLAN["additional_source"],
            PLAN["upstream"]["unchanged_physical_header"],
            PLAN["upstream"]["unchanged_shared_header"]):
        source = HERE / expected_header["file"]
        data = same_file(source, expected_header, "Exact complete header: " + source.name)
        target = directory / source.name
        require(not target.exists(), "Fresh explicit compiler header copy")
        target.write_bytes(data)
        copies.append(dict(original=receipt(source), actual=receipt(target),
                           actual_path=str(target), bytes_unchanged=True))
    destination = directory / expected["file"]
    require(not destination.exists(), "Fresh cache translation-unit source")
    destination.write_bytes(output)
    actual = list(prepared)
    actual[index] = str(destination)
    require(len(actual) == len(original)
            and [i for i, (left, right) in enumerate(zip(original, actual))
                 if left != right] == [index],
            "Only the actual translation-unit path changes")
    prefix = directory / "native_frozen_trace128_prefix.inc"
    require(prefix.is_file(), "The original complete bound R283 prefix exists")
    binding = dict(schema=SCHEMA, implementation=receipt(__file__),
        upstream_factory=receipt(HERE / BASE),
        upstream_prepared_but_not_compiled_binding=ancestry,
        upstream_receipt_execution_labels_are_preparation_ancestry_only=True,
        prepared_ancestor_source=receipt(prior),
        actual_executed_source=receipt(destination),
        actual_executed_source_path=str(destination),
        complete_copied_headers=copies, exact_caller_substitutions=changes,
        unchanged_generated_R283_prefix=receipt(prefix),
        original_requested_compile_command=original,
        actual_executed_command=actual,
        complete_338_by_112_mixed_endpoint_preserved=True,
        all_original_physical_audit_queries_preserved=True,
        all_angular_sums_and_original_C_solve_retained=True,
        finite_word_cache_lifetime="one physical_jets invocation only",
        nonfinite_mode_words_recomputed_by_original_expression=True,
        cross_query_cache=False, new_acceptance_test=False,
        existing_process_deadline_and_errors_delegated_unchanged=True,
        original_public_sources_modified=False,
        whole_run_word_identity_or_speed_claimed=False)
    path = directory / "physical-radial-mode-cache-source-binding.json"
    require(not path.exists(), "Fresh complete R515 compiler-source receipt")
    path.write_bytes(canonical(binding) + b"\n")
    small = dict(event="physical128_radial_mode_cache_compile_source",
        schema=SCHEMA, binding=receipt(path),
        actual_executed_source=receipt(destination),
        source_change_is_not_native_or_fullDN_acceptance=True)
    record = canonical(small)
    require(len(record) <= 90000, "One complete necessary source event")
    print(MARKER + record.decode("ascii"), flush=True)
    return actual, binding


def wrapped_base_process(original):
    # The actual existing process/deadline manager is called exactly once.
    # No compile, science or resource exception is caught and retried here.
    def run(command, stdout_path, stderr_path, seconds):
        actual, binding = prepare_compile(command)
        result = original(actual, stdout_path, stderr_path, seconds)
        if binding is not None:
            kind = binding.get("schema")
            key = ("live128_physical_radial_mode_cache_source_binding"
                if kind == SCHEMA else
                "live128_physical_scalar_source_binding"
                if kind == baseline().SCHEMA else "explicit_JSON_quote_binding")
            result[key] = binding
            result["actual_executed_command"] = actual
            result["original_requested_compile_command"] = list(command)
            result["compiler_stdout_full_line_readback"] = forward_lines(
                stdout_path, "compiler-stdout")
        result["child_stderr_full_line_readback"] = forward_lines(
            stderr_path, "child-stderr")
        return result
    return run
