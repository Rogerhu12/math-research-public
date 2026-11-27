#!/usr/bin/env python3
"""Source/parameter-only complete public09 N4096 plans; no scientific result is supplied."""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

SCHEMA='complete-public09-N4096-analytic-frame-ready-construction-v1'
PARENT_NAME='run09-public-reference-analytic-frame-v2-complete-ready.json'
PARENT_BYTES=93108
PARENT_SHA='2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f'
PARENT_DRIVER='ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5'
PARENT_READER='aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32'
DRIVER='fullclosed_angular_refined_public_reference_so3_qp.py'
LAUNCHER='launch_angular_refined_public_reference_so3_actions.py'
READER='read_angular_refined_public_reference_so3_report.py'
CONSTRUCTION=(
    'derive_public_reference_angular_refined_core.py',
    'derive_public_reference_angular_refined_memory.py',
    'public_reference_angular_binding_additions.py',
    'derive_public_reference_angular_binding.py',
    'public_reference_angular_transfer_additions.py',
    'derive_public_reference_angular_transfer.py',
    'derive_public_reference_angular_entry.py',
    'reproduce_public_reference_angular_refined_sources.py',
    'make_public_reference_angular_refined_ready.py')


def record(path):
    data=Path(path).read_bytes()
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())


def literal(text,key):
    for node in ast.parse(text).body:
        if isinstance(node,ast.Assign) and any(isinstance(v,ast.Name) and v.id==key for v in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError('Missing complete literal '+key)


def option(args,key,value):
    if args.count(key)!=1:raise ValueError('Require one complete option '+key)
    args[args.index(key)+1]=value


def remove_mode(args):
    answer=[];index=0
    while index<len(args):
        if args[index]=='--independent-envelope-branch':index+=1
        elif args[index] in ('--pending-parallel-envelope-run','--pending-parallel-envelope-source'):index+=2
        else:answer.append(args[index]);index+=1
    return answer


def build(parent_path,generated,construction,kind):
    if record(parent_path)!=dict(bytes=PARENT_BYTES,sha256=PARENT_SHA):
        raise ValueError('Use the whole actual public09 analytic-frame parameter source')
    original=json.loads(parent_path.read_bytes())
    if (original['fixed_target']['identity_sha256']!='7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a'
            or original['fixed_target']['whole_actual_binding_sha256']!='2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d'):
        raise ValueError('Do not relabel another run or chart as the complete actual09 target')
    steps=copy.deepcopy(original['steps'])
    olddir='run09-public-reference-analytic-frame-v2-first'
    newdir={'independent':'run09-angular-N4096-analytic-frame-v2-independent',
        'terminal':'run09-angular-N4096-analytic-frame-v2-from-terminal-history',
        'final':'run09-angular-N4096-analytic-frame-v2-from-complete-final'}[kind]
    for i,step in enumerate(steps):
        step['id']=('complete-' if i==0 else 'actual-')+newdir+'-20261127'
        step['script']='topics/visible-flex-larger-amplitude/scripts/resume_20261126/'+(LAUNCHER if i==0 else READER)
        step['args']=[v.replace(olddir,newdir) for v in step['args']]
        step['outputs']=[v.replace(olddir,newdir) for v in step['outputs']]
        step['summary']={k.replace(olddir,newdir):v for k,v in step['summary'].items()}
        if 'cleanup_generated_patterns' in step:
            step['cleanup_generated_patterns']=[v.replace(olddir,newdir) for v in step['cleanup_generated_patterns']]
        step['scope']=('Complete N4096 observer of the entire actually frozen run09 target. All 1025 quarter angles, '
            'copied old 513/even words, complete P0 and old/current radial grids, all 32 stages, full free variables, '
            'analytic full frame/J3, current sixjet lift and immutable current-cache packets remain. All old values and '
            'finite objective baselines are reread under the new source.' if i==0 else
            'Pure complete-source/actual09-target/75-role/history/packet/N4096 read. Original reference parent keeps '
            'initial failures readable. No F/J/root/integral or packet upgrade.')
    option(steps[0]['args'],'--angles','4096')
    parent_report='{work}/'+olddir+'/report.json'
    parent_final='{work}/'+olddir+'/final-new-field.npz'
    if kind!='independent':
        steps[0]['args']=remove_mode(steps[0]['args'])
        steps[0]['args']+=['--material-envelope-parent-report',parent_report]
        if kind=='final':
            steps[0]['args']+=['--material-envelope-seed-report',parent_report,
                '--material-envelope-seed-checkpoint',parent_final]
            steps[0]['parent_bundle']=olddir+'/final-new-field.npz'
    else:
        steps[0]['args']+=['--pending-parallel-envelope-run','45943410994/1',
            '--pending-parallel-envelope-source','45943410994/1='+PARENT_DRIVER]
    if steps[1]['parent_bundle']!='axisymmetric-R690-reference-v2-first/reference.npz':
        raise ValueError('The pure reader must not depend on an unreturned new final')
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
    expected=literal((construction/'reproduce_public_reference_angular_refined_sources.py').read_text(),'EXPECTED')
    for name,item in expected.items():
        if record(generated/name)!=item:raise ValueError('The complete runtime source differs: '+name)
    pins=literal((generated/DRIVER).read_text(),'SOURCE_PINS')
    if len(pins)!=75:raise ValueError('Retain all 75 complete runtime source roles')
    result=copy.deepcopy(original)
    result.update(schema='complete-actual-public09-analytic-frame-N4096-parameter-plan-v2',executed=False,queued=False,
        complete_source_and_parameter_closure=True,
        scope='N2048 to N4096 current observation of the exact complete returned run09 target, with frozen N2048 reference, '
            'M160 chart, all scalar parameters/exact nodes, J923 mesh, outer eight-point radial integration and common 32-stage '
            'normal chain. New finite angular measure; no old finite Phi, physical values or certificates inherited.',
        source_sha256={name:item['sha256'] for name,item in expected.items()},
        runtime_source_roles={role:[relative,digest] for role,(relative,digest) in pins.items()},
        complete_source_constructors={name:record(construction/name) for name in CONSTRUCTION},
        complete_parent_ready=dict(path='computations/'+PARENT_NAME,bytes=PARENT_BYTES,sha256=PARENT_SHA),
        complete_source_reproducer=dict(name='reproduce_public_reference_angular_refined_sources.py',
            **record(construction/'reproduce_public_reference_angular_refined_sources.py'),
            complete_output_source_count=18,complete_actual_source_roles=75),
        complete_numeric_parameter_provenance=dict(
            all_original_numeric_parameters_retained_except_current_observer_N=True,
            numerical_argument_changes=[dict(option='--angles',old='2048',new='4096')],
            directions=1,maxiter=16,restoration_directions=4,restoration_maxiter=64,
            normal_stages=32,outer_radial_Gauss_order=8,seed_radial_Gauss_order=8,
            parent_science_words=len(original['steps'][0]['args']),current_science_words=len(steps[0]['args']),
            parent_pure_words=len(original['steps'][1]['args']),current_pure_words=len(steps[1]['args']),
            original_all_science_summary_selectors_retained=True,original_all_pure_summary_selectors_retained=True,
            science_summary_count=len(science),pure_summary_count=len(pure)),
        complete_scientific_suffix=dict(
            original_sha256='d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376',
            original_complete_scientific_suffix_retained_after_removing_only_declared_same_buffer_attribution=True,
            both_original_record_only_packet_hooks_retained=True,fields_or_rows_not_recomputed_for_attribution=True),
        independent_branch=dict(mode=kind,actual_parent_source=PARENT_DRIVER,actual_parent_reader=PARENT_READER,
            complete_N2048_parent_terminal_required=kind!='independent',
            complete_actual_final_required=kind=='final',
            complete_parent_report=parent_report if kind!='independent' else None,
            complete_parent_final=parent_final if kind=='final' else None,
            actual_parent_report_sha256=None,actual_parent_final_sha256=None,
            actual_parent_field_has_not_been_fabricated=True,
            all_old_literal_addresses_and_uncapped_typed_lineage_transferred=True,
            frozen_reference_seed_not_reselected_from_parent_final=True,
            original_reference_initial_point_used=kind!='final',
            all_current_initial_values_roots_geometry_and_finite_Phi_reread=True),
        source_only_checks=dict(all_75_whole_runtime_source_roles_verified=True,
            AST_and_compile_without_import=True,complete_18_body_reproducer_exit_code=0,
            duplicate_literal_keys_keywords_and_trailing_whitespace_checked=True,
            selected_adjacent_guard_matches_actual_definition=True,
            thirteen_runtime_bodies_unchanged_from_prior_candidate=True,
            scientific_imports_or_F_J_root_or_fixtures_executed_locally=False),
        actual_future_definition_or_field_sha256=None,
        actual_parent_run_status_note='Actual e3cb setup failed before report at an adjacent-policy getter: '
            'all_original was absent while the selected analytic-J3 source declares all_selected. Its actual full '
            'child log is 6387 bytes, SHA256 33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de. '
            'This complete revision2 binds repaired ff544/aee22 sources. Their future terminal/final is not fabricated.',
        limitations='No local science, field result, normal-root existence/uniqueness certificate, inverse-error enclosure, '
            'continuous geometry certificate, radial refinement, M refinement, or equivalence with any other run target is claimed.',
        steps=steps)
    # Complete parameter/source data are inline. The already immutable original
    # failure evidence is referenced by its whole parent-ready, not copied twice.
    result['actual_failure_and_exact_repair']=dict(
        complete_evidence_source=dict(path='computations/'+PARENT_NAME,bytes=PARENT_BYTES,sha256=PARENT_SHA),
        complete_evidence_field='actual_failure_and_exact_repair',
        actual_log_bytes=6387,actual_log_sha256='33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de',
        missing_key='all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained',
        actual_key='all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained',
        old_science_report_produced=False,old_pure_readout_produced=False,
        repaired_scientific_success_inferred=False)
    result['unreturned_peer_evidence']['45909290354/1'].update(
        actual_API_observation_time_UTC='2026-11-27T05:02:15Z',actual_API_updated_at_UTC='2026-11-27T05:00:28Z',
        scientific_child_termination_time_UTC=None,scientific_child_termination_cause=None,
        observation_time_is_not_scientific_child_end_time=True)
    if kind=='independent':
        result['unreturned_peer_evidence']['45943410994/1']=dict(driver_sha256=PARENT_DRIVER,
            repaired_parent_terminal_report_consumed=False,complete_terminal_field_or_typed_state_read=False,
            prior_e3cb_attempt_report_absent=True,actual_unpaid_provenance_obligation_retained=True,
            unknown_is_not_empty=True)
    for i in range(2):
        before=next(iter(original['steps'][i]['summary'].values()))
        after=next(iter(steps[i]['summary'].values()))
        if any(after.get(k)!=v for k,v in before.items()):
            raise ValueError('Do not remove or reinterpret any actual original summary selector')
    if len(json.dumps(steps,separators=(',',':')).encode())>=95000:
        raise ValueError('The entire actual two-step queue must fit below 95KB')
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent-ready',type=Path,required=True)
    p.add_argument('--generated-directory',type=Path,required=True)
    p.add_argument('--construction-directory',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--output-directory',type=Path,required=True)
    a=p.parse_args();a.output_directory.mkdir(parents=True,exist_ok=True)
    outputs={}
    for kind in ('independent','terminal','final'):
        value=build(a.parent_ready,a.generated_directory,a.construction_directory,kind)
        path=a.output_directory/('public09-angular-N4096-analytic-frame-v2-'+kind+'-ready.json')
        path.write_text(json.dumps(value,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
        if len(path.read_bytes())>=100000:raise ValueError('Keep each complete parameter source below100KB')
        outputs[path.name]=record(path)
    print(json.dumps(outputs,sort_keys=True))


if __name__=='__main__':main()
