#!/usr/bin/env python3
"""Small actual combined R153/R155 field check, without BVP or body ODE."""
from __future__ import annotations
import argparse,json,resource,time
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,save_npz
from fd2d_gc_positive_gauss_l_native_field import physical_profile_third
from fd2d_gc_positive_trace_branch import positive_trace_delta
from fd2d_gc_positive_trace_native_field_v2 import (
    PositiveTraceNativeField,terminal_window_jets,positive_trace_native_jets)


def packed(q,suffix=''):
    return np.stack([q[name+suffix] for name in ('n','m','l')],axis=-1)


def maximum(value):return float(np.max(abs(value),initial=0.))


def error(got,expected):
    d=np.asarray(got)-np.asarray(expected)
    return dict(absolute_maximum=maximum(d),scaled_maximum=maximum(d)/max(1.,maximum(expected)))


def json_scalar(value):
    if isinstance(value,np.ndarray):return value.tolist()
    if isinstance(value,np.integer):return int(value)
    if isinstance(value,np.floating):return float(value)
    raise TypeError(type(value).__name__)


def write_json(path,value):
    path.write_text(json.dumps(value,indent=2,allow_nan=False,default=json_scalar)+'\n')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('field','candidate','inlet','cache','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a new native check prefix')
    here=Path(__file__).resolve().parent
    sources=[identity(here/name) for name in ('fd2d-metric-positive-trace-native-check-v2.py',
        'fd2d_gc_positive_trace_native_field_v2.py','fd2d_gc_positive_trace_branch.py',
        'fd2d_gc_raw_bump_positive_trace.py','fd2d_gc_positive_gauss_l_native_field.py')]
    input_identity=identity(args.field)
    r=PositiveTraceNativeField(args.field,args.candidate,
        reference_inlet=args.inlet,reference_cache=args.cache)
    indices=np.array([0,5,17,31,53,64,89,123]);xi=np.asarray(r.angular_atlas.theta[indices],float)
    point_labels=('terminal_rim','terminal_plateau')
    points=[(r.trace_start+r.trace_ramp_stop)/2,(r.trace_ramp_stop+r.trace_cut)/2]
    # Retain the same literal query if interior. Otherwise select the
    # midpoint of its actual saved P1 cell, never change the field mesh.
    for i,x in enumerate(points):
        if x in r.nodes:
            j=int(np.searchsorted(r.nodes,x,side='right')-1)
            points[i]=float((r.nodes[j]+r.nodes[j+1])/2)
    boundaries=np.unique(np.r_[r.nodes,r.profile.breaks,r.trace_start,r.trace_ramp_stop,r.trace_cut])
    rows=[];samples={};helper_error=0.;same_m=0.;d_error=0.;angular_error=0.;gauss_error=0.;Ks_contribution=0.
    for i,(label,x) in enumerate(zip(point_labels,points)):
        bg=r.evaluate_coast_native(x,xi);q=r.evaluate_native(x,xi)
        angular=r.evaluate_angular_native(x,xi)
        if any(key in angular for key in ('n_x','l_x','n_x_xi','l_x_xi')):
            raise ArithmeticError('Angular query carried stale changed radial jets')
        for suffix in ('','_xi','_xixi'):
            angular_error=max(angular_error,maximum(packed(angular,suffix)-packed(q,suffix)))
        for suffix in ('','_x','_xi','_xixi','_x_xi'):
            same_m=max(same_m,maximum(q['m'+suffix]-bg['m'+suffix]))
            d_error=max(d_error,maximum((q['n'+suffix]-q['l'+suffix])-(bg['n'+suffix]-bg['l'+suffix])))
            samples[f'point_{i}{suffix}']=packed(q,suffix)
            samples[f'background_{i}{suffix}']=packed(bg,suffix)
        w,ws=terminal_window_jets(x,r.trace_start,r.trace_ramp_stop)
        K=-bg['a_ss']/bg['a'];D=positive_trace_delta(packed(bg),packed(bg,'_xi'),K,w)
        helper_error=max(helper_error,maximum(D['actual']-packed(q)),maximum(D['actual_angular']-packed(q,'_xi')))
        G0=bg['n']*bg['l']-bg['m']**2-K
        G=q['n']*q['l']-q['m']**2-K
        predicted=(1-w)*G0-w*(1-w)*(D['h']-bg['n']-bg['l'])**2/4
        gauss_error=max(gauss_error,maximum(G-predicted))
        third=float(physical_profile_third(r.profile,[x])[0])
        Ks=-third/bg['a']+bg['a_ss']*bg['a_s']/bg['a']**2
        without=positive_trace_native_jets(bg,w,ws,K_s=np.zeros_like(Ks))
        Kterm=w*Ks/D['h'];Ks_contribution=max(Ks_contribution,maximum(Kterm))
        difference=error(q['n_x']-without['n_x'],Kterm)
        distance=float(np.min(abs(boundaries-x)))
        if distance==0.:raise ValueError('Derivative sample must be inside an actual P1 cell')
        step=min(2e-6,distance/8)
        finite=[]
        for h in (step,step/2):
            xp,xm=r.evaluate_native(x+h,xi),r.evaluate_native(x-h,xi)
            up,um=r.evaluate_native(x,xi+h),r.evaluate_native(x,xi-h)
            finite.append(dict(step=h,
                x=error((packed(xp)-packed(xm))/(2*h),packed(q,'_x')),
                xi=error((packed(up)-packed(um))/(2*h),packed(q,'_xi')),
                xixi=error((packed(up,'_xi')-packed(um,'_xi'))/(2*h),packed(q,'_xixi')),
                x_xi_from_x=error((packed(xp,'_xi')-packed(xm,'_xi'))/(2*h),packed(q,'_x_xi')),
                x_xi_from_xi=error((packed(up,'_x')-packed(um,'_x'))/(2*h),packed(q,'_x_xi'))))
        pu=r.physical_angular(x,q['u']);full=r.physical(x,q['u'])
        chains={suffix or 'value':maximum(packed(pu,suffix)-packed(full,suffix))
                for suffix in ('','_u','_uu')}
        rows.append(dict(label=label,physical_s=float(x),weight=float(w),weight_s=float(ws),
            K=float(K[0]),K_s=float(Ks[0]),minimum_actual_h=float(np.min(D['h'])),
            sampled_actual_n_minimum=float(np.min(q['n'])),sampled_actual_l_minimum=float(np.min(q['l'])),
            sampled_actual_Gauss_maximum=maximum(G),
            nonzero_K_s_contribution=maximum(Kterm),K_s_radial_witness=difference,
            finite_difference_checks=finite,physical_angular_vs_full=chains))
    # The terminal map is exactly inactive in the coast and an intervening
    # exterior interval. The actual R153 nonlinear coast remains in place.
    outside=[];outside_error=0.
    for label,x in (('coast',(r.coast_reference.entry_s+r.coast_reference.exit_s)/2),
                    ('between_windows',(r.coast_reference.exit_s+r.trace_start)/2)):
        bg=r.evaluate_coast_native(x,xi);q=r.evaluate_native(x,xi)
        d=max(maximum(packed(bg,suffix)-packed(q,suffix)) for suffix in ('','_x','_xi','_xixi','_x_xi'))
        outside_error=max(outside_error,d);outside.append(dict(label=label,physical_s=x,all_five_jet_difference=d))
    cut=r.evaluate_angular_native(r.trace_cut,xi)
    cutbg=r.evaluate_coast_angular_native(r.trace_cut,xi)
    cuterror=max(maximum(packed(cut,suffix)-packed(cutbg,suffix)) for suffix in ('','_xi','_xixi'))
    cutphysical=r.physical_angular(r.trace_cut,cut['u'])
    cutphysicalerror=maximum(packed(cutphysical)-packed(cut))
    zero_tail=int(np.count_nonzero((cut['n']==0.)&(cut['m']==0.)&(cut['l']==0.)))
    radial_cut_rejected=False
    try:r.evaluate_native(r.trace_cut,xi)
    except ValueError as exc:
        radial_cut_rejected='radial II jets are not claimed' in str(exc)
    definition=stem.with_name(stem.name+'-definition.json');write_json(definition,r.definition())
    restored=PositiveTraceNativeField.from_definition(definition)
    reload=0.
    for i,x in enumerate(points):
        q=restored.evaluate_native(x,xi)
        for suffix in ('','_x','_xi','_xixi','_x_xi'):
            reload=max(reload,maximum(packed(q,suffix)-samples[f'point_{i}{suffix}']))
    samples.update(xi=xi,physical_s=np.array(points),angular_indices=indices,
        cut_values=packed(cut),cut_xi=packed(cut,'_xi'),cut_xixi=packed(cut,'_xixi'))
    sampleid=save_npz(stem.with_name(stem.name+'-samples.npz'),**samples)
    fine=max(row['finite_difference_checks'][-1][key]['scaled_maximum'] for row in rows
        for key in ('x','xi','xixi','x_xi_from_x','x_xi_from_xi'))
    physicalmax=max(v for row in rows for v in row['physical_angular_vs_full'].values())
    checks=dict(actual_interior_spatial_jets=fine<5e-5,
        frozen_helper_value_and_angle=helper_error<1e-10,
        actual_d_invariant_all_five_jets=d_error<1e-9,actual_m_unchanged=same_m==0.,
        angular_only_matches=angular_error==0.,actual_Gauss_window_identity=gauss_error<1e-10,
        real_K_s_used=Ks_contribution>1e-6 and max(row['K_s_radial_witness']['scaled_maximum'] for row in rows)<1e-9,
        physical_angular_chains=physicalmax<1e-9,
        prior_coast_and_exterior_unchanged=outside_error==0.,
        exact_cut_angular_trace_retained=cuterror==0. and cutphysicalerror<1e-10,
        zero_tail_handled_without_square_root_derivative=zero_tail>0,
        cut_radial_jet_not_fabricated=radial_cut_rejected,
        definition_reload=reload==0.,input_unchanged=identity(args.field)==input_identity,
        sources_unchanged=all(identity(row['path'])['sha256']==row['sha256'] for row in sources))
    report=dict(schema='fd2d-R155-actual-combined-native-small-check-v1',actual_execution=True,
        passed=all(checks.values()),checks=checks,sources=sources,input=input_identity,
        candidate=identity(args.candidate),inlet=identity(args.inlet),cache=identity(args.cache),
        angular_indices=indices.tolist(),point_queries=rows,outside_queries=outside,
        maximum_fine_fd_scaled_error=fine,helper_difference=helper_error,difference_invariant_error=d_error,
        unchanged_m_error=same_m,angular_only_error=angular_error,Gauss_identity_error=gauss_error,
        actual_K_s_contribution=Ks_contribution,
        exact_cut=dict(s=r.trace_cut,angular_twojet_difference=cuterror,physical_value_difference=cutphysicalerror,
            zero_matrix_samples=zero_tail,radial_jet_fabrication_rejected=radial_cut_rejected,
            interior_to_cut_angular_second_continuity_certified=False),
        definition_reload_difference=reload,definition=identity(definition),samples=sampleid,
        BVP_run=False,body_integration_run=False,Jacobian_assembled=False,
        continuous_residual_certificate=False,continuous_endpoint_regularity_certificate=False,
        closed_surface_certificate=False,additional_C3_completion_requirement=False,
        seconds=time.monotonic()-start,maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    output=stem.with_name(stem.name+'-report.json');write_json(output,report)
    print(json.dumps(dict(report=identity(output),passed=report['passed'],checks=checks,
        fine_fd_scaled_error=fine,K_s_contribution=Ks_contribution,
        seconds=report['seconds'],maximum_rss_kib=report['maximum_rss_kib']),allow_nan=False),flush=True)
    raise SystemExit(0 if report['passed'] else 1)


if __name__=='__main__':main()
