#!/usr/bin/env python3
"""Request185 candidate: full-ten predictor and complete-three normal correction.

This independent helper keeps the frozen178/183 complete10 proposal engine,
fixed physical scales, all three original residual units, and original outer
Armijo bound. At each original alpha only temporary working points move.
Fresh complete3x10 responses correct the entire affine-target deviation.
No normal tolerance, singular-value cutoff, rank certificate or additional
outer acceptance gate is introduced. All execution is public Actions only.
"""
from __future__ import annotations
import hashlib
import importlib
import os
from pathlib import Path
import traceback

HERE=Path(__file__).resolve().parent
ENTRY='geometry_20261115_fixed_power_ten_predictor_normal.py'
SCHEMA='fixed-power-ten-complete-three-predictor-normal-v1'
ENGINE='geometry_20261115_fixed_power_ten_scaled_newton.py'
ENGINE_SHA='6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861'
MODEL_SHA='8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7'
FAMILY_SHA='09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016'
QR_SHA='433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0'
POLICY=dict(
    complete_parameter_dimension=10,complete_residual_dimension=3,
    selected_support_index=1,selected_power=4,selected_catalogue_index=3,
    frozen_original_proposal_source_sha256=ENGINE_SHA,
    fixed_scales_from_actual157_words_not_current_or_future_parent_recomputed=True,
    scaled_outer_proposal_radius='1',normal_proposal_scaled_radius='1',
    full_ten_direction_budget=8,original_real_backtrack_budget=20,
    maximum_normal_updates_per_original_alpha=3,
    normal_real_backtrack_budget_per_update=20,
    normal_target='original base F plus original alpha times original Jd',
    normal_equations='all three components; fresh complete three by ten J',
    normal_proposal='frozen R378 full minimum-norm QR with its explicit full Cauchy fallback',
    total_displacement_projection='radial projection in the same fixed S ball',
    original_base_merit_slope_alpha_Armijo_bound_frozen_during_each_alpha=True,
    outer_acceptance='every actual finite domain-valid point uses only original full3 Armijo',
    temporary_update='strict decrease of full three affine-target deviation only after outer rejection',
    no_normal_tolerance_or_rank_threshold_added=True,
    unaccepted_working_points_never_adopted_by_owner=True,
    full3_primal_domain_guards_unchanged=True,
    original_final_FD_scalar_circle_full112_consumers_remain_caller_responsibility=True,
    numerical_proposals_are_not_interval_or_discrete_rounding_derivative_certificates=True,
    future_initial_parent_must_be_actual183_complete_final_words_not_prefilled=True)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('All scientific execution is restricted to public repository Actions')


def load_bound(name,wanted):
    require_actions()
    path=HERE/name
    if hashlib.sha256(path.read_bytes()).hexdigest()!=wanted:
        raise ValueError('The complete frozen numerical helper differs: '+name)
    return importlib.import_module(name[:-3])


engine=load_bound(ENGINE,ENGINE_SHA)
k=engine.k
qrlib=engine.qrlib
ZERO,ONE,TWO=k.ZERO,k.ONE,k.TWO
direction=engine.direction
fixed_physical_scales=engine.fixed_physical_scales
finite=engine.finite


