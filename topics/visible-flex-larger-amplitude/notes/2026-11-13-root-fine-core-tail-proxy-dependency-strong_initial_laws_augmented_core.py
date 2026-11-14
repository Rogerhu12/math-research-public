#!/usr/bin/env python3
"""Optional absent defaults for pulse and monotone physical design controls.

Only these two explicit profile keys may be absent with value zero. Every
other baseline lookup, all-core/geometry parameter layout, raw/chart mapping,
physical equation, derivative and original acceptance gate remains unchanged.
"""
import ast
import hashlib
from pathlib import Path
import types
import strong_pulse_augmented_core as pulse

HERE = Path(__file__).resolve().parent
EXPECTED = "4fabc9ef77753185ed83e7bd7ff26854522d4a4a363c10a6841332944e8fb1a4"


def transformed_source():
    digest = lambda value: hashlib.sha256(value).hexdigest()
    if digest((HERE/"strong_pulse_augmented_core.py").read_bytes()) != EXPECTED:
        raise ValueError("Retained pulse optional-default adapter changed")
    original, prior = pulse.transformed_source()
    before = "baseline_profile.get(name,0.) if name=='initial_speed_pulse' else baseline_profile[name]"
    after = "baseline_profile.get(name,0.) if name in ('initial_speed_pulse','initial_speed_frontload') else baseline_profile[name]"
    if original.count(before) != 1:
        raise ValueError("Optional-default anchor is not unique")
    source = original.replace(before, after, 1)
    ast.parse(source, filename="<original-actual-first-piece-defaults>")
    if source.count(after) != 1 or source.replace(after, before, 1) != original:
        raise ValueError("Optional-default reverse does not recover original source")
    return source, dict(scope=__doc__, prior=prior, pulse_adapter_sha256=EXPECTED,
        adapter_sha256=digest(Path(__file__).read_bytes()),
        prior_transformed_sha256=digest(original.encode()),
        transformed_sha256=digest(source.encode()),
        replacements=[dict(before=before, after=after, count=1)],
        missing_defaults={"initial_speed_pulse":0., "initial_speed_frontload":0.},
        every_other_profile_key_remains_required=True,
        every_original_actual_equation_and_gate_unchanged=True)


def load_augmented_core():
    source, record = transformed_source()
    module = types.ModuleType("strong_initial_laws_original_augmented_core")
    module.__file__ = str(HERE/"strong_actual_augmented_core.py")
    exec(compile(source, "<original-actual-first-piece-defaults>", "exec"), module.__dict__)
    module.initial_laws_default_source_transform = record
    return module
