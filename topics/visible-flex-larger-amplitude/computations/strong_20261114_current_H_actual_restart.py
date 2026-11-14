#!/usr/bin/env python3
"""Restart an unaccepted actual iterate with its genuinely audited current H.

The original actual entry already has a strict complete x/y/p/cubic reader.
Its fresh-merit front end deliberately rejects pending affine-inner restarts.
This separately named entry admits the different, explicit operation here:
restore that raw field and start the original outer coupling at a newly solved
and audited complete current H. It does not preserve the previous affine
anchor or claim to reproduce its Newton trajectory. The candidate, fixed
positive physical merit, original strict raw reader, all tail identity checks,
complete nonlinear/J/audit requests and final prefix gates remain unchanged.

Author: strong_amplitude (GPT-6 Astra Pro; AI-assisted), 2026-11-14.
"""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path
import numpy as np

import strong_20261114_loop_actual_bvp as loop
import strong_fresh_resource_actual_bvp as resource
from strong_20261114_audit_iterate_H import complete_height
from strong_20261114_audit_complete_tail_packet import equations, read, sha


HERE = Path(__file__).resolve().parent


def prepare_current_H(original, argv):
    """Keep the original merit definition; bind the restored field to new H."""
    def argument(name):
        if argv.count(name) != 1:
            raise ValueError('Require one explicit current-H restart argument: ' + name)
        index = argv.index(name)
        if index + 1 >= len(argv):
            raise ValueError('Missing current-H restart argument value: ' + name)
        return Path(argv[index + 1]).resolve()

    if any(name in argv for name in ('--resume-original-affine-anchor',
                                     '--original-inner-entry-raw',
                                     '--original-inner-entry-tail-config')):
        raise ValueError('This entry starts at actual current H, not a saved affine anchor')
    paths = {name: argument(name) for name in (
        '--resume-actual-iterate', '--resume-tail-config',
        '--initial-audited-tail-packet', '--initial-audited-tail-ready',
        '--actual-reference')}
    filtered = list(argv)
    for name in ('--resume-actual-iterate', '--resume-tail-config'):
        index = filtered.index(name)
        del filtered[index:index + 2]
    configuration = original(filtered)
    H, raw, binding = complete_height(paths['--resume-actual-iterate'],
                                     paths['--resume-tail-config'])
    context = raw['identity']['coupling_context']
    if (context['actual_targets'] != configuration['target_actual_core']
            or context['baseline_sha256'] != sha(paths['--actual-reference'])
            or raw['identity']['modes'] != configuration['modes']
            or raw['identity']['gauge'] != configuration['gauge']):
        raise ValueError('Restored actual target, accepted baseline, M or gauge differs')
    packet_path = paths['--initial-audited-tail-packet']
    packet = read(packet_path)
    request, response = packet['request'], packet['response']
    M = len(H)
    if (not request.get('jacobian') or not request.get('audit')
            or not response.get('converged') or response.get('audit') is None
            or response['residual'] > packet['config']['solveTolerance']
            or len(response['heightJetJacobian']) != (3*M + 2)*M
            or not np.array_equal(np.asarray(request['height']), H)
            or not np.array_equal(np.asarray(response['checkpoint']['cutHeight']), H)):
        raise ValueError('The actual current complete H has no matching full solve/J/audit packet')
    if equations(packet['config']) != equations(read(paths['--resume-tail-config'])):
        raise ValueError('The audited current-H tail physical or numerical equations differ')
    if '--tail-warm-checkpoint' in argv:
        warm = argument('--tail-warm-checkpoint')
        if sha(warm) != sha(packet_path):
            raise ValueError('Use this exact current-H response as the explicit first warm state')
    configuration.update(
        mode='restored-current-H-fixed-physical-core-coordinate-merit-v1',
        scope=__doc__,
        current_H_restart=dict(
            raw=binding,
            files={name: dict(file=str(path), sha256=sha(path))
                   for name, path in paths.items()},
            complete_current_H=H.tolist(),
            actual_current_H_residual=response['residual'],
            strict_original_complete_raw_reader_still_required=True,
            strict_original_packet_ready_source_identity_checks_still_required=True,
            original_affine_anchor_not_restored=True,
            fresh_outer_anchor_at_genuinely_solved_current_H=True,
            original_outer_method_and_all_final_acceptance_gates_unchanged=True,
            raw_iterate_and_prefix_still_unaccepted=True))
    return configuration


def main():
    original_retained = resource.retained_module

    def retained():
        fresh = original_retained()
        original_prepare, original_build = fresh.prepare_configuration, fresh.build_source
        fresh.prepare_configuration = lambda argv: prepare_current_H(original_prepare, argv)

        def build(configuration, disk_configuration):
            source, provenance = original_build(configuration, disk_configuration)
            anchor = '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'
            if source.count(anchor) != 1:
                raise ValueError('The actual source identity insertion point changed')
            own = ('strong_20261114_current_H_actual_restart.py',
                   'strong_20261114_audit_iterate_H.py',
                   'strong_20261114_audit_complete_tail_packet.py')
            changed = source.replace(anchor, '    source_names += ' + repr(own) + '\n' + anchor, 1)
            ast.parse(changed)
            record = dict(provenance)
            record['source_sha256'] = {
                **provenance['source_sha256'],
                **{str(HERE/name): sha(HERE/name) for name in own}}
            record['prior_transformed_source_sha256'] = provenance['transformed_source_sha256']
            record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
            record['current_H_restart'] = configuration['current_H_restart']
            record['pending_affine_inner_trajectory_reproduced'] = False
            record['all_original_raw_restore_and_current_H_gates_retained'] = True
            return changed, record

        fresh.build_source = build
        return fresh

    resource.retained_module = retained
    try:
        loop.main()
    finally:
        resource.retained_module = original_retained


if __name__ == '__main__':
    main()
