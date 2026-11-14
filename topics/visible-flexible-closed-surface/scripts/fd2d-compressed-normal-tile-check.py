#!/usr/bin/env python3
"""One small original-class compressed transport check, without assembly."""
from __future__ import annotations

import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'

import argparse
import hashlib
import io
import json
from pathlib import Path
import struct
import tempfile
import time
from types import SimpleNamespace

import numpy as np

from fd2d_gc_archive_arrays import identity
from fd2d_gc_local_normal_system import LocalNormalSystem
from fd2d_gc_compressed_normal_tile import (
    save_compressed_normal_tile,load_compressed_normal_tile,
    read_logical_manifest,read_logical_piece)


def same(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,(np.ndarray,np.generic)):
        x,y=np.asarray(a),np.asarray(b)
        return x.shape==y.shape and x.dtype==y.dtype and x.tobytes()==y.tobytes()
    if type(a) is float:return struct.pack('>d',a)==struct.pack('>d',b)
    if type(a) in (tuple,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    if type(a) is dict:return list(a)==list(b) and all(same(a[k],b[k]) for k in a)
    return a==b


def rejects(call,fragment):
    try:call()
    except ValueError as error:return fragment in str(error)
    return False


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.perf_counter()
    root=Path(tempfile.mkdtemp(prefix='fd2d-compressed-normal-tile-fixture-'))
    K,e,q,P,N=31,32,95,54,9
    pairs=np.array([(6*q+j,6*q+63+j) for j in range(e)],int)
    core=(np.arange(e*K,dtype=float).reshape(e,K)-121.)/257.
    problem=SimpleNamespace(N=N,q=q,parameter_count=P,K=K,e=e,
        fixed_central_nodes=np.array([0,1],int),
        additional_fixed_field_indices=np.r_[3*q+np.arange(63,q),pairs[:,1]],
        trace_gauge_pairs=pairs,core_coefficients=core)
    normal=LocalNormalSystem(problem)
    arrays=normal.diagonal+normal.upper+[normal.Hfp,normal.Hpp,normal.gf,normal.gp,
                                      normal.field_norm_squared,normal.parameter_norm_squared]
    for a in arrays:
        a.fill(0)
        if a.size:a.flat[::17]=-0.0
    # A sparse tile-shaped synthetic payload, not J^T J or a real equation.
    rng=np.random.default_rng(20261113)
    for a in (normal.diagonal[4],normal.upper[4],normal.Hpp,normal.gp):
        a[:]=rng.standard_normal(a.shape)
        if a.size:a.flat[::17]=-0.0
    left,right=map(int,normal.mapping.offsets[4:6])
    normal.Hfp[left:right]=rng.standard_normal((right-left,P))
    normal.gf[left:right]=rng.standard_normal(right-left)
    normal.residual_squared=13.125;normal.rows=103;normal.blocks=7
    normal.row_groups={'synthetic_only':103}
    normal.info=dict(scope='transport-only sparse synthetic tile',signed_zero=-0.0,
        scalar=np.float64(-0.),integer=np.int64(7),tuple_data=('one',2),
        tiny_array=np.array([.1,-0.,np.nextafter(1.,2.)]),nested={'none':None,'ok':True})
    binding=dict(schema='fd2d-compressed-tile-transport-fixture-v1',
        input='synthetic nine-node data, not an actual physical field',
        counts=dict(K=K,tail=16,profile=7,parameters=P),finite_objective=None)
    manifest=save_compressed_normal_tile(normal,root/'tile',binding=binding)
    logical=read_logical_manifest(manifest)
    rows=[]
    for row in logical['pieces']:
        data=read_logical_piece(manifest,row)
        assert len(data)==row['bytes']<1_000_000
        assert hashlib.sha256(data).hexdigest()==row['sha256']
        with np.load(io.BytesIO(data),allow_pickle=False) as packet:
            assert set(packet.files)==set(row['arrays'])
        rows.append(dict(file=row['file'],bytes=len(data),sha_equal=True))
    loaded=load_compressed_normal_tile(problem,manifest,expected_binding=binding)
    values={key:same(getattr(normal,key),getattr(loaded,key)) for key in (
        'diagonal','upper','Hfp','Hpp','gf','gp','field_norm_squared','parameter_norm_squared',
        'residual_squared','rows','blocks','row_groups','info')}
    mappings={key:same(getattr(normal.mapping,key),getattr(loaded.mapping,key)) for key in (
        'N','q','P','total','count','central_nodes','extra','pairs','fixed','free','node_free',
        'widths','offsets','field_maps','parameter_maps')}
    bad_binding=dict(binding,input='wrong input')
    binding_rejected=rejects(lambda:load_compressed_normal_tile(problem,manifest,
        expected_binding=bad_binding),'binding differs')
    bad_row=dict(logical['pieces'][0],bytes=logical['pieces'][0]['bytes']+1)
    row_rejected=rejects(lambda:read_logical_piece(manifest,bad_row),'not exactly bound')
    outer=json.loads(manifest.read_text())
    inner=json.loads((manifest.parent/'payload/index.json').read_text())
    damaged=manifest.parent/'payload'/inner['pieces'][-1]['compressed_file']
    original=damaged.read_bytes();change=bytearray(original);change[-1]^=1
    try:
        damaged.write_bytes(change)
        corruption_rejected=rejects(lambda:read_logical_piece(manifest,logical['pieces'][-1]),
                                   'compressed piece SHA')
    finally:damaged.write_bytes(original)
    owned_raw_removed=not list(root.glob('.tile.raw-*'))
    report=dict(schema='fd2d-compressed-normal-tile-small-roundtrip-v1',
        source=identity(__file__),helper=identity(Path(__file__).with_name('fd2d_gc_compressed_normal_tile.py')),
        fixture_manifest=identity(manifest),fixture_definition=outer,
        logical_manifest_schema=logical['schema'],logical_piece_checks=rows,
        original_class_used=type(loaded) is LocalNormalSystem,
        values_bitwise_equal=all(values.values()),value_checks=values,
        rebuilt_mapping_bitwise_equal=all(mappings.values()),mapping_checks=mappings,
        wrong_binding_rejected=binding_rejected,altered_piece_row_rejected=row_rejected,
        compressed_one_byte_corruption_rejected=corruption_rejected,
        own_raw_temporary_directory_removed=owned_raw_removed,
        logical_numerical_bytes=outer['logical_numerical_bytes'],
        compressed_numerical_bytes=outer['compressed_numerical_bytes'],
        largest_compressed_piece_bytes=outer['largest_compressed_piece_bytes'],
        disk_savings_are_for_this_synthetic_payload_only=True,
        no_F_J_normal_assembly_QP_BVP_or_body=True,
        old_actual_normals_tiles_sources_modified=False,
        seconds=time.perf_counter()-start)
    report['passed']=bool(all(values.values()) and all(mappings.values()) and binding_rejected
        and row_rejected and corruption_rejected and owned_raw_removed)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:report[key] for key in ('passed','values_bitwise_equal',
        'rebuilt_mapping_bitwise_equal','logical_numerical_bytes','compressed_numerical_bytes',
        'largest_compressed_piece_bytes','seconds')},allow_nan=False))
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
