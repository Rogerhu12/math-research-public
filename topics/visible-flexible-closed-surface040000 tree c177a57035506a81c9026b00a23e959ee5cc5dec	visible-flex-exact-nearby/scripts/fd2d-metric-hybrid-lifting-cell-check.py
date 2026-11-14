#!/usr/bin/env python3
"""One immutable atlas cell: hybrid identity, unchanged state J, and p JVPs.

Only the reported exit cell is assembled. No whole-domain BVP matrix,
nonlinear solve, or actual position-map integration is performed.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_raw_bump_ruling_atlas import RulingAtlasRawBumpDAE
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2 as endpoint
from fd2d_gc_hybrid_lifting_codazzi_d2 import (gauss_cell_codazzi_hybrid_d2,
    known_lifting_correction, point_view)
from fd2d_gc_codazzi_complement import _high
from fd2d_gc_d2_complements import d2_high_rows


def maximum(q):
    return float(np.max(abs(np.asarray(q)), initial=0.))


def joined(q):
    return np.r_[q['retained_residual'], q['high_residual']]


def error(a, b):
    d=np.asarray(a)-np.asarray(b)
    return dict(absolute_maximum=maximum(d),
        relative_l2=float(np.linalg.norm(d)/max(1e-30,np.linalg.norm(b))),
        scaled_maximum=maximum(d)/max(1.,maximum(b)))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('field','source-report','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--cell',type=int,default=71)
    args=ap.parse_args();started=time.monotonic();stem=str(args.out_prefix)
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a fresh immutable check stem')
    report0=json.loads(args.source_report.read_text());saved=load_npz(args.field)
    fid=identity(args.field);rid=identity(args.source_report)
    if fid['sha256']!=report0['latest_checkpoint']['sha256']:
        raise ValueError('Selected report must bind this immutable accepted field')
    settings=report0['settings'];cref=json.loads(str(saved['coast_reference_definition']))
    atlas=json.loads(str(saved['angular_atlas_definition']))
    whole=RulingAtlasRawBumpDAE(settings['candidate'],modes=int(saved['modes']),max_step=.04,
        supports=saved['profile_supports'],profile_count=int(saved['profile_count']),
        base_kind=str(saved['base_kind']),blend=tuple(saved['blend']),
        reference_inlet=settings['reference_inlet'],reference_cache=settings['reference_cache'],
        reference_rim_fraction=cref['rim_fraction'],
        atlas_entry_start=atlas['entry_transition'][0],atlas_exit_stop=atlas['exit_transition'][1])
    if (not np.array_equal(whole.x,saved['mesh']) or whole.angular_atlas_definition!=atlas
            or whole.coast_reference_definition!=cref
            or whole.seed_weight_definition!=json.loads(str(saved['seed_weight_definition']))):
        raise ValueError('Actual defining mesh/atlas/lifting identity differs from the checkpoint')
    cell=args.cell
    if not 0<=cell<whole.N-1:
        raise ValueError('Cell outside actual saved mesh')
    problem=point_view(whole,whole.x[cell:cell+2])
    z=np.r_[saved['corrections'][cell:cell+2].ravel(),saved['parameters']]
    initial_z=z.copy();initial_mesh=problem.x.copy()
    initial_coords={k:v.copy() for k,v in problem.coords.items()}
    beforeF,beforeData=problem.evaluate(z,jacobian=False)
    beforeFields=beforeData['fields'].copy();del beforeData
    here=Path(__file__).resolve().parent
    sources=[identity(__file__)]+[identity(here/name) for name in (
        'fd2d_gc_hybrid_lifting_codazzi_d2.py','fd2d_gc_gauss_cell_codazzi_endpoint_d2.py',
        'fd2d_gc_raw_bump_ruling_atlas.py','fd2d_gc_frozen_ruling_atlas.py',
        'fd2d_gc_raw_bump_coast_reference.py','fd2d_gc_codazzi_complement.py')]
    base=endpoint(problem,z,order=2,high_weight=1.,jacobian=True)
    hybrid=gauss_cell_codazzi_hybrid_d2(problem,z,known_order=8,jacobian=True)
    offset=problem.N*problem.q
    state_difference=max(maximum((hybrid[key][:,:offset]-base[key][:,:offset]).data)
        for key in ('retained_jacobian','high_jacobian'))
    y,p=problem.unpack(z)
    known8=known_lifting_correction(problem,p,known_order=8,jacobian=True)
    fine_rule=known8['cells'][0]
    # Independently compose the already frozen endpoint rule on each true
    # subpanel with y=0. This checks signs and h-normalization without
    # constructing any high-order zero-field Jacobian.
    zero=np.r_[np.zeros(offset),p]
    coarse0=endpoint(problem,zero,order=2,jacobian=False)
    fine0={key:np.zeros_like(coarse0[key]) for key in
        ('retained_residual','high_residual','full_codazzi_cells')}
    for a,b in zip(fine_rule['split_knots'][:-1],fine_rule['split_knots'][1:]):
        sub=point_view(problem,np.array([a,b]));zz=np.r_[np.zeros(sub.N*sub.q),p]
        q=endpoint(sub,zz,order=8,jacobian=False);weight=(b-a)/problem.h[0]
        for key in fine0:
            fine0[key]+=weight*q[key]
    identity_errors={key:maximum(hybrid[key]-base[key]-fine0[key]+coarse0[key]) for key in fine0}
    twelve=gauss_cell_codazzi_hybrid_d2(problem,z,known_order=12,jacobian=False)
    comparison=dict(full=maximum(twelve['full_codazzi_cells']-hybrid['full_codazzi_cells']),
        retained=maximum(twelve['retained_residual']-hybrid['retained_residual']),
        high=maximum(twelve['high_residual']-hybrid['high_residual']),
        whole_G2_sampled_maximum=maximum(base['full_codazzi_cells']),
        hybrid_G8_sampled_maximum=maximum(hybrid['full_codazzi_cells']),
        hybrid_G12_sampled_maximum=maximum(twelve['full_codazzi_cells']),
        continuous_error_bound=False)
    compression=d2_high_rows(problem)
    def change_rows(q):
        low=np.concatenate((problem.PE@q[:,:,0],problem.PO@q[:,:,1]),axis=0).T.ravel()
        high=np.concatenate((compression.project(_high(q[:,:,0],problem.E,problem.PE),'even'),
            compression.project(_high(q[:,:,1],problem.O,problem.PO),'odd')),axis=0).T.ravel()
        return np.r_[low,high]
    rng=np.random.default_rng(152152);rows=[];witnesses={}
    tail=np.arange(problem.tail_parameter_slice.start,problem.tail_parameter_slice.stop)
    tail=tail[(p[tail]>1e-3)&(p[tail]<1.2-1e-3)]
    if not len(tail):
        raise ValueError('Choose an actual field with a nonempty interior tail parameter direction')
    groups=(('nonzero_interior_tail_parameters',tail),
            ('nonzero_physical_profile_parameters',np.arange(problem.profile_parameter_slice.start,problem.profile_parameter_slice.stop)))
    for name,ids in groups:
        direction=np.zeros(problem.size);direction[offset+ids]=rng.standard_normal(len(ids))
        direction/=np.linalg.norm(direction);step=1e-6
        analytic=np.r_[hybrid['retained_jacobian']@direction,hybrid['high_jacobian']@direction]
        old_analytic=np.r_[base['retained_jacobian']@direction,base['high_jacobian']@direction]
        plus=gauss_cell_codazzi_hybrid_d2(problem,z+step*direction,jacobian=False)
        plus_change=change_rows(known_lifting_correction(problem,p+step*direction[offset:],jacobian=False)['change'])
        minus=gauss_cell_codazzi_hybrid_d2(problem,z-step*direction,jacobian=False)
        minus_change=change_rows(known_lifting_correction(problem,p-step*direction[offset:],jacobian=False)['change'])
        finite=(joined(plus)-joined(minus))/(2*step)
        delta_finite=(plus_change-minus_change)/(2*step)
        row=dict(group=name,parameter_indices=ids.tolist(),step=step,
            analytic_JVP_l2=float(np.linalg.norm(analytic)),
            added_known_lifting_JVP_l2=float(np.linalg.norm(analytic-old_analytic)),
            full_hybrid_error=error(finite,analytic),
            added_known_lifting_error=error(delta_finite,analytic-old_analytic))
        rows.append(row);witnesses[name+'_direction']=direction
        witnesses[name+'_analytic']=analytic;witnesses[name+'_finite']=finite
        witnesses[name+'_added_analytic']=analytic-old_analytic;witnesses[name+'_added_finite']=delta_finite
    afterF,afterData=problem.evaluate(z,jacobian=False)
    unchanged=dict(original_local_provider_F=maximum(afterF-beforeF),
        original_local_fields=maximum(afterData['fields']-beforeFields),
        vector=maximum(z-initial_z),mesh=maximum(problem.x-initial_mesh),
        chart=max(maximum(problem.coords[k]-v) for k,v in initial_coords.items()),
        actual_Gauss2_point_Gauss=maximum(hybrid['point_gauss']-base['point_gauss']))
    projection_error=max(
        maximum((problem.PE@hybrid['full_codazzi_cells'][:,:,0]).T.ravel()-hybrid['retained_cells'][:,:problem.e].ravel()),
        maximum((problem.PO@hybrid['full_codazzi_cells'][:,:,1]).T.ravel()-hybrid['retained_cells'][:,problem.e:].ravel()))
    checks=dict(hybrid_zero_field_identity=max(identity_errors.values())<5e-11,
        state_Jacobian_exactly_unchanged=state_difference==0.,
        both_parameter_JVPs_nonzero=all(row['analytic_JVP_l2']>1e-8 and row['added_known_lifting_JVP_l2']>1e-8 for row in rows),
        full_and_added_parameter_JVPs=all(row[key]['relative_l2']<2e-5 for row in rows for key in ('full_hybrid_error','added_known_lifting_error')),
        original_local_quantities_unchanged=max(unchanged.values())==0.,
        full_projection_matches_retained=projection_error<5e-11,
        actual_normal_subpanel_rules=all(x['narrow_panel_fallback'] is None for x in fine_rule['panels']),
        field_bytes_unchanged=identity(args.field)['sha256']==fid['sha256'],
        sources_unchanged=all(identity(x['path'])['sha256']==x['sha256'] for x in sources))
    witnesses.update(actual_local_vector=z,actual_cell_endpoints=problem.x,
        original_full=base['full_codazzi_cells'],hybrid8_full=hybrid['full_codazzi_cells'],
        hybrid12_full=twelve['full_codazzi_cells'])
    packet=save_npz(Path(stem+'-witnesses.npz'),**witnesses)
    report=dict(schema='fd2d-R152-actual-cell-hybrid-known-lifting-check-v1',
        actual_execution=True,passed=all(checks.values()),checks=checks,sources=sources,
        field=fid,source_report=rid,cell=cell,actual_cell_endpoints=problem.x.tolist(),
        actual_whole_node_count=whole.N,local_view_nodes=problem.N,angular_work=problem.work,
        hybrid_identity_errors=identity_errors,state_Jacobian_maximum_change=state_difference,
        known_Gauss8_vs_12=comparison,JVPs=rows,JVP_seed=152152,
        unchanged_original_local_quantities=unchanged,full_projection_error=projection_error,
        finite_rule=hybrid['info'],witnesses=packet,whole_BVP_matrix_assembled=False,
        nonlinear_solve_performed=False,body_integration_run=False,continuous_certificate=False,
        seconds=time.monotonic()-started,maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    path=Path(stem+'-report.json');path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(path),passed=report['passed'],checks=checks,
        known_Gauss8_vs_12=comparison,JVPs=rows,seconds=report['seconds'],maximum_rss_kib=report['maximum_rss_kib'])),flush=True)
    return 0 if report['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
