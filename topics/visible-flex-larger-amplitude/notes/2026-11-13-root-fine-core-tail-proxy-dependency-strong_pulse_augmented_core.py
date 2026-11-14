#!/usr/bin/env python3
"""Explicit optional pulse default for the retained all-core actual factory.

Only the absent initial_speed_pulse baseline value is defined to be zero.
Every other control lookup, parameter layout, physical equation, derivative,
chart, raw conversion and acceptance condition remains the original source.
"""
import ast
import hashlib
from pathlib import Path
import types

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE/'strong_actual_augmented_core.py'
EXPECTED = '74c64ab558953c6d0378948dd4affb5d354d1faaecab7922b83cfdf76041bad7'
BEFORE = '        **{name: baseline_profile[name]+value for name, value in external_shifts.items()}}'
AFTER = ('        **{name: (baseline_profile.get(name,0.) if name==\'initial_speed_pulse\' '
         'else baseline_profile[name])+value for name, value in external_shifts.items()}}')


def transformed_source():
    original = TEMPLATE.read_text()
    digest = lambda value: hashlib.sha256(value).hexdigest()
    if digest(original.encode()) != EXPECTED or original.count(BEFORE) != 1:
        raise ValueError('Retained augmented-core source or pulse anchor changed')
    source = original.replace(BEFORE,AFTER,1)
    if source.count(AFTER) != 1 or source.replace(AFTER,BEFORE,1) != original:
        raise ValueError('The single pulse-default replacement is not reversible')
    ast.parse(source,filename='<pulse-default-original-actual-augmented-core>')
    return source,dict(scope=__doc__,original_sha256=EXPECTED,
        transformed_sha256=digest(source.encode()),
        adapter_sha256=digest(Path(__file__).read_bytes()),
        replacements=[dict(before=BEFORE,after=AFTER,count=1)],
        exact_reverse_recovers_original=True,default_pulse=0.,
        all_other_profile_keys_still_required=True,
        all_original_actual_equations_and_gates_unchanged=True)


def load_augmented_core():
    source,record = transformed_source()
    module = types.ModuleType('strong_pulse_original_augmented_core')
    module.__file__ = str(TEMPLATE)
    exec(compile(source,'<pulse-default-original-actual-augmented-core>','exec'),module.__dict__)
    module.pulse_default_source_transform = record
    return module
