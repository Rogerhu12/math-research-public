#!/usr/bin/env python3
"""Finite actual-body screen of a bound raw three-field prefix.

Read --field and --report, reconstruct the P1 corrections plus exact liftings,
and integrate the 24-column frame/angle-variation system at FIXED material u.
No physical BVP is solved. Report actual Gram, normal, generalized principal
curvatures, and every cut Cartesian two-jet under one proper rigid registration.
This floating finite sample is never a continuous certificate or seam proof.
"""
from __future__ import annotations
import os
for _thread_name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_thread_name]='1'
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import time
import traceback
import numpy as np
from scipy.integrate import solve_ivp
from fd2d_balanced_curvature_core import FixedBalancedGeometry
from fd2d_gc_raw_native_field import (RawLiftedNativeField,actual_body_twojet,
    body_rhs_from_fields,unpack_body_state)
from fd2d_gc_archive_arrays import identity,save_npz

HERE=Path(__file__).resolve().parent
TOP=HERE.parent
JET_KEYS=('X','X_s','X_u','X_ss','X_su','X_uu')
SCOPE=('Floating finite material-angle/radial samples of the actual ODE-defined '
       'map. Integration, coefficient and quadrature error are not certified; '
       'no continuous metric, reach, seam, or completed closed surface claim.')


def atomic_json(path,value):
    path=Path(path)
    data=json.dumps(value,indent=2,allow_nan=False)+'\n'
    temporary=path.with_name(path.name+'.tmp')
    temporary.write_text(data);temporary.replace(path)


def resolve_identity(owner,row):
    if not isinstance(row,dict) or not isinstance(row.get('sha256'),str):
        raise ValueError('A bound input identity with sha256 is required')
    original=Path(row.get('path',row.get('file','')))
    options=[original,Path(owner).parent/original.name,TOP/'notes'/original.name,HERE/original.name]
    # Repository-relative paths from CI reports may be portable as written.
    if not original.is_absolute():
        options.extend((TOP/original,TOP.parent.parent/original))
    for candidate in options:
        if candidate.is_file() and identity(candidate)['sha256']==row['sha256']:
            return candidate
    raise ValueError('Missing or changed bound input '+str(original))


def matching_identities(value,sha256,prefix='$'):
    out=[]
    if isinstance(value,dict):
        if value.get('sha256')==sha256:
            out.append(prefix)
        for key,item in value.items():
            out.extend(matching_identities(item,sha256,prefix+'.'+str(key)))
    elif isinstance(value,list):
        for j,item in enumerate(value):
            out.extend(matching_identities(item,sha256,prefix+'['+str(j)+']'))
    return out


