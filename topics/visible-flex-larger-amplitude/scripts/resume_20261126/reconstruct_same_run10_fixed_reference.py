#!/usr/bin/env python3
"""Regenerate run10's complete fixed reference, with truthful new-run provenance.

Only actual source-bound warm inputs are consumed. The complete 2218-leaf
integer table replaces the origin's time-dependent admission stopping rule.
All original 7377 observations, complete cached four scalar jets, their errors,
initial H, mesh and full 160-word chart are reconstructed. Whole 71f/512f/081
and e711/b240 matches are required before same-reference input is returned.
The origin's scalar/node file hashes stay ORIGIN provenance; new files have
their actual hashes. No old nonlinear direction, final point or typed list is
invented. The complete original reference context is initialized through an
explicit new constructor; the old 4e constructor/guards are not modified.
Scientific input reconstruction is restricted to public repository Actions.
"""
import argparse
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

TOPIC='topics/visible-flex-larger-amplitude'
SCHEMA='R690-independent-axisymmetric-SO3-reference-input-v1'
PREPARATION_SCHEMA='complete-reconstructed-run10-reference-preparation-v1'
REPORT_SCHEMA='actual-complete-same-run10-reference-regeneration-v1'
BRIDGE_NAME='same_run10_frozen_reference_input_binding.py'
BRIDGE_SHA='5aee3276dc2c70a3adc52dda618494a8ef458f4b1496c34a5c2640c00a5735b0'
ORIGIN_PRODUCER_NAME='freeze_run10_public_reference_and_restore_run05_carrier.py'
ORIGIN_PRODUCER_SHA='fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a'
ORIGIN_BINDER_SHA='9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209'
REFERENCE_NAME='so3_axisymmetric_reference.py'
REFERENCE_SHA='4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
TARGET_SCHEMA='independently-frozen-actual-public-run10-scalar-and-material-chart-v1'
WARM_SOURCE_SHA='bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3'
ORIGIN_MESH_SHA='eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262'
PARAMETERS_SHA='e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa'
ORIGIN_CHART_SHA='90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e'
ORIGIN_PARAMETERS_SHA='d7c6fd9d571542f9c17f3ddc4e7ace589025ca74b69246c45b0c2e4239b8c088'
OLD_RECORD_SHA='6eca69a388330b3e539aac4e2c793ce8256c724d52abf11adc8c8e85d49d08b3'
OLD_STEP='independent-axisymmetric-R690-reference-prepare-v2-first-20261126-05'

def require_actions():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        raise RuntimeError('Complete numerical input reconstruction requires public repository Actions')

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def record(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)

