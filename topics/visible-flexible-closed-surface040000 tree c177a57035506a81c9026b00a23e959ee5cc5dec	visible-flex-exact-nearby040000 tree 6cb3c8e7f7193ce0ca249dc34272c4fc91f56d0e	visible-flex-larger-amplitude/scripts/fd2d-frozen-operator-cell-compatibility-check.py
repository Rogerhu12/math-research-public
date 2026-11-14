#!/usr/bin/env python3
"""One actual coast cell through the untouched strict R152 type guard.

No BVP, global objective, global J, body or active process is touched.
The original and adapted complete no-J cell consumers use the same fixed
4251 input and physical interval, including original fine known lifting.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem
from fd2d_gc_positive_trace_stream_normal import radial_view
from fd2d_gc_frozen_operator_projections import install_frozen_operator_projection_cache
from fd2d_gc_gauss_cell_positive_trace import gauss_cell_positive_trace
from fd2d_gc_gauss_cell_frozen_operator_compatible import gauss_cell_positive_trace_frozen_operator_compatible


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('input','candidate','radius-packet','reference-inlet','reference-cache','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a new immutable check report')
    begun=time.perf_counter();saved=load_npz(a.input)
    proof=json.loads(a.radius_packet.read_text())
    witness=dict(**identity(a.radius_packet),candidate_sha256=proof['candidate_sha256'])
    problem=create_midpoint_refined_problem(a.candidate,saved_field=saved,split_cells=(),
        max_step=.04,gap=.9,reference_inlet=a.reference_inlet,reference_cache=a.reference_cache,
        base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=.1)
    indices=np.array([64,65]);y=saved['corrections'];parameters=saved['parameters']
    z=np.r_[y[indices].ravel(),parameters]
    old=radial_view(problem,indices)
    before=gauss_cell_positive_trace(old,z,order=2,high_weight=1.,jacobian=False)
    cache=install_frozen_operator_projection_cache(problem,byte_limit=32*1024*1024)
    new=radial_view(problem,indices)
    after=gauss_cell_positive_trace_frozen_operator_compatible(new,z,order=2,high_weight=1.,jacobian=False)
    fields=('retained_residual','high_residual','retained_cells','omitted_codazzi_cells',
            'full_codazzi_cells','point_gauss','quadrature_points')
    comparisons={}
    for key in fields:
        aa,bb=np.asarray(before[key]),np.asarray(after[key])
        if aa.shape!=bb.shape or not np.all(np.isfinite(aa)) or not np.all(np.isfinite(bb)):
            raise ValueError('Invalid compared original cell output '+key)
        comparisons[key]=dict(shape=list(aa.shape),
            maximum_absolute=float(np.max(abs(aa-bb),initial=0.)),
            maximum_scaled=float(np.max(abs(aa-bb)/(1+abs(aa)),initial=0.)),
            bitwise_equal=bool(aa.dtype==bb.dtype and aa.tobytes()==bb.tobytes()))
    original_info_preserved={key:before['info'][key]==after['info'][key] for key in before['info']}
    scope=after['info']['runtime_operator_cache_compatibility']
    passed=(all(v['bitwise_equal'] for v in comparisons.values())
            and all(original_info_preserved.values())
            and scope['old_strict_identity_check_unchanged']
            and not scope['operator_projection_cache_used_in_R152_R153_background'])
    report=dict(schema='fd2d-original-R152-background-operator-cache-compatibility-check-v1',
        actual_execution=True,passed=bool(passed),source=identity(__file__),input=identity(a.input),
        candidate=identity(a.candidate),
        compatibility_source=identity(Path(__file__).with_name('fd2d_gc_gauss_cell_frozen_operator_compatible.py')),
        projection_source=identity(Path(__file__).with_name('fd2d_gc_frozen_operator_projections.py')),
        original_cell_source=identity(Path(__file__).with_name('fd2d_gc_gauss_cell_positive_trace.py')),
        original_hybrid_source=identity(Path(__file__).with_name('fd2d_gc_positive_gauss_coast_hybrid.py')),
        input_node_indices=indices.tolist(),physical_interval=problem.x[indices].tolist(),
        comparisons=comparisons,original_info_preserved=original_info_preserved,
        runtime_compatibility=scope,cache_statistics=cache.statistics(),
        known_lifting_selected_cells=before['info'].get('selected_coast_local_cells'),
        known_lifting_order=before['info'].get('known_lifting_quadrature_order'),
        no_BVP=True,no_whole_residual=True,no_Jacobian=True,no_body=True,
        original_or_active_source_changed=False,
        seconds=time.perf_counter()-begun,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(passed=report['passed'],comparisons=comparisons,
        cache=cache.statistics(),seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])))
    if not passed:raise SystemExit(1)


if __name__=='__main__':main()
