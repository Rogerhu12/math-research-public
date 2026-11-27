#!/usr/bin/env python3
"""Source-only complete N-refined geometry/driver/launcher/reader derivation."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import pprint

PINS={
 'so3_reference_centred_c1_material_envelope_geometry.py':'bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f',
 'fullclosed_reference_centred_c1_material_envelope_so3_qp.py':'cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5',
 'launch_reference_centred_c1_material_envelope_so3_actions.py':'b93af9809adaf42a3eee9328c6ca857156c38609f40db975a92c3bea5f5af991',
 'read_reference_centred_c1_material_envelope_so3_report.py':'104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7',
}
NAMES={
 'meridian':'so3_angular_refined_smooth_triangle_meridian_operator.py',
 'endpoint':'so3_angular_refined_reference_centred_normal_lift_operator.py',
 'reference_calibration':'angular_refined_reference_centred_calibration.py',
 'frame_C1':'angular_refined_normal_frame_c1_reuse.py',
 'new_moment_input':'angular_refined_smooth_triangle_literal_zero_moment_input.py',
 'envelope_memory':'angular_refined_material_envelope_memory.py',
 'envelope_transfer':'angular_refinement_history_transfer.py',
 'angular_observation':'angular_observation_refinement.py',
 'geometry':'so3_angular_refined_material_envelope_geometry.py',
}
DRIVER='fullclosed_angular_refined_material_envelope_so3_qp.py'
LAUNCHER='launch_angular_refined_material_envelope_so3_actions.py'
READER='read_angular_refined_material_envelope_so3_report.py'
SCHEMA='complete-N4096-fixed-reference-material-envelope-normal-plane-SO3-QP-v1'
NORMAL_SCHEMA='complete-angular-refined-reference-centred-C1-fixed-normal-plane-SO3-v1'
BASE_SCHEMA='complete-angular-refined-supported-smooth-triangle-reference-so3-meridian-v1'
INPUT_SCHEMA='angular-refined-supported-smooth-triangle-literal-Q-input-v1'
Q_SCHEMA='angular-refined-supported-smooth-triangle-literal-two-bubble-Q-v1'
SNAPSHOT='actual-N4096-reference-centred-normal-current-point-snapshot-v1'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def once(text,old,new):
    if text.count(old)!=1:
        raise ValueError('Exact source change missing/repeated: '+old[:120])
    return text.replace(old,new)


def replace_function(text,name,value):
    node=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name)
    lines=text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1])+value.rstrip()+'\n'+''.join(lines[node.end_lineno:])


ARGUMENTS="""    p.add_argument('--material-envelope-seed-report',type=Path)
    p.add_argument('--material-envelope-seed-checkpoint',type=Path)
    p.add_argument('--material-envelope-parent-report',type=Path,action='append',default=[])
    p.add_argument('--independent-reference-start',action='store_true')
"""
ARGUMENT_CHECKS="""    if a.seed_so3_report is not None or a.seed_so3_checkpoint is not None:
        raise ValueError('This N-only entry uses a complete cc0a parent, its own restart, or explicit reference start')
    if bool(a.material_envelope_seed_report)!=bool(a.material_envelope_seed_checkpoint):
        raise ValueError('A complete original parent needs both its report and all thirteen checkpoint members')
    choices=int(a.restart_checkpoint is not None)+int(a.material_envelope_seed_report is not None)+int(a.independent_reference_start)
    if choices!=1 or a.normal_stages!=32 or a.integration_order!=8:
        raise ValueError('Choose one actual origin and retain the complete original 32 stages and eight radial Gauss nodes')
    for name in ('material_envelope_seed_report','material_envelope_seed_checkpoint'):
        if getattr(a,name) is not None:
            setattr(a,name,getattr(a,name).resolve())
    a.material_envelope_parent_report=[v.resolve() for v in a.material_envelope_parent_report]
