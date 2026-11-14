#!/usr/bin/env python3
"""Continue actual A with genuine loop-profile controls and their responses.

This extends the explicit physical design interface by the four loop controls
implemented by the original provider. It retains all core unknowns and the
three delta/LB/vp unknowns, original full-H nonlinear tail coupling, fixed
physical merit, RMS criterion and final physical audits. The complete local
response is only an initial guess. These design changes are not same-g
refinement and cannot by themselves certify any closed surface or amplitude.
"""
from __future__ import annotations

import ast
import hashlib
import os
from pathlib import Path

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import strong_full_tangent_initial_laws_anchor_actual_bvp as entry

EXTRA = ("loop_curvature", "loop_radius", "loop_speed", "terminal_peak_fraction")
SOURCE = Path(__file__).resolve()


def main():
    previous = entry.ORIGINAL_BUILD

    def loop_build(original_build):
        retained = previous(original_build)

        def build(configuration, disk_configuration):
            source, provenance = retained(configuration, disk_configuration)
            before = "'loop_ratio', 'initial_speed_pulse', 'initial_speed_frontload')"
            after = before[:-1] + ", " + ", ".join(repr(name) for name in EXTRA) + ")"
            if source.count(before) != 1:
                raise ValueError("The existing physical design-control list differs")
            source = source.replace(before, after, 1)
            core_before = "    from strong_initial_laws_augmented_core import load_augmented_core\n"
            core_after = "    from strong_20261114_loop_augmented_core import load_augmented_core\n"
            if source.count(core_before) != 1:
                raise ValueError("The actual augmented core import differs")
            source = source.replace(core_before, core_after, 1)
            anchor = "    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}"
            if source.count(anchor) != 1:
                raise ValueError("The existing numerical source list differs")
            source = source.replace(anchor,
                "    source_names += ('strong_20261114_loop_actual_bvp.py',"
                "'strong_20261114_loop_augmented_core.py','strong_20261114_loop_bridge.py')\n" + anchor, 1)
            ast.parse(source)
            result = dict(provenance)
            result["source_sha256"] = {**provenance["source_sha256"],
                str(SOURCE): hashlib.sha256(SOURCE.read_bytes()).hexdigest()}
            result["transformed_source_sha256"] = hashlib.sha256(source.encode()).hexdigest()
            result["replacements"] = list(provenance["replacements"]) + [
                dict(before=before, after=after, count=1),
                dict(before=core_before, after=core_after, count=1)]
            result["loop_profile_actual_continuation"] = dict(
                scope=__doc__, added_physical_controls=list(EXTRA),
                new_control_uses_full_real_response=True,
                all_core_and_three_geometry_unknowns_preserved=True,
                physical_metric_changes=True,
                prefix_and_finite_bridge_controls_synchronized=True,
                physical_infinite_tail_cut_and_parameters_unchanged=True,
                original_tail_RMS_physical_BC_and_audit_gates_preserved=True)
            return source, result

        return build

    entry.ORIGINAL_BUILD = loop_build
    try:
        entry.main()
    finally:
        entry.ORIGINAL_BUILD = previous


if __name__ == "__main__":
    main()
