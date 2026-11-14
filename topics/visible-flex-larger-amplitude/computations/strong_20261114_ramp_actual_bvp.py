#!/usr/bin/env python3
"""Continue the actual surface with a declared first-turn ramp design control.

This extends the original loop-control entry only by descending_turn_ramp.
Absent or .08 reproduces the original profile. Nondefault values change the
prefix scalar metric; the complete finite bridge and physical tail remain
attached by their original checks. All 35 unknowns, full-H solves, Newton,
physical BC, RMS and final audit gates remain unchanged.
"""
from __future__ import annotations
import ast
import hashlib
import os
from pathlib import Path

for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import strong_full_tangent_initial_laws_anchor_actual_bvp as entry

EXTRA = ('loop_curvature', 'loop_radius', 'loop_speed',
         'terminal_peak_fraction', 'descending_turn_ramp')
SOURCE = Path(__file__).resolve()


def main():
    previous = entry.ORIGINAL_BUILD

    def ramp_build(original_build):
        retained = previous(original_build)

        def build(configuration, disk_configuration):
            source, prior = retained(configuration, disk_configuration)
            control_before = "'loop_ratio', 'initial_speed_pulse', 'initial_speed_frontload')"
            lookup = "reference['frozen_profile'].get(name,0.) if name in ('initial_speed_pulse','initial_speed_frontload') else reference['frozen_profile'][name]"
            anchor = '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'
            edits = [
                (control_before, control_before[:-1] + ', ' + ', '.join(map(repr, EXTRA)) + ')'),
                (lookup, "reference['frozen_profile'].get(name,.08) if name=='descending_turn_ramp' else (" + lookup + ')'),
                ('    from strong_initial_laws_augmented_core import load_augmented_core\n',
                 '    from strong_20261114_ramp_augmented_core import load_augmented_core\n'),
                ('                frontload_hook.install(value)\n',
                 '                frontload_hook.install(value)\n'
                 '                import strong_20261114_descending_turn_ramp as ramp_hook\n'
                 '                ramp_hook.install(value)\n'),
                (anchor, "    source_names += ('strong_20261114_ramp_actual_bvp.py',"
                 "'strong_20261114_ramp_augmented_core.py','strong_20261114_descending_turn_ramp.py',"
                 "'strong_20261114_loop_augmented_core.py','strong_20261114_loop_bridge.py')\n" + anchor),
            ]
            for before, after in edits:
                if source.count(before) != 1:
                    raise ValueError('Ramp actual source anchor differs: ' + repr(before))
                source = source.replace(before, after, 1)
            ast.parse(source)
            record = dict(prior)
            record['source_sha256'] = {**prior['source_sha256'],
                str(SOURCE): hashlib.sha256(SOURCE.read_bytes()).hexdigest()}
            record['transformed_source_sha256'] = hashlib.sha256(source.encode()).hexdigest()
            record['replacements'] = list(prior['replacements']) + [
                dict(before=a, after=b, count=1) for a, b in edits]
            record['descending_ramp_actual'] = dict(scope=__doc__,
                added_physical_controls=list(EXTRA), absent_ramp=.08,
                prefix_metric_changes_for_nondefault=True,
                original_all_core_geometry_unknowns_and_gates_retained=True,
                original_full_current_H_solve_and_audit_retained=True)
            return source, record

        return build

    entry.ORIGINAL_BUILD = ramp_build
    try:
        entry.main()
    finally:
        entry.ORIGINAL_BUILD = previous


if __name__ == '__main__':
    main()
