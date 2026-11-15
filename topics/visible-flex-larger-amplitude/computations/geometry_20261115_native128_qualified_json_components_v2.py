#!/usr/bin/env python3
"""Version2 explicit JSON-helper and exact statistics-name qualification.

Five SHA-pinned original C++ texts are copied only into the actual temporary
compiler directory. JSON calls gain a leading blank before ::quoted to keep
any preceding conditional colon a separate token. Only the two stage and
four exporter statistics use sites gain operator_trace128:: qualification;
header definitions, base classes and all mathematical expressions stay intact.
Counts, derived SHA and whole inverse-source checks bind every change. The
actual150/152 compiler errors motivate this repair, not a numerical gate.
Original repository sources, scientific Python bodies and budgets stay intact.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import types

HERE = Path(__file__).resolve().parent
OPERATOR = "geometry_20261115_native_operator_final128.py"
OPERATOR_SHA = "a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef"
CERTIFICATE = "geometry_20261115_literal_root_field_certificate.py"
CERTIFICATE_SHA = "cd73cb044e72052b38c6fc9d6517a7e436517f15777a4ace74333bb8a92af596"
OPERATOR_SCHEMA = "native-persistent128-qualified-JSON-and-statistics-contracted-trace-components-launch-v2"
CERTIFICATE_SCHEMA = "literal-root-field-certificate-qualified-JSON-and-statistics-launch-v2"
CHANGES = {
    "geometry_20261115_native_operator_trace128.hpp": [
        "950e1810106f2d268dd87da89be9c042ad3d3a014ea25e7c688701d731a3ddb0",
        12,
        "4610e1e851a1f3b51f829355f08ef4555d1dc212b61f193db2edce5bb2a13435"
    ],
    "geometry_20261115_native_operator_stage128.cpp": [
        "86782f8038e57bd87f578ca8a4b48640514ce36e8b11de4df172b20bd10d2926",
        9,
        "2f45f84a462e0ee9f9613344994ca3117ffac0bab664c141b24e02b44ea753f8"
    ],
    "geometry_20261115_native_boundary128.cpp": [
        "c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96",
        4,
        "37f6aab4604d6c39069486527eacda8c599c69ab496dadbbc74e92175fcd17ff"
    ],
    "geometry_20261115_native_physical_final128.cpp": [
        "a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415",
        49,
        "ecf14bf4d5cfd7a9f7796d0fa513822a05ca6cdc5a3ecc291859cff58a91b265"
    ],
    "geometry_20261115_literal_root_field_tape128.cpp": [
        "2aa2ad6737ca16854350967bddf49846e345ba5195d799d21dcc40a870c925bb",
        2,
        "af2f46fd754ab4282e0e79500c5a19122c30e6a352145b9bef2f686ef2d10a34"
    ]
}
TYPE_CHANGES = {
    "geometry_20261115_native_operator_stage128.cpp": [
        [
            "std::vector<BatchStats> stats(p.depth);",
            "std::vector<operator_trace128::BatchStats> stats(p.depth);",
            1
        ],
        [
            "size_t done=0;BatchStats total;",
            "size_t done=0;operator_trace128::BatchStats total;",
            1
        ]
    ],
    "geometry_20261115_literal_root_field_tape128.cpp": [
        [
            "BatchStats &stats",
            "operator_trace128::BatchStats &stats",
            3
        ],
        [
            "    BatchStats stats;",
            "    operator_trace128::BatchStats stats;",
            1
        ]
    ]
}
OLD = "quoted("
NEW = " ::quoted("
QUALIFICATION_BASELINE = "geometry_20261115_native128_qualified_json_components.py"
QUALIFICATION_BASELINE_SHA = "e609fb0aeae3142fcdb779004ddc0966e86c87c437da0984f50ffa814fb40d36"
SOURCE_FACTORY_ANCHOR = '            original_owner_binding=original_binding, file_manifest=receipt(manifest),'
SOURCE_FACTORY_INSERT = (
    '            compiler_readout_source_binding=result["compilation"].get("explicit_JSON_quote_binding"),\n'
    '            qualification_source_factory=_qualification_source_factory,\n'
)
MARKER = "NATIVE_PERSISTENT128 "
FRAME_LIMIT = 60000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def receipt(path):
    path = Path(path)
    return dict(file=path.name, bytes=path.stat().st_size, sha256=digest(path))


def emit(event, **fields):
    value = dict(event=event, lifecycle_schema="native128-explicit-JSON-and-statistics-qualification-v2",
                 **fields)
    raw = canonical(value)
    require(len(raw) <= 90000, "Whole semantic event exceeds transport limit")
    sys.stdout.buffer.write(MARKER.encode()+raw+b"\n")
    sys.stdout.buffer.flush()


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "Only the public Actions job may compile or execute these consumers")


def checked_module(name, expected, label):
    raw = (HERE/name).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected, "Exact frozen launcher: "+name)
    spec = importlib.util.spec_from_file_location(label, HERE/name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[label] = module
    spec.loader.exec_module(module)
    return module


def load_base():
    """Unchanged R314 input binder/lifecycle, including same-job owner identity."""
    return checked_module(CERTIFICATE, CERTIFICATE_SHA,
                          "_qualified_JSON_original_strict_binder").load_base()


def load_baseline():
    """Unchanged R305/R302 input binder/lifecycle for the complete consumers."""
    return checked_module(OPERATOR, OPERATOR_SHA,
                          "_qualified_JSON_original_operator_binder").load_baseline()


def copy_named_source(name, directory):
    require(name in CHANGES, "Only a declared named translation source may change")
    original_sha, count, derived_sha = CHANGES[name]
    original = (HERE/name).read_bytes()
    require(hashlib.sha256(original).hexdigest() == original_sha,
            "Complete original source identity: "+name)
    text = original.decode("utf-8")
    require(NEW not in text and text.count(OLD) == count,
            "Exact predeclared JSON-call token count: "+name)
    changed = text.replace(OLD, NEW)
    type_records = []
    for old, new, expected_count in TYPE_CHANGES.get(name, []):
        require(changed.count(old) == expected_count and new not in changed,
                "Exact declared statistics use sites: "+name)
        changed = changed.replace(old, new)
        type_records.append(dict(old=old, new=new, count=expected_count))
    require(":::quoted(" not in changed,
            "Conditional colon and global qualification must be separate tokens")
    inverse = changed
    for old, new, expected_count in reversed(TYPE_CHANGES.get(name, [])):
        require(inverse.count(new) == expected_count,
                "Exact inverse statistics use-site count: "+name)
        inverse = inverse.replace(new, old)
    inverse = inverse.replace(NEW, OLD)
    require(inverse == text,
            "Whole original source recovered by explicit qualification reversals")
    raw = changed.encode("utf-8")
    require(hashlib.sha256(raw).hexdigest() == derived_sha,
            "Complete predeclared executed-source identity: "+name)
    destination = directory/name
    require(not destination.exists(), "Fresh named compiler copy")
    destination.write_bytes(raw)
    return dict(original=receipt(HERE/name), executed=receipt(destination),
                absolute_executed_file=str(destination), old_token=OLD, new_token=NEW,
                exact_replacement_count=count, inverse_whole_source_equal=True,
                conditional_colon_lexical_separator_preserved=True,
                exact_statistics_use_site_replacements=type_records,
                header_statistics_definitions_and_base_qualifications_unchanged=True,
                numerical_expression_change=False)


def prepare_compile(command):
    """The caller's flags, deadline, executable and includes remain unchanged."""
    if not command or Path(command[0]).name != "g++":
        return list(command), None
    require(command.count("-o") == 1, "Unique actual compiler output")
    out_index = command.index("-o")+1
    require(out_index < len(command), "Actual compiler executable path")
    executable = Path(command[out_index]).resolve()
    directory = executable.parent.resolve(strict=True)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(directory != runner and runner in directory.parents,
            "Same-job temporary compiler directory")
    matches = [(i, Path(token).name) for i, token in enumerate(command)
               if Path(token).name in CHANGES and token.endswith(".cpp")]
    require(len(matches) == 1, "Exactly one declared actual translation unit")
    index, name = matches[0]
    require(Path(command[index]).resolve(strict=True) == (HERE/name).resolve(strict=True),
            "The actual source is the checked public original")
    needed = [name]
    if name in ("geometry_20261115_native_operator_stage128.cpp",
                "geometry_20261115_literal_root_field_tape128.cpp"):
        needed.append("geometry_20261115_native_operator_trace128.hpp")
    records = [copy_named_source(item, directory) for item in needed]
    changed = list(command)
    changed[index] = str(directory/name)
    require([i for i, (a, b) in enumerate(zip(command, changed)) if a != b] == [index],
            "Compiler invocation changes only its explicit source path")
    prefix = directory/"native_frozen_trace128_prefix.inc"
    require(prefix.is_file(), "The original launcher already wrote its bound R283 prefix")
    binding = dict(schema="native128-explicit-JSON-and-statistics-compiler-input-v2",
        implementation=receipt(__file__), translation_unit=name,
        original_qualification_baseline=dict(file=QUALIFICATION_BASELINE,
            sha256=QUALIFICATION_BASELINE_SHA, executed=False),
        original_command=list(command), actual_executed_command=changed,
        sources=records, unchanged_generated_R283_prefix=receipt(prefix),
        original_Git_sources_modified=False, numerical_formula_or_budget_change=False,
        global_JSON_helper_definition_unchanged=True,
        Cpp_standard_library_ADL_removed_from_named_JSON_calls=True,
        all_named_JSON_calls_have_a_leading_lexical_separator=True,
        statistics_use_sites_resolve_to_the_declared_operator_structure=True,
        local_compilation_or_science_performed_before_Actions=False)
    path = directory/"explicit-JSON-source-binding.json"
    require(not path.exists(), "Fresh compile source-binding record")
    path.write_bytes(canonical(binding))
    emit("explicit_JSON_compile_source_identity", binding=binding,
         binding_file=receipt(path), native_accepted=False)
    return changed, binding


