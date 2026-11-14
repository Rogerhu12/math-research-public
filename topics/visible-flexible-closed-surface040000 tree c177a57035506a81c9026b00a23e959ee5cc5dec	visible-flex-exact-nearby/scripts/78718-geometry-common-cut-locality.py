#!/usr/bin/env python3
"""Certify one common-cut map using its exact lower-mode prefix locality.

The common-cut definition changes no coefficient on spans before its saved
correction_start_index.  Certify those spans on the defining base map and
the remaining spans on the common-cut map, then take extrema.  No old map
certificate is reused and no tail, cap, metric, or reach claim is added.
"""
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def run(args):
    started = time.monotonic()
    meta = json.loads(args.geometry.read_text())
    if meta.get('representation') != 'exact-common-cut-prefix':
        raise ValueError('Expected the exact common-cut representation')
    common = load('geometry_locality_common', HERE/'78718-prefix-common-cut-storage-v1.py')
    if meta['common_cut_implementation_sha256'] != sha(common.__file__):
        raise ValueError('Common-cut map is defined by a different implementation')
    base_path = common.resolve(args.geometry, meta['base_geometry'])
    if sha(base_path) != meta['base_geometry_sha256']:
        raise ValueError('Defining base map changed')
    start = int(meta['correction_start_index'])
    base_meta = json.loads(base_path.read_text())
    base_out = args.out.with_name(args.out.stem+'-base-part.json')
    cut_out = args.out.with_name(args.out.stem+'-cut-part.json')
    ordinary = load('geometry_locality_base', HERE/'78718-prefix-continuous-hermite-storage-v1.py')
    shared = dict(angular=args.angular, radial=args.radial, batch=args.batch,
                  ell=args.ell, witness=args.witness)
    # The old certifier writes each full report.  Keep its verbose stdout out
    # of the caller's numerical transcript; only a small summary is printed.
    with contextlib.redirect_stdout(io.StringIO()):
        ordinary.certify(SimpleNamespace(geometry=base_path, out=base_out,
                                        start=0, stop=start, **shared))
        # Preserve the same exact rational trigonometry cache.  The base
        # certificate is already complete before replacing the constructor.
        common.install(ordinary)
        ordinary.certify(SimpleNamespace(geometry=args.geometry, out=cut_out,
                                        start=start, stop=None, **shared))
    left, right = (json.loads(p.read_text()) for p in (base_out, cut_out))
    total = right['total_spans']
    if not (0 < start < total and left['total_spans'] == total
            and left['first_span'] == 0 and left['last_span_exclusive'] == start
            and right['first_span'] == start and right['last_span_exclusive'] == total
            and left['ell_as_binary64'] == right['ell_as_binary64']
            and left['inlet_exact'] == right['inlet_exact']):
        raise ValueError('The two actual certified pieces do not cover the defining map')
    out = dict(right)
    out.update(scope=__doc__, geometry=str(args.geometry),
               geometry_sha256=sha(args.geometry), script_sha256=sha(__file__),
               first_span=0, last_span_exclusive=total,
               entire_finite_prefix_covered=True, continuous_bounds_certified=True,
               locality=dict(correction_start_index=start,
                             base_geometry=str(base_path), base_geometry_sha256=sha(base_path),
                             common_cut_implementation_sha256=sha(common.__file__),
                             base_modes=base_meta['modes'], common_modes=meta['modes'],
                             equality='Every coefficient of the map and its first two derivatives '
                                      'is the defining base coefficient before the correction start. '
                                      'The added quintic has zero value, first, and second jet at that start.',
                             pieces=[dict(file=str(p), sha256=sha(p)) for p in (base_out, cut_out)]))
    for key in ('support_lower', 'area_element_lower'):
        out[key] = min(left[key], right[key])
    for key in ('principal_curvature_upper', 'norm_upper'):
        out[key] = max(left[key], right[key])
    if args.witness:
        out['witness_distance_lower'] = min(left['witness_distance_lower'], right['witness_distance_lower'])
    out['two_ball_diameter_upper'] = float(ordinary.up(2*out['norm_upper']))
    out['time_seconds'] = time.monotonic()-started
    args.out.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: out[key] for key in (
        'geometry_sha256', 'first_span', 'last_span_exclusive',
        'support_lower', 'principal_curvature_upper', 'norm_upper',
        'area_element_lower', 'entire_finite_prefix_covered', 'time_seconds')}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--angular', type=int, default=256)
    parser.add_argument('--radial', type=int, default=1)
    parser.add_argument('--batch', type=int, default=16)
    parser.add_argument('--ell', type=float, default=0.)
    parser.add_argument('--witness', action='store_true')
    run(parser.parse_args())
