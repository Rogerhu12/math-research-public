#!/usr/bin/env python3
"""Complete closed-image distance from a fixed phase witness, using R656/R658.

This position-only calculation proves a Hausdorff lower component. It does not
assert embedding, reach, an isometry or a positive Euclidean quotient distance.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def cover_cell(reader, radius, cell):
    I = reader.I
    pieces = reader._cell_pieces(cell)
    best, where = float('inf'), None
    for part, piece in enumerate(pieces):
        controls = radius.position_controls(reader, cell, piece)
        divided = [reader.radial_parts(c) for c in controls]
        for sub in range(reader.subdivisions):
            X = [(c[sub][0].min(axis=0), c[sub][1].max(axis=0)) for c in divided]
            for sign in (-1, 1):
                distance2 = reader.norm2([
                    I.sub(X[k], I.scale(reader.witness_rotating[k], sign))
                    for k in range(3)])[0]
                angle = int(np.argmin(distance2))
                if float(distance2[angle]) < best:
                    best = max(0., float(distance2[angle]))
                    where = dict(piece=part, radial_subcell=sub,
                        angle_grid_index=angle, witness_sign=sign)
    return dict(cell=cell, exact_pieces=len(pieces),
        witness_distance_squared_lower=best, worst_box=where,
        complete_continuous_position_cover=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('bundle', 'node-report', 'interval-source', 'geometry-source',
                 'radius-source', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--radial-subdivisions', type=int, default=1)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Keep earlier covers and select a fresh output')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic()
    geometry = load(a.geometry_source, 'complete_witness_geometry_kernel')
    radius = load(a.radius_source, 'complete_witness_position_kernel')
    reader = geometry.Reader(a.bundle, a.node_report, a.interval_source,
        angles=a.angles, radial_subdivisions=a.radial_subdivisions,
        beta='1/4', witness=True)
    records = []
    caps = reader.cap_bounds()
    report = dict(schema='fullclosed-complete-witness-distance-outward-v1',
        source_sha256=sha(__file__), radius_source_sha256=sha(a.radius_source),
        geometry_source_sha256=sha(a.geometry_source), metadata=reader.metadata(),
        cap_bounds=caps, records=records, full_body_witness_certified=False,
        embedding_certified=False, reach_certified=False, metric_certified=False)
    for cell in range(reader.J-1):
        records.append(cover_cell(reader, radius, cell))
        if len(records) % 64 == 0:
            report['seconds'] = time.monotonic()-started
            a.out.write_text(json.dumps(report, indent=2)+'\n')
            print(json.dumps(dict(event='witness_cover_progress',
                completed=len(records), total=reader.J-1,
                minimum_distance_squared_lower=min(r['witness_distance_squared_lower'] for r in records),
                seconds=report['seconds'])), flush=True)
    if [r['cell'] for r in records] != list(range(reader.J-1)):
        raise ValueError('Incomplete original radial coverage')
    squared = min(caps['witness_distance_squared_lower'],
        *(r['witness_distance_squared_lower'] for r in records))
    distance = float(reader.I.sqrt(reader.I.exact(squared))[0])
    report.update(full_body_witness_certified=True,
        witness_distance_squared_lower=squared, witness_distance_lower=distance,
        bottom_cells=sorted(records,key=lambda r:r['witness_distance_squared_lower'])[:10],
        covered_original_cells=len(records), seconds=time.monotonic()-started,
        proof='R656 exact phase witness +/- orbit and R658 position cover on every cell; both flat caps and horizontal mirror')
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('records','metadata')}),flush=True)
    print(json.dumps(dict(event='witness_cover_complete',report_sha256=sha(a.out))),flush=True)


if __name__ == '__main__':
    main()