def explicit_definition(report,report_path):
    parameters=report.get('parameters',{})
    if not isinstance(parameters,dict):
        raise ValueError('The report parameters must be a settings object')
    schema=str(report.get('schema',''))
    central=report.get('central_definition',report.get('initial_geometry',{}))
    if not isinstance(central,dict):central={}
    choices={}
    origins={}
    for key in ('profile_kind','tail_kind','base_kind'):
        value=parameters.get(key,report.get(key))
        if key=='base_kind' and value is None:value=central.get('base_kind')
        if value is not None:
            choices[key]=str(value);origins[key]='explicit report setting or central definition'
    if schema=='fd2d-raw-three-field-exact-lifting-finite-design-v1':
        for key,value in dict(profile_kind='legacy_coast',tail_kind='signed_bubble',
                              base_kind='balanced_seed').items():
            if key not in choices:
                choices[key]=value;origins[key]='explicit historical v1 schema contract'
    elif schema=='fd2d-raw-three-field-exact-lifting-finite-design-v2':
        if 'base_kind' not in choices:
            choices['base_kind']='balanced_seed'
            origins['base_kind']='historical v2 raw provider fixed central base'
    missing=set(('profile_kind','tail_kind','base_kind'))-set(choices)
    if missing:
        raise ValueError('Report lacks explicit field factory choices: '+','.join(sorted(missing)))
    radial=report.get('radial_chart')
    if not isinstance(radial,dict) or 'reference_T' not in radial:
        raise ValueError('Report must bind radial_chart.reference_T; actual T comes from the field')
    angular=report.get('angular_chart',{})
    blend=angular.get('blend_interval') if isinstance(angular,dict) else None
    if blend is None:blend=report.get('blend_interval')
    if not isinstance(blend,(list,tuple)) or len(blend)!=2:
        raise ValueError('Report must bind the actual moving-chart blend interval')
    if isinstance(angular,dict) and angular.get('kind') not in (
        None,'fixed-seed-normal-to-material-quintic'):
        raise ValueError('This consumer implements the recorded moving chart, not another angular map')
    candidate=resolve_identity(report_path,report.get('candidate_input'))
    geometry_status={}
    if 'exact_moments' in central and 'exact_weighted_means' in central:
        moments=resolve_identity(report_path,central['exact_moments'])
        means=resolve_identity(report_path,central['exact_weighted_means'])
        geometry=FixedBalancedGeometry(moments=moments,means=means)
        geometry_status['source']='Report central-definition exact packets'
    elif 'moments' in report and 'means' in report:
        geometry=FixedBalancedGeometry(moments=resolve_identity(report_path,report['moments']),
            means=resolve_identity(report_path,report['means']))
        geometry_status['source']='Report top-level exact packets'
    else:
        geometry=FixedBalancedGeometry()
        geometry_status.update(source='Current published FixedBalancedGeometry defaults, bound in this output',
            source_report_did_not_bind_these_packets=True,
            note='This explicit floating consumer definition is recorded; no absent source closure is inferred.')
    return dict(candidate=candidate,reference_T=float(radial['reference_T']),
        blend_interval=tuple(float(x) for x in blend),geometry=geometry,choices=choices,
        choices_origin=origins,geometry_binding=geometry_status,
        report_radial_actual_T=radial.get('actual_T'),
        report_central_coefficients=central.get('coefficients_exact'))


def field_summary(reader,x,u,state):
    physical=reader.physical(x,u)
    jets=actual_body_twojet(state,a=physical['a'],l=physical['l'])
    X,F,_,_,_,_=unpack_body_state(state)
    a=np.asarray(physical['a'],float)
    ts,tu=jets['X_s'],jets['X_u']/a[:,None]
    gram=np.empty((len(u),2,2))
    gram[:,0,0]=np.einsum('ij,ij->i',ts,ts)
    gram[:,0,1]=gram[:,1,0]=np.einsum('ij,ij->i',ts,tu)
    gram[:,1,1]=np.einsum('ij,ij->i',tu,tu)
    metric_eigen=np.linalg.eigvalsh(gram)
    metric_error=np.max(np.abs(metric_eigen-1),axis=1)
    normal=np.asarray(jets['N'])
    II=np.empty_like(gram)
    ii=np.asarray(jets['actual_second_form_orthonormal'])
    II[:,0,0],II[:,0,1],II[:,1,0],II[:,1,1]=ii[:,0],ii[:,1],ii[:,1],ii[:,2]
    # Stable actual tangent QR. R maps the target-scaled coordinate basis
    # to an orthonormal basis of the induced metric, so shape=R^-T II R^-1.
    r11=np.linalg.norm(ts,axis=1)
    if np.any(r11<=0):raise FloatingPointError('Actual radial tangent vanished at a sample')
    e1=ts/r11[:,None]
    e2=np.cross(normal,e1)
    r12=np.einsum('ij,ij->i',e1,tu)
    r22=np.einsum('ij,ij->i',e2,tu)
    if np.any(r22<=0) or not np.all(np.isfinite(r22)):
        raise FloatingPointError('Actual oriented tangent basis cannot be represented at a sample')
    inverse=np.zeros_like(gram)
    inverse[:,0,0]=1/r11
    inverse[:,0,1]=-r12/(r11*r22)
    inverse[:,1,1]=1/r22
    shape=np.swapaxes(inverse,-1,-2)@II@inverse
    shape=.5*(shape+np.swapaxes(shape,-1,-2))
    curvatures=np.linalg.eigvalsh(shape)
    formal=np.stack((physical['n'],physical['m'],physical['l']),axis=-1)
    formal_radius=np.hypot(formal[:,0]-formal[:,2],2*formal[:,1])
    formal_curv=np.column_stack(((formal[:,0]+formal[:,2]-formal_radius)/2,
                                (formal[:,0]+formal[:,2]+formal_radius)/2))
    frame_normal=F[:,:,2]
    frame_length=np.linalg.norm(frame_normal,axis=1)
    if np.any(frame_length<=0):raise FloatingPointError('Numerical frame normal vanished')
    frame_normal=frame_normal/frame_length[:,None]
    normal_error=np.linalg.norm(normal-frame_normal,axis=1)
    support=-np.einsum('ij,ij->i',X,normal)
    output=dict(x=float(x),s=float(physical['s'][0]),a=float(a[0]),J=float(physical['J'][0]),
        state=np.asarray(state).copy(),gram=gram,II=II,
        normal=normal,principal_curvatures=curvatures,
        metric_relative_error=metric_error,metric_eigenvalues=metric_eigen,
        frame_normal_error=normal_error,
        frame_orthogonality_error=np.asarray(jets['frame_orthogonality_error']),
        support_outward_about_original_origin=support,
        auxiliary_nml=formal,auxiliary_eigenvalues=formal_curv,
        angle_inverse_error=np.asarray(physical['angle_inverse_error']),
        jets={k:np.asarray(jets[k]).copy() for k in JET_KEYS})
    for key in ('gram','II','normal','principal_curvatures','metric_relative_error'):
        if not np.all(np.isfinite(output[key])):
            raise FloatingPointError('Nonfinite actual geometric sample: '+key)
    return output