def own_identity():
    raw=Path(__file__).read_bytes()
    return dict(name=ENTRY,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def validate_runtime(model,scales):
    require_actions()
    if not isinstance(model,k.LiteralTenModel):
        raise ValueError('Use the actual frozen complete ten-coordinate model instance')
    binding=model.binding
    family=binding.get('independent_ten_control_family') or {}
    if (binding.get('source',{}).get('sha256')!=MODEL_SHA
            or binding.get('parameter_dimension')!=10
            or binding.get('field_and_tail_modes')!=112
            or binding.get('original_mesh_nodes')!=699
            or family.get('schema')!='R259-nine-plus-selected-power-C2-ten-control-circle-family-v1'
            or family.get('source',{}).get('sha256')!=FAMILY_SHA
            or family.get('parameter_count')!=10
            or family.get('catalogue_index')!=3):
        raise ValueError('The same frozen support1/power4 full699/112 ten family is required')
    if (engine.MODEL_SHA!=MODEL_SHA or engine.QR_SHA!=QR_SHA
            or len(scales)!=10 or not finite(list(scales))
            or any(x<=ZERO for x in scales)):
        raise ValueError('Retain the full source closure and positive finite fixed S')
    return dict(helper=own_identity(),engine_sha256=ENGINE_SHA,
        model_sha256=MODEL_SHA,family_sha256=FAMILY_SHA,QR_sha256=QR_SHA,
        model_canonical_binding_sha256=binding.get('canonical_binding_sha256'),
        fixed_physical_scales=list(scales),fixed_shape_catalogue_index=3,
        initial_parent_source_and_final_words_must_be_bound_by_the_calling_owner=True,
        no_parent_parameters_or_accepted_state_fabricated_here=True)


def actual_state_fields(state,merit):
    """Only original returned fields and the original search's diagnostic minima."""
    return dict(actual_merit=merit,actual_parameters=list(state['parameters']),
        actual_unit_equations=list(state['equation']),
        actual_full112_right=list(state['full_right']),
        actual_scalar_node_and_mid_minimum_radius=min(
            x[0] for x in state['scalar_nodes']+state['scalar_middle']),
        actual_circle_node_and_mid_minimum_beta2=min(state['margin']+state['margin_mid']),
        all_original_finite_primal_domain_guards_passed=True,
        finite_primal_guards_not_a_continuous_target_domain_certificate=True)


def target_deviation(state,target):
    residual=list(state['equation'])
    if len(residual)!=3 or len(target)!=3 or not finite(residual+target):
        raise k.NumericalFailure('A complete finite three-component target deviation is required')
    error=[value-goal for value,goal in zip(residual,target)]
    square=k.dot(error,error)/TWO
    if not finite(error+[square]):
        raise k.NumericalFailure('The whole three-component target deviation is nonfinite')
    return error,square


def projected_normal_point(base_parameters,working_parameters,correction,scales,beta,record):
    """Record the true Decimal pre/post points; projection is proposal formation."""
    before=[x+beta*v for x,v in zip(working_parameters,correction)]
    if not finite(before):
        raise k.NumericalFailure('An unprojected full-ten normal proposal is nonfinite')
    scaled=[(x-origin)/scale for x,origin,scale in zip(before,base_parameters,scales)]
    size=k.norm(scaled)
    if not finite(scaled+[size]):
        raise k.NumericalFailure('A full-ten displacement norm is nonfinite')
    factor=ONE if size<=ONE else ONE/size
    after=(list(before) if factor==ONE else
        [origin+scale*(factor*z) for origin,scale,z in zip(base_parameters,scales,scaled)])
    if not finite(after):
        raise k.NumericalFailure('A projected full-ten normal proposal is nonfinite')
    realized=[(x-origin)/scale for x,origin,scale in zip(after,base_parameters,scales)]
    realized_size=k.norm(realized)
    record.update(beta=beta,projection_active=factor!=ONE,
        unprojected_parameter_words=before,
        unprojected_parameter_identity=k.digest(before),
        unprojected_complete_scaled_displacement=scaled,
        unprojected_scaled_L2=size,radial_projection_factor=factor,
        projected_parameter_words=after,projected_parameter_identity=k.digest(after),
        actual_projected_scaled_displacement=realized,
        actual_projected_scaled_L2=realized_size,
        exact_radial_ball_claim_does_not_certify_Decimal_rounding=True,
        no_unprojected_point_evaluation_or_merit_substituted=True)
    return after


def candidate_for_alpha(model,base,scales,alpha,initial_point,bound,
                        outer_row,label,checkpoint,check_budget):
    """At most three complete normal updates, each with twenty true trials.

    The original base p/F/W/Jd/slope and this alpha's Armijo bound never
    change. Every domain-valid evaluated point is first eligible for the
    original full3 Armijo acceptance. A smaller target deviation only
    advances a temporary working point when that original test rejects.
    """
    require_actions()
    p=tuple(base['parameters']);F=tuple(base['residual'])
    # Auxiliary target formation cannot veto an original accepted predictor.
    target=None;target_failure=None
    try:
        target=[f+alpha*action for f,action in zip(F,base['action'])]
        if len(target)!=3 or not finite(target):
            raise k.NumericalFailure('The auxiliary complete-three target is nonfinite')
    except (k.NumericalFailure,ArithmeticError) as error:
        target=None
        target_failure=dict(exception=repr(error),traceback=traceback.format_exc())
    info=dict(schema=SCHEMA,source=own_identity(),policy=dict(POLICY),
        original_base_parameter_words=list(p),
        original_base_three_residual=list(F),original_base_merit=base['merit'],
        original_base_full3_slope=base['slope'],
        original_alpha=alpha,original_Armijo_bound=bound,
        original_complete_three_linear_action=list(base['action']),
        affine_three_target=target,auxiliary_target_formation_failure=target_failure,
        target_failure_cannot_cancel_original_Armijo_acceptance=True,
        predictor={},normal_updates=[],
        unvisited_normal_update_indices=list(range(3)),
        new_primal_attempts=0,new_primal_returns=0,
        new_complete_ten_response_attempts=0,new_complete_ten_response_returns=0,
        owner_updated_here=False,selected_actual_point_kind=None,
        stop_reason=None,original_outer_gate_checked_before_normal_working_decrease=True,
        model_internal_counts_and_runtime_include_all_additional_scientific_calls=True)
    outer_row['complete_three_predictor_normal']=info
    checkpoint()

    def evaluate(point,item,context):
        check_budget()
        item.update(actual_parameter_proposal=list(point),
            actual_parameter_proposal_identity=k.digest(point),
            original_Armijo_bound=bound,accepted=False,
            original_primal_returned=False,full3_merit_returned=False)
        info['new_primal_attempts']+=1
        checkpoint()
        try:
            with model.context(context):
                state=model.evaluate(list(point))
            info['new_primal_returns']+=1
            item['original_primal_returned']=True
            item['all_original_finite_primal_domain_guards_passed']=True
            actual=k.merit(state)
            item.update(actual_state_fields(state,actual),full3_merit_returned=True)
        except k.NumericalFailure as error:
            item.update(reason='Original finite primal/domain or original merit evaluation rejected',
                exception=repr(error),traceback=traceback.format_exc())
            if not item['original_primal_returned']:
                item['all_original_finite_primal_domain_guards_passed']=False
            checkpoint()
            return None,None,None,False
        except ArithmeticError as error:
            item.update(reason='Recorded finite arithmetic failure while forming this real candidate',
                exception=repr(error),traceback=traceback.format_exc())
            checkpoint()
            return None,None,None,False
        accepted=actual.is_finite() and actual<=bound
        item.update(accepted=accepted,reason=('Original complete3 merit Armijo accepted'
            if accepted else 'Original complete3 merit Armijo rejected'))
        error=None;error_merit=None
        if target is None:
            item.update(normal_target_deviation_unavailable=True,
                normal_target_deviation_exception='Auxiliary target formation did not return finite three components',
                normal_target_deviation_failure_does_not_cancel_original_Armijo_acceptance=True)
        else:
            try:
                error,error_merit=target_deviation(state,target)
                item.update(complete_three_target_deviation=error,
                    complete_three_target_deviation_merit=error_merit)
            except (k.NumericalFailure,ArithmeticError) as diagnostic_error:
                item.update(normal_target_deviation_unavailable=True,
                    normal_target_deviation_exception=repr(diagnostic_error),
                    normal_target_deviation_failure_does_not_cancel_original_Armijo_acceptance=True)
        checkpoint()
        return state,error,error_merit,accepted

    def select(state,item,kind):
        # This only returns a candidate to the owner. It does not mutate the
        # owner's state, p, F, W, J, direction, scales, or accepted counters.
        outer_row.update(actual_state_fields(state,item['actual_merit']),
            accepted=True,reason='Original complete3 merit Armijo accepted',
            accepted_point_kind=kind,
            affine_target_deviation_not_an_outer_acceptance_gate=True)
        info.update(selected_actual_point_kind=kind,
            selected_actual_parameter_words=list(state['parameters']),
            stop_reason='Original full3 Armijo returned an actual domain-valid point')
        checkpoint()
        return state

    predictor=info['predictor']
    state,error,error_merit,accepted=evaluate(initial_point,predictor,label+'-predictor')
    if accepted:return select(state,predictor,'original-full-ten-predictor')
    if state is None:
        info['stop_reason']='The predictor did not return a usable actual primal; no fresh correction J was formed'
        outer_row['reason']='Original predictor primal/domain/arithmetic failure; this alpha is unaccepted'
        checkpoint()
        return None
    if error is None:
        info['stop_reason']='No finite whole-three target deviation for correction; original rejected predictor retained only as history'
        outer_row['reason']='Original Armijo rejected and full3 normal proposal unavailable'
        checkpoint()
        return None
    working=state;current_error=error;current_error_merit=error_merit
    for update in range(3):
        if current_error_merit==ZERO:
            info['stop_reason']='Actually formed target deviation is zero but original outer Armijo rejected; no exact-root claim'
            break
        check_budget()
        work_p=list(working['parameters'])
        row=dict(index=update,working_parameter_words=work_p,
            actual_working_three_residual=list(working['equation']),
            affine_three_target=target,current_complete_three_target_deviation=current_error,
            current_target_deviation_merit=current_error_merit,
            direction_model={},trials=[],unvisited_normal_trial_indices=list(range(20)),
            working_point_updated=False,
            original_base_merit_slope_alpha_and_Armijo_bound_unchanged=True)
        info['normal_updates'].append(row)
        info['unvisited_normal_update_indices']=list(range(update+1,3))
        info['new_complete_ten_response_attempts']+=1
        checkpoint()
        try:
            with model.context(label+'-normal-'+str(update)+'-fresh-complete-ten-forward'):
                J,response,forward_state=model.response(work_p,label='all-ten-normal-current-axes')
            info['new_complete_ten_response_returns']+=1
            row.update(current_complete_three_by_ten_J=J,
                current_complete_response_report=response,
                forward_primal_three_residual=list(forward_state['equation']),
                forward_equation_words_equal_working_primal=forward_state['equation']==working['equation'],
                actual_working_primal_not_overwritten_by_forward_primal=True)
            checkpoint()
            correction,normal_action=direction(
                list(current_error),J,list(scales),row['direction_model'])
            row.update(frozen_helper_input_is_full_affine_target_deviation_not_original_F=True,
                original_full_three_normal_direction=correction,
                original_complete_three_normal_linear_action=normal_action)
        except (k.NumericalFailure,qrlib.NumericalFailure,ArithmeticError) as error:
            row.update(stop_reason='A fresh full3x10 normal response/proposal failed',
                exception=repr(error),traceback=traceback.format_exc())
            info['stop_reason']=row['stop_reason'];checkpoint()
            break
        if correction is None:
            row['stop_reason']='No finite complete3 normal descent proposal from the original QR/Cauchy helper'
            info['stop_reason']=row['stop_reason'];checkpoint()
            break
        advanced=False
        for trial in range(20):
            check_budget()
            beta=ONE/(TWO**trial)
            attempt=dict(trial=trial,beta=beta,accepted=False,
                temporary_working_decrease=False)
            row['trials'].append(attempt)
            row['unvisited_normal_trial_indices']=list(range(trial+1,20))
            checkpoint()
            try:
                point=projected_normal_point(p,work_p,correction,scales,beta,attempt)
            except (k.NumericalFailure,ArithmeticError) as formation_error:
                attempt.update(reason='Finite full-ten normal proposal formation failed',
                    exception=repr(formation_error),traceback=traceback.format_exc(),
                    actual_primal_call_started=False)
                checkpoint()
                continue
            candidate,next_error,next_merit,accepted=evaluate(
                point,attempt,label+'-normal-'+str(update)+'-real-trial-'+str(trial))
            if accepted:
                row.update(stop_reason='Original full3 Armijo accepted this actual corrected point',
                    selected_normal_trial=trial)
                return select(candidate,attempt,'full-three-normal-update-'+str(update)+'-trial-'+str(trial))
            if candidate is not None and next_error is not None and next_merit<current_error_merit:
                # A model-work acceptance only. The source-owned state is
                # unchanged until select returns a genuine outer acceptance.
                attempt.update(temporary_working_decrease=True,
                    reason='Original full3 Armijo rejected; full3 target-deviation decrease advances only this alpha working point')
                working=candidate;current_error=next_error;current_error_merit=next_merit
                row.update(working_point_updated=True,selected_working_trial=trial,
                    next_working_parameter_words=list(working['parameters']),
                    next_complete_three_target_deviation=current_error,
                    next_target_deviation_merit=current_error_merit,
                    stop_reason='Only temporary normal working point advanced')
                advanced=True;checkpoint()
                break
            if candidate is not None:
                attempt['reason']='Original full3 Armijo rejected and no strict full3 target-deviation working decrease'
            checkpoint()
        if not advanced:
            row['stop_reason']='All available normal proposal trials failed to accept or advance this temporary working point'
            info['stop_reason']=row['stop_reason'];checkpoint()
            break
    else:
        info['stop_reason']='Explicit three full3 normal updates exhausted; no owner acceptance inferred'
    info.update(last_temporary_parameter_words=list(working['parameters']),
        last_temporary_three_residual=list(working['equation']),
        last_temporary_target_deviation=current_error,
        last_temporary_target_deviation_merit=current_error_merit,
        last_temporary_point_discarded_for_next_original_alpha=True)
    outer_row.update(accepted=False,
        reason='This original alpha produced no actual point passing its unchanged full3 Armijo bound')
    checkpoint()
    return None


def search(model,state,initial_J,scales,status,checkpoint,event_sink,check_budget):
    require_actions()
    runtime_binding=validate_runtime(model,scales)
    status.update(predictor_normal_source_binding=runtime_binding,
        predictor_normal_policy=dict(POLICY),
        additional_primal_and_forward_calls_are_explicit_new_science=True)
    status.update(outer_steps=[],unvisited_outer_indices=list(range(8)),
        fixed_physical_scales=scales,scaled_trust_radius=ONE,
        accepted_point_count=0,complete_outer_direction_budget=8,
        complete_real_trial_budget_per_direction=20,
        stop_reason=None,normal_curved_path_used=True)
    J=initial_J
    for outer in range(8):
        check_budget()
        p=list(state['parameters']);F=list(state['equation']);before=k.merit(state)
        if k.maxabs(F)<=k.TOL:
            status['stop_reason']='Original unit stopping tolerance reached; full final consumers still required'
            break
        record=dict(direction=outer,parameters_before=p,original_full3_residual=F,
            original_full3_merit_before=before,direction_model={},trials=[],
            unvisited_real_trial_indices=list(range(20)),accepted=False,
            source_owned_state_not_replaced_by_projected_or_forward_primal=True)
        status['outer_steps'].append(record);status['unvisited_outer_indices']=list(range(outer+1,8))
        checkpoint()
        if outer:
            with model.context('joint-ten-direction-'+str(outer)+'-fresh-complete-ten-forward'):
                J,response,forward_state=model.response(p,label='all-ten-current-axes')
            record.update(current_response_report=response,
                current_forward_equation_words_equal_owned_primal=forward_state['equation']==F,
                complete_current_forward_parameters=list(p))
        else:
            record['initial_complete_ten_J_from_initial_description']=True
        record['current_complete_three_by_ten_J']=J
        d,action=direction(F,J,scales,record['direction_model'])
        checkpoint()
        if d is None:
            record['stop_reason']='No finite full-ten direction with original strict negative full3 slope'
            status['stop_reason']=record['stop_reason']
            break
        slope=k.dot(F,action)
        record.update(actual_ten_direction=d,original_complete_three_directional_response=action,
            original_full3_slope=slope)
        if not finite(d+action+[slope]) or slope>=ZERO:
            record['stop_reason']='The actual full-ten direction lacks the original finite strict negative slope'
            status['stop_reason']=record['stop_reason']
            break
        for trial in range(20):
            check_budget()
            alpha=ONE/(TWO**trial)
            point=[x+alpha*v for x,v in zip(p,d)]
            bound=before+k.ARM*alpha*slope
            row=dict(trial=trial,alpha=alpha,seed_parameters=point,
                original_Armijo_bound=bound,original_full3_slope=slope,accepted=False)
            record['trials'].append(row);record['unvisited_real_trial_indices']=list(range(trial+1,20))
            checkpoint()
            try:
                base=dict(parameters=p,residual=F,merit=before,J=J,
                    direction=d,action=action,slope=slope)
                candidate=candidate_for_alpha(model,base,scales,alpha,point,bound,row,
                    'joint-ten-direction-'+str(outer)+'-real-trial-'+str(trial),
                    checkpoint,check_budget)
                if candidate is not None:
                    actual=row['actual_merit']
                    row.update(accepted=True,reason='Original complete3 merit Armijo accepted')
                    state=candidate
                    status['accepted_point_count']+=1
                    record.update(accepted=True,accepted_alpha=alpha,
                        original_actual_merit_after=actual,
                        accepted_ten_parameter_words=list(state['parameters']),
                        stop_reason='Actual full-ten direction accepted by original Armijo')
                    status['current_accepted_ten_parameter_words']=list(state['parameters'])
                    checkpoint()
                    break
                # candidate_for_alpha retained the exact reason and full temporary scope.
            except k.NumericalFailure as error:
                row.update(reason='Original real primal/domain evaluation rejected',
                    exception=repr(error),all_original_finite_primal_domain_guards_passed=False)
            checkpoint()
        else:
            record['stop_reason']='All original20 real trials rejected; current accepted ten-state retained'
            status['stop_reason']=record['stop_reason']
            checkpoint()
            break
    else:
        status['stop_reason']='Explicit eight full-ten direction budget completed'
    status['current_accepted_ten_parameter_words']=list(state['parameters'])
    status['attempted_outer_directions']=len(status['outer_steps'])
    status['original_trial_records']=sum(len(row['trials']) for row in status['outer_steps'])
    status['complete_planned_outer_rows']=[
        dict(index=i,started=i<len(status['outer_steps']),
            stop_reason=status['outer_steps'][i].get('stop_reason') if i<len(status['outer_steps']) else status['stop_reason'])
        for i in range(8)]
    checkpoint()
    return state
