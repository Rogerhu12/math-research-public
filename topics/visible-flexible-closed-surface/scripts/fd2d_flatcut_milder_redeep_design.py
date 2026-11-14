#!/usr/bin/env python3
"""Generate two NEW flat-cut metrics with a milder redeepening phase.

The v1 metric is kept unchanged.  Only the explicitly listed physical phase
parameters change.  There is no linear DN root or claimed nonlinear solution.
This generator can run in CI using only inputs already published on main.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,hashlib,json,math,time
from pathlib import Path
import numpy as np
from fd2d_flat_cut_prefix_candidate import FlatCutCandidate,fm
from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def alter(source,*,redeepen_curvature=4.5,vmid=.12,ramp=.02,
          brake_length=.026,cylinder=.4,coast=.04):
    b=copy.deepcopy(source)
    rows=b['segments']
    ids={q.get('label'):j for j,q in enumerate(rows)}
    ie,ip,ix=[ids[x] for x in ('partial_return_acceleration_entry',
        'partial_return_acceleration_plateau','partial_return_acceleration_exit')]
    previous=rows[ie-1]
    if previous['kind']!='hermite' or 'jet1' not in previous:
        raise ValueError("This design binds the published shared-jet inlet")
    jet=previous['jet1']
    phi0=math.asin(jet[1]);ps0=jet[2]/math.cos(phi0)
    contraction_curvature=float(b['flat_cut_design']['contraction_curvature'])
    phi1=-math.asin(vmid)
    entry_end=phi0+ramp*(ps0-contraction_curvature)/2
    exit_start=phi1+contraction_curvature*ramp/2
    plateau=(entry_end-exit_start)/contraction_curvature
    if plateau<=0:raise ValueError("Nonpositive contraction plateau")
    rows[ie]=dict(kind='phase_bridge',p0=phi0,p1=entry_end,L=ramp,
        ps0=ps0,ps1=-contraction_curvature,start_from_previous=True,
        start_second_from_previous=True,label='partial_return_acceleration_entry')
    rows[ip]=dict(kind='phase_bridge',p0=entry_end,p1=exit_start,L=plateau,
        ps0=-contraction_curvature,ps1=-contraction_curvature,start_from_previous=True,
        label='partial_return_acceleration_plateau')
    rows[ix]=dict(kind='phase_bridge',p0=exit_start,p1=phi1,L=ramp,
        ps0=-contraction_curvature,ps1=0.,start_from_previous=True,
        label='partial_return_acceleration_exit')
    early=rows[ids['early_shallow_return']]
    early.update(p0=phi1,p1=-.1,K=3.4,L=abs(-.1-phi1)/(.92*3.4),
                 length_from_turn_rate=True)
    if early['L']<=0:raise ValueError("This chart retains a positive early return")
    rows[ids['central_cylinder']]['L']=cylinder
    rows[ids['partial_return_matching_coast']]['L']=coast
    redeep=rows[ids['redeepen_after_partial_return']]
    redeep.update(K=redeepen_curvature,
        L=abs(redeep['p1']-redeep['p0'])/(.92*redeepen_curvature),
        length_from_turn_rate=True)
    rows[ids['cut_second_jet_brake']]['L']=brake_length
    for key in ('radial_coast_budget','selection_reason','finite_linear_screen',
                'full_m2_amplification','metric_diagnostics','physical_parameter'):
        b.pop(key,None)
    b['generated_by']=Path(__file__).name
    b['generator_sha256']=digest(__file__)
    b['partial_return_design_parameters'].update(vmid=vmid,coast_length=coast,
        K=redeepen_curvature)
    b['flat_cut_design'].update(vmid=vmid,ramp_length=ramp,coast_length=coast,
        cylinder_length=cylinder,brake_length=brake_length,
        redeepen_curvature=redeepen_curvature,contraction_plateau_length=plateau,
        physical_metric_changed=True)
    b['redeepen_outer_design']=dict(
        selected_parameters=dict(redeepen_curvature=redeepen_curvature,vmid=vmid,
            contraction_ramp=ramp,terminal_brake_length=brake_length,
            central_cylinder_length=cylinder,coast_T=coast),
        motivation="Reduce the actual original initializer's positive-K/n amplification in redeepen; compensate radial room by milder preceding contraction.",
        same_a0=True,same_flat_cut_jet=[.8,-1.,0.],
        all_T_changes_are_outer_metric_design=True,
        raw_three_field_tail_lift_required=True,
        rotational_Z_is_not_actual_nonlinear_cut_Z=True)
    b['status']=dict(metric_frozen=True,nonlinear_prefix_solved=False,
        nonlinear_tail_matched=False,closed_nonround_surface=False,
        reach_certified=False,strong_target_complete=False)
    return b


def radial_budget(bundle):
    rows=bundle['segments']
    labels={q.get('label'):j for j,q in enumerate(rows)}
    deep=labels['final_deep_coast']
    short=copy.deepcopy(bundle);short['segments']=copy.deepcopy(rows[:deep])
    prefix=fm.Candidate(short)
    brake=dict(rows[labels['cut_second_jet_brake']])
    brake['p0']=prefix.segments[-1]['p1']
    dbrake=fm.phase_integral(brake,1.)
    current_room=prefix.segments[-1]['a_end']+dbrake-.8
    T=rows[labels['partial_return_matching_coast']]['L']
    vm=math.sin(-.1);vd=math.sin(brake['p0'])
    return dict(physical_T_lower_open=0.,physical_T_upper_open=T+current_room/(-vm),
        deep_coast_at_T=current_room/(-vd),current_radial_room=current_room,
        T=T,vm=vm,vd=vd,positive_at_T=(T>0 and current_room>0),
        formula="Ldeep(T)=(R0+vm*T)/(-vd), 0<T<R0/(-vm)")


def write_case(source,stem,parameters):
    b=alter(source,**parameters)
    budget=radial_budget(b)
    if not budget['positive_at_T']:
        return dict(parameters=parameters,feasible=False,budget=budget,
                    failure="No positive deep coast at the selected T; no candidate emitted.")
    b['positive_coast_domain']=budget
    b['partial_return_design_parameters']['fraction']=parameters['coast']/budget['physical_T_upper_open']
    candidate=FlatCutCandidate(b)
    path=stem.with_name(stem.name+'-candidate.json')
    path.write_text(json.dumps(b,indent=2,allow_nan=False)+'\n')
    profile=PositiveCoastDesignProfile(path)
    trials=[]
    x=np.unique(np.concatenate([np.linspace(q['s0'],q['s1'],9) for q in profile.segments]))
    for fraction in (.1,.5,.9):
        T=fraction*profile.model.Tmax
        profile.set_parameter(T);j=profile.jet(x)
        trials.append(dict(T=T,minimum_s_x=float(np.min(j['radial_scale'])),
            actual_end=profile.current.end,cut_jet=[float(v[0]) for v in profile.current.profile([profile.current.end])]))
    profile.set_parameter(parameters['coast'])
    s=np.unique(np.concatenate([np.linspace(q['s0'],q['s1'],65) for q in candidate.segments]))
    data=candidate.meridian_reference(s)
    data['K']=-data['app']/data['a']
    file=stem.with_name(stem.name+'-meridian.npz')
    np.savez_compressed(file,**data)
    u=2*np.pi*np.arange(64)/64
    cut=candidate.reference(np.full(len(u),candidate.end),u)
    z=candidate.background_cut_height
    expected=dict(
        X=np.column_stack((.8*np.cos(u),.8*np.sin(u),np.full(len(u),z))),
        X_s=np.column_stack((-np.cos(u),-np.sin(u),np.zeros(len(u)))),
        X_u=np.column_stack((-.8*np.sin(u),.8*np.cos(u),np.zeros(len(u)))),
        X_ss=np.zeros((len(u),3)),
        X_su=np.column_stack((np.sin(u),-np.cos(u),np.zeros(len(u)))),
        X_uu=np.column_stack((-.8*np.cos(u),-.8*np.sin(u),np.zeros(len(u)))))
    errors={key:float(np.max(np.abs(cut[key]-value))) for key,value in expected.items()}
    coasts=[dict(label=q['label'],L=q['L']) for q in candidate.segments if q['kind'] in ('coast','coast_to')]
    redeep_index=next(j for j,q in enumerate(candidate.segments) if q.get('label')=='redeepen_after_partial_return')
    in_redeep=data['piece']==redeep_index
    result=dict(feasible=True,parameters=parameters,candidate_file=path.name,
        candidate_sha256=digest(path),meridian_file=file.name,meridian_sha256=digest(file),
        budget=budget,positive_clock_physical_Tmax=profile.model.Tmax,
        budget_vs_model_Tmax_error=abs(profile.model.Tmax-budget['physical_T_upper_open']),
        clock_trials=trials,positive_coasts=coasts,
        background_cut_Z=z,background_Z_is_not_actual_nonlinear_Z=True,
        central_a0=candidate.a0,physical_meridian_length=candidate.end,
        scalar_metric=candidate.metric_diagnostics(),
        sampled_background_max_meridian_curvature=float(np.max(abs(data['phase_speed']))),
        sampled_redeep_max_abs_meridian_curvature=float(np.max(abs(data['phase_speed'][in_redeep]))),
        sampled_redeep_max_Gauss_curvature=float(np.max(data['K'][in_redeep])),
        sampled_background_min_outward_support=float(np.min(data['a']*data['b']-data['z']*data['ap'])),
        complete_rotational_cut_jet_errors=errors,
        flat_endpoint_II_max=float(max(np.max(abs(cut[key])) for key in ('l','m','n'))),
        nonlinear_prefix_solved=False,continuous_geometry_certified=False)
    if not all(q['L']>0 for q in coasts) or max(errors.values())>1e-12:
        raise AssertionError("The emitted candidate failed its finite physical endpoint/coast check")
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--redeepen-curvature',type=float,default=4.5)
    ap.add_argument('--vmid',type=float,default=.12)
    ap.add_argument('--ramp',type=float,default=.02)
    ap.add_argument('--brake-length',type=float,default=.026)
    ap.add_argument('--coast',type=float,default=.04)
    ap.add_argument('--cylinders',type=float,nargs='+',default=[.4,.47])
    args=ap.parse_args()
    stem=args.out_prefix;stem.parent.mkdir(parents=True,exist_ok=True)
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError("Use a new output stem")
    started=time.monotonic()
    source=json.loads(args.source.read_text())
    source.setdefault('inputs',{})['new_redeep_source']={
        'file':args.source.name,'sha256':digest(args.source),
        'generator':Path(__file__).name,'generator_sha256':digest(__file__)}
    original=FlatCutCandidate(source)
    failures=[]
    # Two directed original-shape attempts quantify the actual lost radial room.
    for K in (4.5,3.4):
        b=alter(source,redeepen_curvature=K,vmid=.4,ramp=.04,
                brake_length=.04,cylinder=.4,coast=.02)
        failures.append(dict(parameters=dict(redeepen_curvature=K,vmid=.4,ramp=.04,
            brake_length=.04,cylinder=.4,coast=.02),budget=radial_budget(b),
            candidate_emitted=False,scope="Original preceding shape with only redeepen K and cylinder changed."))
    rows=[]
    for cylinder in args.cylinders:
        params=dict(redeepen_curvature=args.redeepen_curvature,vmid=args.vmid,
            ramp=args.ramp,brake_length=args.brake_length,cylinder=cylinder,coast=args.coast)
        tag=f'cyl{round(cylinder*100):03d}'
        rows.append(write_case(source,stem.with_name(stem.name+'-'+tag),params))
    report=dict(schema='fd2d-flatcut-milder-redeep-physical-design-v1',
        actual_execution=True,source_sha256=digest(args.source),
        generator_sha256=digest(__file__),
        published_reader_sha256=digest(HERE/'fd2d_flat_cut_prefix_candidate.py'),
        scalar_reader_sha256=digest(HERE/'fd2d_frozen_ellipse_candidate.py'),
        positive_clock_sha256=digest(HERE/'fd2d_gc_design_profile_positive.py'),
        old_candidate_unchanged=True,old_central_a0=original.a0,
        original_shape_lower_K_attempts=failures,candidates=rows,
        seconds=time.monotonic()-started,
        scope="Outer physical design; all entries are complete scalar metrics and rotational reference checks, never a nonround same-g solution.")
    out=stem.with_name(stem.name+'-report.json')
    out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,allow_nan=False))
    if not any(q['feasible'] for q in rows):raise SystemExit(1)
if __name__=='__main__':main()
