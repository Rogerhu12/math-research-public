#!/usr/bin/env python3
"""Add the explicit initial-speed-pulse direction to the original actual response.

This is still the original accepted fixed-view full-field Jacobian response,
with disk storage, full backward checks, and half-step forcing checks.  The
provider hook is installed on the actual nested root-dual provider loader.
At an absent/zero pulse the original baseline geometry is delegated exactly;
nonzero external perturbations are new metric directions, never refinements.
No altered BVP or nonlinear acceptance is introduced.  A saved M+3 endpoint
must undergo the original genuine fixed-view conversion before using this.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import strong_disk_actual_fixed_control_response as disk

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_disk_actual_fixed_control_response.py': 'e20e9724b82130848562142ac23cec3c65959949e5470436a643358b664ba0bf',
    'strong_initial_speed_pulse.py': 'f1d8c0867d598313da760fcd4910cd20c5f387afd7c6bd90a31b257848acbf73',
}
ORIGINAL_TRANSFORM = disk.transformed_source


def transformed_source():
    digest = lambda value: hashlib.sha256(value).hexdigest()
    added = {}
    for name, expected in EXPECTED.items():
        data = (HERE/name).read_bytes()
        if digest(data) != expected:
            raise ValueError('Frozen pulse-response source changed: '+name)
        added[str(HERE/name)] = expected
    added[str(Path(__file__))] = digest(Path(__file__).read_bytes())
    original, provenance = ORIGINAL_TRANSFORM()
    edits = [
        ("        'descending_sync_curvature','coast_outward','loop_ratio'))",
         "        'descending_sync_curvature','coast_outward','loop_ratio','initial_speed_pulse'))"),
        ("            original=float(baseline_cfg[field]);width=2e-6*max(.1,abs(original));forcings=[]",
         "            original=float(baseline_cfg.get(field,0.) if field=='initial_speed_pulse' else baseline_cfg[field]);width=2e-6*max(.1,abs(original));forcings=[]"),
        ("        if Path(path).name=='root_dual_core_bvp.py':\n            original_main=loaded.main",
         "        if Path(path).name=='root_dual_core_bvp.py':\n"
         "            original_provider_loader=loaded.module\n"
         "            def pulse_provider_loader(provider_name,provider_path):\n"
         "                value=original_provider_loader(provider_name,provider_path)\n"
         "                if Path(provider_path).name=='alternative-neck-provider.py':\n"
         "                    import strong_initial_speed_pulse as pulse_hook\n"
         "                    pulse_hook.install(value)\n"
         "                return value\n"
         "            loaded.module=pulse_provider_loader\n"
         "            original_main=loaded.main"),
        ("    input_report['disk_response_adapter'] = DISK_WRAPPER_PROVENANCE\n",
         "    input_report['disk_response_adapter'] = DISK_WRAPPER_PROVENANCE\n"
         "    input_report['initial_speed_pulse_adapter'] = DISK_WRAPPER_PROVENANCE['initial_speed_pulse_adapter']\n"),
    ]
    changed = original
    records = []
    for before, after in edits:
        count = changed.count(before)
        if count != 1:
            raise ValueError('Pulse-response transform anchor not unique: '+repr(before))
        changed = changed.replace(before, after, 1)
        records.append(dict(before=before, after=after, replacements=1))
    ast.parse(changed, filename='<pulse-direction-original-disk-actual-response>')
    reverse = changed
    for before, after in reversed(edits):
        if reverse.count(after) != 1:
            raise ValueError('Pulse response reverse anchor not unique')
        reverse = reverse.replace(after, before, 1)
    if reverse != original:
        raise ValueError('The explicit four changes did not reconstruct the original disk response')
    provenance['source_sha256'].update(added)
    provenance['initial_speed_pulse_adapter'] = dict(scope=__doc__,
        physical_profile_key='initial_speed_pulse', absent_baseline_value=0.,
        disk_only_transformed_source_sha256=digest(original.encode()),
        transformed_source_sha256=digest(changed.encode()), explicit_transforms=records,
        exact_reverse_of_four_transforms_recovers_original_disk_source=True,
        baseline_reference_and_raw_identity_unchanged=True,
        provider_default_zero_same_arithmetic=True,
        baseline_full_H_and_physical_BC_reproduction_still_required=True,
        full_Jacobian_and_half_step_and_stream_backward_checks_preserved=True,
        actual_new_BVP_or_nonlinear_acceptance=False)
    provenance['disk_only_transformed_source_sha256'] = provenance['transformed_source_sha256']
    provenance['transformed_source_sha256'] = digest(changed.encode())
    provenance['explicit_transforms'].extend(records)
    return changed, provenance


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--prepare-source-record', type=Path)
    opts, remaining = parser.parse_known_args()
    if opts.prepare_source_record:
        text, provenance = transformed_source()
        result = dict(scope='Source-only preparation; no saved raw/Flow/RHS/Jac/BVP/Node evaluated.',
            source_compiles=True, provenance=provenance, actual_response_executed=False,
            source_bytes=len(text.encode()))
        with opts.prepare_source_record.open('x') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
        print(json.dumps(dict(prepared=True, actual_response_executed=False,
            transformed_sha256=provenance['transformed_source_sha256'])), flush=True)
        return
    if '--response-fields' not in remaining:
        remaining += ['--response-fields', 'delta,boost_length,boost_speed,initial_speed_pulse']
    elif 'initial_speed_pulse' not in remaining[remaining.index('--response-fields')+1].split(','):
        raise ValueError('This explicit entry requires the initial_speed_pulse response field')
    old, old_argv = disk.transformed_source, sys.argv
    disk.transformed_source = transformed_source
    sys.argv = [old_argv[0], *remaining]
    try:
        disk.main()
    finally:
        disk.transformed_source = old
        sys.argv = old_argv


if __name__ == '__main__':
    main()