def sample_row(sample,u):
    metrics=sample['metric_relative_error']
    curvature=np.max(np.abs(sample['principal_curvatures']),axis=1)
    im,ik=int(np.argmax(metrics)),int(np.argmax(curvature))
    return dict(x=sample['x'],s=sample['s'],a=sample['a'],
        metric_error_max=float(metrics[im]),metric_worst_u=float(u[im]),
        gram_min_eigenvalue=float(np.min(sample['metric_eigenvalues'])),
        actual_curvature_abs_max=float(curvature[ik]),curvature_worst_u=float(u[ik]),
        actual_principal_curvature_min=float(np.min(sample['principal_curvatures'])),
        actual_principal_curvature_max=float(np.max(sample['principal_curvatures'])),
        auxiliary_curvature_abs_max=float(np.max(np.abs(sample['auxiliary_eigenvalues']))),
        frame_normal_error_max=float(np.max(sample['frame_normal_error'])),
        frame_orthogonality_error_max=float(np.max(sample['frame_orthogonality_error'])),
        outward_support_about_original_origin_min=float(np.min(sample['support_outward_about_original_origin'])),
        radius_max=float(np.max(np.linalg.norm(sample['jets']['X'],axis=1))),
        z_min=float(np.min(sample['jets']['X'][:,2])),z_max=float(np.max(sample['jets']['X'][:,2])),
        angular_inverse_error_max=float(np.max(np.abs(sample['angle_inverse_error']))))


