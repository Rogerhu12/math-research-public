#!/usr/bin/env python3
"""R493 exact physical128 scalar-word export with explicit compiler sources.

The original four mathematical C++ consumers remain public immutable inputs.
Only the original physical endpoint/audit translation unit obtains the four
declared scalar export insertions, after the already published JSON lexical
qualification. This module runs only in the public Actions namespace.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SCHEMA = "R493-physical128-live-scalar-export-source-composition-v1"
BASE = "geometry_20261115_native128_qualified_json_components_v2.py"
BASE_SHA = "5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf"
MARKER = "LIVE128_SCALAR_SOURCE "
PLAN = json.loads(r"""{
  "schema": "R493-physical128-live-scalar-export-source-view-plan-v1",
  "public_baseline": {
    "file": "geometry_20261115_native_physical_final128.cpp",
    "bytes": 18055,
    "sha256": "a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415"
  },
  "qualified_baseline": {
    "file": "geometry_20261115_native_physical_final128.cpp",
    "bytes": 18202,
    "sha256": "ecf14bf4d5cfd7a9f7796d0fa513822a05ca6cdc5a3ecc291859cff58a91b265",
    "producer": "geometry_20261115_native128_qualified_json_components_v2.py",
    "producer_sha256": "5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf"
  },
  "output": {
    "file": "geometry_20261116_native_physical_live_scalar128.cpp",
    "bytes": 19958,
    "sha256": "5f6b2d3c641befb6816c3e411ba00b7faf6eb3407b210f8b4c68b1c655746502"
  },
  "patches": [
    {
      "label": "same-actual-cut-scalar-words",
      "before": "    std::ostringstream bs;\n    bs<<\"{\\\"radius\\\":\"<< ::quoted(qstr(g.r))<<\",\\\"backgroundSlope\\\":\"<< ::quoted(qstr(g.w))\n      <<\",\\\"backgroundSecond\\\":\"<< ::quoted(qstr(g.w*physical.cut.k/g.dr))\n      <<\",\\\"E\\\":\"<< ::quoted(qstr(g.E))<<\",\\\"Ep\\\":\"<< ::quoted(qstr(2*g.w2*physical.cut.k/g.dr))\n      <<\",\\\"meanSlope\\\":\"<< ::quoted(qstr(g.w+base.rows[2*p.M]))\n      <<\",\\\"meanSecond\\\":\"<< ::quoted(qstr(g.w*physical.cut.k/g.dr+base.rows[2*p.M+1]))\n      <<\",\\\"minLeading\\\":\"<< ::quoted(qstr(base.jets.minA))<<\",\\\"minD\\\":\"<< ::quoted(qstr(base.jets.minD))\n      <<\",\\\"endpointFullD\\\":\"<< ::quoted(qstr(base.jets.maxDarboux))\n      <<\",\\\"endpointPhi\\\":\"<< ::quoted(qstr(base.jets.holonomy))\n      <<\",\\\"formalCurvature\\\":\"<< ::quoted(qstr(base.jets.curvature))\n      <<\",\\\"original_C_radial_solve_readback\\\":\"<< ::quoted(qstr(base.jets.radial_solve_readback))<<\"}\";\n    base_scalars=bs.str();",
      "after": "    // R493: form the original scalar expressions once, then serialize the same Q words.\n    const V live_cut_scalar_words={g.r,g.w,g.w*physical.cut.k/g.dr,g.E,2*g.w2*physical.cut.k/g.dr,g.w+base.rows[2*p.M],g.w*physical.cut.k/g.dr+base.rows[2*p.M+1],base.jets.minA,base.jets.minD,base.jets.maxDarboux,base.jets.holonomy,base.jets.curvature,base.jets.radial_solve_readback};\n    raw128(arrays/\"cut-protocol-scalars.f128\",live_cut_scalar_words);\n    std::ostringstream bs;\n    bs<<\"{\\\"radius\\\":\"<< ::quoted(qstr(live_cut_scalar_words[0]))\n      <<\",\\\"backgroundSlope\\\":\"<< ::quoted(qstr(live_cut_scalar_words[1]))\n      <<\",\\\"backgroundSecond\\\":\"<< ::quoted(qstr(live_cut_scalar_words[2]))\n      <<\",\\\"E\\\":\"<< ::quoted(qstr(live_cut_scalar_words[3]))\n      <<\",\\\"Ep\\\":\"<< ::quoted(qstr(live_cut_scalar_words[4]))\n      <<\",\\\"meanSlope\\\":\"<< ::quoted(qstr(live_cut_scalar_words[5]))\n      <<\",\\\"meanSecond\\\":\"<< ::quoted(qstr(live_cut_scalar_words[6]))\n      <<\",\\\"minLeading\\\":\"<< ::quoted(qstr(live_cut_scalar_words[7]))\n      <<\",\\\"minD\\\":\"<< ::quoted(qstr(live_cut_scalar_words[8]))\n      <<\",\\\"endpointFullD\\\":\"<< ::quoted(qstr(live_cut_scalar_words[9]))\n      <<\",\\\"endpointPhi\\\":\"<< ::quoted(qstr(live_cut_scalar_words[10]))\n      <<\",\\\"formalCurvature\\\":\"<< ::quoted(qstr(live_cut_scalar_words[11]))\n      <<\",\\\"original_C_radial_solve_readback\\\":\"<< ::quoted(qstr(live_cut_scalar_words[12]))<<\"}\";\n    base_scalars=bs.str();",
      "count": 1
    },
    {
      "label": "explicit-cut-scalar-layout",
      "before": "    <<\",\\\"cut_original_jet_scalars\\\":\"<<base_scalars",
      "after": "    <<\",\\\"cut_original_jet_scalars\\\":\"<<base_scalars\n    <<\",\\\"live_response_scalar_word_layout\\\":{\\\"schema\\\":\\\"R493-complete-physical128-protocol-scalar-words-v1\\\",\\\"file\\\":\\\"large-arrays/cut-protocol-scalars.f128\\\",\\\"names\\\":[\\\"radius\\\",\\\"backgroundSlope\\\",\\\"backgroundSecond\\\",\\\"E\\\",\\\"Ep\\\",\\\"meanSlope\\\",\\\"meanSecond\\\",\\\"minLeading\\\",\\\"minD\\\",\\\"endpointFullD\\\",\\\"endpointPhi\\\",\\\"formalCurvature\\\",\\\"original_C_radial_solve_readback\\\"],\\\"words\\\":13,\\\"bytes\\\":208,\\\"format\\\":\\\"little-endian-IEEE-binary128\\\",\\\"value_scope\\\":\\\"the-same-Q-words-as-cut_original_jet_scalars\\\"}\"",
      "count": 1
    },
    {
      "label": "complete-audit-aggregate-words",
      "before": "  const bool done=complete==size_t(p.depth);\n  std::ostringstream s;",
      "after": "  const bool done=complete==size_t(p.depth);\n  if(done)raw128(out/\"large-arrays\"/\"audit-protocol-scalars.f128\",V{total.fullD,total.normalized,total.minA,total.minD,total.curvature,total.PV,total.metric,total.holonomy,total.radial_solve_readback});\n  std::ostringstream s;",
      "count": 1
    },
    {
      "label": "explicit-audit-scalar-layout",
      "before": "    <<\",\\\"extrema_are_partial_if_complete_false\\\":true\"",
      "after": "    <<\",\\\"extrema_are_partial_if_complete_false\\\":true\"\n    <<\",\\\"live_response_scalar_word_layout\\\":{\\\"schema\\\":\\\"R493-complete-physical128-protocol-scalar-words-v1\\\",\\\"file\\\":\\\"large-arrays/audit-protocol-scalars.f128\\\",\\\"names\\\":[\\\"fullD\\\",\\\"normalizedFullDefect\\\",\\\"minLeading\\\",\\\"minD\\\",\\\"formalCurvature\\\",\\\"maxPhysicalPV\\\",\\\"actualMetric\\\",\\\"holonomy\\\",\\\"C_radial_solve_readback_max\\\"],\\\"words\\\":9,\\\"bytes\\\":144,\\\"format\\\":\\\"little-endian-IEEE-binary128\\\",\\\"value_scope\\\":\\\"actual-complete-independent-audit-aggregate-Q-variables\\\"}\"",
      "count": 1
    }
  ],
  "cut_layout": {
    "schema": "R493-complete-physical128-protocol-scalar-words-v1",
    "file": "large-arrays/cut-protocol-scalars.f128",
    "names": [
      "radius",
      "backgroundSlope",
      "backgroundSecond",
      "E",
      "Ep",
      "meanSlope",
      "meanSecond",
      "minLeading",
      "minD",
      "endpointFullD",
      "endpointPhi",
      "formalCurvature",
      "original_C_radial_solve_readback"
    ],
    "words": 13,
    "bytes": 208,
    "format": "little-endian-IEEE-binary128",
    "value_scope": "the-same-Q-words-as-cut_original_jet_scalars"
  },
  "audit_layout": {
    "schema": "R493-complete-physical128-protocol-scalar-words-v1",
    "file": "large-arrays/audit-protocol-scalars.f128",
    "names": [
      "fullD",
      "normalizedFullDefect",
      "minLeading",
      "minD",
      "formalCurvature",
      "maxPhysicalPV",
      "actualMetric",
      "holonomy",
      "C_radial_solve_readback_max"
    ],
    "words": 9,
    "bytes": 144,
    "format": "little-endian-IEEE-binary128",
    "value_scope": "actual-complete-independent-audit-aggregate-Q-variables"
  },
  "source_only_plan_not_currently_called": true,
  "scientific_execution_performed": false
}""")
_cached_base = None


def require(condition, message):
    if not condition:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY", "").lower() ==
            "rogerhu12/math-research-public",
            "Only this public Actions job may prepare or execute the live source")


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def receipt(path):
    path = Path(path)
    return dict(file=path.name, bytes=path.stat().st_size, sha256=digest(path))


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def baseline():
    global _cached_base
    actions()
    if _cached_base is None:
        path = HERE / BASE
        require(digest(path) == BASE_SHA, "Exact unchanged v2 source qualifier")
        name = "_R493_original_v2_source_qualifier"
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        _cached_base = module
    return _cached_base


def copy_named_source(name, directory):
    # The stage caller still receives the original qualified fallback header.
    return baseline().copy_named_source(name, directory)


def forward_lines(path, label):
    return baseline().forward_lines(path, label)


def prepare_compile(command):
    """Change only the declared physical translation-unit path and source."""
    actions()
    physical = PLAN["public_baseline"]["file"]
    matches = [i for i, item in enumerate(command)
               if Path(str(item)).name == physical]
    if not command or Path(str(command[0])).name != "g++" or not matches:
        return baseline().prepare_compile(command)
    require(len(matches) == 1 and command.count("-o") == 1,
            "One actual original physical translation unit and executable")
    index = matches[0]
    original_path = Path(command[index]).resolve(strict=True)
    require(original_path == (HERE / physical).resolve(strict=True),
            "Use the exact public original physical source")
    directory = Path(command[command.index("-o") + 1]).resolve().parent
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(directory.is_dir() and directory != runner and
            directory.is_relative_to(runner),
            "Use this job's existing temporary compiler directory")
    original = original_path.read_bytes()
    original_spec = PLAN["public_baseline"]
    require(len(original) == original_spec["bytes"] and
            hashlib.sha256(original).hexdigest() == original_spec["sha256"],
            "The whole original physical source differs")
    qualifier = baseline()
    require(qualifier.CHANGES[physical] == [
                original_spec["sha256"], 49,
                PLAN["qualified_baseline"]["sha256"]],
            "The declared physical source qualification differs")
    text = original.decode("utf-8")
    require(text.count("quoted(") == 49 and " ::quoted(" not in text,
            "Exact original JSON-call token count")
    qualified = text.replace("quoted(", " ::quoted(")
    require(qualified.replace(" ::quoted(", "quoted(") == text,
            "Qualification preserves the whole original source")
    raw = qualified.encode("utf-8")
    qspec = PLAN["qualified_baseline"]
    require(len(raw) == qspec["bytes"] and
            hashlib.sha256(raw).hexdigest() == qspec["sha256"],
            "Exact published v2-qualified physical bytes")
    changed = qualified
    patch_records = []
    for item in PLAN["patches"]:
        require(item["count"] == 1 and changed.count(item["before"]) == 1 and
                item["after"] not in changed,
                "One declared physical scalar source site: " + item["label"])
        changed = changed.replace(item["before"], item["after"], 1)
        patch_records.append(dict(label=item["label"], replacements=1,
                                  before_sha256=hashlib.sha256(
                                      item["before"].encode()).hexdigest(),
                                  after_sha256=hashlib.sha256(
                                      item["after"].encode()).hexdigest()))
    inverse = changed
    for item in reversed(PLAN["patches"]):
        require(inverse.count(item["after"]) == 1,
                "Unique inverse scalar export site: " + item["label"])
        inverse = inverse.replace(item["after"], item["before"], 1)
    require(inverse == qualified,
            "Removing four exact export sites recovers all qualified bytes")
    output = changed.encode("utf-8")
    expected = PLAN["output"]
    require(len(output) == expected["bytes"] and
            hashlib.sha256(output).hexdigest() == expected["sha256"],
            "Actual scalar-export physical translation identity")
    destination = directory / expected["file"]
    require(not destination.exists(), "Fresh scalar-export source path")
    destination.write_bytes(output)
    prefix = directory / "native_frozen_trace128_prefix.inc"
    require(prefix.is_file(), "Original complete R283 prefix is present")
    actual = list(command)
    actual[index] = str(destination)
    require([i for i, pair in enumerate(zip(command, actual))
             if pair[0] != pair[1]] == [index],
            "Only the actual translation-unit path changes")
    binding = dict(
        schema=SCHEMA, implementation=receipt(__file__),
        original_qualification_source=receipt(HERE / BASE),
        public_original=receipt(original_path),
        qualified_baseline=dict(qspec, executed_translation_unit=False),
        actual_executed_source=receipt(destination),
        actual_executed_source_path=str(destination),
        exact_export_insertions=patch_records,
        cut_scalar_layout=PLAN["cut_layout"],
        audit_scalar_layout=PLAN["audit_layout"],
        original_command=list(command), actual_executed_command=actual,
        unchanged_generated_R283_prefix=receipt(prefix),
        whole_inverse_qualified_source_equal=True,
        original_public_sources_modified=False,
        original_endpoint_and_audit_arithmetic_expressions_retained=True,
        raw_scalar_export_only_after_original_values_exist=True,
        new_RHS_root_or_boundary_evaluation_added=False,
        component_scientific_budget_unchanged=True)
    path = directory / "live-physical-scalar-source-binding.json"
    require(not path.exists(), "Fresh complete scalar-source receipt")
    path.write_bytes(canonical(binding) + b"\n")
    small = dict(event="physical128_live_scalar_compile_source", schema=SCHEMA,
                 binding=receipt(path), original_source=receipt(original_path),
                 actual_executed_source=receipt(destination),
                 exact_export_site_count=len(patch_records),
                 original_mathematical_consumers_not_duplicated=True)
    record = canonical(small)
    require(len(record) <= 90000, "One necessary source event must fit")
    print(MARKER + record.decode(), flush=True)
    return actual, binding


def wrapped_base_process(original):
    """The original process/deadline manager executes the explicit new source."""
    def run(command, stdout_path, stderr_path, seconds):
        actual, binding = prepare_compile(command)
        result = original(actual, stdout_path, stderr_path, seconds)
        if binding is not None:
            key = ("live128_physical_scalar_source_binding"
                   if binding.get("schema") == SCHEMA
                   else "explicit_JSON_quote_binding")
            result[key] = binding
            result["actual_executed_command"] = actual
            result["original_requested_compile_command"] = list(command)
            result["compiler_stdout_full_line_readback"] = forward_lines(
                stdout_path, "compiler-stdout")
        result["child_stderr_full_line_readback"] = forward_lines(
            stderr_path, "child-stderr")
        return result
    return run
