#!/usr/bin/env python3
"""Overlay complete selected spans of a finer packet onto a full coarse one.

Only exact zero padding and row selection are performed. The original
analytic claims remain separate dependencies; this is an interface helper.
"""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(path):
    meta = json.loads(path.read_text())
    if meta.get('finished') is not True:
        raise ValueError('An unfinished packet cannot be overlaid')
    p = path.parent/meta['data_file']
    if sha(p) != meta['data_sha256']:
        raise ValueError('Data hash mismatch')
    content = p.read_bytes()
    if content[:2] == b'\x1f\x8b':
        content = gzip.decompress(content)
    return meta, np.load(io.BytesIO(content), allow_pickle=False)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('coarse', type=Path)
    ap.add_argument('fine', type=Path)
    ap.add_argument('out', type=Path)
    args = ap.parse_args()
    cm, c = read(args.coarse)
    fm, f = read(args.fine)
    if cm['finite_tail_manifest_sha256'] != fm['finite_tail_manifest_sha256']:
        raise ValueError('Different finite maps')
    for key in ('checkpoint', 'calibrations', 'cell_zero_A', 'inner_A', 'outer_B'):
        if cm['background_definition_hashes'][key]['sha256'] != fm['background_definition_hashes'][key]['sha256']:
            raise ValueError('Different exact background definitions')
    selected = set(map(int, f['span_index']))
    for span in selected:
        j = np.flatnonzero(f['span_index'] == span)
        if (f['u_left'][j[0]] != 0 or f['u_right'][j[-1]] != 1
            or not np.array_equal(f['u_right'][j[:-1]], f['u_left'][j[1:]])
            or not np.all(f['u_left'][j] < f['u_right'][j])):
            raise ValueError('Fine packet does not cover the selected span')
    keep = np.array([int(v) not in selected for v in c['span_index']])
    raw = {}
    names = ['span_index', 'u_left', 'u_right', 'w_lo', 'w_hi', 'w_remainder',
             'wr_lo', 'wr_hi', 'wr_remainder']
    for key in names:
        a, b = c[key][keep], f[key]
        if a.ndim == 2:
            width = max(a.shape[1], b.shape[1])
            a = np.pad(a, ((0, 0), (0, width-a.shape[1])))
            b = np.pad(b, ((0, 0), (0, width-b.shape[1])))
        raw[key] = np.concatenate([a, b])
    order = np.lexsort((raw['u_left'], raw['span_index']))
    raw = {key: value[order] for key, value in raw.items()}
    payload = io.BytesIO()
    np.savez_compressed(payload, **raw)
    content = payload.getvalue()
    if len(content) >= 5_000_000:
        raise ValueError('Overlay data exceed the file-size limit')
    path = args.out.with_suffix('.npz')
    path.write_bytes(content)
    result = dict(status='exact-row-overlay-analytic-suppliers-remain-dependencies', finished=True,
        finite_tail_manifest_sha256=cm['finite_tail_manifest_sha256'],
        data_file=path.name, data_sha256=sha(path),
        background_definition_hashes=fm['background_definition_hashes'],
        sources={str(p): sha(p) for p in (args.coarse, args.fine)},
        script_sha256=sha(__file__), overlaid_spans=sorted(selected),
        analytic_definition='Same exact background; use fine packet on the listed complete spans and coarse packet elsewhere.')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(rows=len(order), fine_span_count=len(selected),
                          fine_span_range=[min(selected), max(selected)+1], bytes=len(content))))


if __name__ == '__main__':
    main()
