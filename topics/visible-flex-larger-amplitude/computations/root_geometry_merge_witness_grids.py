#!/usr/bin/env python3
"""Merge saved finite witness coordinates without relabelling their identities.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This only prepares a comparison grid. It samples no field and proves no bound.
"""
import argparse
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, nargs='+', required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh witness union')
    inputs = [json.loads(x.read_text()) for x in a.input]
    angular = inputs[0]['angular']
    if any(d['angular'] != angular for d in inputs):
        raise ValueError('An exact common angular grid is required')
    witnesses = []
    ts = []
    for path, d in zip(a.input, inputs):
        for w in d.get('known_reference_witnesses', []):
            t = d['numerical_t'][w['radial_index']]
            if not 0 <= t <= 1 or not 0 <= w['angular_index'] < angular:
                raise ValueError('Saved witness is outside its original grid')
            ts.append(t)
            witnesses.append(dict(w, numerical_t=t,
                                  witness_original_grid=str(path),
                                  witness_original_grid_sha256=sha(path)))
    ts = sorted(set(ts))
    for w in witnesses:
        w['radial_index'] = ts.index(w['numerical_t'])
    out = dict(scope=__doc__, angular=angular, numerical_t=ts,
               known_reference_witnesses=witnesses,
               only_coordinate_union=True, new_field_evaluation=False,
               original_witness_identity_and_values_retained=True,
               source_sha256=sha(__file__),
               input_sha256={str(x): sha(x) for x in a.input})
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'path': str(a.out), 'sha256': sha(a.out),
                      'witnesses': len(witnesses), 'radial_points': len(ts)}))


if __name__ == '__main__':
    main()