def proper_rigid_registration(source,target):
    """One position-only Kabsch fit: target ~= Q*source + translation.

    The same Q,t is subsequently applied to all derivatives. No phase change,
    reflection, per-angle alignment, or separate normal fit is permitted.
    """
    source,target=np.asarray(source,float),np.asarray(target,float)
    if source.shape!=target.shape or source.ndim!=2 or source.shape[1]!=3:
        raise ValueError('Rigid fit needs equal Nx3 corresponding points')
    source_mean,target_mean=source.mean(axis=0),target.mean(axis=0)
    A,B=source-source_mean,target-target_mean
    U,singular,Vt=np.linalg.svd(A.T@B)
    sign=1. if np.linalg.det(Vt.T@U.T)>=0 else -1.
    fix=np.diag([1.,1.,sign])
    Q=Vt.T@fix@U.T
    translation=target_mean-Q@source_mean
    residual=source@Q.T+translation-target
    source_singular=np.linalg.svd(A,compute_uv=False)
    scale=float(source_singular[0]) if len(source_singular) else 0.
    rank=int(np.count_nonzero(source_singular>max(1.,scale)*64*np.finfo(float).eps))
    zaxis=Q[:,2]
    return dict(Q=Q,translation=translation,position_residual=residual,
        covariance_singular_values=singular,source_centered_singular_values=source_singular,
        source_sample_rank=rank,proper_rotation_det=float(np.linalg.det(Q)),
        orthogonality_error=float(np.max(np.abs(Q.T@Q-np.eye(3)))),
        z_axis_after_rotation=zaxis,
        oriented_z_tilt_radians=float(np.arccos(np.clip(zaxis[2],-1.,1.))),
        unoriented_vertical_axis_tilt_radians=float(np.arccos(np.clip(abs(zaxis[2]),0.,1.))),
        horizontal_translation_norm=float(np.linalg.norm(translation[:2])),
        position_rms=float(np.sqrt(np.mean(np.sum(residual*residual,axis=1)))),
        position_max=float(np.max(np.linalg.norm(residual,axis=1))))


def cut_comparison(reader,cut,u,out_prefix):
    tail=reader.tail.cut_port(u,position_jets=True)
    fit=proper_rigid_registration(tail['X'],cut['jets']['X'])
    Q,t=fit['Q'],fit['translation']
    arrays=dict(material_u=u,Q_tail_to_prefix=Q,translation_tail_to_prefix=t,
        body_state=cut['state'],body_gram=cut['gram'],body_II=cut['II'],
        body_principal_curvatures=cut['principal_curvatures'],
        body_inward_normal=cut['normal'],tail_inward_normal=tail['N'],
        tail_registered_inward_normal=np.asarray(tail['N'])@Q.T,
        tail_coefficients=np.asarray(reader.tail.coefficients))
    errors={}
    radius=float(reader.tail.cut_radius)
    divisors=dict(X=1.,X_s=1.,X_u=radius,X_ss=1.,X_su=radius,X_uu=radius**2)
    for key in JET_KEYS:
        raw=np.asarray(tail[key])
        moved=raw@Q.T+(t if key=='X' else 0.)
        body=cut['jets'][key]
        difference=body-moved
        lengths=np.linalg.norm(difference,axis=1)
        worst=int(np.argmax(lengths))
        arrays['body_'+key]=body
        arrays['tail_'+key]=raw
        arrays['registered_tail_'+key]=moved
        arrays['difference_'+key]=difference
        errors[key]=dict(absolute_vector_max=float(lengths[worst]),
            rms=float(np.sqrt(np.mean(lengths*lengths))),worst_material_u=float(u[worst]),
            target_scaled_vector_max=float(lengths[worst]/divisors[key]),
            target_scaling_divisor=divisors[key])
    normal_difference=cut['normal']-np.asarray(tail['N'])@Q.T
    arrays['difference_inward_normal']=normal_difference
    field=reader.physical(reader.nodes[-1],u,side='left')
    formal_cut=np.stack((field['n'],field['m'],field['l']),axis=-1)
    tail_nml=np.stack((tail['n'],tail['m'],tail['l']),axis=-1)
    arrays['auxiliary_cut_nml']=formal_cut
    arrays['tail_cut_nml']=tail_nml
    packet=save_npz(Path(str(out_prefix)+'-cut.npz'),**arrays)
    serial={k:(v.tolist() if isinstance(v,np.ndarray) else v)
        for k,v in fit.items() if k!='position_residual'}
    serial.update(method='One proper position-only Kabsch fit from same-u tail cut to prefix cut',
        mathematical_direction='Y_tail_registered=Q_tail_to_prefix*X_tail+translation',
        no_phase_optimization=True,no_reflection=True,no_separate_derivative_or_normal_fit=True,
        tilt_not_forced_to_zero=True,horizontal_translation_not_forced_to_zero=True)
    return dict(status='FINITE_CUT_SAMPLE_COMPARISON_ONLY',registration=serial,
        jets=errors,inward_normal_vector_error_max=float(np.max(np.linalg.norm(normal_difference,axis=1))),
        auxiliary_nml_difference_max=float(np.max(np.abs(formal_cut-tail_nml))),
        prefix_target_radius=float(cut['a']),tail_declared_cut_radius=radius,
        radius_difference=float(cut['a']-radius),
        saved_cut_correction_absolute_max=float(np.max(np.abs(reader.values[-1]))),
        saved_cut_correction_exactly_zero=bool(np.all(reader.values[-1]==0.)),
        arrays=packet,tail_quadrature_order=int(reader.tail.quadrature_order),
        scope='One fitted rigid comparison; errors neither vanish by definition nor prove an exact C2 seam.')