def forward_lines(path, label):
    """Forward complete UTF-8 lines, without base64 or splitting a raw value."""
    path = Path(path)
    if not path.is_file():
        return dict(present=False, complete=False, reason="file-not-produced")
    original = receipt(path)
    count = 0
    omitted = []
    with path.open("rb") as stream:
        for index, raw in enumerate(stream):
            # Length decisions concern log transport only, never a scientific gate.
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                omitted.append(dict(line=index, bytes=len(raw),
                                    sha256=hashlib.sha256(raw).hexdigest(),
                                    reason="non-UTF8-original-log-line"))
                continue
            value = dict(label=label, original_file=original, line_index=index,
                         original_line_bytes=len(raw),
                         original_line_sha256=hashlib.sha256(raw).hexdigest(),
                         text_including_original_line_ending=text,
                         original_error_is_not_classified_as_a_mathematical_rejection=True)
            if len(canonical(value)) > FRAME_LIMIT:
                omitted.append(dict(line=index, bytes=len(raw),
                                    sha256=hashlib.sha256(raw).hexdigest(),
                                    reason="indivisible-original-log-line-over-transport-cap"))
                continue
            emit("qualified_component_original_log_line", **value)
            count += 1
    result = dict(present=True, original_file=original, complete=not omitted,
                  lines_forwarded=count, unforwarded_indivisible_lines=omitted)
    emit("qualified_component_original_log_readback", label=label, result=result,
         native_accepted=False)
    return result


