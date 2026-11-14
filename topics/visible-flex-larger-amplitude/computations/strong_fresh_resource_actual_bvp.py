#!/usr/bin/env python3
"""Give every fresh actual live-tail generation the explicit V8 resource guard.

The retained fresh fixed-S/disk-QR entry, complete outer coupling method,
full-H audited packet gates, accepted baseline, equations and final checks
are unchanged.  The resource class wraps the original stage client before
the exact-audited lazy port is formed.  Saved-H dispatch therefore creates
no worker; every changed-H live generation keeps its original complete solve,
full Jacobian/audit, immutable packet and release-before-prefix behavior.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_fresh_physical_merit_actual_bvp.py':
        'b8a898cf5f9dd34e3fe0f9b0ebf2ea12181b93f5a166fb69f7f108c93de47a7d',
    'strong_tail_young_space_guard.py':
        '867244ef03a99ea50f7629d437873c073e9a07ee8a88b48568c79817be7b7eba',
    'strong_tail_constructor_guard.py':
        '6f51a896e44aff8aa8a2f66a71320b68f15d279ec2a8e2ee0e3093cedf0696a3',
}
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def retained_module():
    for name, expected in EXPECTED.items():
        actual = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError('Retained fresh/resource source changed: '+name)
    spec = importlib.util.spec_from_file_location(
        'strong_fresh_retained_resource_entry',
        HERE/'strong_fresh_physical_merit_actual_bvp.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resource_build(original_build, old_heap, semi_space):
    if old_heap <= 0 or semi_space not in (1, 2, 4, 8, 16):
        raise ValueError('Invalid explicit Node resource settings')

    def build(configuration, disk_configuration):
        source, retained = original_build(configuration, disk_configuration)
        edits = [
            ('            stage_base = loaded.WeightedTailPort\n',
             '            from strong_tail_young_space_guard import resource_port_class\n'
             '            stage_base = resource_port_class(loaded.WeightedTailPort, '
             +repr(old_heap)+', '+repr(semi_space)+')\n'),
            ("        'strong_exact_stage_seed.mjs', 'strong_exact_stage_evaluation_check.mjs')",
             "        'strong_exact_stage_seed.mjs', 'strong_exact_stage_evaluation_check.mjs',\n"
             "        'strong_fresh_resource_actual_bvp.py', 'strong_tail_young_space_guard.py',\n"
             "        'strong_tail_constructor_guard.py')"),
        ]
        for before, after in edits:
            if source.count(before) != 1:
                raise ValueError('Fresh live-resource anchor is not unique: '+repr(before))
            source = source.replace(before, after, 1)
        ast.parse(source, filename='<fresh-actual-resource-wrapper>')
        record = dict(retained)
        record['source_sha256'] = dict(retained['source_sha256'])
        record['source_sha256'].update(
            {str(HERE/name): value for name, value in EXPECTED.items()})
        record['source_sha256'][str(Path(__file__).resolve())] = SELF_SHA
        record['prior_transformed_source_sha256'] = retained['transformed_source_sha256']
        record['transformed_source_sha256'] = hashlib.sha256(source.encode()).hexdigest()
        record['replacements'] = list(retained['replacements']) + [
            dict(before=a, after=b, count=1) for a, b in edits]
        record['explicit_live_tail_resource_wrapper'] = dict(
            source_sha256=SELF_SHA, old_heap_MiB=old_heap,
            young_semi_space_MiB=semi_space,
            installed_before_lazy_audited_packet_adapter=True,
            exact_saved_H_creates_no_worker=True,
            every_live_generation_uses_original_complete_tail=True,
            release_worker_and_full_packet_checks_unchanged=True,
            no_numerical_MJS_changes=True,
            cache_key_and_original_math_unchanged=True,
            no_claim_about_prior_signal9_cause=True)
        return source, record

    return build


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--node-young-semi-space', type=int,
        choices=(1, 2, 4, 8, 16), required=True)
    own, remaining = parser.parse_known_args()
    if remaining.count('--node-heap') != 1:
        raise ValueError('Fresh actual continuation needs one explicit old-heap limit')
    old_heap = int(remaining[remaining.index('--node-heap')+1])
    entry = retained_module()
    original_build, old_argv = entry.build_source, sys.argv
    entry.build_source = resource_build(original_build, old_heap, own.node_young_semi_space)
    sys.argv = [old_argv[0], *remaining]
    try:
        entry.main()
    finally:
        entry.build_source = original_build
        sys.argv = old_argv


if __name__ == '__main__':
    main()
