#!/usr/bin/env python3
"""Publish an already complete normal tile with compact JSON transport.

No field, residual, Jacobian, normal assembly or factorization is evaluated.
The original raw checkpoint remains untouched. Its exact mathematical
binding, typed metadata and numerical piece identities must survive.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import json
from pathlib import Path
import traceback
from fd2d_gc_signed_search_context_v2 import NumericalContext
from fd2d_gc_signed_compressed_normal_tile_io import partition_context, tile_binding
from fd2d_gc_compressed_normal_tile_v2 import (
    pack_existing_raw_checkpoint, read_logical_manifest)
from fd2d_gc_archive_arrays import identity


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--raw-manifest', type=Path, required=True)
    ap.add_argument('--tile-id', required=True)
    args = ap.parse_args()
    ctx = NumericalContext(args.request, args.out_prefix, install_caches=False)
    original_id = identity(args.raw_manifest)
    ctx.save_report(stage='recover_complete_raw_normal_without_reassembly',
        stage_source=identity(__file__), original_raw_manifest=original_id,
        actual_F_J_or_normal_assembly_evaluations=0,
        original_raw_checkpoint_modified=False,
        mathematical_common_binding_unchanged=True)
    try:
        root, plan, common, baseline = partition_context(ctx)
        selected = [d for d in plan['tiles'] if d['id'] == args.tile_id]
        if len(selected) != 1:
            raise ValueError('Use one actual declared tile')
        descriptor = selected[0]
        expected = tile_binding(common, descriptor)
        original = json.loads(args.raw_manifest.read_text())
        if original['binding'] != expected:
            raise ValueError('Saved complete raw tile has a different binding')
        result = pack_existing_raw_checkpoint(args.raw_manifest,
            root / 'normal-tiles' / args.tile_id, expected_binding=expected)
        logical = read_logical_manifest(result)
        if logical != original:
            raise ValueError('Whitespace-only transport changed the JSON object')
        if identity(args.raw_manifest) != original_id:
            raise ValueError('Original checkpoint manifest was modified')
        ctx.save_report(completed=True, tile_descriptor=descriptor,
            tile_manifest=identity(result), logical_JSON_object_equal=True,
            component_identities_equal=all(logical[k] == original[k] for k in
                ('binding_sha256', 'mapping_sha256', 'metadata_sha256', 'pieces')),
            actual_transport_source=identity(Path(__file__).with_name(
                'fd2d_gc_compressed_normal_tile_v2.py')))
        ctx.event('complete_raw_normal_recovered_without_numerical_evaluation',
            tile_id=args.tile_id, manifest=str(result))
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__, message=str(exc),
            traceback=traceback.format_exc()))
        raise


if __name__ == '__main__':
    raise SystemExit(main())
