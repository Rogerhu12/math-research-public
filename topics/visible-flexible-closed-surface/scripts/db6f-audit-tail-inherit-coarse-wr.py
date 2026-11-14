#!/usr/bin/env python3
"""Keep fine w packets and inherit proved constant w_r boxes on selected spans.

This changes only an enclosure, never the background or the finite map.
Every selected fine interval is a subset of its same-span coarse interval.
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


def read(p):
    meta = json.loads(p.read_text())
    if meta.get('finished') is not True:
        raise ValueError('Unfinished input packet')
    path = p.parent/meta['data_file']
    if sha(path) != meta['data_sha256']:
        raise ValueError('Input data hash mismatch')
    raw = path.read_bytes()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    with np.load(io.BytesIO(raw), allow_pickle=False) as data:
        return meta, {k: np.array(data[k], copy=True) for k in data.files}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('fine', type=Path)
    ap.add_argument('coarse', type=Path)
    ap.add_argument('out', type=Path)
    ap.add_argument('--minimum-span', type=int, required=True)
    args = ap.parse_args()
    fm, f = read(args.fine)
    cm, c = read(args.coarse)
    if fm['finite_tail_manifest_sha256'] != cm['finite_tail_manifest_sha256']:
        raise ValueError('Different finite maps')
    for k in ('checkpoint', 'calibrations', 'cell_zero_A', 'inner_A', 'outer_B'):
        if fm['background_definition_hashes'][k]['sha256'] != cm['background_definition_hashes'][k]['sha256']:
            raise ValueError('Different exact backgrounds')
    if not (np.all(c['u_left'] == 0) and np.all(c['u_right'] == 1)):
        raise ValueError('The coarse input must have complete original spans')
    if not (np.all(c['wr_lo'][:, 1:] == 0) and np.all(c['wr_hi'][:, 1:] == 0)):
        raise ValueError('Only constant coarse derivative boxes may be inherited')
    indices = {int(v): j for j, v in enumerate(c['span_index'])}
    if len(indices) != len(c['span_index']):
        raise ValueError('Repeated coarse span')
    selected = np.flatnonzero(f['span_index'] >= args.minimum_span)
    if not len(selected):
        raise ValueError('No selected fine rows')
    for j in selected:
        if not 0 <= f['u_left'][j] < f['u_right'][j] <= 1:
            raise ValueError('A fine row is not a subset of the whole original span')
        k = indices[int(f['span_index'][j])]
        f['wr_lo'][j] = 0
        f['wr_hi'][j] = 0
        f['wr_lo'][j, 0] = c['wr_lo'][k, 0]
        f['wr_hi'][j, 0] = c['wr_hi'][k, 0]
        f['wr_remainder'][j] = c['wr_remainder'][k]
    buf = io.BytesIO()
    np.savez_compressed(buf, **f)
    payload = buf.getvalue()
    if len(payload) >= 5_000_000:
        raise ValueError('Combined packet exceeds the per-file size limit')
    path = args.out.with_suffix('.npz')
    path.write_bytes(payload)
    result = dict(fm)
    result.update(status='fine-background-values-with-inherited-proved-derivative-boxes',
        data_file=path.name, data_sha256=sha(path),
        derivative_box_inheritance=dict(
            fine_packet=str(args.fine), fine_packet_sha256=sha(args.fine),
            coarse_packet=str(args.coarse), coarse_packet_sha256=sha(args.coarse),
            coarse_data_sha256=cm['data_sha256'], minimum_span=args.minimum_span,
            affected_rows=len(selected), script_sha256=sha(__file__),
            justification='The constant coarse wr enclosure is valid on the entire same original span; each fine row is a subset. All w arrays and all physical coordinates are unchanged.'))
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(rows=len(f['span_index']), inherited_rows=len(selected), bytes=len(payload))))


if __name__ == '__main__':
    main()
