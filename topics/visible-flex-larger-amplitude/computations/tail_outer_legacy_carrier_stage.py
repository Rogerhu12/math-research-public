#!/usr/bin/env python3
"""Run frozen carrier mathematics with an explicit recovered-schema reader.

Original module SHA values identify components, not this executor.  The
execution-provenance file binds this driver, the exact reader, original PM/PA
formal records, local derived views, the frozen numerical module, and argv.
No source statement or numerical parameter in that module is replaced.
Only its JSON read entry accepts the explicitly verified old PM/PA schema.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import sys
import time

from tail_outer_legacy_schema_reader import LegacyReader, digest

MODULES = {
    "positive-A": "tail_outer_background_carrier_integral",
    "carrier-J": "tail_outer_physical_substage_candidate_rebuilt",
    "comparison": "tail_outer_carrier_candidate_comparison",
    "mean-v3": "tail_outer_carrier_mean_ledger_v3",
    "frame": "tail_outer_carrier_frame_ledger",
}


def save(path, value, fresh=False):
    path = Path(path)
    if fresh and path.exists():
        raise FileExistsError("Use a fresh explicitly identified stage prefix: " + str(path))
    temporary = path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--legacy-topic", type=Path, required=True)
    ap.add_argument("--derived-root", type=Path, required=True)
    ap.add_argument("--math-directory", type=Path, required=True)
    ap.add_argument("--stage", choices=tuple(MODULES), required=True)
    ap.add_argument("--provenance", type=Path, required=True)
    ap.add_argument("remainder", nargs=argparse.REMAINDER)
    args = ap.parse_args()
    argv = args.remainder[1:] if args.remainder[:1] == ["--"] else args.remainder
    if not argv or "--rss-limit-mib" not in argv:
        raise ValueError("Pass the actual frozen stage arguments and explicit memory observation gate")
    limit = int(argv[argv.index("--rss-limit-mib")+1])
    if limit <= 0 or limit > 96:
        raise ValueError("This recovered execution is limited to the authorized 96 MiB observation gate")
    os.chdir(args.legacy_topic)
    reader = LegacyReader(args.legacy_topic, args.derived_root, limit)
    report = reader.report()
    sys.path.insert(0, str(args.math_directory.resolve()))
    module = importlib.import_module(MODULES[args.stage])
    mathematical_source = Path(module.__file__)
    module.read = reader.read
    if args.stage == "frame":
        module.core.read = reader.read
    if hasattr(module, "check_sources"):
        original_check = module.check_sources

        def explicit_sources(extra=()):
            result = original_check(extra)
            for path in (Path(__file__), Path(__file__).with_name("tail_outer_legacy_schema_reader.py")):
                same_component = args.math_directory/path.name
                if not same_component.is_file() or digest(same_component) != digest(path):
                    raise ValueError("The exact stage/reader source is absent from the declared module tree")
                result[path.name] = digest(path)
            return result

        module.check_sources = explicit_sources
    result_path = (Path(argv[argv.index("--out")+1]) if "--out" in argv else
        Path(argv[argv.index("--out-prefix")+1]+"-summary.json"))
    if result_path.exists():
        raise FileExistsError("Do not overwrite a complete numerical stage result")
    record = dict(schema="explicit-legacy-carrier-stage-execution-v1",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)", stage=args.stage,
        status="Prepared exact identities; stage not yet complete",
        driver=dict(path=str(Path(__file__).resolve()), sha256=digest(__file__)),
        schema_reader=dict(path=str(Path(__file__).with_name("tail_outer_legacy_schema_reader.py").resolve()),
            sha256=reader.source_sha),
        numerical_component=dict(path=str(mathematical_source), sha256=digest(mathematical_source)),
        exact_stage_argv=argv, actual_working_directory=str(Path.cwd()),
        legacy_original_and_view_report=report,
        source_statement_or_mathematical_parameter_changes=False,
        complete_original_PM_PA_recomputed=False,
        result_path=str(result_path))
    save(args.provenance, record, fresh=True)
    started = time.monotonic()
    old_argv = sys.argv
    try:
        sys.argv = [str(mathematical_source), *argv]
        module.main()
    except BaseException as error:
        record.update(status="Actual stage failed; any saved recovery remains incomplete",
            error=dict(type=type(error).__name__, message=str(error)),
            stage_seconds=time.monotonic()-started)
        save(args.provenance, record)
        raise
    finally:
        sys.argv = old_argv
    record.update(status="Actual frozen mathematics completed under the explicit legacy reader",
        stage_seconds=time.monotonic()-started,
        unaugmented_numerical_result_sha256=digest(result_path))
    save(args.provenance, record)
    # Add provenance outside input_hashes: existing primary headers must keep
    # their exact common dictionaries.  This is part of the same actual run,
    # before the outer wait4 wrapper records its formal exit.
    with result_path.open() as stream:
        result = json.load(stream)
    result["explicit_legacy_execution_provenance"] = dict(path=str(args.provenance),
        sha256=digest(args.provenance), driver_sha256=digest(__file__),
        reader_sha256=reader.source_sha,
        original_module_hash_is_component_not_executor_identity=True)
    save(result_path, result)
    print(json.dumps(dict(event="complete_explicit_legacy_stage", stage=args.stage,
        result=str(result_path), result_sha256=digest(result_path),
        provenance=str(args.provenance), provenance_sha256=digest(args.provenance))), flush=True)


if __name__ == "__main__":
    main()
