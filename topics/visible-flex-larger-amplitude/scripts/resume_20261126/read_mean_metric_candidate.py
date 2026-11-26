#!/usr/bin/env python3
"""Actions-only R684 diagnostic of the SAME R671 field against a NEW metric.

No field update, solve, geometry pass, J product or old-g refinement occurs.
This reads all old/Gauss angular rows once, then reports the exact finite
material-weighted mean/variance split and renormalized new-metric error.
Only summaries are written; no metric arrays or regenerated payload are
published. The finite averaging rule is an explicit possible new design,
not a claim that the old target was met or an exact isometry exists.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
import subprocess

import numpy as np


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, Path(path).resolve())
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def operator_error(raw):
    e, f, d = raw[..., 0], raw[..., 1], raw[..., 2]
    return .5*(np.abs(e+d)+np.hypot(e-d, 2*f))


def point_loss(raw, p, epsilon, scale):
    e, f, d = raw[..., 0], raw[..., 1], raw[..., 2]
    gap = np.hypot(e-d, 2*f)
    plus, minus = .5*(e+d+gap), .5*(e+d-gap)
    return (((plus*plus+epsilon*epsilon)/(scale*scale))**(p//2)
            + ((minus*minus+epsilon*epsilon)/(scale*scale))**(p//2))


def location(op, stage, angle):
    return dict(stage=int(stage), s_carrier=float(op.times[stage]),
        cell=int(op.observation_cells[stage]), u=float(op.observation_u[stage]),
        phi_over_pi_numerator=int(angle), phi_over_pi_denominator=int(2*(op.N-1)),
        phi_carrier=float(op.phi[angle]), is_legacy=bool(stage < op.legacy_P))


def read_all(op, x, transform_type, fraction, p, epsilon, scale, target):
    prepared = op.prepare(x)
    if not np.isfinite(prepared.rho).all() or np.any(prepared.rho <= 0):
        raise ValueError('The actual material-coordinate density is not positive at all angle rows')
    m, w = op.multiplicity, op.mixed_stage_weights(fraction)
    norm = float(w.sum()*m.sum())
    component = np.array([1., 2., 1.])
    old_sse=np.zeros(3);old_phi=0.;old_max=0.;old_worst=None;old_bad=0
    min_det=float('inf');stages_read=0
    def state():
        return dict(old_sse=np.zeros(3),centered_sse=np.zeros(3),mean_sse=np.zeros(3),
            new_sse=np.zeros(3),new_phi_sse=np.zeros(3),new_phi=0.,maximum=0.,worst=None,
            min_A=float('inf'),max_A=0.,min_C=float('inf'),max_C=0.,
            min_physical_C=float('inf'),max_physical_C=0.,mean_nonzero=np.zeros(2),
            above_target=0,top=[])
    states={key:state() for key in ('material','physical')}
    for start in range(0, op.P, op.stage_block):
        stop = min(op.P, start+op.stage_block)
        # Exactly one common first-jet read serves BOTH new-metric variants.
        V, d = op._first_batch(prepared, start, stop)
        a = op.a[start:stop, None];ar = a*prepared.rho[None]
        E = np.einsum('bni,bni->bn', V, V)
        F = np.einsum('bni,bni->bn', V, d)
        G = np.einsum('bni,bni->bn', d, d)
        raw = np.stack((E-1, F/ar, G/(ar*ar)-1), axis=-1)
        weighted = w[start:stop, None, None]*m[None, :, None]*component[None, None]
        point_weights=w[start:stop,None]*m[None]
        old_sse+=np.sum(raw*raw*weighted,axis=(0,1))
        old_phi+=float(np.sum(point_loss(raw,p,epsilon,scale)*point_weights))
        oe=operator_error(raw)
        old_bad+=int(np.sum(m[None]*(oe>target)))
        oi=np.unravel_index(int(np.argmax(oe)),oe.shape)
        if float(oe[oi])>old_max:
            old_max=float(oe[oi]);old_worst=location(op,start+oi[0],oi[1])
            old_worst['raw_components']=raw[oi].tolist()
        min_det=min(min_det,float(np.min((1+raw[...,0])*(1+raw[...,2])-raw[...,1]**2)))
        for kind in ('material','physical'):
            q=states[kind];t=transform_type(raw,m,prepared.rho,averaging=kind)
            fresh=t.result;me,md=t.mean_e,t.mean_d
            center=raw.copy();center[...,0]-=me[:,None];center[...,2]-=md[:,None]
            # Orthogonal split uses the SAME positive measure as its mean.
            chosen_weight=weighted*(prepared.rho[None,:,None] if kind=='material' else 1.)
            q['old_sse']+=np.sum(raw*raw*chosen_weight,axis=(0,1))
            q['centered_sse']+=np.sum(center*center*chosen_weight,axis=(0,1))
            q['new_sse']+=np.sum(fresh*fresh*chosen_weight,axis=(0,1))
            q['new_phi_sse']+=np.sum(fresh*fresh*weighted,axis=(0,1))
            q['mean_sse'][0]+=float(w[start:stop]@(me*me))*float(t.mass)
            q['mean_sse'][2]+=float(w[start:stop]@(md*md))*float(t.mass)
            q['new_phi']+=float(np.sum(point_loss(fresh,p,epsilon,scale)*point_weights))
            ne=operator_error(fresh);q['above_target']+=int(np.sum(m[None]*(ne>target)))
            ni=np.unravel_index(int(np.argmax(ne)),ne.shape)
            physical_C=op.a[start:stop]**2*t.angular
            if float(ne[ni])>q['maximum']:
                q['maximum']=float(ne[ni]);q['worst']=location(op,start+ni[0],ni[1])
                q['worst'].update(raw_components=raw[ni].tolist(),new_components=fresh[ni].tolist(),
                    same_point_old_error=float(oe[ni]),new_E=float(t.radial[ni[0]]),
                    new_C=float(physical_C[ni[0]]))
            q['min_A']=min(q['min_A'],float(t.radial.min()));q['max_A']=max(q['max_A'],float(t.radial.max()))
            q['min_C']=min(q['min_C'],float(t.angular.min()));q['max_C']=max(q['max_C'],float(t.angular.max()))
            q['min_physical_C']=min(q['min_physical_C'],float(physical_C.min()))
            q['max_physical_C']=max(q['max_physical_C'],float(physical_C.max()))
            q['mean_nonzero']=np.maximum(q['mean_nonzero'],[float(np.max(np.abs(me))),float(np.max(np.abs(md)))])
            for k in range(stop-start):
                angle=int(np.argmax(ne[k]));st=start+k
                q['top'].append(dict(**location(op,st,angle),old_max=float(oe[k].max()),
                    new_max=float(ne[k,angle]),new_E=float(t.radial[k]),new_C=float(physical_C[k]),
                    new_components=fresh[k,angle].tolist()))
            q['top']=sorted(q['top'],key=lambda v:v['new_max'],reverse=True)[:12]
        stages_read+=stop-start
    variants={}
    for kind,q in states.items():
        original=float(q['old_sse'].sum());mean=float(q['mean_sse'].sum())
        mass=float(np.sum(m*prepared.rho)) if kind=='material' else float(m.sum())
        variants[kind]=dict(
            definition=('theta-Haar quadrature omega=m*rho/sum(m*rho)' if kind=='material'
                else 'Explicit FIXED physical-phi quadrature omega=m/sum(m); NOT a material Haar mean'),
            full_cross_mean='Exactly zero by the proved reflection parity; positive quarter cross mean is never subtracted',
            energy_measure='m*rho' if kind=='material' else 'm',angular_mass=mass,
            exact_finite_mean_variance_split=dict(baseline_sse_in_this_measure=original,
                baseline_component_sse=q['old_sse'].tolist(),removed_diagonal_mean_sse=mean,
                removed_component_sse=q['mean_sse'].tolist(),
                centered_old_normalization_sse=float(q['centered_sse'].sum()),
                centered_component_sse=q['centered_sse'].tolist(),
                removed_fraction=mean/original if original>0 else 0.,
                pythagorean_closure_defect=original-mean-float(q['centered_sse'].sum()),
                scope='Finite split in OLD metric normalization and this explicit measure. It is not fixed-old-g improvement.'),
            proposed_new_mean_metric=dict(E_range=[q['min_A'],q['max_A']],
                C_range=[q['min_physical_C'],q['max_physical_C']],
                C_divided_by_original_a_squared_range=[q['min_C'],q['max_C']],
                largest_changes_in_old_normalized_diagonal=q['mean_nonzero'].tolist(),
                positive_at_all_read_rows=q['min_A']>0 and q['min_physical_C']>0,
                maximum_sampled_relative_Gram=q['maximum'],worst=q['worst'],
                frobenius_sse_in_this_measure=float(q['new_sse'].sum()),
                normalized_frobenius_mean_in_this_measure=float(q['new_sse'].sum())/(float(w.sum())*mass),
                phi_weighted_frobenius_sse=float(q['new_phi_sse'].sum()),
                phi_normalized_frobenius_mean=float(q['new_phi_sse'].sum())/norm,
                phi_normalized_spectral_Phi=q['new_phi']/norm,
                represented_points_above_target=q['above_target'],sampled_target_pass=q['maximum']<=target,
                top12_rows_by_new_error=q['top']))
    return dict(stages_read=stages_read,representative_angles=op.N,full_angles=op.full_N,
        represented_point_rows=op.P*op.full_N,original_free_variables=op.free_size,
        field_passes=1,variants_share_exact_same_first_jet_values=True,
        angular_weights_sum=float(m.sum()),material_angular_weights_sum=float(np.sum(m*prepared.rho)),
        mixed_radial_weight_sum=float(w.sum()),legacy_fraction=fraction,phi_normalization=norm,
        original_metric=dict(maximum_sampled_relative_Gram=old_max,worst=old_worst,
            phi_weighted_frobenius_sse=float(old_sse.sum()),phi_weighted_component_sse=old_sse.tolist(),
            phi_normalized_frobenius_mean=float(old_sse.sum())/norm,
            phi_normalized_spectral_Phi=old_phi/norm,represented_points_above_target=old_bad),
        design_variants=variants,minimum_original_relative_actual_Gram_determinant=min_det,
        spectral_parameters=dict(p=p,epsilon=epsilon,scale=scale),target=target,
        physical_field_changed=False,geometry_evaluations=0,new_J_products=0,nonlinear_solves=0,
        new_fixed_old_g_result=False,frozen_final_metric_created=False,continuous_metric_certified=False,
        exact_solution_existence_certified=False,topic_completion_certified=False)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--bundle',type=Path,required=True)
    ap.add_argument('--carrier',type=Path,required=True)
    ap.add_argument('--node-report',type=Path,required=True)
    ap.add_argument('--scalar-input',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--transform-source',type=Path)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--stage-block',type=int,default=64)
    ap.add_argument('--legacy-fraction',type=float,default=.5)
    ap.add_argument('--spectral-p',type=int,default=8)
    ap.add_argument('--spectral-epsilon',type=float,default=.001)
    ap.add_argument('--spectral-scale',type=float,default=.05)
    ap.add_argument('--target',type=float,default=1e-6)
    args=ap.parse_args()
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise SystemExit('New numerical R684 reads belong to this public repository Actions, not a local scientific run.')
    if (args.angles<4 or args.angles%4 or args.stage_block<1
            or not 0<args.legacy_fraction<1 or args.spectral_p<2 or args.spectral_p%2
            or args.spectral_epsilon<=0 or args.spectral_scale<=0 or args.target<=0):
        raise ValueError('Invalid complete-row diagnostic configuration')
    args.out=args.out.resolve()
    if args.out.exists():
        raise FileExistsError(args.out)
    repo=args.repo.resolve();topic=repo/'topics/visible-flex-larger-amplitude';src=topic/'scripts/resume_20261120'
    paths=dict(exact_tail=src/'exact_reference_tail_lift.py',observed=src/'gauss_observed_closed_gram.py',
        dense=topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        batch=topic/'scripts/resume_20261120_batched_closed_gram.py',
        scalar=topic/'notes/2026-11-17-parallel-model-full-hold-oracle.py',
        integer=topic/'notes/2026-11-17-parallel-inward-integral-enclosure.py',
        hold=topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py',
        transform=(args.transform_source or Path(__file__).with_name('mean_metric_design.py')).resolve(),
        source=Path(__file__).resolve())
    inputs={key:getattr(args,key.replace('-','_')).resolve()
            for key in ('bundle','carrier','node-report','scalar-input')}
    started=time.monotonic()
    with np.load(inputs['bundle'],allow_pickle=False) as z:
        if 'reference_tail_model_json' not in z.files:
            raise ValueError('This entry consumes the canonical R671 field, not an untagged old bundle')
        model=json.loads(str(z['reference_tail_model_json'].item()))
        lam=float(z['reference_tail_lambda'])
        if model.get('schema')!='R671-exact-reference-tail-lift-v1' or model.get('lambda_value')!=lam or lam<=0:
            raise ValueError('Missing or inconsistent positive-lambda R671 identity')
    exact=load('_r684_exact_tail',paths['exact_tail'])
    transform=load('_r684_mean_metric',paths['transform'])
    context=exact.TailLiftContext.from_files(bundle=inputs['bundle'],carrier=inputs['carrier'],
        node_report=inputs['node-report'],scalar_input=inputs['scalar-input'],
        scalar_source=paths['scalar'],integer_source=paths['integer'],hold_source=paths['hold'],
        observed_source=paths['observed'],eta_start_node=int(model['eta_start_node']),lambda_value=lam)
    op,_=context.create_pair(paths['dense'],paths['batch'],N=args.angles,
        stage_block=args.stage_block,quarter=True)
    x,affine=op.pack(context.data['qjets'],float(context.data['Hcap']),require_affine=True)
    x,identity=context.transfer_seed(op,x,source_lambda=lam,mode='keep-q')
    if not identity.get('physical_field_unchanged'):
        raise ValueError('A read-only diagnostic must not migrate the actual field')
    result=read_all(op,x,transform.MeanMetricTransform,args.legacy_fraction,
        args.spectral_p,args.spectral_epsilon,args.spectral_scale,args.target)
    actual_source_commit=subprocess.run(['git','-C',str(repo),'rev-parse','HEAD'],
        check=True,text=True,capture_output=True).stdout.strip()
    report=dict(schema='R684-same-R671-field-new-mean-metric-diagnostic-v1',
        run_id=os.environ.get('GITHUB_RUN_ID'),run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        source_commit=actual_source_commit,workflow_trigger_sha=os.environ.get('GITHUB_SHA'),
        repository=os.environ.get('GITHUB_REPOSITORY'),
        file_sha256={str(v):sha(v) for v in [*paths.values(),*inputs.values()]},
        source_paths={k:str(v) for k,v in paths.items()},input_paths={k:str(v) for k,v in inputs.items()},
        bundle_sha256=sha(inputs['bundle']),model_definition=context.definition(),
        actual_same_field_check=identity,affine=affine,result=result,
        elapsed_seconds=time.monotonic()-started,
        scope='NEW metric design diagnostic of one unchanged physical field; old metric not met by reinterpretation; final target/parameters must be frozen before actual refinement')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='R684_mean_metric_diagnostic_complete',report=str(args.out),
        report_sha256=sha(args.out),bundle_sha256=report['bundle_sha256'],
        stages=result['stages_read'],old_max=result['original_metric']['maximum_sampled_relative_Gram'],
        variants={k:dict(new_max=v['proposed_new_mean_metric']['maximum_sampled_relative_Gram'],
            removed_Frobenius_fraction=v['exact_finite_mean_variance_split']['removed_fraction'],
            new_target_sampled_pass=v['proposed_new_mean_metric']['sampled_target_pass'])
            for k,v in result['design_variants'].items()},
        field_passes=1,field_changed=False,completion_claimed=False)),flush=True)


if __name__=='__main__':
    main()
