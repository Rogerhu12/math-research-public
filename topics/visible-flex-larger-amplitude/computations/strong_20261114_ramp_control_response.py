#!/usr/bin/env python3
"""Original full-field response with the first descending-turn ramp control.

All original actual-field, full-H, full/half forcing and backward checks are
retained. The existing loop bridge is rebuilt by its original adapter.
The ramp is a new physical prefix metric direction, not a same-g refinement.
No nonlinear solution follows from this derivative computation.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path
import strong_20261114_loop_control_response as loop

SOURCE = Path(__file__).resolve()


def main():
    old_extra, old_anchor_main = loop.EXTRA, loop.anchor.main
    loop.EXTRA = (*old_extra, 'descending_turn_ramp')

    def with_ramp_anchor():
        # loop.main has installed its complete loop/bridge transform here.
        retained = loop.laws.transformed_source

        def transformed():
            source, prior = retained()
            lookup = "baseline_cfg.get(field,0.) if field in ('initial_speed_pulse','initial_speed_frontload') else baseline_cfg[field]"
            edits = [
                (lookup, "baseline_cfg.get(field,.08) if field=='descending_turn_ramp' else (" + lookup + ')'),
                ('                    frontload_hook.install(value)\n',
                 '                    frontload_hook.install(value)\n'
                 '                    import strong_20261114_descending_turn_ramp as ramp_hook\n'
                 '                    ramp_hook.install(value)\n'),
            ]
            for before, after in edits:
                if source.count(before) != 1:
                    raise ValueError('Ramp response source anchor differs: ' + repr(before))
                source = source.replace(before, after, 1)
            ast.parse(source)
            record = dict(prior)
            record['source_sha256'] = {**prior['source_sha256'],
                str(SOURCE): hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                str(SOURCE.with_name('strong_20261114_descending_turn_ramp.py')):
                    hashlib.sha256(SOURCE.with_name('strong_20261114_descending_turn_ramp.py').read_bytes()).hexdigest()}
            record['transformed_source_sha256'] = hashlib.sha256(source.encode()).hexdigest()
            record['explicit_transforms'] = list(prior['explicit_transforms']) + [
                dict(before=a, after=b, replacements=1) for a, b in edits]
            record['descending_ramp_response'] = dict(scope=__doc__,
                physical_control='descending_turn_ramp', absent_value=.08,
                original_baseline_matrix_and_tail_J=True,
                original_full_half_forcing_and_backward_gates=True)
            return source, record

        loop.laws.transformed_source = transformed
        try:
            old_anchor_main()
        finally:
            loop.laws.transformed_source = retained

    loop.anchor.main = with_ramp_anchor
    try:
        loop.main()
    finally:
        loop.EXTRA, loop.anchor.main = old_extra, old_anchor_main


if __name__ == '__main__':
    main()
