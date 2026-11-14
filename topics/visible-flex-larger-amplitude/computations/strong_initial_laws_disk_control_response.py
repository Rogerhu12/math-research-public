#!/usr/bin/env python3
"""Compare pulse and monotone first-piece directions in one actual fixed-J solve.

The input must already be a genuinely verified actual fixed-view endpoint.
Both external columns use the complete saved field, all core coefficients,
the original physical full-H boundary, full stream backward error and half
step forcing checks. This is a derivative computation, never a new BVP.
All nonzero front-loaded reloads use the explicit monotone provider hook.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import strong_pulse_disk_control_response as pulse
import strong_disk_actual_fixed_control_response as disk

HERE = Path(__file__).resolve().parent
EXPECTED = {
    "strong_pulse_disk_control_response.py":
        "7b74a86e2e7f8e88d1280985dce7bcae85aa273a174f00f9511f3a4d14099f7f",
    "strong_monotone_initial_speed.py":
        "12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7",
}
ORIGINAL = pulse.transformed_source


def transformed_source():
    digest = lambda value: hashlib.sha256(value).hexdigest()
    own = {}
    for name, expected in EXPECTED.items():
        actual = digest((HERE/name).read_bytes())
        if actual != expected:
            raise ValueError("Declared first-piece response source changed: "+name)
        own[str(HERE/name)] = actual
    own[str(Path(__file__).resolve())] = digest(Path(__file__).read_bytes())
    original, provenance = ORIGINAL()
    edits = [
        ("'loop_ratio','initial_speed_pulse'))",
         "'loop_ratio','initial_speed_pulse','initial_speed_frontload'))"),
        ("baseline_cfg.get(field,0.) if field=='initial_speed_pulse' else baseline_cfg[field]",
         "baseline_cfg.get(field,0.) if field in ('initial_speed_pulse','initial_speed_frontload') else baseline_cfg[field]"),
        ("                    pulse_hook.install(value)\n",
         "                    pulse_hook.install(value)\n"
         "                    import strong_monotone_initial_speed as frontload_hook\n"
         "                    frontload_hook.install(value)\n"),
    ]
    changed = original
    for before, after in edits:
        if changed.count(before) != 1:
            raise ValueError("First-piece response anchor is not unique: "+repr(before))
        changed = changed.replace(before, after, 1)
    ast.parse(changed, filename="<original-actual-first-piece-directions>")
    reverse = changed
    for before, after in reversed(edits):
        if reverse.count(after) != 1:
            raise ValueError("First-piece response reverse anchor differs")
        reverse = reverse.replace(after, before, 1)
    if reverse != original:
        raise ValueError("Additional response source changed")
    provenance["source_sha256"].update(own)
    provenance["before_monotone_transformed_source_sha256"] = provenance["transformed_source_sha256"]
    provenance["transformed_source_sha256"] = digest(changed.encode())
    records = [dict(before=a, after=b, replacements=1) for a, b in edits]
    provenance["explicit_transforms"].extend(records)
    provenance["monotone_initial_speed_adapter"] = dict(scope=__doc__,
        physical_profile_key="initial_speed_frontload", absent_baseline_value=0.,
        fixed_degree_key="initial_speed_frontload_degree", absent_fixed_degree=22,
        provider_hook_sha256=EXPECTED["strong_monotone_initial_speed.py"],
        fields_are_new_physical_metric_directions=True,
        baseline_zero_path_delegates_original_arithmetic=True,
        full_original_field_Jacobian_and_H_identity_gates_preserved=True,
        full_backward_error_and_half_step_forcing_checks_preserved=True,
        original_sources_and_all_MJS_unmodified=True,
        pulse_and_frontload_nonzero_simultaneous_law_not_declared=True,
        exact_reverse_of_three_replacements_recovers_original_pulse_response=True)
    return changed, provenance


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument("--prepare-source-record", type=Path)
    own, remaining = parser.parse_known_args()
    if own.prepare_source_record:
        source, provenance = transformed_source()
        result = dict(scope="Source-only transform/reverse/AST preparation. No raw/RHS/Jac/Node or BVP.",
            prepared=True, actual_response_executed=False,
            source_bytes=len(source.encode()), provenance=provenance)
        with own.prepare_source_record.open("x") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
        print(json.dumps(dict(prepared=True, actual_response_executed=False,
            transformed_source_sha256=provenance["transformed_source_sha256"])), flush=True)
        return
    if "--response-fields" not in remaining:
        remaining += ["--response-fields",
            "delta,boost_length,boost_speed,initial_speed_pulse,initial_speed_frontload"]
    elif "initial_speed_frontload" not in remaining[remaining.index("--response-fields")+1].split(","):
        raise ValueError("This explicit entry requires the frontload physical response field")
    old, old_argv = disk.transformed_source, sys.argv
    disk.transformed_source = transformed_source
    sys.argv = [old_argv[0], *remaining]
    try:
        disk.main()
    finally:
        disk.transformed_source, sys.argv = old, old_argv


if __name__ == "__main__":
    main()
