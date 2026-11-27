#!/usr/bin/env python3
"""Complete source-only actual-public09 N4096 analytic-frame/J3/packet entry."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import pprint

PINS = {'fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py': 'ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5',
 'launch_run09_public_reference_analytic_frame_actions_v2.py': 'c1888457b67c85185aebe6c91d2bd4942ccc2d2074407e17f7f54a2825927d23',
 'read_run09_public_reference_analytic_frame_so3_report_v2.py': 'aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32',
 'so3_run09_public_reference_analytic_frame_geometry_v2.py': 'e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13'}
NAMES={
    'meridian':'so3_angular_refined_smooth_triangle_meridian_operator.py',
    'new_moment_input':'angular_refined_smooth_triangle_literal_zero_moment_input.py',
    'angular_observation':'angular_observation_refinement.py',
    'analytic_J3':'angular_refined_public_reference_stage_jacobian.py',
    'analytic_frame':'angular_refined_public_reference_normal_frame.py',
    'frame_C1':'angular_refined_public_reference_frame_c1.py',
    'stage_matrices':'angular_refined_public_reference_stage_matrices.py',
    'adjacent_matrices':'angular_refined_public_reference_adjacent_matrices.py',
    'reference_calibration':'angular_refined_public_reference_calibration.py',
    'endpoint':'so3_angular_refined_public_reference_normal_lift.py',
    'root_packets':'immutable_angular_refined_public_reference_root_packets.py',
    'independent_envelope_memory':'angular_refined_public_reference_memory.py',
    'envelope_transfer':'angular_refined_public_reference_history_transfer.py',
    'analytic_J3_binding':'angular_refined_public_reference_source_binding.py',
    'geometry':'so3_angular_refined_public_reference_envelope_geometry.py'}
DRIVER='fullclosed_angular_refined_public_reference_so3_qp.py'
LAUNCHER='launch_angular_refined_public_reference_so3_actions.py'
READER='read_angular_refined_public_reference_so3_report.py'
SCHEMA='complete-public09-N4096-analytic-frame-material-envelope-SO3-QP-v1'
NORMAL_SCHEMA='complete-angular-refined-public-reference-analytic-frame-normal-plane-SO3-v1'
BASE_SCHEMA='complete-angular-refined-supported-smooth-triangle-reference-so3-meridian-v1'
INPUT_SCHEMA='angular-refined-supported-smooth-triangle-literal-Q-input-v1'
Q_SCHEMA='angular-refined-supported-smooth-triangle-literal-two-bubble-Q-v1'
SNAPSHOT='actual-angular-refined-public-reference-analytic-frame-snapshot-v1'


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def once(text,old,new):
    if text.count(old)!=1:
        raise ValueError('Exact source change missing or repeated '+old[:100]+' '+str(text.count(old)))
    return text.replace(old,new)


def body(text,name):
    n=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name)
    return '\n'.join(text.splitlines()[n.lineno-1:n.end_lineno])+'\n'


def assign(text,name,value):
    n=next(n for n in ast.parse(text).body if isinstance(n,ast.Assign)
        and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id==name)
    lines=text.splitlines(keepends=True)
    return ''.join(lines[:n.lineno-1])+name+' = '+pprint.pformat(value,sort_dicts=True,width=112)+'\n'+''.join(lines[n.end_lineno:])


EXTRA_CHECKS="""    if a.material_envelope_binding is None or a.normal_stages!=32 or a.integration_order!=8:
        raise ValueError('N-only refinement retains the whole independent target, all 32 stages and eight radial Gauss nodes')
"""
ATTRIBUTION="""            angular_observation_attribution=observer.attribute(raw,stage_weights,q.multiplicity,parameters,
                spectral=spectral,centered=centered,stage_block=args.stage_block),
