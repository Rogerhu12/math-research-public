#!/usr/bin/env python3
"""Actual continuation with explicit first-piece laws and exact prefix storage.

The two external optional controls are initial_speed_pulse and
initial_speed_frontload. Nonzero values change g. A saved nonzero law must
always be reloaded with this same explicit provider. This first interface
compares the separate laws, and the provider rejects both being nonzero.

The original actual all-core+delta/LB/vp equations, complete warm tangents,
full-H outer method, disk QR/backward error, fixed physical Newton merit,
original RMS and final full tail/Jacobian/audit gates all remain unchanged.
No MJS file is modified. This entry does not accept background geometry or
an inner Newton checkpoint as a new coupled solution.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

import strong_fresh_resource_actual_bvp as resource
import strong_cached_prefix_actual_bvp as cached
import strong_pulse_actual_bvp as pulse
import strong_prefix_evaluation_cache as cache
from strong_initial_laws_augmented_core import transformed_source as core_source

HERE = Path(__file__).resolve().parent
EXPECTED = {
    "strong_pulse_actual_bvp.py":
        "bf34b54857ca35e270f4198344ec9b96f5b210781d2a95afb92b044c8f61738f",
    "strong_cached_prefix_actual_bvp.py":
        "986de6d32371144d20dc5a511dd027875e0b43aa976201447e75a7151e940faa",
    "strong_monotone_initial_speed.py":
        "12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7",
    "strong_initial_laws_augmented_core.py":
        "067940d3d2f581beebf1fd64e0649c80d9d5eaa61052fa8c2ab6cd54f5004646",
}


def initial_laws_build(original_build):
    pulse_build = pulse.pulse_build(original_build)
    def build(configuration, disk_configuration):
        digest = lambda value: hashlib.sha256(value).hexdigest()
        own = {}
        for name, expected in EXPECTED.items():
            value = digest((HERE/name).read_bytes())
            if value != expected:
                raise ValueError("Declared initial-law production source changed: "+name)
            own[str(HERE/name)] = value
        own[str(Path(__file__).resolve())] = digest(Path(__file__).read_bytes())
        unused, core_record = core_source()
        original, provenance = pulse_build(configuration, disk_configuration)
        edits = [
            ("'loop_ratio', 'initial_speed_pulse')",
             "'loop_ratio', 'initial_speed_pulse', 'initial_speed_frontload')"),
            ("reference['frozen_profile'].get(name,0.) if name=='initial_speed_pulse' else reference['frozen_profile'][name]",
             "reference['frozen_profile'].get(name,0.) if name in ('initial_speed_pulse','initial_speed_frontload') else reference['frozen_profile'][name]"),
            ("    from strong_pulse_augmented_core import load_augmented_core\n",
             "    from strong_initial_laws_augmented_core import load_augmented_core\n"),
            ("                pulse_hook.install(value)\n",
             "                pulse_hook.install(value)\n"
             "                import strong_monotone_initial_speed as frontload_hook\n"
             "                frontload_hook.install(value)\n"),
            ("    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}",
             "    source_names += ('strong_initial_laws_actual_bvp.py',"
             "'strong_initial_laws_augmented_core.py','strong_monotone_initial_speed.py')\n"
             "    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}"),
        ]
        source = original
        for before, after in edits:
            if source.count(before) != 1:
                raise ValueError("Initial-law production anchor not unique: "+repr(before))
            source = source.replace(before, after, 1)
        ast.parse(source, filename="<original-actual-initial-laws-production>")
        reverse = source
        for before, after in reversed(edits):
            if reverse.count(after) != 1:
                raise ValueError("Initial-law production reverse anchor differs")
            reverse = reverse.replace(after, before, 1)
        if reverse != original:
            raise ValueError("Initial-law adapter altered other production code")
        record = dict(provenance)
        record["source_sha256"] = {**provenance["source_sha256"], **own}
        record["prior_transformed_source_sha256"] = provenance["transformed_source_sha256"]
        record["transformed_source_sha256"] = digest(source.encode())
        record["replacements"] = list(provenance["replacements"]) + [
            dict(before=a, after=b, count=1) for a, b in edits]
        record["monotone_initial_law_actual_adapter"] = dict(scope=__doc__,
            physical_profile_key="initial_speed_frontload", absent_value=0.,
            fixed_degree_key="initial_speed_frontload_degree", absent_degree=22,
            provider_sha256=EXPECTED["strong_monotone_initial_speed.py"],
            augmented_default_transform=core_record,
            default_zero_delegates_original_geometry=True,
            every_nonzero_reload_requires_same_provider=True,
            complete_actual_warm_field_and_original_RMS_full_H_audit_gates_preserved=True,
            all_MJS_unchanged=True, original_outer_method_preserved=True,
            exact_reverse_recovers_original_pulse_production=True)
        return source, record
    return build


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument("--prefix-cache-directory", type=Path)
    parser.add_argument("--prefix-cache-budget-MiB", type=int, default=256)
    parser.add_argument("--prepare-source-record", type=Path)
    own, remaining = parser.parse_known_args()
    if not 1 <= own.prefix_cache_budget_MiB <= 256:
        raise ValueError("Keep the original explicit prefix cache budget")
    configuration = dict(
        directory=(str(own.prefix_cache_directory.resolve()) if own.prefix_cache_directory
            else "SOURCE-ONLY-NOT-A-PRODUCTION-CACHE"),
        budget_bytes=own.prefix_cache_budget_MiB*1024**2, inspect_output=None)
    if own.prepare_source_record:
        fresh = resource.retained_module()
        source, record = resource.resource_build(
            cached.build_wrapper(initial_laws_build(fresh.build_source), configuration), 96, 4)(
            {"stage_cache_directory":"SOURCE-ONLY-NOT-A-PRODUCTION-CACHE"},
            {"temporary_parent":None, "backward_error_tolerance":5e-11, "heartbeat_seconds":20.})
        with own.prepare_source_record.open("x") as stream:
            json.dump(dict(scope="Source-only exact transform/reverse/AST preparation; no Flow/RHS/Jac/Node or BVP.",
                prepared=True, production_executed=False, source_bytes=len(source.encode()),
                transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
                provenance=record), stream, indent=2)
            stream.write("\n")
        print(json.dumps(dict(prepared=True, production_executed=False,
            transformed_source_sha256=record["transformed_source_sha256"])), flush=True)
        return
    if own.prefix_cache_directory is None:
        raise ValueError("Give one fresh or exact-identity prefix storage directory")
    old_configuration, original_retained, old_argv = (
        cache.RUNTIME_CONFIGURATION, resource.retained_module, sys.argv)
    def retained():
        value = original_retained()
        value.build_source = cached.build_wrapper(initial_laws_build(value.build_source), configuration)
        return value
    resource.retained_module = retained
    cache.RUNTIME_CONFIGURATION = configuration
    sys.argv = [old_argv[0], *remaining]
    try:
        resource.main()
    finally:
        resource.retained_module = original_retained
        cache.RUNTIME_CONFIGURATION = old_configuration
        sys.argv = old_argv


if __name__ == "__main__":
    main()
