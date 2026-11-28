#!/usr/bin/env python3
"""One unchanged complete accurate-fee entry with durable Python-exception evidence.

This wrapper calls the pinned original Python source exactly once, with its
complete original argument vector, __file__ and source directory. It changes
no mathematical function, source registry, time/leaf budget, field, request
identity or success condition. It never opens a scientific report or array.

A diagnostic is execution evidence only. It is not a normal-root, quadrature,
Gram, reach, closed-surface or completion certificate. A returned exit zero
can still mean an original partial/unavailable fee report.

All execution is restricted to the original public repository Actions.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import runpy
import sys
import time
import traceback
import uuid

SCHEMA = "complete-accurate-fee-original-entry-exception-capture-v1"
REPOSITORY = "Rogerhu12/math-research-public"
SMALL_DIAGNOSTIC_LIMIT = 95000


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Original complete fee execution belongs to public repository Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))


def utc():
    return datetime.now(timezone.utc).isoformat()


def atomic_json(path, value):
    path = Path(path)
    payload = (json.dumps(value, sort_keys=True, indent=2,
        ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
    temporary = path.with_name(path.name + ".partial-" + uuid.uuid4().hex)
    with temporary.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)
    return record(path)


def full_text(path, value):
    path = Path(path)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(value)
        stream.flush()
        os.fsync(stream.fileno())
    return record(path)


def diagnostic_record(directory, value):
    """Retain all metadata; a large metadata body gets its own complete file."""
    payload = (json.dumps(value, sort_keys=True, indent=2,
        ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
    if len(payload) < SMALL_DIAGNOSTIC_LIMIT:
        return atomic_json(directory / "execution-diagnostic.json", value)
    complete = atomic_json(directory / ("complete-execution-event-"
        + uuid.uuid4().hex + ".json"), value)
    small = dict(
        schema=SCHEMA,
        invocation_identity=value["invocation_identity"],
        wrapper_source=value["wrapper_source"],
        original_target_source=value.get("original_target_source"),
        expected_target_source=value["expected_target_source"],
        actual_run_id=value["actual_run_id"],
        actual_run_attempt=value["actual_run_attempt"],
        recorded_at_utc=value["recorded_at_utc"],
        phase=value["phase"],
        original_entry_invoked=value["original_entry_invoked"],
        original_entry_completed_or_raised=value.get("original_entry_completed_or_raised"),
        actual_python_exception_type=value.get("actual_python_exception_type"),
        actual_python_exception_module=value.get("actual_python_exception_module"),
        actual_python_exception_message_preview=value.get("actual_python_exception_message_preview"),
        original_SystemExit_code=value.get("original_SystemExit_code"),
        full_exception_message=value.get("full_exception_message"),
        full_python_traceback=value.get("full_python_traceback"),
        complete_python_traceback_text=None,
        complete_python_traceback_text_in_this_diagnostic=False,
        complete_unabridged_execution_event=complete,
        scientific_report_or_arrays_read=False,
        scientific_report_or_original_source_modified=False,
        mathematical_success_inferred=False,
        complete_metadata_retained=True,
    )
    return atomic_json(directory / "execution-diagnostic.json", small)


def parse_args(argv):
    if "--" not in argv:
        raise ValueError("Keep a literal -- followed by the entire original fee argument vector")
    divider = argv.index("--")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-script", type=Path, required=True)
    parser.add_argument("--target-sha256", required=True)
    parser.add_argument("--target-bytes", type=int, required=True)
    parser.add_argument("--diagnostic-directory", type=Path, required=True)
    args = parser.parse_args(argv[:divider])
    target_argv = list(argv[divider + 1:])
    if (len(args.target_sha256) != 64
            or any(c not in "0123456789abcdef" for c in args.target_sha256)
            or args.target_bytes < 0):
        raise ValueError("Bind the full original target source by exact byte count and SHA256")
    if not target_argv:
        raise ValueError("The entire original scientific argument vector must be supplied")
    return args, target_argv


def prepare_directory(directory, target, target_argv):
    directory = Path(directory).resolve()
    target = Path(target).resolve()
    # A fresh, separate diagnostic directory is not the scientific output
    # directory. In particular it cannot replace any original argument path.
    candidates = [target]
    for value in target_argv:
        if isinstance(value, str) and os.path.isabs(value):
            candidates.append(Path(value).resolve())
    for path in candidates:
        if directory == path or directory in path.parents:
            raise ValueError("The diagnostic output cannot contain or replace an original source/input/output path")
    if directory.exists():
        raise FileExistsError("Use a fresh diagnostic directory for this one actual invocation")
    directory.mkdir(parents=True, exist_ok=False)
    return directory


def source_record_if_available(path):
    try:
        return record(path)
    except BaseException as error:
        return dict(path=str(Path(path).resolve()),
            unavailable_type=type(error).__name__,
            unavailable_reason=str(error))


def retain_exception(directory, error, state, started):
    # Formatting preserves the actual Python cause/context chain and all
    # ExceptionGroup entries. Locals, array values and new scientific calls
    # are neither inspected nor evaluated.
    message = str(error)
    message_record = full_text(directory / "exception-message.txt", message)
    trace_path = directory / "python-exception-traceback.txt"
    trace = traceback.TracebackException(
        type(error), error, error.__traceback__, capture_locals=False,
        compact=False, max_group_width=sys.maxsize, max_group_depth=sys.maxsize)
    with trace_path.open("x", encoding="utf-8", newline="\n") as stream:
        for piece in trace.format(chain=True):
            stream.write(piece)
        stream.flush()
        os.fsync(stream.fileno())
    trace_record = record(trace_path)
    trace_text = (trace_path.read_text(encoding="utf-8")
        if trace_record["bytes"] < SMALL_DIAGNOSTIC_LIMIT else None)
    state.update(
        phase="original-entry-raised" if state["original_entry_invoked"]
              else "source-binding-raised-before-original-entry",
        original_entry_completed_or_raised=state["original_entry_invoked"],
        actual_python_exception_type=type(error).__name__,
        actual_python_exception_module=type(error).__module__,
        actual_python_exception_message_preview=message[:6000],
        full_exception_message=message_record,
        full_python_traceback=trace_record,
        complete_python_traceback_text=trace_text,
        complete_python_traceback_text_in_this_diagnostic=trace_text is not None,
        recorded_at_utc=utc(),
        elapsed_seconds_binary64_hex=float(time.monotonic() - started).hex(),
        actual_target_source_after_call=source_record_if_available(
            state["expected_target_source"]["path"]),
        original_SystemExit_code=(
            error.code if isinstance(error, SystemExit)
            and (error.code is None or type(error.code) in (int, str))
            else None),
        original_exception_is_reraised_without_conversion=True,
        scientific_report_or_arrays_read=False,
        scientific_report_or_original_source_modified=False,
        mathematical_success_inferred=False,
    )
    return diagnostic_record(directory, state)


def diagnostic_stderr(value):
    """Execution evidence must not alter original stdout or its exit status."""
    try:
        print(value, file=sys.stderr, flush=True)
    except BaseException:
        pass


def safe_record_exception(directory, error, state, started):
    try:
        result = retain_exception(directory, error, state, started)
        diagnostic_stderr(json.dumps(dict(schema=SCHEMA, diagnostic=result,
            actual_python_exception_type=type(error).__name__,
            original_exception_will_be_reraised=True,
            mathematical_success_inferred=False), sort_keys=True))
    except BaseException as recording_error:
        # A failed diagnostic write must never replace the original exception.
        diagnostic_stderr("Actual fee exception diagnostic could not be saved: "
            + type(recording_error).__name__)


def safe_record_return(directory, state, started, exit_code):
    try:
        state.update(
            phase="original-entry-returned",
            original_entry_completed_or_raised=True,
            original_SystemExit_code=exit_code,
            actual_python_exception_type=None,
            actual_python_exception_module=None,
            actual_python_exception_message_preview=None,
            full_exception_message=None,
            full_python_traceback=None,
            complete_python_traceback_text=None,
            complete_python_traceback_text_in_this_diagnostic=False,
            recorded_at_utc=utc(),
            elapsed_seconds_binary64_hex=float(time.monotonic() - started).hex(),
            actual_target_source_after_call=source_record_if_available(
                state["expected_target_source"]["path"]),
            scientific_report_or_arrays_read=False,
            scientific_report_or_original_source_modified=False,
            mathematical_success_inferred=False,
        )
        result = diagnostic_record(directory, state)
        diagnostic_stderr(json.dumps(dict(schema=SCHEMA, diagnostic=result,
            original_entry_returned=True, original_SystemExit_code=exit_code,
            mathematical_success_inferred=False), sort_keys=True))
    except BaseException as recording_error:
        # Diagnostic output cannot change an otherwise returned original code.
        diagnostic_stderr("Actual fee return diagnostic could not be saved: "
            + type(recording_error).__name__)


def main(argv=None):
    require_actions()
    args, target_argv = parse_args(sys.argv[1:] if argv is None else argv)
    target = args.target_script.resolve()
    directory = prepare_directory(args.diagnostic_directory, target, target_argv)
    started = time.monotonic()
    state = dict(
        schema=SCHEMA,
        invocation_identity=uuid.uuid4().hex,
        wrapper_source=record(__file__),
        expected_target_source=dict(path=str(target), bytes=args.target_bytes,
            sha256=args.target_sha256),
        original_target_source=None,
        complete_original_target_argv=target_argv,
        original_target_argv_word_count=len(target_argv),
        actual_run_id=os.environ.get("GITHUB_RUN_ID"),
        actual_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        actual_repository=os.environ.get("GITHUB_REPOSITORY"),
        actual_source_commit_environment=os.environ.get("GITHUB_SHA"),
        actual_process_id=os.getpid(),
        started_at_utc=utc(),
        recorded_at_utc=utc(),
        phase="binding-original-source",
        original_entry_invoked=False,
        original_entry_completed_or_raised=False,
        no_original_numerical_argument_changed=True,
        original_entry_invocation_count=0,
        maximum_declared_original_entry_invocations=1,
        source_registry_and_original_report_identity_not_relabelled=True,
        scientific_report_or_arrays_read=False,
        scientific_report_or_original_source_modified=False,
        mathematical_success_inferred=False,
    )
    diagnostic_record(directory, state)
    original_argv, original_path = sys.argv, list(sys.path)
    try:
        actual_source = record(target)
        if actual_source != state["expected_target_source"]:
            raise ValueError("The complete original accurate-fee target source differs")
        state["original_target_source"] = actual_source
        sys.argv = [str(target)] + target_argv
        if sys.path:
            sys.path[0] = str(target.parent)
        else:
            sys.path.append(str(target.parent))
        state["phase"] = "ready-to-invoke-original-entry"
        state["recorded_at_utc"] = utc()
        diagnostic_record(directory, state)
        # The original __main__ block, imports, guards, parser, workload,
        # budgets, reports and all exceptions execute here exactly once.
        # No fallible diagnostic operation intervenes between marking this
        # one invocation in memory and the call itself.
        state["original_entry_invoked"] = True
        state["original_entry_invocation_count"] = 1
        runpy.run_path(str(target), run_name="__main__")
    except SystemExit as error:
        if error.code is None or type(error.code) is int and error.code == 0:
            safe_record_return(directory, state, started, error.code)
        else:
            safe_record_exception(directory, error, state, started)
        raise
    except BaseException as error:
        safe_record_exception(directory, error, state, started)
        raise
    else:
        safe_record_return(directory, state, started, 0)
        return 0
    finally:
        sys.argv = original_argv
        sys.path[:] = original_path


if __name__ == "__main__":
    raise SystemExit(main())
