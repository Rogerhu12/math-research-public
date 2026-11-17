#!/usr/bin/env python3
"""Collect an exact finite-state n4 engine allocation comparison without arrays."""
import argparse
import json
from pathlib import Path
import shlex
from record_fixed_actual import sha, scalar_tree, load


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('comparison', 'manifest', 'resource', 'tail', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    check, manifest, resource = (load(getattr(args, name))
                                 for name in ('comparison', 'manifest', 'resource'))
    tail = load(args.tail)
    assert check['input_sha256'] == sha(args.tail)
    assert tail['response']['converged']
    assert not any(check['differences'].values())
    assert check['originalBitHash'] == check['sharedBitHash']
    assert not any(value for key, value in check['mutableScratch'].items()
                   if key not in ('sameEngineStage', 'differentEngineStage'))
    assert manifest['canonical_unchanged'] and manifest['sparse_global_solve_unchanged']
    result = dict(
        scope='Independent complete n4 actual-M20 same-state comparison of original and same-mu cached periodic engines. Allocation only; no new tail solve, numerical gate change, or universal equivalence/speed theorem is asserted.',
        collector_sha256=sha(__file__), comparison=check,
        installation=manifest, resource=scalar_tree(resource),
        resource_semantics='The reported RUSAGE_CHILDREN maxrss is not a whole-tree peak or a memory-reduction measurement. Both engines coexist during this comparison.',
        physical_and_discrete_tail_parameters=scalar_tree(tail['response']['checkpoint']['parameters']),
        actual_command=shlex.join(resource['command']),
        file_hashes={name: sha(getattr(args, name))
                     for name in ('comparison', 'manifest', 'resource', 'tail')},
        data_policy='Source, physical/discrete parameters, finite scalar audit and hashes only; all stage states and Jacobian arrays remain scratch-only.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out))))


if __name__ == '__main__':
    main()
