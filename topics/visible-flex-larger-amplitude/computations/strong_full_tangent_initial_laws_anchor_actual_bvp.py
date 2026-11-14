#!/usr/bin/env python3
"""Use the corrected first-append anchor in the original actual BVP entry.

Only the explicit prefix provider import is changed, with both source hashes
and the exact reversible transform in production provenance. All-core plus
delta/LB/vp layout, optional-control defaults, full-flow warm storage, Newton,
true full-H boundary, RMS and physical audit remain the original routines.
The already running zero-law M32 refinement is unrelated and is not changed.
"""
from __future__ import annotations
import ast
import hashlib
from pathlib import Path
import strong_initial_laws_actual_bvp as laws
import strong_full_tangent_initial_laws_actual_bvp as full

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_initial_laws_actual_bvp.py': '55af2c6b3f2fb91631481ed0078d89b608fe37eb439b46eb7b17f999fc65d9cc',
    'strong_full_tangent_initial_laws_actual_bvp.py': '31868ba1465e489a9eecc1423a9bde567de0946b0f75e02c9bc627b998991b42',
    'strong_initial_laws_augmented_core.py': '067940d3d2f581beebf1fd64e0649c80d9d5eaa61052fa8c2ab6cd54f5004646',
    'strong_monotone_initial_speed.py': '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py': '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def anchor_build(original_build):
    previous = ORIGINAL_BUILD(original_build)
    def build(configuration, disk_configuration):
        source, prior = previous(configuration, disk_configuration)
        edits = [
            ('                import strong_monotone_initial_speed as frontload_hook\n',
             '                import strong_monotone_initial_speed_anchor as frontload_hook\n'),
            ('    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}',
             "    source_names += ('strong_monotone_initial_speed_anchor.py',"
             "'strong_full_tangent_initial_laws_anchor_actual_bvp.py')\n"
             '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'),
        ]
        changed = source
        for before, after in edits:
            if changed.count(before) != 1:
                raise ValueError('Original production anchor import/identity is not unique')
            changed = changed.replace(before, after, 1)
        reverse = changed
        for before, after in reversed(edits):
            if reverse.count(after) != 1:
                raise ValueError('Original production reverse anchor differs')
            reverse = reverse.replace(after, before, 1)
        if reverse != source:
            raise ValueError('The first-append fix changed another production site')
        ast.parse(changed, filename='<actual-original-first-append-anchor>')
        import strong_monotone_initial_speed_anchor as anchor
        record = dict(prior)
        record['source_sha256'] = {**prior['source_sha256'],
            str(HERE/'strong_monotone_initial_speed_anchor.py'): EXPECTED['strong_monotone_initial_speed_anchor.py'],
            str(Path(__file__)): sha(__file__)}
        record['prior_transformed_source_sha256'] = prior['transformed_source_sha256']
        record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
        record['replacements'] = list(prior['replacements'])+[
            dict(before=a, after=b, count=1) for a, b in edits]
        record['first_append_anchor_actual_adapter'] = dict(scope=__doc__,
            provider_source_identity=anchor.source_identity(),
            actual_augmented_core_and_layout_unchanged=True,
            optional_zero_defaults_unchanged=True,
            initial_law_installation_order='original angle, original pulse, corrected frontload',
            complete_original_nonlinear_acceptance_gates_unchanged=True,
            exact_reverse_recovers_original_initial_laws_production=True)
        return changed, record
    return build


ORIGINAL_BUILD = laws.initial_laws_build


def main():
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen original/anchor source differs: '+name)
    original = laws.initial_laws_build
    laws.initial_laws_build = anchor_build
    try:
        full.main()
    finally:
        laws.initial_laws_build = original


if __name__ == '__main__':
    main()
