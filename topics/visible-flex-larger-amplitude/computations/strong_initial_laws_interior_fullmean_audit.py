#!/usr/bin/env python3
"""Reload the accepted physical quintic with the declared initial-speed law.

This adds only the existing pulse/frontload providers to the saved physical
loader used by the frozen complete-mean interior audit. Its original C2
polynomial, curvature and metric formulas, complete mean rule and sampling
grid are unchanged. Every reported number remains a finite sample, not a
continuous certificate or a new nonlinear solution.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_interior_jet_fullmean_audit.py':
        '5622e694bd16a3a8a294d564cdab42bcec33555cf212ebc1d26ff342fcc999e0',
    'strong_interior_jet_audit.py':
        '1b7f45785fffc41595eda9aae844c3081d2954d3ea08ac0da6e5a90c935294fa',
    'geometric-checkpoint-core-pullback.py':
        'd319574d946f2f6c465b76ffeb92117201aa95bc4318e7100377b184a530fa33',
    'strong_initial_speed_pulse.py':
        'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',
    'strong_monotone_initial_speed.py':
        '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def install_audit_loader(original, observations):
    def load(name, path):
        value = original(name, path)
        if Path(path).name != 'geometric-checkpoint-core-pullback.py':
            return value
        original_module = value.module

        def module(provider_name, provider_path):
            provider = original_module(provider_name, provider_path)
            if Path(provider_path).name == 'alternative-neck-provider.py':
                import strong_initial_speed_pulse as pulse
                import strong_monotone_initial_speed as frontload
                pulse.install(provider)
                frontload.install(provider)
                observations['provider_loads'] += 1
            return provider

        value.module = module
        original_saved = value.load_saved

        def load_saved(*args, **kwargs):
            saved, loader = original_saved(*args, **kwargs)
            record = saved.rec
            if not record.get('solver_success') or record.get('audit_pending', True):
                raise ValueError('A fully accepted actual endpoint is required')
            profile = record['frozen_profile']
            actual = saved.flow._alternative_neck
            if actual.cfg != profile:
                raise ValueError('The reloaded initial-law physical profile differs')
            weight = float(profile.get('initial_speed_frontload', 0.))
            pulse = float(profile.get('initial_speed_pulse', 0.))
            degree = profile.get('initial_speed_frontload_degree', 22)
            first = actual.segments[0]
            if weight != 0. and (
                    first.get('strong_initial_speed_frontload') != weight or
                    first.get('strong_initial_speed_frontload_degree') != degree or
                    not first.get('strong_initial_speed_frontload_nonnegative_derivative_hull')):
                raise ValueError('The saved nonzero frontload law was not actually installed')
            observations['saved_fields'].append(dict(
                initial_speed_frontload=weight, initial_speed_pulse=pulse,
                initial_speed_frontload_degree=degree,
                physical_profile_unchanged=True,
                zero_weight_uses_original_arithmetic=(weight == 0. and pulse == 0.),
                physical_length=float(saved.flow.end),
                physical_length_original_gate_passed=True))
            return saved, loader

        value.load_saved = load_saved
        return value

    return load


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--out', type=Path, required=True)
    own, unused = parser.parse_known_args()
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('The frozen physical audit/provider changed: '+name)
    source = (HERE/'strong_interior_jet_fullmean_audit.py').read_text()
    before = "    namespace['main']()\n"
    after = ("    namespace['load'] = INITIAL_LAWS_AUDIT_LOADER(namespace['load'])\n"
             + before)
    if source.count(before) != 1:
        raise ValueError('The complete-mean loader hook is not unique')
    changed = source.replace(before, after, 1)
    ast.parse(changed, filename='<complete-mean-with-initial-law-loader>')
    if changed.count(after) != 1 or changed.replace(after, before, 1) != source:
        raise ValueError('The loader hook changed other complete-mean code')
    observations = dict(provider_loads=0, saved_fields=[])
    namespace = dict(__file__=str(Path(__file__).resolve()),
        __name__='strong_initial_laws_frozen_fullmean_audit',
        INITIAL_LAWS_AUDIT_LOADER=lambda old: install_audit_loader(old, observations))
    exec(compile(changed, '<complete-mean-with-initial-law-loader>', 'exec'), namespace)
    namespace['main']()
    if observations['provider_loads'] != 1 or len(observations['saved_fields']) != 1:
        raise RuntimeError('Expected exactly one actual saved field/provider load')
    result = json.loads(own.out.read_text())
    result['initial_laws_provider_adapter'] = dict(
        scope=__doc__, observations=observations,
        source_sha256={**EXPECTED, Path(__file__).name: sha(__file__)},
        complete_mean_source_transformed_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        exact_reverse_recovers_original_complete_mean_source=True,
        original_physical_quintic_and_all_metric_curvature_formulas_unchanged=True,
        numerical_solution_or_continuous_certificate_created=False)
    temporary = own.out.with_name(own.out.name+'.initial-laws.tmp')
    temporary.write_text(json.dumps(result, indent=2)+'\n')
    temporary.replace(own.out)


if __name__ == '__main__':
    main()
