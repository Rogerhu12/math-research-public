#!/usr/bin/env python3
"""Compile and reverse the complete fresh actual resource-only source transform.

This is a standard-library source check, not a numerical solve.  The original
full program is built with its frozen prior transforms, then the two new
changes are reversed literally.  The original young-space and constructor
fixtures separately exercised process dispatch and owned-child cleanup.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh source-check result path')
    started = time.monotonic()
    import strong_fresh_resource_actual_bvp as wrapper
    retained = wrapper.retained_module()
    configuration = dict(stage_cache_directory='source-check-only-no-worker')
    disk = dict(temporary_parent=None, backward_error_tolerance=5e-11,
        heartbeat_seconds=20.)
    old_source, old_record = retained.build_source(configuration, disk)
    source, record = wrapper.resource_build(retained.build_source, 128, 4)(configuration, disk)
    compile(source, '<fresh-resource-complete-program-check>', 'exec')
    additions = record['replacements'][len(old_record['replacements']):]
    reversed_source = source
    for row in reversed(additions):
        if reversed_source.count(row['after']) != 1:
            raise AssertionError('The resource transform cannot be reversed uniquely')
        reversed_source = reversed_source.replace(row['after'], row['before'], 1)
    checks = dict(
        complete_program_compiles=True,
        exactly_two_additive_replacements=len(additions) == 2,
        reverse_transform_restores_complete_prior_source_bytes=(reversed_source == old_source),
        prior_transform_hash_matches=(record['prior_transformed_source_sha256'] ==
            hashlib.sha256(old_source.encode()).hexdigest()),
        current_transform_hash_matches=(record['transformed_source_sha256'] ==
            hashlib.sha256(source.encode()).hexdigest()),
        full_prior_transform_chain_preserved=(record['replacements'][:len(old_record['replacements'])] ==
            old_record['replacements']),
        wrapper_class_created_before_ExplicitStagePort=(source.index(
            'stage_base = resource_port_class(loaded.WeightedTailPort, 128, 4)') <
            source.index('class ExplicitStagePort(stage_base):')),
        original_lazy_port_created_after_ExplicitStagePort=(source.index(
            'loaded.WeightedTailPort = ExplicitStagePort') <
            source.index('loaded.WeightedTailPort = make_port_class(loaded.WeightedTailPort,')),
        per_generation_seed_prefix_preserved=(
            "str(Path(record_prefix).resolve())+'-exact-initial'" in source),
        release_argument_unchanged=(
            'release_between_responses=options.release_tail_worker_between_responses)' in source),
        all_new_source_hashes_recorded=all(str(HERE/name) in record['source_sha256'] for name in (
            'strong_fresh_resource_actual_bvp.py', 'strong_tail_young_space_guard.py',
            'strong_tail_constructor_guard.py')),
    )
    # Parsing the entire result above also checks that the additions remain in
    # the intended actual loader closure rather than in a dead top-level block.
    tree = ast.parse(source)
    main_function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    loader = next(n for n in main_function.body if isinstance(n, ast.FunctionDef) and n.name == 'load')
    loader_text = ast.unparse(loader)
    checks['resource_call_is_in_actual_nested_loader'] = (
        'resource_port_class(loaded.WeightedTailPort, 128, 4)' in loader_text)
    report = dict(scope=__doc__, passed=all(checks.values()), checks=checks,
        physical_Flow_instances=0, physical_RHS_calls=0, tail_workers=0, BVPs=0,
        numerical_surface_result=False, source_sha256_at_start={
            str(Path(__file__).resolve()): SELF_SHA,
            str(HERE/'strong_fresh_resource_actual_bvp.py'): wrapper.SELF_SHA,
            **{str(HERE/name): sha for name, sha in wrapper.EXPECTED.items()}},
        source_transform=record, seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(passed=report['passed'], checks=checks,
        seconds=report['seconds'], physical_Flow_instances=0, tail_workers=0)), flush=True)
    if not report['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