def wrapped_base_process(original):
    def run(command, stdout_path, stderr_path, seconds):
        actual, binding = prepare_compile(command)
        result = original(actual, stdout_path, stderr_path, seconds)
        if binding is not None:
            result["explicit_JSON_quote_binding"] = binding
            result["actual_executed_command"] = actual
            result["caller_command_is_original_source_request"] = True
            result["original_requested_compile_command"] = list(command)
            result["compiler_stdout_full_line_readback"] = forward_lines(stdout_path, "compiler-stdout")
        result["child_stderr_full_line_readback"] = forward_lines(stderr_path, "child-stderr")
        return result
    return run


def run_operator():
    module = checked_module(OPERATOR, OPERATOR_SHA, "_qualified_JSON_R305_operator")
    original_load = module.load_baseline
    original_receipts = module.source_receipts

    def bound_baseline():
        base = original_load()
        base.run_process = wrapped_base_process(base.run_process)
        return base

    def sources(base):
        records = original_receipts(base)
        records[OPERATOR] = receipt(HERE/OPERATOR)
        records[Path(__file__).name] = receipt(__file__)
        return records

    module.load_baseline = bound_baseline
    module.source_receipts = sources
    module.__file__ = str(Path(__file__).resolve())
    module.SCHEMA = OPERATOR_SCHEMA
    emit("qualified_operator_entry", original_launcher=receipt(HERE/OPERATOR),
         actual_entry=receipt(__file__), schema=OPERATOR_SCHEMA,
         original_numerical_main_search_and_final_consumer_functions_unchanged=True,
         original_failure_and_partial_flags_retained=True, native_accepted=False)
    return int(module.main())


