"""Retain the actual all-core equations with one declared optional ramp default.

The new physical design field descending_turn_ramp has absent value .08.
The loop bridge and physical-tail checks are those of the existing loop core.
This does not create an additional unknown or alter a boundary condition.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path
import types
import strong_20261114_loop_augmented_core as loop


def transformed_source():
    source, prior = loop.transformed_source()
    before = "baseline_profile.get(name,0.) if name in ('initial_speed_pulse','initial_speed_frontload') else baseline_profile[name]"
    after = "baseline_profile.get(name,.08) if name=='descending_turn_ramp' else (" + before + ")"
    if source.count(before) != 1:
        raise ValueError('The original optional physical-control lookup differs')
    changed = source.replace(before, after, 1)
    ast.parse(changed)
    return changed, dict(scope=__doc__, prior=prior,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        replacement=dict(before=before, after=after, count=1),
        default_ramp=.08, original_core_and_three_geometry_layout=True)


def load_augmented_core():
    source, record = transformed_source()
    module = types.ModuleType('strong_20261114_ramp_augmented_original')
    module.__file__ = str(Path(__file__).with_name('strong_actual_augmented_core.py'))
    exec(compile(source, module.__file__, 'exec'), module.__dict__)
    module.descending_ramp_source_transform = record
    return module
