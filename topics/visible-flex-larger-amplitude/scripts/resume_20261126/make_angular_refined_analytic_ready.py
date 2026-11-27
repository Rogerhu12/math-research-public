#!/usr/bin/env python3
"""Prepare complete, unexecuted N4096 parameter sets from actual locked N2048 sets."""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

SCHEMA='complete-N4096-independent-chart-analytic-J3-ready-construction-v1'
PARENTS={
 'independent':('analytic-J3-packets-independent-fixed-chart7c-ready.json',91360,'3e53d6da8cd0e02a4e0b5a8699e53b3efc7ca3428eb4f339aafb3e47eaa18f32'),
 'complete':('analytic-J3-packets-from-95559-complete-final-ready.json',91676,'66438158e8b337af2a8fec1581ee98b6df07a4cfab7723bd26d6ebba62d2bdb5')}
DRIVER='fullclosed_angular_refined_analytic_envelope_so3_qp.py'
LAUNCHER='launch_angular_refined_analytic_envelope_so3_actions.py'
READER='read_angular_refined_analytic_envelope_so3_report.py'
CONSTRUCTION=[
 'derive_angular_refined_analytic_core.py',
 'derive_angular_refined_independent_chart_memory.py',
 'angular_refined_analytic_binding_additions.py',
 'derive_angular_refined_analytic_binding.py',
 'angular_refined_analytic_transfer_additions.py',
 'derive_angular_refined_analytic_transfer.py',
 'derive_angular_refined_analytic_entry.py',
 'reproduce_angular_refined_analytic_envelope_sources.py',
 'make_angular_refined_analytic_ready.py']


