#!/usr/bin/env python3
"""Apply full-tail tangent storage after all retained resource transforms.

This fixes only the composition order of the first storage entry: its guard
import exists after the retained resource builder, not inside the prefix
cache builder.  The complete retained cache/resource/fixed-merit/actual BVP
source is checked and executed with one explicit hook.  The original full
Newton, complete changed-H tail, full Jacobian, positivity, physical boundary,
RMS and audit gates are untouched.  Stored full flows supply guesses only.
All MJS, physical tail parameters and snapshot identities remain unchanged.
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
    'strong_fresh_resource_actual_bvp.py': '26f0c2ba1bdbb413ba7819f8f1aaafa7892787a7e14509357b6a28821e8c808f',
}
OWN = ('strong_full_tangent_actual_bvp_v2.py',
       'strong_full_tangent_tail_client.py', 'strong_full_tangent_tail_worker.mjs',
       'strong_full_flow_tangent_storage.mjs', 'strong_full_tangent_resource_guard.py')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def resource_outer(original):
    """Apply storage to the complete output of the retained resource builder."""
    def installed(original_build, old_heap, semi_space):
        retained = original(original_build, old_heap, semi_space)

        def build(merit, disk):
            source, record = retained(merit, disk)
            edits = [
                ("loaded = original_loader(name+'_exact_stage', HERE/'strong_exact_stage_tail_client.py')",
                 "loaded = original_loader(name+'_full_tangent', HERE/'strong_full_tangent_tail_client.py')"),
                ('from strong_tail_young_space_guard import resource_port_class',
                 'from strong_full_tangent_resource_guard import resource_port_class'),
                ("        'strong_tail_constructor_guard.py')",
                 "        'strong_tail_constructor_guard.py',\n"
                 "        'strong_full_tangent_actual_bvp_v2.py', 'strong_full_tangent_tail_client.py',\n"
                 "        'strong_full_tangent_tail_worker.mjs', 'strong_full_flow_tangent_storage.mjs',\n"
                 "        'strong_full_tangent_resource_guard.py')"),
            ]
            for before, after in edits:
                if source.count(before) != 1:
                    raise ValueError('Final full tangent storage anchor is not unique: '+repr(before))
                source = source.replace(before, after, 1)
            ast.parse(source, filename='<actual-full-flow-storage-after-resources>')
            result = dict(record)
            result['source_sha256'] = {**record['source_sha256'],
                **{str(HERE/name): sha(HERE/name) for name in OWN}}
            result['prior_transformed_source_sha256'] = record['transformed_source_sha256']
            result['transformed_source_sha256'] = hashlib.sha256(source.encode()).hexdigest()
            result['replacements'] = list(record['replacements'])+[
                dict(before=a, after=b, count=1) for a, b in edits]
            result['full_flow_tangent_storage'] = dict(
                scope=__doc__, installed_after_complete_resource_transform=True,
                original_predictor_factory_unchanged=True,
                complete_checkpoint_and_source_binding_required=True,
                binary_values_preserved=True, warm_guess_only=True,
                original_actual_BVP_and_all_final_gates_unchanged=True,
                initial_manifest=os.environ.get('VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST'),
            )
            return source, result

        return build

    return installed


def cached_main_after_resources(production):
    path = HERE/'strong_cached_prefix_actual_bvp.py'
    if sha(path) != EXPECTED[path.name]:
        raise ValueError('The retained complete cache entry changed')
    source = path.read_text()
    before = '    entry=importlib.util.module_from_spec(spec);spec.loader.exec_module(entry)\n'
    after = before+'    entry.resource_build=FULL_TANGENT_RESOURCE_OUTER(entry.resource_build)\n'
    if source.count(before) != 1:
        raise ValueError('The retained cache resource construction hook is not unique')
    source = source.replace(before, after, 1)
    ast.parse(source, filename='<retained-cache-with-final-storage-hook>')
    namespace = dict(__file__=str(path), __name__='strong_full_tangent_cached_entry',
                     FULL_TANGENT_RESOURCE_OUTER=resource_outer)
    exec(compile(source, '<retained-cache-with-final-storage-hook>', 'exec'), namespace)
    # The accepted-field secant may explicitly wrap the original cache builder.
    # Preserve that exact currently active builder rather than bypassing it.
    namespace['build_wrapper'] = production.build_wrapper
    namespace['main']()


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
        path = Path(remaining[remaining.index('--initial-audited-tail-packet')+1])
        data = path.read_bytes()
        packet = json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)
        for name in ('strong_full_tangent_tail_client.py', 'strong_full_tangent_tail_worker.mjs',
                     'strong_full_flow_tangent_storage.mjs'):
            if packet.get('source_sha256', {}).get(name) != sha(HERE/name):
                raise ValueError('An audited shortcut needs this actually audited storage client')
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
    old_main, old_argv = production.main, sys.argv
    production.main = lambda: cached_main_after_resources(production)
    sys.argv = [old_argv[0], *remaining]
    try:
        entry.main()
    finally:
        production.main, sys.argv = old_main, old_argv
        if previous is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = previous


if __name__ == '__main__':
    main()
