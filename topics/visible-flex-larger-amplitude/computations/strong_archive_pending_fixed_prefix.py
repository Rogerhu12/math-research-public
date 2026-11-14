#!/usr/bin/env python3
"""Archive a real fixed-core pending affine-inner result without accepting it.

The unchanged original archiver targets the M+3 continuation layout. This
fresh storage adapter instead requires the exact original fixed-core M-vector
layout. Every complete array/hash/RMS/current-H/prior-tail gate remains. No
RHS, Jacobian, tail worker or BVP is evaluated by this archive operation.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ORIGINAL = 'strong_archive_pending_prefix.py'
ORIGINAL_SHA = '08a0d7be01d9813a7d27822658af29c9ebc462cbd3dd4080a1793e0b07f12b7e'
LAYOUT = 'p0=log(actual_q/gauge_q); p1=(q4-reference_q4)/gauge_q^2; p2..=higher support/recorded scale'


def transformed():
    source = (HERE/ORIGINAL).read_text()
    if hashlib.sha256(source.encode()).hexdigest() != ORIGINAL_SHA:
        raise ValueError('The complete original pending archiver source differs')
    changes = [
        ("    modes, nodes = int(raw['identity']['modes']), len(arrays['x'])\n",
         "    if (not raw['identity']['fixed'] or raw['identity']['parameter_layout'] != FIXED_CORE_LAYOUT):\n"
         "        raise ValueError('Require the exact original fixed-core raw parameter identity')\n"
         "    modes, nodes = int(raw['identity']['modes']), len(arrays['x'])\n"),
        ("arrays['p'].shape != (modes+3,)", "arrays['p'].shape != (modes,)"),
        ("'The complete original augmented field is inconsistent'",
         "'The complete original fixed-core field is inconsistent'"),
        ("    if args.manifest.exists():\n",
         "    result['fixed_core_storage_adapter'] = FIXED_STORAGE_PROVENANCE\n"
         "    if args.manifest.exists():\n"),
    ]
    changed = source
    for before, after in changes:
        if changed.count(before) != 1:
            raise ValueError('Original storage layout anchor is not unique')
        changed = changed.replace(before, after, 1)
    reverse = changed
    for before, after in reversed(changes):
        if reverse.count(after) != 1:
            raise ValueError('Original storage reverse anchor is not unique')
        reverse = reverse.replace(after, before, 1)
    if reverse != source:
        raise ValueError('An undeclared original archive gate changed')
    ast.parse(changed, filename='<original-pending-fixed-core-archive>')
    provenance = dict(scope=__doc__, original_source=ORIGINAL, original_sha256=ORIGINAL_SHA,
        adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        transformed_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        exact_parameter_layout=LAYOUT, original_complete_pending_acceptance_gates_preserved=True,
        transformations=[dict(before=a, after=b, count=1) for a, b in changes],
        reverse_transform_recovers_original_source_exactly=True)
    return changed, provenance


def main():
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument('--prepare-source-record', type=Path)
    own, remaining = p.parse_known_args()
    source, provenance = transformed()
    if own.prepare_source_record:
        with own.prepare_source_record.open('x') as stream:
            json.dump(dict(scope='Source-only preparation; no actual pending field archived.',
                prepared=True, actual_archive_executed=False, provenance=provenance), stream, indent=2)
            stream.write('\n')
        print(json.dumps(dict(prepared=True, actual_archive_executed=False)))
        return
    namespace = dict(__file__=str(Path(__file__).resolve()), __name__='original_fixed_core_pending_archive',
        FIXED_CORE_LAYOUT=LAYOUT, FIXED_STORAGE_PROVENANCE=provenance)
    exec(compile(source, '<original-pending-fixed-core-archive>', 'exec'), namespace)
    old = sys.argv
    sys.argv = [old[0], *remaining]
    try:
        namespace['main']()
    finally:
        sys.argv = old


if __name__ == '__main__':
    main()
