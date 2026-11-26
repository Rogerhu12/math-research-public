#!/usr/bin/env python3
"""Exact-symbolic radial/M/N transfer for ONE fixed deep-valley profile.

This is a complete transfer-only initializer. R676's byte-bound Hermite
restriction, observation inclusion and exact location remapping are reused
on the NEW scalar law; its old canonical-model main/reader is never called.
The actual new scalar carriers and all six lift jets are rebuilt. A complete
fine nonlinear solve and a common-parent-measure comparison follow separately.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
from types import SimpleNamespace

import numpy as np

SCHEMA='same-fixed-deep-scalar-complete-refinement-transfer-v1'
FACTORY_SHA='4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
DEEP_SHA='e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
KERNEL_SHA='2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a'
GEOMETRY_SHA='2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377'
INTERVAL_SHA='f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'
DIFFERENCE_SHA='f3b5acf135589c2ad6f10c80bebf7dfdf919350d4b06e9dbb764ba2a2ca0ade0'
BASE_SHA='2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific fixed-deep-scalar transfer belongs only in public repository Actions')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def record(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size)


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def load(name,path,digest):
    if sha(path)!=digest:raise ValueError('Changed complete refinement source '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def write_json(path,value):
    path=Path(path);temporary=path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    temporary.replace(path)


def event(**value):print(json.dumps(value,allow_nan=False),flush=True)


def source_paths(repo):
    topic=Path(repo)/'topics/visible-flex-larger-amplitude'
    old=topic/'scripts/resume_20261120';new=Path(__file__).resolve().parent
    return dict(factory=new/'deep_valley_reference_factory.py',deep_scalar=new/'deep_valley_tail_input.py',
        base_factory=old/'exact_reference_tail_lift.py',kernel=old/'refine_fixed_g_fullclosed.py',
        geometry_interval=old/'fullclosed_geometry_interval.py',
        interval=topic/'scripts/parallel_20261117_arclength_interval_positive.py',
        difference=old/'fullclosed_C0_difference_interval.py',
        dense=topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        batch=topic/'scripts/resume_20261120_batched_closed_gram.py',
        observed=old/'gauss_observed_closed_gram.py',
        scalar=topic/'notes/2026-11-17-parallel-model-full-hold-oracle.py',
        integer=topic/'notes/2026-11-17-parallel-inward-integral-enclosure.py',
        hold=topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py')


def bind_parent_model(context,paths):
    """Bind actual source records and compare the full canonical definition.

    This validates the scalar/model without building or evaluating a coarse
    field. Exactly these already verified sources are later used by the
    ordinary fine create_pair, whose own independent model equality remains.
    """
    context._operator_sources={role:context.base.source_record(paths[role])
                               for role in ('dense','batch','observed')}
    actual=context.definition()
    if context._prior_definition!=actual:
        raise ValueError('The actual complete parent deep-scalar model does not match its input/source definition')
    return actual


def radial_data(context,paths):
    """Only the documented exact-S Hermite formulas; no old scalar reader."""
    geometry=load('_deep_refine_radial_formulas',paths['geometry_interval'],GEOMETRY_SHA)
    interval=load('_deep_refine_outward_binary',paths['interval'],INTERVAL_SHA)
    difference=load('_deep_refine_affine_interface',paths['difference'],DIFFERENCE_SHA)
    r=geometry.Reader.__new__(geometry.Reader)
    r.I=interval;r.mesh=np.array(context.mesh,copy=True);r.J=len(r.mesh);r.M=context.M;r.n=3*r.M+2
    r.nodes=list(context.nodes);r.width=Q(context.width);r.W=r.fraction(r.width)
    r.S_exact=tuple(Q(value,context.full.h.S) for value in context.full.S)
    r.R_exact=tuple(Q(value,context.deep_module.SCALE) for value in context.deep.R)
    r.S=r.bounds(*r.S_exact);r.R=r.bounds(*r.R_exact);r.nu=2*np.arange(r.M+1)
    d=SimpleNamespace(base=context.data,r=r,I=interval)
    # This method checks only the unchanged literal free-coordinate interface.
    # It does not instantiate or accept the old canonical scalar model.
    difference.Difference.validate_member(d,context.data)
    if (r.nodes[0]!=(Q(0),Q(0)) or r.nodes[-1]!=(Q(1),Q(0))
            or len(r.nodes)!=len(r.mesh)):
        raise ValueError('Keep the full declared exact symbolic radial domain')
    return d


def scalar_carriers(context,plan,nodes,radius,kernel):
    """Fresh same-profile values at every actual new/inherited exact s."""
    values=np.empty(len(plan.cells));errors=np.empty_like(values);time_errors=np.empty_like(values)
    cache={};legacy=[];started=time.monotonic()
    for stage,(cell,u,t) in enumerate(zip(plan.cells,plan.local_u,plan.times)):
        definition=kernel.exact_point(nodes,int(cell),Q(float(u)))
        if definition not in cache:
            abox=context._a_box_at_definition(definition)
            timebox=context.full.affine_time(*definition)
            value=float(Q(abox[0]+abox[1],2*context.deep_module.SCALE))
            if definition==(Q(0),Q(0)):value=1.
            if definition==(Q(1),Q(0)):value=float(radius)
            error=context.base.upper_error(value,abox,context.deep_module.SCALE)
            cache[definition]=(value,error,timebox,abox)
        value,error,timebox,abox=cache[definition]
        values[stage],errors[stage]=value,error
        time_errors[stage]=kernel.upper_float(max(abs(Q(float(t))-Q(edge,context.full.h.S)) for edge in timebox))
        if stage<plan.legacy_count:legacy.append(context.deep_module.enclosure(abox))
        if (stage+1)%512==0:
            event(event='fixed_deep_scalar_refinement_values',stages_done=stage+1,total_stages=len(values),
                unique_exact_queries=len(cache),seconds=time.monotonic()-started)
    if not np.isfinite(values).all() or not np.all(values>0):
        raise ValueError('The same exact fixed profile requires positive finite target carriers')
    return values,errors,time_errors,legacy,dict(unique_exact_point_queries=len(cache),total_rows=len(values),
        maximum_a_carrier_absolute_error=float(errors.max()),maximum_time_carrier_absolute_error=float(time_errors.max()),
        fresh_exact_profile_values_at_every_current_symbolic_point=True,
        old_a_values_interpolated=False,target_fit_or_mean_projection_used=False,
        radius_literal_carrier_preserved=True,
        radius_carrier_absolute_error=context.base.upper_error(radius,context.deep.R,context.deep_module.SCALE),
        exact_profile_identity_sha256=context.deep.model_identity_sha256,
        actual_scalar=context.deep.metadata(),seconds=time.monotonic()-started)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','bundle','carrier','node-report','scalar-input','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--manifest',type=Path,action='append',required=True)
    p.add_argument('--radial-factor',type=int,choices=(1,2),default=2)
    p.add_argument('--modes',type=int)
    p.add_argument('--source-angles',type=int,required=True)
    p.add_argument('--angles',type=int,required=True)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--panels',type=int,default=128)
    p.add_argument('--scalar-admission-seconds',type=float,default=300.)
    p.add_argument('--scalar-integral-tolerance',default='1e-18')
    p.add_argument('--scalar-tail-cutoff',default='1/8')
    a=p.parse_args();require_actions()
    for key in ('repo','bundle','carrier','node_report','scalar_input','outdir'):
        setattr(a,key,getattr(a,key).resolve())
    if a.outdir.exists():raise FileExistsError('Use a new actual refinement transfer directory')
    started=time.monotonic();paths=source_paths(a.repo)
    kernel=load('_deep_refine_complete_R676_kernels',paths['kernel'],KERNEL_SHA)
    expected={key:value for key,value in kernel.EXPECTED.items() if key in paths and key!='factory'}
    expected.update(factory=FACTORY_SHA,deep_scalar=DEEP_SHA,base_factory=BASE_SHA,kernel=KERNEL_SHA)
    for role,path in paths.items():
        if sha(path)!=expected[role]:raise ValueError('Changed actual transfer dependency '+role)
    factory=load('_deep_refine_complete_new_factory',paths['factory'],FACTORY_SHA)
    observed=load('_deep_refine_complete_observation_plan',paths['observed'],expected['observed'])
    with np.load(a.bundle,allow_pickle=False) as raw:
        labels={key:np.array(raw[key],copy=True) for key in raw.files}
    if 'reference_tail_model_json' not in labels:
        raise ValueError('Refine an actual canonical fixed-deep-scalar parent')
    parent_definition=json.loads(str(labels['reference_tail_model_json'].item()))
    if parent_definition.get('schema')!=factory.SCHEMA or parent_definition.get('lambda_value')!=1.:
        raise ValueError('This transfer keeps the genuine new fixed-scalar lambda=1 model')
    parent_context=factory.TailLiftContext.from_files(bundle=a.bundle,carrier=a.carrier,
        node_report=a.node_report,scalar_input=a.scalar_input,scalar_source=paths['scalar'],
        integer_source=paths['integer'],hold_source=paths['hold'],observed_source=paths['observed'],
        eta_start_node=int(parent_definition['eta_start_node']),lambda_value=1.,panels=a.panels,
        base_factory_source=paths['base_factory'],deep_scalar_source=paths['deep_scalar'],
        scalar_admission_seconds=a.scalar_admission_seconds,
        scalar_integral_tolerance=a.scalar_integral_tolerance,scalar_tail_cutoff=a.scalar_tail_cutoff)
    parent_definition=bind_parent_model(parent_context,paths)
    identity=parent_context.deep.model_identity_sha256
    data=parent_context.data;old_nodes=list(parent_context.nodes);old_plan=parent_context.plan
    old_carrier=parent_context._input_carrier_arrays
    oldM=parent_context.M;M=oldM if a.modes is None else a.modes
    ratio=a.angles//a.source_angles if a.source_angles>0 else 0
    if (M<oldM or a.angles<=4*M or a.angles%4 or a.source_angles<=4*oldM
            or a.source_angles%4 or a.angles%a.source_angles or ratio<1 or ratio&(ratio-1)
            or a.stage_block<1 or a.panels<1):
        raise ValueError('Retain all old modes and every old angle in an explicit dyadic supergrid')
    if a.radial_factor==1 and M==oldM and a.angles==a.source_angles:
        raise ValueError('Declare an actual radial, frequency or angular refinement')
    recorded=old_carrier.get('observation_default_full_angles',data.get('refinement_evaluation_full_angles'))
    if recorded is not None and int(recorded)!=a.source_angles:
        raise ValueError('The source angles disagree with the actual current parent carrier')
    d=radial_data(parent_context,paths)
    jets,nodes,mesh,errors,transfer=kernel.restrict_jets(d,M,a.radial_factor)
    transfer['continuous_sixjet_rounding_difference']=kernel.difference_bounds(d.r,nodes,errors,M)
    transfer['continuous_sixjet_rounding_difference']['scope']=(
        'Exact common-S shared-quintic q, identical fixed deep profile/core/H; newly rounded q carriers minus ideal restriction. Numerical scalar carrier approximation is recorded separately.')
    transfer['fixed_scalar_metric_identity_sha256']=identity
    plan,inherited=kernel.combine_observations(observed,mesh,float(data['width']),nodes,old_nodes,old_plan,a.radial_factor)
    radius=float(data['radius'])
    values,scalar_errors,time_errors,legacy_boxes,scalar_info=scalar_carriers(parent_context,plan,nodes,radius,kernel)
    if parent_context.full.carrier(parent_context.full.S)!=float(mesh[-1]):
        raise ValueError('The exact original S and its literal carrier must remain fixed')
    start_symbol=tuple(Q(v) for v in parent_definition['eta_start_symbolic'])
    end_symbol=tuple(Q(v) for v in parent_definition['eta_end_symbolic'])
    start,end=nodes.index(start_symbol),nodes.index(end_symbol)
    if (old_nodes[parent_definition['eta_start_node']]!=start_symbol
            or old_nodes[parent_definition['eta_end_node']]!=end_symbol
            or end_symbol!=(Q(1),-Q(float(data['width'])))):
        raise ValueError('The current physical eta symbols must be literally preserved')
    a.outdir.mkdir(parents=True,exist_ok=False)
    error_path=a.outdir/'transfer-jet-error-boxes.npz'
    np.savez_compressed(error_path,lower=errors[0],upper=errors[1],old_node_to_new=np.arange(len(old_nodes))*a.radial_factor)
    base_arrays=dict(mesh=mesh,a_stages=values[:plan.legacy_count],
        a_stage_absolute_error=scalar_errors[:plan.legacy_count],
        stage_time_absolute_error=time_errors[:plan.legacy_count],qjets=jets,
        radius=np.asarray(data['radius']),width=np.asarray(data['width']),
        fixed_core_first3=np.asarray(data['fixed_core_first3']),Hcap=np.asarray(data['Hcap']),
        core_coefficients=jets[0,0,1:M+1],refinement_evaluation_full_angles=np.array(a.angles))
    carrier_path=a.outdir/'refined-deep-observations.npz'
    arrays=plan.arrays()
    arrays.update({key:base_arrays[key] for key in ('mesh','a_stages','radius','width','fixed_core_first3',
        'a_stage_absolute_error','stage_time_absolute_error')})
    arrays.update(a_observations=values,a_observation_absolute_error=scalar_errors,
        observation_time_absolute_error=time_errors,refinement_parent_stage_map=inherited,
        refinement_parent_carrier_sha256=np.array(sha(a.carrier)),observation_default_full_angles=np.array(a.angles),
        deep_valley_scalar_identity_sha256=np.array(identity),
        quadrature_definition=np.array('one half new six-Gauss plus one half complete parent quadrature; all inherited rows retained with positive mixed weights'))
    np.savez_compressed(carrier_path,**arrays)
    node_path=a.outdir/'refined-deep-symbolic-nodes.json'
    node=dict(schema='deep-valley-fixed-scalar-symbolic-nodes-v1',source_sha256=sha(__file__),
        creation_kind='exact-symbolic-refinement',refinement_kernel_sha256=KERNEL_SHA,
        base_factory_source_sha256=FACTORY_SHA,input_sha256=sha(a.scalar_input),
        S_carrier=float(mesh[-1]),radius_carrier=radius,true_scalar_nodes=[
            dict(S_coefficient=str(alpha),constant=str(beta)) for alpha,beta in nodes],
        scalar_model_identity_sha256=identity,scalar_model_definition=parent_context.deep.definition,
        scalar=parent_context.deep.metadata(),original_fullhold=parent_context.full.metadata(),
        scalar_working_accuracy=parent_context._scalar_working,
        mesh_sha256=parent_context.base.array_sha(mesh),new_carrier_sha256=sha(carrier_path),
        M=M,J=len(nodes),cells=len(nodes)-1,stages=plan.legacy_count,observation_rows=len(plan.cells),
        suggested_operator_N=a.angles,width_exact=parent_definition['width_exact'],
        true_a_stage_boxes=legacy_boxes,maximum_a_observation_absolute_error=float(scalar_errors.max()),
        maximum_stage_time_carrier_absolute_error=float(time_errors.max()),
        new_radius_absolute_carrier_error=scalar_info['radius_carrier_absolute_error'],
        radius_literal_carrier_preserved=True,original_symbolic_S_preserved=True,
        fixed_new_scalar_metric=True,original_fixed_deep_metric_preserved=True,
        parent_node_report=record(a.node_report),parent_observation_carrier=record(a.carrier),
        parent_bundle=record(a.bundle),parent_model_definition=parent_definition,
        refinement=dict(radial_factor=a.radial_factor,source_M=oldM,target_M=M,
            all_old_symbolic_nodes_retained=True,all_old_modes_retained=True,
            exact_profile_definition_unchanged=True,physical_eta_symbolic_unchanged=True),
        numerical_scalar_carriers_are_not_a_new_target_formula=True,
        old_metric_or_geometry_certificates_inherited=False)
    write_json(node_path,node)
    # Generate the genuine new canonical grid/model and let the unchanged
    # NEW factory independently reconstruct and check every field below.
    predicted=json.loads(json.dumps(parent_definition))
    predicted.update(M=M,mesh_sha256=parent_context.base.array_sha(mesh),
        node_report_sha256=sha(node_path),original_observation_carrier_sha256=sha(carrier_path),
        eta_start_node=start,eta_end_node=end,eta_start_carrier=float(mesh[start]),eta_end_carrier=float(mesh[end]))
    if predicted['profile_identity_sha256']!=identity or predicted['profile_definition']!=parent_definition['profile_definition']:
        raise ValueError('A refinement cannot redefine the exact scalar profile')
    provisional=a.outdir/'refined-coordinate-carrier.npz'
    provisional_arrays=dict(base_arrays,reference_tail_lambda=np.array(1.),exact_tail_lambda=np.array(1.),
        exact_tail_eta_start_node=np.array(start),reference_tail_model_json=np.array(json.dumps(predicted,sort_keys=True)),
        fixed_new_scalar_metric_identity_sha256=np.array(identity))
    np.savez_compressed(provisional,**provisional_arrays)
    context=factory.TailLiftContext.from_files(bundle=provisional,carrier=carrier_path,node_report=node_path,
        scalar_input=a.scalar_input,scalar_source=paths['scalar'],integer_source=paths['integer'],
        hold_source=paths['hold'],observed_source=paths['observed'],eta_start_node=start,lambda_value=1.,panels=a.panels,
        base_factory_source=paths['base_factory'],deep_scalar_source=paths['deep_scalar'],
        scalar_admission_seconds=a.scalar_admission_seconds,scalar_integral_tolerance=a.scalar_integral_tolerance,
        scalar_tail_cutoff=a.scalar_tail_cutoff)
    problem,_=context.create_pair(paths['dense'],paths['batch'],N=a.angles,stage_block=a.stage_block,quarter=True)
    actual=context.definition()
    if (actual!=predicted or actual['profile_definition']!=parent_definition['profile_definition']
            or actual['profile_identity_sha256']!=identity
            or tuple(Q(v) for v in actual['eta_start_symbolic'])!=start_symbol
            or tuple(Q(v) for v in actual['eta_end_symbolic'])!=end_symbol
            or float(problem.R).hex()!=radius.hex()):
        raise ValueError('The actual fine factory changed the fixed profile, physical eta or shared radius carrier')
    profile_path=a.outdir/'refined-deep-reference-profiles.npz'
    profile_json=a.outdir/'refined-deep-reference-profiles.json'
    profile=context.save_carrier(profile_path,profile_json)
    x,affine=problem.pack(jets,float(data['Hcap']),require_affine=True)
    affine.update(representation=factory.SCHEMA,fixed_scalar_metric_identity_sha256=identity)
    final_arrays=context.bundle_arrays(problem,x)
    final_arrays.update(exact_tail_lambda=np.array(1.),exact_tail_eta_start_node=np.array(start),
        field_representation=np.array(factory.SCHEMA),refinement_evaluation_full_angles=np.array(a.angles),
        fixed_new_scalar_metric_identity_sha256=np.array(identity))
    final=a.outdir/'refined-deep-seed.npz';np.savez_compressed(final,**final_arrays)
    locations,ancestry=kernel.remap_manifests(a.manifest,a.carrier,old_plan,old_nodes,nodes,a.radial_factor,a.source_angles)
    location_path=a.outdir/'refined-deep-permanent-locations.json'
    location=dict(schema='fixed-deep-scalar-exact-refinement-location-transfer-v1',
        carrier_sha256=sha(carrier_path),bundle_sha256=sha(final),fixed_scalar_metric_identity_sha256=identity,
        parent_bundle_sha256=sha(a.bundle),parent_carrier_sha256=sha(a.carrier),
        refinement_source_sha256=sha(__file__),sources=ancestry,**locations,
        remapping='Exact dyadic symbolic s; every binary phi preserved; no decimal merge',
        all_declared_exact_locations_retained=True,old_geometry_or_metric_values_inherited=False)
    location_path.write_text(json.dumps(location,separators=(',',':'),allow_nan=False)+'\n')
    report=dict(schema=SCHEMA,source_sha256=sha(__file__),
        source_commit=subprocess.check_output(['git','-C',str(a.repo),'rev-parse','HEAD'],text=True).strip(),
        execution={key:os.environ.get(key) for key in ('GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA')},
        sources={key:record(path) for key,path in paths.items()},
        inputs=dict(bundle=record(a.bundle),carrier=record(a.carrier),node_report=record(a.node_report),scalar_input=record(a.scalar_input)),
        outputs=dict(bundle=record(final),carrier=record(carrier_path),node_report=record(node_path),
            permanent_locations=record(location_path),transfer_error_boxes=record(error_path),
            reference_carrier=record(profile_path),reference_manifest=record(profile_json)),
        fixed_scalar_metric_identity_sha256=identity,parent_model=parent_definition,refined_model=actual,
        transfer=transfer,exact_affine_seed=affine,scalar_preparation=scalar_info,
        new_complete_scalar_profiles=profile,refined_context=context.metadata(),
        physical_eta=dict(parent_start_node=parent_definition['eta_start_node'],refined_start_node=start,
            parent_end_node=parent_definition['eta_end_node'],refined_end_node=end,
            same_start_symbolic=[str(v) for v in start_symbol],same_end_symbolic=[str(v) for v in end_symbol]),
        observations=dict(parent_rows=len(old_plan.cells),new_rows=len(plan.cells),refined_legacy_rows=plan.legacy_count,
            inherited_row_mapping_complete=True,positive_row_weights=True,legacy_fraction=.5,
            inherited_scalar_carriers_bitwise_equal=bool(np.array_equal(values[inherited],old_carrier['a_observations'])),
            maximum_inherited_target_carrier_difference=float(np.max(np.abs(values[inherited]-old_carrier['a_observations']))),
            new_values_from_same_exact_profile=True,new_target_fitted=False,
            parent_measure_comparison_requires_parent_literal_a_carriers=True,
            quadrature_mixture='one half new six-Gauss plus one half complete parent quadrature',
            old_positive_rows_and_weights_present=True),
        angular_refinement=dict(source_full_angles=a.source_angles,refined_full_angles=a.angles,
            dyadic_angle_multiplier=ratio,all_original_angles_retained=True),
        nonlinear_solve_performed=False,finite_metric_or_geometry_readout_performed=False,
        coarse_parent_field_or_J_evaluated=False,old_candidate_certificates_inherited=False,
        same_fixed_profile_preserved=True,radius_literal_carrier_preserved=True,
        fixed_g_refinement_convergence_demonstrated=False,topic_complete=False,seconds=time.monotonic()-started)
    report_path=a.outdir/'refinement-report.json';write_json(report_path,report)
    event(event='fixed_deep_scalar_refinement_transfer_returned',report=record(report_path),
        profile_identity=identity,source_J=len(old_nodes),target_J=len(nodes),source_M=oldM,target_M=M,
        source_eta=parent_definition['eta_start_node'],target_eta=start,
        parent_rows=len(old_plan.cells),target_rows=len(plan.cells),
        actual_nonlinear_solve_performed=False,seconds=report['seconds'])


if __name__=='__main__':main()
