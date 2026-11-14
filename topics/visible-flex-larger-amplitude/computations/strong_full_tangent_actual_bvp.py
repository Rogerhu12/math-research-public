#!/usr/bin/env python3
"""Use exact persisted full-state tail tangents only for continuation guesses.

This wrapper changes the retained exact-stage worker to its fresh binary-flow
storage extension. The original actual BVP, fixed physical merit, disk QR,
complete H solve, positivity, Jacobian, RMS, boundary and audit gates remain.
An explicit initial tangent manifest is checked against the complete original
checkpoint. It never supplies a nonlinear response or changes a boundary.
"""
from __future__ import annotations

import argparse
import ast
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_cached_prefix_actual_bvp.py': '986de6d32371144d20dc5a511dd027875e0b43aa976201447e75a7151e940faa',
    'strong_secant_actual_bvp_v2.py': '99817229111f91bbec5b27a241a5eb20ff6cad6bb4eca58d7ebd85fcd3dc2a30',
}
OWN = (
    'strong_full_tangent_actual_bvp.py', 'strong_full_tangent_tail_client.py',
    'strong_full_tangent_tail_worker.mjs', 'strong_full_flow_tangent_storage.mjs',
    'strong_full_tangent_resource_guard.py',
)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def storage_build(original):
    def outer(original_build, configuration):
        retained_build = original(original_build, configuration)

        def build(merit, disk):
            source, record = retained_build(merit, disk)
            edits = [
                ("loaded = original_loader(name+'_exact_stage', HERE/'strong_exact_stage_tail_client.py')",
                 "loaded = original_loader(name+'_full_tangent', HERE/'strong_full_tangent_tail_client.py')"),
                ('from strong_tail_young_space_guard import resource_port_class',
                 'from strong_full_tangent_resource_guard import resource_port_class'),
                ("        'strong_tail_constructor_guard.py')",
                 "        'strong_tail_constructor_guard.py',\n"
                 "        'strong_full_tangent_actual_bvp.py', 'strong_full_tangent_tail_client.py',\n"
                 "        'strong_full_tangent_tail_worker.mjs', 'strong_full_flow_tangent_storage.mjs',\n"
                 "        'strong_full_tangent_resource_guard.py')"),
            ]
            for before, after in edits:
                if source.count(before) != 1:
                    raise ValueError('Full tangent BVP storage anchor is not unique: '+repr(before))
                source = source.replace(before, after, 1)
            ast.parse(source, filename='<actual-full-flow-tangent-storage>')
            result = dict(record)
            result['source_sha256'] = {**record['source_sha256'],
                **{str(HERE/name): sha(HERE/name) for name in OWN}}
            result['prior_transformed_source_sha256'] = record['transformed_source_sha256']
            result['transformed_source_sha256'] = hashlib.sha256(source.encode()).hexdigest()
            result['replacements'] = list(record['replacements'])+[
                dict(before=a, after=b, count=1) for a, b in edits]
            result['full_flow_tangent_storage'] = dict(
                scope=__doc__, original_predictor_factory_unchanged=True,
                complete_checkpoint_and_source_binding_required=True,
                binary_values_preserved=True, warm_guess_only=True,
                original_actual_BVP_and_all_final_gates_unchanged=True,
                initial_manifest=os.environ.get('VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST'),
            )
            return source, result

        return build

    return outer


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--continuation-entry', choices=('control-response', 'secant-v2'),
                        default='control-response')
    parser.add_argument('--initial-full-tangent-manifest', type=Path)
    own, remaining = parser.parse_known_args()
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Retained continuation source differs: '+name)
    if '--initial-audited-tail-packet' in remaining:
        packet = Path(remaining[remaining.index('--initial-audited-tail-packet')+1])
        data = packet.read_bytes()
        saved = json.loads(gzip.decompress(data) if packet.suffix == '.gz' else data)
        sources = saved.get('source_sha256', {})
        for name in ('strong_full_tangent_tail_client.py', 'strong_full_tangent_tail_worker.mjs',
                     'strong_full_flow_tangent_storage.mjs'):
            if sources.get(name) != sha(HERE/name):
                raise ValueError('An audited shortcut needs an actually audited packet from this storage client')
    manifest = own.initial_full_tangent_manifest
    if manifest is not None and not manifest.is_file():
        raise ValueError('The explicit initial full tangent manifest is missing')
    import strong_cached_prefix_actual_bvp as production
    entry = production
    if own.continuation_entry == 'secant-v2':
        import strong_secant_actual_bvp_v2 as entry
    key = 'VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST'
    previous = os.environ.get(key)
    if manifest is None:
        os.environ.pop(key, None)
    else:
        os.environ[key] = str(manifest.resolve())
    old_build, old_argv = production.build_wrapper, sys.argv
    production.build_wrapper = storage_build(old_build)
    sys.argv = [old_argv[0], *remaining]
    try:
        entry.main()
    finally:
        production.build_wrapper, sys.argv = old_build, old_argv
        if previous is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = previous


if __name__ == '__main__':
    main()
