#!/usr/bin/env python3
"""One streaming pointwise physical Gauss/Codazzi screen of an actual field.

Every original P1 cell is queried at its two Gauss2 points and midpoint,
on one fixed physical material-angle grid. Derivatives are true one-sided
native interpolant derivatives transformed to fixed u, never a solver RHS.
No Jacobian, BVP, body integration or continuous certificate is computed.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import json
import time
import resource
import traceback
import platform
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField, terminal_window_jets
from fd2d_gc_ruling_atlas_native_field import RulingAtlasRawBumpNativeField
from fd2d_gc_bump_coast_native_field import window
from fd2d_gc_three_field_residual import native_residuals


def maximum(x):
    return float(np.max(abs(np.asarray(x)),initial=0.))


def scalar(x,index=0):
    a=np.asarray(x)
    return float(a.reshape(-1)[index]) if a.size else None


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field',type=Path,required=True)
    ap.add_argument('--run-report',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--angles',type=int,default=128)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh screen output stem')
    if args.angles<64 or args.angles%4:
        raise ValueError('Use a recorded uniform angular grid divisible by four')
    start=time.monotonic();here=Path(__file__).resolve().parent
    source_names=('fd2d-metric-physical-differential-screen.py','fd2d_gc_positive_trace_native_field_v2.py',
        'fd2d_gc_positive_gauss_l_native_field.py','fd2d_gc_ruling_atlas_native_field.py',
        'fd2d_gc_three_field_residual.py')
    sources={name:identity(here/name) for name in source_names}
    report=dict(schema='fd2d-actual-physical-pointwise-Gauss-Codazzi-screen-v1',
        source=sources,input_field=identity(args.field),source_run_report=identity(args.run_report),
        status='running',execution_complete=False,all_requested_points_defined=False,
        finite_sampling_only=True,continuous_certificate=False,no_Jacobian=True,no_BVP=True,no_body=True,
        representation_changed=False,physical_g_changed=False,
        versions=dict(python=platform.python_version(),numpy=np.__version__),
        actual_residuals=dict(G='n*l-m*m-K',Rn='n_s-m_u/a-(a_s/a)*(l-n)',
            Rm='m_s-l_u/a+2*(a_s/a)*m',K='-a_ss/a'),
        derivatives='True saved P1 and complete lifting/nonlinear native jets, transformed by (partial_x-U_x/U_xi*partial_xi)/J at fixed physical u',
        not_solver_integrated_objective=True)
    progress_path=stem.with_name(stem.name+'-progress.jsonl')
    try:
        previous=json.loads(args.run_report.read_text());settings=previous['settings']
        reader=PositiveTraceNativeField(args.field,Path(settings['candidate']),
            reference_inlet=Path(settings['reference_inlet']),reference_cache=Path(settings['reference_cache']))
        if report['input_field']['sha256']!='d2c538f65b10f0ea6262d5e831efd17c80116ca958fd6634a9cbb831fac57bfc':
            raise ValueError('This diagnostic is explicitly bound to the closed 18 b4 accepted2 state')
        report['actual_input_scope']='18 b4 accepted2 immutable field; not the later 19/20 working state'
        report['candidate']=identity(Path(settings['candidate']))
        report['representation_kind']=reader.representation_kind
        ncell=len(reader.nodes)-1;W=args.angles
        g,wg=np.polynomial.legendre.leggauss(2);g=(g+1)/2
        fractions=np.array([g[0],.5,g[1]])
        u=2*np.pi*np.arange(W)/W
        report['sampling']=dict(original_nodes=len(reader.nodes),original_cells=ncell,
            radial_labels=['gauss_left','midpoint','gauss_right'],radial_fractions=fractions.tolist(),
            fraction_binary_hex=[float(x).hex() for x in fractions],angle_count=W,
            physical_u_formula='2*pi*j/W, j=0,...,W-1',radial_side='right at any coincident internal physical definition boundary',
            all_samples_strictly_inside_saved_P1_cells=True,angular_intervals_certified=False)
        names=('G','Rn','Rm','connection_operator_norm')
        points=np.empty((ncell,3));residuals=np.zeros((ncell,3,W,3));valid=np.zeros((ncell,3,W),bool)
        point_max=np.zeros((ncell,3,4));argmax=np.full((ncell,3,4),-1,int)
        point_rms=np.zeros((ncell,3,4));target=np.empty((ncell,3,4))
        field_ranges=np.zeros((ncell,3,7))
        global_peaks={name:None for name in names};failures=[];cells=[]
        maximum_inverse_error=0.;complete_cells=0
        ref=reader.coast_reference
        for cell,(left,right) in enumerate(zip(reader.nodes[:-1],reader.nodes[1:])):
            for ri,fraction in enumerate(fractions):
                s=float(left+(right-left)*fraction);points[cell,ri]=s
                if not left<s<right:
                    raise ArithmeticError('A requested interior sample rounded onto a saved P1 node')
                xi=reader.invert_angle(s,u)
                try:
                    q=reader.evaluate_native(s,xi,side='right')
                    ids=np.arange(W)
                except FloatingPointError as exc:
                    # Preserve and identify a real unrepresented domain;
                    # do not replace it by zeros or silently relax the saved
                    # positive-n evaluation floor.
                    raw=RulingAtlasRawBumpNativeField.evaluate_native(reader,s,xi,side='right')
                    cw,_=window(s,ref.entry_s,ref.length,reader.reference_rim_fraction)
                    rejected=(raw['n']<=reader.minimum_active_n) if cw>0 else np.ones(W,bool)
                    failures.append(dict(cell=cell,radial_index=ri,s=s,exception_type=type(exc).__name__,
                        exception=str(exc),physical_angle_indices=np.flatnonzero(rejected).tolist(),
                        raw_n_at_rejected=np.asarray(raw['n'])[rejected].tolist(),
                        saved_finite_floor=reader.minimum_active_n,
                        mathematical_nonpositive_n=bool(np.any(np.asarray(raw['n'])[rejected]<=0.))))
                    ids=np.flatnonzero(~rejected)
                    if not len(ids):
                        jet=reader.profile.jet([s]);target[cell,ri]=[jet[k][0] for k in ('a','a_s','a_ss','K')]
                        continue
                    q=reader.evaluate_native(s,xi[ids],side='right')
                if not np.all(np.asarray(q['cell'])==cell):
                    raise ArithmeticError('Native evaluation used the wrong actual defining P1 cell')
                query_error=maximum(q['u']-u[ids]);maximum_inverse_error=max(maximum_inverse_error,query_error)
                fields=('a','a_s','a_ss','l','m','n','J','U_x','U_xi','l_xi','m_xi','n_xi','m_x','n_x')
                out=native_residuals(**{key:q[key] for key in fields})
                v=np.stack([out[name] for name in names],axis=-1)
                if not np.all(np.isfinite(v)):
                    raise FloatingPointError('Nonfinite actual physical residual')
                residuals[cell,ri,ids]=v[:,:3];valid[cell,ri,ids]=True
                target[cell,ri]=[scalar(q['a']),scalar(q['a_s']),scalar(q['a_ss']),-scalar(q['a_ss'])/scalar(q['a'])]
                disc=np.hypot(q['n']-q['l'],2*q['m'])
                kappa=np.maximum(abs(q['n']+q['l']+disc),abs(q['n']+q['l']-disc))/2
                field_ranges[cell,ri]=[np.min(q['n']),np.max(q['n']),np.min(q['m']),np.max(q['m']),np.min(q['l']),np.max(q['l']),np.max(kappa)]
                base=reader.profile.base;piece_index=int(np.clip(np.searchsorted(base.breaks,s,side='right')-1,0,len(base.segments)-1))
                piece=base.segments[piece_index]
                cw,cws=window(s,ref.entry_s,ref.length,reader.reference_rim_fraction)
                tw,tws=terminal_window_jets(s,reader.trace_start,reader.trace_ramp_stop)
                physical=out['physical_jets']
                for ci,name in enumerate(names):
                    local_index=int(np.argmax(abs(v[:,ci])));j=int(ids[local_index]);height=float(abs(v[local_index,ci]))
                    point_max[cell,ri,ci]=height;argmax[cell,ri,ci]=j
                    point_rms[cell,ri,ci]=float(np.sqrt(np.mean(v[:,ci]**2)))
                    if global_peaks[name] is None or height>global_peaks[name]['absolute_value']:
                        a,ap,app=(scalar(q[key],local_index) for key in ('a','a_s','a_ss'))
                        n,m,l=(scalar(q[key],local_index) for key in ('n','m','l'))
                        c=ap/a;K=-app/a
                        ns,ms,mu,lu=(scalar(physical[key],local_index) for key in ('n_s','m_s','m_u','l_u'))
                        global_peaks[name]=dict(absolute_value=height,signed_value=float(v[local_index,ci]),
                            cell=cell,cell_left=float(left),cell_right=float(right),cell_width=float(right-left),
                            radial_label=report['sampling']['radial_labels'][ri],radial_fraction=float(fraction),
                            physical_s=s,physical_u=float(u[j]),angle_index=j,native_xi=float(xi[j]),
                            inverse_error=float(q['u'][local_index]-u[j]),
                            actual_II=dict(n=n,m=m,l=l),actual_target=dict(a=a,a_s=ap,a_ss=app,K=K),
                            actual_physical_first=dict(n_s=ns,m_s=ms,m_u=mu,l_u=lu),
                            decomposition=dict(nl=n*l,m_squared=m*m,K=K,
                                Rn_n_s=ns,Rn_m_u_over_a=mu/a,Rn_connection=c*(l-n),
                                Rm_m_s=ms,Rm_l_u_over_a=lu/a,Rm_connection=2*c*m),
                            base_piece=dict(index=piece_index,kind=piece['kind'],left=float(piece['s0']),right=float(piece['s0']+piece['L'])),
                            coast_weight=float(cw),coast_weight_s=float(cws),terminal_weight=float(tw),terminal_weight_s=float(tws))
            gauss_max=np.max(point_max[cell,[0,2]],axis=0);mid=point_max[cell,1]
            width=float(right-left)
            summary=dict(cell=cell,left=float(left),right=float(right),width=width,
                maximum_abs={name:float(np.max(point_max[cell,:,ci])) for ci,name in enumerate(names)},
                G2_point_maximum_abs={name:float(gauss_max[ci]) for ci,name in enumerate(names)},
                midpoint_maximum_abs={name:float(mid[ci]) for ci,name in enumerate(names)},
                midpoint_excess_over_G2={name:float(max(0.,mid[ci]-gauss_max[ci])) for ci,name in enumerate(names)},
                sampled_connection_width_proxy=width*float(np.max(point_max[cell,:,3])),
                proxy_is_not_an_integral_bound=True,defined_points=int(np.count_nonzero(valid[cell])),requested_points=3*W)
            cells.append(summary)
            if np.all(valid[cell]):complete_cells+=1
            with progress_path.open('a') as handle:
                handle.write(json.dumps(summary,allow_nan=False)+'\n')
            if cell%16==0 or cell==ncell-1:
                print(json.dumps(dict(event='cell_complete',cell=cell,total=ncell,seconds=time.monotonic()-start,
                    maxima={key:None if row is None else row['absolute_value'] for key,row in global_peaks.items()})),flush=True)
        # The prefix-side radial II cut trace is intentionally not assigned
        # by this native definition. Query only its actual angular trace.
        cut=reader.physical_angular(reader.trace_cut,u)
        cutG=cut['n']*cut['l']-cut['m']**2+cut['a_ss']/cut['a']
        zero=np.all(np.stack([cut[name] for name in ('n','m','l')],axis=-1)==0.,axis=-1)
        tail=reader.tail.cut_port(u)
        cut_tail_error=max(maximum(cut[name]-tail[name]) for name in ('n','m','l'))
        scope=dict(exact_cut_queried_for='actual values/angular jets and pointwise Gauss only',
            prefix_cut_Rn_Rm='not assigned: exact cut radial II trace is not certified by this reader',
            exact_cut_G_maximum=maximum(cutG),exact_cut_zero_II_angle_count=int(np.count_nonzero(zero)),
            exact_cut_tail_value_difference=cut_tail_error,
            zero_tail_II_angles_do_not_require_division_by_n=True,
            interfaces=[float(x) for x in (reader.angular_atlas_definition['entry_transition'][0],
                ref.entry_s,ref.exit_s,reader.angular_atlas_definition['exit_transition'][1],
                reader.trace_start,reader.trace_ramp_stop,reader.trace_cut)],
            all_saved_P1_cells_sampled_in_their_interiors=True,
            P1_and_atlas_radial_jumps_not_replaced_by_common_traces=True,
            no_global_C3_requirement=True)
        definition_path=stem.with_name(stem.name+'-definition.json')
        definition=reader.definition();definition_path.write_text(json.dumps(definition,indent=2,allow_nan=False)+'\n')
        sample_id=save_npz(stem.with_name(stem.name+'-samples.npz'),
            mesh=reader.nodes,radial_points=points,radial_fractions=fractions,physical_u=u,
            residuals_G_Rn_Rm=residuals,defined_mask=valid,point_maxima_G_Rn_Rm_connection=point_max,
            point_argmax_angle=argmax,point_angular_rms=point_rms,
            target_a_as_ass_K=target,field_ranges_nmin_nmax_mmin_mmax_lmin_lmax_formalkappamax=field_ranges,
            cut_G=cutG,cut_zero_II_mask=zero)
        top={name:sorted(cells,key=lambda row:row['maximum_abs'][name],reverse=True)[:8] for name in names}
        excess={name:sorted(cells,key=lambda row:row['midpoint_excess_over_G2'][name],reverse=True)[:8] for name in names}
        report.update(status='completed' if np.all(valid) else 'completed_with_undefined_samples',
            execution_complete=True,all_requested_points_defined=bool(np.all(valid)),
            requested_points=int(valid.size),defined_points=int(np.count_nonzero(valid)),complete_cells=complete_cells,
            maximum_inverse_error=maximum_inverse_error,global_peaks=global_peaks,
            top_cells_by_component=top,top_midpoint_excess_cells=excess,
            cell_summaries=cells,domain_failures=failures,cut_and_interface_scope=scope,
            samples=sample_id,definition=identity(definition_path),
            zero_fill_for_undefined_storage='Residual storage is zero only where defined_mask is false; such values are not residual observations',
            prior_solver_report_scope='Original source report is provenance only; its fixed-xi node/integral norms are not a same-angle-grid comparison',
            adaptive_interpretation='Use actual locations and midpoint-vs-G2 differences to choose future cells; these sampled peaks and width proxies are not continuous bounds or new acceptance gates')
        report['all_definition_sources_unchanged']=all(identity(Path(item['path']))['sha256']==item['sha256'] for item in definition['sources'])
    except BaseException as exc:
        report.update(status='failed',exception_type=type(exc).__name__,exception=str(exc),traceback=traceback.format_exc())
        print(report['traceback'],flush=True)
    report['seconds']=time.monotonic()-start;report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['screen_sources_unchanged']=all(identity(here/name)['sha256']==row['sha256'] for name,row in sources.items())
    finished=report['execution_complete'] and report['all_requested_points_defined'] and report['screen_sources_unchanged'] and report.get('all_definition_sources_unchanged',False)
    report['complete_finite_screen']=bool(finished)
    destination=stem.with_name(stem.name+'-report.json')
    destination.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='physical_differential_screen_complete',status=report['status'],complete=finished,
        seconds=report['seconds'],report=str(destination))),flush=True)
    return 0 if finished else 1


if __name__=='__main__':
    raise SystemExit(main())
