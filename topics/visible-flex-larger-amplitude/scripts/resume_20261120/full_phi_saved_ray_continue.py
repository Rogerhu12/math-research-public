#!/usr/bin/env python3
"""Continue an actually accepted original-lift ray after a fresh Phi derivative.

No new QP or J product is performed. Every proposed point is evaluated with
all original/Gauss rows and every permanent curvature/radius location. This
is a finite nonlinear line search, never a continuous geometry certificate.
The separate R671 lift factory is deliberately not inferred from old files.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def safe(value):
    if isinstance(value,float) and not math.isfinite(value):
        return dict(nonfinite_value=repr(value))
    if isinstance(value,dict):return {key:safe(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):return [safe(item) for item in value]
    return value


def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(safe(value),ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',type=Path,required=True)
    parser.add_argument('--slope',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--line-trials',type=int,default=15)
    parser.add_argument('--max-increment',type=float,default=2.)
    parser.add_argument('--armijo',type=float,default=1e-4)
    args=parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise RuntimeError('Scientific execution belongs in the authorized public repository Actions')
    if (args.line_trials<1 or not math.isfinite(args.max_increment) or args.max_increment<=0
            or not 0<args.armijo<1):
        raise ValueError('Positive finite declared ray budget and Armijo factor required')
    if args.outdir.exists():raise FileExistsError(args.outdir)
    started=time.monotonic()
    args.report=args.report.resolve();args.slope=args.slope.resolve();args.outdir=args.outdir.resolve()
    parent=json.loads(args.report.read_text());slope_record=json.loads(args.slope.read_text())
    driver_path=Path(__file__).with_name('fullclosed_gauss_inequality_qp.py')
    slope_path=Path(__file__).with_name('full_phi_saved_ray_slope.py')
    if parent.get('source_sha256')!=sha(driver_path):
        raise ValueError('This consumer uses only the unchanged original-lift complete-QP driver')
    if (slope_record.get('source_sha256')!=sha(slope_path)
            or slope_record.get('input_report_sha256')!=sha(args.report)):
        raise ValueError('The fresh derivative does not belong to this exact report and reader')
    directions=parent.get('directions',[])
    if not parent.get('complete') or parent.get('objective')!='spectral' or len(directions)!=1 or not directions[0].get('accepted'):
        raise ValueError('Use an actual completed accepted single spectral direction')
    direction=directions[0]
    bundle=Path(parent['final_bundle']);carrier_path=Path(parent['observation_carrier'])
    step_path=args.report.parent/('direction-%03d.npz'%direction['index'])
    for path,expected in ((bundle,parent['final_bundle_sha256']),
            (carrier_path,parent['observation_carrier_sha256']),
            (step_path,direction['direction_sha256'])):
        if sha(path)!=expected:raise ValueError('Actual saved input changed: '+str(path))
    if (slope_record.get('accepted_bundle_sha256')!=sha(bundle)
            or slope_record.get('direction_sha256')!=sha(step_path)
            or slope_record.get('observation_carrier_sha256')!=sha(carrier_path)):
        raise ValueError('The derivative identities differ from this accepted ray')
    args.outdir.mkdir(parents=True)
    output=args.outdir/'report.json'
    result=dict(schema='actual-accepted-original-lift-ray-continuation-v1',
        source_sha256=sha(__file__),source_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        github_run_id=os.environ.get('GITHUB_RUN_ID'),github_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        input_report=str(args.report),input_report_sha256=sha(args.report),
        slope_report=str(args.slope),slope_report_sha256=sha(args.slope),
        parent_bundle=str(bundle),parent_bundle_sha256=sha(bundle),
        observation_carrier=str(carrier_path),observation_carrier_sha256=sha(carrier_path),
        saved_direction=str(step_path),saved_direction_sha256=sha(step_path),
        source_paths=parent['source_paths'],source_sha256_by_role=parent['source_sha256_by_role'],
        original_driver_sha256=sha(driver_path),fresh_slope_reader_sha256=sha(slope_path),
        numerical_safety=parent['numerical_reach_safety_factor'],requested_reach_ratio=parent['requested_reach_ratio'],
        line_trials=args.line_trials,max_increment=args.max_increment,armijo=args.armijo,
        parameterization='x_accepted + eta * original_saved_full_free_step; eta is an increment after the recorded accepted alpha',
        new_QP_directions=0,new_JVP_calls=0,new_VJP_calls=0,actual_residual_evaluations=0,
        residual_count_scope='Attempted calls, including a call that raises a numerical exception',
        actual_complete_geometry_evaluations=0,accepted=False,complete=False,trials=[],
        continuous_geometry_certified=False,continuous_metric_certified=False,
        fixed_g_refinement_completed=False,README_completion_claimed=False)
    true_slope=slope_record.get('true_current_Phi_directional_derivative')
    prior_stats=parent.get('current',parent['initial'])
    parent_filter=parent['final_curvature_filter']
    parent_domain=all(prior_stats[key]>0 for key in ('rho_sample_min','min_relative_E','min_relative_determinant'))
    margin=parent['numerical_reach_safety_factor']-parent_filter['necessary_reach_product']
    additional_cap=parent.get('sampled_curvature_cap')
    strict_geometry=margin>0 and (additional_cap is None or parent_filter['sampled_curvature']<additional_cap)
    eligible=(slope_record.get('status')=='actual_accepted_field_derivative_returned'
        and isinstance(true_slope,(int,float)) and math.isfinite(true_slope) and true_slope<0
        and parent_domain and parent_filter.get('passed') and strict_geometry)
    result.update(true_current_Phi_directional_derivative=true_slope,
        positive_finite_domain_margin=bool(parent_domain),strict_known_point_margin=bool(strict_geometry),
        known_point_product_from_hashed_parent_report=parent_filter['necessary_reach_product'],
        parent_geometry_reread=False,conditional_local_descent_hypotheses_observed=bool(eligible))
    if not eligible:
        result.update(status='no_extension_without_negative_fresh_slope_and_strict_retained_margins',
            initial=prior_stats,current=prior_stats,final_curvature_filter=parent_filter,
            final_curvature_memory=parent['final_curvature_memory'],final_radius_memory=parent['final_radius_memory'])
        final=args.outdir/'final.npz';shutil.copyfile(bundle,final)
        result.update(final_bundle=str(final),final_bundle_sha256=sha(final),
            final_is_exact_parent_copy=True,complete=True,seconds=time.monotonic()-started)
        save(output,result);print(json.dumps(dict(event=result['status'],report_sha256=sha(output))),flush=True)
        return
    import numpy as np
    np.seterr(over='raise',invalid='raise',divide='raise',under='ignore')
    paths={key:Path(value) for key,value in parent['source_paths'].items()}
    required=('operator','implementation','base_batch','helpers','spectral','geometry','observed_geometry','point')
    for role in required:
        if sha(paths[role])!=parent['source_sha256_by_role'][role]:
            raise ValueError('An actually used source changed: '+role)
    observed=load('ray_extend_observed',paths['implementation'])
    batch=load('ray_extend_batch',paths['base_batch'])
    helper=load('ray_extend_statistics',paths['helpers'])
    spectral=load('ray_extend_spectral',paths['spectral'])
    geometry_module=load('ray_extend_geometry',paths['geometry'])
    observed_geometry=load('ray_extend_observed_geometry',paths['observed_geometry'])
    point_module=load('ray_extend_point_geometry',paths['point'])
    original_driver=load('ray_extend_original_full_driver',driver_path)
    geometry_module.fields_block=observed_geometry.fields_block_observed
    with np.load(bundle,allow_pickle=False) as z:data={key:np.array(z[key]) for key in z.files}
    with np.load(carrier_path,allow_pickle=False) as z:carrier={key:np.array(z[key]) for key in z.files}
    with np.load(step_path,allow_pickle=False) as z:step=np.array(z['step'])
    for key in ('mesh','a_stages','radius','width','fixed_core_first3'):
        if not np.array_equal(data[key],carrier[key]):raise ValueError('Retain the actual same-g carrier: '+key)
    plan=observed.ObservationPlan.from_arrays(carrier)
    o=observed.create(paths['operator'],data['mesh'],data['a_stages'],float(data['radius']),
        data['fixed_core_first3'],M=(data['qjets'].shape[-1]-2)//3,N=parent['N'],
        width=float(data['width']),stage_block=64,quarter=True,batch_source=batch,
        observation_plan=plan,a_observations=carrier['a_observations'])
    x,affine=o.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    if step.shape!=x.shape or not np.isfinite(step).all():raise ValueError('The stored complete direction uses another space')
    parameters_record=direction['quadratic_model']['bridge']['blocks']
    parameters=spectral.Parameters(p=parameters_record['p'],epsilon=parameters_record['epsilon'],scale=parameters_record['scale'])
    weights=o.mixed_stage_weights(parent['radial_weights']['legacy_fraction'])
    normalizer=float(weights.sum()*o.full_N)
    witnesses=[dict(value) for value in parent['final_curvature_memory']]
    radius_witnesses=[dict(value) for value in parent['final_radius_memory']]
    if not witnesses or not radius_witnesses:raise ValueError('Retain both complete permanent location lists')
    def statistics(point,error):
        stats=helper.statistics(o,point,error)
        cost=np.sum(error[:,:,0]**2+2*error[:,:,1]**2+error[:,:,2]**2,axis=1)
        weighted=float(weights@cost)
        stats.update(all_raw_frobenius_sse=float(cost.sum()),legacy_raw_frobenius_sse=float(cost[:o.legacy_P].sum()),
            radial_weighted_frobenius_sse=weighted,radial_weighted_mean_sse=weighted/normalizer)
        raw=o.unweight(error).reshape(o.P,o.N,3)
        stats['spectral']=spectral.statistics(raw,weights,o.multiplicity,parameters)
        return stats
    def geometry(point):
        result['actual_complete_geometry_evaluations']+=1
        value=original_driver.point_geometry(o,point)
        value['observation_grid_worst']=value.get('worst')
        value['observation_grid_maximum_curvature']=value.get('maximum_absolute_principal_curvature')
        value['arbitrary_witnesses']=[]
        if not value['complete']:return value
        prepared=o.prepare(point)
        for witness in witnesses+radius_witnesses:
            item=point_module.witness_geometry(o,prepared,witness,geometry_module,observed)
            value['arbitrary_witnesses'].append(item)
            if not item['complete']:
                value['complete']=False;return value
            if item['maximum_absolute_principal_curvature']>value['maximum_absolute_principal_curvature']:
                value['maximum_absolute_principal_curvature']=item['maximum_absolute_principal_curvature']
                value['worst']=dict(kind='arbitrary_witness',**{k:item[k] for k in ('cell','u','phi','s')})
            if 2*item['radius']>value['closed_body_diameter_point_lower']:
                value['closed_body_diameter_point_lower']=2*item['radius']
                value['maximum_radius_point']=dict(kind='arbitrary_witness',**{k:item[k] for k in ('cell','u','phi','s')})
            value['min_area']=min(value['min_area'],item['area'])
        value['additional_witness_point_count']=len(witnesses)+len(radius_witnesses)
        return value
    def curvature_filter(point,value):
        _,height,_=o.unpack(point)
        D=max(2.,2*abs(float(height)),value.get('closed_body_diameter_point_lower',0.))
        ratio=parent['requested_reach_ratio'];safety=parent['numerical_reach_safety_factor']
        cap=safety/(ratio*D)
        if additional_cap is not None:cap=min(cap,additional_cap)
        K=value.get('maximum_absolute_principal_curvature',float('inf'))
        return dict(passed=bool(value['complete'] and K<=cap),height=float(height),
            reference_diameter_lower_bound=D,applied_curvature_cap=cap,sampled_curvature=K,
            necessary_reach_product=ratio*D*K,
            scope='All original and Gauss observations plus all retained arbitrary positions; necessary finite screen only')
    def remember(location,destination):
        if location is None:return None
        if 'stage' in location:
            stage=int(location['stage']);point=dict(cell=int(o.observation_cells[stage]),
                u=float(o.observation_u[stage]),phi=float(location['phi']))
        else:point={key:location[key] for key in ('cell','u','phi')}
        key=lambda p:(int(p['cell']),round(float(p['u']),13),round(float(p['phi']),13))
        if any(key(point)==key(old) for old in destination):return None
        destination.append(point);return point
    result['actual_residual_evaluations']+=1;initial_error=o.residual(x)
    current=statistics(x,initial_error);old_phi=current['spectral']['phi_normalized']
    result.update(initial=current,current=current,affine=affine,
        fresh_initial_Phi_minus_accepted_report=old_phi-prior_stats['spectral']['phi_normalized'],
        original_full_rows=3*o.P*o.full_N,original_variables=o.free_size,
        original_curvature_location_count=len(witnesses),original_radius_location_count=len(radius_witnesses))
    estimate=slope_record.get('residual_Hessian_model_increment')
    increment=min(args.max_increment,estimate) if isinstance(estimate,(int,float)) and math.isfinite(estimate) and estimate>0 else args.max_increment
    result['initial_increment']=increment
    final_filter=parent_filter
    save(output,result)
    for index in range(args.line_trials):
        point=x+increment*step
        error_text=None;stats={};curvature=None;filter_result=None
        try:
            result['actual_residual_evaluations']+=1;residual=o.residual(point)
            finite=bool(np.isfinite(residual).all())
            if finite:stats=statistics(point,residual)
            phi=stats['spectral']['phi_normalized'] if finite else None
            feasible=bool(finite and all(stats[key]>0 for key in ('rho_sample_min','min_relative_E','min_relative_determinant')))
            descent=bool(finite and phi<old_phi and phi<=old_phi+args.armijo*increment*true_slope)
            if feasible and descent:
                curvature=geometry(point);filter_result=curvature_filter(point,curvature)
        except (FloatingPointError,OverflowError) as error:
            finite=feasible=descent=False;phi=None;error_text=repr(error)
        accepted=bool(feasible and descent and filter_result is not None and filter_result['passed'])
        trial=dict(index=index,increment=increment,total_original_ray_parameter=direction['accepted_alpha']+increment,
            finite=finite,feasible=feasible,descent=descent,accepted=accepted,statistics=stats,
            Phi=phi,curvature_filter=filter_result,curvature_points=curvature,arithmetic_error=error_text,
            new_permanent_curvature_locations=[],new_permanent_radius_locations=[])
        if curvature is not None:
            for loc in (curvature.get('observation_grid_worst'),curvature.get('worst')):
                p=remember(loc,witnesses)
                if p is not None:trial['new_permanent_curvature_locations'].append(p)
            p=remember(curvature.get('maximum_radius_point'),radius_witnesses)
            if p is not None:trial['new_permanent_radius_locations'].append(p)
        result['trials'].append(trial)
        print(json.dumps(safe(dict(event='saved_ray_actual_trial',index=index,increment=increment,Phi=phi,
            finite=finite,feasible=feasible,descent=descent,accepted=accepted,curvature_filter=filter_result))),flush=True)
        if accepted:
            x=point;current=stats;final_filter=filter_result
            result.update(accepted=True,accepted_increment=increment,
                accepted_total_original_ray_parameter=direction['accepted_alpha']+increment,current=current)
            save(output,result);break
        save(output,result);increment/=2
    final=args.outdir/'final.npz'
    if result['accepted']:
        jets,height,_=o.unpack(x)
        arrays={key:data[key] for key in ('mesh','a_stages','radius','width','fixed_core_first3','a_stage_absolute_error','stage_time_absolute_error') if key in data}
        arrays.update(qjets=jets,Hcap=np.array(height));np.savez_compressed(final,**arrays)
    else:shutil.copyfile(bundle,final)
    # Every newly found position is explicitly reread on the final member.
    # This includes an accepted new member and an unchanged retained parent.
    if (len(witnesses)!=result['original_curvature_location_count']
            or len(radius_witnesses)!=result['original_radius_location_count']):
        final_filter=curvature_filter(x,geometry(x))
    result.update(status='actual_saved_ray_search_returned',complete=True,current=current,
        final_bundle=str(final),final_bundle_sha256=sha(final),final_is_exact_parent_copy=not result['accepted'],
        final_curvature_filter=final_filter,final_curvature_memory=witnesses,final_radius_memory=radius_witnesses,
        final_known_point_safety_pass=final_filter['passed'],
        sample_target_reached=current['max_relative_gram']<=parent['target'],
        process_peak_rss_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),seconds=time.monotonic()-started)
    save(output,result)
    print(json.dumps(dict(event='saved_ray_search_complete',accepted=result['accepted'],
        final_bundle_sha256=sha(final),Phi=current['spectral']['phi_normalized'],
        max_relative_gram=current['max_relative_gram'],product=final_filter['necessary_reach_product'],
        final_known_point_safety_pass=final_filter['passed'],seconds=result['seconds'])),flush=True)


if __name__=='__main__':main()