"""


def derive(parent,generated):
    old={}
    for name,digest in PINS.items():
        old[name]=(parent/name).read_text()
        if sha(old[name])!=digest:
            raise ValueError('Changed complete actual analytic parent '+name)
    original_driver=old['fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py']
    source_pins=next(ast.literal_eval(n.value) for n in ast.parse(original_driver).body
        if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='SOURCE_PINS' for t in n.targets))
    originals=dict(source_pins)
    core={role:(generated/name).read_text() for role,name in NAMES.items() if role!='geometry'}
    substitutions=[
        ('complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1',BASE_SCHEMA),
        ('complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1',NORMAL_SCHEMA),
        ('supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1',INPUT_SCHEMA),
        ('supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1',Q_SCHEMA),
        ('actual-reference-centred-analytic-frame-normal-current-point-snapshot-v1',SNAPSHOT)]
    for role,text in core.items():
        if role in originals:
            substitutions.extend(((originals[role][1],sha(text)),(Path(originals[role][0]).name,NAMES[role])))
    def changed(text):
        for before,after in substitutions:text=text.replace(before,after)
        return text
    original_geometry=old['so3_run09_public_reference_analytic_frame_geometry_v2.py']
    geometry=changed(original_geometry)
    expected_c1="policy.get('source_sha256') != "+repr(sha(core['frame_C1']))
    if geometry.count(expected_c1)!=1:
        raise ValueError('The complete current GeometryScreen C1 guard must bind the new actual helper')
    selected_key='all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained'
    old_key='all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained'
    definition=next(n for n in ast.parse(core['adjacent_matrices']).body
        if isinstance(n,ast.FunctionDef) and n.name=='definition')
    flags=[kw.value.value for n in ast.walk(definition) if isinstance(n,ast.Call)
        and isinstance(n.func,ast.Name) and n.func.id=='dict' for kw in n.keywords
        if kw.arg==selected_key and isinstance(kw.value,ast.Constant)]
    if (flags!=[True] or geometry.count("adjacent.definition.get("+repr(selected_key)+")")!=1
            or old_key in geometry):
        raise ValueError('The GeometryScreen guard must read the actual selected-J3 adjacent definition key')
    geometry=assign(geometry,'SCHEMA','complete-public09-angular-refined-analytic-frame-envelope-world-geometry-v1')
    core['geometry']=geometry
    for role,text in core.items():
        if role in originals:
            source_pins['angular_parent_'+role]=originals[role]
        source_pins[role]=('scripts/resume_20261126/'+NAMES[role],sha(text))
    source_pins['angular_parent_driver']=('scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py',PINS['fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py'])
    source_pins['angular_parent_reader']=('scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py',PINS['read_run09_public_reference_analytic_frame_so3_report_v2.py'])
    driver=changed(original_driver)
    driver=assign(driver,'SCHEMA',SCHEMA)
    driver=assign(driver,'SOURCE_PINS',source_pins)
    driver=once(driver,"or report['N'] != args.angles", "or report['N'] != 2048")
    driver=once(driver,"    p.add_argument('--angles', type=int, default=2048)","    p.add_argument('--angles', type=int, default=4096)")
    driver=once(driver,'a.angles != 2048','a.angles != 4096')
    driver=once(driver,'    a.manifest = [path.resolve() for path in a.manifest]',EXTRA_CHECKS+'    a.manifest = [path.resolve() for path in a.manifest]')
    driver=once(driver,"    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])",
        "    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])\n"
        "    observer = load('_so3_complete_actual_angular_observation',paths['angular_observation'])")
    driver=once(driver,'context.create_problem(N=args.angles,stage_block=args.stage_block)',
        'context.create_problem(N=2048,stage_block=args.stage_block)')
    driver=once(driver,'seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean)',
        'seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean,angular_observation_module=observer)')
    driver=once(driver,'        representation=q.model, coordinate_norm=coordinates.record,',
        '        representation=q.model, coordinate_norm=coordinates.record,\n'
        '        angular_observation_refinement=base.angular_observation,\n'
        "        angular_observation_source=file_record(paths['angular_observation']),\n"
        '        reference_full_N=2048,current_full_N=4096,\n'
        '        reference_quarter_angle_count=513,current_quarter_angle_count=1025,\n'
        '        radial_observation_refinement_performed=False,full_fixed_reference_target_unchanged=True,\n'
        '        saved_parent_Phi_used_as_current_baseline=False,')
    driver=once(driver,'        return dict(spectral=spectrum, max_relative_gram=maximum(raw), legacy_max_relative_gram=maximum(old),',
        '        return dict(spectral=spectrum, max_relative_gram=maximum(raw), legacy_max_relative_gram=maximum(old),\n'+ATTRIBUTION.rstrip())
    start='    def save_report():'
    if driver[driver.index(start):].replace(ATTRIBUTION,'')!=original_driver[original_driver.index(start):]:
        raise ValueError('Only the explicitly declared same-buffer attribution may change the full scientific suffix')
    launcher=changed(old['launch_run09_public_reference_analytic_frame_actions_v2.py'])
    launcher=assign(launcher,'DRIVER_SHA',sha(driver))
    launcher=launcher.replace('fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py',DRIVER)
    launcher=once(launcher,"    p.add_argument('--angles', type=int, default=2048)","    p.add_argument('--angles', type=int, default=4096)")
    launcher=once(launcher,'a.angles != 2048','a.angles != 4096')
    launcher=once(launcher,'    a.manifest = [path.resolve() for path in a.manifest]',EXTRA_CHECKS+'    a.manifest = [path.resolve() for path in a.manifest]')
    reader=changed(old['read_run09_public_reference_analytic_frame_so3_report_v2.py'])
    reader=assign(reader,'DRIVER_SHA',sha(driver))
    reader=assign(reader,'REPORT_SCHEMA',SCHEMA)
    reader=reader.replace('fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py',DRIVER)
    result={NAMES['geometry']:geometry,DRIVER:driver,LAUNCHER:launcher,READER:reader}
    for name,text in result.items():
        ast.parse(text);compile(text,name,'exec')
        if len(text.encode())>=100000:
            raise ValueError('Keep every complete source below 100KB: '+name+' '+str(len(text.encode())))
    def method_map(text):
        return {(c.name,n.name):ast.dump(n,include_attributes=False)
            for c in ast.parse(text).body if isinstance(c,ast.ClassDef)
            for n in c.body if isinstance(n,ast.FunctionDef)}
    before,after=method_map(original_geometry),method_map(geometry)
    if any(before[key]!=after[key] for key in before if key!=('GeometryScreen','__init__')):
        raise ValueError('The complete original physical geometry/rows/scan bodies must remain unchanged')
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--parent-directory',type=Path,required=True)
    p.add_argument('--generated-directory',type=Path,required=True)
    a=p.parse_args()
    values=derive(a.parent_directory,a.generated_directory)
    for name,text in values.items():(a.generated_directory/name).write_text(text)
    print(json.dumps({name:dict(sha256=sha(text),bytes=len(text.encode())) for name,text in values.items()},sort_keys=True))


if __name__=='__main__':
    main()
