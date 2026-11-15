#!/usr/bin/env python3
"""Request178: complete ten-coordinate scaled minimum-norm Newton proposals.

The selected support1/power4 shape is fixed by the producer.  This module
uses every current row and column of the actual Decimal50 three-by-ten
response.  It reuses the frozen full Householder QR arithmetic, never
forms a normal matrix, and never truncates a singular direction.  An
explicit scaled Cauchy proposal is a fallback, not a rank certificate.
Only original real-domain/full3 Armijo evaluations adopt new parameters.
"""
from __future__ import annotations
import hashlib
import importlib
import os
from pathlib import Path
import traceback

HERE=Path(__file__).resolve().parent
ENTRY='geometry_20261115_fixed_power_ten_scaled_newton.py'
SCHEMA='fixed-power-ten-complete-scaled-minimum-norm-Newton-v1'
MODEL='geometry_20261115_adjoint_selected_ten_decimal_model.py'
MODEL_SHA='8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7'
QR='geometry_20261115_nine_control_decimal_curved_search.py'
QR_SHA='433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0'
POLICY=dict(complete_parameter_dimension=10,complete_residual_dimension=3,
    selected_support_index=1,selected_power=4,selected_catalogue_index=3,
    original_nine_relative_scale='0.01',new_xi_absolute_scale='0.01',
    fixed_scales_use_actual157_nine_input_words=True,
    scales_recomputed_after_acceptance=False,scaled_trust_radius='1',
    original_parent_radius_is_provenance_only=True,
    full_ten_direction_budget=8,original_real_backtrack_budget=20,
    proposal='column-pivoted QR of complete transpose(J*S), minimum-norm solve then radial clip',
    fallback='complete scaled Cauchy direction after recorded Newton arithmetic failure or nonnegative formed slope',
    scalar_residual_rows_reweighted=False,normal_matrix_formed=False,
    singular_value_cutoff_or_rank_acceptance_gate=False,
    normal_curved_path_used=False,post_rejection_same_point_retry=False,
    original_full3_strict_slope_and_exact_binary64_lift_Armijo=True)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('All scientific execution is restricted to public repository Actions')


def load_bound(name,wanted):
    require_actions()
    if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=wanted:
        raise ValueError('A complete source-bound numerical helper differs: '+name)
    return importlib.import_module(name[:-3])


k=load_bound(MODEL,MODEL_SHA)
qrlib=load_bound(QR,QR_SHA)
ZERO,ONE,TWO=k.ZERO,k.ONE,k.TWO


