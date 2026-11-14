#!/usr/bin/env python3
"""An explicit new initial field, resetting coast corrections once.

This is not an exact representation transfer and is not the plain-bump
initialization pathway. It preserves the existing global ruling atlas,
physical p/g and full known lifting; new nodal corrections are (1-w)*old.
Their true radial interpolant is P1. The resulting full residual is paid.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,datetime,json,resource,time,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_raw_bump_ruling_atlas import RulingAtlasRawBumpDAE,checkpoint_arrays
from fd2d_gc_raw_bump_coast_reference import coast_window
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2
from fd2d_gc_bump_residual_locations import residual_locations


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('candidate','warm-start','radius-packet','reference-inlet','out-prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path);args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('A distinct new-field stem is required')
    start=time.monotonic();report=dict(schema='fd2d-explicit-ruling-coast-correction-reset-initializer-v1',
        source=identity(__file__),input=identity(args.warm_start),candidate=identity(args.candidate),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        completed=False,nonlinear_solve_performed=False,whole_strong_solution=False,exception=None)
    def save():
        report.update(seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        a=load_npz(args.warm_start);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:raise ValueError('Wrong base radius packet')
        witness=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256'])
        problem=RulingAtlasRawBumpDAE(args.candidate,modes=int(a['modes']),max_step=.04,gap=.9,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=.1)
        for key,expected in (('angular_atlas_definition',problem.angular_atlas_definition),
                ('coast_reference_definition',problem.coast_reference_definition),
                ('reference_evaluation_definition',problem.reference_evaluation_definition),
                ('seed_weight_definition',problem.seed_weight_definition)):
            if key not in a or json.loads(str(a[key]))!=expected:raise ValueError('Different actual field '+key)
        if str(a['candidate_sha256'])!=report['candidate']['sha256'] or not np.array_equal(a['mesh'],problem.x):
            raise ValueError('Different physical candidate or computational mesh')
        old=np.r_[a['corrections'].ravel(),a['parameters']];y,p=problem.unpack(old)
        ref=problem.coast_reference;w,_=coast_window(problem.x,ref.entry_s,ref.length,problem.reference_rim_fraction)
        changed=(1-w)[:,None]*y
        before=np.r_[changed.ravel(),p.copy()];vector=problem.impose_linear_boundary_values(before)
        new_y,new_p=problem.unpack(vector)
        report['explicit_reset']=dict(formula='new node correction=(1-w)*old node correction',
            known_lifting_changed=False,angular_atlas_changed=False,physical_parameters_unchanged=bool(np.array_equal(new_p,p)),
            physical_metric_changed=False,old_full_field_preserved=False,
            exact_boundary_projection_change=float(np.max(abs(vector-before))),
            zero_weight_nodes_unchanged=bool(np.array_equal(new_y[w==0],y[w==0])),
            plateau_node_indices=np.flatnonzero(w==1).tolist(),
            plateau_corrections_maximum=float(np.max(abs(new_y[w==1]),initial=0.)),
            maximum_correction_change=float(np.max(abs(new_y-y))),
            between_nodes='actual P1 of new nodal coefficients, not the nonlinear product (1-w(s))*old P1',
            plain_bump_initializer_used=False,coast_physical_reference_exact_GC_scope='frozen base delta=0 only')
        report['warm']=save_npz(stem.with_name(stem.name+'-warm.npz'),**checkpoint_arrays(problem,vector,report['candidate']['sha256']),
            initializer_definition=np.array(json.dumps(report['explicit_reset'],sort_keys=True)),
            initializer_input_sha256=np.array(report['input']['sha256']))
        # The new field is evaluated once; old diagnostics remain bound to
        # their own closed report instead of being recomputed here.
        trap,data=problem.evaluate(vector);del data['lift'],data['fields_parameters']
        quadrature=gauss_cell_codazzi(problem,vector,order=2,high_weight=1.,jacobian=False,block_cells=8,
            consumer=gauss_cell_codazzi_endpoint_d2)
        raw=np.r_[quadrature['retained_residual'],trap[(problem.N-1)*problem.d:]]
        data['codazzi_cells']=quadrature['retained_cells'];n,m,l=(data['fields'][:,:,j] for j in range(3));disc=np.hypot(l-n,2*m)
        report['actual_new_initial']=dict(raw_maximum=float(np.max(abs(raw))),
            full_gauss_node_maximum=float(np.max(abs(data['full_gauss']))),
            formal_curvature_node_maximum=float(np.max(np.maximum(abs(n+l+disc),abs(n+l-disc)))/2),
            full_endpoint_codazzi_maximum=quadrature['info']['sampled_full_average_codazzi_maximum'],
            high_endpoint_codazzi_maximum=quadrature['info']['sampled_omitted_average_codazzi_maximum'],
            minimum_central_curvature=float((problem.seed+problem.core_basis@p[:problem.K]).min()),
            gap=float(data['axes']['gap']),node_n_minimum=float(n.min()))
        report['actual_new_locations']=residual_locations(problem,vector,data,
            {'omitted_codazzi_cells':quadrature['omitted_codazzi_cells']},7.2)
        report['node_field_change_maximum']=float(np.max(abs(np.stack((problem.E@(new_y[:,:problem.e]-y[:,:problem.e]).T,
            problem.O@(new_y[:,problem.e:problem.d]-y[:,problem.e:problem.d]).T,
            problem.E@(new_y[:,problem.d:]-y[:,problem.d:]).T),axis=-1))))
        report['reference_cache_statistics']=problem.coast_reference.cache_statistics()
        report['completed']=True;save();print(json.dumps(dict(completed=True,warm=report['warm'],diagnostics=report['actual_new_initial']),allow_nan=False),flush=True)
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc());save();raise

if __name__=='__main__':main()