def stack_samples(samples,u,out_prefix):
    if not samples:return None
    arrays=dict(computational_x=np.array([q['x'] for q in samples]),
        physical_s=np.array([q['s'] for q in samples]),
        target_a=np.array([q['a'] for q in samples]),
        radial_scale=np.array([q['J'] for q in samples]),material_u=u)
    for key in ('state','gram','II','normal','principal_curvatures','metric_relative_error',
                'metric_eigenvalues','frame_normal_error','frame_orthogonality_error',
                'support_outward_about_original_origin','auxiliary_nml','auxiliary_eigenvalues',
                'angle_inverse_error'):
        arrays[key]=np.stack([q[key] for q in samples])
    for key in JET_KEYS:
        arrays[key]=np.stack([q['jets'][key] for q in samples])
    return save_npz(Path(str(out_prefix)+'-samples.npz'),**arrays)


def totals(rows):
    if not rows:return {}
    maxima=('metric_error_max','actual_curvature_abs_max','auxiliary_curvature_abs_max',
        'frame_normal_error_max','frame_orthogonality_error_max','radius_max',
        'angular_inverse_error_max','z_max')
    minima=('gram_min_eigenvalue','outward_support_about_original_origin_min','z_min',
        'actual_principal_curvature_min')
    result={}
    for key in maxima:
        row=max(rows,key=lambda q:q[key])
        result[key]=dict(value=row[key],x=row['x'],s=row['s'],
            material_u=row.get('metric_worst_u') if key=='metric_error_max'
                else row.get('curvature_worst_u') if key=='actual_curvature_abs_max' else None)
    for key in minima:
        row=min(rows,key=lambda q:q[key]);result[key]=dict(value=row[key],x=row['x'],s=row['s'])
    result['actual_principal_curvature_max']=max(q['actual_principal_curvature_max'] for q in rows)
    return result