def load(name,path,expected):
    if sha(path)!=expected:raise ValueError('The complete source changed: '+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:raise ValueError('Complete source cannot be loaded')
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    return module

def bridge_module():
    return load('_same_run10_reference_bridge',Path(__file__).with_name(BRIDGE_NAME),BRIDGE_SHA)

def write_json(path,value):
    p=Path(path);temporary=p.with_name(p.name+'.tmp')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n');temporary.replace(p)

def event(**value):
    print(json.dumps(value,sort_keys=True,allow_nan=False),flush=True)

def verify_origin_contract(path):
    if sha(path)!=ORIGIN_PARAMETERS_SHA:raise ValueError('Use all original recorded parameters')
    value=json.loads(Path(path).read_text())
    if value.get('schema')!='complete-run10-fixed-reference-continuation-origin-parameters-v1':
        raise ValueError('The complete origin parameter schema changed')
    if canonical(value['origin_public_input_evidence'])!='47a8fa781713388379a6de4c259f4ddf7f810e1b3d69c63f8630565031b761ef':
        raise ValueError('The original public evidence was not reconstructed exactly')
    if value['complete_actual_reference_record']['metrics']['axisymmetric-R690-reference-v2-first/report.json']['scalar_leaves']!=2218:
        raise ValueError('Keep the actual current table size, not historical 2397')
    return value

def reconstruct_origin_target(origin,model,parameters,definitions,core):
    # This exactly regenerates the origin DEFINITION. It is not a new execution
    # of the old public binder and its paths are not dereferenced as new files.
    evidence=copy.deepcopy(origin['origin_public_input_evidence'])
    actual=dict(model=model,complete_scalar_parameters=parameters,
        exact_scalar_node_definitions=[[str(a),str(b)] for a,b in definitions],
        fixed_chart_core_binary64_hex=[float(v).hex() for v in core],
        fixed_chart_core_array_record=bridge_module().original_word_reader().chart_record([float(v).hex() for v in core]))
    equal=actual['fixed_chart_core_array_record']['sha256']==ORIGIN_CHART_SHA
    return dict(schema=TARGET_SCHEMA,definition_source_sha256=ORIGIN_PRODUCER_SHA,
        public_input_binding_source_sha256=ORIGIN_BINDER_SHA,
        complete_public_input_evidence=copy.deepcopy(evidence),
        complete_public_input_evidence_identity_sha256=canonical(evidence),
        complete_current_reference_model=copy.deepcopy(model),
        current_reference_model_identity_sha256=canonical(model),
        complete_current_reference_bundle_sha256=evidence['current_files']['current_reference_bundle']['sha256'],
        complete_scalar_parameters=copy.deepcopy(actual['complete_scalar_parameters']),
        complete_scalar_parameters_identity_sha256=PARAMETERS_SHA,
        complete_current_fixed_scalar_profile_definition=copy.deepcopy(model['fixed_scalar_profile_definition']),
        current_fixed_scalar_metric_identity_sha256=model['fixed_scalar_metric_identity_sha256'],
        fixed_chart_core_binary64_hex=list(actual['fixed_chart_core_binary64_hex']),
        fixed_chart_core_array_record=copy.deepcopy(actual['fixed_chart_core_array_record']),
        exact_scalar_node_definitions=copy.deepcopy(actual['exact_scalar_node_definitions']),
        exact_scalar_node_definitions_identity_sha256=canonical(actual['exact_scalar_node_definitions']),
        exact_node_recipe_source_sha256=WARM_SOURCE_SHA,complete_literal_mesh_array_sha256=ORIGIN_MESH_SHA,
        exact_literal_width_hex=float(.05).hex(),
        mathematical_target='ds^2+a_R690(s)^2*dTheta_actual_run10(phi0)^2',
        fixed_chart='all 160 literal actual reference coefficients are frozen in this definition',
        original_complete_scalar_source_sha256=REFERENCE_SHA,
        historical_original_chart_core_sha256=ORIGIN_CHART_SHA,
        current_and_historical_fixed_chart_words_sha_equal=equal,
        same_original_fixed_chart=equal,same_mathematical_g_claimed=False,
        historical_metric_relation='not claimed by this independent input; unequal metadata identities are not a mathematical inequality',
        independently_bound_target_identity=True,old_target_identity_inherited=False,
        exact_old_to_new_chart_conjugacy_claimed=False,target_fixed_before_any_field_or_direction=True,
        current_free_core_does_not_redefine_target=True,current_free_height_is_not_a_target_parameter=True,
        old_and_current_literal_material_addresses_all_retained=True,
        historical_angles_reinterpreted_as_new_fixed_chart_phi0=True,
        same_historical_physical_points_claimed=False,
        unknown_parallel_typed_priorities_reconstructed=False,
        unresolved_parallel_history_remains_an_explicit_obligation=True,
        original_branch_replaced_or_declared_finished=False,
        old_field_values_or_scientific_certificates_inherited=False)

def generate_carrier(ref,modules,full,deep,plan,definitions,mesh,core,width,path):
    import numpy as np
    d=modules['deep_scalar']
    a,ae,te=[],[],[]
    for index,(cell,u,tc) in enumerate(zip(plan.cells,plan.local_u,plan.times)):
        definition=ref.point_definition(definitions,int(cell),float(u))
        value,error=ref.midpoint_and_error(ref.target_a_box(full,deep,d,definition),d.SCALE)
        a.append(value);ae.append(error)
        sb=full.affine_time(*definition)
        te.append(ref.upper_float(max(abs(F(float(tc))-F(sb[0],full.h.S)),
            abs(F(float(tc))-F(sb[1],full.h.S)))))
        if (index+1)%1024==0:
            event(event='complete_reference_observations_reconstructed',
                source_profile_identity=deep.model_identity_sha256,completed=index+1,total=7377)
    a,ae,te=np.asarray(a),np.asarray(ae),np.asarray(te)
    if not np.isfinite(a).all() or np.any(a<=0):raise ArithmeticError('Every fixed observation must remain positive')
    radius,radius_error=ref.midpoint_and_error(deep.R,d.SCALE)
    np.savez_compressed(path,**plan.arrays(),mesh=mesh,a_stages=a[:1845],
        a_observations=a,a_observation_absolute_error=ae,observation_time_absolute_error=te,
        radius=np.array(radius),width=np.array(width),fixed_core_first3=core[:3],
        fixed_scalar_metric_identity_sha256=np.array(deep.model_identity_sha256))
    return a,radius,radius_error

def generate_reference(ref,modules,full,deep,plan,definitions,warm,origin,raw,outdir):
    import numpy as np
    mesh=np.array(warm['mesh'],copy=True)
    core=np.array(warm['qjets'][0,0,1:161],copy=True)
    width=float(warm['width'])
    carrier_path=outdir/'observations.npz'
    a,radius,radius_error=generate_carrier(ref,modules,full,deep,plan,definitions,mesh,core,width,carrier_path)
    if sha(carrier_path)!='71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d' or carrier_path.stat().st_size!=227202:
        raise ArithmeticError('Reconstructed complete run10 carrier words differ; no same-input claim')
    law=ref.WholeAxisymmetricLaw(full,modules['deep_scalar'],tail_cutoff='1/8')
    gx,gw=np.polynomial.legendre.leggauss(8)
    gu,gw=(gx+1)/2,gw/2
    cells,local=np.repeat(np.arange(922),8),np.tile(gu,922)
    addresses,cv,ce,seen=[],[],[],set()
    for cell,u in zip(np.r_[cells,plan.cells],np.r_[local,plan.local_u]):
        key=(int(cell),float(u).hex())
        if key in seen:continue
        seen.add(key)
        value,error=law.at(ref.point_definition(definitions,int(cell),float(u)))
        addresses.append((int(cell),float(u)));cv.append(value);ce.append(error)
        if len(addresses)%1024==0:
            event(event='complete_reference_four_scalar_jets_reconstructed',completed=len(addresses))
    lookup={(cell,u.hex()):v for (cell,u),v in zip(addresses,cv)}
    iv=np.array([lookup[(int(cell),float(u).hex())] for cell,u in zip(cells,local)])
    b,c=iv[:,0],iv[:,1]
    normalized_c=c/np.sqrt(b*b+c*c)
    height=float(np.sum(np.sum(normalized_c.reshape(922,8)*gw[None],axis=1)*np.diff(mesh)))
    if not math.isfinite(height):raise ArithmeticError('Nonfinite original complete height seed')
    origin_files=origin['origin_public_input_evidence']['current_files']
    model = dict(schema=SCHEMA,source_sha256=REFERENCE_SHA,
        fixed_scalar_metric_identity_sha256=deep.model_identity_sha256,fixed_scalar_profile_definition=deep.definition,
        scalar_input_sha256=origin_files['current_scalar_input']['sha256'],original_scalar_parameters_identity_sha256=canonical(ref.scalar_parameters(raw)),
        symbolic_node_report_sha256=origin_files['current_node_report']['sha256'],original_warm_bundle_sha256=origin_files['current_warm_bundle']['sha256'],
        observation_carrier_sha256=sha(carrier_path),mesh_sha256=ref.array_sha(mesh),M=160,J=923,
        fixed_chart_core_sha256=ref.array_sha(core),fixed_core_first3=[float(v).hex() for v in core[:3]],
        radius_carrier_hex=radius.hex(),radius_error_upper=radius_error,
        radius_definition='Exact R690 terminal radius, with a bound working carrier',
        radius_complete_enclosure=modules['deep_scalar'].enclosure(deep.R),
        a_observations_sha256=ref.array_sha(a),working_scalar_tail_cutoff=str(F('1/8')),
        exact_domain='Original complete affine-in-S 923-node mesh and exact original S',
        frozen_chart='theta0(phi)=Theta_initial_warm_core(phi); every current free core may change',
        T0='a_s er(theta0)+c ez; c>=0,a_s^2+c^2=1; complete prefix/Hold/R690 law',
        T0_ports='T0(0)=ez; T0_s,z(0)=0; T0(S)=-er(theta0); T0_s(S)=0',
        fixed_metric='ds^2+a_deep(s)^2*dtheta0^2',
        old_optimized_q_field_required=False,old_nonlinear_directions_required=False,
        initial_height_rule='Working whole-cell Gauss integral of normalized c; free H, not an exact integral claim',
        seed_integration_order=int(8),all_original_free_core_coefficients_retained=True)
    if canonical(model)!=origin['origin_reference_model_identity_sha256']:
        raise ArithmeticError('The regenerated complete original reference model differs')
    reference_path=outdir/'reference.npz'
    np.savez_compressed(reference_path,schema=np.array(SCHEMA),mesh=mesh,initial_core=core,
        initial_height=np.array(height),original_warm_height=np.array(float(warm['Hcap'])),
        radius=np.array(radius),width=np.array(width),fixed_core_first3=core[:3],
        cached_scalar_cells=np.array([cell for cell,u in addresses],dtype=np.int64),
        cached_scalar_local=np.array([u for cell,u in addresses]),cached_scalar_values=np.asarray(cv),
        cached_scalar_errors=np.asarray(ce),
        reference_model_json=np.array(json.dumps(model,sort_keys=True,separators=(',',':'))),
        reference_model_identity_sha256=np.array(canonical(model)))
    if sha(reference_path)!='512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b' or reference_path.stat().st_size!=866207:
        raise ArithmeticError('Reconstructed whole run10 reference differs; no original-word claim')
    return model,reference_path,carrier_path,law,height

def prepare_history(ref,modules,args,node,raw,reference_path,carrier_path):
    locations=modules['history'].Locations(923,7377,2048)
    sources,provenance=[],[]
    for path in args.manifest:
        payload=json.loads(path.read_text())
        binding=ref.add_supplied_locations(locations,payload,path=path,node=node,scalar=raw,angles=2048)
        provenance.append(binding)
        sources.append({k:v for k,v in binding.items() if k!='original_payload'})
    if sum(x.get('kind')=='complete-published-a04-historical-package' for x in provenance)!=1:
        raise ValueError('Keep the entire original ordered eleven-payload package')
    indexed=locations.resolve_grid(carrier_path);arrays=locations.arrays()
    provenance_path=args.outdir/'supplied-location-provenance.json'
    write_json(provenance_path,dict(schema='independent-axisymmetric-SO3-complete-supplied-history-v1',
        ordered_inputs=provenance,historical_capacities_are_not_new_storage_limits=True,
        actual_carrier_sha256=sha(carrier_path),actual_reference_bundle_sha256=sha(reference_path),
        legacy_angle_reinterpretation='Original literal angles use the same proven run10 frozen material chart; no old field value or unknown typed priority is transferred',
        inherited_geometric_values=False,unprovided_later_runner_reports_reconstructed=False))
    location_path=args.outdir/'locations.json'
    write_json(location_path,dict(schema='independent-axisymmetric-SO3-literal-position-input-v1',
        carrier_sha256=sha(carrier_path),reference_bundle_sha256=sha(reference_path),
        N=2048,J=923,P=7377,source_inputs=sources,complete_supplied_provenance=record(provenance_path),
        curvature_points=arrays['curvature_points'],radius_points=arrays['radius_points'],
        protected_curvature_points=arrays['protected_curvature_points'],
        exact_location_summary=locations.summary(),resolved_grid_positions=indexed,
        legacy_angle_reinterpretation='same frozen run10 material chart; original literal words retained',
        only_supplied_positions_claimed_complete=True,old_geometry_values_transferred=False))
    return location_path,provenance_path,sources,locations.summary()

def _integer_table(deep):
    def exact(value):
        if isinstance(value,F):return str(value)
        if isinstance(value,dict):return {k:exact(v) for k,v in value.items()}
        if isinstance(value,(tuple,list)):return [exact(v) for v in value]
        if isinstance(value,(int,str,bool)) or value is None:return value
        raise TypeError('Only exact integer/Fraction scalar-table words are recorded')
    return dict(schema='complete-origin-run10-2218-leaf-integer-table-reconstruction-v1',
        definition=deep.definition,model_identity_sha256=deep.model_identity_sha256,
        integral_leaf_count=len(deep.leaves),integral_leaf_evaluations=deep.leaves_evaluated,
        leaves=exact(deep.leaves),total_integrals_dimensionless=exact(deep.total_integrals_dimensionless),
        integral_enclosure_width_exact=str(deep.integral_uncertainty),
        requested_integral_accuracy_reached=deep.requested_integral_accuracy_reached,
        all_infinite_tail_included=True,origin_actual_table_stored_words_available=False,
        exact_original_source_and_priority_count_reconstruction=True)

def execute(args,public_report):
    require_actions()
    import numpy as np
    started=time.monotonic();repo=args.repo.resolve();outdir=args.outdir.resolve()
    bridge=bridge_module()
    origin=verify_origin_contract(args.origin_parameters)
    if os.environ.get('GITHUB_RUN_ID')=='45972294636':
        raise ValueError('This is a separate-run continuation input, not an overwrite of the running origin')
    ref=load('_original_complete_run10_reference',Path(__file__).with_name(REFERENCE_NAME),REFERENCE_SHA)
    old=load('_original_complete_carrier_reconstructor',Path(__file__).with_name(ORIGIN_PRODUCER_NAME),ORIGIN_PRODUCER_SHA)
    paths,modules=ref.paths_and_modules(repo)
    for name in ('counted_tail_class','exact_node_definitions','read_public_step'):
        if sha(getattr(old,name).__code__.co_filename)!=ORIGIN_PRODUCER_SHA:
            raise ValueError('Keep the complete exact reconstruction source: '+name)
    inputs={key:record(path) for key,path in dict(warm_bundle=args.warm_bundle,
        node_report=args.node_report,scalar_input=args.scalar_input).items()}
    input_records={key:record(path) for key,path in dict(inputs_warm=args.warm_bundle,
        inputs_node=args.node_report,inputs_scalar=args.scalar_input,
        origin_parameters=args.origin_parameters,historical_public_record=args.historical_public_record).items()}
    for j,path in enumerate(args.manifest):input_records['manifest_'+str(j)]=record(path)
    public_report['actual_new_inputs']=copy.deepcopy(inputs)
    public_report['complete_source_records']={
        'reference':record(Path(ref.__file__)),'origin_reconstructor':record(Path(old.__file__)),
        'input_bridge':record(Path(bridge.__file__)),
        **{role:record(path) for role,path in paths.items()}}
    node=json.loads(args.node_report.read_text())
    if (node.get('schema')!='fullclosed-hold-real-pulse-warm-v1'
            or node.get('source_sha256')!=ref.SOURCE_PINS['warm_producer'][1]
            or node.get('bundle_sha256')!=inputs['warm_bundle']['sha256']
            or node.get('input_sha256')!=inputs['scalar_input']['sha256']
            or node.get('M')!=160 or node.get('J')!=923 or node.get('exact_core_affine') is not True):
        raise ValueError('Use the actual complete new warm/node/scalar source closure')
    with np.load(args.warm_bundle,allow_pickle=False) as data:
        warm={key:np.array(data[key],copy=True) for key in data.files}
    if set(warm)!=set(bridge.original_word_reader().WARM_MEMBERS):
        raise ValueError('Every complete original warm member remains required')
    mesh=np.array(warm['mesh'],copy=True);core=np.array(warm['qjets'][0,0,1:161],copy=True)
    if (warm['qjets'].shape!=(923,3,482) or mesh.shape!=(923,)
            or str(mesh.dtype)!='float64' or str(core.dtype)!='float64'
            or not np.isfinite(mesh).all() or not np.all(np.diff(mesh)>0)
            or ref.array_sha(mesh)!=origin['origin_mesh_array_sha256']
            or ref.array_sha(core)!=origin['origin_chart_array_sha256']
            or not np.array_equal(core[:3],warm['fixed_core_first3'])
            or float(warm['width']).hex()!=float(.05).hex()):
        raise ValueError('The real new warm does not reproduce every consumed frozen mesh/chart word')
    raw=ref.read_scalar(args.scalar_input);parameters=ref.scalar_parameters(raw)
    if canonical(parameters)!=PARAMETERS_SHA:
        raise ValueError('A different complete mathematical scalar input is not this continuation')
    full=modules['scalar'].FullHold(raw,paths['integer'],paths['hold'],panels=128)
    if full.carrier(full.S)!=float(mesh[-1]) or full.carrier(full.R)!=float(warm['radius']):
        raise ValueError('Keep the original accurate scalar domain and actual warm endpoint carrier')
    width=float(warm['width'])
    definitions=old.exact_node_definitions(mesh,full,width)
    declared=[(F(v['S_coefficient']),F(v['constant'])) for v in node['true_scalar_nodes']]
    if definitions!=declared or canonical([[str(a),str(b)] for a,b in definitions])!=origin['origin_affine_nodes_identity_sha256']:
        raise ValueError('The full exact original symbolic domain was not reproduced')
    origin_metric=origin['complete_actual_reference_record']['metrics']['axisymmetric-R690-reference-v2-first/report.json']
    scalar_identity=dict(scalar_input=origin['origin_public_input_evidence']['current_files']['current_scalar_input']['sha256'],
        scalar_source=ref.SOURCE_PINS['scalar'][1],integer_source=ref.SOURCE_PINS['integer'][1],hold_source=ref.SOURCE_PINS['hold'][1])
    counted=old.counted_tail_class(modules['deep_scalar'])
    deep=counted(full,original_input_identity=scalar_identity,target_leaves=2218,
        epsilon=F(1,8),integral_tolerance=F(1,10**18),historical_clock_seconds=300.)
    if (deep.model_identity_sha256!=origin['origin_fixed_scalar_identity_sha256']
            or str(deep.integral_uncertainty)!=origin_metric['scalar_width_exact']
            or deep.requested_integral_accuracy_reached is not False):
        raise ArithmeticError('The complete recorded current scalar table/accuracy was not reproduced')
    table_path=outdir/'complete-current-2218-integer-table.json'
    write_json(table_path,_integer_table(deep))
    breaks=[j for j,v in enumerate(definitions) if v==(F(1),-F(width))]
    if len(breaks)!=1:raise ValueError('The exact original lift breakpoint must be unique')
    plan=modules['observed'].make_plan(mesh,width,order=6,lift_break_node=breaks[0])
    if len(plan.cells)!=7377 or plan.legacy_count!=1845:
        raise ValueError('Keep all original 1845 legacy and 5532 Gauss observations')
    model,reference_path,carrier_path,law,height=generate_reference(
        ref,modules,full,deep,plan,definitions,warm,origin,raw,outdir)
    target=reconstruct_origin_target(origin,model,parameters,definitions,core)
    bridge.validate_origin_target(target)
    target_path=outdir/'origin-run10-fixed-target-definition.json'
    target_path.write_text(json.dumps(target,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n')
    if record(target_path)['bytes']!=97335 or sha(target_path)!=bridge.TARGET_FILE_SHA:
        raise ArithmeticError('The complete original target definition was not reproduced')
    old_step,old_metric,old_outputs,old_args=old.read_public_step(
        args.historical_public_record,OLD_RECORD_SHA,OLD_STEP,bridge.OLD_CARRIER_SHA,historical=True)
    old_input=dict(scalar_input=old_metric['scalar_input'],
        scalar_source=ref.SOURCE_PINS['scalar'][1],integer_source=ref.SOURCE_PINS['integer'][1],hold_source=ref.SOURCE_PINS['hold'][1])
    old_deep=counted(full,original_input_identity=old_input,target_leaves=int(old_metric['scalar_leaves']),
        epsilon=F(old_args['tail_cutoff']),integral_tolerance=F(old_args['integral_tolerance']),
        historical_clock_seconds=old_args['clock_admission_seconds'])
    if (old_metric['scalar_leaves']!=2397 or old_deep.model_identity_sha256!=old_metric['fixed_profile']
            or old_deep.integral_uncertainty!=F(old_metric['scalar_width_exact'])
            or old_deep.requested_integral_accuracy_reached!=old_metric['scalar_tolerance_reached']):
        raise ArithmeticError('The separate original historical scalar-address reconstruction failed')
    old_path=outdir/'run05-observations-restored.npz'
    generate_carrier(ref,modules,full,old_deep,plan,definitions,mesh,core,width,old_path)
    if sha(old_path)!=bridge.OLD_CARRIER_SHA or old_path.stat().st_size!=227202:
        raise ArithmeticError('The complete original dc5 address carrier was not reproduced')
    locations_path,provenance_path,location_sources,location_summary=prepare_history(
        ref,modules,args,node,raw,reference_path,carrier_path)
    execution=dict(repository=os.environ['GITHUB_REPOSITORY'],run_id=os.environ['GITHUB_RUN_ID'],
        run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),workflow_trigger_commit=os.environ.get('GITHUB_SHA'))
    # This report is NEW. It deliberately does not claim the old preparation
    # source, paths, elapsed time, public return or whole35f bytes.
    preparation=dict(schema=PREPARATION_SCHEMA,source_sha256=sha(__file__),
        source_commit=public_report['source_commit'],original_reference_source_sha256=REFERENCE_SHA,
        source_paths={role:str(path) for role,path in paths.items()},
        source_sha256_by_role={role:sha(path) for role,path in paths.items()},
        complete=True,N=2048,M=160,J=923,P=7377,
        old_warm_bundle=inputs['warm_bundle'],old_warm_node_report=inputs['node_report'],
        input_for_solver={role:record(path) for role,path in dict(reference_bundle=reference_path,
            carrier=carrier_path,node_report=args.node_report,scalar_input=args.scalar_input).items()},
        new_locations=record(locations_path),complete_supplied_location_provenance=record(provenance_path),
        supplied_location_sources=location_sources,reference_model_identity_sha256=canonical(model),
        reference_definition=model,fixed_scalar_metric_identity_sha256=deep.model_identity_sha256,
        original_scalar_parameters_identity_sha256=PARAMETERS_SHA,
        true_scalar=deep.metadata(),whole_unit_meridian_law=law.metadata(),
        complete_reconstructed_current_integer_table=record(table_path),
        new_height=height,original_warm_height=float(warm['Hcap']),
        all_original_free_core_and_height_retained=True,initial_height_is_only_a_free_variable_seed=True,
        optimized_old_q_field_read_as_T0=False,original_positive_observations_and_angle_orbits_retained=True,
        historical_nonlinear_directions_replayed=False,old_certificates_inherited=False,
        exact_location_summary=location_summary,complete_same_field_metric_or_geometry_read=False,
        physical_new_field_still_requires_full_initial_read=True,complete_scalar_tail_included=True,
        seconds=time.monotonic()-started,execution=execution,
        origin_fixed_target_definition_identity_sha256=bridge.TARGET_SHA,
        origin_reference_definition_is_frozen_provenance=True,
        new_actual_scalar_file_is_not_origin_scalar_file=inputs['scalar_input']['sha256']!=scalar_identity['scalar_input'],
        exact_scalar_defining_projection_equal=True,
        complete_reference_and_carrier_words_equal_to_origin=True,
        current_2218_table_is_not_historical_2397=True,
        original_preparation_report_relabelled_as_current=False)
    preparation_path=outdir/'preparation.json';write_json(preparation_path,preparation)
    files=dict(current_warm_bundle=inputs['warm_bundle'],current_node_report=inputs['node_report'],
        current_scalar_input=inputs['scalar_input'],current_reference_bundle=record(reference_path),
        current_carrier=record(carrier_path),current_preparation_report=record(preparation_path))
    projection=bridge.current_projection(files,target)
    unresolved=[dict(run_id='45972294636',run_attempt='1',
        scope='All actual later fields, complete 13-member final and uncapped typed/protected history, when genuinely available, remain separate continuation inputs; the frozen initial reference is not that final point',
        complete_report_or_typed_history_inferred=False,unknown_history_is_empty=False,
        terminal_or_final_status_inferred=False,original_branch_declared_finished=False)]
    value=dict(schema=bridge.SCHEMA,source_sha256=BRIDGE_SHA,
        producer=dict(source_sha256=sha(__file__),source_commit=public_report['source_commit'],
            reconstruction_scope='Complete original 2218-leaf run10 reference and historical dc5 address carrier; actual new execution separated from frozen origin evidence'),
        current_execution=execution,current_files=files,
        fixed_target_definition=target,fixed_target_definition_identity_sha256=bridge.TARGET_SHA,
        origin_fixed_target_definition=copy.deepcopy(target),origin_fixed_target_definition_identity_sha256=bridge.TARGET_SHA,
        origin_execution_evidence_is_not_current_execution=True,current_files_relabelled_as_origin=False,
        old_field_values_or_scientific_certificates_inherited=False,
        origin_carrier=record(old_path),current_carrier=record(carrier_path),
        original_full_carrier_sha_verified=True,consumer_must_rehash_and_read_complete_arrays=True,
        surface_history_values_or_certificates_inherited=False,
        complete_reference_member_payloads=projection['complete_reference_member_payloads'],
        unresolved_parallel_history_obligations=unresolved)
    checked=bridge.validate_bridge(value,expected_producer_source_sha256=sha(__file__))
    binding_path=outdir/'material-envelope-carrier-binding.json';write_json(binding_path,value)
    for key,item in input_records.items():
        if record(item['path'])!=item:raise ValueError('Actual source input changed during regeneration: '+key)
    for key,item in public_report['complete_source_records'].items():
        if record(item['path'])!=item:raise ValueError('Complete source changed during regeneration: '+key)
    if sha(__file__)!=public_report['source_sha256'] or sha(Path(__file__).with_name(BRIDGE_NAME))!=BRIDGE_SHA:
        raise ValueError('The actual complete new constructor/source changed during reconstruction')
    public_report.update(complete=True,seconds=time.monotonic()-started,
        actual_preparation=record(preparation_path),reference_bundle=record(reference_path),
        carrier=record(carrier_path),historical_carrier=record(old_path),
        origin_fixed_target=record(target_path),material_envelope_binding=record(binding_path),
        locations=record(locations_path),complete_supplied_location_provenance=record(provenance_path),
        full_current_scalar_table=record(table_path),bridge_validation=checked,
        origin_target_identity_sha256=bridge.TARGET_SHA,reference_model_identity_sha256=bridge.MODEL_SHA,
        fixed_scalar_identity_sha256=bridge.PROFILE_SHA,fixed_chart_core_sha256=bridge.CHART_SHA,
        current_scalar_live_leaves=2218,historical_scalar_live_leaves=2397,
        full_reference_whole_SHA_match=True,full_current_carrier_whole_SHA_match=True,
        all_inputs_and_sources_rechecked=True,physical_field_evaluations=0,
        Jacobian_evaluations=0,root_evaluations=0,old_nonlinear_directions_replayed=0,
        later_run10_final_or_typed_memory_reconstructed=False)

def validate_independent_fixed_target_binding(value,*,actual_model=None,**records):
    bridge=bridge_module()
    if actual_model is not None and actual_model!=value['fixed_target_definition']['complete_current_reference_model']:
        raise ValueError('Caller reference is not the whole frozen origin model')
    supplied={key:item for key,item in records.items() if item is not None}
    return bridge.validate_bridge(value,expected_producer_source_sha256=sha(__file__),current_files=supplied)

def from_files(*,repo,reference_bundle,carrier,node_report,scalar_input,preparation_report,
        material_envelope_binding,panels=128):
    """Complete explicit new constructor; all original 4e scientific methods remain original."""
    require_actions()
    import numpy as np
    if panels!=128:raise ValueError('Retain the complete original scalar working parameter')
    ref=load('_same_run10_context_original_reference',Path(__file__).with_name(REFERENCE_NAME),REFERENCE_SHA)
    bridge=bridge_module()
    payload,checked=bridge.read_bridge(material_envelope_binding,
        expected_producer_source_sha256=sha(__file__),current_files=dict(
            current_reference_bundle=reference_bundle,current_carrier=carrier,
            current_node_report=node_report,current_scalar_input=scalar_input,
            current_preparation_report=preparation_report))
    target=payload['fixed_target_definition']
    paths_and_modules=ref.paths_and_modules
    SOURCE_PINS=ref.SOURCE_PINS
    array_sha=ref.array_sha
    file_record=ref.file_record
    read_scalar=ref.read_scalar
    scalar_parameters=ref.scalar_parameters
    WholeAxisymmetricLaw=ref.WholeAxisymmetricLaw
    point_definition=ref.point_definition
    require_actions()
    paths, modules = paths_and_modules(repo)
    report = json.loads(Path(preparation_report).read_text())
    actual = dict(reference_bundle=reference_bundle, carrier=carrier,
        node_report=node_report, scalar_input=scalar_input)
    if (report.get('schema') != PREPARATION_SCHEMA or report.get('source_sha256') != sha(__file__)
            or report.get('complete') is not True):
        raise ValueError('Use the actual complete new reconstruction preparation')
    for role, value in actual.items():
        if report['input_for_solver'][role]['sha256'] != sha(value):
            raise ValueError('Changed independent input bytes: '+role)
    for role, (_, expected) in SOURCE_PINS.items():
        if report['source_sha256_by_role'].get(role) != expected:
            raise ValueError('Actual preparation omitted a complete source: '+role)
    with np.load(reference_bundle, allow_pickle=False) as data:
        saved = {key: np.array(data[key], copy=True) for key in data.files}
    with np.load(carrier, allow_pickle=False) as data:
        obs = {key: np.array(data[key], copy=True) for key in data.files}
    model = json.loads(str(saved['reference_model_json'].item()))
    identity = canonical(model)
    if (str(saved['schema'].item()) != SCHEMA or model.get('schema') != SCHEMA
            or model.get('source_sha256') != REFERENCE_SHA
            or str(saved['reference_model_identity_sha256'].item()) != identity
            or report.get('reference_model_identity_sha256') != identity
            or model.get('scalar_input_sha256') != target['complete_current_reference_model']['scalar_input_sha256']
            or model.get('symbolic_node_report_sha256') != target['complete_current_reference_model']['symbolic_node_report_sha256']
            or model.get('observation_carrier_sha256') != sha(carrier)
            or canonical(model['fixed_scalar_profile_definition']) != model['fixed_scalar_metric_identity_sha256']):
        raise ValueError('The complete new reference/model/source identity differs')
    self = ref.AxisymmetricReferenceContext()
    self.repo, self.paths, self.modules = Path(repo).resolve(), paths, modules
    self.input_records = {role: file_record(value) for role, value in actual.items()}
    self.input_records['preparation_report'] = file_record(preparation_report)
    self.model, self.identity, self.preparation, self.data = model, identity, report, saved
    self.mesh, self.core = np.array(saved['mesh'], copy=True), np.array(saved['initial_core'], copy=True)
    self.height, self.radius, self.width = (float(saved[k]) for k in ('initial_height','radius','width'))
    self.M, self.J = len(self.core), len(self.mesh)
    nodes = json.loads(Path(node_report).read_text())
    self.nodes = [(F(row['S_coefficient']),F(row['constant'])) for row in nodes['true_scalar_nodes']]
    if (self.M != 160 or self.J != 923 or self.core.shape != (160,)
            or len(self.nodes) != self.J or self.nodes[0] != (F(0),F(0)) or self.nodes[-1] != (F(1),F(0))
            or self.mesh[0] != 0 or not np.isfinite(self.mesh).all() or not np.all(np.diff(self.mesh)>0)
            or not np.isfinite(self.core).all() or not math.isfinite(self.height)
            or model['mesh_sha256'] != array_sha(self.mesh)
            or model['fixed_chart_core_sha256'] != array_sha(self.core)
            or model['fixed_core_first3'] != [float(v).hex() for v in self.core[:3]]
            or model['radius_carrier_hex'] != self.radius.hex()
            or not np.array_equal(saved['fixed_core_first3'], self.core[:3])):
        raise ValueError('Keep the actual full domain and complete core/H parameters')
    for key in ('mesh','radius','width','fixed_core_first3'):
        if not np.array_equal(saved[key],obs[key]):
            raise ValueError('Reference and observation carrier disagree: '+key)
    self.observed = modules['observed']
    self.plan = self.observed.ObservationPlan.from_arrays(obs)
    self.a_observations = np.array(obs['a_observations'],copy=True)
    if (len(self.plan.cells) != 7377 or self.plan.legacy_count != 1845 or self.plan.order != 6
            or self.a_observations.shape != (7377,) or not np.isfinite(self.a_observations).all()
            or np.any(self.a_observations <= 0) or model['a_observations_sha256'] != array_sha(self.a_observations)):
        raise ValueError('Retain all original positive legacy and Gauss observations')
    parameters = read_scalar(scalar_input)
    if canonical(scalar_parameters(parameters)) != model['original_scalar_parameters_identity_sha256']:
        raise ValueError('The true original scalar law changed')
    self.full = modules['scalar'].FullHold(parameters,paths['integer'],paths['hold'],panels=int(panels))
    if self.full.carrier(self.full.S) != float(self.mesh[-1]):
        raise ValueError('Keep the same exact S and its carrier')
    self.scalar_identity = model['fixed_scalar_metric_identity_sha256']
    self.scalar_definition = model['fixed_scalar_profile_definition']
    self.law = WholeAxisymmetricLaw(self.full,modules['deep_scalar'],tail_cutoff=model['working_scalar_tail_cutoff'])
    self.reference_cache = {}
    cells,local,values,errors = (saved[k] for k in
        ('cached_scalar_cells','cached_scalar_local','cached_scalar_values','cached_scalar_errors'))
    if (cells.ndim != 1 or local.shape != cells.shape or values.shape != (len(cells),4)
            or errors.shape != values.shape or not np.isfinite(values).all()
            or not np.isfinite(errors).all() or np.any(errors < 0)):
        raise ValueError('Keep the complete scalar jet/error carrier')
    for cell,u,value,error in zip(cells,local,values,errors):
        if int(cell) != cell:
            raise ValueError('Cached cell must be an exact integer')
        point_definition(self.nodes,int(cell),float(u))
        key = (int(cell),float(u).hex())
        if key in self.reference_cache:
            raise ValueError('Duplicate cached scalar address')
        value.setflags(write=False); error.setflags(write=False)
        self.reference_cache[key] = value,error
    self.maximum_reference_errors = np.zeros(4)
    self.actual_cached_queries = self.actual_new_queries = 0
    self.same_run10_reference_continuation_binding = checked
    self.same_run10_reference_constructor_source_sha256 = sha(__file__)
    return self

def bind_prepared_input(args,paths):
    """Full pure setup contract used by the independently named solver entry."""
    bridge=bridge_module()
    payload,checked=bridge.read_bridge(args.material_envelope_binding,
        expected_producer_source_sha256=sha(__file__),current_files=dict(
            current_reference_bundle=args.reference_bundle,current_carrier=args.carrier,
            current_node_report=args.node_report,current_scalar_input=args.scalar_input,
            current_preparation_report=args.preparation_report))
    report=json.loads(args.preparation_report.read_text())
    for role,digest in report['source_sha256_by_role'].items():
        if role not in paths or sha(paths[role])!=digest:
            raise ValueError('The solver omitted a complete original reference source: '+role)
    if (int(args.angles)!=2048 or int(args.panels)!=128
            or report['new_locations']['sha256'] not in {sha(path) for path in args.manifest}):
        raise ValueError('Keep the full observation grid, scalar working definition and entire supplied location union')
    return report,dict(preparation_report=record(args.preparation_report),
        actual_source=record(paths['reference']),actual_constructor_source=record(Path(__file__)),
        reference_model_identity_sha256=report['reference_model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=report['fixed_scalar_metric_identity_sha256'],
        original_scalar_parameters_identity_sha256=PARAMETERS_SHA,
        actual_input_records=report['input_for_solver'],new_locations=report['new_locations'],
        complete_supplied_location_provenance=report['complete_supplied_location_provenance'],
        all_supplied_history_retained=True,old_optimized_parent_required=False,
        explicit_same_run10_reference_continuation=checked,
        original_target_evidence_not_relabelled_as_current=True)

def parse_args():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('repo','warm-bundle','node-report','scalar-input','origin-parameters',
                 'historical-public-record','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--manifest',type=Path,action='append',required=True)
    args=parser.parse_args()
    for name in ('repo','warm_bundle','node_report','scalar_input','origin_parameters',
                 'historical_public_record','outdir'):
        setattr(args,name,getattr(args,name).resolve())
    args.manifest=[p.resolve() for p in args.manifest]
    if args.outdir.exists() or args.outdir==args.repo or args.repo in args.outdir.parents:
        raise ValueError('Use fresh complete raw output outside the repository')
    return args

def main():
    require_actions();args=parse_args();args.outdir.mkdir(parents=True)
    report=dict(schema=REPORT_SCHEMA,source_sha256=sha(__file__),
        source_commit=subprocess.check_output(['git','-C',str(args.repo),'rev-parse','HEAD'],text=True).strip(),
        complete=False,origin_actual_run_id='45972294636',origin_actual_run_attempt='1',
        current_actual_run_id=os.environ.get('GITHUB_RUN_ID'),current_actual_run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        original_target_is_origin_evidence_not_current_execution=True,
        physical_field_evaluations=0,Jacobian_evaluations=0,root_evaluations=0,
        later_run10_final_or_typed_memory_reconstructed=False)
    output=args.outdir/'report.json';write_json(output,report)
    try:
        execute(args,report)
    except BaseException as error:
        report.update(complete=False,error=repr(error))
        write_json(output,report)
        event(event='same_run10_reference_regeneration_failed',report=record(output),error=repr(error))
        raise
    write_json(output,report)
    event(event='same_run10_complete_reference_regenerated',report=record(output),
        origin_target_identity_sha256=report['origin_target_identity_sha256'],
        current_actual_run_id=report['current_actual_run_id'],reference_bundle=report['reference_bundle']['sha256'],
        carrier=report['carrier']['sha256'],reference_model=report['reference_model_identity_sha256'],
        current_scalar_live_leaves=2218,historical_scalar_live_leaves=2397,
        current_execution_is_not_origin=True,unknown_later_run10_history_not_empty=True)

if __name__=='__main__':main()
