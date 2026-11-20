#!/usr/bin/env python3
"""Complete-body position-only continuous enclosure using the R656 kernel.

All original radial cells and all angles are covered. Omits curvature and
metric work, preserving the exact same q/analytic lift and outward model.
A radius enclosure alone does not prove embedding, reach or isometry.
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


def load(path):
    spec = importlib.util.spec_from_file_location('fullclosed_radius_geometry_kernel', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def position_controls(reader, cell, piece):
    I = reader.I
    left, right, u0, u1, active = piece
    h = reader.width_box(reader.nodes[cell], reader.nodes[cell+1])
    if float(h[0]) <= 0:
        raise ValueError('Exact original cell width must be positive')
    b = reader.hermite(I.at(reader.jets, cell), I.at(reader.jets, cell+1), h)
    b = reader.elevate(reader.restrict(b, u0, u1))
    X = [reader.angle_boxes(c, parity) for c,parity in reader.channels(b, 0)]
    lift = reader.lift_controls(left, right, active)
    f = lift['f'][0][:,None], lift['f'][1][:,None]
    chi = lift['chi'][0][:,None], lift['chi'][1][:,None]
    X = [I.add(X[k], I.mul(f, reader.er[k])) for k in range(3)]
    X[2] = I.add(X[2], I.mul(chi, reader.Hbox))
    return X


def cover_cell(reader, cell):
    pieces = reader._cell_pieces(cell)
    best, where = 0., None
    for part,piece in enumerate(pieces):
        controls = position_controls(reader, cell, piece)
        divided = [reader.radial_parts(c) for c in controls]
        for sub in range(reader.subdivisions):
            X = [(c[sub][0].min(axis=0), c[sub][1].max(axis=0)) for c in divided]
            bound = reader.norm2(X)[1]
            angle = int(np.argmax(bound))
            if float(bound[angle]) > best:
                best = float(bound[angle])
                where = dict(piece=part, radial_subcell=sub, angle_grid_index=angle)
    return dict(cell=cell, exact_pieces=len(pieces), radius_squared_upper=best,
        worst_box=where, complete_continuous_position_cover=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('bundle','node-report','interval-source','geometry-source','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--radial-subdivisions',type=int,default=1)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Keep preceding covers and choose a fresh output')
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
    started = time.monotonic()
    module = load(a.geometry_source)
    reader = module.Reader(a.bundle,a.node_report,a.interval_source,
        angles=a.angles,radial_subdivisions=a.radial_subdivisions,beta='1/4',witness=False)
    records=[]
    caps=reader.cap_bounds()
    report=dict(schema='fullclosed-complete-radius-outward-v1',source_sha256=sha(__file__),
        geometry_source_sha256=sha(a.geometry_source),metadata=reader.metadata(),
        cap_bounds=caps,records=records,full_body_radius_certified=False,
        embedding_certified=False,reach_certified=False,metric_certified=False)
    for cell in range(reader.J-1):
        records.append(cover_cell(reader,cell))
        if len(records)%64==0:
            report['seconds']=time.monotonic()-started
            a.out.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(dict(event='radius_cover_progress',completed=len(records),
                total=reader.J-1,maximum_radius_squared_upper=max(r['radius_squared_upper'] for r in records),
                seconds=report['seconds'])),flush=True)
    if [r['cell'] for r in records] != list(range(reader.J-1)):
        raise ValueError('Incomplete original radial coverage')
    squared=max(caps['maximum_radius_squared_upper'],*(r['radius_squared_upper'] for r in records))
    diameter=float(reader.I.scale(reader.I.sqrt(reader.I.exact(squared)),2.)[1])
    top=sorted(records,key=lambda r:r['radius_squared_upper'],reverse=True)[:10]
    report.update(full_body_radius_certified=True,maximum_radius_squared_upper=squared,
        diameter_upper=diameter,top_cells=top,covered_original_cells=len(records),
        seconds=time.monotonic()-started,proof='R656 position Bernstein/angle cover on every original cell; both flat disks and horizontal mirror; D<=2 sup|F|')
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('records','metadata')}),flush=True)
    print(json.dumps(dict(event='radius_cover_complete',report_sha256=sha(a.out))),flush=True)


if __name__=='__main__':
    main()
