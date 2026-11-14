#!/usr/bin/env python3
"""Retain supplemental wrapper provenance while matching every physical input.

AI-assisted research workflow, strong_recovery, 2026-11-13.
The original saved-six recovery lacks two wrapper-provenance fields that the
genuine supplemental response records. This fresh read-only bridge validates
those exact additions and preserves both, then executes the unchanged original
array, half-step, identity, core-exchange, and combination arithmetic.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import ast
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORIGINAL = HERE/'strong_merge_completed_six_missing_two.py'
ORIGINAL_SHA = 'a022090a89062002a591a062a40cd9bc1af83dfae0599ae448985a6766878e0b'
SOURCES = {
    'strong_actual_fixed_control_response.py': 'a2552b5b67e7555b3d402f10127a89fcf99eea566d7768a4050535c8105c2de1',
    'strong_disk_actual_backend.py': '402830e66390f660d7f8e846165a2ae7c1e9858addc2317df06348dc1e8634f1',
    'strong_initial_laws_disk_control_response.py': '42db431d26f8cc87b56f3e8baf38b7afba38816f701d185efd1955028afe9750',
    'strong_monotone_initial_speed.py': '12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7',
    'strong_monotone_initial_speed_anchor.py': '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
    'strong_samechart_initial_laws_anchor_response.py': 'd83947ea4f7457435a272863b9ba88a9a7ddfe551e76dc4db596c63dc61de212',
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def value_sha(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def check_identity(old, new, two):
    extras = {'disk_response_adapter', 'initial_speed_pulse_adapter'}
    if set(new)-set(old) != extras or set(old)-set(new):
        raise ValueError('Only the two observed supplemental provenance additions are allowed')
    if canonical(old) != canonical({k:v for k,v in new.items() if k not in extras}):
        raise ValueError('An original complete physical input identity still differs')
    disk, pulse = new['disk_response_adapter'], new['initial_speed_pulse_adapter']
    if (canonical(disk) != canonical(two['disk_block_storage']['adapter'])
            or canonical(pulse) != canonical(disk['initial_speed_pulse_adapter'])):
        raise ValueError('Supplemental provenance does not match its recorded disk wrapper')
    if disk['original_source_sha256'] != SOURCES['strong_actual_fixed_control_response.py']:
        raise ValueError('The actual original full-field response source differs')
    for name, expected in SOURCES.items():
        key = str(HERE/name)
        if (digest(HERE/name) != expected or disk['source_sha256'].get(key) != expected
                or two['source_sha256'].get(key) != expected):
            raise ValueError('A supplemental source identity is absent or changed: '+name)
    anchor = disk['first_append_anchor_response']
    if (canonical(anchor['missing_only']) != canonical(two['previous_completed_six'])
            or not anchor['original_complete_raw_H_tail_J_identity_preserved']
            or not anchor['original_full_field_and_external_half_step_gates_preserved']
            or not anchor['additional_half_and_forcing_storage_only']
            or not anchor['exact_reverse_recovers_original_initial_laws_response']):
        raise ValueError('The supplemental first-append provenance differs')
    provider = anchor['provider_source_identity']
    if (provider['original_source_sha256'] != SOURCES['strong_monotone_initial_speed.py']
            or provider['adapter_source_sha256'] != SOURCES['strong_monotone_initial_speed_anchor.py']
            or not provider['exact_reverse_recovers_original_source']
            or provider['only_changed_expression'] !=
            'first nonzero Hermite physical_piece a0 argument: segment[a0] -> self.aend'):
        raise ValueError('The declared zero-baseline first-append anchor identity differs')
    if (pulse['physical_profile_key'] != 'initial_speed_pulse'
            or pulse['absent_baseline_value'] != 0.0
            or not pulse['provider_default_zero_same_arithmetic']
            or not pulse['baseline_reference_and_raw_identity_unchanged']
            or not pulse['baseline_full_H_and_physical_BC_reproduction_still_required']
            or not pulse['full_Jacobian_and_half_step_and_stream_backward_checks_preserved']
            or pulse['actual_new_BVP_or_nonlinear_acceptance']):
        raise ValueError('The supplemental pulse-loader provenance differs')
    cfg = two['baseline']['profile']
    if cfg.get('initial_speed_pulse', 0.0) != 0.0 or cfg.get('initial_speed_frontload', 0.0) != 0.0:
        raise ValueError('This bridge binds the actual original zero-law baseline only')
    return dict(scope=__doc__, original_physical_input_keys=sorted(old),
        every_original_physical_input_equal=True,
        physical_input_identity_sha256=value_sha(old),
        supplemental_recorded_provenance={k:new[k] for k in sorted(extras)},
        supplemental_recorded_provenance_sha256={k:value_sha(new[k]) for k in sorted(extras)},
        all_original_input_packets_unmodified=True, baseline_zero_path_only=True,
        original_merger_sha256=ORIGINAL_SHA, identity_bridge_sha256=digest(__file__))


def main():
    if digest(ORIGINAL) != ORIGINAL_SHA:
        raise ValueError('The frozen original merger changed')
    source = ORIGINAL.read_text()
    replacements = [
        ("    if canon(old_identity) != canon(new_identity):\n"
         "        raise ValueError('The original complete H/raw/tail-J input identity differs')\n",
         "    input_identity_bridge = CHECK_ADDITIONAL_PROVENANCE(old_identity, new_identity, two)\n"),
        ("        assembly_source_sha256=sha(__file__), corrected_anchor_sha256=ANCHOR_SHA,\n",
         "        assembly_source_sha256=sha(__file__), corrected_anchor_sha256=ANCHOR_SHA,\n"
         "        input_identity_bridge=input_identity_bridge,\n"
         "        original_assembly_source_sha256=ORIGINAL_ASSEMBLY_SHA,\n"
         "        transformed_assembly_source_sha256=TRANSFORMED_ASSEMBLY_SHA,\n"
         "        identity_bridge_exact_reverse_recovers_original_merger=True,\n"),
    ]
    transformed = source
    for before, after in replacements:
        if transformed.count(before) != 1:
            raise ValueError('The exact original identity/metadata source site differs')
        transformed = transformed.replace(before, after, 1)
    reverse = transformed
    for before, after in reversed(replacements):
        if reverse.count(after) != 1:
            raise ValueError('The source bridge reverse is not unique')
        reverse = reverse.replace(after, before, 1)
    if reverse != source:
        raise ValueError('An undeclared original merger operation changed')
    ast.parse(transformed, filename=str(ORIGINAL))
    namespace = dict(__name__='__main__', __file__=str(Path(__file__).resolve()),
        CHECK_ADDITIONAL_PROVENANCE=check_identity, ORIGINAL_ASSEMBLY_SHA=ORIGINAL_SHA,
        TRANSFORMED_ASSEMBLY_SHA=hashlib.sha256(transformed.encode()).hexdigest())
    exec(compile(transformed, str(ORIGINAL)+'[explicit-provenance-bridge]', 'exec'), namespace)


if __name__ == '__main__':
    main()