"""


READER_ADDITION="""
def angular_binding(topic,report,model,roles,driver):
    pins=load_pins(driver)
    modules={}
    for role in ('angular_observation','envelope_transfer'):
        relative,digest=pins[role]
        path=topic/relative
        if sha(path)!=digest or roles[role]!=digest:
            raise ValueError('Keep the complete actual N-observer and old-history transfer sources')
        name='_complete_angular_reader_'+digest
        spec=importlib.util.spec_from_file_location(name,path)
        module=importlib.util.module_from_spec(spec);sys.modules[name]=module
        spec.loader.exec_module(module)
        modules[role]=module
    observer=modules['angular_observation']
    transferred=modules['envelope_transfer']
    observed=observer.validate_report(report.get('angular_observation'),model)
    if (report.get('reference_full_N')!=2048 or report.get('N')!=4096
            or report.get('J')!=923 or report.get('M')!=160
            or report.get('angular_observation_source',{}).get('sha256')!=roles['angular_observation']
            or report.get('reference_full_N_is_current_observer') is not False):
        raise ValueError('The fixed reference and current finite observer must remain distinct')
    pins['_topic']=str(topic)
    relation=transferred.validate_metadata(report.get('angular_history_transfer'),model=model,
        envelope=report['material_envelope'],caller_source_sha256=report['source_sha256'],
        carrier_sha256=report['observation_carrier_sha256'],pins=pins)
    seed=transferred.validate_seed_metadata(report.get('prior_final_variable_seed'),
        report=report,model=model,transfer=report['angular_history_transfer'])
    if report.get('history',{}).get('angular_history_transfer')!=report['angular_history_transfer']:
        raise ValueError('The complete initial history and its literal N transfer must bind the same report')
    return dict(observation=observed,history=relation,complete_prior_final_seed=seed)


def angular_attribution(value):
    path=Path(__file__).with_name('angular_observation_refinement.py')
    if sha(path)!=ANGULAR_OBSERVER_SHA:
        raise ValueError('The pure same-buffer angular attribution source changed')
    name='_complete_angular_attribution_'+ANGULAR_OBSERVER_SHA
    if name not in sys.modules:
        spec=importlib.util.spec_from_file_location(name,path)
        module=importlib.util.module_from_spec(spec);sys.modules[name]=module
        spec.loader.exec_module(module)
    return sys.modules[name].validate_attribution(value)

