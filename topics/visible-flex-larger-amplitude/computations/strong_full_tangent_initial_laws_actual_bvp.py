#!/usr/bin/env python3
"""Compose the explicit initial-law actual BVP with saved full-flow guesses.

The frozen initial-law provider is installed by its existing production entry.
Only after its complete cache/resource transform do we install the previously
verified full-flow storage adapter. All current-H nonlinear tail solves, full
Jacobians, physical boundary checks, original RMS, and final audits remain.
Saved tangent flows are initial guesses only. No MJS source is changed.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED = {
    'strong_initial_laws_actual_bvp.py':
        '55af2c6b3f2fb91631481ed0078d89b608fe37eb439b46eb7b17f999fc65d9cc',
    'strong_full_tangent_actual_bvp_v2.py':
        '44a0c4c06a6171ddb2219b58bbdbfb8336aacf3454f674bdfdba874b9bdf81d5',
    'strong_fresh_resource_actual_bvp.py':
        '26f0c2ba1bdbb413ba7819f8f1aaafa7892787a7e14509357b6a28821e8c808f',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resource_outer(original):
    import strong_full_tangent_actual_bvp_v2 as storage
    with_storage = storage.resource_outer(original)

    def installed(original_build, old_heap, semi_space):
        retained = with_storage(original_build, old_heap, semi_space)

        def build(merit, disk):
            source, prior = retained(merit, disk)
            before = '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'
            after = ("    source_names += ('strong_full_tangent_initial_laws_actual_bvp.py',)\n"
                     + before)
            if source.count(before) != 1:
                raise ValueError('Initial-law full-flow source identity anchor differs')
            changed = source.replace(before, after, 1)
            ast.parse(changed, filename='<initial-laws-complete-full-flow-production>')
            if changed.count(after) != 1 or changed.replace(after, before, 1) != source:
                raise ValueError('The final identity hook altered other production code')
            record = dict(prior)
            record['source_sha256'] = {**prior['source_sha256'],
                str(Path(__file__).resolve()): sha(__file__)}
            record['prior_transformed_source_sha256'] = prior['transformed_source_sha256']
            record['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
            record['replacements'] = list(prior['replacements']) + [
                dict(before=before, after=after, count=1)]
            record['initial_laws_full_flow_composition'] = dict(
                scope=__doc__, installed_after_initial_laws_cache_and_resource=True,
                initial_speed_frontload_provider_unchanged=True,
                zero_law_delegates_original_provider=True,
                all_saved_nonzero_laws_require_explicit_provider=True,
                original_actual_equations_and_acceptance_gates_unchanged=True,
                all_MJS_unchanged=True, storage_is_warm_only=True,
                exact_reverse_recovers_prior_complete_production=True)
            return changed, record

        return build

    return installed


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--initial-full-tangent-manifest', type=Path)
    own, remaining = parser.parse_known_args()
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen initial-law/storage production entry differs: '+name)
    if '--initial-audited-tail-packet' in remaining:
        import gzip
        import json
        path = Path(remaining[remaining.index('--initial-audited-tail-packet')+1])
        data = path.read_bytes()
        packet = json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)
        for name in ('strong_full_tangent_tail_client.py',
                     'strong_full_tangent_tail_worker.mjs',
                     'strong_full_flow_tangent_storage.mjs'):
            if packet.get('source_sha256', {}).get(name) != sha(HERE/name):
                raise ValueError('Audited reuse requires this actually audited storage client')
    manifest = own.initial_full_tangent_manifest
    if manifest is not None and not manifest.is_file():
        raise ValueError('The explicit initial full-flow manifest is missing')
    import strong_initial_laws_actual_bvp as entry
    import strong_fresh_resource_actual_bvp as resource
    key = 'VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST'
    previous = os.environ.get(key)
    if manifest is None:
        os.environ.pop(key, None)
    else:
        os.environ[key] = str(manifest.resolve())
    original, old_argv = resource.resource_build, sys.argv
    resource.resource_build = resource_outer(original)
    sys.argv = [old_argv[0], *remaining]
    try:
        entry.main()
    finally:
        resource.resource_build, sys.argv = original, old_argv
        if previous is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = previous


if __name__ == '__main__':
    main()
