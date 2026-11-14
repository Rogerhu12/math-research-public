#!/usr/bin/env python3
"""A NEW physical flat-cut metric with the old positive-K feedback tail removed.

Keep the shared-jet feedback only to its saved radial-speed maximum, define
that final acceleration to be exactly zero, and insert a positive-phase
coast. Its length is selected by a scalar radial budget; all following main
turn curvatures can be lowered while the exact cut stays (.8,-1,0).
No nonlinear prefix solution or all-time geometry certificate is asserted.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,hashlib,json,math,time
from pathlib import Path
import numpy as np
from fd2d_flat_cut_prefix_candidate import FlatCutCandidate,fm
from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile
from fd2d_flatcut_milder_redeep_design import radial_budget

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build(source,*,cylinder=.32,turn_curvature=3.4,vmid=.12,ramp=.02,
          coast=.02,deep_phase=1.45,brake_length=.026,target_deep_coast=.005):
    if min(cylinder,turn_curvature,ramp,coast,brake_length,target_deep_coast)<=0:
        raise ValueError('Positive construction lengths and curvature required')
    old=copy.deepcopy(source)
    feedback=[(i,p) for i,p in enumerate(old['segments']) if p.get('label')=='frozen_feedback_prefix']
    index,last=max(feedback,key=lambda q:q[1]['jet1'][1])
    retained=copy.deepcopy(old['segments'][:index+1])
    if retained[0].get('label')!='central_cylinder':raise ValueError('Unexpected source inlet')
    retained[0]['L']=cylinder
    previous_acceleration=retained[-1]['jet1'][2]
    retained[-1]['jet1'][2]=0.
    speed=retained[-1]['jet1'][1]
    phi0=math.asin(speed);phi1=-math.asin(vmid)
    if not 0<phi0<math.pi/2:raise ValueError('A positive outward phase is required')
    entry_end=phi0-turn_curvature*ramp/2
    exit_start=phi1+turn_curvature*ramp/2
    plateau=(entry_end-exit_start)/turn_curvature
    if plateau<=0:raise ValueError('Nonpositive main contraction plateau')
    early_length=abs(-.1-phi1)/(.92*turn_curvature)
    if early_length<=0:raise ValueError('The coast-T chart retains a positive early-return piece')
    rows=retained+[
        dict(kind='coast',p0=phi0,p1=phi0,L=0.,start_from_previous=True,label='outward_peak_spacer'),
        dict(kind='phase_bridge',p0=phi0,p1=entry_end,L=ramp,ps0=0.,ps1=-turn_curvature,
             start_from_previous=True,start_second_from_previous=True,label='partial_return_acceleration_entry'),
        dict(kind='phase_bridge',p0=entry_end,p1=exit_start,L=plateau,
             ps0=-turn_curvature,ps1=-turn_curvature,start_from_previous=True,label='partial_return_acceleration_plateau'),
        dict(kind='phase_bridge',p0=exit_start,p1=phi1,L=ramp,ps0=-turn_curvature,ps1=0.,
             start_from_previous=True,label='partial_return_acceleration_exit'),
        dict(kind='turn',p0=phi1,p1=-.1,L=early_length,K=turn_curvature,
             start_from_previous=True,length_from_turn_rate=True,label='early_shallow_return'),
        dict(kind='coast',p0=-.1,p1=-.1,L=coast,start_from_previous=True,label='partial_return_matching_coast'),
        dict(kind='turn',p0=-.1,p1=-deep_phase,L=(deep_phase-.1)/(.92*turn_curvature),K=turn_curvature,
             start_from_previous=True,length_from_turn_rate=True,label='redeepen_after_partial_return'),
        dict(kind='coast_to',p0=-deep_phase,p1=-deep_phase,start_from_previous=True,
             radius_after_next=.8,label='final_deep_coast'),
        dict(kind='phase_bridge',p0=-deep_phase,p1=-math.pi/2,L=brake_length,ps0=0.,ps1=0.,
             start_from_previous=True,label='cut_second_jet_brake',exact_endpoint_phase='-pi/2',
             geometric_role='flat_cut_quadratic_brake')]
    b=copy.deepcopy(old);b['segments']=rows
    for key in ('radial_coast_budget','selection_reason','finite_linear_screen','full_m2_amplification',
                'metric_diagnostics','physical_parameter','positive_coast_domain','redeepen_outer_design'):
        b.pop(key,None)
    zero=radial_budget(b)
    wanted=math.sin(deep_phase)*target_deep_coast
    length=(wanted-zero['current_radial_room'])/speed
    if length<=0:raise ValueError('The selected target does not require a positive outward spacer')
    rows[len(retained)]['L']=length
    budget=radial_budget(b)
    if not budget['positive_at_T']:raise ValueError('The actual derived final coast is not positive')
    b['partial_return_design_parameters']=dict(vmid=vmid,return_phase=.1,
        coast_length=coast,fraction=coast/budget['physical_T_upper_open'],K=turn_curvature,
        transition=ramp,epsilon=math.pi/2-deep_phase)
    b['flat_cut_design']=dict(vmid=vmid,contraction_curvature=turn_curvature,
        early_return_curvature=turn_curvature,redeepen_curvature=turn_curvature,
        ramp_length=ramp,coast_length=coast,deep_phase=deep_phase,brake_length=brake_length,
        cylinder_length=cylinder,contraction_plateau_length=plateau,
        physical_metric_changed=True,terminal_phase='-pi/2 + O((s_cut-s)^2)',
        future_design_T='Outer physical design; freeze after a solution is selected')
    b['peak_spacer_design']=dict(
        retained_source_feedback_raw_last_index=index,
        retained_feedback_length=sum(p['L'] for p in retained if p.get('label')=='frozen_feedback_prefix'),
        removed_feedback_length=sum(p['L'] for i,p in feedback if i>index),
        original_final_acceleration=previous_acceleration,new_exact_final_acceleration=0.,
        final_shared_position_and_velocity=retained[-1]['jet1'][:2],
        feedback_change='The last retained quintic has the same endpoint radius/speed and a newly defined zero acceleration; the old positive-K suffix is not retained.',
        outward_phase=phi0,outward_radial_speed=speed,outward_coast_length=length,
        zero_spacer_radial_budget_for_selection=zero,
        target_final_deep_coast_for_selection=target_deep_coast,
        actual_final_deep_coast_from_frozen_spacer=budget['deep_coast_at_T'],
        selection_formula='E=(sin(pdeep)*target_Ldeep-zero_spacer_room)/saved_peak_radial_speed',
        zero_spacer_used_only_to_evaluate_the_affine_design_budget=True,
        spacer_length_frozen_as_written_binary64=True,
        exact_final_radius_from_derived_coast_to=True,
        same_central_a0=True,background_height_is_not_actual_nonlinear_height=True)
    b['positive_coast_domain']=budget
    b['generated_by']=Path(__file__).name;b['generator_sha256']=digest(__file__)
    b['status']=dict(metric_frozen=True,nonlinear_prefix_solved=False,nonlinear_tail_matched=False,
        closed_nonround_surface=False,reach_certified=False,strong_target_complete=False)
    return b


def close(b,stem):
    path=stem.with_name(stem.name+'-candidate.json')
    path.write_text(json.dumps(b,indent=2,allow_nan=False)+'\n')
    candidate=FlatCutCandidate(b);profile=PositiveCoastDesignProfile(path)
    x=np.unique(np.concatenate([np.linspace(p['s0'],p['s1'],9) for p in profile.segments]))
    trials=[]
    for fraction in (.1,.5,.9):
        T=fraction*profile.model.Tmax;profile.set_parameter(T);q=profile.jet(x)
        trials.append(dict(T=T,minimum_s_x=float(np.min(q['radial_scale'])),
            cut_jet=[float(v[0]) for v in profile.current.profile([profile.current.end])]))
    profile.set_parameter(profile.reference_T)
    s=np.unique(np.concatenate([np.linspace(p['s0'],p['s1'],65) for p in candidate.segments]))
    data=candidate.meridian_reference(s);data['K']=-data['app']/data['a']
    datafile=stem.with_name(stem.name+'-meridian.npz');np.savez_compressed(datafile,**data)
    u=2*np.pi*np.arange(64)/64;cut=candidate.reference(np.full(len(u),candidate.end),u)
    expected=dict(X=np.column_stack((.8*np.cos(u),.8*np.sin(u),np.full(len(u),candidate.background_cut_height))),
        X_s=np.column_stack((-np.cos(u),-np.sin(u),np.zeros(len(u)))),
        X_u=np.column_stack((-.8*np.sin(u),.8*np.cos(u),np.zeros(len(u)))),X_ss=np.zeros((len(u),3)),
        X_su=np.column_stack((np.sin(u),-np.cos(u),np.zeros(len(u)))),
        X_uu=np.column_stack((-.8*np.cos(u),-.8*np.sin(u),np.zeros(len(u)))))
    errors={k:float(np.max(abs(cut[k]-v))) for k,v in expected.items()}
    pieces=[]
    for j,p in enumerate(candidate.segments):
        if p.get('label')=='frozen_feedback_prefix':continue
        keep=data['piece']==j
        pieces.append(dict(label=p.get('label'),L=p['L'],a_start=p['a_start'],a_end=p['a_end'],
            sampled_abs_meridian_curvature=float(np.max(abs(data['phase_speed'][keep]))),
            sampled_K_min=float(np.min(data['K'][keep])),sampled_K_max=float(np.max(data['K'][keep]))))
    feedback=np.isin(data['piece'],[j for j,p in enumerate(candidate.segments) if p.get('label')=='frozen_feedback_prefix'])
    coasts=[p for p in candidate.segments if p['kind'] in ('coast','coast_to')]
    if min(p['L'] for p in coasts)<=0 or max(errors.values())>1e-12:
        raise AssertionError('The actual physical coast/cut check failed')
    return dict(candidate_file=path.name,candidate_sha256=digest(path),
        meridian_file=datafile.name,meridian_sha256=digest(datafile),
        generator_sha256=digest(__file__),parameters=b['flat_cut_design'],design=b['peak_spacer_design'],
        full_physical_T_domain_open=[0.,profile.model.Tmax],positive_clock_trials=trials,
        central_a0=candidate.a0,meridian_length=candidate.end,background_cut_Z=candidate.background_cut_height,
        scalar_metric=candidate.metric_diagnostics(),piece_diagnostics=pieces,
        sampled_maximum_background_meridian_curvature=float(np.max(abs(data['phase_speed']))),
        sampled_maximum_positive_Gauss_curvature=float(np.max(data['K'])),
        sampled_feedback_K_max=float(np.max(data['K'][feedback])),
        sampled_feedback_K_min=float(np.min(data['K'][feedback])),
        sampled_minimum_outward_support=float(np.min(data['a']*data['b']-data['z']*data['ap'])),
        complete_rotational_cut_jet_errors=errors,
        flat_endpoint_II_max=float(max(np.max(abs(cut[k])) for k in ('l','m','n'))),
        nonlinear_prefix_solved=False,continuous_geometry_certified=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,default=ROOT/'notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json')
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--turn-curvature',type=float,default=3.4)
    ap.add_argument('--cylinders',type=float,nargs='+',default=[.32,.38])
    ap.add_argument('--vmid',type=float,default=.12)
    ap.add_argument('--coast',type=float,default=.02)
    ap.add_argument('--target-deep-coast',type=float,default=.005)
    args=ap.parse_args();stem=args.out_prefix;stem.parent.mkdir(parents=True,exist_ok=True)
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a new physical-input stem')
    started=time.monotonic();source=json.loads(args.source.read_text());rows=[]
    for cylinder in args.cylinders:
        b=build(source,cylinder=cylinder,turn_curvature=args.turn_curvature,vmid=args.vmid,
                coast=args.coast,target_deep_coast=args.target_deep_coast)
        b.setdefault('inputs',{})['peak_spacer_source']=dict(file=args.source.name,sha256=digest(args.source),
            generator=Path(__file__).name,generator_sha256=digest(__file__))
        rows.append(close(b,stem.with_name(stem.name+f'-cyl{round(cylinder*100):03d}')))
    report=dict(schema='fd2d-flatcut-peak-spacer-physical-design-v1',actual_execution=True,
        source_sha256=digest(args.source),generator_sha256=digest(__file__),
        dependencies_sha256={p.name:digest(p) for p in (HERE/'fd2d_flat_cut_prefix_candidate.py',
            HERE/'fd2d_frozen_ellipse_candidate.py',HERE/'fd2d_gc_design_profile_positive.py',
            HERE/'fd2d_flatcut_milder_redeep_design.py')},candidates=rows,
        seconds=time.monotonic()-started,
        scope='Complete NEW scalar metric inputs and finite rotational checks; no transfer of an old IVP state or nonlinear success.')
    out=stem.with_name(stem.name+'-report.json');out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,allow_nan=False))
if __name__=='__main__':main()