"""


def derive(parent,generated,observer):
    old={}
    for name,digest in PINS.items():
        old[name]=(parent/name).read_text()
        if sha(old[name])!=digest:
            raise ValueError('Changed complete original '+name)
    core={role:(generated/name).read_text() for role,name in NAMES.items() if role not in ('angular_observation','geometry')}
    core['angular_observation']=observer
    source_pins=next(ast.literal_eval(n.value) for n in ast.parse(old['fullclosed_reference_centred_c1_material_envelope_so3_qp.py']).body
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_PINS' for t in n.targets))
    substitutions=[
        ('complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1',BASE_SCHEMA),
        ('complete-R711-reference-centred-C1-reuse-SO3-fixed-normal-plane-six-control-layer-v1',NORMAL_SCHEMA),
        ('supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1',INPUT_SCHEMA),
        ('supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1',Q_SCHEMA),
        ('actual-reference-centred-C1-normal-current-point-snapshot-v1',SNAPSHOT)]
    for role,text in core.items():
        if role in source_pins:
            substitutions.append((source_pins[role][1],sha(text)))
            substitutions.append((Path(source_pins[role][0]).name,NAMES[role]))
    def changed(text):
        for a,b in substitutions:
            text=text.replace(a,b)
        return text
    geometry=changed(old['so3_reference_centred_c1_material_envelope_geometry.py'])
    geometry=once(geometry,"SCHEMA = 'complete-R715-C1-material-envelope-world-geometry-and-preserved-prefix-rows-v1'",
        "SCHEMA = 'complete-angular-refined-material-envelope-world-geometry-and-preserved-prefix-v1'")
    core['geometry']=geometry
    for role,text in core.items():
        source_pins[role]=('scripts/resume_20261126/'+NAMES[role],sha(text))
    source_pins['angular_parent_driver']=('scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py',PINS['fullclosed_reference_centred_c1_material_envelope_so3_qp.py'])
    source_pins['angular_parent_reader']=('scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py',PINS['read_reference_centred_c1_material_envelope_so3_report.py'])
    driver=changed(old['fullclosed_reference_centred_c1_material_envelope_so3_qp.py'])
    assignment=next(n for n in ast.parse(driver).body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='SOURCE_PINS' for t in n.targets))
    lines=driver.splitlines(keepends=True)
    driver=''.join(lines[:assignment.lineno-1])+'SOURCE_PINS = '+pprint.pformat(source_pins,sort_dicts=True,width=110)+'\n'+''.join(lines[assignment.end_lineno:])
    driver=once(driver,"SCHEMA = 'complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1'",'SCHEMA = '+repr(SCHEMA))
    driver=once(driver,"or report['N'] != args.angles", "or report['N'] != 2048")
    driver=once(driver,"    p.add_argument('--angles', type=int, default=2048)",ARGUMENTS+"    p.add_argument('--angles', type=int, default=4096)")
    driver=once(driver,'a.angles != 2048','a.angles != 4096')
    driver=once(driver,'    a.manifest = [path.resolve() for path in a.manifest]',ARGUMENT_CHECKS+'    a.manifest = [path.resolve() for path in a.manifest]')
    driver=once(driver,"    envelope_memory = load('_so3_complete_material_envelope_memory',paths['envelope_memory'])",
        "    envelope_memory = load('_so3_complete_material_envelope_memory',paths['envelope_memory'])\n"
        "    observer = load('_so3_complete_dyadic_angular_observation',paths['angular_observation'])\n"
        "    transfer = load('_so3_complete_original_N_history_transfer',paths['envelope_transfer'])")
    driver=once(driver,'context.create_problem(N=args.angles,stage_block=args.stage_block)',
        'context.create_problem(N=2048,stage_block=args.stage_block)')
    driver=once(driver,'seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean)',
        'seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean,angular_observation_module=observer)')
    start=driver.index('    address_parent = restart if restart is not None else seed_report')
    end=driver.index('    stage_weights = q.mixed_stage_weights',start)
    driver=driver[:start]+'''    witnesses,radius_witnesses,history_record,envelope,angular_transfer = transfer.load_memory(
        args,preparation,q,history,memory=envelope_memory,current_driver_source=Path(__file__),restart=restart)
    parent_words,parent_seed_record=transfer.seed_from_complete_prior_final(args,q,
        current_driver_source=Path(__file__),transfer_record=angular_transfer)
    if parent_words is not None:
        x=parent_words
    initial_point_sha256=meridian.array_sha(x)
'''+driver[end:]
    driver=once(driver,'        representation=q.model, coordinate_norm=coordinates.record,',
        '''        representation=q.model, coordinate_norm=coordinates.record,
        reference_full_N=2048,reference_full_N_is_current_observer=False,
        angular_observation=base.angular_observation,
        angular_observation_source=file_record(paths['angular_observation']),
        angular_history_transfer=angular_transfer,
        prior_final_variable_seed=parent_seed_record,
        explicit_prior_final_variable_seed_requested=args.material_envelope_seed_checkpoint is not None,
        initial_full_variable_point_sha256=initial_point_sha256,
        initial_point_source='complete actual original parent final' if parent_seed_record is not None else
            ('complete same-source restart' if restart is not None else 'explicit frozen reference initial point'),''')
    driver=once(driver,'        changed_control_map_has_independent_model_identity=True,',
        '        changed_control_map_has_independent_model_identity=False,\n'
        '        observer_refinement_has_independent_model_identity=True,\n'
        '        original_complete_field_equation_and_fixed_target_unchanged=True,\n'
        '        computed_float_field_equality_to_parent_claimed=False,')
    driver=once(driver,'        new_zero_closure_seed_changes_physical_field=restart is None,',
        '        new_zero_closure_seed_changes_physical_field=False,')
    driver=once(driver,'            endpoint_roots=endpoint_readout(q))',
        '''            endpoint_roots=endpoint_readout(q),
            angular_observation_attribution=observer.attribute(raw,stage_weights,q.multiplicity,parameters,
                spectral=spectral,centered=centered,stage_block=args.stage_block))''')
    # The original loop and true screenings remain complete. The statistics
    # helper adds same-buffer all/even/odd attribution, never another F read.
    launcher=old['launch_reference_centred_c1_material_envelope_so3_actions.py']
    launcher=launcher.replace('fullclosed_reference_centred_c1_material_envelope_so3_qp.py',DRIVER)
    launcher=launcher.replace(PINS['fullclosed_reference_centred_c1_material_envelope_so3_qp.py'],sha(driver))
    launcher=once(launcher,"    p.add_argument('--angles', type=int, default=2048)",ARGUMENTS+"    p.add_argument('--angles', type=int, default=4096)")
    launcher=once(launcher,'a.angles != 2048','a.angles != 4096')
    launcher=once(launcher,'    a.manifest = [path.resolve() for path in a.manifest]',ARGUMENT_CHECKS+'    a.manifest = [path.resolve() for path in a.manifest]')
    launcher=once(launcher,'        if isinstance(value, list):',
        "        if isinstance(value,bool):\n            if value:\n                command.append(flag)\n        elif isinstance(value, list):")
    launcher=once(launcher,'    if args.restart_checkpoint is not None:\n        inputs.extend([args.restart_checkpoint, args.restart_report])',
        '''    if args.material_envelope_binding is not None:
        inputs.append(args.material_envelope_binding)
    inputs.extend(args.material_envelope_parent_report)
    if args.material_envelope_seed_checkpoint is not None:
        inputs.extend([args.material_envelope_seed_checkpoint,args.material_envelope_seed_report])
    if args.restart_checkpoint is not None:
        inputs.extend([args.restart_checkpoint, args.restart_report])''')
    reader=changed(old['read_reference_centred_c1_material_envelope_so3_report.py'])
    reader=reader.replace('fullclosed_reference_centred_c1_material_envelope_so3_qp.py',DRIVER)
    reader=reader.replace(PINS['fullclosed_reference_centred_c1_material_envelope_so3_qp.py'],sha(driver))
    reader=reader.replace("REPORT_SCHEMA = 'complete-R711-reference-centred-C1-material-envelope-fixed-normal-plane-SO3-QP-v1'",'REPORT_SCHEMA = '+repr(SCHEMA))
    reader=once(reader,'def read_report(repo, report_path, *, verify_final_bundle=False):',
        "ANGULAR_OBSERVER_SHA = '"+sha(observer)+"'\n"+READER_ADDITION+'\ndef read_report(repo, report_path, *, verify_final_bundle=False):')
    reader=once(reader,'    envelope_binding,envelope_check,envelope_row_check = material_envelope_binding(topic,report,roles,driver)',
        '    envelope_binding,envelope_check,envelope_row_check = material_envelope_binding(topic,report,roles,driver)\n'
        '    angular=angular_binding(topic,report,model,roles,driver)')
    reader=once(reader,'        material_envelope_binding=envelope_binding,',
        '        material_envelope_binding=envelope_binding,angular_observation_refinement=angular,')
    reader=once(reader,"        domain=value.get('domain'), endpoint_roots=endpoint_roots(value.get('endpoint_roots')))",
        "        domain=value.get('domain'), endpoint_roots=endpoint_roots(value.get('endpoint_roots')),\n"
        "        angular_observation_attribution=angular_attribution(value.get('angular_observation_attribution')))")
    reader=reader.replace('actual-complete-R711-reference-centred-C1-material-envelope-normal-plane-SO3-scalar-readout-v1',
        'actual-complete-N4096-fixed-reference-material-envelope-normal-plane-readout-v1')
    result={NAMES['geometry']:geometry,DRIVER:driver,LAUNCHER:launcher,READER:reader}
    for name,text in result.items():
        ast.parse(text);compile(text,name,'exec')
        if len(text.encode())>=100000:
            raise ValueError('The complete source exceeds 100KB: '+name)
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--parent-directory',type=Path,required=True)
    p.add_argument('--generated-directory',type=Path,required=True)
    p.add_argument('--observer-source',type=Path,required=True)
    a=p.parse_args()
    values=derive(a.parent_directory,a.generated_directory,a.observer_source.read_text())
    for name,text in values.items():
        (a.generated_directory/name).write_text(text)
    print(json.dumps({n:dict(bytes=len(t.encode()),sha256=sha(t)) for n,t in values.items()},sort_keys=True))


if __name__=='__main__':
    main()
