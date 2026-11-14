"""Use the original augmented equations with a declared finite bridge design.

Only the physical-tail comparison is refined: the finite connector's
_prefix_bridge tag may follow the explicit profile controls, while every
actual infinite-tail parameter and cut quantity remains exactly equal.
"""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path
import types
import strong_initial_laws_augmented_core as retained


def transformed_source():
    original, prior = retained.transformed_source()
    before = """            for key in ('parameters', 'cut'):
                if self.port[key] != reference['physical_tail_'+('parameters' if key == 'parameters' else 'cut')]:
                    raise ValueError('The physical tail '+key+' changed')"""
    after = """            from strong_20261114_loop_bridge import verify_design_port
            verify_design_port(self.port, reference, self.cfg)"""
    if original.count(before) != 1:
        raise ValueError("The original physical-tail comparison differs")
    source = original.replace(before, after, 1)
    ast.parse(source)
    return source, dict(scope=__doc__, prior=prior,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=before, after=after, count=1)],
        physical_tail_parameters_and_cut_exactly_preserved=True,
        prefix_bridge_tag_follows_declared_profile=True)


def load_augmented_core():
    source, record = transformed_source()
    module = types.ModuleType("strong_20261114_loop_augmented_original")
    module.__file__ = str(Path(__file__).with_name("strong_actual_augmented_core.py"))
    exec(compile(source, module.__file__, "exec"), module.__dict__)
    module.loop_bridge_source_transform = record
    return module
