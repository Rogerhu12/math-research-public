#!/usr/bin/env python3
"""One small actual-point check of the new frozen-geometry cache only."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,copy,hashlib,json,resource,time,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem
from fd2d_gc_raw_bump_coast_reference import coast_window
from fd2d_gc_prepared_geometry_cache import install_prepared_geometry_cache


def difference(a,b):
    if set(a)!=set(b):raise ValueError('Different returned packet keys')
    return max((float(np.max(abs(np.asarray(a[k])-np.asarray(b[k])),initial=0.)) for k in a),default=0.)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field',type=Path,required=True);ap.add_argument('--run-report',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh closed check stem')
    started=time.monotonic();here=Path(__file__).resolve().parent
    names=['fd2d_gc_prepared_geometry_cache.py',Path(__file__).name,
        'fd2d_gc_frozen_ruling_atlas.py','fd2d_gc_raw_bump_ruling_atlas.py',
        'fd2d_gc_raw_lifted_dae.py','fd2d_gc_blended.py','fd2d_gc_midpoint_refined_positive_trace_v3.py']
    source={n:identity(here/n) for n in names}
    r=dict(schema='fd2d-actual-prepared-frozen-geometry-cache-check-v1',status='running',passed=False,
        sources=source,input_field=identity(args.field),input_run_report=identity(args.run_report),
        no_BVP=True,no_body=True,no_whole_profile=True,no_Jacobian=True,no_speedup_claim=True)
    try:
        saved=load_npz(args.field);s=json.loads(args.run_report.read_text())['settings']
        candidate=Path(s['candidate']);radius=Path(s['radius_packet']);proof=json.loads(radius.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=identity(candidate)['sha256']:raise ValueError('Wrong actual base radius packet')
        witness=dict(**identity(radius),candidate_sha256=proof['candidate_sha256'])
        p=create_midpoint_refined_problem(candidate,saved_field=saved,split_cells=(),modes=int(saved['modes']),
            max_step=s['mesh_step'],gap=s['gap'],reference_inlet=Path(s['reference_inlet']),
            reference_cache=Path(s['reference_cache']),reference_rim_fraction=s['reference_rim_fraction'],
            minimum_active_n=s['minimum_active_n'],mesh_relative_tolerance=s['mesh_relative_tolerance'],
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=s['radius_floor'])
        before_identity=hashlib.sha256(saved['parameters'].tobytes()+saved['corrections'].tobytes()).hexdigest()
        chart,ref=p.chart,p.coast_reference;e,L=ref.entry_s,ref.length;f=e+L
        points=np.array([e+.17*L,e+.63*L,f+.1*(chart.exit_stop-f)])
        labels=np.array([.17,.53,1.12],np.longdouble);small_s=float(points[0]);near_s=np.nextafter(small_s,np.inf)
        base=chart.coordinates(points);w,ws=coast_window(points,e,L,p.reference_rim_fraction)
        active=(w!=0)|(ws!=0);base_ref=ref.jet_on_grid(points,base,active_mask=active)
        baseline_small=chart.coordinates([small_s],coordinate=labels)
        baseline_near=chart.coordinates([near_s],coordinate=labels)
        baseline_left=chart.coordinates([e],coordinate=labels,side='left')
        baseline_coast=chart.coordinates([e],coordinate=labels,side='coast')
        baseline_ruling=chart.ruling_jet(small_s,labels,include_native=False)
        baseline_seed=chart.original.reference.reference_coordinate(labels)
        handle=install_prepared_geometry_cache(p)
        first=chart.coordinates(points);first_ref=ref.jet_on_grid(points,first,active_mask=active)
        counts_first=handle.statistics()
        repeated=chart.coordinates(points);repeated_ref=ref.jet_on_grid(points,repeated,active_mask=active)
        counts_repeat=handle.statistics()
        original_delta=p.profile.coefficients.copy();delta1=saved['parameters'][p.profile_parameter_slice].copy()
        delta2=delta1+np.array([1,-2,3,-1,2,-3,1])*1e-5
        p.profile.set_parameters(delta1);target1=p.profile.jet(points)
        frozen1=chart.coordinates(points);ref1=ref.jet_on_grid(points,frozen1,active_mask=active)
        p.profile.set_parameters(delta2);target2=p.profile.jet(points)
        frozen2=chart.coordinates(points);ref2=ref.jet_on_grid(points,frozen2,active_mask=active)
        p.profile.set_parameters(original_delta)
        small=chart.coordinates([small_s],coordinate=labels)
        before_near=handle.statistics()['by_kind']['coordinates']['misses']
        near=chart.coordinates([near_s],coordinate=labels)
        after_near=handle.statistics()['by_kind']['coordinates']['misses']
        left=chart.coordinates([e],coordinate=labels,side='left')
        coast=chart.coordinates([e],coordinate=labels,side='coast')
        ruling=chart.ruling_jet(small_s,labels,include_native=False)
        ruling_again=chart.ruling_jet(small_s,labels,include_native=False)
        seed=chart.original.reference.reference_coordinate(labels)
        seed_again=chart.original.reference.reference_coordinate(labels)
        attempted_mutation_rejected=False
        try:repeated['u'][0,0]=0.
        except ValueError:attempted_mutation_rejected=True
        detached=chart.coordinates(points);detached.pop('u')
        container_survived='u' in chart.coordinates(points)
        view=copy.copy(p)
        changes=dict(original_vs_cached_coordinates=difference(base,first),
            original_vs_cached_reference=difference(base_ref,first_ref),
            repeated_coordinates=difference(first,repeated),repeated_reference=difference(first_ref,repeated_ref),
            different_delta_frozen_coordinates=difference(frozen1,frozen2),
            different_delta_frozen_reference=difference(ref1,ref2),
            different_actual_label_grid=difference(baseline_small,small),
            distinct_adjacent_binary_s=difference(baseline_near,near),
            left_side=difference(baseline_left,left),coast_side=difference(baseline_coast,coast),
            standalone_ruling=difference(baseline_ruling,ruling),repeated_ruling=difference(ruling,ruling_again),
            fixed_seed=difference(baseline_seed,seed),repeated_seed=difference(seed,seed_again))
        target_change={k:float(np.max(abs(target1[k]-target2[k]))) for k in ('a','a_s','a_ss','c','K')}
        statistics=handle.statistics()
        r.update(status='completed',dimensions=dict(raw=p.K,tail=p.tail_parameter_count,nodes=p.N,work=p.work),
            radial_points=points.tolist(),active_reference_mask=active.tolist(),actual_small_labels=[str(v) for v in labels],
            scalar_s_hex=small_s.hex(),distinct_adjacent_s_hex=float(near_s).hex(),
            original_vs_cached_maximum_differences=changes,
            actual_current_profile_changes_not_cached=target_change,
            distinct_side_radial_u_s_difference=float(np.max(abs(left['u_s']-coast['u_s']))),
            adjacent_binary_s_caused_a_new_cache_miss=after_near==before_near+1,
            exact_repetition_increased_coordinate_hits=counts_repeat['by_kind']['coordinates']['hits']>counts_first['by_kind']['coordinates']['hits'],
            exact_repetition_increased_reference_hits=counts_repeat['by_kind']['reference_point']['hits']>counts_first['by_kind']['reference_point']['hits'],
            cached_array_mutation_rejected=attempted_mutation_rejected,mapping_container_mutation_isolated=container_survived,
            copy_views_share_chart_and_reference=view.chart is chart and view.coast_reference is ref,
            repeated_install_returns_same_handle=install_prepared_geometry_cache(view) is handle,
            source_vector_bytes_unchanged=hashlib.sha256(saved['parameters'].tobytes()+saved['corrections'].tobytes()).hexdigest()==before_identity,
            definition=handle.definition(),statistics=statistics,
            verification_scope='Three full-grid radial points plus small label/side/adjacent-s queries; no whole residual or solver computation',
            forced_eviction_stress_run=False)
        r['passed']=bool(max(changes.values())==0. and target_change['a']>0 and target_change['K']>0
            and r['adjacent_binary_s_caused_a_new_cache_miss'] and attempted_mutation_rejected and container_survived
            and r['copy_views_share_chart_and_reference'] and r['repeated_install_returns_same_handle']
            and r['exact_repetition_increased_coordinate_hits'] and r['exact_repetition_increased_reference_hits']
            and statistics['within_byte_limit'] and statistics['original_reference_staging_entries']<=1
            and r['source_vector_bytes_unchanged'])
    except BaseException as exc:
        r.update(status='failed',exception_type=type(exc).__name__,exception=str(exc),traceback=traceback.format_exc())
        print(r['traceback'],flush=True)
    r['seconds']=time.monotonic()-started;r['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    r['sources_unchanged']=all(identity(here/n)['sha256']==v['sha256'] for n,v in source.items())
    if not r['sources_unchanged']:r['passed']=False
    dst=stem.with_name(stem.name+'-report.json');dst.write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=r['status'],passed=r['passed'],seconds=r['seconds'],peak_rss_kib=r['peak_rss_kib'],report=str(dst))),flush=True)
    return 0 if r['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
