"""One balanced nonzero state/tail/profile JVP for grouped coast quadrature."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import resource
import time
import traceback
import numpy as np
from scipy import sparse

from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem
from fd2d_gc_positive_trace_stream_normal import radial_view
from fd2d_gc_grouped_coast_codazzi import gauss_cell_positive_trace_grouped_coast


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field',type=Path,required=True)
    ap.add_argument('--run-report',type=Path,required=True)
    ap.add_argument('--previous-witness',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a new closed stem')
    started=time.monotonic();here=Path(__file__).resolve().parent
    names=[Path(__file__).name,'fd2d_gc_grouped_coast_codazzi.py',
        'fd2d_gc_midpoint_refined_positive_trace_v3.py','fd2d_gc_positive_trace_stream_normal.py',
        'fd2d_gc_gauss_cell_frozen_operator_compatible.py','fd2d_gc_frozen_operator_projections.py',
        'fd2d_gc_gauss_cell_positive_trace.py','fd2d_gc_hybrid_lifting_codazzi_d2.py',
        'fd2d_gc_positive_gauss_l.py','fd2d_gc_codazzi_complement.py',
        'fd2d_gc_d2_complements.py','fd2d_gc_raw_bump_ruling_atlas.py',
        'fd2d_gc_frozen_ruling_atlas.py','fd2d_gc_raw_bump_positive_trace.py']
    sources={n:identity(here/n) for n in names}
    r=dict(schema='fd2d-actual-grouped-coast-single-balanced-JVP-v1',status='running',passed=False,
        sources=sources,input_field=identity(args.field),input_run_report=identity(args.run_report),
        old_four_cell_witness=identity(args.previous_witness),no_whole_J=True,no_BVP=True,no_body=True,
        no_continuous_certificate=True,original_affine_R152_not_rechecked=True)
    arrays={}
    try:
        if r['input_field']['sha256']!='a485ca86233a196223f16fc2f9c01b7cf3592ae5499d9a04fd94bd7f2511e81e':
            raise ValueError('Use immutable23b3')
        a=load_npz(args.field);old=json.loads(args.run_report.read_text());s=old['settings']
        candidate=Path(s['candidate']);radius=Path(s['radius_packet']);proof=json.loads(radius.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=identity(candidate)['sha256']:
            raise ValueError('Wrong base radius packet')
        witness=dict(**identity(radius),candidate_sha256=proof['candidate_sha256'])
        problem=create_midpoint_refined_problem(candidate,saved_field=a,split_cells=(),modes=int(a['modes']),
            max_step=s['mesh_step'],gap=s['gap'],reference_inlet=Path(s['reference_inlet']),
            reference_cache=Path(s['reference_cache']),reference_rim_fraction=s['reference_rim_fraction'],
            minimum_active_n=s['minimum_active_n'],mesh_relative_tolerance=s['mesh_relative_tolerance'],
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=s['radius_floor'])
        cell=64;view=radial_view(problem,[cell,cell+1])
        z=np.r_[a['corrections'][cell:cell+2].ravel(),a['parameters']]
        original_bytes=hashlib.sha256(z.tobytes()).hexdigest()
        result=gauss_cell_positive_trace_grouped_coast(view,z,jacobian=True)
        J=sparse.vstack((result['retained_jacobian'],result['high_jacobian']),format='csc')
        residual=np.r_[result['retained_residual'],result['high_residual']]
        offset=2*view.q
        state=np.zeros_like(z);tail=np.zeros_like(z);profile=np.zeros_like(z)
        state[31]=.4;state[view.e+30]=-.3;state[view.d+31]=.2
        state[view.q+2]=-.15;state[view.q+view.e+1]=.17;state[view.q+view.d+4]=-.11
        for j,v in [(31,.17),(35,-.12),(38,.1),(42,-.2),(46,.2)]:tail[offset+j]=v
        profile[offset+view.profile_parameter_slice.start:offset+view.profile_parameter_slice.stop]=[.12,-.17,.21,-.13,.14,.18,-.11]
        groups={'state':state,'tail':tail,'physical_profile':profile};norms={};balanced={}
        for name,direction in groups.items():
            action=np.asarray(J@direction);norm=float(np.linalg.norm(action))
            if not norm>1e-10:raise ValueError('The declared direction has no real action: '+name)
            norms[name]=norm;balanced[name]=direction/norm
            arrays[name+'_unscaled_action']=action
        direction=sum(balanced.values());analytic=np.asarray(J@direction)
        step=1e-6
        def value(v):
            packet=gauss_cell_positive_trace_grouped_coast(view,v,jacobian=False)
            return np.r_[packet['retained_residual'],packet['high_residual']]
        plus=value(z+step*direction);minus=value(z-step*direction)
        difference=(plus-minus)/(2*step)
        error=difference-analytic
        relative_l2=float(np.linalg.norm(error)/max(np.linalg.norm(analytic),np.finfo(float).tiny))
        relative_max=float(np.max(abs(error))/max(np.max(abs(analytic)),np.finfo(float).tiny))
        with np.load(args.previous_witness,allow_pickle=False) as oldw:
            old_full=oldw['cell64_saved_full'].copy()
            isolated=oldw['cell64_hypothetical_full'].copy()
        actual=result['full_codazzi_cells'][:,0]
        row_projection=np.r_[view.PE@actual[:,0],view.PO@actual[:,1]]
        decomposition=np.stack((view.E@result['retained_cells'][0,:view.e],
                                view.O@result['retained_cells'][0,view.e:]),axis=-1)+result['omitted_codazzi_cells'][:,0]
        r.update(status='completed',cell=cell,endpoints=view.x.tolist(),
            dimensions=dict(raw=problem.K,tail=problem.tail_parameter_count,parameters=problem.parameter_count,
                            global_nodes=problem.N,local_nodes=2,work=problem.work),
            nonzero_balanced_component_action_norms={k:float(np.linalg.norm(J@v)) for k,v in balanced.items()},
            unscaled_component_action_norms=norms,direction_definition={k:np.flatnonzero(v).tolist() for k,v in groups.items()},
            finite_difference_step=step,analytic_action_l2=float(np.linalg.norm(analytic)),
            finite_difference_action_l2=float(np.linalg.norm(difference)),
            relative_l2_error=relative_l2,relative_maximum_error=relative_max,
            absolute_error_maximum=float(np.max(abs(error))),
            retained_projection_difference=float(np.max(abs(row_projection-result['retained_residual']))),
            full_low_high_decomposition_difference=float(np.max(abs(actual-decomposition))),
            old_saved_full_maxima=np.max(abs(old_full),axis=0).tolist(),
            isolated_delta_only_refinement_full_maxima=np.max(abs(isolated),axis=0).tolist(),
            grouped_whole_actual_fine_full_maxima=np.max(abs(actual),axis=0).tolist(),
            grouped_retained_maximum=float(np.max(abs(result['retained_residual']))),
            grouped_omitted_sampled_maximum=float(np.max(abs(result['omitted_codazzi_cells']))),
            original_G2_point_gauss_shape=list(result['point_gauss'].shape),
            original_G2_diagnostic_points=result['quadrature_points'].tolist(),
            info=result['info'],source_vector_bytes_unchanged=original_bytes==hashlib.sha256(z.tobytes()).hexdigest(),
            scope='One cell crossing the saved left coast plateau endpoint, one balanced direction with nonzero raw state, independent tail and physical-profile actions; no global Jacobian or main solve')
        arrays.update(local_vector=z,direction=direction,analytic_action=analytic,finite_difference_action=difference,
            plus_residual=plus,minus_residual=minus,baseline_residual=residual,
            grouped_full=actual,old_saved_full=old_full,isolated_delta_only_full=isolated,
            grouped_omitted=result['omitted_codazzi_cells'][:,0],grouped_retained=result['retained_cells'][0])
        r['arrays']=save_npz(stem.with_name(stem.name+'-witnesses.npz'),**arrays)
        r['passed']=bool(relative_l2<1e-5 and relative_max<1e-5 and r['source_vector_bytes_unchanged']
                         and r['retained_projection_difference']<1e-8
                         and r['full_low_high_decomposition_difference']<1e-8)
    except BaseException as exc:
        r.update(status='failed',exception_type=type(exc).__name__,exception=str(exc),traceback=traceback.format_exc())
        print(r['traceback'],flush=True)
    r['seconds']=time.monotonic()-started;r['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    r['sources_unchanged']=all(identity(here/n)['sha256']==v['sha256'] for n,v in sources.items())
    if not r['sources_unchanged']:r['passed']=False
    path=stem.with_name(stem.name+'-report.json');path.write_text(json.dumps(r,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=r['status'],passed=r['passed'],seconds=r['seconds'],
        relative_l2_error=r.get('relative_l2_error'),grouped_maxima=r.get('grouped_whole_actual_fine_full_maxima'),report=str(path))),flush=True)
    return 0 if r['passed'] else 1


if __name__=='__main__':raise SystemExit(main())