def record(path):
    data=Path(path).read_bytes()
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def literal(text,key):
    for node in ast.parse(text).body:
        if isinstance(node,ast.Assign) and any(isinstance(v,ast.Name) and v.id==key for v in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError('Missing complete literal assignment '+key)


def option(args,key,value):
    if args.count(key)!=1:raise ValueError('Require exactly one complete option '+key)
    args[args.index(key)+1]=value


def read_parent(directory,kind):
    name,size,digest=PARENTS[kind];path=directory/name
    if record(path)!=dict(bytes=size,sha256=digest):raise ValueError('The entire actual parent ready changed')
    return json.loads(path.read_bytes())


def build(parent_directory,generated,construction,kind):
    original=read_parent(parent_directory,'independent' if kind=='independent' else 'complete')
    steps=copy.deepcopy(original['steps'])
    olddir=steps[0]['args'][steps[0]['args'].index('--outdir')+1].split('/')[-1]
    newdir={'independent':'angular-N4096-analytic-J3-packets-independent-first',
        'parent95559':'angular-N4096-analytic-J3-packets-from-95559-final',
        'parent0dfb':'angular-N4096-analytic-J3-packets-from-0dfb-final'}[kind]
    for index,step in enumerate(steps):
        step['id']=('complete-' if index==0 else 'actual-')+newdir+'-20261127'
        step['script']='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+(LAUNCHER if index==0 else READER)
        step['args']=[word.replace(olddir,newdir) for word in step['args']]
        step['outputs']=[word.replace(olddir,newdir) for word in step['outputs']]
        step['summary']={key.replace(olddir,newdir):value for key,value in step['summary'].items()}
        if 'cleanup_generated_patterns' in step:
            step['cleanup_generated_patterns']=[value.replace(olddir,newdir) for value in step['cleanup_generated_patterns']]
        step['scope']=('Complete N4096 observer of the same independently frozen 7c reference, analytic working J3, '
            'all original 32 normal stages, full outer variables, current sixjet lift and immutable packet capture. '
            'All N2048 literal angles are copied to even columns; full old/current radial grids are read at all 1025 '
            'current quarter angles. No old field values, finite Phi or certificates are inherited.' if index==0 else
            'Pure full-source/full-target/full-history N4096 reader. Original reference parent keeps initial failures '
            'readable; verify the actual final only when present. No F/J/root or packet upgrade.')
    if steps[0]['args'][steps[0]['args'].index('--angles')+1]!='2048':raise ValueError('Original observer must be N2048')
    option(steps[0]['args'],'--angles','4096')
    if kind=='parent0dfb':
        previous='reference-centred-independent-chart-envelope-normal-lift-first'
        actual='reference-centred-analytic-J3-packets-independent-first'
        steps[0]['args']=[word.replace(previous,actual) for word in steps[0]['args']]
        steps[0]['parent_bundle']=steps[0]['parent_bundle'].replace(previous,actual)
    if steps[1]['parent_bundle']!='axisymmetric-R690-reference-v2-first/reference.npz':
        raise ValueError('The pure read must not depend on an unreturned new final')
    science=next(iter(steps[0]['summary'].values()))
    science.update(reference_full_N='reference_full_N',current_full_N='current_full_N',
        reference_quarter_angle_count='reference_quarter_angle_count',current_quarter_angle_count='current_quarter_angle_count',
        same_full_fixed_reference_target='full_fixed_reference_target_unchanged',
        radial_observation_refinement='radial_observation_refinement_performed',
        old_parent_Phi_inherited='saved_parent_Phi_used_as_current_baseline',
        observer_definition='angular_observation_refinement.definition_identity_sha256',
        old_even_words_preserved='angular_observation_refinement.all_old_angle_words_preserved',
        old_indices_reinterpreted='angular_observation_refinement.old_grid_indices_reinterpreted',
        initial_same_buffer_all_Phi='initial.angular_observation_attribution.groups.all.spectral.centered_phi_normalized',
        initial_same_buffer_even_Phi='initial.angular_observation_attribution.groups.old_even.spectral.centered_phi_normalized',
        initial_same_buffer_odd_Phi='initial.angular_observation_attribution.groups.new_odd.spectral.centered_phi_normalized',
        final_same_buffer_all_Phi='final_statistics.angular_observation_attribution.groups.all.spectral.centered_phi_normalized',
        final_same_buffer_even_Phi='final_statistics.angular_observation_attribution.groups.old_even.spectral.centered_phi_normalized',
        final_same_buffer_odd_Phi='final_statistics.angular_observation_attribution.groups.new_odd.spectral.centered_phi_normalized')
    pure=next(iter(steps[1]['summary'].values()))
    for name,key in dict(reference_full_N='reference_full_N',current_full_N='current_full_N',
            reference_quarter_angle_count='reference_quarter_count',current_quarter_angle_count='current_quarter_count',
            observer_definition='definition_identity_sha256',old_even_words_preserved='all_old_angle_words_preserved',
            old_indices_reinterpreted='old_grid_indices_reinterpreted',radial_observation_refinement='radial_refinement_performed',
            free_coordinate_count_changed='free_coordinate_count_changed',
            actual_same_buffer_attribution_count='actual_same_buffer_attribution_count').items():
        pure[name]='analytic_stage_jacobian.angular_observation.'+key
    expected=literal((construction/'reproduce_angular_refined_analytic_envelope_sources.py').read_text(),'EXPECTED')
    for name,item in expected.items():
        if record(generated/name)!=item:raise ValueError('The complete runtime source is not the replayed version: '+name)
    pins=literal((generated/DRIVER).read_text(),'SOURCE_PINS')
    if len(pins)!=64:raise ValueError('All 64 runtime source roles are required')
    branch=copy.deepcopy(original['independent_branch'])
    if kind=='parent0dfb':
        branch['parent_complete_driver_sha256']='0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51'
        branch['parent_complete_reader_sha256']='c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e'
    branch.update(complete_parent_field_has_original_N2048=True,current_observer_has_N4096=True,
        complete_actual_old_report_must_precede_any_final_import=True,
        old_indices_resolved_before_literal_transfer=True,
        radial_or_frequency_refinement_performed=False)
    if kind=='independent':
        branch['complete_actual_old_report_must_precede_any_final_import']=False
        branch['no_prior_terminal_field_is_imported']=True
    peer_evidence=copy.deepcopy(original['unreturned_peer_evidence'])
    peer_evidence['45909290354/1'].update(
        actual_API_observation_time_UTC='2026-11-27T05:02:15Z',
        actual_API_updated_at_UTC='2026-11-27T05:00:28Z',
        scientific_child_termination_time_UTC=None,scientific_child_termination_cause=None,
        observation_time_is_not_scientific_child_end_time=True)
    return dict(schema='complete-independent-fixed-chart-analytic-J3-N4096-ready-v1',executed=False,queued=False,
        source_revision=2,previous_unexecuted_candidate_not_admitted=True,
        revision_scope='Only GeometryScreen C1 whole-source guard and dependent pins; complete mathematical bodies and arguments retained.',
        scientific_execution_permitted_only_in_public_Actions=True,
        scope='Current angular observation refinement only: N2048 to N4096 for the already independently frozen 7c target. '
            'This is not a run09 input adapter, radial refinement, M320 refinement, same-old90-target claim, or continuous certificate.',
        source_sha256=expected[DRIVER]['sha256'],
        runtime_source_roles={role:dict(path=relative,sha256=digest) for role,(relative,digest) in pins.items()},
        complete_runtime_sources={name:item for name,item in expected.items()},
        complete_source_constructors={name:record(construction/name) for name in CONSTRUCTION},
        complete_parent_ready=dict(path='computations/'+PARENTS['independent' if kind=='independent' else 'complete'][0],
            bytes=PARENTS['independent' if kind=='independent' else 'complete'][1],
            sha256=PARENTS['independent' if kind=='independent' else 'complete'][2]),
        actual_existing_inputs=copy.deepcopy(original['actual_existing_inputs']),
        fixed_target=copy.deepcopy(original['fixed_target']),input_producer=copy.deepcopy(original['input_producer']),
        complete_input_ready=copy.deepcopy(original['complete_input_ready']),
        actual_source_field_or_root_result=None,
        parameter_changes=dict(angles=dict(original='2048',current='4096'),
            original_directions=1,original_metric_maxiter=16,original_restoration_directions=4,
            original_restoration_maxiter=64,original_normal_stages=32,original_outer_radial_Gauss_order=8,
            original_seed_radial_Gauss_order=8,all_other_numeric_arguments_retained=True,
            explicit_source_script_outdir_and_parent_paths_changed=True,
            parent_science_argument_words=len(original['steps'][0]['args']),
            current_science_argument_words=len(steps[0]['args']),
            no_full_field_or_geometry_check_removed=True),
        independent_or_actual_parent_mode=branch,
        unreturned_peer_evidence=peer_evidence,
        pending_meaning=original['pending_meaning'],
        same_input_availability_scope='These literal {work} paths must contain the actual whole run08 7c-bound files, '
            'original dc5 carrier and complete 105289 input proof. A new warm/ref on another run is not presumed identical. '
            'No unavailable actual parent or final digest is filled in. The independent mode requires no terminal peer report; '
            'the strict modes transfer actual whole parent evidence and every saved free word.',
        source_only_verification=dict(AST_compile=True,complete_17_body_replay=True,complete_64_source_roles_verified=True,
            no_local_scientific_modules_imported=True,no_local_F_J_root_quadrature_or_fixture=True),steps=steps)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent-ready-directory',type=Path,required=True)
    p.add_argument('--generated-directory',type=Path,required=True)
    p.add_argument('--construction-directory',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--output-directory',type=Path,required=True)
    a=p.parse_args();a.output_directory.mkdir(parents=True,exist_ok=True)
    result={}
    for kind in ('independent','parent95559','parent0dfb'):
        value=build(a.parent_ready_directory,a.generated_directory,a.construction_directory,kind)
        path=a.output_directory/('angular-N4096-analytic-J3-'+kind+'-ready.json')
        path.write_text(json.dumps(value,ensure_ascii=False,indent=1,allow_nan=False)+'\n')
        if len(path.read_bytes())>=95000:raise ValueError('Keep the entire complete ready below95KB')
        result[path.name]=record(path)
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':main()
