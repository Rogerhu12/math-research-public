#!/usr/bin/env python3
# New 78718 explicit storage adaptation; original mathematical source is retained below.
"""Build an exact shared-jet C2 mirror seam from a finite prefix.

The underlying fixed physical metric and BVP checkpoint are untouched.
The finite interpolant alone imposes the exact inlet parity needed for
reflection across z=0. This is an approximation, not an exact isometry or
an infinite-tail existence certificate.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent

_storage_spec = importlib.util.spec_from_file_location(
    'prefix_78718_explicit_storage', HERE/'78718-prefix-storage-v1.py')
storage = importlib.util.module_from_spec(_storage_spec)
_storage_spec.loader.exec_module(storage)
spec = importlib.util.spec_from_file_location(
    'mirror_original', HERE / '78718-prefix-fullxyz-hermite-storage-v1.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
flat_spec = importlib.util.spec_from_file_location(
    'mirror_flat_source', HERE / 'db6f-prefix-flat-geometry-source.py')
flat_source = importlib.util.module_from_spec(flat_spec)
flat_spec.loader.exec_module(flat_source)
base.source = flat_source.source


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def fraction_record(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator),
            'display': float(x)}


def build(args):
    base.build(args)
    meta_path = args.out_prefix.with_suffix('.json')
    meta = json.loads(meta_path.read_text())
    stored_meta, payload, _storage_bindings = storage.read_payload(meta_path, verify_arrays=True)
    if stored_meta != meta:
        raise ValueError('Base metadata changed during storage read')
    saved = np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False)
    arrays = {k: saved[k].copy() for k in saved.files}
    jets = arrays['jets']
    M = meta['modes']
    old_second = jets[2, 0, 2*M+1:].copy()
    jets[2, 0, 2*M+1:] = 0.0
    assert np.all(jets[0, 0, 2*M+1:] == 0)
    assert np.all(jets[1, 0, :-1] == 0)
    assert jets[1, 0, -1] == 1
    assert np.all(jets[2, 0, 2*M+1:] == 0)
    stream = io.BytesIO()
    np.savez(stream, **arrays)
    logical_payload = gzip.compress(stream.getvalue(), mtime=0)
    storage_record = storage.write_payload(args.out_prefix, logical_payload,
                                           nodes=meta['nodes'], modes=meta['modes'])
    radial = [Fraction(float(v)) for v in jets[0, 0, :M+1]]
    tangent = [Fraction(float(v)) for v in jets[0, 0, M+1:2*M+1]]
    outer = sum(radial)
    inner = sum(v*((-1)**j) for j,v in enumerate(radial))
    tangent_inner = inner + sum(3*j*v*((-1)**j)
                               for j,v in enumerate(tangent, 1))
    meta.update(
        data_storage=storage_record, data_sha256=storage_record['logical_sha256'],
        wrapper_sha256=sha(__file__),
        profile_loader_sha256=sha(HERE / 'db6f-prefix-flat-geometry-source.py'),
        profile_implementation_sha256=sha(HERE / 'db6f-prefix-flat-profile.py'),
        mirror_inlet_C2_exact=True,
        mirror_definition='X(s,psi) for s>=0; diag(1,1,-1) X(-s,psi) '
                          'for s<=0. Height and height second jet at s=0 '
                          'are exactly zero; first s jet is exactly e_z.',
        mirror_second_height_adjustment_max=float(abs(old_second).max()),
        exact_inlet_witness={
            'radius_at_psi_0': fraction_record(outer),
            'radius_at_psi_pi_over_3': fraction_record(inner),
            'radial_gap': fraction_record(outer-inner),
            'tangent_at_psi_pi_over_3': fraction_record(tangent_inner),
            'radial_normal_points_outward': tangent_inner > 0,
            'positive_radii_and_gap': outer > inner > 0},
        complete_closed_surface=False,
        exact_isometry_certified=False)
    meta['mathematical_definition'] += (
        ' Additionally all inlet height second jets are exactly zero. '
        'Thus direct upper/lower reflection is exactly C2 without a '
        'central cylinder; its inlet immersion follows from a nonzero '
        'planar angular tangent and the exact vertical first s jet.')
    meta_path.write_text(json.dumps(meta, indent=2)+'\n')
    print(json.dumps({k: meta[k] for k in (
        'mirror_inlet_C2_exact', 'mirror_second_height_adjustment_max',
        'exact_inlet_witness', 'complete_closed_surface')}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-root', 'checkpoint', 'linear-port', 'out-prefix'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--modes', type=int, default=16)
    parser.add_argument('--angular', type=int, default=768)
    parser.add_argument('--quadrature', type=int, default=8)
    parser.add_argument('--subdivide', type=int, default=1)
    parser.add_argument('--ell', type=float, default=0.)
    build(parser.parse_args())


if __name__ == '__main__':
    main()
