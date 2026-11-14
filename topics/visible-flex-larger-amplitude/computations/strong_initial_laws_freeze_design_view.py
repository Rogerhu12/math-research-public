#!/usr/bin/env python3
"""Genuine fixed-view verification with both explicit first-piece providers.

A nonzero saved front-loading weight is reloaded as its actual physical g.
The original complete raw/PPoly/core/chart/H/RMS/BC identities remain
mandatory. This representation conversion starts no Node or BVP and does
not accept an unaccepted endpoint.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import strong_pulse_freeze_design_view as pulse

HERE = Path(__file__).resolve().parent
EXPECTED = {
    "strong_pulse_freeze_design_view.py":
        "18ff9e44b4f69e52017c5a7d20998e1a7d06c77fd3930bd7b21b767d984f4e7e",
    "strong_monotone_initial_speed.py":
        "12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7",
}


def transformed_source():
    digest = lambda data: hashlib.sha256(data).hexdigest()
    own = {}
    for name, expected in EXPECTED.items():
        actual = digest((HERE/name).read_bytes())
        if actual != expected:
            raise ValueError("Declared first-piece fixed-view source changed: "+name)
        own[str(HERE/name)] = actual
    own[str(Path(__file__).resolve())] = digest(Path(__file__).read_bytes())
    original, provenance = pulse.transformed_source()
    before = "                    pulse_hook.install(value)\n"
    after = before + (
        "                    import strong_monotone_initial_speed as frontload_hook\n"
        "                    frontload_hook.install(value)\n")
    if original.count(before) != 1:
        raise ValueError("First-piece fixed-view loader anchor is not unique")
    source = original.replace(before, after, 1)
    ast.parse(source, filename="<original-genuine-fixed-view-initial-laws>")
    if source.count(after) != 1 or source.replace(after, before, 1) != original:
        raise ValueError("First-piece fixed-view reverse does not recover original")
    provenance["source_sha256"].update(own)
    provenance["prior_transformed_sha256"] = provenance["transformed_sha256"]
    provenance["transformed_sha256"] = digest(source.encode())
    provenance["replacements"].append(dict(before=before, after=after, count=1))
    provenance["monotone_initial_speed_fixed_view"] = dict(scope=__doc__,
        physical_profile_key="initial_speed_frontload",
        fixed_degree_key="initial_speed_frontload_degree", absent_degree=22,
        same_explicit_saved_physical_metric_required=True,
        original_raw_PPoly_core_chart_H_RMS_BC_gates_unchanged=True,
        original_no_worker_and_no_BVP_conditions_unchanged=True,
        exact_reverse_recovers_original_pulse_fixed_view=True)
    return source, provenance


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument("--prepare-source-record", type=Path)
    own, remaining = parser.parse_known_args()
    source, provenance = transformed_source()
    if own.prepare_source_record:
        with own.prepare_source_record.open("x") as stream:
            json.dump(dict(scope="Source-only transform/reverse/AST; no physical object, raw residual or conversion.",
                prepared=True, conversion_executed=False, provenance=provenance), stream, indent=2)
            stream.write("\n")
        print(json.dumps(dict(prepared=True, conversion_executed=False,
            transformed_source_sha256=provenance["transformed_sha256"])), flush=True)
        return
    namespace = dict(__file__=str(Path(__file__).resolve()),
        __name__="strong_initial_laws_genuine_fixed_view",
        PULSE_FIXED_VIEW_TRANSFORM=provenance)
    old = sys.argv
    sys.argv = [old[0], *remaining]
    try:
        exec(compile(source, "<original-genuine-fixed-view-initial-laws>", "exec"), namespace)
        namespace["main"]()
    finally:
        sys.argv = old


if __name__ == "__main__":
    main()
