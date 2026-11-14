#!/usr/bin/env python3
"""Actual three-control continuation with an explicit external speed pulse.

The saved accepted baseline, true complete-H tail, fixed material/numerical
charts, all core unknowns, delta/LB/vp controls, disk QR, fixed physical merit
and every original final gate remain. The optional initial_speed_pulse is a
new physical prefix design parameter. A nonzero saved pulse requires this
same provider hook for all later physical reloads and fixed-view conversions.
This entry does not accept background budgets or tangent warm fields as a
new actual solution. It does not change any MJS source or tail cache identity.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

import strong_fresh_resource_actual_bvp as resource
from strong_pulse_augmented_core import transformed_source as augmented_source

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_fresh_resource_actual_bvp.py':
        '26f0c2ba1bdbb413ba7819f8f1aaafa7892787a7e14509357b6a28821e8c808f',
    'strong_initial_speed_pulse.py':
        'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',
    'strong_actual_augmented_core.py':
        '74c64ab558953c6d0378948dd4affb5d354d1faaecab7922b83cfdf76041bad7',
}


def pulse_build(original_build):
    def build(configuration,disk_configuration):
        digest = lambda value: hashlib.sha256(value).hexdigest()
        own = {}
        for name,expected in EXPECTED.items():
            if digest((HERE/name).read_bytes()) != expected:
                raise ValueError('Retained pulse-production source changed: '+name)
            own[str(HERE/name)] = expected
        for name in ('strong_pulse_actual_bvp.py','strong_pulse_augmented_core.py'):
            own[str(HERE/name)] = digest((HERE/name).read_bytes())
        unused,augmented = augmented_source()
        original,provenance = original_build(configuration,disk_configuration)
        edits = [
            ("            'descending_sync_curvature', 'coast_outward', 'loop_ratio')",
             "            'descending_sync_curvature', 'coast_outward', 'loop_ratio', 'initial_speed_pulse')"),
            ("        **{name: reference['frozen_profile'][name]+value for name, value in external_shifts.items()}}",
             "        **{name: (reference['frozen_profile'].get(name,0.) if name=='initial_speed_pulse' else reference['frozen_profile'][name])+value for name, value in external_shifts.items()}}"),
            ('    import strong_actual_augmented_core as augmented',
             '    from strong_pulse_augmented_core import load_augmented_core\n'
             '    augmented = load_augmented_core()'),
            ('    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}',
             "    source_names += ('strong_pulse_actual_bvp.py','strong_pulse_augmented_core.py','strong_initial_speed_pulse.py')\n"
             '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'),
            ('        source_factory = loaded.make_dual\n        original_main = loaded.main',
             '        original_provider_loader = loaded.module\n'
             '        def pulse_provider_loader(provider_name,provider_path):\n'
             '            value = original_provider_loader(provider_name,provider_path)\n'
             "            if Path(provider_path).name=='alternative-neck-provider.py':\n"
             '                import strong_initial_speed_pulse as pulse_hook\n'
             '                pulse_hook.install(value)\n'
             '            return value\n'
             '        loaded.module = pulse_provider_loader\n'
             '        source_factory = loaded.make_dual\n        original_main = loaded.main'),
        ]
        source = original
        for before,after in edits:
            if source.count(before) != 1:
                raise ValueError('Pulse-production source anchor not unique: '+repr(before))
            source = source.replace(before,after,1)
        ast.parse(source,filename='<pulse-original-actual-production>')
        reverse = source
        for before,after in reversed(edits):
            if reverse.count(after) != 1:
                raise ValueError('Pulse-production reverse anchor not unique')
            reverse = reverse.replace(after,before,1)
        if reverse != original:
            raise ValueError('Pulse-production transforms changed additional source')
        record = dict(provenance)
        record['source_sha256'] = {**provenance['source_sha256'],**own}
        record['prior_transformed_source_sha256'] = provenance['transformed_source_sha256']
        record['transformed_source_sha256'] = digest(source.encode())
        record['replacements'] = list(provenance['replacements']) + [
            dict(before=a,after=b,count=1) for a,b in edits]
        record['initial_speed_pulse_actual_adapter'] = dict(scope=__doc__,
            provider_hook_sha256=EXPECTED['strong_initial_speed_pulse.py'],
            physical_profile_key='initial_speed_pulse',absent_baseline_value=0.,
            augmented_default_source_transform=augmented,
            default_zero_delegates_original_geometry=True,
            nonzero_pulse_changes_physical_metric=True,
            every_nonzero_pulse_reload_requires_same_provider_hook=True,
            original_baseline_raw_and_full_H_identity_checks_preserved=True,
            full_actual_J_tangent_required_for_external_pulse_step=True,
            original_RMS_true_H_full_Jacobian_audit_final_gates_preserved=True,
            all_MJS_and_tail_cache_identity_unchanged=True,
            exact_reverse_recovers_prior_production_source=True)
        return source,record
    return build


def main():
    parser = argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--prepare-pulse-source-record',type=Path)
    own,remaining = parser.parse_known_args()
    if own.prepare_pulse_source_record:
        # The source-builder uses only this directory field. No baseline or
        # physical object is loaded; these dictionaries are syntax fixtures.
        fresh = resource.retained_module()
        source,record = resource.resource_build(pulse_build(fresh.build_source),96,4)(
            {'stage_cache_directory':'SOURCE-ONLY-NOT-A-PRODUCTION-CACHE'},
            {'temporary_parent':None,'backward_error_tolerance':5e-11,'heartbeat_seconds':20.})
        report = dict(scope='Source-only exact transform/reverse/AST check; no Flow/RHS/Jac/BVP/Node executed.',
            prepared=True,production_executed=False,source_bytes=len(source.encode()),
            transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),provenance=record)
        with own.prepare_pulse_source_record.open('x') as stream:
            json.dump(report,stream,indent=2);stream.write('\n')
        print(json.dumps(dict(prepared=True,production_executed=False,
            transformed_source_sha256=report['transformed_source_sha256'])),flush=True)
        return
    original_retained,old_argv = resource.retained_module,sys.argv
    def retained():
        value = original_retained()
        value.build_source = pulse_build(value.build_source)
        return value
    resource.retained_module = retained
    sys.argv = [old_argv[0],*remaining]
    try:
        resource.main()
    finally:
        resource.retained_module = original_retained
        sys.argv = old_argv


if __name__ == '__main__':
    main()
