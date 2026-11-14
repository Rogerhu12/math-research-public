#!/usr/bin/env python3
"""One small original-class transport roundtrip, with no mathematical assembly."""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import copy
import hashlib
import json
from pathlib import Path
import resource
import struct
import tempfile
import time
from types import SimpleNamespace
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_local_normal_system import LocalNormalSystem
from fd2d_gc_normal_checkpoint import save_normal_checkpoint,load_normal_checkpoint,PIECE_LIMIT


def same(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,(np.ndarray,np.generic)):
        x,y=np.asarray(a),np.asarray(b)
        return x.shape==y.shape and x.dtype==y.dtype and x.tobytes()==y.tobytes()
    if type(a) is float:return struct.pack('>d',a)==struct.pack('>d',b)
    if type(a) in (list,tuple):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    if type(a) is dict:return list(a)==list(b) and all(same(a[k],b[k]) for k in a)
    return a==b


def rejected(call,text):
    try:call()
    except ValueError as error:return text in str(error)
    return False


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    started=time.monotonic();root=Path(tempfile.mkdtemp(prefix='fd2d-normal-checkpoint-fixture-'))
    # Same raw/parameter widths as current K31/tail16/profile7, but only
    # nine abstract nodes. No real surface/profile/field is evaluated.
    K,e,q,P,N=31,32,95,54,9
    central=np.array([0,1],int)
    pairs=np.array([(6*q+j,6*q+63+j) for j in range(e)],int)
    extra=np.r_[3*q+np.arange(63,q),pairs[:,1]]
    core=(np.arange(e*K,dtype=float).reshape(e,K)-121.)/257.
    problem=SimpleNamespace(N=N,q=q,parameter_count=P,K=K,e=e,
        fixed_central_nodes=central,additional_fixed_field_indices=extra,
        trace_gauge_pairs=pairs,core_coefficients=core)
    normal=LocalNormalSystem(problem);rng=np.random.default_rng(20261112)
    arrays=normal.diagonal+normal.upper+[normal.Hfp,normal.Hpp,normal.gf,normal.gp,
                                      normal.field_norm_squared,normal.parameter_norm_squared]
    for a in arrays:
        a[:]=rng.standard_normal(a.shape)
        if a.size:a.flat[::17]=-0.0
    normal.residual_squared=13.125
    normal.rows=103;normal.blocks=7
    normal.row_groups={'abstract_node_rows':71,'abstract_cell_rows':32}
    normal.info=dict(scope='synthetic transport data, not an assembled physical normal',
        signed_zero=-0.0,numpy_scalar=np.float64(-0.0),numpy_integer=np.int64(7),
        small_array=np.array([.1,-0.,np.nextafter(1.,2.)]),tuple_metadata=('one',2),
        nested={'flag':True,'none':None,'unicode':'精确保存'},row_groups=normal.row_groups.copy())
    binding=dict(schema='fd2d-transport-only-test-binding-v1',
        state='synthetic nine-node payload, not23b4 or any actual physical objective',
        input_sha256=hashlib.sha256(b'fd2d-single-small-transport-fixture').hexdigest(),
        widths=dict(K=K,tail_count=16,profile_count=7,raw=q,parameters=P),
        objective=None,source_sha256=identity(Path(__file__).with_name('fd2d_gc_local_normal_system.py'))['sha256'])
    manifest=save_normal_checkpoint(normal,root/'normal',binding=binding)
    loaded=load_normal_checkpoint(problem,manifest,expected_binding=binding)
    checks={key:same(getattr(normal,key),getattr(loaded,key)) for key in (
        'diagonal','upper','Hfp','Hpp','gf','gp','field_norm_squared','parameter_norm_squared',
        'residual_squared','rows','blocks','row_groups','info')}
    map_checks={key:same(getattr(normal.mapping,key),getattr(loaded.mapping,key)) for key in (
        'N','q','P','total','count','central_nodes','extra','pairs','fixed','free','node_free',
        'widths','offsets','field_maps','parameter_maps')}
    saved=json.loads(manifest.read_text())
    # Three cheap integrity refusals on this same small transport fixture.
    # No second normal assembly or roundtrip is performed.
    bad_binding=dict(binding,state='different actual input')
    binding_refusal=rejected(lambda:load_normal_checkpoint(problem,manifest,expected_binding=bad_binding),'binding differs')
    bad_problem=copy.copy(problem);bad_problem.core_coefficients=core.copy()
    bad_problem.core_coefficients[0,0]=np.nextafter(core[0,0],np.inf)
    mapping_refusal=rejected(lambda:load_normal_checkpoint(bad_problem,manifest,expected_binding=binding),'elimination map differs')
    piece=manifest.parent/saved['pieces'][-1]['file'];data=piece.read_bytes()
    damaged=bytearray(data);damaged[-1]^=1
    try:
        piece.write_bytes(damaged)
        corruption_refusal=rejected(lambda:load_normal_checkpoint(problem,manifest,expected_binding=binding),'SHA256 mismatch')
    finally:piece.write_bytes(data)
    report=dict(schema='fd2d-single-small-normal-checkpoint-transport-check-v1',
        source=identity(__file__),helper=identity(Path(__file__).with_name('fd2d_gc_normal_checkpoint.py')),
        original_normal_source=identity(Path(__file__).with_name('fd2d_gc_local_normal_system.py')),
        fixture_manifest=identity(manifest),fixture_manifest_definition=saved,
        original_class_used=True,modes=K,raw_width=q,parameter_width=P,abstract_node_count=N,
        zero_width_nodes=np.flatnonzero(normal.mapping.widths==0).tolist(),
        normal_storage_bytes=normal.storage_bytes(),all_normal_values_bitwise_equal=all(checks.values()),
        value_checks=checks,all_rebuilt_mapping_values_bitwise_equal=all(map_checks.values()),mapping_checks=map_checks,
        wrong_binding_rejected=binding_refusal,one_ulp_central_mapping_change_rejected=mapping_refusal,
        one_byte_piece_corruption_rejected=corruption_refusal,
        final_fixture_piece_restored=hashlib.sha256(piece.read_bytes()).hexdigest()==saved['pieces'][-1]['sha256'],
        largest_numerical_piece_bytes=max(p['bytes'] for p in saved['pieces']),piece_limit_exclusive=PIECE_LIMIT,
        at_most_four_nodes_in_each_node_piece=all(p['node_range'][1]-p['node_range'][0]<=4
            for p in saved['pieces'] if p['kind']=='nodes'),
        no_actual_objective_evaluation=True,no_J_assembly=True,no_normal_assembly=True,
        no_QP=True,no_BVP=True,no_body=True,
        original_active_sources_modified=False,
        seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    report['passed']=bool(all(checks.values()) and all(map_checks.values()) and binding_refusal
        and mapping_refusal and corruption_refusal and report['final_fixture_piece_restored']
        and report['largest_numerical_piece_bytes']<PIECE_LIMIT and report['at_most_four_nodes_in_each_node_piece'])
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:report[key] for key in ('passed','normal_storage_bytes','largest_numerical_piece_bytes',
        'all_normal_values_bitwise_equal','all_rebuilt_mapping_values_bitwise_equal','seconds','peak_rss_kib')}),flush=True)
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