def own_identity():
    raw=Path(__file__).read_bytes()
    return dict(name=ENTRY,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def mv(matrix,vector):
    return [k.dot(row,vector) for row in matrix]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def finite(values):
    return all(x.is_finite() for x in values)


def fixed_physical_scales(actual_parent_words):
    require_actions()
    if len(actual_parent_words)!=9:
        raise ValueError('Nine original physical coefficients are required')
    relative=k.dec(POLICY['original_nine_relative_scale'])
    xi=k.dec(POLICY['new_xi_absolute_scale'])
    result=[relative*max(ONE,abs(k.dec(word))) for word in actual_parent_words]+[xi]
    if not finite(result) or any(x<=ZERO for x in result):
        raise k.NumericalFailure('The explicit physical-coordinate scales are not positive finite')
    return result


def realized_proposal(J,F,scales,z,label,record):
    """Form the actual full3 linear action used by the unchanged slope gate."""
    physical=[s*x for s,x in zip(scales,z)]
    action=mv(J,physical)
    slope=k.dot(F,action)
    predicted=[f+a for f,a in zip(F,action)]
    record.update(kind=label,complete_scaled_coordinates=z,
        complete_physical_direction=physical,
        original_complete_three_directional_response=action,
        original_full3_slope=slope,
        scaled_step_L2=k.norm(z),
        exact_model_radial_clip_bound_not_an_interval_certificate=True,
        original_model_full_step_residual=predicted,
        original_model_full_step_merit=k.dot(predicted,predicted)/TWO,
        finite_complete_direction_and_action=finite(z+physical+action+[slope]))
    return physical,action,slope


def direction(F,J,scales,record):
    """Exact full-row-rank theorem is conditional; actual Decimal fields are recorded."""
    require_actions()
    if (len(F)!=3 or len(J)!=3 or any(len(row)!=10 for row in J)
            or len(scales)!=10 or not finite(F+scales)
            or not all(finite(row) for row in J)):
        raise k.NumericalFailure('The full current three-by-ten model is malformed or nonfinite')
    A=[[row[j]*scales[j] for j in range(10)] for row in J]
    record.update(schema=SCHEMA,source=own_identity(),
        current_complete_three_residual=F,current_complete_three_by_ten_J=J,
        fixed_physical_scales=scales,complete_scaled_matrix=A,
        scaled_trust_radius=ONE,all_three_rows_and_ten_columns_retained=True,
        original_residual_merit_not_reweighted=True,
        normal_matrix_formed=False,singular_value_truncation=False,
        rank_or_accuracy_acceptance_gate=False,newton={},fallback=None)
    nr=record['newton']
    try:
        Q,R,pivot=qrlib.qr_factor(transpose(A))
        nr.update(complete_Q=Q,complete_R=R,equation_column_permutation=pivot,
            factorization_convention='transpose(A)[:,pivot] = Q[:,0:3] * R[0:3,:]',
            Q_orientation='original Householder updates Q <- Q*H; returned Q, not transpose(Q)',
            complete_upper_diagonal=[R[i][i] for i in range(3)])
        if sorted(pivot)!=list(range(3)):
            raise ValueError('The complete three-equation permutation is malformed')
        if any(R[i][i]==ZERO for i in range(3)):
            raise k.NumericalFailure('An actually formed required R diagonal is exactly zero; no row or singular direction discarded')
        rhs=[-F[pivot[j]] for j in range(3)]
        y=[ZERO]*3
        for j in range(3):
            y[j]=(rhs[j]-sum((R[i][j]*y[i] for i in range(j)),ZERO))/R[j][j]
        z=[sum((Q[i][j]*y[j] for j in range(3)),ZERO) for i in range(10)]
        if not finite(y+z):
            raise k.NumericalFailure('The full minimum-norm triangular solve is nonfinite')
        size=k.norm(z)
        theta=ONE if size<=ONE else ONE/size
        clipped=[theta*x for x in z]
        nr.update(permuted_original_rhs=rhs,triangular_solution=y,
            original_transpose_triangular_residual=[
                sum((R[i][j]*y[i] for i in range(j+1)),ZERO)-rhs[j] for j in range(3)],
            original_unclipped_scaled_direction=z,original_unclipped_scaled_norm=size,
            original_complete_linear_residual=[a+f for a,f in zip(mv(A,z),F)],
            radial_clip_factor=theta,
            clipped_complete_linear_residual=[a+theta*f for a,f in zip(mv(A,clipped),F)],
            conditional_exact_minimum_norm_only_if_full_row_rank_and_exact_arithmetic=True,
            actual_rounded_QR_or_slope_not_an_accuracy_certificate=True)
        d,action,slope=realized_proposal(J,F,scales,clipped,'radially-clipped-complete-minimum-norm-Newton',nr)
        if finite(d+action+[slope]) and slope<ZERO:
            nr['selected']=True
            record.update(selected_kind=nr['kind'],selected_proposal=nr)
            return d,action
        nr.update(selected=False,rejection_reason='The actual formed complete direction is nonfinite or lacks the original strict negative slope')
    except (k.NumericalFailure,qrlib.NumericalFailure,ArithmeticError) as error:
        nr.update(selected=False,exception=repr(error),traceback=traceback.format_exc(),
            rejection_reason='Recorded finite-arithmetic Newton proposal failure; try complete scaled Cauchy')
    fb={};record['fallback']=fb
    try:
        gradient=mv(transpose(A),F)
        size=k.norm(gradient)
        fb.update(complete_scaled_merit_gradient=gradient,scaled_gradient_L2=size)
        if not finite(gradient+[size]) or size<=ZERO:
            fb.update(selected=False,stop_reason='No finite nonzero formed complete scaled gradient; no exact stationarity conclusion')
            record['selected_kind']=None
            return None,None
        action_gradient=mv(A,gradient)
        numerator=k.dot(gradient,gradient)
        denominator=k.dot(action_gradient,action_gradient)
        boundary=ONE/size
        length=min(boundary,numerator/denominator) if denominator>ZERO else boundary
        z=[-length*x for x in gradient]
        fb.update(complete_scaled_gradient_action=action_gradient,
            exact_line_model_numerator=numerator,exact_line_model_denominator=denominator,
            boundary_length=boundary,selected_line_length=length,
            zero_denominator_fallback_is_a_finite_proposal_not_an_exact_rank_claim=denominator==ZERO)
        d,action,slope=realized_proposal(J,F,scales,z,'complete-scaled-Cauchy-fallback',fb)
        if finite(d+action+[slope]) and slope<ZERO:
            fb['selected']=True
            record.update(selected_kind=fb['kind'],selected_proposal=fb)
            return d,action
        fb.update(selected=False,stop_reason='Cauchy proposal does not have a finite original strict negative full3 slope')
    except (k.NumericalFailure,qrlib.NumericalFailure,ArithmeticError) as error:
        fb.update(selected=False,exception=repr(error),traceback=traceback.format_exc(),
            stop_reason='Complete scaled Cauchy arithmetic failed')
    record['selected_kind']=None
    return None,None


def search(model,state,initial_J,scales,status,checkpoint,event_sink,check_budget):
    require_actions()
    status.update(outer_steps=[],unvisited_outer_indices=list(range(8)),
        fixed_physical_scales=scales,scaled_trust_radius=ONE,
        accepted_point_count=0,complete_outer_direction_budget=8,
        complete_real_trial_budget_per_direction=20,
        stop_reason=None,normal_curved_path_used=False)
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
                with model.context('joint-ten-direction-'+str(outer)+'-real-trial-'+str(trial)):
                    candidate=model.evaluate(point)
                actual=k.merit(candidate)
                row.update(actual_merit=actual,actual_parameters=candidate['parameters'],
                    actual_unit_equations=candidate['equation'],actual_full112_right=candidate['full_right'],
                    actual_scalar_node_and_mid_minimum_radius=min(x[0] for x in candidate['scalar_nodes']+candidate['scalar_middle']),
                    actual_circle_node_and_mid_minimum_beta2=min(candidate['margin']+candidate['margin_mid']),
                    all_original_finite_primal_domain_guards_passed=True)
                if actual.is_finite() and actual<=bound:
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
                row['reason']='Original complete3 merit Armijo rejected'
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
