#!/usr/bin/env python3
"""Read complete existing scalar metadata on the original public Actions runner.

This is a standard-library readout of an already returned complete input report.
It uses the original constructor's whole-file validation and exports the complete
FullHold metadata and complete initial scalar law without reconstructing a field,
performing a new integration, or substituting an old radius for the R690 radius.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
MAKER_PATH = "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py"
MAKER_SHA256 = "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"
PARAMETERS_SHA256 = "e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa"
TARGET_SHA256 = "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9"

def record(path):
    p = Path(path).resolve()
    raw = p.read_bytes()
    return dict(path=str(p), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, sort_keys=True, separators=(",", ":"), allow_nan=False)
        stream.write("\n")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--preparation", type=Path, required=True)
    parser.add_argument("--expected-preparation-sha256", required=True)
    parser.add_argument("--expected-preparation-bytes", type=int, required=True)
    parser.add_argument("--expected-run", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    result = dict(schema="complete-existing-fixed-scalar-metadata-readout-v1",
                  complete=False, status="started", reader=record(__file__),
                  declared_arguments=vars(args).copy(),
                  physical_field_evaluations=0, Jacobian_evaluations=0,
                  normal_root_evaluations=0, new_scalar_integrations=0,
                  source_or_parameter_mutations=False,
                  certificate_or_new_solution_claimed=False)
    result["declared_arguments"] = {k: str(v) if isinstance(v, Path) else v
                                    for k, v in result["declared_arguments"].items()}
    try:
        if (os.environ.get("GITHUB_ACTIONS") != "true"
                or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY
                or os.environ.get("GITHUB_RUN_ID") != args.expected_run):
            raise ValueError("Use the declared original public Actions runner")
        repo = args.repo.resolve()
        path = args.preparation.resolve()
        if output == path or output == Path(__file__).resolve() or output.exists():
            raise ValueError("Use a fresh readout path")
        before = record(path)
        result["actual_preparation"] = before
        if (before["sha256"] != args.expected_preparation_sha256
                or before["bytes"] != args.expected_preparation_bytes):
            raise ValueError("The complete previously returned input report differs")
        maker_path = repo / MAKER_PATH
        maker_record = record(maker_path)
        result["complete_input_constructor"] = maker_record
        if maker_record["sha256"] != MAKER_SHA256:
            raise ValueError("The complete original constructor differs")
        spec = importlib.util.spec_from_file_location("_existing_scalar_metadata_maker", maker_path)
        maker = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(maker)
        report, checked = maker.read_preparation(path)
        if (record(path) != before
                or report["complete_scalar_parameters_identity_sha256"] != PARAMETERS_SHA256
                or report["mathematical_target_identity_sha256"] != TARGET_SHA256):
            raise ValueError("The complete existing fixed target differs")
        parameters = report["complete_scalar_parameters"]
        origin = float(parameters["analytic_extension_origin"])
        geometry = parameters["geometry"]
        law = geometry["initial_law"]
        metadata = report["complete_FullHold_scalar_metadata"]
        if not isinstance(law, dict) or not isinstance(metadata, dict):
            raise ValueError("The complete original metadata objects are required")
        result.update(
            complete=True, status="complete",
            actual_execution=dict(
                run=os.environ["GITHUB_RUN_ID"],
                attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
                checked_out_source_commit=subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()),
            original_execution=report["execution"],
            complete_source_records=report["source_records"],
            complete_original_parameter_source_records=report["input_records"],
            actual_scalar_input=report["outputs"]["scalar_input"],
            complete_preparation_binding=checked,
            complete_FullHold_scalar_metadata=metadata,
            complete_initial_law=law,
            initial_law_binary64_words={k: float(v).hex() for k, v in ((k, law[k]) for k in ("length", "velocity", "k0"))},
            initial_law_exact_binary_rationals={k: str(Fraction(float(v))) for k, v in ((k, law[k]) for k in ("length", "velocity", "k0"))},
            analytic_extension_origin=origin,
            analytic_extension_origin_binary64=origin.hex(),
            analytic_extension_origin_exact=str(Fraction(origin)),
            complete_last_scalar_knot=geometry["knots"][-1],
            original_scalar_knot_count=len(geometry["knots"]),
            complete_scalar_parameters_identity_sha256=PARAMETERS_SHA256,
            mathematical_target_identity_sha256=TARGET_SHA256,
            scope="Complete existing FullHold metadata and original initial law; S is the physical FullHold interval, not its integer arithmetic scale. R in this object is the original FullHold radius and is not the modified R690 radius. All original parameters remain in their exact full source file.")
        if record(path) != before:
            raise ValueError("The original input report changed during the full read")
        write(output, result)
        print(json.dumps(dict(schema=result["schema"], complete=True, output=record(output)),
                         sort_keys=True), flush=True)
        return 0
    except Exception as exc:
        result.update(complete=False, status="failed", error_type=type(exc).__name__,
                      error=str(exc), complete_traceback=traceback.format_exc())
        if not output.exists() and output != args.preparation.resolve():
            write(output, result)
        print(json.dumps(dict(schema=result["schema"], complete=False,
                              error_type=type(exc).__name__, error=str(exc)),
                         sort_keys=True), flush=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