def checkpoint(path,x,state,u,field_sha,report_sha,completed_spans):
    temporary=Path(str(path)+'.tmp')
    with temporary.open('wb') as stream:
        np.savez_compressed(stream,computational_x=np.array(x),state=state,material_u=u,
            input_field_sha256=np.array(field_sha),input_report_sha256=np.array(report_sha),
            completed_spans=np.array(completed_spans,dtype=np.int64))
    temporary.replace(path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field',type=Path,required=True)
    parser.add_argument('--report',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--angles',type=int,choices=(8,16,32,64),default=32)
    parser.add_argument('--radial-samples-per-span',type=int,default=2)
    parser.add_argument('--rtol',type=float,default=2e-10)
    parser.add_argument('--atol',type=float,default=2e-12)
    parser.add_argument('--max-step',type=float,default=.02)
    parser.add_argument('--max-rhs-evaluations',type=int,default=250000)
    args=parser.parse_args()
    if args.radial_samples_per_span<1 or args.max_rhs_evaluations<1:
        raise ValueError('Positive sample and evaluation counts are required')
    if not 0<args.rtol<1 or not 0<args.atol<1 or not args.max_step>0:
        raise ValueError('Invalid ODE numerical settings')
    stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh diagnostic output stem')
    stem.parent.mkdir(parents=True,exist_ok=True)
    report_path=Path(str(stem)+'-report.json')
    progress_path=Path(str(stem)+'-progress.jsonl')
    checkpoint_path=Path(str(stem)+'-endpoint-current.npz')
    started=time.monotonic()
    report=dict(schema='fd2d-raw-actual-body-finite-screen-v1',scope=SCOPE,
        source=identity(__file__),input_field=identity(args.field),input_report=identity(args.report),
        settings={k:(str(v) if isinstance(v,Path) else v) for k,v in vars(args).items()},
        completed=False,computation_completed=False,continuous_certificate=False,
        closed_surface=False,exception=None,completed_spans=0,rhs_evaluations=0,
        array_scope='Approximate ODE samples, not an exact dense polynomial or a continuous enclosure',
        auxiliary_l_is_independent=True,physical_material_angle_held_fixed=True)
    samples=[];rows=[];u=2*np.pi*np.arange(args.angles)/args.angles
    rhs_calls=0;latest_state=None;latest_x=None
    def save():
        report['seconds']=time.monotonic()-started
        report['maximum_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report['rhs_evaluations']=rhs_calls
        atomic_json(report_path,report)
    def event(kind,**values):
        row=dict(event=kind,seconds=time.monotonic()-started,**values)
        with progress_path.open('a') as stream:
            stream.write(json.dumps(row,allow_nan=False)+'\n')
        return row
    save()
    try:
        source_report=json.loads(args.report.read_text())
        matches=matching_identities(source_report,report['input_field']['sha256'])
        if not matches:
            raise ValueError('Selected field SHA is not bound anywhere in the supplied report; supply its true report')
        report['field_identity_matches_in_report']=matches
        definition=explicit_definition(source_report,args.report)
        reader=RawLiftedNativeField(args.field,definition['candidate'],
            reference_T=definition['reference_T'],blend_interval=definition['blend_interval'],
            geometry=definition['geometry'],**definition['choices'])
        source_modes=source_report.get('parameters',{}).get('modes')
        if source_modes is not None and int(source_modes)!=reader.K:
            raise ValueError('Report mode count differs from the selected defining arrays')
        report['source_solver_status']={key:source_report.get(key) for key in
            ('schema','success','completed','accepted_steps','stop_reason','exception')}
        report['source_solver_status_is_not_a_geometry_certificate']=True
        report['definition_settings']=dict(reference_T=definition['reference_T'],
            actual_T_from_field=float(reader.parameters[-1]),
            report_recorded_actual_T=definition['report_radial_actual_T'],
            recorded_actual_T_may_describe_initial_checkpoint=True,
            blend_interval=list(definition['blend_interval']),**definition['choices'],
            choices_origin=definition['choices_origin'],geometry_binding=definition['geometry_binding'])
        recorded_c=definition['report_central_coefficients']
        actual_c=[str(Fraction.from_float(float(x))) for x in reader.parameters[:reader.K]]
        if recorded_c is not None:
            report['selected_field_c_equals_report_current_c']=(list(recorded_c)==actual_c)
        definition_path=Path(str(stem)+'-definition.json')
        atomic_json(definition_path,reader.definition())
        report['actual_field_definition']=identity(definition_path)
        source_files=['fd2d_gc_raw_native_field.py','fd2d_gc_archive_arrays.py',
            'fd2d_gc_three_field_residual.py','fd2d_balanced_curvature_core.py',
            'fd2d_gc_design_profile.py','fd2d_gc_design_profile_positive.py',
            'fd2d_flat_developable_family.py','fd2d_positive_flat_developable_family.py']
        report['consumer_sources']=[identity(HERE/name) for name in source_files]
        end=float(reader.nodes[-1])
        extra=np.r_[reader.profile.breaks,reader.blend_interval,
                    .42*reader.profile.end,min(.55,.4*reader.profile.end)]
        splits=np.unique(np.r_[reader.nodes,extra[(extra>0)&(extra<end)]])
        report['integration_spans']=len(splits)-1
        report['split_rule']='All actual P1 nodes, scalar-profile breaks, chart blend endpoints, and lifting transition endpoints'
        report['material_angles']=dict(count=len(u),formula='2*pi*j/N, j=0,...,N-1',include_symmetry_axes=True)
        state=reader.body_initial(u)
        latest_state,latest_x=state.copy(),float(splits[0])
        initial=field_summary(reader,latest_x,u,state)
        samples.append(initial);rows.append(sample_row(initial,u))
        def rhs(x,flat):
            nonlocal rhs_calls
            rhs_calls+=1
            if rhs_calls>args.max_rhs_evaluations:
                raise RuntimeError('Recorded diagnostic RHS evaluation allocation exhausted; no geometric impossibility is inferred')
            values=reader.physical(float(x),u)
            result=body_rhs_from_fields(flat.reshape(len(u),24),
                **{key:values[key] for key in ('J','l','m','l_u','m_u','l_uu','m_uu')})
            if not np.all(np.isfinite(result)):
                raise FloatingPointError('Nonfinite actual fixed-material frame RHS')
            return result.ravel()
        last_print=started
        save();print(json.dumps(event('start',modes=reader.K,angles=len(u),spans=len(splits)-1)),flush=True)
        for number,(left,right) in enumerate(zip(splits[:-1],splits[1:]),1):
            evaluation=np.linspace(left,right,args.radial_samples_per_span+1)[1:]
            solution=solve_ivp(rhs,(float(left),float(right)),state.ravel(),method='DOP853',
                rtol=args.rtol,atol=args.atol,max_step=min(args.max_step,float(right-left)),
                t_eval=evaluation)
            if not solution.success:
                raise RuntimeError('Actual frame ODE failed: '+str(solution.message))
            if solution.y.shape[1]!=len(evaluation):
                raise RuntimeError('Actual frame ODE did not return the complete requested span')
            for j,x in enumerate(evaluation):
                value=solution.y[:,j].reshape(len(u),24)
                sample=field_summary(reader,float(x),u,value)
                samples.append(sample);rows.append(sample_row(sample,u))
            state=solution.y[:,-1].reshape(len(u),24).copy()
            latest_state,latest_x=state.copy(),float(right)
            report['completed_spans']=number
            checkpoint(checkpoint_path,latest_x,state,u,report['input_field']['sha256'],
                report['input_report']['sha256'],number)
            current=rows[-1]
            item=event('span',number=number,right_x=latest_x,s=current['s'],
                sampled_metric_max=max(q['metric_error_max'] for q in rows),
                sampled_actual_curvature_max=max(q['actual_curvature_abs_max'] for q in rows),
                rhs_evaluations=rhs_calls)
            if number==1 or number==len(splits)-1 or time.monotonic()-last_print>=10:
                report['sample_totals']=totals(rows);save()
                print(json.dumps(item),flush=True);last_print=time.monotonic()
        report['cut']=cut_comparison(reader,samples[-1],u,stem)
        report['completed']=report['computation_completed']=True
        report['status']='FINITE_ACTUAL_BODY_AND_CUT_SCREEN_COMPLETED'
        report['stop_reason']='Requested finite diagnostic completed; no continuous or final acceptance claim'
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        report['status']='FINITE_BODY_SCREEN_FAILED_OR_INCOMPLETE'
        report['stop_reason']='See the actual exception; no mathematical nonexistence or completed geometry is inferred'
        event('exception',type=type(exc).__name__,message=str(exc))
    finally:
        report['sample_totals']=totals(rows)
        report['sample_rows']=rows
        report['saved_sample_count']=len(samples)
        if latest_x is not None:
            report['last_complete_endpoint_x']=latest_x
        try:
            report['sample_arrays']=stack_samples(samples,u,stem)
            if checkpoint_path.is_file():report['last_complete_endpoint_checkpoint']=identity(checkpoint_path)
            report['progress_log']=identity(progress_path) if progress_path.is_file() else None
        except Exception as exc:
            report['output_error']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
            report['completed']=report['computation_completed']=False
        save()
    print(json.dumps(dict(report=str(report_path),computation_completed=report['computation_completed'],
        sampled_totals=report['sample_totals'],exception=report['exception'],
        surface_certified=False)),flush=True)
    return 0 if report['computation_completed'] else 1


if __name__=='__main__':raise SystemExit(main())