def strict_module():
    original = (HERE/CERTIFICATE).read_bytes()
    require(hashlib.sha256(original).hexdigest() == CERTIFICATE_SHA,
            "Exact frozen complete-field certificate launcher")
    text = original.decode("utf-8")
    require(text.count(SOURCE_FACTORY_ANCHOR) == 1 and SOURCE_FACTORY_INSERT not in text,
            "Unique evidence-binding metadata insertion")
    changed = text.replace(SOURCE_FACTORY_ANCHOR,
                           SOURCE_FACTORY_INSERT+SOURCE_FACTORY_ANCHOR, 1)
    require(changed.replace(SOURCE_FACTORY_INSERT, "", 1) == text,
            "Entire original certificate launcher recovered by metadata reversal")
    factory = dict(original_launcher=receipt(HERE/CERTIFICATE),
        executed_Python_source_bytes=len(changed.encode()),
        executed_Python_source_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        only_inserted_evidence_binding_metadata=True, inverse_source_byte_equal=True,
        actual_wrapper=receipt(__file__))
    module = types.ModuleType("_qualified_JSON_R314_certificate")
    module.__file__ = str(Path(__file__).resolve())
    module.__dict__["_qualification_source_factory"] = factory
    sys.modules[module.__name__] = module
    exec(compile(changed, str(HERE/CERTIFICATE), "exec"), module.__dict__)
    module.SCHEMA = CERTIFICATE_SCHEMA
    module.OWN_PINS[CERTIFICATE] = CERTIFICATE_SHA
    original_run = module.run_process

    def run(base, command, out, cap, deadline):
        actual, binding = prepare_compile(command)
        result = original_run(base, actual, out, cap, deadline)
        if binding is not None:
            result["explicit_JSON_quote_binding"] = binding
            result["original_requested_compile_command"] = list(command)
            result["compiler_stdout_full_line_readback"] = forward_lines(out/"stdout.log", "compiler-stdout")
        result["child_stderr_full_line_readback"] = forward_lines(out/"stderr.log", "child-stderr")
        (out/"process.json").write_bytes(canonical(result))
        return result

    module.run_process = run
    emit("qualified_certificate_entry", source_factory=factory,
         schema=CERTIFICATE_SCHEMA, original_certifier_and_interval_arithmetic_unchanged=True,
         original_child_exit70_and_summary_incomplete_are_not_overridden=True,
         native_accepted=False)
    return module


def main():
    actions()
    require(len(sys.argv) > 1 and sys.argv[1] in
            ("--operator-components", "--strict-field-certificate"),
            "Explicit independent component entry")
    kind = sys.argv.pop(1)
    sys.argv[0] = str(Path(__file__).resolve())
    if kind == "--operator-components":
        return run_operator()
    return int(strict_module().main())


if __name__ == "__main__":
    raise SystemExit(main())
