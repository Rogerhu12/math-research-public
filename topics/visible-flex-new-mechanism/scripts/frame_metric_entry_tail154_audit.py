#!/usr/bin/env python3
"""Restore four necessary temporary prefixes, then one new two-block154 stage.

All research evaluation is public Actions only. Growth, strip and scaled SOC
and the previous103 stage are each restored once with original budgets. The
new stage holds the same g/b0 and9 height coefficients fixed and changes the declared
proposal subspace/radius, and keeps complete original coarse/fine acceptance.
No reproducible payload is published; stdout gives the scientific conclusions.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import tempfile
import time
import traceback
import numpy as np

from frame_collar_bvp import atomic_save
from frame_collar_residual_audit import digest
from frame_entry_paired_repair_audit import require_public_actions
from frame_entry_short_bounded_audit import audit_data,compare_data
from frame_independent_height_solve import state_record
from frame_curvature_epigraph_exchange import GROUPS
from frame_metric_budget_recovery import recovery_decision
from frame_metric_epigraph import geometry_values
from frame_metric_spectral_recovery import EPSILON_EXACT,PROPOSAL_BRANCHES,spectral_proposal_rows
from frame_curvature_soc_metric_reserve_audit import exact_vector
import frame_metric_budget_restoration_rows as rows_api
import frame_metric_spectral_trust_growth_audit as growth
import frame_metric_spectral_strip_reserve_audit as strip
import frame_metric_spectral_soc_scaling_audit as soc
import frame_metric_entry_body103_audit as body103
import frame_metric_entry_body103 as body103_library
from frame_entry_tail_blocks import EntryTail154Subspace,RationalRowGrid
from frame_metric_entry_tail154 import (EntryTail154Objective,run_restricted_recovery,
    configuration,implementation_hashes as library_hashes,developer_check as restricted_check,
    restriction_definition,restricted_growth_definition,layout_from_problem,POSITION_JETS,
    strip_floor_definition,penalty_definition,floor_definition,scaling_definition)

SCHEMA='same-g-entry-tail154-after-four-temporary-prefixes-audit-v1'
STAGE='metric_entry_tail154_stage'
PREFIX_STAGE=body103.STAGE
OBSERVED_BODY103_RUN='43691833140'
OBSERVED_BODY103_SOURCE='2f25b5aacea5664574c18aa795c662fdeede3eab'
OBSERVED_BODY103_STATE='bfbd7465044bd742b48d731f0f381ef015e32fa0867b20442488be9bd9831b1a'
OBSERVED_BODY103_REPORT_SHA='70caae17e8745dc790c2b98f08f8a0335f43c6dba38b7dea2b8751ae963ebb18'
FROZEN_PREFIX_SOURCE_SHA256={
    'frame_metric_spectral_trust_growth.py':'19394bea4779c4497851c169a15dddad5839469067d550f64bef7af3bb88dcc6',
    'frame_metric_spectral_strip_reserve.py':'0d653e66947b95efe56e518e8bf4705076bc9ef687e5a596a1884b8367d22ae3',
    'frame_metric_spectral_strip_reserve_audit.py':'4347bdc3afc2504b2a6546d41176e0e3a9e340533ee1eee16ff831257e149e38',
    'frame_second_order_correction_scaling.py':'3b74cc8cc840aaece3aaf4c188728fffff4a7409289d65d1aba6aeb9e70ef98f',
    'frame_metric_spectral_soc_scaling.py':'6e3ef11a7ee232436d609573de970a55be58858dac9364323383c37313a44958',
    'frame_metric_spectral_soc_scaling_audit.py':'d09cd8b4e435d252aaa56b0a14f13dce69b6904597b8c4e4c75753d1fe670966',
    'frame_entry_body_subspace.py':'09f91a1d53c807ff58bb8862c7e7765cb21d09ca93bc0ccfc100f19ef446d022',
    'frame_metric_entry_body103.py':'7054eaa6466f5f5b8bdc8f595bbdd2b1747b2063908cfaecd506d74084a08fd3',
    'frame_metric_entry_body103_audit.py':'90a03cea625d73822183019df269c1bd8713a9c66aacb4adf54644719939413c'}
INPUTS=growth.INPUTS
SHA_NAMES=growth.SHA_NAMES
coefficients=growth.coefficients
curvature_grid=growth.curvature_grid
summary_path=growth.summary_path
GATE_ORDER=soc.GATE_ORDER
GATE_NUMBERS=soc.GATE_NUMBERS
_scalar=soc._scalar
_gate_codes=soc._gate_codes


def implementation_hashes():
    result=body103.implementation_hashes();result.update(library_hashes())
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def require_frozen_prefix_sources():
    actual=body103.implementation_hashes()
    for name,expected in FROZEN_PREFIX_SOURCE_SHA256.items():
        if actual.get(name)!=expected:raise ValueError('necessary temporary prefix source differs: '+name)


def restored_body103_controller(stage,cfg):
    body103_library.restriction_definition(cfg)
    radius=float(Q(cfg['entry_body103_initial_trust_exact']));streak=0
    models=stage.get('solver',{}).get('models',[]);without_update=False
    for i,model in enumerate(models):
        if model.get('number')!=i+1 or model.get('trust_before_model')!=radius:
            raise ValueError('restored103 sequential model/controller radius differs')
        feedback=model.get('scale_feedback_update')
        if feedback is None:
            if i!=len(models)-1:raise ValueError('only final103 model may lack completed scale update')
            without_update=True;continue
        updated,count,expected=body103_library.next_restricted_trust(model,
            feedback['trust_after_original_controller'],streak,cfg)
        if feedback!=expected:raise ValueError('restored103 completed scale feedback differs from its frozen source')
        radius,streak=updated,count
    if (stage.get('last_restricted_trust')!=radius
            or stage.get('final_consecutive_growth_qualifying_models')!=streak):
        raise ValueError('restored103 final actual controller differs')
    return {'schema':'recorded-restored103-controller-not-new-block-seed-v1',
        'trust_evaluated':radius,'trust_binary64_exact':str(Q.from_float(radius)),
        'success_streak':streak,'last_model_without_completed_scale_feedback':without_update,
        'origin':'old103 explicit initial scale followed by its completed scale_feedback_update records',
        'unfinished_last_model_not_counted_as_success':without_update,
        'new_two_block_policy_starts_from_its_explicit_parameters':True}


def handoff_restored_body103(prepared,prefix,raw_binding,*,artificial=False):
    """Structural in-memory handoff; no geometry, optimizer, or fake old SHA."""
    require_frozen_prefix_sources()
    restored,bindings,tenth,old_replay,old_coarse,old_fine=prepared
    problem,old_initial,gate,lower,upper,source_cfg,old_cfg=restored
    if (prefix.get('schema')!=body103.SCHEMA
            or prefix.get('status')!='complete-two-grid-entry-body103-audit'
            or bool(prefix.get('artificial_inputs_only'))!=bool(artificial)):
        raise ValueError('completed current temporary entry/body103 result required')
    if (prefix.get('source_files_sha256')!=body103.implementation_hashes()
            or prefix.get('configuration')!=old_cfg or prefix.get('exact_input_storage')!=bindings
            or prefix.get('input_replay')!=old_replay
            or prefix.get('initial_state')!=state_record(problem,old_initial)
            or prefix.get('old_optimizer_calls_this_run')!=3
            or prefix.get('necessary_growth_prefix_restoration_calls')!=1
            or prefix.get('necessary_strip_prefix_restoration_calls')!=1
            or prefix.get('necessary_SOC_prefix_restoration_calls')!=1
            or prefix.get('new_scientific_solver_calls')!=1
            or prefix.get('unchanged_complete_metric_and_height_reference') is not True):
        raise ValueError('temporary entry/body103 source/configuration/legacy inputs/initial identity differ')
    if not artificial and (prefix.get('github_sha')!=os.environ.get('GITHUB_SHA')
            or str(prefix.get('github_run_id'))!=os.environ.get('GITHUB_RUN_ID')
            or prefix.get('github_repository')!='Rogerhu12/math-research-public'
            or problem.nunknown!=163):
        raise ValueError('prefix must be the current public job and same163 family')
    stage=prefix[PREFIX_STAGE]
    if stage.get('error') is not None or 'error' in stage.get('status',''):
        raise ValueError('prefix implementation failure is not a qualified restoration')
    snap=stage['checkpoint'];point=snap.get('selected_two_grid_physical_point')
    if not point:raise ValueError('temporary entry/body103 accepted state missing')
    checked=exact_vector(point.get('exact_binary64_physical_coefficients'),problem.nunknown)
    state=np.asarray(point.get('physical_parameter_coefficients_binary64'),float)
    if state.shape!=checked.shape or not np.array_equal(state,checked):
        raise ValueError('temporary numeric coefficients differ from their exact rational record')
    state=state.copy()  # retain any explicit binary64 signed zeros from the actual prefix
    if (state.tolist()!=point.get('physical_parameter_coefficients_binary64')
            or coefficients(state)!=point.get('exact_binary64_physical_coefficients')
            or digest(problem.identity(state))!=point.get('physical_state_sha256')
            or prefix.get('final_state')!=state_record(problem,state)):
        raise ValueError('temporary final exact coefficients or canonical identity differ')
    accepted=snap.get('accepted_iterates',[])
    old_subspace=body103.EntryBody103Subspace(body103.layout_from_problem(problem))
    if state[old_subspace.fixed_columns].tobytes()!=np.asarray(old_initial)[old_subspace.fixed_columns].tobytes():
        raise ValueError('restored103 changed its declared fixed60 coefficients')
    if (not accepted or accepted[-1]!=point
            or problem.metric_model(state)!=problem.metric_model(old_initial)
            or old_replay.get('fixed_b0_definition_sha256')!=digest(problem.height_base_definition)):
        raise ValueError('temporary accepted state, fixed g or fixed b0 differ')
    validation=prefix.get('final_selection_validation',{})
    if not validation.get('both_value_grids_hard_and_old_metric_pass'):
        raise ValueError('temporary final two-grid actual gate failed')
    decisions=[prefix.get(k,{}) for k in ['final_full_grid_constraints','final_doubled_constraints']]
    for decision in decisions:
        if not decision.get('single_grid_admissible_recovery_point'):
            raise ValueError('temporary final decision was not independently admissible')
        for key in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
                'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']:
            if decision.get(key)!=old_cfg[key]:raise ValueError('temporary actual gate identity differs: '+key)
    if validation.get('both_grid_maximum_eta')!=max(d['direct_max_eta'] for d in decisions):
        raise ValueError('temporary final maximum does not agree with both decisions')
    radial,theta,grid=curvature_grid(tenth)
    if prefix.get('full_value_sampling_definition')!=grid:
        raise ValueError('temporary original full value sampling definition differs')
    histories=[snap.get(k,[]) for k in ['active_row_pool_history','fine_physical_row_pool_history']]
    if not all(histories):raise ValueError('temporary complete pool histories missing')
    coarse,fine=(h[-1] for h in histories);ci,fi=coarse.get('row_indices'),fine.get('row_indices')
    for row,ids,total,rule,cap,previous in [
        (coarse,ci,11*len(radial)*len(theta),'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index',
            old_cfg['max_pool_rows'],old_coarse),
        (fine,fi,22*len(radial)*len(theta),'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index',
            old_cfg['max_fine_physical_pool_rows'],old_fine)]:
        if (not isinstance(ids,list) or not ids or any(type(i) is not int for i in ids)
                or ids!=sorted(set(ids)) or row.get('row_count')!=len(ids)
                or row.get('row_indices_sha256')!=digest(ids) or row.get('group_order')!=list(GROUPS)
                or row.get('total_full_grid_rows')!=total or row.get('flat_index_rule')!=rule
                or min(ids)<0 or max(ids)>=total or len(ids)>cap or not set(previous).issubset(ids)):
            raise ValueError('temporary pool IDs/hash/group/layout/cap or inherited rows differ')
    added=fine.get('added_row_indices');fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
    if (not isinstance(added,list) or any(type(i) is not int for i in added)
            or not set(added).issubset(fi)
            or fine.get('added_original_grid_coordinates')!=rows_api.fine_coordinates(added,radial,fine_theta)):
        raise ValueError('temporary fine original coordinate binding differs')
    locations={}
    for decision in [decisions[-1]]+[v.get('decision',{}) for v in snap.get('saved_fine_trials',[])
            if v.get('status')=='complete-doubled-angle-value-call']:
        loc=decision.get('direct_max_eta_location')
        if loc is not None:
            pair=(float(loc['t']),float(loc['theta']))
            if not all(np.isfinite(pair)):raise ValueError('temporary metric peak is not finite')
            locations[pair]={'t':pair[0],'theta':pair[1]}
    continuation=restored_body103_controller(stage,old_cfg)
    observed={'run':OBSERVED_BODY103_RUN,'source':OBSERVED_BODY103_SOURCE,
        'canonical_physical_state_sha256':OBSERVED_BODY103_STATE,
        'temporary_complete_report_sha256':OBSERVED_BODY103_REPORT_SHA,
        'raw_report_not_available_or_used_as_a_new_input':True}
    restoration={'schema':'same-job-temporary-entry/body103-prefix-restoration-v1',
        'purpose':'restore necessary runtime state under metadata-only output policy, not a new scientific comparison',
        'prefix_scientific_implementation_sha256':body103.implementation_hashes(),
        'prefix_configuration':copy.deepcopy(old_cfg),'prefix_current_run':prefix.get('github_run_id'),
        'prefix_current_source':prefix.get('github_sha'),
        'prefix_temporary_raw_file':copy.deepcopy(raw_binding),
        'prefix_status':stage.get('status'),'prefix_budget_message':stage.get('budget_message'),
        'controller_continuation':continuation,
        'prefix_source_initial_physical_sha256':digest(problem.identity(old_initial)),
        'prefix_regenerated_final_physical_sha256':point['physical_state_sha256'],
        'observed_reference':observed,
        'regenerated_final_equals_observed_body103_bfbd':point['physical_state_sha256']==OBSERVED_BODY103_STATE,
        'old_raw_report_SHA_equality_not_required_or_claimed':True,
        'no_budget_extension_or_repeat_until_an_old_hash_matches':True,
        'different_wall_selected_state_may_continue_only_after_actual_two_grid_gates':True,
        'prefix_final_selection_validation':copy.deepcopy(validation),
        'prefix_final_gate_values':{name:{k:d.get(k) for k in [
            'single_grid_admissible_recovery_point','previous_metric_budget_pass','hard_strip_pass',
            'hard_ball_pass','signed_height_pass','independent_direct_curvature_pass',
            'direct_max_eta','direct_maximum_absolute_principal_curvature','maximum_absolute_y',
            'inner_strip_absolute_margin','minimum_signed_height','direct_mirror_radius_min_finite']}
            for name,d in zip(['coarse','fine'],decisions)},
        'prefix_accepted_count':len(accepted),
        'prefix_linear_program_count':stage.get('solver',{}).get('linear_program_invocation_count'),
        'prefix_shared_full_values':snap.get('total_full_value_physical_evaluations'),
        'prefix_optimization_active_seconds':prefix.get('optimization_active_seconds'),
        'prefix_run_audit_elapsed_seconds':prefix.get('run_audit_elapsed_seconds'),
        'prefix_preparation_elapsed_seconds':prefix.get('prepare_elapsed_seconds'),
        'prefix_failed_trials_remain_in_the_temporary_report_until_consumed':True,
        'prefix_report_and_summary_not_published_or_retained_after_this_job':True}
    learned={'schema':'temporary-body103-complete-learned-pool-handoff-v1',
        'source_coarse_rows':len(ci),'source_fine_rows':len(fi),
        'source_coarse_row_indices_sha256':digest(ci),'source_fine_row_indices_sha256':digest(fi),
        'source_full_value_grid_sha256':grid['definition_sha256'],'group_order':list(GROUPS),
        'new_metric_proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
        'all_previous_coarse_and_fine_integer_IDs_retained':True,
        'groups2_to10_have_original_actual_values_and_derivatives':True}
    cfg=configuration(old_cfg)
    actual_layout=layout_from_problem(problem)
    replay={'schema':'temporary-body103-to-two-block154-in-memory-handoff-v1',
        'canonical_physical_state_sha256':point['physical_state_sha256'],
        'complete_metric_sha256':problem.metric_model(state)['mathematical_definition_sha256'],
        'fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'physical_parameter_count':problem.nunknown,'learned_pool':learned,
        'known_fine_metric_locations':list(locations.values()),'temporary_input_restoration':restoration,
        'controller_continuation':continuation,
        'temporary_input_restorations':copy.deepcopy(old_replay['temporary_input_restorations'])+[restoration],
        'layout_derived_from_actual_problem':actual_layout,
        'explicit_new_constraint_definition':{
            'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
            'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'metric_restoration_target_exact':cfg['fixed_metric_budget_exact'],
            'proposal_epsilon_exact':EPSILON_EXACT,'proposal_branch_mapping':copy.deepcopy(PROPOSAL_BRANCHES),
            'strip_proposal_floor_definition':strip_floor_definition(cfg),
            'curvature_proposal_floor_definition':floor_definition(cfg),
            'primary_physical_step_cost_definition':penalty_definition(cfg),
            'new_restricted_proposal_definition':restriction_definition(cfg),
            'new_restricted_scale_definition':restricted_growth_definition(cfg),
            'SOC_reversible_scaling':scaling_definition(cfg),
            'all_actual_gates_and163_physical_family_unchanged':True,
            'actual_new_stage_progress_is_measured_from_this_regenerated_initial_state':True,
            'no_initial_match_to_observed_body103_bfbd_is_assumed':True}}
    return ((problem,state,gate,lower,upper,source_cfg,cfg),bindings,tenth,replay,
        np.asarray(ci,np.int64),np.asarray(fi,np.int64))


def small_summary(report,out):
    legacy=copy.copy(report);stage=legacy.pop(STAGE,None)
    if stage is not None:legacy[soc.STAGE]=stage
    result=soc.small_summary(legacy,out)
    if soc.STAGE in result:result[STAGE]=result.pop(soc.STAGE)
    for key in ['restricted_proposal_definition','initial_field_diagnostics','final_field_diagnostics',
            'final_fixed_support_replay','total_drop_reference','necessary_SOC_prefix_restoration_calls','necessary_body103_prefix_restoration_calls']:
        if key in report:result[key]=copy.deepcopy(report[key])
    if STAGE in result:
        for key in ['entry_tail154','initial_fixed_domain_and_height_diagnostic','last_pre_LP_decision',
                'last_restricted_trust','final_consecutive_growth_qualifying_models']:
            if key in stage:result[STAGE][key]=copy.deepcopy(stage[key])
        result[STAGE]['projection_models']=[{'number':m['number'],
            'projection':copy.deepcopy(m.get('linear_program',{}).get('projection'))}
            for m in stage.get('solver',{}).get('models',[])]
    return result


def save_report(out,report):
    atomic_save(out,report)
    path=summary_path(out);tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(small_summary(report,out),ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n')
    os.replace(tmp,path)


def field_diagnostics(data,grid,subspace,cfg):
    """Read ordinary already computed jets, not a new geometry/derivative call."""
    val=geometry_values(data);eta=np.asarray(val['eta']);e,f=val['e'],val['f']
    b=np.asarray(data['height']['b'],float)
    if eta.shape!=(grid.nr,grid.nt) or b.shape!=(grid.nr,):raise ValueError('same complete field grid required')
    masks={
        'entry':np.array([subspace.left<t<Q(117,1000) for t in grid.nodes]),
        'body':np.array([Q(117,1000)<=t<Q(153,200) for t in grid.nodes]),
        'new_variable_tail':np.array([Q(153,200)<=t<subspace.right for t in grid.nodes]),
        'variable_domain':np.array([subspace.left<t<subspace.right for t in grid.nodes]),
        'fixed_outside':np.array([not(subspace.left<t<subspace.right) for t in grid.nodes])}
    rows=spectral_proposal_rows(e,f,float(Q(cfg['fixed_metric_budget_exact'])),float(Q(EPSILON_EXACT)))
    result={'grid':grid.definition,'regions':{},'same_evaluated_complete_ordinary_jets':True,
        'no_extra_geometry_or_derivative_evaluation':True}
    for name,mask in masks.items():
        ids=np.flatnonzero(mask)
        if not len(ids):result['regions'][name]={'sample_count':0};continue
        q=np.unravel_index(int(np.argmax(eta[mask])),eta[mask].shape);ri,ti=int(ids[q[0]]),q[1]
        result['regions'][name]={'sample_count':int(len(ids)*grid.nt),
            'maximum_actual_eta':float(eta[ri,ti]),'location':grid.coordinate(ri*grid.nt+ti),
            'E_minus_one':float(e[ri,ti]),'F_over_a':float(f[ri,ti])}
    outside=masks['fixed_outside'];ids=np.flatnonzero(outside);r=rows[:,outside]
    q=np.unravel_index(int(np.argmin(r)),r.shape);ri,ti=int(ids[q[1]]),q[2]
    result.update(rho_out=max(0.,-float(r[q])),
        rho_out_attainer=grid.coordinate(q[0]*grid.point_count+ri*grid.nt+ti))
    bound=b*b-1.;bi=int(np.argmax(bound));mean=np.mean(data['Xs'],axis=1)
    mean[:,2]-=b
    result['fixed_height_diagnostic']={'maximum_b_squared_minus_one':float(bound[bi]),
        'nonnegative_eta_lower_bound_evaluated':max(0.,float(bound[bi])),
        'location':{'radial_index':bi,'t_exact':str(grid.nodes[bi]),'b':float(b[bi])},
        'mean_Xs_minus_b_ez_maximum':float(np.max(abs(mean))),
        'Jensen_necessary_bound_scope':'same exact Pi/mean definition; finite samples are not a validated integral bound',
        'not_used_as_an_extra_actual_gate':True}
    return result


def outside_replay(reference,subspace,grid,data):
    outside=np.array([not(subspace.left<t<subspace.right) for t in grid.nodes])
    ref=reference['grids'][grid.label]
    return {'outside_six_jet_difference_max':{k:float(np.max(abs(np.asarray(data[k])[outside]-ref[k]))) for k in POSITION_JETS},
        'outside_metric_jet_difference_max':{k:float(np.max(abs(np.asarray(data['metric'][k])[outside]-ref['metric'][k])))
            for k in ['a','a_s','a_ss']},
        'whole_common_center_difference_max':float(np.max(abs(np.asarray(data['center'])-ref['center']))),
        'whole_fixed_height_jet_difference_max':{k:float(np.max(abs(np.asarray(data['height'][k])-ref['height'][k])))
            for k in ['b','b_s','b_ss']},
        'same_existing_complete_evaluation_no_extra_call':True,
        'floating_replay_is_not_a_continuous_certificate':True}


def supplementary_outcome_text(report):
    lines=['ENTRY/TAIL154: TWO BLOCKS IN THE SAME g/b0/163 FAMILY',
        'B=[0,54)+[81,129)+{153}, T=[54,81)+[129,153); height9 stay bitwise fixed.',
        'Exact variable domain (9/250,423/500); endpoints and outside two-jets remain fixed.',
        'All original full384/768 actual gates remain; full selected geometry Jacobians still have163 columns.',
        'New common body r=cap=1/4000, tail r/8=1/32000, streak0; prior103 controller is reported.',
        'The total eta decrease1e-4 is a diagnostic reference, not an acceptance threshold.']
    stage=report.get(STAGE,{})
    initial=stage.get('solver',{}).get('new_restricted_controller_initialization',{})
    lines.append('New controller initialization: '+json.dumps(initial,sort_keys=True,ensure_ascii=False))
    for name,entry in [('initial',stage.get('solver',{}).get('initial_pre_LP_decision')),
            ('last',stage.get('last_pre_LP_decision'))]:
        if entry:lines.append(name+' pre-LP decision: '+json.dumps(entry,sort_keys=True))
    lines.append('DOMAIN METRIC: phase | grid | region | n | eta max | exact t | theta/pi | e | f')
    for phase,key in [('initial','initial_field_diagnostics'),('final','final_field_diagnostics')]:
        for grid_name,record in report.get(key,{}).items():
            for region,value in record['regions'].items():
                loc=value.get('location',{})
                row=[phase,grid_name,region,value.get('sample_count'),value.get('maximum_actual_eta'),
                    loc.get('t_exact'),loc.get('theta_over_pi_exact'),value.get('E_minus_one'),value.get('F_over_a')]
                lines.append(' | '.join(_scalar(v,digits=17) for v in row))
            lines.append(phase+' '+grid_name+' complete outside rho: '+_scalar(record['rho_out'],digits=17)+
                ' at '+json.dumps(record['rho_out_attainer'],sort_keys=True))
            lines.append(phase+' '+grid_name+' fixed-height diagnostic: '+json.dumps(record['fixed_height_diagnostic'],sort_keys=True))
    lines.append('RESTRICTED MODELS: number | active rows | invariant selected rows | internal zeroJ | outside Jmax | rho_out | eta_out | LP variables | LP bytes')
    for model in stage.get('solver',{}).get('models',[]):
        lp=model.get('linear_program',{});p=lp.get('projection',{})
        row=[model['number'],p.get('active_original_row_count'),p.get('invariant_original_selected_row_count'),
            p.get('in_domain_zero_J_rows_kept'),p.get('outside_selected_J_max_diagnostic_only'),
            p.get('rho_out'),p.get('eta_out'),lp.get('variables'),lp.get('matrix_bytes')]
        lines.append(' | '.join(_scalar(v,digits=17) for v in row))
        lines.append('model '+str(model['number'])+' exact projection mappings: '+str(p.get('active_original_row_mapping_sha256'))+
            ' / '+str(p.get('invariant_original_row_mapping_sha256')))
    lines.append('BLOCK PROPOSALS: model | rB | rT | body-use | tail-use | weighted-use | physical-norm | physical-cost')
    for model in stage.get('solver',{}).get('models',[]):
        d=model.get('linear_program',{}).get('primary_step_cost_diagnostic',{})
        row=[model['number']]+[d.get(k) for k in ['common_body_radius','tail_radius','body_utilization',
            'tail_utilization','actual_trust_normalized_step_norm','actual_physical_box_normalized_step_norm','physical_norm_cost_evaluated']]
        lines.append(' | '.join(_scalar(v,digits=17) for v in row))
        for ci,correction in enumerate(model.get('corrections',[])):
            c=correction.get('linear_program',{})
            lines.append('BLOCK SOC '+str(model['number'])+'/'+str(ci)+': '+json.dumps({k:c.get(k) for k in [
                'primary_box_normalized_step_infinity_norm','primary_block_normalized_step_infinity_norm',
                'body_correction_radius','tail_correction_radius','correction_block_normalized_infinity_norm',
                'correction_box_normalized_l1_norm','maximum_linear_row_violation','maximum_linear_bound_violation']},sort_keys=True))
    for key in ['final_fixed_support_replay','total_drop_reference','final_selection_validation','value_evaluation_counts']:
        if key in report:lines.append(key+': '+json.dumps(report[key],sort_keys=True,ensure_ascii=False))
    # The established supplementary formatter reads these same stored tables.
    # Only its display title is changed; it makes no geometry or solver call.
    alias=copy.copy(report);alias[soc.STAGE]=stage
    text=soc.supplementary_outcome_text(alias).replace(
        'SOC EQUIVALENT SCALING -- original gates and original-unit LP residual limit retained',
        'TWO-BLOCK154 TRIAL/FLOOR/DUAL/DEFECT DETAILS -- original gates and original-unit residuals retained')
    lines.append(text.rstrip())
    lines.append('These sampled diagnostics do not establish exact isometry, continuous gates or whole-surface reach; reproducible payloads remain temporary.')
    return '\n'.join(lines)+'\n'


def print_new_stage_outcomes(report):
    print(supplementary_outcome_text(report),end='',flush=True)


def _temporary_binding(path):
    raw=Path(path).read_bytes()
    return {'filename':Path(path).name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
        'temporary_current_job_file_only':True,'not_an_observed_old_report_SHA_replay':True}


def run_pipeline(args,*,artificial=False,evaluate_only=False,process_started=None):
    started=time.monotonic() if process_started is None else process_started
    phase='public-environment-and-original24-input-contract';restorations=[];raw_bindings=[]
    invoked={'growth':0,'strip':0,'SOC':0,'body103':0,'two-block154':0}
    try:
        require_frozen_prefix_sources()
        if not artificial:
            require_public_actions(os.environ.get('GITHUB_ACTIONS'),os.environ.get('GITHUB_REPOSITORY'),
                [getattr(args,k) for k in INPUTS])
        parent='/dev/shm' if artificial and Path('/dev/shm').is_dir() else os.environ.get('RUNNER_TEMP')
        with tempfile.TemporaryDirectory(prefix='visible-entry-tail154-inputs-',dir=parent) as folder:
            growth_out=Path(folder)/'restored-growth.json';strip_out=Path(folder)/'restored-strip.json'
            soc_out=Path(folder)/'restored-scaled-SOC.json';body_out=Path(folder)/'restored-body103.json'
            prefix_args=copy.copy(args);prefix_args.out=growth_out
            phase='strict-original24-input-preparation';before=time.monotonic()
            prepared=growth.prepare_run(prefix_args,artificial=artificial,process_started=started)
            prepare_seconds=time.monotonic()-before
            phase='one-necessary-frozen-growth-restoration';invoked['growth']=1
            previous=growth.run_audit(prepared,growth_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=prepare_seconds)
            binding=_temporary_binding(growth_out);raw_bindings.append(binding)
            phase='growth-qualified-state-and-all-pools-handoff'
            continued=strip.handoff_restored_growth(prepared,previous,binding,artificial=artificial)
            restorations.append(continued[3]['temporary_input_restoration'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'growth'),end='',flush=True)
            del previous,prepared
            phase='one-necessary-frozen-strip-restoration';invoked['strip']=1
            previous=strip.run_audit(continued,strip_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(strip_out);raw_bindings.append(binding)
            phase='strip-qualified-state-and-all-pools-controller-handoff'
            prepared_soc=soc.handoff_restored_strip(continued,previous,binding,artificial=artificial)
            restorations=list(prepared_soc[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'strip-reserve'),end='',flush=True)
            del previous,continued
            phase='one-necessary-frozen-scaled-SOC-restoration';invoked['SOC']=1
            previous=soc.run_audit(prepared_soc,soc_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(soc_out);raw_bindings.append(binding)
            phase='SOC-qualified-state-complete-pools-and-explicit-new-subspace-handoff'
            prepared_body=body103.handoff_restored_soc(prepared_soc,previous,binding,artificial=artificial)
            restorations=list(prepared_body[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'scaled-SOC'),end='',flush=True)
            print('Regenerated scaled-SOC equals observed ec76: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_SOC_ec76'])+'; never a forced replay condition.',flush=True)
            del previous,prepared_soc
            phase='one-necessary-frozen-body103-restoration';invoked['body103']=1
            previous=body103.run_audit(prepared_body,body_out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
            binding=_temporary_binding(body_out);raw_bindings.append(binding)
            phase='body103-qualified-full-state-complete-pools-handoff'
            new_prepared=handoff_restored_body103(prepared_body,previous,binding,artificial=artificial)
            restorations=list(new_prepared[3]['temporary_input_restorations'])
            print(soc.prefix_outcome_text(previous,restorations[-1],'entry-body103'),end='',flush=True)
            print('Regenerated body103 equals observed bfbd: '+_scalar(
                restorations[-1]['regenerated_final_equals_observed_body103_bfbd'])+'; never a forced replay condition.',flush=True)
            del previous,prepared_body
            phase='one-new-entry-tail154-two-block-stage';invoked['two-block154']=1
            return run_audit(new_prepared,args.out,artificial=artificial,evaluate_only=evaluate_only,
                process_started=started,prepare_seconds=time.monotonic()-started)
    except Exception as error:
        failure={'schema':SCHEMA,'status':'entry-tail154-pipeline-failed-last-written-checkpoint-preserved',
            'phase':phase,'source_files_sha256':implementation_hashes(),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
            'necessary_growth_prefix_restoration_calls':invoked['growth'],
            'necessary_strip_prefix_restoration_calls':invoked['strip'],
            'necessary_SOC_prefix_restoration_calls':invoked['SOC'],
            'necessary_body103_prefix_restoration_calls':invoked['body103'],
            'new_scientific_solver_calls':invoked['two-block154'],
            'temporary_prefix_raw_bindings':raw_bindings,'temporary_input_restorations':restorations,
            'process_total_elapsed_seconds':time.monotonic()-started,
            'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}}
        if invoked['two-block154'] and Path(args.out).exists():
            try:
                existing=json.loads(Path(args.out).read_text())
                existing['scientific_status_before_pipeline_failure']=existing.get('status')
                existing['status']='entry-tail154-pipeline-error-last-checkpoint-preserved';existing['pipeline_failure']=failure
                save_report(args.out,existing);return existing
            except (OSError,ValueError,TypeError,KeyError):pass
        save_report(args.out,failure);return failure


def run_audit(prepared,out,*,artificial=False,evaluate_only=False,process_started=None,prepare_seconds=0.):
    restored,bindings,tenth,replay,coarse_pool,fine_pool=prepared
    problem,initial,gate,lower,upper,source_cfg,cfg=restored
    started=time.monotonic();process_started=started if process_started is None else process_started
    metric=copy.deepcopy(problem.metric_model(initial));b0=copy.deepcopy(problem.height_base_definition)
    layout=layout_from_problem(problem);subspace=EntryTail154Subspace(layout)
    if layout!=replay['layout_derived_from_actual_problem']:raise ValueError('derived restricted layout changed after handoff')
    report={'schema':SCHEMA,'source_files_sha256':implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,
        'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
        'github_repository':os.environ.get('GITHUB_REPOSITORY'),'artificial_inputs_only':bool(artificial),
        'old_optimizer_calls_this_run':4,'necessary_growth_prefix_restoration_calls':1,
        'necessary_strip_prefix_restoration_calls':1,'necessary_SOC_prefix_restoration_calls':1,
        'necessary_body103_prefix_restoration_calls':1,
        'new_scientific_solver_calls':0,'old_failed_metric_auxiliary_delta':tenth['selected_raw_auxiliary_delta'],
        'initial_state':state_record(problem,initial),'unchanged_complete_metric_and_height_reference':True,
        'prepare_elapsed_seconds':prepare_seconds,'learned_pool_replay':replay['learned_pool'],
        'temporary_input_restorations':replay['temporary_input_restorations'],
        'new_constraint_role_definition':replay['explicit_new_constraint_definition'],
        'restricted_proposal_definition':restriction_definition(cfg),
        'process_clock_scope':'main includes four one-time necessary temporary prefixes and one new two-block154 budget; each clock separately reported'}
    def save(status):
        now=time.monotonic();snapshot=report.get(STAGE,{}).get('checkpoint',{})
        report.update(status=status,elapsed_seconds=now-started,run_audit_elapsed_seconds=now-started,
            process_total_elapsed_seconds=now-process_started,
            optimization_active_seconds=snapshot.get('optimization_elapsed_seconds') or 0.,
            peak_rss_kib_linux=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_report(out,report)
    save('original24-inputs-and-four-qualified-prefixes-replayed-before-new-geometry')
    try:
        radial,theta,grid=curvature_grid(tenth);order=int(source_cfg['primitive_order'])
        report['full_value_sampling_definition']=grid;report['phase']='entry-tail154-complete-initialization'
        def checkpoint(snapshot):
            report[STAGE]={'status':'current-two-block154-last-qualified-checkpoint','checkpoint':snapshot,'solver':{}}
            save('two-block154-last-accepted-physical-checkpoint')
        objective=EntryTail154Objective(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint,
            radial_nodes_exact=grid['radial_nodes_exact'])
        objective.evaluation_definition.update(complete_value_sampling_definition=grid,
            temporary_restored_body103_raw_sha256=replay['temporary_input_restoration']['prefix_temporary_raw_file']['sha256'],
            learned_pool_replay=replay['learned_pool'],temporary_input_restoration=replay['temporary_input_restoration'],
            new_constraint_role_definition=replay['explicit_new_constraint_definition'])
        objective.evaluation_sha256=digest(objective.evaluation_definition)
        objective.set_pool(coarse_pool,{'kind':'retain-all-temporary-body103-coarse-original-IDs','source':replay['learned_pool']})
        objective.set_fine_pool(fine_pool,{'kind':'retain-all-temporary-body103-eleven-group-fine-original-IDs','source':replay['learned_pool']})
        report['initial_current_constraints']=copy.deepcopy(objective.evaluate(objective.vector(initial))['decision'])
        report['initial_full_grid_audit']=audit_data(problem,initial,objective.geometry_cache,source_cfg['tau'])
        report['initial_doubled_constraints']=copy.deepcopy(objective.fine_decision(initial))
        report['initial_field_diagnostics']={g.label:field_diagnostics(d,g,subspace,cfg) for g,d in
            [(objective.row_grids[0],objective.geometry_cache),(objective.row_grids[1],objective.fine_cache['data'])]}
        save('complete-initial-original-gates-and-fixed-domain-height-diagnostics')
        report['phase']='one-shared-budget-two-block154-stage';report['new_scientific_solver_calls']=1
        stage=run_restricted_recovery(objective,initial,known_metric_locations=replay['known_fine_metric_locations'],
            restored_controller=replay['controller_continuation'],artificial_inputs_only=artificial,evaluate_only=evaluate_only)
        report[STAGE]=stage;point=stage['checkpoint'].get('selected_two_grid_physical_point')
        if point is None:
            print_new_stage_outcomes(report);save('no-original-two-grid-hard-qualified-restricted-baseline');return report
        final=np.asarray(point['physical_parameter_coefficients_binary64'],float)
        if coefficients(final)!=point['exact_binary64_physical_coefficients'] or digest(problem.identity(final))!=point['physical_state_sha256']:
            raise ValueError('selected restricted full coefficients or identity differ')
        fixed=subspace.fixed_columns
        if final[fixed].tobytes()!=np.asarray(initial)[fixed].tobytes():raise ArithmeticError('one of9 fixed height coefficients changed')
        identity=problem.identity(final);frozen,fc=problem.frozen_metric_copy(final)
        if (fc.tobytes()!=final.tobytes() or frozen.identity(fc)!=identity or frozen.metric_model(fc)!=metric
                or frozen.height_base_definition!=b0 or layout_from_problem(frozen)!=layout):
            raise ArithmeticError('final freezing changed g/b0/full coefficients/derived layout')
        problem,final=frozen,fc;report['final_state']=state_record(problem,final)
        reference=objective.restricted_reference;grids=objective.row_grids
        report['phase']='independent-final-same-state-original384-and768-values'
        work=problem.geometry(final,radial,theta,order)
        report['final_full_grid_audit']=audit_data(problem,final,work,source_cfg['tau'])
        report['final_full_grid_constraints']=recovery_decision(problem,gate,final,work,lower,upper,cfg)
        report['final_field_diagnostics']={'coarse':field_diagnostics(work,grids[0],subspace,cfg)}
        report['final_fixed_support_replay']={'fixed9_height_coefficients_bitwise_unchanged':True,
            'coarse':outside_replay(reference,subspace,grids[0],work)}
        save('last-restricted-qualified-point-recomputed-on-original-coarse-grid')
        del objective
        fine_theta=np.arange(2*len(theta))*np.pi/len(theta)
        fine=problem.geometry(final,radial,fine_theta,order)
        report['final_doubled_angle_audit']=audit_data(problem,final,fine,source_cfg['tau'],with_rows=False)
        report['final_doubled_constraints']=recovery_decision(problem,gate,final,fine,lower,upper,cfg)
        report['final_field_diagnostics']['fine']=field_diagnostics(fine,grids[1],subspace,cfg)
        report['final_fixed_support_replay']['fine']=outside_replay(reference,subspace,grids[1],fine)
        report['same_parameter_Pi_refinement']=compare_data(problem,work,problem,fine,final,
            name='same two-block154 state, fixed g/b0, original angular grids',theta_stride=2)
        if problem.identity(final)!=identity:raise ArithmeticError('final Pi evaluation changed physical identity')
        c,f=report['final_full_grid_constraints'],report['final_doubled_constraints']
        eligible=bool(c['single_grid_admissible_recovery_point'] and f['single_grid_admissible_recovery_point'])
        maximum=max(c['direct_max_eta'],f['direct_max_eta'])
        start=max(report['initial_current_constraints']['direct_max_eta'],report['initial_doubled_constraints']['direct_max_eta'])
        new_target=bool(c['single_grid_new_target_qualified'] and f['single_grid_new_target_qualified'])
        report['final_selection_validation']={'both_value_grids_hard_and_old_metric_pass':eligible,
            'both_grid_maximum_eta':maximum,'initial_both_grid_maximum_eta':start,'actual_eta_decrease':start-maximum,
            'both_grid_maximum_curvature':max(c['direct_maximum_absolute_principal_curvature'],f['direct_maximum_absolute_principal_curvature']),
            'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
            'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
            'new_metric_target_qualified_on_both_grids':new_target,
            'previous_qualified_budget_exact':cfg['previous_qualified_metric_budget_exact'],
            'qualification_not_assumed_from_restricted_LP_or_constant_support':True,'whole_surface_reach_not_certified':True}
        reference_drop=float(Q(cfg['entry_tail154_effective_total_eta_drop_reference_exact']))
        report['total_drop_reference']={'reference_exact':cfg['entry_tail154_effective_total_eta_drop_reference_exact'],
            'actual_total_two_grid_eta_drop':start-maximum,'reference_met':bool(start-maximum>=reference_drop),
            'not_an_acceptance_gate_or_continuous_bound':True,
            'if_not_met_next_direction_must_use_observed_limits_not_same_budget_extension':True}
        count=stage['checkpoint']['total_full_value_physical_evaluations']
        report['value_evaluation_counts']={'shared_initialization_and_trial_full_values':count,
            'shared_cap':cfg['max_physical_evaluations'],'independent_final_same_state_value_calls':2,
            'total_counted_full_value_calls_in_this_new_driver':count+2,
            'four_necessary_prefix_counts_are_separate':True,
            'failed_fine_and_actual_fine_SOC_residuals_count':True,
            'full163_Jacobian_batches_recorded_separately_not_reduced_by154_LP':True,'no_final_optimizer':True}
        report['limitations']={'all_geometric_gates_sampled_only':True,'new_target026_not_exact_isometry':True,
            'hard_cap58_not_final_reach_target':True,'full_nonlocal_reach_not_paid':True,
            'same_g_b0_and163_not_expanded':True,'fixed_outside_may_limit_global_maximum_drop':True,
            'four_prefixes_each_once_not_new_scientific_progress':True,'no_forced_observed_prefix_hash':True}
        print_new_stage_outcomes(report)
        save('entry-tail154-controller-error-last-qualified-preserved' if stage.get('error') else
            'complete-two-grid-entry-tail154-audit' if eligible else 'final-recheck-failed-do-not-use-as-new-warm-start')
        return report
    except Exception as error:
        report['error']={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}
        print_new_stage_outcomes(report);save('entry-tail154-audit-error-last-checkpoint-preserved');return report



def developer_check():
    """New array/control/metadata interfaces and a real tiny artificial class API.

    No published candidate is loaded, no former development suite is replayed,
    and the four scientific prefix solvers are stubbed for the IO count check.
    """
    import contextlib
    import io
    import sys
    from types import SimpleNamespace
    from unittest.mock import patch
    from frame_entry_tail_blocks import expected_layout
    from frame_metric_entry_tail154 import _TwoBlockArrayObjective,artificial_single_Q_cache_check
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    targeted=restricted_check()
    targeted['real_artificial_SingleQ_cache_API']=artificial_single_Q_cache_check()
    module=sys.modules[__name__]
    layout=expected_layout();subspace=EntryTail154Subspace(layout)
    class ToyProblem:
        nunknown=163
        slices={k:slice(*v) for k,v in layout['slices'].items()}
        height_base_definition={'schema':'pure-artificial-restricted103-IO-fixed-b0'}
        def identity(self,x):
            return {'family':'pure-artificial-restricted103-IO','exact_coefficients':coefficients(x)}
        def metric_model(self,x):
            return {'schema':'pure-artificial-restricted103-IO-g','mathematical_definition_sha256':digest({'g':'toy'})}
        def evaluation_definition(self):return {'schema':'pure-artificial-restricted103-IO-no-surface'}
        def frozen_metric_copy(self,x):return self,np.asarray(x,float).copy()
    problem=ToyProblem();old_state=np.zeros(163);old_state[60]=-0.;old_state[154]=.125
    new_state=old_state.copy();new_state[0]=1e-4
    nodes=['0','9/250','9/100','99/500','33/50','153/200','309/400','423/500','9/10']
    radial=np.array([float(Q(x)) for x in nodes]);theta=np.arange(4)*np.pi/2
    grid={'schema':'tiny-artificial-restricted103-IO-grid','radial_nodes_exact':nodes,
        'definition_sha256':digest({'r':nodes,'nt':4})}
    cfg=body103_library.configuration(soc.configuration(recovery_configuration(start_configuration(),target='13/50',curvature_cap='58'),artificial=True))
    initial_controller={'schema':'restored-growth-controller-continuation-v1',
        'trust_binary64_exact':str(Q.from_float(float(Q(1,32000)))),'trust_evaluated':float(Q(1,32000)),
        'success_streak':1,'origin':'artificial completed previous stage'}
    binding={'filename':'artificial-scaled-SOC.json','bytes':1,'sha256':'e'*64}
    bindings={'fixture':{'decoded_sha256':'f'*64,'decoded_bytes':1,'stored_sha256':'f'*64,
        'stored_bytes':1,'gzip_storage':False}}
    decision={k:cfg[k] for k in ['fixed_metric_budget_exact','previous_qualified_metric_budget_exact',
        'fixed_hard_curvature_cap_exact','hard_strip_half_width_exact','mirror_target_exact']}
    decision.update(single_grid_admissible_recovery_point=True,direct_max_eta=.2665,
        direct_max_eta_location={'t':.66,'theta':0.},direct_maximum_absolute_principal_curvature=2.,
        hard_strip_pass=True,hard_ball_pass=True,signed_height_pass=True,independent_direct_curvature_pass=True,
        previous_metric_budget_pass=True,maximum_absolute_y=.1,inner_strip_absolute_margin=.28999,
        minimum_signed_height=.05,direct_mirror_radius_min_finite=.1)
    previous_restoration={'regenerated_final_equals_observed_SOC_ec76':False,'prefix_current_run':'artificial','prefix_current_source':'artificial-source',
        'prefix_status':'artificial-completed','prefix_budget_message':None,
        'prefix_source_initial_physical_sha256':'0'*64,
        'prefix_regenerated_final_physical_sha256':digest(problem.identity(old_state)),
        'regenerated_final_equals_observed_f2bb':False,'regenerated_final_equals_observed_strip267':False,
        'prefix_accepted_count':1,'prefix_linear_program_count':1,'prefix_shared_full_values':2,
        'prefix_optimization_active_seconds':.01,'prefix_run_audit_elapsed_seconds':.02,
        'prefix_preparation_elapsed_seconds':.01,'prefix_temporary_raw_file':binding,
        'prefix_scientific_implementation_sha256':growth.implementation_hashes(),
        'prefix_configuration':cfg,'controller_continuation':dict(initial_controller,
            unfinished_last_model_not_counted_as_success=False)}
    replay={'schema':'pure-artificial-current-prepared-SOC','fixed_b0_definition_sha256':digest(problem.height_base_definition),
        'controller_continuation':initial_controller,'temporary_input_restoration':previous_restoration,
        'temporary_input_restorations':[copy.deepcopy(previous_restoration) for _ in range(3)]}
    prepared=((problem,old_state,None,np.full(163,-8.),np.full(163,8.),
        {'primitive_order':3,'tau':'61/1000'},cfg),bindings,{'fixture':'grid','selected_raw_auxiliary_delta':.2},
        replay,np.array([0,128]),np.array([0,256]))
    def pool(ids,fine=False):
        nt=2*len(theta) if fine else len(theta)
        record={'version':1,'row_indices':ids,'added_row_indices':ids,'row_count':len(ids),'row_indices_sha256':digest(ids),
            'group_order':list(GROUPS),'total_full_grid_rows':11*len(radial)*nt,
            'flat_index_rule':'group*(Nr*Nfine)+radial_index*Nfine+fine_theta_index' if fine
                else 'group*(Nr*Ntheta)+radial_index*Ntheta+theta_index'}
        if fine:record.update(added_row_indices=ids,added_original_grid_coordinates=rows_api.fine_coordinates(
            ids,radial,np.arange(nt)*2*np.pi/nt))
        return record
    point={'exact_binary64_physical_coefficients':coefficients(new_state),
        'physical_parameter_coefficients_binary64':new_state.tolist(),
        'physical_state_sha256':digest(problem.identity(new_state))}
    models=[{'number':1,'trust_before_model':float(Q(1,4000)),
        'trials':[],'scale_feedback_trials':[],'result':'artificial-primary-failed'},
        {'number':2,'trust_before_model':float(Q(1,8000)),
            'trials':[{'attempt_status':'coarse-value-call-complete'}]}]
    _,_,feedback=body103_library.next_restricted_trust(models[0],float(Q(1,8000)),0,cfg)
    models[0]['scale_feedback_update']=feedback
    prefix={'schema':body103.SCHEMA,'status':'complete-two-grid-entry-body103-audit',
        'artificial_inputs_only':True,'source_files_sha256':body103.implementation_hashes(),'configuration':cfg,
        'exact_input_storage':bindings,'input_replay':replay,'initial_state':state_record(problem,old_state),
        'old_optimizer_calls_this_run':3,'necessary_growth_prefix_restoration_calls':1,
        'necessary_strip_prefix_restoration_calls':1,'necessary_SOC_prefix_restoration_calls':1,'new_scientific_solver_calls':1,
        'unchanged_complete_metric_and_height_reference':True,'final_state':state_record(problem,new_state),
        'github_run_id':'pure-artificial','github_sha':'pure-artificial-no-research',
        'github_repository':'Rogerhu12/math-research-public','full_value_sampling_definition':grid,
        'initial_current_constraints':decision,'initial_doubled_constraints':copy.deepcopy(decision),
        'final_full_grid_constraints':copy.deepcopy(decision),'final_doubled_constraints':copy.deepcopy(decision),
        'final_selection_validation':{'both_value_grids_hard_and_old_metric_pass':True,'both_grid_maximum_eta':.2665},
        PREFIX_STAGE:{'status':'shared-value-time-or-pool-budget-exit','error':None,
            'final_consecutive_growth_qualifying_models':0,'last_restricted_trust':float(Q(1,8000)),
            'solver':{'models':models,'linear_program_invocation_count':2,'restored_controller_continuation':initial_controller},
            'checkpoint':{'selected_two_grid_physical_point':point,'accepted_iterates':[point],
                'active_row_pool_history':[pool([0,1,128])],
                'fine_physical_row_pool_history':[pool([0,1,256],True)],
                'saved_fine_trials':[],'total_full_value_physical_evaluations':4}}}
    with patch.object(module,'curvature_grid',return_value=(radial,theta,grid)), \
            patch.object(module,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)), \
            patch.object(body103,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)):
        before=copy.deepcopy(prefix);restored=handoff_restored_body103(prepared,prefix,binding,artificial=True)
        immutable=prefix==before
        rc=restored[3]['controller_continuation'];actual=np.asarray(restored[0][1])
        handoff_ok=bool(actual.tobytes()==new_state.tobytes()
            and rc['trust_evaluated']==float(Q(1,8000)) and rc['success_streak']==0
            and rc['unfinished_last_model_not_counted_as_success']
            and len(restored[3]['temporary_input_restorations'])==4
            and not restored[3]['temporary_input_restoration']['regenerated_final_equals_observed_body103_bfbd']
            and restored[0][-1]['entry_tail154_initial_trust_exact']=='1/4000')
        rejects={}
        for name in ['coefficient','gate','pool','controller','source','sampling','implementation-error']:
            bad=copy.deepcopy(prefix)
            if name=='coefficient':bad[PREFIX_STAGE]['checkpoint']['selected_two_grid_physical_point']['exact_binary64_physical_coefficients'][0]='123'
            elif name=='gate':bad['final_doubled_constraints']['single_grid_admissible_recovery_point']=False
            elif name=='pool':bad[PREFIX_STAGE]['checkpoint']['fine_physical_row_pool_history'][-1]['row_indices']=[0]
            elif name=='controller':bad[PREFIX_STAGE]['final_consecutive_growth_qualifying_models']=1
            elif name=='source':bad['source_files_sha256']['frame_metric_entry_body103.py']='0'*64
            elif name=='sampling':bad['full_value_sampling_definition']['radial_nodes_exact'][2]='1/10'
            else:bad[PREFIX_STAGE]['error']={'type':'RuntimeError','message':'injected implementation failure'}
            try:handoff_restored_body103(prepared,bad,binding,artificial=True);rejects[name]=False
            except (ValueError,KeyError):rejects[name]=True
    calls={'prepare':0,'growth':0,'strip':0,'SOC':0,'body103':0,'new':0};temporary=[]
    shallow={k:copy.deepcopy(prefix[k]) for k in ['initial_current_constraints','initial_doubled_constraints',
        'final_full_grid_constraints','final_doubled_constraints']}
    def prepare_stub(args,**kwargs):calls['prepare']+=1;return ('opaque-original24-preparation',)
    def prefix_stub(label,data):
        def run(p,out,**kwargs):
            calls[label]+=1;temporary.append(Path(out));atomic_save(out,data);return copy.deepcopy(data)
        return run
    def new_stub(p,out,**kwargs):
        calls['new']+=1
        if len(p[3]['temporary_input_restorations'])!=4:raise AssertionError('four distinct prefix records required')
        result={'schema':SCHEMA,'status':'pure-artificial-restricted-new-stage-stub',
            'temporary_input_restorations':p[3]['temporary_input_restorations'],STAGE:{'solver':{},'checkpoint':{}}}
        atomic_save(out,result);return result
    def patch_pipeline(stack,runner):
        stack.enter_context(patch.object(module,'curvature_grid',return_value=(radial,theta,grid)))
        stack.enter_context(patch.object(module,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)))
        stack.enter_context(patch.object(body103,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)))
        stack.enter_context(patch.object(growth,'prepare_run',side_effect=prepare_stub))
        stack.enter_context(patch.object(growth,'run_audit',side_effect=prefix_stub('growth',shallow)))
        stack.enter_context(patch.object(strip,'handoff_restored_growth',return_value=prepared))
        stack.enter_context(patch.object(strip,'run_audit',side_effect=prefix_stub('strip',shallow)))
        stack.enter_context(patch.object(soc,'handoff_restored_strip',return_value=prepared))
        stack.enter_context(patch.object(soc,'run_audit',side_effect=prefix_stub('SOC',shallow)))
        stack.enter_context(patch.object(body103,'handoff_restored_soc',return_value=prepared))
        stack.enter_context(patch.object(body103,'run_audit',side_effect=prefix_stub('body103',prefix)))
        stack.enter_context(patch.object(module,'run_audit',side_effect=runner))
    with tempfile.TemporaryDirectory(prefix='entry-tail154-new-IO-',dir='/dev/shm') as folder:
        args=SimpleNamespace(out=Path(folder)/'new-audit.json');printed=io.StringIO()
        with contextlib.ExitStack() as stack:
            patch_pipeline(stack,new_stub);stack.enter_context(contextlib.redirect_stdout(printed))
            result=run_pipeline(args,artificial=True,evaluate_only=True)
        once=calls=={'prepare':1,'growth':1,'strip':1,'SOC':1,'body103':1,'new':1}
        unique=bool([p.name for p in Path(folder).glob('*-audit.json')]==['new-audit.json']
            and all(not p.exists() for p in temporary)
            and [k for k,v in result.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        prefix_print=all(s in printed.getvalue() for s in ['RESTORATION growth','RESTORATION strip-reserve',
            'RESTORATION scaled-SOC','RESTORATION entry-body103','initial_doubled_constraints','final_doubled_constraints',
            'Regenerated scaled-SOC equals observed ec76:','Regenerated body103 equals observed bfbd:'])
        args_bad=SimpleNamespace(out=Path(folder)/'failure.json')
        with patch.object(growth,'prepare_run',side_effect=ValueError('new artificial inputloader failure')):
            bad=run_pipeline(args_bad,artificial=True,evaluate_only=True)
        failure_ok=bool(bad['phase']=='strict-original24-input-preparation'
            and bad['necessary_growth_prefix_restoration_calls']==0 and bad['new_scientific_solver_calls']==0
            and json.loads(args_bad.out.read_text())['error']['type']=='ValueError')
    # Exercise the actual new audit/main calling signatures with labelled arrays.
    # Real SingleQ/cache APIs were separately exercised above on a small synthetic ellipse.
    class DriverArrayObjective(_TwoBlockArrayObjective):
        def __init__(self,problem,gate,radial,theta,order,lower,upper,*,cfg,checkpoint,radial_nodes_exact):
            super().__init__(cfg);self.problem=problem;self.gate=gate
            if list(radial_nodes_exact)!=nodes or not np.array_equal(radial,self.radial):raise ValueError('toy grid differs')
            self.lower=np.asarray(lower).copy();self.upper=np.asarray(upper).copy();self.checkpoint=checkpoint
            self.pool_history=[];self.fine_history=[]
        def set_pool(self,ids,reason):
            self.pool=np.asarray(ids,np.int64).copy();self.pool_history.append(pool(self.pool.tolist()))
        def set_fine_pool(self,ids,reason):
            self.fine_pool=np.asarray(ids,np.int64).copy();self.fine_history.append(pool(self.fine_pool.tolist(),True))
        def snapshot(self):
            r=super().snapshot();r['active_row_pool_history']=copy.deepcopy(self.pool_history)
            r['fine_physical_row_pool_history']=copy.deepcopy(self.fine_history);return r
    class ArrayProblem(ToyProblem):
        def geometry(self,state,r,t,order,**kwargs):
            obj=_TwoBlockArrayObjective(restored[0][-1]);g=RationalRowGrid('coarse' if len(t)==4 else 'fine',nodes,len(t))
            data,rr,decision=obj._data(state,g)
            data['IO_mock_decision']=decision;return data
    ap=ArrayProblem();ax=restored[0][1].copy();gate=SimpleNamespace(kind='artificial-array',row=np.zeros(163),intercept=0.,target=0.)
    areplay=copy.deepcopy(restored[3]);areplay['known_fine_metric_locations']=[]
    aprepared=((ap,ax,gate,np.full(163,-8.),np.full(163,8.),{'primitive_order':3,'tau':'61/1000'},restored[0][-1]),
        bindings,prepared[2],areplay,restored[4],restored[5])
    def compare_arrays(p,a,q,b,state,**kwargs):
        return {'same_artificial_state':p.identity(state)==q.identity(state),
            'evaluation_before':p.evaluation_definition(),'evaluation_after':q.evaluation_definition(),
            'same_parameter_two_grid_difference':{k:float(np.max(abs(a[k]-b[k][:,::2]))) for k in POSITION_JETS}}
    with tempfile.TemporaryDirectory(prefix='entry-tail154-new-main-',dir='/dev/shm') as folder:
        out=Path(folder)/'new-audit.json';printed=io.StringIO()
        with patch.object(module,'curvature_grid',return_value=(radial,theta,grid)), \
                patch.object(module,'layout_from_problem',side_effect=lambda p:copy.deepcopy(layout)), \
                patch.object(module,'EntryTail154Objective',DriverArrayObjective), \
                patch.object(module,'audit_data',side_effect=lambda *a,**k:{'artificial_labelled_arrays_no_surface':True}), \
                patch.object(module,'compare_data',side_effect=compare_arrays), \
                patch.object(module,'recovery_decision',side_effect=lambda p,g,s,d,*a,**k:d['IO_mock_decision']), \
                patch.object(module,'geometry_values',side_effect=lambda d:{'eta':d['eta'],'e':d['e'],'f':d['f']}), \
                contextlib.redirect_stdout(printed):
            full=run_audit(aprepared,out,artificial=True,evaluate_only=True)
        native=json.loads(summary_path(out).read_text());raw=out.read_bytes()
        full_ok=bool(full['status']=='complete-two-grid-entry-tail154-audit'
            and full[STAGE]['solver']['linear_program_invocation_count']==0
            and full['initial_state']==full['final_state']
            and full['final_selection_validation']['both_value_grids_hard_and_old_metric_pass']
            and full['final_fixed_support_replay']['fixed9_height_coefficients_bitwise_unchanged']
            and full[STAGE]['solver']['new_restricted_controller_initialization']['new_restricted_initial_trust_exact']=='1/4000'
            and native['full_report']['sha256']==hashlib.sha256(raw).hexdigest()
            and [k for k,v in native.items() if k.endswith('_stage') and isinstance(v,dict)]==[STAGE])
        scientific_print=all(s in printed.getvalue() for s in ['RESTRICTED MODELS','fixed-height diagnostic',
            'final_selection_validation','total_drop_reference','value_evaluation_counts'])
        def save_then_fail(p,out,**kwargs):save_report(out,full);raise RuntimeError('injected new post-checkpoint exception')
        args=SimpleNamespace(out=Path(folder)/'preserved-audit.json')
        with contextlib.ExitStack() as stack:
            patch_pipeline(stack,save_then_fail);stack.enter_context(contextlib.redirect_stdout(io.StringIO()))
            kept=run_pipeline(args,artificial=True,evaluate_only=True)
        keep_ok=bool(kept.get('status')=='entry-tail154-pipeline-error-last-checkpoint-preserved'
            and kept.get('final_state')==full.get('final_state') and kept.get(STAGE)==full.get(STAGE)
            and kept.get('pipeline_failure',{}).get('error',{}).get('type')=='RuntimeError')
    # No extra LP: reuse the newly generated artificial correction report to check
    # that projected groups keep original row IDs in the small stdout supplement.
    lp=copy.deepcopy(targeted['SOC_linear_program'])
    groups=lp.get('curvature_proposal_diagnostics',{}).get('group_statistics',[])
    mapping=lp.get('curvature_proposal_diagnostics',{}).get('group8_selected_rows',{})
    columns=mapping.get('columns',[]);actual_rows=mapping.get('rows',[])
    required=['active_projection_stack_index','original_full_selected_stack_index','original_grid','original_flat_row_id']
    expected_active=[];offset=0
    for label,nt in [('coarse',4),('fine',8)]:
        for rid in range(11*len(nodes)*nt):
            ri=(rid%(len(nodes)*nt))//nt
            if subspace.left<Q(nodes[ri])<subspace.right:expected_active.append((offset+rid,label,rid))
        offset+=11*len(nodes)*nt
    mapping_ok=bool(actual_rows and all(k in columns for k in required))
    if mapping_ok:
        at=[columns.index(k) for k in required]
        mapping_ok=all(tuple(row[i] for i in at[1:])==expected_active[int(row[at[0]])]
            for row in actual_rows)
    actual_gate={k:True for k in GATE_ORDER};actual_gate['independent_direct_curvature_pass']=False
    stress={STAGE:{'solver':{'models':[{'number':i+1,'linear_program':lp,
        'trials':[{'coarse_decision':{'actual_gate_booleans':actual_gate},
                   'fine_decision':{'actual_gate_booleans':actual_gate}}],
        'corrections':[{'linear_program':lp}]} for i in range(6)]}}}
    stress_text=supplementary_outcome_text(stress)
    checks={'new_library_projection_and_controller_development':targeted['passed'],
        'new_real_SingleQ_cache_API_and_tail_support':targeted['real_artificial_SingleQ_cache_API']['passed'],
        'actual_prefix_state_signed_zero_and_original_controller_record_bound':handoff_ok,
        'prefix_dictionary_not_mutated':immutable,'all_new_bad_handoffs_rejected':all(rejects.values()),
        'exactly_one_each_four_prefixes_and_one_new_stage':once,
        'one_top_level_audit_and_stage_temporary_prefix_cleanup':unique,
        'all_four_prefix_initial_final_gates_and_observed_hash_relation_printed':prefix_print,
        'input_failure_preserves_small_JSON':failure_ok,
        'complete_new_run_audit_IO_final_freeze_native_summary':full_ok,
        'post_checkpoint_failure_preserves_state_and_stage':keep_ok,
        'fixed_domain_height_and_reference_science_printed':scientific_print,
        'projected_SOC_group8_rows_bind_active_original_stack_grid_and_ID':mapping_ok,
        'SOC_group_and_original_unit_dual_summaries_are_printed':bool(groups and 'ORIGINAL UNIT DUAL' in stress_text),
        'new_extra_stdout_stays_under_64KiB':len(stress_text.encode())<65536}
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema':SCHEMA+'-new-artificial-interface-check','artificial_inputs_only':True,
        'research_candidate_constructed_evaluated_or_optimized':False,
        'old_development_suites_and_scientific_prefixes_not_repeated':True,
        'new_library_checks':targeted,'checks':checks,'new_handoff_rejections':rejects,
        'new_pipeline_call_counts_across_success_and_injected_failure_paths':calls,'new_pipeline_status':result.get('status'),
        'new_pipeline_phase':result.get('phase'),'new_pipeline_error':result.get('error'),
        'new_post_checkpoint_status':kept.get('status'),'new_post_checkpoint_error':kept.get('error'),
        'new_artificial_audit_status':full.get('status'),'new_artificial_audit_error':full.get('error'),
        'new_artificial_stage_error':full.get(STAGE,{}).get('error'),
        'extra_stdout_stress_bytes':len(stress_text.encode()),'passed':all(checks.values())}


def main():
    started=time.monotonic();parser=argparse.ArgumentParser(description=__doc__)
    for name in INPUTS:parser.add_argument('--'+name.replace('_','-'),type=Path)
    for name in SHA_NAMES:parser.add_argument('--expected-'+name+'-sha256')
    parser.add_argument('--check-only',action='store_true')
    parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    if args.check_only:
        try:result=developer_check()
        except Exception as error:
            atomic_save(args.out,{'schema':SCHEMA+'-development-error','passed':False,
                'artificial_inputs_only':True,'source_files_sha256':implementation_hashes(),
                'process_total_elapsed_seconds':time.monotonic()-started,
                'error':{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()}})
            raise
        result.update(source_files_sha256=implementation_hashes(),process_total_elapsed_seconds=time.monotonic()-started)
        atomic_save(args.out,result);print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    report=run_pipeline(args,process_started=started)
    print(json.dumps({'out':str(args.out),'status':report.get('status')}),flush=True)
    if report.get('status')!='complete-two-grid-entry-tail154-audit':raise SystemExit(1)


if __name__=='__main__':main()
